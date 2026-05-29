# Soviet Collapse Focus Trees Current-State Audit

Timestamp: 2026-05-29 11:55:04 UTC  
Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Mode: read-only audit. No gameplay files were patched.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Required offline wiki pages from `paradox_wiki/`: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla documentation under `~/projects/Hearts of Iron IV/documentation/`, especially `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

## Concise Pass/Fail Table

| Focus tree | File line | Count | Status | Reason |
| --- | ---: | ---: | --- | --- |
| `soviet_collapse_ukraine_focus_tree` | republics:19 | 83 | Partial | Real width and route AI exist, but socialist/high-chaos helper refresh spam remains and the tree still has repeated helper cadence. |
| `soviet_collapse_breakaway_focus_tree` | republics:2317 | 36 | Fail | Generic fallback tree is still too shallow for political, military, diplomacy, and expansion depth. |
| `soviet_collapse_internal_republic_focus_tree` | republics:3104 | 62 | Partial | Good width, but branches remain generic and lack strong expansion/postwar hooks. |
| `soviet_collapse_baltic_focus_tree` | republics:4608 | 42 | Partial | Compact regional tree; defensive identity exists but expansion and decision mechanics are light. |
| `soviet_collapse_caucasus_focus_tree` | republics:5572 | 40 | Partial | Needs stronger mountain, oil, neighbor-conflict, and settlement mechanics. |
| `soviet_collapse_central_asia_focus_tree` | republics:6496 | 45 | Partial | Has some high-chaos/claim content, but route payoffs need decision/postwar handling. |
| `soviet_collapse_moldova_focus_tree` | republics:7628 | 48 | Partial | Dniester/Prut routes exist but updater spam and light payoff depth remain. |
| `soviet_collapse_belarus_focus_tree` | republics:8797 | 53 | Partial | Route AI exists, but military/security/foreign outcomes need more unique mechanics. |
| `soviet_collapse_kazakhstan_focus_tree` | republics:10123 | 92 | Partial | Broadest republic tree, but many rewards are helper/stat refreshes and flat AI weights. |
| `FTH_soviet_collapse_focus_tree` | custom:16 | 47 | Partial | Full shell exists with aggressive helper hooks, but still heavily template/helper-driven. |
| `PRA_soviet_collapse_focus_tree` | custom:1220 | 22 | Fail | Too shallow; railway state lacks full political, industry, military/diplomatic, expansion loops. |
| `TSC_soviet_collapse_focus_tree` | custom:1746 | 18 | Fail | Crisis ladder, not a full tree; needs special-mechanic and expansion depth. |
| `RMC_soviet_collapse_focus_tree` | custom:2216 | 18 | Fail | Death/cult premise is not matched by branch depth or aggressive mechanics until the end. |
| `DSC_soviet_collapse_focus_tree` | custom:2693 | 18 | Fail | Dead-army premise needs real army/economy/expansion branches. |
| `NRF_soviet_collapse_focus_tree` | custom:3167 | 18 | Fail | Fleet premise needs naval, port, raid, and expansion mechanics. |
| `ICD_soviet_collapse_focus_tree` | custom:3632 | 18 | Fail | Commissariat premise is a short ladder with limited mechanic payoff. |
| `BSC_soviet_collapse_focus_tree` | custom:4103 | 47 | Partial | Full shell exists; regional branches still rely on shared identity helpers. |
| `TNC_soviet_collapse_focus_tree` | custom:5233 | 47 | Partial | Full shell exists; regional branches still rely on shared identity helpers. |
| `ALA_soviet_collapse_focus_tree` | custom:6371 | 47 | Partial | Full shell exists; needs stronger Alash-specific political/expansion mechanics. |
| `BBH_soviet_collapse_focus_tree` | custom:7491 | 47 | Fail | Missing 3 icon sprite definitions and anarchist/raider route needs more direct mechanics. |
| `KRS_soviet_collapse_focus_tree` | custom:8695 | 47 | Partial | Port-council depth exists, but one direct updater plus identity helper remains. |
| `UDC_soviet_collapse_focus_tree` | custom:9938 | 47 | Partial | Command-network hooks exist; still template-heavy. |
| `SDZ_soviet_collapse_focus_tree` | custom:11139 | 47 | Partial | Archive-control hooks exist; still template-heavy. |
| `GAC_soviet_collapse_focus_tree` | custom:12384 | 47 | Partial | Full shell exists; needs more unique green-army route play. |
| `DHC_soviet_collapse_focus_tree` | custom:13567 | 47 | Partial | Host route has bespoke hooks, but repeated generic helper cadence remains. |
| `KHC_soviet_collapse_focus_tree` | custom:14773 | 47 | Partial | Host route has bespoke hooks, but repeated generic helper cadence remains. |
| `FEV_soviet_collapse_focus_tree` | custom:15972 | 47 | Partial | Far Eastern tree is broader than shallow crisis trees but has heavy icon reuse/helper reliance. |
| `SZA_soviet_collapse_focus_tree` | custom:17147 | 47 | Partial | Siberian route exists but needs deeper bespoke economy/expansion mechanics. |
| `UWD_soviet_collapse_focus_tree` | custom:18327 | 47 | Partial | Factory/rail logic exists but has heavy icon reuse/helper reliance. |
| `MRC_soviet_collapse_focus_tree` | custom:19529 | 47 | Partial | Mountain route exists; note lowercase `mrc_*` ids remain in this tree. |
| `IUL_soviet_collapse_focus_tree` | custom:20705 | 47 | Partial | Corridor/federal route exists but needs stronger Idel-Ural settlement decisions. |
| `BAC_soviet_collapse_focus_tree` | custom:21862 | 47 | Partial | Refuge/archive route exists but remains helper-heavy. |
| `ARD_soviet_collapse_focus_tree` | custom:23008 | 47 | Partial | Arctic/directorate route exists but remains helper-heavy. |
| `NLC_soviet_collapse_focus_tree` | custom:24183 | 47 | Partial | Many direct updater focuses remain in the winter/logistics branch. |
| `CFR_soviet_collapse_focus_tree` | factory:17 | 47 | Partial | Stronger than prior state; still icon reuse and compact reward cadence remain. |
| `OGB_soviet_collapse_focus_tree` | factory:1074 | 23 | Fail | Restoration route has war goals, but tree is still too short for full depth. |
| `MFR_soviet_collapse_focus_tree` | factory:1663 | 58 | Pass with cleanup | Strong factory successor with endpoint aggression; minor updater/icon cleanup only. |

## Idea / Updater / Helper Spam

No direct `add_ideas` or `swap_ideas` calls remain in the three focus files. Direct focus-file idea effects are cleanup-only `remove_ideas` calls:

- `PRA_the_board_overrules_ministers` removes `pra_dispatcher_court_tensions`.
- `TSC_the_committee_of_instruments` removes `tsc_field_station_rivalries`.
- `RMC_communes_of_witnesses` removes `rmc_credal_cell_rivalries`.
- `DSC_witness_officers` removes `dsc_grave_regiment_rivalries`.
- `NRF_living_harbor_committees` removes `nrf_drowned_crew_disputes`.
- `ICD_commissars_of_last_addresses` removes `icd_grave_commissar_rivalries`.
- `mrc_protect_village_autonomy` removes `mrc_pass_confederation_rivalries`.
- `OGB_the_council_takes_the_seal` removes `ogb_disputed_restored_name`.

Definite same-reward duplicate/update spam:

| Focus id | Location | Problem |
| --- | --- | --- |
| `ukr_soviet_collapse_the_ukrainian_commune_debate` | `005_soviet_collapse_republics.txt:482` | Calls both `soviet_collapse_apply_focus_socialist_sovereignty` and `soviet_collapse_apply_focus_high_chaos_identity`; both refresh consolidated republic ideas through helper internals. |
| `central_asia_soviet_collapse_khwarazm_restoration_debate` | `005_soviet_collapse_republics.txt:7443` | Calls `soviet_collapse_apply_focus_high_chaos_identity` and directly calls `soviet_collapse_update_consolidated_republic_ideas`. |
| `moldova_soviet_collapse_smugglers_and_border_committees` | `005_soviet_collapse_republics.txt:8647` | Calls `soviet_collapse_apply_focus_high_chaos_identity` and directly calls `soviet_collapse_update_consolidated_republic_ideas`. |
| `kaz_soviet_collapse_red_nomad_committees` | `005_soviet_collapse_republics.txt:11569` | Calls `soviet_collapse_apply_focus_socialist_sovereignty` and directly calls `soviet_collapse_update_consolidated_republic_ideas`. |
| `KRS_inner_faction` | `005_soviet_collapse_custom_splinters.txt:8917` | Calls `soviet_collapse_apply_custom_splinter_inner_faction_identity` and directly calls `soviet_collapse_update_consolidated_republic_ideas`. |

Adjacent direct updater refreshes:

| Tree | Adjacent focus edge |
| --- | --- |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_ports_need_soldiers` -> `ukr_soviet_collapse_equipment_corridor_authority` |
| `soviet_collapse_moldova_focus_tree` | `moldova_soviet_collapse_district_prefect_rolls` -> `moldova_soviet_collapse_republic_without_a_patron` |
| `soviet_collapse_moldova_focus_tree` | `moldova_soviet_collapse_neutral_bridge_statute` -> `moldova_soviet_collapse_republic_without_a_patron` |
| `soviet_collapse_moldova_focus_tree` | `moldova_soviet_collapse_romanian_aid_without_annexation` -> `moldova_soviet_collapse_prut_relief_depots` |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_aul_horse_registers` -> `kaz_soviet_collapse_horse_and_truck_columns` |
| `NLC_soviet_collapse_focus_tree` | `NLC_winter_road_columns` -> `NLC_apatity_rear_area` |

Template-wide helper cadence still reads like updater/helper spam even when not a literal duplicate call in one focus. The 47-focus custom splinter template prefixes `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, and `NLC` repeatedly call route identity helpers on adjacent focuses. The recurring exact suffixes are:

- `*_birth` direct updater.
- `*_first_guard`, `*_stores`, `*_legitimacy`, `*_rival`, `*_doctrine`, `*_economy`, `*_league`, `*_foreign`, `*_inner_faction`, `*_special_arm`, `*_supply`, `*_enemy_front`, `*_civil_rule`, `*_propaganda`, `*_settlement`, `*_industry_plan`, `*_hidden_doctrine`, and `*_extreme_gate` via `soviet_collapse_apply_custom_splinter_*_identity`.
- `*_war_plan` via `soviet_collapse_apply_custom_splinter_enemy_front_identity` where present.
- `*_extreme_path` via `soviet_collapse_apply_focus_high_chaos_identity`.

These helpers are useful centralization, but the player-facing reward layer still often becomes "same staged idea updater plus small variable/stat reward" instead of distinct branch mechanics. Parent should consolidate refresh calls so each route stage refreshes once after all variable changes, and reserve identity helpers for major route milestones.

## Route-Depth Failures

Highest-priority failures:

| Tree / branch | Exact focus ids | Missing depth |
| --- | --- | --- |
| Generic breakaway tree | `soviet_collapse_military_defense_council`, `soviet_collapse_republican_survival_pact`, `soviet_collapse_a_small_state_with_teeth`, `soviet_collapse_border_militia_standard`, `soviet_collapse_armed_neutrality`, `soviet_collapse_the_republic_endures`, `soviet_collapse_a_republic_worth_naming` | Needs real expansion and postwar mechanics, not only survival/stat helpers. |
| PRA | `PRA_the_board_overrules_ministers`, `PRA_armored_train_directorate`, `PRA_neutral_corridor_letters`, `PRA_charge_for_safe_passage`, `PRA_claim_the_branch_lines`, `PRA_seize_the_junction_cities`, `PRA_rails_over_capitals` | 22 focuses; needs separate political, industry/logistics, armored-train military, diplomacy/transit, and expansion branches. |
| TSC | `TSC_the_committee_of_instruments`, `TSC_observatory_guard`, `TSC_perimeter_regiments`, `TSC_letters_to_academies`, `TSC_claim_the_impact_zone`, `TSC_sky_over_siberia`, `TSC_starfall_mandate` | 18 focuses; needs a real anomaly/observatory mechanic, science diplomacy, aggressive perimeter, and postwar/impact-zone decisions. |
| RMC | `RMC_communes_of_witnesses`, `RMC_cadres_of_resurrection`, `RMC_reliquary_guard`, `RMC_dead_volunteer_columns`, `RMC_claim_the_burial_roads`, `RMC_procession_columns`, `RMC_resurrection_without_state` | 18 focuses; needs cult governance, shrine economy, undead/volunteer force loop, expansion, and aftermath mechanics. |
| DSC | `DSC_witness_officers`, `DSC_revenant_staff_line`, `DSC_dead_regiment_columns`, `DSC_maps_of_lost_armies`, `DSC_claim_the_soldiers_road`, `DSC_armies_that_do_not_demobilize`, `DSC_congress_of_the_dead_army` | 18 focuses; needs distinct army command, military industry, aggressive front, and unit/war logic. |
| NRF | `NRF_living_harbor_committees`, `NRF_revenant_admiralty`, `NRF_dead_convoy_supply_board`, `NRF_ghost_convoy_escorts`, `NRF_claim_the_white_sea_lane`, `NRF_fleet_that_does_not_dock`, `NRF_northern_revenant_fleet` | 18 focuses; needs naval/convoy raiding, port control, dockyard, northern expansion, and attack AI mechanics. |
| ICD | `ICD_commissars_of_last_addresses`, `ICD_commissars_who_do_not_die`, `ICD_dead_roll_supply_bureau`, `ICD_memorial_battalions`, `ICD_claim_the_unburied_front`, `ICD_grave_columns_march`, `ICD_commissariat_without_end` | 18 focuses; needs commissariat governance, recruitment/terror loop, front expansion, and cleanup/aftermath. |
| OGB | `OGB_reopen_volga_trade_tolls`, `OGB_raise_the_heritage_guard`, `OGB_the_volga_cannot_have_two_seals`, `OGB_answer_the_idel_ural_question`, `OGB_claim_the_old_trade_cities`, `OGB_the_old_name_survives_modern_war` | 23 focuses; has war goals but lacks enough political, industrial, diplomatic, and restoration depth. |

Broader partial-depth issues:

- `soviet_collapse_baltic_focus_tree`, `soviet_collapse_caucasus_focus_tree`, `soviet_collapse_central_asia_focus_tree`, and `soviet_collapse_moldova_focus_tree` have compact regional routes but need more decision/missions, postwar settlement, claims/cores, and AI strategy connections.
- `soviet_collapse_kazakhstan_focus_tree` is large enough, but too many routes still pay off through repeated staged idea helpers instead of unique mechanics.
- The full 47-focus custom splinters have enough scaffolding for political, economy, military, diplomacy, and high-chaos routes, but the middle branches are still template-heavy. Parent should replace repeated helper milestones with tag-specific mechanics where the country concept demands it.

## Chaos-Country Aggression

Current aggressive hooks that do exist:

- `soviet_collapse_apply_custom_splinter_expansion_claims` cores all controlled non-core states, creates a war goal on `SOV`, and creates war goals on non-allied neighbors.
- That helper is called by `soviet_collapse_apply_custom_splinter_extreme_gate_identity` and by `soviet_collapse_apply_custom_splinter_war_plan_bonus` when the war-plan payoff gate is active.
- `soviet_collapse_spawn_custom_splinter_assault_columns` exists in the custom splinter aggression path.
- Shallow crisis trees have direct endpoint war goals: `PRA_rails_over_capitals`, `TSC_starfall_mandate`, `RMC_resurrection_without_state`, `DSC_congress_of_the_dead_army`, `NRF_northern_revenant_fleet`, and `ICD_commissariat_without_end`.
- Factory successors have direct endpoint war goals and AI attack pushes: `CFR_rebuild_russia_without_moscow`, `OGB_the_volga_cannot_have_two_seals`, `OGB_the_old_name_survives_modern_war`, and `MFR_eternal_arsenal_marches`.

Remaining aggression gaps:

- `soviet_collapse_apply_focus_high_chaos_identity` only changes variables/pressure and refreshes ideas; it does not grant factories, units, cores, claims, war goals, or attack AI. Any branch that only uses this helper is not meeting the "extremely overpowered chaos country" requirement.
- Most full custom splinters delay real aggression until `*_hidden_doctrine`, `*_war_plan`, `*_extreme_gate`, or `*_extreme_path`. Early and mid-route chaos focuses still feel like staged-helper reward cadence.
- Tag-specific attack behavior is mostly generic. `common/ai_strategy/005_soviet_collapse.txt` has generic custom/high-chaos force routes and route AI for Ukraine, Belarus, and Kazakhstan, but not full tag-specific aggressive plans for every custom splinter.

## Layout / Pathline Audit

Mechanical parser results across all three scoped files:

- Focus trees parsed: 37.
- Focus blocks parsed: 1,634.
- Duplicate focus coordinates per tree: 0 found.
- Straight-line prerequisite blockers: 0 found.
- Focuses sitting between same-row or same-column mutually exclusive endpoints: 0 found.

No exact current layout/pathline failures were found by this audit. This does not replace an in-game screenshot pass, but it covers duplicate coordinates and the obvious straight-line pathline failures that were present before recent layout cleanup.

## Icon Coverage

| Tree group | Status |
| --- | --- |
| All scoped trees | Every focus has an `icon = ...` assignment. |
| All scoped trees except BBH | Referenced focus icon ids resolve to interface sprite definitions. |
| `BBH_soviet_collapse_focus_tree` | Missing sprite definitions for `GFX_focus_generic_military_academy` on `BBH_column_schools`, `GFX_focus_generic_self_management` on `BBH_commune_mediation`, and `GFX_focus_generic_diplomatic_treaty` on `BBH_non_domination_pacts`. |
| Repeated icon groups | Still visually noisy in several trees: `FEV` has 13 repeated icon groups, `SZA` 12, `UWD` 15, `MRC` 12, `IUL` 15, `CFR` 11. Republic trees have smaller repeated groups except Kazakhstan, which has no repeated focus icons in this parse. |

## Localisation And Reward Mismatch

- Missing focus name/description localisation pairs: 0 found for all 1,634 parsed focuses.
- The remaining mismatch is design-level rather than missing keys: many titles/descriptions promise institutional consolidation, route transformation, or dangerous splinter escalation while the reward is still mostly a staged idea refresh, small variable gain, equipment stockpile, or generic helper.
- Direct idea spam in focus files is mostly gone. Remaining visible spam risk comes from helper internals and repeated refresh cadence.

## AI Behavior Gaps

Every parsed focus has an `ai_will_do` block.

Flat or weakly route-aware focus AI remains:

- Republic file: Ukraine has 27 flat focus weights, generic breakaway 18, internal republic 25, Baltic 18, Caucasus 23, Central Asia 15, Moldova 20, Belarus 12, Kazakhstan 61.
- Custom splinters: older/full template trees mostly have modifier blocks, but `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, and `ARD` still have 9-13 flat focus weights each.
- Factory successors: all focus AI blocks have modifiers, but route-level AI strategy is still strongest only at endpoints.

Route-aware AI strategy coverage exists for Soviet crisis behavior, generic breakaway survival, custom/high-chaos force routes, Ukraine, Belarus, Kazakhstan, and foreign patrons. It does not yet provide tag-specific plans for every custom splinter's expansion style, target selection, war-plan timing, League behavior, or high-chaos escalation.

## Prioritized Implementation List

1. Fix the definite duplicate updater/helper rewards first: `ukr_soviet_collapse_the_ukrainian_commune_debate`, `central_asia_soviet_collapse_khwarazm_restoration_debate`, `moldova_soviet_collapse_smugglers_and_border_committees`, `kaz_soviet_collapse_red_nomad_committees`, and `KRS_inner_faction`.
2. Collapse adjacent direct updater refreshes into one final refresh at the last focus in each edge listed above, after all variable changes are applied.
3. Add or swap icon sprite ids for `BBH_column_schools`, `BBH_commune_mediation`, and `BBH_non_domination_pacts`.
4. Redesign the shallow crisis trees: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD`. These need full branch families, not small local patches.
5. Expand `OGB_soviet_collapse_focus_tree` from a short restoration tree into a real restoration state tree with politics, industry, diplomacy, military, expansion, and postwar handling.
6. Replace the custom splinter template's repeated identity-helper cadence with fewer route-stage refreshes and more tag-specific mechanics: decisions, missions, units, cores, claims, war goals, factories, and postwar integration.
7. Upgrade `soviet_collapse_apply_focus_high_chaos_identity` call sites that represent actual chaos routes. Either use stronger bespoke helpers or add follow-on focuses/decisions so high-chaos paths do more than pressure variables.
8. Add tag-specific AI strategy plans for custom splinter aggression and expansion timing. Prioritize the chaos/death/raider trees and the shallow crisis trees.
9. Add postwar handling to regional republic expansion routes, especially Baltic, Caucasus, Central Asia, Moldova, and the generic breakaway tree.
10. After depth work, rerun the icon repetition pass and replace repeated high-frequency icons in `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, and `CFR`.

## Validation Run

Read-only validation performed:

- Parsed focus trees, focus ids, coordinates, prerequisites, mutual exclusions, icon ids, localisation keys, and `ai_will_do` blocks.
- Checked duplicate coordinates per tree.
- Checked straight-line prerequisite blockers.
- Checked same-row/same-column focuses between mutual-exclusion endpoints.
- Checked focus icon definitions against `interface/*.gfx`.
- Checked focus name and description keys against `localisation/english/*.yml`.

Skipped validation:

- No gameplay files were edited.
- No full HOI4 launch or external parser run was performed.
- No screenshot validation was performed, so dense curved/engine-routed path visuals still need in-game review after parent edits.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
