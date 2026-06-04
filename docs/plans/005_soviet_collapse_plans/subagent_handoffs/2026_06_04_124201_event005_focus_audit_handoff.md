# Event005 Soviet Collapse Focus Audit Handoff

Date: 2026-06-04 12:42 UTC

Role: `chaosx_focus_tree_auditor`

## Scope

Audited the Event005 Soviet Collapse focus-tree rework surfaces requested by the parent agent:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- Event005 localisation presence as needed for focus/reward sanity checks

The user constraint to not touch flags was respected. No files under `gfx/flags` or `interface/flags` were edited.

## Required References Used

Repo skill used:

- `hoi4-focus-trees`
- `hoi4-decisions-missions`, because several focus rewards unlock or depend on decisions/missions

Offline Paradox wiki pages consulted before Event005 inspection:

- Data structures
- Triggers
- Effect
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- National focus modding

Vanilla documentation and precedents consulted:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `~/projects/Hearts of Iron IV/common/script_constants/documentation.md`
- `~/projects/Hearts of Iron IV/common/decisions/_documentation.md`
- `~/projects/Hearts of Iron IV/common/ai_strategy/_documentation.md`
- `~/projects/Hearts of Iron IV/common/national_focus/estonia.txt`
- `~/projects/Hearts of Iron IV/common/national_focus/generic.txt`

## Changed Files

Gameplay files were not patched in this audit. The only added file is this handoff:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_124201_event005_focus_audit_handoff.md`

Reason: the target gameplay files already contain broad unrelated dirty work, and the remaining issues are mostly branch depth, filter policy, and layout redesign items that should be applied by the parent integrator in controlled tranches.

## Focus Tree Inventory

`005_soviet_collapse_republics.txt`

- `soviet_collapse_ukraine_focus_tree`: 83 focuses
- `soviet_collapse_breakaway_focus_tree`: 36 focuses
- `soviet_collapse_internal_republic_focus_tree`: 62 focuses
- `soviet_collapse_baltic_focus_tree`: 42 focuses
- `soviet_collapse_caucasus_focus_tree`: 40 focuses
- `soviet_collapse_central_asia_focus_tree`: 45 focuses
- `soviet_collapse_moldova_focus_tree`: 48 focuses
- `soviet_collapse_belarus_focus_tree`: 53 focuses
- `soviet_collapse_kazakhstan_focus_tree`: 92 focuses

`005_soviet_collapse_custom_splinters.txt`

- `FTH_soviet_collapse_focus_tree`: 47 focuses
- `PRA_soviet_collapse_focus_tree`: 22 focuses
- `TSC_soviet_collapse_focus_tree`: 18 focuses
- `RMC_soviet_collapse_focus_tree`: 18 focuses
- `DSC_soviet_collapse_focus_tree`: 18 focuses
- `NRF_soviet_collapse_focus_tree`: 18 focuses
- `ICD_soviet_collapse_focus_tree`: 18 focuses
- 24 additional custom splinter trees with 47 focuses each

`005_soviet_collapse_factory_successors.txt`

- `CFR_soviet_collapse_focus_tree`: 47 focuses
- `OGB_soviet_collapse_focus_tree`: 23 focuses
- `MFR_soviet_collapse_focus_tree`: 58 focuses

`005_soviet_collapse_ancient_restorations.txt`

- `KZR_soviet_collapse_focus_tree`: 16 focuses
- `SOG_soviet_collapse_focus_tree`: 16 focuses
- `KHW_soviet_collapse_focus_tree`: 16 focuses
- `ALN_soviet_collapse_focus_tree`: 16 focuses

## Finding 1: Idea Spam And Duplicate Idea Rewards

No direct `add_ideas` or `add_timed_idea` calls were found inside the four audited focus files. This part of the rework is moving in the right direction: focuses are not directly stacking duplicate permanent ideas.

Helper-driven idea additions found in `common/scripted_effects/005_soviet_collapse_effects.txt`:

- `soviet_collapse_initialize_crisis_values`, line 1405, adds `soviet_collapse_union_crisis`.
- `soviet_collapse_apply_breakaway_setup_package`, line 3632, adds `soviet_collapse_republican_startup_disorder`.
- `soviet_collapse_update_pra_authority_idea`, line 7633, swaps one PRA authority idea after first clearing the authority idea set. This is lifecycle replacement, not duplicate spam.
- `soviet_collapse_ensure_cfr_construction_mandates_idea`, line 11034, adds `cfr_construction_mandates` only if absent.
- `soviet_collapse_apply_cfr_reconstruction_contracts`, line 11053, adds `cfr_housing_ration_boards` only if absent.
- `soviet_collapse_apply_mfr_audit_arsenal_orders`, line 11756, adds `mfr_arsenal_quotas` only if absent.
- `soviet_collapse_apply_mfr_convert_depots_to_arms_lines`, line 11770, adds `mfr_factory_guard_state` only if absent.
- Setup helpers around line 17145 add one guarded identity idea per successor if absent.

Focuses that trigger the PRA authority idea lifecycle:

- `PRA_the_timetable_declares_authority`, line 1206
- `PRA_armored_train_directorate`, line 1378
- `PRA_passport_of_the_moving_state`, line 1545
- `PRA_league_transit_bargain`, line 1611

Recommendation: keep the current guarded/helper-driven idea approach. Do not reintroduce direct idea stacking in focus rewards.

## Finding 2: Repeated Small Reward Patterns

The main residual spam problem is not duplicate ideas. It is repeated low-impact reward signatures across many branches.

High-frequency patterns from scripted focus scan:

- 151 focuses have an `add_stability`-only direct reward signature.
- 68 focuses have an `add_political_power`-only direct reward signature.
- 52 focuses have an `army_experience`-only direct reward signature.
- 40 focuses have an `add_war_support`-only direct reward signature.
- 34 focuses directly add only one infrastructure building.
- 16 focuses use the single civilian factory plus building-slot pattern.
- 10 focuses use the single arms factory plus building-slot pattern.
- 10 focuses use the same support equipment package.
- 9 focuses use the same convoy-only reward.

Representative focus IDs:

- Stability-only: `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_elections_under_shellfire`, `blr_soviet_collapse_minsk_emergency_office`, `blr_soviet_collapse_council_bargains_with_forests`, `blr_soviet_collapse_belarusian_question_answered`.
- Political-power-only: `ukr_soviet_collapse_workers_congress_in_kharkiv`, `ukr_soviet_collapse_the_commander_or_the_cabinet`, `ukr_soviet_collapse_coalition_of_three_ministries`, `soviet_collapse_capital_committee_records`, `internal_soviet_collapse_idel_ural_congress`.
- Army-experience-only: `ukr_soviet_collapse_moscows_officers_in_our_barracks`, `ukr_soviet_collapse_civilian_command_over_the_army`, `ukr_soviet_collapse_foreign_advisers_in_plain_coats`, `blr_soviet_collapse_orders_printed_like_timetables`.
- War-support-only: `ukr_soviet_collapse_army_of_the_republic`, `ukr_soviet_collapse_great_steppe_and_sea_plan`, `blr_soviet_collapse_swamp_roads_closed`, `blr_soviet_collapse_regular_forest_brigades`.
- Single civilian factory plus slot: `soviet_collapse_home_industry_contracts`, `internal_soviet_collapse_komi_mine_and_timber_contracts`, `moldova_soviet_collapse_vineyard_and_cannery_committees`, `kaz_soviet_collapse_karaganda_coal_accounting`, `TSC_kirensk_field_stations`, `BSC_road_and_well_ledger`.
- Single arms factory plus slot: `internal_soviet_collapse_bashkir_oilfield_security`, `moldova_soviet_collapse_tiraspol_depot_belt`, `kaz_soviet_collapse_mining_workers_councils`, `FTH_hidden_workshop_cells`, `BBH_workshop_cells`, `MFR_foundry_line_holds`.
- Reused support equipment package: `soviet_collapse_foreign_liaison_government`, `internal_soviet_collapse_republic_volunteer_standards`, `ICD_letters_to_grieving_cities`, `FEV_siberian_factory_letters`.
- Convoy-only: `baltic_soviet_collapse_the_baltic_customs_desk`, `kaz_soviet_collapse_iranian_caspian_notes`, `FTH_ukrainian_border_letters`, `FEV_sakhalin_ferry_protocols`, `IUL_volga_trade_letters`, `ARD_league_convoy_bargain`, `NLC_diplomatic_plan`.

Recommendation: parent should replace repeated flat rewards in priority branches with route mechanics: decision unlocks, timed missions, state-targeted buildout packages, AI strategies, claims, cores, unit/template unlocks, pressure changes, and chaos escalation hooks.

## Finding 3: Shallow Or Disconnected Branches

Priority examples where focuses still look disconnected from Soviet Collapse mechanics, decisions, release pressure, wars, or identity systems:

Ukraine:

- `ukr_soviet_collapse_guard_the_telegraph_house`, line 54: decryption plus legal-recognition helper, no decision or route unlock.
- `ukr_soviet_collapse_question_of_statehood`, line 145: stability plus legal-recognition helper.
- `ukr_soviet_collapse_war_without_a_declaration`, line 164: generic military consolidation only.
- `ukr_soviet_collapse_moscows_officers_in_our_barracks`, line 192: army XP only.
- `ukr_soviet_collapse_socialist_republic_without_moscow`, line 234: socialist sovereignty helper only.
- `ukr_soviet_collapse_workers_congress_in_kharkiv`, line 354: political power plus socialist helper.
- `ukr_soviet_collapse_purge_moscow_loyalists`, line 398: command power plus socialist helper.
- `ukr_soviet_collapse_foreign_courts_notice_kyiv`, line 744: foreign-recognition helper without a diplomatic decision unlock.
- `ukr_soviet_collapse_british_caution`, line 1379: foreign-recognition helper without a diplomatic decision unlock.
- `ukr_soviet_collapse_black_soil_oath`, line 2085: high-chaos identity helper plus basic stat.
- `ukr_soviet_collapse_grain_census_of_everyone`, line 2142: high-chaos identity helper plus basic stat.

Belarus:

- `blr_soviet_collapse_minsk_emergency_office`, line 8716: stability plus legal-recognition helper.
- `blr_soviet_collapse_first_corridor_guard`, line 8764: generic military consolidation only.
- `blr_soviet_collapse_evacuation_choice`, line 8825: stability plus depot helper.
- `blr_soviet_collapse_national_council_of_minsk`, line 8867: legal/compact helpers only.
- `blr_soviet_collapse_socialist_autonomy_without_moscow`, line 8895: socialist helper only.
- `blr_soviet_collapse_foreign_corridor_administration`, line 8953: foreign-channel/recognition helpers only.
- `blr_soviet_collapse_red_without_the_center`, line 9005: socialist plus depot helpers.
- `blr_soviet_collapse_liaison_hotels`, line 9052: stability plus foreign-channel helper.
- `blr_soviet_collapse_belarusian_question_answered`, line 9072: stability plus legal helper.
- `blr_soviet_collapse_swamp_roads_closed`, line 9428: war support plus generic military helper.
- `blr_soviet_collapse_regular_forest_brigades`, line 9513: war support plus generic military helper.
- `blr_soviet_collapse_the_green_border`, line 9599: foreign-recognition helper only.
- `blr_soviet_collapse_the_forest_state_rumor`, line 9763: high-chaos helper only.

`blr_soviet_collapse_timetable_state`, line 9196, calls `blr_soviet_collapse_apply_timetable_state`; verify helper strength before changing it because the focus itself may be correctly helper-driven.

PRA:

- Good mechanics exist now: rail authority variables, train stockpiles, rail construction, armored train tech, rail guard spawn, SOV pressure, and a wargoal payoff in `PRA_rails_over_capitals`.
- `PRA_timetable_law`, line 1304, is still mostly stability, rail authority, and legal helper.
- `PRA_neutral_corridor_letters`, line 1568, is liaison plus foreign recognition only.

DSC:

- `DSC_letters_to_veteran_towns`, line 3086: experience/command power plus recognition helper only.
- `DSC_league_of_old_fronts`, line 3108: league-prep helper plus variable only.
- `DSC_republic_of_roll_calls`, line 3199: political power/stability plus compact helper; peaceful end is weaker than the dead-army identity premise.

NRF:

- Stronger than older flat trees: has ship-log recovery, revenant fleet call, icebound marines, dockyards, naval bases, convoy rewards, claims, SOV pressure, and a wargoal payoff in `NRF_northern_revenant_fleet`.
- `NRF_signal_from_lost_convoys`, line 3313: high-chaos helper plus variable only.
- `NRF_letters_to_sailor_towns`, line 3625: navy XP plus foreign recognition only.
- `NRF_league_of_cold_ports`, line 3647: league-prep helper only.
- `NRF_claim_the_white_sea_lane`, line 3667: one claim, variable, and high-chaos helper. It should probably unlock sea-lane raiding or port-capture decisions.

DHC:

- `DHC_birth`, line 13678: political power, stability, variables only.
- `DHC_kuban_letters`, line 13978: recognition and foreign-channel helper only.
- `DHC_river_patrol_school`, line 14045: army XP plus military helper only.
- `DHC_don_endurance`, line 14816: high-chaos helper/stat only.
- `DHC_extreme_path`, line 14839: high-chaos helper/stat only.

FEV:

- `FEV_birth`, line 16066: political power, stability, variables only.
- `FEV_khabarovsk_assembly_records`, line 16106: stability, legal helper, variables.
- `FEV_free_port_merchants`, line 16509: foreign-recognition helper only.
- `FEV_pacific_city_compact`, line 16991: political power plus compact helper only.
- `FEV_extreme_path`, line 17101: command power plus high-chaos helper only.

NLC:

- `NLC_birth`, line 24227: political power, stability, variables only.
- `NLC_weather_station_staff`, line 24792: command power plus foreign-channel helper only.
- `NLC_station_court_registers`, line 24814: stability, legal helper, variables.
- `NLC_commune_staff_map`, line 25204: command power, socialist helper, variables.

OGB:

- `OGB_restore_the_bolghar_name`, line 1133: stability/political power plus `ogb_volga_legitimacy` only.
- `OGB_scholars_guard_the_charter`, line 1176: stability and legitimacy only.
- `OGB_clerics_guard_the_charter`, line 1196: ideology popularity and legitimacy only.
- `OGB_steppe_caravan_letters`, line 1271: political power, foreign-channel helper, river authority only.
- `OGB_friday_schools_and_court_records`, line 1291: stability and legitimacy only.
- `OGB_society_of_the_restored_name`, line 1338: basic stats and variable only.
- `OGB_letters_to_kazan_and_ufa`, line 1499: political power and legitimacy only.
- `OGB_answer_the_idel_ural_question`, line 1522: political power and legitimacy only.
- `OGB_claim_the_old_trade_cities`, line 1542: filter suggests annexation/industry, but direct scan did not find a claim, wargoal, core, or building reward in the focus block. Verify helper contents before treating it as complete.

MFR:

- The tree has stronger industrial and military payoffs than OGB, but several focuses still read as reward payloads rather than mechanics.
- `MFR_factory_guard_columns`, line 2485: building reward but no industry filter.
- `MFR_gates_sirens_rifles`, line 2536: building reward but no industry filter.
- `MFR_workers_own_the_arsenal`, line 2834: building reward but no industry filter.
- `MFR_arm_all_clients`, line 2916: thematically good, but should be checked for decision/AI strategy linkage.
- `MFR_no_peace_without_orders`, line 2935: claims/wars/equipment reward, but filters do not reflect army/annexation payload.
- `MFR_eternal_arsenal_marches`, line 3006: late payoff should be checked against decision and AI behavior expectations.

## Finding 4: Layout And Pathline Problems

Parser layout scan found no duplicate focus coordinates after correcting for focus-tree boundaries.

Likely parent-above-child or same-row prerequisite issues:

- `soviet_collapse_local_courts_and_militia_rolls`, line 2466, depends on `soviet_collapse_capital_committee_records`; parent at `(10,5)`, child at `(9,3)`.
- `soviet_collapse_foreign_cadre_school`, line 2645, depends on `soviet_collapse_foreign_liaison_government`; parent at `(6,4)`, child at `(7,3)`.
- `soviet_collapse_sponsor_aid_audit`, line 2908, depends on `soviet_collapse_foreign_liaison_government`; parent at `(6,4)`, child at `(5,3)`.
- `CFR_a_civilian_factory_in_every_capital`, line 606, depends on `CFR_the_debt_map`; both are on row `y = 12`.
- `CFR_the_city_without_citizens`, line 786, depends on `CFR_the_concrete_committee`; both are on row `y = 6`.

Likely line-through-focus issue:

- In `soviet_collapse_moldova_focus_tree`, the vertical line from `moldova_soviet_collapse_moldova_route_fork` to `moldova_soviet_collapse_river_guard_brigades` appears to pass through `moldova_soviet_collapse_ukrainian_border_compact` at `(12,3)`.

Close or crossing mutual-exclusion diamonds:

- `internal_soviet_collapse_legal_autonomy_congress` with `internal_soviet_collapse_security_council`; coordinates `(14,5)` and `(16,4)`.
- `internal_soviet_collapse_legal_autonomy_congress` with `internal_soviet_collapse_border_and_rail_liaisons`; coordinates `(14,5)` and `(12,4)`.
- `baltic_soviet_collapse_legal_continuity_government` with `baltic_soviet_collapse_military_border_government`; same row with wide span `(16,3)` to `(28,3)`.
- `moldova_soviet_collapse_independent_republic_council` with `moldova_soviet_collapse_ukrainian_border_compact`; coordinates `(11,4)` and `(12,3)`.
- `kaz_soviet_collapse_alash_memory_restored` with `kaz_soviet_collapse_socialist_steppe_republic`; coordinates `(36,3)` and `(34,4)`.
- `kaz_soviet_collapse_socialist_steppe_republic` with `kaz_soviet_collapse_resource_defense_directorate`; coordinates `(34,4)` and `(32,3)`.
- `CFR_elect_the_site_committees` with `CFR_the_concrete_committee`; same row with wide span `(9,6)` to `(25,6)`.
- `CFR_cities_first` with `CFR_contracts_first`; same row with wide span `(8,9)` to `(22,9)`.

Recommendation: parent should patch Ukraine/Belarus/CFR/custom splinter pathlines in a layout-only tranche after gameplay reward changes, because reward rewiring may change branch shape.

## Finding 5: Chaos-Country Identity Gaps

Highest-priority identity gaps:

- OGB remains the weakest of the priority chaos successors. It has a restored-name/Volga legitimacy premise, but too many focuses only add stability, political power, ideology popularity, or legitimacy variables. It needs claims, river authority decisions, Idel-Ural diplomacy, sacred/legal restoration mechanics, militia or cavalry templates, aggressive border choices, and SOV pressure.
- DHC has a strong host-circle premise but many focus rewards are generic. It needs host congress mechanics, Don/Kuban river pressure, mounted/host unit templates, raid or border-choice decisions, and a more threatening high-chaos path.
- DSC is thematically strong but under-mechanized outside the dead-soldier identity premise. It needs veteran-town recruitment, memorial mobilization, roll-call legitimacy, resurrected-front decisions, and pressure hooks.
- PRA is comparatively strong and already has rail mechanics. Remaining work should focus on turning corridor diplomacy into decisions and route pressure, not adding more stat rewards.
- CFR has construction mechanics and is directionally good. Remaining work is layout, decision visibility, and making the construction directorate feel powerful rather than only productive.
- MFR has industrial identity and arsenal rewards but needs cleaner filter alignment and stronger decision/AI linkage for arms-market aggression.
- NRF is comparatively strong and has the right naval identity. Remaining work should add sea-lane decisions, convoy raiding, port-capture choices, and AI strategy.
- FEV is still generic compared with its strategic location. It needs Pacific/free-port decisions, ferry/harbor pressure, Far Eastern diplomacy, border war choices, or naval/army hybrid mechanics.

Secondary chaos successors with likely generic branch surfaces:

- NLC: polar commune/weather station premise needs stronger Arctic survival, station network, and northern-route mechanics.
- ICD: iron/dead commissariat premise should be checked for unit and repression mechanics.
- TSC/RMC: short trees should be checked for whether their 18 focuses have enough payoff density.
- Ancient restoration trees are compact and likely acceptable structurally, but repeated border-file/building patterns should be made more distinctive if time allows.

## Finding 6: Search Filter Consistency

Search-filter scan found many likely mismatches. Some are false positives when helper effects hide the real reward; parent should verify helper contents before mass patching.

Priority exact examples:

- `ukr_soviet_collapse_emergency_rada`, line 37: has `add_manpower`, filters only political/stability. Add `FOCUS_FILTER_MANPOWER` if keeping manpower.
- `ukr_soviet_collapse_first_republican_line`, line 122: adds capital fort, filters army/manpower. Add `FOCUS_FILTER_INDUSTRY` if forts are treated as construction rewards.
- `ukr_soviet_collapse_purge_moscow_loyalists`, line 398: adds command power, filters political/stability. Add `FOCUS_FILTER_ARMY_XP` or replace command-power reward.
- `blr_soviet_collapse_orders_printed_like_timetables`, line 9026: rail construction plus command/army XP, filters political/army only. Add `FOCUS_FILTER_INDUSTRY`.
- `blr_soviet_collapse_partisans_or_army`, line 9449: supply node/rail construction plus template decision unlock, filters political/army only. Add `FOCUS_FILTER_INDUSTRY`.
- `PRA_the_board_overrules_ministers`, line 1348: rail/infrastructure construction, filters political/stability. Add `FOCUS_FILTER_INDUSTRY`.
- `PRA_armored_train_schools`, line 1512: supply node/rail construction plus train equipment/tech, filters army only. Add `FOCUS_FILTER_INDUSTRY`.
- `PRA_seize_the_junction_cities`, line 1662: manpower/equipment/buildings/annexation payload, filters annexation/army/industry. Add `FOCUS_FILTER_MANPOWER`.
- `DSC_call_the_dead_soldiers_congress`, line 2751: manpower/equipment/buildings, filters army/political. Add `FOCUS_FILTER_MANPOWER` and `FOCUS_FILTER_INDUSTRY`.
- `DSC_field_hospital_memorials`, line 2967: manpower/support equipment, filters army only. Add `FOCUS_FILTER_MANPOWER`.
- `NRF_count_the_drowned_crews`, line 3382: infantry equipment/depot payload, filters political/manpower. Add `FOCUS_FILTER_ARMY_XP` if equipment remains the meaningful reward category.
- `NRF_living_harbor_committees`, line 3406: infantry equipment, convoys, naval base, coastal bunker, filters political/stability/navy. Add `FOCUS_FILTER_INDUSTRY` and possibly army.
- `NRF_ghost_convoy_escorts`, line 3560: coastal bunker construction, filters navy/manpower. Add `FOCUS_FILTER_INDUSTRY`.
- `FEV_harbor_fortress_line`, line 16617: building rewards, filters army/navy. Add `FOCUS_FILTER_INDUSTRY`.
- `NLC_war_plan`, line 24573: air-related reward, filters army/industry. Add `FOCUS_FILTER_AIR_XP` if the air payload is kept.
- `MFR_factory_guard_columns`, line 2485: building reward, filters army/manpower. Add `FOCUS_FILTER_INDUSTRY`.
- `MFR_no_peace_without_orders`, line 2935: claims/wars/equipment reward, filters industry/political. Add `FOCUS_FILTER_ANNEXATION` and `FOCUS_FILTER_ARMY_XP`.
- `KZR_old_border_files`, line 175: annexation filter is present, but building rewards also need industry if retained.
- `SOG_old_city_border_files`, line 569: annexation filter is present, but building rewards also need industry if retained.
- `KHW_old_oasis_border_files`, line 953: annexation filter is present, but building rewards also need industry if retained.
- `ALN_old_pass_border_files`, line 1346: annexation filter is present, but building rewards also need industry if retained.

## Recommended Next Parent Patches

Suggested order:

1. Patch OGB first. It is a priority chaos successor and currently the clearest identity/mechanic gap.
2. Patch DHC and DSC next. Convert generic high-chaos/stat branches into unit, decision, pressure, and route mechanics.
3. Patch PRA/NRF/FEV with narrower additions: corridor diplomacy, sea-lane/port decisions, and Far Eastern/Pacific pressure mechanics.
4. Patch Ukraine and Belarus flat reward focuses where they are route anchors. Do not spend time on every small support focus before the route anchors are mechanical.
5. Do a search-filter cleanup pass after reward changes settle.
6. Do a layout-only pass for CFR, Moldova, internal republic, Baltic, and Kazakhstan mutex/pathline issues after reward placement stabilizes.

Avoid broad bulk generation. The trees are large enough that mechanical rewrites should be applied in small identity-specific tranches and reviewed against helper effects and decisions after each tranche.

## Validation

Audit methods used:

- Parsed focus-tree blocks, coordinates, prerequisites, mutual exclusions, direct reward keys, and search filters.
- Scanned helper effects for idea additions and focus-linked reward helpers.
- Inspected vanilla focus precedents for focus reward structure, decision unlock tooltips, unit/template rewards, and search filter usage.

Validation commands to run after parent patches:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Brace-balance check over all four Event005 focus files.
- `git status --short -- gfx/flags interface/flags`

Commands run for this handoff:

- `git diff --check -- docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_124201_event005_focus_audit_handoff.md`: passed.
- Brace-balance check over the four audited Event005 focus files: all returned balance `0`.
- `git status --short -- gfx/flags interface/flags`: produced no output.

No gameplay patch was made in this handoff. The final parent integration should rerun focus-file `git diff --check` and brace balance after source edits.

## Remaining Risks

- Helper-driven rewards can hide meaningful effects from direct focus scans. The filter findings should be applied with helper inspection, not as a blind mechanical replacement.
- Some flat-looking focuses may be acceptable if they are intentionally minor support nodes. The route anchors and chaos identity forks should receive priority.
- Layout fixes should follow reward/branch rewiring. Moving focuses first may create churn if later mechanics change path depth.
- No flag issue was inspected or patched because flags are explicitly out of scope.
