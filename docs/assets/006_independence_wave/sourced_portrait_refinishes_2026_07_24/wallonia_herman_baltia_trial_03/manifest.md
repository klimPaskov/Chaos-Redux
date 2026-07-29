# AFX Herman Baltia identity-preserving portrait trial 03

Status: `candidate_requires_independent_audit`.

Trial 03 is a source-only repaint retry after trial 02 passed style but failed likeness.

It uses no generated or HOI4 portrait as an identity input.

It proposes a guarded player-facing identity transfer from the fictional working name `Marcel Delcourt` to the real historical subject Herman Baltia while retaining the existing stable Event 6 character and sprite.

No DDS is authorized or wired unless an independent reviewer separately passes every provenance, likeness, style, role, ownership, male-only, and consumer-boundary gate.

## Stable consumer

| Field | Value |
|---|---|
| Character | `AFX_walloon_reserve_commander` |
| Sprite | `GFX_portrait_AFX_walloon_reserve_commander` |
| Runtime DDS after approval | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| Role family | Army commander and emergency territorial authority |
| Gender gate | Male |
| Authorized surface | Full-size `civilian.large` and `army.large` through the same sprite |

This package contains no advisor, dossier, operative, female, or `_small` asset.

## Historical role

Herman Baltia was a Belgian lieutenant-general who commanded the Arlon-based 10th Line Regiment, the formation lineage transformed into the 1st Regiment of Chasseurs Ardennais in 1933.

He was alive in 1936 but retired and seventy-two years old.

The Event 6 role is an explicit alternate-history territorial and reserve-command abstraction grounded in that Arlon and Chasseurs Ardennais lineage.

The package does not claim that Baltia historically commanded an independent Walloon state or that the source's 1909 uniform is a 1936 uniform.

## Immutable archival photograph

| Field | Value |
|---|---|
| Subject | Baron Herman Baltia |
| Master | `source_masters/AFX_herman_baltia_1909_master.jpg` |
| Dimensions | `389x473` |
| SHA-256 | `73597E416240754B2F5A9C78AAC4798287B58642F1ABD93C920F3020D95A1B66` |
| Source page | <https://commons.wikimedia.org/wiki/File:General_Baltia_Herman.jpg> |
| Direct original | <https://upload.wikimedia.org/wikipedia/commons/e/eb/General_Baltia_Herman.jpg> |
| Caption and date | `Major Baltia 1909` |
| Rights | Public Domain Mark 1.0 and `PD-old` as recorded by Commons |

The unchanged direct archival upload is the only identity authority.

## Exact head-and-shoulders crop

| Field | Value |
|---|---|
| Crop | `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` |
| Crop record | `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` |
| Master rectangle | `(20,12,373,473)` |
| Dimensions | `353x461` |
| Crop SHA-256 | `4980AC2A82FAE576809ADC1B10141CA711118BBBC58548C63942E4650A7A25A1` |
| Crop record SHA-256 | `4EEF10B5531C8C1660D684AF5F35826204BCE36F7D2CE4435A0C5871E48AC3AD` |
| Decoded-pixel equality | `true`; both domain-free RGBA payloads hash to `B3E0A376DB6422EAB69CF85EF3192A461FF2588D59B379B31E4265B59C5CB326` |

The skill-local crop utility extracted the rectangle without resizing, enhancement, recolouring, or retouching and proved exact decoded-pixel equality.

## Source-locked ImageGen repaint

| Field | Value |
|---|---|
| Sole input | The exact archival crop above |
| Prompt | `identity_repaint_prompt.md` |
| Raw repaint | `imagegen_results/AFX_herman_baltia_identity_preserve_trial_03.png` |
| Raw dimensions | `1097x1434` |
| Raw SHA-256 | `B4EA2C284226385FD30646C59D5AF9C3623289042703809E41F34BBD7E9E86EB` |

The prompt permits only a painted surface and restrained colour treatment over the source geometry.

It expressly preserves the unequal eye geometry, long narrow nose, asymmetrical moustache curls, receding hairline, long jaw and chin, source uniform, and source pose.

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
| Candidate SHA-256 | `F9095A351A709B859264C61647EF9DCFCC35A9AD9244C2207E2C7474FE6D8143` |
| Candidate domain-separated decoded RGBA SHA-256 | `477C7C86B4AC15AE4630FCEAE2D1C809D6069A342D2AF1CC53463ECCEA54E720` |
| Metadata | `processed_png/portrait_AFX_walloon_reserve_commander.png.json` |
| Metadata SHA-256 | `C97398A5F1E5BF69E2503D3B106750A2F812ED910833251A82B36732E3DF6A36` |
| Style sheet | `review/AFX_herman_baltia_commander_style_sheet.png` |
| Style-sheet SHA-256 | `BA861497873379EBA642A5D60D1E25067436A93C2A2990603F6D6B9BFC751F79` |

The processor uses the canonical commander reference family for deterministic finishing and style comparison only.

Its `decoded_rgba_sha256` uses the documented domain prefix and encoded dimensions and is not directly comparable to a plain SHA-256 of raw pixel bytes.

## Independent audit gate

The reviewer must compare the unchanged master, exact crop and equality JSON, raw repaint, native `156x210` candidate, prompt, metadata, and canonical commander references at native size and a disposable nearest-neighbour enlargement.

The reviewer must return separate verdicts for rights and source identity, crop equality, historical role, likeness, HOI4 commander style, native framing, male-only scope, stable-consumer ownership, and absence of advisor, dossier, operative, and `_small` derivatives.

The likeness verdict must specifically test the forehead and hairline, unequal eye sizes and heights, nose length and width, unequal moustache curls, ears, face width, jaw, chin, expression, head angle, and shoulder geometry.

If every gate passes, the parent may update the stable localisation to `Herman Baltia`, describe the alternate-history role accurately, convert this exact processed PNG to the stable DDS, prove pixel equality, and request a fresh full IW-006 package audit.

Any failed gate leaves trial 03 export-only.
