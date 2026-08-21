# Report DDS Header Repair Handoff

Status: complete.

Scope: container-header-only repair of two existing 210x176 report-event DDS files.

No artwork was generated, resized, cropped, filtered, recolored, redrawn, or replaced.
The exact existing BGRA pixel payload from each malformed file was preserved byte-for-byte.

## Method

The canonical writer at `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was imported and its `write_bgra_dds` function was used with width `210`, height `176`, and the untouched payload bytes.

Before writing, the bridge file was asserted to be `147,968` bytes and its payload was taken from byte offset `128`.

Before writing, the ice-melt file was asserted to be `147,980` bytes and its payload was taken from byte offset `140`.

Both payloads were asserted to be exactly `147,840` bytes.

## Results

| File | Before length | Payload source | Before full SHA-256 | After length | After full SHA-256 | Preserved payload SHA-256 |
| --- | ---: | ---: | --- | ---: | --- | --- |
| `gfx/event_pictures/fallout/report_event_fallout_bridge_that_moved.dds` | 147,968 | `[128:]` | `72f181314114d09392550523a14def3ec62e754dd5e1ea415ae4886acadca664` | 147,968 | `5e5c063e0d77f41e442f89e736a211ad3eb44aef3468b0f7945dd402873ef287` | `82d97df529925424456fd33b83a93dd82155f780099823edb4d3e4a6c31431e7` |
| `gfx/event_pictures/fallout/report_event_fallout_ice_melt_rations.dds` | 147,980 | `[140:]` | `25c825cc6ea6d5835f23c00367bc6273991b824e20c441180ee0b604accf0493` | 147,968 | `1a52a154a95b4e52aaa78fc24e48383c67b70ca19c6bee17698bf4b79aac485d` | `410a910e101118e473a9f232f2ed05b97b10f91d0de59fbfc5f5a54dd5c73617` |

The post-repair payload at `[128:]` matches the corresponding pre-repair payload hash for both files.

## Validation evidence

Both repaired files passed all requested legacy uncompressed BGRA checks:

- `DDS ` magic at byte `0`.
- Header size `124` at byte `4`.
- Declared dimensions `210x176`.
- Pixel-format size `32` at byte `76`.
- Pixel-format flags `65`.
- FourCC `0` and 32-bit pixel depth.
- BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`.
- `DDSCAPS_TEXTURE` `0x1000` at byte `108`.
- Exact final length `147,968` bytes.
- Alpha-byte range `255..255` for both existing opaque report images.
- Pillow decode passed with size `(210, 176)` and mode `RGBA` for both files.

## Files changed

- `gfx/event_pictures/fallout/report_event_fallout_bridge_that_moved.dds`.
- `gfx/event_pictures/fallout/report_event_fallout_ice_melt_rations.dds`.
- `docs/plans/shared_gfx_asset_integrity_plans/subagent_handoffs/2026-08-21_report_dds_header_repair.md`.

No `.gfx`, `.gui`, gameplay, localisation, source-art, or other asset files were changed.

## Remaining risks and blockers

No blocker remains for the assigned container repair.

Runtime `.gfx` registration and in-game visual acceptance remain parent-owned and were not changed in this bounded task.

---

## Additional exact historical restoration

Status: complete.

On the parent-authorized restoration request, the two missing DDS files were restored exactly from commit `74cd1226e`.

For each path, `git show 74cd1226e:<path>` supplied the historical Git LFS pointer, and the matching object was resolved under `.git/lfs/objects/` by its SHA-256 OID.
The exact LFS object bytes were copied to the path-identical runtime location without generation, cropping, recoloring, filtering, or artwork replacement.

| Restored runtime path | Historical LFS OID and object size | Header dimensions | Pillow decode | Registry sprite and texture reference |
| --- | --- | --- | --- | --- |
| `gfx/event_pictures/004_random_war/report_event_random_war.dds` | `0ac8ecc5f850eec6e332ac65171b5032ec188fe330776fbc3bb7dc592d48c0b7`, `37,440` bytes | `210x176` | PASS, RGBA | `GFX_report_event_random_war` at `interface/chaosx_pictures.gfx:48`, exact texture path at line 49 |
| `gfx/event_pictures/018_random_resource/news_random_resource.dds` | `e887051f826aa448a5d19f35adac2147d9ec63369b5b87017020458f723a29db`, `31,328` bytes | `397x153` | PASS, RGBA | `GFX_news_random_resource` at `interface/chaosx_pictures.gfx:104`, exact texture path at line 105 |

Restoration validation passed for both files.

- Each restored file's full SHA-256 equals its historical LFS OID exactly.
- Each file has `DDS ` magic, a 124-byte legacy header, the declared dimensions above, one mip level, and `DDSCAPS_TEXTURE` `0x1000`.
- The report file uses the historical compressed DDS pixel format and decodes at `210x176`.
- The news file uses the historical compressed DDS pixel format and decodes at `397x153`.
- The existing `interface/chaosx_pictures.gfx` texture paths match the restored runtime paths exactly.

Additional files restored:

- `gfx/event_pictures/004_random_war/report_event_random_war.dds`.
- `gfx/event_pictures/018_random_resource/news_random_resource.dds`.

No registry, `.gfx`, `.gui`, gameplay, localisation, or unrelated asset files were edited.

No blocker remains for this exact historical restoration.
