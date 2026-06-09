# Event 006 Mesopotamian River Compact Package Handoff

## Scope

Implemented a vanilla-backed Mesopotamian River Compact package for Event 006 Independence Wave using `IRQ` as the carrier. The package starts from Baghdad state `291` only when `IRQ` is inactive, chaos tier IV/V is active, and state `291` has a weakened non-capital host that remains above the host-survival floor.

No flag, country tag, country history, state history, or country-definition files were edited. The package reuses vanilla IRQ history, characters, localisation, portraits, and flag assets.

## Gameplay wiring

- Added Mesopotamia constants for package id, formation family, event-log types, costs, thresholds, gains, integration stage, and failure pressure.
- Added `can_independence_wave_seed_mesopotamia_package`, `is_independence_wave_mesopotamia_package`, river-control, records, petition, proclamation, and failure triggers.
- Added IRQ reduced-release anchor preference for state `291` and candidate seeding.
- Added package classification for IRQ releases: `independence_wave_package_mesopotamia`, historical-return package type, Mesopotamia package id, Mesopotamian River Compact formable family, old-state memory gain, and package spirit.
- Added Formation Ledger decisions:
  - `independence_wave_open_mesopotamian_river_records`
  - `independence_wave_map_mesopotamian_river_petitions`
  - `independence_wave_proclaim_mesopotamian_river_compact`
  - `independence_wave_integrate_mesopotamian_river_compact`
- River petitions add claims only on Mosul `676`, Basrah `1011`, Anbar `1010`, and Al Hajara `675`; they do not transfer territory or add starting cores.
- Added two shared provisional focus overlays:
  - `independence_wave_mesopotamian_river_records`
  - `independence_wave_mesopotamian_river_charter`
- Added `independence_wave_mesopotamian_river_compact_spirit`.
- Added AI old-name restraint conditions for the Mesopotamia package.

## Event log and localisation

- Added package and formation log constants:
  - `mesopotamian_river_records_package_type`
  - `mesopotamian_river_compact_formation_type`
- Added record helpers:
  - `independence_wave_record_mesopotamian_river_records_package_log_entry`
  - `independence_wave_record_mesopotamian_river_compact_formation_log_entry`
- Added scripted localisation branches for current list, history detail, event detail, selected title, and selected body groups.
- Added GUI labels for package and formation log rows.
- Added English localisation for the package label, spirit, focuses, decisions, requirements, and integration tooltips.

## Documentation and catalog

- Updated `docs/events/006_independence_wave.md` for the IRQ anchor, package list, focus overlays, formation decisions, event-log rows, asset notes, and future-work package status.
- Updated `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md` with the implemented Mesopotamia package matrix row and implementation notes.
- Updated workbook row `G7` in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` to include `Mesopotamia/IRQ River Compact`.
- Removed the obsolete `chaosx_iw_event005_collision_checked` row from the achievement spec after audit found Event 006 was still carrying an Event 005 collision marker.

## Audit and fixes

Subagent Hilbert (`019e92ba-1a41-7eb3-a3bd-9ee43272636c`) returned an initial FAIL on the broader Event 006/Event 005 separation gate, while passing the Mesopotamia package itself. The reported blocker was that Event 006 trigger/effect logic still referenced `chaosx_iw_event005_collision_checked`, `chaosx_release_origin_soviet_collapse`, and `soviet_collapse_*` flags.

Parent fix:

- Removed Soviet Collapse/Event 005 flag checks from Event 006 release identity, achievement release, candidate-use, first impossible-state super-event, and first old-name super-event gates.
- Removed the `chaosx_iw_event005_collision_checked` set from Event 006 achievement tracking.
- Removed the obsolete achievement-spec variable row.

Hilbert re-audit result after the parent fix: PASS. The blocker grep returned no matches, trigger/effect brace balance stayed clean, and the Mesopotamia smoke check still held.

## Validation

Parent validation passed:

- Brace balance on touched Event 006 script files: all `balance=0 min=0`.
- Unsupported operator scan for `<=` and `>=`: no hits.
- Localisation BOM check: `006_independence_wave_l_english.yml` and `chaosx_gui_l_english.yml` both have UTF-8 BOM.
- Localisation `:0` scan: no hits.
- Mesopotamia localisation presence scan: package label, spirit, focuses, decisions, requirements, integration tooltips, and GUI log labels all present.
- Event 006/Event 005 runtime dependency grep after fix:
  - `rg -n "event005_collision|soviet_collapse|chaosx_release_origin_soviet" common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt`
  - no output.
- Workbook zip parse: `testzip = None`.
- Workbook row `G7`: contains `Mesopotamia/IRQ River Compact`.
- Flag/country/history/tag diff guard:
  - `git diff --name-only -- common/countries common/country_tags history/countries history/states gfx/flags common/flags`
  - no output.
- Vanilla reference checks:
  - `IRQ = "countries/Iraq.txt"` exists in vanilla country tags.
  - Vanilla `IRQ - Iraq.txt` uses `capital = 291`.
  - Vanilla states `291`, `676`, `1010`, `1011`, and `675` are IRQ-owned/core states.
  - Vanilla IRQ flag assets exist in large, medium, and small flag folders.

## Remaining risks

- The wider Event 006 goal is still incomplete. Remaining Event 006 package families, deeper overlays, visual polish, final audits, and closure checks remain open.
