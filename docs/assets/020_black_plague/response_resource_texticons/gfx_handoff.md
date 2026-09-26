# Event 020 Resource Texticon Handoff

This package contains two original native-alpha inline resource icons. The parent reports both sprite registrations and three Response Capacity hover consumers are wired.

| Value | Sprite key | Runtime texture | Target size | Manifest |
| --- | --- | --- | --- | --- |
| Medical Reserve | `GFX_black_plague_medical_reserve_texticon` | `gfx/texticons/020_black_plague/medical_reserve_texticon.dds` | 18x18 | `medical_reserve_texticon_manifest.json` |
| Response Capacity | `GFX_black_plague_response_capacity_texticon` | `gfx/texticons/020_black_plague/response_capacity_texticon.dds` | 18x18 | `response_capacity_texticon_manifest.json` |

The proposed owning GFX file is `interface/020_black_plague_texticons.gfx`, supplied by the parent. The Medical Reserve token is ready for the wider cost-row rollout; no Medical Reserve localisation key was edited in this asset pass.

Both generated sources were produced by built-in `image_gen.imagegen` with `transparent_background=true`. Processed PNGs and DDS files retain real alpha, and both DDS files decode pixel-for-pixel equal to their processed PNGs. The DDS textures use 18x18 legacy uncompressed BGRA with one level and no mipmaps.

The 18x18 contact sheet at `review/contact_sheet.png` shows generated source transparency, exact native PNG and DDS canvases, nearest and smooth enlarged previews, visible alpha bounds, and the rejected first Response Capacity candidate. Candidate 01 was rejected because the two bays and cross collapsed to a low-contrast shape at native size; candidate 02 is selected.

Vanilla precedents inspected: `GFX_fuel_texticon` and `GFX_civ_factory` at 18x18, plus `GFX_manpower_texticon` at 18x16 in the installed `interface/texticons.gfx`. The canonical `icons/decisions/contact_sheet.png` was inspected before the current Event 020 Medical Reserve decision icon was used as subject context. The decision icon itself was not copied or resized.

This handoff covers source art, processed PNGs, DDS files, manifests, and the contact sheet. The parent owns the GFX and localization integration; the parent reports the GFX registration and Response Capacity hover usage are wired. No in-game validation was performed by this asset subagent.
