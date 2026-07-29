# Event 006 CHU Galimzhan Ibrahimov independent portrait audit

Date: 2026-07-28.

> Superseded portrait snapshot. This v1 audit remains provenance and visual
> traceability for the rejected v1 repaint. The current federal-presidium
> consumer uses the independently audited v2 candidate and the parent-promoted
> DDS recorded in `006_galimzhan_portrait_v2_runtime_promotion_2026_07_28.md`.

Reviewer: independent sourced-visual audit subagent, separate from the repaint producer.

Scope: archival source master, exact source crop and equality JSON, raw ImageGen repaint, flat-shelf raw copy, deterministic `156x210` candidate, processor metadata, review sheet, and canonical vanilla country-leader references. No source art, PNG, DDS, `.gfx`, gameplay, localisation, character, or runtime file was edited, staged, or replaced by this audit.

## Disposition

Visual likeness and HOI4 leader-style gates **PASS**. The candidate is visually suitable for the Galimzhan Ibrahimov federal-presidium consumer, subject to the provenance-record hold below.

DDS conversion and runtime wiring are **not permitted from this audit state**. The source-rights chain is documented, but the generated portrait package does not retain an exact ImageGen prompt or equivalent generation-record hash and its processor metadata has `portrait_provenance = null`. The parent may clear this documentation hold by retaining the exact prompt or a signed generation record, linking it to the immutable source/crop and updating the package manifest; no visual repaint change is required by this audit.

The flat-shelf rule is satisfied for the new shelf entry: the original-size RGB repaint master is present as a single flat-shelf copy under `docs/assets/006_independence_wave/portraits_generated_png/`, while the normalized candidate remains only in the portrait source-research package. No normalized `156x210` file is present in the flat shelf.

## Evidence reviewed

| Artifact | Path | Native facts / SHA-256 |
|---|---|---|
| Immutable archival source master | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/source_masters/volga/chu_galimzhan_ibrahimov.jpg` | JPEG grayscale `L`, `863x1272`, `344,829` bytes, `931a6dd35f70e2fd4fbd58aafd030d60a2755dc6a7dc68704b8267aefb864532`. |
| Exact source crop | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/source_crops/CHU_federal_presidium_galimzhan_ibrahimov_head_shoulders.png` | Lossless PNG grayscale `L`, `680x1040`, crop rectangle `(100,20,780,1060)`, `538,499` bytes, `accab14222f1154300ce9d6e36d101d11d0d59800172ec231c33468c88fbca75`. |
| Crop equality record | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/crop_metadata/CHU_federal_presidium_galimzhan_ibrahimov_crop.json` | `status = exact_source_crop_verified`, Pillow decoded-pixel equality `true`, matching master-crop/output RGBA equality hashes, and the recorded source hash. |
| Raw ImageGen repaint master | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_raw/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v1.png` | PNG RGB `1086x1448`, `2,252,321` bytes, `cc49f0c33d495d2a7a554b4d0548f3d5ce9f6ad5aa76dd150734441c312285dc`. |
| Flat-shelf raw copy | `docs/assets/006_independence_wave/portraits_generated_png/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v1.png` | PNG RGB `1086x1448`, `2,252,321` bytes, same SHA-256 `cc49f0c33d495d2a7a554b4d0548f3d5ce9f6ad5aa76dd150734441c312285dc`; byte-for-byte equal to the package raw master. |
| Deterministic candidate | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_processed/CHU_federal_presidium_galimzhan_ibrahimov_156x210_candidate.png` | PNG RGBA `156x210`, fully opaque alpha, `55,947` bytes, `9c5a8b273153c69acde1b23de5e0778235ea7f972de4f3cd4cafae2dbde261d2`. |
| Processing metadata | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/processing_metadata/CHU_federal_presidium_galimzhan_ibrahimov_156x210.json` | Processor `the retired portrait-processing utility` v5.0, processor SHA-256 `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`, `mode = leader`, `role_family = leader`, `source_kind = real`, candidate status `candidate_requires_visual_approval`. |
| Processor review sheet | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/review/CHU_federal_presidium_galimzhan_ibrahimov_processing_review.png` | RGBA PNG `1344x464`, `688,007` bytes, `c92e013bc1410d295599c7a5e3a66edcec0129159ddf0204d71bedef01f75afe`; shows the raw processor input, normalized candidate, and selected leader references. |
| Canonical style reference 1 | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png` | `156x210`; SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`. |
| Canonical style reference 2 | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png` | `156x210`; SHA-256 `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`. |

The processor metadata records the same two canonical leader references and does not include a frame, paper, advisor overlay, or generated institutional-emblem overlay.

## Gate verdicts

| Gate | Verdict | Independent finding |
|---|---|---|
| Archival source identity | **PASS** | The unchanged grayscale source is an attributed portrait of Galimzhan Ibrahimov, a Tatar writer, publicist, and politician who lived to 1938. It is the same immutable master used by the exact crop record and the prior source ledger. |
| Rights and source provenance | **PASS WITH RECORDED UNCERTAINTY** | The prior source ledger records the Commons file, Kazan State University library credit, 1920s estimate, unknown photographer, and Commons Public Domain Mark/PD-old basis. The original KSU page was unreachable during the source pass and the Commons upload history notes image-processing provenance, so those uncertainties must remain in the permanent handoff. The source bitstream itself was not altered. |
| Crop equality | **PASS** | The crop utility JSON reports `exact_source_crop_verified` and `decoded_pixels_equal = true` for `(100,20,780,1060)`. The crop hash and source hash match the prior source ledger. |
| Source-locked repaint chain | **PASS FOR ARTIFACT INTEGRITY** | The raw repaint is retained separately from the source and crop, and the flat-shelf copy is byte-for-byte equal to the package raw. The deterministic processor consumed only the raw repaint at the recorded full-canvas rectangle and produced the recorded `156x210` candidate. |
| Exact likeness | **PASS** | Native comparison of the archival master/crop, raw repaint, candidate, and review sheet preserves the broad brimmed hat and hat-band arc, three-quarter head angle, forehead and hair silhouette, unequal eye placement and gaze, long nose plane, compact moustache shape, cheek and jaw contour, ear exposure, collar/overcoat silhouette, and reserved expression. The raw colorizes and paints the halftone source, but no material face substitution, genericization, beautification, symmetrization, or opposite-person drift is visible. At `156x210`, the hat, eyes, nose, moustache, and coat remain readable. |
| Source-visible detail discipline | **PASS WITH MINOR INTERPRETIVE NOTE** | The raw repaint adds warm skin and sepia/olive toning to the grayscale source and smooths the halftone texture into painterly brushwork. These are permitted HOI4-family treatment choices. No unsupported Tatar/Soviet emblem, flag, medal, rank mark, text, watermark, modern prop, or hidden institutional insignia was added. |
| HOI4 country-leader style | **PASS** | The raw and candidate use a restrained painted finish, modeled facial planes, subdued warm-grey background, dark upper-bust clothing, and controlled vignette consistent with the canonical leader references `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`. The candidate is not a raw photograph, flat resize, card, dossier, or UI composition. |
| Framing and native canvas | **PASS** | The candidate is fully opaque RGBA `156x210`, centered on one male upper-bust subject with safe hat and shoulder margins, visible collar, and no frame or extra subject. The opaque canvas is consistent with the selected vanilla leader references. |
| Male and route-role fit | **PASS** | The source and repaint show one male subject. `common/characters/006_independence_wave_iw043_iw058_characters.txt:21-28` declares the existing federal-presidium character `gender = male` and the `civilian.large` sprite consumer. Current localisation names the consumer `Galimzhan Ibrahimov` and describes the Tatar federal-presidium role. |
| Stable consumer / ownership | **PASS FOR CONSUMER MAPPING** | `interface/006_independence_wave_iw043_iw058_portraits.gfx:15-16` already maps `GFX_portrait_CHU_independence_wave_federal_presidium` to `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds`; this audit does not edit that mapping. The prior source ownership scan found no competing vanilla or project character/portrait owner for Galimzhan Ibrahimov. |
| Forbidden derivatives | **PASS** | The candidate package contains no advisor, operative, high-command, dossier, `_small`, `50x67`, group, female, generic, or alternate-person derivative. No DDS exists in the candidate package and no runtime file was touched. |
| Prompt / generation-record completeness | **HOLD** | The package has the source-locked repaint plan and raw/candidate hashes, but no exact ImageGen prompt, prompt hash, or equivalent portrait-provenance manifest is retained. `processing_metadata.json` explicitly records `portrait_provenance = null`. The flat-shelf inventory row is useful generation evidence but does not replace the missing prompt/provenance record required for grounded real-person admission. |

## Likeness notes

The archival subject's distinctive silhouette is the strongest identity anchor and is preserved: a wide light felt hat with a dark curved band, dark wavy hair at the sides, a narrow moustache above a closed mouth, a long straight nose, a slightly turned head, and a heavy dark overcoat with a pointed collar.

The raw repaint keeps the source's head angle and asymmetric face readability instead of forcing a frontal or symmetrical studio pose. The eyes remain slightly unequal and the moustache remains compact and horizontal rather than becoming a generic full beard or modern facial-hair style.

The deterministic candidate loses some fine halftone and moustache detail at native size, as expected, but retains the features needed to distinguish Ibrahimov from a generic Volga civic leader. The candidate's lower coat is very dark, but the face and hat remain separated from the background and readable in the review sheet.

## Provenance and promotion blockers

1. The exact ImageGen prompt or a reproducible generation record is missing from the package. The source-locked repaint plan documents the intended constraints but is not an exact prompt payload or prompt hash.
2. `processing_metadata.json` leaves `portrait_provenance` null. The parent should add a provenance record linking the raw output hash to the immutable source master hash, exact crop hash, prompt/generation record, role family, and review date.
3. The KSU source page was unreachable in the source pass and the photographer remains unknown. This is not a newly discovered identity failure, but the Commons/KSU uncertainty must remain attached to any final manifest or runtime handoff.

These are documentation/provenance holds, not visual repaint defects. A fresh repaint is not required unless the parent cannot recover or author an exact generation record.

## Runtime boundary

DDS conversion and runtime wiring are **not permitted yet** because the mandatory independent provenance evidence is incomplete. Once the parent retains the exact prompt or equivalent generation record, updates the package/permanent handoff with `portrait_provenance`, and rechecks the source-rights uncertainty, the visual gates in this audit support conversion with the repository-standard DDS tool and wiring to the existing `GFX_portrait_CHU_independence_wave_federal_presidium` sprite path.

This audit did not convert DDS, edit `.gfx`, replace an existing runtime DDS, alter the character, change localisation, or stage/commit any file.

## Validation performed

- Reopened the immutable source, exact crop, raw package master, flat-shelf copy, candidate, review sheet, and canonical leader references with Pillow and confirmed their recorded dimensions and file hashes.
- Confirmed the flat-shelf raw copy and package raw master have identical bytes and SHA-256 values.
- Reopened the crop equality JSON and confirmed `exact_source_crop_verified`, `decoded_pixels_equal = true`, crop rectangle `(100,20,780,1060)`, and matching source/crop hashes.
- Confirmed the candidate decodes as fully opaque RGBA `156x210` and contains no alpha holes or checkerboard matte.
- Inspected source, crop, raw, candidate, review sheet, and canonical leader references at native display scale and compared the identity-bearing facial and clothing features directly.
- Confirmed no DDS, `.gfx`, gameplay, localisation, advisor, dossier, `_small`, or alternate-person derivative was produced or changed by this audit.

No fallback or substitute identity was used. The only remaining hold is the missing exact generation/prompt provenance record and the already-recorded uncertainty around the archival source page/photographer.
