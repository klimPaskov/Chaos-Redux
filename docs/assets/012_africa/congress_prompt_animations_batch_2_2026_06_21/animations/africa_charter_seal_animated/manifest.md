# Africa Charter Seal Animated Manifest

## Asset

- Asset id: `africa_charter_seal_animated`
- Event: `012_africa`
- Gameplay surface: Continental Congress scripted GUI charter-state seal
- Source type: generated per-frame fictional symbolic seal art
- Frame count: `8`
- Processed frame size: `64x64`
- Sheet size: `512x64`
- Static fallback frame: `004`, peak charter flare

## Files

### Source Frames

- `source_frames/africa_charter_seal_animated_000_source.png`
- `source_frames/africa_charter_seal_animated_001_source.png`
- `source_frames/africa_charter_seal_animated_002_source.png`
- `source_frames/africa_charter_seal_animated_003_source.png`
- `source_frames/africa_charter_seal_animated_004_source.png`
- `source_frames/africa_charter_seal_animated_005_source.png`
- `source_frames/africa_charter_seal_animated_006_source.png`
- `source_frames/africa_charter_seal_animated_007_source.png`

### Processed Frames

- `processed_frames/africa_charter_seal_animated_000.png`
- `processed_frames/africa_charter_seal_animated_001.png`
- `processed_frames/africa_charter_seal_animated_002.png`
- `processed_frames/africa_charter_seal_animated_003.png`
- `processed_frames/africa_charter_seal_animated_004.png`
- `processed_frames/africa_charter_seal_animated_005.png`
- `processed_frames/africa_charter_seal_animated_006.png`
- `processed_frames/africa_charter_seal_animated_007.png`

### Package Outputs

- `africa_charter_seal_animated_sheet_512x64.png`
- `africa_charter_seal_static_64x64.png`
- `africa_charter_seal_animated_preview.gif`
- `africa_charter_seal_animated_contact_sheet.png`

### Final DDS Outputs

- `gfx/interface/animated/012_africa/charter_seal_prompt_sheet_512x64.dds`
- `gfx/interface/animated/012_africa/charter_seal_prompt_static_64x64.dds`

## Processing Notes

- Source frames arrived as opaque green-screen PNGs.
- The green screen was chroma-keyed with ImageMagick, then each frame was trimmed, resized to fit inside a stable centered `64x64` transparent canvas, and appended into a horizontal frame sheet.
- The fallback static frame uses frame `004`, the brightest charter flare, so a non-animated UI still communicates active charter readiness.

## Validation

Commands used:

```bash
identify -format '%f %wx%h %[channels] %[depth]-bit\n' processed_frames/*.png africa_charter_seal_animated_sheet_512x64.png africa_charter_seal_static_64x64.png gfx/interface/animated/012_africa/charter_seal_prompt_*.dds
```

Result summary:

- Eight processed frames are `64x64 srgba 8-bit`.
- Sheet is `512x64 srgba 8-bit`.
- Static fallback is `64x64 srgba 8-bit`.
- Final DDS files are `512x64 srgba 8-bit` and `64x64 srgba 8-bit`.

Pixel validation:

- Processed PNG and DDS alpha ranges: `0-255`.
- All four corners are fully transparent.
- Opaque white matte pixels: `0`.
- Opaque green matte pixels: `0`.
