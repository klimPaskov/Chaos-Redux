# rival_bloc_alert

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 72x72 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_rival_bloc_alert_animated`.
- Static fallback sprite: `GFX_012_africa_rival_bloc_alert_animated_static`.
- Static fallback PNG: `rival_bloc_alert_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/rival_bloc_alert_static.dds`.
- Horizontal sheet PNG: `sheets/rival_bloc_alert_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/rival_bloc_alert_sheet.dds`.
- Review GIF: `previews/rival_bloc_alert_preview.gif` (review only); row contact sheet: `previews/rival_bloc_alert_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: rival bloc.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `9308cf683e6c6326e6b7ccdeb767da6293ac961b1a139ceb0dac370a3c44059f`; processed set `9692a3343a92101a14c0bc2d6f0828a04db43cafe57d5d99b4c9dc70356424ba`; sheet PNG `95b8eb85d73d8b289961b67687f76d97d0a0e4923241ccd25bbcca7faad3a4a4`; static PNG `2efbb41306c82926456f85105e376a8427b0ee480d706056f86c8d7e9fb53fe7`; sheet DDS `fca99f40bc370190fa6dd9f95530f3cf124d9ee9a31ab3159901c2cf87fb8cf5`; static DDS `5787cccf6dc7fc8261de41c24f51dd1399002c7a7b270e2ea55d4670e45da0ac`; review GIF `fd34a387f28f0f556bd88df185f202883ec6932ee1b16f69e06e04486dbe9d82`; contact `d1a00ee4834f61c27b91a9f41b1506a2d19f603cf44702e2067180b23d54138b`.
