# IW-002 Wales J. H. Thomas trial-01 independent portrait audit

Date: 2026-07-25.

Reviewer: independent sourced-visual audit subagent; not the producer of the trial package.

Decision: `FAIL`.

Disposition: `blocked` / `export-only`; do not convert this candidate to DDS or wire it to the WLS consumer.

Identity is a separate non-compensable gate. The usable HOI4 style and framing do not offset the likeness failure.

## Audit scope and source lineage

This audit covers only `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_j_h_thomas_trial_01/`.

I compared the unchanged archival master, exact crop, crop-equality JSON, repaint prompt, raw ImageGen result, deterministic `156x210` candidate, processing metadata, review sheet, and the two processor-selected canonical Vanilla HOI4 country-leader references.

The source-clearance authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw002_wales_portrait_source_clearance_2026_07_25.md`, delivered by commit `cb4250f59` (`Clear JH Thomas and Robert Ross Wales portrait sources`).

`git log` contains no later Wales-specific correction commit touching this J. H. Thomas source-clearance handoff or its clearance package; the current clearance evidence and the trial bytes were therefore audited as they exist in the workspace.

No source, crop, prompt, raw result, processed PNG, metadata, review sheet, DDS, GFX, localisation, character, history, gameplay, advisor, dossier, `_small`, or package file was edited by this audit.

## Grounded identity, provenance, rights, and role

The subject is James Henry Thomas (J. H. Thomas, 1874-1949), a real male Welsh-born Newport trade-union leader and Labour politician who served as Secretary of State for the Colonies from 1935 to 1936.

The identity is grounded and therefore correctly uses the sourced-real-person path rather than a generated officeholder.

The unchanged source is a Bain / Library of Congress George Grantham Bain Collection photograph, digital identifier `ggbain.29625`, recorded by Commons as circa 1920 with `PD-Bain` treatment and by the Library of Congress as having no known copyright restrictions.

The source is period-appropriate for an adult J. H. Thomas alive in the 1936 setting, but it is not a 1936 photograph and must not be described as one.

The civic or national-council role is historically bounded and plausible for an alternate-history WLS opening because Thomas was Welsh-born, connected to Newport and labour politics, and active in national government before the scenario start.

The package does not claim that Thomas historically chaired the Event 006 Welsh National Council.

The trial master and crop are byte-identical to the corresponding cleared-package copies. The crop JSON intentionally retains the canonical clearance-package paths; the independent byte and decoded-pixel checks below confirm that this path wording does not hide a replacement or resize.

## Recomputed artifact evidence

All file hashes below were independently recomputed from the current workspace bytes. Decoded-RGBA hashes use the repository domain-separated scheme (`chaos-redux-decoded-rgba-v1`, NUL, little-endian width and height, then RGBA bytes). The crop-equality digest is the plain RGBA digest recorded by the crop utility.

| Artifact | Decoded dimensions and mode | File SHA-256 | Decoded evidence |
|---|---:|---|---|
| `source_masters/WLS_j_h_thomas_circa_1920_master.jpg` | `3674x4977 L JPEG` | `4f70ef8f6f2f970f5cd9216e15f65348dd92330be390389f2e2e717d0cec8cf5` | domain RGBA `7dbddd8076736533564d9fa33ec58893fae7c94b8599d2860db698aef617c349` |
| `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.png` | `3000x4000 L PNG` | `0b0b8e8ca7807939391a29c64a04f241c56e47e84ba649060f418fe71ef087be` | equality RGBA `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6`; domain RGBA `3247d208dd2df2f21b7b73d5f2f61c3dc80ecef790d0d92036e3677e2a224b6c` |
| `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.json` | JSON | `3c8e4aa25fdcd3b6c58dfe12b6495b1e62495ce969a4a91fa8a5c1d44ea380ec` | `decoded_pixels_equal: true` |
| `identity_repaint_prompt.md` | Markdown | `eff8e8fccc2b5abbb4793a31b632d90f73ce6e4cc32eff16e58db9b0009f901e` | source-only crop and identity-preservation constraints retained |
| `imagegen_results/WLS_j_h_thomas_identity_preserve_trial_01.png` | `1082x1454 RGB PNG` | `2efe615fdec12cdccd811a87e6b9f123e24b15c3a002589364fbdef42a0f22f4` | domain RGBA `e1196ee0fa6e7e6f5aea37651015c37981eccb987ab06300db419a9a70860ec1` |
| `processed_png/portrait_WLS_independence_wave_national_council.png` | `156x210 RGBA PNG`, alpha `255..255` | `4412d588370735206a7a4a7abfbbd8e2d1d349aa29c8b8014aa21a556f813680` | domain RGBA `298b494097c9134b8fee0273747f7a083bd537362286c3bdde8bd1ebe38ea330` |
| `processed_png/portrait_WLS_independence_wave_national_council.png.json` | JSON | `ee0094f984baeb0482b28f55b903150d394a00ddb0489ea6da788d855a62549b` | metadata payload `740a30a50a54616a3dbb9d9b805f7cc2226c495bbd09a1154be406529d95d083` |
| `review/WLS_j_h_thomas_leader_style_sheet.png` | `1344x464 RGBA PNG`, alpha `255..255` | `242d5c2bdffa8dc863df3ce160c4d8632e0db1377f4126de9e19ff9175a02e5c` | domain RGBA `3f6b0b85995a977d03afbab8abae9bf8db947ce1e818f351b4269a502ed93652` |
| Canonical `den_thorvald_stauning.png` | `156x210 RGBA PNG` | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` | selected leader reference |
| Canonical `fin_carl_mannerheim.png` | `156x210 RGBA PNG` | `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e` | selected leader reference |

The exact crop rectangle is half-open `(350,200,3350,4200)` in decoded master pixels.

Independent Pillow decoding and cropping produced `3000x4000`, `12,000,000` pixels, and `decoded_pixels_equal: true` against the trial crop, with matching plain RGBA digest `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6`.

The processing metadata independently agrees with the current raw file, candidate file, review-sheet file, output dimensions, domain-separated candidate digest, review digest, processor `5.0`, `leader` mode, `leader` role family, source kind `real`, raw crop `(1,0,1081,1454)`, and selected Stauning/Mannerheim references.

## Visual review method

I inspected the unchanged master, exact crop, raw repaint, processed candidate, and retained review sheet at native resolution.

I inspected the canonical leader contact sheet and both selected Stauning and Mannerheim references at native resolution.

I generated disposable `4x` nearest-neighbour comparison renders outside the repository at `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial01_4x_nearest.png` and a closer face comparison at `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial01_face_8x_nearest.png`.

Those temporary renders were review aids only and are not source art, final art, or runtime inputs.

The retained leader review sheet is `1344x464` and shows the processor input crop, candidate, and selected role references at a 2x Lanczos display scale because the leader processor uses its leader-family review path. It is not itself a 4x nearest-neighbour sheet; the independent disposable renders supplied the required 4x nearest-neighbour inspection without changing package evidence.

## Separate gate verdicts

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Attributed real-person source | `PASS` | Bain / Library of Congress source, Commons `PD-Bain`, circa 1920, retained unchanged. |
| Rights and provenance | `PASS with record note` | Source page, attribution, date, rights record, immutable master hash, crop hash, prompt, raw result, processor metadata, and review sheet are retained. `portrait_provenance` is `null` in the leader metadata because no advisor overlay manifest is applicable; it does not replace the source rights record. |
| Exact source crop and equality JSON | `PASS` | Pillow crop `(350,200,3350,4200)` independently decodes to exact equality with matching `58ac...` RGBA digest. |
| Male presentation and grounded role | `PASS` | One male-presenting subject; full-size civilian country-leader role matches the existing WLS national-council surface. |
| Historical and era fit | `PASS with wording boundary` | Welsh-born Thomas was alive and politically active in 1936; the circa-1920 source must not be presented as a 1936 photograph or a documented historical WLS council chairmanship. |
| Exact identity and likeness | `FAIL (non-compensable)` | The raw repaint and deterministic candidate regularize source-specific asymmetry and materially drift in the eyes/gaze, facial planes, nose, moustache, mouth, ears, and age texture. |
| HOI4 painted country-leader style | `PASS` | Restrained oil/gouache treatment, warm interwar palette, full-size leader composition, readable face, no text/UI/watermark/modern props. The dark textured studio background is a minor style note only. |
| Native canvas and framing | `PASS` | Candidate is opaque `156x210`, contains the complete head, neck, bow tie, lapels, and both shoulders, and has no advisor frame or dossier border. |
| Current-project and reference-mod ownership | `PASS for exact candidate identity` | Current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, approved mod `2265420196`, and approved mod `1458561226` searches found no Thomas character, recruitment, portrait, GFX, or localisation owner. |
| Stable WLS consumer declaration | `PASS for declaration; transfer pending` | Existing male token, civilian-large sprite, and reserved DDS path are coherent; parent must perform any name/description/portrait transfer atomically after a passing candidate. |
| Advisor/dossier/operative/commander-small/`_small` absence | `PASS` | The trial root contains only the expected nine source/evidence files and no candidate-specific derivative; the live WLS national-council surface has no `_small` consumer. |
| DDS/runtime readiness | `BLOCKED` | No final DDS exists by design. The existing runtime DDS is a valid opaque `156x210` BGRA texture but decodes to a different photographic subject and is not Thomas approval or a fallback. |

## Detailed identity and likeness findings

Identity is judged against the unchanged archival master and exact crop first, with the raw repaint and processed candidate treated as the same attempted repaint because the candidate preserves the raw drift.

| Feature | Archival source | Raw repaint and `156x210` candidate | Identity finding |
|---|---|---|---|
| Forehead height | High, broad forehead with a large uninterrupted plane. | High forehead remains, but the painterly surface is smoother and the upper side contour is slightly softened. | Broad feature retained; minor smoothing does not rescue the other failures. |
| Receding hairline and side part | Strong receding side hairline and clear side part with sparse temple hair. | Side part and receding crown remain recognizable, but side hair reads a little fuller and more filled at the temples. | Minor hairline drift. |
| Brow weight | Heavy, unequal brows, with the viewer-left brow visibly weightier and more sloped. | Brows are dark and readable but more even in weight and slope. | Asymmetry is regularized. |
| Unequal eye openings and gaze | Viewer-left eye is distinctly narrower and more hooded; viewer-right eye is more open, with an off-centre, slightly lower-looking gaze. | Both eyes are more open and nearly equalized; catchlights and pupils read more directly and slightly higher/upward than the source. | Material eye regularization and possible upward-gaze shift; identity gate fails. |
| Nose length and rounded tip | Long, prominent, narrow bridge ending in a rounded tip with source-specific nostril asymmetry. | Bridge is softer and somewhat broader, with a fuller/shorter-looking tip and less source-specific nostril asymmetry. | Nose geometry drifts beyond painterly variation. |
| Moustache width, droop, and ends | Thick moustache is broad, dense, asymmetric, and visibly droops at the ends. | Moustache becomes bushier and more uniformly dark, with more symmetric curled or upturned ends and less of the source droop. | Explicit moustache drift; identity gate fails. |
| Mouth | Closed, serious mouth largely hidden beneath the drooping moustache. | Mouth reads softer and more directly neutral, with a more visible/full lower lip under the repaint moustache. | Expression and mouth geometry drift. |
| Face length and width | Long facial proportions with a broad forehead and source-specific taper through the lower face. | Mid-face and lower face are smoother and rounder, reducing the source's long, structured planes. | Face genericization is visible at native and 4x. |
| Cheeks | Unequal cheek planes with visible source texture and hollowness under the eyes. | Cheeks are fuller, smoother, and more symmetrical, with reduced source hollowness. | Cheek asymmetry and plane structure are lost. |
| Jaw and chin | Defined lower jaw and broad, rounded-square chin. | Jaw and chin read rounder and less defined, with a softer taper. | Lower-face geometry drifts. |
| Ears | Viewer-left ear is compact and partly integrated into the cheek; viewer-right ear is more exposed and larger. | Ear exposure is more even, with the viewer-left ear enlarged and the right-ear asymmetry softened. | Ear asymmetry is regularized. |
| Source age | Circa-1920 adult face with forehead marks, under-eye lines, and coarse photographic skin texture. | Adult age band remains plausible, but skin is smoother and slightly more beautified/younger-looking. | Age texture is softened; this compounds the identity drift. |
| Expression | Restrained, stern, closed-mouth expression. | Softer, more direct, and more neutral expression. | Expression drift is visible. |
| Pose and head angle | Near-frontal with a slight three-quarter angle and source-specific facial offset. | Overall pose remains, but the face and gaze read a little more frontal. | Pose broadly retained; frontalization contributes to the likeness failure. |
| Bow tie and lapels | Large asymmetric bow tie with distinctive tails, white collar, and dark suit lapels. | Bow tie, collar, and lapels remain source-visible with no unsupported insignia, but folds and asymmetry are simplified. | Clothing/role framing passes; small shape drift is not identity-compensating. |
| Shoulders | Both shoulders and the broad suit silhouette are visible. | Both shoulders remain inside the full leader frame with a compatible suit silhouette. | Framing passes. |

The raw repaint is a genuine painted reinterpretation rather than a raw photograph, colourized photograph, or simple filter, but the source-specific face is not preserved strictly enough for a grounded real-person portrait.

## Stable consumer and runtime boundary

The current generated WLS token is `WLS_independence_wave_national_council` in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:257-273`, with `gender = male`, three civilian country-leader ideologies, and `set_portraits = { civilian = { large = GFX_portrait_WLS_independence_wave_national_council } }`.

The existing sprite declaration is `interface/006_independence_wave_region_01_portraits.gfx:62-65` and points to `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.

The current player-facing identity remains `Saunders Lewis` with a Saunders-specific description at `localisation/english/006_independence_wave_scotland_wales_l_english.yml:5-6`.

The reserved runtime DDS currently exists as a valid one-level BGRA `156x210` texture (`131168` bytes; file SHA-256 `12ca49ed34c4d84b4135e580baa1c36994dc391baade62d02dbd80e1fd1fed05`) but decodes to an unrelated photographic subject. It must not be counted as a Thomas result, used as a likeness fallback, or silently left as evidence of this candidate.

No exact or variant J. H. Thomas owner was found in the current project, installed vanilla, Kaiserreich `1521695605`, approved mod `2265420196`, or approved mod `1458561226`. This clears the additive source-ownership gate, but it does not authorize replacing the current Saunders Lewis identity until a candidate passes likeness and the parent performs the guarded name, description, DDS, and evidence transfer.

No advisor, dossier-card, operative, commander-small, `_small`, alternate-country, generic, female, or fallback derivative was created or found for this trial package.

## Validation performed and intentionally skipped

- Recomputed master, crop, crop JSON, prompt, raw, candidate, metadata, review-sheet, and selected-reference hashes.
- Recomputed source and crop dimensions, modes, alpha coverage, processor metadata payload hash, domain-separated decoded-RGBA hashes, and exact crop equality.
- Confirmed trial master and crop byte equality against the cleared J. H. Thomas source package.
- Inspected source master, exact crop, raw repaint, candidate, processor review sheet, canonical leader contact sheet, Stauning, Mannerheim, and the existing reserved runtime DDS decode at native size.
- Inspected source, raw, candidate, and role references in disposable 4x nearest-neighbour comparisons outside the repository.
- Searched current Chaos Redux, installed vanilla, and approved reference-mod ownership roots for exact and variant Thomas identity forms.
- Enumerated the trial root and live WLS portrait surface for advisor, dossier, operative, commander-small, `_small`, generic, alternate, and fallback derivatives.
- Did not run DDS conversion, modify `.gfx`, modify localisation or characters, transfer the stable identity, launch HOI4, or claim runtime proof because the non-compensable likeness gate fails and the task explicitly forbids those mutations.

## Required disposition and parent follow-up

This trial is `FAIL / blocked / export-only`.

The parent must not convert the candidate to DDS, replace the existing runtime texture, or rename the WLS localisation from Saunders Lewis using this candidate.

A future source-locked repaint must preserve the photographed unequal eyelid openings and gaze, brow-weight asymmetry, long narrow rounded-tip nose, broad drooping asymmetric moustache and ends, long facial planes, cheek hollowness, jaw/chin geometry, ear exposure, source age texture, stern expression, and slight head angle while retaining the full civilian bow-tie-and-lapel framing.

No fallback, generic substitute, advisor/dossier asset, `_small` derivative, or unrelated portrait is approved.

Final verdict: **FAIL.**
