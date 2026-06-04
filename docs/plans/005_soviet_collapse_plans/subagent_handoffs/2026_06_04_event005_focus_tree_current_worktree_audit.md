# Event 005 Soviet Collapse Focus Tree Audit Handoff

Date: 2026-06-04
Role: `chaosx_focus_tree_auditor`
Scope: current worktree state for Soviet Collapse focus files and focus reward helpers.

No gameplay files were patched. No files under `gfx/flags` or `interface/flags` were touched.

## References Consulted

- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla focus examples: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`, `baltic_shared.txt`.
- Repo skill: `hoi4-focus-trees`.

## Files Audited

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- Related focus localisation files were located, but this pass did not perform localisation completeness patching.

## Mechanical Counts

Parsed current focus blocks:

- `005_soviet_collapse_republics.txt`: 501 focuses
- `005_soviet_collapse_custom_splinters.txt`: 1005 focuses
- `005_soviet_collapse_factory_successors.txt`: 128 focuses
- Total scoped focus blocks: 1634
- Scripted effects parsed in `005_soviet_collapse_effects.txt`: 764 top-level helper definitions

Idea reward count:

- Focus blocks with direct `add_ideas` or `add_timed_idea`: 0
- Focus blocks that call helper paths which add or swap ideas within two helper levels: 12
- Top-level helper definitions with direct `add_ideas`: 39
- `add_timed_idea` in audited helper definitions: 0

Current state does not show raw direct focus idea spam. The complaint remains partially valid through repeated staged-idea helper calls, mostly PRA and DSC/CFR helper paths.

## Idea/Helper Reward Findings

Focuses that currently call staged or idea-adding helper paths:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1207` `PRA_the_timetable_declares_authority` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1349` `PRA_the_board_overrules_ministers` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1380` `PRA_armored_train_directorate` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1547` `PRA_passport_of_the_moving_state` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1613` `PRA_league_transit_bargain` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1702` `PRA_rails_over_capitals` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1744` `PRA_flags_on_every_station` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1773` `PRA_the_pale_line_endures` -> `soviet_collapse_update_pra_authority_idea`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3184` `DSC_armies_that_do_not_demobilize` -> dead-army politics update path
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3234` `DSC_congress_of_the_dead_army` -> dead-army politics update path
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3272` `DSC_memorial_frontier_state` -> dead-army politics update path
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1035` `CFR_pour_the_final_foundation` -> `soviet_collapse_apply_cfr_raise_factory_city_belt`

Idea helper details:

- `common/scripted_effects/005_soviet_collapse_effects.txt:7610` `soviet_collapse_update_pra_authority_idea` removes all PRA authority ideas and re-adds one of `pra_moving_state_authority`, `pra_corridor_toll_authority`, `pra_railway_guard`, or `pra_timetable_sovereignty_board`. This is a good staged-idea lifecycle pattern, but eight PRA focuses call it, so it can read as repeated idea reward churn unless the focus tooltip clearly frames it as authority-state progression.
- `common/scripted_effects/005_soviet_collapse_effects.txt:16504` `soviet_collapse_update_dsc_dead_army_idea` adds `dsc_dead_army_politics`; it is reached by late DSC focus/endgame paths.
- `common/scripted_effects/005_soviet_collapse_effects.txt:10801`, `10869`, and `10907` add guarded `cfr_construction_mandates`; the guards avoid duplicate visible ideas, but the same idea is still used as the main visible institution for several CFR construction rewards.
- `common/scripted_effects/005_soviet_collapse_effects.txt:11523` and `11537` add `mfr_arsenal_quotas` / `mfr_factory_guard_state`; these are narrower and better than direct focus idea spam.

No focus block had duplicate identical helper calls in the same completion reward in this audit.

## Worst Generic Or Repeated Reward Surfaces

The dominant helper calls in focus rewards are still broad, reusable reward wrappers:

- 141 calls: `soviet_collapse_apply_focus_depot_and_supply_control`
- 132 calls: `soviet_collapse_apply_focus_military_consolidation`
- 104 calls: `soviet_collapse_apply_focus_legal_recognition`
- 80 calls: `soviet_collapse_apply_focus_republican_compact_plan`
- 65 calls: `soviet_collapse_apply_focus_foreign_channel`
- 60 calls: `soviet_collapse_apply_focus_high_chaos_identity`
- 58 calls: `soviet_collapse_apply_focus_security_supply_plan`
- 52 calls: `soviet_collapse_apply_focus_league_preparation`
- 38 calls: `soviet_collapse_apply_custom_splinter_league_identity`
- 36 calls: `soviet_collapse_apply_custom_splinter_enemy_front_identity`

Worst focus examples where the reward is mostly generic helper identity rather than focus-specific mechanics:

- `005_soviet_collapse_republics.txt:54` `ukr_soviet_collapse_guard_the_telegraph_house` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:145` `ukr_soviet_collapse_question_of_statehood` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:164` `ukr_soviet_collapse_war_without_a_declaration` -> `soviet_collapse_apply_focus_military_consolidation`
- `005_soviet_collapse_republics.txt:268` `ukr_soviet_collapse_black_banner_compact` -> `soviet_collapse_apply_focus_high_chaos_identity`
- `005_soviet_collapse_republics.txt:308` `ukr_soviet_collapse_elections_under_shellfire` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:531` `ukr_soviet_collapse_officers_above_parties` -> `soviet_collapse_apply_focus_military_consolidation`
- `005_soviet_collapse_republics.txt:616` `ukr_soviet_collapse_the_commander_or_the_cabinet` -> `soviet_collapse_apply_focus_military_consolidation`
- `005_soviet_collapse_republics.txt:940` `ukr_soviet_collapse_republic_of_laws` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:961` `ukr_soviet_collapse_civilian_command_over_the_army` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:2345` `soviet_collapse_guard_the_radio_stations` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:2375` `soviet_collapse_factory_defense_committees` -> `soviet_collapse_apply_focus_military_consolidation`
- `005_soviet_collapse_republics.txt:3133` `internal_soviet_collapse_convene_republic_presidium` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:4592` `baltic_soviet_collapse_restore_the_state_seal` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:4730` `baltic_soviet_collapse_military_border_government` -> `soviet_collapse_apply_focus_military_consolidation`
- `005_soviet_collapse_republics.txt:5551` `caucasus_soviet_collapse_convene_mountain_and_city_councils` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:5668` `caucasus_soviet_collapse_mountain_federal_compact` -> `soviet_collapse_apply_focus_legal_recognition`
- `005_soviet_collapse_republics.txt:6114` `caucasus_soviet_collapse_ancient_thrones_in_the_mountains` -> `soviet_collapse_apply_focus_high_chaos_identity`
- `005_soviet_collapse_republics.txt:6185` `caucasus_soviet_collapse_no_one_owns_the_passes_alone` -> `soviet_collapse_apply_focus_republican_compact_plan`
- `005_soviet_collapse_custom_splinters.txt:13244-13329` custom splinter identity wrappers are repeated across many 47-focus trees; they centralize behaviour, but the wrapper naming and identical structure make the trees feel scaffolded.

These helpers are not empty: the scripted effects often advance route depth, add variables, unlock decisions, and trigger high-chaos payloads. The issue is presentation and country specificity: many focus rewards feel interchangeable because focus files call the same helper without a local named payload or route-specific follow-up.

## Branch Depth And Layout Findings

Shallow trees:

- `PRA_soviet_collapse_focus_tree`: 22 focuses. Has a distinctive staged rail idea and rail-guard mechanics, but is still short for a high-chaos successor.
- `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`: 18 focuses each. These are the clearest shallow-tree cases.
- `OGB_soviet_collapse_focus_tree`: 23 focuses.
- Most other custom splinter trees have 47 focuses, but many are built from the same identity helper scaffold. They have count depth, but not enough bespoke branch identity.

Ukraine layout risks:

- Coordinate audit found 21 adjacent close-pairs in the Ukraine tree. Close pairs are not always wrong, but this tree has many compressed unrelated branches.
- `005_soviet_collapse_republics.txt:642` `ukr_soviet_collapse_army_supremacy` requires `ukr_soviet_collapse_foreign_courts_notice_kyiv` and sits at `(8,7)`, while its other nearby military/cabinet nodes sit around `(9,6)` and `(10,8)`. This creates a political/foreign prerequisite line into a military mutually exclusive choice.
- `005_soviet_collapse_republics.txt:777` `ukr_soviet_collapse_free_soil_compromise` at `(24,9)` is a long jump from `ukr_soviet_collapse_elections_under_shellfire` at `(13,5)`.
- `005_soviet_collapse_republics.txt:891` `ukr_soviet_collapse_provincial_governors_or_elected_radas` depends on `rural_deputy_bloc` and `minority_autonomy_statutes`, then immediately chains to `appointed_governors` at `:918`; this is visually tight and mechanically odd because the fork setup is adjacent to only one visible route lock.

Belarus layout risks:

- `005_soviet_collapse_republics.txt:8988` `blr_soviet_collapse_council_bargains_with_forests` at `(6,7)` depends on `blr_soviet_collapse_forest_defense_staff` at `(28,3)`, a Manhattan distance of 26. This is a severe pathline crossing risk.
- `005_soviet_collapse_republics.txt:9393` `blr_soviet_collapse_guide_companies` at `(29,8)` depends on `blr_soviet_collapse_council_bargains_with_forests` at `(6,7)`, distance 24. This sends the line back across the tree.
- `005_soviet_collapse_republics.txt:9437` `blr_soviet_collapse_swamp_roads_closed` at `(27,9)` depends on `blr_soviet_collapse_national_council_of_minsk` at `(7,5)`, distance 24. This verifies the user complaint about Belarus layout ugliness.

Other long-edge examples:

- `005_soviet_collapse_republics.txt:8586` `moldova_soviet_collapse_republic_of_crossings` has long prerequisites from `(3,7)` and `(12,2)` to `(21,12)`.
- `005_soviet_collapse_republics.txt:10679` `kaz_soviet_collapse_steppe_federation_charter` depends from `(2,3)` to `(19,5)`.
- `005_soviet_collapse_factory_successors.txt:356` `CFR_cities_first` is 13 coordinate steps from `CFR_the_board_becomes_the_cabinet`; the entire CFR strategy fork is spread in a way that likely produces messy connector lines.

Mutex/branch usefulness risks:

- CFR first political fork: `CFR_elect_the_site_committees` `:133`, `CFR_publish_the_planners_charter` `:163`, `CFR_invite_the_foreign_contract_board` `:195`, `CFR_the_concrete_committee` `:226`. Four-way mutexes need stronger downstream exclusivity proof than the current shared construction board.
- CFR strategy fork: `CFR_cities_first` `:356`, `CFR_rails_first` `:388`, `CFR_factories_first` `:430`, `CFR_contracts_first` `:465`. These are mutually exclusive but appear to feed overlapping construction-reward logic.
- Baltic route fork: `baltic_soviet_collapse_legal_continuity_government` `:4695`, `military_border_government` `:4730`, `baltic_league_first` `:4765`, `foreign_protection_council` `:4796`. This is mechanically plausible, but the rewards should have route-specific follow-through and not just generic legal/military/foreign helper wrappers.
- Central Asia route fork: `central_asia_soviet_collapse_local_republic_council` `:6545`, `military_border_authority` `:6741`, `foreign_border_patronage` `:6950`, `turkestan_federation_road` `:6985`. Same concern: plausible route split, but it needs stronger branch-specific downstream mechanics.

## Chaos-Country OP/Aggression Needs

Existing high-chaos payload support is useful but not consistently surfaced per tree:

- `common/scripted_effects/005_soviet_collapse_effects.txt:8459` `soviet_collapse_apply_high_chaos_focus_payload` can spawn assault columns, add expansion claims, add conquer/antagonize AI strategy, and issue war goals or declarations in terminal/chaos conditions.
- `common/scripted_effects/005_soviet_collapse_effects.txt:10309` `soviet_collapse_apply_high_chaos_focus_identity_payload` grants high-chaos identity bonuses by successor type.

Needed helper surfaces:

- Per-tag signature escalation helper: `soviet_collapse_apply_<tag>_signature_escalation_focus`, called by mid and capstone focuses, not only by generic high-chaos wrapper.
- Per-tag aggression helper: `soviet_collapse_<tag>_launch_neighbor_wars` or `soviet_collapse_<tag>_issue_expansion_wargoals`, with AI strategies and validity guards.
- Per-tag decision unlock helper: `soviet_collapse_unlock_<tag>_mechanic_decisions`, so each chaos tree changes the decision category instead of only giving stats.
- Per-tag idea lifecycle helper: `soviet_collapse_update_<tag>_route_idea`, following the PRA staged-idea pattern but with fewer focus calls and clearer route thresholds.
- Per-tag capstone helper: `soviet_collapse_complete_<tag>_endgame`, bundling final claims/cores/wargoals/AI/faction or world-state effects.

Specific candidates:

- `FTH` / `BBH`: black-banner raids, anti-state commune spread, mobile tachanka columns, anti-puppet war goals, hostile AI against neighbors and SOV.
- `KRS`: naval mutiny, port seizure, convoy interdiction, dockyard/raiding decisions, maritime claims.
- `TSC`: anomaly research meter, radar/airbase spread, science missions that escalate into Siberian claims.
- `RMC`, `DSC`, `ICD`, `NRF`: death-state/revenant mobilization, casualty or memorial fuel, forced-march columns, aggressive anti-SOV and neighbor war helpers.
- `BSC`, `TNC`, `ALA`, `MRC`, `IUL`: regional federation or restoration mechanics with claims, protectorate offers, and pass/steppe/corridor wars.
- `UDC`, `SDZ`: loyalist/security reconquest tools, coups, archive blackmail decisions, stronger AI aggression.
- `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `BAC`, `ARD`, `NLC`: each needs a specific economy/war/diplomacy loop instead of only the shared 47-focus scaffold.
- `CFR` and `MFR`: already closest to mechanic-backed OP successors; deepen their construction/arms-market decision loops and make route capstones visibly aggressive.

## Good Helper Patterns To Reuse

- `soviet_collapse_update_pra_authority_idea` at `005_soviet_collapse_effects.txt:7610`: staged idea lifecycle with removal/replacement rather than direct idea stacking.
- `soviet_collapse_build_pra_corridor_network` at `:7653` and `soviet_collapse_spawn_pra_rail_guard_columns` at `:7700`: route-specific infrastructure, supply, template, and unit payloads.
- `soviet_collapse_unlock_league_unit_deployment_decisions` at `:2139`: focus-to-decision integration, useful for avoiding flat stat rewards.
- `soviet_collapse_apply_ukr_black_sea_hegemony` at `:7348` and `soviet_collapse_apply_ukr_outside_old_map_settlement` at `:7421`: claims/wargoals and postwar core settlement.
- `soviet_collapse_apply_focus_security_supply_plan` at `:8950`: equipment, mobile column, factory reward, route variables, and Soviet crisis pressure in one helper.
- `soviet_collapse_apply_high_chaos_focus_payload` at `:8459`: OP/aggression hook with claims, war goals/declarations, assault columns, and AI strategy.
- `soviet_collapse_apply_cfr_*` helpers at `:10801-10907`: guarded ideas plus construction depth variables, buildings, and AI strategy.
- `soviet_collapse_apply_mfr_convert_depots_to_arms_lines` at `:11537` and `soviet_collapse_apply_mfr_focus_client_arms_network` at `:11790`: arsenal-specific equipment, arms factories, quotas, and contract variables.

## Validation

Brace balance:

- `common/national_focus/005_soviet_collapse_republics.txt`: final depth 0, min depth 0
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: final depth 0, min depth 0
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: final depth 0, min depth 0
- `common/scripted_effects/005_soviet_collapse_effects.txt`: final depth 0, min depth 0

Flag-folder safety:

- `git status --short -- gfx/flags interface/flags` produced no output.

## Remaining Risks

- This was a text/structure audit, not an in-game screenshot audit. Layout findings are coordinate/pathline risks, not confirmed rendered screenshots.
- Localisation completeness was not exhaustively checked.
- No full-tree rewrite was attempted by design.
- No gameplay patches were made, so all findings remain queued for the parent implementation pass.
