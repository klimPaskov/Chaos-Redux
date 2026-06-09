# Event005 Soviet Collapse Focus Tree Audit Handoff

Timestamp: 2026-06-05 06:52:57 UTC

Role: Chaos Redux focus-tree audit subagent.

Scope audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Patched: no. This is a read-only audit handoff. The parent is continuing implementation locally, and the four focus files are already dirty, so I avoided gameplay edits. I did not touch `gfx/`, flags, or sprite assets.

## References Consulted

- Skill: `hoi4-focus-trees`
- Repo rules: `AGENTS.md`
- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`
- Vanilla examples: `soviet.txt`, `baltic_shared.txt`, `uk.txt`
- Event005 focus spec: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`

## Findings

### High: pathline blockers from prerequisites beside or below child focuses

The parser found no duplicate focus IDs and no duplicate coordinates, but it found several prerequisites placed on the same row as, or below, their child. The offline focus wiki notes prerequisite focuses should be above children or the renderer can draw bad path sprites.

Priority fixes:

| File:line | Focus | Problem |
| --- | --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt:1347` | `ukr_soviet_collapse_german_liaison_question` | Prereq `ukr_soviet_collapse_foreign_courts_notice_kyiv` is on same row at `:724`. |
| `common/national_focus/005_soviet_collapse_republics.txt:1465` | `ukr_soviet_collapse_equipment_corridor_authority` | Prereq `ukr_soviet_collapse_ports_need_soldiers` is on same row at `:1937`. |
| `common/national_focus/005_soviet_collapse_republics.txt:2052` | `ukr_soviet_collapse_bread_state_whispers` | Prereq `ukr_soviet_collapse_breadbasket_empire` is below it at `:1775`. |
| `common/national_focus/005_soviet_collapse_republics.txt:2282` | `ukr_soviet_collapse_when_the_fields_refuse_the_state` | Prereq `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map` is below it at `:2029`. |
| `common/national_focus/005_soviet_collapse_republics.txt:2808` | `soviet_collapse_depots_choose_flags_branch` | Prereq `soviet_collapse_factory_defense_committees` is on same row at `:2381`. |
| `common/national_focus/005_soviet_collapse_republics.txt:3690` | `internal_soviet_collapse_idel_ural_congress` | Prereq `internal_soviet_collapse_kazan_ufa_workshop_board` is on same row at `:3635`. |
| `common/national_focus/005_soviet_collapse_republics.txt:7270` | `central_asia_soviet_collapse_the_southern_shield` | Prereq `central_asia_soviet_collapse_khwarazm_restoration_debate` is on same row at `:7457`. |
| `common/national_focus/005_soviet_collapse_republics.txt:9135` | `blr_soviet_collapse_red_without_the_center` | Prereq `blr_soviet_collapse_timetable_state` is below it at `:9331`. |
| `common/national_focus/005_soviet_collapse_republics.txt:9186` | `blr_soviet_collapse_liaison_hotels` | Prereq `blr_soviet_collapse_foreign_corridor_administration` is below it at `:9070`. |
| `common/national_focus/005_soviet_collapse_republics.txt:9582` | `blr_soviet_collapse_partisans_or_army` | Prereq `blr_soviet_collapse_the_green_rail_pact` is on same row at `:10048`. |
| `common/national_focus/005_soviet_collapse_republics.txt:10372` | `kaz_soviet_collapse_the_alash_courts` | Prereq `kaz_soviet_collapse_a_state_across_distances` is on same row at `:10297`. |
| `common/national_focus/005_soviet_collapse_republics.txt:11072` | `kaz_soviet_collapse_the_written_alash_program` | Prereq `kaz_soviet_collapse_lone_steppe_state` is below it at `:10848`. |
| `common/national_focus/005_soviet_collapse_republics.txt:11315` | `kaz_soviet_collapse_the_steppe_arbitration_court` | Prereq `kaz_soviet_collapse_steppe_federation_charter` is on same row at `:10792`. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt:557` | `CFR_construction_battalions` | Prereq `CFR_the_unfinished_city_speaks` is below it at `:113`. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt:696` | `CFR_the_city_without_citizens` | Prereq `CFR_the_concrete_committee` is below it at `:193`. |

### High: long AND prerequisite fans create tangled lines and hard-to-read routes

These are legal, but they are the main source of pathline clutter. Several are route finishers that require 4 to 9 separate completed focuses, causing long lines across branch lanes.

Worst examples:

- `soviet_collapse_armed_neutrality` at `common/national_focus/005_soviet_collapse_republics.txt:3037`: seven prerequisites.
- `moldova_soviet_collapse_republic_of_crossings` at `common/national_focus/005_soviet_collapse_republics.txt:8679`: eight prerequisites.
- `FEV_endgame` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:17351`: nine prerequisites.
- `SZA_endgame` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:18520`: nine prerequisites.
- `BAC_endgame` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:23159`: six prerequisites.
- `ARD_endgame` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:24358`: six prerequisites.
- `blr_soviet_collapse_minsk_supplies_the_front` at `common/national_focus/005_soviet_collapse_republics.txt:9852`: four prerequisites, including a mixed OR prerequisite block plus another separate prerequisite to `quiet_recognition_letters`.
- Ancient `old_border_files` foci at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:177`, `:586`, `:985`, and `:1393`: three prerequisites each in compact 16-focus trees, likely drawing a visible convergence knot.

Recommendation: for large fan-ins, choose one visible path prerequisite and move route proof into `available = { ... }` with custom trigger tooltip, or add a clean intermediate convergence focus directly above the finisher.

### Medium: same-row mutual-exclusion pairs are widespread

Same-row pairs are not always broken, but they crowd the mutual-exclusion marker and can make pathlines run through the symbol or between sibling focuses. This repeats across many custom splinters.

Most important examples:

- `kaz_soviet_collapse_steppe_federation_charter` vs `kaz_soviet_collapse_lone_steppe_state` at `common/national_focus/005_soviet_collapse_republics.txt:10792` and `:10848`.
- `PRA_the_board_overrules_ministers` vs `PRA_armored_train_directorate` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1376` and `:1406`.
- `TSC_the_committee_of_instruments` vs `TSC_the_committee_of_signs` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2000` and `:2033`.
- `RMC_communes_of_witnesses` vs `RMC_cadres_of_resurrection` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2447` and `:2478`.
- `DSC_witness_officers` vs `DSC_revenant_staff_line` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2938` and `:2970`.
- `NRF_living_harbor_committees` vs `NRF_revenant_admiralty` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3510` and `:3542`.
- `ICD_commissars_of_last_addresses` vs `ICD_commissars_who_do_not_die` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:4016` and `:4048`.
- `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, and `MFR_merchants_of_ammunition` at `common/national_focus/005_soviet_collapse_factory_successors.txt:1696`, `:1725`, and `:1753`.
- Ancient symbolic vs expansionist pairs at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:213`, `:622`, `:1021`, and `:1430`.

Recommendation: move one side of each pair down one row or use a central fork focus with route-specific child lanes separated by at least four x units and one y unit.

### Medium: compact chaos trees remain branch-light

The 18-focus high-chaos trees have concrete war/claim/endgame hooks, but several do not clearly expose all four requested branch families at playable depth.

Tree metrics from the scan:

| Tree | Count | Decision focuses | War focuses | Claim focuses | AI strategy focuses | Concern |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `TSC_soviet_collapse_focus_tree` | 18 | 3 | 1 | 0 | 1 | Political/industry/military exist, but diplomacy and expansion are very shallow. |
| `RMC_soviet_collapse_focus_tree` | 18 | 1 | 1 | 2 | 1 | Expansion exists, but decision integration is thin. |
| `NRF_soviet_collapse_focus_tree` | 18 | 6 | 1 | 2 | 3 | Better aggression, but branch depth is still compact for a special naval chaos actor. |
| `ICD_soviet_collapse_focus_tree` | 18 | 1 | 1 | 2 | 1 | Very thin decision integration outside the final high-chaos path. |
| `OGB_soviet_collapse_focus_tree` | 23 | 7 | 1 | mostly helper-driven | 2 | Much improved, but it still has only one direct war-goal focus and several generic/stat-only steps. |
| Ancient KZR/SOG/KHW/ALN trees | 16 each | 2 each | 1 each | 3 each | 1 each | They are functional compact trees, but political/industry/military/diplomacy/expansion are compressed into a narrow convergence shape. |

Recommendation: do not enlarge all compact trees blindly. Pick TSC and ICD first, then add one small diplomacy/decision lane and one visible expansion payoff per tree without rewriting the whole layout.

### Medium: chaos aggression is present but uneven

The audit found many high-chaos hooks: `soviet_collapse_spawn_custom_splinter_assault_columns*`, `soviet_collapse_apply_custom_splinter_expansion_claims*`, `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`, direct `create_wargoal`, and AI conquer/antagonize strategies.

Uneven spots:

- `TSC_soviet_collapse_focus_tree` has one war focus and no direct claim focus in the structural scan.
- `ICD_soviet_collapse_focus_tree` has one direct decision focus despite having strong late war hooks at `ICD_commissariat_without_end` (`common/national_focus/005_soviet_collapse_custom_splinters.txt:4321`).
- `OGB_soviet_collapse_focus_tree` gives a direct Soviet war goal only at `OGB_the_old_name_survives_modern_war` (`common/national_focus/005_soviet_collapse_factory_successors.txt:1523`), with earlier expansion mostly claims/decision-helper based.
- Ancient expansion routes are appropriately aggressive at `KZR_expansionist_steppe_levy` (`:240`), `SOG_expansionist_merchant_claims` (`:648`), `KHW_expansionist_water_claims` (`:1046`), and `ALN_expansionist_mountain_claims` (`:1455`), but each tree has only one main war-goal focus.

Recommendation: add aggression through route-specific decision unlocks and postwar coring/integration, not by adding more direct `create_wargoal` spam.

### Low: direct idea spam appears resolved, but indirect lifecycle helpers should stay under watch

Results:

- No duplicate focus IDs found across the four files.
- No duplicate coordinates found per focus tree.
- No direct duplicate `add_ideas` within a single focus found.
- No direct visible `add_ideas` focus spam found in the four focus files.

Indirect helper calls reviewed:

- `soviet_collapse_clear_focus_starting_tension_ideas` is called by `PRA_the_board_overrules_ministers` (`common/national_focus/005_soviet_collapse_custom_splinters.txt:1376`), `TSC_the_committee_of_instruments` (`:2000`), `RMC_communes_of_witnesses` (`:2447`), `DSC_witness_officers` (`:2938`), `NRF_living_harbor_committees` (`:3510`), `ICD_commissars_of_last_addresses` (`:4016`), and `OGB_the_council_takes_the_seal` (`common/national_focus/005_soviet_collapse_factory_successors.txt:1059`). Its helper body is hidden at `common/scripted_effects/005_soviet_collapse_effects.txt:5904`.
- `soviet_collapse_update_pra_authority_idea` is called by `PRA_the_timetable_declares_authority` (`:1230`), `PRA_armored_train_directorate` (`:1406`), `PRA_passport_of_the_moving_state` (`:1575`), and `PRA_league_transit_bargain` (`:1641`). It clears/adds one PRA authority spirit in hidden effect at `common/scripted_effects/005_soviet_collapse_effects.txt:8006`.
- `soviet_collapse_update_dsc_dead_army_idea` is called by `DSC_revenant_staff_line` (`common/national_focus/005_soviet_collapse_custom_splinters.txt:2970`) and is hidden at `common/scripted_effects/005_soviet_collapse_effects.txt:17386`.

This does not look like visible tooltip spam right now. The parent should still preserve the hidden helper pattern if editing these routes.

### Low: generic reward dumps remain in isolated focuses

Examples worth improving when those branches are touched:

- `PRA_armored_train_schools` (`common/national_focus/005_soviet_collapse_custom_splinters.txt:1542`): XP, command power, train equipment, tech, depot variable, buildings, and columns in one reward.
- `ICD_memorial_battalions` (`common/national_focus/005_soviet_collapse_custom_splinters.txt:4150`): manpower, support equipment, command power, variable gain, and every-owned-state bunkers.
- `MFR_workers_own_the_arsenal` (`common/national_focus/005_soviet_collapse_factory_successors.txt:2738`): variable gains, XP, manpower, command power, popularity, factory slot, and factory build.
- `KZR_caspian_patrol_letters` (`common/national_focus/005_soviet_collapse_ancient_restorations.txt:130`): multiple variables, navy XP, convoys, dockyard/naval base, and decryption in one focus.
- `ALN_alan_pass_charter` (`common/national_focus/005_soviet_collapse_ancient_restorations.txt:1505`): variable gains, command power, XP, forts, and bunkers in one focus.

Recommendation: when revisiting these, shift part of the payload to unlocked decisions or route-specific helper tooltips so the focus remains readable.

## Next-Tranche Recommendation Matrix

| Priority | Tranche | Files/foci | Recommended action | Collision risk |
| --- | --- | --- | --- | --- |
| 1 | Pathline repair | Ukraine, Belarus, Kazakhstan, CFR entries listed under High finding 1 | Move child or prerequisite coordinates so every visible prerequisite is above the child; keep IDs and rewards unchanged. | Medium, because parent may be editing these same trees. |
| 2 | Long fan-in cleanup | `soviet_collapse_armed_neutrality`, `moldova_soviet_collapse_republic_of_crossings`, `FEV_endgame`, `SZA_endgame`, `BAC_endgame`, `ARD_endgame` | Replace most visible prerequisite lines with a single convergence focus plus `available` route-proof and custom tooltip. | High, because it changes visible layout. |
| 3 | Same-row mutex polish | PRA/TSC/RMC/DSC/NRF/ICD, OGB, MFR, ancient symbolic/expansion pairs | Stagger mutual-exclusive children by one y row and keep siblings visually separated. | Low to medium if only coordinates change. |
| 4 | Compact chaos depth | TSC and ICD first; then RMC/NRF if time | Add one diplomacy/decision lane and one route-specific expansion/postwar decision payoff. | Medium, because it adds content. |
| 5 | Generic reward cleanup | PRA `:1542`, ICD `:4150`, MFR `:2738`, ancient `:130`/`:1505` patterns | Move large payloads behind helper tooltips or staged decisions; do not add new ideas unless replacing/upgrading an existing lifecycle. | Medium. |
| 6 | Final focus audit pass | All four files | Re-run ID/coordinate/prereq/mutex/idea scans after parent patches and then do manual screenshot-equivalent layout review in game if available to parent. | Low. |

## Validation Performed

- Parsed 41 focus trees and 1,698 focuses from the four requested files.
- Checked duplicate focus IDs: none found.
- Checked duplicate coordinates per tree: none found.
- Checked direct duplicate `add_ideas` within one focus: none found.
- Checked direct visible idea-add spam in focus files: none found.
- Checked indirect lifecycle helper call sites and helper bodies for hidden removal/add patterns.
- Checked direct war/claim/core/unit/decision/AI strategy occurrences for compact tree aggression.
- Checked same-row/below prerequisites, long prerequisite fan-ins, and same-row mutual exclusions.
- Reviewed representative blocks manually with `nl -ba` around the highest-risk findings.

## Status to Parent

Read-only audit complete. I did not patch gameplay files and do not claim completion of the parent Event005 goal. The main blockers to a clean completion claim are pathline cleanup in republic/factory trees, long fan-in route finishers, and branch-depth polish for the smallest high-chaos trees.
