# Event 006 BRI regionalist — Régis de l'Estourbeillon v3 visual/provenance audit

Date: 2026-07-22  
Scope: read-only independent audit of the retained John Wickens 1904 source, v2 and v3 identity-preserving ImageGen edits, v3 processed portrait, comparison evidence, prompt, manifest, hashes, and male country-leader references.  
No asset, DDS, GFX, gameplay, localisation, manifest, or producer handoff was edited.  

## Verdict

**NEEDS_USER_REVIEW (not blocked).** The v3 visual/provenance gate passes on this
independent review: it remains recognisably the same sourced male, uses an
explicit 156x210 head-and-shoulders crop, and is visibly a muted full-color
HOI4-painted treatment rather than a raw photograph or simple sepia conversion.
A valid v3 DDS is now present both in the temporary package and at the intended
runtime path, but this audit did not create or edit either file. The parent still
needs to reconcile the manifest's older deferred-conversion wording and perform
the final direct acceptance/wiring review before marking the portrait complete.

## Evidence and hashes

All entries listed in the package `sha256sums.txt` were recomputed with SHA-256;
every listed hash matched, including the unchanged source copy.

Package root for the relative paths in the table is the exact directory
`docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/`.

| Evidence | Native size / mode | SHA-256 |
| --- | --- | --- |
| `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_john_wickens_1904_source_master.jpg` | 1145x1707 RGB JPEG | `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D` |
| `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png` (v2) | 1024x1536 RGB PNG | `CAE505FFA05FBEE59360FAB7993062078482F01142F83F061A73193EB7953FF7` |
| `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon.png` (v2) | 156x210 RGB PNG | `BDEDCCB06A25807C70A774871607AE72DA4F9A51B711E88E45F1E389A99500C8` |
| `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master_v3.png` | 1082x1454 RGB PNG | `660E954102CC6DF902792E84D0B0F97F178351476485A008362E64A1610E8120` |
| `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon_v3.png` | 156x210 RGB PNG | `5426E39BC1622E7ECD32A41CC0A1C05D6596446A40FA0B7BA2047EF350BBAE80` |
| `final_dds/BRI/portrait_BRI_independence_wave_civic_commission.dds` (temporary package artifact observed during audit) | 156x210 legacy BGRA DDS, 131168 bytes | `583F821ED7F8B78A89321DBB7E1E7B7CAD7E30829DFA5DD14B6F255E42E27DC0` |
| `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` (runtime artifact observed during audit) | 156x210 legacy BGRA DDS, 131168 bytes | `583F821ED7F8B78A89321DBB7E1E7B7CAD7E30829DFA5DD14B6F255E42E27DC0` |
| `contact_sheets/bri_regionalist_v3_comparison.png` | 1368x980 RGB PNG | `2184DA3B7B898035BBBF73DC59460CA4C54E1679EF6BEEA3A6889631C23A486D` |
| `contact_sheets/bri_regionalist_identity_review.png` | 1032x980 RGB PNG | `01069C9BA6750562F909222115C071052F84D1C285B7B84BBA0FC3F6D8A00329` |
| `prompt.md` | UTF-8 prompt record | `5AB0022BFDA9F214CCBE3DCEB17564AAD168526FD92C433C62E3CCAE57AAC2D` |
| `manifest.md` | package manifest | `E45F1F88D6CD5C9554219AB81459AFD2CE6464EEB947A41EE0379E0A85595E1A` |
| `sha256sums.txt` | package hash list | `114E6929BE5D26EE3BE84F4ADE5E453B7D06BB872ED255EB4837E1455FA5D901` |

The v1 candidate is retained in the package but is not the selected v3 output:
`source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_candidate_v1.png`
(`8BE51C6A25E14BB93CE1996483F0E76CAB76B708118723091C998B49E454418B`).

## Independent gate results

| Gate | Result | Evidence |
| --- | --- | --- |
| Same-person likeness / no material face drift | **PASS** | Direct source/v2/v3 comparison shows the same male facial silhouette, brow/eyes and leftward gaze, nose, cheeks/jaw, ears, moustache, apparent age, expression, head angle, and proportions. The broad hat, trailing hat cloth, shoulder silhouette, and source-visible Breton costume remain. Differences read as restrained paint texture, edge cleanup, and color/lighting treatment; no material face replacement or genericisation was observed. |
| Male-only | **PASS** | Source subject and manifest identify Régis de l'Estourbeillon as a male civic/regionalist leader; all supplied leader style references are the male country-leader family. No female, second person, or gender-ambiguous substitute appears. |
| Source / era / role fit | **PASS** | The unchanged source is attributed to John Wickens, *A Book of Mad Celts* (1904), depicting the historical Breton regionalist in Breton national costume. The portrait has no modern props, postwar uniform, fantasy regalia, or invented cultural shorthand; the documented civic/regionalist role fits the BRI leader token. |
| Explicit head-and-shoulders crop | **PASS** | v3 processed PNG is exactly 156x210 and visibly keeps the complete hat, face, both shoulders, and source-supported upper-torso costume. It is not a dossier-size 65x67 crop. |
| Full-color restrained HOI4 finish | **PASS** | v3 is visibly RGB with muted skin, slate/charcoal costume, dull-metal highlights, and a quiet neutral painted background. Brush texture and softened photographic halftone are visible; the busy source background is replaced. It is not raw photography, monochrome, or merely a brown/sepia tint. |
| No invented costume/symbol/stereotype/fantasy detail | **PASS** | Comparison and prompt constraints show no text, watermark, UI, flag, medal, invented insignia, sacred/pseudo-Celtic motif, modern object, extra person, stereotype, or fantasy detail. The patterned chest panel and hat are source-visible and remain materially consistent. |
| Provenance / rights traceability | **PASS with retention note** | Manifest records the Commons source link, John Wickens attribution, 1904 date, Public Domain/PD basis, direct-original link, and an explicit caveat to preserve attribution rather than relying on the Commons tag alone. The unchanged source is retained byte-for-byte and hash-verified. Keep this attribution and caveat with durable Event 006 documentation. |
| Native-size readability | **PASS** | At 156x210 the face, moustache, gaze direction, hat silhouette, and shoulder/costume contrast remain legible. No text or small symbol is needed for recognition. |
| Runtime output | **OBSERVED / NEEDS_USER_REVIEW** | During the audit, a 131168-byte legacy BGRA DDS was present in both `final_dds/BRI/portrait_BRI_independence_wave_civic_commission.dds` and `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`, with identical SHA-256. Header checks pass: `DDS ` magic, header size 124, 156x210 dimensions, pixel format size 32/flags 65/fourCC 0/32-bit BGRA masks, `DDSCAPS_TEXTURE`, no mipmaps, exact length, and opaque alpha 255. Its decoded RGB payload is byte-identical to the v3 processed PNG. The audit did not create or edit these DDS files. The package manifest still states that DDS conversion was deferred, so the parent must reconcile that stale status and verify the existing `.gfx` registration before completion. |

## Reference review

The matching canonical country-leader family and male quick-reference pack were
inspected. The v3 comparison uses the following style-only references, all full
156x210 male country-leader textures; the quick-reference copies are byte-
identical to their canonical counterparts:

- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png` — `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6`
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/ire_eamon_de_valera.png` — `FF5F8689F1E8EA75BF88BEA4C4A87DCF60518B1E062EA53BE4A9CEFF3509DCB0`
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/afg_mohammed_zahir_shah.png` — `F606BC3C6204E0DBD35D8EDCEB21F87AE6F93A0AE7AD657382C7E9043E8907A0`
- Canonical family sheet: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` — `8966AE351D1FE8FC13D47CA1C59EC3D8A34DA9101CE5FD65F7ACFF3421BD0401`
- Male quick-reference sheet: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/contact_sheet.png` — `BF1AC6A6ED7F1D91B3FA8E4069C7B9F396BB63F450AF1FE340005F7981A3CB60`

The references were used only to judge quiet background, controlled value range,
head-and-shoulders framing, and restrained HOI4 paint. No reference face,
identity, clothing, insignia, or pose was copied into the Event 006 portrait.

## Parent action

Treat v3 as the accepted visual/provenance candidate pending the parent’s direct
review of the comparison sheet. If the parent sees any material face/gaze/nose/
moustache/jaw/age/hat/costume/pose drift, fail closed and leave the civic slot
blocked rather than using v2, the v1 candidate, the Dulac illustration, or a
generated substitute. If accepted, retain only the existing v3-derived DDS/runtime
mapping after the parent verifies it against the current `.gfx`; this audit did not
perform conversion or edit runtime files. The current package manifest's
"no DDS was created/deferred" note should be reconciled by the parent because a
matching v3 DDS is now present.
