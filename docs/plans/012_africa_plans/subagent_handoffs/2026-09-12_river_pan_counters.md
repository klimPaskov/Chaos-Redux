# Riverborn and Pan Sappers counter finalize handoff

Date: 2026-09-12.

Owner: `/root/river_sapper_finalize/river_pan_counters`.

Status: both bounded counter packages are complete production candidates and remain `needs_user_review` for parent visual review. The revised frame 1 art now follows the inspected installed vanilla bordered NATO/schematic plate family.

The owned package roots are `docs/assets/012_africa/models_3d/riverborn/counters/finalize_20260912/` and `docs/assets/012_africa/models_3d/pan_sappers/counters/finalize_20260912/`. The only shared planning surface updated by this subagent is this handoff. No shared GFX, unit-definition, gameplay, runtime texture, or historical counter file was edited or copied.

## Consumer and reference evidence

The exact consumers are `common/units/012_africa_strange_forces.txt:306` for `riverborn`, with `sprite = riverborn`, `map_icon_category = infantry`, and `type = { infantry }`, and `common/units/012_africa_strange_forces.txt:213` for `pan_sappers`, with `sprite = chaosx_pan_sappers`, `map_icon_category = infantry`, and `type = { infantry support }`.

The existing parent-owned registrations are `GFX_unit_riverborn_icon_medium`, `GFX_unit_riverborn_icon_medium_white`, `GFX_unit_pan_sappers_icon_medium`, and `GFX_unit_pan_sappers_icon_medium_white` in `interface/012_africa_strange_force_counters.gfx`. Stable runtime targets remain `gfx/interface/counters/divisions_large/unit_<slug>_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_<slug>_icon.dds`; all candidate DDS files remain package-local.

The matching canonical contact sheets were inspected before individual references at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png` and `units/land/map_counters/contact_sheet.png`. The installed definitions and DDS were inspected at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, `gfx/interface/counters/divisions_large/unit_infantry_icon.dds`, `unit_engineer_icon.dds`, `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`, and `onmap_unit_engineer_icon.dds`.

The exact installed infantry comparison references are large `unit_infantry_icon.dds` SHA-256 `b33a8e3b69cc789eb0e31ba99f4e5ba4e5b0a8b51ec1a7a7f709c3516f720c23` and map `onmap_unit_infantry_icon.dds` SHA-256 `58ab78662c2a64a519b8d5d144582e7b2785915bd0a0a822696d87a9de6f766c`. Both are strict legacy BGRA32. The contract is large `152x42` with two adjacent `76x42` frames and map `60x12` with two adjacent `30x12` frames, each `noOfFrames = 2`.

The frame semantics are now stated without inferring a static selected state. The documented `noOfFrames = 2` layout indexes the left half as frame 0 and the right half as frame 1. Installed infantry strips show frame 0 as the normal identity family and frame 1 as a pale bordered schematic plate. Installed `interface/settings.gui` exposes `NATO_COUNTERS`, and `localisation/english/frontend_l_english.yml` resolves it to `Use NATO symbols`, supporting the NATO/schematic family label. The engine chooses the active frame dynamically for the consumer state; the source GFX declaration itself does not name a permanent selected state.

The sampled vanilla green anchors are RGB `(20,34,21)`, dominant `(73,106,73)`, and pale `(154,175,147)`. Frame 0 identity art is luminance graded against this exact family with the recorded 1.45 scale and piecewise anchors. Map frame 0 uses neutral grayscale with opaque luminance lifted into the inspected `94..236` range using gamma `0.5`; frame 1 preserves the generated near-black plate border and glyph ink as opaque RGB `(0,0,0)` while grading its pale plate into the same installed range. No old counter pixels or copied vanilla glyphs were used.

All new state-plate sources were generated with the official `image_gen__imagegen` tool and native transparency requested in the initial prompt. Each package retains its prompt TXT files, source PNGs, processed frame PNGs, enlarged previews, strict DDS, decoded round trips, manifests, comparison sheets, and `gfx_handoff.md`. Prompt SHA-256 records are in each `manifest.json`.

## Riverborn package

Active source records are:

- `source_png/riverborn_large_identity_source.png` SHA `ea6e6daa93499232021c6b3ee48875bac30a54e57a71f9ba7fcd345c9ad1cb1b`, native `1685x933`, alpha `[0,255]`.
- `source_png/riverborn_large_schematic_strong_plate_source.png` SHA `ee676ff65be8f7d0a9b467b28afc63879857865b64f7f71d22a1237943b9f2fb`, native `1684x934`, alpha `[0,255]`.
- `source_png/riverborn_map_identity_local_removed.png` SHA `e477e89192aa2eb338e0c0b87a98d962b26de49135f61f5a55133089c583dcc8`, native `1983x793`, alpha `[0,255]`.
- `source_png/riverborn_map_schematic_strong_plate_source.png` SHA `7cbc4c59ad27fc34abb12500180a5b6118a78b6bb0733490df61568403c9bb10`, native `1774x887`, alpha `[0,255]`.

The old Riverborn source candidates remain retained, including `riverborn_large_schematic_source.png` SHA `38bff706bbda2ab1bb29ac150cc15575f399508e2275941f126cf6e9f15a5f12`, `riverborn_large_schematic_transparency_edit.png` SHA `be2ac1c3dbf5f2a9ace8a71b66f67c6ebaacd891cd3fc11de40ebda171d9c692`, `riverborn_large_schematic_plate_source.png` SHA `8385de1957d32aa50e9b0d1b46fb7d5cb98d8a684dfdd4a943c473691d9351db`, and `riverborn_map_selected_source.png` SHA `8bf818ab8f4b210459df62a80fceb32f4f56339642979d5d4aadf9bf9043f229`. The opaque checkerboard map input and failed edit remain retained, as do the previous map plate candidates. The new strong bordered plate sources supersede the previous active plate mappings.

The Riverborn active frame order is `[normal_identity_frame0, nato_schematic_plate_frame1]` for both large and map strips. Processed frame bounds are large `[19,4,57,38]` and `[9,5,67,36]`, map `[7,1,22,11]` and `[4,0,26,12]`. The exact `30x12` Riverborn map frame 1 contains `89` opaque RGB `(0,0,0)` border/glyph pixels. Strip SHA-256 values are large `c252b0cf22997c97576fecc608de654a6eb01ba409b2be5664d4c70a40229bc5` and map `0ed08aea3af4fb5c2c2769fece82096f4bab3c9705f35c8c416b3b8711a1a30e`.

Package DDS SHA-256 values are large `acbe7f747a8ebb2abb6bd05c842e3e3d127fb4e386b37c58bb976785d2e1363d` and map `792362bbf1f1c293e383cb76f816ef898f2245b414a8d6bfa019714d3b6c3d3b`.

## Pan Sappers package

Active source records are:

- `source_png/pan_sappers_large_identity_source.png` SHA `515aef9cc456b5da7e66d4259b3a5ee850e59d9ec123cae7f52805fc6d386ce0`, native `1688x932`, alpha `[0,255]`.
- `source_png/pan_sappers_large_schematic_strong_plate_source.png` SHA `2ea64314cc41717a3f2ffbb300a7c3cf3e693fa193a308508c02544ba7e912fa`, native `1685x933`, alpha `[0,254]`.
- `source_png/pan_sappers_map_identity_source.png` SHA `81d6bbbef77f412091fe0cbce98c1b1acdf1e0ca7b6a6198444fd5815e3eee74`, native `1983x793`, alpha `[0,255]`.
- `source_png/pan_sappers_map_schematic_strong_plate_source.png` SHA `982b96965aad13d309815fac6b70f02c716f3633d6cc4e5511c93727a97bc837`, native `1942x809`, alpha `[0,255]`.

The old Pan Sappers source candidates remain retained, including `pan_sappers_large_schematic_source.png` SHA `33dcc405a056e92350b002f9e0362a01190273bb7b9c8ed718451f062fd2ac02`, `pan_sappers_large_schematic_plate_source.png` SHA `962b5e324aec34fcc939180d9ba80972c9fb215eef941107b04931191dac134b`, `pan_sappers_map_selected_source.png` SHA `7617c61bb7422a43e2ac16a0baee39826a6bad0104f8c256e74135f9940e3b3e`, and `pan_sappers_map_selected_plate_schematic_source.png` SHA `65f84078b2337e8288c90512aff1d6674bceb7f8ef0c2d4c3d01c8d7eaf8e002`. The new strong bordered plate sources supersede the previous active plate mappings.

The Pan Sappers active frame order is `[normal_identity_frame0, nato_schematic_plate_frame1]` for both large and map strips. Processed frame bounds are large `[20,4,55,38]` and `[9,5,67,36]`, map `[3,1,27,11]` and `[1,0,28,12]`. The exact `30x12` Pan Sappers map frame 1 contains `108` opaque RGB `(0,0,0)` border/glyph pixels. Strip SHA-256 values are large `de6c9ff528296ced9e4babc877535872095bc02285ad6716f65cac692ec97b7f` and map `552ea0a9ecda52edc27d24b1aa3a470bd95d31befecdbad93120aaff3872e45b`.

Package DDS SHA-256 values are large `a4a6befe11b4391530a9039f2ca7f8313a89bea3da3134e668598d1c20fdfee7` and map `12c2c29c6b0058820fd2fd9f1b63df40b58e2aea441fc64474b3d05689bb2499`.

## Review and validation

Parent visual review sheets are:

- `docs/assets/012_africa/models_3d/riverborn/counters/finalize_20260912/contact_sheets/riverborn_counter_contact_sheet.png`.
- `docs/assets/012_africa/models_3d/riverborn/counters/finalize_20260912/contact_sheets/riverborn_installed_vanilla_comparison.png`.
- `docs/assets/012_africa/models_3d/pan_sappers/counters/finalize_20260912/contact_sheets/pan_sappers_counter_contact_sheet.png`.
- `docs/assets/012_africa/models_3d/pan_sappers/counters/finalize_20260912/contact_sheets/pan_sappers_installed_vanilla_comparison.png`.

Each installed comparison sheet contains direct vanilla-infantry versus candidate rows for large frame 0, large frame 1, map frame 0, and map frame 1 at native frame size plus nearest-neighbour enlargement. Enlarged strip previews remain in each package's `enlarged_previews/` folder.

The Riverborn contact sheet SHA is `2f688ae0872eb4da20f201420188e9007d062500fd0f0659f09830bd143ce005`, its installed comparison SHA is `1b32b6678f91c0e62774988a0af70e53ac2c6c0843a8fb0f5db8824e90812213`, and its enlarged strip SHAs are `5b3d56a057c9c23075707749eb45f0bc56a7b925b03bc13b8901c9901cbf0b13` and `19b019fac89bde2073f159d97e737a56c4e2c1516dc6db37dee5fa0a5820f563`.

The Pan Sappers contact sheet SHA is `db4bee550d3750d647b930ec1054f569084b2c62a4ca794e97c24d27dbda8263`, its installed comparison SHA is `cf341e45cc62a752cadd1a4e5aa3097c02054777909dd0434a82c9da1164269e`, and its enlarged strip SHAs are `0f80903e8639744b3b9bf4e3cdedd40cfc597c0cc34e98d08b7b61463c828fb9` and `ce2a1e88dc0d125c138f338cd0af752472fe3dcba63feeef3a8360d59b9571df`.

The package-local verifier reads each final DDS as strict legacy uncompressed BGRA32, confirms exact dimensions and file lengths, preserves alpha, and checks pixel equality against the processed strip. Both large files are `25,664` bytes with `608` byte rows. Both map files are `3,008` bytes with `240` byte rows. All four decoded round trips pass pixel equality, and both manifests record `installed_vanilla_comparison = true` and `frame_state_semantics_verified = true`.

The builder is `docs/assets/012_africa/models_3d/riverborn/counters/finalize_20260912/validation/build_counter_packages.py`; it writes only the two owned package roots. DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` for the four package-local outputs.

## Simplifications, omissions, and blockers

Riverborn map identity is the only transparency fallback. Both native transparency attempts for its inherited map identity returned checkerboards, so the untouched source and failed edit are retained and `prompts/riverborn_map_identity_transparency_fallback.txt` records the verified local Pillow/NumPy/SciPy 8-connected border flood fill over mean RGB at least `190` and channel chroma at most `18`. Its transparent corners, zero nonzero border pixels, zero transparent RGB residue, visible bounds `[543,61,1510,714]`, and no canvas-edge clipping are recorded in `manifest.json`.

No Meshy call, Blender operation, runtime promotion, GFX edit, gameplay edit, or historical counter replacement was performed. No other simplification or blocker remains inside the bounded packages. Parent contact-sheet review, any requested art iteration, runtime promotion, and live consumer validation remain pending by ownership boundary, so both packages stay `needs_user_review`.
