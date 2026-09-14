# Workstead working agreements

## Context

Read `docs/CODEX-HANDOFF.md`, `docs/START-HERE.md`, `docs/STATUS.md`, and the relevant requirements and decisions first.
This is a personal exploratory project, not an Amundi deployment.
All repository content, code, identifiers, issues and commit messages must be English.
Conversation with Emmanuel may remain French.
Use installed BMAD skills as documented; file existence does not prove workflow completion.

## Delivery discipline

- Identify applicable REQ identifiers and acceptance criteria before implementation.
- Prefer maintained existing components. Justify significant dependencies in an architecture decision.
- Paperclip/OpenClaw remains a candidate until qualification produces evidence.
- Distinguish sourced facts, proposals, accepted decisions and executed results.
- Use focused branches, inspect diffs, run relevant checks and update documentation.
- Do not alter official BMAD skills to bypass instructions, permissions or workflow gates.
- Never commit credentials, .env files, private transcripts or third-party personal information.
- Do not attribute commits to Emmanuel without explicit author configuration. Bootstrap commits use Codex.
- Project initialization does not authorize public deployment or paid provider operations.
- Do not replace an existing remote repository; inspect ownership and content first.

## Validation

`python3 scripts/check_project.py` validates the documentation baseline only.
Add integration and recovery tests alongside the corresponding product components.
A PASS needs commands, date, results and scope in the qualification report.

## Handoff

Update `docs/STATUS.md` after each delivery batch: completed work, remaining work, blockers and next action.
The repository is the project record. A conversation alone is not an approved decision.

## Current collaboration boundary

The owner requires interactive, step-by-step BMAD product work. Earlier broad autonomy or headless-work recommendations in historical drafts are superseded. Invoke the installed bmad-help workflow to establish the next step; do not treat existing drafts or archived reviews as approved specifications. Do not begin implementation before the agreed product and architecture gates. Historical material under _bmad-output/handoff-drafts is reference input only.
