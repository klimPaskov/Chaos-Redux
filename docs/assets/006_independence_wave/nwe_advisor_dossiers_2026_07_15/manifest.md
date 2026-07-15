# Event 006 northern/western Europe advisor dossier manifest

Date: `2026-07-15`
Event: `006_independence_wave`
Asset tranche: RHI, BAY, SCO, and WLS institutional advisor dossiers
Source mode: official built-in ImageGen (`$imagegen`)
Disclosure: every depicted person is fictional
Current asset status: `installed_and_registered` (final DDS files and their dedicated `.gfx` registry are present)

## Asset contract

These are native HOI4 advisor assets, not leader portraits. ImageGen created twelve distinct full-resolution fictional portrait masters. Each final card then used its own explicit head-and-shoulders crop and `.tools/process_hoi4_portrait.py advisor`. The processor composed the crop with the separately generated frame and paper/seal overlays from `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/`, producing the `65x67` dark bevelled dossier card and transparent outer corners. No leader portrait was created, resized, padded, repurposed, or wired as an advisor.

Every generation used the three canonical leader portraits under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` as style/framing inputs only. Every processed candidate was compared at native size and at 5x nearest-neighbour size against all three canonical advisor references:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/generic_europe_1.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/generic_female_europe.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/generic_asia_1.png`

No generated portrait source contains text, labels, signatures, watermarks, logos, flags, medals, borders, dossier paper, or UI framing. The small paper marks visible in final cards come from the original ImageGen-authored reusable paper overlay; they are deliberately illegible archival marks, not generated readable text and not locally drawn primitives.

## Shared paths and fields

For every `<stem>` in the inventory:

- prompt record: `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/prompts/advisor_prompts.md`
- raw ImageGen master: `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/source_png/imagegen_raw/<stem>_imagegen_raw.png`
- processed native PNG: `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/processed_png/advisors/<stem>.png`
- processor crop metadata: `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/metadata/crops/<stem>.json`
- package DDS mirror: `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/final_dds/advisors/<stem>.dds`
- decoded verification PNG: `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/decoded_png/advisors/<stem>.png`
- installed runtime DDS: `gfx/interface/ideas/006_independence_wave/advisors/<stem>.dds`
- target size: `65x67`
- intended in-game use: `small` political-advisor portrait for the matching Event 006 country package
- source kind: `fictional`
- source mode: official built-in ImageGen
- registered `.gfx` file: `interface/006_independence_wave_nwe_advisors.gfx`
- related character file: `common/characters/006_independence_wave_nwe_advisors.txt`
- asset status: `handed_off`

## Inventory

| Stable stem | Institutional role | Apparent gender presentation | Explicit crop `[left, top, right, bottom]` | Source dimensions | Existing character/name key | Exact sprite handle |
| --- | --- | --- | --- | ---: | --- | --- |
| `advisor_RHI_independence_wave_municipal_customs_administrator` | RHI municipal/customs administrator | male-presenting | `[160, 50, 930, 1120]` | `1080x1457` | `RHI_independence_wave_municipal_customs_administrator` | `GFX_portrait_advisor_RHI_independence_wave_municipal_customs_administrator` |
| `advisor_RHI_independence_wave_rail_works_liaison` | RHI rail-and-works liaison | female-presenting | `[140, 40, 930, 1100]` | `1082x1454` | `RHI_independence_wave_rail_works_liaison` | `GFX_portrait_advisor_RHI_independence_wave_rail_works_liaison` |
| `advisor_RHI_independence_wave_river_defense_planner` | RHI river-defense planner | male-presenting | `[150, 60, 950, 1140]` | `1083x1452` | `RHI_independence_wave_river_defense_planner` | `GFX_portrait_advisor_RHI_independence_wave_river_defense_planner` |
| `advisor_BAY_independence_wave_district_finance_administrator` | BAY district finance administrator | female-presenting | `[150, 50, 930, 1150]` | `1077x1460` | `BAY_independence_wave_district_finance_administrator` | `GFX_portrait_advisor_BAY_independence_wave_district_finance_administrator` |
| `advisor_BAY_independence_wave_estates_constitutional_liaison` | BAY estates/constitutional liaison | male-presenting | `[210, 30, 1040, 1160]` | `1240x1269` | `BAY_independence_wave_estates_constitutional_liaison` | `GFX_portrait_advisor_BAY_independence_wave_estates_constitutional_liaison` |
| `advisor_BAY_independence_wave_alpine_supply_inspector` | BAY alpine supply inspector | female-presenting | `[150, 40, 970, 1130]` | `1107x1421` | `BAY_independence_wave_alpine_supply_inspector` | `GFX_portrait_advisor_BAY_independence_wave_alpine_supply_inspector` |
| `advisor_SCO_independence_wave_shipping_authority_commissioner` | SCO shipping authority commissioner | male-presenting | `[150, 45, 930, 1130]` | `1077x1460` | `SCO_independence_wave_shipping_authority_commissioner` | `GFX_portrait_advisor_SCO_independence_wave_shipping_authority_commissioner` |
| `advisor_SCO_independence_wave_industrial_reconstruction_secretary` | SCO industrial reconstruction secretary | female-presenting | `[110, 30, 970, 1140]` | `1078x1460` | `SCO_independence_wave_industrial_reconstruction_secretary` | `GFX_portrait_advisor_SCO_independence_wave_industrial_reconstruction_secretary` |
| `advisor_SCO_independence_wave_territorial_defense_planner` | SCO territorial defense planner | male-presenting | `[140, 35, 940, 1110]` | `1083x1452` | `SCO_independence_wave_territorial_defense_planner` | `GFX_portrait_advisor_SCO_independence_wave_territorial_defense_planner` |
| `advisor_WLS_independence_wave_bilingual_civil_service_commissioner` | WLS bilingual civil-service commissioner | female-presenting | `[150, 70, 930, 1180]` | `1075x1463` | `WLS_independence_wave_bilingual_civil_service_commissioner` | `GFX_portrait_advisor_WLS_independence_wave_bilingual_civil_service_commissioner` |
| `advisor_WLS_independence_wave_coal_rail_organizer` | WLS coal-and-rail organizer | male-presenting | `[140, 30, 980, 1100]` | `1119x1406` | `WLS_independence_wave_coal_rail_organizer` | `GFX_portrait_advisor_WLS_independence_wave_coal_rail_organizer` |
| `advisor_WLS_independence_wave_mountain_defense_planner` | WLS mountain-defense planner | female-presenting | `[130, 60, 950, 1160]` | `1083x1452` | `WLS_independence_wave_mountain_defense_planner` | `GFX_portrait_advisor_WLS_independence_wave_mountain_defense_planner` |

Gender presentation is deliberate implementation metadata. Later personal names must use the corresponding male or female name pool. None of these portraits may be assigned a name from the opposite pool.

## Review and validation evidence

- source overview: `contact_sheets/advisor_sources_contact_sheet.png`
- native `65x67` overview: `contact_sheets/advisor_portraits_native_contact_sheet.png`
- 5x nearest-neighbour overview: `contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`
- decoded-DDS overview: `contact_sheets/advisor_portraits_decoded_contact_sheet.png`
- processor comparisons: `contact_sheets/advisor_reviews/`
- per-asset comparisons against all three canonical advisor references: `contact_sheets/canonical_all_three/`
- consolidated crop and gender metadata: `metadata/advisor_identity_and_crop_metadata.json`
- machine-readable DDS, hash, distinctness, and decode validation: `advisor_validation_2026_07_15.json`
- review findings: `visual_review_notes.md`
- sprite registration handoff: `gfx_handoff.md`
- SHA-256 inventory: `checksums.sha256`

All twelve installed and package DDS files are uncompressed one-level `65x67` BGRA textures with alpha, exact length `17,548` bytes, valid legacy headers, and pixel-identical decoded output. Raw ImageGen hashes are all unique; processed PNG hashes are all unique; package and runtime DDS copies are byte-identical.

## Source and rights note

The characters are original fictional ImageGen output created for Chaos Redux. The three leader and three advisor reference images remain skill-local vanilla review assets only and are not copied or shipped as final Chaos Redux art.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none.
- Reused leader art: none.
- Transform-only fake styling: none.
- Generic fallback art: none.
- Rejected or blocked final advisors: none; all twelve first selected masters met the required restrained dossier style after native and canonical comparison.
- Gameplay, localisation, `.gfx`, GUI, event, focus, idea, decision, history, package, or spreadsheet edits: none.
- Parent integration complete: all twelve exact sprite definitions from `gfx_handoff.md` are registered in `interface/006_independence_wave_nwe_advisors.gfx`.
