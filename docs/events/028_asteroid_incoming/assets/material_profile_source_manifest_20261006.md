# Material-profile production evidence

Disposition: implemented production evidence retained as a historical producer snapshot from before parent wiring.
Its pending-review and old-sprite statements below are superseded by `material_profiles.md` and the matching installed consumers.
Current parent acceptance and wiring are recorded in `material_profiles.md`.
Paths below refer to the active ignored workspace `docs/assets/028_asteroid_incoming/profile_icons_20261006/`; it is retained while Event 028 remains incomplete.
The workspace is not shipped or force-added to Git.

# Event 028 crater material profile icon package

Record date: 2026-10-06.
Disposition: all three source, preview, and DDS assets are produced; parent art review and sprite/consumer wiring remain pending.
Acceptance basis: the parent task explicitly authorizes these three missing material-profile icons and cites takeover history `phase2_history/028.md impl:r3`; the current accepted material-profile design appears in the Event 028 specification and overview.
The cited takeover-history file was not present under the repository's `docs/` tree during this bounded lookup, so this package follows the direct parent assignment and the current repository specification.

## Consumer and requirement

The three persistent profile-only state markers are `asteroid_incoming_crater_material_dense_metallic`, `asteroid_incoming_crater_material_fused_silicate`, and `asteroid_incoming_crater_material_shock_crystal` in `common/dynamic_modifiers/028_asteroid_incoming_crater_dynamic_modifiers.txt`.
Each marker currently uses the fragment-crater sprite and has no modifier values.
The Event 028 overview states that the marker's profile art is the remaining asset gap.
Part 5 names the three site profiles, and Part 6 places the names in the material-survey flow.
Each profile communicates material flavour only; none changes armour or any gameplay value.

The exact consumer and existing Event 028 state-modifier examples establish a 32x32 RGBA single-frame texture with genuine transparent unused canvas.
All three final files use the requested legacy uncompressed BGRA DDS encoding at 32x32.

## Runtime crosswalk

| Profile | State marker consumer | Parent-reserved sprite | Final DDS | Processed PNG | ImageGen source PNG | DDS SHA-256 | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dense metallic meteorite | `asteroid_incoming_crater_material_dense_metallic` | `GFX_idea_asteroid_incoming_dense_metallic` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_dense_metallic.dds` | `processed_png/asteroid_dense_metallic_32x32.png` | `source_png/asteroid_dense_metallic_imagegen_source.png` | `ea7473d96b9fbd436b9b641a62f0eece4950f986f67dd8eca637318b619b6552` | Needs parent art review and wiring |
| Fused silicate composite | `asteroid_incoming_crater_material_fused_silicate` | `GFX_idea_asteroid_incoming_fused_silicate` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_fused_silicate.dds` | `processed_png/asteroid_fused_silicate_32x32.png` | `source_png/asteroid_fused_silicate_imagegen_source.png` | `deb585735ba5889be760bae5f4f9c2afb5c8705434e1184b33e56b139c468f99` | Needs parent art review and wiring |
| Shock-formed crystal and glass | `asteroid_incoming_crater_material_shock_crystal` | `GFX_idea_asteroid_incoming_shock_crystal` | `gfx/interface/state_modifiers/028_asteroid_incoming/asteroid_shock_crystal.dds` | `processed_png/asteroid_shock_crystal_32x32.png` | `source_png/asteroid_shock_crystal_imagegen_source.png` | `db9e94939204e69f28bb219cacd908a6e97eef7c56f4705661ec6a1d1b2a1c1d` | Needs parent art review and wiring |

The parent owns `interface/028_asteroid_incoming.gfx` and the three dynamic-modifier icon assignments.
No GFX, gameplay, localisation, GUI, event, history, or shared asset catalog file was changed by this package.

## Original art and processing

Each asset has one separate built-in ImageGen call with `transparent_background: true` in the initial request.
The original returned 1254x1254 RGBA PNG is preserved byte-for-byte in `source_png/`, with its exact prompt under `prompts/` and the returned output path and alpha evidence under `tool_receipts/`.
No model or backend name is claimed because the exposed ImageGen tool offered no model selector.
No CLI/API generation fallback or background-removal fallback was used.

Processing uses the complete nonzero-alpha source bounds plus an 8-source-pixel guard, one aspect-preserving Lanczos resize in premultiplied RGBA mode, and integer-centered placement on a transparent 32x32 canvas.
The maximum fitted specimen edge is 26 pixels, leaving transparent breathing room and preserving each generated silhouette.
The unmodified source, processed PNG, and final DDS remain separate files.

The generated materials read distinctly at native size: a silver-gray exposed iron-nickel face for dense metallic, subdued amber fused seams over an ash-brown composite for fused silicate, and cool angular fractured faces for shock crystal/glass.
The crystal/glass art has no emissive glow or fantasy jewel treatment.
No visual component or background layer was applied; the component catalog has no matching state-modifier material component or appropriate `background_template`.

## Reference inspection

The canonical contact sheet at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/state_modifiers/contact_sheet.png` was opened before the individual references.
The selected vanilla state-modifier references are the CZE separatism and generic guerrilla-base icons, plus the radiation hazard icon.
Each is native 32x32, transparent, and was byte-source-checked against its installed vanilla DDS; hashes, paths, source-kind evidence, and comparisons are in `qa/reference_inspection_v1.json`.
The radiation image is recorded in the canonical `REFERENCE_MANIFEST.md` and its installed `interface/countrystateview.gfx` declaration, although it has no row in the current `CATALOG.md` table.
The exact installed references confirm the vanilla texture family and the transparent 32x32 treatment; their depicted symbols were not copied into the new art.

The existing Event 028 fragment-crater DDS was decoded to `qa/consumer_fragment_crater_reference.png` for motif review.
It is a compact dark meteorite fragment on transparent canvas and remains unmodified at its runtime path.

## Validation and review

All three source files have alpha extrema 0 through 255 and transparent corners.
All processed PNGs and decoded DDS files are exactly 32x32 with alpha extrema 0 through 255 and transparent corners.
Every final DDS has a strict 124-byte DDS header, a 32-byte pixel-format header, 32-bit BGRA masks, one image level, and a 4,224-byte total length.
Pillow decoding of each DDS is pixel-equal to its processed PNG, and the full file, PNG, decoded-pixel, and processing hashes are recorded in `qa/asset_validation_v1.json`.

Native-size and 4x nearest-neighbour contact sheets are in `contact_sheets/`; `qa/background_review_native.png` shows each 32x32 subject on dark, light, and checker review backgrounds.
The 4x sheet is for inspection only; nearest-neighbour enlargement is not used in any final texture.
Producer review found no opaque backing, clipping, coloured fringe, matte, fake checkerboard, unintended transparent hole, or lost outer silhouette.
Parent visual acceptance remains pending.

## Evidence index

| Evidence | Path |
| --- | --- |
| Native generated source atlas | `contact_sheets/source_atlas.png` |
| Native 32x32 contact sheet | `contact_sheets/profile_icons_native_32x32.png` |
| 4x nearest-neighbour contact sheet | `contact_sheets/profile_icons_4x_nearest.png` |
| Transparent-background review | `qa/background_review_native.png` |
| Consumer motif decode | `qa/consumer_fragment_crater_reference.png` |
| Reference paths, source kinds, and pixel comparisons | `qa/reference_inspection_v1.json` |
| Source, crop, alpha, DDS, and pixel-equality receipts | `qa/asset_validation_v1.json` |
| Processing geometry | `qa/processing_geometry_v1.json` |
| Exact prompts | `prompts/` |
| Built-in ImageGen tool receipts | `tool_receipts/` |

Live state-window and in-game consumer acceptance have not been performed by this producer.
