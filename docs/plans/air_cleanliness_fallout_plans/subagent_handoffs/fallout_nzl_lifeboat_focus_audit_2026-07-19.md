# Fallout NZL Lifeboat focus audit handoff

Date: 2026-07-19
Scope: `fallout_nzl_lifeboat_focus_tree`, its consumed NZL AI plans, and the direct focus-to-decision and focus-to-idea contracts.
Status: focus and AI safety patch complete. The package remains dormant.

## Changed files

- `common/national_focus/fallout_nzl_lifeboat_focus.txt`
  - All 42 focus nodes now include `fallout_nzl_lifeboat_package_is_current = yes` in `available`.
  - Existing state and route conditions remain in their original `available` blocks.
  - All 42 nodes now use `cancel_if_invalid = yes`. No focus was intentionally excluded.
  - `fallout_nzl_bind_the_two_islands` now uses the generation-aware `fallout_nzl_opening_result_is_current` and `fallout_nzl_domestic_result_is_current` triggers.
  - The parent-owned native `navy_experience` effect remains at `fallout_nzl_southern_cross_patrols` line 521.
- `common/ai_strategy_plans/fallout_nzl_lifeboat_ai.txt`
  - Added missing prerequisite focuses to both route plans.
  - Added a valid-partner gate to the humanitarian pre-route enable path.
  - Added the existing sea-lane security constant as a narrow isolation enable condition.
- No decision, idea, character, localisation, GFX, DDS, event, or asset binary was changed in this audit.

## Route coverage

| Route surface | Focus identifiers | Coverage and route behavior |
| --- | --- | --- |
| Opening trunk | `fallout_nzl_count_the_living`, `fallout_nzl_seat_the_lifeboat_parliament`, `fallout_nzl_open_wellington_quays`, `fallout_nzl_relay_auckland_radio`, `fallout_nzl_measure_the_dairy_stores`, `fallout_nzl_bind_the_two_islands` | All six are present. `bind_the_two_islands` has three separate prerequisite blocks, so the opening focuses are ANDed. It now requires current opening and domestic result receipts. |
| Humanitarian | `fallout_nzl_keep_the_harbor_lights`, `fallout_nzl_admit_the_first_rescue_fleet`, `fallout_nzl_publish_the_berth_ledger`, `fallout_nzl_elect_the_relief_speaker`, `fallout_nzl_guarantee_lifeboat_rights`, `fallout_nzl_pacific_relief_republic` | All six are present. The route is mutually exclusive with `fallout_nzl_draw_the_southern_cordon`. The later identity focus is gated by the humanitarian route helper. |
| Isolation | `fallout_nzl_draw_the_southern_cordon`, `fallout_nzl_close_unregistered_anchorages`, `fallout_nzl_license_every_sea_road`, `fallout_nzl_appoint_the_harbor_constable`, `fallout_nzl_reserve_the_last_berths`, `fallout_nzl_southern_refuge` | All six are present. The route is mutually exclusive with `fallout_nzl_keep_the_harbor_lights`. The later identity focus is gated by the isolation route helper. |
| Economy and survival | `fallout_nzl_dairy_relief_fleet`, `fallout_nzl_repair_the_milk_rail`, `fallout_nzl_fishery_quota_compacts`, `fallout_nzl_weatherproof_the_grain_sheds`, `fallout_nzl_rebuild_devonport`, `fallout_nzl_storm_port_engineers`, `fallout_nzl_radio_weather_chain`, `fallout_nzl_two_island_supply_ring` | All eight are present. The rail focus has the state 723 ownership gate. `weatherproof_the_grain_sheds` and `two_island_supply_ring` use separate prerequisite blocks for AND semantics. |
| Military | `fallout_nzl_home_guard_rolls`, `fallout_nzl_port_militia_drill`, `fallout_nzl_convoy_volunteer_corps`, `fallout_nzl_southern_cross_patrols`, `fallout_nzl_pirate_bearing_rooms`, `fallout_nzl_armed_rescue_cutters`, `fallout_nzl_coastal_denial_batteries`, `fallout_nzl_lifeboat_navy` | All eight are present. Southern Cross requires both militia and convoy focuses. Coastal batteries requires both anti-piracy and armed cutters and preserves exact state 284 and 1079 controls. |
| External and late | `fallout_nzl_call_the_island_radios`, `fallout_nzl_offer_rescue_passages`, `fallout_nzl_pacific_rescue_mandate`, `fallout_nzl_relief_ports_without_annexation`, `fallout_nzl_demand_quiet_seas`, `fallout_nzl_punitive_anti_piracy_patrols`, `fallout_nzl_southern_sea_exclusion_zone`, `fallout_nzl_year_ten_order` | All eight are present. The shared call uses OR semantics between the two route identities, as intended. Exclusion can bypass punitive patrols when no aggressor was proven, while a proven aggressor requires a current settlement. Year Ten uses OR prerequisites with branch-specific `available` conditions, so each route reaches its own late identity. |

The focus inspector recognized all 42 nodes. The authored layout has 52 connectors, zero connector crossings, zero node intersections, zero same-row spacing violations, and three long connectors. No focus was structurally unreachable from its authored route because of an accidental OR versus AND error.

## Missing or simplified content

The following items are not fixed by the narrow focus safety patch:

1. Four focus rewards set flags that have no decision block anywhere under `common/decisions`:
   - `fallout_nzl_home_guard_decision_open` from `fallout_nzl_home_guard_rolls` at focus line 478.
   - `fallout_nzl_dairy_convoy_decisions_open` from `fallout_nzl_dairy_relief_fleet` at focus line 347.
   - `fallout_nzl_postwar_relief_decisions_open` from `fallout_nzl_relief_ports_without_annexation` at focus line 657.
   - `fallout_nzl_quiet_seas_decisions_open` from `fallout_nzl_demand_quiet_seas` at focus line 670.
   These orphan unlock flags leave the home guard, dairy convoy, postwar relief, and quiet-seas promises shallow.
2. `fallout_nzl_license_every_sea_road` at line 268 only opens `fallout_nzl_last_berth_closure` and grants harbor capacity. Its description and the accepted focus specification also promise numbered permits, patrol windows, piracy reduction, and a convoy operating tradeoff.
3. `fallout_nzl_count_the_living` at line 24 sets the census receipt and starts event 127 or 128. Visible mechanic values are initialized in `fallout_nzl_activate_lifeboat_package` in `common/scripted_effects/fallout_nzl_lifeboat_effects.txt`, not by the focus itself. This is safe while activation remains the single initialization boundary, but the focus description and specification role are not one-to-one.
4. The accepted specification names `fallout_nzl_port_militia_training_mission` and `fallout_nzl_arm_rescue_cutters_action` as focus identifiers. The implementation focus identifiers are `fallout_nzl_port_militia_drill` and `fallout_nzl_armed_rescue_cutters`, while the decision identifiers use the specification names. This is a documentation and identifier reconciliation task.
5. Focus-created idea stages can exceed the stated three active focus-created spirits. A valid sequence can retain `fallout_nzl_dairy_relief_fleet_idea`, a route identity idea, `fallout_nzl_lifeboat_navy_idea`, and `fallout_nzl_two_island_supply_ring_idea`. `fallout_nzl_two_island_supply_ring` removes the harbor stage ideas and storm ports, but not the dairy relief fleet or final navy idea. The specification promises a route-maturity Food Compact, but no such idea exists in `common/ideas/fallout_nzl_lifeboat_ideas.txt`. The four activation foundation ideas are not counted as focus-created for this finding.
6. The live Fallout allocator still has no caller for `fallout_nzl_activate_lifeboat_package`. Samoa and Aotearoa conflict receipts remain unresolved. The dormant boundary must remain closed.

## Icon coverage

The focus file references 24 unique NZL goal sprites. All 24 have matching definitions in `interface/fallout_world_end.gfx` and matching DDS files under `gfx/interface/goals/fallout_world_end_nzl_lifeboat_state`. The table records deliberate reuse rather than missing assets.

| Icon | Focus identifiers using it |
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

No icon ID or asset was changed in this audit. The focus inspector's remaining blocking icon diagnostics are the 14 shared generic continuous-focus sprites in the installed game surface, not NZL goal sprites.

## Localisation and reward mismatch list

All 42 focus title and `_desc` keys exist in `localisation/english/fallout_nzl_lifeboat_l_english.yml`. The mismatches that need broader content work are:

- `fallout_nzl_home_guard_rolls` says district defenders and state call-up records, but its only reward is the orphan `fallout_nzl_home_guard_decision_open` flag.
- `fallout_nzl_dairy_relief_fleet` says protected dairy sailings, but its decision flag has no consumer.
- `fallout_nzl_relief_ports_without_annexation` says postwar quay aid, but its decision flag has no consumer.
- `fallout_nzl_demand_quiet_seas` says governments are told which waters are closed, but its decision flag has no consumer.
- `fallout_nzl_license_every_sea_road` says numbered permits and patrol windows, while its current reward is only the last-berth decision flag and a harbor-capacity gain.
- `fallout_nzl_count_the_living` describes the first census as deciding harbor governance, while the governance result is delivered by the opening event chain and values are initialized by activation.

The localisation file is UTF-8 with BOM and no focus key is missing. No localisation key was changed here.

## AI behavior gaps and changes

- All 42 focus nodes have an `ai_will_do` block.
- The humanitarian AI plan now includes `fallout_nzl_port_militia_drill` and `fallout_nzl_pirate_bearing_rooms`, which were required by the `southern_cross_patrols` and `coastal_denial_batteries` prerequisites.
- The isolation AI plan now includes `fallout_nzl_convoy_volunteer_corps`, which is required by `southern_cross_patrols`.
- Humanitarian pre-route enable now requires a current external partner candidate. Isolation enable now responds to sea-lane security below `constant:fallout_nzl_value.critical` in addition to war or harbor-critical conditions.
- All focus nodes lack `search_filters`, producing MCP `FOCUS_FILTER_MISSING` warnings. No filter taxonomy was invented in this patch.
- Vanilla NZL alternate AI plans retain empty abort blocks. The engine proof records this as an activation blocker because an additive retirement surface has not been proved.

## High-priority follow-up

1. Add and localize consumers for the four orphan decision-open flags, or remove those unlock rewards in an accepted redesign.
2. Reconcile the focus-created spirit cap and add the promised Food Compact or an explicitly accepted replacement sequence.
3. Reconcile the two focus ID pairs in the specification and align descriptions with actual effects.
4. Prove an additive abort surface for vanilla NZL AI plans before activation.
5. Add focus search filters and complete the pending event-log, Event Details, workbook, and dedicated asset review surfaces.

## Validation and skipped checks

Meaningful checks completed:

- `hoi4.focus_inspect` on `common/national_focus/fallout_nzl_lifeboat_focus.txt` and `fallout_nzl_lifeboat_focus_tree` recognized all 42 focuses. It reported layout hash `9f0b08848257a2a99f989ffffa4aa7a3d1e560e05cac8d4a3c9aac6a91f83911`, 52 connectors, zero crossings, zero node intersections, zero same-row spacing violations, and three long connectors.
- The same inspection found no NZL focus icon reference error and resolved all 42 focus titles. Its 14 blocking diagnostics are shared generic continuous-focus sprite errors outside this package, plus NZL search-filter warnings.
- `hoi4.focus_render` produced review artifacts. Updated SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f77e6bc08744da7cfe9b692c01b2a94c126531812006c0ef68673c781d65918a/a179452b9e8bebb4a9861267b146cb97af27c686147a128f222ab09af465ff17/fallout_nzl_lifeboat_focus_tree.focus.svg`.
- A repository count confirms 42 focus `available` gates and 42 `cancel_if_invalid` entries after the patch.
- A source audit confirms 24 unique NZL goal icons, 24 matching GFX definitions, and 24 matching DDS files.
- A source audit confirms every AI focus identifier resolves to an authored focus ID.

Skipped checks:

- HOI4 was not run, so runtime focus cancellation, AI plan selection, and save persistence remain unobserved.
- `hoi4.focus_rewrite` was not used because the authored layout was already structurally clean and no node placement changed.
- No decision implementation was added because the missing decision surfaces are a broader content tranche, not a safe focus-only patch.
- No shared generic continuous-focus sprite was changed.

## Remaining route risks

The tree now fails closed at each focus node when the package generation, identity, state package, or initialized values are no longer current. The route can still expose orphan flags, incomplete action families, and the unresolved idea-cap sequence listed above. The package remains dormant because the activation helper has no live caller and the conflict ledger and vanilla AI retirement gates remain unresolved.
