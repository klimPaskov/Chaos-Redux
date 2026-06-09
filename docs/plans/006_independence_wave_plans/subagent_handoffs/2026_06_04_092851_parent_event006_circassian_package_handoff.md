# Event006 Circassian Mountain Council Package Handoff

Parent implementation tranche for `iw_pkg_circassia`.

## Scope

- Added the Circassian Mountain Council as a local-polity Event006 package using vanilla `KBK` and release anchor state `827`.
- Added mountain-records and pass-petition proof work, two focus overlays, four Formation Ledger decisions/missions, event-log entries, localisation, documentation, and catalog alignment.
- Reused existing Event006 local-polity icons and vanilla `KBK` country/flag assets. No new flags, flag replacements, or new flag artwork were created in this tranche.
- Event006 remains incomplete.

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
  - Added Circassian package ids, log types, formation family, costs, thresholds, and tuning constants.
- `common/scripted_triggers/006_independence_wave_triggers.txt`
  - Added `KBK` candidate eligibility and Circassian package/proof/integration/failure triggers.
- `common/scripted_effects/006_independence_wave_effects.txt`
  - Added `KBK` release anchor handling, candidate seeding, package scoring, Circassian proof effects, pass-petition claims, integration/failure effects, and event-log emitters.
- `common/ideas/006_independence_wave_ideas.txt`
  - Added `independence_wave_circassian_mountain_council_spirit`.
- `common/decisions/006_independence_wave_decisions.txt`
  - Added Circassian mountain records, pass petitions, council proclamation, and integration mission decisions.
- `common/national_focus/006_independence_wave_focus.txt`
  - Added `independence_wave_circassian_mountain_records` and `independence_wave_circassian_pass_petitions`; current focus count is 81.
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
  - Added the Circassia package label resolver branch.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  - Added list, history, event-detail, selected-title, and selected-body routing for Circassian Mountain Records and Circassian Mountain Council log types.
- `localisation/english/006_independence_wave_l_english.yml`
  - Added player-facing package, idea, focus, decision, mission, tooltip, and effect text.
- `localisation/english/chaosx_gui_l_english.yml`
  - Added event-log type labels.
- `docs/events/006_independence_wave.md`
  - Documented the package, focus-count increase, anchor state, pass-petition states, and event-log coverage.
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
  - Added the implemented `iw_pkg_circassia` package row and carrier note.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
  - Updated Event006 row `7` to refer to the 81-focus tree and include Circassia in the verified starter-proof package list.

## Validation

- Workbook integrity readback:
  - `unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx`: passed.
  - LibreOffice headless conversion to `/tmp/chaosx_catalog_validate_event006_circassia/chaos_redux_events_catalog.xlsx`: passed.
  - Workbook XML scan: `formula_count 23`, no Excel error literals found, no stale 60-focus or 79-focus wording in the workbook.
  - Event006 row `C7`, `G7`, and `O7` read back with the 81-focus tree and Circassia package wording.
- Earlier mechanical checks in this tranche found balanced braces for the touched Event006 script/localisation files, no raw unsupported less-than-or-equal or greater-than-or-equal tokens in touched code/localisation, BOM preserved for edited English localisation files, and 81 focus blocks in `common/national_focus/006_independence_wave_focus.txt`.
- Full Event006 focus localisation coverage check: 81 canonical focus blocks, 0 missing title/description keys.
- New scripted effects depth check: all Circassian scripted effects and event-log emitters begin at root scope.

## Supersession note

- This handoff supersedes the earlier 79-focus catalog evidence in `2026_06_04_090650_event006_catalog_spreadsheet_alignment_handoff.md` and `2026_06_04_091023_parent_event006_catalog_alignment_review.md`.
- Those handoffs remain useful historical alignment notes, but the current Event006 package/tree count is the Circassian-inclusive 81-focus state described here.

## Remaining blockers

- Event006 remains incomplete. Remaining blockers still include future package/formable depth, deeper package overlays, richer scripted-GUI states, final animated/category assets, future catalog rows, and final validation.
- No subagent was spawned for flags because this tranche reused vanilla `KBK` flag assets and did not require new flag artwork.
