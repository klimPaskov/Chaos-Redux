# Event 006 current shelf and index reconciliation after ASY Haydo, ASY Barsoum, and CHU v1/v2/v3 additions

Date: 2026-08-01

Role: `chaosx_documentation_curator`

Scope: documentation-only reconciliation of the current Event 006 portrait-shelf authority and related resume/source-of-truth references. Gameplay, localisation, GFX, DDS, source assets, manifests, and the event catalog workbook were outside this pass.

## Disposition

Event 006 remains **HOLD / PARTIAL** under the existing completion authority. The current physical shelf check is 78 original-size PNG masters in `docs/assets/006_independence_wave/portraits_generated_png/`. The parent-authorized current authority is 73 indexed rows, leaving five older physical PNGs outside that index (four ARX masters and the CHU Mirsaid master). The asset manifest remains an owner surface and is not edited here; this count does not admit any additional runtime consumer.

The CHU Karim Tinchurin package-local v3 prompt is retained at `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/prompts/karim_tinchurin_hoi4_repaint_v3.txt` with SHA-256 `c0c370e6346e79c6f3b1373e8b18754edaae3afcfa49be19d7a6bf74ffd435ba`. The v3 candidate passes identity/style/provenance under `subagent_handoffs/006_iw043_chu_bolgar_repaint_identity_style_audit_v95_2026_08_01.md` but remains **HOLD / evidence-only** for rights/date (`needs_user_review`); no DDS, `.gfx`, character, or content-attestation promotion is claimed. The earlier v2 candidate remains HOLD/evidence-only under v94.

The ASY Shamoun Hanne Haydo source/repaint evidence is retained under `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/`. The raw repaint is `repaints_raw/ASY_levies_guardianship_shamoun_hanne_haydo_hoi4_repaint_v1.png` (SHA-256 `99fbe008d7088f1306a1acad054f19a02104f6652e10f1f83834b3a147411fa5`), the deterministic candidate is `repaints_processed/ASY_levies_guardianship_shamoun_hanne_haydo_156x210_candidate_v1.png` (SHA-256 `d3e66f378858e9f704d601124b52d4b3d3cf0b75781c9414ba989da930f40b2b`), and the prompt is `prompts/ASY_levies_guardianship_shamoun_hanne_haydo_hoi4_repaint_v1.txt` (SHA-256 `470d76877d092ee56723aea896963e4f810a7f3c5b0aa2842faeb3fc2b8ccfa1`). The v92 audit passes visual likeness, HOI4 style, and provenance, but rights/date remains HOLD (`needs_user_review`); no DDS, `.gfx`, character, or content-attestation promotion is claimed.

The ASY Barsoum v2 evidence package is retained under `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/`. Its raw repaint is `repaints_raw/ASY_concordat_council_ignatius_afram_barsoum_hoi4_repaint_v1.png` (SHA-256 `8b0251b0638340ef85fe4610efd2cafa70b561e6297490dcd07cac8d2707ef35`), its deterministic candidate is `repaints_processed/ASY_concordat_council_ignatius_afram_barsoum_156x210_candidate_v1.png` (SHA-256 `220e81c29b35963668bcc2de3d8340aec3047a74da6655fabcda07f26d59d595`), and its prompt is `prompts/ASY_concordat_council_ignatius_afram_barsoum_hoi4_repaint_v1.txt` (SHA-256 `0643f7f9cc1368a68607932205c4d9c8e159f5f4a1019e76070499487641590e`). It remains evidence-only pending independent identity/style/provenance audit and has no runtime admission.

## Files changed

- `docs/events/006_independence_wave/overview.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_documentation_curator_shelf_reconciliation_v95_2026_08_01.md`

The overview, resume packet, and source-of-truth map now use 78 physical masters and 73 indexed rows for current authority. Current CHU v3 audit evidence, ASY Haydo v92 audit evidence, and the ASY Barsoum evidence package are cross-referenced without changing the intended gameplay or asset gate. Dated historical counts, including the earlier 63-master and 68-entry records, remain unchanged for traceability.

## Reconciliation and dispositions

| Documentation surface | Disposition | Notes |
| --- | --- | --- |
| Current Event 006 overview authority | Updated | Current 78-PNG / 73-indexed shelf statement; CHU v3 PASS/HOLD, ASY Haydo v92 PASS/HOLD, and Barsoum evidence-only status are explicit. |
| Event 006 resume packet | Updated | Current authority and resume routing use 78/73; historical 63/68 records remain dated history. |
| Event 006 source-of-truth map | Updated | Current allocator, static visual package, and portrait-shelf authority use 78/73; current candidate gate status is explicit. |
| CHU v3 package/audit | Left unchanged | Prompt evidence and v95 identity/style/provenance PASS are linked from current docs; rights/date remains HOLD and no runtime admission is inferred. |
| ASY Haydo package/source handoff | Left unchanged | v92 identity/style/provenance PASS and rights/date HOLD are recorded; no admission is inferred. |
| ASY Barsoum v2 package/source handoff | Left unchanged | New evidence package is linked from current docs; independent audit and runtime admission remain open. |
| Asset manifests and README files | Left unchanged | They are asset-owner surfaces and were outside this documentation-only pass. |

## Validation and unresolved risks

- Direct shelf inspection found 78 `.png` files and 81 total files in `portraits_generated_png/` (the remainder are documentation files).
- Targeted searches confirmed current references to 78, 73, the CHU v3 prompt path/hash, the ASY Haydo audit, and the ASY Barsoum evidence package in the three authority documents; stale current 75/76/77 wording was removed from those surfaces.
- Historical 63/68 references remain intentionally present where their dates and supersession context are explicit.
- `PRE_RESIZE_MANIFEST.md` still describes its own 72-row historical index and 77-file physical snapshot; the parent-authorized current authority is 73 indexed rows and 78 physical PNGs after the Barsoum shelf copy. The asset manifest was not edited, and the snapshot drift remains an asset-owner follow-up.
- The v95 CHU audit records identity/style/provenance PASS with rights/date HOLD; no DDS or runtime admission is inferred.
- The v92 ASY Haydo audit records identity/style/provenance PASS with rights/date HOLD; no DDS or runtime admission is inferred.
- The ASY Barsoum v2 package is evidence-only pending an independent audit; no audit result or runtime promotion is claimed.
- No runtime, save/load, live game, DDS, GFX, localisation, gameplay, or workbook validation was performed because those surfaces are outside this curator scope and require their owning agents or the parent.

## Parent decisions and next actions

1. Keep the parent-authorized 73 indexed-row count as current authority unless the asset owner reconciles the manifest's 72-row/77-file snapshot against the current 78-file shelf.
2. Keep CHU v3 and ASY Haydo blocked on their rights/date HOLDs before any DDS, `.gfx`, character, or attestation work.
3. Route ASY Barsoum v2 to an independent likeness/style/provenance audit before any runtime promotion; do not infer admission from shelf presence or the clearer source rights record.

## Post-audit addendum (2026-08-02)

The requested audit is now recorded in `006_iw058_asy_barsoum_pd1923_portrait_visual_audit_v93_2026_08_02.md` (commit `eaa0b6789`). Identity/likeness, HOI4 style/framing, provenance, and the PD-1923/1921 rights/date basis pass with the documented low-resolution group-photo caveat; parent follow-up v94 promotes only the existing concordat-council DDS consumer. No GFX/character/localisation/advisor/small-portrait promotion occurred, so the shelf remains reference-only and IW-058 remains outside attestation.
