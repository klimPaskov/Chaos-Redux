# continent_war_terminal

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 128x128 per frame; 12 frames; horizontal sheet; 8 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_continent_war_terminal_animated`.
- Static fallback sprite: `GFX_012_africa_continent_war_terminal_animated_static`.
- Static fallback PNG: `continent_war_terminal_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/continent_war_terminal_static.dds`.
- Horizontal sheet PNG: `sheets/continent_war_terminal_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/continent_war_terminal_sheet.dds`.
- Review GIF: `previews/continent_war_terminal_preview.gif` (review only); row contact sheet: `previews/continent_war_terminal_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (12 separately authored PNGs); processed frames: `processed_frames/` (12 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 12`; `animation_rate_fps = 8`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: terminal war.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `65784c0da853582d0caa3add2a035e4647a5d05769ad41010de8e8b87a93dded`; processed set `0c3b802919d52c5def20f13ece64c7250b16f38719628f96aea44ddb252503c2`; sheet PNG `03189094e648415d5c9062b3935ee2cc9e43b631ed923bbd87c68b1cb96e0896`; static PNG `b386305c488176bda35fc963cd7e10efbf745f0b0b19c2030005978db605b42b`; sheet DDS `533d8d66a5904365282f3777d27913d7b9df2517543d9bac57060c544a28ac78`; static DDS `cd0a6fc7b0f8cc6ef2cbb4212871eb90bb2ce26acdc3bc7df112a3519c110b54`; review GIF `609b9c94d40ee3bb7833619de55d27fc09646599272737d007fb8c59f59a1580`; contact `155ab3260ec313f5730bdb015f18fb150fab73a69c0f0ec5c7beea6d57e53a24`.
