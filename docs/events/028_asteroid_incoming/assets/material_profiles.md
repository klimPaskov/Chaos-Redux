# Asteroid material profile icons

Disposition: implemented and parent accepted for artwork, processing, and source wiring on 2026-10-06; native state-window presentation remains to be observed.
Acceptance basis: the user authorized completion of the 028 workstream, including the profile artwork gap recorded by takeover round 3 and specification Parts 5 and 6.
The parent independently inspected the native-size background review and the 4x contact sheet after production.
The compact metal section, ochre fused stone, and blue-grey crystal cluster are distinct, centered, and readable against dark, light, and checkerboard backgrounds, with no opaque square or fantasy glow.

| State modifier | Sprite in `interface/028_asteroid_incoming.gfx` | Runtime DDS | SHA-256 |
| --- | --- | --- | --- |
| `asteroid_incoming_crater_material_dense_metallic` | `GFX_idea_asteroid_incoming_dense_metallic` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_dense_metallic.dds` | `ea7473d96b9fbd436b9b641a62f0eece4950f986f67dd8eca637318b619b6552` |
| `asteroid_incoming_crater_material_fused_silicate` | `GFX_idea_asteroid_incoming_fused_silicate` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_fused_silicate.dds` | `deb585735ba5889be760bae5f4f9c2afb5c8705434e1184b33e56b139c468f99` |
| `asteroid_incoming_crater_material_shock_crystal` | `GFX_idea_asteroid_incoming_shock_crystal` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_shock_crystal.dds` | `db9e94939204e69f28bb219cacd908a6e97eef7c56f4705661ec6a1d1b2a1c1d` |

All three images use separate native ImageGen sources with transparency requested at creation.
The processor preserves alpha and produces single-frame 32x32 legacy BGRA DDS files.
Strict DDS decoding matches each processed PNG exactly; all files are 4,224 bytes with alpha spanning 0 to 255.
The exact consumer and installed vanilla references are documented in the producer's reference inspection.
No background-removal fallback or unrelated-icon substitution was used.
These three state markers contain no modifier values and leave armour unchanged.

The active evidence package is `docs/assets/028_asteroid_incoming/profile_icons_20261006/`, including `manifest.md`, prompts, ImageGen receipts, source and processed PNGs, decoded DDS previews, `qa/reference_inspection_v1.json`, and native/4x contact sheets.
The production handoff is `docs/plans/028_asteroid_incoming_plans/subagent_handoffs/profile_icons_20261006.md`.
Keep the event workspace while the larger event remains incomplete; no runtime sprite references that workspace.
The seven earlier impact/recovery state icons remain covered by `state_modifiers.md`.
