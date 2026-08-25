# Event 014 focus layout repair handoff

Date: 2026-08-24.

Scope: bounded coordinate cleanup in `common/national_focus/014_cannibalism_focus.txt`. Ownership was limited to `x` and `y` fields of unified-tree focuses named by current `FOCUS_LAYOUT_LINEAR_DETOUR` or `FOCUS_LAYOUT_ZIGZAG_CHAIN` diagnostics. No prerequisite, exclusion, availability, reward, AI, icon, localisation, id, cost, Warlord coordinate, or Wendigo coordinate outside the listed ownership was changed.

The file already contained four unrelated, pre-existing Wendigo y-coordinate edits. They remain byte-for-byte present and were never staged or claimed: `ZZZ_wendigo_begin_the_countdown` (`y 9 -> 7`), `ZZZ_wendigo_designate_the_last_hunt` (`y 10 -> 8`), `ZZZ_wendigo_hunt_every_remaining_capital` (`y 11 -> 9`), and `ZZZ_wendigo_the_world_beneath_winter` (`y 12 -> 10`).

## Coordinate edits applied

The following unified-tree coordinate edits are present in the worktree. The first twenty came from the authored unified route plan; the final five were exposed one at a time by the subsequent linear-detour diagnostics.

| Focus id | Before | After |
| --- | --- | --- |
| `CBL_bind_the_network_territories` | `x 33, y 3` | `x 34, y 3` |
| `CBL_the_single_operational_will` | `x 28, y 15` | `x 24, y 15` |
| `CBL_confederation_under_one_name` | `x 30, y 15` | `x 28, y 15` |
| `CBL_classify_the_consumption_states` | `x 36, y 10` | `x 34, y 7` |
| `CBL_integrate_the_warbands` | `x 22, y 7` | `x 16, y 7` |
| `CBL_the_army_that_does_not_end` | `x 21, y 14` | `x 16, y 14` |
| `CBL_raider_flotillas` | `x 4, y 10` | `x 8, y 10` |
| `CBL_prison_hulks` | `x 4, y 11` | `x 8, y 11` |
| `CBL_convoy_hunt_tables` | `x 4, y 12` | `x 8, y 12` |
| `CBL_amphibious_feeding_columns` | `x 4, y 13` | `x 8, y 13` |
| `CBL_silent_anchorages` | `x 4, y 14` | `x 8, y 14` |
| `CBL_island_command_network` | `x 4, y 15` | `x 8, y 15` |
| `CBL_repair_the_captured_airframes` | `x 12, y 9` | `x 10, y 9` |
| `CBL_global_courier_network` | `x 33, y 16` | `x 30, y 16` |
| `CBL_perfect_the_false_surrender` | `x 28, y 19` | `x 30, y 19` |
| `CBL_sleep_beneath_retreat` | `x 28, y 20` | `x 30, y 20` |
| `CBL_synchronize_the_uprisings` | `x 34, y 21` | `x 30, y 21` |
| `CBL_reactivate_the_cured_networks` | `x 34, y 22` | `x 30, y 22` |
| `CBL_the_war_begins_inside` | `x 34, y 23` | `x 30, y 23` |
| `CBL_read_the_continental_weakness` | `x 24, y 18` | `x 28, y 18` |
| `CBL_terror_ultimata` | `x 26, y 19` | `x 28, y 19` |
| `CBL_cell_backed_border_incidents` | `x 24, y 20` | `x 28, y 20` |
| `CBL_host_theaters_without_borders` | `x 26, y 21` | `x 28, y 21` |
| `CBL_final_global_mobilization` | `x 32, y 26` | `x 28, y 26` |
| `CBL_dismantle_the_ordinary_world` | `x 33, y 27` | `x 28, y 27` |

The source diff was checked after the edits and contains exactly these twenty-five unified coordinate hunks plus the four pre-existing Wendigo y hunks.

## MCP evidence

The baseline unified inspect succeeded with revision `08191b7c291dba6c1a163963936a3f8d4dde4ff37b24e1166a1df442b781c7b9`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02f056685ce2479b733b29e2d9cff7de22cb39990bf175845db3de49bf2c3cb8/df30debd5b4b4dd9031869c5f868673fb8f3ebd7eb2f6f8039e1e04053769e8d/focus-inspect.08191b7c291dba6c.json`. It reported 108 focuses, 103 connectors, no crossings or node intersections, and the original Event 014 layout detours and zigzag chain.

`hoi4.focus_rewrite` accepted a complete authored 108-focus plan containing only the proposed unified coordinate changes and produced validated proposed HTML, SVG, JSON, diff, and validation artifacts. Both apply attempts returned `REWRITE_SOURCE_STALE` with `changedFiles: []` because concurrent workspace dependency changes invalidated the transaction. No MCP rewrite bytes were applied. The first proposed HTML artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9eee748735f52632af56655cb3daf2361329de9ba96dd8193017c419437ed4bf/4fe1fc91344e0a8b0ea27a6d8b09b9a1b9332be501da83cdb37a530709a871a7/cannibalism_unified_focus_tree.focus.html`.

After the manual coordinate-only fallback, the first all-tree inspect succeeded with unified revision `4f6a7fc26d59dc76f7ffe193fa7d397a35da7300a85191da8af88cc857d068a5`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9e3b090e981e6af0b32e738a5506e74719a4425c17e98a5116f4e5ce4389d4a6/4c2dfa1e64011d7f1d00eaaed318c9855a600b81d9f1b57c7088aa0929c4591a/focus-inspect.4f6a7fc26d59dc76f7ffe193fa7d397a35da7300a85191da8af88cc857d068a.json`. Unified had 108 focuses, zero crossings and node intersections, and one remaining Event 014 linear detour (`CBL_raider_flotillas -> CBL_prison_hulks`) plus two long-connector warnings from `CBL_classify_the_consumption_states`; Warlord had 68 focuses and zero Event 014 layout diagnostics; Wendigo had 28 focuses and zero Event 014 layout diagnostics.

Sequential unified inspections after the exposed naval-route moves succeeded as follows. Revision `7deab3a3546f0b614c3d4ffa36928b608377d65c2c190674cdfcbd0a03f3906b`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f52f7b0f2274b313f627084360d262bdc35921e18630d2e61ed3463cfbd85b7/cf125247dd3d12fde92758e33f1c7a5e36db895d77b8eec8be371fb52fc8f5a8/focus-inspect.7deab3a3546f0b61.json`, reported `CBL_convoy_hunt_tables -> CBL_amphibious_feeding_columns` as the remaining linear detour. Revision `57ad98a9e93fb3f14c9bf77ff1156a02cd2682516698eb631a41ad1fe45c9e8c`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fa566bd93e0f043068cf6777a8d97969ca121bbd5692e47e9567f2bc47cfe46/998892e77c82a2f9fe2c3e6bc2b56d0585d2cb4c52ad4973c7c8253a080b68ab/focus-inspect.57ad98a9e93fb3f1.json`, reported `CBL_amphibious_feeding_columns -> CBL_silent_anchorages`. Revision `4d33edb047461c5b6ee9b64fb501bb57cbe9e4f27cdb2921316e627dc63865b1`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c997323c49a5c58c0473a2d7277740830ccc9e4cfae978804b712b5d46d14599/8cf97aa72ab47f3c5a77f412c14b9a537a41f94cf050cdedd27d3ba26a88f8e0/focus-inspect.4d33edb047461c5b.json`, reported `CBL_silent_anchorages -> CBL_island_command_network`.

The final inspect after moving `CBL_island_command_network` was not completed. A later concurrent all-tree request was stopped after timeout pressure: the unified branch returned `INTERNAL_ERROR`, the Warlord branch timed out after 180 seconds, and Wendigo succeeded with revision `385b4c9a57682e3d3f19f6e208f8b2e750005b806987619ed83ed984924c0fe5`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/976751388cd8dc4edac3c0fce5fa3b5155e501dc498fe7b584fe195d399d79e2/445a540976659859c3e906f916503db0a4dc3d79f39993ad9dbbb8a115ff9df4/focus-inspect.385b4c9a57682e3d.json`; Wendigo remained at 28 focuses with zero Event 014 layout diagnostics. No `hoi4.focus_raster` call was completed for any tree in this repair pass.

The only recurring non-Event-014 diagnostic was the vanilla `continuous_restrict_freedom` missing localisation warning. The two unified `FOCUS_LAYOUT_LONG_CONNECTOR` warnings from `CBL_classify_the_consumption_states` remained in the successful inspections and are outside the requested `FOCUS_LAYOUT_LINEAR_DETOUR`/`FOCUS_LAYOUT_ZIGZAG_CHAIN` ownership set.

## Commit decision and next action

No commit was created for this repair. The coordinate changes can be separated from the Wendigo hunks at the patch-hunk level, but the required final unified inspect and all-tree raster evidence are incomplete, and zero Event 014 layout diagnostics is therefore unproven. The parent should continue with a bounded sequential inspect from the current source, move only newly named linear/zigzag focus coordinates, run final inspect and raster for all three trees, then stage only the twenty-five unified coordinate hunks. The four Wendigo y hunks must remain unstaged and unclaimed.

## Parent completion pass

The parent completed the bounded repair after the interrupted worker pass. Three additional unified coordinate changes resolved the only remaining Event 014 diagnostics:

| Focus id | Before | After | Reason |
| --- | --- | --- | --- |
| `CBL_build_the_storage_network` | `x 36, y 12` | `x 36, y 10` | Reduce its prerequisite connector from five rows to three. |
| `CBL_boards_of_captured_industry` | `x 40, y 12` | `x 40, y 10` | Reduce its prerequisite connector from five rows to three. |
| `CBL_every_ocean_a_corridor` | `x 4, y 16` | `x 8, y 16` | Keep the mechanically linear island-command chain in one column. |

The final unified inspect succeeded with revision `4a429db165ceb75420478d06fb5a24a44b51897bb78a5aa548ac4615ec82f1ea` and layout hash `29064367ddef9fc917547f65c9cfe4dcf48cda240902f03eb18e51086e8cd364`. It resolved 108 focuses and 103 connectors with zero Event 014 diagnostics, zero crossings, zero node intersections, and zero long connectors. The final Warlord inspect resolved 68 focuses with zero Event 014 diagnostics, zero crossings, and zero node intersections. The final Wendigo inspect resolved 28 focuses with the same clean result. The recurring `continuous_restrict_freedom_desc` warning belongs to the imported vanilla continuous-focus palette rather than Event 014.

Final decoded-icon raster evidence completed for all three trees:

- Unified PNG: `b480972e006a20a5e28c8b7713bbb7aac76cfa03f2d76277f0fbcfefb37594af`, 6640×3368.
- Warlord PNG: `db189c17e054f1a25371794aa7aae7eb7b4c28f968d5f9f76fba2b2bc84d4ff6`, 3120×3136.
- Wendigo PNG: `f64cacab6386fd3f87a87209b3d5e16cc86955604b83cff34b99b64d1d2c654e`, 2768×1396.

The accepted patch therefore contains twenty-eight unified coordinate-only changes. The four pre-existing Wendigo y-coordinate changes remain outside this repair's staged ownership.

## Superseded Wendigo coordinate note

The historical ownership statement above predates the parent continuation pass. The current source now deliberately owns the four Wendigo terminal-column coordinates: `ZZZ_wendigo_begin_the_countdown` y 7, `ZZZ_wendigo_designate_the_last_hunt` y 8, `ZZZ_wendigo_hunt_every_remaining_capital` y 9, and `ZZZ_wendigo_the_world_beneath_winter` y 10. The parent rechecked the final tree with MCP raster and inspect evidence; the current continuation handoff records the result and supersedes the earlier “pre-existing” disposition.
