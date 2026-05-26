# Event 005 Generated Event Art Sidecar Handoff

Date: 2026-05-26

Scope: inspect `docs/assets/005_soviet_union_collapse/manifest.md`, `gfx/leaders/005_soviet_collapse/`, and current Event 005 custom/non-vanilla flag assets under `gfx/flags/`. Do not edit gameplay, localisation, `.gfx`, GUI, focus, decision, event, scripted effect, scripted trigger, spreadsheet files, or docs outside this handoff path.

## Files Changed

- Added this handoff only: `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/generated_event_art_sidecar_2026_05_26_flags_portraits_recheck.md`

No asset files were created or modified.

## Inspection Summary

- Active custom/cosmetic flag families checked: `33` (`32` active custom Event 005 tags from the manifest plus `UKR_BLACK_BANNER`).
- Active flag result: no missing normal/medium/small TGA files, no invalid dimensions, no invalid 32bpp/bottom-origin TGA headers, and no byte-identical base-vs-ideology duplicate groups.
- Active leader/council portraits checked: `37` (`32` active custom Event 005 tags plus vanilla-supported release council portraits `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`).
- Active portrait result: no missing DDS files, all active DDS files are `156x210`, no duplicate active portrait hashes, and no vanilla leader DDS hash matches.
- Vanilla-supported ordinary/internal republic default flag overrides checked for `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`: no mod-side default `gfx/flags/<TAG>*.tga` overrides found.

## Assets Created Or Skipped

Created: none.

Skipped as already complete:

- Active generated/historically grounded custom ideology and route flag art for the manifest active set and `UKR_BLACK_BANNER`.
- Active generated leader/council portraits for custom Event 005 tags and the release council tags `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`.

Skipped as inactive/stale:

- `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS` have portrait DDS files and full flag triads on disk, but prior Event 005 handoffs identify them as inactive/stale asset families. Their flag ideology variants are still byte-identical within each family. I did not generate replacements because the current parent task only authorizes genuinely missing custom Event 005 assets, and these tags should not be revived unless the parent restores them to active country-package use.

## Blockers And Uncertainty

- No blocker for the active Event 005 generated leader/council portrait or custom route/ideology flag surfaces inspected here.
- The only uncertainty is design ownership for the inactive/stale tag families listed above. If the parent makes any of those tags active again, they will need unique generated council portraits/flag families or an explicit approval to keep their current inactive placeholder-style asset state.

## Validation Commands

- Parsed DDS headers for active leader portrait dimensions.
- Parsed TGA headers for active custom/cosmetic flag dimensions, bpp, and origin bits.
- Compared SHA-256 hashes within active leader portraits, within active flag family base/ideology variants, and against vanilla leader DDS files under `/home/klim/projects/Hearts of Iron IV/`.
- Checked that vanilla-supported ordinary/internal republic tags have no default mod-side flag overrides.
