# cannibalism_selected_target_overlay Animation Brief

- In-game use: current country/state evidence selection overlay
- Gameplay surface: cannibalism_network_window
- Target frame size: 374x64
- Frame count: 6
- Horizontal sheet size: 2244x64
- Static fallback sprite: `GFX_cannibalism_selected_target_overlay_static`
- Animated sprite: `GFX_cannibalism_selected_target_overlay_animated`
- Animation rate: 6 FPS
- Looping: yes
- Play on show: yes
- Anchor: center
- Source mode: six separate built-in image_gen outputs/edits on removable chroma-key
- Subject classification: fictional transparent state-selection UI frame
- Source-art change: same blood-wet forensic steel brackets with an open transparent center; each frame redraws clamp jaws, lamps, blood runnels and torn evidence corners
- Final static PNG/DDS stem: `gfx/interface/animated/014_cannibalism/cannibalism_selected_target_overlay_static`
- Final sheet PNG/DDS stem: `gfx/interface/animated/014_cannibalism/cannibalism_selected_target_overlay_sheet`
- Review GIF: `docs/assets/014_cannibalism/gui_animation_portraits/animations/cannibalism_selected_target_overlay/previews/cannibalism_selected_target_overlay_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/gui_animation_portraits/animations/cannibalism_selected_target_overlay/previews/cannibalism_selected_target_overlay_contact.png`
- Target GFX file: `interface/014_cannibalism.gfx`
- Target GUI file: `interface/014_cannibalism_frontline_hunger.gui`
- Wiring precedent: vanilla `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, and `interface/leadergroups.gfx`; one-row horizontal `frameAnimatedSpriteType`.

Local processing may only crop, resize, align, remove the flat chroma key, assemble the sheet, create review outputs, and convert DDS. It does not create motion.

