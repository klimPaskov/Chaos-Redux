# GFX handoff — ready-formable federation flags

The twelve native flag files are ready for the four registered cosmetic identities.

| Cosmetic tag | Federation name | Normal 82x52 | Medium 41x26 | Small 10x7 |
| --- | --- | --- | --- | --- |
| `NCX` | North Caucasian Federation | `gfx/flags/NCX.tga` | `gfx/flags/medium/NCX.tga` | `gfx/flags/small/NCX.tga` |
| `IDX` | Indus Federation | `gfx/flags/IDX.tga` | `gfx/flags/medium/IDX.tga` | `gfx/flags/small/IDX.tga` |
| `MRX` | Maritime Federation | `gfx/flags/MRX.tga` | `gfx/flags/medium/MRX.tga` | `gfx/flags/small/MRX.tga` |
| `MSX` | Mainland Southeast Asian Federation | `gfx/flags/MSX.tga` | `gfx/flags/medium/MSX.tga` | `gfx/flags/small/MSX.tga` |

Target `.gfx`: none; these are native country/cosmetic-tag flag paths.

Sprite name: none; standard HOI4 flag lookup uses the cosmetic tag basename and the native size subfolders.

The tags, registered colors, and English names are already present in the files identified in `manifest.md`.

Use the base no-suffix flag triplet when the corresponding Event 006 federation route applies its cosmetic identity; this package contains no ideology-specific flag variants.

The parent integration should confirm each route selects the intended cosmetic tag and that the engine displays its normal, medium, and small files; this handoff makes no live-engine completion claim.

Use `manifest.md` for visual review, source lineage, exact hashes, TGA schema evidence, and contact sheets.
