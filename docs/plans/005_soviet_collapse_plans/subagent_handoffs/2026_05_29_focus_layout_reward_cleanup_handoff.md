# Soviet Collapse Focus Layout and Reward Cleanup Handoff

## Scope

- Edited `common/national_focus/005_soviet_collapse_custom_splinters.txt`.
- No scripted effects, scripted triggers, constants, decisions, localisation, or assets were changed.

## Changed focus ids

- PRA rewards: `PRA_count_the_locomotives`, `PRA_repair_crews_without_ministries`, `PRA_coal_water_and_spare_parts`, `PRA_charge_for_safe_passage`.
- UWD layout/rewards: `UWD_radical_turn`, `UWD_kama_foundry_contracts`, `UWD_rail_yard_repair_trust`, `UWD_trans_ural_dispatch_board`, `UWD_ural_factory_endurance`.
- ARD layout/rewards: `ARD_settlement`, `ARD_radical_turn`, `ARD_industry_plan`, `ARD_hidden_doctrine`, `ARD_extreme_gate`, `ARD_extreme_path`, `ARD_fuel_and_convoy_escorts`, `ARD_white_sea_port_tolls`, `ARD_league_convoy_bargain`.
- NLC layout/rewards: `NLC_birth`, `NLC_stores`, `NLC_rival`, `NLC_league`, `NLC_foreign`, `NLC_diplomatic_plan`, `NLC_aurora_council_records`, `NLC_weather_station_staff`, `NLC_enemy_front`, `NLC_war_plan`, `NLC_settlement`, `NLC_radical_turn`, `NLC_winter_guarantees`, `NLC_station_battery_posts`, `NLC_tundra_watch_posts`, `NLC_winter_road_columns`, `NLC_apatity_rear_area`, `NLC_foreign_science_letters`, `NLC_volunteer_station_schools`, `NLC_ice_port_tolls`, `NLC_league_weather_bargain`, `NLC_heated_workshop_contracts`, `NLC_polar_commune_endurance`, `NLC_station_mediation`, `NLC_endgame`.

## Behavior before and after

- PRA rail focuses had several single-state infrastructure rewards. They now add railways or supply nodes alongside existing logistics effects, preserving the rail-state identity without adding new helpers.
- UWD's settlement/radical mutual-exclusion pair was very tight. `UWD_radical_turn` was moved left and `UWD_kama_foundry_contracts` was moved left to keep the row readable. UWD rail/factory payoffs now add railways or a second factory-type payoff where the reward was a single infrastructure/supply/industry building.
- ARD's hidden-doctrine route was routed from the center industry focus to a far-right focus, causing a long line through the tree. The hidden/extreme chain was pulled back near the industry branch. The settlement/radical pair was widened, and convoy/port rewards were strengthened with existing convoy effects.
- NLC's tree was visibly over-wide. The right-side opening, war, diplomatic, and polar branches were pulled left, the settlement/radical mutual-exclusion pair was widened, and the polar/endgame mutual pair was aligned on one row with no focus between them. Weather/station rewards now add radar or infrastructure alongside existing effects where they were one-off map rewards.

## Localisation keys and icon ids changed

- None.

## Validation run

- Brace balance sanity check for `common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed.
- `rg -n '<=|>=' common/national_focus/005_soviet_collapse_custom_splinters.txt`: no matches.
- Coordinate audit for same-row mutual-exclusion blockers in the file: passed.

## Skipped validation

- No full HOI4 parser or in-game layout preview was run from this subagent environment.
- No localisation validation was run because localisation was intentionally out of scope and unchanged.

## Remaining risks

- This patch cleans a high-impact subset only. Other custom splinter and factory successor trees in this same file may still have cramped rows, generic helper-only rewards, and long diagonal prerequisite paths.
- Several existing focus blocks in the touched regions still have inconsistent indentation from prior edits. This patch did not do a broad reformat to avoid churn.
- The file was already modified before this pass, so this handoff describes only the layout/reward cleanup performed here.
