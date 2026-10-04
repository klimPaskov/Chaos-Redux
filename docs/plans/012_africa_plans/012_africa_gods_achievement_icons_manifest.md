# Event 012 Gods of Africa achievement icons

Local working files live under `docs/assets/012_africa/achievements/gods/` (ignored by Git); the runtime DDS files are committed.

Produced 2026-10-04 with the `chaos-redux-event-assets` achievement workflow: one native-transparency ImageGen subject per achievement, processed into a centered 64x64 colour layer (subject bounding box scaled to 50 px), a deterministic grayscale layer, and a not-eligible layer made from the grey layer plus the unchanged `template/overlay.png`, then composited by `tools/process_achievement_icons.py` onto the supplied templates.

| Achievement id | ImageGen source | Source triplet | Runtime DDS | Review PNGs |
| --- | --- | --- | --- | --- |
| `africa_gods_long_obedience` | `source/africa_gods_long_obedience_imagegen.png` | `processed/africa_gods_long_obedience/` | `gfx/achievements/africa_gods_long_obedience{,_grey,_not_eligible}.dds` | `review/` |
| `africa_gods_survive_defiance` | `source/africa_gods_survive_defiance_imagegen.png` | `processed/africa_gods_survive_defiance/` | `gfx/achievements/africa_gods_survive_defiance{,_grey,_not_eligible}.dds` | `review/` |
| `africa_gods_continental_provision` | `source/africa_gods_continental_provision_imagegen.png` | `processed/africa_gods_continental_provision/` | `gfx/achievements/africa_gods_continental_provision{,_grey,_not_eligible}.dds` | `review/` |
| `africa_gods_careful_gambler` | `source/africa_gods_careful_gambler_imagegen.png` | `processed/africa_gods_careful_gambler/` | `gfx/achievements/africa_gods_careful_gambler{,_grey,_not_eligible}.dds` | `review/` |

Subjects:

- Long Obedience: a bronze offering bowl of grain, a cartridge clip and a crate held in two open hands under an abstract geometric sunburst.
- Survive Defiance: a battered helmet and an unbroken iron shield splitting the rays of a looming golden sunburst.
- Continental Provision: varied tribute (rifle crate, fuel drum, gun wheel, rail, grain) heaped before a bronze African continent, with arrows from four directions.
- The Careful Gambler: a gloved hand holding cards over a sealed demand with a cracked sunburst wax seal, and a coin on edge.

Every prompt asked for a genuinely transparent background with no frame, square backdrop, wreath, text, letters, flags, or checkerboard; all four sources have native alpha (no background removal).
Achievements are a root-only family, so no `.gfx` registration is used; the ids in `common/achievements/chaos_redux_achievements.txt` name the files.
`preview_sheet.png` in `processed/` shows the four subjects on the completed template at 4x.
Status: wired; in-game appearance is a live check.
