# congress_ready_emblem

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 72x72 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_congress_ready_emblem_animated`.
- Static fallback sprite: `GFX_012_africa_congress_ready_emblem_animated_static`.
- Static fallback PNG: `congress_ready_emblem_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/congress_ready_emblem_static.dds`.
- Horizontal sheet PNG: `sheets/congress_ready_emblem_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/congress_ready_emblem_sheet.dds`.
- Review GIF: `previews/congress_ready_emblem_preview.gif` (review only); row contact sheet: `previews/congress_ready_emblem_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: congress ready.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `3e6d049a73e046a7286e85bcf2497e80e3764723e525df92677241cc4682ce65`; processed set `9e6011873f737727f8b8094d8707afc140e942ad3ea1e1877466c6229aab0709`; sheet PNG `3e4176ceaa4ada878f53b50c333ffb277feb3a12344a064bdbb184875085778b`; static PNG `fe19eb6aee516a7a9696c9d53674c8cd89607de260d1bcff889b720fe0f9557f`; sheet DDS `9e80f15ccb138c896d680089bcb62625cef74547a9241c66af2f1649b7e1c3b7`; static DDS `bae45b3fa104387418bbc350a095c74139e21858e3e5011166c2ed65ec6a110e`; review GIF `ccb5f4e7e2d90a217bc0bf4757ccef5538ad49aebb693c5a2f5f793a6a43e00c`; contact `574c701233955be13583419c7bfd178a97cfc425777ead7c3e07e23dd3d70592`.
