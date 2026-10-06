# Event 021 decision icon crop repair handoff

The two Event 021 decision icons fill their existing 32x32 canvases with the original source subjects.
The parent reviewed both icons on light and dark backgrounds and accepted the framing.
The parent corrected the relief subject's residual opacity after the first crop, raising its nonzero alpha mean from 192.175 to 201.092 without changing its 28x27 bounds or transparent corners.
The final relief DDS SHA-256 is `12aa00530ad9baac214c8d69ef9eca30b0529488b7de7bc8a6ee8a6c722ba5e4`.
Its decoded pixels exactly match `processed_png/decisions/decision_021_relief_corridor_alpha_corrected.png`, and the final size check reports `ghosted: false` for both icons.
`contact_sheets/parent_alpha_review.png` and `records/parent_final_size.json` supersede the relief measurements in the worker's original table below.

## Scope and processing

I changed only the two authorized Event 021 runtime DDS assets and their repair evidence. Existing sprite names, dimensions, and `.gfx` texture paths remain stable. The existing entries are `GFX_decision_event021_relief_corridor` at `interface/021_random_civil_war.gfx:37-38` and `GFX_decision_event021_reconstruction` at lines 45-46.

The Event 021 rows in `C:\Users\klimp\Videos\chaos_redux_trailer\records\gfx_review\gfx_fix_plan.md` authorize recropping and enlarging the original subjects to about 28 px on the existing 32x32 canvas. The cross-cutting framing rule at line 113 targets roughly 90% fill with a 2-4 px margin.

I reused the existing native-alpha generated masters and their archived prompts. The full 1254x1254 RGBA source PNGs remain unchanged. Each derivative crop uses the source alpha>=8 bounds, preserving all RGBA samples inside the crop, then applies proportional premultiplied-alpha Lanczos resizing and centers the subject on a transparent 32x32 canvas. The repair adds no art or symbols and makes no opacity adjustment.

## Before and after measurements

Bounds use half-open coordinates. Subject-alpha means match the `.tools/gfx/gfx.py size` report.

| Sprite | Before alpha>=16 bounds | Before size | Before alpha mean | After bounds | After size | After alpha mean | Final DDS SHA-256 |
|---|---|---:|---:|---|---:|---:|---|
| `GFX_decision_event021_relief_corridor` | `[8, 8, 25, 24]` | `17x16` | `148.643` | `[2, 2, 30, 29]` | `28x27` | `192.175` | `5159ce6d45c78cbb0ba2f1fc78add79693a74087aff49bf8a4f3d92e63a0f165` |
| `GFX_decision_event021_reconstruction` | `[7, 8, 25, 24]` | `18x16` | `175.081` | `[2, 3, 30, 28]` | `28x25` | `216.106` | `d206c589871ea0ada2788a9b0611ac1c68bc53dbcebd5bea08945fae0e0062b3` |

Each installed DDS is a 32x32, 4,224-byte straight-alpha BGRA texture with alpha 0-255. Its decoded pixels equal the processed PNG exactly, and all canvas corners remain transparent. The relief record includes `ghosted: true` with an empty findings list; visual light and dark composites show a complete, legible subject without edge clipping or halo. I preserved the source transparency and left the diagnostic for parent disposition.

## Reference and validation evidence

I inspected `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decisions/contact_sheet.png` before the individual canonical references `decision_generic_guerilla_base_2.png` and `decision_generic_disband_irregulars.png`. Their catalog rows are at `CATALOG.md:219-220`. The installed vanilla sprite definitions are in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\decisions.gfx` at lines 1233-1234 and 2899-2900.

The repository `.tools/gfx/gfx.py dds` helper used the shared canonical BGRA writer and returned zero findings. The staged DDS dimensions, header, file lengths, and decoded pixels were checked. The installed DDS files then passed `python -B .tools/gfx/gfx.py size` with `--profile decision --canvas 32 32 --margin 2`, which returned zero findings. The round-trip contact sheet includes current and final DDS imagery on light and dark backgrounds, native 32px swatches, smooth 8x views, and the vanilla examples.

## Git handoff note

The repository ignores `docs/assets/` via `.gitignore:80`. The new source crops, previews, staged DDS outputs, review sheets, and evidence records remain in the shared filesystem but do not appear in normal Git status. The parent can force-add only the approved package paths if those sources and previews belong in the commit. I did not change the ignore rule or stage files.

## Files changed

- `gfx/interface/decisions/021_random_civil_war/decision_021_relief_corridor.dds`
- `gfx/interface/decisions/021_random_civil_war/decision_021_reconstruction.dds`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/manifest.md`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/source_png/decisions/decision_021_relief_corridor_source_crop_alpha8.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/source_png/decisions/decision_021_reconstruction_source_crop_alpha8.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/processed_png/decisions/decision_021_relief_corridor.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/processed_png/decisions/decision_021_reconstruction.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/contact_sheets/decision_icon_repair_2026-10-06.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/contact_sheets/decision_icon_repair_dds_roundtrip_2026-10-06.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/candidate_dds/processed_png/decisions/decision_021_relief_corridor.dds`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/candidate_dds/processed_png/decisions/decision_021_reconstruction.dds`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/review/decoded_dds/decision_021_relief_corridor_roundtrip.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/review/decoded_dds/decision_021_reconstruction_roundtrip.png`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/records/process_record.json`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/records/dds_conversion.json`
- `docs/assets/021_random_civil_war/repair_2026-10-06/decision_icons/records/dds_roundtrip_record.json`
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/2026-10-06_icon_repair.md`

Skills used: `chaos-redux-event-assets` for the canonical decision references, crop, alpha, DDS, and preview contract; `chaos-redux-subagents` for this bounded ownership and handoff boundary. The source prompt files retain the original ImageGen source-mode evidence.

No `.gfx` or gameplay wiring change is needed.
Parent visual review and the relief-alpha correction are complete.
The game was not launched.
