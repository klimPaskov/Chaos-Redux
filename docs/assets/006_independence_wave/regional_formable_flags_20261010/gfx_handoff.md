# GFX handoff - regional formable federation flags

Native flag files for the three registered cosmetic identities. Each tag has the base triplet plus the four ideology aliases (`_communism`, `_democratic`, `_fascism`, `_neutrality`) at every size, which are byte copies of the base file.

| Cosmetic tag | Federation name | Normal 82x52 | Medium 41x26 | Small 10x7 |
| --- | --- | --- | --- | --- |
| `LKX` | Great Lakes Federation | `gfx/flags/LKX.tga` | `gfx/flags/medium/LKX.tga` | `gfx/flags/small/LKX.tga` |
| `HLX` | Horn League State | `gfx/flags/HLX.tga` | `gfx/flags/medium/HLX.tga` | `gfx/flags/small/HLX.tga` |
| `IOX` | Indian Ocean League State | `gfx/flags/IOX.tga` | `gfx/flags/medium/IOX.tga` | `gfx/flags/small/IOX.tga` |

Alias naming per size folder: `<TAG>_communism.tga`, `<TAG>_democratic.tga`, `<TAG>_fascism.tga`, `<TAG>_neutrality.tga` in `gfx/flags/`, `gfx/flags/medium/` and `gfx/flags/small/`. Total 45 files.

Target `.gfx`: none; these are native country and cosmetic-tag flag paths.

Sprite name: none; standard HOI4 flag lookup uses the tag basename (with the ideology suffix) and the native size subfolders.

Tags, palette colours and English names are registered outside this package (`common/countries/cosmetic.txt` and localisation). The parent integration confirms that each formable route applies its cosmetic tag and that the engine displays the three sizes; this handoff makes no live-engine claim.

Use `manifest.md` for the design table, lineage, rejected candidates, TGA schema evidence, hashes and verification.
