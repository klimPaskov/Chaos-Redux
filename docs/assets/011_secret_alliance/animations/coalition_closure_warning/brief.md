# Coalition Closure Warning Animation Brief

- Asset: `coalition_closure_warning`
- Event: `011_secret_alliance`
- In-game use: state-driven warning inside the compact counter-network panel when Evolution III is active and the offensive countdown is running
- Gameplay surface: event-owned decision-category scripted GUI
- Subject: a broken wax-and-metal seal surrounded by three jointed metal arms and taut dark cords that close inward, hold, then ease back slightly without reopening
- Subject type: fictional symbolic UI art
- Source mode: eight separate `$imagegen` source frames, one generated output per planned visual state
- Frame size: `128x96`
- Frame count: `8`
- Horizontal sheet size: `1024x96`
- Static fallback: fully closed, readable warning state derived from approved frame 004
- Static sprite: `GFX_011_secret_alliance_coalition_closure_warning`
- Animated sprite: `GFX_011_secret_alliance_coalition_closure_warning_animated`
- Playback: `8` FPS, looping, `play_on_show = yes`, no pause on loop
- Anchor: center; the cracked seal center and arm pivots remain fixed across frames
- Loop: frames close from a guarded rest to full closure, then ease back to a near-rest state that connects visually to frame 000
- Palette: oxidized gunmetal, aged brass, dark burgundy wax, soot-black cords, restrained amber edge light
- Avoid: transform-only motion, opacity pulses, one-image filters, flashing red fields, generated text, national flags, extremist symbols, maps, modern surveillance imagery
- Static DDS: `gfx/interface/011_secret_alliance/coalition_closure_warning_static.dds`
- Animated DDS: `gfx/interface/011_secret_alliance/coalition_closure_warning_sheet.dds`
- Working sheet PNG: `docs/assets/011_secret_alliance/animations/coalition_closure_warning/sheets/coalition_closure_warning_sheet.png`
- GIF preview: `docs/assets/011_secret_alliance/animations/coalition_closure_warning/previews/coalition_closure_warning_preview.gif`
- Contact sheet: `docs/assets/011_secret_alliance/animations/coalition_closure_warning/previews/coalition_closure_warning_contact.png`
- Target GFX: `interface/011_secret_alliance.gfx`
- Target GUI: `interface/011_secret_alliance.gui`
- Wiring precedents: offline `Graphical asset modding`, `Interface modding`, and `Scripted GUI modding` wiki pages; vanilla `interface/alerts.gfx`; Chaos Redux `interface/013_natural_disasters.gfx` and `interface/013_natural_disasters.gui`

The GIF is review-only. The HOI4 runtime asset is the horizontal BGRA DDS sheet.
