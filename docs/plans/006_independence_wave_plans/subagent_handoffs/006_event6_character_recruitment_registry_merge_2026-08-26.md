# Event 006 startup character recruitment registry merge

Date: 2026-08-26

## Scope

The two Event 006 startup recruitment files were merged into one history registry to reduce file fragmentation without changing the startup effects.

## Source change

- Removed `history/general/006_independence_wave_character_recruitment.txt`.
- Removed `history/general/006_independence_wave_additional_character_recruitment.txt`.
- Added `history/general/006_independence_wave_character_recruitment_registry.txt` containing the former blocks in their original order.

`history/general` files are loaded as general history effects, so no include directive or loader registration is required.

## Parity evidence

The merged registry contains 25 `every_possible_country` blocks and 54 `recruit_character` calls, matching the two former files exactly after comment removal. The block sequence and each guarded recruitment body are byte-equivalent at the script-body level; no country, character, condition, effect, or order was changed.

No FER recruitment was added because IW-057 remains a separate unresolved identity/rights gate. No runtime Event 006 gameplay, localisation, focus, AI, decision, asset, or portrait behavior was changed.

## Validation

- Static block-parity audit: 25 old blocks = 25 merged blocks; 54 old recruitment calls = 54 merged calls; exact block parity: pass.
- Repository reference scan found no active loader or script path that requires either former filename.
- No live game or save/load run was performed; that validation remains user-owned.

## Disposition

This is a structural file-fragmentation cleanup only. The Event 006 package admission boundary and all gameplay readiness gates remain unchanged.
