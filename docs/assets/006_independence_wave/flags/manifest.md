# Event 006 Flag Manifest

Status: regenerated with imagegen, processed, converted, and wired.

This manifest records the 2026-06-08 Independence Wave flag regeneration pass. The pass uses imagegen-created raster flag art for the current custom Event 006 tags, then converts each tag into the HOI4 country-flag size set.

## Current Scope

The regenerated tags are:

- `ASN` - Asante Council
- `KBN` - Kanem-Bornu Authority
- `DFR` - Darfur Council
- `ZUL` - Zulu Council
- `PLM` - Palmares Council
- `AYM` - Aymara Highland Congress
- `MAP` - Mapuche Land Congress

Each tag has a unique generated flag identity. Ideology variants intentionally share that tag's generated country flag instead of inventing separate ideology banners in this tranche; the variants exist so vanilla HOI4 flag lookups resolve cleanly for democratic, communist, fascist, and neutrality governments.

## Processing Notes

- Source mode: imagegen raster artwork created for this pass.
- Visual policy: fictional, period-compatible symbolic flags; no readable text; no copied modern state flags.
- Target sizes: large `82x52`, medium `41x26`, small `10x7`.
- Final folders: `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Final formats: TGA and uncompressed DDS siblings for every base and ideology variant.
- Orientation: final TGAs were verified visually and checked so the TGA origin marker does not carry the `- top` flag. Processed PNGs and final TGAs compare as identical after decode.
- Contact sheet: `docs/assets/006_independence_wave/flags/regenerated_2026_06_08/contact_sheets/event006_regenerated_flags_large_contact.png`

## Asset Rows

| tag | source_png | processed_large | final_large | final_medium | final_small | notes |
| --- | --- | --- | --- | --- | --- | --- |
| `ASN` | `docs/assets/006_independence_wave/flags/asn/source_png/ASN_generated_2026_06_08_source.png` | `docs/assets/006_independence_wave/flags/asn/processed_png/large/ASN.png` | `gfx/flags/ASN.tga` / `gfx/flags/ASN.dds` | `gfx/flags/medium/ASN.tga` / `gfx/flags/medium/ASN.dds` | `gfx/flags/small/ASN.tga` / `gfx/flags/small/ASN.dds` | Golden stool, sun, and court-symbol language for the Asante story lane. |
| `KBN` | `docs/assets/006_independence_wave/flags/kbn/source_png/KBN_generated_2026_06_08_source.png` | `docs/assets/006_independence_wave/flags/kbn/processed_png/large/KBN.png` | `gfx/flags/KBN.tga` / `gfx/flags/KBN.dds` | `gfx/flags/medium/KBN.tga` / `gfx/flags/medium/KBN.dds` | `gfx/flags/small/KBN.tga` / `gfx/flags/small/KBN.dds` | Lake Chad, caravan, and Sahel authority motifs for Kanem-Bornu. |
| `DFR` | `docs/assets/006_independence_wave/flags/dfr/source_png/DFR_generated_2026_06_08_source.png` | `docs/assets/006_independence_wave/flags/dfr/processed_png/large/DFR.png` | `gfx/flags/DFR.tga` / `gfx/flags/DFR.dds` | `gfx/flags/medium/DFR.tga` / `gfx/flags/medium/DFR.dds` | `gfx/flags/small/DFR.tga` / `gfx/flags/small/DFR.dds` | Acacia, sun, and spear frontier motifs for Darfur. |
| `ZUL` | `docs/assets/006_independence_wave/flags/zul/source_png/ZUL_generated_2026_06_08_source.png` | `docs/assets/006_independence_wave/flags/zul/processed_png/large/ZUL.png` | `gfx/flags/ZUL.tga` / `gfx/flags/ZUL.dds` | `gfx/flags/medium/ZUL.tga` / `gfx/flags/medium/ZUL.dds` | `gfx/flags/small/ZUL.tga` / `gfx/flags/small/ZUL.dds` | Lion-mask, shield, and royal-house motifs for the Zulu story lane. |
| `PLM` | `docs/assets/006_independence_wave/flags/plm/source_png/PLM_generated_2026_06_08_source.png` | `docs/assets/006_independence_wave/flags/plm/processed_png/large/PLM.png` | `gfx/flags/PLM.tga` / `gfx/flags/PLM.dds` | `gfx/flags/medium/PLM.tga` / `gfx/flags/medium/PLM.dds` | `gfx/flags/small/PLM.tga` / `gfx/flags/small/PLM.dds` | Palm, palisade, and broken-chain motifs for Palmares. |
| `AYM` | `docs/assets/006_independence_wave/flags/aym/source_png/AYM_generated_2026_06_08_source.png` | `docs/assets/006_independence_wave/flags/aym/processed_png/large/AYM.png` | `gfx/flags/AYM.tga` / `gfx/flags/AYM.dds` | `gfx/flags/medium/AYM.tga` / `gfx/flags/medium/AYM.dds` | `gfx/flags/small/AYM.tga` / `gfx/flags/small/AYM.dds` | Condor, mountain, sun, and stepped highland motifs for Aymara. |
| `MAP` | `docs/assets/006_independence_wave/flags/map/source_png/MAP_generated_2026_06_08_source.png` | `docs/assets/006_independence_wave/flags/map/processed_png/large/MAP.png` | `gfx/flags/MAP.tga` / `gfx/flags/MAP.dds` | `gfx/flags/medium/MAP.tga` / `gfx/flags/medium/MAP.dds` | `gfx/flags/small/MAP.tga` / `gfx/flags/small/MAP.dds` | Drum, mountain, and river motifs for Mapuche. |

For every tag above, the same source identity is copied through the `_democratic`, `_communism`, `_fascism`, and `_neutrality` variants in all three HOI4 flag sizes.
