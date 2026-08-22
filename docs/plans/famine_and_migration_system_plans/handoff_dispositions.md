# Famine and Migration System Handoff Dispositions

This file records the parent review of every project-subagent handoff used to implement the shared famine and migration system.

## Repository exploration

Source: `docs/plans/famine_and_migration_system_plans/repo_exploration.md`

Disposition: partially accepted.

Accepted findings:

- Reuse `apply_exact_state_civilian_population_loss` and `apply_state_population_loss_without_recruitable_manpower_gain` from `common/scripted_effects/chaosx_dynamic_effects.txt`.
- Use the shared event-log, cluster, scenario, achievement-registry, scoped-hook, and workbook surfaces identified in the report.
- Treat Event 149 as absent source rather than an implemented event chain.
- Record the Event MCP large-workspace projection limitation as a validation blocker where it recurs.

Rejected or superseded findings:

- The Deaths owners are resolved as `common/script_constants/chaos_meter_constants.txt`, `common/scripted_effects/chaos_meter_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`, and `localisation/english/chaosx_chaos_meter_l_english.yml`.
- Air Cleanliness owners are resolved through `common/scripted_effects/fallout_consolidated_effects.txt` and its paired trigger/constants surfaces.
- Condemnation owners are resolved through `common/script_constants/condemnation_sanctions_constants.txt`, `common/scripted_effects/condemnation_sanctions_effects.txt`, and `common/scripted_triggers/condemnation_sanctions_triggers.txt`.
- Camp and genocide owners are resolved through `common/scripted_effects/camp_repression_rework_effects.txt`, `common/scripted_effects/genocide_crisis_effects.txt`, and their paired trigger and constants files.
- `chaosx_ai_probability_auditor` is callable in this runtime. The claimed tool blocker is rejected.
- Event 149 requires no additional design decision. The binding specification authorizes retirement and absorption, forbids a replacement event ID, and forbids an event-pacing weight.
- Missing roots 118, 120, and 131 are catalog/integration gaps, not permission to invent event sources. Event 013 remains the current volcano/disaster owner.

## Pre-change AI probability audit

Source: `docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md`

Disposition: accepted as a historical baseline and modified for the current ledger.

The audit proves that Event 149 and all shared famine/migration weighted surfaces were absent before implementation. All twenty named scenarios remain useful baseline cases, but this pre-change report is not current balance evidence. The same scenario IDs must be rerun through `hoi4.probability_compare` after a successful current inspection before balance or completion can be claimed.

## Map inspection

Source: HOI4 MCP artifact `map-inspect.de30e4f6849d41e0.json` for representative historical-profile states 7, 113, 195, 271, 295, 335, 671, and 935.

Disposition: accepted with an unrelated map-validation blocker.

The inspection resolved all eight requested state records and passed province definitions, bitmap geometry, state and strategic-region membership, adjacency, supply, and railway checks. The workspace-wide locator pass also reported pre-existing invalid floating-harbor/building positions in `map/buildings.txt`, with diagnostics truncated after 1,999 retained entries and 2,654 omitted errors. This system will not edit map geometry or claim that those unrelated locator errors are resolved.

A second bounded inspection covered the remaining historical-profile anchors in states 36, 47, 119, 186, 187, 192, 193, 202, 218, 221, 227, 233, 239, 430, 431, 432, 435, 550, 583, 589, 590, 607, 772, 842, 1051, and 1066. It returned `MAP_INSPECTED`, resolved all 26 records without unknown IDs or missing province geometry, and retained artifact `map-inspect.e20e71fb0b43c19c.json` with SHA-256 `517d53dcdb11e4db9ac8722363b2e469ee333728f267e81c71075a9e20d0d635`. The same unrelated `map/buildings.txt` diagnostic ceiling recurred and remains outside this system's map-neutral scope.

## Generated report art

Source: `docs/plans/famine_and_migration_system_plans/subagent_handoffs/generated_event_art.md`

Disposition: accepted.

All seven binding report-image subjects were delivered as distinct source PNG, processed PNG, and final DDS assets. Parent review of the contact sheet confirmed readable 210×176 compositions, period-appropriate treatment, distinct incident silhouettes, and no embedded text. The handoff records successful DDS round-trip inspection and stable proposed sprite identifiers. Current source has the package `.gfx` registrations, while gameplay/report consumers remain parent-owned and report-event consumer integration is still pending.

## Scripted-system architecture

Source: `docs/plans/famine_and_migration_system_plans/subagent_handoffs/scripted_system_architect.md`

Disposition: accepted after parent-requested corrections.

The reusable constants, bounded state/country registries, fail-closed pressure and route adapters, exact transfer contract, border/reception/return helpers, and cleanup contracts are accepted. Parent review caught and returned two correctness issues before acceptance: population measurements were changed from the unavailable `state_population` link to `state_population_k` multiplied by the shared people-per-thousand constant, and blockade proof was expanded to require explicit isolation, route-or-port disruption, and convoy-or-escort shortage. The transfer now validates one resolved route before debit, measures actual origin debit and destination credit, logs route deaths without a second population debit, and exposes a conservation residual. Current source contains the bounded stage processing, scheduled jobs, decisions, Deaths reason registration, adapters, and runtime seams described by the handoff, while owner-local cross-system wiring, weighted AI evidence, and parent runtime validation remain open and are not implied complete by this handoff.

## Icon and achievement-art package

Source: `docs/plans/famine_and_migration_system_plans/subagent_handoffs/icon_artist.md`

Disposition: accepted for all assigned surfaces, with the formerly separate Deaths-texticon follow-up now completed.

Parent review accepted the category icon, nine state/reception icons, ten decision icons, and all eight achievement triplets. The four source/processed/DDS contact sheets show distinct HOI4-readable silhouettes, real transparent padding, correct grayscale states, and canonical not-eligible overlays. The original icon handoff records 44 of 44 BGRA8 one-mip DDS round trips with zero pixel mismatch, and the completed Deaths follow-up adds two 18×18 BGRA8 one-mip texticons with zero round-trip mismatch. `fm_deaths_famine` and `fm_deaths_displacement` are now registered in `interface/chaosx_texticons.gfx` and consumed by the current Deaths cause localisation. The distinct opaque 114×101 `fm_pic_displacement` category picture was outside this handoff and is routed to generated art; it is not replaced by the 52×40 category icon.

The generated-art follow-up has since completed `fm_pic_displacement`. Parent visual review accepted its distinct 114×101 wartime railway reception scene, and the handoff records a byte-exact BGRA8 DDS round trip. `GFX_fm_pic_displacement` and the 44 original icon/achievement sprites are registered in the dedicated `interface/famine_and_migration_system.gfx`; the two Deaths texticons are registered in `interface/chaosx_texticons.gfx`; all seven report sprites are registered in `interface/famine_and_migration_system_event_pictures.gfx`.

## Curator reconciliation of every completed handoff

The table below gives one explicit current disposition for every completed famine and migration handoff available in the working tree.

| Handoff | Disposition | Reconciliation |
| --- | --- | --- |
| `docs/plans/famine_and_migration_system_plans/repo_exploration.md` | modified | Accepted the owner paths, reusable loss helpers, Event 149 absence, and MCP limitation; superseded its pre-implementation claim that shared contracts still required design decisions. |
| `docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md` | modified | Accepted it as a pre-change baseline; retained its 20 unresolved scenarios and queued the required post-change inspect/compare because the current evaluation timed out. |
| `docs/plans/famine_and_migration_system_plans/mapmode_validation.md` | modified | Accepted exact two-mapmode source and static asset evidence; retained the hardcoded GUI zero-element/render-timeout limitation and current map-inspect locator blocker. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/decision_mission_audit.md` | modified | Accepted 26 decisions, three missions, source wiring, and transaction evidence; superseded the old safe-resettlement bind risk with the current safe rebind contract and queued weighted scenario comparison. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/generated_event_art.md` | modified | Accepted the delivered seven report images and category picture; queued report registry and event-consumer ownership because source consumers are not identified. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/icon_artist.md` | modified | Accepted the original 44 icon/achievement package and the completed two-texticon Deaths follow-up; rejected the obsolete “not produced” interpretation and recorded current GFX/localisation wiring. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/localisation_auditor.md` | accepted | Accepted the complete key audit and BOM evidence; left planned report/profile consumers as queued because localisation availability does not prove a gameplay consumer. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/mapmode_icon_artist.md` | modified | Accepted the four dedicated mapmode DDS variants and current GFX registration; queued supported GUI/render evidence for the visual runtime gate. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/mapmode_repo_explorer.md` | modified | Accepted exact mapmode IDs, scopes, priority, and sparse-source findings; superseded its stale “no setters” finding with current reception/overcrowding/return projection setters. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/scripted_system_architect.md` | modified | Accepted the bounded registries, formulas, transfer conservation, profile matrix, and safe rebind implementation; Deaths ownership and current texticon/localisation wiring are documented, while owner adapters, weighted AI evidence, parent runtime, and live validation remain queued. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/skill_maintainer.md` | accepted | Accepted the reusable `chaos-redux-state-ledgers` skill and its UTF-8 validation; left explicit future owner-prompt routing as a parent decision. |

The old sections above remain as historical handoff evidence, while this table is the current documentation-curator disposition ledger.

The current decision-file MCP lint request used `hoi4.event_inspect` with `mode = lint`, selector `kind = file` and `sourcePath = common/decisions/famine_migration_decisions.txt`, `expandHelpers = true`, `maxNodes = 800`, `maxEdges = 1600`, and workspace `chaosx_redux`; it was accepted but timed out at 180 seconds without diagnostics. The earlier malformed selector response was a `-32602` request error and is not treated as substantive evidence.

No row above claims gameplay completion.

## Plan and report dispositions

| Plan or report | Disposition | Current status |
| --- | --- | --- |
| `docs/plans/famine_and_migration_system_plans/improvement_review_addendum.md` | queued | Closure remains deferred for FM-R1 owner adapters, FM-R2 report-picture carrier, FM-R3 achievement evidence, FM-R4 weighted balance, and FM-R6 visual evidence; FM-R5 Event 149 catalog alignment is resolved and FM-R7 documentation reconciliation is this handoff. The addendum forbids new mechanics, a third mapmode, and a replacement random-event ID. |
| `docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md` | modified | Retained as pre-change absence evidence; post-change 20-scenario inspection/evaluation/compare remains queued after the recorded timeout. |
| `docs/plans/famine_and_migration_system_plans/mapmode_validation.md` | modified | Retained exact-two-mapmode source and static asset evidence; GUI hardcoded-window artifact limitation remains queued for parent/runtime validation. |
| `docs/plans/famine_and_migration_system_plans/repo_exploration.md` | modified | Retained owner paths and MCP limitations; implementation now supersedes its pre-change “contracts absent” framing. |

The plan table is separate from the completed-handoff table because these files are working plans or reports rather than subagent handoffs.
