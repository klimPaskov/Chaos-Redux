# Louis Ruquoy / Rucquoy portrait-owner audit

This audit searched the exact and variant identity forms `Louis Hubert Ruquoy`, `Louis Rucquoy`, `Louis Ruquoy`, `Ruquoy`, and `Rucquoy` before treating the source as an additive grounded commander candidate.

## Search roots

- Current Chaos Redux: `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/`.
- Vanilla Hearts of Iron IV: the same five ownership paths under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
- Kaiserreich workshop reference `1521695605`: the same five ownership paths.
- Workshop references `2265420196` and `1458561226`: the same five ownership paths.

The search used case-insensitive whole-name and surname variants with `rg --pcre2`. No common-name pool or unrelated prose hit was treated as a character owner.

## Result

| Root | Exact or variant character/portrait owner | Disposition |
| --- | --- | --- |
| Chaos Redux | NO_MATCH | Safe additive research candidate |
| Vanilla HOI4 | NO_MATCH | No vanilla transfer guard needed |
| Kaiserreich 1521695605 | NO_MATCH | No reference-mod conflict found |
| Reference 2265420196 | NO_MATCH | No reference-mod conflict found |
| Reference 1458561226 | NO_MATCH | No reference-mod conflict found |

No live character, leader, commander, operative, portrait, or officeholder owner was found for the searched variants. No guarded existing-character transfer is required. This evidence does not authorize simultaneous ownership if another mod or future branch later defines Ruquoy; rerun the audit before runtime wiring.

## Identity and role evidence

The French-language biography snapshot in `research/ruquoy_frwiki_identity.html` records Louis Ruquoy's 3 November 1861 birth at Frasnes-lez-Buissenal, Hainaut, his 24 January 1937 death at Braine-l'Alleud, lieutenant-general rank, 5th Division command, 6 January 1917 Chief of the General Staff appointment, and later occupation-force command. This establishes the Walloon-region connection and confirms that he was alive in the complete 1936 calendar year.

The retirement caveat remains material: Ruquoy was pensioned on 1 January 1927. Use as a senior Walloon council commander or veteran strategist, not as a claim that he actively held the Belgian General Staff in 1936.
