# member_departure_warning

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 72x72 per frame; 10 frames; horizontal sheet; 8 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_member_departure_warning_animated`.
- Static fallback sprite: `GFX_012_africa_member_departure_warning_animated_static`.
- Static fallback PNG: `member_departure_warning_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/member_departure_warning_static.dds`.
- Horizontal sheet PNG: `sheets/member_departure_warning_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/member_departure_warning_sheet.dds`.
- Review GIF: `previews/member_departure_warning_preview.gif` (review only); row contact sheet: `previews/member_departure_warning_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (10 separately authored PNGs); processed frames: `processed_frames/` (10 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 10`; `animation_rate_fps = 8`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: leaving timer.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `3270ca781315ebb99a9776b79df3bf44917d17666e4e732ce6d1ed78dedc9793`; processed set `abbc0c379a6a78f8fc112b6262d590c1ede474ca218dc603d6506432f3983fcd`; sheet PNG `bddf87e4fe08c25b13686166684a61ffbd076f51afbd115f3e184402190caa3b`; static PNG `6c66be2fb3540712cfdab2df7cd77b9f10c0519578e8b134a9f22f33c09da4a4`; sheet DDS `88a6bd352e5e81de14df6356770cfc47511d1a3f34bc22c8d39bcd301d38a007`; static DDS `3e665c0a32ab3aa6803efb6d0478e2efa5438d4c4499c8de476ddb32fe539bd0`; review GIF `a0869ac946adbdafee454e3aac34d98972c0b3dc2ccebce8252e7ac3c9a7200c`; contact `de001baceea690276fdcbc3ff68b44b6a396e8f1ae0a7c63da8b56a9e59db398`.
