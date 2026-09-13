# Event32 operations temp19 probability evidence

Audit status: baseline READY for the parent cleanup review on 2026-09-05.

This is a read-only pass over `common/scripted_effects/032_missiles_operations_effects.txt` at raw SHA-256 `E20B0F6130AEEAEC04E9885B775413220B593BC95A6FC11CFD3D0D62730F0EB3`. The bounded scope is the seven terminal `clear_temp_variable` statements at lines 199-201, 1682-1684, and 1844; no source change was made here.

## MCP baseline

Scenario id: `E32-TEMP19-B0`. No seed, cadence, state-transition schedule, or runtime candidate realization was declared because the three helpers below either calculate a durable value or run a deterministic strict-greater score race.

The mandatory narrow call was `hoi4.probability_inspect({source:{path:"common/scripted_effects/032_missiles_operations_effects.txt",identifier:"missiles_calculate_command_pressure"},refresh:true})`.

The result was `status=ok`, `code=PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=source_inventory`, MCP `sourceRevision=d01b0cd3369af2a9668e16e52291e40febfac25cf342b749e141ca38f3261df8`, and MCP `sourceHash=7bb2c40578426f18e237ea44c2b1eb886e8d76f1140253950e5ff920d179a001`.

The preserved artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d543936e37afbcaf7167018534ed7db3e4aaf2724787239fb97f32d93916054/c044bbbf44161dbd559b19932ad1495b1eaef780444addfe4bb0c60571c7e774/probability-inspect-7bb2c40578426f18e237ea44c2b1eb886e8d76f1140253950e5ff920d179a001.json` with artifact SHA-256 `3d543936e37afbcaf7167018534ed7db3e4aaf2724787239fb97f32d93916054`.

The inspect found `candidates=0` for the requested helper and only a suggested `random_list` adapter with 19 available candidates, `identifierMatches=0`, and `candidatePoolMatches=19`; every example is a later `032_missiles_operations_effects.txt:2517.entry.*` surface and is outside this FIRST2000 audit scope.

Therefore no probability distribution, timing result, rank reversal, dominance, starvation, repetition, or exploit-risk conclusion is available for this cleanup. The adapter limitation is exact: the discovered random-list pool is out of scope, while the requested country and state helpers are deterministic score races.

## Bounded source data flow

`missiles_calculate_command_pressure` at lines 183-201 initializes each component before use. `missiles_command_pressure_component` is set and reduced at lines 184-185, then copied into durable `missiles_command_pressure` at line 186; `missiles_stability_pressure` is set and multiplied at lines 187-188, then consumed while forming the gap at line 190; `missiles_stability_pressure_gap` is set, reduced, multiplied, and added into durable `missiles_command_pressure` at lines 189-192. The three cleanup lines 199-201 occur after those reads, and the bounded identifier search found no later reads of these component temporaries.

The durable `missiles_command_pressure` result is later read by `missiles_evaluate_rogue_incident_from_firing` through random-list modifiers at lines 364 and 369-378. That downstream surface is outside this cleanup audit and does not read any of the three temporary identifiers.

`missiles_score_target_country_candidate` at lines 1631-1685 sets `missiles_target_factory_score` at line 1637, multiplies it at line 1638, and adds it to the aggregate at line 1639; it sets `missiles_target_state_score` at line 1640, multiplies it at line 1641, and adds it at line 1642. The two component temporaries have write-before-read proof and no later reads before cleanup at lines 1682-1683.

`missiles_target_candidate_score` is different from those components. It is initialized at line 1632, receives the conditional score additions, is compared against `ROOT.missiles_best_target_country_score` at line 1671, and is then observed by `PREV.missiles_target_candidate_score` inside the nested `ROOT` block at line 1674 before cleanup at line 1684. The local write-before-read order is established, but this is a scoped read of an unscoped temporary; the engine's `PREV` resolution for that pattern is not established by the available probability adapter, so preservation of that observed value remains unresolved engine-semantic evidence.

`missiles_score_operation_target_state_candidate` at lines 1776-1845 initializes `missiles_target_state_candidate_score` at line 1777, applies the conditional additions, compares it against `ROOT.missiles_best_target_state_score` at line 1835, and observes it through `PREV.missiles_target_state_candidate_score` inside `ROOT` at line 1839 before cleanup at line 1844. The local write-before-read order is established, but the same unscoped-temp `PREV` resolution limitation applies; no later scratch read was found in the bounded helper/caller path.

The country selector iterates eligible entries in `global.enabled_countries_list` and calls the country scorer, while the state selector iterates valid profile-bearing owned and controlled states of the selected target. Both selectors retain the first item on ties because the update condition is strict `greater_than`; these are score-only deterministic selection races, not probability-proportional choices.

The target score baseline is `constant:missiles_target_score.baseline = -100000`, with source constants for major `180`, factory step `4`, controlled-state step `5`, profile value `100`, profile-specific values `100-130`, capital `70`, active war `45`, first-use pressure `30`, evidence pressure `35`, strategic depth `25`, frontline `-35`, island `-20`, resistance `-30`, secure state `20`, and poor-guidance isolation `45`. These are source traces only; no runtime score evaluation was available.

## Cleanup and limitations

The consulted vanilla documentation documents `set_temp_variable` and `clear_variable`; it contains no `clear_temp_variable` entry. The offline wiki describes temporary variables as unscoped values with effect/trigger-block lifetime, but it does not provide a supported cleanup route matching the seven statements. No `clear_variable` replacement is recommended for these temporary names.

The parent may remove only the seven terminal cleanup statements while preserving every set, multiply, subtract, add, compare, and `PREV` read. This report supports unchanged source arithmetic and selection order after terminal cleanup, with the explicit unresolved caveat for the two scoped `PREV` reads above; it does not authorize changing those reads or any score constants.

`hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, and `hoi4.probability_render` were skipped because no valid in-scope weighted adapter or complete runtime candidate pool exists. No probability comparison attempt was started, so there is no interrupted comparison to recover. Event structural inspect/render was also skipped in this bounded probability-only pass and is not claimed by this report.
