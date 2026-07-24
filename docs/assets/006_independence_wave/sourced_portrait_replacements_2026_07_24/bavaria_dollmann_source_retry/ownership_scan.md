# IW-009 Bavaria Friedrich Dollmann ownership scan

This scan records the exact and variant ownership gate for `BAY_independence_wave_mountain_commandant`.

## Search terms

The scan used `Friedrich Dollmann`, `Friedrich Dollman`, `Friedrich Karl Albert Dollmann`, `Friedrich Karl Dollmann`, `Dollmann, Friedrich`, `Dollmann Friedrich`, `Generaloberst Dollmann`, `General der Artillerie Dollmann`, `Friedrich_Dollmann`, `Friedrich-Dollmann`, `friedrich_dollmann`, `GER_friedrich_dollmann`, `Dollmann`, and `Dollman`.

The stable token search additionally used `BAY_independence_wave_mountain_commandant` and `GFX_portrait_BAY_independence_wave_mountain_commandant`.

## Roots and results

| Root | Character/history/portrait/interface/localisation result | Disposition |
| --- | --- | --- |
| Current Chaos Redux: `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, `localisation/` | No Dollmann/Dollman identity owner. The stable token exists only in the IW-009 Bavaria package and its expected sprite consumer. | No origin owner; target token may retain its stable identity key. |
| Installed vanilla: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, `localisation/` | No Dollmann/Dollman character, recruitment, portrait, `.gfx` consumer, or localisation owner. | No vanilla transfer conflict. |
| Installed vanilla: `history/units/GER_1939.txt` | Incidental comment at line 461: `7. Armee (CO: Dollmann)`. | Not character ownership; no character id, portrait, or recruitment consumer resolves from this comment. |
| Installed vanilla: `history/units/GER_1939_nsb.txt` | Incidental comment at line 453: `7. Armee (CO: Dollmann)`. | Not character ownership; no character id, portrait, or recruitment consumer resolves from this comment. |
| Approved reference mod `1521695605`: corresponding character/history/portrait/interface/localisation roots | No Dollmann/Dollman identity owner and no Dollmann/Dollman-named file. | Disclosure only; no art or source copied. |
| Approved reference mod `2265420196`: corresponding character/history/portrait/interface/localisation roots | No Dollmann/Dollman identity owner and no Dollmann/Dollman-named file. | Disclosure only; no art or source copied. |
| Approved reference mod `1458561226`: corresponding character/history/portrait/interface/localisation roots | No Dollmann/Dollman identity owner and no Dollmann/Dollman-named file. | Disclosure only; no art or source copied. |

The `common/operatives/` directory is absent in all five roots and therefore has no possible owner match in this scan.

No same-person owner is active in the current project, installed vanilla, or approved reference mods.

No transfer guard is required.

## Stable consumer evidence

Current IW-009 source keeps `BAY_independence_wave_mountain_commandant` as the generated character token, checks it as a corps commander, assigns `GFX_portrait_BAY_independence_wave_mountain_commandant`, and localises the existing display name separately.

This source retry does not alter any of those gameplay, GFX, or localisation files.
