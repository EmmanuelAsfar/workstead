# Product requirements

Status: DRAFT. Based on the 2026-09-14 discussion. BMAD review remains pending.

| ID | Requirement | Pilot acceptance criterion |
|---|---|---|
| REQ-001 | Configurable organizations and roles | Instantiate the studio from configuration without editing business code |
| REQ-002 | Persistent identities, intermittent runs | An idle agent retains identity without a continuous LLM loop |
| REQ-003 | Mission ownership and constraints | Every dispatched mission has an ID, owner, budget and acceptance criteria |
| REQ-004 | Hybrid participation | A verified human can own a task, comment and approve work |
| REQ-005 | Replaceable channels | Replay a process through two channels with explicit mappings |
| REQ-006 | Replaceable ticketing | An external ticket creates one mission; ownership of synchronized fields is documented |
| REQ-007 | Versioned deliverables | Approval references the exact artifact version or digest |
| REQ-008 | Observable activity | Show mission, agent, tool actions, outputs, errors and human waits |
| REQ-009 | Cost management | Distinguish estimated, committed and settled spend; unknown costs stay explicit |
| REQ-010 | Configurable providers | Map role/task type to a configured model and gateway |
| REQ-011 | Recovery and idempotency | Replayed events do not duplicate missions or paid provider jobs |
| REQ-012 | Cancellation | Display local cancellation separately from actual provider state |
| REQ-013 | Portable storage | Use local then external storage; verify access rights and previews |
| REQ-014 | Reproducible operations | Rebuild from pinned versions and verify backup restoration |
| REQ-015 | Execution isolation | Generated code cannot access cockpit secrets or the host Docker socket |
| REQ-016 | Organizational knowledge | Separate approved procedures from notes; identify sources and freshness |

## Main journey

Brief → mission → plan → specialist work → review → requested changes → version-specific acceptance.
Errors, budget limits and missing capabilities result in explicit states and human escalation.

## Open decisions

Full organizational-chart parity; first media provider; second channel; first external storage provider; hosting target.
No delivery-date or total-cost commitment before measuring the prototype.
