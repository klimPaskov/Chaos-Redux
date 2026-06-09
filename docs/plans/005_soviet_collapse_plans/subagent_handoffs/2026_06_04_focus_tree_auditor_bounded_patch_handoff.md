# Event005 Focus Tree Auditor Bounded Patch Handoff

## Scope

Audited only the requested Event005 focus, effect, decision, and localisation files. No flag files, `.tga` files, `gfx/flags`, or flag-related sprites were touched.

Required local references consulted before patching:

- `AGENTS.md`
- `hoi4-focus-trees` skill
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`
- Vanilla focus precedent: `common/national_focus/generic.txt`

## Patches Made

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `CFR_soviet_collapse_focus_tree`
  - `CFR_cities_first`
  - Changed prerequisite from `CFR_minutes_from_every_workshop` to `CFR_the_board_becomes_the_cabinet` so the cities-first strategy sits on the same fork parent as `CFR_rails_first`, `CFR_factories_first`, and `CFR_contracts_first`.

- `common/national_focus/005_soviet_collapse_republics.txt`
  - `soviet_collapse_ukraine_focus_tree`
  - `ukr_soviet_collapse_direct_national_claims`
  - Added `FOCUS_FILTER_ANNEXATION`; the focus directly applies Ukraine claim logic.

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `NLC_soviet_collapse_focus_tree`
  - `NLC_station_battery_posts`
  - Added `FOCUS_FILTER_AIR_XP`; the focus directly grants `air_experience` and anti-air construction.

## Validation

- Brace balance checked clean on:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
  - `localisation/english/005_soviet_collapse_l_english.yml`

- Targeted reference check confirmed:
  - `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, and `CFR_contracts_first` now share `CFR_the_board_becomes_the_cabinet` as the immediate fork parent.
  - `NLC_station_battery_posts` has `FOCUS_FILTER_AIR_XP`.
  - `ukr_soviet_collapse_direct_national_claims` has `FOCUS_FILTER_ANNEXATION`.

- Flag diff check produced no flag-related changed paths.

## Audit Findings Left For Parent

### Dense raw reward blocks needing helper extraction

These focus rewards are still large direct-effect bundles and should be moved into identity-specific scripted effects rather than patched one-by-one here:

- `KZR_soviet_collapse_ancient_focus_tree`: `KZR_caspian_patrol_letters`, `KZR_old_border_files`, `KZR_khazar_charter`
- `SOG_soviet_collapse_ancient_focus_tree`: `SOG_old_city_border_files`, `SOG_sogdian_city_charter`
- `KHW_soviet_collapse_ancient_focus_tree`: `KHW_canal_recognition_letters`, `KHW_old_oasis_border_files`, `KHW_khwarazmian_water_charter`
- `ALN_soviet_collapse_ancient_focus_tree`: `ALN_mountain_envoy_guarantees`, `ALN_old_pass_border_files`, `ALN_alan_pass_charter`
- `NRF_soviet_collapse_focus_tree`: `NRF_living_harbor_committees`

Parent implementation should create/extend scripted effects in `common/scripted_effects/005_soviet_collapse_effects.txt` for each tag's border-file, charter, and envoy/patrol payoff pattern, then leave focus rewards as flags, tooltips, and one helper call.

### Multi-helper focus rewards

No focus in the audited files called the same helper twice, but many focuses still combine multiple different helpers. High-priority consolidation candidates:

- `FTH_soviet_collapse_focus_tree`: `FTH_war_plan`, `FTH_endgame`
- `PRA_soviet_collapse_focus_tree`: `PRA_seize_the_junction_cities`, `PRA_rails_over_capitals`, `PRA_the_pale_line_endures`
- `TSC_soviet_collapse_focus_tree`: `TSC_starfall_mandate`, `TSC_the_quiet_sky_settlement`
- `RMC_soviet_collapse_focus_tree`: `RMC_resurrection_without_state`, `RMC_shrine_state`
- `DSC_soviet_collapse_focus_tree`: `DSC_grave_ordnance_claims`, `DSC_congress_of_the_dead_army`, `DSC_memorial_frontier_state`
- `soviet_collapse_ukraine_focus_tree`: `ukr_soviet_collapse_great_steppe_and_sea_plan`, `ukr_soviet_collapse_the_western_question_cannot_wait`, `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map`

Parent should consolidate these only when the helper preserves route identity and tooltip clarity. I did not collapse them in this pass because several are intentional cross-system payoffs.

### Pathline/layout risks

Tree-local coordinate overlap audit found no exact duplicate focus coordinates. The following path corridors still likely need layout work:

- `soviet_collapse_ukraine_focus_tree`
  - `ukr_soviet_collapse_army_of_the_republic` -> `ukr_soviet_collapse_the_western_question_cannot_wait` passes through `ukr_soviet_collapse_black_sea_port_ledgers` and `ukr_soviet_collapse_direct_national_claims`.
  - `ukr_soviet_collapse_army_of_the_republic` -> `ukr_soviet_collapse_direct_national_claims` passes through `ukr_soviet_collapse_black_sea_port_ledgers`.
  - `ukr_soviet_collapse_officers_above_parties` -> `ukr_soviet_collapse_officer_patronage_lists` runs near `ukr_soviet_collapse_army_supremacy`.

- `soviet_collapse_belarus_focus_tree`
  - `blr_soviet_collapse_council_bargains_with_forests` -> `blr_soviet_collapse_a_forest_that_can_govern` crosses near `blr_soviet_collapse_armored_train_workshops`, `blr_soviet_collapse_forest_ammunition_hides`, and `blr_soviet_collapse_the_league_depot_at_minsk`.
  - `blr_soviet_collapse_foreign_aid_through_brest` -> `blr_soviet_collapse_brest_is_not_a_gift` runs near `blr_soviet_collapse_timetable_state` and `blr_soviet_collapse_minsk_central_dispatch`.

- `soviet_collapse_kazakhstan_focus_tree`
  - `kaz_soviet_collapse_rail_to_the_mines` -> `kaz_soviet_collapse_the_steppe_arsenal` runs near `kaz_soviet_collapse_lone_steppe_state` and `kaz_soviet_collapse_the_written_alash_program`.
  - `kaz_soviet_collapse_the_alash_courts` -> `kaz_soviet_collapse_the_steppe_keeps_many_memories` runs near `kaz_soviet_collapse_the_written_alash_program` and `kaz_soviet_collapse_teachers_of_the_new_steppe`.

- `NLC_soviet_collapse_focus_tree`
  - `NLC_ice_road_customs` -> `NLC_ration_and_signal_escorts` runs near `NLC_supply`.
  - `NLC_greenhouse_boards` -> `NLC_heated_workshop_contracts` runs near `NLC_ration_and_signal_escorts`.

- `DHC_soviet_collapse_focus_tree`: `DHC_stanitsa_mediation` -> `DHC_convoy_autonomy_guarantees` runs near `DHC_winter_road_columns`.
- `KHC_soviet_collapse_focus_tree`: `KHC_stanitsa_mediation` -> `KHC_grain_passage_guarantees` runs near `KHC_winter_corridor_columns`.
- `UWD_soviet_collapse_focus_tree`: `UWD_war_plan` -> `UWD_industry_plan` runs near `UWD_trans_ural_dispatch_board`.
- `ARD_soviet_collapse_focus_tree`: `ARD_white_sea_customs` -> `ARD_murmansk_dockyard_contracts` runs near `ARD_white_sea_port_tolls`.

Parent should move affected children one to two columns or split prerequisites into visible prerequisite blocks where the route logic requires multiple parents.

### Mutex review

Broad mutex sibling groups remain and should be reviewed for whether they are real identity locks:

- `soviet_collapse_central_asia_focus_tree`
  - Parent: `central_asia_soviet_collapse_southern_route_fork`
  - Locked siblings: `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_military_border_authority`, `central_asia_soviet_collapse_foreign_border_patronage`, `central_asia_soviet_collapse_turkestan_federation_road`

- `soviet_collapse_moldova_focus_tree`
  - Parent: `moldova_soviet_collapse_union_with_romania_question`
  - Locked siblings: `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_conditional_union`, `moldova_soviet_collapse_reject_the_union_question`

- `CFR_soviet_collapse_focus_tree`
  - Parent: `CFR_the_unfinished_city_speaks`
  - Governance locks: `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee`
  - Adjacent unlocked military support: `CFR_construction_battalions`

Parent should keep mutexes only where they represent incompatible governing authority. Support branches should usually be unlocked route follow-ups, not siblings competing with identity locks.

### Remaining filter mismatches

I patched two obvious filter mismatches. Additional high-confidence candidates:

- `soviet_collapse_ukraine_focus_tree`: `ukr_soviet_collapse_black_sea_port_ledgers` should likely include `FOCUS_FILTER_NAVY_XP`.
- `soviet_collapse_internal_republic_focus_tree`: `internal_soviet_collapse_peninsula_fortress_plan` should likely include `FOCUS_FILTER_AIR_XP`; `internal_soviet_collapse_far_eastern_port_authority` and `internal_soviet_collapse_pacific_harbor_guard` should likely include `FOCUS_FILTER_NAVY_XP`.
- `soviet_collapse_kazakhstan_focus_tree`: `kaz_soviet_collapse_airstrips_on_the_steppe` and `kaz_soviet_collapse_army_of_the_open_horizon` should likely include `FOCUS_FILTER_AIR_XP`; `kaz_soviet_collapse_iranian_caspian_notes` should likely include `FOCUS_FILTER_NAVY_XP`.
- `NRF_soviet_collapse_focus_tree`: `NRF_living_harbor_committees`, `NRF_letters_to_sailor_towns`, `NRF_memorial_convoy_state` should likely include `FOCUS_FILTER_NAVY_XP`.
- `ARD_soviet_collapse_focus_tree`: most port, fleet, convoy, and dockyard focuses should be reviewed for missing `FOCUS_FILTER_NAVY_XP`, including `ARD_murmansk_dockyard_sheds`, `ARD_white_sea_customs`, `ARD_foreign_fleet_letters`, `ARD_white_sea_port_tolls`, and `ARD_arctic_port_endurance`.

## Skills Used

- `hoi4-focus-trees`

No skills were created or updated.
