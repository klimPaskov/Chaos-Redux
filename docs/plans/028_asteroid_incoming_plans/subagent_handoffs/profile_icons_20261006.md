# Event 028 material-profile icon production handoff

Record date: 2026-10-06.
Disposition: implemented by the asset producer; parent art acceptance, sprite registry wiring, consumer rewiring, and final documentation alignment remain pending.
Acceptance basis: the parent task explicitly authorized exactly three crater material-profile state-modifier icons and cited takeover-history `phase2_history/028.md impl:r3`; the current accepted requirements are present in Event 028 specification Parts 5 and 6 and `docs/events/028_asteroid_incoming/overview.md`.
The cited takeover-history file was not found under the repository `docs/` tree in the bounded lookup; the direct parent task and current specification supplied the full asset scope and stable names.

## Produced assets

The package contains exactly three new runtime DDS files, all at the parent-specified paths:

| Profile | Parent-reserved sprite | Final DDS | Runtime SHA-256 |
| --- | --- | --- | --- |
| Dense metallic meteorite | `GFX_idea_asteroid_incoming_dense_metallic` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_dense_metallic.dds` | `ea7473d96b9fbd436b9b641a62f0eece4950f986f67dd8eca637318b619b6552` |
| Fused silicate composite | `GFX_idea_asteroid_incoming_fused_silicate` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_fused_silicate.dds` | `deb585735ba5889be760bae5f4f9c2afb5c8705434e1184b33e56b139c468f99` |
| Shock-formed crystal and glass | `GFX_idea_asteroid_incoming_shock_crystal` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_shock_crystal.dds` | `db9e94939204e69f28bb219cacd908a6e97eef7c56f4705661ec6a1d1b2a1c1d` |

Source art, prompts, processed previews, contact sheets, exact generation receipts, source/reference metadata, alpha measurements, strict DDS decode evidence, and the sprite handoff are in `docs/assets/028_asteroid_incoming/profile_icons_20261006/`.
The complete file crosswalk and processing record are in that package's `manifest.md`.

## Design and evidence

Part 5 names the dense metallic, fused silicate, and shock-formed crystal/glass profiles.
The Part 6 survey flow reveals the profile and applies a matching named state marker.
The current Event 028 overview states that the markers have no modifier values, do not change armour, and still reuse the fragment-crater icon pending profile artwork.

The exact state-modifier consumer, the seven existing Event 028 state DDS files, and the canonical `icons/state_modifiers` contact sheet confirm a single transparent 32x32 frame.
Canonical reference sources and installed vanilla definitions were inspected, with source-kind evidence and PNG-to-DDS pixel equality retained in `qa/reference_inspection_v1.json`.
The produced final DDS files each have a strict 124-byte header, 32x32 dimensions, legacy 32-bit BGRA masks, 4,224-byte size, alpha from 0 through 255, and decoded pixels identical to their processed PNG.
Three separate built-in ImageGen calls requested genuine transparency at creation; no opaque canvas, chroma background, background-removal fallback, component layer, primitive local drawing, or unrelated icon resize was used.

## Parent follow-up and limits

The parent owns `interface/028_asteroid_incoming.gfx`, all three dynamic-modifier sprite assignments, and updating the Event 028 overview and existing state-modifier asset documentation after wiring.
The current overview's note that the three profiles reuse the fragment-crater sprite remains accurate until those assignments are made.
The parent should inspect the native-size and 4x contact sheets, record an independent art verdict, wire the exact identifiers and paths, and complete its broader Event 028 acceptance work.
No gameplay, modifier, armour, localisation, GUI, event, history, or spreadsheet file was changed.
No source or generated art was promoted as parent-accepted, and no live in-game state-window acceptance is claimed.

No simplification or asset fallback was used.
