# Event 006 decision and mission completion audit

## Outcome

Status: **PARTIAL / HOLD**.

The decision and mission surface is materially healthier than the 2026-07-25 audit recorded.

The earlier permanent DM-58 global lock, incomplete custom-cost localisation triplets, absent values surface, and AGX conference cancellation gap are not present in the current source.

No gameplay file was edited by this audit.

The remaining hold is the DM-58 preflight's inability to prove an injective three-member-to-three-owner front assignment before the player starts the mission.

## Scope and sources checked

- `common/decisions/006_independence_wave_decisions.txt` — shared DM actions, including `independence_wave_coordinate_reclamation_fronts` (DM-58).
- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt` — AGX/Frisia waterline category, mission, projects, former-host reconciliation, route lock, and conference.
- `common/decisions/006_independence_wave_scenario_decisions.txt` — SCN-008 ledger navigation decisions.
- `common/decisions/categories/006_independence_wave_categories.txt` and `common/decisions/categories/006_independence_wave_wallonia_frisia_categories.txt` — category visibility and the decision-owned ledger surface.
- `common/scripted_effects/006_independence_wave_decision_effects.txt` and `common/scripted_effects/006_independence_wave_effects.txt` — DM-58 execution, rollback, operation cleanup, reset, and origin-end cleanup.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`, `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`, `common/scripted_effects/006_independence_wave_scenario_effects.txt`, and region package publishers — shared release-plan reservations and SCN-008 dispatch.
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, `common/scripted_triggers/006_independence_wave_package_triggers.txt`, and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` — legality, host survival, collision, content-attestation, and scenario preflight gates.
- `common/scripted_guis/006_independence_wave_scripted_gui.txt`, `interface/006_independence_wave.gui`, `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt`, and `localisation/english/006_independence_wave_gui_l_english.yml` — Statehood Ledger presentation.
- All `common/decisions/006_independence_wave*.txt` and `localisation/english/006_independence_wave*.yml` — custom-cost linkage inventory.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md` and `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` — intended action, phase, and value-surface contracts.

The offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, and AI were consulted.

Vanilla precedents and documentation consulted were `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/decisions/foreign_influence.txt`, and `common/decisions/formable_nation_decisions.txt`.

## Issue list, ordered by severity

1. **High — DM-58 acceptance HOLD:** `has_independence_wave_reclamation_front_preflight` counts three independently eligible member countries, but does not prove that those members can be matched to three distinct external owners at activation time.
   The resolver enforces owner and state uniqueness while freezing targets and rolls back without charging costs if fewer than three pairs are created.
   The mission can therefore be offered in a world state that resolves into the designed failure branch after its timer rather than being unavailable immediately.
   Fixing this requires a reusable matching/preflight design, not a narrow local decision patch.
2. **Medium — dynamic SCN-008 evidence HOLD:** static source proves host-remnant and reservation gates, but this audit did not execute a deterministic scenario sweep that shows accepted and rejected rows for every admitted package under collision-heavy maps.
   This is an evidence gap, not a confirmed release-plan defect.
3. **Low — AGX gate clarity:** `independence_wave_agx_convene_north_sea_coastal_conference` has correct package, waterline, recognition, network, federation-candidate, mandate, client-route, and capital gates.
   Its route, mandate, and candidate gates remain raw hidden visibility conditions rather than named player-facing prerequisite tooltips or a visible reveal state.

## Decision category lifecycle notes

- `independence_wave_founding_category` is visible only to active Event 006 countries and owns `independence_wave_status_scripted_gui`.
- Government, recognition, security, host-relations, patron, network, league, borders, formables, and high-chaos categories use the active-country state machine rather than a passive political-power store.
- The AGX waterline category is package-gated, while `independence_wave_scenario_ledger_category` is only exposed during SCN-008 ledger use.
- The ledger panel presents legitimacy, recognition, capacity, security, and instability, plus host, patron, network, phase, and commitments.
- Its five tab buttons only set local display flags, have no gameplay cost or effect, and correctly disable AI interaction because they are presentation-only.

## Mission quality notes

| Owner and category | Mission or decision | Region and requirement | Duration and outcomes | Duplicate / cleanup risk |
| --- | --- | --- | --- | --- |
| AGX / `independence_wave_agx_waterline_category` | `independence_wave_agx_hold_the_waterline` | Frisia; exact IW-007 package, setup complete, unstable waterline | 540-day automatic crisis; stable waterline resolves it, capital/package loss or timeout fails it | PASS: terminal flags prevent duplicate resolution and package/capital cancellation is bounded. |
| AGX / waterline category | Pump, harbour, rail, and dike projects | Frisia; package, controlled capital, one active project at once | Short/standard project durations; different materials and different waterline/security gains | PASS: serialisation flag, cancellation penalties, and project completion flags prevent farming. |
| AGX / waterline category | `independence_wave_agx_reconcile_water_board_records` | Frisia; living former host, peace, stable capital, no project | Administrative reconciliation with normal completion/cancellation paths | PASS at source level: host and capital gates avoid dead-host or war reuse. |
| League / high-chaos category | `independence_wave_coordinate_reclamation_fronts` (DM-58) | Radical charter member, focus authorisation, three eligible member fronts, reserve threshold | Long selectable mission; success creates finite 365-day take-state goals, failure/timeout starts league crisis | PARTIAL: rollback and post-freeze charging are sound, but preflight cannot establish the required distinct-owner matching. |
| Scenario / ledger category | `independence_wave_scenario_ledger_previous`, `_next`, `_close` | SCN-008 ledger flag and row bounds | Immediate navigation only; close clears the ledger surface | PASS: no cost, no material reward, zero AI weight, and bounded visibility. |

## Cost and requirement clarity

- A static inventory found **101** Event 006 `custom_cost_text` identifiers.
- All 101 have the base key, `_tooltip` key, and `_blocked` key in Event 006 English localisation.
- AGX's North Sea conference uses the dedicated `independence_wave_cost_agx_coastal_conference` string and a three-civilian-factory strategic commitment for 300 days.
- DM-58 requires strategic and major-security material costs plus a shared-reserve threshold, and pays both costs only after the resolver freezes at least three legal pairs.
- SCN-008 navigation is correctly not represented as a costed political-power exchange.

## AI validity and route-lock notes

- AGX's crisis projects use urgency/high weights, and the conference starts at standard weight with constitutional and popular route multipliers.
- DM-58 has a high AI weight but retains the same activation preflight, radical-charter, client-route, active-country, and shared-reserve checks as the player.
- The scenario ledger has no gameplay-bearing AI action; its scripted GUI has `ai_enabled = { always = no }`, which is appropriate for local-tab presentation.
- AGX conference cancellation repeats its package, waterline, recognition, network, federation-candidate, mandate, client-route, and capital checks, closing the previously reported route-loss continuation path.
- Package and scenario release gates require a dormant exact tag, exclude Event 005/012 origin collisions and Soviet-collapse origins, reserve countries and states through the shared release plan, and reject un-attested package IDs before dispatch.

## Localisation, tooltip, cleanup, and exploit-risk notes

- The Statehood Ledger resolves the five required live values through scripted localisation rather than duplicating static decision descriptions.
- `independence_wave_cleanup_reclamation_front_operation` clears the operation flag, state use/claim flags, active member receipts, arrays, and count at reset, league transition, dissolution, and member-count failure.
- DM-58 rollback removes only claims added by the operation, removes the matching finite war goal, clears staging, and clears its arrays before the failed branch applies league penalties.
- The remaining AGX raw prerequisite presentation gap is low severity because the cost availability itself has a custom cost tooltip and the locked decision is not executable.
- No paid-failure, free-unit, equipment-farming, core-spam, or war-goal-spam loop was found in the audited AGX, DM-58, or SCN-008 paths.

## GUI evidence

- Focused inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72ba51ba5277a65c14759aa20ce1ab925ff17a2d48bbecdb49d7e82599376dfd/df478d3f4204e3106b809bea93093c4f2222340473e399d689edfe81052dbde4/gui-inspect.e0342f9b582da5e3.json`.
- Rendered the decision-owned `independence_wave_status_window` at 1920x1080 and 1280x720 for normal, warning, long-text, and missing-localisation states.
- Render matrix artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9137a6524ae42b587028542e9f72767a6df18efb4ed6a8671c31e79caf8357c5/b96cd92f64b16a83ea6e1b1c6a472cb6308d58db1073c1b9e353ba61f430ef02/independence_wave_status_window-state-matrix.json`.
- Representative full render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a78229236125fa50e3b1073c8ca8202455d37d7b55e9a551cf02dd61382dc97/521efc6c6e86e334df9d97c37b70127f0feee4cec72cd620760ab83d33556eb5/independence_wave_status_window-full.png`.
- The GUI tool reports workspace-wide unresolved/import fidelity findings, so this is source-linkage and rendered-state evidence rather than a full GUI fidelity PASS.

## Recommended fixes and ownership

1. **Parent or scripted-system architect:** design an injective DM-58 preflight over member, state, and owner arrays, then replace the independent `any_country = { count = ... }` proof in `common/scripted_triggers/006_independence_wave_decision_triggers.txt`.
2. **Parent validation tranche:** run a deterministic allocator/scenario evidence sweep with the admitted SCN-008 packages in contested-host, reserved-state, duplicate-tag, and closed-route cases.
3. **Optional local clarity pass:** add named prerequisite tooltips or an authorised-but-waiting presentation state for `independence_wave_agx_convene_north_sea_coastal_conference` in its decision and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`.

## Validation and handoff

- Meaningful validation run: static cross-file custom-cost linkage returned 101 total custom cost identifiers, with 0 missing base keys, 0 missing tooltip keys, and 0 missing blocked keys.
- Meaningful validation run: source tracing confirmed AGX conference continuation gates, DM-58 post-freeze payment and rollback, Statehood Ledger linkage, and SCN-008 reservation/content-attestation gates.
- Meaningful validation run: decision-owned GUI inspection and multi-resolution state rendering were completed using the artifact references above.
- Skipped meaningful validation: no live HOI4 run was performed, per repository ownership rules.
- Skipped meaningful validation: no full deterministic scenario/weighted-logic sweep was available in this bounded audit, leaving the two HOLD evidence items above.
- Changed files: this handoff only.
- Changed gameplay, decision, mission, scripted-GUI, and localisation identifiers: none.
- Simplifications: none were made by this audit.
