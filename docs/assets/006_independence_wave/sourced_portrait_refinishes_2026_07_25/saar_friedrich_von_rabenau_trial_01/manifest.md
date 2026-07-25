# IW-010 Saar Friedrich von Rabenau portrait trial 01

Status: `approved_and_runtime_promoted_2026_07_25`.

The independent audit passed every provenance, crop-equality, identity, style, framing, role, ownership, and consumer-boundary gate.

The parent then converted this exact audited `156x210` PNG to DDS, copied the package DDS byte-for-byte to the pre-existing runtime path, and atomically replaced the fictional player-facing identity with Friedrich von Rabenau while preserving the stable internal consumer and sprite tokens.

This package contains no advisor, dossier, operative, commander-small, `_small`, female, generic, or fallback portrait.

## Stable consumer

| Field | Value |
| --- | --- |
| Package | IW-010 Saar, carrier `AJX` |
| Existing character | `AJX_karl_becker` |
| Existing sprite | `GFX_portrait_AJX_karl_becker` |
| Runtime path | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` |
| Stable internal consumer token | `AJX_karl_becker` |
| Promoted sourced identity | Friedrich von Rabenau |
| Role family | Full-size army commander |
| Authorized portrait surfaces | Existing `civilian.large` and `army.large` consumer through the same sprite |

## Historical and ownership boundary

Friedrich von Rabenau was a real male German Army Generalleutnant and Chief of the Heeresarchive who was alive in the 1936 setting.

The package treats him as an alternate-history German corps-command figure available to the Saar emergency state.

It does not claim that he historically held a Saarbrücken command or industrial-security office.

The source-clearance and ownership authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_military_role_source_clearance_2026_07_25.md`.

That audit found no meaningful current Chaos Redux, vanilla, Kaiserreich `1521695605`, or approved-mod `2265420196`/`1458561226` owner for the exact identity.

## Archival source and exact crop

| Field | Value |
| --- | --- |
| Source page | `https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-C05190,_Friedrich_v._Rabenau.jpg` |
| Attribution | `Bundesarchiv, Bild 183-C05190 / Foto: Dorneth / CC BY-SA 3.0 DE` |
| Date | 13 April 1937 |
| Master | `source_masters/AJX_friedrich_von_rabenau_1937_master.jpg` |
| Master dimensions | `581x800` |
| Master SHA-256 | `F6B51E6B3A39E35734D67FA4DB4081C6DA26AEB40084569FF6747CD9ACA0480B` |
| Exact crop | `source_crops/AJX_friedrich_von_rabenau_1937_head_shoulders.png` |
| Crop rectangle | `(20,30,540,730)` |
| Crop dimensions | `520x700` |
| Crop SHA-256 | `B153E0310340D1EC5ED02484A52049C5D018767FEC6C5C525BA237B5803161E1` |
| Crop equality JSON | `source_crops/AJX_friedrich_von_rabenau_1937_head_shoulders.json` |
| Decoded-pixel equality | `true` |

The copied equality JSON retains the canonical clearance-package paths and hash evidence.

The unchanged archival crop is the sole identity, geometry, pose, clothing, insignia, lighting, and composition authority.

## Source-locked ImageGen repaint

| Field | Value |
| --- | --- |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `F0026D0198E1884A94412D3B82B37732863E855C7C3FA9414B9807E3FE3D088E` |
| Raw repaint | `imagegen_results/AJX_friedrich_von_rabenau_identity_preserve_trial_01.png` |
| Raw dimensions | `1086x1448` |
| Raw SHA-256 | `B352289AFAE5AD3C326E0B964582249BF3CC4E1B305D752FE6DAA3B9B917A1A9` |

The first ImageGen request was rejected before output.

The retained raw repaint is the only produced candidate and was generated directly from the exact archival crop.

No rejected repaint, substitute face, or style portrait was supplied as an identity input.

## Deterministic `156x210` processing

| Field | Value |
| --- | --- |
| Processor | `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` |
| Processor version | `5.0` |
| Positional mode | `leader` |
| Role family | `commander` |
| Source kind | `real` |
| Raw repaint crop | `(5,0,1081,1448)` |
| Candidate | `processed_png/portrait_AJX_saar_industrial_security_commissioner.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `FEC2653228598C9E5A9F18292ECAA07528469AA9477DCB2FFF800F73E6E55627` |
| Candidate decoded RGBA SHA-256 | `96C790A415E354AEA836B40DEDBCC4F3DF6F8F014B01E654841FB11B7AE6F62F` |
| Metadata | `processed_png/portrait_AJX_saar_industrial_security_commissioner.png.json` |
| Metadata SHA-256 | `539CEA30D73B76810D5D4DDCC5AED86379B2FE684F42F08844AC735D30DE60E6` |
| Style sheet | `review/AJX_friedrich_von_rabenau_commander_style_sheet.png` |
| Style-sheet SHA-256 | `F4478CB4339AF7B8971AB2D141AB3DAB01FA72CBD1AA5D1E573BD966EF45586D` |

The processor performs deterministic crop, grade, resize, and export only.

Its selected style controls are the canonical Montgomery and Witzleben commander references recorded in the metadata.

## Independent audit result

The independent reviewer compared the unchanged master, exact crop and equality JSON, raw repaint, native `156x210` candidate, processing metadata, review sheet, and role-specific canonical references at native size and at least `4x` nearest-neighbour enlargement.

The authoritative audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_rabenau_trial01_independent_portrait_audit_2026_07_25.md`.

Decision: **PASS** / `approved_for_parent_promotion`.

The audit separately passed provenance, exact-crop equality, non-compensable identity likeness, HOI4 commander style, `156x210` framing, ownership, stable-consumer transfer, and absence of advisor, dossier, operative, commander-small, and `_small` derivatives.

## DDS and runtime proof

| Field | Value |
| --- | --- |
| Package DDS | `final_dds/portrait_AJX_saar_industrial_security_commissioner.dds` |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` |
| Dimensions | `156x210` |
| Mode after decode | `RGBA` |
| Package/runtime DDS SHA-256 | `6595D33FC6A08B840EB51DEBE3E05BDE56BDAD38009CB22EEF0019720A1EABFD` |
| Direct decoded RGBA SHA-256 | `D54990852253F9E90CA31EEFEB37F6DF480CB893EE50E6827C37B07113B9F307` |
| Audited PNG/package DDS decoded equality | `true` |
| Package DDS/runtime DDS byte equality | `true` |
| Package DDS/runtime DDS decoded equality | `true` |

The existing `GFX_portrait_AJX_karl_becker` registration already points to the runtime path, so no `.gfx` edit or duplicate sprite was needed.

The internal token remains stable for history, scripted triggers, and saved consumer references.

The player-facing name and current package documentation identify the person as Friedrich von Rabenau and make only the bounded alternate-history German corps-command claim accepted by the audit.

This promotion does not admit IW-010 by itself.

The civic Walter Simons consumer must pass the same independent portrait gate and the completed country package must pass a fresh post-wire audit.
