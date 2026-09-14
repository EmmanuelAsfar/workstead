---
title: Workstead Product Requirements
status: draft
created: 2026-09-14
updated: 2026-09-14
revision: 0.2
approval: pending-product-baseline-review
---

# Workstead product requirements

## 1. Purpose and vision

Workstead lets an operator configure a hybrid organization, delegate digital work, inspect progress and accept the resulting deliverables. Humans and agents share missions, conversations and reviewable outputs. The operator can replace collaboration, ticketing, storage and AI providers without rewriting the organization's roles and process.

This PRD defines observable product behavior. It is a refined planning draft, not evidence that any runtime can deliver it. Architecture candidates and transport decisions belong in `addendum.md` and architecture records. Stable REQ identifiers from revision 0.1 are preserved. New inferred choices are marked [ASSUMPTION] and have an owner and revisit point.

The first goal is a convincing, usable personal pilot. Workstead must make actual work and intervention visible; an animated organization chart or a busy conversation feed alone does not demonstrate success.

## 2. Users and working journeys

The initial operator is Emmanuel, an experienced developer experimenting personally with digital production. A participating human may receive a task, provide content, request changes or accept a deliverable. An agent has a declared role, capabilities and delegated authority; it is identified as an agent in shared surfaces.

Jobs to be done: turn an objective into accountable work; see what is happening without inspecting raw logs first; intervene before waste; judge the deliverable; reuse the organization in a different tool environment.

**UJ-1 — Direct a digital studio.** Emmanuel provides a creative brief, inspects the proposed work, contributes or corrects a script, and reviews a video or small application. He can open the actual deliverable, request a revision and accept a specific version. This journey is supported by REQ-003, REQ-004, REQ-007 and REQ-008. This is structured from the user's described scenario; exact screens and stage ordering remain proposed UX decisions.

**UJ-2 — Investigate a blocked mission.** Emmanuel opens an agent's current activity, sees whether it is waiting for a human, a provider or a retry decision, and supplies the missing decision. A timeout never appears as a successful delivery. Supported by REQ-008, REQ-009, REQ-011 and REQ-012.

**UJ-3 — Reuse the organization.** Emmanuel applies another connector profile and runs the same process. Role instructions and acceptance rules remain unchanged; provider-specific mappings and unsupported capabilities are visible. Supported by REQ-001, REQ-005, REQ-006, REQ-010 and REQ-013.

## 3. Vocabulary

- **Organization:** roles, participants, policies and missions belonging to one operational boundary.
- **Role:** a reusable definition of responsibilities, skills and allowed actions.
- **Participant:** an identified human or agent belonging to an organization.
- **Agent:** a persistent participant identity whose work is performed through intermittent runs.
- **Mission:** accountable work with an owner, objective, budget policy and acceptance criteria; it may have child missions.
- **Run:** one execution attempt on a mission. A run completing does not mean the mission is accepted.
- **Artifact:** a retrievable deliverable with a version, provenance and access policy.
- **Review:** a recorded assessment of a specific artifact version. Acceptance is an authorized review outcome.
- **Connector profile:** configuration selecting external systems, mappings and declared capabilities.
- **Provider job:** an external operation that may continue independently of a run, such as media generation.

## 4. Functional requirements

### Organization and delegation

#### REQ-001 — Configure organizations and roles

The operator can instantiate an organization from reusable role and process configuration. Changing the number of agents does not require editing business logic. Invalid role references or unavailable capabilities are reported before activation. The pilot uses one organization; its configuration must be exportable without secrets.

#### REQ-002 — Persistent agents, intermittent execution

An agent retains its identity, assigned work and context across runs. Idle or paused agents do not repeatedly call a model merely to demonstrate availability. The operator can create, pause, resume and retire an agent. Pause and retirement prevent new runs; already admitted runs and provider jobs remain visible and continue unless explicitly cancelled under REQ-012. Retirement preserves history and exposes unfinished assignments for reassignment. [ASSUMPTION A1: agent creation that expands concurrency or spending requires operator authorization in the pilot.]

#### REQ-003 — Missions, ownership and bounded delegation

Every dispatched mission has a stable ID, one accountable owner, an objective, acceptance criteria and an explicit budget policy. A mission may contain child missions, with visible dependencies and responsibility. Delegation preserves organizational access restrictions and does not silently multiply the parent budget. Circular dependencies or a configured delegation limit block dispatch with an actionable reason.

### Hybrid collaboration and openness

#### REQ-004 — Human participation and controlled reviews

A verified human can own a mission, contribute an artifact, comment, request changes and accept work when authorized. Agent messages identify their origin. Approval uses the authenticated reviewer's identity and authority; quoted text or an incoming message claiming to be the owner is not authorization. The operator sees the human's work beside agent work. Perfect visual parity in the organization chart is not required for pilot acceptance, but ownership and review must be first-class behaviors. [ASSUMPTION A2: approvals can initially open a cockpit link from chat.]

#### REQ-005 — Replaceable conversations

A supported channel accepts a brief or follow-up, associates it with its organization and mission, and returns replies in the correct conversation. Participants can address each other or ask the operator for a decision through authorized shared channels. Conversation events that create work are deduplicated. Prove the same process on two selected channel systems. Email is a required connector family: sending, receiving, threading and recipient restrictions must be specified; live email can follow the first two-channel demonstration. [ASSUMPTION A3: defer live email execution until channel portability passes.]

#### REQ-006 — Replaceable ticketing

An external work item can start or update a mission. The integration records external references, field ownership and mapping rules. Receiving the same event twice does not create two missions. Conflicting edits produce a visible conflict or a documented deterministic resolution; updates must not echo indefinitely between systems. The pilot demonstrates one external ticketing system in addition to native mission management.

#### REQ-010 — Configurable models, gateways and tools

The operator maps roles and task types to provider/model profiles and permitted tools, including suitable third-party MCP servers. A run records the profile actually used. Any fallback is explicit, attributable and subject to the same permission and budget constraints; unavailable or incompatible profiles do not silently change behavior. Image, video, sound and application-production capabilities are configurable as supported tools; the pilot selects a bounded subset of providers rather than promising universal support.

#### REQ-013 — Portable artifact storage

An artifact can be stored locally or through a selected external storage connector while retaining mission association and provenance. Authorized humans and agents can retrieve it; denied access is reported. A connector declares whether it supports immutable versions, previews and revocable links. The pilot proves local and one external storage profile. A missing remote file is not displayed as a completed deliverable.

### Deliverables, knowledge and supervision

#### REQ-007 — Artifact versions and acceptance

Each deliverable has a stable identity, version or digest, producer and originating mission/run. The review displays the exact submitted content or an unambiguous version-specific link. A material change creates a new version and cannot inherit acceptance of the previous version. Requesting changes reopens work without losing the earlier decision. The submitter cannot provide its own final acceptance where the process requires an independent reviewer.

#### REQ-008 — Visual supervision and intervention

The operator can move from organization overview to mission to run and its artifacts. Show working, idle, paused, waiting-for-human, waiting-for-provider and failed conditions distinctly. The activity detail exposes observable tool calls, messages, results, errors and reported usage, with sensitive values redacted. Show the last confirmed update time. After a configurable `stale_after_seconds` interval without a confirmed update, display stale telemetry rather than asserting that the last observed execution state is current. When no telemetry source exists, display unknown. Qualification verifies the boundary with a controlled clock. The UI must not imply access to private model reasoning. Users can inspect documents and media without hunting through unrelated logs; application deliverables provide an isolated preview or a clearly identified unavailable-preview state.

#### REQ-016 — Knowledge and memory provenance

Role instructions, approved procedures, reference documents and agent-written notes remain distinguishable. A run can retrieve authorized mission history and relevant organizational documents with source/version provenance. The operator can correct or withdraw a procedure and inspect what context supported a recorded output. Agent notes cannot silently become organizational policy. Long-term knowledge access respects organization and document permissions. Automatic organizational learning is deferred.

### Cost and lifecycle correctness

#### REQ-009 — Spending visibility and controls

Show estimated, committed and settled spend by organization, mission and agent, with model/provider detail where available. Include paid media operations and identify unreported costs as unknown rather than zero. A paid operation must pass the configured admission policy before submission. When a reliable ceiling cannot be established, require an explicit operator exception or decline dispatch. Existing commitments remain visible when a limit blocks new work. Parallel admissions must not each consume the same remaining allowance. Display the currency, unit, calculation source and reconciliation status; do not claim a guaranteed provider invoice cap when the provider cannot enforce one.

#### REQ-011 — Restart and duplicate delivery

Persist accepted mission dispatches and provider-job references before acknowledging recoverable work as accepted. Replayed events or restarted workers must reconcile prior outcomes before issuing another external effect. An ambiguous provider result is marked unknown and routed for reconciliation; a second paid submission is not the default recovery action. Qualification deliberately interrupts processing and checks mission count, job identifiers and provider charges where available.

#### REQ-012 — Honest cancellation

An authorized operator can stop new work on a mission and request cancellation of active runs and provider jobs. Show requested, confirmed, unsupported and unknown cancellation outcomes separately. Cancellation does not imply a refund or immediate remote termination. A late provider result remains traceable and cannot automatically revive a cancelled mission or be published outside its permissions.

## 5. Cross-cutting quality requirements

#### REQ-014 — Reproducible setup and recovery

A clean checkout and documented configuration reproduce the pilot using pinned component versions. A backup includes the state, files, runtime context and protected recovery material needed to restore it. Verify restoration in a separate environment; record any loss window instead of implying zero loss. Retain release identifiers and migration compatibility for rollback.

#### REQ-015 — Isolation and least authority

Generated code cannot access cockpit credentials, unrelated organization data or unrestricted host administration. Each participant and tool is limited to the resources required for the current mission. The pilot explicitly tests denied access. Imported documents and messages are task data, not a source of permissions or operating-policy overrides. Broader tenant isolation is deferred until independent organizations are introduced.

Additional pilot quality boundaries:

- **NFR-01 — Bounded concurrency:** configure a maximum active-run count and visible queue. Start at two active runs to measure behavior; this is an assumption, not a capacity claim. [ASSUMPTION A4]
- **NFR-02 — Tablet operation:** at a viewport width of 768 CSS pixels, an operator can inspect a mission, open its artifact and submit a review without a desktop-only interaction. [ASSUMPTION A5: responsive web is the initial product surface.]
- **NFR-03 — Frugality evidence:** measure idle memory, active resource use, connector setup effort and custom maintained code during qualification. No unmeasured RAM or infrastructure-cost target is asserted. If meeting the pilot requirements needs a permanent upstream fork, or both a rebuilt cockpit and a new execution scheduler, stop feature expansion and compare alternatives before accepting the candidate. Otherwise record every required service, its purpose, and the connector maintenance demonstrated by the portability exercise.

## 6. Pilot boundary and success

The pilot is an experience-and-portability demonstration: one hybrid studio with configurable agent roles and a human operator; real digital outputs; visible intervention; recoverable execution; and a second tool environment. All REQ identifiers describe the target pilot except explicit phased email execution and later organization federation.

The first qualification slice uses fewer agents and one tool profile to test lifecycle behavior. It is not the completed pilot. The portability slice adds a second channel, external ticketing and external storage. [ASSUMPTION A6: qualify one representative provider per connector family before adding more.]

**SM-01 — Complete work:** execute a script, video and small-application mission with retrievable outputs and recorded review outcomes. This is a proposed acceptance set drawn from the user's examples, not a claim of existing capability. Validates REQ-003, REQ-004 and REQ-007.

**SM-02 — Portability:** replay the selected process with a second connector profile; record changed configuration/mappings and demonstrate no role or process rewrite. Validates REQ-001, REQ-005, REQ-006, REQ-010 and REQ-013.

**SM-03 — Recovery:** all selected qualification scenarios record evidence; no unexplained duplicate external operation or unowned accepted work remains at acceptance. Validates REQ-009, REQ-011, REQ-012 and REQ-014.

**Counter-metrics:** track total spend, human correction effort, retry/delegation count and rejected-output rate alongside completed missions. Optimizing message count, number of agents or apparent activity is not success.

Non-goals: real portfolio management, enterprise compliance certification, unattended unlimited spend, fifty simultaneous agents, a native mobile app, universal connectors, or deployment across mutually untrusted organizations in the pilot. Independent organizations communicating across servers remain a product direction and must not be designed out by hard-coded global identities.

## 7. Open decisions and assumptions

| Item | Owner | Resolution point |
|---|---|---|
| OQ-01: select two channel systems and the email phase | Emmanuel; agent proposes based on access and connector evidence | Before portability stories are committed |
| OQ-02: select media provider, allowable spend and test credentials | Emmanuel | Before any paid qualification operation |
| OQ-03: choose first external ticketing/storage profiles | Agent proposes; Emmanuel confirms account access | Before connector implementation |
| OQ-04: accept, revise or reject runtime/cockpit pairing | Agent supplies qualification evidence; Emmanuel chooses material tradeoffs | Before architecture baseline and implementation readiness |
| OQ-05: choose hosting and data-retention policy | Agent proposes; Emmanuel confirms | Before a persistent hosted pilot |

Assumptions A1–A6 are provisional implementation-planning defaults, not silently approved user requirements: controlled spawning, cockpit-linked approvals, phased email, two-run initial concurrency, responsive web/tablet support, and one representative provider per connector family. They allow drafting and technical research; they do not authorize paid operations or production release.
