# WLS George Cornwallis-West identity-preserving portrait trial 01

Status: `rejected_export_only`.

The unchanged archival crop is the sole identity, geometry, anatomy, pose, uniform, insignia, and composition authority.

The canonical commander portrait is style-only.

No DDS, localisation transfer, GFX change, gameplay change, package attestation, or runtime wiring is authorized unless an independent reviewer passes every gate.

## Stable consumer and guarded transfer

| Field | Value |
| --- | --- |
| Package | IW-002 Wales, carrier `WLS` |
| Character | `WLS_independence_wave_mountain_commandant` |
| Sprite | `GFX_portrait_WLS_independence_wave_mountain_commandant` |
| Runtime DDS after approval | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |
| Current identity | Mountain Commandant |
| Proposed sourced identity | Major George Frederick Myddleton Cornwallis-West |
| Role family | Army commander and emergency-route country leader |
| Gender gate | Male |
| Authorized portrait surfaces | Full-size `civilian.large` and `army.large` through the same sprite |

Promotion must retain the one stable character token and one stable sprite, replace the generic player-facing title with the Cornwallis-West name and historically bounded description, replace the stable DDS, and update the package evidence in one parent-owned transaction.

The description must identify him as a Welsh-born Scots Guards officer and must not claim that he historically commanded a Welsh mountain force.

The transaction may not create a second character, simultaneous identity owner, advisor, dossier, operative, commander-small, or `_small` derivative.

## Historical source and exact crop

George Frederick Myddleton Cornwallis-West was born in Ruthin and served as a Scots Guards officer, with later Royal Marines and Royal Naval Division service.

The selected Henry Walter Barnett portrait is dated between 1900 and 1910.

It preserves Cornwallis-West as photographed and does not attempt to fabricate a 1936-age face.

| Field | Value |
| --- | --- |
| Source page | <https://commons.wikimedia.org/wiki/File:Georgecornwalliswest.jpg> |
| Rights | Public domain according to Commons, with the recorded PD-Art jurisdiction caution retained |
| Photographer | Henry Walter Barnett |
| Master | `source_masters/WLS_george_cornwallis_west_master.png` |
| Master dimensions | `1080x1371` |
| Master SHA-256 | `DBA6C6BC4B5A261C4E761323944BC2D504B0F3DE992F0D8301F2D28535E5ED2C` |
| Exact crop | `source_crops/WLS_george_cornwallis_west_head_shoulders.png` |
| Crop rectangle | `(40,40,1040,1320)` |
| Crop dimensions | `1000x1280` |
| Crop SHA-256 | `3483095E908CD993D46469D4033AABA4AD8CF7009E3BD7D8BA69F890CEA066C4` |
| Equality JSON | `source_crops/WLS_george_cornwallis_west_head_shoulders.json` |
| Equality JSON SHA-256 | `2BBCBBF01212DF963D7C0710CEB61524DA70E861AB459917AA2E0FB35D2BDF2A` |
| Decoded-pixel equality | `true` |

The skill-local crop utility extracted the rectangle without resampling, enhancement, recolouring, or retouching and self-bound the JSON evidence to this trial.

## ImageGen repaint and deterministic processing

| Field | Value |
| --- | --- |
| Style-only reference | `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/ger_erwin_von_witzleben.png` |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `B27B6EF2623907A63902406A9599D434D6099CE6B99CB573A2F41015A782F7EA` |
| Raw repaint | `imagegen_results/WLS_george_cornwallis_west_identity_preserve_trial_01.png` |
| Raw dimensions | `1122x1402` |
| Raw SHA-256 | `525A948795C8C0A455631BDB4A0E8463F9A6BF4D8CE6102EF3C8A45CEF0668FB` |
| Processor | `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`, version `5.0` |
| Mode and role | `leader`, role family `commander`, source kind `real` |
| Raw crop | `(40,0,1081,1402)` |
| Candidate | `processed_png/portrait_WLS_independence_wave_mountain_commandant.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `C8B287458F5BF34DA81A7EAF4A10C3BB3DC1364A80BBB16BC6231D40F8BCC833` |
| Candidate decoded RGBA SHA-256 | `0DCFBDDB29D4DEC1DAC9F025D4AB6628E0E49EF04F7A20575DB9F43A75E05E91` |
| Metadata | `processed_png/portrait_WLS_independence_wave_mountain_commandant.png.json` |
| Metadata SHA-256 | `07D7FDC9849D3F26D1B82949E70D77F2D29BE73B2DA3FEAAA14156F29582F570` |
| Review sheet | `review/WLS_george_cornwallis_west_commander_style_sheet.png` |
| Review-sheet SHA-256 | `0B92D324B84A7FB1735E2CFF91081A1D3545098007284AD6FEAB7F39354C5A43` |

The processor performs deterministic crop, grade, resize, and export only.

## Independent audit gate

The independent reviewer must compare the immutable master, exact crop and equality JSON, prompt, raw repaint, native `156x210` candidate, metadata, and canonical commander references at native size and a disposable nearest-neighbour enlargement.

The likeness verdict must independently test Cornwallis-West's high broad forehead, bald crown, narrow side hair, long oval head, small unequal eyes, long narrow nose, lean cheeks, compact ears, thin pointed asymmetric moustache, narrow jaw, rounded chin, expression, head angle, long neck, sloped shoulders, uniform, and insignia geometry.

Return separate verdicts for provenance and rights, crop equality, historical role, likeness, HOI4 commander style, native framing, male-only scope, ownership, guarded stable-token transfer, and absence of advisor, dossier, operative, commander-small, and `_small` derivatives.

The independent audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wales_trial01_independent_portrait_audit_2026_07_24.md` returned a non-compensable likeness `FAIL`.

The repaint enlarged and regularized the eyes, filled the lower face, thickened and curled the moustache, and moved the gaze toward a more frontal presentation.

Trial 01 is rejected and export-only.

It supplies no DDS, GFX, localisation, gameplay, or package-attestation authority.
