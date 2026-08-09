# priority_member_promotion_card

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_priority_member_promotion_card`.
- Static fallback sprite: `GFX_012_africa_priority_member_promotion_card_static`.
- Static fallback PNG: `priority_member_promotion_card_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/restorations/priority_member_promotion_card.dds`.
- Horizontal sheet PNG: `sheets/priority_member_promotion_card_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/restorations/priority_member_promotion_card_sheet.dds`.
- Review GIF: `previews/priority_member_promotion_card_preview.gif` (review only); row contact sheet: `previews/priority_member_promotion_card_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: eligibility/promotion.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `56fc488658cc62eff6ca1f6c1c10930bfbe6f4854e09bd931f562bdab73c9b9a`; processed set `568121ca5a7275ba22fd49a680c9d4e5458b0b1fe843350ff18b5e30593fb308`; sheet PNG `35d3674defb83c3a26541f50d221c96b08c9e9d2d6c558c3566bdeff5edd3433`; static PNG `abcbc90f66d961e1f9d00226f4d6a66034778b152b5d0a52499cbff8085bac91`; sheet DDS `938e76ac20761ed3138f0a14c47f9bffb5f6f1dccea6512de6a1138b113d067e`; static DDS `3d8cd8e4c214eec47df48aa9ba292b224bf71954c1d5127886faa9bf898ea17e`; review GIF `9951951308fd56c1ef2aac77c5d6d703205bdbf0d9983b6ed5c315a90fef260e`; contact `415ff66c9a7307ee8b0c67c90ef0ee672fb18c36333e12d1bfa0142de1607224`.
