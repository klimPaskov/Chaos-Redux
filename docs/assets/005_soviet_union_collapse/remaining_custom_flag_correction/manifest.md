# Event 005 Remaining Custom Flag Correction Manifest

Event id: `005`

Event slug: `soviet_union_collapse`

Asset package: `remaining_custom_flag_correction`

Source mode for replaced assets: generated art.

Why generation is appropriate: all replaced targets are fictional/custom Event 005 base or route flags. No real historical national base flag or vanilla-supported country default flag was generated or overridden.

## Replaced Assets

Each asset status is `complete`.

| Asset | Type | Source PNG | Processed PNGs | Final TGAs | Notes |
| --- | --- | --- | --- | --- | --- |
| `BBH` | custom base flag | `source_png/BBH_base_source.png` | `processed_png/BBH_base_normal.png`, `processed_png/BBH_base_medium.png`, `processed_png/BBH_base_small.png` | `gfx/flags/BBH.tga`, `gfx/flags/medium/BBH.tga`, `gfx/flags/small/BBH.tga` | Generated Black Banner Host flag; replaces duplicate of preserved `FTH`. |
| `UKR_BLACK_BANNER` | route/cosmetic base flag | `source_png/UKR_BLACK_BANNER_base_source.png` | `processed_png/UKR_BLACK_BANNER_base_normal.png`, `processed_png/UKR_BLACK_BANNER_base_medium.png`, `processed_png/UKR_BLACK_BANNER_base_small.png` | `gfx/flags/UKR_BLACK_BANNER.tga`, `gfx/flags/medium/UKR_BLACK_BANNER.tga`, `gfx/flags/small/UKR_BLACK_BANNER.tga` | Generated fictional black-banner route flag; not a default `UKR` override. |
| `TNC` | custom base flag | `source_png/TNC_base_source.png` | `processed_png/TNC_base_normal.png`, `processed_png/TNC_base_medium.png`, `processed_png/TNC_base_small.png` | `gfx/flags/TNC.tga`, `gfx/flags/medium/TNC.tga`, `gfx/flags/small/TNC.tga` | Generated Turkestan National Council flag; replaces duplicate of preserved `BSC`. |
| `ALA` | custom base flag | `source_png/ALA_base_source.png` | `processed_png/ALA_base_normal.png`, `processed_png/ALA_base_medium.png`, `processed_png/ALA_base_small.png` | `gfx/flags/ALA.tga`, `gfx/flags/medium/ALA.tga`, `gfx/flags/small/ALA.tga` | Generated Alash Restoration Authority flag; replaces duplicate of preserved `BSC`. |
| `GAC` | custom base flag | `source_png/GAC_base_source.png` | `processed_png/GAC_base_normal.png`, `processed_png/GAC_base_medium.png`, `processed_png/GAC_base_small.png` | `gfx/flags/GAC.tga`, `gfx/flags/medium/GAC.tga`, `gfx/flags/small/GAC.tga` | Generated Green Army Congress flag; replaces duplicate of preserved `BSC`. |
| `UWD` | custom base flag | `source_png/UWD_base_source.png` | `processed_png/UWD_base_normal.png`, `processed_png/UWD_base_medium.png`, `processed_png/UWD_base_small.png` | `gfx/flags/UWD.tga`, `gfx/flags/medium/UWD.tga`, `gfx/flags/small/UWD.tga` | Generated Ural Workers Directorate flag; replaces duplicate of preserved `DSC`. |
| `IUL` | custom base flag | `source_png/IUL_base_source.png` | `processed_png/IUL_base_normal.png`, `processed_png/IUL_base_medium.png`, `processed_png/IUL_base_small.png` | `gfx/flags/IUL.tga`, `gfx/flags/medium/IUL.tga`, `gfx/flags/small/IUL.tga` | Generated Idel-Ural League flag; replaces duplicate of preserved `DSC`. |
| `ICD` | custom base flag | `source_png/ICD_base_source.png` | `processed_png/ICD_base_normal.png`, `processed_png/ICD_base_medium.png`, `processed_png/ICD_base_small.png` | `gfx/flags/ICD.tga`, `gfx/flags/medium/ICD.tga`, `gfx/flags/small/ICD.tga` | Generated Iron Commissariat of the Dead flag; replaces duplicate of preserved `DSC`. |
| `ARD` | custom base flag | `source_png/ARD_base_source.png` | `processed_png/ARD_base_normal.png`, `processed_png/ARD_base_medium.png`, `processed_png/ARD_base_small.png` | `gfx/flags/ARD.tga`, `gfx/flags/medium/ARD.tga`, `gfx/flags/small/ARD.tga` | Generated Arctic Naval Directorate flag; replaces duplicate of preserved `NRF`. |
| `NLC` | custom base flag | `source_png/NLC_base_source.png` | `processed_png/NLC_base_normal.png`, `processed_png/NLC_base_medium.png`, `processed_png/NLC_base_small.png` | `gfx/flags/NLC.tga`, `gfx/flags/medium/NLC.tga`, `gfx/flags/small/NLC.tga` | Generated Northern Lights Commune flag; replaces duplicate of preserved `NRF`. |

## Inspected, Not Replaced

- Preserved duplicate-cluster identities: `FTH`, `BSC`, `DSC`, `NRF`.
- User-named active flag sets: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR`.
- OGB active flag set: `OGB`, `OGB_communism`, `OGB_democratic`, `OGB_fascism`, `OGB_neutrality`.

No overwrite was made for these inspected sets because validation found no duplicate hashes within the active base/ideology sets and the contact sheets decoded upright.

## Validation Summary

- Duplicate base groups after replacement: no duplicate hashes across `FTH/BBH/UKR_BLACK_BANNER`, `BSC/TNC/ALA/GAC`, `DSC/UWD/IUL/ICD`, and `NRF/ARD/NLC` in normal, medium, or small outputs.
- Dimensions: replaced normal flags are `82x52`, medium flags are repository-standard `41x26`, and small flags are `10x7`.
- TGA format: replaced files are uncompressed true-color TGAs, 32 bpp, descriptor `8`.
- Orientation: contact sheets for normal, medium, and small outputs decode upright. No upside-down `OGB` output was found in the current active files.
- No default overrides were created for vanilla-supported countries.
