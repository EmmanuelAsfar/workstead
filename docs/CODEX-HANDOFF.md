# Workstead — Codex cloud handoff

Date: 2026-09-14. Purpose: carry the product conversation and working evidence into a new repository-backed Codex session without restarting discovery or implying approval.

## Read this first

The owner has connected GitHub and reports creating a Codex cloud environment. He works from a tablet or phone and wants no dependency on his PC. This handoff does not verify the environment settings. Read AGENTS.md, this file, docs/STATUS.md and the installed bmad-help skill before choosing the next workflow.

Conversation: French. Repository artifacts, code, identifiers, issues and commits: English. Product name: Workstead. Repository: EmmanuelAsfar/workstead.

## Latest working agreement — overrides earlier autonomy

The owner initially delegated broad autonomous work, then explicitly stopped it because product documents were advancing without visible, collaborative BMAD steps. He wants the actual installed BMAD workflows, with discussion and validation at each agreed product stage. The latest request authorizes committing a handoff and preserving pending work; it does not approve the PRD, architecture or implementation.

Do not begin another autonomous PRD rewrite, silently accept provisional scope, launch implementation or mark BMAD stages complete. Start by explaining the actual stage and the recommended next BMAD step, then ask the next relevant product question. Reuse established context rather than asking him to describe the whole project again. Do not interpret historical memlog autonomy entries as current authorization. Follow applicable workflow instructions; do not modify the method to bypass gates.

## Confirmed product intent

Workstead is a personal exploratory platform for configuring and supervising hybrid human/AI organizations. Earlier Amundi portfolio-management examples motivated the idea but are not the pilot or its deployment scope.

The owner wants to define roles (for example producer, developer, artistic agent or commercial director), instantiate variable numbers of agents, assign objectives, missions, responsibilities and budgets, and supervise delivery. Initial experiments produce purely digital outputs: videos, small applications, film scripts and related artifacts.

The demonstration must be highly visual: see organizational activity, active/idle agents, their actions, outputs and documents; drill into an agent's work and model usage; review and accept deliverables with human participation; understand tokens and costs, including media generation. Persistent identity, state, goals and useful memory are needed across intermittent execution and restarts.

Humans and agents should collaborate using familiar shared tools: email and conversational channels such as Slack, Teams or alternatives. Work tracking, dashboards, file storage and providers should be replaceable through configuration and explicit integration boundaries. Examples include Jira or other task systems, a shared drive/Google Drive/SharePoint or other storage, multiple model gateways, external MCP servers and image/video/audio providers. Email is an expressed need; deferring it was an agent proposal, not an agreed exclusion.

The platform must be open source and architecturally open. Favor existing maintained components, minimal custom code, few services and low connector maintenance. Deployment should be packaged for a small server or cloud hosting; Railway was an example, not a selected target. It should evolve toward more robust operation. Independently deployed organizations/departments, with their own agents and persistence, should eventually communicate across servers; the release boundary for federation is not approved.

## Proposals and unresolved decisions

Paperclip plus OpenClaw with a bounded integration service is a candidate, not a selected or verified stack. Sim and Mastra were alternatives considered. Documentation research is not evidence of production reliability or broad enterprise adoption. Recheck versions, licenses and actual supported integrations during qualification.

A small digital studio with four agents plus the owner, initial two-run concurrency, controlled spawning, cockpit-linked approvals, a tablet web UI, representative providers and delayed live email were proposed assumptions. None is a user-approved release baseline. Do not turn these into constraints without discussion.

Still resolve: initial user journey and acceptance outcome; pilot roles and autonomy; channel/email priorities; ticketing/storage/provider choices; model and media budgets; deployment target; identity and approval authority; quantitative usability, frugality and quality expectations; memory scope; federation timing. Choose which to discuss through BMAD rather than presenting a large questionnaire.

## Repository map and actual evidence

- _bmad/ and .agents/skills/: official BMAD 6.12.0 core/bmm installation, 29 Codex skills. Do not reinstall or upgrade routinely.
- _bmad-output/planning-artifacts/: original draft brief, PRD and candidate architecture. File existence does not prove workflow completion.
- _bmad-output/handoff-drafts/2026-09-14/: preserved uncommitted PRD revision, recovered memlog, reconciliation, reviews, methodology research and related draft changes. Read its README before use. Archived relative links may not resolve.
- docs/DELIVERY-WORKFLOW.md: intended sequence; not a completion report.
- docs/specs/contracts.md and docs/validation/qualification.md: draft contracts and qualification plan.
- docs/architecture/decisions/: bootstrap decision and proposed runtime decision.
- GitHub Issues #1 product review, #2 runtime qualification, #3 cloud connection were created. Their current status should be checked before updating them; the user now reports cloud setup.

No product runtime has been installed or tested. No product implementation, paid provider operation or deployment has occurred. Qualification scenarios remain NOT RUN. The baseline checker only validates documentation structure/references. Bootstrap GitHub Actions run 34867180158 passed for commit 76b19c5; this is not product acceptance or evidence for later changes.

An independent rubric review of local PRD revision 0.2 reported 0 critical, 0 high, 3 medium and 1 low finding, with a verdict suitable for UX exploration/qualification, not implementation. Resolutions were authored but not independently revalidated. BMAD finalization and joint approval remain incomplete.

## Resume through BMAD

1. Read .agents/skills/bmad-help/SKILL.md and follow it, including resolving project configuration and reading its installed catalog.
2. Inspect the brief and PRD as existing unapproved inputs. State the unfinished stage and recommend the appropriate collaborative workflow; do not assume the old partial PRD Update is the user's preferred re-entry point.
3. Discuss the next product decision with Emmanuel. Execute only the agreed workflow step, preserving the confirmed intent above.
4. Keep active outputs in _bmad-output, record assumptions and actual approvals, then commit/push or open a focused PR for review. Report a GitHub link and distinguish local changes from published changes.

Use the actual installed skill names and instructions, not guessed commands from a newer BMAD release. If a workflow requires delegation but the environment lacks it, state the limitation rather than claiming the review happened.

## Development boundaries

The repository is the durable project record; the new session does not need access to the old chat. GitHub Issues tracks development work and Markdown holds specifications. Deterministic GitHub Actions is the current verification baseline; Jira for developing Workstead is not needed now and remains separate from product connector requirements.

Existing setup command: bash scripts/cloud-setup.sh. Existing check: python3 scripts/check_project.py. Setup checks the documentation baseline and provisions uv if absent; it does not install the product. The no-uv installation path was not previously tested. A ChatGPT subscription does not establish an API budget for the deployed product.

The owner previously authorized publication while the repository was public; do not block routine project work by re-requesting that permission. Repository-owned open-source license selection remains unresolved; bundled BMAD has its own MIT notice. Never commit credentials or personal transcripts. Product initialization and this handoff do not authorize paid calls or production deployment.
