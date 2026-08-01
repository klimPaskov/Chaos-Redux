# IW-043 CHU Bolgar civic-presidium portrait v3 audit v95

Date: 2026-08-01 (Europe/Kyiv).

Reviewer: OpenAI Codex asset-source auditor `/root/event6_chu_bolgar_repaint_audit_v93b`.

Scope: independent review of the parent-produced final bounded v3 Karim Tinchurin repaint and deterministic `156x210` candidate against the unchanged 1937 source master, the exact lossless crop, the v3 prompt and processing record, the prior v2 evidence, and the canonical male country-leader references. I did not produce the v3 repaint or candidate. No gameplay, characters, `.gfx`, localisation, DDS, central attestation, or catalog file was changed.

## Decision

**Overall verdict: HOLD; the v3 candidate remains ineligible for DDS promotion and runtime wiring because the source rights/date decision is still open.** V3 is a meaningful visual correction over v2: it keeps the bald crown and high hairline, narrows and lengthens the face, lowers and separates the eyes, reduces the brow weight, retains the long straight nose and thin closed mouth, and restores the compact jaw and source asymmetry. The visual likeness gate passes with a source-resolution caveat, the HOI4 leader style/framing gate passes, and the v3 prompt/processing/source chain is complete. Rights/date acceptance remains `needs_user_review` because the source is a 1937 NKVD mug-shot image, one year after the 1936 baseline, with the parent decision on the Commons legal basis still pending.

Separate gate verdicts are **identity/likeness: PASS with source-resolution caveat**, **HOI4 leader style/framing: PASS**, **provenance/chain: PASS**, **rights/date: HOLD (`needs_user_review`)**, and **DDS/runtime promotion: BLOCKED**.

The identity pass is bounded to visible source evidence. The archival crop is low-resolution, so the repaint's high-frequency eye, skin, and brush details are reconstructions rather than independently verified pixels; they must not be treated as permission to add hair, beautify, symmetrize, or redesign the subject.

## Evidence reviewed

| Artifact | Dimensions/mode | SHA-256 or proof | Review use |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_masters/karim_tinchurin_mug_shots_1937.jpg` | 1600x1086 RGB JPEG | `cc49680ff52c80b61f0198236e70c111f19bbabe20067c6246837c0484d04573` | Unchanged archival mug-shot sheet; the frontal right-hand panel is the identity source. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_crops/karim_tinchurin_head_shoulders.png` | 745x1035 RGB PNG | `1f44b5b72318839a4ccdf6f922a5fc5be53a278aaca25e6621ed870d4cb7cadf` | Exact frontal head-and-shoulders crop used as the sole identity authority. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/crop_metadata/karim_tinchurin_crop.json` | JSON evidence | `bbaa5a25faf768c538497bd57c310518d69b72614c64d777d45577ad4266caac` | Rectangle `(760,45,1505,1080)`; `decoded_pixels_equal: true`; matching decoded RGBA hash `693e7e77897665cc5895195d528c4d1cc5b4c12e6f4dd23816356071b752e103`; Pillow 11.1.0 and utility v1.0 recorded. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_raw/karim_tinchurin_hoi4_repaint_v1.png` | 1064x1478 RGB PNG | `e5b7236ea1a72ced0ae7a20d0116ee1414218a6eb1c49a94491984c2eb552fb3` | Prior repaint context; v93 audit recorded identity HOLD. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_raw/karim_tinchurin_hoi4_repaint_v2.png` | 1066x1476 RGB PNG | `d7c077a3ae82d3c0d1271ba937f1ae0faa152d5892cbf54c57b9ba5096d0b558` | Prior targeted retry context; v94 audit recorded identity HOLD. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_raw/karim_tinchurin_hoi4_repaint_v3.png` | 1064x1478 RGB PNG | `41b51a5c067cbcefe40a862bbd06093de3374f7536da085fef593b540a2e8470` | Final bounded v3 source-locked repaint under audit; evidence only. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_candidate_v2.png` | 156x210 RGB PNG | `8db2849f750b765bf54ee20026720abcfee2eaa57866c68a999253602fc5db48` | Prior native candidate context; not promoted. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_candidate_v3.png` | 156x210 RGB PNG | `e39e98f5f96ce0a9d69a418c27b0e217011e7993e5908efe74fc18c8823e2fc6` | Deterministic native v3 country-leader candidate; not DDS. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_processing_v3.md` | Processing record | `9006ee540a2821def1f8c8860c85eecc4269895b44898383fe2d0d5fdd66554c` | Raw v3 crop box `(0,22.8461538462,1064,1455.1538461538)` then Pillow `ImageOps.fit` LANCZOS to exact `156x210`, RGB, no enhancement. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/prompts/karim_tinchurin_hoi4_repaint_v3.txt` | Prompt record | `c0c370e6346e79c6f3b1373e8b18754edaae3afcfa49be19d7a6bf74ffd435ba` | Third source-locked prompt; it explicitly preserves the bald crown, low-set unequal eyes, long narrow nose, thin mouth, hollow cheeks, compact chin, jaw, asymmetry, collar, and plain jacket. |
| `docs/assets/006_independence_wave/portraits_generated_png/CHU_karim_tinchurin_hoi4_repaint_v3.png` | 1064x1478 RGB PNG | `41b51a5c067cbcefe40a862bbd06093de3374f7536da085fef593b540a2e8470` | Byte-identical flat original-size v3 shelf copy; evidence only. |
| `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.png` | 1064x1478 RGB PNG | `e5b7236ea1a72ced0ae7a20d0116ee1414218a6eb1c49a94491984c2eb552fb3` | Existing durable ComfyUI source pair for the portrait basename; it is the v1 source and is not a v3 generation record. |
| `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.txt` | Prompt TXT | `e5e3f716df77daef42416ddaded1d6d2e50eaa92bac08df3dfd790c8cb6fdd6c` | Existing durable ComfyUI replacement prompt; queue is not runtime storage. Refresh only if v3 becomes the accepted runtime source. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_v3_full_chain_4x_v95.png` | 2400x1960 RGB PNG | `04d06adae49a8f91f3cb3e76c02e02e85292236b5a6d1f660d7c109c4c5bead1` | Evidence-only sheet of immutable master, exact crop, v2 context, v3 raw/candidate, and canonical style reference at native/4x scale. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_v3_face_geometry_close_v95.png` | 2640x1140 RGB PNG | `5b93779a62f4c246481b3cae11007c99f400c1daf2c7d2b425271e028ab2c719` | Nearest-neighbour close comparison of the source crop face, raw v3 face, and processed v3 candidate face. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_leader_refs_native_4x_v93.png` | 2240x2320 RGB PNG | `117037e506cc125bdaa4e7d64a034172ccd75ef62a6439124fe1a9f83cb930fd` | Six curated male country-leader references at native and 4x nearest-neighbour scale; style controls only. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/manifest.md` | Package manifest | `5fa068f47ac723ffd8293aa6a41488eedfccee9faa8b768b97100a85fbc8e824` | Package-local v1/v2/v3 source, processing, prompt, shelf-copy, and no-wire ledger. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/hashes.sha256` | Hash ledger | `09d79f7e360da4719915c06f68b00b38ea7cff8d8b3f4a465e8d7a56cfd48c42` | Package hash entries for v2/v3 raw, candidate, shelf copy, and prompt records. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw043_chu_bolgar_civic_portrait_source_v90_2026_08_01.md` | Source-research handoff | `71e0e4c240639737ec993f3797aa5bb80ac085319812512d978ce4d7e2d69f5e` | Historical role/date, source URL, Commons rights record, collision check, and `needs_user_review` disposition. |

The canonical role family was `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/`. The package-specific sheet contains the six curated native `156x210` male leader references and their 4x nearest-neighbour views. They were used as style-family controls only and never as face sources.

## Gate findings

### Identity and likeness - PASS with source-resolution caveat

V3 corrects the prior v1/v2 blockers at native and 4x nearest-neighbour scale. The bald crown and high hairline remain source-matched with no invented fringe, the face is narrow and elongated rather than the earlier broader/rounder construction, the eyes are lower-set and less opened, and the asymmetry between eyelids and gaze is retained sufficiently for the low-resolution source. The long straight nose, thin closed mouth, hollow-cheek shading, compact chin, long jaw, large ears, neutral unsmiling expression, open white collar, and plain dark jacket remain visibly source-linked. The raw repaint and native candidate agree, and no face substitution, beauty retouching, symmetry correction, hat, hair, medal, insignia, jewelry, prop, modern object, or advisor frame is present.

The source does not support pixel-level confidence in the reconstructed eye, skin, or brush details. V3 still models the eyes and brows more clearly than the mug-shot crop and smooths some source grain, but it does not materially alter the visible broad geometry or identity anchors. Treat this as a bounded visual pass, not a license to add hidden detail; any further work must use the unchanged crop as sole identity authority and preserve the same low-set eye asymmetry, narrow face, long nose, thin mouth, and bald crown.

### HOI4 leader style and framing - PASS

The candidate is an opaque RGB `156x210` country-leader portrait with centered head-and-shoulders framing, restrained bust scale, subdued dark civilian clothing, a quiet muted warm-gray painted background, and readable native-scale contrast. It sits within the canonical male country-leader family. The matte brush texture is somewhat more modeled than the archival source but remains a controlled HOI4-style repaint rather than a photograph, modern concept render, dossier card, or generic officer image. No text, watermark, UI, advisor frame, or unsupported insignia is present.

### Provenance and chain - PASS

The unchanged master, exact crop, decoded-pixel equality JSON, v3 raw PNG, deterministic native candidate, v3 processing record, package-local v3 prompt, v3 shelf copy, package manifest, hash ledger, source-research handoff, and independent native/4x review sheets are present and hashable. The v3 prompt is now a package-local source-locked record, and the processing record names the fractional Pillow fit box. The existing durable ComfyUI pair remains tied to the original v1 source and is not misrepresented as v3 evidence; if v3 becomes the accepted runtime candidate after the rights decision, refresh that durable pair before final promotion. This queue note does not change the current provenance pass for the evidence-only v3 retry.

### Rights and date - HOLD (`needs_user_review`)

The source-research handoff identifies Karim Tinchurin (1887-1938), a Tatar dramatist, actor, director, and theatre organiser whose official theatre biography supports his civic/cultural role and confirms that he was alive in the 1936 baseline. The archival source is [Commons](https://commons.wikimedia.org/wiki/File:Karim_Tinchurin_mug_shots_(1937).jpg) with [original JPEG](https://upload.wikimedia.org/wikipedia/commons/6/6f/Karim_Tinchurin_mug_shots_%281937%29.jpg). The immutable Commons raw snapshot records date `1937`, author `NKVD`, `{{Pd-old}}`, and `{{PD-RU-exempt|type=mug shots}}`; the official Tinchurin State Theatre role snapshot is retained in the source package. The source is one year after the 1936 baseline, and the parent has not yet accepted the Russian mug-shot legal basis and post-baseline date for the intended release.

Role and identity evidence are strong, but the legal/date gate remains a separate non-compensable decision. Keep all v3 files at `needs_user_review` and do not infer rights acceptance from the visual pass.

### DDS promotion and runtime wiring - BLOCKED

No DDS conversion, `.gfx` admission, character edit, or runtime replacement was made. The stable intended consumer remains `CHU_independence_wave_bolgar_civic_presidium`, with the stable sprite `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium` and documented runtime path `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.dds`. Promotion is blocked by the rights/date HOLD; the existing v1 durable ComfyUI pair is not a runtime path.

## No-advisor-icon boundary

The reviewed asset is only a full `156x210` country-leader/civilian-large portrait candidate. No native `65x67` advisor, theorist, military-high-command, officer-corps, dossier, commander-small, operative, or `_small` derivative was created, reviewed as a substitute, or authorized. Preserve this boundary if the parent later admits v3.

## Required next action

1. Keep the unchanged master and exact crop immutable; use the exact crop as the sole identity authority for any future pass.
2. Record the parent's decision on the Commons NKVD mug-shot legal basis and the one-year post-baseline 1937 date; keep `needs_user_review` until that decision is explicit.
3. If rights/date are accepted, refresh the durable ComfyUI source/prompt pair from the accepted v3 lineage, then re-check the same identity anchors at native and 4x nearest-neighbour scale before DDS conversion.
4. Convert to DDS and wire the stable civilian-large sprite only after separate identity PASS, style PASS, provenance PASS, and rights/date acceptance; otherwise retain every v3 file as evidence-only.

**Final status: HOLD pending explicit rights/date review; v3 is the strongest bounded visual candidate but remains BLOCKED from DDS/runtime admission.**
