# Event 020 Royal Node counterstrike decision icon

This package supplies the dedicated 2D icon for the existing shared-category `Strike Royal Node` operation. It does not add a decision category, country tag, scripted GUI, or model.

## Runtime contract

- Sprite: `GFX_decision_black_plague_strike_royal_node`
- Definition: `interface/020_black_plague_response.gfx`
- Consumer: `black_plague_shared_strike_royal_node` in `common/decisions/020_black_plague_shared_response_decisions.txt`.
- Runtime texture: `gfx/interface/decisions/020_black_plague/decision_strike_royal_node.dds`.
- Canvas: 33x32, one-level transparent DDS with no mipmaps.

The icon depicts a basalt Royal Node split by a silver counterstrike spear and an electric break in the plague sigil. It is visually distinct from the Crown Strike seal and the generic military support icon it replaces.

## Source and processing evidence

- Source PNG: `docs/assets/020_black_plague/source_png/decision_strike_royal_node_imagegen_source.png` (1275x1234 RGB), SHA-256 `c2ad4667117ba5fb19fc40a895992e2ecebe5d92600d333de585145a3803fd21`.
- Chroma-key intermediate: `docs/assets/020_black_plague/alpha_intermediate/decision_strike_royal_node_transparent_fullres.png`, SHA-256 `add43a18c9f32e028b4da752371bec2e4f307228e2438d106ccfad5b4b453575`.
- Processed icon: `docs/assets/020_black_plague/processed_png/decisions/decision_strike_royal_node_33x32.png`, SHA-256 `f612bfe56fe337c527ce95c5dafa7df516a20c3f6fb3858a4449e8e3f08c4733`.
- Runtime DDS SHA-256: `b416e63596f10386acb3cb96ca8dbd2440e9651679ed195d99d31234914e137d`.
- DDS header: `DDS `, header size 124, flags 4111, height 32, width 33, pitch/linear size 132.

The source was generated with the built-in ImageGen workflow on 2026-08-01 using a prior Crown Strike icon only as a style reference. The source prompt required a distinct Royal Node, silver spear, plague-sigil break, no text, no flag, no human unit, no rat, and vivid chroma-green isolation. No third-party source or model asset is used.
