# Camp building icon asset handoff — 2026-08-02

> Superseded for visual acceptance by `2026-08-02_camp_building_icon_hoi4_style_correction.md`. The dimensions and frame-order history below remain useful, but its dark freeform artwork was rejected because it did not match the vanilla HOI4 building-tile style.

## Completed asset package

- Standalone concentration icon: `gfx/interface/buildings/building_concentration_camp.dds`, 27x23, SHA-256 `988589e8d6902cd7b53bf2f292ee5ad1e03062c10bf567e74c68b90c994b0c20`.
- Standalone extermination icon: `gfx/interface/buildings/building_extermination_camp.dds`, 27x23, SHA-256 `b769a1236f6fe773cb2d2da5b3a94c44335d73d9d17c6da97b94d68365a096cb`.
- Shared strip: `gfx/interface/buildings/building_icon_strip.dds`, 1610x46, 35 ordered 46x46 frames, SHA-256 `57480b03c2805e307ccdaf74e85ed76fbbe4cba841487be2beae947753163aa8`.

## Reviewed temporary evidence

The active package was reviewed under `docs/assets/system_camp_building_icons/` before completion cleanup. It contained the exact prompts, four built-in `$imagegen` source PNGs, alpha-cleaned selections, native processed PNGs, a checker-background contact sheet, a frames 31–35 order sheet, the manifest, source-mode notes, and the GFX handoff. The final runtime files and the durable provenance below remain authoritative after removal of that temporary workspace.

The accepted visual evidence is preserved at `docs/plans/system_camp_repression_rework_plans/subagent_handoffs/2026-08-02_camp_building_icon_contact_sheet.png` and `docs/plans/system_camp_repression_rework_plans/subagent_handoffs/2026-08-02_camp_building_icon_strip_frames31_35.png`.

## Durable source and prompt provenance

All four source artworks were generated independently with the official built-in `$imagegen` path on a flat `#00ff00` chroma-key background. The official `remove_chroma_key.py` helper supplied the soft matte, despill, and one-pixel edge contraction used for the selected alpha-cleaned sources. Vanilla building references supplied scale, palette, visual weight, and strip-order guidance only; no reference image was copied into the generated icons.

| Source artwork | Exact prompt intent | Generated source SHA-256 | Selected alpha source SHA-256 |
| --- | --- | --- | --- |
| Concentration standalone | Native `27x23` HOI4 building icon of an austere guarded detention compound with a short watchtower, low barracks, gate, and barbed-wire enclosure; muted iron, ochre, and grey; no people, text, political symbols, gore, bodies, flags, flames, skulls, generic fort, or opaque background. | `c61ff6a1877fa4e67461b624cddec9f0528e3dec962835adedec3b88c02fe386` | `0de2ba9ea5aa94ccf03eff8d8d843dc6e083ea4b202111fd083ca6ef5aa32113` |
| Concentration strip frame | Native `46x46` HOI4 strip tile of a front-facing guarded detention compound with a central gate, small watchtower, low barracks, and barbed-wire perimeter; square readable silhouette; independently composed rather than resized from the standalone icon; the same non-graphic constraints. | `148725fca0f6bb7e42010b139f8032a7da135b62a11c06daf75eb38ab86cbff0` | `e898272f41e403bb74ba0974f979d3b92dc49052d309b4bc12986d417a2493ef` |
| Extermination standalone | Native `27x23` HOI4 building icon of a sealed terminal industrial facility with barbed-wire perimeter, stark crematorium-style masonry, rigid gate, tall soot-dark chimney, and restrained cold smoke; charcoal, ash, and rust; no people, text, political symbols, gore, bodies, flags, flames, skulls, generic factory, or opaque background. | `7f0b23d4e5ef3072cb632f098986b568dbc10c7bd4503d6d1cb4eddd8131e4e5` | `2a4087b6e42a52e8ab906eb614c3ed7956f5b2ee9c4f5795cbd3bf30d5d4e9af` |
| Extermination strip frame | Native `46x46` HOI4 strip tile of a sealed industrial extermination facility with front perimeter and gate, soot-stained masonry, tall chimney, and cold smoke; independently composed rather than recoloured or resized from either concentration icon; the same non-graphic constraints. | `72bc5903b641a26c60b5151925ef836d96180c36f9b83e71de00bb67808048f6` | `8cc037454b9bfa01992680df86af8b7ff41e29fe7c1fe6139069a3710f663d40` |

The final processed PNG hashes were `da860374a6535ccf928b91e19b2356a641f7bdb2de002c4522f65b8b3ae1c0c9` for the concentration standalone, `f0a7d761ea271f5dddb6155213c1af19b1aa180ff79c3c48bd98f9bca743f3d4` for frame 34, `cff037141a0b73d6be31d853ac4311757bb8fed9356d338445e7abf60472221a` for the extermination standalone, `53a3da495d83ee73ad7d2ac6349d47314a8372903cb98d92d4aaa5112f6e796f` for frame 35, and `52f7b551150cf2b11fa068f795da7eb363f267d7ac5949c149764b1b60481b9c` for the assembled flattened strip.

## Strip reconstruction

Frames 1–31 were copied from the installed vanilla strip with per-pixel equality preserved. Existing Chaos frames 32–33 were retained pixel-for-pixel across their original 45 columns and repaired to 46x46 by appending one transparent rightmost column. Generated concentration and extermination tiles were appended as frames 34 and 35. No frame was shifted or resampled during strip assembly.

## QA and parent-owned work

The three DDS files have exact declared dimensions, full file lengths, legacy uncompressed BGRA headers, and alpha ranges of 0–255. The parent agent owns `.gfx`, GUI, gameplay, localisation, and runtime wiring; the building definitions already point to frames 34 and 35, and the shared strip declaration should expose 35 frames.

## Source limitation

The layered `gfx/interface/buildings/building_icon_strip.psd` was inspected but intentionally not overwritten because no safe layer-preserving writer is available. It remains the original 1516x46 historical source; the 1610x46 runtime DDS, hashes, reconstruction record, and exact frame crosswalk in this handoff are authoritative. No runtime consumer reads the PSD.
