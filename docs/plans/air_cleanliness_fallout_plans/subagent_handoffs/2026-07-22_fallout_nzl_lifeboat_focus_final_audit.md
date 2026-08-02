# Fallout NZL Lifeboat focus final audit handoff

Date: 2026-07-22
Scope: the dormant `fallout_nzl_lifeboat_focus_tree`, its NZL strategy plans, and directly consumed focus contracts.
Status: one narrow AI route patch is complete. The package remains dormant and no activation boundary was changed.

## Changed files and identifiers

- `common/ai_strategy_plans/fallout_consolidated_ai.txt`
  - Added `fallout_nzl_fishery_quota_compacts` to the isolation plan at line 154.
  - Added `fallout_nzl_weatherproof_the_grain_sheds` to the isolation plan at line 155.
  - The order now places repair, fishery, radio weather, weatherproofing, and the two-island ring in a dependency-safe sequence.
- No focus source, trigger helper, decision, idea, character, localisation, GFX, DDS, event, or asset file was changed.
- No focus identifier was renamed.

The proposed change to `fallout_nzl_lifeboat_package_is_current` in `common/scripted_triggers/fallout_consolidated_triggers.txt:66-78` was rejected. The exact five-state trigger already gates package activation and starting-force creation at lines 59-63 of that file. Making it a durable current-package condition would close all focus, decision, event, advisor, and AI surfaces whenever a player temporarily loses or occupies one of the support states. That would conflict with continued play during war pressure and the existing capital-loss memory in `common/on_actions/fallout_consolidated_on_actions.txt:116-133`.

## Route coverage

| Route surface | Focus identifiers | Coverage and behavior |
| --- | --- | --- |
| Opening trunk | `fallout_nzl_count_the_living`, `fallout_nzl_seat_the_lifeboat_parliament`, `fallout_nzl_open_wellington_quays`, `fallout_nzl_relay_auckland_radio`, `fallout_nzl_measure_the_dairy_stores`, `fallout_nzl_bind_the_two_islands` | All six exist at `common/national_focus/fallout_consolidated_focus.txt:24-137`. The bind focus uses three separate prerequisite blocks, so the three opening receipts are ANDed. Generation-aware opening and domestic result triggers prevent stale event results. |
| Humanitarian | `fallout_nzl_keep_the_harbor_lights`, `fallout_nzl_admit_the_first_rescue_fleet`, `fallout_nzl_publish_the_berth_ledger`, `fallout_nzl_elect_the_relief_speaker`, `fallout_nzl_guarantee_lifeboat_rights`, `fallout_nzl_pacific_relief_republic` | All six exist at lines 141-240. The first focus is mutually exclusive with `fallout_nzl_draw_the_southern_cordon`. The route commits a humanitarian flag, opens rescue transactions, promotes a runtime relief speaker, upgrades the morality idea, and applies the humanitarian identity. |
| Isolation | `fallout_nzl_draw_the_southern_cordon`, `fallout_nzl_close_unregistered_anchorages`, `fallout_nzl_license_every_sea_road`, `fallout_nzl_appoint_the_harbor_constable`, `fallout_nzl_reserve_the_last_berths`, `fallout_nzl_southern_refuge` | All six exist at lines 244-359. The route is mutually exclusive with the humanitarian route. Security, trust, harbor capacity, the last-berth decision, runtime constable promotion, and the isolation identity are wired. The `license_every_sea_road` reward mismatch remains open below. |
| Economy and survival | `fallout_nzl_dairy_relief_fleet`, `fallout_nzl_repair_the_milk_rail`, `fallout_nzl_fishery_quota_compacts`, `fallout_nzl_weatherproof_the_grain_sheds`, `fallout_nzl_rebuild_devonport`, `fallout_nzl_storm_port_engineers`, `fallout_nzl_radio_weather_chain`, `fallout_nzl_two_island_supply_ring` | All eight exist at lines 363-506. Rail repair checks state 723. Weatherproofing and the final supply ring use separate prerequisite blocks for AND semantics. The final idea lifecycle replaces the harbor and weather stages after both island logistics are proven. |
| Military | `fallout_nzl_home_guard_rolls`, `fallout_nzl_port_militia_drill`, `fallout_nzl_convoy_volunteer_corps`, `fallout_nzl_southern_cross_patrols`, `fallout_nzl_pirate_bearing_rooms`, `fallout_nzl_armed_rescue_cutters`, `fallout_nzl_coastal_denial_batteries`, `fallout_nzl_lifeboat_navy` | All eight exist at lines 510-635. Southern Cross uses separate militia and convoy prerequisites. Coastal batteries uses separate anti-piracy and rescue-cutter prerequisites plus exact Wellington and Auckland control. Rewards use decisions, bounded equipment and convoy actions, naval experience, buildings, and a final navy idea. |
| External and late | `fallout_nzl_call_the_island_radios`, `fallout_nzl_offer_rescue_passages`, `fallout_nzl_pacific_rescue_mandate`, `fallout_nzl_relief_ports_without_annexation`, `fallout_nzl_demand_quiet_seas`, `fallout_nzl_punitive_anti_piracy_patrols`, `fallout_nzl_southern_sea_exclusion_zone`, `fallout_nzl_year_ten_order` | All eight exist at lines 639-801. The shared radio focus has an intentional OR between the two route identities. Humanitarian focuses require valid partner receipts. Isolation focuses require a valid aggressor or an explicit no-aggressor settlement path. Year Ten uses route-specific availability and the 3,650-day readiness trigger. |

## Missing or simplified content

1. `fallout_nzl_license_every_sea_road` at `common/national_focus/fallout_consolidated_focus.txt:289-307` sets `fallout_nzl_last_berth_decision_open`, raises sea-lane security, and lowers harbor capacity. The accepted specification at `docs/specs/air_cleanliness_fallout_specs/fallout_nzl_lifeboat_state_pilot_spec.md:120-129` promises numbered permits, patrol windows, reduced piracy risk, and a higher convoy operating cost. Current code does not implement the convoy operating cost tradeoff.
2. Official modifier documentation supports `underway_replenishment_convoy_cost` and `convoy_escort_efficiency`, but neither is a direct focus effect and no current NZL idea stage carries the required cost modifier. `trade_cost_for_target_factor` changes the cost for another country to buy this country's resources, not convoy operating cost. The wiki's generic `production_cost_max_convoy` entry is not present in the official modifier documentation consulted for this audit. Implementing the promised tradeoff therefore needs a deliberate idea or transaction design outside this narrow focus and AI scope. I did not invent a substitute modifier or relabel the existing harbor penalty.
3. The focus inspector reports runtime leader references `NZL_fallout_relief_speaker` and `NZL_fallout_harbor_constable` as missing at focus lines 202 and 321. These leaders are generated by `fallout_nzl_activate_lifeboat_package` in `common/scripted_effects/fallout_consolidated_effects.txt`, so static character definitions are intentionally absent. Runtime activation proof remains blocked because the helper has no caller.
4. The accepted specification names `fallout_nzl_port_militia_training_mission` and `fallout_nzl_arm_rescue_cutters_action` as focus identifiers. The implementation uses `fallout_nzl_port_militia_drill` and `fallout_nzl_armed_rescue_cutters`. The decision identifiers retain the specification names. This is a documentation reconciliation item, not a missing route.
5. The live Fallout allocator still has no caller for `fallout_nzl_activate_lifeboat_package`. Samoa 726 and the Aotearoa or GRX conflict receipts remain unresolved. Vanilla NZL alternate AI plans still have empty abort blocks. These are activation blockers outside the focus-only patch.

## Icon coverage

The focus file references 24 unique NZL goal sprites. The current inspection found a matching GFX definition and DDS file for every one under `interface/fallout_consolidated.gfx` and `gfx/interface/goals/fallout_world_end_nzl_lifeboat_state`. Reuse is deliberate.

| Icon id | Focus identifiers using it |
| --- | --- |
| `GFX_goal_fallout_nzl_admit_the_first_rescue_fleet` | `admit_the_first_rescue_fleet`, `convoy_volunteer_corps`, `armed_rescue_cutters` |
| `GFX_goal_fallout_nzl_appoint_the_harbor_constable` | `appoint_the_harbor_constable`, `home_guard_rolls` |
| `GFX_goal_fallout_nzl_bind_two_islands` | `bind_the_two_islands`, `two_island_supply_ring` |
| `GFX_goal_fallout_nzl_close_unregistered_anchorages` | `close_unregistered_anchorages`, `port_militia_drill`, `coastal_denial_batteries` |
| `GFX_goal_fallout_nzl_count_the_living` | `count_the_living` |
| `GFX_goal_fallout_nzl_dairy_relief_fleet` | `dairy_relief_fleet` |
| `GFX_goal_fallout_nzl_draw_southern_cordon` | `draw_the_southern_cordon`, `southern_cross_patrols`, `punitive_anti_piracy_patrols`, `southern_sea_exclusion_zone` |
| `GFX_goal_fallout_nzl_elect_relief_speaker` | `elect_the_relief_speaker` |
| `GFX_goal_fallout_nzl_fishery_quota_compacts` | `fishery_quota_compacts` |
| `GFX_goal_fallout_nzl_guarantee_lifeboat_rights` | `guarantee_lifeboat_rights`, `offer_rescue_passages` |
| `GFX_goal_fallout_nzl_keep_harbor_lights` | `keep_the_harbor_lights` |
| `GFX_goal_fallout_nzl_license_every_sea_road` | `license_every_sea_road`, `pirate_bearing_rooms`, `demand_quiet_seas` |
| `GFX_goal_fallout_nzl_measure_dairy_stores` | `measure_the_dairy_stores` |
| `GFX_goal_fallout_nzl_open_wellington_quays` | `open_wellington_quays`, `relief_ports_without_annexation` |
| `GFX_goal_fallout_nzl_pacific_relief_republic` | `pacific_relief_republic`, `pacific_rescue_mandate` |
| `GFX_goal_fallout_nzl_publish_the_berth_ledger` | `publish_the_berth_ledger` |
| `GFX_goal_fallout_nzl_rebuild_devonport` | `rebuild_devonport`, `lifeboat_navy` |
| `GFX_goal_fallout_nzl_relay_auckland_radio` | `relay_auckland_radio`, `radio_weather_chain`, `call_the_island_radios` |
| `GFX_goal_fallout_nzl_repair_the_milk_rail` | `repair_the_milk_rail` |
| `GFX_goal_fallout_nzl_reserve_the_last_berths` | `reserve_the_last_berths` |
| `GFX_goal_fallout_nzl_seat_the_lifeboat_parliament` | `seat_the_lifeboat_parliament`, `year_ten_order` |
| `GFX_goal_fallout_nzl_southern_refuge` | `southern_refuge` |
| `GFX_goal_fallout_nzl_storm_port_engineers` | `storm_port_engineers` |
| `GFX_goal_fallout_nzl_weatherproof_the_grain_sheds` | `weatherproof_the_grain_sheds` |

## Localisation and reward mismatch list

- All 42 focus title and description keys resolve in `localisation/english/fallout_consolidated_l_english.yml`. The file remains UTF-8 with BOM.
- `fallout_nzl_license_every_sea_road_desc` at localisation line 222 promises numbered permits and patrol windows, while the reward at focus lines 298-304 only opens the last-berth decision and changes the two stored values. The missing convoy operating cost is the same accepted-spec mismatch described above.
- The count focus description presents the census as deciding harbor governance, while activation initializes the four values and the opening event receipt handles governance. This remains a safe activation-boundary simplification, not a missing localisation key.
- The military identifier pairs listed above need documentation alignment. No player-facing key is missing.

## AI behavior gaps and changes

- All 42 focus nodes have `ai_will_do` blocks and `search_filters` in `common/national_focus/fallout_consolidated_focus.txt`.
- The humanitarian plan at `common/ai_strategy_plans/fallout_consolidated_ai.txt:50-84` already covers its economy and military prerequisites.
- Before this patch, the isolation plan at lines 129-161 omitted fishery quota compacts and weatherproof grain sheds. The omission could strand the listed `two_island_supply_ring` focus behind its weatherproof prerequisite. Both IDs are now present at lines 154-155.
- A static sequence check confirms repair, fishery, radio weather, weatherproofing, and the final ring occur in dependency-safe order. All 66 plan focus references resolve to authored focus IDs.
- Humanitarian pre-route selection requires a valid partner candidate. Isolation selection responds to war, critical harbor capacity, or sea-lane security below the critical constant. Route aborts require a current package and the opposite route is excluded.
- Vanilla NZL alternate AI plans retain empty abort blocks. This needs a proven additive retirement surface before the dormant package can activate.

## High-priority follow-up

1. Resolve the dormant activation caller and conflict receipts before enabling the package. Do not add a fallback activation path.
2. Design the convoy operating cost tradeoff for `fallout_nzl_license_every_sea_road` with a supported idea or transaction mechanic, then align the focus reward, localisation, AI weight, and cleanup.
3. Prove a safe way to retire or abort vanilla NZL alternate AI plans while preserving continuation after temporary state loss.
4. Reconcile the two focus identifier pairs in the accepted specification.
5. Keep the runtime-generated leader proof and the radio advisor asset blocker in the parent country-package audit.

## Validation and skipped checks

Meaningful checks completed:

- `hoi4.focus_inspect` recognized all 42 NZL focuses. The authored layout hash is `9f0b08848257a2a99f989ffffa4aa7a3d1e560e05cac8d4a3c9aac6a91f83911`. It reports 52 connectors, zero crossings, zero node intersections, zero same-row spacing violations, and three long connectors. Inspection JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e0c87bebbbed49c912d0629c199c144fdc93e223ae44941270e2ce9a18e0502/eb72fd4ce4a0e07355bf15ef3c7b8dc5482e9cb190ae21d2bde52f564948590a/focus-inspect.13c4aa16d8e11bce.json`.
- `hoi4.focus_render` produced current HTML, SVG, JSON, source-map, and plan artifacts. SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2a8711911712b777abd1119066bcfaa9a019edb33465eb7872500531e91d9e2/6d390155a0fecb72ccb86a1402d50ae220686570532036894c4814c00e54412f/fallout_nzl_lifeboat_focus_tree.focus.svg`.
- `hoi4.focus_raster` decoded all NZL goal assets and produced the current PNG. PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdc7e4a56d740a3832c6e97671d2fd7ab854b3ae2b6760039671a1bedc22e75e/0a7d89a40cc06974b9d0d29763c706194126b76465f61d648936a56e858e21dc/fallout_nzl_lifeboat_focus_tree.focus.png`.
- A source check confirms 42 focus nodes plus the tree id, 42 focus-level package-current availability gates plus the tree gate, 42 cancellation gates, 24 unique NZL icons with matching GFX and DDS assets, and no unknown AI focus references.
- A route-order check confirms the newly patched isolation path can reach the two-island supply ring without skipping either fishery or weatherproofing.

Skipped checks:

- HOI4 was not launched, so runtime activation, leader generation, AI plan selection, focus cancellation, and save persistence remain unobserved.
- `hoi4.focus_rewrite` was not used because no focus layout changed and inspection found no crossings or node collisions.
- No idea or decision file was changed because the convoy-cost mismatch needs broader mechanic design and a supported modifier contract.
- No activation caller or conflict-resolution fallback was added.

## Remaining route risks

The authored tree has complete route coverage and clean NZL layout geometry, with three long connectors noted by inspection. Its package gate remains generation and assignment based by design. Exact five-state ownership is required for activation, but it is not a durable current-package gate so a temporary loss of a support state does not erase continuation surfaces. Runtime-generated leaders and the radio advisor asset remain dependent on parent-owned activation and country-package proof. The convoy tradeoff promised by `license_every_sea_road` remains the highest focus reward mismatch. No separate improvement plan was written by this audit.
