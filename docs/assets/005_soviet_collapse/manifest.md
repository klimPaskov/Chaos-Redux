# Event 005 Soviet Collapse Asset Manifest

Package scope: Soviet Collapse event-log evolution details portrait animation.

Reference inspection completed:
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/fakegfx.txt`
- `~/projects/Hearts of Iron IV/interface/countryintelligenceagencyview.gfx`
- `interface/007_fury.gfx`
- `interface/003_holy_realm.gfx`
- Existing Soviet Collapse portrait DDS files in `gfx/leaders/005_soviet_collapse/`

DDS conversion note:
- Local processing converted the existing Soviet Collapse `156x210` DDS portraits into source and processed PNG frame copies.
- The final horizontal sheet was exported with `convert -define dds:compression=none`.
- Final DDS dimensions were validated after export: `10296x210` for the animated sheet and `156x210` for the static fallback.

## Assets

### `soviet_collapse_evolution_portraits`

| Field | Value |
| --- | --- |
| Related event id | `5` |
| Related event slug | `soviet_collapse` |
| Asset type | animated event-log evolution details portrait |
| Intended in-game use | Portrait-style evolution details window for Soviet Collapse secession and high-chaos successor evolutions |
| Source mode | existing Chaos Redux portrait DDS source frames |
| Source frames | `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/source_frames/` |
| Processed frames | `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/processed_frames/` |
| Sheet PNG | `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/sheets/soviet_collapse_evolution_portraits_sheet.png` |
| Preview GIF | `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/previews/soviet_collapse_evolution_portraits_preview.gif` |
| Contact sheet | `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/previews/soviet_collapse_evolution_portraits_contact.png` |
| Final sheet DDS | `gfx/interface/leader_frames/soviet_collapse/soviet_collapse_evolution_portraits_sheet.dds` |
| Static fallback DDS | `gfx/interface/leader_frames/soviet_collapse/soviet_collapse_evolution_portraits_static.dds` |
| Target size | `156x210` per frame |
| Frame count | `66` |
| Sheet size | `10296x210` |
| Animation rate | `1` FPS |
| Loop behavior | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Anchor point | center |
| Static sprite | `GFX_soviet_collapse_evolution_portraits` |
| Animated sprite | `GFX_soviet_collapse_evolution_portraits_animated` |
| `.gfx` file | `interface/005_soviet_collapse_custom_icons.gfx` |
| GUI surface | `interface/chaosx_events_log_popup.gui` through `events_log_evolution_details_portrait` |
| Scripted selector | `GetEventsLogSelectedEvolutionPortrait` |
| Trigger gate | `has_events_log_selected_soviet_collapse_evolution` |
| Asset status | `complete` |

Frame source notes: every frame is one existing Soviet Collapse leader portrait, copied mechanically into source and processed PNG form at the same `156x210` size before sheet assembly. No transform-only motion, recolor-only motion, generated interpolation, crop drift, or preview GIF source was used.
