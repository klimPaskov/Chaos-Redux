# Event005 Soviet Collapse Focus Tree Full Current-State Read-Only Audit

Role: `chaosx_focus_tree_auditor`
Date: 2026-06-04 19:39 UTC
Scope: Event 005 Soviet Collapse focus trees and directly related helper/localisation files.

This was a read-only audit of gameplay state. I did not patch focus files, helper files, localisation, assets, flags, or sprites. The only file written by this run is this handoff report.

## Skills and references used

- Repo skills: `hoi4-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`.
- Offline wiki pages consulted: `National focus modding`, `Data structures`, `Triggers`, `Effect`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`.
- Vanilla documentation consulted: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/ai_strategy/_documentation.md`, `common/decisions/_documentation.md`, `common/on_actions/_documentation.md`.
- Vanilla precedent inspected: `common/national_focus/generic.txt`, `common/national_focus/switzerland.txt`.
- Event specs consulted: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_3_decisions_missions_influence.md`, part 4, part 5, and part 6.

Key standards used from the references:

- Focus prerequisites are OR within one `prerequisite = { ... }` block and AND across multiple prerequisite blocks.
- Duplicate focus IDs can break focus path lines; none were found in the current audited files.
- Important focus trees need branch families with mechanical payoffs, not only flat modifier/stat rewards.
- Focuses should connect to decisions, missions, ideas, units, buildings, war goals, claims, cores, diplomacy, AI, events, or visible mechanics.
- Idea progression should use hidden lifecycle helpers and guarded swaps/removals, not visible repeated add/remove clutter.

## Files audited

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse*_l_english.yml`

## Current counts

Total current focus trees: 41.
Total current focus blocks: 1,698.
Duplicate focus IDs found: 0.
Focuses missing `ai_will_do`: 0.
Focus localisation coverage: 1,698 / 1,698 focus title and `_desc` keys found.

| File | Trees | Focus blocks |
| --- | ---: | ---: |
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 501 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25 | 1,005 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 4 | 64 |

Tree-level counts:

| File | Focus tree | Focuses |
| --- | --- | ---: |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree` | 83 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_breakaway_focus_tree` | 36 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | 62 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | 42 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_caucasus_focus_tree` | 40 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | 45 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | 48 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | 53 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_kazakhstan_focus_tree` | 92 |
| `005_soviet_collapse_custom_splinters.txt` | `FTH_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | 22 |
| `005_soviet_collapse_custom_splinters.txt` | `TSC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `DSC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `ICD_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `BSC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `TNC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ALA_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BBH_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KRS_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UDC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SDZ_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `GAC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `DHC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KHC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `FEV_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SZA_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UWD_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `MRC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `IUL_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BAC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ARD_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `NLC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_factory_successors.txt` | `OGB_soviet_collapse_focus_tree` | 23 |
| `005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 58 |
| `005_soviet_collapse_ancient_restorations.txt` | `KZR_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `SOG_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `ALN_soviet_collapse_ancient_focus_tree` | 16 |

## Highest-priority findings

1. Ukraine has three exact coordinate collisions that should be fixed before more route work:
   - `ukr_soviet_collapse_arsenal_cities` around `005_soviet_collapse_republics.txt:1115` and `ukr_soviet_collapse_army_of_the_republic` around `:1140` both resolve to `(23,6)`.
   - `ukr_soviet_collapse_great_steppe_and_sea_plan` around `:1921` and `ukr_soviet_collapse_dead_fields_living_columns` around `:2148` both resolve to `(34,12)`.
   - `ukr_soviet_collapse_black_banner_takes_the_villages` around `:2239` and `ukr_soviet_collapse_when_the_fields_refuse_the_state` around `:2316` both resolve to `(38,14)`.
2. Eleven trees are still shallow against the spec's branch-depth standard: `PRA` at 22, `TSC`/`RMC`/`DSC`/`NRF`/`ICD` at 18, `OGB` at 23, and all four ancient restoration trees at 16. These do not yet provide enough political, industry, military, diplomacy, expansion, and special-mechanic branch families for their intended identities.
3. The short high-chaos trees have layout/flow fragmentation. `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` each have three root focuses, with late side branches not visibly rooted in the opening trunk. Examples: `TSC_observatory_guard` around `005_soviet_collapse_custom_splinters.txt:2066`, `TSC_night_survey_columns` around `:2127`; `DSC_field_hospital_memorials` around `:3046`, `DSC_maps_of_lost_armies` around `:3132`.
4. Direct focus reward idea spam is currently controlled: no direct `add_ideas`, `remove_ideas`, or `swap_ideas` operations were found in the four focus files. The risk has moved into helper chains. The main lifecycle hotspots are `soviet_collapse_add_republic_focus_recovery_progress` at `005_soviet_collapse_effects.txt:4880`, `soviet_collapse_clear_republic_staged_ideas` at `:5655`, `soviet_collapse_clear_focus_starting_tension_ideas` at `:5825`, `soviet_collapse_update_pra_authority_idea` around `:7896`, `soviet_collapse_update_dsc_dead_army_idea` at `:17253`, and starting-idea helper blocks around `:17639-18228`.
5. Several focuses combine multiple high-impact helper packages in one completion. The temp-variable guard in `soviet_collapse_add_republic_focus_recovery_progress` prevents repeated recovery progress inside the same focus completion, but these rewards still read as over-bundled and can double-apply distinct route payload families. Highest-risk examples:
   - `kaz_soviet_collapse_the_southern_republics_do_not_kneel` around `005_soviet_collapse_republics.txt:11072`: calls League security, high-chaos identity, chaos assault, neighbor expansion, and neighbor conflict helpers.
   - `FTH_war_plan` around `005_soviet_collapse_custom_splinters.txt:455`: calls expansion claims, neighbor conflict, chaos assault, and security supply helpers.
   - `NLC_war_plan` around `005_soviet_collapse_custom_splinters.txt:24727`: same pattern plus direct construction/variable reward.
   - `PRA_armored_train_directorate` around `005_soviet_collapse_custom_splinters.txt:1406`: rail authority, PRA authority idea update, rail guard columns, and military consolidation in one focus.
6. Far Eastern/Pacific content exists but is still underpowered relative to the objective. `FEV_war_plan` around `005_soviet_collapse_custom_splinters.txt:16831`, `FEV_vladivostok_harbor_board` around `:16941`, `FEV_pacific_observer_missions` around `:17081`, `FEV_sakhalin_ferry_protocols` around `:17102`, `FEV_pacific_city_compact` around `:17127`, and `FEV_pacific_between_empires` around `:17288` should become stronger Pacific-facing mechanics, not mostly generic foreign/security helpers.
7. Naval actors need stronger naval mechanics and filters. `NRF` is only 18 focuses despite being a required naval revenant actor. `KRS` and `ARD` have more content, but focus filters and rewards are not consistently naval-facing. Review `KRS_war_plan` around `:9373`, `KRS_naval_infantry_oaths` around `:9930`, `KRS_port_guard_schools` around `:10030`, `ARD_murmansk_dockyard_sheds` around `:23648`, `ARD_naval_infantry_yards` around `:23860`, `ARD_foreign_fleet_letters` around `:24050`, `ARD_white_sea_port_tolls` around `:24097`, and `ARD_arctic_port_endurance` around `:24218`.
8. Several mutually exclusive branches are real but too small to feel like route differences. The weakest cases are two-focus or endpoint-only forks: `OGB_scholars_guard_the_charter` / `OGB_clerics_guard_the_charter`, `OGB_treat_with_idel_ural` / `OGB_the_volga_cannot_have_two_seals`, and the ancient symbolic-vs-expansion pairs at `KZR_symbolic_crossing_state` / `KZR_expansionist_steppe_levy`, `SOG_symbolic_city_league` / `SOG_expansionist_merchant_claims`, `KHW_symbolic_oasis_authority` / `KHW_expansionist_water_claims`, `ALN_symbolic_pass_principality` / `ALN_expansionist_mountain_claims`.
9. Some focus filters still do not match rewards. Representative current examples:
   - `BSC_hidden_doctrine` around `005_soviet_collapse_custom_splinters.txt:5401` and `BSC_extreme_gate` around `:5427` use expansion/neighbor helpers but lack `FOCUS_FILTER_ANNEXATION`.
   - `KRS_first_guard` around `:8980`, `KRS_sailors_assembly_registers` around `:9460`, and `KRS_free_soviet_congress` around `:9650` grant or imply naval rewards without consistent `FOCUS_FILTER_NAVY_XP`.
   - `ARD_murmansk_dockyard_sheds`, `ARD_white_sea_customs`, `ARD_foreign_fleet_letters`, `ARD_white_sea_port_tolls`, and `ARD_arctic_port_endurance` should be reviewed for `FOCUS_FILTER_NAVY_XP`.
   - `internal_soviet_collapse_far_eastern_port_authority` around `005_soviet_collapse_republics.txt:4238` and `internal_soviet_collapse_pacific_harbor_guard` around `:4274` should be reviewed for navy/industry filter alignment.

## Mechanics connection gaps

The focus files use many Soviet Collapse variables and helpers, so they are not disconnected from the event. The gap is that too many route endpoints still touch the shared mechanics generically instead of changing visible decisions, missions, or country-specific systems.

Priority gap groups:

- Progressive release and Union Unmade: several successor focus trees can pressure `SOV` through helper variables, but few route endpoints visibly alter release wave behavior, Union Unmade settlement, or scenario release/war behavior. Good candidates for hooks: `kaz_soviet_collapse_the_southern_republics_do_not_kneel`, `FEV_pacific_between_empires`, `ARD_endgame`, `KRS_endgame`, `DSC_congress_of_the_dead_army`, and all ancient restoration endgames.
- Influence/funding: diplomacy branches generally raise recognition, liaison, or foreign variables, but many do not unlock or modify foreign patron/funding decisions. Candidates: `FEV_pacific_observer_missions`, `FEV_sakhalin_ferry_protocols`, `BSC_diplomatic_plan`, `TNC_diplomatic_plan`, `ALA_diplomatic_plan`, `ARD_foreign_fleet_letters`, `KRS_free_port_conference`.
- League decisions: League-preparation helpers are used, but several focuses that promise League logistics or regional coordination do not clearly unlock a new League decision tier. Candidates: `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_minsk_supplies_the_front`, `central_asia_soviet_collapse_the_south_survives_together`, `BSC_central_asian_defense_council`, `TNC_central_asian_defense_council`, `ALA_central_asian_league_draft`.
- Republic-vs-republic wars: high-chaos helpers can create neighbor claims/wars, but short trees often compress this into one endpoint. Candidates for explicit war-plan/claim/settlement decision chains: `DSC_congress_of_the_dead_army`, `NRF_northern_revenant_fleet`, `ICD_commissariat_without_end`, `RMC_resurrection_without_state`, `TSC_starfall_mandate`.
- Chaos-tier releases: high-chaos payloads exist, but current focus route availability and payoff rarely communicate chaos-tier release behavior to the player. Candidates: all short high-chaos trees plus `NLC_extreme_path`, `FTH_war_plan`, `FEV_extreme_path`, `ARD_extreme_path`.

## Shallow or underpowered trees

These are current-state design failures against the spec, not parser errors.

- `PRA_soviet_collapse_focus_tree`, 22 focuses: has railway identity and meaningful helpers, but still too compact for a major rail/logistics state. It needs rail sovereignty decisions, moving-state logistics, rail-hub seizure missions, and stronger map-facing route payoffs.
- `TSC_soviet_collapse_focus_tree`, 18 focuses: strange science/myth identity exists, but the tree is too short and fragmented. It needs a visible observatory/science mechanic, event hooks, expansion consequences, and clearer diplomacy or containment pressure.
- `RMC_soviet_collapse_focus_tree`, 18 focuses: martyr cult identity exists, but the route needs more recruitment, legitimacy, failure pressure, and war/settlement mechanics.
- `DSC_soviet_collapse_focus_tree`, 18 focuses: death-state concept is too compressed. It needs a full dead army route, front-road missions, special units, neighbor-war escalation, and postwar handling.
- `NRF_soviet_collapse_focus_tree`, 18 focuses: naval revenant identity needs actual fleet, convoy, port, raid, naval militia, and Arctic settlement systems.
- `ICD_soviet_collapse_focus_tree`, 18 focuses: iron/dead commissariat needs security, archives, coercive mobilisation, dead-roll administration, and grim command mechanics beyond flat variables.
- `OGB_soviet_collapse_focus_tree`, 23 focuses: Volga restoration remains narrow. It needs trade/river authority, religion and society, Idel-Ural relations, future-event hooks, expansion settlement, and stronger late branch.
- `KZR`, `SOG`, `KHW`, `ALN` ancient trees, 16 each: all are compact symbolic-restoration stubs. They need full or at least robust compact routes around historical legitimacy, trade/water/pass authority, military survival, League/Union Unmade interaction, and expansion consequences.

## Layout findings

Exact duplicate coordinates:

- `soviet_collapse_ukraine_focus_tree`:
  - `(23,6)`: `ukr_soviet_collapse_arsenal_cities`, `ukr_soviet_collapse_army_of_the_republic`.
  - `(34,12)`: `ukr_soviet_collapse_great_steppe_and_sea_plan`, `ukr_soviet_collapse_dead_fields_living_columns`.
  - `(38,14)`: `ukr_soviet_collapse_black_banner_takes_the_villages`, `ukr_soviet_collapse_when_the_fields_refuse_the_state`.

No missing `relative_position_id`, missing same-tree prerequisites, or missing same-tree mutual exclusion targets were found by the current parser.

Continuous panel overlap risk:

- No current exact panel obstruction was found from tree width alone. The widest trees use x ranges up to 38, 36, or 31 focus units while their continuous focus panels are positioned in pixel space. This should still be screenshot-checked after coordinate fixes, but it is not the highest current blocker.

Potential pathline / branch-flow risks:

- `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` have three roots each. This can be intentional for side packages, but currently reads as disconnected route content in very short trees.
- Several focuses use hidden `available = { has_completed_focus = ... }` locks instead of visible path structure. Examples include BSC/TNC/ALA regional route locks and FEV late endgame locks. These may be valid, but the parent should review whether the player sees the route requirement clearly.

## Mutually exclusive branch quality

Meaningful route differences:

- `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, and `MFR_eternal_arsenal` form a real four-way governance fork with distinct helper names.
- Belarus rail neutrality vs rail war and Central Asian loose pact vs federation have plausible route intent.

Weak or clutter-risk route differences:

- `OGB_scholars_guard_the_charter` vs `OGB_clerics_guard_the_charter`: two small legitimacy variants, not yet a full scholarship-vs-clergy route.
- `OGB_treat_with_idel_ural` vs `OGB_the_volga_cannot_have_two_seals`: important concept, but too short to carry a whole regional settlement split.
- Ancient symbolic-vs-expansion pairs are too thin: the expansion side gets claims/war helpers, while symbolic side is mostly legitimacy/League variables. They need follow-up branches or decision unlocks to become real routes.
- Short high-chaos tree final forks often boil down to "state survives" vs "high-chaos endpoint" without enough middle-route consequences.

## Focus filter mismatches

This audit used a heuristic reward-to-filter pass and manual review of representative findings. The parent should treat these as high-confidence review candidates, not an exhaustive final patch list.

Quick filter fixes:

- Add or review `FOCUS_FILTER_ANNEXATION` for focuses that call neighbor expansion/claim/war helpers:
  - `BSC_hidden_doctrine`, `BSC_extreme_gate`
  - `TNC`/`ALA`/other equivalent hidden doctrine and extreme gate clones
  - `UDC_rival`, `UDC_enemy_front`, `UDC_war_plan`
  - `KZR_expansionist_steppe_levy`, `SOG_expansionist_merchant_claims`, `KHW_expansionist_water_claims`, `ALN_expansionist_mountain_claims`
- Add or review `FOCUS_FILTER_NAVY_XP` on naval actors:
  - `KRS_first_guard`, `KRS_sailors_assembly_registers`, `KRS_free_soviet_congress`, `KRS_gulf_mine_watch`, `KRS_port_guard_schools`, `KRS_endgame`
  - `NRF_living_harbor_committees`, `NRF_letters_to_sailor_towns`, `NRF_memorial_convoy_state`, `NRF_northern_revenant_fleet`
  - `ARD_murmansk_dockyard_sheds`, `ARD_white_sea_customs`, `ARD_foreign_fleet_letters`, `ARD_white_sea_port_tolls`, `ARD_arctic_port_endurance`
- Add or review industry filters on focuses with direct construction rewards:
  - `BSC_desert_airstrips`, `TNC_airfields_for_the_council`, `KRS_petrograd_signal_watch`, `KRS_convoy_escort_ledger`, `UDC_radio_command_posts`, and analogous cloned regional focuses.

## Prioritized parent patch plan

### Batch 1: Safe quick fixes

Files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Work:

- Fix Ukraine duplicate coordinates for `ukr_soviet_collapse_arsenal_cities`, `ukr_soviet_collapse_army_of_the_republic`, `ukr_soviet_collapse_great_steppe_and_sea_plan`, `ukr_soviet_collapse_dead_fields_living_columns`, `ukr_soviet_collapse_black_banner_takes_the_villages`, and `ukr_soviet_collapse_when_the_fields_refuse_the_state`.
- Add clear missing focus filters for high-confidence reward mismatches listed above.
- Review hidden `available = { has_completed_focus = ... }` route locks and add visible prerequisite lines or `custom_trigger_tooltip` where the lock is player-facing.

Validation:

- Re-run focus count, duplicate coordinate audit, `rg -n '<=|>='`, bracket depth, and focus localisation coverage.

### Batch 2: Helper-chain consolidation

Files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- related localisation files for any new custom tooltips

Focus IDs:

- `kaz_soviet_collapse_the_southern_republics_do_not_kneel`
- `FTH_war_plan`
- `NLC_war_plan`
- `PRA_armored_train_directorate`
- `moldova_soviet_collapse_romanian_aid_without_annexation`
- `moldova_soviet_collapse_prut_relief_depots`
- `internal_soviet_collapse_many_republics_common_front`
- `blr_soviet_collapse_minsk_supplies_the_front`

Helper IDs:

- `soviet_collapse_apply_focus_high_chaos_identity`
- `soviet_collapse_apply_high_chaos_focus_payload`
- `soviet_collapse_apply_focus_chaos_assault_plan`
- `soviet_collapse_apply_breakaway_neighbor_conflict_plan`
- `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`
- `soviet_collapse_add_republic_focus_recovery_progress`
- `soviet_collapse_update_pra_authority_idea`
- `soviet_collapse_update_dsc_dead_army_idea`

Intended gameplay change:

- Replace multi-helper focus dumps with one route-specific scripted effect per focus family.
- Keep temp guards, but make the visible tooltip one coherent route payoff.
- Preserve current power where intended, but separate recovery, identity, expansion, and decision-unlock payloads so a focus does not accidentally feel like four focuses firing at once.

### Batch 3: Shallow high-chaos tree redesign

Files:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

Trees:

- `TSC_soviet_collapse_focus_tree`
- `RMC_soviet_collapse_focus_tree`
- `DSC_soviet_collapse_focus_tree`
- `NRF_soviet_collapse_focus_tree`
- `ICD_soviet_collapse_focus_tree`
- `PRA_soviet_collapse_focus_tree`

Intended gameplay change:

- Add enough branch families to meet the spec: political authority, economy/supply, military or special units, diplomacy/influence or League, expansion/war, and late endgame.
- Add or extend decision hooks instead of only adding variables.
- For `DSC`, prioritize dead army units, front-road states, neighbor wars, and postwar cores/claims.
- For `NRF`, prioritize fleet/convoy/port mechanics, naval militia, Arctic port missions, and naval AI strategies.
- For `TSC`, prioritize observatory/science event hooks and strange containment/expansion mechanics.
- For `PRA`, prioritize railway sovereignty, rail hub missions, moving-state logistics, and rail guard units.

### Batch 4: Far Eastern, Pacific, railway/logistics, and naval power pass

Files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`

Focus IDs:

- `internal_soviet_collapse_far_eastern_rail_contracts`
- `internal_soviet_collapse_far_eastern_port_authority`
- `internal_soviet_collapse_pacific_harbor_guard`
- `FEV_war_plan`
- `FEV_vladivostok_harbor_board`
- `FEV_pacific_observer_missions`
- `FEV_sakhalin_ferry_protocols`
- `FEV_pacific_city_compact`
- `FEV_pacific_between_empires`
- `KRS_war_plan`
- `KRS_naval_infantry_oaths`
- `KRS_port_guard_schools`
- `ARD_murmansk_dockyard_sheds`
- `ARD_naval_infantry_yards`
- `ARD_foreign_fleet_letters`
- `ARD_white_sea_port_tolls`
- `ARD_arctic_port_endurance`

Intended gameplay change:

- Add Pacific and Arctic naval/port decision loops.
- Add route-specific `add_ai_strategy` for convoy raiding, naval invasion, dockyard/naval base building, and antagonize/conquer where appropriate.
- Make Far Eastern and naval actors visibly aggressive enough in high-chaos or scenario release conditions.

### Batch 5: OGB and ancient restoration redesign

Files:

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- relevant localisation files

Trees:

- `OGB_soviet_collapse_focus_tree`
- `KZR_soviet_collapse_ancient_focus_tree`
- `SOG_soviet_collapse_ancient_focus_tree`
- `KHW_soviet_collapse_ancient_focus_tree`
- `ALN_soviet_collapse_ancient_focus_tree`

Intended gameplay change:

- Expand OGB from compact Volga memory tree into a real Volga restoration actor with trade, religion/society, Idel-Ural relations, claims, modern survival, and future event hook.
- Give each ancient restoration at least one distinct mechanic: `KZR` toll/trade authority, `SOG` city/oasis trade, `KHW` canal/water authority, `ALN` pass/host authority.
- Tie these to League/Union Unmade/neighbor settlement, not only generic recognition and expansion helpers.

## Validation run

- Focus/tree count parser over all four focus files: 41 trees, 1,698 focus blocks.
- Duplicate focus ID parser: no duplicate focus IDs found.
- Corrected absolute coordinate parser: three duplicate coordinates found, all in Ukraine.
- Missing same-tree prerequisite / relative-position / mutual-exclusion target parser: no missing same-tree references found.
- Bracket-depth parser over all four focus files: final depth 0, minimum depth 0, no early-close lines.
- `rg -n '<=|>='` over audited focus/helper/idea/decision files: no matches.
- `rg -n '\b(add_ideas|remove_ideas|swap_ideas)\b'` over all four focus files and `005_soviet_collapse_effects.txt`: no direct focus-file idea operations; helper-level idea lifecycle operations remain in `005_soviet_collapse_effects.txt`.
- Focus localisation coverage script over Event005 localisation files: 1,698 / 1,698 focus title and `_desc` keys found.
- BOM check over `localisation/english/005_soviet_collapse*_l_english.yml`: all 12 files have UTF-8 BOM.
- `git diff --stat` showed pre-existing gameplay/localisation changes in the working tree. I did not modify those files in this run.

## Skipped validation

- No game launch or in-game validation.
- No screenshot/layout render validation.
- No asset or flag inspection; flags/assets were explicitly out of scope.
- No patch validation because this run did not patch gameplay files.
- No full decision availability simulation; decision files were inspected only as needed to verify focus reward connection surfaces.

## Remaining uncertainty

- The coordinate parser computes focus coordinates from current `x`, `y`, and `relative_position_id`. It does not render curved prerequisite lines. Parent should verify the Ukraine fixes and short-tree flow with screenshots or in-game focus view after patching.
- Some focus filters are heuristic review candidates. A parent patch should inspect each focus reward block before applying bulk filter edits.
- Helper-chain risk is design-level, not necessarily a runtime bug. The temp guards prevent some duplicate progress in one focus completion, but the parent should decide which bundled route payloads are intended power spikes and which should be split.
- Existing dirty worktree changes predate this read-only report. Parent should review current diffs before implementing any patch batches.
