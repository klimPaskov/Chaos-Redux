# ASX Sicily — Vincenzo Di Benedetto source-locked refinish trial

Date: 2026-07-22  
Event/package: IW-019 ASX Sicily  
Asset type: full male leader/army-command portrait  
Source mode: `grounded_source_only`  
Overall status: `needs_user_review` — source and crop are complete; the painted
real-person edit is intentionally pending an allowed generated-art producer and
independent identity/style audit.

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

## Finish request (not executed by this sourced subagent)

An allowed generated-art producer may use the exact source crop as the sole
identity reference and apply the prompt in `imagegen_prompt.md`. The result
must remain a separate raw master, then a processed opaque `156x210` PNG. The
producer must preserve facial geometry, expression, apparent age, hair, suit,
tie, pose, and recognizable source details; only the background, contrast, and
restrained painted texture may change. Reject any result that genericises,
beautifies, re-ages, invents a uniform/insignia, changes pose, or cannot be
identified confidently against the source.

This sourced role is forbidden from generating or reconstructing a real
portrait, so no ImageGen call or generated result is included here. The parent
must route the edit to an allowed generated-art workflow or keep this package
at `needs_user_review`.

## Style comparison

`comparisons/source_style_comparison.png` places the unchanged source crop, the
source-only native preview, and the canonical painted leader/commander families
side by side. The canonical references are not copied into the package:

- `den_thorvald_stauning.png` (leader family), SHA-256
  `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6`.
- `generic_africa_navy_2.png` (commander family), SHA-256
  `A608D7554187CD944130862E09ED4279FD5311F16A6735D07CF357148D11250F`.

No generated result exists to compare yet; the contact sheet deliberately labels
the source-only preview as non-final.

## DDS and runtime status

No final DDS exists. Converting the source-only resize would falsely present a
non-painted source as an approved final, so the repository converter is deferred
until an allowed finish is produced and independently audited. No runtime DDS,
`.gfx`, character, history, localisation, GUI, or gameplay file was edited.

## Ownership gate

Exact and variant `Di Benedetto`/`Vincenzo Di Benedetto` searches found no active
character or meaningful portrait owner in current Chaos Redux character/history,
portrait, interface/GFX, or localisation roots, and no exact owner in installed
vanilla character/history/interface/localisation roots. This scoped check does
not make an exclusivity claim about unrelated reference mods.

## Simplifications and blockers

- The source and crop are complete, but the requested painted identity edit is
  not produced in this sourced-agent package because real-person portrait
  generation/editing is outside this role's authority.
- Di Benedetto's emergency army slot is an explicit role adaptation; it must not
  be described as an active 1936 historical command.
- The civilian suit and tie are intentional source evidence; no invented
  military clothing or insignia is authorized.
- No generated identity, generic substitute, female portrait, advisor/dossier,
  `_small` file, DDS, GFX edit, or gameplay change was made.
