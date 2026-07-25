# IW-002 Wales J. H. Thomas trial-02 independent portrait audit

Date: 2026-07-25.

Reviewer: independent sourced-visual audit subagent; not the producer of the trial package.

Decision: `FAIL / rejected_and_unwired`.

Disposition: `blocked` / `export-only`; do not convert this candidate to DDS, replace the reserved WLS runtime texture, or wire the candidate to the WLS consumer.

Identity is a separate non-compensable gate. Trial-02 improves several trial-01 features, but it still regularizes or softens enough source-specific geometry, gaze, age, and expression that likeness approval is not defensible.

## Audit scope and no-mutation boundary

This audit covers only `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_j_h_thomas_trial_02/` and compares it with the rejected `wales_j_h_thomas_trial_01/` package.

I compared the unchanged archival master, exact crop, crop-equality JSON, trial-02 repaint prompt, raw ImageGen result, deterministic `156x210` candidate, processing metadata, retained review sheet, rejected trial-01 candidate, and the two processor-selected canonical Vanilla HOI4 country-leader references.

The source-clearance authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw002_wales_portrait_source_clearance_2026_07_25.md`, delivered by commit `cb4250f59` (`Clear JH Thomas and Robert Ross Wales portrait sources`).

No source, crop, prompt, raw result, processed PNG, metadata, review sheet, DDS, GFX, localisation, character, history, gameplay, advisor, dossier, `_small`, fallback, or package file was edited by this audit.

The trial-02 package contains the expected nine source/evidence files: manifest, repaint prompt, source master, exact crop, crop JSON, raw repaint, processed candidate, processing metadata, and review sheet. It contains no `gfx_handoff.md`, DDS, runtime copy, advisor/dossier/operative/commander-small derivative, `_small` derivative, female portrait, generic substitute, or fallback portrait. That omission is intentional while the candidate is blocked.

## Grounded identity, provenance, rights, and role

The subject is James Henry Thomas (J. H. Thomas, 1874-1949), a real male Welsh-born Newport trade-union leader and Labour politician who served as Secretary of State for the Colonies from 1935 to 1936.

The identity is grounded and correctly uses the sourced-real-person path rather than a generated officeholder. The source page is `https://commons.wikimedia.org/wiki/File:James_Henry_Thomas_(1874-1949)_portrait.jpg`.

The attributed source is Bain / Library of Congress George Grantham Bain Collection digital `ggbain.29625`, recorded as circa 1920. The package records Commons `PD-Bain` treatment and the Library of Congress no-known-copyright-restrictions record. The source is period-compatible for an adult Thomas alive in the 1936 setting, but it is not a 1936 photograph and must not be described as one.

The civic or national-council role is historically bounded and plausible for an alternate-history WLS opening because Thomas was Welsh-born, connected to Newport and labour politics, and active in national government before the scenario start. The package does not claim that he historically chaired the Event 006 Welsh National Council.

Trial-02 starts from the unchanged cleared crop and does not use trial-01, another generated face, or a style portrait as an identity input. The trial-02 master and crop are byte-identical to the cleared-package copies.

## Recomputed artifact evidence

All file hashes below were independently recomputed from the current workspace bytes. Decoded-RGBA hashes use the repository domain-separated scheme (`chaos-redux-decoded-rgba-v1`, NUL, little-endian width and height, then RGBA bytes). The crop-equality digest is the plain RGBA digest recorded by the crop utility.

| Artifact | Decoded dimensions and mode | File SHA-256 | Decoded or integrity evidence |
| --- | ---: | --- | --- |
| `source_masters/WLS_j_h_thomas_circa_1920_master.jpg` | `3674x4977 L JPEG` | `4f70ef8f6f2f970f5cd9216e15f65348dd92330be390389f2e2e717d0cec8cf5` | domain RGBA `7dbddd8076736533564d9fa33ec58893fae7c94b8599d2860db698aef617c349` |
| `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.png` | `3000x4000 L PNG` | `0b0b8e8ca7807939391a29c64a04f241c56e47e84ba649060f418fe71ef087be` | equality RGBA `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6`; domain RGBA `3247d208dd2df2f21b7b73d5f2f61c3dc80ecef790d0d92036e3677e2a224b6c` |
| `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.json` | JSON | `3c8e4aa25fdcd3b6c58dfe12b6495b1e62495ce969a4a91fa8a5c1d44ea380ec` | `status: exact_source_crop_verified`; `decoded_pixels_equal: true` |
| `identity_repaint_prompt.md` | Markdown | `9fcbdb587cabd1100c25273d1e92925156c4d3da4b6f8866fc9450dc54d1e69a` | source-only trial-02 locks retained |
| `imagegen_results/WLS_j_h_thomas_identity_preserve_trial_02.png` | `1080x1456 RGBA PNG` | `22f880f443cdee78eb992922f8a48709b6bc08f4bd6456cf024c7c4094caa248` | domain RGBA `45ada6b618fe5911ae1dd6d0cb011e092024ddeb56bd03582a14d44e8696947d` |
| `processed_png/portrait_WLS_independence_wave_national_council.png` | `156x210 RGBA PNG`, alpha `255..255` | `7b352adba5a88ffa783ece46c1d6eef654261522529670bc112430a4eed57c8c` | domain RGBA `f6725767509bd93962f31cf7ef08d2e7a47143c8e34f54ff656ea4d12028376a` |
| `processed_png/portrait_WLS_independence_wave_national_council.png.json` | JSON | `73b0048591dd19ca19e804706623f22b8dec6332f578a9e30bcac28b0cb93883` | metadata payload `d0e0fd2e90e7f79101121dfd4249711d21709ed5dbb0266d51a03b7ce3dc5f24`; recomputed match `true` |
| `review/WLS_j_h_thomas_leader_style_sheet.png` | `1344x464 RGBA PNG`, alpha `255..255` | `e5c067ffa498c57011ad2600b9f6e373a38b519c45d2d2aeed40257b1356ead6` | domain RGBA `2629573dcad4019a3481e2b9d22d2964877e19b2554cd00ea5a28ad2d02afb17` |
| Canonical `den_thorvald_stauning.png` | `156x210 RGBA PNG` | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` | selected civilian country-leader reference |
| Canonical `fin_carl_mannerheim.png` | `156x210 RGBA PNG` | `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e` | selected civilian country-leader reference |

The exact crop rectangle is half-open `(350,200,3350,4200)` in decoded master pixels. Independent Pillow decoding and cropping produced `3000x4000`, `12,000,000` pixels, and `decoded_pixels_equal: true` against the trial-02 crop, with matching plain RGBA digest `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6`.

The trial-02 master file SHA matches the clearance master SHA, and the trial-02 crop file SHA matches the clearance crop SHA. The copied crop JSON intentionally retains canonical clearance-package paths; the independent byte, dimensions, and decoded-pixel checks confirm that the path wording does not hide a replacement or resize.

The metadata independently agrees with the current raw SHA, raw decoded RGBA digest, candidate SHA and decoded digest, review-sheet SHA and decoded digest, `156x210` output dimensions, processor `5.0`, `leader` mode, `leader` role family, source kind `real`, raw crop `(0,1,1080,1455)`, and selected Stauning/Mannerheim references.

## Visual review method

I inspected the unchanged source master and exact crop at native resolution, then inspected the raw trial-02 repaint, processed candidate, retained review sheet, rejected trial-01 candidate, canonical leader contact sheet, and both selected canonical references at native resolution.

I generated disposable review-only renders outside the repository at `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial02_4x\comparison_4x_nearest_labeled.png`, `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial02_4x\face_comparison_8x_nearest_labeled.png`, `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial02_4x\feature_face_8x_nearest_labeled.png`, `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial02_4x\eyes_20x_nearest_labeled.png`, `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial02_4x\lower_face_20x_nearest_labeled.png`, and `C:\Users\klimp\AppData\Local\Temp\wales_jh_thomas_trial02_4x\forehead_brow_20x_nearest_labeled.png`.

The temporary renders normalize the source crop and raw repaint to the candidate frame for side-by-side inspection and enlarge with nearest-neighbour only. They are review aids, not source art, final art, or runtime inputs.

The retained leader review sheet is `1344x464` and shows the processor input crop, candidate, and selected role references at the processor's leader-family display scale. It is not itself the required independent 4x nearest-neighbour audit; the disposable renders supplied that enlarged inspection without changing package evidence.

## Separate gate verdicts

| Gate | Verdict | Evidence and finding |
| --- | --- | --- |
| Attributed real-person source | `PASS` | Bain / Library of Congress source, Commons `PD-Bain`, circa 1920, retained unchanged. |
| Rights and provenance | `PASS with record note` | Source page, attribution, date, rights record, immutable master/crop hashes, crop-equality JSON, source-only prompt, raw result, processor metadata, and review sheet are retained. `portrait_provenance` is `null` in leader metadata because no advisor overlay manifest applies; it does not replace the source rights record. |
| Exact source crop and equality JSON | `PASS` | Pillow crop `(350,200,3350,4200)` independently decodes to exact equality with matching `58ac...` RGBA digest. |
| Male presentation and grounded role | `PASS` | One male-presenting subject; full-size civilian country-leader role matches the existing WLS national-council surface. |
| Historical and era fit | `PASS with wording boundary` | Welsh-born Thomas was alive and politically active in 1936; the circa-1920 source must not be presented as a 1936 photograph or as documented historical WLS council-chair evidence. |
| Trial-02 source lineage | `PASS` | Trial-02 uses the exact cleared crop and does not use trial-01 or any generated substitute as identity input. |
| Exact identity and likeness | `FAIL (non-compensable)` | Trial-02 improves eye-opening asymmetry and nose/moustache direction relative to trial-01, but still makes gaze more direct, regularizes brow and moustache asymmetry, fills/smooths cheeks, softens the jaw/chin and age texture, and weakens the stern source expression. |
| HOI4 painted country-leader style | `PASS` | Restrained oil/gouache treatment, warm desaturated interwar palette, full-size leader composition, readable face, quiet studio background, and no text, watermark, UI border, modern props, uniform, medals, or insignia. |
| Native canvas and framing | `PASS` | Candidate is opaque `156x210`, includes complete hair and head, neck, large bow tie, white collar, dark lapels, both shoulders, and no advisor/dossier frame. |
| Current-project and reference-mod ownership | `PASS for exact candidate identity` | The clearance authority found no meaningful Thomas owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196`/`1458561226`. This does not override the failed likeness gate. |
| Stable WLS consumer declaration | `PASS for declaration; transfer blocked` | Existing male token, civilian-large sprite, and reserved DDS path are coherent; parent must not perform the identity transfer with this candidate. |
| Advisor/dossier/operative/commander-small/`_small` absence | `PASS` | The trial-02 root has no candidate-specific derivative, and the live WLS national-council consumer has no `_small` slot. |
| DDS/runtime readiness | `BLOCKED` | No final DDS exists in trial-02 by design. The existing runtime DDS is an unrelated photographic subject and is not Thomas approval or a fallback. |

## Detailed identity and likeness findings

Identity is judged against the unchanged archival master and exact crop first, with raw trial-02 and its deterministic candidate treated as the same attempted repaint. Trial-01 is used only as a rejected comparison, never as a source.

| Source-specific lock | Archival source | Trial-02 raw repaint and `156x210` candidate | Finding |
| --- | --- | --- | --- |
| Forehead height and hairline | High broad forehead, strong recession, sparse temple hair, and clear side part. | High forehead and receding side part remain recognizable; the temple contour is slightly softened but not materially replaced. | `PASS` for this subfeature. |
| Unequal brow weight | Heavy, unequal brows with a visibly different slope and weight on the two sides. | Both brows are dark and readable, but their weight and slope are closer to one another than in the photograph. | `FAIL` for the exact source lock; asymmetry is partly retained but regularized. |
| Unequal eyelid openings | Viewer-left eye is distinctly narrower and more hooded than viewer-right. | Trial-02 keeps a visibly narrower viewer-left opening and a more open viewer-right opening, improving on the most obvious trial-01 equalization. | `PASS` for opening asymmetry, but not sufficient for overall identity approval. |
| Gaze | Off-centre and slightly lower-looking rather than a direct or upward look. | Pupils and catchlights read more centered/direct and slightly higher than the source in the raw and native candidate. | `FAIL`; the trial-01 direct/upward drift is reduced but not eliminated. |
| Nose length, bridge, tip, and nostrils | Long prominent narrow bridge, rounded tip, and source-specific nostril asymmetry. | Trial-02 retains a long narrow bridge and a rounded tip without the pronounced trial-01 broadening; nostril asymmetry is less photographic but remains plausible. | `PASS` for this subfeature, with minor painterly simplification. |
| Moustache width, density, droop, and ends | Broad dense asymmetric moustache with clearly drooping ends and a closed mouth mostly hidden beneath it. | Trial-02 is less curled and less bushy than trial-01 and retains a broad moustache, but the two ends read more even and less distinctly drooping than the photograph. | `FAIL` for the exact source lock; partial improvement only. |
| Long facial planes | Long face with structured forehead, under-eye, cheek, and lower-face planes. | Overall face length remains, but the cheek-to-jaw transitions are smoother and the lower planes are less structured and more generic. | `FAIL` for the source-specific plane lock. |
| Cheek hollowness | Unequal hollow cheek planes and visible under-eye structure. | Mid-face is visibly fuller and smoother, especially through the photographed hollow areas; asymmetry is reduced. | `FAIL`; this is an explicit trial-02 rejection condition. |
| Jaw and chin | Defined jaw and broad rounded-square chin. | Lower face is softer and rounder, with a less defined jaw and a narrower/rounder chin impression than the source. | `FAIL`; this is an explicit trial-02 rejection condition. |
| Ear exposure | Viewer-left ear compact and partly hidden; viewer-right ear larger and more exposed. | Viewer-left ear remains compact and viewer-right remains more exposed; no material left-ear enlargement is visible. | `PASS` for this subfeature. |
| Source age texture | Circa-1920 adult face with coarse photographic texture, forehead marks, and under-eye lines. | Painterly texture is present, but forehead marks, cheek texture, and some under-eye age structure are smoothed and the face reads slightly beautified/younger. | `FAIL`; the source-age lock is not fully preserved. |
| Stern expression and mouth | Restrained stern closed mouth mostly concealed by the moustache. | Mouth remains closed, but the lower lip is more visible and the expression reads softer, more neutral, and more direct than the source. | `FAIL`; expression drift remains. |
| Slight head angle | Slight three-quarter facial offset with source-specific asymmetry. | Ear and jaw asymmetry retain a small offset, but the face and gaze are more frontal/direct than the photograph. | `FAIL` for the full pose lock; broad framing is retained. |
| Bow tie and collar | Large asymmetric bow tie, white collar, and distinctive tails. | Large bow tie and collar remain visible with a broadly similar asymmetry; folds and small details are simplified. | `PASS` for role/framing, not identity-compensating. |
| Dark lapels and both shoulders | Dark suit lapels and both shoulders fill the source head-and-shoulders composition. | Dark lapels and both shoulders remain fully inside the `156x210` leader frame with no unsupported insignia. | `PASS` for framing and clothing surface. |

The trial-02 raw repaint is a genuine painted reinterpretation rather than a raw photograph, colourized photograph, or simple filter. That style pass cannot compensate for the remaining source-specific identity failures.

## Stable WLS consumer and runtime boundary

The live generated WLS token is `WLS_independence_wave_national_council` in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:257-273`, with `gender = male`, three civilian country-leader ideologies, and `set_portraits = { civilian = { large = GFX_portrait_WLS_independence_wave_national_council } }`.

The existing sprite declaration is `interface/006_independence_wave_region_01_portraits.gfx:62-65` and points to `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.

The current player-facing identity remains `Saunders Lewis` with a Saunders-specific description at `localisation/english/006_independence_wave_scotland_wales_l_english.yml:5-6`. No name, description, character token, GFX declaration, DDS, or gameplay transfer was made by this audit.

The reserved runtime DDS exists as a valid opaque one-level `156x210` BGRA texture with `131168` bytes and file SHA-256 `12ca49ed34c4d84b4135e580baa1c36994dc391baade62d02dbd80e1fd1fed05`. Pillow decodes it as a photographic young man in a dark work shirt, not J. H. Thomas. It must not be counted as a Thomas result, used as a likeness fallback, or silently treated as evidence for trial-02.

No exact or variant J. H. Thomas owner was found in the clearance scan for current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`. This clears the additive source-ownership gate only; it does not authorize replacing Saunders Lewis while the candidate fails likeness.

No advisor, dossier-card, operative, commander-small, `_small`, alternate-country, generic, female, or fallback derivative was created or found for trial-02.

## Validation performed and intentionally skipped

- Recomputed trial-02 master, crop, crop JSON, prompt, raw, candidate, metadata, review-sheet, and selected-reference hashes.
- Recomputed source and crop dimensions, modes, alpha coverage, processor metadata payload hash, domain-separated decoded-RGBA hashes, and exact crop equality.
- Confirmed trial-02 master and crop byte equality against the cleared J. H. Thomas source package.
- Confirmed the metadata payload hash recomputes exactly to `d0e0fd2e90e7f79101121dfd4249711d21709ed5dbb0266d51a03b7ce3dc5f24`.
- Inspected source master, exact crop, raw trial-02 repaint, native candidate, trial-01 candidate, retained trial-02 review sheet, canonical leader contact sheet, Stauning, Mannerheim, and the existing reserved runtime DDS decode.
- Inspected source, raw, candidate, rejected comparison, and role references at native and disposable 4x nearest-neighbour enlargement, with closer 8x/20x nearest-neighbour feature comparisons outside the repository.
- Confirmed that trial-02 contains no DDS, GFX edit, runtime copy, `gfx_handoff.md`, advisor/dossier/operative/commander-small derivative, `_small` derivative, generic substitute, or fallback portrait.
- Did not run DDS conversion, modify `.gfx`, modify localisation or characters, transfer the stable identity, launch HOI4, or claim runtime proof because the non-compensable likeness gate fails and this audit owns no runtime wiring.

## Residual risks and parent follow-up

The circa-1920 source remains an era-fit wording boundary for a 1936 alternate-history civic role. Any future handoff must preserve the source date and must not imply that Thomas historically chaired the Event 006 council.

The next repaint attempt must use the unchanged cleared crop as its sole identity input and must not use either generated trial as a reference. It needs a visibly off-centre lower gaze, stronger brow-weight asymmetry, the broad drooping asymmetric moustache ends, hollow cheek planes, defined broad jaw/chin, coarse adult age texture, stern closed-mouth expression, and slight facial offset without changing the bow-tie-and-lapel framing.

No fallback, generic substitute, advisor/dossier asset, `_small` derivative, or unrelated portrait is approved. The current Saunders Lewis identity remains wired until a later candidate independently passes every gate and the parent performs the guarded atomic name, description, DDS, and runtime transfer.

Final verdict: `FAIL / rejected_and_unwired`.
