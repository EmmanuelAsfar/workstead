# PRD addendum: preserved technical context

Status: proposed technical context, not an accepted architecture.

The discussed candidate is Paperclip for missions/cockpit and OpenClaw for execution/channels/tools, joined by a bounded integration service.
Sim is an alternative if integration overhead overwhelms the cockpit benefit; Mastra is an alternative if a custom product is justified.
These names are deliberately kept out of functional requirements to preserve a replaceable implementation.

Potential persistence: PostgreSQL for the cockpit and integration records; runtime-native session storage; local artifacts before external storage; versioned role/process configuration.
Use documented APIs across component boundaries. Candidate mechanisms include durable inbox/outbox processing, idempotency keys, reservation ledgers and reconciliation of provider jobs.
These mechanisms require runtime qualification and are not proven by this PRD.

Future organization federation: separate instances own their budgets, identities and persistence, exchange delegation/acceptance/question/result/cancellation contracts, and authenticate each other.
MCP addresses tool access; it does not by itself define mission ownership, cost accounting or cross-organization trust.

Deployment direction: cloud-only development through Codex and GitHub; a separately hosted persistent pilot later. No workstation setup is required for the development process.
