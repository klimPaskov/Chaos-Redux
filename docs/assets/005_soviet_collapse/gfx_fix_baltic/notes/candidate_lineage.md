# Baltic Event 005 Candidate Lineage

This record preserves each generated source, focused edit branch, exact prompt file, tool output location, acceptance decision, and selected processed output.

## Shared production contract

All generated focus art used the built-in ImageGen tool with `transparent_background: true`; no opaque or chroma background was requested, no background removal was used, and each original returned PNG is retained at a separate `source_png/imagegen/` path. The final consumer canvas for newly generated or reframed focus icons is 94x86. Processing crops the visible native-alpha subject and aspect-preservingly contains it inside an 88x80 inner window, then centers it on a transparent 94x86 canvas. The source image, processed PNG, final DDS, and runtime crosswalk remain separate.

The style references inspected before generation were the canonical national-focus contact sheet and the individual Vanilla HOI4 references `focus_aus_danubian_socialist_communes.png`, `focus_aus_defence_of_the_homeland.png`, and `focus_generic_population_growth.png`; the reference catalog marks them `Vanilla HOI4`. Focus-piece and focus-background catalog entries are marked `reference`, so none was layered into the final art.

## Restoration pact candidates

| Candidate | Tool output and workspace source | Prompt | Decision |
| --- | --- | --- | --- |
| Restoration R1 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-091aca5b-f397-41b3-83cf-53edfe08e8fa.png`; `source_png/imagegen/goal_005_baltic_restoration_pact_source.png`; SHA-256 `288772330d0569e86b9e84caf73bf8433c2b0e8a28951618819a8eb343aaad5a` | `prompts/goal_005_baltic_restoration_pact.prompt.txt` | Rejected because the Latvian center stripe did not clearly show the required narrow white band. |
| Restoration R1 edit 1 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-b485361b-c810-48a4-a603-5f7d67cda34e.png`; `source_png/imagegen/goal_005_baltic_restoration_pact_edit1_rejected.png`; SHA-256 `4b9539a39c9fd4cf766ba8380a0622921807a8ecbd9ca6e98a86c3716b8fe6b5` | `prompts/goal_005_baltic_restoration_pact_edit1.prompt.txt` | Rejected because the focused edit still did not make the Latvian 2:1:2 bands visually clear. |
| Restoration R2 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-dc42e91c-4770-47e2-9c6a-2ff0e24deaea.png`; `source_png/imagegen/goal_005_baltic_restoration_pact_v2_source.png`; SHA-256 `b991bc3c2d8a5119024c8ac438a5e0c8ff949185201258aca61b4211bf9e3f82` | `prompts/goal_005_baltic_restoration_pact_v2.prompt.txt` | Accepted as a flag-geometry branch but rejected as final because faint pseudo-writing remained on the scroll. |
| Restoration R2 edit 1 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-68988b13-4172-47b0-9726-6ed039af1e1e.png`; `source_png/imagegen/goal_005_baltic_restoration_pact_edit2_rejected.png`; SHA-256 `d5c48733927d81df487e785d1d349eefa71b0f8f2646b425087f06f584ed1a2e` | `prompts/goal_005_baltic_restoration_pact_edit2.prompt.txt` | Rejected because removing the pseudo-writing changed the Latvian flag proportions. |
| Restoration R3 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-bf82f963-395c-4eba-ad8d-6edc13ac7cdd.png`; `source_png/imagegen/goal_005_baltic_restoration_pact_v3_source.png`; SHA-256 `caa4850029507626b46de0e285c5021e32649ef6ef4f8e016ccf5f7b6df40ed9` | `prompts/goal_005_baltic_restoration_pact_v3.prompt.txt` | Selected. The scroll is blank; Estonia is blue-black-white, Latvia is carmine-white-carmine with a narrow central white band, and Lithuania is yellow-green-red. The full-size source and the native 94x86 preview were reviewed. |

## Pan-Baltic war-room candidates

| Candidate | Tool output and workspace source | Prompt | Decision |
| --- | --- | --- | --- |
| War room P1 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-81773f3c-1e81-4f15-8a27-918af96fa829.png`; `source_png/imagegen/goal_005_baltic_pan_baltic_war_room_v1_source.png`; SHA-256 `3f98202b588ba08e63b8bec55d2a1ab2a01c282fd477d06905b06fea4d0cbc14` | `prompts/goal_005_baltic_pan_baltic_war_room.prompt.txt` | Rejected because the flags were wind-folded and the Latvian stripe geometry was not clear. |
| War room P2 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-987d3727-3cdc-4ec5-9417-b7bd396d6570.png`; `source_png/imagegen/goal_005_baltic_pan_baltic_war_room_v2_source.png`; SHA-256 `9847ff597f79fa00282cefdbcb60aba0e8083166572d77f15bf20cdbf2a1fe7a` | `prompts/goal_005_baltic_pan_baltic_war_room_v2.prompt.txt` | Rejected because the alpha-visible wreath crossed all four source-canvas edges; before processing, source bounds were `[0,0,1312,1199]` and boundary pixels included alpha values up to 219. |
| War room P2 edit 1 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-15f8403f-91c7-47f3-93fc-5c3e719fd1c8.png`; `source_png/imagegen/goal_005_baltic_pan_baltic_war_room_edit1_source.png`; SHA-256 `b2b29f479aef19e43da3f5f22f43194ef8d74c5858fda6ef90d9514df15cffb8` | `prompts/goal_005_baltic_pan_baltic_war_room_edit1.prompt.txt` | Accepted for complete framing; superseded after the central Latvian stripe geometry received a focused correction. |
| War room P2 edit 2 | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-d4a95469-91cb-4401-8454-224a476d1e19.png`; `source_png/imagegen/goal_005_baltic_pan_baltic_war_room_edit2_source.png`; SHA-256 `ea4e4fe57ceba000b256a795e6ae8e72f79ae6362c61dd4d9f65011b04b3b796` | `prompts/goal_005_baltic_pan_baltic_war_room_edit2.prompt.txt` | Selected. The outer laurel is complete and contained; three flat flags retain Estonia blue-black-white, Latvia carmine-white-carmine with a narrow white band, and Lithuania yellow-green-red. The source visible bounds are `[116,91,1195,1105]`; processed 94x86 visible bounds are `[4,3,89,83]`. |

## Other new subjects

| Asset | Tool output and retained native-alpha source | Prompt | Review |
| --- | --- | --- | --- |
| Home Guard Staff | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-975fb42d-778b-4a73-bd7a-eff178c3301e.png`; `source_png/imagegen/goal_005_baltic_home_guard_staff_source.png`; SHA-256 `3662f3eb20c83d5c02948a9c8cbd78b6567e9876eb92af711fc532f90b879773` | `prompts/goal_005_baltic_home_guard_staff.prompt.txt` | Selected as coastal watch post, crossed rifles, and Baltic pine-shore emblem. |
| Baltic Defense Compact | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-bbb4dd28-426f-4583-918c-17f715462ab1.png`; `source_png/imagegen/goal_005_baltic_baltic_defense_compact_source.png`; SHA-256 `1e6f9f3ffe30a9cec31596efdf4ddfe88b47cac1374502db2f34b2ba01ef2b72` | `prompts/goal_005_baltic_baltic_defense_compact.prompt.txt` | Selected as three linked shields and crossed rifles, visually distinct from the war room and city-chair rotation. |
| Tallinn-Riga-Vilnius Rotation | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-8d197d1a-fd86-49be-809c-485371228f73.png`; `source_png/imagegen/goal_005_baltic_tallinn_riga_vilnius_rotation_source.png`; SHA-256 `49350df1801ba0c077abf26a98032cde415560a4a87985c74ca94f6c59143ff0` | `prompts/goal_005_baltic_tallinn_riga_vilnius_rotation.prompt.txt` | Selected as three separate civic seals linked by a rotating chair. |
| German Border Pressure | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-9525f7aa-992c-4431-9800-439bc3a8aa61.png`; `source_png/imagegen/goal_005_baltic_german_border_pressure_source.png`; SHA-256 `fdefe084fae2b387721fe83d2f13ef28383d6fa9d6b76e42c1fb98cd1eac847f` | `prompts/goal_005_baltic_german_border_pressure.prompt.txt` | Selected as a dark heraldic eagle looming above a Baltic border map; no warning sign, red arrows, swastika, party symbol, text, or flag. |
| Estonian Forest-Coast Guard | `C:/Users/klimp/.codex/generated_images/01a10ece-dd27-7202-bf7e-9e2c2153a4dd/exec-4e9238e6-c300-4692-84e0-f5583d1c450a.png`; `source_png/imagegen/goal_005_baltic_estonian_forest_coast_guard_source.png`; SHA-256 `7e49f63a2a9f17226e057b56a4ba97aca2ad1e595e63e6567ec6418067bc442f` | `prompts/goal_005_baltic_estonian_forest_coast_guard.prompt.txt` | Selected as a full coastal battery, pine watch-post, and forested shoreline focus medallion, replacing the small terrain vignette. |

## Native-alpha evidence

Every selected source PNG has real alpha (`min=0`, `max=255`) and transparent corner pixels. The source files are preserved unmodified; no background-removal route or component layer was used. Final processed PNGs retain `alpha_range=[0,255]`; their exact visible bounds and hashes are in `notes/imagegen_processing_final.json` and `notes/top_crop_processing_margin2.json`.

## Selected processed files and runtime candidates

| Logical asset | Selected processed PNG | Staged DDS path(s) |
| --- | --- | --- |
| Home Guard Staff | `processed_png/goal_005_baltic_home_guard_staff_94x86.png` | `final_dds/gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_home_guard_staff.dds` |
| Restoration Pact | `processed_png/goal_005_baltic_restoration_pact_v3_94x86.png` | `final_dds/gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_restoration_pact.dds` |
| Pan-Baltic War Room | `processed_png/goal_005_baltic_pan_baltic_war_room_edit2_94x86.png` | `final_dds/gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_pan_baltic_war_room.dds`; proposed legacy alias target `final_dds/gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_pan_baltic_war_room.dds` |
| Baltic Defense Compact | `processed_png/goal_005_baltic_baltic_defense_compact_94x86.png` | `final_dds/gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_baltic_defense_compact.dds` |
| Tallinn-Riga-Vilnius Rotation | `processed_png/goal_005_baltic_tallinn_riga_vilnius_rotation_94x86.png` | `final_dds/gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_tallinn_riga_vilnius_rotation.dds` |
| German Border Pressure | `processed_png/goal_005_baltic_german_border_pressure_edgeclean_94x86.png` | Direct and focus aliases use their matching `baltic_soviet_collapse_german_border_pressure.dds` and `focus_005_baltic_soviet_collapse_german_border_pressure.dds` staged files. |
| Estonian Forest-Coast Guard | `processed_png/goal_005_baltic_estonian_forest_coast_guard_94x86.png` | `final_dds/gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_estonian_forest_coast_guard.dds` |
