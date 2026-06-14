# Soviet Collapse Evolution Portrait Animation Brief

## Purpose

Create a single animated portrait for Soviet Collapse evolution details. The animation iterates through the existing Soviet Collapse portrait set and gives both secession and high-chaos successor evolution detail popups the portrait-style details layout.

## Visual Direction

- Existing Chaos Redux Soviet Collapse leader, council, factory, and high-chaos successor portraits.
- The loop is deliberately stepped: each frame is a different Soviet Collapse portrait rather than a transformed version of one portrait.
- The subject changes by source frame, not by local movement, glow, recolor, zoom, crop, or filter effects.
- Keep every frame at standard HOI4 portrait size, `156x210`.

## Technical Targets

- Source frames: 66 existing Soviet Collapse portrait DDS files converted to review PNGs.
- Processed frames: `156x210` PNGs.
- Final frame sheet: `10296x210` DDS, 66 horizontal frames.
- Static fallback: `gfx/interface/leader_frames/soviet_collapse/soviet_collapse_evolution_portraits_static.dds`.
- Animated sheet: `gfx/interface/leader_frames/soviet_collapse/soviet_collapse_evolution_portraits_sheet.dds`.
- Static sprite: `GFX_soviet_collapse_evolution_portraits`.
- Animated sprite: `GFX_soviet_collapse_evolution_portraits_animated`.
- Playback: 4 FPS, looping, `play_on_show = yes`.
- Anchor: center.

## Required Outputs

- Source frames: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/source_frames/`
- Processed frames: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/processed_frames/`
- Sheet PNG: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/sheets/soviet_collapse_evolution_portraits_sheet.png`
- Static PNG: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/sheets/soviet_collapse_evolution_portraits_static.png`
- Preview GIF: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/previews/soviet_collapse_evolution_portraits_preview.gif`
- Contact sheet: `docs/assets/005_soviet_collapse/animations/soviet_collapse_evolution_portraits/previews/soviet_collapse_evolution_portraits_contact.png`
- Final DDS files: `gfx/interface/leader_frames/soviet_collapse/`

## References

- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/countryintelligenceagencyview.gfx`
- `interface/007_fury.gfx`
- `interface/003_holy_realm.gfx`
- `gfx/leaders/005_soviet_collapse/`
