# covenant_obligation_review_states

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_decision_012_africa_covenant_obligation`.
- Static fallback sprite: `GFX_decision_012_africa_covenant_obligation_static`.
- Static fallback PNG: `covenant_obligation_review_states_static.png` (acceptance source); runtime static DDS: `gfx/interface/decisions/012_africa/covenant_obligation_review_states_static.dds`.
- Horizontal sheet PNG: `sheets/covenant_obligation_review_states_sheet.png`; runtime sheet DDS: `gfx/interface/decisions/012_africa/covenant_obligation_review_states_sheet.dds`.
- Review GIF: `previews/covenant_obligation_review_states_preview.gif` (review only); row contact sheet: `previews/covenant_obligation_review_states_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: obligation review.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `376bbd2e0bccab500d480c4657a3ff4399611262c0eb79cd2f193b4506e5d6ce`; processed set `f71cc0f85c0be7288a1cbe78a41fdc57c6a7e2179b83d08a17bffa6ac97f3465`; sheet PNG `ebcc535268d2415cf79bf61ca887cf1a9124a165904598c8abd146086e4f9672`; static PNG `164fa02c19a551055bc14a814ea11a02c0edabccd6b2aed5dd74f8eaf006d044`; sheet DDS `2f73205ac3e5ac1898d61bb9ac22a1a8cd748968d7eb1f67079811438879e5ee`; static DDS `bf6aedde527e80cb1c0aa41316b4fd03b06d4380d2f01703c90e5d0ffe4eadc7`; review GIF `b0cc97f0892be893690707a647301b512e98d8ff21485abbebe64c2a9a54f078`; contact `bd75cc1f21f23e7f2e89123ca50ca91c0d6828adc8826fa863657645fe7eb1ae`.
