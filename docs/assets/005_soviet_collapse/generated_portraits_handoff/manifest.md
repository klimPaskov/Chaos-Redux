# Event 005 Soviet Collapse Generated Portrait Manifest

Scope: bounded generated-art handoff for `BEC`, `BLT`, `COU`, `ILU`, and `IRA` leader/council portraits only.

This package did not edit gameplay, focus, event, localisation, `.gfx`, spreadsheet, country, flag, or active leader files. The current worktree had the target tracked DDS files deleted before this pass, so final DDS outputs were kept under this handoff folder instead of restoring or overwriting dirty `gfx/leaders/005_soviet_collapse/` paths.

## References Inspected

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- Required core Paradox wiki pages listed in `AGENTS.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/`
- Existing Chaos Redux leader portraits in `gfx/leaders/005_soviet_collapse/`
- Vanilla leader portrait folders under `/home/klim/projects/Hearts of Iron IV/gfx/leaders/`

There is no leader-specific reference folder under `.agents/skills/chaos-redux-event-assets/assets/`, so existing Event 005 and vanilla leader portraits were used as the style reference.

## Processing Notes

- Source mode: `$imagegen`, because the targets are fictional/symbolic council or alternate-history authority portraits and repo evidence did not identify them as real persons.
- Source files were copied from the built-in image generation output directory into `source_png/`.
- Processed previews were cropped/resized to 156x210 with centered HOI4-like portrait framing.
- DDS files were produced as 156x210 uncompressed 32-bit DDS files in `final_dds/`.
- The repo converter attempted to use `/mnt/c/Tools/texconv/texconv.exe`, but that executable is not runnable from this Linux session. Its ffmpeg fallback also errored before writing a file. Final DDS files were therefore created with ImageMagick uncompressed 32-bit output and validated at 156x210.
- Target final paths are documented below but were not written, because those tracked files are currently deleted in the dirty worktree.

## Assets

| Tag | Asset type | Source PNG | Processed PNG | Handoff DDS | Target final DDS path | Proposed sprite name | Suggested `.gfx` file | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BEC` | fictional council leader portrait | `source_png/BEC_leader_source.png` | `processed_png/BEC_leader.png` | `final_dds/BEC_leader.dds` | `gfx/leaders/005_soviet_collapse/BEC_leader.dds` | `GFX_portrait_BEC_emergency_council` | `interface/005_soviet_collapse_custom_icons.gfx` | handed_off |
| `BLT` | fictional council leader portrait | `source_png/BLT_leader_source.png` | `processed_png/BLT_leader.png` | `final_dds/BLT_leader.dds` | `gfx/leaders/005_soviet_collapse/BLT_leader.dds` | `GFX_portrait_BLT_emergency_council` | `interface/005_soviet_collapse_custom_icons.gfx` | handed_off |
| `COU` | fictional council leader portrait | `source_png/COU_leader_source.png` | `processed_png/COU_leader.png` | `final_dds/COU_leader.dds` | `gfx/leaders/005_soviet_collapse/COU_leader.dds` | `GFX_portrait_COU_mountain_republican_council` | `interface/005_soviet_collapse_custom_icons.gfx` | handed_off |
| `ILU` | fictional council leader portrait | `source_png/ILU_leader_source.png` | `processed_png/ILU_leader.png` | `final_dds/ILU_leader.dds` | `gfx/leaders/005_soviet_collapse/ILU_leader.dds` | `GFX_portrait_ILU_desert_route_authority` | `interface/005_soviet_collapse_custom_icons.gfx` | handed_off |
| `IRA` | fictional council leader portrait | `source_png/IRA_leader_source.png` | `processed_png/IRA_leader.png` | `final_dds/IRA_leader.dds` | `gfx/leaders/005_soviet_collapse/IRA_leader.dds` | `GFX_portrait_IRA_far_eastern_provisional_council` | `interface/005_soviet_collapse_custom_icons.gfx` | handed_off |

## Contact Sheets

- `contact_sheets/reference_portrait_style_sheet.png`
- `contact_sheets/generated_portraits_contact_sheet.png`

## Blockers and Uncertainty

- I did not copy DDS files into `gfx/leaders/005_soviet_collapse/` because the corresponding tracked files are currently deleted in the dirty worktree and the task asked not to overwrite existing user/main-agent changes.
- I did not edit `.gfx` files. Proposed sprite names and suggested `.gfx` destination are handoff notes only.
- Prior sidecars describe these tags as possibly inactive/stale. This handoff treats them as requested candidate missing portraits and provides final-source assets without deciding active gameplay use.
