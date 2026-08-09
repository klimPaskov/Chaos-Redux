# Event 018 improvement-loop closure handoff

## Disposition

**Result: RF-018-01 through RF-018-08 are closed. No new depth addendum and no further improvement-loop planner run are required.**

This was the mandatory closure-only return requested by the implementation-depth addendum. The review inspected current gameplay, localisation, GFX registration, runtime assets, event documentation, source specifications, acceptance evidence, and the event catalog workbook. It did not rely on the addendum's stale implementation snapshot.

No gameplay, localisation, asset, or workbook file was changed by this planner. Documentation changes are limited to this handoff, the closure disposition in `018_resources_found_implementation_depth_addendum.md`, the clarified global chronology contract in source-spec Part 4, and the package manifest needed to keep those accepted specification promotions traceable.

The accepted static-proof mode recorded in `018_static_acceptance_report.md` remains the proof boundary. The user waived live engine and interactive campaign evidence for this completion pass, so deterministic definitions, exact fixtures, registered runtime files, and focused static audits close PG-01 through PG-06. This handoff does not invent live results.

## Required reference basis

The closure pass read and applied:

- the complete offline Paradox wiki core set required by `AGENTS.md`, plus the resource-system page;
- vanilla `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `dynamic_variables_documentation.md`, `script_concept_documentation.md`, and script-constant documentation;
- the complete `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-events`, and `chaos-redux-subagents` skills;
- the complete 26-file Event 018 specification package;
- every current Event 018 plan, implementation handoff, and audit under this plans folder;
- the current Event 018 gameplay, localisation, interface, asset-manifest, event-documentation, and workbook surfaces relevant to RF-018-01 through RF-018-08.

No web Paradox wiki material was used.

## RF-018-01 through RF-018-08 closure ledger

| Item | Final disposition | Current implementation evidence | Promotion or closure evidence |
| --- | --- | --- | --- |
| RF-018-01, cave opening strength | **Implemented and promoted** | `resources_found_strength` centralizes minimum 6, maximum 30, score cap 120, five score per division, and the 720-resource mandatory-package floor. `resources_found_calculate_cave_starting_strength` subtracts that floor before resource scoring, applies every recorded contributor and mitigation, clamps the result, converts it through `6 + floor(score / 5)`, copies the result to DHO, and `resources_found_cave_spawn_opening_allocation` spawns exactly that allocation. | Source-spec Part 4 points to the accepted formula. `matrices/tuning_and_balance_framework.md` records the exact equation, caps, bands, and deterministic regression fixture. `subagent_handoffs/rf_018_01_cave_strength_recalibration_handoff.md` records the boundary profiles. |
| RF-018-02, controlled denial | **Implemented and promoted** | `resources_found_prepare_cave_resource_denial` applies the visible denied-resource modifier and stores a centralized three-capacity penalty. Every anchor attempt adds the centralized 30-day denial delay while the preparation remains active. Interrupted attempts leave it prepared. A successful activation subtracts three, clamps at zero, then consumes the penalty and flags. Liberation and defeat cleanup remove the denial identity. | Source-spec Part 5 records the exact delayed, one-shot, zero-clamped contract. The decision/mission audit confirms the action remains available for positive-capacity states instead of becoming an accidental total exclusion. |
| RF-018-03, DHO focus rewards | **Implemented and promoted** | The five doctrine focus completions call substantive helpers. Interlocking Carapaces and Great-Gun Resistance swap one cumulative Stone spirit with defense, cohesion, speed, and supply tradeoffs and target strongpoints. Urban Cellar Networks swaps the Burrow spirit, selects a transport objective, and applies the bounded infiltration package. Split Great Broods and Lighter Plates swap cumulative Scree spirits, alter spawn pacing or preference, and trade defense/cohesion/supply for speed. Route target flags are consumed by `front_unit_request` plus route-specific `front_control` strategies. Count Every Vein accelerates replacement broods after exact capacity recalculation. Chamber Autonomy reduces non-origin activation time and prefers frontier anchors while extending anchor grace. The former no-op template-refresh helper is absent. | Source-spec Part 6 records one cumulative spirit per doctrine route and the implemented map, spawn, hierarchy, and AI consumers. The earlier 65-focus audits remain historical evidence; `subagent_handoffs/final_focus_audit_2026-08-09.md` identified the two strict hierarchy gaps, and the later 67-focus MCP/current-source audit closes them. |
| RF-018-04, shared evolution chronology | **Implemented and promoted** | The four `resources_found_record_evolution_*_from_field` wrappers each have a distinct global `resources_found_evolution_*_chronology_recorded` guard. The first qualifying field supplies the logged stage, actor, and state. Later field progression continues through its own physical flags and events without appending another shared row. | Source-spec Part 4 now states exactly one shared Event Details row per event-wide tier while preserving later fields' local history. The implementation-depth addendum and static acceptance report record the same disposition. |
| RF-018-05, defeat severity and reconstruction | **Implemented and promoted** | `resources_found_classify_defeat_scale` accepts Event 018 world-end history, a created cross-continent foothold, or complete origin-continent consumption sustained for at least 365 days. The 75-percent milestone is not read by the classifier. Another active world end blocks the classification unless it is Event 018's own terminal identity. Reconstruction readiness requires global eligibility, contributor evidence, three personal cleanup contributions, no remaining cleanup state, and no live cave threat. Event `.99` sets its presented flag immediately, offers mutually exclusive join/lead/refuse commitments, and the later project completes the chosen commitment without firing `.99` again. | Source-spec Part 7 records the exact classifier and one-time reconstruction lifecycle. The decision audit and static acceptance truth table cover regional, 75-percent, full-continent, foothold/world-end, incompatible-terminal, and reconstruction branches. |
| RF-018-06, rendered decision and mission text | **Implemented and source-spec aligned** | A current-source audit finds 134 decision/mission identifiers: 125 rendered identifiers with both name and description localisation, plus the nine intentionally hidden four-gate scheduler missions. All referenced `custom_effect_tooltip` keys resolve, with no duplicate localisation key, and the localisation retains the required UTF-8 BOM. | Source-spec Part 8 and the acceptance matrix already carry the governing writing and localisation requirements, so implementation introduced no new design rule to promote. The earlier localisation and decision handoffs remain historical family-by-family reviews; the final completion audit owns the post-repair count. |
| RF-018-07, icon and UI asset package | **Implemented and source-spec aligned** | The package resolves 67 focus sprites, 36 unique idea/state sprites, 39 decision-family sprites across 125 visible icon lines, five category icons, and five category pictures. The permanent asset record preserves the original 150-row source/processed/runtime audit plus the two later focus-icon round-trip records. `interface/chaosx_achievements.gfx` registers 15 complete achievement triplets and all 45 files exist. Five real-frame selected-field animations are registered at 10, 10, 12, 12, and 12 frames, with matching 128-pixel frame widths, static fallbacks, Suspended, and a live exact-seal Closed history identity. | Source-spec Part 8 and the acceptance matrix already require the completed asset families and achievement triplets. `docs/events/018_resources_found/assets.md` is the durable inventory after temporary-workspace cleanup. `subagent_handoffs/asset_audio_reaudit_handoff.md`, `icon_provenance_repair_handoff.md`, `event018_two_focus_icons_2026-08-09.md`, `field_gui_animation_handoff.md`, and `event018_scripted_gui_visual_fix_handoff.md` retain the detailed production and review evidence. |
| RF-018-08, workbook and documentation alignment | **Implemented and source-spec aligned** | `Events!A19:M19` records Event 18 as `Resources Found`, four localized evolutions, intentional blank Evo V, the localized world-end scenario, `Minor Repeatable`, cluster 7, `Medium`, and `Implemented`. `Clusters!A10:G10` records `Economy (pos)`, member 18, chaos level 1, and `Implemented`. The player-facing details, evolution title/body pairs, world-end title/body, and cluster description match their live localisation keys. The workbook has five expected sheets, no formulas, and no stored formula-error values. | Source-spec Part 1 and the acceptance matrix already define the event identity, cluster, severity, and workbook-alignment contract. `subagent_handoffs/spreadsheet_doc_worker_handoff.md` records the guarded wording correction, workbook hashes, structure preservation, ZIP integrity, and rendered review. |

No RF item was rejected, deferred, or replaced with a fallback.

## Reconciliation of the earlier stale audit

The read-only error-log/acceptance audit was valuable at its snapshot, but its latent gameplay findings are not current blockers:

- `resources_found_unsealed_nest` now has a real event setter and cleanup paths, so the opening-strength input is reachable;
- the unset `resources_found_normal_training_completed` achievement disqualifier was removed instead of being represented as false engine proof;
- Event `.83` has a delayed natural call, and its choices set the piercing and hostile-air observation flags used by the focus route;
- continental-capital capture is recorded from the bounded state-control transition;
- rich, strongpoint, and transport objectives have decision and AI assignment consumers;
- `front_unit_request` supplements `front_control` for origin, anchor, and doctrine-objective allocation;
- field binding sets `resources_found_field_system_participant`, preserving the narrow annex cleanup hook;
- the deeper-test project and enrichment eligibility use the same `resources_found_deep_survey_complete` flag;
- the repaired observation and capital milestones allow the normal focus chain to reach its terminal verification route.

These checks prevent the closure decision from inheriting obsolete failures from the earlier snapshot.

## Proof-gate disposition

| Gate | Closure basis |
| --- | --- |
| PG-01, opening strength | Exact equation and constants, deterministic boundary profiles, and exact spawn-allocation consumption are present. |
| PG-02, capacity and denial | Capacity formula, origin exclusion, 30-day activation, three-capacity denial, zero clamp, interrupted-attempt persistence, 21-day grace, and spawn intervals are represented by deterministic definitions and focused static traces. |
| PG-03, combat and route AI | The five repaired focus rewards have real cumulative mechanics, observation gates have setters, map objectives have assignment consumers, and origin/anchor defense uses unit-request strategies. The accepted static-proof mode does not claim a live combat campaign. |
| PG-04, evolution and closure | Four global chronology guards, active-field progression, full-seal exact ledger reversal, and closure documentation are aligned. |
| PG-05, terminal and aftermath | The classifier and reconstruction truth tables match the live triggers/effects/events, including incompatible-world-end and duplicate-choice prevention. |
| PG-06, UI, assets, and text | Current localisation key coverage, registered texture existence, exact animation frame counts, static fallbacks, and achievement triplets are complete. |

## New-depth review

No genuine depth gap remains inside the accepted Event 018 design. The existing system already connects the persistent field economy, exact resource ledgers, trade and commission routes, escalating incidents, exact closure, Oth-Kesh country package, three doctrines, captured-resource deployment, counterplay, terminal route, defeat cleanup, reconstruction, achievements, Event Details, audiovisual package, and catalog documentation.

The optional ideas rejected by the implementation-depth addendum remain rejected for this completion pass: Evolution V, a second cave country, a commodity exchange or resource currency, a normal cave production economy, a fourth doctrine, a hidden retaliation, and breadth-only incident or art work. None is needed to close a defect or fulfill the accepted source specification.

## Unresolved items and next ownership

There is no unresolved RF-018-01 through RF-018-08 item and no planner blocker.

The next workflow step is the parent-owned final `chaosx_event_completion_auditor` review and the parent-owned plan-scoped Git commit required by repository policy. Those are completion-process steps, not design gaps, and do not require another improvement-loop planner run.

## Simplifications, omissions, and blockers

No simplification, fallback, omitted RF item, or new blocker was introduced. Live engine proof is not claimed and was not required under the recorded user-approved static acceptance boundary.

## Skill usage

- Used `chaos-redux-improvement-loop` for the bounded closure decision and no-breadth rule.
- Used `chaos-redux-event-planning` to distinguish source-spec promotion from implementation evidence.
- Used `chaos-redux-events` to verify event, chronology, documentation, and workbook alignment.
- Used `chaos-redux-subagents` to reconcile handoffs and retain parent ownership of final validation and commit.
- Used `xlsx` for read-only workbook inspection and formula/error verification.
- No skill was created or modified.
