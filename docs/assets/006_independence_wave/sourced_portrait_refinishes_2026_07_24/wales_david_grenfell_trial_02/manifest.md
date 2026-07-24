# WLS David Rhys Grenfell identity-preserving portrait trial 02

Status: `rejected_export_only`.

Trial 02 is a new source-locked ImageGen repaint made directly from the unchanged archival crop after trial 01 failed likeness.

It is not derived from the rejected trial-01 repaint.

No DDS, GFX, localisation, gameplay, or package-attestation change is authorized unless an independent reviewer passes every gate.

## Stable consumer and ownership boundary

| Field | Value |
| --- | --- |
| Package | IW-002 Wales, carrier `WLS` |
| Character | `WLS_independence_wave_national_council` |
| Sprite | `GFX_portrait_WLS_independence_wave_national_council` |
| Proposed identity | David Rhys Grenfell |
| Role family | Civic and national country leader |
| Gender gate | Male |
| Authorized surface after approval | Full-size `civilian.large` only |

The parent-owned promotion must retain the stable token and sprite, replace the player-facing identity and DDS in one transaction, and create no advisor, dossier, operative, commander, or `_small` derivative.

## Archival identity source

| Field | Value |
| --- | --- |
| Source page | <https://commons.wikimedia.org/wiki/File:David_Grenfell.jpg> |
| Institutional record | <https://www.npg.org.uk/collections/search/portrait/mw64853/David-Rhys-Grenfell> |
| Rights | Public domain according to Commons; retain Bassano Ltd and National Portrait Gallery credit |
| Master | `source_masters/WLS_david_grenfell_master.png` |
| Master dimensions | `620x800` |
| Master SHA-256 | `7B613FAAD429E155133B60FB9E4C403639281E7054DF47F07D5CDD6EA3E10E70` |
| Exact crop | `source_crops/WLS_david_grenfell_head_shoulders.png` |
| Crop rectangle | `(70,65,600,790)` |
| Crop dimensions | `530x725` |
| Crop SHA-256 | `55F5CD025F7BFC070F3B821E90BCFABBA0BA6DAAFFFCB6D4A161A1A7DB73392F` |
| Equality JSON | `source_crops/WLS_david_grenfell_head_shoulders.json` |
| Equality JSON SHA-256 | `0D777384A38A20D8931DC52CB317429E7CBFB418294CC055DE179DE536AF9182` |
| Decoded-pixel equality | `true` |

The exact-pixel crop utility created and self-bound the crop without resampling, enhancement, recolouring, or retouching.

## Trial-02 repaint and deterministic processing

| Field | Value |
| --- | --- |
| Prompt | `identity_repaint_prompt.md` |
| ImageGen input | The exact archival crop above, and no rejected portrait |
| Raw repaint | `imagegen_results/WLS_david_grenfell_identity_preserve_trial_02.png` |
| Raw dimensions | `1061x1483` |
| Raw SHA-256 | `CA207D5843B1A144E5BE04C7C36B9D88768CC19D2468171D11FB3AEC3BE85348` |
| Deterministic raw crop | `(0,27,1061,1455)` |
| Candidate | `processed_png/portrait_WLS_independence_wave_national_council.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `0DF68C70BDDDB8E65B78271181709A95EF58F840FA11DDCBCDAAAB2DCA2D73E5` |
| Candidate decoded RGBA SHA-256 | `8513388558F764D7F680A6F7FC313BA9F00584980954FB96F0BE060C2881550C` |
| Metadata | `processed_png/portrait_WLS_independence_wave_national_council.png.json` |
| Metadata SHA-256 | `55574D22847243B1448E203D6196BB9F35EA5CE24ADF9128865493664BB26490` |
| Review sheet | `review/WLS_david_grenfell_leader_style_sheet.png` |
| Review-sheet SHA-256 | `06AB7C079AD6BF9A64C4B4EDAD353ECCDF7B54A708CA8F6CB916D5E46432E336` |

The processor only cropped, graded, resized, and exported the candidate.

## Independent audit gate

The independent reviewer must compare the unchanged master, exact crop and equality JSON, prompt, raw repaint, native `156x210` candidate, metadata, and leader references at native size and a disposable nearest-neighbour enlargement.

Likeness is a separate non-compensable gate.

The audit must test Grenfell's exact head angle and gaze, eyelid opening, small unequal eyes, narrow skull and cheeks, long nose, ear geometry, thin straight moustache, jaw, chin, expression, neck, shoulders, and suit.

The independent audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wales_trial02_independent_portrait_audit_2026_07_24.md` returned a non-compensable likeness `FAIL`.

The repaint again opened, brightened, rounded, and regularized the eyes, filled and frontalized the face, broadened and darkened the moustache, and rounded the jaw and chin.

Trial 02 is rejected and export-only.

It supplies no DDS, GFX, localisation, gameplay, or package-attestation authority.
