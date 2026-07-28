# Fallout Great Lakes Lock Winter asset manifest

This manifest owns the dedicated report card for the Great Lakes Lock Winter tranche. It is fictional documentary art and does not reuse zombie, ordinary event, or Fallout blackout art.

| Asset | Purpose | Source | Processed PNG | Final DDS | Size | Sprite | Status |
|---|---|---|---|---|---:|---|---|
| `fallout_great_lakes_lock_winter` | Human opening, delayed result, and thaw callback report card | `source_png/great_lakes_lock_winter_source.png` | `processed_png/report_event_fallout_great_lakes_lock_winter.png` | `gfx/event_pictures/fallout_world_end/report_event_fallout_great_lakes_lock_winter.dds` | 210x176 | `GFX_report_event_fallout_great_lakes_lock_winter` | wired |

## Production record

The source was generated through the approved image workflow because the scene is fictional. The prompt requested an icy Great Lakes lock with covered fuel trucks, port crews, a distant lighthouse, ash-darkened snow, and no readable text, modern branding, real people, or copied flags. The source was processed with `process_report_event_image.py` using deterministic seed `663`, then converted with `convert_to_dds.py` to the legacy 32-bit BGRA DDS format.

Source SHA-256: `b8168909b6d2fe8e1cbb12980d49b1fc13413880f413e08dd1a8956daa41a602`

Processed PNG SHA-256: `2f497b0d6cb2094f7bac9b599ce9e59821a406c5315e630e0add6d103a964776`

Final DDS SHA-256: `569b6b2ddd08e18d9f173e67b2e56f2b429be06c4615377a969baaf7a6c5cc28`

The sprite is registered in `interface/fallout_world_end.gfx` and referenced by events `chaosx.fallout.663`, `chaosx.fallout.665`, and `chaosx.fallout.667`. No asset is assigned to the consequence coordinator itself.

