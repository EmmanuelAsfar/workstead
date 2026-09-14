# Candidate architecture

Status: PROPOSED. No end-to-end integration has been executed.

- Paperclip owns missions, assignments, decisions and the organization cockpit.
- OpenClaw owns execution, sessions, channels and tool use.
- A bounded integration service owns external references, durable events, mappings and reconciliation.
- PostgreSQL stores cockpit state and a separate integration namespace.
- Runtime-native persistence preserves sessions; local volumes hold files before external storage integration.

Create or resolve a mission before substantial channel-triggered work. Avoid competing autonomous schedulers.
Declare connector capabilities explicitly; MCP does not define business semantics.
Mutate another component through its documented API, not direct database writes.

## Alternatives

Evaluate Sim if cockpit integration requires excessive custom work; Mastra if custom product development becomes necessary.
Do not combine all runtimes. Pin Paperclip/OpenClaw versions during qualification.

## Growth

Use one deployment per trust boundary. Later federation exchanges structured missions with separate budgets and identities.
