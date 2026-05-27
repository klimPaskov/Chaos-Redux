## Event 005 Duplicate Focus Icon Queue

Scope respected:

- audited duplicate focus icon assignments from `common/national_focus/005_soviet_collapse*.txt`
- checked current sprite targets in `interface/005_soviet_collapse*.gfx`
- did not edit gameplay, focus, localisation, `.gfx`, or shared asset manifests
- wrote only this handoff plus a bounded asset package under `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/`

### Audit Summary

High-priority four-use duplicate groups confirmed:

| Current shared sprite | Current shared DDS | Use count | Focus ids |
| --- | --- | --- | --- |
| `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_rail_and_irrigation_boards.dds` | `4` | `central_asia_soviet_collapse_irrigation_and_bread_councils`, `central_asia_soviet_collapse_cotton_rail_republic`, `central_asia_soviet_collapse_the_oasis_arsenal`, `central_asia_soviet_collapse_the_cotton_question` |
| `GFX_central_asia_soviet_collapse_steppe_federation` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_steppe_federation.dds` | `4` | `central_asia_soviet_collapse_turkestan_city_congress`, `central_asia_soviet_collapse_turkestan_federation_road`, `central_asia_soviet_collapse_federation_delegates`, `central_asia_soviet_collapse_federation_state` |
| `GFX_focus_FEV_diplomatic_plan` | `gfx/interface/goals/soviet_collapse/005_fev_custom_splinter_focus.dds` | `4` | `FEV_diplomatic_plan`, `FEV_siberian_factory_letters`, `FEV_pacific_observer_missions`, `FEV_pacific_between_empires` |
| `GFX_focus_SZA_diplomatic_plan` | `gfx/interface/goals/soviet_collapse/005_sza_custom_splinter_focus.dds` | `4` | `SZA_diplomatic_plan`, `SZA_ural_factory_letters`, `SZA_yenisei_city_federation`, `SZA_siberia_between_oceans` |
| `GFX_focus_IUL_supply` | `gfx/interface/goals/soviet_collapse/005_iul_custom_splinter_focus.dds` | `4` | `IUL_supply`, `IUL_samara_crossing_ledger`, `IUL_bashkir_rear_camps`, `IUL_kazan_ufa_workshop_cordon` |
| `GFX_focus_IUL_war_plan` | `gfx/interface/goals/soviet_collapse/005_iul_custom_splinter_focus.dds` | `4` | `IUL_bashkir_cavalry_roads`, `IUL_rail_and_river_patrols`, `IUL_war_plan`, `IUL_orenburg_approach_posts` |
| `GFX_focus_MRC_civil_rule` | `gfx/interface/goals/soviet_collapse/005_mrc_custom_splinter_focus.dds` | `4` | `mrc_summon_mountain_elders`, `mrc_protect_village_autonomy`, `MRC_civil_rule`, `MRC_mountain_market_pledges` |
| `GFX_focus_MRC_foreign` | `gfx/interface/goals/soviet_collapse/005_mrc_custom_splinter_focus.dds` | `4` | `MRC_foreign`, `mrc_negotiate_with_georgia_or_azerbaijan`, `MRC_tiflis_letters`, `MRC_black_sea_transit_protocols` |

Ancient shared generic groups still duplicated at four uses each and still not replaced by tag-specific sprites for those exact focuses:

- `GFX_focus_soviet_collapse_ancient_guard_old_routes`
- `GFX_focus_soviet_collapse_ancient_league_bargain`
- `GFX_focus_soviet_collapse_ancient_old_border_files`
- `GFX_focus_soviet_collapse_ancient_restoration_survives`
- `GFX_focus_soviet_collapse_ancient_returned_names_endgame`
- `GFX_focus_soviet_collapse_ancient_symbolic_state`
- `GFX_focus_soviet_collapse_ancient_workshop_compact`

### Produced Batch

Completed as a bounded prototype batch:

- package: `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/`
- target group replaced: `GFX_central_asia_soviet_collapse_steppe_federation`
- suggested target `.gfx`: `interface/005_soviet_collapse_regional_icons.gfx`

Produced icons:

| Focus id | Proposed sprite | Final DDS target | Source | Processed | Final status |
| --- | --- | --- | --- | --- | --- |
| `central_asia_soviet_collapse_turkestan_city_congress` | `GFX_central_asia_soviet_collapse_turkestan_city_congress` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_city_congress.dds` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/source_png/central_asia_soviet_collapse_turkestan_city_congress_source.png` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/processed_png/central_asia_soviet_collapse_turkestan_city_congress.png` | `needs_user_review` |
| `central_asia_soviet_collapse_turkestan_federation_road` | `GFX_central_asia_soviet_collapse_turkestan_federation_road` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_federation_road.dds` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/source_png/central_asia_soviet_collapse_turkestan_federation_road_source.png` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/processed_png/central_asia_soviet_collapse_turkestan_federation_road.png` | `needs_user_review` |
| `central_asia_soviet_collapse_federation_delegates` | `GFX_central_asia_soviet_collapse_federation_delegates` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_delegates.dds` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/source_png/central_asia_soviet_collapse_federation_delegates_source.png` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/processed_png/central_asia_soviet_collapse_federation_delegates.png` | `needs_user_review` |
| `central_asia_soviet_collapse_federation_state` | `GFX_central_asia_soviet_collapse_federation_state` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_state.dds` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/source_png/central_asia_soviet_collapse_federation_state_source.png` | `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/processed_png/central_asia_soviet_collapse_federation_state.png` | `needs_user_review` |

Validation performed:

- exact size checks on all processed PNGs and DDS files: `94x86`
- `identify -verbose` confirms `TrueColorAlpha` on produced DDS files
- checker review sheet written to `docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/contact_sheets/central_asia_federation_first_batch_checker.png`

### Remaining Queue

#### Central Asia Rail And Irrigation Boards

Current shared sprite:

- `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`

Queued replacements:

| Focus id | Proposed sprite | Proposed final DDS target |
| --- | --- | --- |
| `central_asia_soviet_collapse_irrigation_and_bread_councils` | `GFX_central_asia_soviet_collapse_irrigation_and_bread_councils` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_irrigation_and_bread_councils.dds` |
| `central_asia_soviet_collapse_cotton_rail_republic` | `GFX_central_asia_soviet_collapse_cotton_rail_republic` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_cotton_rail_republic.dds` |
| `central_asia_soviet_collapse_the_oasis_arsenal` | `GFX_central_asia_soviet_collapse_the_oasis_arsenal` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_the_oasis_arsenal.dds` |
| `central_asia_soviet_collapse_the_cotton_question` | `GFX_central_asia_soviet_collapse_the_cotton_question` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_the_cotton_question.dds` |

#### FEV Diplomatic/Economy/Supply Slice

Queued diplomatic four-use replacements:

| Focus id | Proposed sprite | Proposed final DDS target |
| --- | --- | --- |
| `FEV_diplomatic_plan` | `GFX_FEV_diplomatic_plan` | `gfx/interface/goals/soviet_collapse/FEV_diplomatic_plan.dds` |
| `FEV_siberian_factory_letters` | `GFX_FEV_siberian_factory_letters` | `gfx/interface/goals/soviet_collapse/FEV_siberian_factory_letters.dds` |
| `FEV_pacific_observer_missions` | `GFX_FEV_pacific_observer_missions` | `gfx/interface/goals/soviet_collapse/FEV_pacific_observer_missions.dds` |
| `FEV_pacific_between_empires` | `GFX_FEV_pacific_between_empires` | `gfx/interface/goals/soviet_collapse/FEV_pacific_between_empires.dds` |

#### SZA Diplomatic/Economy/Supply Slice

Queued diplomatic four-use replacements:

| Focus id | Proposed sprite | Proposed final DDS target |
| --- | --- | --- |
| `SZA_diplomatic_plan` | `GFX_SZA_diplomatic_plan` | `gfx/interface/goals/soviet_collapse/SZA_diplomatic_plan.dds` |
| `SZA_ural_factory_letters` | `GFX_SZA_ural_factory_letters` | `gfx/interface/goals/soviet_collapse/SZA_ural_factory_letters.dds` |
| `SZA_yenisei_city_federation` | `GFX_SZA_yenisei_city_federation` | `gfx/interface/goals/soviet_collapse/SZA_yenisei_city_federation.dds` |
| `SZA_siberia_between_oceans` | `GFX_SZA_siberia_between_oceans` | `gfx/interface/goals/soviet_collapse/SZA_siberia_between_oceans.dds` |

#### IUL Groups

Queued supply replacements:

| Focus id | Proposed sprite | Proposed final DDS target |
| --- | --- | --- |
| `IUL_supply` | `GFX_IUL_supply` | `gfx/interface/goals/soviet_collapse/IUL_supply.dds` |
| `IUL_samara_crossing_ledger` | `GFX_IUL_samara_crossing_ledger` | `gfx/interface/goals/soviet_collapse/IUL_samara_crossing_ledger.dds` |
| `IUL_bashkir_rear_camps` | `GFX_IUL_bashkir_rear_camps` | `gfx/interface/goals/soviet_collapse/IUL_bashkir_rear_camps.dds` |
| `IUL_kazan_ufa_workshop_cordon` | `GFX_IUL_kazan_ufa_workshop_cordon` | `gfx/interface/goals/soviet_collapse/IUL_kazan_ufa_workshop_cordon.dds` |

Queued war-plan replacements:

| Focus id | Proposed sprite | Proposed final DDS target |
| --- | --- | --- |
| `IUL_bashkir_cavalry_roads` | `GFX_IUL_bashkir_cavalry_roads` | `gfx/interface/goals/soviet_collapse/IUL_bashkir_cavalry_roads.dds` |
| `IUL_rail_and_river_patrols` | `GFX_IUL_rail_and_river_patrols` | `gfx/interface/goals/soviet_collapse/IUL_rail_and_river_patrols.dds` |
| `IUL_war_plan` | `GFX_IUL_war_plan` | `gfx/interface/goals/soviet_collapse/IUL_war_plan.dds` |
| `IUL_orenburg_approach_posts` | `GFX_IUL_orenburg_approach_posts` | `gfx/interface/goals/soviet_collapse/IUL_orenburg_approach_posts.dds` |

#### MRC Groups

Queued civil-rule replacements:

| Focus id | Proposed sprite | Proposed final DDS target |
| --- | --- | --- |
| `mrc_summon_mountain_elders` | `GFX_mrc_summon_mountain_elders` | `gfx/interface/goals/soviet_collapse/mrc_summon_mountain_elders.dds` |
| `mrc_protect_village_autonomy` | `GFX_mrc_protect_village_autonomy` | `gfx/interface/goals/soviet_collapse/mrc_protect_village_autonomy.dds` |
| `MRC_civil_rule` | `GFX_MRC_civil_rule` | `gfx/interface/goals/soviet_collapse/MRC_civil_rule.dds` |
| `MRC_mountain_market_pledges` | `GFX_MRC_mountain_market_pledges` | `gfx/interface/goals/soviet_collapse/MRC_mountain_market_pledges.dds` |

Queued foreign replacements:

| Focus id | Proposed sprite | Proposed final DDS target |
| --- | --- | --- |
| `MRC_foreign` | `GFX_MRC_foreign` | `gfx/interface/goals/soviet_collapse/MRC_foreign.dds` |
| `mrc_negotiate_with_georgia_or_azerbaijan` | `GFX_mrc_negotiate_with_georgia_or_azerbaijan` | `gfx/interface/goals/soviet_collapse/mrc_negotiate_with_georgia_or_azerbaijan.dds` |
| `MRC_tiflis_letters` | `GFX_MRC_tiflis_letters` | `gfx/interface/goals/soviet_collapse/MRC_tiflis_letters.dds` |
| `MRC_black_sea_transit_protocols` | `GFX_MRC_black_sea_transit_protocols` | `gfx/interface/goals/soviet_collapse/MRC_black_sea_transit_protocols.dds` |

#### Ancient Shared Generic Queue

All of the following still use shared generic DDS and can follow the same naming rule `GFX_<focus_id>` -> `gfx/interface/goals/soviet_collapse/<focus_id>.dds` once promoted:

- `KZR_guard_the_crossings`
- `SOG_oasis_checkpoint_guard`
- `KHW_guard_the_pumps`
- `ALN_guard_the_pass_line`
- `KZR_league_transit_bargain`
- `SOG_league_city_bargain`
- `KHW_league_irrigation_bargain`
- `ALN_league_pass_bargain`
- `KZR_old_border_files`
- `SOG_old_city_border_files`
- `KHW_old_oasis_border_files`
- `ALN_old_pass_border_files`
- `KZR_restoration_survives_modern_war`
- `SOG_restoration_survives_modern_war`
- `KHW_restoration_survives_modern_war`
- `ALN_restoration_survives_modern_war`
- `KZR_returned_names_endgame`
- `SOG_returned_names_endgame`
- `KHW_returned_names_endgame`
- `ALN_returned_names_endgame`
- `KZR_symbolic_crossing_state`
- `SOG_symbolic_city_league`
- `KHW_symbolic_oasis_authority`
- `ALN_symbolic_pass_principality`
- `KZR_customs_workshop_compact`
- `SOG_bazaar_workshop_compact`
- `KHW_oasis_workshop_compact`
- `ALN_mountain_workshop_compact`

Recommended next batch order:

1. `central_asia_soviet_collapse_rail_and_irrigation_boards`
2. `GFX_focus_FEV_diplomatic_plan`
3. `GFX_focus_SZA_diplomatic_plan`
4. `GFX_focus_IUL_supply`
5. `GFX_focus_IUL_war_plan`
6. `GFX_focus_MRC_civil_rule`
7. `GFX_focus_MRC_foreign`
8. ancient shared generic groups
