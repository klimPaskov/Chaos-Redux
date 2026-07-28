# Event 006 CHU Galimzhan Ibrahimov repaint v2 independent audit

Date: 2026-07-28.

Reviewer: independent sourced-visual audit subagent, separate from the ImageGen producer.

Scope: the new ImageGen output, immutable archival source master and exact crop, deterministic `156x210` leader candidate, canonical vanilla leader references, prompt record, provenance record, and source/shelf copy integrity. No gameplay, character, localisation, `.gfx`, DDS, or runtime file was edited or wired by this audit.

## Disposition

**PASS for v2 visual likeness, HOI4 country-leader style, framing, artifact, crop, and provenance gates, with the archival-source uncertainties recorded below.** The v2 raw master is preserved in the flat pre-resize shelf and the originating package; the normalized candidate and review evidence remain in the package workspace.

DDS conversion and runtime wiring are **permitted for parent-side promotion after review** because the independent gates pass. This audit did not create a DDS, edit `.gfx`, or replace the existing runtime texture. The v1 portrait remains superseded evidence and is not the approved promotion candidate.

## Evidence and hashes

| Artifact | Path | Native facts / SHA-256 |
|---|---|---|
| Immutable archival source master | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/source_masters/volga/chu_galimzhan_ibrahimov.jpg` | JPEG grayscale `L`, `863x1272`, `344,829` bytes, `931a6dd35f70e2fd4fbd58aafd030d60a2755dc6a7dc68704b8267aefb864532`. |
| Exact identity crop | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/source_crops/CHU_federal_presidium_galimzhan_ibrahimov_head_shoulders.png` | Lossless PNG grayscale `L`, `680x1040`, crop `(100,20,780,1060)`, `538,499` bytes, `accab14222f1154300ce9d6e36d101d11d0d59800172ec231c33468c88fbca75`. |
| Crop equality JSON | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/crop_metadata/CHU_federal_presidium_galimzhan_ibrahimov_crop.json` | `status = exact_source_crop_verified`; `decoded_pixels_equal = true`; source/crop/output equality hashes match. |
| Recorded prompt | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaint_plans/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v2_prompt.md` | Exact prompt record, SHA-256 `101fcf94f4e5b68d1e662c9247e7d29326b40c75244c9b7d85a1fcbc5e9a38a0`; names the exact crop, leader role, constraints, and ImageGen output path. |
| New external ImageGen output | `C:\Users\klimp\.codex\generated_images\019f6059-0778-7992-8f0d-f7582beecbeb\exec-2971dbe3-49e7-4412-9842-1071b85557a9.png` | PNG RGB `1013x1552`, `2,178,302` bytes, `76a43eccc7d3acb9cdd3fdec682656786c50d4b27cea482f415f1ae9398c5c7b`. |
| Versioned package raw master | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_raw/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v2.png` | PNG RGB `1013x1552`, `2,178,302` bytes, `76a43eccc7d3acb9cdd3fdec682656786c50d4b27cea482f415f1ae9398c5c7b`; byte-for-byte equal to the external output. |
| Versioned flat-shelf raw master | `docs/assets/006_independence_wave/portraits_generated_png/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v2.png` | PNG RGB `1013x1552`, `2,178,302` bytes, same `76a43eccc7d3acb9cdd3fdec682656786c50d4b27cea482f415f1ae9398c5c7b`; byte-for-byte equal to the package raw. No normalized candidate is stored in the shelf. |
| Deterministic normalized candidate | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_processed/CHU_federal_presidium_galimzhan_ibrahimov_156x210_v2_candidate.png` | PNG RGBA `156x210`, fully opaque alpha, `5f54733be97f4008e265e4b21da2716e211533d56cfc4589612db089cb74c094`. |
| Processor metadata | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/processing_metadata/CHU_federal_presidium_galimzhan_ibrahimov_156x210_v2.json` | Processor v5.0, processor SHA-256 `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`, role family `leader`, source kind `real`, deterministic crop `[0,0,1013,1552]`. File SHA-256 `36776689ea0f062904dc8d0f521aecc1a9bbc8b6c7b814de1989a5fc275ed136`. |
| Processor review sheet | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/review/CHU_federal_presidium_galimzhan_ibrahimov_v2_processing_review.png` | RGBA PNG `1344x464`, `286ffeddc1c7e6278e87b79a748f4dc6c9ff51919eeb09f921196a065eced668`; shows processor input, normalized candidate, and canonical leader references. |
| Provenance record | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/processing_metadata/CHU_federal_presidium_galimzhan_ibrahimov_repaint_v2_provenance.json` | SHA-256 `4c2aaccbdb8bdd483ddd081ec98011bb5012886913213f135469a0db61b3fd8e`; pins source, crop, prompt, ImageGen handle, generation output, normalized candidate, review sheet, rights uncertainty, and runtime boundary. |

The exact generation handle is `exec-2971dbe3-49e7-4412-9842-1071b85557a9`. The prompt record explicitly requires identity preservation, the exact crop as ImageGen input, a male country-leader portrait, controlled 1930s grand-strategy brushwork, blue-grey studio field, no unsupported insignia, and no advisor treatment.

## Canonical style references

The processor and audit used only the canonical leader family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` for style, framing, and tonal comparison.

| Reference | SHA-256 | Audit comparison |
|---|---|---|
| `den_thorvald_stauning.png` | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` | Opaque `156x210` leader canvas, modeled face, subdued background, and readable upper-bust silhouette. |
| `fin_carl_mannerheim.png` | `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e` | Opaque `156x210` leader canvas, controlled contrast, period clothing, and painterly facial planes. |

No commander, advisor, dossier, operative, or institutional group reference was used for this country-leader candidate.

## Independent gate verdicts

| Gate | Verdict | Finding |
|---|---|---|
| Archival identity source | **PASS** | The unchanged source is an attributed 1920s-era portrait of Galimzhan Ibrahimov, a Tatar writer, publicist, and politician who lived to 1938. It remains the sole identity authority. |
| Exact crop | **PASS** | The existing crop JSON proves the decoded pixels equal the archival master rectangle `(100,20,780,1060)` with no resize, retouch, recolour, or enhancement. The v2 prompt references this exact crop. |
| ImageGen source lock | **PASS** | The v2 prompt names the crop as Image 1 and requires the same man, head angle, hat, eyes, moustache, nose, hairline, overcoat, and framing. The v2 output is retained under its external path and two byte-equal repository paths. |
| Exact likeness | **PASS** | The v2 master and normalized candidate preserve the broad light felt hat and dark band, three-quarter head angle, high cheekbone/narrow-face reading, slightly hooded unequal eyes, nose profile, compact dark moustache, dark side hair and hairline, visible ear, serious expression, and high-collared overcoat. The face is not frontalized, beautified, symmetrized, genericized, or replaced by another person. Fine source halftone detail is intentionally translated into painterly planes, while the identity-bearing asymmetries remain legible at `156x210`. |
| Male / role fit | **PASS** | The subject remains one male civilian country leader. `common/characters/006_independence_wave_iw043_iw058_characters.txt:21-28` declares `gender = male` and the `civilian.large` consumer; current localisation names the token Galimzhan Ibrahimov and describes the Tatar federal-presidium role. |
| HOI4 leader style | **PASS** | The v2 uses a restrained 1930s grand-strategy painted finish with modeled facial planes, controlled brush texture, muted blue-grey field, soft vignette, dark period overcoat, and readable face. It is stylistically compatible with the Stauning/Mannerheim leader references without copying their faces or clothing. |
| Framing / native canvas | **PASS** | The raw v2 aspect ratio is `1013x1552` (`0.6522`), closely matching the `680x1040` identity crop (`0.6538`). It is a centered vertical bust with hat, shoulders, collar, and clean background margins. The deterministic candidate is fully opaque RGBA `156x210` and has no dossier/card treatment. |
| Artifact and exclusion checks | **PASS** | Native inspection found no text, watermark, UI, logo, extra person, weapon, emblem, modern clothing, advisor frame, checkerboard matte, transparent hole, malformed eye/ear, or painterly geometry artifact. The lower coat remains dark but readable and does not obscure the identity. |
| Rights / source provenance | **PASS WITH RECORDED UNCERTAINTY** | The source ledger records Commons Public Domain Mark/PD-old basis, Kazan State University library credit, estimated 1920s date, and unknown photographer. The KSU page was unreachable during the source pass and the Commons upload history notes image-processing provenance; the unchanged master, links, uncertainty, prompt hash, crop hash, generation handle, and output hashes are all preserved in the v2 provenance record. |
| Stable consumer / ownership | **PASS FOR PARENT PROMOTION** | The existing character and sprite consumer are stable and unchanged. `interface/006_independence_wave_iw043_iw058_portraits.gfx:15-16` maps `GFX_portrait_CHU_independence_wave_federal_presidium` to `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds`; this audit does not edit that mapping. |
| Forbidden derivatives | **PASS** | Only a country-leader raw master and deterministic country-leader candidate were produced. No advisor icon, dossier card, operative, high-command, `_small`, `50x67`, alternate-person, or generic substitute exists in the v2 package. |

## Visual comparison notes

Compared with the archival crop, v2 keeps the hat silhouette, dark band, head turn, eye asymmetry, cheek and nose planes, moustache width, hairline, ear exposure, collar angle, and reserved civic-intellectual expression. The source's monochrome halftone is converted to warm skin and neutral blue-grey paint, which is the requested HOI4 treatment rather than an identity substitution.

Compared with v1, v2 uses the requested blue-grey studio field and a source-matching aspect ratio, keeps the face and hat closer to the archival crop, and reads more cleanly at normalized leader size. V1 remains evidence only and is not the approved runtime candidate.

Compared with the canonical leader references, v2 has the same opaque `156x210` country-leader canvas, centered upper-bust hierarchy, quiet background, modeled planes, and subdued period palette. Its visible brushwork is slightly stronger than Stauning or Mannerheim, but it remains controlled and readable rather than sketchy or photo-realistic.

## Runtime boundary

All independent gates pass with the archival source uncertainties explicitly recorded. DDS conversion and runtime wiring are therefore permitted for the parent-owned promotion step using the existing sprite path and intended DDS path `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds`.

This audit did not run DDS conversion, edit `.gfx`, replace an existing DDS, alter gameplay, change localisation, launch HOI4, or stage/commit unrelated work.

## Validation performed

- Reopened the external v2 PNG, package raw copy, flat-shelf copy, candidate, processor metadata, review sheet, immutable source, exact crop, and canonical leader references with Pillow.
- Confirmed the external output, package raw master, and flat-shelf raw master have identical `1013x1552` RGB dimensions, byte counts, and SHA-256 values.
- Confirmed the v2 normalized candidate is `156x210` RGBA with fully opaque alpha and the processor's decode-after-save equality flag is true.
- Confirmed the exact crop JSON reports `exact_source_crop_verified` and `decoded_pixels_equal = true` for the recorded source rectangle.
- Recomputed the prompt, processor metadata, review sheet, provenance-record, raw, shelf, and normalized candidate hashes recorded above.
- Inspected the archival crop, v2 raw master, v2 normalized candidate, review sheet, and canonical leader references at native and review scales for likeness, style, framing, and artifacts.
- Confirmed the flat shelf contains the v2 original-size RGB master and no v2 normalized candidate.

No simplification, fallback, alternate identity, runtime wiring, or gameplay change was used.
