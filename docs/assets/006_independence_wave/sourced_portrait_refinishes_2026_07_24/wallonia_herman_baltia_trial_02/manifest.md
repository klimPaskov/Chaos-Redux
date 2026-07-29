# AFX Herman Baltia identity-preserving portrait trial 02

Status: `candidate_requires_independent_audit`.

This package retries the rejected trial-01 likeness from the unchanged archival master and a newly regenerated exact-pixel crop record.

It proposes a guarded identity transfer from the fictional working name `Marcel Delcourt` to the real historical subject Herman Baltia while retaining the existing stable Event 6 consumer.

No DDS is authorized or wired unless an independent reviewer separately passes provenance, likeness, HOI4 commander style, role fit, male-only scope, consumer ownership, and the absence of advisor or `_small` derivatives.

## Stable consumer

| Field | Value |
|---|---|
| Character | `AFX_walloon_reserve_commander` |
| Sprite | `GFX_portrait_AFX_walloon_reserve_commander` |
| Runtime DDS after approval | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| Role family | Army commander and emergency territorial authority |
| Gender gate | Male |
| Authorized portrait surface | Full-size `civilian.large` and `army.large` through the same stable sprite |

This package contains no advisor portrait, advisor icon, dossier, operative portrait, female asset, or `_small` derivative.

## Historical role decision

Herman Baltia was a Belgian lieutenant-general who commanded the Arlon-based 10th Line Regiment, the formation lineage transformed into the 1st Regiment of Chasseurs Ardennais in 1933.

He was alive in 1936 but retired and seventy-two years old.

The Event 6 role is an alternate-history senior territorial and reserve-command abstraction grounded in his Arlon and Chasseurs Ardennais lineage.

The package does not claim that Baltia commanded an independent Walloon state in real history or that the 1909 uniform is a 1936 uniform.

## Archival source and rights

| Field | Value |
|---|---|
| Subject | Baron Herman Baltia |
| Master | `source_masters/AFX_herman_baltia_1909_master.jpg` |
| Dimensions | `389x473` |
| SHA-256 | `73597E416240754B2F5A9C78AAC4798287B58642F1ABD93C920F3020D95A1B66` |
| Source page | <https://commons.wikimedia.org/wiki/File:General_Baltia_Herman.jpg> |
| Direct upload | <https://upload.wikimedia.org/wikipedia/commons/e/eb/General_Baltia_Herman.jpg> |
| Caption and date | `Major Baltia 1909` |
| Rights | Public Domain Mark 1.0 and `PD-old` as recorded by Commons |

The master is the unchanged direct archival upload and remains the only photographic identity authority.

## Explicit head-and-shoulders crop

| Field | Value |
|---|---|
| Crop | `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` |
| Crop record | `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` |
| Master rectangle | `(20,12,373,473)` |
| Dimensions | `353x461` |
| Crop SHA-256 | `4980AC2A82FAE576809ADC1B10141CA711118BBBC58548C63942E4650A7A25A1` |
| Crop record SHA-256 | `B60815E5ABD161B2E58858BF44A12B63F824A95CDB615735B85857B3230190E5` |
| Decoded-pixel equality | `true`; both RGBA payloads hash to `B3E0A376DB6422EAB69CF85EF3192A461FF2588D59B379B31E4265B59C5CB326` |

The skill-local crop utility decoded the master, extracted the half-open rectangle without resizing or enhancement, reopened the lossless PNG, and proved exact decoded-pixel equality.

## Identity-preserving ImageGen repaint

| Field | Value |
|---|---|
| Identity input | The exact archival crop above |
| Style-only references | `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png` |
| Prompt | `identity_repaint_prompt.md` |
| Raw repaint | `imagegen_results/AFX_herman_baltia_identity_preserve_trial_02.png` |
| Raw dimensions | `1097x1434` |
| Raw SHA-256 | `FCFE0EBB08ADB38FE974BD3B14E5957765E60B8156A0FF2A2DF93C19A18E2F6F` |

The repaint keeps the archival crop as the sole identity, anatomy, pose, clothing, and composition authority.

Unlike trial 01, it retains the source-visible dress uniform instead of inventing a replacement tunic.

## Deterministic 156x210 processing

| Field | Value |
|---|---|
| Processor | `retired_advisor_card_processor_REMOVED` |
| Positional mode | `leader` |
| Role family | `commander` |
| Source kind | `real` |
| Raw repaint crop | `(15,0,1081,1434)` |
| Candidate | `processed_png/portrait_AFX_walloon_reserve_commander.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `D06CFDBB56F1348CD61218C86B53A0D7C5BE85220ECD83F99732E4BC51362047` |
| Candidate decoded RGBA SHA-256 | `EAB689A10A5B42C5AAF4E0FEFB99F301B95615C55D11437A7CCDEEABA2AEF435` |
| Metadata | `processed_png/portrait_AFX_walloon_reserve_commander.png.json` |
| Metadata SHA-256 | `963EDABB634879A804AFC4333A89ADF6FC37C98534A31B6B10759E402DB2C7A5` |
| Processor style sheet | `review/AFX_herman_baltia_commander_style_sheet.png` |
| Style-sheet SHA-256 | `5AA51DC2A58080920421512A3ACC4547292321E3DA107E53F519F2D6F35D110F` |

The processor uses the canonical commander reference family and performs deterministic crop, grade, and export only.

The processor sheet is style evidence, not a substitute for comparing the immutable archival crop to the raw and native-size candidate.

## Independent audit gate

The independent reviewer must inspect the unchanged master, exact crop and JSON proof, raw repaint, `156x210` candidate, prompt, processing metadata, and commander references at native size and a lossless nearest-neighbour enlargement.

The reviewer must return separate verdicts for source identity and rights, historical role, exact crop equality, likeness preservation, HOI4 commander style, native framing, stable-consumer ownership, male-only scope, and absence of advisor, dossier, operative, and `_small` assets.

The likeness gate must specifically compare the high narrow forehead, sparse receding hairline, unequal deep-set eyes, long narrow nose, asymmetric moustache curls, ears, jaw, chin, expression, head angle, and shoulder geometry.

If every gate passes, the parent may update the stable character localisation to `Herman Baltia`, describe the guarded alternate-history role accurately, convert the approved PNG to the stable DDS path, prove decoded-pixel equality, and request a fresh IW-006 package audit.

Any failed gate leaves trial 02 export-only and forbids DDS promotion.
