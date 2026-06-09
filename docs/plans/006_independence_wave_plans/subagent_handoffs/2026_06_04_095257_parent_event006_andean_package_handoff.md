# Event006 Andean Community League Package Handoff

Implemented the bounded `iw_pkg_andes_communes` tranche for Event006 Independence Wave using vanilla `INC` as the carrier.

## Scope

- Added high-chaos `INC` candidate seeding through `can_independence_wave_seed_andean_package`.
- Seeded temporary release cores only on states `947`, `494`, and `951`.
- Added package-specific reduced-release anchors for those states so the initial release starts from one verified seat and does not grant Lima or broader Andean claims for free.
- Added cleanup for temporary `INC` cores if the candidate is not released, and flag cleanup if it is released.
- Added package assignment flags, package id `andes_communes`, local-polity package type, formable family, and startup spirit.
- Added Formation Ledger decisions:
  - `independence_wave_open_andean_highland_records`
  - `independence_wave_map_andean_petitions`
  - `independence_wave_proclaim_andean_community_league`
  - `independence_wave_integrate_andean_community_league`
- Added two focus overlay nodes:
  - `independence_wave_andean_highland_records`
  - `independence_wave_andean_petition_map`
- Added event-log package and formation emitters:
  - `andean_highland_records_package_type`
  - `andean_community_league_formation_type`
- Updated package label scripted localisation, event-log scripted localisation, English localisation, Event006 docs, country package spec, and workbook Event006 row.

## Vanilla Evidence

- Vanilla `INC` exists in `common/country_tags/00_countries.txt`.
- Vanilla `history/countries/INC - Inca.txt` provides capital/history setup and `INC_inca_council`.
- Vanilla localisation provides Neo-Inca/Inca names and adjective strings.
- Vanilla flags, country history, council, portraits, and localisation are reused. No new flags were created or edited.
- Mapuche was not used as a fallback. Vanilla evidence still points to Mapuche being cosmetic Chile content rather than a standalone release tag.

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

## Validation

- Brace balance passed for touched Event006 script/localisation helper files.
- Raw unsupported operator scan for `<=` and `>=` returned no hits in touched files/docs.
- Localisation files still have UTF-8 BOM and no `:0` keys.
- Focus block count is `83`.
- Focus name and description localisation coverage is complete for the Event006 focus tree.
- Workbook Event006 row now references the `83-focus` tree and Andean Community League starter proof.
- LibreOffice headless conversion opened and rewrote the workbook successfully.
- Direct workbook XML scan found no Excel formula error tokens.

## Remaining Risks

- `recalc.py` could not run because `openpyxl` is not installed in the environment. No workbook formulas were edited; the change only touched inline text cells.
- The Andean package deliberately starts from non-capital supported seats and records Lima, Piura, and Antofagasta as later claims. It does not implement a deeper Aymara-specific package or a Mapuche package.
- Event006 remains incomplete overall. Remaining blockers in the event docs still apply.
