# Cloud-first getting started

No workstation installation is required. Use GitHub and Codex cloud from a browser.
Repository: https://github.com/EmmanuelAsfar/workstead

## Connect Codex cloud

1. Sign in at https://chatgpt.com/codex with the ChatGPT account used for this project.
2. Authorize access to EmmanuelAsfar/workstead in the GitHub connection.
3. Create or select a Codex cloud environment for this repository.
4. Use `bash scripts/cloud-setup.sh` as the setup command.
5. Start a task on main with the resume prompt below.

These account/environment settings require the user's authenticated UI unless a dedicated management tool is available.
The cloud setup script checks the baseline and provisions uv only if missing. It does not install product runtimes or call paid APIs.

## Resume prompt

Read AGENTS.md and docs/STATUS.md. Use the installed BMAD 6.12.0 skills to review the draft product brief and PRD.
Preserve established decisions, distinguish proposals from validated outcomes, and keep repository artifacts in English.
Use French for conversation. Do not install or deploy the product before the relevant qualification plan is established.

## BMAD

The installed official skills and runtime are committed. Do not reinstall them at each cloud task.
For a fresh empty directory only:

```sh
npx --yes bmad-method@6.12.0 install --directory . --modules bmm --tools codex --user-name Emmanuel --communication-language French --document-output-language English --yes
```

References: https://learn.chatgpt.com/docs/cloud and https://learn.chatgpt.com/docs/environments/cloud-environment
