# IW-006 Wallonia Louis Ruquoy portrait trial 01

Status: `candidate_requires_independent_audit`.

No DDS conversion, character transfer, localisation change, GFX edit, package attestation, or runtime wiring is authorized unless an independent reviewer passes every provenance, crop-equality, identity, style, framing, role, ownership, and consumer-boundary gate.

This package contains no advisor, dossier, operative, commander-small, `_small`, female, generic, or fallback portrait.

## Stable consumer

| Field | Value |
| --- | --- |
| Package | IW-006 Wallonia, vanilla carrier `AFX` |
| Existing dynamic character token | `AFX_independence_wave_walloon_reserve_commander` |
| Existing sprite | `GFX_portrait_AFX_walloon_reserve_commander` |
| Runtime path after approval | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| Proposed sourced identity | Lieutenant-General Louis Hubert baron Ruquoy (Rucquoy) |
| Role family | Full-size army commander |
| Authorized portrait surface | Existing commander consumer through the same full-size sprite |

## Historical and ownership boundary

Louis Hubert baron Ruquoy (period spelling Rucquoy) was a real male Belgian lieutenant-general born in Frasnes-lez-Buissenal in Hainaut, Wallonia. He commanded the Belgian 5th Division and served as Chief of the General Staff during the First World War; he was retired by 1927 and alive in the 1936 setting. The Event 006 reserve-commander role is an alternate-history appointment and must not be presented as a documented 1936 Walloon government office.

Primary source: Agence Rol / Bibliothèque nationale de France, Gallica item `btv1b531010537`, dated 12 March 1923, with the archive caption identifying Rucquoy as the center general. Commons records the source as public domain under PD-France/PD-1996/US-expiry treatment. Preserve the archive and attribution in any redistribution: `Agence Rol / Bibliothèque nationale de France, Gallica, item btv1b531010537`.

Ownership audit found no exact or variant Louis Ruquoy/Rucquoy character or portrait consumer in the current project, installed vanilla, Kaiserreich `1521695605`, or approved mods checked by the source researcher.

## Archival source and exact crop

| Field | Value |
| --- | --- |
| Immutable master | `source_masters/AFX_louis_ruquoy_rol_1923_group.jpg` |
| Master dimensions | `8419x6051` |
| Exact crop | `source_crops/AFX_louis_ruquoy_rol_1923_head_shoulders.png` |
| Crop rectangle | `(3300,1000,5050,2900)` |
| Crop dimensions | `1750x1900` |
| Crop equality JSON | `source_crops/AFX_louis_ruquoy_rol_1923_head_shoulders.json` |
| Master SHA-256 | `BF11028C9B7DA593062F4EB8730417C760748D10A5C6DE8493CBBB8BC667C7AC` |
| Crop SHA-256 | `4AAF3591D040A9E6423803715404030148A2FCB0CC38801118BCE9C398B6CA6A` |
| Crop decoded RGBA equality | `true`; `ed034beac18575bf34e9d4f3801698846256e50caa89106e2f36eb17910be58d` |

The unchanged attributed master and exact crop are the sole identity, geometry, age, pose, clothing, lighting, and composition authorities.

## Source-locked ImageGen repaint

| Field | Value |
| --- | --- |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `FFC4D0920B694972C2BCF841597E8079CA345A9F1DF09A799371845472192B42` |
| Raw repaint | `imagegen_results/AFX_louis_ruquoy_identity_preserve_trial_01.png` |
| Raw dimensions | `1080x1456` |
| Raw SHA-256 | `332B6AC29CB09ECB9D339B18914B5E6CC60006A9A17DF371DE57E898C4B2B624` |
| Original ImageGen cache | `C:/Users/klimp/.codex/generated_images/019f6059-0778-7992-8f0d-f7582beecbeb/exec-4af82da0-67e9-49ca-b8cc-9b3fef3ad3fc.png` |

The raw repaint was generated directly from the exact ROL crop and does not use comparison images or a generated substitute.

## Deterministic `156x210` processing

| Field | Value |
| --- | --- |
| Processor | `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` |
| Processor version | `5.0` |
| Positional mode | `leader` |
| Role family | `commander` |
| Source kind | `real` |
| Raw repaint crop | `(0,0,1080,1456)` |
| Candidate | `processed_png/portrait_AFX_walloon_reserve_commander.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `FAFFBFE12921431353C962215C04F8E69FF40B8CAA083C61FC8F46719A477EC0` |
| Candidate decoded RGBA SHA-256 | `594904EE285E9E360F0C488A48B8174BE45790807C4049E4BEF7D11950020FC9` |
| Metadata | `processed_png/portrait_AFX_walloon_reserve_commander.png.json` |
| Metadata SHA-256 | `11744FC9D2653B18B9F022826B26ECB304529B9A265B4292EB5C5405CE7C1F57` |
| Review sheet | `review/AFX_louis_ruquoy_commander_style_sheet.png` |
| Review-sheet SHA-256 | `D835EAE207E0294A77FE0411E4FC7BF126F8AFB2B0685A28FBCA3DC7C7C7DCCC` |

The processor performs deterministic crop, grade, resize, and export only.

## Independent audit gate

The independent auditor must compare the unchanged master, exact crop and equality JSON, raw repaint, native `156x210` candidate, processing metadata, review sheet, source comparison images, and commander-family references at native size and at least `4x` nearest-neighbour enlargement.

Identity is a non-compensable gate. The review must separately record provenance/rights, source-crop equality, male and role fit, exact likeness, HOI4 commander style, framing, ownership, stable consumer, forbidden-derivative absence, and runtime readiness.

Only an all-gates `PASS` permits the parent to convert this exact candidate to DDS, prove package/runtime byte equality, perform any player-facing identity update, and request a fresh IW-006 country-package audit.
