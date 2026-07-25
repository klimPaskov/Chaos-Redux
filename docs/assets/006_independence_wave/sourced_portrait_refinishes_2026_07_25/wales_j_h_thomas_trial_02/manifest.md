# IW-002 Wales J. H. Thomas portrait trial 02

Status: `rejected_and_unwired`.

Independent audit verdict: `FAIL`.

No DDS conversion, character transfer, localisation change, GFX edit, package attestation, or runtime wiring is authorized for this rejected candidate.

This package contains no advisor, dossier, operative, commander-small, `_small`, female, generic, or fallback portrait.

## Stable consumer

| Field | Value |
| --- | --- |
| Package | IW-002 Wales, vanilla carrier `WLS` |
| Existing dynamic character token | `WLS_independence_wave_national_council` |
| Existing sprite | `GFX_portrait_WLS_independence_wave_national_council` |
| Runtime path after approval | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` |
| Current unwired working identity | Saunders Lewis |
| Proposed sourced identity | James Henry Thomas, commonly J. H. Thomas |
| Role family | Full-size civilian country leader |
| Authorized portrait surface | Existing `civilian.large` consumer through the same sprite |

## Historical and ownership boundary

J. H. Thomas was a real male Welsh-born Newport trade-union leader and Labour politician who served as Secretary of State for the Colonies from 1935 to 1936.

He was alive in the 1936 setting and is used as an alternate-history civic and national-council figure for Wales.

The package does not claim that he historically chaired the Event 006 Welsh National Council.

The source-clearance and ownership authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw002_wales_portrait_source_clearance_2026_07_25.md`.

That audit found no meaningful current Chaos Redux, vanilla, Kaiserreich `1521695605`, or approved-mod `2265420196`/`1458561226` owner for the exact identity.

The parent accepted this source for downstream review without invented age progression.

The circa-1920 source age remains the identity authority and is not presented as a 1936 photograph.

Trial 01 remains rejected and unwired because its independent audit found non-compensable face and expression drift.

Trial 02 starts again from the unchanged archival crop and does not use trial 01 as an input.

## Archival source and exact crop

| Field | Value |
| --- | --- |
| Source page | `https://commons.wikimedia.org/wiki/File:James_Henry_Thomas_(1874-1949)_portrait.jpg` |
| Attribution | Bain / Library of Congress George Grantham Bain Collection, `ggbain.29625` |
| Rights record | Commons `PD-Bain`; Library of Congress no known copyright restrictions |
| Date | Circa 1920 |
| Master | `source_masters/WLS_j_h_thomas_circa_1920_master.jpg` |
| Master dimensions | `3674x4977` |
| Master SHA-256 | `4F70EF8F6F2F970F5CD9216E15F65348DD92330BE390389F2E2E717D0CEC8CF5` |
| Exact crop | `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.png` |
| Crop rectangle | `(350,200,3350,4200)` |
| Crop dimensions | `3000x4000` |
| Crop SHA-256 | `0B0B8E8CA7807939391A29C64A04F241C56E47E84BA649060F418FE71EF087BE` |
| Crop equality JSON | `source_crops/WLS_j_h_thomas_circa_1920_head_shoulders.json` |
| Crop equality JSON SHA-256 | `3C8E4AA25FDCD3B6C58DFE12B6495B1E62495CE969A4A91FA8A5C1D44EA380EC` |
| Decoded-pixel equality | `true` |
| Equality RGBA SHA-256 | `58ACBFEA5A056C43490682A10CCA063828DFA0268A092092A346C307C67368F6` |

The copied equality JSON retains the canonical clearance-package paths and hash evidence.

The unchanged archival crop is the sole identity, geometry, age, pose, clothing, lighting, and composition authority.

## Source-locked ImageGen repaint

| Field | Value |
| --- | --- |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `9FCBDB587CABD1100C25273D1E92925156C4D3DA4B6F8866FC9450DC54D1E69A` |
| Raw repaint | `imagegen_results/WLS_j_h_thomas_identity_preserve_trial_02.png` |
| Raw dimensions | `1080x1456` |
| Raw SHA-256 | `22F880F443CDEE78EB992922F8A48709B6BC08F4BD6456CF024C7C4094CAA248` |
| Original ImageGen cache | `C:/Users/klimp/.codex/generated_images/019f6059-0778-7992-8f0d-f7582beecbeb/call_GRuQDToAcugagm5nd6NjAaNt.png` |

The raw repaint was generated directly from the exact archival crop.

No generated face, rejected candidate, substitute person, or style portrait was supplied as an identity input.

## Deterministic `156x210` processing

| Field | Value |
| --- | --- |
| Processor | `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` |
| Processor version | `5.0` |
| Positional mode | `leader` |
| Role family | `leader` |
| Source kind | `real` |
| Raw repaint crop | `(0,1,1080,1455)` |
| Candidate | `processed_png/portrait_WLS_independence_wave_national_council.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `7B352ADBA5A88FFA783ECE46C1D6EEF654261522529670BC112430A4EED57C8C` |
| Candidate decoded RGBA SHA-256 | `F6725767509BD93962F31CF7EF08D2E7A47143C8E34F54FF656EA4D12028376A` |
| Metadata | `processed_png/portrait_WLS_independence_wave_national_council.png.json` |
| Metadata SHA-256 | `73B0048591DD19CA19E804706623F22B8DEC6332F578A9E30BCAC28B0CB93883` |
| Style sheet | `review/WLS_j_h_thomas_leader_style_sheet.png` |
| Style-sheet SHA-256 | `E5C067FFA498C57011AD2600B9F6E373A38B519C45D2D2AEED40257B1356EAD6` |

The processor performs deterministic crop, grade, resize, and export only.

Its selected style controls are the canonical Stauning and Mannerheim leader references recorded in the metadata.

## Independent audit gate

The independent audit is recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wales_jh_thomas_trial02_independent_portrait_audit_2026_07_25.md`.

The candidate passed source attribution, rights, exact-crop equality, source-only lineage, male and role fit, HOI4 country-leader style, `156x210` framing, ownership, stable-consumer declaration, and forbidden-derivative absence.

It failed the non-compensable likeness gate.

Relative to the archival crop, the repaint still raised and centered the gaze, regularized brow and moustache asymmetry, filled and smoothed the cheek planes, softened the jaw and chin, reduced age texture, weakened the stern expression, and made the slight head offset more frontal.

The candidate is retained only as rejected process evidence.

The existing runtime DDS remains an unrelated pre-existing portrait and is not a fallback or evidence for this attempt.

## Gate requirements retained for any later retry

The independent reviewer must compare the unchanged master, exact crop and equality JSON, raw repaint, native `156x210` candidate, processing metadata, review sheet, rejected trial-01 evidence, and role-specific canonical references at native size and at least `4x` nearest-neighbour enlargement.

Identity is a non-compensable gate.

The reviewer must test whether this retry actually corrects the trial-01 failures without introducing new drift.

The source-specific locks are the unequal eyelid openings and gaze, brow-weight asymmetry, long narrow rounded-tip nose, broad drooping asymmetric moustache and ends, long facial planes, cheek hollowness, jaw and chin geometry, unequal ear exposure, source age texture, stern expression, slight head angle, bow tie, lapels, and shoulders.

The review must fail if the retry remains more direct or upward-looking, makes the eyes too equal, broadens or softens the nose, makes the moustache bushier or more symmetrical, fills the cheeks, rounds the jaw and chin, enlarges the viewer-left ear, smooths the photographed age, or changes the expression.

Style quality cannot compensate for identity drift.

Only an all-gates `PASS` permits the parent to replace the unwired Saunders Lewis player-facing identity in one atomic transfer, convert this exact candidate to DDS, prove runtime/package equality, and request a fresh IW-002 package audit.
