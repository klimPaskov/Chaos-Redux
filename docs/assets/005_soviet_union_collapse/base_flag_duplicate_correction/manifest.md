# Event 005 Base Flag Duplicate Correction

Scope: asset-only generated flag pass for active Event 005 custom/cosmetic tags with duplicate no-suffix base flags. This pass did not edit gameplay, `.gfx`, localisation, focus, decision, history, country, or spreadsheet files.

Reference folders inspected:

- `.agents/skills/chaos-redux-event-assets/assets/flags`
- `gfx/flags/`
- `docs/assets/005_soviet_union_collapse/manifest.md`

User constraints applied:

- Existing vanilla-supported ordinary/internal tags keep game-provided base and ideology flags.
- No default mod-side overrides are created for `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, or `TAN`.
- Custom active tags with duplicate no-suffix base flags receive unique normal, medium, and small TGA outputs.
- Ideology flags were inspected by hash; this pass found no active custom/cosmetic ideology duplicate hashes and did not create simple recolor/filter/shape-only ideology variants.
- Final flag TGAs use the repository flag format: 32-bit TGA, bottom-left origin, normal `82x52`, medium `41x26`, small `10x7`.

Initial audit result:

- Missing active custom/cosmetic flag files: `0`
- Bad active custom/cosmetic flag dimensions: `0`
- Vanilla-supported default mod-side flag overrides: `0`
- Duplicate no-suffix base flag groups before this pass: `5` groups, `20` files across each size.

Completed bounded output:

| Tag | Asset type | Source mode | Source PNG | Processed PNG previews | Final TGA outputs | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `DHC` | base country flag | Codex built-in `image_gen` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/source_png/DHC_base_source.png` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/processed_png/DHC_base_<normal\|medium\|small>.png` | `gfx/flags/DHC.tga`, `gfx/flags/medium/DHC.tga`, `gfx/flags/small/DHC.tga` | complete |
| `KHC` | base country flag | Codex built-in `image_gen` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/source_png/KHC_base_source.png` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/processed_png/KHC_base_<normal\|medium\|small>.png` | `gfx/flags/KHC.tga`, `gfx/flags/medium/KHC.tga`, `gfx/flags/small/KHC.tga` | complete |
| `FEV` | base country flag | Codex built-in `image_gen` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/source_png/FEV_base_source.png` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/processed_png/FEV_base_<normal\|medium\|small>.png` | `gfx/flags/FEV.tga`, `gfx/flags/medium/FEV.tga`, `gfx/flags/small/FEV.tga` | complete |
| `SZA` | base country flag | Codex built-in `image_gen` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/source_png/SZA_base_source.png` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/processed_png/SZA_base_<normal\|medium\|small>.png` | `gfx/flags/SZA.tga`, `gfx/flags/medium/SZA.tga`, `gfx/flags/small/SZA.tga` | complete |
| `MRC` | base country flag | Codex built-in `image_gen` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/source_png/MRC_base_source.png` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/processed_png/MRC_base_<normal\|medium\|small>.png` | `gfx/flags/MRC.tga`, `gfx/flags/medium/MRC.tga`, `gfx/flags/small/MRC.tga` | complete |
| `BAC` | base country flag | Codex built-in `image_gen` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/source_png/BAC_base_source.png` | `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/processed_png/BAC_base_<normal\|medium\|small>.png` | `gfx/flags/BAC.tga`, `gfx/flags/medium/BAC.tga`, `gfx/flags/small/BAC.tga` | complete |

Contact sheet:

- `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/contact_sheets/event005_base_flag_duplicate_correction.png`

Post-pass audit result:

- Missing active custom/cosmetic flag files: `0`
- Bad active custom/cosmetic flag dimensions: `0`
- Bad active custom/cosmetic TGA bpp/origin: `0`
- Vanilla-supported default mod-side flag overrides: `0`
- Duplicate no-suffix base flag groups remaining after the follow-up audit: `0`.

Notes:

- This pass intentionally does not claim completion of the overall Event 005 goal.
- Flags are final HOI4 TGA assets rather than DDS assets because HOI4 country flags are consumed from `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
