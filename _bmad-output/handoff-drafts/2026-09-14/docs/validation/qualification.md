# Qualification plan

All product scenarios are NOT RUN. Documentation baseline checks do not change these states.

| ID | Requirements | Scenario and required evidence |
|---|---|---|
| QUAL-01 | REQ-003, REQ-008 | Brief to mission to run to visible real file, with correlated identifiers |
| QUAL-02 | REQ-004, REQ-007 | Human review, revision and new version; old approval cannot authorize the revision |
| QUAL-03 | REQ-011 | Restart during a media job, recover the result and verify no second billed submission |
| QUAL-04 | REQ-009, REQ-012 | Concurrent work, budget reached and cancellation; compare local and provider state |
| QUAL-05 | REQ-005, REQ-006, REQ-013 | Replay with a second channel, external ticketing and storage without changing roles |
| QUAL-06A | REQ-014 | Restore state, files and sessions in a separate environment; record the actual recovery window |
| QUAL-06B | REQ-015 | Verify generated code and untrusted input cannot obtain cockpit secrets or expand authority |
| QUAL-07 | REQ-001, REQ-002, REQ-003, REQ-010 | Instantiate a configuration, pause/resume/retire an agent, preserve unfinished work and verify the actual model/tool profile used |
| QUAL-08 | REQ-016 | Withdraw an approved procedure, retrieve authorized history and verify that agent notes cannot silently replace policy |

Record versions, date, commands, sanitized inputs, evidence, PASS/FAIL/INCONCLUSIVE and deviations.
Documentation checks do not prove product behavior. Paid calls require a configured budget.

## Evaluation rules

- QUAL-03: compare persistent mission/run/provider identifiers before and after interruption. If provider billing cannot be verified, record INCONCLUSIVE rather than PASS.
- QUAL-04: record admitted, blocked and still-committed work; verify concurrent admissions and late results. Unsupported remote cancellation is an expected explicit state, not successful cancellation.
- QUAL-05: preserve role/process configuration hashes; list every changed mapping and validate permission behavior.
- QUAL-06A and QUAL-06B are independent gates; one passing result cannot imply the other passed.
- QUAL-07 and QUAL-08 are required before pilot acceptance, even if the first runtime spike addresses only QUAL-01 through QUAL-04.
