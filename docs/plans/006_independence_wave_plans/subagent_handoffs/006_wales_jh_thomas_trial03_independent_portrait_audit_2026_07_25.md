# IW-002 Wales J. H. Thomas trial-03 independent portrait audit

Date: 2026-07-25.

Reviewer: independent sourced-visual audit subagent; not the producer of the trial-03 package.

Decision: `PASS`.

Disposition: `approved_for_parent_conversion_only`; the parent may convert this exact candidate to DDS and perform the guarded WLS identity transfer after its own runtime/package checks.

No DDS, GFX, localisation, character, history, gameplay, advisor, dossier, operative, commander-small, `_small`, or fallback file was created or changed by this audit.

## Audit scope and evidence boundary

This audit covers only `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_j_h_thomas_trial_03/` and the retained source-clearance, vanilla-reference, and rejected-trial evidence needed to judge it.

I compared the unchanged archival master, explicit crop, crop-equality JSON, identity repaint prompt, raw ImageGen repaint, deterministic `156x210` candidate, processing metadata, retained review sheet, rejected trial-01 and trial-02 candidates, the full canonical Vanilla HOI4 country-leader reference sheet, the curated male leader quick-reference sheet, and the two processor-selected role references.

The required native and at-least-`4x` nearest-neighbour comparisons were inspected with disposable review renders outside the repository; those renders were review aids only and were deleted after inspection.

The trial-03 package remains source-only and contains exactly the expected nine evidence files: manifest, prompt, source master, exact crop, crop JSON, raw repaint, processed candidate, processing metadata, and review sheet.

The trial root contains no DDS, GFX, localisation, runtime copy, advisor or dossier derivative, operative derivative, commander-small derivative, `_small` derivative, female variant, generic substitute, or fallback portrait.

## Grounded identity, source provenance, and rights

The proposed subject is James Henry Thomas, commonly J. H. Thomas, a real male Welsh-born Newport trade-union leader and Labour politician who served as Secretary of State for the Colonies from 1935 to 1936.

This is a grounded real-person identity, so the sourced-real-person workflow is required and is correctly used.

The unchanged source is the Bain / Library of Congress George Grantham Bain Collection photograph with digital identifier `ggbain.29625`, recorded by Commons as James Henry Thomas circa 1920.

The retained local Commons snapshot `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_page_snapshots/j_h_thomas_commons_file_page.html` contains the Library of Congress identifier, the Bain attribution, circa-1920 date, `PD-Bain` category, and the Library of Congress no-known-copyright-restrictions notice.

The source page is `https://commons.wikimedia.org/wiki/File:James_Henry_Thomas_(1874-1949)_portrait.jpg`.

The rights record is sufficient for this source-only review, with the ordinary wording boundary that "no known copyright restrictions" and a Commons public-domain classification are retained as source evidence rather than a new legal opinion.

The circa-1920 source is compatible with an adult Thomas alive in the 1936 scenario, but it must not be described as a 1936 photograph or as proof that Thomas historically chaired the Event 006 Welsh National Council.

The source-clearance authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw002_wales_portrait_source_clearance_2026_07_25.md`.

## Recomputed artifact evidence

All hashes and dimensions below were recomputed from the current workspace bytes during this audit.

| Artifact | Dimensions and decode | SHA-256 | Independent result |
| --- | --- | --- | --- |
| `source_masters/WLS_j_h_thomas_circa_1920_master.jpg` | `3674x4977`, grayscale JPEG | `4f70ef8f6f2f970f5cd9216e15f65348dd92330be390389f2e2e717d0cec8cf5` | Unchanged attributed archival master. |
| `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.png` | `3000x4000`, grayscale PNG | `0b0b8e8ca7807939391a29c64a04f241c56e47e84ba649060f418fe71ef087be` | Exact decoded source crop. |
| `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.json` | JSON | `3c8e4aa25fdcd3b6c58dfe12b6495b1e62495ce969a4a91fa8a5c1d44ea380ec` | Crop-equality JSON with `decoded_pixels_equal: true`. |
| `identity_repaint_prompt.md` | Markdown | `a41e8e70d1984173b0fc844e0e8c9362ce5ec9e703ac7f6876764a7389d8d3c1` | Source-locked identity-preserving trial-03 brief. |
| `imagegen_results/WLS_j_h_thomas_identity_preserve_trial_03.png` | `1086x1448`, RGB PNG | `d92c267bd9ff55e97997a9fc3b3df4e78e17af2d17173f14f4d66deb8b0bfa8b` | Raw ImageGen repaint, used as the only processed-source input. |
| `processed_png/portrait_WLS_independence_wave_national_council.png` | `156x210`, opaque RGBA PNG | `d808b76d93363815f7e4fc953d4209a6d069fe9835724e975a6741a81a008a69` | Deterministic full-size leader candidate. |
| `processed_png/portrait_WLS_independence_wave_national_council.png.json` | JSON | `339e42157adf81582759b9889de0c88461273fa400d4889d2070e57f06a61c04` | Candidate metadata and integrity record. |
| `review/WLS_j_h_thomas_leader_style_sheet.png` | `1344x464`, opaque RGBA PNG | `d2eb87b4561ded5e6619de3a742dc721a925c1f7581d5d976cb05cdd07f1f221` | Processor review sheet containing input crop, candidate, and selected role references. |

The trial master and crop bytes are identical to the cleared-package master and crop bytes.

The source master and the crop equality JSON both report Pillow decoding, the half-open crop rectangle `(350,200,3350,4200)`, `3000x4000` output dimensions, and `decoded_pixels_equal: true`.

Independent Pillow re-cropping of the current master produced the same `3000x4000` decoded pixels and the same equality RGBA digest `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6` recorded by the utility.

The equality utility is `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, version `1.0`, with current file SHA-256 `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`.

The processor is `the retired portrait-processing utility`, version `5.0`, with current file SHA-256 `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`.

The candidate is opaque with alpha range `255..255`, has no advisor frame, dossier paper, transparent corners, or `_small` treatment, and is the correct full-size country-leader canvas.

## Source-only ImageGen lineage and deterministic processing

The trial-03 prompt explicitly says that the unchanged archival crop is the sole identity authority and that neither rejected trial nor any generated portrait may be supplied as an identity input.

The raw repaint is a genuine subdued oil/gouache-style HOI4 portrait reinterpretation rather than an unchanged photograph, colorized photograph, simple filter, or resized source.

The raw repaint is the sole `source_kind = real` processing input recorded in metadata, with crop `(0,0,1086,1448)`, `mode = leader`, and `role_family = leader`.

I replayed the exact processor invocation into a disposable repository-local audit directory and obtained the same candidate bytes and candidate SHA-256 `d808b76d93363815f7e4fc953d4209a6d069fe9835724e975a6741a81a008a69` and the same review-sheet SHA-256 `d2eb87b4561ded5e6619de3a742dc721a925c1f7581d5d976cb05cdd07f1f221`.

The replay confirms deterministic crop, grade, resize, and export behavior without changing the retained package.

The metadata state remains `candidate_requires_visual_approval`, which is correct for producer output; this independent handoff supplies the separate approval evidence and does not mutate the producer metadata.

## Canonical Vanilla HOI4 references

The role-specific canonical folder is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.

Its contact sheet contains eight full-size `156x210` leader references, including the selected `den_thorvald_stauning.png` and `fin_carl_mannerheim.png` references.

The matching curated male leader quick-reference folder is `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/`, whose contact sheet contains four full-size male references.

The selected canonical files were inspected at native size and at disposable nearest-neighbour enlargement.

| Reference | SHA-256 | Role evidence |
| --- | --- | --- |
| `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png` | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` | Full-size Vanilla civilian country-leader style reference. |
| `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png` | `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e` | Full-size Vanilla leader-family style reference. |

The processor review sheet is a style and framing aid and is not treated as identity evidence for Thomas.

The source master, exact crop, raw repaint, candidate, and canonical references were all compared separately; no canonical face was used to invent or replace Thomas's identity.

## Separate gate verdicts

| Gate | Verdict | Evidence and finding |
| --- | --- | --- |
| Attributed real-person archival source | `PASS` | Bain / Library of Congress George Grantham Bain Collection source, `ggbain.29625`, circa 1920, retained unchanged. |
| Provenance and rights record | `PASS` | Commons snapshot, Bain attribution, Library of Congress record, `PD-Bain`, no-known-copyright-restrictions notice, source URL, immutable master hash, and source-clearance handoff are retained. |
| Exact source crop | `PASS` | Pillow utility crop `(350,200,3350,4200)` reproduces the current crop exactly with matching equality digest and `decoded_pixels_equal: true`. |
| Source-locked ImageGen lineage | `PASS` | Trial-03 prompt and metadata identify the exact crop as sole identity input; the raw repaint hash matches metadata and no prior trial was used as an input. |
| Male identity presentation | `PASS` | The repaint is clearly one male-presenting adult subject; no female, collective, or invented person is present. |
| Civic country-leader role | `PASS` | Full-size civilian country-leader treatment matches the existing WLS national-council consumer and the subject's documented Welsh civic/political connection. |
| Historical wording boundary | `PASS` | The circa-1920 date is preserved and not presented as a 1936 photograph or documented historical WLS council chairmanship. |
| Exact identity and likeness | `PASS` | Trial-03 preserves every required non-compensable feature listed in the feature audit below at native and enlarged review scales. |
| HOI4 painted country-leader style | `PASS` | Restrained painted oil/gouache finish, controlled warm interwar palette, crisp identity-bearing face, quiet background, and no modern concept-art or photographic finish. |
| Native canvas and framing | `PASS` | Opaque `156x210` full-size portrait with complete head and hair, neck, bow tie, white collar, dark lapels, both shoulders, and no dossier frame. |
| Canonical reference-family fit | `PASS` | Leader-family references were inspected at native and >=4x nearest-neighbour scales; the candidate matches the full-size civilian leader surface without copying a reference face. |
| Current-project and reference-mod ownership | `PASS` | Current Chaos Redux and installed vanilla exact/variant identity searches returned no Thomas owner; the clearance authority also records no meaningful owner in Kaiserreich `1521695605` or approved mods `2265420196`/`1458561226`. |
| Stable WLS consumer declaration | `PASS` | Existing male token `WLS_independence_wave_national_council`, civilian-large sprite, and reserved runtime path are coherent; parent-owned transfer remains pending. |
| Forbidden derivative absence | `PASS` | No DDS, advisor/dossier, operative, commander-small, `_small`, female, generic, fallback, or alternate-country derivative exists in the trial root. |
| DDS/runtime readiness | `PASS for parent conversion gate` | No DDS is present by design; conversion and runtime/package equality remain parent-owned post-approval actions. |

## Non-compensable identity feature audit

Identity is judged against the unchanged archival master and exact crop first, with the raw repaint and deterministic candidate treated as the same trial-03 attempt.

| Required lock | Trial-03 finding | Verdict |
| --- | --- | --- |
| Unequal brow weight and slope | The image-left brow remains visibly heavier and more sloped than the image-right brow; the repaint does not regularize the brows into a matched pair. | `PASS` |
| Unequal eyelid openings | The image-left eye remains distinctly narrower and more hooded while the image-right eye remains more open, matching the source asymmetry. | `PASS` |
| Off-centre, slightly low gaze | The raw repaint and candidate retain the source's non-frontal, slightly lowered eye direction rather than the direct/upward look that remained in trials 01 and 02. | `PASS` |
| Long, narrow nose with rounded tip | The bridge remains long and narrow, the tip remains rounded, and the nostril silhouette stays asymmetric rather than broad or shortened. | `PASS` |
| Broad asymmetric drooping moustache | The moustache remains broad and dense with unequal drooping ends; it is not bushier, curled, waxed, upturned, or symmetrized. | `PASS` |
| Hollow cheek planes | The under-eye and cheek planes remain visibly hollow and unequal, with directional shading rather than a filled, smooth, beautified mid-face. | `PASS` |
| Defined broad jaw and rounded-square chin | The lower face remains broad with a defined jaw line and broad rounded-square chin instead of the softened round lower face seen in rejected trials. | `PASS` |
| Unequal ears | The image-left ear remains smaller and less exposed while the image-right ear remains larger and more exposed. | `PASS` |
| Coarse adult age texture | Forehead marks, under-eye lines, cheek texture, and adult age band remain readable in the raw repaint and candidate; the finish does not rejuvenate or age-progress him. | `PASS` |
| Stern closed mouth | The mouth remains closed and largely concealed by the moustache, with a restrained stern expression rather than a softened neutral smile. | `PASS` |
| Slight head angle | The facial offset, ear exposure, jaw shading, and unequal planes preserve the slight three-quarter angle instead of frontalizing the head. | `PASS` |
| Bow tie and white collar | The large asymmetric bow tie and white collar remain source-visible and correctly civilian. | `PASS` |
| Dark lapels and both shoulders | Both dark lapels and both shoulders remain inside the full leader frame without unsupported uniform, medals, or insignia. | `PASS` |

The trial-03 candidate corrects the specific non-compensable failures recorded for trials 01 and 02: trial 01 equalized the eyes and gaze, broadened and softened the nose, bushified and symmetrized the moustache, filled the cheeks, rounded the jaw and chin, softened ear asymmetry, smoothed age texture, and neutralized the expression; trial 02 improved some of those features but still raised and centered the gaze, regularized brows and moustache, filled the cheeks, softened the jaw/chin and age texture, and weakened the stern expression.

Trial-03 retains the source-specific asymmetries and lower-face geometry at native `156x210` and at the disposable >=4x nearest-neighbour inspection scale.

Style quality was evaluated separately and was not used to compensate for likeness.

## Stable consumer and runtime boundary

The live generated WLS token is `WLS_independence_wave_national_council` in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:257-273`, with `gender = male`, three civilian country-leader ideologies, and `set_portraits = { civilian = { large = GFX_portrait_WLS_independence_wave_national_council } }`.

The existing sprite declaration is `interface/006_independence_wave_region_01_portraits.gfx:62-65` and points to `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.

The current player-facing localisation remains Saunders Lewis until the parent performs its guarded transfer; this audit did not alter that identity.

No `_small` or dossier consumer was found for the WLS national-council token.

The existing runtime DDS, if inspected by the parent, must not be counted as Thomas approval or as a fallback for this candidate.

## Validation performed and intentionally skipped

- Recomputed trial-03 master, crop, crop JSON, prompt, raw repaint, candidate, processing metadata, review-sheet, and selected-reference hashes.
- Recomputed current master and crop dimensions, decode modes, alpha coverage, exact crop equality, metadata source SHA, candidate SHA, candidate dimensions, and selected-reference hashes.
- Confirmed trial-03 master and crop byte equality against the cleared J. H. Thomas source package.
- Replayed the deterministic leader processor into a disposable repository-local audit directory and confirmed byte-identical candidate and review-sheet output hashes, then removed that directory.
- Inspected the source master, exact crop, raw repaint, candidate, retained review sheet, rejected trial-01 and trial-02 raw/candidate evidence, canonical leader contact sheet, curated male quick-reference sheet, and selected Stauning/Mannerheim references.
- Inspected all required source/candidate/reference views at native scale and disposable >=4x nearest-neighbour scale, with closer face, eye, and lower-face nearest-neighbour views.
- Searched current Chaos Redux and installed vanilla runtime roots for exact and variant Thomas identity forms and found no owner; the source-clearance handoff records the corresponding Kaiserreich and approved-mod ownership scan.
- Enumerated the trial-03 root for forbidden derivative filenames and found none.
- Did not run DDS conversion, modify `.gfx`, modify localisation or characters, transfer Saunders Lewis, launch HOI4, or claim runtime proof because those actions belong to the parent after this independent source-only approval.

## Parent handoff and limits

The parent may convert only `processed_png/portrait_WLS_independence_wave_national_council.png` to the reserved `156x210` runtime DDS path after reviewing this PASS and performing its own converter/header/package-equality checks.

The parent owns the atomic identity transfer from Saunders Lewis to J. H. Thomas, including name and description localisation, character metadata, GFX/runtime synchronization, and any subsequent package audit.

No fallback, generic substitute, advisor/dossier asset, `_small` derivative, alternate-country portrait, or unrelated portrait is approved.

Final verdict: **PASS**.
