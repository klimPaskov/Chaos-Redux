# Event 020 aftermath recovery tranche

## Delivered

The shared disease category now contains five paid post-crisis country projects: Rebuild and Keep Vigilance, International Inspection Compact, Condemn Future Weaponization, Population Recovery Programme, and Memorial and Biosecurity Charter. They are phase- and defeat-gated, use the country material band and civilian-factory reservations, register Response Capacity, resolve through Event 020 reports, and never cure a state by fiat.

Population Recovery applies a 420-day state stewardship modifier to controlled recovering or cured states with measurable devastation, lowering devastation and relapse risk while improving treatment. Memorial and Biosecurity Charter applies a permanent country flag and recovered-state stewardship modifier, advances findings, and records stability and war-support effects. Inspection Compact reduces internal transport, troop, refugee, and port spread through both source and target route calculations while its timed flag remains active.

## Changed source surfaces

- `common/script_constants/020_black_plague_shared_response_constants.txt`
- `common/script_constants/020_black_plague_constants.txt`
- `common/dynamic_modifiers/020_black_plague_dynamic_modifiers.txt`
- `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`
- `common/scripted_effects/020_black_plague_shared_response_effects.txt`
- `common/scripted_effects/020_black_plague_spread_effects.txt`
- `common/decisions/020_black_plague_shared_response_decisions.txt`
- `events/020_black_death.txt`
- `localisation/english/020_black_plague_response_l_english.yml`
- `localisation/english/020_black_plague_reports_l_english.yml`

## Evidence

The touched Clausewitz files have balanced braces and no unsupported comparison operators. Both modified localisation files retain UTF-8 BOM encoding and have no duplicate keys. New Event 020 report surfaces `.91` through `.95` have title, description, and option localisation. The country-tag audit continues to find exactly the accepted RTA/RTX rat package with no external collisions. Offline Event Inspector lint for `.94` and `.95` returned no blocking diagnostics.

## Open boundary

SCN-012 still fails closed on preflight and clears reservations on downstream failure, but a complete journaled rollback of every already-applied disease, transfer, country, and Chaos mutation is not yet proven. Live mission, mapmode, audio, balance, and release-rights validation remain user-owned checks. No 3D models were created or added.
