# IW-006 AFX Wallonia commander ownership scan

Date: 2026-07-24  
Candidate: Henri Denis / Henri-Jean-Charles-Eugene Denis  
Stable Event 006 consumer: `AFX_walloon_reserve_commander`

## Search terms

The scan used the exact and normalized variants `Henri Denis`, `Henri-Jean-Charles-Eugène Denis`, `Henri Jean Charles Eugene Denis`, `Denis Henri`, `Henri_Denis`, and `BEL_henri_denis`.

## Root results

| Root | Result |
|---|---|
| Current Chaos Redux `common`, `history`, `interface`, `gfx`, `localisation` | No exact or variant Henri Denis owner found. The current Event 006 AFX character remains the fictional `AFX_walloon_reserve_commander`; no identity transfer contract is present. |
| Vanilla HOI4 `common`, `history`, `interface`, `gfx`, `localisation` | No exact Henri Denis owner found. Vanilla does own considered alternatives `BEL_jules_pire`, `BEL_jean_baptiste_piron`, and `BEL_charles_bastin`, so those identities are not reusable clones. |
| Kaiserreich 1521695605 `common/characters` | `common/characters/BEL characters.txt:864-878` defines active `BEL_henri_denis` with `GFX_portrait_BEL_henri_denis_army_small`. |
| Kaiserreich 1521695605 `history/countries` | `history/countries/BEL - Belgium.txt:200` recruits `BEL_henri_denis`; line 249 marks it `BEL_walloon_character`. |
| Kaiserreich 1521695605 `interface` | `interface/kaiserreich/portraits/BEL_portraits.gfx:267-268` binds the portrait sprite to `gfx/interface/advisors/BEL/BEL_henri_denis.png`. |
| Kaiserreich 1521695605 `localisation` | `localisation/english/KR_country_specific/BEL - Belgium l_english.yml:1827-1828` names Henri Denis and records his Marbais birth. |
| Approved reference 2265420196 | No exact Henri Denis owner found in searched roots. |
| Approved reference 1458561226 | No exact Henri Denis owner found; incidental Pire/Bastin/Piron identity hits are not reusable. |

## Decision

The approved Kaiserreich character, recruitment, portrait, and Walloon marker are a live exact owner. Under the grounded portrait identity-ownership gate, this source cannot be cloned into the AFX consumer without a guarded transfer contract that explicitly invalidates or supersedes the origin owner.

The source package is therefore `blocked_current_owner`, even though the candidate has strong Wallonia linkage, 1936 viability, and a role-credible Belgian Army record.
