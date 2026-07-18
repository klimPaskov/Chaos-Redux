# Event 19 Decision and Mission Independent Audit — 2026-07-16

## Audit result

The final live-source audit found no unresolved decision, mission, category, Muster Board, scenario-lock, controlled one-formation combat-trial, or exact recorded-formation recreate/prove/delete defects.

| Severity | Unresolved findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |

One P1 candidate was identified during the audit: the Muster Board could invoke Counter-Command and Discredit through their shared effects without observing the decision-only `days_re_enable`. The implementation owner repaired the shared trigger/effect contract while the audit was active. The final source was reread and the issue is closed; it is not included in the unresolved count.

This auditor changed no gameplay, localisation, interface, asset, specification, or spreadsheet source. This report is the only file written by the auditor.

## Scope and method

The audit inspected the final live Event 19 source rather than relying on an earlier handoff or report. Coverage included:

- all ordinary, claimant, and derivative decision definitions;
- all Event 19 mission definitions and their activation, timeout, cancellation, reactivation, and cleanup paths;
- all three decision categories;
- Muster Board click effects, enable triggers, list selection, and AI-equivalent paths;
- scenario transaction locks, setup, rollback, and history isolation;
- controlled one-formation combat-trial eligibility, cost, start, callback, victory, cancellation, and cleanup paths;
- exact recorded-formation recreate/prove/delete gates and parent isolation;
- unit-family registry train/spawn capability dispatch;
- decision and GUI costs, refunds, cooldowns, AI weights, localisation, icons, and textures.

Required offline references consulted before source review were `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`, `Interface modding`, `Scripted GUI modding`, `Division modding`, and `Unit modding` from `paradox_wiki/`.

Official documentation consulted included:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md`;
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`;
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/_documentation.md`;
- the relevant trigger, effect, variable, script-concept, and script-constant documentation under the vanilla `documentation/` and `common/script_constants/` directories.

The principal vanilla precedent was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/BALTIC.txt`: its custom-cost decisions confirm that the custom trigger/text are presentation and availability contracts while the completion path performs the debit; its missions also provide activation, cancellation, timeout, and reactivation precedents. Event 19 follows that split through shared can-triggers and transactional pay/refund effects.

## Exact inventory proof

The first-level definitions in the three Event 19 decision files contain exactly **68 decisions and 14 missions**, matching the required matrix in `docs/specs/019_infantry_spawn_specs/matrices/019_decision_mission_map.md:92-116`.

### Ordinary and Muster Board decisions — 39

Source: `common/decisions/019_infantry_spawn_decisions.txt:10-897`.

1. `infantry_spawn_open_muster_board`
2. `infantry_spawn_select_next_ordinary_lot`
3. `infantry_spawn_select_next_unaccounted_lot`
4. `infantry_spawn_settle_selected_lot_obligations`
5. `infantry_spawn_audit_selected_lot`
6. `infantry_spawn_assign_territorial_roles`
7. `infantry_spawn_open_standardization_cycle`
8. `infantry_spawn_supervised_demobilization`
9. `infantry_spawn_emergency_field_integration`
10. `infantry_spawn_establish_muster_districts`
11. `infantry_spawn_appoint_integration_staff`
12. `infantry_spawn_issue_common_tables`
13. `infantry_spawn_preserve_specialist_companies`
14. `infantry_spawn_recognize_emergency_reserve`
15. `infantry_spawn_survey_formation_lots`
16. `infantry_spawn_open_training_cycle`
17. `infantry_spawn_reserve_rail_corridors`
18. `infantry_spawn_preserve_prototype_formation`
19. `infantry_spawn_cannibalize_advanced_lot`
20. `infantry_spawn_request_field_reinforcement`
21. `infantry_spawn_request_mobile_reserve`
22. `infantry_spawn_request_territorial_defenders`
23. `infantry_spawn_request_specialist_firepower`
24. `infantry_spawn_request_numbers`
25. `infantry_spawn_request_discipline`
26. `infantry_spawn_request_firepower`
27. `infantry_spawn_request_mobility`
28. `infantry_spawn_request_anything`
29. `infantry_spawn_request_selected_anomalous_family`
30. `infantry_spawn_open_selected_family_cantonment_decision`
31. `infantry_spawn_appoint_selected_family_liaison_decision`
32. `infantry_spawn_restrict_selected_family_deployment_decision`
33. `infantry_spawn_sustain_selected_family_decision`
34. `infantry_spawn_seal_selected_family_breach_decision`
35. `infantry_spawn_disperse_selected_anomalous_lot_decision`
36. `infantry_spawn_achievement_one_battalion_combat_trial`
37. `infantry_spawn_achievement_combined_arms_combat_trial`
38. `infantry_spawn_achievement_borrowed_future_combat_trial`
39. `infantry_spawn_achievement_barracks_of_babel_combat_trial`

### Claimant decisions — 6

Source: `common/decisions/019_infantry_spawn_claimant_decisions.txt:9-156`.

1. `infantry_spawn_recognize_claimant`
2. `infantry_spawn_accept_claimant_demand`
3. `infantry_spawn_refuse_claimant_demand`
4. `infantry_spawn_counter_command_claimant`
5. `infantry_spawn_discredit_claimant`
6. `infantry_spawn_arrest_claimant`

### Derivative decisions — 23

Source: `common/decisions/019_infantry_spawn_derivative_decisions.txt:26-604`.

1. `infantry_spawn_derivative_rotate_collective_commands_decision`
2. `infantry_spawn_derivative_centralize_collective_muster_decision`
3. `infantry_spawn_derivative_ratify_species_compacts_decision`
4. `infantry_spawn_derivative_proclaim_family_primacy_decision`
5. `infantry_spawn_derivative_secure_muster_depot_decision`
6. `infantry_spawn_derivative_authorize_base_zombie_training_decision`
7. `infantry_spawn_derivative_rally_zombie_band_decision`
8. `infantry_spawn_derivative_manifest_ghost_host_decision`
9. `infantry_spawn_derivative_bind_golem_host_decision`
10. `infantry_spawn_derivative_pay_family_sustainment_decision`
11. `infantry_spawn_derivative_rally_claimant_guard_decision`
12. `infantry_spawn_derivative_establish_sustainment_site_decision`
13. `infantry_spawn_derivative_offer_zombie_containment_decision`
14. `infantry_spawn_derivative_offer_ghost_border_recognition_decision`
15. `infantry_spawn_derivative_offer_golem_material_agreement_decision`
16. `infantry_spawn_derivative_integrate_zombie_muster_district_decision`
17. `infantry_spawn_derivative_recognize_ghost_anchor_district_decision`
18. `infantry_spawn_derivative_bind_golem_foundry_district_decision`
19. `infantry_spawn_derivative_suppress_fragmentation_decision`
20. `infantry_spawn_derivative_break_former_parent_command_net_decision`
21. `infantry_spawn_derivative_demand_local_submission_decision`
22. `infantry_spawn_derivative_preserve_claimant_decision`
23. `infantry_spawn_derivative_replace_claimant_decision`

### Missions — 14

Ordinary source: `common/decisions/019_infantry_spawn_decisions.txt:903-1041`. Derivative source: `common/decisions/019_infantry_spawn_derivative_decisions.txt:465-484,567-625`.

1. `infantry_spawn_achievement_combat_trial_mission`
2. `infantry_spawn_formation_roll_call_mission`
3. `infantry_spawn_standardization_cycle_mission`
4. `infantry_spawn_supervised_demobilization_mission`
5. `infantry_spawn_training_cycle_mission`
6. `infantry_spawn_muster_districts_mission`
7. `infantry_spawn_officer_search_mission`
8. `infantry_spawn_specialist_preservation_mission`
9. `infantry_spawn_prototype_maintenance_trial_mission`
10. `infantry_spawn_rail_corridor_mission`
11. `infantry_spawn_request_cooldown_mission`
12. `infantry_spawn_derivative_integrate_conquered_district_mission`
13. `infantry_spawn_derivative_submission_warning_mission`
14. `infantry_spawn_derivative_survive_former_parent_front`

### Categories — 3

- `infantry_spawn_formation_management_category` — `common/decisions/categories/019_infantry_spawn_decision_categories.txt:11-36`;
- `infantry_spawn_claimant_category` — `common/decisions/categories/019_infantry_spawn_claimant_categories.txt:10-20`;
- `infantry_spawn_derivative_operations_category` — `common/decisions/categories/019_infantry_spawn_derivative_decision_categories.txt:10-25`.

There is no additional top-level Event 19 scenario decision in these files. Scenario launch belongs to the shared triggerable-scenario framework; its Event 19 host, transaction, setup, rollback, and actor-isolation contracts were audited as dependencies of the decision and GUI surfaces.

## Evidence matrix

| Surface | Live-source evidence | Result |
| --- | --- | --- |
| Definition completeness | The three files contain 68 decision entries and 14 mission entries. Every decision has an icon, `complete_effect`, and `ai_will_do`; every mission has an icon and timeout effect. | Pass |
| Category isolation | Ordinary, claimant, and derivative categories all require an idle scenario transaction; ordinary excludes derivatives and derivative requires derivative identity (`common/decisions/categories/019_infantry_spawn_decision_categories.txt:13-34`, `...claimant_categories.txt:12-18`, `...derivative_decision_categories.txt:12-22`). | Pass |
| Muster Board isolation | Board availability requires an idle scenario transaction, an active ordinary Event 19 host, the correct evolution state, and no derivative/world-end state (`common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt:10-17`). | Pass |
| GUI action parity | Muster Board clicks call the same effects as the decisions, and enabled states call the same can-triggers (`common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:22-103,105-205`). Action effects revalidate the authoritative trigger before payment or mutation (`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:538-729`). | Pass |
| Selected-lot integrity | Selected indexes are bounded and unresolved/anomalous state is checked (`common/scripted_triggers/019_infantry_spawn_triggers.txt:605-630`). Settlement uses preflight and exact obligation commit (`common/scripted_effects/019_infantry_spawn_management_effects.txt:2458-2611`); standardization, demobilization, specialist preservation, prototype proof, and cannibalization retain the selected immutable lot identity (`...management_effects.txt:649-796,3103-3237,3719-3960`). | Pass |
| Costs and rollback | Request costs are refreshed, loaded, paid, snapshotted, refunded on failure, dispatched, and verified before commit (`common/scripted_effects/019_infantry_spawn_management_effects.txt:4011-5076`). Family requests follow the same pay/materialize/verify/commit ordering (`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:857-1262`). | Pass |
| AI behavior | All 68 decisions define `ai_will_do`. The seven player selection/action entries that are deliberately UI-disabled for AI have an AI-equivalent family loop (`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1522-1611`) invoked by the Event 19 pulse (`common/scripted_effects/019_infantry_spawn_pulse_effects.txt:50`). | Pass |
| Scenario transaction safety | Launch inputs, valid host, and surviving hostile roster are separately checked (`common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:13-22,31-200,212-236`). Same-tag and dynamic-actor rollback delete and prove package objects before unlocking (`common/scripted_effects/019_infantry_spawn_scenario_effects.txt:1827-1989,2222-2363`); final actor setup proves provider and isolation state (`...scenario_effects.txt:2436-2673`). | Pass |
| Ordinary history isolation | Ordinary evolution history rejects derivative, scenario actor, dynamic breakaway, takeover actor, and setup-bypass identities (`common/scripted_triggers/019_infantry_spawn_triggers.txt:44-55`). Management, family-request, claimant-request, and incident writes use that guard before Event 19 progression counters (`common/scripted_effects/019_infantry_spawn_management_effects.txt:39-79,5040-5058,5698-5715`; `...muster_board_effects.txt:1195-1230`; `...claimant_demand_effects.txt:407-441`). | Pass |
| Parent isolation and recorded formation | Derivative identity requires the parent event identity to be absent (`common/scripted_triggers/019_infantry_spawn_triggers.txt:1027-1103`). Natural derivative creation freezes the source, recreates its recorded unit data, proves the destination package and unchanged global state, then deletes the exact source only after proof (`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:1578-2593,5198-5270`). | Pass |
| Unit-family capability dispatch | Zombie base formations register as trainable and use the training path; Ghost and Golem formations register as spawn-only and use their spawn paths (`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4112-4260,4348-4486,4571-4719`). Muster Board, derivative, and scenario paths dispatch through those registered provider contracts. | Pass |
| Controlled one-formation combat trials | Eligibility requires exact generated identity and a locked recorded gate (`common/scripted_triggers/019_infantry_spawn_achievement_triggers.txt:160-245`). Attacker and defender state safety, exact frozen pair, and live-state checks are at `:249-451`. Costs are debited only after a successful start (`common/scripted_effects/019_infantry_spawn_achievement_effects.txt:1308-1368,1655-1724`); cleanup proves the exact opponent and clears the attacker marker and mission state (`:1428-1551`). Callback resolution rechecks the frozen pair before awarding (`events/019_infantry_spawn.txt:830-948`; `...achievement_effects.txt:1582-1643`). | Pass |
| Mission lifecycle | Ordinary mission starts are paired with explicit final cleanup removals (`common/scripted_effects/019_infantry_spawn_management_effects.txt:503-607,687,3139,3208,3353,3400,3497,3844,5054,7415-7424`). Derivative missions have cancel/timeout effects plus defeat/final cleanup removal (`common/decisions/019_infantry_spawn_derivative_decisions.txt:465-484,567-625`; `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:6732-6899,7152-7154,7372-7374`). | Pass |
| Localisation | All 85 player-facing definitions (68 decisions, 14 missions, 3 categories) have exact name and `_desc` keys: 170 of 170 present. All 209 unique direct decision/GUI tooltip and custom-cost references resolve in `localisation/english/019_infrantry_spawn_l_english.yml`. | Pass |
| Icons and textures | The audited decision/category/GUI sources reference 61 distinct sprites. Sixty Event 19 sprites resolve through `interface/019_infantry_spawn.gfx`; the remaining `GFX_tiled_window_transparent` is vanilla. Every referenced Event 19 texture file exists. | Pass |

## Closed during audit: claimant response cooldown parity

### Original condition

The two claimant decisions declared decision-local cooldowns at:

- `common/decisions/019_infantry_spawn_claimant_decisions.txt:101`;
- `common/decisions/019_infantry_spawn_claimant_decisions.txt:123`.

The Muster Board invoked their shared effects directly at `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:83-89`, and its enabled checks used the shared can-triggers at `:193-194`. Before remediation, those shared contracts did not carry the cooldown, so repeated GUI activation could bypass the decision-local restriction.

### Final live-source retest

- `infantry_spawn_can_counter_command_selected_claimant` rejects `infantry_spawn_counter_command_cooldown` at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:327-332`.
- `infantry_spawn_can_discredit_selected_claimant` rejects `infantry_spawn_discredit_claimant_cooldown` at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:335-340`.
- The shared Counter-Command effect sets the timed flag from `constant:infantry_spawn_timer.officer_search_days` at `common/scripted_effects/019_infantry_spawn_claimant_response_effects.txt:21-39`.
- The shared Discredit effect sets its corresponding timed flag at `common/scripted_effects/019_infantry_spawn_claimant_response_effects.txt:48-62`.
- Ordinary and derivative teardown clear both flags at `common/scripted_effects/019_infantry_spawn_management_effects.txt:7505-7506` and `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:108-109`.

Because the decisions and GUI both use the repaired shared can-trigger/effect pairs, both entry surfaces now enforce the same cost and cooldown contract. Status: **closed**.

## Tooling limitation

The required HOI4 MCP route was attempted. A first narrow event-inspect request rejected an incomplete selector; the corrected scan and GUI-inspect requests then failed with `ARTIFACT_STORAGE_LIMIT`. Consequently, no MCP render/compare artifact was available for this handoff. This limitation did not prevent direct inspection of the linked live decision, trigger, effect, scripted-GUI, event-callback, localisation, sprite, and texture sources, but it should remain visible rather than being presented as MCP-backed proof.

## Final verdict

The final source satisfies the required **68 decisions + 14 missions + 3 categories** inventory. The audited decision and mission surfaces share their authoritative gates and transactional effects, remain locked during scenario transactions, preserve ordinary-history and parent-isolation boundaries, provide AI-equivalent handling for UI-only family actions, and resolve their localisation and visual references.

Final unresolved severity count: **P0 0 / P1 0 / P2 0**.

No implementation simplification or omission was introduced by this audit. The only audit limitation is the explicitly recorded MCP artifact-storage failure above.
