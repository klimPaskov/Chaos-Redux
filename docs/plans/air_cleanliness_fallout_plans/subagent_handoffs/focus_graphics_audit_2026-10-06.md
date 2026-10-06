# Fallout generic focus graphics and layout audit handoff

Date: 2026-10-06

Disposition: implemented evidence for parent review. The parent owns the gameplay and graphics source edits and final completion claim.

## Scope and acceptance basis

This audit covers the 33-focus national tree fallout_generic_focus_tree in common\national_focus\fallout_consolidated_focus.txt, its sprite definitions in interface\fallout_consolidated.gfx, and the generated focus DDS package in gfx\interface\goals\fallout_generic.

The parent accepted the three coordinate-only changes within G5 on 2026-10-06 and asked for a matched final focus inspection and raster pass. The position updates preserve each focus prerequisite, availability block, reward, localisation reference, and AI block.

The source proof FALLOUT_GENERIC_FOCUS_TREE_PROOF.md records this 33-focus generic tree as the complete core Fallout focus surface and lists its route architecture. Bespoke successor-country trees remain outside this accepted generic-tree scope.

## Changed source surface and identifiers

The focus source diff contains 33 icon-token replacements and three y-coordinate changes, for 36 additions and 36 removals. No prerequisite, effect, availability, localisation, AI, or route-gating clause changed.

The three coordinate changes are:

| Focus id | Before | After | Route effect |
| --- | --- | --- | --- |
| fallout_generic_federate_survivor_leagues | (20,13) | (20,10) | Same prerequisite and reward; the federation payoff is one row below invite_neighbor_compacts. |
| fallout_generic_reclaim_the_heartland | (18,13) | (18,10) | Same prerequisite and reward; the reclamation payoff is one row below settle_the_new_border. |
| fallout_generic_year_ten_order | (20,15) | (20,12) | Same two-option OR prerequisite and late-game requirements; the capstone remains below both route endpoints. |

The final coordinates place the two route endpoints at x=18 and x=20 on row 10, with the Year Ten focus at x=20 on row 12. The regional leaves stay at row 11, so the compacted capstones do not overlap their lane.

The focus identifiers and icon tokens are now one-to-one across all 33 focuses. The previous source used 16 icon tokens for 33 focuses; the final source uses 33 unique tokens.

The .gfx file declares 33 base sprites and 33 shine sprites. Every pair points to its matching 94x86 DDS, and each shine sprite uses gfx/FX/buttonstate.lua. All 33 runtime DDS headers report 94x86, and the paired-token, path, and file-presence audit found zero issues.

The shared .gfx diff also contains five B7 USA decision sprite path changes outside this focus audit: GFX_decision_fallout_usa_depot_belt_repair, GFX_decision_fallout_usa_guard_muster, GFX_decision_fallout_usa_lakes_charter, GFX_decision_fallout_usa_radio_sweep, and GFX_decision_fallout_usa_reconstruction_drive. They now point into gfx\interface\decisions\fallout_successor_b7_usa. The broader graphics owner should review those five consumers in their task handoff.

## Route coverage

| Route layer | Focus coverage | Status |
| --- | --- | --- |
| Survival opening | fallout_generic_wake_the_survivors; fallout_generic_map_the_ruins; fallout_generic_hold_the_capital | Present and unchanged. |
| Government and charter | fallout_generic_civic_compact; fallout_generic_ration_congress; fallout_generic_command_directorate; fallout_generic_shelter_council; fallout_generic_publish_survival_charter | Present and unchanged. |
| Recovery and logistics | fallout_generic_reopen_power_grid; fallout_generic_repair_rail_spine; fallout_generic_reclaim_workshops | Present and unchanged. |
| Military security | fallout_generic_raise_survivor_guard; fallout_generic_train_frontier_columns; fallout_generic_arm_the_cordon | Present and unchanged. |
| Diplomacy and federation | fallout_generic_open_radio; fallout_generic_found_frontier_pact; fallout_generic_invite_neighbor_compacts; fallout_generic_federate_survivor_leagues | Present and unchanged. Federation still requires its active Pact leadership and an allied member. |
| Border pressure and reclamation | fallout_generic_claim_the_empty_belt; fallout_generic_issue_border_ultimatum; fallout_generic_settle_the_new_border; fallout_generic_reclaim_the_heartland | Present and unchanged. The reclamation route remains target-gated. |
| Regional programme | fallout_generic_open_the_regional_ledger plus its nine region leaves | Present and unchanged; one matching regional leaf is exposed per country. |
| Late order | fallout_generic_year_ten_order | Present and unchanged; its prerequisite block still allows either the federation or heartland endpoint. |

The nine regional leaves are fallout_generic_north_america_relay, fallout_generic_europe_water_councils, fallout_generic_eurasian_inland_road, fallout_generic_east_asia_seed_banks, fallout_generic_south_asia_delta_routes, fallout_generic_mena_quarantine_roads, fallout_generic_africa_river_wards, fallout_generic_latin_america_water_charters, and fallout_generic_oceania_remote_stations.

Each leaf has an allow_branch check against its own fallout_region_id constant. This makes one leaf available for a given country's assigned region; it is intentional regional selection.

## Icon coverage

| Focus id | Base sprite | Runtime DDS | Shine status |
| --- | --- | --- | --- |
| fallout_generic_wake_the_survivors | GFX_goal_fallout_generic_wake_the_survivors | gfx/interface/goals/fallout_generic/goal_fallout_generic_wake_the_survivors.dds | Base + shine verified |
| fallout_generic_map_the_ruins | GFX_goal_fallout_generic_map_the_ruins | gfx/interface/goals/fallout_generic/goal_fallout_generic_map_the_ruins.dds | Base + shine verified |
| fallout_generic_hold_the_capital | GFX_goal_fallout_generic_hold_the_capital | gfx/interface/goals/fallout_generic/goal_fallout_generic_hold_the_capital.dds | Base + shine verified |
| fallout_generic_civic_compact | GFX_goal_fallout_generic_civic_compact | gfx/interface/goals/fallout_generic/goal_fallout_generic_civic_compact.dds | Base + shine verified |
| fallout_generic_ration_congress | GFX_goal_fallout_generic_ration_congress | gfx/interface/goals/fallout_generic/goal_fallout_generic_ration_congress.dds | Base + shine verified |
| fallout_generic_command_directorate | GFX_goal_fallout_generic_command_directorate | gfx/interface/goals/fallout_generic/goal_fallout_generic_command_directorate.dds | Base + shine verified |
| fallout_generic_shelter_council | GFX_goal_fallout_generic_shelter_council | gfx/interface/goals/fallout_generic/goal_fallout_generic_shelter_council.dds | Base + shine verified |
| fallout_generic_publish_survival_charter | GFX_goal_fallout_generic_publish_survival_charter | gfx/interface/goals/fallout_generic/goal_fallout_generic_publish_survival_charter.dds | Base + shine verified |
| fallout_generic_reopen_power_grid | GFX_goal_fallout_generic_reopen_power_grid | gfx/interface/goals/fallout_generic/goal_fallout_generic_reopen_power_grid.dds | Base + shine verified |
| fallout_generic_repair_rail_spine | GFX_goal_fallout_generic_repair_rail_spine | gfx/interface/goals/fallout_generic/goal_fallout_generic_repair_rail_spine.dds | Base + shine verified |
| fallout_generic_reclaim_workshops | GFX_goal_fallout_generic_reclaim_workshops | gfx/interface/goals/fallout_generic/goal_fallout_generic_reclaim_workshops.dds | Base + shine verified |
| fallout_generic_raise_survivor_guard | GFX_goal_fallout_generic_raise_survivor_guard | gfx/interface/goals/fallout_generic/goal_fallout_generic_raise_survivor_guard.dds | Base + shine verified |
| fallout_generic_train_frontier_columns | GFX_goal_fallout_generic_train_frontier_columns | gfx/interface/goals/fallout_generic/goal_fallout_generic_train_frontier_columns.dds | Base + shine verified |
| fallout_generic_arm_the_cordon | GFX_goal_fallout_generic_arm_the_cordon | gfx/interface/goals/fallout_generic/goal_fallout_generic_arm_the_cordon.dds | Base + shine verified |
| fallout_generic_open_radio | GFX_goal_fallout_generic_open_radio | gfx/interface/goals/fallout_generic/goal_fallout_generic_open_radio.dds | Base + shine verified |
| fallout_generic_found_frontier_pact | GFX_goal_fallout_generic_found_frontier_pact | gfx/interface/goals/fallout_generic/goal_fallout_generic_found_frontier_pact.dds | Base + shine verified |
| fallout_generic_invite_neighbor_compacts | GFX_goal_fallout_generic_invite_neighbor_compacts | gfx/interface/goals/fallout_generic/goal_fallout_generic_invite_neighbor_compacts.dds | Base + shine verified |
| fallout_generic_claim_the_empty_belt | GFX_goal_fallout_generic_claim_the_empty_belt | gfx/interface/goals/fallout_generic/goal_fallout_generic_claim_the_empty_belt.dds | Base + shine verified |
| fallout_generic_issue_border_ultimatum | GFX_goal_fallout_generic_issue_border_ultimatum | gfx/interface/goals/fallout_generic/goal_fallout_generic_issue_border_ultimatum.dds | Base + shine verified |
| fallout_generic_settle_the_new_border | GFX_goal_fallout_generic_settle_the_new_border | gfx/interface/goals/fallout_generic/goal_fallout_generic_settle_the_new_border.dds | Base + shine verified |
| fallout_generic_open_the_regional_ledger | GFX_goal_fallout_generic_open_the_regional_ledger | gfx/interface/goals/fallout_generic/goal_fallout_generic_open_the_regional_ledger.dds | Base + shine verified |
| fallout_generic_north_america_relay | GFX_goal_fallout_generic_north_america_relay | gfx/interface/goals/fallout_generic/goal_fallout_generic_north_america_relay.dds | Base + shine verified |
| fallout_generic_europe_water_councils | GFX_goal_fallout_generic_europe_water_councils | gfx/interface/goals/fallout_generic/goal_fallout_generic_europe_water_councils.dds | Base + shine verified |
| fallout_generic_eurasian_inland_road | GFX_goal_fallout_generic_eurasian_inland_road | gfx/interface/goals/fallout_generic/goal_fallout_generic_eurasian_inland_road.dds | Base + shine verified |
| fallout_generic_east_asia_seed_banks | GFX_goal_fallout_generic_east_asia_seed_banks | gfx/interface/goals/fallout_generic/goal_fallout_generic_east_asia_seed_banks.dds | Base + shine verified |
| fallout_generic_south_asia_delta_routes | GFX_goal_fallout_generic_south_asia_delta_routes | gfx/interface/goals/fallout_generic/goal_fallout_generic_south_asia_delta_routes.dds | Base + shine verified |
| fallout_generic_mena_quarantine_roads | GFX_goal_fallout_generic_mena_quarantine_roads | gfx/interface/goals/fallout_generic/goal_fallout_generic_mena_quarantine_roads.dds | Base + shine verified |
| fallout_generic_africa_river_wards | GFX_goal_fallout_generic_africa_river_wards | gfx/interface/goals/fallout_generic/goal_fallout_generic_africa_river_wards.dds | Base + shine verified |
| fallout_generic_latin_america_water_charters | GFX_goal_fallout_generic_latin_america_water_charters | gfx/interface/goals/fallout_generic/goal_fallout_generic_latin_america_water_charters.dds | Base + shine verified |
| fallout_generic_oceania_remote_stations | GFX_goal_fallout_generic_oceania_remote_stations | gfx/interface/goals/fallout_generic/goal_fallout_generic_oceania_remote_stations.dds | Base + shine verified |
| fallout_generic_federate_survivor_leagues | GFX_goal_fallout_generic_federate_survivor_leagues | gfx/interface/goals/fallout_generic/goal_fallout_generic_federate_survivor_leagues.dds | Base + shine verified |
| fallout_generic_reclaim_the_heartland | GFX_goal_fallout_generic_reclaim_the_heartland | gfx/interface/goals/fallout_generic/goal_fallout_generic_reclaim_the_heartland.dds | Base + shine verified |
| fallout_generic_year_ten_order | GFX_goal_fallout_generic_year_ten_order | gfx/interface/goals/fallout_generic/goal_fallout_generic_year_ten_order.dds | Base + shine verified |

Review of the eight native/4x contact sheets in docs\assets\air_cleanliness_fallout\graphics\contact_sheets found a coherent painted-medallion family with distinct subjects, clear route silhouettes, and matching decoded DDS panels. The sheets cover all 33 assets across focus batches 01, 02, 03, 04, 06, 07, 08, and 09.

The full-tree final raster shows all 33 focus icons, including the regional row and the compacted route capstones. No missing or repeated focus icon references remain.

## Localisation and reward mismatch list

All 33 focus titles resolved in the final MCP inspect. A source-key check found all 66 title and description keys for the 33 focuses in localisation\english\fallout_consolidated_l_english.yml.

No localisation keys or reward text changed in this tranche. The artwork subjects match the focus names at native and enlarged review sizes, and the source diff leaves the focus rewards untouched. The wider reward-to-description audit remains the responsibility of the existing Fallout generic-tree proof and parent review.

MCP reports one unrelated installed-game warning: continuous_restrict_freedom_desc is missing from the vanilla generic continuous-focus palette at game:common/continuous_focus/generic.txt lines 498-525. It is not a Fallout focus key and was left untouched.

## AI behavior gaps

No AI field or focus weight changed. The existing proof records archetype-aware route weights and region-aware modifiers for the generic tree. No probability audit was rerun because this graphics and coordinate tranche changes no weighted surface; any later AI-weight change needs the required probability auditor workflow.

## Before and after MCP evidence

| Evidence | Before | After |
| --- | --- | --- |
| Source revision | abeab8b06d3cccaf388ee4933a81b7f9a41f1aba58767da6c6560e0eb2ae4a73 | 2c0e98e05ece8af96531b59a79b107c0458970107652fdb9c617b6e823b1722c |
| Layout hash | 7f73fe81728d555d51eed8b334cee0f90e9f84b3bcca0c2aab5df3cc5ef1e70c | b3b29630f5f343814778e7c865428a02e17dab2d103b7d979afc6e403abbc666 |
| Focuses / connectors | 33 / 36 | 33 / 36 |
| Crossings / node intersections | 0 / 0 | 0 / 0 |
| Same-row spacing violations | 0 | 0 |
| Long connector warnings | 3 regional edges | 3 regional edges |
| Linear detour warnings | 2 | 0 |
| Maximum y / row count | 15 / 16 | 12 / 13 |
| Raster dimensions | 4880x1976 | 4880x1628 |

The final rendered view lowers the tree height by three rows and removes the two four-row route detours without changing route structure. Connector count and regional branch geometry remain stable.

The three long connector warnings remain on fallout_generic_open_the_regional_ledger to fallout_generic_africa_river_wards, fallout_generic_latin_america_water_charters, and fallout_generic_oceania_remote_stations, at horizontal spans of 10, 12, and 14 columns respectively. These are the far leaves of a nine-way region fan. The all-source MCP render displays every authored leaf, while the focus renderer does not evaluate country-specific allow_branch conditions; source inspection confirms that each country exposes only its matching leaf. The current view therefore proves authored geometry, not a conditional engine view. In each actual country tree the fan reduces to one connector and has no competing regional edges.

The warnings measure connector distance only; final inspect reports zero crossings and zero node overlaps. I recommend keeping the fan positions in this graphics tranche. A remote-island country still has one visibly long connector from the regional ledger; live country-view appearance remains unverified.

## Validation and skipped checks

Completed task-specific checks:

- hoi4.focus_inspect ran before and after the source changes and recognized all 33 focuses.
- hoi4.focus_render produced matched before and after HTML, SVG, and JSON layouts.
- hoi4.focus_raster produced before and after 4880-pixel-wide PNGs with decoded focus icons.
- The final icon consumer check found 33 unique focus tokens, 33 base sprites, 33 shine sprites, 33 DDS files, and zero missing or mismatched pairs.
- All 33 DDS headers report 94x86.
- The focus source diff is limited to 33 icon assignments and three y-coordinate assignments.
- A localisation key check found all 66 focus title and description keys.

Skipped meaningful checks and limits:

- No HOI4 game session was launched, and no country-specific runtime screenshot was produced. The project assigns live-game validation to the user.
- MCP inspect and render do not evaluate the nine country-specific allow_branch conditions, so the per-country single-leaf behavior is inferred from the exact source gates.
- No probability workflow ran because no AI weight or other weighted surface changed.
- hoi4.focus_rewrite was not used because this audit did not apply a source patch.

## Remaining risks and simplifications

No simplification was introduced to the accepted 33-focus generic tree. No route, reward, availability, localisation, or AI behavior was removed or substituted.

The remote-island regional connector remains long in the authored layout, and the renderer cannot show its conditional single-leaf country view. The five B7 USA decision sprite path changes share the .gfx file and need review in the broader graphics task.

Bespoke successor-country trees were not audited because the accepted scope is the core generic tree.

## Files and evidence paths

Implementation surfaces reviewed:

- common\national_focus\fallout_consolidated_focus.txt; SHA-256 1a55234090fa0fa1e6ac9f1c3a1b54955e5dd87a1882aef7d606464523c0d61c.
- interface\fallout_consolidated.gfx; SHA-256 77667fdda03241919f6460366151cee5568b53b363b65849f4c59780bfff97b2.
- gfx\interface\goals\fallout_generic; 33 DDS files.

Durable audit outputs written by this subagent:

- docs\plans\air_cleanliness_fallout_plans\subagent_handoffs\focus_graphics_audit_2026-10-06.md.
- docs\plans\air_cleanliness_fallout_plans\subagent_handoffs\focus_graphics_audit_2026-10-06.json.
- C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\air_cleanliness_fallout_plans\subagent_handoffs\focus_graphics_audit_2026-10-06_baseline.png; SHA-256 51cbc0a6a2699be97b69ff98391812dd29452e6626d91a27d88fa1c96b5f9253.
- C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\air_cleanliness_fallout_plans\subagent_handoffs\focus_graphics_audit_2026-10-06_final.png; SHA-256 7a434b0ea83519208d8c2413ecd89adc1ef61012f2d2aca227af8d38f6af2083.

MCP artifact references:

- Baseline inspect JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32cad9a2b29b5b54a34bbe4578a707555493ea64583552bd917203861c6c630e/7f36bbd7c1bd666bd221796f3abc5ef4c2e3f1df8a611347df916fe636277ffb/focus-inspect.abeab8b06d3cccaf.json.
- Baseline render HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ecc0c7578b022863f4111e7a4375cc819d7679be39308670affa59dad890984/b7de5447761b50e5ade6c1f6a7323f80a63039374c20f7065de1fd3750cf7/fallout_generic_focus_tree.focus.html.
- Baseline render SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/726a3ac5d046b733bf5dd95c7206e8fcbfd8192a6e8a4d25699d659d3025542e/345c3583c8394637cc7b86cb7ca09b8e8eb78ad3b4c02e58ee44f7ed3777be97/fallout_generic_focus_tree.focus.svg.
- Baseline raster PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51cbc0a6a2699be97b69ff98391812dd29452e6626d91a27d88fa1c96b5f9253/b9b45f27617772425ebbf72de5d7944da7ff8741565dc6915556001650593e2b/fallout_generic_focus_tree.focus.png.
- Final inspect JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1eff997f5acf90fecc96a630c5b35d8c045f3682d64fe168d3d2a5a2362ae672/f7b5bd846273009f0a5cdf08dcd495c9c8edfe227591ba1ff28e866d2a395d35/focus-inspect.2c0e98e05ece8af9.json.
- Final render HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc1ba0eebc0ac06e355685956ab5ef2ccc634616ba81c28ef2e98f0ca310b7fd/749949198e73406fe44c709a93c6070b13a5001a62880c11d4773ee9854b81fa/fallout_generic_focus_tree.focus.html.
- Final render SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d31235c8addd2facd7a88fbddbde4437f413a2c3df240f7fe1ea38e5033d60f5/337e056c2a8fdb9dedda4e56599116fa7976f9d9f21a8cff887e2d37c0194719/fallout_generic_focus_tree.focus.svg.
- Final raster PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a434b0ea83519208d8c2413ecd89adc1ef61012f2d2aca227af8d38f6af2083/7a0aec770a20a4a4e1f712cd2d67756c8f33ee7d8c4461c6a6483012c5b53647/fallout_generic_focus_tree.focus.png.

Skills used: chaos-redux-focus-trees, chaos-redux-event-assets, and chaos-redux-subagents. No skill file was created or changed.


## Post-commit matched refresh and NZL visual review

After parent commit f0d05ef16, the source received a comment-only correction at lines 37-39 of common\national_focus\fallout_consolidated_focus.txt. The final generic focus inspect, render, and raster now bind to source revision c0c9c76855b9962b59e6208707c834ecc9c6190ec1dc3d2038aa82d0f981fc91 and full source SHA-256 6229c37e810aac70059f559b47b7046fb9991b6f74cd5e89a0d02c7ecbd9f91b. The comment correction did not change the generic tree layout hash, icons, coordinates, prerequisites, rewards, availability, localisation, or AI. Current layout hash remains b3b29630f5f343814778e7c865428a02e17dab2d103b7d979afc6e403abbc666.

The current inspector still reports 33 focuses, 36 connectors, zero crossings, zero node intersections, zero same-row spacing violations, three long regional fan edges, and zero linear detours. The updated inspect JSON is linked at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fee502aeb436f8ee0570b3d570b5bbaf4db9c6eee00e7b0be2675106a3fdc12a/a704237ba8027419d8ce39044946eb479e7cfc69a4f7c46a5dbd86131f5acb9a/focus-inspect.c0c9c76855b9962b.json. The updated raster artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a434b0ea83519208d8c2413ecd89adc1ef61012f2d2aca227af8d38f6af2083/ab03bfdc5a8ec384feb0f5f33fb297a7cae848208565e0d4626b43e868694cbd/fallout_generic_focus_tree.focus.png. Its 4880x1628 bytes still match the durable local final PNG and SHA-256 recorded above.

### NZL Lifeboat visual audit

I verified the supplied full NZL raster from 56 byte-range reads against its declared 453,909-byte length, PNG signature, 6992x1744 dimensions, and SHA-256 0cc5bdbd3591ce90834c6ac2c8eec6601abadef5497b087bae7ba156fc9efad8. The saved full image is C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\air_cleanliness_fallout_plans\subagent_handoffs\focus_graphics_audit_2026-10-06_nzl_full.png.

The NZL inspector revision is a2d843d701810dabc43cc86d164d9eaff031fc0e608c7fff34e85a73684b358d and its layout hash is 9f0b08848257a2a99f989ffffa4aa7a3d1e560e05cac8d4a3c9aac6a91f83911. It found 42 focuses and 52 connectors, zero crossings, zero node intersections, zero same-row spacing violations, three long connectors, five linear detours, and two zigzag chains. The matched NZL render HTML is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3cc300c85729f26f06b50d4a3447ab822f6b3dab3ffef19d797b89d8dc8101b/624061105fd3f662d5c287c7bbc6367b0810cbaf1bffc1e0d42c26159402bde2/fallout_nzl_lifeboat_focus_tree.focus.html, with SVG companion hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c302f7861c7534078dc5482d2d974b6b8d55f255214f69689a69fc8b7a947e5c/f0f6cc293151681efd56df36b401e7b3392ccef190b17f4438fcbe31c5ab9594/fallout_nzl_lifeboat_focus_tree.focus.svg.

The full PNG visibly confirms a broad fan from fallout_nzl_bind_the_two_islands at (18,3) to home_guard_rolls at (2,4), dairy_relief_fleet at (32,4), and rebuild_devonport at (36,4). The fan is long across open space but does not cross other connectors or pass through focus nodes. The three edges serve separated military, relief, and port/logistics lanes; a local move of one opener would bend its child chain, so I recommend no isolated fan coordinate change.

The two zigzags are visible in fallout_nzl_rebuild_devonport (36,4) -> fallout_nzl_storm_port_engineers (38,5) -> fallout_nzl_radio_weather_chain (36,6) and fallout_nzl_offer_rescue_passages (14,10) -> fallout_nzl_pacific_rescue_mandate (12,11) -> fallout_nzl_relief_ports_without_annexation (14,12). The first route steps right then back left, and the second steps left then back right.

For the shorter elect-speaker branch, moving fallout_nzl_guarantee_lifeboat_rights alone from (12,7) to (10,7) would shift a diagonal to its child, fallout_nzl_pacific_relief_republic at (12,8). The smallest complete straightening is to move fallout_nzl_elect_the_relief_speaker from (10,6) to (12,6); that places it under publish_the_berth_ledger at (12,5), then guarantee_lifeboat_rights at (12,7) and pacific_relief_republic at (12,8) remain straight. Elect_the_relief_speaker still requires admit_the_first_rescue_fleet at (8,5) and publish_the_berth_ledger at (12,5), so its two-parent convergence remains explicit.

I also recommend two coordinate-only moves for the flagged zigzags: fallout_nzl_storm_port_engineers from (38,5) to (36,5), aligning the rebuild_devonport / storm_port_engineers / radio_weather_chain sequence on x=36; and fallout_nzl_pacific_rescue_mandate from (12,11) to (14,11), aligning the offer_rescue_passages / pacific_rescue_mandate / relief_ports_without_annexation sequence on x=14.

Collision review found no focus at the proposed target cells. The nearest current nodes are two columns away from storm_port_engineers at (36,5), ten columns away from the proposed elect_the_relief_speaker at (12,6), and ten columns away from pacific_rescue_mandate at (14,11). The proposed moves alter only x positions; all prerequisites, rewards, availability, localisation, and AI remain untouched. Parent accepted and applied these coordinate-only recommendations; the matched after inspect and raster are recorded in the addendum below.

Skills used remain chaos-redux-focus-trees, chaos-redux-event-assets, and chaos-redux-subagents. No source, localisation, GFX, AI, gameplay, or staged Git edits were made by this subagent.



## Parent-applied NZL coordinate repairs and matched after evidence

The parent accepted and applied the three coordinate-only NZL moves below after reviewing the proposal. All focus prerequisites, rewards, availability, localisation, and AI clauses remain unchanged.

| Focus id | Before | After | Result |
| --- | --- | --- | --- |
| fallout_nzl_elect_the_relief_speaker | (10,6) | (12,6) | Sits below publish_the_berth_ledger; the existing fleet and ledger prerequisites remain intact, and the downstream rights and republic chain stays at x=12. |
| fallout_nzl_storm_port_engineers | (38,5) | (36,5) | Aligns rebuild_devonport, storm_port_engineers, and radio_weather_chain vertically at x=36. |
| fallout_nzl_pacific_rescue_mandate | (12,11) | (14,11) | Aligns offer_rescue_passages, pacific_rescue_mandate, and relief_ports_without_annexation vertically at x=14. |

The post-change NZL inspector revision is e50dda97a3f3e6b41da44926e59c48517aa85c83acdc21cc7349cc672d0e4828, with layout hash ec6bb005e8ae43c12e34cd39e6cc051bd30c9d8a54b339d9287d791c7930ede3. It reports 42 focuses, 52 connectors, zero crossings, zero node intersections, zero same-row spacing violations, zero linear detours, zero zigzag chains, and the same three long connector warnings on the Bind the Two Islands fan.

The verified after PNG is saved at C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\air_cleanliness_fallout_plans\subagent_handoffs\focus_graphics_audit_2026-10-06_nzl_after.png. It is 6640x1744, 445,736 bytes, and SHA-256 8b81a7fd5eea5315df1a176c54760b33a13abc290433aa362c0e1f9a592a34e5. The MCP raster artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b81a7fd5eea5315df1a176c54760b33a13abc290433aa362c0e1f9a592a34e5/45e3dfbaf49a9cb55636190c88717e985186bf3970558b2ea1b041fa3a8fe575/fallout_nzl_lifeboat_focus_tree.focus.png.

The generic tree was re-inspected against the same whole-file source revision. Its focus source revision is d8fe64177815903793b30fcaa1acb44ee6291b927c1a5438232f81f42beae5f9 and its full source SHA-256 is e6916e64cf71e0822aea34a16aa1f7d6b6a0c396bbc60652bd3e66aa339af828. Its layout hash remains b3b29630f5f343814778e7c865428a02e17dab2d103b7d979afc6e403abbc666 with 33 focuses, 36 connectors, zero crossings, zero node intersections, zero spacing violations, and three conditional regional long-connector warnings.

The coordinate repairs are applied and validated. The broad Bind the Two Islands fan remains visually long across open space but has no intersections or crossings, so no further lane move is proposed in this bounded audit.
