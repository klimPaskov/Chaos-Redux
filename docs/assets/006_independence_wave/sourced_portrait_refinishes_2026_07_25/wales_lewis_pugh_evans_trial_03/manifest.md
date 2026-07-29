# IW-002 Wales Lewis Pugh Evans portrait trial 03

Status: `rejected_and_unwired`.

Independent audit verdict: `FAIL / blocked`.

No DDS conversion, character transfer, localisation change, GFX edit, package attestation, or runtime wiring is authorized for this rejected candidate.

This package contains no advisor, dossier, operative, commander-small, `_small`, female, generic, or fallback portrait.

## Stable consumer

| Field | Value |
| --- | --- |
| Package | IW-002 Wales, vanilla carrier `WLS` |
| Existing dynamic character token | `WLS_independence_wave_mountain_commandant` |
| Existing sprite | `GFX_portrait_WLS_independence_wave_mountain_commandant` |
| Runtime path after approval | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |
| Current player-facing identity | role label only; parent-owned localisation remains unchanged pending PASS |
| Proposed sourced identity | Brigadier Lewis Pugh Evans VC |
| Role family | Full-size army commander |
| Authorized portrait surface | Existing commander consumer through the same full-size sprite |

## Historical and ownership boundary

Lewis Pugh Evans was a real male Welsh-born British Army officer who commanded the 159th Welsh Border Infantry Brigade from 1933 through January 1938, making the identity alive and role-compatible for the 1936 WLS package.

The source is circa 1918 and must not be described as a 1936 photograph or as evidence that Evans historically commanded a Welsh independence government.

Source page: `https://commons.wikimedia.org/wiki/File:Lewis_Pugh_Evans_VC_IWM_HU_93411.jpg`.

Archive: Imperial War Museums, HU 93411; photograph attributed to Henry Walter Barnett; Commons records Public Domain/Public Domain Mark. Recommended credit: `Imperial War Museums, HU 93411; photograph by Henry Walter Barnett`.

The source is retained from the cleared package `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/`; prior Evans trials are rejected evidence only and are not ImageGen inputs.

## Archival source and exact crop

| Field | Value |
| --- | --- |
| Immutable master | `source_masters/WLS_lewis_pugh_evans_iwm_hu93411.jpg` |
| Master dimensions | `605x800` |
| Exact decoded master | `source_master_png/WLS_lewis_pugh_evans_iwm_hu93411_master.png` |
| Exact crop | `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png` |
| Crop rectangle | `(60,20,580,730)` |
| Crop dimensions | `520x710` |
| Crop equality JSON | `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.json` |
| Crop decoded RGBA equality | `true`; `c3ee9bee1d58e2a84edc7afb56446a390ee9efbf3b7be0b68ab1cc849de1fd38` |

The unchanged attributed master and exact crop are the sole identity, geometry, age, pose, clothing, lighting, and composition authorities.

## Source-locked ImageGen repaint

| Field | Value |
| --- | --- |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `B84BA941C7D529A96FEE1C36FD404070E81B0B4160BA11BFE38EA25627EBF639` |
| Raw repaint | `imagegen_results/WLS_lewis_pugh_evans_identity_preserve_trial_03.png` |
| Raw dimensions | `1079x1458` |
| Raw SHA-256 | `74B1A1C5793036132851B214FBC1DE0BD6C4BEFC93599079C33D2D3ED09A6DBF` |
| Original ImageGen cache | `C:/Users/klimp/.codex/generated_images/019f6059-0778-7992-8f0d-f7582beecbeb/exec-18912e30-223c-480a-b4c0-14a793dd917f.png` |

The raw repaint was generated directly from the canonical exact crop and does not use either rejected Evans trial or any external face reference.

## Deterministic `156x210` processing

| Field | Value |
| --- | --- |
| Processor | `retired_advisor_card_processor_REMOVED` |
| Processor version | `5.0` |
| Positional mode | `leader` |
| Role family | `commander` |
| Source kind | `real` |
| Raw repaint crop | `(0,0,1079,1458)` |
| Candidate | `processed_png/portrait_WLS_independence_wave_mountain_commandant.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `3A41485403E291294B2C6956CAEBF68ECE5808D90F6D90B520A393F9BDBFF17` |
| Candidate decoded RGBA SHA-256 | `52D5707056E57AAAA7EE9AFF0A0450872C44AF943A891F15101DC222BF700DF1` |
| Metadata | `processed_png/portrait_WLS_independence_wave_mountain_commandant.png.json` |
| Metadata SHA-256 | `DF48407FBE786977C83B2EC5153E9E387CA0EA7F6C7D8125528DC6D407346481` |
| Review sheet | `review/WLS_lewis_pugh_evans_commander_style_sheet.png` |
| Review-sheet SHA-256 | `4C471ACF341BCCB5BFAAE1F75714915BFA160E13ED82BCC9E9601E41A07944A8` |

The processor performs deterministic crop, grade, resize, and export only.

## Independent audit gate

The independent audit is recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wales_lewis_pugh_evans_trial03_independent_portrait_audit_2026_07_25.md` and committed as `f5a744b3e`.

The candidate passed provenance, exact crop equality, male role fit, HOI4 commander style, framing, ownership, metadata integrity, stable-consumer declaration, and forbidden-derivative absence.

It failed the non-compensable likeness gate: the repaint regularized the unequal eyes and ears, frontalized the gaze and head, thickened the pencil moustache, rounded the nose tip, softened the hollow cheeks and narrow pointed jaw, and smoothed source age texture.

The candidate is retained only as rejected process evidence. No fallback or unrelated runtime portrait is approved.

## Gate requirements retained for any later retry

The independent auditor must compare the unchanged master, exact crop and equality JSON, raw repaint, native `156x210` candidate, processing metadata, review sheet, prior rejected trials, and commander-family references at native size and at least `4x` nearest-neighbour enlargement.

Identity is a non-compensable gate. The review must separately record provenance/rights, source-crop equality, male and role fit, exact likeness, HOI4 commander style, framing, ownership, stable consumer, forbidden-derivative absence, and runtime readiness.

Only an all-gates `PASS` permits the parent to convert this exact candidate to DDS, prove package/runtime byte equality, perform any player-facing identity update, and request a fresh IW-002 country-package audit.
