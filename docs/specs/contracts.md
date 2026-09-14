# Candidate integration contracts

Status: conceptual draft. Produce executable schemas after qualifying the real APIs.

Identifiers: organization_id, participant_id, mission_id, run_id, artifact_id, artifact_version, external_ref.

| Port | Operations | Invariants |
|---|---|---|
| Conversation | receive, reply, notify | Verified actor; preserved channel/thread; deduplicated event |
| Work | create, assign, comment, transition | Explicit field ownership; no circular synchronization |
| Artifact | put, get, version, link | Real retrievable output; immutable accepted version |
| Execution | start, status, cancel, events | Mission/run/provider-job correlation |
| Cost | estimate, reserve, settle | Currency and units; estimates distinct from bills; unknown is never zero |

Each connector declares version support, limits, cancellation semantics and authentication modes.
Duplicate delivery must not create another effect. Reconcile ambiguous provider state before retrying.
