# Event 005 Current Asset Handoff

This is a review-only handoff for the active Event 005 Soviet Collapse asset state on 2026-05-25. It intentionally does not edit `.gfx`, gameplay, localisation, focus, decision, interface, or active flag files.

## Portraits

No generated portrait replacement is currently needed.

Evidence:

- Active wired portrait sprites checked: 37
- Missing DDS: 0
- Duplicate active portrait hashes: 0
- Bad dimensions: 0
- Expected size: 156x210
- Checked sprite sources: `interface/005_soviet_collapse_custom_icons.gfx`, `interface/005_soviet_collapse_factory_ancient_icons.gfx`
- Checked portrait folder: `gfx/leaders/005_soviet_collapse/`

The active portrait scope includes custom successor and council portraits for `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`, `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `PRA`, `TSC`, `ICD`, `RMC`, `DSC`, `NRF`, `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, and `ALN`.

## Flags

Missing flag files: none.

Duplicate active flag hashes: none.

Active dirty files that still need replacement or re-export review:

- `gfx/flags/small/CFR*.tga`
- `gfx/flags/small/KZR*.tga`
- `gfx/flags/small/SOG*.tga`
- `gfx/flags/small/KHW*.tga`
- `gfx/flags/small/ALN*.tga`
- `gfx/flags/small/KRS*.tga`
- `gfx/flags/small/RMC*.tga`
- `gfx/flags/small/UDC*.tga`
- `gfx/flags/small/SDZ*.tga`
- `gfx/flags/small/TSC*.tga`

Each group above includes base, `_communism`, `_democratic`, `_fascism`, and `_neutrality`, for 50 total files. The exact file list is in `audit/problem_small_flags.txt`.

Problem: these 50 small flags are currently `10x7` 8-bit color-mapped TGAs with descriptor `0x00`. The vanilla comparison file `/home/klim/projects/Hearts of Iron IV/gfx/flags/small/SOV.tga`, and clean active Event 005 small flags such as `gfx/flags/small/UKR_BLACK_BANNER.tga` and `gfx/flags/small/FTH.tga`, are `10x7` 32bpp RGBA TGAs with descriptor `0x08`.

The normal and medium files for the same tags are already `82x52` and `41x26` 32bpp TGAs with descriptor `0x08`; they do not need generated-art replacement based on this audit.

## Suggested Main-Agent Action

Re-export only the listed small flags as vanilla-compatible 32bpp RGBA TGAs with descriptor `0x08`, preserving the current visible art and orientation. Do this only when the active dirty flag owner is ready, because those files are already dirty and this sidecar deliberately did not overwrite them.

No `.gfx` changes are required for this issue.

## Review Evidence

- Contact sheet: `contact_sheets/problem_small_flags_current.png`
- Manifest: `manifest.md`
- Problem list: `audit/problem_small_flags.txt`
