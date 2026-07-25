# Event 006 IW-002 Wales Lewis Pugh Evans trial 03 independent portrait audit

Audit date: 2026-07-25.

Auditor: independent Chaos Redux asset-audit subagent.

Scope: read-only audit of the unchanged archival master JPG and decoded PNG, exact source crop and equality JSON, trial 03 raw ImageGen result, deterministic `156x210` candidate and metadata, commander-family review sheet and references, rejected Evans trials 01 and 02, provenance and rights evidence, ownership evidence, stable WLS commandant consumer, and forbidden derivative surfaces.

Only this handoff was written. No source master, crop, raw ImageGen result, processed PNG, DDS, GFX, character, history, gameplay, localisation, advisor, dossier, `_small`, female, generic, alternate, or fallback asset was changed.

## Verdict

**FAIL closed — `blocked`; do not convert to DDS or wire.**

The package has a defensible attributed male Evans source, a valid Welsh commander role, exact decoded-pixel crop evidence, a real source-locked repaint record, correct `156x210` commander processing, complete commander-family references, and full framing. The separate non-compensable likeness gate nevertheless fails. Against the unchanged source at native and `4x` nearest-neighbour inspection, trial 03 regularizes the unequal eyes and ears, moves the gaze and head toward a more frontal centered pose, thickens and widens the pencil moustache, rounds and broadens the nose tip, softens the hollow cheek planes and narrow pointed jaw, and smooths the source's specific age texture. The result is a plausible painted British commander inspired by Evans, but not an acceptance-grade identity-preserving portrait. Style quality cannot compensate for this likeness failure.

## Gate checklist

| Gate | Verdict | Evidence and finding |
| --- | --- | --- |
| Provenance and rights | **PASS with disclosed caveat** | The immutable source is Imperial War Museums HU 93411, attributed to Henry Walter Barnett, circa 1918, retained as `source_masters/WLS_lewis_pugh_evans_iwm_hu93411.jpg` and the decoded PNG master. The retained Commons snapshot identifies the file as a photograph of Lieutenant Colonel Lewis Pugh Evans and records `PD-Old`/public-domain treatment. Preserve the IWM/Barnett credit and the territorial-rights caveat already recorded in the clearance package before any release. |
| Grounded identity, male presentation, and historical role | **PASS with wording caveat** | Lewis Pugh Evans was a real Welsh-born male British Army officer who commanded the 159th Welsh Border Infantry Brigade from 1933 through January 1938, so he was alive and in a Welsh formation command at the 1936 start. The source is circa 1918 and must not be described as a 1936 photograph. `mountain_frontier`/mountain commandant is a territorial-defence abstraction, not a claim that Evans served in a specialist mountain branch. |
| Unchanged master JPG and decoded PNG | **PASS** | The trial JPG is `605x800` RGB, SHA-256 `FDFDE87660F50EB9A2112186878FB8EE93B7C1F0E2CB9F533CA9B2C41C26012C`. Pillow decoding of that JPG is pixel-identical to `source_master_png/WLS_lewis_pugh_evans_iwm_hu93411_master.png`, whose file SHA-256 is `E63102DA467856B28A7E14659B100F870B2897BB5CD1232ACEAC6E54FD19A1F7`. Both trial copies are byte-identical to the cleared `wales_two_role_clearance` source copies. |
| Exact source crop and equality proof | **PASS** | `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png` is the Pillow crop `(left=60, top=20, right=580, bottom=730)`, `520x710` RGB, SHA-256 `7C12C4C993CBA694C495267C1BD9BC285151FD9CE88C01C53D1B83D789D2EBB4`. Its JSON SHA-256 is `D8AE94604E4F12C63529FA39AEFC38714D13E7ACC296EE05DEF8B0375DD3BA24`; the JSON records utility SHA-256 `14FA178D6DF999346874A7033E84F9B3AE988E7D845F3A4B2F8A44755E30641C`, Pillow `11.1.0`, `decoded_pixels_equal: true`, and matching RGBA digest `C3EE9B1D58E2A84EDC7AFB56446A390EE9EFBF3B7BE0B68AB1CC849DE1FD38` for the decoded master rectangle and crop output. |
| Source-locked ImageGen provenance | **PASS with no runtime authority** | The raw result `imagegen_results/WLS_lewis_pugh_evans_identity_preserve_trial_03.png` is `1079x1458` RGB, SHA-256 `74B1A1C5793036132851B214FBC1DE0BD6C4BEFC93599079C33D2D3ED09A6DBF`. `identity_repaint_prompt.md` (SHA-256 `B84BA941C7D529A96FEE1C36FD404070E81B0B4160BA11BFE38EA25627EBF639`) states that the exact Evans crop is the sole identity/composition input and that neither rejected trial is an ImageGen input. The prompt's explicit face, age, gaze, clothing, and gesture locks are the correct target, even though the result does not satisfy all of them. |
| Identity and likeness preservation | **FAIL — non-compensable** | At native and `4x` nearest-neighbour, the source's narrow elongated face, high forehead/receding temples, unequal brows and lids, off-centre gaze, long narrow nose, pencil moustache, hollow cheeks, narrow jaw/pointed chin, asymmetric ears, slight head angle, and source-visible age are not all preserved. Trial 03 improves the overall source pose and uniform gesture relative to the earlier attempts, but the raw repaint and candidate still open/regularize the eyes, reduce the ear asymmetry, center the gaze/head, thicken the moustache, broaden/round the nose tip, and soften the lean cheek/jaw planes. These are identity changes rather than an allowed painterly abstraction or crop difference. |
| HOI4 painted commander style | **PASS visually** | The candidate is a genuine subdued interwar painted portrait rather than a raw photograph, filter, generic icon, advisor card, or modern concept-art render. `portrait_WLS_independence_wave_mountain_commandant.png` is opaque RGBA `156x210`; its metadata records `role_family: commander`, the canonical commander directory, and the current processor SHA-256 `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC`. The dark military palette, quiet background, brush texture, and readable full portrait sit within the commander family, but this style PASS cannot override the likeness FAIL. |
| Full framing and source-visible uniform/gesture | **PASS** | The raw result and candidate retain the soft side cap, neck, collar and tie, shoulder seams, ribbon/medal details, both shoulders, forearms, gloves, hands, and the source upper-torso gesture inside the `156x210` canvas. No cap clipping, second person, text, watermark, or dossier frame is introduced. |
| Commander-family references and review evidence | **PASS** | The retained review sheet `review/WLS_lewis_pugh_evans_commander_style_sheet.png` is `1344x464` RGBA, SHA-256 `4C471ACF341BCCB5BFAAE1F75714915BFA160E13ED82BCC9E9601E41A07944A8`, and shows the processor input crop, processed candidate, `eng_bernard_montgomery.png`, and `ger_erwin_von_witzleben.png`. Both role-specific references are full `156x210` commander textures: Montgomery SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E`; Witzleben SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`. Native review-sheet inspection and disposable `4x` nearest-neighbour inspections were both performed; the sheet itself is review evidence, not approval. |
| Processing and metadata integrity | **PASS** | Candidate metadata SHA-256 is `DF48407FBE786977C83B2EC5153E9E387CA0EA7F6C7D8125528DC6D407346481`. Its canonical payload digest, output file digest, decoded RGBA digest, review digest, dimensions, and processor SHA all recompute exactly; the metadata remains `candidate_requires_visual_approval`. The candidate file SHA-256 is `3A41485403E291294B2C6956CAEBF68ECE5808D90F6D90B520A393F9BDBFF17` and its decoded RGBA digest is `52D5707056E57AAAA7EE9AFF0A0450872C44AF943A891F15101DC222BF700DF1`. |
| Prior rejected trials considered | **PASS for audit coverage; both remain rejected** | Trial 01 and trial 02 were re-read and compared as rejected evidence, not as inputs. Trial 01 raw/candidate hashes are `EBEDCB468C4BB724324277C922605BA538F6762230159025AABA04771BC4CFB8` and `EC90604F265225A6ED65BEC91612F4C7191D9AFEBDAF742C1F3F039D189D0091`; trial 02 raw/candidate hashes are `5F61603CCEA5C3BF302DDC2D37184654CBDB14573D0A080D8E9EE3D0789B45D2` and `3758F42C8E0C2A8DA2AEC8BF097C69C22DB2388C46D12EEB24C9260DC2D2EE44`. Their prior audits failed the same separate identity gate for eye/ear asymmetry, nose, moustache, jaw, gaze, and age drift; trial 03 must not be accepted by comparison with those failed outputs. |
| Portrait ownership | **PASS** | The cleared ownership scan searched exact and variant Evans terms across current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, and approved reference mods `2265420196` and `1458561226`, with no active character, recruitment, portrait, GFX, or localisation owner. The rejected trials and source package remain evidence only and do not create an ownership transfer. |
| Stable WLS commandant consumer | **PASS for declaration; parent reconciliation required after any future PASS** | `WLS_independence_wave_mountain_commandant` is generated as `gender = male` with a `corps_commander` and country-leader role in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:275-300`. `GFX_portrait_WLS_independence_wave_mountain_commandant` maps to `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` at `interface/006_independence_wave_region_01_portraits.gfx:66-69`, and the same full-size sprite is assigned to civilian and army `large`. Current localisation remains the generic role label `Mountain Commandant`; no player-facing Evans name or descriptor was changed because this candidate is blocked. |
| Advisor/dossier/`_small`/female/generic/fallback derivative absence | **PASS for this source-only package** | The trial 03 folder contains only the immutable master JPG/PNG, exact crop PNG/JSON, prompt, raw ImageGen PNG, processed `156x210` PNG/JSON, review sheet, and manifest. It contains no DDS, `.gfx`, advisor, dossier, commander-small, `_small`, female, alternate, generic portrait, or fallback derivative. The live source search has no WLS `_small` sprite/file registration. The existing full-size runtime DDS is a stale unrelated asset and is not part of this package or an accepted fallback. |
| Runtime readiness | **FAIL / intentionally blocked** | No DDS conversion or wiring is authorized because likeness fails. The existing `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` is an unrelated dark-haired generated man (legacy SHA-256 `39B165970C8067F5E19BCCD756C2A9D90641F51632BDE68AF738E9CCB808DC4F`, valid `156x210` BGRA header) and must not be counted as Evans approval or retained as a fallback. |

## Visual comparison record

I inspected the unchanged JPG, decoded PNG master, exact crop, raw trial 03 repaint, processed candidate, and both commander references at native size and at `4x` nearest-neighbour enlargement.

At native size the candidate is readable, fully framed, and recognisably derived from Evans, but the face reads as a generalized painted officer when placed beside the source crop. At `4x` nearest-neighbour the source's unequal eyelids and brows, wary off-centre gaze, one-sided ear exposure, long narrow nose, thin horizontal moustache, hollow cheek planes, narrow jaw, pointed chin, and slight head turn are visibly replaced or softened in the raw repaint and remain changed in the candidate. The moustache is the clearest hard failure: the source is a thin pencil line while the repaint makes it a denser, broader moustache. The eyes and head angle are also more open and frontal, and the nose tip and lower face are fuller and rounder than the immutable source.

The candidate keeps the cap, uniform, ribbon/medal bars, shoulders, forearms, gloves, hands, and gesture, and its restrained painterly finish is within the commander family. Those strengths do not compensate for the separate identity gate.

Disposable enlarged inspection files were created only under `%TEMP%\\wls_evans_trial03_audit` and were not added to the repository or used as runtime art.

## Evidence paths

### Trial 03 package

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/manifest.md`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/identity_repaint_prompt.md`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/source_masters/WLS_lewis_pugh_evans_iwm_hu93411.jpg`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/source_master_png/WLS_lewis_pugh_evans_iwm_hu93411_master.png`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.json`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/imagegen_results/WLS_lewis_pugh_evans_identity_preserve_trial_03.png`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/processed_png/portrait_WLS_independence_wave_mountain_commandant.png`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/processed_png/portrait_WLS_independence_wave_mountain_commandant.png.json`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wales_lewis_pugh_evans_trial_03/review/WLS_lewis_pugh_evans_commander_style_sheet.png`.

### Cleared source and ownership evidence

- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/manifest.md`.
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/manifest.json`.
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/research/source_clearance.md`.
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/ownership_scan.md`.
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/source_page_snapshots/lewis_pugh_evans_commons_file_page.html`.

### Prior rejected Evans trials

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_01/manifest.md` and its raw/candidate/review evidence.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_02/manifest.md` and its raw/candidate/review/metadata evidence.

### Canonical commander references and stable consumer

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md` commander rows.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png`.
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/README.md`.
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/REFERENCE_MANIFEST.md`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/eng_bernard_montgomery.png`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/ger_erwin_von_witzleben.png`.
- `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:275-300`.
- `interface/006_independence_wave_region_01_portraits.gfx:66-69`.
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml:7`.

## Required next step

Keep trial 03 and the stable WLS commandant consumer unwired. A future retry must preserve the source's narrow elongated facial geometry, receding temples/high forehead, unequal brows and eyes, off-centre gaze, long narrow nose, pencil moustache, hollow cheeks, narrow jaw/pointed chin, asymmetric ears, slight head angle, source-visible age, and exact cap/uniform/shoulder/hand gesture while retaining the commander-family painted treatment. Do not use the legacy runtime DDS as a fallback and do not create advisor, dossier, `_small`, female, generic, or alternate derivatives.

Final disposition: **`blocked` / `FAIL`; no runtime advancement.**

## Changed files and validation

- Changed documentation: this handoff only.
- No source, crop, raw ImageGen result, processed PNG, DDS, GFX, gameplay, character, history, localisation, advisor, dossier, `_small`, alternate, generic, female, or fallback file was changed.
- Meaningful validation: SHA-256, dimensions, modes, alpha range, metadata canonical digest, candidate/review decoded-pixel integrity, master JPG-to-PNG pixel equality, exact crop equality, byte identity with the cleared source copies, role-specific reference hashes, current processor hash, stable WLS consumer search, and absence of live WLS `_small` registration were rechecked read-only. Native and `4x` nearest-neighbour visual comparison covered the master, crop, raw result, candidate, and both commander references; prior Evans trials were compared as rejected evidence only.
- DDS conversion, runtime wiring, gameplay load testing, and source or processing reruns were skipped because the non-compensable likeness gate fails and the task explicitly forbids runtime advancement for a blocked candidate.
