# Event 006 GHA Gold Coast Legislative Council Tranche Handoff

## Summary

Implemented the GHA / Ghana / Gold Coast Legislative Council starter package as a verified Event 006 local-polity package. The package reuses vanilla GHA tag, Ghana state `274`, vanilla country history, localisation, characters, portraits, and flag assets. No flag, country history, state history, or country tag files were changed.

## Gameplay Wiring

- Added GHA candidate gating through `can_independence_wave_seed_ghana_package`.
- Added reduced-release anchor preference for Ghana state `274`.
- Added GHA to the verified package candidate pool.
- Added package identity assignment for `independence_wave_package_ghana`, local-polity package type, package id `constant:independence_wave_package.ghana`, and formable family `constant:independence_wave_decision.formation_family_ghana_legislative_council`.
- Added Gold Coast records and petition proof triggers, decisions, focus nodes, idea, proclamation effect, integration mission, discredit path, AI strategy coverage, and event-log milestone rows.
- Updated Event 006 docs, package spec, and catalog workbook to include the GHA package and 99-focus tree count.

## Files Changed

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Validation

- Required offline Paradox wiki and vanilla documentation were consulted before the tranche.
- Vanilla references checked:
  - `common/country_tags/00_countries.txt`: `GHA = "countries/Ghana.txt"`
  - `history/countries/GHA - Ghana.txt`: capital `274`, vanilla GHA characters
  - `history/states/274-British Africa.txt`: owner `ENG`, `add_core_of = GHA`
  - vanilla GHA localisation and ideology flag assets
- Brace balance check across touched script files: all balances `0`, minimum depth `0`.
- Unsupported operator check for `<=` and `>=`: no matches in touched gameplay script.
- Focus count check: `99` focus blocks, `99` completion rewards, `99` AI blocks.
- Localisation checks:
  - `006_independence_wave_l_english.yml` keeps UTF-8 BOM, has no `:0`, and no duplicate keys.
  - `chaosx_gui_l_english.yml` keeps UTF-8 BOM, has no `:0`, and no duplicate keys.
- Workbook checks:
  - `unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx`: passed.
  - LibreOffice headless convert check: passed.
- Scope check:
  - No `flags`, `gfx/flags`, `.tga`, `history/countries`, `history/states`, or `common/country_tags` files were touched.

## Subagent Audit

Read-only country-package audit subagent `019e928c-05bc-7142-874a-68f6ebf6e306` returned PASS with no concrete GHA defects.

The subagent confirmed:

- GHA seed gate requirements are present.
- Reduced-release anchor prefers state `274`.
- Startup package identity and spirit are wired.
- Decisions, integration mission, event-log rows, docs, and catalog include GHA.
- No flag/history/state files were touched.

## Simplifications, Omissions, and Blockers

- No simplifications were used for the GHA tranche.
- No new flags were created because vanilla GHA flag assets already exist and are reused.
- No in-game parser or live game validation was run.
- The broader Event 006 goal remains incomplete; this is one completed country-package tranche.
- Several Event 006 files are still untracked in the current worktree, so this handoff describes the current workspace state rather than a committed baseline.
