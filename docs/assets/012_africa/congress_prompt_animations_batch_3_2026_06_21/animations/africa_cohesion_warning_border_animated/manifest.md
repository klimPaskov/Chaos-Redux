# Africa Cohesion Warning Border Animated Manifest

## Asset

- Asset id: `africa_cohesion_warning_border_animated`
- Event: `012_africa`
- Event slug: `africa`
- Asset type: animated scripted-GUI border
- Intended in-game use: warning / rebellion / cohesion crisis border around the Continental Congress warning docket card
- Related GUI element: `africa_continental_congress_warning_status_card`
- Source mode: `$imagegen`
- Source mode rationale: this is a fictional symbolic UI ornament, not a historical or archival image; generation is appropriate and required for the invented brass / dark-red Congress warning border language
- Source PNGs:
  - `source_frames/africa_cohesion_warning_border_generated_source_sheet.png`
  - `source_frames/africa_cohesion_warning_border_animated_000_source.png`
  - `source_frames/africa_cohesion_warning_border_animated_001_source.png`
  - `source_frames/africa_cohesion_warning_border_animated_002_source.png`
  - `source_frames/africa_cohesion_warning_border_animated_003_source.png`
  - `source_frames/africa_cohesion_warning_border_animated_004_source.png`
  - `source_frames/africa_cohesion_warning_border_animated_005_source.png`
  - `source_frames/africa_cohesion_warning_border_animated_006_source.png`
  - `source_frames/africa_cohesion_warning_border_animated_007_source.png`
- Processed PNGs:
  - `processed_frames/africa_cohesion_warning_border_animated_000.png`
  - `processed_frames/africa_cohesion_warning_border_animated_001.png`
  - `processed_frames/africa_cohesion_warning_border_animated_002.png`
  - `processed_frames/africa_cohesion_warning_border_animated_003.png`
  - `processed_frames/africa_cohesion_warning_border_animated_004.png`
  - `processed_frames/africa_cohesion_warning_border_animated_005.png`
  - `processed_frames/africa_cohesion_warning_border_animated_006.png`
  - `processed_frames/africa_cohesion_warning_border_animated_007.png`
- Package outputs:
  - `africa_cohesion_warning_border_animated_sheet_4160x58.png`
  - `africa_cohesion_warning_border_static_520x58.png`
  - `africa_cohesion_warning_border_animated_preview.gif`
  - `africa_cohesion_warning_border_animated_contact_sheet.png`
- Final DDS outputs:
  - `gfx/interface/animated/012_africa/cohesion_warning_border_sheet_4160x58.dds`
  - `gfx/interface/animated/012_africa/cohesion_warning_border_static_520x58.dds`
- Target size: `520x58`
- Sheet size: `4160x58`
- Sprite names:
  - static: `GFX_africa_cohesion_warning_border`
  - animated: `GFX_africa_cohesion_warning_border_animated`
- Suggested `.gfx` file: `interface/012_africa.gfx`
- Frame count: `8`
- Frame timing: `7 fps`
- Loop behavior: `looping = yes`
- Play on show: `yes`
- Anchor point: full-frame centered border
- Static fallback frame: `003`
- Asset status: `complete`

## Source Notes By Frame

- `000`: calm border, dim lamps, no active crack burst
- `001`: rising lamp intensity and bead warmth
- `002`: stronger warning pulse with first visible crack flicker
- `003`: peak readable alert state, chosen as static fallback
- `004`: peak aftermath with lingering hot rails
- `005`: receding pulse and reduced crack energy
- `006`: near-rest dimmed state
- `007`: rest-ready return frame for clean loop closure

## Processing Notes

- The generated master source was a single eight-frame horizontal source sheet from built-in `$imagegen`.
- Each frame was extracted to a dedicated source PNG before any local processing.
- Chroma removal used the official helper:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
  --input <source_frame> \
  --out <processed_tmp> \
  --auto-key border \
  --soft-matte \
  --transparent-threshold 12 \
  --opaque-threshold 220 \
  --despill
```

- After chroma removal, frames were trimmed, resized to `520x58`, and the center text-safe window was enforced as transparent to prevent pulse residue from sitting under live GUI text.
- The final sheet was assembled left-to-right as one row of eight frames.

## Validation

Commands used:

```bash
identify -format '%f %wx%h %[channels] %[depth]-bit\n' \
  processed_frames/*.png \
  africa_cohesion_warning_border_animated_sheet_4160x58.png \
  africa_cohesion_warning_border_static_520x58.png \
  gfx/interface/animated/012_africa/cohesion_warning_border_sheet_4160x58.dds \
  gfx/interface/animated/012_africa/cohesion_warning_border_static_520x58.dds

python3 - <<'PY'
from PIL import Image
files=[
  './docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_cohesion_warning_border_animated/africa_cohesion_warning_border_static_520x58.png',
  './docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_cohesion_warning_border_animated/africa_cohesion_warning_border_animated_sheet_4160x58.png',
  './gfx/interface/animated/012_africa/cohesion_warning_border_static_520x58.dds',
  './gfx/interface/animated/012_africa/cohesion_warning_border_sheet_4160x58.dds',
]
for path in files:
    img=Image.open(path).convert('RGBA')
    w,h=img.size
    data=list(img.getdata())
    alpha=[a for _,_,_,a in data]
    corners=[img.getpixel((0,0))[3],img.getpixel((w-1,0))[3],img.getpixel((0,h-1))[3],img.getpixel((w-1,h-1))[3]]
    green=sum(1 for r,g,b,a in data if a>0 and g>200 and r<80 and b<80)
    magenta=sum(1 for r,g,b,a in data if a>0 and r>200 and b>200 and g<80)
    if w == 520:
        center_alpha=max(img.crop((78,13,441,45)).getchannel('A').getdata())
        print(path, min(alpha), max(alpha), corners, green, magenta, center_alpha)
    else:
        center_alpha=max(img.crop((78,13,441,45)).getchannel('A').getdata())
        print(path, min(alpha), max(alpha), corners, green, magenta, center_alpha)
PY
```

Result summary:

- Processed frames:
  - `africa_cohesion_warning_border_animated_000.png 520x58 srgba 8-bit`
  - `africa_cohesion_warning_border_animated_001.png 520x58 srgba 8-bit`
  - `africa_cohesion_warning_border_animated_002.png 520x58 srgba 8-bit`
  - `africa_cohesion_warning_border_animated_003.png 520x58 srgba 8-bit`
  - `africa_cohesion_warning_border_animated_004.png 520x58 srgba 8-bit`
  - `africa_cohesion_warning_border_animated_005.png 520x58 srgba 8-bit`
  - `africa_cohesion_warning_border_animated_006.png 520x58 srgba 8-bit`
  - `africa_cohesion_warning_border_animated_007.png 520x58 srgba 8-bit`
- Sheet PNG: `4160x58 srgba 8-bit`
- Static PNG: `520x58 srgba 8-bit`
- Final DDS sheet: `4160x58 srgba 8-bit`
- Final DDS static: `520x58 srgba 8-bit`
- PNG alpha range: `0-255`
- DDS alpha range: `0-255`
- Transparent corners: all four corners alpha `0` for static PNG, sheet PNG, static DDS, and sheet DDS
- Transparent center validation:
  - static PNG center-window max alpha: `0`
  - sheet PNG first-frame center-window max alpha: `0`
  - static DDS center-window max alpha: `0`
  - sheet DDS first-frame center-window max alpha: `0`
- Opaque green matte pixels: `0` in final PNG and DDS outputs
- Opaque magenta matte pixels: `0` in final PNG and DDS outputs
- Bright white pixels exist only as brass highlight detail, not as corner or center matte; the transparent outer corners and transparent interior passed

## Notes

- The source generated as a square-ish banner row rather than a native `4160x58` strip, so deterministic local normalization resized the extracted frames into the requested gameplay dimensions.
- No `.gfx`, `.gui`, gameplay, localisation, or unrelated docs were edited.
