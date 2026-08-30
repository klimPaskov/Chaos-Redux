# Event 023 mission icon production handoff

Status: production complete; parent `.gfx` wiring and visual review remain `needs_user_review`.

Asset: `sov_nuclear_mission_device_assembly`, a dedicated 33x32 mission icon for the timed Event 023 device-assembly/production mission.

| Source PNG | Processed PNG | Runtime DDS | Size | Sprite proposal |
| --- | --- | --- | ---: | --- |
| `docs/assets/023_sov_nuclear_bombs/source_png/missions/sov_nuclear_mission_device_assembly_source.png` | `docs/assets/023_sov_nuclear_bombs/processed_png/missions/sov_nuclear_mission_device_assembly_33x32.png` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_mission_device_assembly.dds` | 33x32 | `GFX_mission_sov_nuclear_mission_device_assembly` |

Suggested target registry: parent-owned `interface/023_sov_nuclear_bombs.gfx`.

SHA-256:

- Source PNG: `9a63672cdbe08964f8a87988cfe496a06fbb8f05db56e96c3d17113c5e9bbe16`
- Processed PNG: `3e0eae495662bcb810d702550af2805cc0e74f5a983d7335b389e8e50796deab`
- Runtime DDS: `6ef8ffaa4b79bfd310cf888cb8aae2b9c69f8dcb2029640984ba56eed217c035`

Validation: PASS. The source and processed PNGs retain native transparent alpha with alpha range 0..255 and zero-alpha corners. The processed bounds are `(1, 1, 32, 31)`. The DDS is a 33x32, 4352-byte, one-level legacy uncompressed BGRA texture with the required header masks and texture caps. Decoded DDS pixels match the processed PNG exactly.

Provenance: Generated with the official built-in ImageGen workflow on 2026-08-30 with a genuine transparent background request. No external source and no background-removal fallback were used. The source is an original period-industrial composition of a sealed olive-green casing in a precision jig with wrenches, micrometer, and reactor-control hardware, distinct from the existing Event 023 mission icons. Processing used the existing Event 023 contained Lanczos resize convention with a one-pixel inset and transparent-fringe clamp.

Canonical reference: inspected `icons/missions/contact_sheet.png` and all five individual mission references under the single canonical `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference` root before generation. The existing Event 023 mission contact sheet was refreshed with the source, processed, and DDS round-trip row.

No blocker. No `.gfx`, gameplay, localisation, GUI, workbook, portrait, flag, counter, animation, or 3D files were edited.
