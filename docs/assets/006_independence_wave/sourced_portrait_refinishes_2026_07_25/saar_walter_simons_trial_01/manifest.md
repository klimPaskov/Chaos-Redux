# IW-010 Saar Walter Simons portrait trial 01

Status: `approved_and_runtime_promoted_2026_07_25`.

The independent audit passed every provenance, crop-equality, identity, style, framing, role, ownership, and consumer-boundary gate.

The parent then converted this exact audited `156x210` PNG to DDS, copied the package DDS byte-for-byte to the pre-existing runtime path, and atomically replaced the fictional player-facing identity with Walter Simons while preserving the stable internal consumer and sprite tokens.

This package contains no advisor, dossier, operative, commander-small, `_small`, female, generic, or fallback portrait.

## Stable consumer

| Field | Value |
| --- | --- |
| Package | IW-010 Saar, carrier `AJX` |
| Stable internal consumer token | `AJX_friedrich_hoffmann` |
| Existing sprite | `GFX_portrait_AJX_friedrich_hoffmann` |
| Runtime path | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` |
| Promoted sourced identity | Walter Simons |
| Role family | Full-size civilian country leader |
| Authorized portrait surface | Existing `civilian.large` consumer through the same sprite |

## Historical and ownership boundary

Walter Simons was a real male independent constitutional figure from the Prussian Rhine Province who served as Weimar Foreign Minister, president of the Reichsgericht, and acting head of state.

He was alive in the 1936 setting and is used as an alternate-history constitutional civic figure for the Saar emergency state.

The package does not claim that he historically chaired an independent Saar commission.

The source-clearance and ownership authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_two_role_source_clearance_2026_07_24.md`.

That audit found no meaningful current Chaos Redux, vanilla, Kaiserreich `1521695605`, or approved-mod `2265420196`/`1458561226` owner for the exact identity.

## Archival source and exact crop

| Field | Value |
| --- | --- |
| Source page | `https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-12279,_Walter_Simons.jpg` |
| Attribution | `Bundesarchiv, Bild 102-12279 / CC-BY-SA 3.0` |
| Date | September 1931 |
| Master | `source_masters/AJX_walter_simons_1931_master.jpg` |
| Master dimensions | `558x800` |
| Master SHA-256 | `789961BC6505993F4A6441979CA4D1F247609531D23CFB8D7088CCC2D4A170B3` |
| Exact crop | `source_crops/AJX_walter_simons_1931_head_shoulders.png` |
| Crop rectangle | `(55,45,520,650)` |
| Crop dimensions | `465x605` |
| Crop SHA-256 | `2B1C394DA30F31F0E81B35CD6740CC0E0235A71326FDC976CCE9F0217688EFD7` |
| Crop equality JSON | `source_crops/AJX_walter_simons_1931_head_shoulders.json` |
| Decoded-pixel equality | `true` |

The copied equality JSON retains the canonical clearance-package paths and hash evidence.

The unchanged archival crop is the sole identity, geometry, pose, clothing, lighting, and composition authority.

## Source-locked ImageGen repaint

| Field | Value |
| --- | --- |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `7E60788AA4C49946FEFC5DDE6540B184CB1BC9597202EDE28A491065EE0B25D6` |
| Raw repaint | `imagegen_results/AJX_walter_simons_identity_preserve_trial_01.png` |
| Raw dimensions | `1082x1453` |
| Raw SHA-256 | `DD0B7B274A6E07402991EF0BBED93F7077701C342C372E4A1426FB642AA6C80D` |

The raw repaint was generated directly from the exact archival crop.

No rejected repaint, substitute face, or style portrait was supplied as an identity input.

## Deterministic `156x210` processing

| Field | Value |
| --- | --- |
| Processor | `retired_advisor_card_processor_REMOVED` |
| Processor version | `5.0` |
| Positional mode | `leader` |
| Role family | `leader` |
| Source kind | `real` |
| Raw repaint crop | `(1,0,1080,1453)` |
| Candidate | `processed_png/portrait_AJX_saar_municipal_neutral_commission.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `A7DE632090AD42ECDAD19583A7B76DE3B3231E75D597E1EFED06486A801A9E04` |
| Candidate decoded RGBA SHA-256 | `436641A4292F9BB5FB93CBE25E3B43ADEAC1A46CADB0B05C1EDD045145BBF1B0` |
| Metadata | `processed_png/portrait_AJX_saar_municipal_neutral_commission.png.json` |
| Metadata SHA-256 | `602287C33DC1C412DA0D7FBAA2A522A88485E136E0F22D69F825273FD29FE0B7` |
| Style sheet | `review/AJX_walter_simons_leader_style_sheet.png` |
| Style-sheet SHA-256 | `8FFED31089D54489AA6DCFA959046563CE9393866294C9B4D4A8B288473E9684` |

The processor performs deterministic crop, grade, resize, and export only.

Its selected style controls are the canonical Stauning and Mannerheim leader references recorded in the metadata.

## Independent audit result

The independent reviewer compared the unchanged master, exact crop and equality JSON, raw repaint, native `156x210` candidate, processing metadata, review sheet, and role-specific canonical references at native size and at least `4x` nearest-neighbour enlargement.

The authoritative audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_walter_simons_trial01_independent_portrait_audit_2026_07_25.md`.

Decision: **PASS** / `approved_for_parent_promotion`.

The audit separately passed provenance, exact-crop equality, non-compensable identity likeness, HOI4 country-leader style, `156x210` framing, ownership, stable-consumer transfer, and absence of advisor, dossier, operative, commander-small, and `_small` derivatives.

## DDS and runtime proof

| Field | Value |
| --- | --- |
| Package DDS | `final_dds/portrait_AJX_saar_municipal_neutral_commission.dds` |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` |
| Dimensions | `156x210` |
| Mode after decode | `RGBA` |
| Package/runtime DDS SHA-256 | `07EFF6959101BED7629F722276DBD46EC6D91D3E5E58F5D3462057C131BED426` |
| Direct decoded RGBA SHA-256 | `E647225F7B38022EEB2E0E335D3319603C6D5366A9A44EE75209768F55EB5E2A` |
| Audited PNG/package DDS decoded equality | `true` |
| Package DDS/runtime DDS byte equality | `true` |
| Package DDS/runtime DDS decoded equality | `true` |

The existing `GFX_portrait_AJX_friedrich_hoffmann` registration already points to the runtime path, so no `.gfx` edit or duplicate sprite was needed.

The internal token remains stable for history, scripted effects, scripted triggers, and saved consumer references.

The player-facing name, neutral-route tooltip, and current package documentation identify the person as Walter Simons and make only the bounded alternate-history Rhenish constitutional-civic claim accepted by the audit.

Both IW-010 full-size portraits now satisfy the source-locked workflow, but this promotion does not admit IW-010 by itself.

The completed country package must pass a fresh post-wire audit.
