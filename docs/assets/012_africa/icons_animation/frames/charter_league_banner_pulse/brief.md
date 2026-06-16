# Charter League Banner Pulse Brief

- Asset name: `charter_league_banner_pulse`
- In-game use: Charter League or Africa Is One pulse/banner loop
- Gameplay surface: proposed faction emblem, route banner, or scripted GUI ornament
- Target frame size: 160x96
- Frame count: 4
- Sheet size: 640x96
- Static fallback sprite: `GFX_africa_charter_league_banner_static`
- Animated sprite: `GFX_africa_charter_league_banner_anim`
- FPS recommendation: 8
- Looping: yes
- `play_on_show`: yes
- Anchor: center
- Source mode: generated per frame with transparent background
- Subject type: fictional symbolic banner emblem
- Reference folders inspected: focuses, ideas, decisions
- Final preview paths:
  - `previews/charter_league_banner_pulse_sheet.png`
  - `previews/charter_league_banner_pulse_preview.gif`
  - `previews/charter_league_banner_pulse_contact_sheet.png`
- Intended `.gfx`: `interface/012_africa_animated_icons.gfx`

## Frame plan

| Frame | Motion state | Visual change | Loop note |
| --- | --- | --- | --- |
| 000 | rest | calm banner with low metallic light | matches 003 closely |
| 001 | rising | brighter wreath and slight cloth lift | easing in |
| 002 | peak | strongest gold pulse and wider cloth flare | peak state |
| 003 | falling | banner settles and glow declines | returns to 000 |
