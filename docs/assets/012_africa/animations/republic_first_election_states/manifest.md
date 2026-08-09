# republic_first_election_states

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 8 FPS; looping = yes; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_decision_012_africa_first_election`.
- Static fallback sprite: `GFX_decision_012_africa_first_election_static`.
- Static fallback PNG: `republic_first_election_states_static.png` (acceptance source); runtime static DDS: `gfx/interface/decisions/012_africa/decision_012_africa_first_election.dds`.
- Horizontal sheet PNG: `sheets/republic_first_election_states_sheet.png`; runtime sheet DDS: `gfx/interface/decisions/012_africa/republic_first_election_states_sheet.dds`.
- Review GIF: `previews/republic_first_election_states_preview.gif` (review only); row contact sheet: `previews/republic_first_election_states_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 8`; `looping = yes`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: election states.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `445c465f0aecf8eccc9013f6ee2bee29229d255ed0df6774ce465b23fdde7a7a`; processed set `b818ddd280ff9e4af6d6925e8b04b24de983ea6e7fc0e76d3bb1c6d773e28cdf`; sheet PNG `fb37f2dc7a5ea7853fcadcd0c6aaa318bfb03d728e75c0692c3c515934b8bd2e`; static PNG `9e852a3a8032181513c856cff77f702db1f86870b585db5bf0deb3a00a62c273`; sheet DDS `faeb964c55e0965914181fe9ca725690d9096c0d8dc0731db68ef594ff28d73e`; static DDS `86d08acd5760921a51bd2414c5f24cd90d43e6cd5524d2e7357c38a3abb7c779`; review GIF `59d64926578f7b803d5672602a5e62464db7e8a883889c248ac984a2faa168a6`; contact `71b3264f5613917437ec4698eceb42d2cb26b4f92e19ed2d50cbd58426ab5919`.
