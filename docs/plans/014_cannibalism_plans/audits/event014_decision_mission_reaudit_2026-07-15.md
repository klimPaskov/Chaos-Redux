# Event 014 Decision and Mission Final Reaudit

> Superseded for current authority by `event014_decision_mission_consolidation_reaudit_2026-07-15.md`. This same-day checkpoint remains historical evidence only.

Date: 2026-07-15

Audit basis: live shared working tree after remediation of the three findings from the earlier Event 014 decision and mission reaudit. The working tree also contained concurrent Event 014 work, so this report treats current source files as authoritative and does not infer ownership from Git status.

Audit mode: source review plus task-specific mechanical cross-checks. Historical audits were used only to identify the findings that required closure, not as proof of the final result.

## Final Verdict

The Event 014 decision and mission package has no unresolved audit finding on the assigned surface.

- P0: 0
- P1: 0
- P2: 0
- P3: 0

All three prior P3 findings are closed:

- P3-01: exact displayed balances now satisfy every paid Event 014 affordability gate.
- P3-02: one idempotent reset helper removes every Event 014 mission object and clears every mission family's runtime without resolving missions or disturbing another actor's terminal hunt.
- P3-03: manual scenario launch now constructs and validates an exact actor, state, and reusable-slot manifest before the first Event 014 gameplay mutation.

## P3-01 Closure: Exact-Balance Affordability

### Static affordability contracts

Strict engine comparisons now use a paired gate immediately below the amount that the resolver spends:

- manpower gates are exact cost minus 1 person;
- command power, political power, army experience, navy experience, air experience, and fuel gates are exact cost minus 0.01;
- equipment checks retain the existing inclusive inverse form, `NOT = { has_equipment = { type < cost } }`;
- Larder checks use `check_variable` with `compare = greater_than_or_equals`.

The paired static contracts cover baseline containment, maintained objectives, international response, reconstruction, warlord operations, integration, unified terminal actions, and the existing Wendigo and focus-closure packages. The final constant/trigger cross-check found 74 paid static strict gates, and every gate differed from its paired spend by the correct unit. No missing or mismatched pair remained.

Representative contracts include:

- `cannibalism_decision_cost.logistics_manpower` 3000 with `logistics_manpower_gate` 2999;
- `cannibalism_objective_cost.network_resistance_command` 20 with `network_resistance_command_gate` 19.99;
- `cannibalism_international_response_cost.landing_manpower` 7000 with `landing_manpower_gate` 6999;
- `cannibalism_warlord_decision.synchronized_command_cost` 15 with `synchronized_command_gate` 14.99;
- `cannibalism_integration.prisoner_feeding_command_cost` 10 with `prisoner_feeding_command_gate` 9.99;
- `cannibalism_unified_decision.terminal_command` 25 with `terminal_command_gate` 24.99;
- `cannibalism_wendigo_decision.identify_political_power` 25 with the existing `identify_political_power_gate` 24.99.

The existing Wendigo and focus-closure cost pairs were reviewed across their full paid decision surfaces and required no edit.

### Dynamic unified-operation contracts

`cannibalism_unified_refresh_affordability_gates` derives 43 runtime gate variables from the final runtime costs. It subtracts `constant:cannibalism_unified_affordability.manpower_gate_step` or `constant:cannibalism_unified_affordability.fixed_point_gate_step` as appropriate.

The refresh runs after `cannibalism_unified_refresh_hostility_pressure`, so hostility surcharges are already included before a gate is derived. The unified affordability triggers consume those derived gate variables while the execution effects continue to spend the full runtime cost variables. Mechanical comparison found all 43 expected dynamic gates set, adjusted, and used.

### Thresholds that are not costs

`cannibalism_unified_operation.air_program_experience_gate = 5` and `air_program_airframe_gate = 25` remain unchanged. They are qualifying foundation thresholds inside `cannibalism_unified_has_air_program_foundation`, not resources spent by `cannibalism_unified_execute_air_foundation`. The foundation execution pays manpower, support equipment, and fuel only. Treating either threshold as a cost pair would change the mechanic rather than fix affordability.

## P3-02 Closure: Complete Idempotent Mission Reset

`cannibalism_clear_all_current_country_mission_runtime` is the first effect called by `cannibalism_reset_current_country_incarnation_state` in `common/scripted_effects/014_cannibalism_core_effects.txt`.

The helper guards `remove_mission` with `has_active_mission` and covers the exact set of 14 Event 014 timed missions:

- 2 baseline missions: supply corridor and formation rotation;
- 6 maintained objectives: investigation, hold prison, reach island, break network, stop unification, and stop transformation;
- 1 compact-vigilance mission;
- 4 unified receipt missions: command, Larder, war machine, and counterwar;
- 1 Wendigo terminal-hunt mission.

The mission inventory and reset-helper inventory are set-equal: 14 expected, 14 cleared, no missing ID, and no extra ID.

After removing active mission objects, the helper invokes the family-specific runtime clear effects. The investigation and hold-prison clear helpers no longer set objective-resolution flags; those flags are now set only by their full, partial, or failed outcome effects. The compact cleanup is separated from participant completion, so reset clears runtime without granting a reconstruction result. The four unified clear helpers also clear their persisted duration variables.

Terminal cleanup is owner-safe:

- if the resetting country has `cannibalism_wendigo_terminal_hunt_active`, the canonical terminal cleanup runs with target-lock cleanup enabled;
- otherwise only that country's local terminal pressure, counterpressure, date, and cooldown state is cleared;
- another actor's global terminal target and defender lock are not touched.

The family cleanup purity scan found no outcome-setting `set_country_flag` call in any of the 13 non-terminal runtime clear helpers. Repeated reset calls therefore remain idempotent and do not manufacture mission success, partial success, or failure.

## P3-03 Closure: Atomic Manual Scenario Preflight

`trigger_cannibalism_scenario` now calls `cannibalism_scenario_build_manual_preflight_plan` before `cannibalism_scenario_prepare_runtime` or any actor, node, evolution, warlord, history, scheduler, or achievement mutation.

The preflight manifest freezes:

- the exact source and additional actor countries;
- enough valid opening states for every planned actor;
- every external Island, Siege, and March state required by the selected profile and intensity;
- the exact reusable CBA-CBH country scopes required for all planned warlords.

Planned external states exclude every planned actor controller. State manifests also contain explicit cross-array exclusions. The origin predicates are independently disjoint: Island requires an island state, Siege requires a non-island state with a siege package, and March requires a non-island state without a siege package. The explicit exclusions make that invariant local to the manifest builder and prevent any future predicate expansion from double-counting a state.

Actor opening-state capacity matches the canonical initializer:

- Discipline Collapse requires 1 clear opening state per actor; at high and maximum intensity the source requires 2 because it supplies the one additional source node.
- Ritual Cells requires 2 clear opening states per actor.
- Silent Islands, Warlord States, and Convergence require 3 clear network opening states for their single source actor.

The exact external manifest and consumption matrix is:

| Profile | Low | Medium | High | Maximum |
| --- | --- | --- | --- | --- |
| Discipline Collapse | 1 actor; 1 opening each | 2 actors; 1 opening each | 3 actors; 1 opening each; source 2 | 5 actors; 1 opening each; source 2 |
| Ritual Cells | 1 actor; 2 opening each | 2 actors; 2 opening each | 3 actors; 2 opening each | 5 actors; 2 opening each |
| Silent Islands | I1, hosts 0, slots 0 | I2, hosts 1, slots 1 | I4, hosts 1, slots 1 | I6, hosts 2, slots 2 |
| Warlord States | S1, slots 1 | I1 + S1, slots 2 | I1 + S2 + M1, slots 4 | I2 + S2 + M2, slots 6 |
| Convergence | I1 + S1 + M1, slots 3 | I2 + S1 + M1, slots 4 | I2 + S2 + M1, slots 5 | I2 + S2 + M2, slots 6 |

`I`, `S`, and `M` mean Island, Siege, and March states. Silent Islands uses one source actor with 3 opening states at every intensity; Warlord States and Convergence do the same.

The manual setup path consumes the frozen arrays rather than repeating global searches. Island warlord-capable states are inserted first so Silent Islands consumes the required host states before node-only islands. Reusable slots are consumed in deterministic array order and revalidated immediately before their canonical allocator is called.

The preflight proves all canonical formation predicates that setup can otherwise fail on: Evolution II authorization, no active convergence, supported region, valid normal controller, no recovery or formation lock, no consumption cooldown, sufficient population, mature node strength, feeding-state stage, matching origin geography, and an exact reusable slot. Setup is a single synchronous effect chain, so no other Event 014 pulse can consume a frozen state or slot between preflight and commit.

Failure behavior is mutation-safe:

- a failed preflight sets only the launcher's `cannibalism_manual_scenario_setup_failed` marker;
- global runtime, actors, nodes, evolutions, warlords, history, launch counters, and manual-scenario achievement disqualification remain unchanged;
- temporary manifests are cleared before the wrapper returns;
- reservation cleanup is limited to committed preflights.

The automatic Evolution III prefire explicitly sets `cannibalism_scenario_use_preflight_plan = 0` and retains its dynamic source/state/slot path. Manual atomicity work therefore does not mark or reroute automatic prefire as a manual scenario.

## Retained Decision and Mission Inventory

The final parser inspected all eight Event 014 decision files and both Event 014 category files.

| Surface | Count | Result |
| --- | ---: | --- |
| Decision entries | 127 | All parsed |
| Read-only achievement tracker entries | 18 | Permanently unavailable and effect-free |
| Operational decision and mission entries | 109 | All inspected |
| Custom affordability triggers | 94 | All traced to cost/payment contracts |
| Timed missions | 14 | Complete activation, cancellation, timeout, and runtime cleanup |
| Operational selectable non-mission decisions without `ai_will_do` | 0 | Pass |

The broader prior audit results remain valid after remediation:

- exact population loss remains the source for Larder, Deaths, and recruitment accounting;
- no free recruitment, duplicate population consumption, or spawned-unit hidden strength path was introduced;
- humane, exploitation, convergence, unified, counterwar, and Wendigo route gates remain connected to their canonical effects;
- the active warlord origin set remains Island Host, Siege Commune, and March Host only;
- all 18 root achievement consumers still call their exact completion triggers and the 18 tracker decisions remain read-only;
- decision and category localisation, sprite definitions, category panels, and referenced Event 014 texture paths remain complete on the audited inventory.

## Files Reviewed and Changed for Finding Closure

Affordability constants and triggers:

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
- `common/scripted_effects/014_cannibalism_unified_decision_effects.txt`

Mission reset and scenario atomicity:

- `common/scripted_effects/014_cannibalism_core_effects.txt`
- `common/scripted_effects/014_cannibalism_objective_effects.txt`
- `common/script_constants/014_cannibalism_scenario_constants.txt`
- `common/scripted_triggers/014_cannibalism_scenario_triggers.txt`
- `common/scripted_effects/014_cannibalism_scenario_effects.txt`

Documentation:

- `docs/events/014_cannibalism.md`
- this final reaudit
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_decision_mission_findings_remediation_handoff_2026-07-15.md`

## References Consulted

Project guidance and skills:

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

Offline Paradox wiki snapshot:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- Interface Modding
- Graphical asset modding

Vanilla documentation:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`

Vanilla mission precedents:

- `common/decisions/ETH.txt`, `ETH_hold_harar_mission`
- `common/decisions/BALTIC.txt`, `BALTIC_forest_brothers_resistance`
- `common/decisions/CHI_decisions.txt`, `CHI_holding_state_mission`

## Validation Evidence

Task-specific final checks against the live tree produced:

- 127 decision entries, 94 custom affordability triggers, and 14 timed missions;
- 74 paid static strict gates with zero cost/gate delta errors;
- 43 derived unified runtime gates with zero missing assignments, adjustments, or trigger uses;
- exact set equality between all 14 timed mission IDs and the all-mission reset helper;
- zero outcome-setting flags in the 13 non-terminal family runtime clear helpers;
- exact equality between every profile/intensity preflight requirement and its downstream planned-state/slot consumption;
- explicit no-double-count exclusions across all planned state arrays;
- preflight call order before the first runtime mutation, success history only after setup success, and automatic prefire forced onto the non-manifest path.

The optional Event Chain Viewer lint could not persist an artifact because the shared artifact store reported `ARTIFACT_STORAGE_LIMIT`. Source inspection and the independent task-specific validators above did not depend on that optional artifact.

## Simplifications, Omissions, and Blockers

None. All three findings were implemented across their full Event 014 surfaces. No fallback, placeholder, omitted route, weakened substitute, or unresolved blocker remains in the assigned scope.
