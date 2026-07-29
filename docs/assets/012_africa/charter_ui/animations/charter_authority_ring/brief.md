# Charter authority ring animation brief

In-game use: decorative authority ring beside the Charter League header values in the Event 012 decision-category window.

Target frame size: 64x64. Frame count: 10. Sheet: 640x64 horizontal. Static fallback: `charter_authority_ring_static.dds`. Animated sprite: `GFX_012_africa_charter_authority_ring_animated`. Rate: 6 fps. Loop: yes, `play_on_show = yes`, with the existing `.gfx` `pause_on_loop = 0.4`. Anchor: centered, transparent corners.

Source mode: one independent built-in ImageGen source frame per state on a flat chroma-key backdrop, followed by mechanical key removal and normalization. Subject: fictional/symbolic UI authority seal. Reference review: canonical `icons/decision_categories/contact_sheet.png` and `icons/balance_of_power/contact_sheet.png`.

Final paths: `sheets/charter_authority_ring_sheet.png`, `previews/charter_authority_ring_preview.gif`, `charter_authority_ring_static.png`, and runtime `gfx/interface/012_africa/animations/charter_authority_ring_{sheet,static}.dds`.
