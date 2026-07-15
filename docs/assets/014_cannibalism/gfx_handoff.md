# Event 014 GFX Handoff

Date: 2026-07-15

The game-facing registrations use exactly one dedicated Event 014 registry plus two required shared registries:

| Registration file | Event 014 responsibility |
| --- | --- |
| `interface/014_cannibalism.gfx` | Consolidated Event 014 registry: ideas, decisions, categories, portraits, GUI art, all three focus trees, achievement tracker, 18 achievement triplets, aftermath pictures, objective art, and every static fallback or animation sheet |
| `interface/chaosx_pictures.gfx` | Event 014 report/news picture registrations |
| `interface/chaosx_super_events.gfx` | Reveal, ordinary world end, Wendigo world end, and global-defeat super-events |

## Animated portraits

| Sprite | Runtime sheet | Frames | Static fallback |
| --- | --- | ---: | --- |
| `GFX_cannibalism_revealed_portrait_animated` | `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds` | 12 at 12 FPS with `gfx/FX/buttonstate_blendframes.lua` | `GFX_cannibalism_revealed_portrait_static`, directly bound to `gfx/leaders/014_cannibalism/hannibal.dds` |
| `GFX_cannibalism_wendigo_portrait_animated` | `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds` | 16 at 12 FPS with `gfx/FX/buttonstate_blendframes.lua` | `GFX_cannibalism_wendigo_portrait_static`, directly bound to `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` |

Both sheets use the supplied portrait as exact frame `000`, followed by separately image-generated action states rather than transforms of one still. Source frames, previews, static fallbacks, manifests, and validation are under `leader_portraits_refresh/`.

Together with the twelve non-portrait GUI packages, Event 014 has exactly 14 semantic animation packages and 142 genuine source plus 142 processed frames.

## Registration closure

- 812 Event 014 texture references
- 598 unique texture paths
- 598 unique texture hashes
- 0 missing runtime paths
- 204 focus DDS files
- 135 decision/category DDS files
- 62 registered idea/modifier DDS files
- 29 report/news DDS files
- 54 achievement DDS files
- 4 super-event DDS files

Event 014 adds no custom subunit or equipment identifiers. Existing battalion and equipment surfaces remain in use, so this handoff has no bespoke unit-counter or equipment-art registration. That is a verified scope disposition, not a fallback.

Country flags are resolved by HOI4 tag and cosmetic-tag naming rather than a GFX sprite registration. Their exact 65-design/195-file handoff is under `flags_refresh/manifest.md`.
