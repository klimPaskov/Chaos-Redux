# ecological_wrath_active

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 96x96 per frame; 10 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_ecological_wrath_active_animated`.
- Static fallback sprite: `GFX_012_africa_ecological_wrath_active_animated_static`.
- Static fallback PNG: `ecological_wrath_active_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/ecological_wrath_active_static.dds`.
- Horizontal sheet PNG: `sheets/ecological_wrath_active_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/ecological_wrath_active_sheet.dds`.
- Review GIF: `previews/ecological_wrath_active_preview.gif` (review only); row contact sheet: `previews/ecological_wrath_active_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (10 separately authored PNGs); processed frames: `processed_frames/` (10 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 10`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: wrath threshold.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `999d564e360937adf2463c7aa09d6ae596fbe95b71221b7e063c9ac21f9c1a18`; processed set `53d0aa652b408e99da3cca39ccfb1df01ce24c745c4c9ba3488222b5ffbd454e`; sheet PNG `fd9042b894950dffb605aff4ce69f5f6c1fede694d4363d43c98ed518d2c8bec`; static PNG `a59a24959bb723466a3796cade043b3913256193eb640053c34856b206b3e20a`; sheet DDS `67b69dd3b21f05038f118803f3ce8bce093cbb1abf3b29461546f7f1b0e3c7c6`; static DDS `a01536184e78c15e0231bde31adf3cd20c8dac3f8cf5454d3f0255146ff4e61c`; review GIF `f747a03f8b9fd153fd679dab03a03b0fdb89f40ee397a0efe820e79cd198ad96`; contact `2bd2a650a302e248bbe02ad03fb1427818ff6ebfe885ffccd4331e5e630eec99`.
