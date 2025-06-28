
# n8n Codex Assistant

This repo contains both broken and working n8n automation workflows for training an agent to:
- Debug workflows (expression errors, branching logic, API issues)
- Suggest improvements (looping, webhook structure, etc.)
- Generate new flows from scratch

## Contents

- `broken_personal_chef.json`: User-facing WhatsApp recipe bot, fails to parse suggestions and loop correctly.
- `fixed_template_personal_chef.json`: Refactored version that parses recipes and handles looping.
- `working_instagram_automation.json`: Sample flow for lead scraping and profile filtering.

Workflows are in raw n8n JSON format. Each file can be tested inside n8n.cloud or self-hosted environments.
