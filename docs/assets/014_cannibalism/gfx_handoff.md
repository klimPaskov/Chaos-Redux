# Event 014 GFX Handoff

Date: 2026-07-15

The game-facing registrations are distributed across the following files:

| Registration file | Event 014 responsibility |
| --- | --- |
| `interface/014_cannibalism.gfx` | Core ideas, decisions, categories, portraits, GUI art, ordinary and Wendigo portrait fallbacks/sheets |
| `interface/014_cannibalism_achievement_tracker.gfx` | Achievement tracker presentation |
| `interface/014_cannibalism_achievements.gfx` | Eighteen achievement icon triplets |
| `interface/014_cannibalism_aftermath_pictures.gfx` | Eligible global-defeat aftermath pictures |
| `interface/014_cannibalism_focus_closure.gfx` | Unified and Wendigo focus icon closure |
| `interface/014_cannibalism_objectives.gfx` | Timed logistics, unit, convergence, terminal, and containment objective art |
| `interface/014_cannibalism_warlord_focus_assets.gfx` | Sixty-eight warlord focus icons |
| `interface/chaosx_pictures.gfx` | Event 014 report/news picture registrations |
| `interface/chaosx_super_events.gfx` | Reveal, ordinary world end, Wendigo world end, and global-defeat super-events |

## Animated portraits

| Sprite | Runtime sheet | Frames | Static fallback |
| --- | --- | ---: | --- |
| `GFX_cannibalism_revealed_portrait_animated` | `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds` | 12 | `GFX_cannibalism_revealed_portrait_static` |
| `GFX_cannibalism_wendigo_portrait_animated` | `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds` | 16 | `GFX_cannibalism_wendigo_portrait_static` |

Both sheets are frame-authored imagegen sequences rather than transforms of one still. Source frames, previews, static fallbacks, manifests, and validation are under `leader_portraits_refresh/`.

## Registration closure

- 812 Event 014 texture references
- 598 unique texture paths
- 0 missing runtime paths
- 204 focus DDS files
- 135 decision/category DDS files
- 62 registered idea/modifier DDS files
- 29 report/news DDS files
- 54 achievement DDS files
- 4 super-event DDS files

Event 014 adds no custom subunit or equipment identifiers. Existing battalion and equipment surfaces remain in use, so this handoff has no bespoke unit-counter or equipment-art registration. That is a verified scope disposition, not a fallback.

Country flags are resolved by HOI4 tag and cosmetic-tag naming rather than a GFX sprite registration. Their exact 65-design/195-file handoff is under `flags_refresh/manifest.md`.
