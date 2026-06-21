# Event 012 Africa Completion Audit

Date: 2026-06-21 10:59 UTC
Role: read-only Event 012 completion audit
Scope: specs/prompts/plans/current implementation for Event 012 Africa. No gameplay, localisation, asset, spreadsheet, or binary files were edited.

## Verdict

Event 012 Africa is not completion-ready.

The implementation is broad and many formerly blocking surfaces are now live: event root, unifier selection, SCN-008 registration, focus trees, decision families, created actor static country packages, super-event slots/audio, regenerated icons, achievement definitions/icons, and several Authority Atlas/Bestiary/regional-package layers. The remaining blockers are mostly validation, stale documentation alignment, prompt-equivalent GUI proof, route-depth proof, and spreadsheet/catalog follow-up.

Parent follow-up, 2026-06-21: after this audit was written, the parent reconciled the active SCN-008 validation matrix and spreadsheet/catalog wording. `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md` now describes the two current manual types, `Africa Is One` and `World Is One`, and separates the direct manual terminal setup from the ordinary World Is One proof chain. `docs/spreadsheets/chaos_redux_events_catalog.xlsx` Main Sheet row `13` now uses `SCN-008` and the two live type names. The broader audit verdict remains unchanged because live scenario proof, ordinary World Is One proof, GUI render proof, exploit/balance validation, route-depth proof, and final status alignment are still open.

## Priority Findings

1. SCN-008 implementation and validation docs are out of sync.

- Current constants expose only two Africa scenario types: `africa_is_one = 1` and `world_is_one = 2` in `common/script_constants/chaosx_triggerable_scenarios_constants.txt:127-135`.
- Scenario localisation also exposes only `Africa Is One` and `World Is One` in `localisation/english/chaosx_gui_l_english.yml:146-148` and `:183-184`.
- The latest source-of-truth says SCN-008 has only those two types and the `World Is One` type directly sets terminal readiness/world-end behavior (`docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md:96`).
- But the active validation matrix still audits removed old types such as `Standard Unifier`, `Fragile Unifier`, `RSA Civil War`, `Ally Under Attack`, `High-Chaos Covenant`, and `Continental Pole` (`docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md:13-20`). It also says the scenario does not set terminal flags (`:20`, `:26`), which is now false for the current direct `World Is One` type.
- Live code proves the direct terminal path: `africa_apply_triggerable_world_is_one_opening` sets proof/certification/prepared markers and calls `africa_force_triggerable_world_is_one_terminal` (`common/scripted_effects/012_africa_effects.txt:607-628`), which sets `world_end`, `world_end_africa_world_is_one`, `africa_world_is_one_gate_ready`, and `africa_world_is_one_terminal_started` (`:819-824`).

Required fix: replace the stale validation matrix with a SCN-008 two-type validation matrix, then run or record live/manual proof for both types at Low/Medium/High/Maximum, including whether direct terminal launch is intentionally allowed when another world-end branch is active.

2. World Is One normal-route gate is statically strong, but not completion-proven.

- Normal route gate is strict: certification requires chaos tier 5, Africa Is One, super-event fired, continental pole, external proof flags, external world-end readiness, dossier/case/high-chaos/regional package requirements, living cores, and Bestiary actions (`common/scripted_triggers/012_africa_triggers.txt:2389-2434`).
- Preparation revalidates the full chain plus certification and resource costs (`common/scripted_triggers/012_africa_triggers.txt:2436-2481`; `common/decisions/012_africa_decisions.txt:5642-5697`).
- The final focus `AFR_the_world_is_one` is available only through `can_africa_start_world_is_one_gate` and calls `africa_mark_world_is_one_gate_ready` (`common/national_focus/012_africa_focus.txt:2299-2310`).
- No current handoff proves the whole normal sequence live. The current source map still lists final World Is One proof as open (`CURRENT_SOURCE_OF_TRUTH.md:33`, `:113`).

Required fix: validate the normal route separately from SCN-008 direct World Is One: sponsor charters, four proof missions, certification, preparation decision, final focus, and terminal flags only after final focus.

3. Live scenario, balance, and exploit proof is still missing.

- The acceptance criteria require targeted tests and exploit checks (`docs/specs/012_africa_specs/matrices/012_africa_acceptance_criteria.md`, AI/balance section).
- Decision audit says the remaining blockers need runtime proof: living-core conversion, dossier retries, resistance watch loops, Bestiary warnings/actions, sponsor proof repetition, GUI clicks, RSA settlement sequencing, and stale target cleanup (`docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_decision_mission_gui_hook_audit_handoff.md:87-109`).
- Focus audit says route coverage is static-covered, but live validation is still needed for focus loading, Bestiary reveal, Africa Is One gates, sponsor readiness, and final World Is One behavior (`docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_focus_tree_static_audit_handoff.md:97-104`).

Required fix: prioritize scenario-pressure validation over new mechanics.

4. Continental Congress GUI and animated assets are wired but not prompt-complete or live-proven.

- Current source map says the four prompt-named animated packages are wired with static fallbacks, sprite registration, GUI placement, visibility hooks, and tooltips (`CURRENT_SOURCE_OF_TRUTH.md:109`).
- The same line says the current strip is not accepted as full prompt-equivalent coverage for background/header/meters/regional cards or broader state families, and live render/animation proof remains missing.
- The GUI/animation gap handoff leaves background panel, header plate, meter frames/fills, regional authority card states, selected target proof, broader seal/formable states, and live render/playback proof queued (`docs/plans/012_africa_plans/2026-06-21_continental_congress_gui_animation_gap_handoff.md`).

Required fix: either implement the missing GUI/static/state families or write an explicit parent-approved equivalence decision mapping the current fixed panel to each prompt family, then add live screenshot/render proof.

5. Country packages are statically covered but not fully route-bespoke.

- Static package audit found all 25 created actors covered across tags, country files, histories, OOBs, flags, portraits, names, ideas, setup hooks, focus loading, forces, AI, assets, and docs (`docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_created_actor_static_country_package_audit_handoff.md:41-57`).
- The same audit says deeper route-specific country-package consequences remain valid and are not a narrow static defect (`:8-10`, `:76-80`).
- Current source map repeats that deeper route-specific consequences beyond origin/profile, regional-authority mandate/package, dossier slots, and role packages remain open (`CURRENT_SOURCE_OF_TRUTH.md:113`).

Required fix: do not rebuild all countries. Pick a bounded route-depth slice for selected host archetypes plus a few created actors, then validate distinct consequences and AI behavior.

6. Achievements are registered and iconed, but hard route/disqualifier proof is absent.

- Event 012 achievements begin at `common/achievements/chaos_redux_achievements.txt:2167`, with concrete flags/variables and disqualifiers for Archive, Bestiary, Scramble, Living Cores, RSA peace, etc.
- Asset manifest records generated normal/grey/not-eligible achievement icon variants (`docs/assets/012_africa/implementation_asset_manifest.md:117-140`).
- No current validation proves difficult route gates/disqualifiers under play, especially World Is One, Archive/Bestiary, RSA, direct Archive disqualifiers, and no-shortcut core achievements.

Required fix: include achievement trigger/disqualifier checks in the validation slice, not as a separate broad content pass.

7. Spreadsheet/catalog alignment is stale for SCN-008.

- Spreadsheet handoff still records `Scenario id: SCN-012` and cell `W13 -> SCN-012` (`docs/plans/012_africa_plans/2026-06-17_event_012_africa_spreadsheet_alignment_handoff.md:6-18`).
- Current implementation and source map identify the manual scenario as `SCN-008` (`common/script_constants/chaosx_triggerable_scenarios_constants.txt:22`; `CURRENT_SOURCE_OF_TRUTH.md:96`, `:111`).
- Workbook main status was intentionally left `Needs Testing` (`2026-06-17_event_012_africa_spreadsheet_alignment_handoff.md:20-28`).

Required fix: after validation, update workbook/catalog wording for SCN-008 two-type behavior and keep main status below `Implemented` until validation passes.

## Completion Status By Surface

| Surface | Status | Notes |
| --- | --- | --- |
| Event root/baseline | Partial pass | Root, selection, runtime context, N/A fallback, and package setup exist. Completion blocked by validation. |
| SCN-008 scenario | Implemented but documentation/validation stale | Two live types exist; old validation matrix and spreadsheet still describe older scenario shape/ID. |
| Focus trees | Static pass, live unproven | Focus audit found 157 focuses across main/authority trees and no route-family omission; runtime route sequencing remains unproven. |
| Decisions/missions/values | Static partial pass | Not a PP store; broad families exist. Live exploit/cleanup proof still missing. |
| GUI/UI | Partial | GUI and prompt-named animations are wired; broader prompt-equivalent UI families and live proof remain open. |
| Country packages | Static pass, depth partial | 25 created actors have static coverage; not every country has fully bespoke route consequences. |
| Evolutions/logs | Partial | Helpers and docs exist; disabled-evolution and route behavior need validation proof. |
| Super-events/audio | Pass for accepted live package | Slots 68-79 plus root-terminal audio id 80 are documented as sourced/wired; do not reopen unless new roles are accepted. |
| Achievements | Registered, unvalidated | Definitions and icons exist; hard-route proof/disqualifiers remain untested. |
| Assets | Mostly wired; GUI/history caveats | Generated icons, flags, portraits, super-events strong; GUI family proof and historical-source judgment remain. |
| AI/balance | Static partial | AI strategy exists; route behavior under scenario pressure not proven. |
| Docs/spreadsheet | Partial/stale | Current source map is useful; scenario matrix and spreadsheet handoff need SCN-008 reconciliation. |

## Accepted Plans And Disposition

| Plan/handoff | Disposition |
| --- | --- |
| `2026-06-16_foundation_gap_improvement_addendum.md` | Dispositioned by `2026-06-20_foundation_addendum_disposition.md`; no longer one broad blocker, but queued validation/depth/UI/spreadsheet items remain. |
| `2026-06-20_foundation_addendum_disposition.md` | Current ledger; explicitly not a completion claim. |
| `2026-06-20_targeted_scenario_validation_matrix.md` | Stale for current SCN-008 two-type implementation; must be replaced or revised before it can be validation evidence. |
| `2026-06-21_continental_congress_gui_animation_gap_handoff.md` | Current for broader GUI/static/state families and live render proof; superseded only for the four prompt-named animation rows that are now wired. |
| `2026-06-20_012_africa_created_actor_static_country_package_audit_handoff.md` | Current for static actor package coverage; explicitly does not close route-depth/live-validation blockers. |
| `2026-06-21_012_africa_focus_tree_static_audit_handoff.md` | Current for static focus coverage; live route validation still needed. |
| `2026-06-21_012_africa_decision_mission_gui_hook_audit_handoff.md` | Current for decision/mission/GUI static status and sponsor GUI cost parity; runtime exploit validation still needed. |
| Super-event/audio handoffs | Closed for accepted slots/audio. |
| Spreadsheet handoff | Stale scenario ID and status still `Needs Testing`; update after validation. |

## Meaningful Validation Found Or Missing

Found:

- Static focus route coverage and icon/localisation checks.
- Static decision/mission audit and one GUI sponsor cost parity patch.
- Static country-package coverage for 25 created actors.
- Static GFX/asset manifest coverage for accepted icons, flags, portraits, super-events, and four prompt-named GUI animations.
- Strong static normal-route World Is One gates.

Missing:

- Live SCN-008 two-type scenario proof.
- Live normal-route World Is One proof.
- Runtime exploit checks for core conversion, dossier/retry/watch loops, sponsor proofs, Bestiary actions, RSA treaty, GUI clicks, and stale targets.
- Live GUI render/readability/animation proof.
- Achievement hard-route/disqualifier proof.
- Final workbook/catalog alignment.

## Remaining Blockers

1. SCN-008 validation matrix and spreadsheet/catalog are stale.
2. No live validation for SCN-008 `Africa Is One` / `World Is One` behavior across intensities.
3. No live normal-route World Is One proof.
4. No scenario-pressure exploit/balance validation.
5. GUI prompt-equivalence and live render proof remain open.
6. Route-specific country-package depth remains intentionally bounded/shared.
7. Achievement route/disqualifier proof remains missing.

## Recommended Next Implementation Slice

Run a validation-and-reconciliation slice, not a new feature slice:

1. Replace `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md` with a current SCN-008 two-type matrix.
2. Validate SCN-008 `Africa Is One` at Low/Medium/High/Maximum: selected host or WAC fallback, Charter League, paper/living-core state, regional authorities, Authority Atlas, sponsor surfaces, unification wars, values, AI posture, and cleanup.
3. Validate SCN-008 `World Is One` at Low/Medium/High/Maximum: direct terminal flags, external unifier support/war targets, super-event/audio, compatibility with existing `world_end`, and whether direct terminal launch is intended/documented.
4. Validate normal-route World Is One separately: proof missions, certification, preparation, final focus, and terminal flags only after `AFR_the_world_is_one`.
5. Run exploit checks for living cores, dossier/case/retry slots, resistance watches, Bestiary actions, sponsor proofs, RSA peace, and GUI buttons.
6. Capture GUI screenshots/render notes for early, Authority Atlas, Bestiary, sponsor, and World Gate states.
7. Update workbook/catalog to SCN-008 and final wording/status only after the above.

## Improvement Planner Recommendation

Do not spawn a broad `chaosx_improvement_loop_planner` yet. The event technically works across many surfaces, but the current blockers are validation, stale documentation, proof, and bounded route-depth closure. Use the planner only if the validation slice finds a new design gap not already covered by the accepted specs, the foundation disposition, or existing country-package depth notes.
