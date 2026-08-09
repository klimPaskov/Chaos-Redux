# postwar_constitutional_review_states

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_decision_012_africa_postwar_constitutional_review`.
- Static fallback sprite: `GFX_decision_012_africa_postwar_constitutional_review_static`.
- Static fallback PNG: `postwar_constitutional_review_states_static.png` (acceptance source); runtime static DDS: `gfx/interface/decisions/012_africa/decision_012_africa_postwar_constitutional_review.dds`.
- Horizontal sheet PNG: `sheets/postwar_constitutional_review_states_sheet.png`; runtime sheet DDS: `gfx/interface/decisions/012_africa/postwar_constitutional_review_states_sheet.dds`.
- Review GIF: `previews/postwar_constitutional_review_states_preview.gif` (review only); row contact sheet: `previews/postwar_constitutional_review_states_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: postwar review.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `20386eeef89789ccd865628d573903fc415655cef3f1bdb55b992b9f96db9d25`; processed set `f14479e5f6ae83d4641a4f225d1784fa238da6f3532d21609e55f94d12ffbdad`; sheet PNG `a411a14413c788cbdd599f364cd6477eadfeeb2d767c7661e9d6668e95d128a5`; static PNG `aaa9f90e9d20a538ffe7c90d1156473a3e4fb205f99e557830bc2a5aa800c80f`; sheet DDS `924ae382c81b02630a8fbab24d79fb6b1e5ba37f639b9f5c105089a8597ee93a`; static DDS `58a0349817cb291908447fc13c601ab55795bd8f35daffdb7f8d6aacbee90f9d`; review GIF `2d047237b948a3dcf29d4bf45d700d1505d883bf62fa8f53aa5bde9d47993e63`; contact `0ab9dce431f9b22f9cbba2604249df4630320a968e48a21c0f756e96ea25dbe1`.
