# IW-030 Mitar Martinović portrait likeness audit v89 (2026-08-01)

## Decision

**Overall verdict: HOLD.** The approved Mitar Martinović source lead may proceed through the real-person repaint pipeline, but this raw ImageGen repaint and its existing 156x210 candidate are not admitted to runtime or DDS wiring. The source and crop are defensible; the repaint does not yet clear the separate, non-compensable identity gate and also introduces source-visible uniform and insignia drift.

This is a read-only visual audit. No gameplay, character, localisation, `.gfx`, runtime texture, or DDS file was changed.

### v2 re-audit update (2026-08-01)

**v2 overall verdict: HOLD.** The v2 repaint is a modest visual refinement, but it still does not clear the grounded-real-person identity gate. The source lead remains approved to continue, while this v2 raw repaint and native candidate remain evidence-only and must not be converted or wired.

Separate verdicts are **identity: HOLD**, **style: HOLD**, and **provenance: PASS with caveat**. The source master/crop, raw v2, native v2, processing JSON, and durable source/prompt pair are linked and hashable, but provenance completeness does not compensate for weak likeness or unsupported insignia.

## Evidence inspected

| Evidence | Dimensions/mode | SHA-256 or proof | Finding |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/source_masters/mnt_mitar_martinovic_1912_chronicle.jpg` | 684x1135 RGB JPEG | `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76` | Immutable archival 1912 identity master documented in the v87 manifest as a Serbian National Library scan from *Ilustrovana ratna kronika*, with the manifest's `PD-collective-work|Serbia` rights note. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` | 530x670 RGB PNG | `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` | Explicit head-and-shoulders crop; the paired JSON reports `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, and equal decoded RGBA hash `0c7f16cd55741be02cf693c2c0b6d5e92daee087ed873facb93ecb12a807b81f`. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw.png` (external source path: `C:\Users\klimp\.codex\generated_images\019f6059-0778-7992-8f0d-f7582beecbeb\exec-b2d2c5ee-dbb8-42f1-8d91-18fedc9ac028.png`) | 1098x1432 RGB PNG | `8d69a2d39f99cd0d69a7dfddc4da1943af1b176a0eab07e06dc132c7797619d7` | Raw ImageGen repaint retained in the generated-portrait package; evidence only until independent audit. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210.png` | 156x210 RGB PNG | `57c6f654d1f8bb6aa4e8407bb256f7529d645d4ffb9e0d87c9efc047b95c65d8` | Deterministic center-crop/LANCZOS candidate; reviewed at native and 4x nearest-neighbour, not admitted to DDS or runtime. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_comparison_sheet.png` | Review sheet | Package evidence | Side-by-side archival crop, raw repaint, and native 156x210 candidate; review-only. |
| `docs/assets/portraits/006_independence_wave/portrait_MNT_mitar_martinovic.png` and matching `.txt` | Durable source/prompt pair | Source PNG SHA-256 `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` matches the exact crop | Source PNG is the archival crop for later ComfyUI replacement; prompt is retained but currently describes some idealized facial geometry and must be revised for the next repaint. |
| `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and `portraits/commanders/contact_sheet.png`, plus the individual 156x210 leader/commander references | 156x210 native references | Repository canonical reference set | Used for native/enlarged HOI4 painted-style comparison. |

The source crop and raw repaint were reviewed at native resolution and at a 4x nearest-neighbour enlargement. The raw repaint was compared against the source master, exact crop, and canonical leader/commander references rather than against a generic face.

## Gate findings

| Gate | Verdict | Evidence and reason |
| --- | --- | --- |
| Grounded source mode | **PASS** | Montenegro and Mitar Martinović are grounded historical identities; the v87 manifest keeps this on the sourced-real-person path and records an attributed 1912 archival source. |
| Source master and crop linkage | **PASS** | The immutable master, explicit crop, crop coordinates `[80,90,610,760]`, and decoded-pixel equality JSON are present and mutually linked. |
| Identity preservation | **HOLD** | The repaint is recognizably based on the source, but facial geometry is not locked closely enough for a real-person portrait. The detailed observations below are blockers, not style preferences. |
| HOI4 painted portrait family | **HOLD** | It has centered head-and-shoulders framing, period uniform, restrained background, and a painted finish that broadly fits the family. The heavy impasto/noisy brush texture and warmer, darker tonal treatment are less clean than the canonical 156x210 references and need a controlled refinish before runtime processing. |
| Unsupported clothing/insignia | **HOLD** | The repaint reinterprets the cap device and adds or alters decoration details instead of source-locking the visible uniform. See exact blockers below. |
| Role and period fit | **PASS with caveat** | The military general presentation is role-correct for the admitted Martinović candidate and visually period-appropriate. The source is from 1912 while the scenario starts in 1936, a documented 24-year source-era gap that is acceptable only as an explicit historical-source note, not as a claim that the image is from 1936. |
| Runtime readiness | **BLOCKED** | A deterministic 156x210 candidate and comparison sheet exist, but identity/style audit is HOLD and no DDS or `.gfx` admission is allowed before an independent PASS. |

## Identity observations

- **Moustache: partial preservation, not sufficient for PASS.** The broad dark walrus moustache is retained and is the strongest identity anchor, but the repaint makes it fuller, darker, and more dramatically upswept at the outer tips than the source's flatter, softer ends.
- **Eyes: HOLD.** The source shows uneven, narrower eye shapes with visible asymmetry and a different eyelid/gaze relationship. The repaint opens and levels both eyes, brightens them, and makes the eye spacing and gaze more symmetrical.
- **Nose: HOLD.** The source has a broad, relatively short straight bridge and a broad rounded tip. The repaint narrows and lengthens the bridge, changes the nostril/tip shape, and gives the center plane a more sculpted idealized highlight.
- **Jaw and chin: HOLD.** The source reads as a broad, compact lower face beneath the moustache. The repaint lengthens the lower face, sharpens the cheek planes, and gives the chin/jaw a cleaner, more tapered contour.
- **Face proportions and asymmetry: HOLD.** The source has a broad forehead and cheek mass with visible side-to-side asymmetry. The repaint is vertically stretched and visibly beautified/symmetrized, which is identity drift even though the moustache and cap make the subject recognizable.
- **Native 156x210 candidate: HOLD.** The candidate remains readable at game size and preserves the moustache/cap/uniform anchors, but downsampling does not repair the eye, nose, or jaw drift; the face becomes a generic, symmetrical moustached officer when viewed at native size.

## Unsupported changes and period details

- The source cap device is a small, source-specific heraldic ornament. The repaint replaces it with a larger gold crossed/leaf-like emblem with a different silhouette; this is an invented or reinterpreted insignia unless the source-locked prompt explicitly proves otherwise.
- The shoulder rosettes, braided collar/shoulder decoration, diagonal straps, and medal/sash cluster are simplified and re-designed in the repaint. The red ribbon and enlarged cross/medal presentation are not safely inferable from the grayscale source and must not be retained without source support.
- The repaint's warm ochre/red palette is acceptable as a painted conversion only where it maps to source-visible material; it cannot be used to invent hidden colors, ribbons, ranks, or awards.
- The durable ComfyUI prompt is present, but phrases such as `broad dark upswept moustache`, `strong straight nose`, and `square jaw` describe the idealized drift seen in the repaint rather than the source's flatter moustache ends, broader short nose, and compact lower face. Revise the prompt with source-observed geometry before another repaint.

## Required disposition

1. Keep the v87 source master and exact crop immutable and continue to cite the v87 manifest for archive, rights, role, and era notes.
2. Request a source-locked identity-preserving repaint that keeps the source's eye asymmetry, broad short nose, compact jaw/face proportions, and moustache silhouette instead of beautifying or symmetrizing them.
3. Require the cap device, rosettes, collar braid, diagonal straps, and medal/sash cluster to remain source-faithful; remove invented emblem geometry and unsupported color/award detail.
4. Keep the generated-portrait raw PNG, processing JSON, native candidate, comparison sheet, and durable ComfyUI prompt pair together as active evidence. The external ImageGen path is preserved as provenance, while the package copy is the audit input.
5. Request a corrected source-locked repaint and rerun the deterministic 156x210 processing and independent review; the current candidate remains evidence only. Convert to DDS and hand off the stable runtime sprite/path only after an identity/style PASS.
6. Do not relabel `MNT_kristo_popovic` or wire this face under Popović. The v87 handoff requires an explicit parent roster/character identity admission for Martinović before any runtime consumer is changed.

## Final status

**HOLD - source lead approved to proceed; raw repaint and 156x210 candidate blocked from runtime admission.** The exact blockers are weakly locked eye/nose/jaw geometry, symmetry/beautification drift, unsupported cap and decoration reinterpretation, and the lack of an independent identity/style PASS and DDS admission.

## v2 audit evidence and separate verdicts

| v2 evidence | Dimensions/mode | SHA-256 or proof | Finding |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v2.png` | 1115x1410 RGB PNG | `c58c3f0a2a43d86b24a0c9700aaa8ec60c699428505f032fdbf5d7030e3aa111` | Raw v2 ImageGen repaint under audit. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v2.png` | 156x210 RGB PNG | `ffbb69d1998f154a84f230b595b6dbdfecc1e037c0d7fb794feb9cd3a6f972e8` | Deterministic center-crop/LANCZOS candidate; evidence only, no DDS or runtime admission. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_processing_v2.json` | Processing record | `composition_crop=[34,0,1081,1410]`, output `[156,210]` | Records RGB center crop and LANCZOS resize with no padding, recolour, or face edit. |

The immutable source master and exact crop remain the v87 evidence listed above. The v2 raw, native candidate, and processing record were reviewed at native size and 4x nearest-neighbour enlargement against that master/crop and the canonical leader/commander reference contact sheets.

### v2 identity verdict: HOLD

- **Moustache: partial PASS only.** The v2 retains the broad dark moustache and is less dramatically flared than v1, but its outer tips still curl upward and its mass is smoother and more generic than the source's flatter, uneven silhouette. The moustache keeps the subject recognizable but cannot carry the identity gate alone.
- **Eyes: HOLD.** The source's eye shapes and eyelids are uneven and asymmetrical, with a distinctive gaze. V2 levels both eyes, opens the lids, and gives the pupils/spacing a more symmetrical, generic officer expression.
- **Nose: HOLD.** The source has a broad, short bridge and rounded/broad tip. V2 narrows and lengthens the bridge, sharpens the highlight plane, and gives the tip/nostrils a different contour.
- **Jaw, chin, and face proportions: HOLD.** V2 remains narrower and more vertically elongated through the lower face than the source, with a cleaner tapered chin and reduced cheek mass. The native candidate reads as a generic symmetrical moustached officer once downsampled.
- **Cap and visible uniform linkage: HOLD.** The pose and military cap/uniform anchor are preserved, but the cap device is enlarged and reinterpreted as a bright crossed/leaf-like ornament rather than a source-locked rendering. Medal/rosette geometry is simplified and partly redesigned; any bright metal or ribbon colors are not established by the grayscale source.

### v2 style verdict: HOLD

V2 is broadly in the HOI4 painted portrait family because it uses centered head-and-shoulders framing, a restrained neutral background, period military clothing, and a painted rather than photographic finish. It is not yet style-ready for runtime: the heavy impasto brush noise is coarser than the canonical 156x210 references, facial planes and eyes become muddy at native size, and the warm olive/tan palette plus bright ornament make the portrait read more like a generic stylized painting than a controlled HOI4 dossier portrait. The v2's reduced red-sash emphasis is an improvement over v1, but it does not resolve the source-linkage or identity problems.

### v2 provenance verdict: PASS with caveat

The v2 package has a retained raw PNG, native candidate, processing JSON, hashes, dimensions, and source/crop linkage to the immutable v87 evidence. The durable ComfyUI source/prompt pair also remains present, and the source PNG hash matches the exact crop. The caveat is that the current durable prompt still contains idealized descriptors (`broad dark upswept moustache`, `strong straight nose`, `square jaw`) that are inconsistent with the source-observed geometry and likely contribute to the drift; revise that prompt before another repaint. Provenance PASS therefore means the evidence chain is auditable, not that the v2 is runtime-approved.

### v2 blockers and disposition

1. Keep v2 raw and native files as evidence only; do not convert to DDS or wire `.gfx`.
2. Request another source-locked repaint that preserves the source's asymmetric eyes, broad short nose, compact cheek/jaw proportions, and flatter moustache ends.
3. Keep the source-specific cap device, rosette pattern, collar braid, diagonal straps, and medal cluster source-faithful; do not invent or enlarge the bright crossed/leaf-like cap ornament or unsupported color/award detail.
4. Revise the durable prompt to describe visible source geometry instead of `upswept moustache`, `strong straight nose`, and `square jaw`.
5. Re-run independent identity and style review on the next raw and deterministic 156x210 candidate. Only a separate identity PASS and style PASS can unlock DDS and runtime wiring.

**v2 final status: HOLD.** Identity and style are below the admission threshold despite improved evidence packaging; provenance is auditable with the caveat above. The source lead remains approved to proceed, but v2 must not be used as a runtime portrait or as a relabel for `MNT_kristo_popovic`.

## v3 independent audit (2026-08-01)

**v3 overall verdict: HOLD.** V3 remains a recognizable source-derived military portrait, but its identity geometry and insignia are not source-locked strongly enough for a grounded real-person portrait. In addition, the file named `portrait_MNT_mitar_martinovic_hoi4_156x210_v3.png` is not a native candidate at all: it is 1058x1411 and pixel-equal to the declared center crop, despite the processing JSON claiming a 156x210 LANCZOS output. This is a hard provenance/processing blocker independent of the likeness result.

### v3 evidence

| v3 evidence | Dimensions/mode | SHA-256 or proof | Finding |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v3.png` | 1114x1411 RGB PNG | `2d1edd076b3b57e7debbe2225d134cb036786405b962272d16d8fee9fc3eda1c` | Raw v3 ImageGen repaint reviewed against the immutable source/crop and canonical references. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v3.png` | **1058x1411 RGB PNG**, not 156x210 | `f842d2f9abc10be1bfa7b9730283c0c2db30b447ff0732f9e217ed3169ea3d27` | File is pixel-equal to raw v3 crop `[28,0,1086,1411]`; no resize occurred. It cannot be treated as a native candidate. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_processing_v3.json` | Processing record | Claims crop `[28,0,1086,1411]` then output `[156,210]` with LANCZOS | Metadata contradicts the decoded output dimensions and file contents. |

The source master remains 684x1135 RGB with SHA-256 `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76`, and the exact crop remains 530x670 RGB with SHA-256 `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` plus decoded-pixel equality proof. The v3 raw and named candidate were reviewed at native size and 4x nearest-neighbour enlargement against those source files and the canonical leader/commander contact sheets.

### v3 identity verdict: HOLD

- **Eyes and spacing: HOLD.** V3 keeps a frontal gaze but levels and opens both eyes into nearly matched shapes and spacing. The source has visibly uneven eyelids, eye openings, and gaze asymmetry; the repaint's symmetry reads as a generic officer face.
- **Nose: HOLD.** V3 has a narrower, longer central bridge and a more sculpted highlight/tip than the source's broad short bridge and rounded broad tip. The lower nose and nostril contour remain different at 4x inspection.
- **Jaw and face proportions: HOLD.** V3 narrows the cheeks and lengthens/tapers the lower face and chin relative to the source's broader, more compact facial mass. The mismatch is visible even before any native resize.
- **Moustache: partial PASS only.** The broad dark moustache is preserved and makes the subject recognizable, but V3 still gives the outer ends a smoother upward sweep and a more uniform silhouette than the source's flatter, uneven ends. It is not sufficient to offset the eye/nose/jaw drift.
- **Cap emblem and medals: HOLD.** V3 uses a large bright crossed/leaf-like cap emblem whose silhouette and scale do not match the small source-specific device. The rosette, collar braid, diagonal strap, and medal cluster are painted as new high-contrast details; grayscale source evidence does not authorize their exact color or invented geometry.

### v3 style and framing verdict: HOLD

The raw v3 has a centered head-and-shoulders military composition, muted neutral background, and period-looking uniform, so it broadly follows the HOI4 painted portrait family and role/period direction. The impasto texture is still coarser and more repetitive than the canonical 156x210 leader/commander references, with muddy eye planes at native scale and an overly bright cap ornament. Because the file labeled `156x210_v3` is actually 1058x1411, there is no valid native-size style/frame candidate to approve; runtime framing must be reprocessed after the raw identity problem is corrected.

### v3 provenance/processing verdict: HOLD (hard blocker)

The raw v3 has a stable package path and hash, and the source/crop lineage is auditable. However, the v3 package is not processing-complete: the named native candidate is the unresized crop, its decoded dimensions contradict `processing_v3.json`, and `generated_portraits/manifest.md` has no v3 row. The JSON also uses bare filenames rather than the full package paths used by the v2 record. Correct the processing output, hash, dimensions, and manifest before any future review can consider a runtime candidate.

### v3 required disposition

1. Keep both v3 files evidence-only and do not convert or wire either file.
2. Re-run the deterministic processor from the raw v3 after producing a corrected source-locked repaint, and verify decoded dimensions are exactly 156x210 with a matching output hash.
3. Preserve source eye asymmetry, broad short nose, compact jaw/cheek proportions, and flatter moustache ends in the next repaint.
4. Keep the cap device, rosette pattern, collar braid, diagonal straps, and medals source-faithful; remove the enlarged crossed/leaf-like emblem and unsupported color/award additions.
5. Add the corrected v3-or-later raw/candidate/processing rows to `generated_portraits/manifest.md`, using full paths and matching hashes, then obtain independent identity and style PASS before DDS or `.gfx` work.

**v3 final status: HOLD.** Identity and style remain below threshold, and the supposed 156x210 candidate is invalid by exact decoded dimensions and crop-equality evidence. The source lead may continue, but v3 is not admissible as a runtime portrait or as a relabel for `MNT_kristo_popovic`.

## v4 independent audit (2026-08-01)

**v4 overall verdict: HOLD.** V4 fixes the v3 processing defect: the named candidate decodes to exactly 156x210 and its processing JSON records the full raw/output paths, crop, hashes, and immutable-crop source link. The visual identity gate still fails closed, however, because the eyes, nose, lower-face proportions, moustache silhouette, and cap emblem remain visibly genericized or reinterpreted. No DDS or runtime admission is authorized.

### v4 evidence and processing check

| v4 evidence | Dimensions/mode | SHA-256 or proof | Finding |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v4.png` | 1115x1410 RGB PNG | `aadd994e42f2592f7a4479b0af66c9743ad7258c48f1b3d61da0f656166bd842` | Raw v4 ImageGen repaint under audit. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v4.png` | **156x210 RGB PNG** | `18810f98092b9b0a88fa93da69d31383151280cb2261ebb7e6c3eea11c36c9f2` | Valid native candidate dimensions confirmed from the decoded file. |
| `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/generated_portraits/portrait_MNT_mitar_martinovic_processing_v4.json` | Processing record | Crop `[29,0,1086,1410]` to 1057x1410, Pillow LANCZOS to `[156,210]`, source/output hashes match files | Processing metadata is internally consistent and source-linked to the immutable archival crop. |

The immutable source master remains 684x1135 RGB with SHA-256 `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76`, and the exact 530x670 crop remains SHA-256 `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` with decoded-pixel equality proof. V4 raw and native files were reviewed at native size and 4x nearest-neighbour enlargement against that crop and the canonical leader/commander contact sheets.

### v4 identity verdict: HOLD

- **Eyes and spacing: HOLD.** V4 keeps the frontal pose but opens and levels the eyes into nearly mirrored shapes with similar spacing and pupils. The source has uneven eyelids, eye openings, and gaze asymmetry that remain identity-bearing; v4's gaze is a generic symmetrical officer gaze.
- **Nose: HOLD.** V4's bridge is more vertically elongated and its tip/nostrils are more sculpted and narrow than the source's broad short bridge and rounded broad tip. The central highlight and lower-nose contour are not source-locked.
- **Jaw and face proportions: HOLD.** V4 retains a broad forehead but narrows the cheeks and lengthens/tapers the lower face and chin relative to the source's compact lower facial mass. The native 156x210 candidate makes this genericization more apparent.
- **Moustache: partial PASS only.** The dark broad moustache remains the strongest anchor and v4 is less exaggerated than v1, but the outer ends still curl upward and the overall mass is smoother and more evenly shaped than the source's flatter, uneven moustache. It cannot compensate for the eye/nose/jaw drift.
- **Cap emblem and medals: HOLD.** V4's bright cap device is larger and has a crossed/leaf-like silhouette unlike the small source-specific heraldic device. Rosettes, collar braid, diagonal strap, and medal details are painted as high-contrast re-interpretations; the grayscale source does not establish their exact colors or authorize invented award geometry.

### v4 style and framing verdict: HOLD

V4 has centered head-and-shoulders framing, a neutral painted background, and an early-twentieth-century military presentation that broadly fits the HOI4 portrait family and Martinovic's general role. The valid native candidate is legible at 156x210, but its face and eye planes are soft/muddy and the brush texture is coarser and more repetitive than the canonical leader/commander references. The oversized bright cap device and painted uniform embellishments also pull the image away from a controlled source-locked HOI4 dossier portrait.

### v4 provenance verdict: PASS with caveat

The v4 raw/candidate files and processing JSON form a coherent, hash-matched source-to-output chain, and the JSON explicitly links the pipeline to the immutable archival crop. The active `generated_portraits/manifest.md` still lists only the earlier repaint rows, so add a v4 row and its final audit status before any durable promotion. This packaging caveat does not change the identity HOLD and does not authorize DDS or `.gfx` work.

### v4 required disposition

1. Keep v4 raw and native files evidence-only; do not convert to DDS or wire `.gfx`.
2. Request a further source-locked repaint preserving the source's uneven eyes, broad short nose, compact cheek/jaw proportions, and flatter moustache ends.
3. Keep the cap device, rosette pattern, collar braid, diagonal straps, and medals source-faithful; remove the enlarged crossed/leaf-like emblem and unsupported color/award additions.
4. Add the v4 raw/candidate/processing entries to `generated_portraits/manifest.md` with matching hashes and record the separate identity/style HOLD verdict.
5. Re-run independent identity and style review on the next candidate. Only separate identity PASS and style PASS can unlock DDS and runtime wiring.

**v4 final status: HOLD.** Processing and source linkage pass with a manifest caveat, but identity and style remain below the admission threshold. The source lead may continue, while v4 must not be used as a runtime portrait or as a relabel for `MNT_kristo_popovic`.

## v5 independent audit (2026-08-01)

**Overall verdict: HOLD. MNT cannot proceed to runtime admission on v5.** V5 is a validly processed native candidate and is a modest visual improvement in palette and moustache restraint, but the grounded-real-person identity gate remains failed closed.

### Evidence and processing

| Evidence | Dimensions/mode | SHA-256 or proof | Verdict |
| --- | --- | --- | --- |
| `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v5.png` | 1114x1412 RGB PNG | `4ff2aba90318de05fe3ec00be7bfb6ee272663e2c2bce83b2ddfc335b2c407d3` | Raw repaint retained and linked to the source-crop pipeline. |
| `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v5.png` | 156x210 RGB PNG | `7f4186eb160ffbb9e44c3e297ea6b28d6470ff7c5c27ce50d2302ffe5a18ecf4` | Exact native dimensions confirmed; no DDS or runtime wiring. |
| `generated_portraits/portrait_MNT_mitar_martinovic_processing_v5.json` | Crop `[27,0,1086,1412]`, LANCZOS to `[156,210]` | Source/output hashes match the files; `source_link` names the immutable crop | **PASS** processing/provenance chain. The active generated-portrait manifest now records the v5 rows and `pending_independent_audit_v5`. |
| Immutable crop `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` | 530x670 RGB PNG | `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` | Exact source crop remains unchanged and is the identity reference. |

### Separate visual verdicts

- **Identity: HOLD.** At native and 4x nearest-neighbour inspection, v5 still levels and opens the two eyes into near-mirrored shapes with generic spacing and gaze; the source's uneven eyelids and asymmetry are not preserved. The nose remains a more idealized, vertically lengthened bridge/tip rather than the source's broad short nose. The cheek mass and lower face are narrower and more vertically elongated than the source's compact proportions. The broad moustache remains recognizable and is less aggressively curled than earlier attempts, but its ends and even mass still differ and cannot compensate for the eye/nose/jaw drift.
- **Cap/medal source linkage: HOLD.** V5 retains the military cap, rosettes, collar braid, diagonal strap, and medal-bearing composition, but the cap device is enlarged and rendered as a bright gold crown/leaf/cross motif whose silhouette is not source-locked. The painted rosettes, gold collar/medal detail, and blue/red award colors are not established by the grayscale source and include unsupported re-interpretation.
- **HOI4 style/framing: PASS with caveat.** The valid 156x210 candidate is centered, head-and-shoulders, period-military, neutral-background, and broadly compatible with the canonical HOI4 leader/commander painted family. V5 is smoother and less muddy than v4, though the bright cap emblem and still-soft eye planes need refinement if a future identity PASS is achieved.
- **Role/period fit: PASS with caveat.** The general's uniform and bust framing fit the admitted Martinovic role and early-twentieth-century source context; the source is 1912 for a 1936 scenario and must retain the documented era-gap note.

### Required disposition

1. Keep v5 raw and native files as evidence-only; do not convert DDS or wire `.gfx`.
2. Request another source-locked repaint that preserves the source's eye asymmetry/spacing, broad short nose, compact cheek and jaw proportions, and flatter moustache ends.
3. Remove or source-lock the enlarged crown/leaf/cross cap device and unsupported award colors/details before another identity review.
4. Re-run the independent likeness gate on the next candidate. Only identity PASS plus the existing processing/provenance PASS can unlock runtime work.

**v5 final status: HOLD.** Provenance/processing PASS and HOI4 style PASS-with-caveat do not offset the non-compensable identity HOLD. The MNT source lead may continue to another repaint, but v5 cannot be promoted or wired.
