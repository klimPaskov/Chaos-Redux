# host_overlay_federal_amalgamation

- Status: complete visual package; runtime registration is bounded to `interface/012_africa_animations.gfx`; gameplay/GUI consumer binding remains parent-owned.
- Target: 64x64 per frame; 3 frames; horizontal sheet; 4 FPS; looping = no; play_on_show = yes; anchor = centered transparent padding.
- Animated sprite: `GFX_012_africa_host_overlay_federal_amalgamation`.
- Static fallback sprite: `GFX_012_africa_host_overlay_federal_amalgamation_static`.
- Static fallback PNG: `host_overlay_federal_amalgamation_static.png` (acceptance source); runtime static DDS: `gfx/interface/012_africa/host_overlays/host_overlay_federal_amalgamation_static.dds`.
- Horizontal sheet PNG: `sheets/host_overlay_federal_amalgamation_sheet.png`; runtime sheet DDS: `gfx/interface/012_africa/host_overlays/host_overlay_federal_amalgamation_sheet.dds`.
- Review GIF: `previews/host_overlay_federal_amalgamation_preview.gif` (review only); row contact sheet: `previews/host_overlay_federal_amalgamation_contact.png`; package contact sheet: `../animation_acceptance_contact.png`.
- Source frames: `source_frames/` (3 separately authored PNGs); processed frames: `processed_frames/` (3 exact-size PNGs). No frame is empty or byte-repeated.
- Source mode: built-in ImageGen storyboard with independently authored panels; local work only key removal, crop/normalization, sheet assembly, preview, and DDS conversion.
- Registration: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`; `noOfFrames = 3`; `animation_rate_fps = 4`; `looping = no`; `play_on_show = yes`; `alwaystransparent = yes`.
- State purpose: host overlay states.
- Visible QA: PASS. All frames/contact tiles were reviewed; no empty, repeated, drifted, or broken tiles observed. Runtime DDS header PASS: uncompressed 32-bit BGRA, one mip, declared dimensions match the PNG sheet/static canvas, exact payload length.
- Hashes (SHA-256): source set `9ba92456626407fe30cfd4e5efcc056ed06de271d3fb8069be96d63badee739f`; processed set `a641203c3ad9ad66a1d70e1396ae431ced86877bb5b85be278d9f4770b7fe83e`; sheet PNG `fad27c28e5f0853bdb05dee00f3eed41ebcb63574ce55d9a7c2fefa1bf954e35`; static PNG `e94430cdc3d1a27c03125f83af291b7867ef03448b20b31971d5cefe9ab6c5f2`; sheet DDS `20ce9e9f45852373e3a3de0d2b0e742bb16edacafd7cbdcab11e3860fedbbfe7`; static DDS `392d13a5fe02d8f6f3d695534d8755620dba7e21c22bd1dbf9b21524d28f3a5b`; review GIF `dbefebb9fc4d19f485c88273f2d78aa513def3a2cc6b2a91c64831c6a123a5f0`; contact `b1f636da6f10cf69f4e0ef06927cd5a207ec3814da7f1733e9b9bb3330b85151`.
