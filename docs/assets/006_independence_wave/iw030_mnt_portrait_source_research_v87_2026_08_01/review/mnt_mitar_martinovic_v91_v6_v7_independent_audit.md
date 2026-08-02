# IW-030 Mitar Martinovic v6/v7 independent portrait audit

Audit date: 2026-08-02.

Reviewer: independent Chaos Redux sourced-asset auditor (this audit was not produced by the ImageGen/processing producer).

Overall verdict: `needs_user_review`.

No DDS, `.gfx`, character, localisation, attestation, or gameplay promotion is authorized by this audit.

## Gate verdicts

| Gate | Verdict | Evidence and remaining condition |
| --- | --- | --- |
| Identity/likeness | `PASS` for v6 and v7 | At native 156x210 and 4x nearest-neighbour, both repaints retain the archival subject's distinctive cap crest, broad forehead, eye spacing/asymmetry, nose, large curled moustache, cheeks, jaw, expression, and shoulder alignment. No face substitution, genericization, beautification, or symmetrization was observed. |
| HOI4 style/framing | `PASS_WITH_NOTE` for v7; `needs_user_review` for v6 | Both are full `156x210` head-and-shoulders/upper-torso painted portraits with readable faces and period military clothing. v7 is the stronger candidate because its lighter neutral textured background is closer to the canonical leader/commander family; v6 retains a notably dark charcoal/olive background. Both still have heavy visible brush texture and colorized uniform/medal details that need human style sign-off. |
| Source/crop linkage | `PASS` | The unchanged master and explicit crop were rechecked with Pillow. The decoded crop equals the master rectangle `[80,90,610,760]` exactly, with equality SHA-256 `0c7f16cd55741be02cf693c2c0b6d5e92daee087ed873facb93ecb12a807b81f`; the retained crop JSON reports `status=exact_source_crop_verified` and `decoded_pixels_equal=true`. v6 is a source-locked repaint of that crop; v7 records a style-only refinement of v6. |
| Provenance/rights | `PASS_WITH_NOTE` | The package records the 1912 *Ilustrovana ratna kronika* / Serbian National Library scan chain, Commons file `Brigadir Mitar Martinović.jpg`, and `PD-collective-work|Serbia` basis for the underlying historical publication. Preserve the Commons/archive attribution and do not treat the NBS site-terms notice as a blanket waiver. |
| Male presentation | `PASS` | The unchanged archival source, v6, and v7 all present an adult male subject; no female name-pool or `female = yes` pairing is authorized by this evidence. |
| Role fit | `PASS_WITH_NOTE` | Package research identifies the subject as a Montenegrin divisional general, former prime minister and minister of war, and Lovćen Detachment commander. This supports a country-leader or corps-commander role only after the parent explicitly admits this identity as a new/replacement roster subject; it must not be relabeled as `MNT_kristo_popovic`. |
| Date/era fit | `PASS_WITH_NOTE` | The source photograph is dated 1912, while the subject lived 1870-1954 and remained alive in the 1936 scenario. The 24-year pre-scenario source age is an explicit era note, not a claim that the photograph was made in 1936. |
| Ownership/runtime admission | `BLOCKED_PENDING_PARENT` | This audit does not rerun the project/vanilla exact-identity ownership search and does not approve a new stable character key or transfer. Parent must rerun the guarded ownership check and accept a roster/design amendment before any runtime use. |

## Reviewed files and hashes

| File | Dimensions | SHA-256 | Review role |
| --- | ---: | --- | --- |
| `source_masters/mnt_mitar_martinovic_1912_chronicle.jpg` | 684x1135 RGB | `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76` | Immutable attributed archival identity master. |
| `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` | 530x670 RGB | `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` | Explicit head-and-shoulders identity crop. |
| `crop_metadata/mnt_mitar_martinovic_1912_crop.json` | — | `59868797792ab8d25c6a882ef32882609c719946d5b8439ad280eab53bbc9965` | Exact decoded-pixel equality evidence. |
| `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v6.png` | 1114x1412 RGB | `b9f1c5e0e28f0a1e12ebce80b14b935cfe31c32232a784c249bfe15c3073b80a` | Prior source-locked ImageGen repaint, evidence only. |
| `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v6.png` | 156x210 RGB | `4165007d39d70f45780e3615e5e000ea2d12296141d8d79710fcaedf59e9fac7` | Prior deterministic candidate, evidence only. |
| `generated_portraits/portrait_MNT_mitar_martinovic_processing_v6.json` | — | `9063d5aa40395b5c4e88906a91bdfbb6c8eddb33ccf46794e8eed349797ce57c` | v6 center crop `[27,0,1086,1412]`, Pillow LANCZOS, no padding/recolour. |
| `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v7.png` | 1080x1456 RGB | `d30891ac10f58dd080b2eeb85081efec9314d6e7e849ab91f8d01f9c05733b6d` | Constrained style-only refinement of v6, evidence only. |
| `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v7.png` | 156x210 RGB | `6b14b6cb8ef48b9c2b256bc331026448450e6dfbd409f4a9d19da6a8c6254501` | Preferred review candidate, deterministic resize, evidence only. |
| `generated_portraits/portrait_MNT_mitar_martinovic_processing_v7.json` | — | `e67122824e7b93798879cf486bd916b5cc30c211956f8dd3f77972743006b54c` | v7 full-width crop `[0,0,1080,1456]`, Pillow LANCZOS, no padding/recolour. |
| `review/mnt_mitar_martinovic_v91_v6_v7_portrait_audit_sheet.png` | 3240x2824 RGB | `e6d87aaa05904511a82fcbeb195072af9f37764a5882cd123195d30de0bd9365` | Native-source sequence plus exact 4x nearest-neighbour candidate/reference comparison sheet. |

## Native and enlarged comparison evidence

The unchanged master, exact crop, raw v6, raw v7, v6 candidate, v7 candidate, and role-specific canonical references were inspected directly at native resolution.

The v6 and v7 `156x210` candidates and the canonical leader references `fin_carl_mannerheim.png` and `ice_sveinn_bjornsson.png`, plus commander references `eng_bernard_montgomery.png`, `ger_erich_von_manstein.png`, and `ita_pietro_badoglio.png`, were also inspected at exact 4x nearest-neighbour scale.

Reference hashes used for the comparison are `fin_carl_mannerheim.png` `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`, `ice_sveinn_bjornsson.png` `860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14`, `eng_bernard_montgomery.png` `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e`, `ger_erich_von_manstein.png` `7bd74774884e907f4ca6289d20d31d7bfa2546b089b891588a2a8f9de722a71b`, and `ita_pietro_badoglio.png` `9f4f2a5a8d3260ab24866821d3c4edfc75d7bdb1cd0444124d518f7854890e9f`.

The review sheet is `review/mnt_mitar_martinovic_v91_v6_v7_portrait_audit_sheet.png`; its source/crop/raw panels are fitted for sequence context, while candidate/reference panels are exact 4x nearest-neighbour cards.

At native size, v7 has the clearest face/background separation and reads closest to the canonical painted portrait family.

At 4x, both candidates preserve the same facial landmarks and moustache silhouette as the crop; v7 improves background luminance and framing but retains a strong brush-texture signature and unverified colorization of grayscale source details.

No mere resized archival image was treated as a candidate, and neither candidate was approved for DDS conversion.

## Remaining gates and parent handoff

Use v7 as the stronger review candidate, while retaining v6 as prior evidence and not deleting it.

Parent must obtain human style approval, preserve the source/archive attribution, rerun the exact/variant ownership search and guarded transfer check, and explicitly admit Mitar Martinovic as a role-correct identity before assigning any runtime consumer.

Do not assign either candidate to `MNT_kristo_popovic` by relabeling, and do not create a DDS or `.gfx` sprite from this audit alone.

## Changed files in this audit tranche

- `review/mnt_mitar_martinovic_v91_v6_v7_portrait_audit_sheet.png` (new review artifact).
- `review/mnt_mitar_martinovic_v91_v6_portrait_audit_sheet.png` (earlier v6-only review artifact retained as prior evidence; 3240x1916 RGB, SHA-256 `f7acb3e113ec526b3007251484f337c5d0b60c7ea3589a9505eb6f8c6e31d829`).
- `review/mnt_mitar_martinovic_v91_v6_v7_independent_audit.md` (this evidence handoff).

No gameplay, characters, localisation, GFX, DDS, tags, attestation, or runtime files were changed.
