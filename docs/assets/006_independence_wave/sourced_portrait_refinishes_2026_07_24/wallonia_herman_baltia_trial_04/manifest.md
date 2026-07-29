# AFX Herman Baltia identity-preserving portrait trial 04

Status: `rejected_export_only`.

Trial 04 is a source-locked repaint retry after trials 01 through 03 passed broad provenance, role, framing, and style gates but failed the independent likeness gate.

It uses the exact archival crop as the sole identity, anatomy, age, pose, clothing, insignia, medal-placement, and composition authority.

The two canonical commander portraits supplied to ImageGen are style-only references and may not transfer identity, clothing, or pose.

The package proposes a guarded player-facing identity transfer from the fictional working name `Marcel Delcourt` to Herman Baltia while retaining the existing stable Event 6 character and sprite.

No DDS, localisation transfer, or runtime wiring is authorized unless an independent reviewer separately passes every provenance, likeness, style, role, ownership, male-only, and consumer-boundary gate.

## Stable consumer

| Field | Value |
|---|---|
| Package | IW-006 Wallonia, carrier `AFX` |
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
| Crop record SHA-256 | `6E7A2973CA1AD43D018FAD6A65A88869D2B97DD82613E1CCB512D6FC3597A85C` |
| Decoded-pixel equality | `true`; both domain-free RGBA payloads hash to `B3E0A376DB6422EAB69CF85EF3192A461FF2588D59B379B31E4265B59C5CB326` |

The skill-local crop utility extracted the rectangle without resizing, enhancement, recolouring, or retouching and proved exact decoded-pixel equality.

After the independent audit found that the copied equality JSON still named the trial-03 paths, the same utility reran against the unchanged trial-04 master and crop rectangle with `--force`.

The crop PNG and decoded-pixel hash remained byte-identical, while the corrected JSON now binds its master, output, metadata, and normalized command paths to trial 04.

## Source-locked ImageGen repaint

| Field | Value |
|---|---|
| Identity input | The exact archival crop above |
| ImageGen style-only references | `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png` |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `07995E6F2016302702918B712E3D4D8AD1B15FF3FDCCC47A41968AC37BD9A43C` |
| Raw repaint | `imagegen_results/AFX_herman_baltia_identity_preserve_trial_04.png` |
| Raw dimensions | `1081x1455` |
| Raw SHA-256 | `263E508706059AD2B63AD615A8F7D17B8075E3D52442F6A89B63C924FF59B961` |

The prompt explicitly forbids enlarged eyes, a widened or squared face, broadened jaw, shortened nose, thickened lips or moustache, smoothed asymmetry, invented detail, changed clothing, or transferred identity.

## Deterministic 156x210 processing

| Field | Value |
|---|---|
| Processor | `retired_advisor_card_processor_REMOVED` |
| Processor version | `5.0` |
| Positional mode | `leader` |
| Role family | `commander` |
| Source kind | `real` |
| Raw repaint crop | `(0,0,1081,1455)` |
| Candidate | `processed_png/portrait_AFX_walloon_reserve_commander.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `D6B617411D67535E3E4F5BDB90333569B37E07027B185CC14831BB1F2A4AED10` |
| Candidate domain-separated decoded RGBA SHA-256 | `FD67C88D4793FA1187FC3DD9B16A9230F401CF02235AA37EA57CEC5B36FE78DE` |
| Metadata | `processed_png/portrait_AFX_walloon_reserve_commander.png.json` |
| Metadata SHA-256 | `23B0B71B700550050103550E8CF69AA50E1F3E221BC0CDC187336AFF167F7514` |
| Style sheet | `review/AFX_herman_baltia_commander_style_sheet.png` |
| Style-sheet SHA-256 | `29BD756F435FCBFD3D039FC98F286E903F9EEC7822EFE6AC9D1B3A4094149200` |
| Processor review references | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png` |

The processor performs deterministic crop, grade, resize, and export only.

The provider-side and processor-side reference pairs depict the same two canonical commander portraits, but the manifest records their separate roles so neither can be mistaken for an identity input.

## Independent audit gate

The reviewer must compare the unchanged master, exact crop and equality JSON, raw repaint, native `156x210` candidate, prompt, metadata, and canonical commander references at native size and a disposable nearest-neighbour enlargement.

The reviewer must return separate verdicts for rights and source identity, crop equality, historical role, likeness, HOI4 commander style, native framing, male-only scope, stable-consumer ownership, and absence of advisor, dossier, operative, and `_small` derivatives.

The likeness verdict must specifically test the forehead and hairline, unequal eye sizes and heights, nose length and width, unequal moustache curls, ears, face width, jaw, chin, expression, head angle, neck length, and shoulder geometry.

If every gate passes, the parent may update the stable localisation to `Herman Baltia`, describe the alternate-history role accurately, convert this exact processed PNG to the stable DDS, prove decoded-pixel equality, and request a fresh full IW-006 package audit.

Any failed gate leaves trial 04 export-only.

## Independent audit result

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_baltia_trial04_independent_portrait_audit_2026_07_24.md` rejects trial 04.

The source photograph, explicit crop, male commander role, `156x210` framing, HOI4 painted commander style, and absence of advisor, dossier, operative, and `_small` derivatives passed.

Likeness failed because the repaint enlarged and regularized the eyes, broadened the skull, jaw, chin, and nose, filled the cheeks, thickened and regularized the moustache, altered the visible ear and hairline, and shortened and broadened the neck.

The review also found no complete guarded Marcel Delcourt-to-Herman Baltia stable-token transfer contract.

The crop-record path defect cited by the audit is corrected in this retained export-only package, but the independent likeness and transfer failures remain non-compensable.

No DDS, localisation transfer, or runtime wiring is authorized from trial 04.
