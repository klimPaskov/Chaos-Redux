# Parent Handoff: Event006 Itza Package

## Scope

Implemented the `iw_pkg_itza` Central American local-polity tranche for Event 006 Independence Wave.

## Vanilla Evidence

- Vanilla tag: `ITZ`.
- Vanilla history uses Belize state `311` as capital and comments `311` as the Itza core.
- Vanilla character data includes the Itza council leader and portrait registration.
- Vanilla country, localisation, and all ideology flag assets already exist.
- Vanilla Chile liberation decisions dynamically add Itza's core before transfer, so Event 006 follows the same dynamic-core pattern instead of editing state history.

## Gameplay Wiring

- Candidate gate: `can_independence_wave_seed_itza_package`.
- Temporary package core: state `311`, tracked by `independence_wave_itza_package_core_seeded`.
- Cleanup: `independence_wave_restore_temporary_package_cores` removes the temporary ITZ core if ITZ was not selected and only clears the state flag if ITZ exists.
- Startup package: `independence_wave_package_itza`, package id `constant:independence_wave_package.itza`, local-polity family, and `independence_wave_itza_lake_council_spirit`.
- Focus route:
  - `independence_wave_itza_peten_records`
  - `independence_wave_itza_yucatan_petitions`
- Decision route:
  - `independence_wave_open_itza_peten_records`
  - `independence_wave_map_itza_yucatan_petitions`
  - `independence_wave_proclaim_itza_lake_council`
  - `independence_wave_integrate_itza_lake_council`
- Event-log milestones:
  - `constant:independence_wave_event_log.itza_peten_records_package_type`
  - `constant:independence_wave_event_log.itza_lake_council_formation_type`

## Assets

No new flag art was needed. The tranche uses vanilla ITZ flags, council portrait, and existing Event 006 local-polity focus, decision, and idea sprites.

## Files Touched

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Validation Plan

- Run diff whitespace checks for touched files.
- Verify no unsupported inclusive comparison operators.
- Count braces in touched script files.
- Verify localisation BOM and absence of `:0` keys in touched localisation.
- Recount Event 006 focus blocks.
- Verify no flag/country/history files were modified.
- Spawn an Event006 package audit subagent for the Itza tranche.

## Remaining Risks

- The broader Event006 implementation remains incomplete; this handoff only covers the Itza package tranche.
- Live game balance still depends on the wider package pool and chaos-tier release frequency.
