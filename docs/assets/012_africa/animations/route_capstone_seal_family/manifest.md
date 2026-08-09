# route_capstone_seal_family

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 8 frames; horizontal sheet; 8 FPS; looping = no; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_route_capstone_seal_family_animated`.
- Static fallback sprite: `GFX_012_africa_route_capstone_seal_family_animated_static`.
- Static fallback PNG: `route_capstone_seal_family_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/routes/route_capstone_012_africa_covenant.dds`.
- Horizontal sheet PNG: `sheets/route_capstone_seal_family_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/routes/route_capstone_seal_family_sheet.dds`.
- Review GIF: `previews/route_capstone_seal_family_preview.gif` (review only); row contact sheet: `previews/route_capstone_seal_family_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (8 separately authored PNGs); processed frames: `processed_frames/` (8 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 8`; `animation_rate_fps = 8`; `looping = no`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: route capstone reveal.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `d6f08dfed4b7883c1d0be69c381878b61c553addc2b561f0c7ee467c0dec2778`; processed set `eb47bd07bbffed919acacda44611a08304abe019901d28a167188f31c615470b`; sheet PNG `b4f8e7c29fef248e615b3209f71722aa30c5e3e75cc808447be8d7ef2b15f19e`; static PNG `6136c217414a48f5ea1708158b720d5f0a4dfbad94dc333bf6fa3a7206ab9f9b`; sheet DDS `09f6fdf446a61db17606885b5bff3d5dbed205f400b5cdbab825c85cb2ea9bcd`; static DDS `f57d384c2551af200a43cdfef83fe159dcff0820f412feb18510f4850c8e385f`; review GIF `5a252498b55952dab4b1f210ae655c5ab80c1d401980e42b218f22a685aee487`; contact `fc9d810071518f55d3e626b0ff0613bbac20c5e680d663d943530fb262eccef4`.
