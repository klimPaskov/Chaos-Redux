# host_first_proof_state_kit

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 6 frames; horizontal sheet; 6 FPS; looping = no; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_host_first_proof_state`.
- Static fallback sprite: `GFX_012_africa_host_first_proof_state_static`.
- Static fallback PNG: `host_first_proof_state_kit_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/host_overlays/host_first_proof_state_kit_static.dds`.
- Horizontal sheet PNG: `sheets/host_first_proof_state_kit_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/host_overlays/host_first_proof_state_kit_sheet.dds`.
- Review GIF: `previews/host_first_proof_state_kit_preview.gif` (review only); row contact sheet: `previews/host_first_proof_state_kit_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (6 separately authored PNGs); processed frames: `processed_frames/` (6 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 6`; `animation_rate_fps = 6`; `looping = no`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: proof state kit.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `a912d6fb8e2075cef81ac5fa6f105ac8e33064b8b5f330cf864c646dab65f631`; processed set `3cdb00e289f153a3f5604e2d2cf6a5828b15901e3cc5880eb771dc66df02da33`; sheet PNG `f4e1e466eb173bbcb33206940545db12991e63898c22c46c495194b32969af64`; static PNG `b75f7892208acfaf404a4278cbf4dd7e2361b48183aba175de74bbdf74627629`; sheet DDS `b6b3176c386d32e49074cd4bd7ffdb09436cf1233e5ab25bce00ddd68113a9a0`; static DDS `f0d0258d041f89f4c7a148f12c280b9ab02c2dced9c4bf783ef52ca8bb2252da`; review GIF `6e02a5f228cb3c32b60d2ae3178640f8e3c1995f076047a5c5a74482502d0591`; contact `9e4b02f058ab31ad560edc255e09884472b34db295425d5741cc6e69808fc6d7`.
