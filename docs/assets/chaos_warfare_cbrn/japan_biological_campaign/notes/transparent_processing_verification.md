# Transparent Processing and Runtime Verification

Review date: 2026-07-24.

## Source and preview measurements

| Artifact | Dimensions | Mode | Alpha range | Fully transparent pixels | Fully opaque pixels | Chroma-green pixels with alpha greater than zero | SHA-256 |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `source_png/japan_biological_campaign_icon_source_master.png` | `1430x1100` | RGB | `255..255` | `0` | `1573000` | `996280` | `41a4df30b8a14fac5083c81d3a20f4b5ae8636bd59a55eae84a4d047e7db2b3d` |
| `source_png/japan_biological_campaign_icon_source_alpha.png` | `1430x1100` | RGBA | `0..255` | `995779` | `563848` | `0` | `da5f38722f4293d35ece1027ba88daab895a9b04ec447a5cc060260135191be6` |
| `processed_png/decision_category_japan_biological_campaign_52x40.png` | `52x40` | RGBA | `0..255` | `811` | `834` | `0` | `619b201fc4f846029230c3d1587d2eed7d1bc842b97165659e6bdd60e0219777` |

The chroma-green count in the source master is expected because that file is the immutable flat-key ImageGen evidence source. The alpha source and processed preview contain no opaque chroma-green pixels, and all four processed-preview corners are `(0, 0, 0, 0)`.

The contact sheet `contact_sheets/decision_category_japan_biological_campaign_contact_sheet.png` shows the source master, alpha source, and exact 52x40 preview on checkerboard review backgrounds where transparency matters.

## Processing review

- The existing generated source was inspected and retained because it has a clear biological field-medical subject, a compact silhouette, and no disqualifying artefacts at the target size.
- The existing alpha source was inspected as RGBA and verified to have real transparency rather than a fake checkerboard or opaque square matte.
- The existing processed PNG was inspected at exact native dimensions and enlarged with nearest-neighbour review for silhouette readability.
- No source art was regenerated, traced, recoloured, or substituted from another icon family.
- The canonical decision-category contact sheet was inspected before individual canonical decision-category references, as required by the asset workflow.

## DDS validation

The final DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` from the processed 52x40 PNG.

| Field | Value |
| --- | --- |
| Runtime path | `gfx/interface/decisions/biowarfare/japan_china/decision_category_japan_biological_campaign.dds` |
| Dimensions | `52x40` |
| File length | `8448` bytes |
| Expected legacy BGRA length | `128 + (52 * 40 * 4) = 8448` bytes |
| DDS header size | `124` |
| Pixel-format size | `32` |
| Pixel-format flags | `65` (`RGB | ALPHAPIXELS`) |
| FourCC | `00000000` |
| Bit count | `32` |
| Masks | `R=0x00FF0000`, `G=0x0000FF00`, `B=0x000000FF`, `A=0xFF000000` |
| Caps | `0x1000` (`DDSCAPS_TEXTURE`) |
| DDS alpha range | `0..255` |
| DDS SHA-256 | `d8fe58073ec62ba8cd8cb99db2a3b551d04640d80443ea0d51e0e962ed8d7b04` |
| Validation result | `PASS` |

The DDS is static with one frame and no mipmaps. The final texture is in the exact parent-provided runtime folder and does not touch `gfx/interface/military_raids`.
