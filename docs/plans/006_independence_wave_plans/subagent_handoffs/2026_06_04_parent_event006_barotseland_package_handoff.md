# Event 006 Barotseland Package Tranche Handoff

Date: 2026-06-04
Owner: parent Codex agent

## Scope

Implemented the narrow `iw_pkg_barotseland` tranche recommended by the package audit sidecar.

The package uses vanilla `BAR` and state `981` only. Vanilla Barotseland country history, leader/portrait data, localisation, and all ideology flag files already exist, so this tranche does not add or edit country tags, country files, history files, or flag assets.

## Gameplay Wiring

- Added high-chaos BAR candidate gating through `can_independence_wave_seed_barotseland_package`.
- Added BAR to the special candidate exclusion path so it only enters the pool through its verified package gate.
- Added state `981` as the package reduced-release anchor.
- Added BAR package classification through `independence_wave_package_barotseland`, `constant:independence_wave_package.barotseland`, and local-polity package tracking.
- Added the Barotse Floodplain Council family constant and event-log type constants.
- Added a startup spirit, restrained local-polity AI participation, package label resolution, and event-log title resolution.
- Added two focus overlay nodes:
  - `independence_wave_barotse_litunga_records`
  - `independence_wave_barotse_floodplain_treaties`
- Added Formation Ledger decisions:
  - `independence_wave_open_barotse_litunga_records`
  - `independence_wave_map_barotse_floodplain_treaties`
  - `independence_wave_proclaim_barotse_floodplain_council`
  - `independence_wave_integrate_barotse_floodplain_council`
- Added integration success/failure effects and actor-linked package/formation event-log writers.

## Files Touched

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

## Validation

- `git diff --check` on touched files: pass.
- Unsupported operator scan for `<=` and `>=`: pass.
- Brace count on touched script files: pass, all deltas zero.
- Localisation BOM check:
  - `localisation/english/006_independence_wave_l_english.yml`: `efbbbf`
  - `localisation/english/chaosx_gui_l_english.yml`: `efbbbf`
- Localisation `:0 "` scan on modified localisation files: pass.
- Focus count after tranche: 66.
- BAR/Barotse reference coverage was checked across constants, triggers, effects, decisions, focus, AI, scripted localisation, event-log localisation, player localisation, and docs.
- Flag/country/history path status check for `gfx/flags`, `common/country_tags`, `common/countries`, `history/countries`, and `history/states`: no changes.

## Remaining Risks

- No bespoke Barotseland package icons were added. The tranche intentionally reuses existing Event 006 local-land, border-survey, focus, and Lukiko-style spirit sprites because no new mandatory art was needed and vanilla flags are already complete.
- This does not complete the full Event 006 country-package backlog. Dahomey and Americas game-rule packages remain separate future tranches.
