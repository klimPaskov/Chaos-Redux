# cannibalism_critical_larder_glow Animation Brief

- In-game use: critical or overflowing Larder warning in warlord command
- Gameplay surface: cannibalism_warlord_command_window
- Target frame size: 64x64
- Frame count: 8
- Horizontal sheet size: 512x64
- Static fallback sprite: `GFX_cannibalism_critical_larder_glow_static`
- Animated sprite: `GFX_cannibalism_critical_larder_glow_animated`
- Animation rate: 8 FPS
- Looping: yes
- Play on show: yes
- Anchor: center
- Source mode: eight separate built-in image_gen outputs/edits on removable chroma-key
- Subject classification: fictional transparent larder warning emblem
- Source-art change: dented empty mess tin, butcher hook, red field lamp and fictional gore; each source redraws flame/lamp hardware, hook angle within the drawing, blood and tin damage
- Final static PNG/DDS stem: `gfx/interface/animated/014_cannibalism/cannibalism_critical_larder_glow_static`
- Final sheet PNG/DDS stem: `gfx/interface/animated/014_cannibalism/cannibalism_critical_larder_glow_sheet`
- Review GIF: `docs/assets/014_cannibalism/gui_animation_portraits/animations/cannibalism_critical_larder_glow/previews/cannibalism_critical_larder_glow_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/gui_animation_portraits/animations/cannibalism_critical_larder_glow/previews/cannibalism_critical_larder_glow_contact.png`
- Target GFX file: `interface/014_cannibalism.gfx`
- Target GUI file: `interface/014_cannibalism_frontline_hunger.gui`
- Wiring precedent: vanilla `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, and `interface/leadergroups.gfx`; one-row horizontal `frameAnimatedSpriteType`.

Local processing may only crop, resize, align, remove the flat chroma key, assemble the sheet, create review outputs, and convert DDS. It does not create motion.

