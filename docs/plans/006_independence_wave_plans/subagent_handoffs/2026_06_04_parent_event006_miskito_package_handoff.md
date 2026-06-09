# Event006 Miskito Package Parent Handoff

## Scope

Implemented `iw_pkg_miskito` as a high-chaos Event006 local-polity package using vanilla `MIS`.

## Vanilla evidence

- Vanilla tag: `common/country_tags/00_countries.txt` defines `MIS = "countries/Miskito.txt"`.
- Vanilla history: `history/countries/MIS - Miskito.txt` sets capital `317` and comments cores `312, 317`.
- Vanilla character: `common/characters/MIS.txt` defines `MIS_miskito_council` with council leader roles and portrait `GFX_portrait_MIS_council`.
- Vanilla precedent: Chile's Trial of Allegiance liberation decision dynamically adds `MIS` cores to states `312` and `317` before transferring/releasing the tag.
- Vanilla flags: all checked ideology sizes for `MIS` exist. No Chaos Redux flag files were changed.

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Gameplay wiring

- Candidate gate: `can_independence_wave_seed_miskito_package`
- Candidate path: `MIS` bypasses the ordinary pool only when the Miskito seed gate passes.
- Dynamic cores: Event006 adds `MIS` cores to states `312` and `317` before putting `MIS` in the candidate pool.
- Reduced release anchor: `MIS` prefers state `317`.
- Package identity: `independence_wave_package_miskito`, local-polity package type, package id `constant:independence_wave_package.miskito`, formation family `constant:independence_wave_decision.formation_family_shore_council`.
- Startup spirit: `independence_wave_miskito_shore_council_spirit`.
- Focus nodes: `independence_wave_miskito_shore_records`, `independence_wave_miskito_coastal_petitions`.
- Decisions/missions: `independence_wave_open_miskito_shore_records`, `independence_wave_map_miskito_coastal_petitions`, `independence_wave_proclaim_miskito_shore_council`, `independence_wave_integrate_miskito_shore_council`.
- Event log rows: `miskito_shore_records_package_type = 45`, `miskito_shore_council_formation_type = 44`.

## Assets

No new flag, country history, country tag, or country file was created. The package reuses vanilla `MIS` flags, vanilla council portrait, and existing Event006 local-land/border-survey/Guarani-style local-polity sprites.

## Risks for audit

- Verify the repaired Barotseland/Dahomey/Miskito reduced-anchor cluster remains brace-balanced and does not affect other package anchors.
- Verify event-log scripted localisation resolves both Miskito package and formation types in every list/detail context.

## Audit follow-up

The country-package audit found that the first Miskito dynamic core seeding pass could leave `MIS` cores on states `312` and `317` if `MIS` qualified for the candidate pool but was not selected by the random release loop. The implementation now marks those seeded state cores with `independence_wave_miskito_package_core_seeded` and clears them in `independence_wave_restore_temporary_package_cores` when `MIS` does not exist after the loop. If `MIS` does exist, the cleanup clears only the temporary state flags and leaves the cores for the released package.
