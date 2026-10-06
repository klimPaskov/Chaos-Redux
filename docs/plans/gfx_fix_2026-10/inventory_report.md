# Cross-cutting GFX inventory (2026-10)

Path-level evidence: [cross_cutting_inventory.json](cross_cutting_inventory.json), 1409 registered sprite rows over 1234 unique texture paths.

The focus-family inventory includes review-plan aliases and active `GFX_focus_*` aliases. Hashes and decoded dimensions refer to each registered texture. Candidate status calls for visual edge review; it does not authorize automatic erosion. Portraits, full-canvas art, and animated sheets are excluded from automatic edge erosion.

## Rule 1: chroma-edge focus candidates

Rows by family:
- 015: 111.
- baltic: 79.
- blr: 105.
- caucasus: 79.
- central_asia: 84.
- internal: 76.
- kaz: 184.
- moldova: 91.
- soviet_collapse: 36.
- ukr: 157.

Named chroma-fringe findings in the fix plan: 87 sprite rows. All-family edge inspection candidates: 1000 rows. The named-fringe count is narrower than the cross-cutting review set.

Named chroma-fringe examples recorded from the plan include:
- `GFX_baltic_soviet_collapse_coastal_defense_batteries` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_coastal_defense_batteries.dds` ([94, 86]; SHA-256 `35cb4084f64e301b11eeeb8623745e23301768b7e4875514396896b20fb9fcca`).
- `GFX_baltic_soviet_collapse_german_border_pressure` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_german_border_pressure.dds` ([94, 86]; SHA-256 `73f56c358193b9756aaf4b540e0efad9f621d0625f243ca30ce8b6d5b4b01dcf`).
- `GFX_baltic_soviet_collapse_latvian_port_guard_boards` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_latvian_port_guard_boards.dds` ([94, 86]; SHA-256 `0949cbfb1642f626a80c446512c9cd5e0bc8ddf63a03bddb549d2a7819128175`).
- `GFX_baltic_soviet_collapse_military_border_government` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_military_border_government.dds` ([94, 86]; SHA-256 `4e678676c74712878d7d7753982ac68f7f0777b5bdceefba6cb433bd3e3752db`).
- `GFX_baltic_soviet_collapse_no_retreat_from_the_capital` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_no_retreat_from_the_capital.dds` ([94, 86]; SHA-256 `dc4cf0adc3b06f6b3f4f85d2cf6f200c5123d35c2a543fb5e3315fcdd1862cef`).
- `GFX_baltic_soviet_collapse_scandinavian_listening_mission` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_scandinavian_listening_mission.dds` ([94, 86]; SHA-256 `be7fdfc62c5e3df6ad4145ddaf9d326f84d67b075e7af164d4f05900ee378e8f`).
- `GFX_baltic_soviet_collapse_the_border_front_at_home` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_the_border_front_at_home.dds` ([94, 86]; SHA-256 `152690375e5e0ced33beb076cabc46d363baf434250e737db69a84d07cc4174d`).
- `GFX_baltic_soviet_collapse_university_volunteer_lists` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_university_volunteer_lists.dds` ([94, 86]; SHA-256 `96ec50d79734add2193d28005b51dc26c925f86d19855cb24cad9310b5293509`).
- `GFX_baltic_soviet_collapse_volunteer_rifle_societies` -> `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_volunteer_rifle_societies.dds` ([94, 86]; SHA-256 `ac36ed8aa335eb19ea1bc16b3f2c8125255ce7539914a68b4e852a52d85790b9`).
- `GFX_blr_soviet_collapse_guide_companies` -> `gfx/interface/goals/005_soviet_collapse/blr_soviet_collapse_guide_companies.dds` ([94, 86]; SHA-256 `e7c9e2729e813f0943ea1732c6a92940f7ea88aa7b6b6d8875c1e6a795a79170`).
- `GFX_blr_soviet_collapse_last_train_east` -> `gfx/interface/goals/005_soviet_collapse/blr_soviet_collapse_last_train_east.dds` ([94, 86]; SHA-256 `2dd34f57d661ca98fbc1563bc142e324ed3aecae2deaa56c445fda56ccf4d8a1`).
- `GFX_blr_soviet_collapse_league_supply_timetables` -> `gfx/interface/goals/005_soviet_collapse/blr_soviet_collapse_league_supply_timetables.dds` ([94, 86]; SHA-256 `2eff3aaf4d2515261504a6782ac367866f737cdf13cce9629b56e51b542cd18d`).
- `GFX_caucasus_soviet_collapse_black_sea_or_caspian_routes` -> `gfx/interface/goals/005_soviet_collapse/caucasus_soviet_collapse_black_sea_or_caspian_routes.dds` ([94, 86]; SHA-256 `06d55cab5782e15db3f3cb19b5dbe3a58ed32f4aa5abab4659fc32731a8e7522`).
- `GFX_baltic_soviet_collapse_coastal_defense_batteries` -> `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_coastal_defense_batteries.dds` ([100, 88]; SHA-256 `f8658ec9aa6c135ac3901bb676e3a60d7afb1560880decbb5f07e5e950560d74`).
- `GFX_baltic_soviet_collapse_german_border_pressure` -> `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_german_border_pressure.dds` ([94, 86]; SHA-256 `73f56c358193b9756aaf4b540e0efad9f621d0625f243ca30ce8b6d5b4b01dcf`).

The JSON contains all 87 named-fringe rows, including aliases, edge pixel counts by frame, and full plan issue evidence.

Manual edge exceptions:
- `GFX_blr_soviet_collapse_council_bargains_forests` -> `gfx/interface/goals/005_soviet_collapse/blr_soviet_collapse_council_bargains_forests.dds`; manual_review_no_transparent_canvas; size=[100, 88]; SHA-256 `d8fff287063260d771975f1aee2729ae8597c80d73e54c0ef2aa5e3ed2cbabc8`.
- `GFX_focus_blr_soviet_collapse_council_bargains_with_forests` -> `gfx/interface/goals/005_soviet_collapse/focus_005_blr_soviet_collapse_council_bargains_with_forests.dds`; manual_review_no_transparent_canvas; size=[100, 88]; SHA-256 `d8fff287063260d771975f1aee2729ae8597c80d73e54c0ef2aa5e3ed2cbabc8`.

## Rule 4: ghosted-alpha check

407 registered sprites are checked. Scope counts: {'shared_chaosx_missing_unit_texticons_small_icon': 31, 'shared_chaosx_texticons_small_icon': 79, '005_TNC_or_ukr_focus_set': 204, 'mapmode_deselected': 7, 'plan_rule4_specific_issue': 6, 'camp_repression_ledger_glyph_or_tab': 6, 'shared_chaosx_subuniticons_small_icon': 74}. This covers the 005 TNC/Ukraine focus aliases, all small frames in the indexed shared texticon, missing-unit-texticon and subuniticon groups, camp repression ledger glyphs and all tab sprites, and every deselected mapmode sprite. Alpha is measured per declared frame over nonzero-alpha subject pixels. A frame below 200 fails; exactly 200 passes. 195 sprites have at least one failing frame. Every alias, texture, frame mean, dimension, and hash is in JSON.

Path/decode exceptions:
- None; the vanilla deselected-mapmode sheet resolved to the installed game DDS and its source path/hash are in JSON.

## Evidence and gaps

- Read-only inputs: `gfx_fix_plan.md`, `gfx_issues.json`, `index.json`, current `interface/**/*.gfx` registry.
- Per-frame alpha, dimensions, digest, and edge diagnostics use `.tools/gfx/gfx.py` (`sprite_registry`, `load`, `frames`, `alpha_stats`, `edge_stats`, `digest`).
- Shared fringe findings are the specific magenta, violet, purple, or green key cases in the plan. Other dark blurred halos remain review candidates and are not labeled chroma defects.
- The parent successfully used HOI4 reference context/search/read routes; see reference_evidence.json. A narrow source_lookup stayed pending and was stopped. This inventory uses source/pixel checks and claims no runtime render evidence.
