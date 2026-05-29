# Custom Splinter Focus Reward Cleanup Handoff

## Scope

- Audited and patched `common/national_focus/005_soviet_collapse_custom_splinters.txt`.
- Did not edit `005_soviet_collapse_republics.txt`.
- Did not add or change External Support grants.

## Changed Files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_custom_splinter_focus_reward_cleanup.md`

## Gameplay Surface Changed

The custom splinter focus file no longer directly grants the repeated tiny logistics stockpiles that were cluttering focus rewards:

- Removed all direct `constant:soviet_collapse_republic_focus.rail_train_reward` references found in the file during the pre-patch scan.
- Removed all direct `constant:soviet_collapse_republic_focus.motorized_equipment_small` references found in the file during the pre-patch scan.
- Preserved existing route-specific helpers, variables, map construction, XP, claims, endgame effects, and decision/helper unlock calls around those rewards.

Pre-patch scan count in this file:

- `rail_train_reward`: 76 direct references
- `motorized_equipment_small`: 23 direct references
- direct `soviet_collapse_republic_foreign_support_*` or `External Support` focus grants: 0

Post-patch scan count in this file:

- `rail_train_reward`: 0 direct references
- `motorized_equipment_small`: 0 direct references
- direct `soviet_collapse_republic_foreign_support_*` or `External Support` focus grants: 0

## Route Coverage Table

No separate source spec was opened for this narrow subagent pass; route coverage is inferred from the implemented custom splinter focus file and existing helper calls.

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Opening statehood and survival | `*_birth`, `*_first_guard`, `*_stores`, local opening equivalents | Present | Direct train/truck clutter removed; existing identity helpers and variables remain. |
| Military and front preparation | `*_war_plan`, `*_special_arm`, `*_enemy_front`, route-specific staff/front focuses | Present | Direct truck/train rewards removed where found; `soviet_collapse_apply_focus_military_consolidation` and custom war helpers remain. |
| Depot, industry, and logistics | `*_supply`, `*_industry_plan`, rail/workshop/road/depot branches | Present but still compact | Direct stockpile clutter removed from the focus file; helper internals may still need parent tuning. |
| Diplomacy, League, and liaison | `*_league`, `*_foreign`, `*_diplomatic_plan`, League bargain focuses | Present | No direct External Support focus grants found or added. Existing foreign/League helpers remain. |
| Radical, high-chaos, and endgame | `*_radical_turn`, `*_extreme_gate`, `*_extreme_path`, `*_endgame`, `soviet_collapse_complete_*_endgame` hooks | Present | No route redesign performed; reward cleanup only. |

## Missing Or Simplified Content

- Some custom splinter branches remain compact and helper-driven rather than bespoke decision loops.
- Direct focus-file train/truck clutter is gone, but small train/truck payloads still exist inside shared scripted helpers. Parent should decide whether to retune those helper internals because they are shared beyond this file.
- Localisation was not rewritten; if any focus descriptions promise trains, trucks, or rail stockpile rewards, a follow-up localisation audit should align those descriptions with the cleaned reward surface.

## Icon Coverage Table

| Icon surface | Status | Notes |
| --- | --- | --- |
| Existing custom splinter focus icons | Unchanged | No icon IDs were edited. |
| Reused route icons such as `GFX_focus_*_supply` and `GFX_focus_*_war_plan` | Unchanged | Repeated icon quality was not part of this narrow reward patch. |
| New icons | Not applicable | No new sprites or icon references were added. |

## Localisation And Reward Mismatches

- No localisation keys were changed.
- Potential mismatch risk remains only if existing focus descriptions explicitly mention tiny train or truck handouts; this pass did not audit every localisation string.
- No direct External Support idea localisation or focus grant mismatch was found in the scoped focus file.

## AI Behavior Gaps

- Existing `ai_will_do` blocks were left unchanged.
- Some compact custom splinter routes still rely on flat or broad AI weights; route-specific AI cleanup remains a parent-level follow-up if broader depth work continues.

## High-Priority Fixes

1. Completed: remove direct tiny `rail_train_reward` and `motorized_equipment_small` focus rewards from the scoped focus file.
2. Completed: verify no direct External Support focus grant exists in the scoped focus file.
3. Remaining: parent should decide whether shared helper internals should stop granting tiny train/truck payloads.
4. Remaining: parent/localisation audit should check focus text for now-removed train/truck reward promises.

## Focus IDs Patched

Affected focus IDs from the pre-patch scan:

`FTH_first_guard`, `FTH_free_rail_communes`, `FTH_tachanka_front`, `PRA_omsk_station_guard`, `PRA_count_the_locomotives`, `PRA_the_board_overrules_ministers`, `PRA_armored_train_directorate`, `PRA_neutral_corridor_letters`, `PRA_charge_for_safe_passage`, `PRA_rails_over_capitals`, `TSC_portable_laboratory_trains`, `NRF_count_the_drowned_crews`, `NRF_living_harbor_committees`, `NRF_port_republic_of_the_living`, `BSC_road_and_well_ledger`, `BSC_caravan_supply_hubs`, `BSC_hidden_road_depots`, `BSC_radical_turn`, `TNC_first_guard`, `TNC_railway_officer_schools`, `TNC_war_plan`, `TNC_cotton_rail_republic`, `ALA_first_guard`, `ALA_local_district_registers`, `ALA_rail_spine_to_south`, `ALA_karaganda_letters`, `ALA_caspian_oil_survey`, `ALA_southern_republics_council`, `ALA_depot_cavalry_columns`, `ALA_steppe_supply_hubs`, `ALA_anti_puppet_steppe_statute`, `ALA_steppe_republic_charter`, `BBH_armored_car_raids`, `BBH_captured_rail_stores`, `BBH_red_and_black_depots`, `BBH_railway_state_sabotage`, `UDC_mobile_order_columns`, `UDC_loyal_train_orders`, `UDC_signal_truck_yards`, `SDZ_internal_troop_convoys`, `SDZ_prison_train_ledgers`, `DHC_southern_crossing_batteries`, `DHC_winter_road_columns`, `KHC_birth`, `KHC_laba_rear_area`, `KHC_grain_corridor_escorts`, `KHC_winter_corridor_columns`, `FEV_first_guard`, `FEV_khabarovsk_assembly_records`, `FEV_amur_field_staff`, `FEV_railway_militia_charter`, `FEV_winter_rail_columns`, `FEV_vladivostok_harbor_board`, `SZA_war_plan`, `SZA_winter_column_registers`, `SZA_tomsk_omsk_switchyards`, `SZA_baikal_rear_area`, `SZA_far_eastern_transit_protocols`, `UWD_tagil_machine_tool_ledger`, `UWD_rail_yard_repair_trust`, `UWD_trans_ural_dispatch_board`, `UWD_league_arsenal_bargain`, `UWD_rail_belt_armored_patrols`, `UWD_kurgan_rear_area`, `mrc_raid_lowland_depots`, `mrc_negotiate_with_georgia_or_azerbaijan`, `MRC_pass_court_registers`, `MRC_caucasus_pack_train_board`, `MRC_argun_rear_area`, `IUL_radical_turn`, `IUL_ufa_field_commissars`, `IUL_samara_crossing_ledger`, `IUL_tatar_bashkir_courier_board`, `IUL_bashkir_cavalry_roads`, `IUL_kazan_ufa_signal_line`, `IUL_rail_and_river_patrols`, `IUL_league_corridor_bargain`, `IUL_war_plan`, `IUL_diplomatic_plan`, `IUL_kazan_ufa_workshop_cordon`, `IUL_federal_congress_missions`, `BAC_birobidzhan_archive_workshops`, `BAC_winter_road_columns`, `ARD_birth`, `ARD_radical_turn`, `ARD_murmansk_dockyard_sheds`, `NLC_winter_guarantees`, `NLC_ice_road_customs`, `NLC_winter_road_columns`.

## Behavior Before And After

Before:

- Many custom splinter focuses directly displayed tiny train or truck stockpile rewards.
- Some focuses stacked those direct stockpiles on top of route helpers, map construction, variables, XP, or endgame effects, producing noisy focus effects.

After:

- Those direct train/truck stockpile rewards are removed from the custom splinter focus file.
- Existing route helpers remain as the main payoff surface: `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_league_preparation`, `soviet_collapse_apply_focus_foreign_channel`, custom splinter identity helpers, and custom endgame helpers.
- External Support remains driven by outside intervention/influence systems, not direct focus grants in this file.

## Localisation And Icon IDs Changed

- Localisation keys changed: none.
- Icon IDs changed: none.

## Validation Run

- `rg -n "rail_train_reward|motorized_equipment_small|soviet_collapse_republic_foreign_support|External Support" common/national_focus/005_soviet_collapse_custom_splinters.txt` returned no matches.
- Brace count check on `common/national_focus/005_soviet_collapse_custom_splinters.txt`: balanced.
- Unsupported operator check on `common/national_focus/005_soviet_collapse_custom_splinters.txt`: no `<=` or `>=`.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt` passed.

## Skipped Validation

- No full HOI4 game load was run from this subagent.
- No cross-file focus layout audit was run because the patch only removed direct reward effect lines and did not move focuses, change prerequisites, change icons, or change localisation.

## Remaining Route Risks

- This pass removes direct tiny reward clutter from the focus file, but some existing scripted helper effects still contain small train/truck payloads internally. Those helpers are route-specific and shared beyond this subagent's narrow focus-file scope; parent should decide whether to re-tune helper internals globally.
- Some custom splinter branches remain structurally shallow because they rely on compact helper calls rather than larger bespoke decision loops. Broad route deepening should stay with the parent or an improvement-loop plan.
- The focus IDs `mrc_raid_lowland_depots` and `mrc_negotiate_with_georgia_or_azerbaijan` use lowercase prefixes while surrounding Mountain Republic IDs use `MRC_`; not patched because it is outside the reward-cleanup target and may be intentionally referenced elsewhere.
