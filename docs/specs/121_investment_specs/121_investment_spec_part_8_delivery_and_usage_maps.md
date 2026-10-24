# Investment specification, part 8: Delivery and usage maps

## 1. How to use the package

This package is the complete proposed design for Investment. Parts 1–3 own the experience, sector outputs, evolutions and consequences. Part 4 owns the purchase, decision, timer and terminal contracts. Part 5 owns presentation and achievements. Part 6 owns AI and acceptance scenarios. Part 7 owns runtime identities, shared systems and integration. This part assigns implementation work and evidence responsibilities.

The archive's single top-level folder is `121_investment_specs`. Place it under `docs/specs/`. The resulting control documents live at `docs/specs/121_investment_specs/`. Execution plans, assignments, implementation notes and review handoffs belong under `docs/plans/121_investment_plans/`. Keep those notes separate from the specifications they implement.

All eight parts are controlling documents. A shorter handoff prompt does not replace them. If an apparent conflict remains, compare the concrete gameplay rule with its action and integration contract, record the resolution in the implementation plan and update the affected specifications together. Do not silently omit a difficult branch.

Historical package note: the original planning authors recorded a prior request for a full expansion. The current user has separately accepted the uploaded Event 121 identity and authorized catalog migration on 2026-10-24; that decision does not accept the package's numeric gameplay anchors, routes, or mechanics. The 2026-10-24 user-authorized identity/catalog migration is implemented: the current registry records Investment at 121, preserves The Pact as a displaced concept, and reports Unavailable status with no runtime root. This identity decision does not accept gameplay mechanics.

## 2. Implementation sequence and useful milestones

| Milestone | Result that can be reviewed | Principal dependencies |
|---|---|---|
| Identity and ownership | Implemented Event 121 Investment catalog identity, displaced Pact record preserved, fresh file/key inventory, exact owner APIs | Current `AGENTS.md`, task-relevant owning skills/references, pinned research as historical context, current repository revision |
| Funded baseline | Small civilian charter from offer through all paid phases and terminal release | Capacity adapter, phase receipts, legal site selector, basic category |
| Four complete sectors | Every main and alternative sector output, native and alternative special route | Building legality, research bonus ownership, quote/output allocation |
| Incidents and partial outcomes | Delay, overrun, corruption, investigation, reduced completion, brownfield and wind-down | Exact payments, original-payer custody, mission synchronization |
| Fever program | Two-to-four-state sequential and parallel delivery, partial assets and systemic failure | Site allocation, aggregate progress, explicit Event 35 extension |
| Impossible methods | Three methods, inspected/full operation, finite licenses, repair, containment, disappearance and cascade | Service receipts, removable source contributions, exact damage and deaths |
| Presentation and achievement integration | Final localisation, every runtime texture and sprite, five working achievements | Stable consumer IDs and actual delivered behavior |
| Bounded completion review | Source checks, named scenario results, resolved defects and honest native evidence limits | All implemented routes and owner integrations |

These milestones are implementation slices of the complete scope. They do not authorize declaring completion after the baseline while leaving evolutions as documentation. Conversely, a missing optional renderer does not require an endless review loop or a redesign of the event.

## 3. Actual collaboration used for this planning package

The source reading and planning work used the root assistant and three actual generic source/authoring collaborators, followed by one independent generic reviewer. Those agents read and applied the supplied project-role definitions, but they were not launched as the project's configured canonical production workers. The distinction matters when interpreting what was inspected, authored or executed.

| Actual reader | Completed work | Evidence |
|---|---|---|
| Root | Protocol, brief, current planning/delivery, event integration, mechanics and parent design decisions, source reconciliation, targeted repository and primary-source research, parts 1–3 and 8, packaging | Combined coverage ledger and source/review report |
| `source_coverage_audit` | Full asset and subagent-source assignment, presentation and achievement design, pinned presentation registry inspection, part 5 and art/achievement handoffs | Coverage records, pinned evidence manifest, owned deliverables |
| `source_planning_reader` | Full planning/system-source assignment, economy and decision advisory, part 4 and decision/mission handoff | Coverage records and owned deliverables |
| `source_runtime_reader` | Full runtime/catalog assignment with explicit root takeover of two files, pinned Event 34/35 source inspection, AI/integration parts 6–7 and coding handoff | Coverage records, Git blob-verified source manifest and owned deliverables |
| `bounded_spec_review` | Complete independent read of all eight parts and original prompts, supplied improvement-planner contract, new support-document review and focused correction recheck | Source/review report with the finite finding set and actual review boundary |

The combined gate covers 152 distinct text files, 194 text occurrences and five archive occurrences, totaling 3,211,939 distinct text bytes. All distinct versions were read independently. Duplicate copies were matched by SHA-256. Some initial read outputs were truncated and their affected ranges were reread before the gate passed. The final coverage record has no unread source range. Details and caveats are in [the source and review report](121_investment_sources_and_review.md) and [the coverage ledger](121_investment_source_coverage.json).

For each implementation task, read the current `AGENTS.md`, the owning skill for the touched system, and the references and source sections relevant to the actual change. Reuse evidence already checked in the same task while its underlying files remain unchanged; re-read and recheck changed inputs. The package's historical source ledger is provenance, not a substitute for current instructions or task-relevant source inspection. The eight design parts remain the package's required design input.

## 4. Subagent Usage Map for implementation

### Assignment contract

Discover the actual available runtime roles before dispatch. Current source definitions are authoritative, and the supplied configuration does not register every supplied definition. A definition's presence is not evidence that its configured runtime is available.

Each production assignment should use a self-contained prompt with `fork_turns="none"` where the runtime supports that mode. Include the canonical role definition, exact source paths, the relevant full specification parts, owned files, allowed shared reads, output path, explicit exclusions, dependencies and the parent's acceptance question. Do not rely on an agent guessing missing decisions from a short task title.

Use the configured canonical role when available. If the environment only exposes a generic collaborator, give it the bounded canonical contract and describe the fallback honestly. Do not claim that a named project worker, image generator, native validator or game session ran merely because its instructions were read.

### Logic, decisions and world state

| Canonical role | When and why | Owned surfaces and handoff | Parent review and exclusions |
|---|---|---|---|
| `chaosx_repo_explorer` | Before implementation, settle current identifiers and relevant shared contracts | Read current 121/132 references, workbook rows, Event 34 commitment, Event 35 gateway, cost and achievement owners. Write `docs/plans/121_investment_plans/repository_contracts.md` | Verify current revision and evidence scope. Read-only, no registry or workbook mutation |
| `chaosx_scripted_system_architect` | Before coding the long-lived charter, resolve state and payment ownership | Proposed charter, phase, site, service, consequence and closure contracts in `architecture.md`. Review the `121_investment_*` owner families identified in part 7 | Parent approves actor/nonce/date and idempotence boundaries. Shared framework changes remain parent-owned |
| `chaosx_decision_mission_auditor` | After baseline decisions, then after incidents and anomalies | Event-owned decision/category definitions, cost triggers, phase and warning missions, localisation-key contracts. Handoff `decision_mission_review.md` using part 4 and the dedicated prompt | Verify exact equality, real payment, native timer changes, no repay-on-completion and finite exits. No unrelated decisions or generic GUI redesign |
| `chaosx_map_states_worker` | During legal site selection, rail work and physical delivery | Event-owned state effects/triggers and bounded site allocation. Handoff `state_delivery_review.md` with actual legal state/province cases and custody proofs | Verify real slots, port provinces, railway endpoints, one facility group and controlled ownership. No territorial transfer or map-geometry edits |
| `chaosx_ai_probability_auditor` | After concrete weights and checkpoints exist | Inspect only Investment choices, selector weights, MTTH, incident draws and Event 35 handoff alternatives. Handoff `ai_probability_review.md` with named fixtures from part 6 | Separate raw decision scores, exact lotteries, analytical results and sampled/native evidence. No new global AI polling or unowned strategy mutation |
| `chaosx_event_completion_auditor` | Once all branches are implemented | Full event-owned scope plus narrow owner integrations, traced against the eight parts. Handoff `completion_review.md` with defects and accepted evidence | Test all terminal routes and actual files. Do not accept documentation as executable behavior or an all-positive gateway result as success |

### Presentation and release documentation

| Canonical role | When and why | Owned surfaces and handoff | Parent review and exclusions |
|---|---|---|---|
| `chaosx_asset_source_researcher` | Before documentary scenes and reference selection | Industrial, port, construction and period-material references. Write `asset_reference_notes.md` with source URLs, permitted use and relevant crops | Parent verifies references and rights. Historical references inform scenes without claiming generated art is an archival photograph |
| `chaosx_generated_event_art` | Once report/news/category consumers are stable | Event-owned report, news and static category artwork from part 5 and the asset prompt, with editable originals and provenance | Check every selected consumer, documentary style, composition and exact export size. No portraits, shared art overwrite or unrelated theme redesign |
| `chaosx_icon_artist` | After decision, modifier and achievement semantics settle | Independently authored category, decision, modifier and achievement icon families, including required achievement states | Inspect small-size legibility, alpha, unique aliases, dimensions and decoded DDS. Do not downscale one large image into every icon family |
| `chaosx_localisation_auditor` | After stable mechanics and final text authoring | All Investment English text, dynamic values, costs, options, reports, missions, details, news and achievement tooltips | Parent checks tone, conditional facts, correct payer/target and spoiler boundaries. No final wording is supplied by this planning package |
| `chaosx_improvement_loop_planner` | One bounded whole-package or implementation review after the main work | Compare actual behavior and scope with the brief, identify material weaknesses and propose a finite correction set in `bounded_improvement_review.md` | Fix concrete defects and missed gameplay depth, then stop optional review after a representative recheck. No perpetual reclassification gate |
| `chaosx_documentation_curator` | After implementation facts stabilize | Event documentation, system integration notes, implementation evidence and durable asset provenance | Parent ensures docs match actual behavior and distinguish source checks from native observations. No status inflation |
| `chaosx_spreadsheet_doc_worker` | After accepted gameplay details and actual implementation state are established | Authorized player-facing workbook update and generated CSV exports, with immutable before-copy and parsed comparison | The Event 121 identity migration is complete; update only the fields justified by implemented player-facing content. Preserve The Pact, unrelated rows, formulas and workbook package features |

The map-state worker definition is one of the newer supplied roles absent from the supplied older runtime registration. Verify availability instead of silently assuming it can be dispatched. A generic collaborator using that bounded contract is acceptable when disclosed.

### Shared edits remain coordinated

The parent owns the Event 35 caller extension, random-picker/history integration, exact-cost framework adaptations, shared achievement registry, shared asset aliases and catalog migration. Specialists may propose patches or work in explicitly isolated files. Do not let several agents edit the same shared registry concurrently.

A useful handoff includes the source revision, actual read scope, changed files, owned receipts, named scenarios, unresolved native questions and the exact next action. A claim such as reviewed or tested is inadequate without its evidence boundary.

## 5. MCP Usage Map

### Availability in this planning session

The exposed tool inventory was checked and contained no HOI4 or Clausewitz service. No HOI4 MCP inspection, native script validation, probability simulation, GUI render, installed vanilla lookup or live-game run was performed. Connected GitHub reads, local file inspection, primary-source web research and the actual collaboration agents supplied this package's evidence.

The following tool names come from current project instructions. They are intended implementation routes, subject to discovery of the live schema and server version. The map is not a fabricated execution log.

| Capability and intended tool | Exact question for Investment | Inputs and retained result | Safe fallback and limit |
|---|---|---|---|
| `hoi4.mod_index`, overview and next-ID modes | Which current IDs, namespaces, prefixes and layered definitions affect 121, legacy132 and The Pact? | Current mod roots, namespace/prefix, source revision. Retain candidate and all observed conflicts in `mcp_identity.md` | Targeted source search, workbook inspection and definition comparison. A next-ID result does not reserve an ID |
| `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup` | Which installed commands and modifiers implement factory holds, building legality, research bonuses, facility gates, dates and native missions? | Narrow symbol and scope queries, complete relevant definitions and known-mistake citations in `native_contract_evidence.md` | Offline repository snapshots and installed native docs where accessible. State unresolved semantics explicitly, never use a public wiki as the native authority |
| `hoi4.event_inspect`, targeted inventory or compare | Does the implemented graph include all proposal, phase, incident, evolution, service and terminal paths with the right actor? | Investment root and helper set at a recorded revision, preserved before/after graph where comparison matters | Trace actual source and call sites. Helper expansion requires confirmed version/schema support, not guessed async requests |
| `hoi4.script_validate` | Are changed effects and triggers valid in their actual country/state scopes, and what checks were actually performed? | Explicit changed-file paths or narrow scoped bodies. Retain `checksPerformed`, unresolved commands, known-mistake findings and source revision | Direct source checks and focused executable helper tests. A partial validator result does not prove parameter semantics or native behavior |
| `hoi4.probability_inspect` | What weights and draws actually control the eligible country pool, AI choices, checkpoints and evolution offers? | Real candidate pool and named scenario values from part 6. Retain raw scores, exact probabilities where supported and unresolved paths | Evaluate the actual weight order and normalize only true lotteries. Decision willingness is not a percentage |
| `hoi4.probability_analyze`, compare/sweep/simulate/sequence/render as justified | How do budget, war, Exposure, site count and operating mode change choices and cumulative risk? | A bounded representative scenario set, actual changed weights and model assumptions. Save comparisons in `probability_scenarios.md` | Reproducible analytical cases for explicit draws, qualified MTTH reasoning and scenario walkthroughs. Do not run broad simulations merely to collect a large pass count |
| `hoi4.map_inspect` with relevant layers, areas or overlays | Are candidate states, coastal provinces, supply endpoints and corridor edges legal and geographically coherent? | Actual selected IDs and bounded region, state/building/supply layers as supported | Inspect actual state/province definitions and route owners. No invented state IDs or map rewrite is required for script-only development |
| `hoi4.tech_inspect`, compare where relevant | Are the facility and research-bonus dependencies legal, and are the two capability modes exclusive? | Actual affected facility/project gates and bonus categories, current definitions, scoped comparison | Read installed technology and special-project definitions. Facility creation alone never proves project or payload completion |
| Native presentation inspection or rendering, after tool discovery | Do the ordinary category, cost colors, timers, report art and achievement states render correctly? | Representative funded, blocked, incident, critical-warning and terminal states, fixed resolution and UI scale | Source and asset checks with decoded images. Record rendering as unobserved if unavailable. Do not invent a GUI comparison tool or substitute a simulated screenshot |

For each unavailable, unsupported or inconclusive capability, allow the initial appropriate request and at most one meaningful corrected or narrower retry. Skip that retry when availability is already known to be absent. The limit follows the underlying failure across agents and files. Continue useful source-level work and report the specific remaining assurance gap.

Async helper expansion and job operations require confirmed server health, schema and task negotiation. Retain continuation references and final results if such a route is used. A started job is not completed evidence. Request native logs only when the user supplies them or explicitly requests that diagnostic work.

## 6. Required evidence and release honesty

The implementation report should distinguish five types of evidence.

1. **Source fact.** A specific file and revision establish an API, caller allowlist, output key or registry.
2. **Implemented behavior.** Changed source contains a complete route and its owner contracts.
3. **Analytical result.** Exact arithmetic or a source model establishes a bounded fact under stated assumptions.
4. **Tool observation.** A real inspector, validator, renderer or analyzer returns a result whose coverage is preserved.
5. **Native observation.** A real game session demonstrates behavior in a stated version, scenario and capability set.

This planning package provides source facts, authored design and limited analytical checks. It does not provide implemented or native gameplay evidence. The user owns live-game testing under the current project rules. Do not request a screenshot, launch a game by default or wait for a live test as a planning completion gate.

For implementation, test the actual selector, quote, reserve, phase receipt, delivery, refund, closure and handoff helpers. Mock native primitives only where necessary and label those tests as source tests. A no-op substitute for the owner helper under test is not meaningful verification.

Known defects must be corrected. Missing optional evidence must be described. Those are different situations. A source implementation can be handed off with an honest unobserved native behavior, while an identified duplicate reward, negative resource balance or stale callback still needs repair.

## 7. Final integration checklist

| Area | Completion condition |
|---|---|
| Brief fidelity | One country including viable AI minors, four sectors, paid construction, overruns/corruption/abandonment, both requested evolutions |
| Funding | Exact inclusive affordability, owned integer hold, actual funded work, no fake treasury and no second payment at completion |
| Delivery | All agreed native outputs or explicitly accepted alternatives, real legal placement, partial results and one-time receipts |
| UI | Two persistent values, bounded actions and missions, current costs and statuses while paused, complete unavailable reasons |
| Ownership | Capture, transfer, annexation, stale callbacks, inherited service and slot loss follow the same declared contracts |
| Evolutions | Both active and pre-fire entries, disabled-setting behavior, finite anomaly operation and no unlock Chaos |
| Failure | Finite ordinary exits, real national failure criteria, explicit Event 35 caller, no duplicate crisis or leaked hold |
| AI | Legal affordable choices for small/large, wartime/peacetime and all-DLC/no-DLC fixtures, no willingness-as-probability claim |
| Presentation | All declared consumers have verified unique sprites, final localisation and achievement states |
| Records | Accurate history actor, source-owned Chaos and deaths, durable achievement proofs and protected catalog migration |
| Review | Material findings fixed, representative recheck complete, remaining evidence limits explicit |

The final handoff prompts are [coding](121_investment_coding_prompt.md), [decisions and missions](121_investment_decision_mission_prompt.md), [assets](121_investment_asset_prompt.md), [achievements](121_investment_achievement_prompt.md) and [goal](121_investment_goal_prompt.md). They must be used with the full specifications.
