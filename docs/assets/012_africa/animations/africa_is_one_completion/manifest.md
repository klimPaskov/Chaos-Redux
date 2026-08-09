# africa_is_one_completion

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 128x128 per frame; 12 frames; horizontal sheet; 8 FPS; looping = no; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_africa_is_one_completion_animated`.
- Static fallback sprite: `GFX_012_africa_africa_is_one_completion_animated_static`.
- Static fallback PNG: `africa_is_one_completion_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/africa_is_one_completion_static.dds`.
- Horizontal sheet PNG: `sheets/africa_is_one_completion_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/africa_is_one_completion_sheet.dds`.
- Review GIF: `previews/africa_is_one_completion_preview.gif` (review only); row contact sheet: `previews/africa_is_one_completion_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (12 separately authored PNGs); processed frames: `processed_frames/` (12 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 12`; `animation_rate_fps = 8`; `looping = no`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: unification completion.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `3bc339e9a33fa0194e85e1cc19e09069011e636f0c266d263ce38c773effdc18`; processed set `9247e6d2381ab20712ae61d8b7082d48ade4b7be8ef5d27c703ffedd4c224ae0`; sheet PNG `3e57ea009ec559db43c4e505c800b919b3386d49859dba74718c2a69eb74196c`; static PNG `19367027afc0464f7b144b2214eb79b8444d6cf0dfab80e34962a43af8849e1d`; sheet DDS `fa140d26d72fae271343253c5fc388bf54887f989e01c40e4eef06c68825c1c9`; static DDS `f5a6ab9b43fd23f9eccd086351b4c4a51b324c6cfdcacdaecd809c0e432b2c7a`; review GIF `f7f7565693e2a2aa70e9892b21f8f8e889dc0b167f16c7cf569b3001a72266fd`; contact `30c74777f9d810c91e61fd41a80de16d5df279afdb9ee834a60fca9630e035b4`.
