# Event 006 Niche Country Flag Asset Handoff

Timestamp: 2026_06_05_144741 UTC

## Scope

Generated bounded country flag assets for the Event 006 Independence Wave generic niche country tranche requested by the parent:

- `ASN`: Asante Council / Asante
- `KBN`: Kanem-Bornu Authority / Kanem-Bornu
- `PLM`: Palmares Council / Palmares
- `AYM`: Aymara Highland Congress / Aymara

No gameplay, event, scripted effect, scripted trigger, focus, decision, localisation, country tag, country history, or spreadsheet files were edited.

## Output

- Variants per tag: base, democratic, communism, fascism, neutrality.
- Final flag sizes: 82x52, 41x26, 10x7.
- Final folders: `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`.
- Final formats: DDS plus TGA siblings. DDS was requested; TGA was also produced because existing Chaos Redux and vanilla country flags use TGA.
- Source and processed PNG previews: `docs/assets/006_independence_wave/flags/<tag>/`.
- Manifest: `docs/assets/006_independence_wave/flags/manifest.md`.
- Contact sheets: per-tag sheets and `docs/assets/006_independence_wave/flags/event006_niche_country_flags_contact_sheet.png`.

## Visual Notes

- `ASN`: original Asante-inspired stool/gold-weight motifs; no copied modern national flag.
- `KBN`: original Kanem-Bornu-inspired Sahel crescent, Lake Chad, and authority-standard motifs.
- `PLM`: original Palmares-inspired palm and palisade motifs; no text or modern movement insignia.
- `AYM`: original highland sun, mountain, terrace, and stepped-diamond motifs; avoids exact Wiphala reproduction.
- Ideology variants use different compositions and symbols, not mere recolors.
- Orientation checked through direct top-up SVG generation and contact sheets; no upside-down output observed.

## Conversion Commands

- `convert <generated.svg> PNG32:<source_png>`
- `convert <processed_png> -define dds:compression=none DDS:<final_dds>`
- `convert <processed_png> TGA:<final_tga>`
- `convert <source_png> -filter Lanczos -resize 10x7! PNG32:<processed_png>`
- `convert <source_png> -filter Lanczos -resize 41x26! PNG32:<processed_png>`
- `convert <source_png> -filter Lanczos -resize 82x52! PNG32:<processed_png>`
- `montage <processed_pngs> -tile ... <contact_sheet.png>`

## Created Files

- `docs/assets/006_independence_wave/flags/asn/contact_sheets/asn_flags_contact_sheet.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/large/ASN.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/large/ASN_communism.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/large/ASN_democratic.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/large/ASN_fascism.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/large/ASN_neutrality.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/medium/ASN.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/medium/ASN_communism.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/medium/ASN_democratic.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/medium/ASN_fascism.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/medium/ASN_neutrality.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/small/ASN.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/small/ASN_communism.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/small/ASN_democratic.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/small/ASN_fascism.png`
- `docs/assets/006_independence_wave/flags/asn/processed_png/small/ASN_neutrality.png`
- `docs/assets/006_independence_wave/flags/asn/source_png/ASN_communism_source.png`
- `docs/assets/006_independence_wave/flags/asn/source_png/ASN_democratic_source.png`
- `docs/assets/006_independence_wave/flags/asn/source_png/ASN_fascism_source.png`
- `docs/assets/006_independence_wave/flags/asn/source_png/ASN_neutrality_source.png`
- `docs/assets/006_independence_wave/flags/asn/source_png/ASN_source.png`
- `docs/assets/006_independence_wave/flags/aym/contact_sheets/aym_flags_contact_sheet.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/large/AYM.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/large/AYM_communism.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/large/AYM_democratic.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/large/AYM_fascism.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/large/AYM_neutrality.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/medium/AYM.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/medium/AYM_communism.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/medium/AYM_democratic.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/medium/AYM_fascism.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/medium/AYM_neutrality.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/small/AYM.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/small/AYM_communism.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/small/AYM_democratic.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/small/AYM_fascism.png`
- `docs/assets/006_independence_wave/flags/aym/processed_png/small/AYM_neutrality.png`
- `docs/assets/006_independence_wave/flags/aym/source_png/AYM_communism_source.png`
- `docs/assets/006_independence_wave/flags/aym/source_png/AYM_democratic_source.png`
- `docs/assets/006_independence_wave/flags/aym/source_png/AYM_fascism_source.png`
- `docs/assets/006_independence_wave/flags/aym/source_png/AYM_neutrality_source.png`
- `docs/assets/006_independence_wave/flags/aym/source_png/AYM_source.png`
- `docs/assets/006_independence_wave/flags/event006_niche_country_flags_contact_sheet.png`
- `docs/assets/006_independence_wave/flags/kbn/contact_sheets/kbn_flags_contact_sheet.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/large/KBN.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/large/KBN_communism.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/large/KBN_democratic.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/large/KBN_fascism.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/large/KBN_neutrality.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/medium/KBN.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/medium/KBN_communism.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/medium/KBN_democratic.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/medium/KBN_fascism.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/medium/KBN_neutrality.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/small/KBN.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/small/KBN_communism.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/small/KBN_democratic.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/small/KBN_fascism.png`
- `docs/assets/006_independence_wave/flags/kbn/processed_png/small/KBN_neutrality.png`
- `docs/assets/006_independence_wave/flags/kbn/source_png/KBN_communism_source.png`
- `docs/assets/006_independence_wave/flags/kbn/source_png/KBN_democratic_source.png`
- `docs/assets/006_independence_wave/flags/kbn/source_png/KBN_fascism_source.png`
- `docs/assets/006_independence_wave/flags/kbn/source_png/KBN_neutrality_source.png`
- `docs/assets/006_independence_wave/flags/kbn/source_png/KBN_source.png`
- `docs/assets/006_independence_wave/flags/manifest.md`
- `docs/assets/006_independence_wave/flags/plm/contact_sheets/plm_flags_contact_sheet.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/large/PLM.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/large/PLM_communism.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/large/PLM_democratic.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/large/PLM_fascism.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/large/PLM_neutrality.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/medium/PLM.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/medium/PLM_communism.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/medium/PLM_democratic.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/medium/PLM_fascism.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/medium/PLM_neutrality.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/small/PLM.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/small/PLM_communism.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/small/PLM_democratic.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/small/PLM_fascism.png`
- `docs/assets/006_independence_wave/flags/plm/processed_png/small/PLM_neutrality.png`
- `docs/assets/006_independence_wave/flags/plm/source_png/PLM_communism_source.png`
- `docs/assets/006_independence_wave/flags/plm/source_png/PLM_democratic_source.png`
- `docs/assets/006_independence_wave/flags/plm/source_png/PLM_fascism_source.png`
- `docs/assets/006_independence_wave/flags/plm/source_png/PLM_neutrality_source.png`
- `docs/assets/006_independence_wave/flags/plm/source_png/PLM_source.png`
- `gfx/flags/ASN.dds`
- `gfx/flags/ASN.tga`
- `gfx/flags/ASN_communism.dds`
- `gfx/flags/ASN_communism.tga`
- `gfx/flags/ASN_democratic.dds`
- `gfx/flags/ASN_democratic.tga`
- `gfx/flags/ASN_fascism.dds`
- `gfx/flags/ASN_fascism.tga`
- `gfx/flags/ASN_neutrality.dds`
- `gfx/flags/ASN_neutrality.tga`
- `gfx/flags/AYM.dds`
- `gfx/flags/AYM.tga`
- `gfx/flags/AYM_communism.dds`
- `gfx/flags/AYM_communism.tga`
- `gfx/flags/AYM_democratic.dds`
- `gfx/flags/AYM_democratic.tga`
- `gfx/flags/AYM_fascism.dds`
- `gfx/flags/AYM_fascism.tga`
- `gfx/flags/AYM_neutrality.dds`
- `gfx/flags/AYM_neutrality.tga`
- `gfx/flags/KBN.dds`
- `gfx/flags/KBN.tga`
- `gfx/flags/KBN_communism.dds`
- `gfx/flags/KBN_communism.tga`
- `gfx/flags/KBN_democratic.dds`
- `gfx/flags/KBN_democratic.tga`
- `gfx/flags/KBN_fascism.dds`
- `gfx/flags/KBN_fascism.tga`
- `gfx/flags/KBN_neutrality.dds`
- `gfx/flags/KBN_neutrality.tga`
- `gfx/flags/PLM.dds`
- `gfx/flags/PLM.tga`
- `gfx/flags/PLM_communism.dds`
- `gfx/flags/PLM_communism.tga`
- `gfx/flags/PLM_democratic.dds`
- `gfx/flags/PLM_democratic.tga`
- `gfx/flags/PLM_fascism.dds`
- `gfx/flags/PLM_fascism.tga`
- `gfx/flags/PLM_neutrality.dds`
- `gfx/flags/PLM_neutrality.tga`
- `gfx/flags/medium/ASN.dds`
- `gfx/flags/medium/ASN.tga`
- `gfx/flags/medium/ASN_communism.dds`
- `gfx/flags/medium/ASN_communism.tga`
- `gfx/flags/medium/ASN_democratic.dds`
- `gfx/flags/medium/ASN_democratic.tga`
- `gfx/flags/medium/ASN_fascism.dds`
- `gfx/flags/medium/ASN_fascism.tga`
- `gfx/flags/medium/ASN_neutrality.dds`
- `gfx/flags/medium/ASN_neutrality.tga`
- `gfx/flags/medium/AYM.dds`
- `gfx/flags/medium/AYM.tga`
- `gfx/flags/medium/AYM_communism.dds`
- `gfx/flags/medium/AYM_communism.tga`
- `gfx/flags/medium/AYM_democratic.dds`
- `gfx/flags/medium/AYM_democratic.tga`
- `gfx/flags/medium/AYM_fascism.dds`
- `gfx/flags/medium/AYM_fascism.tga`
- `gfx/flags/medium/AYM_neutrality.dds`
- `gfx/flags/medium/AYM_neutrality.tga`
- `gfx/flags/medium/KBN.dds`
- `gfx/flags/medium/KBN.tga`
- `gfx/flags/medium/KBN_communism.dds`
- `gfx/flags/medium/KBN_communism.tga`
- `gfx/flags/medium/KBN_democratic.dds`
- `gfx/flags/medium/KBN_democratic.tga`
- `gfx/flags/medium/KBN_fascism.dds`
- `gfx/flags/medium/KBN_fascism.tga`
- `gfx/flags/medium/KBN_neutrality.dds`
- `gfx/flags/medium/KBN_neutrality.tga`
- `gfx/flags/medium/PLM.dds`
- `gfx/flags/medium/PLM.tga`
- `gfx/flags/medium/PLM_communism.dds`
- `gfx/flags/medium/PLM_communism.tga`
- `gfx/flags/medium/PLM_democratic.dds`
- `gfx/flags/medium/PLM_democratic.tga`
- `gfx/flags/medium/PLM_fascism.dds`
- `gfx/flags/medium/PLM_fascism.tga`
- `gfx/flags/medium/PLM_neutrality.dds`
- `gfx/flags/medium/PLM_neutrality.tga`
- `gfx/flags/small/ASN.dds`
- `gfx/flags/small/ASN.tga`
- `gfx/flags/small/ASN_communism.dds`
- `gfx/flags/small/ASN_communism.tga`
- `gfx/flags/small/ASN_democratic.dds`
- `gfx/flags/small/ASN_democratic.tga`
- `gfx/flags/small/ASN_fascism.dds`
- `gfx/flags/small/ASN_fascism.tga`
- `gfx/flags/small/ASN_neutrality.dds`
- `gfx/flags/small/ASN_neutrality.tga`
- `gfx/flags/small/AYM.dds`
- `gfx/flags/small/AYM.tga`
- `gfx/flags/small/AYM_communism.dds`
- `gfx/flags/small/AYM_communism.tga`
- `gfx/flags/small/AYM_democratic.dds`
- `gfx/flags/small/AYM_democratic.tga`
- `gfx/flags/small/AYM_fascism.dds`
- `gfx/flags/small/AYM_fascism.tga`
- `gfx/flags/small/AYM_neutrality.dds`
- `gfx/flags/small/AYM_neutrality.tga`
- `gfx/flags/small/KBN.dds`
- `gfx/flags/small/KBN.tga`
- `gfx/flags/small/KBN_communism.dds`
- `gfx/flags/small/KBN_communism.tga`
- `gfx/flags/small/KBN_democratic.dds`
- `gfx/flags/small/KBN_democratic.tga`
- `gfx/flags/small/KBN_fascism.dds`
- `gfx/flags/small/KBN_fascism.tga`
- `gfx/flags/small/KBN_neutrality.dds`
- `gfx/flags/small/KBN_neutrality.tga`
- `gfx/flags/small/PLM.dds`
- `gfx/flags/small/PLM.tga`
- `gfx/flags/small/PLM_communism.dds`
- `gfx/flags/small/PLM_communism.tga`
- `gfx/flags/small/PLM_democratic.dds`
- `gfx/flags/small/PLM_democratic.tga`
- `gfx/flags/small/PLM_fascism.dds`
- `gfx/flags/small/PLM_fascism.tga`
- `gfx/flags/small/PLM_neutrality.dds`
- `gfx/flags/small/PLM_neutrality.tga`

## Blockers

None for DDS conversion; ImageMagick DDS support was available and all final DDS files were written. No placeholder blank flags were created.
