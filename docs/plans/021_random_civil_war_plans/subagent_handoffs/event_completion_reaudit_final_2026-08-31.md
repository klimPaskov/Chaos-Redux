# Event 021 Random Civil War — Final Completion Re-audit

Date: 2026-08-31

Audit mode: read-only completion re-audit

Scope: Event 021 Random Civil War, its Event 006 integration surfaces, accepted Event 021 plans and handoffs, documentation/catalog evidence, visual assets, decisions and missions, AI/probability surfaces, and completion gates.

## Final verdict

**Status: incomplete; completion claim is not authorized.**

The current source contains the requested post-creation actor-force receipt machinery, including actual actor division, manpower, and equipment-band capture; pending-ratio consumption and cleanup; last-log receipt fields; and aligned immutable history arrays. However, one demonstrated current source defect remains in the Event 006 adapter path: it records the same opening twice, first from the host and then from the actor. Because the actual receipt variables are actor-scoped, the host-side immutable row carries zero/default actor-force receipt values while the actor-side call appends a second row containing the actual values. This violates the single immutable opening-record requirement and leaves Event 006 receipt history internally inconsistent.

Event 021 correctly remains unavailable pending certification, and it does not own or introduce a custom scripted GUI. No Event 021 UI-worker handoff is required for the shared event log, shared event-details framework, ordinary event windows, or decision category.

Live HOI4 validation remains user-owned. Its absence is not classified as a source defect, but it remains an acceptance blocker wherever the specification requires runtime evidence.

## Audit basis and limits

The audit reviewed the repository instructions, the complete Event 021 event and subagent skills, the improvement-loop, event-planning, event-assets, and decision/mission guidance available before traversal was stopped. It also reviewed the complete Event 021 specification set, all Event 021 prompts/specification materials, the overview and acceptance-evidence documents, existing Event 021 plans and handoffs, the current Event 021 implementation and relevant Event 006 registry/adapter surfaces, the required offline wiki references, and relevant installed-vanilla documentation.

At the user’s instruction, further broad traversal stopped after the defect and evidence below had been established. Requirements not already proven by the gathered evidence remain explicitly blocked or unverified rather than being inferred complete.

## Completion status by surface

| Surface | Status | Audit conclusion |
| --- | --- | --- |
| Availability/certification gate | Source-proven | Event 021 remains disabled until the readiness flag is explicitly certified. |
| Dedicated custom GUI | Correctly absent | Event 021 owns no custom `.gui` mechanic window; no event UI-worker obligation is triggered. |
| Core event chain and six actor routes | Source-present; runtime blocked | Event chain and route structures are present, but MCP helper/lifecycle projections and live execution are not complete. |
| Dynamic territory/remnant/capital/force logic | Source-present; runtime blocked | Dynamic source systems are present; live topology and transfer fixtures remain user-owned acceptance work. |
| Post-creation actor-force receipts | Partial; source defect | Ordinary and secondary civil-war paths capture actual actor receipts, but the Event 006 adapter writes duplicate/inconsistent immutable opening rows. |
| Immutable log history and cleanup | Partial | Arrays, snapshot fields, pending-ratio cleanup, and receipt cleanup exist; Event 006 duplicate append prevents certification. |
| Event 006 complete-human-package adapter | Source-present; runtime blocked | Registry and anchor/carrier crosswalk cover 32 admitted packages in source; live package-matrix proof remains absent. |
| Evolutions I–III and scheduler | Source-present; runtime blocked | Source structures exist; bounded scheduling and route outcomes still require the specified runtime fixtures. |
| Scenario SCN-018 and weighted surfaces | Blocked | Source includes weighted selection/scenario machinery, but the required current-revision probability evidence matrix was not completed in this audit. |
| Decisions and missions | Source-present; evidence incomplete | Event 021 decision and mission definitions are present; current-revision specialist/runtime acceptance remains incomplete. |
| Achievements, logs, and details | Source-present; runtime blocked | Source consumers are present; live shared-log/detail rendering and immutable-history behavior remain unproven. |
| Localisation | Source-present; evidence incomplete | Localisation surfaces were inspected, but this audit does not possess a fresh complete current-revision localisation-specialist result. |
| Visual assets | Source-present; user acceptance blocked | The inspected handoff reports 40 wired texture references resolving; live consumer review remains user-owned. |
| Documentation and catalog/workbook | Partial/evidence incomplete | Overview, acceptance evidence, plans, and handoffs exist. A fresh final workbook/export parity proof was not completed before traversal stopped. |
| MCP event inspection/rendering | Partial/tool blocked | Both chains were inspected and rendered, but the server deferred helper/lifecycle projections. |
| MCP revision comparison | Tool blocked | The requested prior revision was not available in the MCP cache. |
| Live HOI4 acceptance | User-owned blocker | Agents cannot launch HOI4; required runtime fixtures and visual acceptance remain outstanding. |

## Implemented and source-proven requirements

### Certification gate and UI ownership

- `common/scripted_effects/021_random_civil_war_parent_effects.txt` initializes the Event 021 runtime without granting `random_civil_war_rework_ready`.
- The shared default-reworked allowlist does not admit Event 021, and Event 021 trigger paths require the readiness gate.
- Therefore Event 021 is source-proven unavailable until an explicit certification action enables it.
- No Event 021-owned scripted GUI file or dedicated mechanic window was found. Event 021 uses ordinary event, decision, shared log, and shared details consumers. The specification’s “must not own a custom GUI” constraint is satisfied in source.

### Post-creation force receipt implementation

The latest owner patch is materially present in `common/scripted_effects/021_random_civil_war_parent_effects.txt`:

- `event021_parent_prepare_start_ratios` (approximately lines 1558–1590) copies the resolved opening/army/navy/air ratios into pending transaction variables before actor creation.
- `event021_parent_capture_actual_actor_force_receipt` (approximately lines 1592–1612) captures the created actor’s `num_divisions`, manpower, and an equipment-availability band based on infantry, support, and artillery availability.
- The pending primary and secondary ratio variables are cleared by the transaction cleanup helper (approximately lines 1614–1625).
- The current/last log snapshot contains actor division and manpower receipt fields (approximately lines 1629–1666).
- The immutable aligned log arrays append equipment band, actual actor divisions, and actual actor manpower (approximately lines 1668–1710).
- `event021_parent_record_system_log` builds one snapshot and appends one immutable history row per invocation (append at approximately lines 1832–1833).
- The normal primary path captures the actual actor receipt after actor creation and before logging (approximately lines 1879–2003, with capture around line 1992 and one log call around line 1994).
- The secondary actor path follows the same ordering (approximately lines 2010–2090, with capture around line 2065 and one log call around line 2067).
- The ordinary `start_civil_war` branches consume prepared ratios through their dynamic start effect and clear the transaction after the call (approximately lines 2419–2523).
- Core Event 021 cleanup removes the actual actor receipt variables in `common/scripted_effects/021_random_civil_war_effects.txt` (approximately lines 2128–2130).

This proves that the owner patch was not merely documented: the receipt fields, pending-ratio consumers, immutable arrays, and cleanup are implemented. It does not overcome the Event 006 defect described below.

### Event 006 adapter registry

- `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt` contains the admitted package/tag mapping and release behavior for 32 human-package identifiers.
- `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt` contains the corresponding anchor/carrier registry rows.
- The source therefore supersedes the earlier narrow/Scotland-only adapter condition described in historical handoffs.
- Completeness in source does not substitute for the specification’s live matrix across all admitted packages.

### Other implementation surfaces established by source review

- The Event 021 event file contains the root chain and supporting event IDs, including the ordinary chain, route/evolution events, and news consumers.
- The source contains the six actor-route structures, State Authority and hidden Fracture Pressure systems, dynamic target selection, weighted pools, settlement topology including partition/merger outcomes, evolutions, decisions, missions, achievements, logs, shared details hooks, ideas/modifiers, AI strategy integration, scripted localisation, and GFX registrations.
- Three mission definitions with distinct targets and success/failure handling were identified.
- Current source contains the widened Event 006 package registry and dynamic weighted target pool that supersede corresponding historical audit defects.
- Existing asset evidence reports that all 40 Event 021 GFX texture references resolve to files.

These are source-presence findings. They are not promoted to runtime acceptance where the specification requires MCP or live-game evidence.

## Demonstrated current source defect

### Event 006 adapter appends two opening rows, one with zero actor-force receipts

File: `common/scripted_effects/021_random_civil_war_parent_effects.txt`

Relevant helper and call flow:

1. The Event 006 actor is created and the actual receipt is captured in actor scope at approximately line 2797 by `event021_parent_capture_actual_actor_force_receipt`.
2. The adapter then enters host scope and calls `event021_parent_record_system_log` at approximately lines 2813–2815.
3. It then enters actor scope and calls `event021_parent_record_system_log` a second time at approximately lines 2817–2818.
4. `event021_parent_record_system_log` copies the actual actor-force values only from its current scope at approximately lines 1768–1770.
5. Each invocation appends exactly one immutable snapshot/history row at approximately lines 1832–1833.

Consequences:

- The host-side call cannot read the actual receipt variables captured on the actor, so its appended row receives zero/default actor divisions, actor manpower, and equipment band.
- The actor-side call appends a second row for the same opening with the actual actor-force values.
- The same Event 006 opening is therefore represented twice in immutable history, and the aligned history contains one false zero-receipt row.
- Mirroring the last snapshot to both parties does not justify or repair the duplicate immutable append; the ordinary and secondary Event 021 creation paths each record once.

Required owner correction: make the Event 006 adapter construct and append the opening once from the actor scope, while relying on the existing snapshot-mirroring behavior (or an equivalent single-writer design) to expose the result to the host. This audit is read-only and did not modify the source.

This is a completion-blocking source defect because the accepted P0.3 receipt requirement explicitly requires post-creation actual receipts in durable immutable opening evidence, including Event 006 integration.

### Additional source risk, not promoted to a demonstrated runtime defect

`event021_parent_capture_actual_actor_force_receipt` stores the `manpower` dynamic variable. Installed vanilla documentation marks that dynamic variable deprecated and warns that it may overflow, recommending the safer manpower representation where appropriate. The audit did not obtain runtime evidence of overflow in Event 021, so this is recorded as a technical risk rather than a second demonstrated defect. The owner should confirm that the selected representation is safe for the full supported country/manpower range before certification.

## Accepted-plan disposition

### Implemented or materially promoted

- Dynamic weighted target selection is present, superseding the historical unweighted-target defect.
- The complete 32-package Event 006 adapter registry and its anchor/carrier mappings are present, superseding the historical Scotland-only integration defect.
- Settlement topology includes partition/merger and successor handling, superseding the historical incomplete selector disposition.
- Distinct mission target/outcome structures are present.
- The P0.3 post-creation force-receipt design is materially implemented across primary, secondary, and Event 006 creation paths, with pending transactions, actual actor measurements, immutable arrays, and cleanup.
- Asset/GFX wiring and the expanded Event 021 documentation/handoff set are present.

### Partially implemented or not accepted as closed

- P0.3 remains partial because the Event 006 path double-appends the opening and produces one false zero-receipt immutable row.
- P0.2/current-revision weighted probability proof remains open because the required full named scenario evidence was not returned during this audit.
- P0.4/Event 006 package integration is source-present but lacks the required live package matrix.
- Asset completion remains pending live consumer review and eventual cleanup/promotion of temporary asset workspace material at final certification.
- Documentation/catalog closure remains pending fresh final workbook/export parity evidence.

Historical handoffs were treated as evidence of prior work and issue disposition, not as proof that the current revision passes runtime acceptance. Where current source contradicted an old defect, the current source was controlling. Where a handoff claimed completion without current required MCP or live evidence, the claim was not promoted.

## Mandatory HOI4 MCP evidence and tooling blockers

### Fresh event inspection

Both in-scope chains were sent through the mandatory read-only event inspector with helper tracing enabled:

- Event 021 root: `chaosx.nr21.1`
- Event 006 root: `chaosx.nr6.1`
- MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`
- Current MCP revision: `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`
- Graph hash: `e6c16ff...`

Both calls returned `EVENT_INSPECTED_PARTIAL`. The server deferred large-workspace helper/lifecycle projections, returned a helper count of zero, and emitted a blocking workspace diagnostic. Source review was used to identify the defect above, but is not treated as equivalent MCP lifecycle evidence.

Event 021 trace artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48d5fa89daa6ab4bfb34897ee6aaad442d4c1afb2f353f750e7690f78d1b3810/dbcf8f77c87a7ed7d96612146425f99fb524095646ce3874d2a7aca620c1cded/event-trace-2725045f62d1.json`

Event 006 trace artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/769c14dcc787df7d826a0cd5877daa90adcee7d61ddf66e533524f8d4ee51dcd/5320f101589e4f928e11b32065805fd12d32750274aa39cf332c46dcc9452345/event-trace-2725045f62d1.json`

### Fresh event rendering

The first request used `maxNodes = 500` and was rejected because the route accepts at most 240. It was retried at 240.

Both roots returned `EVENT_RENDERED_PARTIAL` because helper projection remained deferred.

Event 021 rendering selected two nodes and produced:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7fd.../0677.../event-overview-2725045f62d1-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0c6.../1a10.../event-overview-2725045f62d1.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/829d.../7e60...svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca00.../42df...png`
- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d902.../6262...html`

Event 006 rendering selected five nodes and produced:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06d525.../a563.../event-overview-2725045f62d1-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10b7.../f027.../event-overview-2725045f62d1.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbad.../a5cd...svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4533.../5ba...png`
- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0067.../56c...html`

The abbreviated artifact segments above reproduce the identifiers returned by the MCP calls available to this audit. They prove the routes were invoked, but the partial renders do not prove the full helper/lifecycle chain.

### Revision comparison

`hoi4.event_compare` was requested between the prior handoff revision `cfdc65be2a281cc4ef468a2feb63ec37cf7111f783c5e240480e4ef2b0351a3b` and current revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`.

The tool returned `EVENT_REVISION_NOT_CACHED` and produced no comparison artifact. A Git/source diff is not substituted for the missing mandatory MCP comparison.

### Weighted probability evidence

The required weighted pass was routed to `chaosx_ai_probability_auditor` for the named Event 021 surfaces and scenarios. No completed current-revision specialist result was available when the user ordered traversal stopped and the report written immediately. Consequently this audit does not certify TGT, ARC, SEV, EVO, FRT, SPN, STR, SET, REC, GLB, CLU, or SCN probability behavior, decision/mission AI scores, random lists, strategy factors, sweeps, seeded simulations, sequence analyses, or before/after probability comparisons.

This is a tooling/evidence blocker, not by itself a demonstrated source defect. It remains an acceptance blocker because the specification and repository workflow require current-revision probability evidence for every weighted surface.

## User-owned live validation

Agents must not launch Hearts of Iron IV. The following evidence therefore remains user-owned and blocks acceptance where required by the specification:

- Fresh-game confirmation that Event 021 is unavailable before certification and becomes available only through the intended certification mechanism.
- All six actor routes, including ordinary, secondary, and Event 006-triggered openings.
- Post-creation division, manpower, and equipment-band receipt values for every creation path, plus proof that each opening produces exactly one immutable history row.
- Rollback/failure paths and cleanup of pending ratios, actual receipt variables, targets, and partial actors.
- Dynamic connected-territory, remnant, capital, settlement, partition, merger, and successor fixtures.
- Low/medium/high SCN-018 share behavior and maximum/all-eligible normal-human behavior.
- All admitted Event 006 human packages, including anchor/carrier resolution and actor creation.
- Evolutions I–III, bounded scheduling, recurrence, and terminal outcomes.
- Decision and mission availability, timers, success/failure transitions, effects, AI behavior, and tooltips.
- Shared event-log and event-details rendering, actor/host mappings, immutable history navigation, and receipt displays.
- Achievement triggers and persistence.
- Localisation rendering, dynamic names, overflow/clipping, and missing-key checks in actual consumers.
- Visual review of event pictures, decision/category icons, achievement art, and every Event 021 GFX consumer at supported resolutions.

Unavailable live evidence must not be described as a source defect. It remains an acceptance blocker because the Event 021 specification expressly requires live proof and repository policy reserves live execution to the user.

## Simplifications, fallbacks, and omissions

### Demonstrated current simplification/fallback status

- No Event 021-owned custom GUI was introduced. This is a required design constraint, not an omission or fallback.
- No character portrait, custom 3D unit, unit-audio package, bespoke map counter, frame animation, super-event, technology tree, doctrine tree, or event-owned scripted GUI was established as part of Event 021’s required current implementation surface. Their specialized handoffs are therefore not demanded by this audit.
- The current source includes dynamic target selection, full Event 006 registry breadth, settlement topology, distinct missions, route/evolution structures, and actual actor receipt fields; the historical narrow substitutes for those surfaces are not treated as current fallbacks.

### Unresolved omissions or weaker evidence

- The Event 006 receipt path’s duplicate append is not an acceptable simplification; it is a source defect.
- Full current-revision probability evidence is missing.
- Full MCP helper/lifecycle projection and revision comparison are missing due to tool responses.
- Fresh final workbook/export parity, localisation-specialist, decision/mission-specialist, country-package-specialist, and live visual/runtime acceptance evidence were not completed in this audit.
- Temporary asset workspace material should remain pending until durable facts are promoted and final certification permits cleanup; its present retention is not classified as a source defect while the event remains incomplete.

No other current source simplification was demonstrated by the evidence gathered before traversal stopped. This statement does not convert unverified requirements into completed requirements.

## Documentation and asset gaps

- `docs/events/021_random_civil_war/overview.md` and `docs/events/021_random_civil_war/acceptance_evidence.md` exist and already frame certification/live-proof boundaries.
- The plan/handoff directory contains implementation, improvement-loop, probability, completion, localisation, asset, icon, spreadsheet, documentation, and scripted-system handoffs. Historical claims were dispositioned against current source rather than accepted at face value.
- Existing asset evidence says all 40 GFX texture references resolve, but final in-consumer visual acceptance remains user-owned.
- The audit did not complete a fresh read-only open/row/export parity check of `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its generated CSV exports after the user stopped traversal. Catalog parity therefore remains evidence-incomplete.
- Documentation must not state final completion while the Event 006 duplicate-log defect and required evidence gates remain open.

## Required next actions

1. Owner: correct the Event 006 adapter so one opening produces exactly one immutable log/history append from the scope that owns the actual actor-force receipt.
2. Owner: assess the deprecated/overflow-prone `manpower` dynamic-variable use and choose a representation proven safe for all supported receipt ranges.
3. Auditor: rerun focused source inspection of the corrected Event 006 call flow and verify aligned-array write cardinality and cleanup.
4. MCP: rerun `hoi4.event_inspect` and `hoi4.event_render` for `chaosx.nr21.1` and `chaosx.nr6.1` when helper/lifecycle projection is callable.
5. MCP: rerun `hoi4.event_compare` with both revisions resident in the MCP cache.
6. Probability auditor: complete the full current-revision named scenario matrix and required compare evidence for every weighted surface.
7. Specialist/read-only audits: complete current decision/mission, country-package, localisation, workbook/export, and asset-consumer evidence where not already current.
8. User: perform the specification’s live HOI4 route, receipt, rollback, topology, scenario, package, evolution, UI/log/details, localisation, achievement, and visual fixtures.
9. Certifier: only after the source defect is fixed and all required evidence passes, authorize the readiness gate. Until then Event 021 must remain unavailable.

## Completion authorization

**Not authorized.**

The Event 006 duplicate immutable-log defect is a demonstrated current source blocker. Independently, mandatory MCP helper/lifecycle evidence, MCP revision comparison, current weighted-probability evidence, selected specialist/catalog evidence, and user-owned live acceptance remain incomplete. The live/tooling gaps are not source defects, but the specification makes them acceptance blockers. Event 021 must remain unavailable and no completion or certification claim should be made.
