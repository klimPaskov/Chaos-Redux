# Event 131 Immigrations: implementation routes and acceptance contracts

## Purpose and evidence status

This document assigns bounded implementation and review responsibilities for the restored starter. The gameplay specification owns the design. These routes describe the interfaces that must support it, the relevant repository owners, and useful verification evidence. They do not prescribe parser changes or a parallel migration system.

The original pass inspected repository snapshot `41bc4e5045a7b5c131be69dda2f08079d478634c`, and the import review re-verified the paths and identifiers named here at `2eabe59360`. Each route still needs a fresh read of the target checkout before implementation. Generic source-reading and review agents supported the original specification. They were not the named Chaos Redux project specialists listed below. No project custom agent, HOI4 MCP tool, or live game was run for this package. Historical tool results quoted in repository documents are source evidence, not checks performed for Event 131.

## Ownership and source boundaries

The parent owns Event 131 integration, shared event registration and logging, shared UI, final localisation wiring, and the final acceptance decision. Migration owns requests, cohorts, destinations, reception, settlement, and return. The neutral transfer owner controls physical population mutation. Famine owns food pressure and direct famine mortality. Native policy owns law choices. [R1–R3]

| Surface | Established owner paths and inspection boundary |
| --- | --- |
| Request and spontaneous movement | `common/scripted_effects/migration_core_effects.txt`, `migration_spontaneous_movement_effects.txt`, and `common/scripted_triggers/migration_core_triggers.txt` were inspected in relevant sections. Their current generic submission does not establish the proposed reservation contract. |
| Cohort and transfer guarantees | `common/scripted_effects/migration_adapter_effects.txt` and `docs/systems/civilian_transfer_system.md` provide inspected contracts. Inspect the exact transaction implementation and cohort-history helpers before changing call sites. |
| Prospective reception | Inspect `common/scripted_effects/migration_reception_preparation_runtime_effects.md` and its implementation for retained-row ownership, consent, expiry, full headroom, and cancellation. The spontaneous-owner document identifies this dependency. |
| Event dispatch and history | Parent verifies the actual Event 131 entry file, `initialize_event_categories`, `common/scripted_effects/chaosx_logic_effects.txt`, and `chaosx_events_log_effects.txt`. Do not infer the entry filename from the event number. |
| Settlement, policy, and aid | Follow `docs/systems/migration_system.md`, `national_policies.md`, and the named integration/return owners. International assistance still needs exact donor, transport, and delivery call-site discovery. No direct migration-panel aid button is established by the seventeen-action inventory, which was re-verified in `docs/systems/migration_system.md` at `2eabe59360`. |

The Event 149 retirement text in `docs/systems/migration_system.md` still conflicts with the user's explicit restoration of Event 131, and its documentation owner must record the narrow exception. Catalog 149 is the former identity. Reconcile that documentation without turning `migration_register_initial_incident` into a generic event factory. That existing seam creates no event, event-log entry, pacing pulse, cohort, or physical movement. [R1, R2]

## Four critical acceptance contracts

### 1. Accepted request and provenance

The migration-owned Event 131 adapter must accept an exact source episode, origin, current authority, cause, requested amount, and unique request identity. Acceptance requires an additional uncommitted population claim above the shared protected floor. The event creates no cohort row itself.

Same-source overlap proof is mandatory. An existing famine, hostile-capture, occupation, or earlier event obligation cannot become another wave because a different event label requests it. Current generic pressure submission is additive. Its inspected validation does not supply reservation or replay protection, and an optional generation record alone does not prove either guarantee. [R2, R3]

Acceptance returns a truthful disposition and accepted amount. Repeating the same request cannot add pressure or create another cohort. A rejected, exhausted, or below-minimum request creates no successful-start claim. Event presentation and accounting must correspond to the committed new episode. Generation, request, and cohort identities remain distinct concepts, with each checked against its own provenance.

Staging reserves part of the accepted claim without creating another claim. Successive first-departure batches cannot exceed its remaining accepted budget, and only their measured actual debit consumes that budget. Onward transfers and returns reuse the same people. A final below-minimum remainder needs a supported exact final batch or real terminal disposition. It cannot be rounded upward, discarded, or left permanently blocked solely by the ordinary batch minimum.

### 2. Foreign intent through shared dispatch

The existing `migration_request_cross_border_flight` queues pressure. The shared owner still selects internal destinations first and classifies eventual movement from actual owner equality. Its name does not guarantee the starter's foreign-directed premise. [R3]

The proposed contract retains originating episode and foreign intent through the shared request, any staged cohort, and any retained prospective row. Untagged migration retains ordinary internal-first behavior. A foreign-intent request may wait, reroute through a valid foreign destination, or have its unrealized intention canceled when its relevant origin obligation safely resolves.

Foreign-only intent applies to each still-unmoved portion. Its first actual foreign arrival fulfills that intention while preserving permanent episode provenance. Later domestic distribution follows the normal shared owner. Arrival of one portion does not clear the intention of an unmoved remainder.

Intent grants no border permission, food safety, transport, capacity, or consent. Pending requests produce no arrivals, deaths, population debit, or reception load. Refusal, expiry, changed control, and unavailable routes preserve the living people and retire only matching permissions. If internal safety later resolves the episode, report that outcome as abandonment of foreign intent, not successful immigration. Cancellation after actual departure cannot erase the hosted cohort.

### 3. Physical movement, reception, and delivered assistance

Every physical leg uses the exact transfer owner and satisfies `actual origin debit = route deaths + actual survivor credit`. Deaths are a slice of the measured debit. Reception uses actual surviving arrivals, and integration never grants those people again. [R2]

The primitive can restore an uncredited residual and finalize a smaller conserved transfer. That does not relax a retained prospective contract requiring full headroom and a complete passage. Do not resize a retained row silently. The current safe spontaneous route requests zero route deaths, so unsafe mortality requires its actual existing owner and route contract. [R3]

International assistance requires a proven payer, eligible recipient, actual resources, and delivery evidence before any receiving benefit is published. Discover and reuse the shared humanitarian donor, relief, or transport contract. If the required response is absent, propose a minimal shared response extension with those guarantees. A pledge, diplomatic agreement, or paid-but-undelivered shipment is not delivered shelter, supplies, or capacity.

### 4. Lifecycle, recurrence, and durable outcomes

Rebinding preserves cohort identity and historical origin while validating its current host and living amount. Onward movement and return depart from that current host. Local integration settles the hosted cohort and releases reception obligations without another population transfer. Refusal or renewed safety alone does not teleport anyone. [R2, R3]

Starter handoff completion is separate from resolution of the migration problem. Dismissed presentation, expired offers, or cleared event flags cannot delete unsettled people. A still-unmoved claim may be released only through its owner after the relevant obligation resolves. Hosted survivors continue under migration.

A later episode must prove additional uncommitted people and fresh request identity. A retry, reroute, or return is not a new wave. Proposed size tiers, a 180-day origin-state repeat interval, and a 30-day calm-resolution observation are draft tuning, not established source guarantees. Use the existing owner cadence. Neither a timer nor a cooldown replaces actual identity, obligation, or safety proof.

## Bounded MCP usage map

All routes below are **not run for this specification**. Discover the installed schema before supplying arguments. Use the current AGENTS.md retry limits, preserve useful unchanged evidence, and report unavailable checks separately from implementation defects. Tool outputs must identify the exact source revision and named scenario. [R4]

| Route | Useful inputs and scenarios | Required output and fallback |
| --- | --- | --- |
| `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup` | Current installed reference context, uncertain population or scope syntax, exact helper consumers, and relevant existing patterns. Search a narrow symbol or question before reading its complete applicable entry. | Installed documentation and exact source precedents. Fall back to the current local owner sources where available, distinguishing documented syntax from an unverified assumption. |
| `hoi4.script_validate` when exposed | Changed effect or trigger bodies under their actual country, state, or other documented scope. | Bounded syntax and scope findings. Source checks remain useful if the tool is unavailable and do not become an engine execution claim. |
| `hoi4.event_inspect`, `hoi4.event_render` | Event 131 entry, dispatch helpers, actor preparation, registration, and history consumers. Review accepted start, rejected commit, duplicate invocation, and later recurrence. | Linked-source findings and an event graph/render where useful. Source tracing can answer unsupported structural questions. Neither path proves live timing or population conservation. |
| `hoi4.map_inspect` | Concrete origin and destination states, adjacency, supply, railways, ownership, and control. Compare valid neighboring passage, blocked transport, and changed-front cases. Use supported view parameters only when geography matters. | Exact topology and source references, with a bounded view when useful. Fall back to the same installed map and state sources. Map inspection alone does not prove consent, capacity, or a valid transfer receipt. |
| `hoi4.probability_inspect`, `hoi4.probability_analyze` | Complete changed origin/destination pools and named calm, stressed, acute, small-host, closed-border, threshold, and untagged-regression scenarios. Use `analysis = sweep` and `compare` where relevant. | Scores, rankings, threshold traces, source revisions, and exact/bounded/score-only conclusions. If unsupported, calculate the same scenarios from source with assumptions. Use `simulate` only for declared uncertainty, `sequence` only for a complete custom cadence, and `render` when it improves review. Never equate willingness scores with click probabilities. |
| `hoi4.gui_inspect`, `hoi4.gui_render` | Only shared surfaces actually changed by the parent, with matching baseline/final states, resolutions, and UI scales. Include pending request, blocked action, and resolved presentation when affected. | Scope, text, layout, click-region, and matching render evidence. Fall back to the same source/layout review and identify unverified native rendering. No separate GUI comparison tool is assumed. |

Receipt uniqueness, same-source overlap, conservation, and terminal behavior also require direct owner-source review. A successful structural tool call is not evidence that those semantic contracts execute correctly.

## Canonical project subagent routes

The canonical definitions below are under `.claude/agents/`. Their supporting skills use `.claude/skills/`, including events, map-states, decisions-missions, scripted-gui, subagents, and xlsx. Future specialist prompts must be self-contained, history-free, and give Event 131's accepted requirements, source revision, exact allowed files, dependencies, forbidden changes, and handoff path. Each returns changed files or findings, meaningful evidence, and remaining limits. The parent reviews every result before integration. [R4]

### `chaosx_scripted_system_architect`

Definition: `.claude/agents/chaosx-scripted-system-architect.md`.

Use first to define the accepted-request, overlap, provenance, and foreign-intent interfaces. Inputs are the four contracts, inspected owners, and actual call sites. Own the bounded helper contract, matching documentation, and narrowly assigned adapter changes. Return scopes, inputs, outputs, side effects, cleanup, and dependency map. Do not redesign migration or author unused helpers. Complete this contract before the state worker edits overlapping files. The parent approves the interface and integrates event call sites.

### `chaosx_map_states_worker`

Definition: `.claude/agents/chaosx-map-states-worker.md`.

Use after interface agreement for assigned sections of migration core effects, spontaneous effects, core triggers, and their matching documentation. Inputs include exact allowed functions, current cohort/prospective contracts, and representative states. Return identity, reservation, conservation, reception, and cleanup evidence. Add retained-reception files only after inspection and explicit scope assignment. No second population path, map-geometry change, or world scan is authorized. The parent reviews interaction with existing callers and owns integration.

### `chaosx_decision_mission_auditor`

Definition: `.claude/agents/chaosx-decision-mission-auditor.md`.

Use when the proposed handoff affects an existing action or shared assistance response. Supply exact decision/action owners, costs, due dates, cancellation, and payment/delivery contracts. Own bounded action-helper and action-text review or assigned local fixes. Return affordability, refund, rejection, pending-work, and exploit findings. Dependencies are accepted request semantics and discovered aid ownership. No new decision system or shared-window layout ownership is granted. The parent implements shared UI and reviews all behavior changes.

### `chaosx_ai_probability_auditor`

Definition: `.claude/agents/chaosx-ai-probability-auditor.md`.

Use after changed weighted surfaces stabilize. Supply exact source files, complete candidate pools, named scenarios, and genuine baseline snapshots. Own read-only probability and score analysis across the changed surfaces. Return classified results, dominance or starvation findings, assumptions, and available artifacts. No gameplay patching is permitted. An unavailable baseline limits before/after claims without preventing current-behavior review. The parent decides tuning and requests rechecks only for affected scenarios.

### `chaosx_localisation_auditor`

Definition: `.claude/agents/chaosx-localisation-auditor.md`.

Use after visible behavior and keys stabilize. Supply Event 131 text and exact affected migration/report keys with their consumers. Own bounded wording and localisation-key review, including request versus arrival, refusal versus return, and integration versus population gain. Return exact edits or defects and unresolved dynamic-text cases. Do not assign catalog edits, gameplay logic, or shared GUI layout. The parent reviews factual consistency and owns final wiring.

### `chaosx_event_completion_auditor`

Definition: `.claude/agents/chaosx-event-completion-auditor.md`.

Use after parent integration. Supply accepted specifications, dispositioned plans, implementation files, and prior useful handoffs. Own a read-only requirement-to-source completion audit. Return missing or stale requirements, known defects, and unavailable verification separately. Do not patch or promote unaccepted proposals into requirements. Reuse unchanged evidence and request only missing or affected weighted checks. The parent owns the final completion claim.

### Documentation and catalog specialists

`chaosx_documentation_curator`, defined in `.claude/agents/chaosx-documentation-curator.md`, receives accepted decisions and final behavior. Own only assigned event/system documentation, including reconciliation of Event 149 retirement wording. Return repaired references and explicit source-versus-acceptance dispositions. Do not edit gameplay or silently rewrite design. Parent review precedes promotion.

`chaosx_spreadsheet_doc_worker`, defined in `.claude/agents/chaosx-spreadsheet-doc-worker.md`, runs after wording and status are established. Own `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its required generated exports through `.tools/export_event_catalog_csv.py`. Supply exact rows, fields, and player-facing source text. Return changed cells and export results. Never edit CSV snapshots directly, invent status, or change localisation. The parent verifies final alignment.

Shared migration UI, event logs, Event Details, and settings remain parent-owned. Do not route them to `chaosx_event_ui_worker`. Unknown repository ownership may justify a narrowly scoped read-only `chaosx_repo_explorer` assignment, not a default broad preflight.

Preserve actual policy, panel, and achievement eligibility when reviewing shared integration. The Holy Realm's documented Event 003 refuge-policy adapter remains authoritative outside the shared civilian-law panel, even though its humanitarian movement predicate passes.

## Source basis

- **R1:** User-directed brief, preserved as `131_immigrations_original_brief.md`. The earlier project source-protocol bundle is not part of this repository, so current guidance is `AGENTS.md` and the canonical `.claude` skills.
- **R2:** `docs/systems/migration_system.md`, `civilian_transfer_system.md`, `national_policies.md`, and `common/scripted_triggers/humanitarian_validation_triggers.md` at the inspected revision.
- **R3:** The named migration core, adapter, spontaneous-owner, and trigger files, including `common/scripted_effects/migration_spontaneous_movement_effects.md`.
- **R4:** Current canonical `.claude/agents/` definitions and `.claude/skills/chaos-redux-subagents/SKILL.md`. Legacy TOML tool names and stricter obsolete fallback rules are not used here.
