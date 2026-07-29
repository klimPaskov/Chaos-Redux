# Charter seal activation animation brief

In-game use: decorative Charter League activation seal in the Event 012 decision-category window.

Target frame size: 64x64. Frame count: 8. Sheet: 512x64 horizontal. Static fallback: `charter_seal_activation_static.dds`. Animated sprite: `GFX_012_africa_charter_seal_activation_animated`. Rate: 8 fps. Loop: yes, `play_on_show = yes`, with the existing `.gfx` `pause_on_loop = 0.4`. Anchor: centered, transparent corners.

Source mode: one independent built-in ImageGen source frame per state on a flat chroma-key backdrop, followed by mechanical key removal and normalization. Subject: fictional/symbolic UI seal. Reference review: canonical `icons/decision_categories/contact_sheet.png` and `icons/balance_of_power/contact_sheet.png`.

Final paths: `sheets/charter_seal_activation_sheet.png`, `previews/charter_seal_activation_preview.gif`, `charter_seal_activation_static.png`, and runtime `gfx/interface/012_africa/animations/charter_seal_activation_{sheet,static}.dds`.
