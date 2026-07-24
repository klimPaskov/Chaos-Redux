# IW-006 AFX Wallonia commander ownership scan: Jules-Joseph Pire

Scan date: 2026-07-24.

Scope: exact and spelling-variant identity ownership for `Jules Pire`, `Jules-Joseph Pire`, `Jules Joseph Pire`, `Jules_Pire`, `Pire Jules`, and `BEL_jules_pire`, plus the current AFX stable consumer `AFX_walloon_reserve_commander` and `Marcel Delcourt`.

## Current Chaos Redux

No active Chaos Redux character, history, portrait, interface/GFX, or localisation owner for the exact Pire identity was found in the searched gameplay and visual roots. The existing AFX consumer is a separate identity:

- `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-62` defines `AFX_walloon_reserve_commander` and points to `GFX_portrait_AFX_walloon_reserve_commander`.
- `history/countries/AFX - Wallonia.txt:18` recruits `AFX_walloon_reserve_commander`.
- `interface/006_independence_wave_region_01_portraits.gfx:14-15` points the stable sprite to `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`.
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4` names the current token `Marcel Delcourt`.

This package does not rename that token, alter its localisation, or modify its portrait path.

## Vanilla owner evidence

The installed game owns Pire as an active Belgium character:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/BEL.txt:652` defines `BEL_jules_pire`.
- `BEL.txt:657` sets `name = BEL_jules_pire`.
- `BEL.txt:660-661` bind `GFX_portrait_BEL_jules_pire` and `GFX_portrait_BEL_jules_pire_small`.
- `BEL.txt:664-684` define the corps-commander instance and its traits/skills.
- `BEL.txt:690-694` define the advisor instance and `idea_token = BEL_jules_pire`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/BEL - Belgium.txt:328` recruits `BEL_jules_pire` in the DLC branch.
- `BEL - Belgium.txt:372` recruits `BEL_jules_pire` in the non-DLC branch.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/ideas_l_english.yml:1407` names the identity “Jules Pire”.

This is a dispositive active-owner collision under the portrait identity gate. No vanilla portrait file was copied or inspected as a source candidate.

## Approved-reference scan

The exact and variant searches returned no Pire owner in the searched roots of approved Kaiserreich `1521695605`, `2265420196`, or `1458561226`. That absence does not make Pire reusable because the installed vanilla owner is active and recruited.

## Transfer decision

No guarded transfer contract exists for `BEL_jules_pire`. Do not clone the vanilla portrait, reuse the vanilla token, or silently relabel `AFX_walloon_reserve_commander` as Pire. A future accepted identity needs a separate source package and an explicit stable-consumer/token decision.
