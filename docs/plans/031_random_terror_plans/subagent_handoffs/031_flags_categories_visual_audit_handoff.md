# Event 31 flag and decision-category visual audit handoff

Audit date: 2026-09-01.

Scope: the 37 assigned Event 31 fictional flag designs and their 111 runtime TGA variants, plus the three 114x101 Event 31 decision-category pictures.

Disposition: the assigned visuals pass the asset-level audit and need no regeneration or pixel repair. Runtime filenames and category-picture DDS files were not changed. The only additions are decoded flag roundtrip evidence and this audit record.

## Reference and inspection basis

The flag family was compared against the canonical vanilla reference set under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags`, including the normal, medium, and small tiers.

The decision-category family was compared against the canonical 114x101 full-canvas references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures`.

Every final flag was opened individually at native dimensions and at enlarged nearest-neighbour scale: 37 normal 82x52 files, 37 medium 41x26 files, and 37 small 10x7 files.

Each category picture was opened individually as source PNG, processed PNG, and decoded DDS roundtrip at native 114x101 and enlarged 684x606 scale.

The flags are flat, opaque, fictional identities with no sacred or real extremist symbols, readable text, watermark, fabric treatment, perspective, or scene background. The category pictures are opaque, warm period-documentary compositions with edge-to-edge crop, clear focal hierarchy, and no readable text, watermark, modern prop, personified supernatural entity, sacred imagery, religious writing, or gore.

## Per-file flag disposition

Each row names the exact three runtime files inspected for that design. `PASS_VISUAL` means the normal and medium emblems are centered and clean and the small 10x7 version retains a recognizable high-contrast identity cue. `NEEDS_USER_REVIEW_IDENTITY` is not a visual failure; it records that the provisional basename-to-cosmetic-tag mapping remains parent-owned and was not inspected by this bounded asset pass.

| Design basename | Exact runtime files | Native family and alpha result | 10x7 readability note | Disposition |
|---|---|---|---|---|
| `event31_dormant_carrier_01` | `gfx/flags/event31_dormant_carrier_01.tga`; `gfx/flags/medium/event31_dormant_carrier_01.tga`; `gfx/flags/small/event31_dormant_carrier_01.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central cross-and-field cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_dormant_carrier_02` | `gfx/flags/event31_dormant_carrier_02.tga`; `gfx/flags/medium/event31_dormant_carrier_02.tga`; `gfx/flags/small/event31_dormant_carrier_02.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Lattice merges at 10x7 but the bright central structure survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_dormant_carrier_03` | `gfx/flags/event31_dormant_carrier_03.tga`; `gfx/flags/medium/event31_dormant_carrier_03.tga`; `gfx/flags/small/event31_dormant_carrier_03.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Ring-and-center cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_dormant_carrier_04` | `gfx/flags/event31_dormant_carrier_04.tga`; `gfx/flags/medium/event31_dormant_carrier_04.tga`; `gfx/flags/small/event31_dormant_carrier_04.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Gate-like central silhouette survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_dormant_carrier_05` | `gfx/flags/event31_dormant_carrier_05.tga`; `gfx/flags/medium/event31_dormant_carrier_05.tga`; `gfx/flags/small/event31_dormant_carrier_05.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Contrasting central mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_dormant_carrier_06` | `gfx/flags/event31_dormant_carrier_06.tga`; `gfx/flags/medium/event31_dormant_carrier_06.tga`; `gfx/flags/small/event31_dormant_carrier_06.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Split-field cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_dormant_carrier_07` | `gfx/flags/event31_dormant_carrier_07.tga`; `gfx/flags/medium/event31_dormant_carrier_07.tga`; `gfx/flags/small/event31_dormant_carrier_07.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central bar-and-field cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_dormant_carrier_08` | `gfx/flags/event31_dormant_carrier_08.tga`; `gfx/flags/medium/event31_dormant_carrier_08.tga`; `gfx/flags/small/event31_dormant_carrier_08.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central diamond cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_09` | `gfx/flags/event31_ordinary_actor_09.tga`; `gfx/flags/medium/event31_ordinary_actor_09.tga`; `gfx/flags/small/event31_ordinary_actor_09.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Strong central chevron survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_10` | `gfx/flags/event31_ordinary_actor_10.tga`; `gfx/flags/medium/event31_ordinary_actor_10.tga`; `gfx/flags/small/event31_ordinary_actor_10.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Crossed central bars survive | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_11` | `gfx/flags/event31_ordinary_actor_11.tga`; `gfx/flags/medium/event31_ordinary_actor_11.tga`; `gfx/flags/small/event31_ordinary_actor_11.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Fine center detail merges but color blocks remain distinct | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_12` | `gfx/flags/event31_ordinary_actor_12.tga`; `gfx/flags/medium/event31_ordinary_actor_12.tga`; `gfx/flags/small/event31_ordinary_actor_12.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central vertical mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_13` | `gfx/flags/event31_ordinary_actor_13.tga`; `gfx/flags/medium/event31_ordinary_actor_13.tga`; `gfx/flags/small/event31_ordinary_actor_13.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Fine center detail merges but the high-contrast center survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_14` | `gfx/flags/event31_ordinary_actor_14.tga`; `gfx/flags/medium/event31_ordinary_actor_14.tga`; `gfx/flags/small/event31_ordinary_actor_14.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central ring/mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_15` | `gfx/flags/event31_ordinary_actor_15.tga`; `gfx/flags/medium/event31_ordinary_actor_15.tga`; `gfx/flags/small/event31_ordinary_actor_15.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Bright central chevron survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_16` | `gfx/flags/event31_ordinary_actor_16.tga`; `gfx/flags/medium/event31_ordinary_actor_16.tga`; `gfx/flags/small/event31_ordinary_actor_16.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central diamond-and-field cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_17` | `gfx/flags/event31_ordinary_actor_17.tga`; `gfx/flags/medium/event31_ordinary_actor_17.tga`; `gfx/flags/small/event31_ordinary_actor_17.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Centered forked mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_18` | `gfx/flags/event31_ordinary_actor_18.tga`; `gfx/flags/medium/event31_ordinary_actor_18.tga`; `gfx/flags/small/event31_ordinary_actor_18.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central stepped mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_19` | `gfx/flags/event31_ordinary_actor_19.tga`; `gfx/flags/medium/event31_ordinary_actor_19.tga`; `gfx/flags/small/event31_ordinary_actor_19.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central opposing bars survive | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_20` | `gfx/flags/event31_ordinary_actor_20.tga`; `gfx/flags/medium/event31_ordinary_actor_20.tga`; `gfx/flags/small/event31_ordinary_actor_20.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central framed mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_21` | `gfx/flags/event31_ordinary_actor_21.tga`; `gfx/flags/medium/event31_ordinary_actor_21.tga`; `gfx/flags/small/event31_ordinary_actor_21.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Split chevron cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_22` | `gfx/flags/event31_ordinary_actor_22.tga`; `gfx/flags/medium/event31_ordinary_actor_22.tga`; `gfx/flags/small/event31_ordinary_actor_22.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central spoke cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_23` | `gfx/flags/event31_ordinary_actor_23.tga`; `gfx/flags/medium/event31_ordinary_actor_23.tga`; `gfx/flags/small/event31_ordinary_actor_23.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central vertical emblem survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_ordinary_actor_24` | `gfx/flags/event31_ordinary_actor_24.tga`; `gfx/flags/medium/event31_ordinary_actor_24.tga`; `gfx/flags/small/event31_ordinary_actor_24.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Arches merge at 10x7 but the paired center blocks survive | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_01` | `gfx/flags/event31_jihadist_route_01.tga`; `gfx/flags/medium/event31_jihadist_route_01.tga`; `gfx/flags/small/event31_jihadist_route_01.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Network detail merges but the high-contrast node pattern survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_02` | `gfx/flags/event31_jihadist_route_02.tga`; `gfx/flags/medium/event31_jihadist_route_02.tga`; `gfx/flags/small/event31_jihadist_route_02.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central angular cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_03` | `gfx/flags/event31_jihadist_route_03.tga`; `gfx/flags/medium/event31_jihadist_route_03.tga`; `gfx/flags/small/event31_jihadist_route_03.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central split-bar cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_04` | `gfx/flags/event31_jihadist_route_04.tga`; `gfx/flags/medium/event31_jihadist_route_04.tga`; `gfx/flags/small/event31_jihadist_route_04.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central pointed mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_05` | `gfx/flags/event31_jihadist_route_05.tga`; `gfx/flags/medium/event31_jihadist_route_05.tga`; `gfx/flags/small/event31_jihadist_route_05.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Centered fork cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_06` | `gfx/flags/event31_jihadist_route_06.tga`; `gfx/flags/medium/event31_jihadist_route_06.tga`; `gfx/flags/small/event31_jihadist_route_06.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central block-and-line cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_07` | `gfx/flags/event31_jihadist_route_07.tga`; `gfx/flags/medium/event31_jihadist_route_07.tga`; `gfx/flags/small/event31_jihadist_route_07.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central chevron survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_jihadist_route_08` | `gfx/flags/event31_jihadist_route_08.tga`; `gfx/flags/medium/event31_jihadist_route_08.tga`; `gfx/flags/small/event31_jihadist_route_08.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central aperture-like mark survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_transnational_command_01` | `gfx/flags/event31_transnational_command_01.tga`; `gfx/flags/medium/event31_transnational_command_01.tga`; `gfx/flags/small/event31_transnational_command_01.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Node detail merges but the strong central network cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_transnational_command_02` | `gfx/flags/event31_transnational_command_02.tga`; `gfx/flags/medium/event31_transnational_command_02.tga`; `gfx/flags/small/event31_transnational_command_02.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central linked-bars cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_transnational_command_03` | `gfx/flags/event31_transnational_command_03.tga`; `gfx/flags/medium/event31_transnational_command_03.tga`; `gfx/flags/small/event31_transnational_command_03.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Central framed diamond survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_transnational_command_04` | `gfx/flags/event31_transnational_command_04.tga`; `gfx/flags/medium/event31_transnational_command_04.tga`; `gfx/flags/small/event31_transnational_command_04.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Centered opposing-chevron cue survives | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |
| `event31_false_revelation_final` | `gfx/flags/event31_false_revelation_final.tga`; `gfx/flags/medium/event31_false_revelation_final.tga`; `gfx/flags/small/event31_false_revelation_final.tga` | 82x52 / 41x26 / 10x7; opaque 24-bit TGA, no alpha | Aperture/prism cue remains distinct | PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY |

The small variants are deliberately reviewed at the actual 10x7 consumer size. Detail collapse in `event31_dormant_carrier_02`, `event31_ordinary_actor_11`, `event31_ordinary_actor_13`, `event31_ordinary_actor_24`, `event31_jihadist_route_01`, and `event31_transnational_command_01` is expected at this tier and does not produce a blank, transparent, or indistinguishable flag.

## Decision-category picture disposition

| Category | Source and processed evidence | Final DDS and roundtrip evidence | Native consumer composition | Disposition |
|---|---|---|---|---|
| Government response | `docs/assets/031_random_terror/category-assets/source_png/random_terror_government_response_category_source.png`; `docs/assets/031_random_terror/category-assets/processed_png/random_terror_government_response_category.png` | `gfx/interface/decisions/031_random_terror/random_terror_government_response_category.dds`; `docs/assets/031_random_terror/category-assets/roundtrip/random_terror_government_response_category_roundtrip.png` | Damaged period station/depot fills the 114x101 canvas; train and rubble establish the scene while civilians, relief, and security remain readable without a cropped focal subject | PASS_VISUAL; NEEDS_PARENT_GFX_WIRING_REVIEW |
| Actor command | `docs/assets/031_random_terror/category-assets/source_png/random_terror_actor_command_category_source.png`; `docs/assets/031_random_terror/category-assets/processed_png/random_terror_actor_command_category.png` | `gfx/interface/decisions/031_random_terror/random_terror_actor_command_category.dds`; `docs/assets/031_random_terror/category-assets/roundtrip/random_terror_actor_command_category_roundtrip.png` | Period command/machine-room scene fills the canvas; foreground table, maps, ledgers, and incidental personnel create the intended institutional hierarchy | PASS_VISUAL; NEEDS_PARENT_GFX_WIRING_REVIEW |
| False revelation | `docs/assets/031_random_terror/category-assets/source_png/random_terror_false_revelation_category_source.png`; `docs/assets/031_random_terror/category-assets/processed_png/random_terror_false_revelation_category.png` | `gfx/interface/decisions/031_random_terror/random_terror_false_revelation_category.dds`; `docs/assets/031_random_terror/category-assets/roundtrip/random_terror_false_revelation_category_roundtrip.png` | Ruined period communications interior fills the canvas; observers and tables frame the centered pale vertical phenomenon without turning it into a character or sacred icon | PASS_VISUAL; NEEDS_PARENT_GFX_WIRING_REVIEW |

All three category finals are opaque 114x101 uncompressed legacy BGRA DDS files. Their DDS roundtrips match the processed PNGs exactly, including the required channel order and alpha bytes.

## Evidence and validation

- `docs/assets/031_random_terror/flags/roundtrip/normal/` contains 37 decoded native 82x52 final-TGA PNGs.
- `docs/assets/031_random_terror/flags/roundtrip/medium/` contains 37 decoded native 41x26 final-TGA PNGs.
- `docs/assets/031_random_terror/flags/roundtrip/small/` contains 37 decoded native 10x7 final-TGA PNGs.
- All 111 flag TGAs decode as type 2, 24-bit, bottom-left-origin files with exact expected dimensions and lengths, and all 111 decoded pixel buffers equal their matching processed PNGs.
- All three category DDS files pass the 124-byte-header, 114x101, uncompressed BGRA mask, opaque-alpha, raw-length, and pixel-roundtrip checks.
- Existing source masters, processed masters, and contact sheets remain in `docs/assets/031_random_terror/flags/` and `docs/assets/031_random_terror/category-assets/`.
- The flag manifest and validation record now document the retained TGA roundtrip evidence.
- No ImageGen repair call was made because the audit found no concrete visual defect; existing generated source and prompt/provenance evidence remain untouched.

## Changed files

- Added 111 decoded flag roundtrip PNGs under `docs/assets/031_random_terror/flags/roundtrip/{normal,medium,small}/`.
- Updated `docs/assets/031_random_terror/flags/manifest.md` with roundtrip provenance and exact-match status.
- Updated `docs/assets/031_random_terror/flags/validation.txt` with roundtrip and visual-audit status.
- Added this handoff at `docs/plans/031_random_terror_plans/subagent_handoffs/031_flags_categories_visual_audit_handoff.md`.
- No runtime TGA or category DDS content was modified.
- No GFX, cosmetic-tag script, gameplay, localisation, spreadsheet, portrait, report/news/super-event, icon, faction-emblem, or animation file was modified.

## Exact blockers for the parent

1. The 37 `event31_*` basenames are provisional package identities. The parent must verify each basename against the exact Event 31 cosmetic tag mapping before treating the flag pool as fully wired. This audit did not inspect or edit the cosmetic-tag script by contract.
2. The parent must register the three category sprite names in the parent-owned decision-category GFX and verify the consuming decision categories. The expected sprite names are `GFX_decision_cat_picture_031_random_terror_government_response`, `GFX_decision_cat_picture_031_random_terror_actor_command`, and `GFX_decision_cat_picture_031_random_terror_false_revelation`.
3. The rejected source candidate `docs/assets/031_random_terror/flags/source_png/event31_ordinary_actor_25_source.png` remains excluded from runtime and must not be wired as a fourth ordinary-actor flag.

No visual simplification or fallback was used. The package is complete at the assigned visual-audit boundary and remains pending only the parent-owned identity and GFX integration checks above.
