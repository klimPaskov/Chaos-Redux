# cannibalism_island_alert Animation Brief

- In-game use: silent-island node alert in the network window
- Gameplay surface: cannibalism_network_window
- Target frame size: 64x64
- Frame count: 8
- Horizontal sheet size: 512x64
- Static fallback sprite: `GFX_cannibalism_island_alert_static`
- Animated sprite: `GFX_cannibalism_island_alert_animated`
- Animation rate: 8 FPS
- Looping: yes
- Play on show: yes
- Anchor: center
- Source mode: retained exact semantic source frames from animations_imagegen/cannibalism_island_signal_card; no reuse elsewhere
- Subject classification: fictional symbolic island alert
- Source-art change: torn island chart and compass with separately drawn cold beacon sweep, sea marks and paper damage
- Final static PNG/DDS stem: `gfx/interface/animated/014_cannibalism/cannibalism_island_alert_static`
- Final sheet PNG/DDS stem: `gfx/interface/animated/014_cannibalism/cannibalism_island_alert_sheet`
- Review GIF: `docs/assets/014_cannibalism/gui_animation_portraits/animations/cannibalism_island_alert/previews/cannibalism_island_alert_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/gui_animation_portraits/animations/cannibalism_island_alert/previews/cannibalism_island_alert_contact.png`
- Target GFX file: `interface/014_cannibalism.gfx`
- Target GUI file: `interface/014_cannibalism_frontline_hunger.gui`
- Wiring precedent: vanilla `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, and `interface/leadergroups.gfx`; one-row horizontal `frameAnimatedSpriteType`.

Local processing may only crop, resize, align, remove the flat chroma key, assemble the sheet, create review outputs, and convert DDS. It does not create motion.

