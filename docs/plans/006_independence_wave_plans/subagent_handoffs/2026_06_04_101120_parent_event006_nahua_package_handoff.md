# Event 006 Nahua Charter Assembly Package Handoff

Date: 2026-06-04

## Scope

Implemented the `iw_pkg_nahua` starter package as a bounded Event 006 tranche. The package uses vanilla `NAH` through San Salvador state `314`, matching vanilla dynamic-core precedent without adding a new country, history file, or flag set.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Identifiers Added

- Package id: `constant:independence_wave_package.nahua`
- Formation family: `constant:independence_wave_decision.formation_family_nahua_charter_assembly`
- Event-log types:
  - `constant:independence_wave_event_log.nahua_charter_assembly_formation_type`
  - `constant:independence_wave_event_log.nahua_san_salvador_records_package_type`
- Package flags:
  - `independence_wave_package_nahua`
  - `independence_wave_nahua_package_core_seeded`
  - `independence_wave_nahua_san_salvador_records_opened`
  - `independence_wave_nahua_charter_petitions_mapped`
  - `independence_wave_nahua_charter_assembly_proclaimed`
  - `independence_wave_nahua_charter_assembly_integrated`
  - `independence_wave_nahua_charter_assembly_failed`
- Focuses:
  - `independence_wave_nahua_san_salvador_records`
  - `independence_wave_nahua_charter_petitions`
- Decisions/missions:
  - `independence_wave_open_nahua_san_salvador_records`
  - `independence_wave_map_nahua_charter_petitions`
  - `independence_wave_proclaim_nahua_charter_assembly`
  - `independence_wave_integrate_nahua_charter_assembly`
- Idea:
  - `independence_wave_nahua_charter_assembly_spirit`

## Implementation Notes

- `can_independence_wave_seed_nahua_package` only permits `NAH` at chaos tier IV/V, while `NAH` does not exist, and while state `314` is controlled by a weakened non-capital host that still passes the host survival floor.
- The resolver dynamically adds a temporary `NAH` core to state `314` before candidate selection and removes it if `NAH` is not released.
- The reduced-release anchor explicitly supports `NAH` on state `314`.
- The formation route keeps wider claims out of this tranche. `independence_wave_map_nahua_charter_petitions_effect` records proof and claim ambition only.
- Event-log script localisation and GUI localisation cover the package and formation log types.
- The Liberation Provisional focus tree now has 85 focus blocks.
- The event catalog workbook row for Event 006 was aligned to the 85-focus count and the Nahua Charter Assembly package.

## Assets And Flags

No new flags or visual assets were created. This tranche reuses vanilla `NAH` flags, country history, localisation, council data, and portraits, plus existing Event 006 icons and the existing Guarani-style local-polity idea sprite.

## Validation

- Touched Clausewitz files are brace-balanced.
- Touched script files contain no `<=` or `>=`.
- `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml` still have UTF-8 BOM and no `:0` keys.
- Focus count check returned `85`.
- Focus localisation coverage found no missing focus names or descriptions.
- Workbook zip/XML scan found no formula-error tokens.
- LibreOffice headless conversion opened and re-exported `docs/spreadsheets/chaos_redux_events_catalog.xlsx` successfully.

## Remaining Risks

- Full Event 006 completion remains open; this handoff only covers the Nahua package tranche.
- No in-game runtime validation was performed in this environment.
