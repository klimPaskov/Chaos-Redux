# Event 014 Decision and Mission Findings Remediation Handoff

Date: 2026-07-15

Owner: `portrait_regen_b`

Mode: patch-capable Event 014 implementation and final self-reaudit. No commit was created because the parent agent owns final integration in the shared working tree.

## Assigned Findings

- P3-01: make exact displayed balances affordable across the full paid Event 014 decision surface.
- P3-02: add one idempotent all-mission runtime cleanup at incarnation reset while preserving another actor's terminal hunt.
- P3-03: make manual scenario launch atomic by validating and freezing every required actor, state, and reusable slot before the first gameplay mutation.

All three findings are implemented. The final audit reports P0 0, P1 0, P2 0, and P3 0.

## Implementation Summary

### P3-01: affordability

Added paired below-cost gates for every paid static strict comparison that previously compared directly against the spend amount. The rule is cost minus 1 for manpower and cost minus 0.01 for fixed-point resources. Existing inclusive equipment and Larder comparisons were retained.

Static constants and trigger consumers changed:

- `common/script_constants/014_cannibalism_core_constants.txt`
- `common/script_constants/014_cannibalism_objective_constants.txt`
- `common/script_constants/014_cannibalism_achievement_constants.txt`
- `common/script_constants/014_cannibalism_country_constants.txt`
- `common/script_constants/014_cannibalism_integration_constants.txt`
- `common/script_constants/014_cannibalism_unified_decision_constants.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/scripted_triggers/014_cannibalism_objective_triggers.txt`
- `common/scripted_triggers/014_cannibalism_achievement_triggers.txt`
- `common/scripted_triggers/014_cannibalism_warlord_triggers.txt`
- `common/scripted_triggers/014_cannibalism_integration_triggers.txt`
- `common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt`

Dynamic unified-operation changes:

- Added `cannibalism_unified_affordability.manpower_gate_step` and `fixed_point_gate_step`.
- Added `cannibalism_unified_refresh_affordability_gates` in `common/scripted_effects/014_cannibalism_unified_decision_effects.txt`.
- The refresh derives 43 gate variables from the final runtime costs after hostility surcharges.
- Unified affordability triggers use the derived gates; execution effects still spend the full runtime cost variables.

Reviewed but intentionally unchanged:

- Wendigo and focus-closure decisions already used complete paired gate contracts.
- `cannibalism_wendigo_decision.identify_political_power` 25 already pairs with `identify_political_power_gate` 24.99.
- `cannibalism_unified_operation.air_program_experience_gate` and `air_program_airframe_gate` are non-cost foundation thresholds. The foundation execution spends manpower, support equipment, and fuel only.

### P3-02: mission reset

Changed `common/scripted_effects/014_cannibalism_core_effects.txt`:

- Added `cannibalism_clear_all_current_country_mission_runtime`.
- Guarded `remove_mission` calls cover all 14 Event 014 timed missions.
- The helper invokes every family runtime clear effect.
- It is the first call in `cannibalism_reset_current_country_incarnation_state`.
- Terminal global cleanup runs only when the resetting country owns `cannibalism_wendigo_terminal_hunt_active`; a non-owner reset clears only local terminal variables and flags.

Changed `common/scripted_effects/014_cannibalism_objective_effects.txt`:

- Added `cannibalism_clear_current_country_compact_vigilance_runtime`.
- Refactored reconstruction retirement to call the pure runtime clear before setting participant completion.
- Removed objective-resolution flags from the pure investigation and hold-prison clear helpers.
- Added those flags explicitly to the corresponding complete, partial, and failed outcomes.

Changed `common/scripted_effects/014_cannibalism_unified_decision_effects.txt`:

- The command, Larder, war-machine, and counterwar mission clear helpers now clear their stored duration variables.

### P3-03: scenario preflight

Changed `common/script_constants/014_cannibalism_scenario_constants.txt`:

- Added `cannibalism_scenario_scale.discipline_extended_source_states = 2` for high/maximum Discipline Collapse, where the source must provide one state beyond its canonical opening node.

Changed `common/scripted_triggers/014_cannibalism_scenario_triggers.txt`:

- Added exact actor opening-state capacity triggers.
- Added preflight source and additional-actor triggers.
- Added Island, Siege, and March preflight state triggers.
- Planned external states exclude all planned actor controllers.
- Convergence preflight rejects active, revealed, or previously broken convergence.

Changed `common/scripted_effects/014_cannibalism_scenario_effects.txt`:

- Added `cannibalism_scenario_prepare_preflight_requirements`.
- Added `cannibalism_scenario_plan_available_warlord_slots`.
- Added `cannibalism_scenario_build_manual_preflight_plan`.
- Added `cannibalism_scenario_allocate_next_planned_warlord_slot`.
- Manual actor, state, and slot selection consumes frozen temporary arrays.
- Added explicit cross-array state exclusions in the manifest builder even though the three origin predicates are already disjoint.
- `trigger_cannibalism_scenario` performs preflight before global runtime preparation.
- Failed preflight sets only the launcher failure marker and clears temporary manifests.
- Launch history, counters, scheduler refresh, and manual-scenario achievement disqualification occur only after setup success.
- Automatic Evolution III prefire explicitly uses the original dynamic path.

Exact external consumption by profile and intensity:

- Silent Islands: I1/I2/I4/I6 states, 0/1/1/2 warlord-capable hosts, 0/1/1/2 slots.
- Warlord States: S1; I1+S1; I1+S2+M1; I2+S2+M2, consuming 1/2/4/6 slots.
- Convergence: I1+S1+M1; I2+S1+M1; I2+S2+M1; I2+S2+M2, consuming 3/4/5/6 slots.

`I`, `S`, and `M` mean Island, Siege, and March states.

## Documentation

Updated:

- `docs/events/014_cannibalism/overview.md`
- `docs/plans/014_cannibalism_plans/audits/event014_decision_mission_reaudit_2026-07-15.md`
- this handoff

The final audit is ASCII-only and replaces the earlier three-finding report with a zero-finding final report.

## Validation Evidence

Decision and affordability inventory:

- 127 Event 014 decision entries.
- 94 custom affordability triggers.
- 74 paid static strict gates checked against paired spends; zero delta errors.
- 43 unified runtime gates; zero missing set, subtract, or trigger-use entries.
- hostility refresh precedes unified gate derivation.
- all paid Larder comparisons use inclusive `greater_than_or_equals` logic.

Mission cleanup inventory:

- 14 timed mission IDs parsed.
- 14 guarded `remove_mission` IDs in the all-mission cleanup.
- missing IDs: none.
- extra IDs: none.
- outcome-setting flags in the 13 non-terminal pure runtime clear helpers: none.

Scenario atomicity checks:

- preflight helper gameplay mutation hits: none.
- preflight precedes runtime preparation: yes.
- runtime preparation is guarded by preflight success: yes.
- state manifests explicitly reject prior array membership: yes.
- per-profile planned actor/state/slot requirements equal downstream consumption: yes.
- success history and counters occur after setup success: yes.
- automatic prefire forces the dynamic path: yes.

Source hygiene:

- touched Clausewitz files have balanced braces.
- no unsupported `<=` or `>=` operator was introduced.
- `git diff --check` reported no whitespace error; it emitted only existing line-ending conversion warnings.

The optional Event Chain Viewer lint could not persist its linked artifact because the shared artifact store reported `ARTIFACT_STORAGE_LIMIT`. This did not block the source-based checks above.

## Integration Notes and Risks

- The repository was already a shared dirty working tree. Several changed Event 014 files also contain concurrent parent-agent edits, including removal of the obsolete Prison Host origin. Those edits were preserved.
- No commit was created.
- No fallback or simplification was used.
- No unresolved gameplay, documentation, audit, or validation blocker remains in this assigned scope.
