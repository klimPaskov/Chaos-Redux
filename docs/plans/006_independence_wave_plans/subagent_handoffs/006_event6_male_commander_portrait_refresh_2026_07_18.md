# Event 006 male commander and institutional portrait refresh handoff

Date: 2026-07-18
Producer: generated event-art asset subagent
Independent visual reviewer: `/root` (reviewed commander and institutional processed contact sheets before runtime promotion)

## Scope completed

- Refreshed ten existing fictional male commander large portraits: ACX, AEX, AFX, AGX, AJX, BAY, BRI, RHI, SCO, WLS.
- Derived ten matching commander small portraits at exact `65x67` from their matching full masters.
- Added ten additional fictional male role-only leader portraits requested for the institutional/country-leader stems: ACX port-and-mines committee, AEX civil-industrial board, AFX provisional assembly, AGX coastal council, AJX municipal-neutral commission, BAY state council, BRI civic commission, RHI provisional directorate, SCO civic convention, WLS national council.
- Every portrait is one distinct adult male person; no women, crowds, collective-body scenes, generic office-title portraits, or duplicate faces.
- Protected runtime files were not touched: BAY Rupprecht SHA-256 `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`; RHI Matthes SHA-256 `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`.

## Package

`docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/`

The package retains ImageGen source PNGs, prompts, source manifests, processed PNGs, review sheets, final DDS files, decoded DDS PNGs, contact sheets, metadata, and hash inventories. `manifest.md` is the package source of truth; `gfx_handoff.md` contains the engine-facing mapping.

## Runtime changes

Thirty non-protected runtime DDS files were updated under `gfx/leaders/006_independence_wave/`: twenty `156x210` large portraits and ten commander-only `65x67` small portraits. Existing filenames and sprite identifiers remain stable. No `.gfx`, gameplay, localisation, GUI, focus, decision, idea, country, history, or tag files were edited.

## Validation evidence

- DDS parser checks: `DDS ` magic, 124-byte header, pixel format at byte 76, flags 65, 32-bit BGRA masks, texture caps, zero mipmaps, exact `128 + width*height*4` length.
- All thirty DDS decodes are pixel-identical to their processed PNG inputs.
- Runtime dimensions: twenty `156x210`, ten `65x67`.
- Current protected BAY/RHI hashes match the user-pinned values exactly.
- Root independently reviewed `processed_156x210_contact_sheet.png`, `institutional_processed_contact_sheet.png`, and the small commander contact sheets and approved all thirty for runtime.
- Package text and filenames contain no advisor, advisor-icon, advisor-portrait, advisor renderer, or advisor reference material.

## Remaining risks

- The main agent should verify the existing `.gfx` registrations still point to these stable filenames; no registration edits were made in this handoff.
- Gameplay should assign plausible actual-ish male personal names from matching regional pools for all one-person portraits, including role labels that mention councils, boards, commissions, or directorates. Do not assign generic office titles or female metadata.

## Simplifications and fallbacks

None. No protected portrait was regenerated, no advisor asset was produced, and no placeholder or fallback artwork was used.
