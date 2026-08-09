# selected_member_confidence

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 8 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_selected_member_confidence_animated`.
- Static fallback sprite: `GFX_012_africa_selected_member_confidence_animated_static`.
- Static fallback PNG: `selected_member_confidence_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/animations/selected_member_confidence_static.dds`.
- Horizontal sheet PNG: `sheets/selected_member_confidence_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/animations/selected_member_confidence_sheet.dds`.
- Review GIF: `previews/selected_member_confidence_preview.gif` (review only); row contact sheet: `previews/selected_member_confidence_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 8`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: confidence state.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `26e1c045a74036ba8f8dcda56574aad136b884b3bc401e9013609e8aea60a0b4`; processed set `a5e1109187abe9a71183906fdcf2066d4e36128506d09639d69c641b0fd090cd`; sheet PNG `de1dba6f1eef64c5a82e993f1b021d9f6d454cc2066f8050208e893c2de10082`; static PNG `db608db68c0d1d1c3f2de3b056b3913904bfd3f21ae2ab6d2e45fd5c7481774a`; sheet DDS `763b87e96b96156112335fbfcef8a58b83c613df83c586fc1e976525170be2e3`; static DDS `8c625069d481affe07b30c107ee508f4c0f41c07f172bb221485ed61648d11aa`; review GIF `50fd391c8fadc8b1cf48269f292ae41f1609dcf0648b572e4ca2a7c617a6fcf2`; contact `3fcda31073fc6cf7be9325a73ece3c81d35ebaf7e26ffbd66b2c6ca4ff199575`.
