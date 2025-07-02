import os
import uuid
import json
import zipfile
import hashlib
from datetime import datetime, timezone
from supabase import create_client, Client
from dotenv import load_dotenv
import openai
import random
import shutil
import time
import subprocess

load_dotenv()

# ----- Fail-safe: Environment Validation -----
required_env_vars = {
    "SUPABASE_URL": os.getenv("SUPABASE_URL"),
    "SUPABASE_SERVICE_KEY": os.getenv("SUPABASE_SERVICE_KEY"),
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
}

missing_vars = [k for k, v in required_env_vars.items() if not v]
if missing_vars:
    print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
    exit(1)

# ----- Auth Setup -----
url = required_env_vars["SUPABASE_URL"]
key = required_env_vars["SUPABASE_SERVICE_KEY"]
supabase: Client = create_client(url, key)

openai.api_key = required_env_vars["OPENAI_API_KEY"]

PACKS_DIR = "workflow_core/packs"
LOGS_DIR = "logs"
MODE = os.getenv("GENERATOR_MODE", "enterprise")
STAGING_BUCKET = os.getenv("STAGING_BUCKET", "workflowpacks")
PROD_BUCKET = os.getenv("PROD_BUCKET", "workflowpacks")
PRUNE_LIMIT = 10
SCORE_THRESHOLD = 60

VERSION_LEDGER = "versions.json"
FEEDBACK_FILE = "feedback.json"

# ----- Utility Functions -----

def hash_file(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def auto_unzip_packs():
    for fname in os.listdir(PACKS_DIR):
        if fname.endswith(".zip"):
            zip_path = os.path.join(PACKS_DIR, fname)
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    contents = zip_ref.namelist()
                    if any(item.startswith("V") and item.endswith("/") for item in contents):
                        print(f"📦 Extracting {fname}...")
                        zip_ref.extractall(PACKS_DIR)
            except zipfile.BadZipFile:
                print(f"⚠️ Invalid zip file: {fname}")

def get_existing_versions():
    try:
        res = supabase.storage.from_(STAGING_BUCKET).list()
        version_nums = []
        for item in res:
            name = item['name']
            if name.startswith("V") and "_n8n_Ultimate_Pack.zip" in name:
                try:
                    v = int(name.split("_")[0][1:])
                    version_nums.append(v)
                except:
                    continue
        return sorted(set(version_nums))
    except Exception as e:
        print(f"⚠️ Failed to fetch versions from Supabase: {e}")
        return []

def get_previous_workflow():
    versions = get_existing_versions()
    if not versions:
        return None
    latest = f"V{versions[-1]}_n8n_Ultimate_Pack"
    path = os.path.join(PACKS_DIR, latest, "workflow.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None

def load_feedback():
    path = os.path.join(PACKS_DIR, FEEDBACK_FILE)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def gpt_generate(prompt):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ GPT error: {e}")
        return "[GPT error]"

# ----- Core Generation -----

def generate_workflow(version):
    prev = get_previous_workflow()
    feedback = load_feedback()
    base_nodes = [
        {"name": "Start", "type": "start", "parameters": {}},
        {"name": "Webhook", "type": "webhook", "parameters": {"path": f"v{version}-trigger"}},
        {"name": "HTTP Request", "type": "httpRequest", "parameters": {"url": "https://api.example.com/data"}},
        {"name": "Set", "type": "set", "parameters": {"fields": [{"name": "status", "value": "processed"}]}},
        {"name": "Supabase Insert", "type": "supabase", "parameters": {"table": "events"}}
    ]

    if prev:
        prev_nodes = prev.get("nodes", [])
        good_nodes = [n for n in prev_nodes if n["type"] in ["httpRequest", "supabase"]]
        for node in good_nodes:
            node_copy = dict(node)
            node_copy["name"] += f"_v{version}"
            base_nodes.append(node_copy)

    random.shuffle(base_nodes)
    return {
        "name": f"Ultimate_Workflow_V{version}",
        "nodes": base_nodes,
        "connections": {
            base_nodes[i]["name"]: [base_nodes[i+1]["name"]] for i in range(len(base_nodes)-1)
        }
    }

def score_workflow(workflow):
    types = [n["type"] for n in workflow["nodes"]]
    score = len(types) * 10
    if "httpRequest" in types: score += 20
    if "supabase" in types: score += 15
    if "webhook" in types: score += 10
    return min(score, 100)

# ----- Filesystem and Validation -----

def simulate_workflow_logic(workflow):
    required_keys = ["name", "nodes", "connections"]
    for key in required_keys:
        if key not in workflow:
            raise ValueError(f"Missing key: {key}")
    if not workflow["nodes"]:
        raise ValueError("No nodes present")
    return True

def write_and_zip(folder, files):
    os.makedirs(folder, exist_ok=True)
    for name, content in files.items():
        with open(os.path.join(folder, name), "w") as f:
            f.write(content if isinstance(content, str) else json.dumps(content, indent=2))

    zip_path = f"{folder}.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                fp = os.path.join(root, file)
                zipf.write(fp, os.path.relpath(fp, folder))
                try:
                    safe_name = file.encode('ascii', 'ignore').decode()
                    print(f"🔐 {safe_name}: {hash_file(fp)}")
                except Exception as e:
                    print(f"⚠️ Skipping file with invalid name: {repr(file)}")
    return zip_path

# ----- Upload & Housekeeping -----

def upload(zip_path, bucket):
    file_name = os.path.basename(zip_path)
    existing = supabase.storage.from_(bucket).list()
    if any(obj['name'] == file_name for obj in existing):
        print(f"⚠️ {file_name} already exists in {bucket}, skipping upload.")
        return False
    with open(zip_path, "rb") as f:
        data = f.read()
    res = supabase.storage.from_(bucket).upload(file_name, data, {"content-type": "application/zip"})
    print(f"⬆️ Uploaded {file_name} to {bucket}: {res}")
    return True

def prune():
    packs = get_existing_versions()
    if len(packs) <= PRUNE_LIMIT:
        return
    to_delete = packs[:-PRUNE_LIMIT]
    for v in to_delete:
        folder = f"V{v}_n8n_Ultimate_Pack"
        try:
            shutil.rmtree(os.path.join(PACKS_DIR, folder))
            print(f"🗑️ Pruned local folder {folder}")
        except:
            print(f"⚠️ Failed to prune local folder: {folder}")

def update_ledger(version, score, hashval):
    entry = {
        "version": version,
        "score": score,
        "hash": hashval,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    if os.path.exists(VERSION_LEDGER):
        with open(VERSION_LEDGER, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(VERSION_LEDGER, "w") as f:
        json.dump(data, f, indent=2)

# ----- Orchestration -----

def run():
    auto_unzip_packs()
    
    # TEMPORARY override to force V22
    version = 22
    
    folder = os.path.join(PACKS_DIR, f"V{version}_n8n_Ultimate_Pack")
    log_folder = os.path.join(LOGS_DIR, f"V{version}")
    os.makedirs(log_folder, exist_ok=True)

    wf1 = generate_workflow(version)
    wf2 = generate_workflow(version)
    simulate_workflow_logic(wf1)
    simulate_workflow_logic(wf2)

    winner = wf1 if score_workflow(wf1) >= score_workflow(wf2) else wf2
    score = score_workflow(winner)
    critique = gpt_generate(f"Critique this n8n workflow: {json.dumps(winner)}")
    feedback_injection = json.dumps(load_feedback(), indent=2)
    self_prompt = gpt_generate(f"Given this critique, what should V{version+1}'s prompt be? {critique}")

    files = {
        "workflow.json": winner,
        "score.txt": f"{score}/100",
        "README.md": gpt_generate(f"Describe V{version} of an enterprise n8n automation workflow pack."),
        "logic_map.md": gpt_generate("Generate a logic map for a complex enterprise n8n automation pack."),
        "deployment.md": gpt_generate("Instructions for deploying an n8n automation pack on Render + Supabase."),
        "node_suggestions.md": gpt_generate(f"Suggest 3 advanced nodes for V{version} with logic + API."),
        "validation.md": critique,
        "feedback_injection.md": feedback_injection,
        "self_prompt.md": self_prompt
    }
    if version > 1:
        files["auto_eval.md"] = gpt_generate(f"Compare V{version-1} to V{version}. Key improvements?")

    zip_path = write_and_zip(folder, files)
    if not upload(zip_path, STAGING_BUCKET):
        print(f"❌ Skipping update. Version V{version} already exists.")
        return

    update_ledger(version, score, hash_file(zip_path))

    if STAGING_BUCKET != PROD_BUCKET:
        upload(zip_path, PROD_BUCKET)

    prune()
    print(f"✅ V{version} complete. Logs, packs, and ledger updated.")

if __name__ == "__main__":
    run()
