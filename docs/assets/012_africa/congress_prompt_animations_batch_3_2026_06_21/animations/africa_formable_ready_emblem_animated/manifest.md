# Africa Formable Ready Emblem Animated Manifest

## Asset

- Asset id: `africa_formable_ready_emblem_animated`
- Event: `012_africa`
- Status: `complete`
- Gameplay surface: Continental Congress scripted-GUI formable/world-order readiness emblem
- Source type: generated per-frame fictional symbolic emblem art
- Generated with: built-in `image_gen`
- First-generation result: accepted
- Frame count: `8`
- Processed frame size: `64x64`
- Sheet size: `512x64`
- Static fallback frame: `004`

## Files

### Source Inputs

- `africa_formable_ready_emblem_animated_source_strip.png`
- `africa_formable_ready_emblem_animated_source_strip_alpha.png`

### Source Frames

- `source_frames/africa_formable_ready_emblem_animated_000_source.png`
- `source_frames/africa_formable_ready_emblem_animated_001_source.png`
- `source_frames/africa_formable_ready_emblem_animated_002_source.png`
- `source_frames/africa_formable_ready_emblem_animated_003_source.png`
- `source_frames/africa_formable_ready_emblem_animated_004_source.png`
- `source_frames/africa_formable_ready_emblem_animated_005_source.png`
- `source_frames/africa_formable_ready_emblem_animated_006_source.png`
- `source_frames/africa_formable_ready_emblem_animated_007_source.png`

### Processed Frames

- `processed_frames/africa_formable_ready_emblem_animated_000.png`
- `processed_frames/africa_formable_ready_emblem_animated_001.png`
- `processed_frames/africa_formable_ready_emblem_animated_002.png`
- `processed_frames/africa_formable_ready_emblem_animated_003.png`
- `processed_frames/africa_formable_ready_emblem_animated_004.png`
- `processed_frames/africa_formable_ready_emblem_animated_005.png`
- `processed_frames/africa_formable_ready_emblem_animated_006.png`
- `processed_frames/africa_formable_ready_emblem_animated_007.png`

### Package Outputs

- `africa_formable_ready_emblem_animated_sheet_512x64.png`
- `africa_formable_ready_emblem_static_64x64.png`
- `africa_formable_ready_emblem_animated_preview.gif`
- `africa_formable_ready_emblem_animated_contact_sheet.png`

### Final DDS Outputs

- `gfx/interface/animated/012_africa/formable_ready_prompt_static_64x64.dds`
- `gfx/interface/animated/012_africa/formable_ready_prompt_sheet_512x64.dds`

## Prompt Summary

- One eight-panel horizontal strip on a flat `#ff00ff` chroma-key background
- Same bronze-and-gold pan-African medallion in every panel
- Fixed framing and scale
- Readiness loop from dormant ember through peak starburst and back down
- No text, no flags, no logos

## Processing Notes

- The accepted first generation attempt produced an eight-panel strip with eight drawn readiness states.
- The strip was copied into the package, chroma-keyed to alpha, segmented by connected non-transparent components, padded, and resized into centered `64x64` transparent frames.
- The final sheet was assembled left-to-right from the processed frames.
- Static fallback uses frame `004`, the clearest peak-readiness state.
- DDS conversion used the repo's documented ImageMagick fallback with uncompressed DDS output.

## Commands

### Chroma Key Removal

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
  --input docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_formable_ready_emblem_animated/africa_formable_ready_emblem_animated_source_strip.png \
  --out docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_formable_ready_emblem_animated/africa_formable_ready_emblem_animated_source_strip_alpha.png \
  --auto-key border \
  --soft-matte \
  --transparent-threshold 12 \
  --opaque-threshold 220 \
  --despill
```

Result:

- Wrote `africa_formable_ready_emblem_animated_source_strip_alpha.png`
- Detected key color: `#fb04f9`
- Transparent pixels: `1299393/1573538`
- Partially transparent pixels: `6963/1573538`

### Dimension Audit

```bash
identify -format '%f %wx%h %[channels] %[depth]-bit\n' \
  docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_formable_ready_emblem_animated/source_frames/*.png \
  docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_formable_ready_emblem_animated/processed_frames/*.png \
  docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_formable_ready_emblem_animated/africa_formable_ready_emblem_animated_sheet_512x64.png \
  docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_formable_ready_emblem_animated/africa_formable_ready_emblem_static_64x64.png \
  gfx/interface/animated/012_africa/formable_ready_prompt_static_64x64.dds \
  gfx/interface/animated/012_africa/formable_ready_prompt_sheet_512x64.dds
```

Result summary:

- Source frames: `230x239` or `231x239`, all `srgba 8-bit`
- Processed frames: eight files, each `64x64 srgba 8-bit`
- Sheet PNG: `512x64 srgba 8-bit`
- Static fallback PNG: `64x64 srgba 8-bit`
- Static DDS: `64x64 srgba 8-bit`
- Sheet DDS: `512x64 srgba 8-bit`

### Alpha / Fringe Audit

```bash
python3 - <<'PY'
from PIL import Image
from pathlib import Path
pkg = Path('docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_formable_ready_emblem_animated')
paths = list(sorted((pkg/'processed_frames').glob('*.png'))) + [
    pkg/'africa_formable_ready_emblem_animated_sheet_512x64.png',
    pkg/'africa_formable_ready_emblem_static_64x64.png',
    Path('gfx/interface/animated/012_africa/formable_ready_prompt_static_64x64.dds'),
    Path('gfx/interface/animated/012_africa/formable_ready_prompt_sheet_512x64.dds'),
]
for path in paths:
    img = Image.open(path).convert('RGBA')
    w, h = img.size
    p = img.load()
    corners = [p[0,0], p[w-1,0], p[0,h-1], p[w-1,h-1]]
    fringe_white = fringe_green = fringe_magenta = 0
    alpha_vals = []
    for y in range(h):
        for x in range(w):
            r, g, b, a = p[x, y]
            alpha_vals.append(a)
            if a < 250:
                continue
            edge = False
            for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0 <= nx < w and 0 <= ny < h and p[nx, ny][3] < 8:
                    edge = True
                    break
            if not edge:
                continue
            if r >= 245 and g >= 245 and b >= 245:
                fringe_white += 1
            if g >= 220 and r <= 80 and b <= 80:
                fringe_green += 1
            if r >= 220 and b >= 220 and g <= 80:
                fringe_magenta += 1
    print(path.name, corners, min(alpha_vals), max(alpha_vals), fringe_white, fringe_green, fringe_magenta)
PY
```

Result summary:

- All processed PNG frames, the sheet PNG, the static PNG, and both DDS outputs have alpha range `0-255`
- All four corners are `(0, 0, 0, 0)` on every validated file
- Transparent-edge fringe counts:
  - white: `0`
  - green: `0`
  - magenta: `0`

## Notes

- Small interior white-hot highlight pixels exist only inside the peak flare and were not treated as matte contamination because transparent-edge white fringe remained `0`.
