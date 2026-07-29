# WLS David Rhys Grenfell identity-preserving portrait trial 01

Status: `rejected_export_only`.

The unchanged archival crop is the sole identity, geometry, anatomy, pose, clothing, and composition authority.

The canonical leader portrait is style-only.

No DDS, localisation transfer, GFX change, gameplay change, package attestation, or runtime wiring is authorized unless an independent reviewer passes every gate.

## Stable consumer and guarded transfer

| Field | Value |
| --- | --- |
| Package | IW-002 Wales, carrier `WLS` |
| Character | `WLS_independence_wave_national_council` |
| Sprite | `GFX_portrait_WLS_independence_wave_national_council` |
| Runtime DDS after approval | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` |
| Current identity | Saunders Lewis |
| Proposed sourced identity | David Rhys Grenfell |
| Role family | Civic and national country leader |
| Gender gate | Male |
| Authorized portrait surface | Full-size `civilian.large` only |

Promotion must retain the one stable character token and one stable sprite, remove the old Saunders Lewis player-facing identity, install the Grenfell name and historically grounded description, replace the stable DDS, and update the package evidence in one parent-owned transaction.

The transaction may not create a second character, simultaneous identity owner, advisor, dossier, operative, commander, or `_small` derivative.

## Historical source and exact crop

David Rhys Grenfell was a Welsh Labour MP for Gower from 1922 to 1959 and chaired the Welsh Parliamentary Labour Party.

The selected Bassano Ltd portrait is dated 1922 and is recorded by the National Portrait Gallery and Wikimedia Commons.

| Field | Value |
| --- | --- |
| Source page | <https://commons.wikimedia.org/wiki/File:David_Grenfell.jpg> |
| Institutional record | <https://www.npg.org.uk/collections/search/portrait/mw64853/David-Rhys-Grenfell> |
| Rights | Public domain according to the Commons record; retain Bassano Ltd and National Portrait Gallery credit |
| Master | `source_masters/WLS_david_grenfell_master.png` |
| Master dimensions | `620x800` |
| Master SHA-256 | `7B613FAAD429E155133B60FB9E4C403639281E7054DF47F07D5CDD6EA3E10E70` |
| Exact crop | `source_crops/WLS_david_grenfell_head_shoulders.png` |
| Crop rectangle | `(70,65,600,790)` |
| Crop dimensions | `530x725` |
| Crop SHA-256 | `55F5CD025F7BFC070F3B821E90BCFABBA0BA6DAAFFFCB6D4A161A1A7DB73392F` |
| Equality JSON | `source_crops/WLS_david_grenfell_head_shoulders.json` |
| Equality JSON SHA-256 | `73B32769F37EAA5A7E4C2E1CE3670F2D205CE69CD0C9E7988A066D0952C03DDB` |
| Decoded-pixel equality | `true` |

The skill-local crop utility extracted the rectangle without resampling, enhancement, recolouring, or retouching and self-bound the JSON evidence to this trial.

## ImageGen repaint and deterministic processing

| Field | Value |
| --- | --- |
| Style-only reference | `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/ire_eamon_de_valera.png` |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `A9E0FC4C89A5141BA059BD80DEB2EDD57999F3C7C227546DAD80AA6570A126CF` |
| Raw repaint | `imagegen_results/WLS_david_grenfell_identity_preserve_trial_01.png` |
| Raw dimensions | `1074x1464` |
| Raw SHA-256 | `4F3B0A31A2A7360EDFE549E038FDC7DBD688B89460999FF608D3447C956ADF79` |
| Processor | `retired_advisor_card_processor_REMOVED`, version `5.0` |
| Mode and role | `leader`, role family `leader`, source kind `real` |
| Raw crop | `(0,9,1074,1455)` |
| Candidate | `processed_png/portrait_WLS_independence_wave_national_council.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `B51594925EE5754DE7A795BCB0BBDD37C7DFFDEF85B411F960A22D33BEAF6667` |
| Candidate decoded RGBA SHA-256 | `B402D41BA604A6EAA69087DDFE0E2EF439BEFE13C6CE7C946AD23254FA820B80` |
| Metadata | `processed_png/portrait_WLS_independence_wave_national_council.png.json` |
| Metadata SHA-256 | `AB072D9033254F31CD71651B7A090E5E54AD6EB847CF15B0316E7F5DB86BEEA4` |
| Review sheet | `review/WLS_david_grenfell_leader_style_sheet.png` |
| Review-sheet SHA-256 | `A1A7A59F5176C041531538CE9E75C7EA1EE0DC2133ACB99E2B15F23DA2066C4D` |

The processor performs deterministic crop, grade, resize, and export only.

## Independent audit gate

The independent reviewer must compare the immutable master, exact crop and equality JSON, prompt, raw repaint, native `156x210` candidate, metadata, and canonical leader references at native size and a disposable nearest-neighbour enlargement.

The likeness verdict must independently test Grenfell's tall narrow forehead, side-parted hair, long narrow face, small unequal eyes, long narrow nose, lean cheeks, compact ears, slim asymmetric moustache, narrow jaw, small chin, expression, head angle, neck, shoulders, and suit geometry.

Return separate verdicts for provenance and rights, crop equality, historical role, likeness, HOI4 leader style, native framing, male-only scope, ownership, guarded stable-token transfer, and absence of advisor, dossier, operative, commander, and `_small` derivatives.

The independent audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wales_trial01_independent_portrait_audit_2026_07_24.md` returned a non-compensable likeness `FAIL`.

The repaint opened and regularized the eyes, filled the cheeks, thickened the moustache, and moved the gaze toward a more frontal presentation.

Trial 01 is rejected and export-only.

It supplies no DDS, GFX, localisation, gameplay, or package-attestation authority.
