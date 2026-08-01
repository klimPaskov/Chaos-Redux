# IW-030 Mitar Martinović portrait likeness audit v89 (2026-08-01)

## Decision

**Overall verdict: HOLD.** The approved Mitar Martinović source lead may proceed through the real-person repaint pipeline, but this raw ImageGen repaint and its existing 156x210 candidate are not admitted to runtime or DDS wiring. The source and crop are defensible; the repaint does not yet clear the separate, non-compensable identity gate and also introduces source-visible uniform and insignia drift.

This is a read-only visual audit. No gameplay, character, localisation, `.gfx`, runtime texture, or DDS file was changed.

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
