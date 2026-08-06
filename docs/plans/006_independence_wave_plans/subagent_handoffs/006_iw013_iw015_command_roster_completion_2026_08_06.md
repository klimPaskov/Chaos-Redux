# Event 006 IW-013 / IW-015 additive command roster completion

Date: `2026-08-06`.

## Changed files

- `common/characters/006_independence_wave_iberian_commanders.txt`
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`
- `events/006_independence_wave.txt`
- `localisation/english/006_independence_wave_iberian_l_english.yml`
- `docs/events/006_independence_wave/iberian_registered_packages.md`

## Contract

The NAV and GLC carriers keep their vanilla history, flags, ruling leader names, and meaningful trees. The hidden synchronous roster event now recruits one additive corps commander per package: `NAV_independence_wave_jose_antonio_aguirre` using the archived `GFX_portrait_NAV_jose_antonio_aguirre` source placeholder, and `GLC_independence_wave_alfonso_daniel_castelao` using `GFX_portrait_GLC_alfonso_daniel_castelao`. Both are all-male sourced historical identities and define only an army portrait plus corps-command role; no advisor or dossier icon is introduced.

The package triggers require the vanilla country leader, the recruited character, and `is_corps_commander = yes`. Setup clears the package checkpoint, invokes `chaosx.nr6.350`, and only then loads the dynamic force mapping. Cleanup retires the additive commander if present and leaves carrier history and ruling leaders untouched.

## Validation boundary

This is a source-level roster completion, not central attestation. The existing source-placeholder, rights, final-style, historical-flag, independent package audit, named probability, and live-game gates remain open. The package therefore remains fail-closed for the automatic ladder until those independent gates are promoted.
