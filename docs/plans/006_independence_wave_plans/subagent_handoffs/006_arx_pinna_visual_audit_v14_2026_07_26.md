# Event 006 ARX Pietro Pinna Parpaglia visual and provenance audit v14

Date: 2026-07-26.

Auditor scope: candidate-only visual and provenance review.

Overall disposition: **BLOCKED / evidence-only; do not convert to DDS, edit GFX or gameplay, or promote ARX.**

The candidate was reviewed independently from the producer package at native size and enlarged inspection scale using the unchanged source, exact crop, raw ImageGen repaint, deterministic candidate, processor sheet, and the country-leader reference family.

## Evidence inspected

- Unchanged primary source: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_26/arx_pinna_crown_v1/source/ARX/Img024PPP.jpg`.
- Corroborating source only: `source/ARX/Pietro_Pinna_Parpaglia_source.jpg`.
- Exact crop: `crops/ARX/Pietro_Pinna_Parpaglia_archival_crop_final.png`.
- Exact-crop equality record: `metadata/ARX/Pietro_Pinna_Parpaglia_archival_crop_final.json`.
- Raw source-locked ImageGen repaint: `repaints/ARX/Pietro_Pinna_Parpaglia_identity_preserve_imagegen.png`.
- Deterministic candidate: `processed/ARX/Pietro_Pinna_Parpaglia_156x210.png`.
- Processor metadata: `processed/ARX/Pietro_Pinna_Parpaglia_156x210.png.json`.
- Processor review sheet: `review/Pietro_Pinna_Parpaglia_processor_review.png`.
- The requested `portraits/country_leader_large/` directory is absent in this checkout.
- The actual canonical country-leader family `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and the male-only quick-reference pack `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/` were inspected instead.
- The processor metadata selects canonical `den_thorvald_stauning.png` and `fin_carl_mannerheim.png` as style references, and the full canonical leader contact sheet was also reviewed.

## Separate verdicts

| Gate | Verdict | Independent finding |
| --- | --- | --- |
| Unchanged source and source identity | **PASS** | `Img024PPP.jpg` is a single adult male in a period Regia Aeronautica uniform and cap; the source-visible cigarette, downward gaze, cap silhouette, facial planes, and medals are usable identity anchors. The full source also contains palms, a cheetah, and border/scan artifacts that are not part of the portrait candidate. |
| Exact head-and-shoulders crop | **PASS** | The final crop is `850x1150` from `(600,900,1450,2050)`. The retained Pillow JSON reports `decoded_pixels_equal = true`, with matching decoded RGBA hash `5d329f8e948041a770319a09d9c2addbdbf7854aa3496fd698261d545d74d303`. A direct Pillow comparison reproduced the same equality. |
| Male-only compliance | **PASS** | The crop, raw repaint, and `156x210` candidate contain one male subject only; no woman, extra person, or opposite-gender substitution is present. |
| Identity preservation / likeness | **PASS, bounded** | The raw repaint and native candidate preserve the dominant source-specific cap, head angle/downward gaze, nose and jaw relationship, cigarette position, dark hairline, and uniform posture. No clear generic face, beautification, frontalization, or face substitution was observed. Source facial detail is partly shadowed by the cap, so this is a bounded visual PASS and not permission to relax the separate identity gate. |
| Unsupported clothing or insignia | **NEEDS_USER_REVIEW** | The repaint retains the source uniform concept and chest decorations, but makes shoulder marks and the medal block more legible than the source. Before any future admission, confirm that every visible rank/medal detail is source-supported and remove any invented insignia. |
| HOI4 country-leader painted style | **PASS, bounded** | The raw repaint uses subdued oil/gouache texture, a quiet dark teal-grey background, controlled contrast, readable facial planes, and a full head-and-shoulders composition consistent with the canonical `156x210` leader family. The candidate is darker than some pale-background references but remains in-family. |
| Native portrait canvas and framing | **PASS** | The deterministic output is opaque RGBA `156x210`, with the cap and both shoulders retained, no dossier frame, no `_small` crop, and no clipped face. Alpha range is `255..255`, which is appropriate for a full leader portrait. |
| Watermark, text, and scene cleanup | **PASS** | No readable watermark, text, UI, palm scenery, cheetah, border, or extra scene element remains in the raw repaint or processed candidate. The corroborating `642x483` source has a visible watermark and was not used as the processing master. |
| Source rights and attribution | **PASS, bounded** | The package manifest records the primary `Img024PPP.jpg` Commons source as uploader C. E. Pinna P., CC BY-SA 4.0, with attribution and share-alike required. The separate corroborating source is recorded as a PD-Italy/PD-1996 Commons copy and is not the processing master. Keep these two source records distinct and retain the CC BY-SA attribution on any later use. |
| Crown/consultative-council role fit | **PARTIAL; FAIL under strict dynastic reading** | Pinna Parpaglia is a Sardinian-born Italian air general and later High Commissioner for Sardinia, which supports a crown-appointed Sardinian military-administrative interpretation. The evidence does not make him a Savoy dynast or a documented 1936 crown-council officeholder. The parent must not silently treat this general as a dynastic officeholder. |
| Exact identity ownership / collision | **BLOCKED / FAIL** | Kaiserreich owns the exact person as `SRD_pietro_pinna_parpaglia` in `common/characters/SRD characters.txt:976-986`, recruits him in `history/countries/SRD - Sardinia.txt:225`, localises him in `localisation/english/KR_country_specific/SRD - Sardinia l_english.yml:689-690`, and portrait-owns him through `interface/kaiserreich/portraits/SRD_portraits.gfx:255-256` and `gfx/interface/advisors/SRD/SRD_pietro_pinna_parpaglia.png`. No guarded transfer or availability contract exists, so cloning this grounded identity into ARX is disallowed even though ARX would use a different civilian-large surface. |
| Runtime consumer boundary | **BLOCKED / unchanged** | The intended ARX consumer would be `ARX_sardinian_crown_consultative_council`, visible name key `ARX_vittorio_pala`, civilian-large sprite `GFX_portrait_ARX_independence_wave_vittorio_pala`, and existing runtime DDS `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_vittorio_pala.dds`. This audit does not replace that identity, create a Pinna DDS, edit `.gfx`, or change character history. |

## Hash and dimension record

| Artifact | Dimensions / mode | SHA-256 |
| --- | --- | --- |
| `source/ARX/Img024PPP.jpg` | `2477x3500` RGB | `8588dcb39daf1e5840542fef851065763c2613931aadb74fd4ea867d27c115de` |
| `crops/ARX/Pietro_Pinna_Parpaglia_archival_crop_final.png` | `850x1150` RGB | `fb7772ece050292a2b85a7e79adf600aebb327b85703948bb83dc222bd25d8e2` |
| `metadata/ARX/Pietro_Pinna_Parpaglia_archival_crop_final.json` | crop schema JSON | `32a4976cd67d0dd967faad4ab6882f75511b8413adf407ee36ef59fad8e84ec2` |
| `repaints/ARX/Pietro_Pinna_Parpaglia_identity_preserve_imagegen.png` | `1082x1454` RGB | `194c2938f5d2772954347a8dd26f5962eb4bcdfe8f5f2dfdd70e11f20cfaec50` |
| `processed/ARX/Pietro_Pinna_Parpaglia_156x210.png` | `156x210` RGBA | `a0429c75ebf0b575668dbcdfb7aa45a2576b85e6aa4f6fb80e6c04ca11343b2f` |
| `processed/ARX/Pietro_Pinna_Parpaglia_156x210.png.json` | processor metadata JSON | `3f44758aa45bfcc6d143caf212a5c83d2f6a974193fb0632c2f59954a06801c0` |
| `review/Pietro_Pinna_Parpaglia_processor_review.png` | `1344x464` RGBA | `bdf8f56cb72b5474699e04534916d2f3576ec8b8d42ddb392855d9eb97f12a7f` |
| canonical leader contact sheet | `8966ae351d1fe8fc13d47ca1c59ec3d8a34da9101ce5fd65f7acff3421bd0401` | reference-only |
| quick-reference leader contact sheet | `bf1ac6a6ed7f1d91b3fa8e4069c7b9f396bb63f450af1fe340005f7981a3cb60` | reference-only |

## Final handoff

The candidate is visually plausible as a male `156x210` HOI4 country-leader portrait, with bounded PASS results for source identity, exact crop, male-only presentation, framing, style, and cleanup.

Those visual results do not overcome the exact Kaiserreich owner collision or the unresolved strict crown/dynastic role contract.

Keep the asset status `candidate_requires_visual_approval` and the package status blocked.

Do not create a DDS, add a new sprite, change `ARX_sardinian_crown_consultative_council`, transfer the Kaiserreich character, or use a generic/fallback identity from this handoff.

If the parent later pursues this identity, it needs an explicit cross-mod transfer/availability design decision, a confirmed crown-role interpretation, a fresh owner/package audit, and a repeat independent visual review after any source, repaint, crop, or processor change.
