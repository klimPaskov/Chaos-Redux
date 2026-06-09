# Event 006 Don Cossack Krug Package Parent Handoff

## Scope

Implemented the next Event 006 country-package tranche recommended by the read-only package audit: vanilla `DON` as the Don Cossack Krug historical-return package.

No flag files were edited or created. The package uses vanilla `DON` flag support and existing Event 006 old-name/archive icon families.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/assets/006_independence_wave/focus_icons/manifest.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_143041_parent_event006_don_package_handoff.md`

## Gameplay Implemented

- Added `can_independence_wave_seed_don_package` for high-chaos weakened-host releases from Rostov state `218`.
- Added `DON` to the Event 006 candidate tag gate and verified package seeding.
- Added a verified reduced-release anchor for `DON` at Rostov `218`.
- Temporarily seeds Rostov as the Don anchor core and masks any existing Don cores on Millerovo `245` and Volgodonsk `238` during release selection, restoring masked cores afterward.
- Classifies Event 006 `DON` releases as `independence_wave_package_don` with package id `don_cossack_host` and formable family `formation_family_don_cossack_krug`.
- Added two focus-tree overlays:
  - `independence_wave_don_river_records`
  - `independence_wave_don_petition_map`
- Added decisions and integration mission:
  - `independence_wave_open_don_river_records`
  - `independence_wave_map_don_petitions`
  - `independence_wave_proclaim_don_cossack_krug`
  - `independence_wave_integrate_don_cossack_krug`
- Added Don Cossack Krug national spirit and AI old-name package restraint hooks.
- Added Event Log package and formation rows for Don River Records and Don Cossack Krug.

## Documentation And Catalog

- Updated Event 006 docs to describe Don as implemented, including no-new-flag handling.
- Updated country-package and focus-tree specs to move Don from candidate framing to implemented package framing.
- Updated focus-icon manifest validation count from 115 to 117.
- Updated `docs/spreadsheets/chaos_redux_events_catalog.xlsx` row 7:
  - `C7`: shared 117-focus Liberation Provisional tree.
  - `G7`: added `Don/DON Cossack Krug` to current starter proofs.
  - `O7`: shared 117-focus Liberation Provisional tree.
  - `L7` and `R7` remain `In progress`.

## Validation

- Focus block count: `117`.
- New focus ids found:
  - `independence_wave_don_river_records`
  - `independence_wave_don_petition_map`
- Lightweight brace balance across touched Clausewitz/scripted localisation files: all `0`.
- Unsupported operator scan over touched Event 006 script/localisation files: no `<=` or `>=`.
- Localisation BOM check:
  - `localisation/english/006_independence_wave_l_english.yml`: UTF-8 BOM preserved.
  - `localisation/english/chaosx_gui_l_english.yml`: UTF-8 BOM preserved.
- Don localisation key check: all new focus, decision, idea, package-label, tooltip, and Event Log keys present.
- Workbook validation:
  - `unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx`: passed.
  - Source workbook XML: `117-focus` count `2`, `115-focus` count `0`, `Don/DON Cossack Krug` count `1`, error strings `0`, formula markers `23`.
  - LibreOffice headless conversion to `/tmp/chaosx_catalog_validate_event006_117/chaos_redux_events_catalog.xlsx`: passed.
  - Converted workbook archive test: passed.
  - Converted workbook XML: `117-focus` count `2`, `115-focus` count `0`, `Don/DON Cossack Krug` count `1`, error strings `0`, formula markers `30`.

## Remaining Risks And Omissions

- Event 006 remains incomplete. Remaining work includes additional package data, formables, GUI states, asset polish, final audits, and completion validation.
- Don leader portrait registration was not verified by the read-only audit; this tranche does not add or depend on new portrait art.
- No flags were changed. No new flag subagent was needed because vanilla `DON` flag assets exist.
