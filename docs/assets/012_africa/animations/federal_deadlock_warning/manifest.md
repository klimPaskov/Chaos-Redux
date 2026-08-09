# federal_deadlock_warning

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 3 frames; horizontal sheet; 5 FPS; looping = no; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_decision_012_africa_federal_deadlock`.
- Static fallback sprite: `GFX_decision_012_africa_federal_deadlock_static`.
- Static fallback PNG: `federal_deadlock_warning_static.png` (acceptance source); runtime static DDS: `gfx/interface/decisions/012_africa/federal_deadlock_warning_static.dds`.
- Horizontal sheet PNG: `sheets/federal_deadlock_warning_sheet.png`; runtime sheet DDS: `gfx/interface/decisions/012_africa/federal_deadlock_warning_sheet.dds`.
- Review GIF: `previews/federal_deadlock_warning_preview.gif` (review only); row contact sheet: `previews/federal_deadlock_warning_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (3 separately authored PNGs); processed frames: `processed_frames/` (3 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 3`; `animation_rate_fps = 5`; `looping = no`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: deadlock/compromise.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `7ecef540e5e310c184823b886334e8635e01c6eb52393902d9e7382f94847526`; processed set `79e9762e816ff59aa55275ffc50ca9b60bb8f799673f0c86709bb1a69b52f7bd`; sheet PNG `24d97763b8b5648283b1e9c533b5ccf9ae8fdd6d36e4aa8832c4a33f7c08310e`; static PNG `e2a2b0d00e007bbc2dd1dfc19c18754224a70b8076e83e69555ab57128a85407`; sheet DDS `55c672895288f9ea4993dd476dfdaf8167473dab52cb4e85729c1b6faaa3cb60`; static DDS `1925c200b7c8664bc73e72f60459908f4b918e583128bb48603b76ec05b220d8`; review GIF `d70d0918e6a54a66a78fc1d38c98e36e0fbf5226efa08e589369448e3b760834`; contact `cbfc9fb98e4b309e44a84bd56d93f02c4a554294aeb3f2c3958399f5a7a6d442`.
