# Development methods for Workstead

Research date: 2026-09-14. Status: proposed operating method, not an executed product qualification. Sources below are official documentation and the installed BMAD distribution. No comparative performance benchmark was run.

## Recommendation

Combine BMAD's product and architecture discipline with Codex's task execution, repository records, and deterministic continuous integration. Astra is the development model, not a substitute for explicit requirements or evidence. Keep the product's runtime architecture independent of our development tooling. Paperclip/OpenClaw remains a candidate until integration experiments pass.

## What Astra changes

**Documented guidance.** OpenAI's September 11 article recommends narrower skill triggers, progressively loading supporting material, and reading documentation according to the task. It warns that elaborate recipes, oversized instruction catalogs, and repeated test instructions can waste context or constrain Astra. It also recommends explicit completion criteria and permission boundaries because Astra may stop earlier than desired when instructions imply a review checkpoint. [Astra prompting and skills guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

**Proposed practice.** Assign a complete outcome: the relevant requirement identifiers, scope, permitted operations, acceptance evidence, and stopping conditions. Let the agent choose implementation steps. Routine reversible work should proceed through implementation, relevant verification, corrections, and documentation without seeking approval at each step. Paid operations, production changes, and unresolved product choices remain distinct boundaries. Do not remove mandatory BMAD gates or claim that model confidence demonstrates correctness.

## BMAD: pin, invoke, and record

**Documented and inspected.** The installed BMAD 6.12.0 `bmad-help` skill reads its catalog and resolved configuration, checks artifact contents, and distinguishes a started workflow from a completed one. Its architecture headless instructions allow non-interactive work with recorded assumptions and open questions while retaining mandatory reviewers and linting. See the installed [help skill](../../.agents/skills/bmad-help/SKILL.md) and [architecture headless reference](../../.agents/skills/bmad-architecture/references/headless.md).

The [current upstream README](https://github.com/bmad-code-org/BMAD-METHOD) now advertises a `bmad` hub, `bmad-build`, and plugin installation routes. These must not be assumed interchangeable with the pinned 6.12 distribution.

**Proposed practice.** Preserve the pinned installation for this baseline. Use its actual help catalog to select product, architecture, specification, build, and review workflows. Record workflow version, inputs, artifact paths, status, and unresolved questions. Run a workflow to completion before marking its stage complete; pre-existing draft files are inputs. Use supported headless operation where applicable to honor the owner's autonomy preference. Evaluate upstream upgrades separately through a small migration trial rather than silently replacing workflows mid-project.

## Repository context and parallel work

**Documented capability.** Codex reads hierarchical `AGENTS.md` instructions. Subagents can isolate independent work and return summaries; current clients expose delegation, but availability and permissions depend on the surface. Each subagent consumes model resources. Git worktrees provide separate checkouts sharing Git metadata. [Repository instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees).

**Proposed practice.** Keep `AGENTS.md` short: project boundaries, documentation entry points, verification commands, and handoff rules. Keep requirements, decisions, and status in versioned files; retrieve relevant sections rather than injecting the whole repository into every task. Reviewers receive the requirements, proposed artifact or diff, and verification evidence in a separate context. This reduces shared conversational bias but does not guarantee independent errors.

Delegate bounded research or review when authorized and useful. Use separate branches/worktrees for concurrent code changes and explicit file ownership for shared documentation work. One integrator resolves overlaps. A task's handoff states what changed, what was checked, remaining uncertainty, and the next executable action.

## Quality gates and GitHub Actions

**Documented capability.** The official Codex GitHub Action runs agent tasks in CI; its documented setup requires an OpenAI API key. It is a separate choice from ordinary GitHub Actions running scripts. [Codex GitHub Action](https://learn.chatgpt.com/docs/github-action).

**Proposed practice.** Make deterministic checks the baseline: document consistency now; later compilation, type checks, contract tests, integration/recovery tests, and relevant browser tests. Pin dependencies and workflow actions; retain reports linked to the tested commit. AI review supplements these checks and does not replace executable evidence. Do not enable paid agent CI simply because Pro is available.

Use GitHub Issues for work and Markdown for specifications; defer Jira until collaboration needs justify it. Each pull request links requirements, implementation, acceptance evidence, and updated operating documentation. Test risk at component boundaries: duplicate events, restart recovery, authorization, version-specific acceptance, cancellation, and costs. Visual acceptance requires inspecting rendered screens and actual outputs, not only successful builds.

## Cost, maturity, and success criteria

**Documented limits.** Usage varies with model, task, and context; OpenAI recommends trimming unnecessary context and tools. No fixed number of Workstead tasks can be inferred from the subscription. [Usage and pricing](https://learn.chatgpt.com/docs/pricing).

**Proposed practice.** Start without unattended loops or experimental runtime dependencies. Use focused Astra tasks for difficult synthesis and implementation, and measure whether additional agents reduce rework enough to justify consumption. Assess our method with lead time, escaped defects, reopened reviews, evidence completeness, and operating effort. Success means a reproducible accepted increment with known limitations, not a large document count or a high agent count.
