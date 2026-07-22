# ASX Sicily — Vincenzo Di Benedetto source-locked refinish trial

Date: 2026-07-22  
Event/package: IW-019 ASX Sicily  
Asset type: full male leader/army-command portrait  
Source mode: `grounded_source_only`  
Overall status: `candidate_requires_independent_review` — source, crop, and
source-locked painted candidate are complete; runtime wiring remains forbidden
until an independent identity/style/provenance audit passes.

## Role decision

The parent has selected Vincenzo Di Benedetto for the separate ASX army slot as
a deliberate alternate-history emergency adaptation: **a retired Sicilian
general recalled for the synchronized independence emergency**. This wording
does not claim that he held an active field command in 1936. Historical records
place him at disposal/unemployed in the 1930s. His source is civilian, so the
portrait must preserve the suit, tie, face, pose, and grayscale appearance. No
military uniform, hat, medals, insignia, weapon, or invented service detail may
be added.

## Source master

| Field | Value |
|---|---|
| File | `source_masters/ASX_vincenzo_di_benedetto_senate_pd.gif` |
| Native image | `314x401`, grayscale GIF, 125,570 bytes |
| SHA-256 | `EC033B2FCD0DC44441A57C93B12B8C9D64828CF72BD3DD2AD646D40480169553` |
| Source page | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Senatore_Vincenzo_Di_Benedetto.gif) |
| Direct master | [Wikimedia Commons unchanged GIF](https://upload.wikimedia.org/wikipedia/commons/3/32/Senatore_Vincenzo_Di_Benedetto.gif) |
| Provenance | Senate of the Republic of Italy portrait; author unknown; dated before 1942; Commons records Italian Senate image collection, PD Italy (20 years after creation), and PD-1996/US. |
| Identity/era | Vincenzo Di Benedetto, born Enna, Sicily, 29 Jan 1866; senior Italian army career; alive in 1936, but reported at disposal/unemployed in the 1930s. |

The source master is unchanged and remains separate from all derived files.
Retain Senate/Commons attribution and both source URLs in any release notes.

## Explicit crop and native preview

The source image was decoded to RGB and cropped exactly as
`(left=8, top=0, right=305, bottom=401)`, producing a `297x401` face-visible
head-and-shoulders crop. The crop keeps the hat/hairline, eyes, nose, mouth,
jaw, shirt collar, tie, lapels, and both shoulders without introducing a new
person or background. It is saved at:

`source_crops/ASX_vincenzo_di_benedetto_source_crop.png`  
SHA-256: `596393635FF9C0DC2511A4319B4583C2F33DA7C2A7488C81EEE386F941239617`

The source-only native canvas preview is resized from that crop to the required
`156x210` leader ratio (`156:210 = 0.742857`):

`processed_previews/ASX_vincenzo_di_benedetto_source_locked_156x210.png`  
SHA-256: `0C7A9D51FA13A9AB27CCA02F3B09026851CA67D3F9DF7549C66AD4C1AED2AE18`

This preview is a source resize, not the final HOI4-painted treatment. It is
kept to prove the crop and to prevent an editor from silently substituting a
different face or pose.

## Source-locked finish

The parent generated a source-locked repaint after the sourced researcher
completed the archival package. The exact source crop is the only identity
input; `den_thorvald_stauning.png` is style-only. The exact executed prompt is
retained at
`prompts/ASX_vincenzo_di_benedetto_identity_preserve_trial_01.txt`.

- Raw ImageGen result:
  `imagegen_results/ASX_vincenzo_di_benedetto_identity_preserve_trial_01.png`,
  `1080x1457`, SHA-256
  `01404A3C74F670DCC238F6B2D68A69AE50F538CF4F48C82B19D548964AED5671`.
- Deterministic finish: skill-local `advisor_icon_processing.py leader`, source
  kind `real`, crop `(0, 1, 1080, 1455)`, canonical vanilla leader review
  directory.
- Processed candidate:
  `processed_png/portrait_ASX_independence_wave_vincenzo_di_benedetto.png`,
  opaque `156x210`, SHA-256
  `37D7256285ABEF55CB9B81EE6A3AC04AAE8E337297120A85DE6C99C489E77108`.
- Processor metadata:
  `metadata/ASX_vincenzo_di_benedetto_processing.json`.

The candidate preserves the civilian suit and tie and contains no military
uniform, medals, insignia, weapon, epaulette, or rank badge. It must still be
rejected if independent review finds that the archival identity, hat shape,
face geometry, source rights, or HOI4 finish do not survive comparison.

## Style comparison

`comparisons/source_style_comparison.png` places the unchanged source crop, the
source-only native preview, and the canonical painted leader/commander families
side by side. The canonical references are not copied into the package:

- `den_thorvald_stauning.png` (leader family), SHA-256
  `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6`.
- `generic_africa_navy_2.png` (commander family), SHA-256
  `A608D7554187CD944130862E09ED4279FD5311F16A6735D07CF357148D11250F`.

`comparisons/ASX_vincenzo_di_benedetto_result_reference.png` compares the raw
painted candidate, processed candidate, and canonical leader references.
`comparisons/ASX_vincenzo_di_benedetto_archival_result_comparison.png` compares
the archival crop directly with the processed candidate and style-only
reference. Their SHA-256 values are respectively
`6603E51F0FF2EC3CEC76FE2E570917EBCDA8688B147F803C91748BFAA3A59A76`
and `7C52D1BD089271AE57F9FBB0291579CE1F03E945FAEC36D072BE509718587665`.

## DDS and runtime status

No final DDS exists. The painted candidate is still awaiting independent audit,
so runtime conversion and wiring remain deferred. No runtime DDS, `.gfx`,
character, history, localisation, GUI, or gameplay file was edited.

## Ownership gate

Exact and variant `Di Benedetto`/`Vincenzo Di Benedetto` searches found no active
character or meaningful portrait owner in current Chaos Redux character/history,
portrait, interface/GFX, or localisation roots, and no exact owner in installed
vanilla character/history/interface/localisation roots. This scoped check does
not make an exclusivity claim about unrelated reference mods.

## Simplifications and blockers

- The source, crop, and painted candidate are complete, but independent review
  and the complete Sicily package audit remain outstanding.
- Di Benedetto's emergency army slot is an explicit role adaptation; it must not
  be described as an active 1936 historical command.
- The civilian suit and tie are intentional source evidence; no invented
  military clothing or insignia is authorized.
- No generated identity, generic substitute, female portrait, advisor/dossier,
  `_small` file, DDS, GFX edit, or gameplay change was made. ImageGen was used
  only to repaint the attributed archival identity under a source lock.
