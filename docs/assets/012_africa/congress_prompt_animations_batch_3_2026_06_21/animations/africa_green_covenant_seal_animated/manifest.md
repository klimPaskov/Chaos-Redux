# Africa Green Covenant Seal Animated Manifest

## Asset

- Asset id: `africa_green_covenant_seal_animated`
- Event: `012_africa`
- Gameplay surface: Continental Congress scripted GUI Green Covenant seal state ornament
- Source type: generated per-frame fictional symbolic seal art
- Frame count: `12`
- Processed frame size: `64x64`
- Sheet size: `768x64`
- Static fallback frame: `006`, peak covenant flare

## Files

### Source Frames

- `source_frames/africa_green_covenant_seal_animated_000_source.png`
- `source_frames/africa_green_covenant_seal_animated_001_source.png`
- `source_frames/africa_green_covenant_seal_animated_002_source.png`
- `source_frames/africa_green_covenant_seal_animated_003_source.png`
- `source_frames/africa_green_covenant_seal_animated_004_source.png`
- `source_frames/africa_green_covenant_seal_animated_005_source.png`
- `source_frames/africa_green_covenant_seal_animated_006_source.png`
- `source_frames/africa_green_covenant_seal_animated_007_source.png`
- `source_frames/africa_green_covenant_seal_animated_008_source.png`
- `source_frames/africa_green_covenant_seal_animated_009_source.png`
- `source_frames/africa_green_covenant_seal_animated_010_source.png`
- `source_frames/africa_green_covenant_seal_animated_011_source.png`

### Processed Frames

- `processed_frames/africa_green_covenant_seal_animated_000.png`
- `processed_frames/africa_green_covenant_seal_animated_001.png`
- `processed_frames/africa_green_covenant_seal_animated_002.png`
- `processed_frames/africa_green_covenant_seal_animated_003.png`
- `processed_frames/africa_green_covenant_seal_animated_004.png`
- `processed_frames/africa_green_covenant_seal_animated_005.png`
- `processed_frames/africa_green_covenant_seal_animated_006.png`
- `processed_frames/africa_green_covenant_seal_animated_007.png`
- `processed_frames/africa_green_covenant_seal_animated_008.png`
- `processed_frames/africa_green_covenant_seal_animated_009.png`
- `processed_frames/africa_green_covenant_seal_animated_010.png`
- `processed_frames/africa_green_covenant_seal_animated_011.png`

### Package Outputs

- `africa_green_covenant_seal_animated_sheet_768x64.png`
- `africa_green_covenant_seal_static_64x64.png`
- `africa_green_covenant_seal_animated_preview.gif`
- `africa_green_covenant_seal_animated_contact_sheet.png`

### Final DDS Outputs

- `gfx/interface/animated/012_africa/green_covenant_seal_static_64x64.dds`
- `gfx/interface/animated/012_africa/green_covenant_seal_sheet_768x64.dds`

## Processing Notes

- Source frames were generated as separate symbolic seal artworks on a flat magenta chroma-key background so the Green Covenant glow did not conflict with the key color.
- The key background was removed to alpha, then all frames were normalized to a shared centered `64x64` transparent canvas so the medallion scale and anchor remain stable across the loop.
- The static fallback uses frame `006`, the brightest covenant state, so the non-animated sprite still communicates the intended active Green Covenant state.

## Validation

Commands used:

```bash
identify -format '%f %wx%h %[channels] %[depth]-bit\n' \
  processed_frames/*.png \
  africa_green_covenant_seal_animated_sheet_768x64.png \
  africa_green_covenant_seal_static_64x64.png \
  gfx/interface/animated/012_africa/green_covenant_seal_static_64x64.dds \
  gfx/interface/animated/012_africa/green_covenant_seal_sheet_768x64.dds

python3 - <<'PY'
from pathlib import Path
from PIL import Image
files = sorted(Path('processed_frames').glob('*.png')) + [
    Path('africa_green_covenant_seal_animated_sheet_768x64.png'),
    Path('africa_green_covenant_seal_static_64x64.png'),
    Path('/home/klim/projects/chaos_redux/gfx/interface/animated/012_africa/green_covenant_seal_sheet_768x64.dds'),
    Path('/home/klim/projects/chaos_redux/gfx/interface/animated/012_africa/green_covenant_seal_static_64x64.dds'),
]
for p in files:
    im = Image.open(p).convert('RGBA')
    a = im.getchannel('A')
    amin, amax = a.getextrema()
    corners = [im.getpixel((0,0))[3], im.getpixel((im.width-1,0))[3], im.getpixel((0,im.height-1))[3], im.getpixel((im.width-1,im.height-1))[3]]
    white = green = magenta = 0
    for r, g, b, aa in im.getdata():
        if aa >= 250:
            if r >= 245 and g >= 245 and b >= 245:
                white += 1
            if g >= 245 and r <= 20 and b <= 20:
                green += 1
            if r >= 245 and b >= 245 and g <= 20:
                magenta += 1
    print(f'{p.name}|alpha={amin}-{amax}|corners={corners}|opaque_white={white}|opaque_green={green}|opaque_magenta={magenta}')
PY
```

Result summary:

- All twelve processed frames are `64x64 srgba 8-bit`.
- Sheet PNG is `768x64 srgba 8-bit`.
- Static fallback PNG is `64x64 srgba 8-bit`.
- Final DDS files are `768x64 srgba 8-bit` and `64x64 srgba 8-bit`.
- Alpha range is `0-255` for every processed frame, the sheet PNG, the static PNG, and both final DDS files.
- All four corners are fully transparent for every processed frame, the sheet PNG, the static PNG, and both final DDS files.
- Opaque white matte pixels: `0` in every processed frame, the sheet PNG, the static PNG, and both final DDS files.
- Opaque green matte pixels: `0` in every processed frame, the sheet PNG, the static PNG, and both final DDS files.
- Opaque magenta matte pixels: `0` in every processed frame, the sheet PNG, the static PNG, and both final DDS files.
