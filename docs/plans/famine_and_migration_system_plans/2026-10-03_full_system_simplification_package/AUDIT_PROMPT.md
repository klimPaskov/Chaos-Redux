# Future whole-system audit prompt

This prompt is dormant documentation.
Run it only when a human explicitly requests this audit in a later task.
The present planning chat will not launch or implement it later.

---

Audit the entire Chaos Redux famine and migration system against current source and the planning package at `docs/plans/famine_and_migration_system_plans/2026-10-03_full_system_simplification_package/`.
Work in `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux` using Windows-native paths.
Read AGENTS.md before work.
This is a read-only gameplay audit; write reports to a dated `audit_runs` child of the package, and do not patch source, assets, specs, workbook, CSV exports, stage, commit, schedule or create an implementation goal.
You are not alone in the codebase; preserve other agents' changes.

Read every package file, especially WHOLE_SYSTEM_AUDIT.md, IMPROVEMENT_PLAN.md, IMPLEMENTATION_AND_ACCEPTANCE.md, EVIDENCE_AND_RESEARCH.md and EVIDENCE_PROBABILITY.md.
Read current `.agents/skills/chaos-redux-improvement-loop/SKILL.md`, `chaos-redux-event-planning/SKILL.md`, `chaos-redux-decisions-missions/SKILL.md`, `chaos-redux-subagents/SKILL.md`, `chaos-redux-state-ledgers/SKILL.md`, `chaos-redux-scripted-gui/SKILL.md`, relevant event integration/localisation guidance and asset coverage guidance.
Read `docs/systems/famine_system.md`, `migration_system.md`, `civilian_transfer_system.md`; current `source_of_truth_map.md`, `completion_report.md`, `handoff_dispositions.md`, `ai_probability_current.md` and improvement review under `docs/plans/famine_and_migration_system_plans/`.
Read all eight specs and supporting decision, profile, integration, Deaths, probability, asset and implementation maps in `docs/specs/famine_and_migration_system_specs/`.
Treat approval decisions, accepted design, executable facts, historical handoffs and unresolved proposals separately.
Dates, spec paths and implementation do not establish approval.

Preserve the accepted boundaries: independent famine/migration namespaces, categories and mapmodes; exact causal owner adapters; one neutral civilian-transfer primitive; population conservation; one Deaths owner; no incident event layer, replacement Event 149 or recurring worldwide scan.
A fresh audit does not authorize expansion, a new GUI, countries, focuses, formables, technology, models or administrative meters.

Freeze current working-file hashes and HEAD before conclusions.
Inventory and trace current famine/migration/civilian-transfer/humanitarian constants, effects, triggers and their paired docs, both decision sources/categories, sparse runtime callbacks, mapmodes/projections, report windows and attachments, dynamic modifiers, localisation/cost selectors, CXT extensions, achievements, and external owner callers.
Use the touchpoint map as a starting list, then find current definitions/callers instead of trusting historical counts.
Inspect actual external adapters for disasters, outbreak, fallout, CBRN occupation, camps/gulags/custody/genocide, occupation, bombing, war/peace, events/clusters/scenarios, and Gods of Africa service install/cleanup.
Classify each integration as implemented with complete proof, called but rejected/incomplete proof, API-only, absent owner, accepted/queued, or unresolved.
Do not fabricate receipts from date, metadata, ideology, total state population, reserve units, or direct deaths.

Investigate A01–A12 directly, with exact source citations and current hashes.
In particular verify proof-one production against strict greater-than-one service setters; the food formula's reachable domain and catastrophe condition; projection clearing versus physical rail repair; land imports charging convoys; reserve release's delay and marginal benefit; country-wide pending-offer/phase suppression; integration at activation versus advertised duration; actual differences between worker and vulnerable evacuation; and all delayed no-service/refund paths.
If any finding was fixed since planning, mark it superseded with its current evidence rather than repeating it.

Audit the player loop over time, not just row counts.
For S01–S22 record current values, cause/recovery communication, every visible action instance per target, payments/commitments, first useful result, total strategic interventions per 60-day crisis, physical objectives, route alternatives, durable outcomes and lingering obligations.
Assess three canonical values per mechanic, three-to-five normal actions with six maximum per selected case, one-to-three urgent subjects, maximum four spendable types and three inline cost values.
Check native rows/tooltips rather than declaring compliance from localisation length alone.
Parallel crises must be permitted when real national resources allow them; concise presentation is not a runtime country lock.

Trace physical population, route-death slices, survivor credit, state/country reception deltas, cohort/history/progress, custody and terminal statuses separately.
Inspect aligned arrays and monotonic identity, exact current-host selection, partial destination credit, rollback/inverse quarantine, protected floor, actor/controller change, annexation, ambiguous co-located rows, A→B→A cycling, reload replay, simultaneous terminal claims, and reward farming.
Confirm independent retirement and no hidden generation reset or population credit from integration/reports/policy.
Report proof and failure injection needed where source cannot settle engine behavior.

Start every weighted/timing audit with `hoi4.probability_inspect` and route it through `chaosx_ai_probability_auditor` with a complete self-contained prompt, `fork_turns="none"`, explicit read-only ownership, current paths, named scenarios and report destination.
Cover decision/mission scores, destination/donor/opposition custom pools and corridor response scoring.
Record complete pools/external factors and distinguish exact, bounded, sampled, score-only and unresolved results.
Use evaluate/sweep/simulation/sequence/render only where semantics and live schema support the question.
This read-only audit makes no weight changes; the report must specify an owner-applied patch and same-scenario `hoi4.probability_compare` gate for any later change.
Do not normalize willingness scores into probabilities or force deterministic cleanup into a random pool.

Discover live MCP schemas and check response/version/health separately from tool exposure.
Use `hoi4.reference_context`, reference_search/read and source_lookup for relevant offline wiki, installed documentation and exact vanilla precedents, retaining path/line/revision.
Do not browse the Paradox wiki on the web.
If a route does not respond in a bounded wait, record the exact call/error/elapsed limit, stop repeated long retries, read pertinent local sources, and leave the affected engine conclusion unresolved.
The 2026-10-03 non-returning requests are historical route gaps, not proof of current health.
Do not use rewrite tools or unconfirmed helper expansion/jobs/native tasks.

Use decision inspection for gate/payment/lifecycle scenarios; GUI inspect/render for both actual report windows and supported native decision consumer; map inspect/render for exact state/province/port/rail/supply/adjacency substrate; narrow external-event inspect/render/compare for changed owner boundaries.
Preserve all artifacts, source/scenario identities, fixture assumptions and unresolved fidelity.
Render 1920×1080 and 2560×1440, both UI scale 1.0; 1280×720 is an optional stress case.
Inspect longest titles/costs, empty/full lists, disabled/hover/active/warning/terminal states, attachments, pictures and click regions.
Action/value budgets are design and readability targets, not HOI4 engine row limits; native capacity or clipping claims require actual consumer evidence.
Map substrate renders do not prove scripted mapmode execution or privacy.
Only if an actual technology/doctrine touchpoint enters accepted scope, verify standalone Technology Tree Viewer separately from tech route exposure/service health and record its absence without inventing capabilities.
Agents do not launch HOI4; user-supplied runtime/save evidence can supplement supported source/MCP proof through `chaos-redux-save-inspection`.

Verify assets by requirement→source/provenance→actual DDS→sprite→consumer→state, not the old total of 61.
Verify all eight achievement routes and their repeat/negative predicates after current action changes.
Audit current system/event documentation and catalog alignment; workbook is authoritative and catalog CSVs are exports only.
Do not edit them during this audit.
Research missing historical/regional claims through primary or institutional sources, separating actual documents read from catalog descriptions, uncertain analogies and factual chronology.

Return a concise verdict with a traceable issue ledger, severity, affected source IDs, current versus proposed behavior, expected player benefit, evidence confidence, missing facts, dependency/owner, and disposition.
Write CURRENT_SOURCE_AUDIT.md, SCENARIO_AND_PAYMENT_MATRIX.md, INTEGRATION_AND_LEDGER_MATRIX.md, and MCP_EVIDENCE.md in the dated report directory, with the probability specialist handoff.
Each recommended change must remove work or create a meaningful strategic choice; state which buttons/values/timers it retires or replaces.
Distinguish fixable defects from unaccepted redesign and exact engine/tool blockers.
Recommend closure when only bounded repairs and validation remain; do not add another broad addendum while this package remains unresolved.
Finish with the evidence the future parent must obtain before implementation or completion claims, without claiming the existing system complete merely because sources parse.
