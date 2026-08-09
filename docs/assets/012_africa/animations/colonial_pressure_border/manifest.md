# colonial_pressure_border

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 96x96 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_colonial_pressure_border_animated`.
- Static fallback sprite: `GFX_012_africa_colonial_pressure_border_animated_static`.
- Static fallback PNG: `colonial_pressure_border_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/colonial_pressure_border_static.dds`.
- Horizontal sheet PNG: `sheets/colonial_pressure_border_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/colonial_pressure_border_sheet.dds`.
- Review GIF: `previews/colonial_pressure_border_preview.gif` (review only); row contact sheet: `previews/colonial_pressure_border_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: pressure critical.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `dea0a7a6223fe1549b136877b2ba2ca09142a814fdf66be7bfae51a3af63c17c`; processed set `63ca109b1fadd3874720806cbcb8fc9737014390a9e0ff0c4cc32d73a60624fa`; sheet PNG `e6eaa9d8f4600d789c00d7e251709053b2a8e340e9192d353c2c8df9835fe734`; static PNG `921bd9e1942cb6872bd753b57aec36e2d08615da49df0dd2596bb1fda06afbf6`; sheet DDS `46bebf566c82f2f2862c9332cf014d06a44805c53803ce5bc91267e6b1705af3`; static DDS `2f84abf8b41de881e94957c6eca9a2a0a3df8d95bd2ed8373d7cb1814761a538`; review GIF `87113ed2df19b8b6b77952d50f7061929c23248e4cf30a862bc12d937c8d2bec`; contact `45350762e875ace82ee4a511d3b482ef01edb809271380481e0cc663539c5366`.
