import os
from openai import OpenAI

client = OpenAI()

def generate_readme(prompt: str, version: int) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    folder = f"outputs/V{version:03}"
    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/README.md", "w") as f:
        f.write(content)

    return folder

