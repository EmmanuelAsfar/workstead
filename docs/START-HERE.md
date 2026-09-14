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

Read AGENTS.md, docs/CODEX-HANDOFF.md and docs/STATUS.md. Follow the installed bmad-help workflow. Existing planning documents and archived revisions are unapproved inputs. Explain the current stage and recommend the next BMAD step, then guide Emmanuel interactively. Do not advance specifications or implementation autonomously. Use French for conversation and English for repository artifacts. Preserve accepted work in _bmad-output and report its GitHub commit or PR link.

## BMAD

The installed official skills and runtime are committed. Do not reinstall them at each cloud task.
For a fresh empty directory only:

```sh
npx --yes bmad-method@6.12.0 install --directory . --modules bmm --tools codex --user-name Emmanuel --communication-language French --document-output-language English --yes
```

References: https://learn.chatgpt.com/docs/cloud and https://learn.chatgpt.com/docs/environments/cloud-environment
