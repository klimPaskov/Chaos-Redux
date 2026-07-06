# Flag Refresh 2026-07-06

## Overview

This pass fixes upside-down flag artwork for the listed country and cosmetic flags, then regenerates the `RMC_neutrality` flag for the Republic of Red Witnesses.

No `.gfx` handoff is required. HOI4 resolves country flags directly from `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

## Source Mode

- `death_herald_of_zol`, `death_black_apostolate`, and `KMB` variants: existing asset correction. The normal flag artwork was flipped vertically, then medium and small variants were regenerated from the corrected normal artwork.
- `RMC_neutrality`: `$imagegen` source artwork, cropped and resized into HOI4 flag sizes.

## Image Generation Prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV country flag source art
Primary request: Create a clean flat fictional flag for the RMC neutrality country, the Republic of Red Witnesses, from a Red Martyrs / revolutionary mourning / witness-commune identity.
Style/medium: flat vexillological flag design, not a waving cloth, no lighting, no folds, no texture mockup.
Composition/framing: landscape rectangle close to 82:52 aspect ratio, centered emblem, bold simple shapes readable at tiny game sizes.
Subject: deep crimson field with a solemn ivory witness ledger or memorial tablet emblem combined with a small red star, black mourning accents, restrained revolutionary shrine symbolism.
Color palette: deep red, black, aged ivory, muted gold if needed.
Constraints: no text, no letters, no numbers, no watermark, no photorealistic fabric, no gradients, no complex coat of arms, no tiny unreadable details, no skulls, no gore.
Avoid: modern logos, crosses, religious symbols that dominate the design, realistic flagpole, background scene.
```

## Files

| Asset | Source | Processed PNG previews | Final TGAs |
| --- | --- | --- | --- |
| death_herald_of_zol | existing TGA correction | `docs/assets/flag_refresh_20260706/processed_png/death_herald_of_zol_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/death_herald_of_zol.tga`, `gfx/flags/medium/death_herald_of_zol.tga`, `gfx/flags/small/death_herald_of_zol.tga` |
| death_black_apostolate | existing TGA correction | `docs/assets/flag_refresh_20260706/processed_png/death_black_apostolate_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/death_black_apostolate.tga`, `gfx/flags/medium/death_black_apostolate.tga`, `gfx/flags/small/death_black_apostolate.tga` |
| KMB | existing TGA correction | `docs/assets/flag_refresh_20260706/processed_png/KMB_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/KMB.tga`, `gfx/flags/medium/KMB.tga`, `gfx/flags/small/KMB.tga` |
| KMB_communism | existing TGA correction | `docs/assets/flag_refresh_20260706/processed_png/KMB_communism_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/KMB_communism.tga`, `gfx/flags/medium/KMB_communism.tga`, `gfx/flags/small/KMB_communism.tga` |
| KMB_democratic | existing TGA correction | `docs/assets/flag_refresh_20260706/processed_png/KMB_democratic_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/KMB_democratic.tga`, `gfx/flags/medium/KMB_democratic.tga`, `gfx/flags/small/KMB_democratic.tga` |
| KMB_fascism | existing TGA correction | `docs/assets/flag_refresh_20260706/processed_png/KMB_fascism_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/KMB_fascism.tga`, `gfx/flags/medium/KMB_fascism.tga`, `gfx/flags/small/KMB_fascism.tga` |
| KMB_neutrality | existing TGA correction | `docs/assets/flag_refresh_20260706/processed_png/KMB_neutrality_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/KMB_neutrality.tga`, `gfx/flags/medium/KMB_neutrality.tga`, `gfx/flags/small/KMB_neutrality.tga` |
| RMC_neutrality | `docs/assets/flag_refresh_20260706/source_png/RMC_neutrality_source.png` | `docs/assets/flag_refresh_20260706/processed_png/RMC_neutrality_82x52.png`, `_41x26.png`, `_10x7.png` | `gfx/flags/RMC_neutrality.tga`, `gfx/flags/medium/RMC_neutrality.tga`, `gfx/flags/small/RMC_neutrality.tga` |

## Contact Sheet

`docs/assets/flag_refresh_20260706/contact_sheets/flag_refresh_20260706_contact_sheet.png`

## Validation

- Normal flags are 82x52.
- Medium flags are 41x26.
- Small flags are 10x7.
- TGAs are uncompressed 32-bit true-color with bottom-left origin and no top-origin bit.
