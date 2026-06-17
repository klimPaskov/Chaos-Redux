# Event 012 Africa GOAL Icon Transparency Handoff

- Scope: focus/goal icons only
- `.gfx` file to keep using: `interface/012_africa.gfx`
- `.gfx` edits made: none
- Idea icons touched: none
- Goal/focus files, localisation, GUI, scripts, spreadsheets touched: none

## Final DDS Targets

- `gfx/interface/goals/012_africa/goal_africa_political_congress.dds` -> `GFX_goal_africa_political_congress`
- `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds` -> `GFX_goal_africa_charter_league_emblem`
- `gfx/interface/goals/012_africa/goal_africa_charter_league_diplomacy.dds` -> `GFX_goal_africa_charter_league_diplomacy`
- `gfx/interface/goals/012_africa/goal_africa_industry_logistics.dds` -> `GFX_goal_africa_industry_logistics`
- `gfx/interface/goals/012_africa/goal_africa_military_forces.dds` -> `GFX_goal_africa_military_forces`
- `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds` -> `GFX_goal_africa_regional_integration`
- `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds` -> `GFX_goal_africa_authority_atlas`
- `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds` -> `GFX_goal_africa_archive_old_seats`
- `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds` -> `GFX_goal_africa_liberation_war_office`
- `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` -> `GFX_goal_africa_high_chaos_bestiary`
- `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds` -> `GFX_goal_africa_scramble_for_africa`
- `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds` -> `GFX_goal_africa_sponsor_paths`
- `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds` -> `GFX_goal_africa_world_order_route`

## Files Changed

- Replaced 13 final DDS files under `gfx/interface/goals/012_africa/`
- Added package folder `docs/assets/012_africa/icon_regen_all_goals_2026_06_17/`
- Added copied source PNGs for each goal icon under `source_png/`
- Added normalized processed PNGs for each goal icon under `processed_png/`
- Added transparency proof sheets under `contact_sheets/`
- Added `manifest.md`
- Added `gfx_handoff.md`

## Validation Run

Exact checks run after export:

```bash
python3 - <<'PY'
from PIL import Image
from pathlib import Path
root = Path('/home/klim/projects/chaos_redux/gfx/interface/goals/012_africa')
for p in sorted(root.glob('goal_africa_*.dds')):
    img = Image.open(p).convert('RGBA')
    w,h = img.size
    corners = [img.getpixel((0,0)), img.getpixel((w-1,0)), img.getpixel((0,h-1)), img.getpixel((w-1,h-1))]
    border_nonzero = 0
    for x in range(w):
        if img.getpixel((x,0))[3] != 0: border_nonzero += 1
        if img.getpixel((x,h-1))[3] != 0: border_nonzero += 1
    for y in range(1,h-1):
        if img.getpixel((0,y))[3] != 0: border_nonzero += 1
        if img.getpixel((w-1,y))[3] != 0: border_nonzero += 1
    print(p.name, w, h, border_nonzero, corners)
PY

identify -format '%f %G %[channels]\n' gfx/interface/goals/012_africa/*.dds
```

Validation result:

- All 13 DDS files report `94x86`
- All 13 DDS files report `srgba`
- All 13 DDS files have transparent corners
- All 13 DDS files have `border_nonzero_alpha=0`
- Transparency proof sheets:
  - `docs/assets/012_africa/icon_regen_all_goals_2026_06_17/contact_sheets/all_goals_on_checker.png`
  - `docs/assets/012_africa/icon_regen_all_goals_2026_06_17/contact_sheets/all_goals_on_dark.png`

## Blocked Assets

- None

## Residual Concerns

- None at the transparency/wiring level
- Source lineage intentionally reuses prior generated icon artwork where the subject already matched the requested goal family; this package rebuilds the processed PNG and final DDS outputs into one audited transparent set
