# Parent Handoff: Event006 Bechuanaland Kgotla Council Package

## Scope

Implemented a vanilla-backed Bechuanaland local-polity package for Event 006 using the existing `BOT` tag and vanilla state `542`.

## Evidence Used

- Vanilla `history/countries/BOT - Botswana.txt` sets capital `542` and provides country history/characters.
- Vanilla `history/states/542-Bechuana Land.txt` gives state `542` a `BOT` core and ENG ownership.
- Vanilla localisation and flag assets already exist for `BOT`; no new flags or placeholder flag files were created.

## Files Changed

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
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
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Implemented Identifiers

- Package flag: `independence_wave_package_bechuanaland`
- Package id: `constant:independence_wave_package.bechuanaland`
- Formation family: `constant:independence_wave_decision.formation_family_bechuanaland_kgotla_council`
- Event-log types:
  - `constant:independence_wave_event_log.bechuanaland_kgotla_council_formation_type`
  - `constant:independence_wave_event_log.bechuanaland_kgotla_records_package_type`
- Focuses:
  - `independence_wave_bechuanaland_kgotla_records`
  - `independence_wave_bechuanaland_land_petitions`
- Decisions:
  - `independence_wave_open_bechuanaland_kgotla_records`
  - `independence_wave_map_bechuanaland_land_petitions`
  - `independence_wave_proclaim_bechuanaland_kgotla_council`
  - `independence_wave_integrate_bechuanaland_kgotla_council`
- Spirit: `independence_wave_bechuanaland_kgotla_council_spirit`

## Validation Status

Validation completed after implementation:

- Focus block/`ai_will_do`/`completion_reward` count is `97`/`97`/`97`.
- Localisation files kept UTF-8 BOM, no `:0` keys were found, and the Bechuanaland keys were present with no duplicates.
- Brace balance passed across touched Event 006 script files.
- Unsupported `<=`/`>=` scan returned no hits in the touched Event 006 script/localisation files.
- Workbook zip integrity passed, the catalog row carries the `97-focus` marker, and headless LibreOffice conversion passed.
- Read-only country-package audit subagent found no BOT gameplay blocker. Its workbook-row finding was fixed by updating Event006 row `G7` to list `Namibia/NMB Land Council` and `Bechuanaland/BOT Kgotla Council`.

## Remaining Risks

- The route intentionally uses vanilla `BOT`; no bespoke flag asset work was required.
- This does not resolve blocked non-vanilla packages such as Mapuche, Herero, Nama, or Basotho because no verified vanilla tag was found for those candidates in the current pass.
