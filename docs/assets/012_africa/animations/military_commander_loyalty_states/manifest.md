# military_commander_loyalty_states

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_decision_012_africa_commander_loyalty`.
- Static fallback sprite: `GFX_decision_012_africa_commander_loyalty_static`.
- Static fallback PNG: `military_commander_loyalty_states_static.png` (acceptance source); runtime static DDS: `gfx/interface/decisions/012_africa/decision_012_africa_commander_loyalty.dds`.
- Horizontal sheet PNG: `sheets/military_commander_loyalty_states_sheet.png`; runtime sheet DDS: `gfx/interface/decisions/012_africa/military_commander_loyalty_states_sheet.dds`.
- Review GIF: `previews/military_commander_loyalty_states_preview.gif` (review only); row contact sheet: `previews/military_commander_loyalty_states_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: commander review.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `10d79347377a61ecc858dd51b6bcd20593b83762be99d0c4e3de39cb320d34ba`; processed set `373204d9d0719908bbaeae6c212c87667ac73491fb877274406e3f724ce14098`; sheet PNG `7065d26ca47a04af8655f65199a2deb300f612d21f7bcb8458dc793411b749d7`; static PNG `c9d393e4541c7fe2fe058afd5be1dcfca0f53d53077e99701604181a531ddd09`; sheet DDS `1dadf0d9e14a561994b658cc35118f493cd60c4f2d315049408717d3b66fa7fe`; static DDS `61886eec62b6562a3d7d1198b5854fb8481d3f74b0405607ebedfbc58081af08`; review GIF `d7226bf247bf61acb588bae58234c0bfdf09b994aad3cea3d23090389f4fc138`; contact `e3bde56adfd4f5d6c3e41c8d93ce69a5256c7f43892ae4cf051a0db7e724f83d`.
