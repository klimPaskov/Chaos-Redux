# confederal_emergency_ratification_states

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 6 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_decision_012_africa_confederal_ratification`.
- Static fallback sprite: `GFX_decision_012_africa_confederal_ratification_static`.
- Static fallback PNG: `confederal_emergency_ratification_states_static.png` (acceptance source); runtime static DDS: `gfx/interface/decisions/012_africa/decision_012_africa_confederal_ratification.dds`.
- Horizontal sheet PNG: `sheets/confederal_emergency_ratification_states_sheet.png`; runtime sheet DDS: `gfx/interface/decisions/012_africa/confederal_emergency_ratification_states_sheet.dds`.
- Review GIF: `previews/confederal_emergency_ratification_states_preview.gif` (review only); row contact sheet: `previews/confederal_emergency_ratification_states_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 6`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: ratification states.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `96cc52d5fa3c879420518b1ddd1a3194f599e3caecf5ad21f8f99cf140c30ba4`; processed set `37ce41c502fe06efb16986aef6cc3ff6093fe08090bc52fccc8fffc7d737fbaf`; sheet PNG `2318930a379f42f4231d7f997e0de34e843d6dccedf509bce0a64e23b3375a7f`; static PNG `e8739420c1f1e5d6eb558f6b9d04e6c48daf20ed1b38ff5214ee0e3fab1f408e`; sheet DDS `1abca4363f0b8e82d865505852c7b4bcac809a7df11bbf610c4f34e35b26a008`; static DDS `f3aaa4d8d4b39016681c0cdc968cc190495a0cbc9aa24995f110a32013049816`; review GIF `f65d339af0e1fd32f9a68e34b6d6d7f20f74e3879622857cd50ca68a93269acb`; contact `4085b7c01fdb8ef716bda3e7d1c59204584e3ff09b9a5b52f0040a58fd2fb30e`.
