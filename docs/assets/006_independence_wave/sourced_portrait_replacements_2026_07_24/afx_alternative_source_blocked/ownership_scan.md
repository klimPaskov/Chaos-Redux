# IW-006 AFX Wallonia commander alternative ownership scan

Scan date: 2026-07-24.

Search terms covered exact and variant forms of `François-Joseph Ley`, `François Ley`, `Francois-Joseph Ley`, `Maurice Bricart`, `François Goormachtigh`, `Alphonse Dantinne`, `Werner Goffinet`, `Albert Bastin`, `Victor Descamps`, `Maurice Keyaerts`, `BEL_*` variants, `AFX_walloon_reserve_commander`, and `Marcel Delcourt`.

## Current Chaos Redux

No exact candidate owner for Ley, Bricart, Goormachtigh, Dantinne, Goffinet, or Albert Bastin was found in the searched current gameplay, portrait, interface, or localisation roots. The only live stable consumer hit is the existing AFX surface:

- `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-62` defines `AFX_walloon_reserve_commander` and uses `GFX_portrait_AFX_walloon_reserve_commander`.
- `history/countries/AFX - Wallonia.txt:18` recruits the token.
- `interface/006_independence_wave_region_01_portraits.gfx:14-15` binds the runtime texture.
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4` still names it `Marcel Delcourt`.

Herman Baltia is excluded by the parent because the existing trial failed likeness/stable-consumer transfer, even though no separate active character owner was found.

## Vanilla owner conflicts

- `common/characters/BEL.txt:730-740` defines `BEL_maurice_keyaerts`, binds `GFX_portrait_BEL_maurice_keyaerts` and its small card, and `history/countries/BEL - Belgium.txt:330` recruits it. Vanilla English localisation names the identity at `localisation/english/WUW_characters_l_english.yml:233`.
- `common/characters/BEL.txt:865-874` defines `BEL_victor_descamps`, binds `GFX_portrait_BEL_victor_descamps` and its small card, and `history/countries/BEL - Belgium.txt:334` recruits it. Vanilla English localisation names the identity at `localisation/english/WUW_characters_l_english.yml:236`.
- Jules-Joseph Pire is separately documented as an active vanilla owner in [the Pire blocked package](../afx_jules_pire_source_blocked/ownership_scan.md).

These active vanilla owners are dispositive. Their portraits or identity tokens must not be copied or repurposed.

## Approved reference scan

The exact and variant searches returned no matching character/portrait files for Ley, Bricart, Goormachtigh, Dantinne, Goffinet, or Albert Bastin in approved Kaiserreich `1521695605` or approved references `2265420196` and `1458561226`. This absence does not cure the independent source-rights failures listed in the manifest.

## Transfer disposition

No guarded transfer contract exists for any candidate in this sweep. Keep `AFX_walloon_reserve_commander` closed until a new identity passes both the source-rights gate and the stable-consumer transfer decision.
