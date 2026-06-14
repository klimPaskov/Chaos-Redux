# Event 005 Soviet Collapse GFX Handoff

The Soviet Collapse evolution details portrait animation is registered in `interface/005_soviet_collapse_custom_icons.gfx`.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_soviet_collapse_evolution_portraits` |
| Animated sprite alias | `GFX_soviet_collapse_evolution_portraits_animated` |
| Static fallback DDS | `gfx/interface/leader_frames/soviet_collapse/soviet_collapse_evolution_portraits_static.dds` |
| Animated sheet DDS | `gfx/interface/leader_frames/soviet_collapse/soviet_collapse_evolution_portraits_sheet.dds` |
| Sheet PNG | `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/sheets/soviet_collapse_evolution_portraits_sheet.png` |
| Frame size | `156x210` |
| Frame count | `66` |
| Sheet size | `10296x210` |
| FPS | `4` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/005_soviet_collapse_custom_icons.gfx` |
| Target GUI | `interface/chaosx_events_log_popup.gui` |
| State gate | `has_events_log_selected_soviet_collapse_evolution` |
| Scripted localisation | `GetEventsLogSelectedEvolutionPortrait` returns `GFX_soviet_collapse_evolution_portraits_animated` |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/countryintelligenceagencyview.gfx`, `interface/007_fury.gfx`, `interface/003_holy_realm.gfx` |

Review assets:

- Source frames: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/source_frames/`
- Processed frames: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/processed_frames/`
- Preview GIF: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/previews/soviet_collapse_evolution_portraits_preview.gif`
- Contact sheet: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/previews/soviet_collapse_evolution_portraits_contact.png`

The event-log details surface already exposes `events_log_evolution_details_portrait` as a dynamic image property. No new GUI container is needed for this animation.
