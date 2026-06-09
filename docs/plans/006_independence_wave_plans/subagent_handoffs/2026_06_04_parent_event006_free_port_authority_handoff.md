# Event 006 Free Port Authority Tranche Handoff

Date: 2026-06-04

## Scope

Implemented generic Free Port Authority gameplay for non-Danzig Event 006 city/port package releases.

Danzig remains on its bespoke Free City Board route. No country tags, country history, state history, or flag assets were created or changed.

## Gameplay wiring

- Non-Danzig city/port package releases now receive `independence_wave_package_free_port_authority`, `independence_wave_package.free_port_authority`, and `formation_family_free_port_authority`.
- Added gates for harbor control through an owned controlled coastal state with `naval_base > 0`.
- Added Formation Ledger decisions:
  - `independence_wave_open_free_port_manifest`
  - `independence_wave_negotiate_free_port_customs_charter`
  - `independence_wave_proclaim_free_port_authority`
  - `independence_wave_integrate_free_port_authority`
- Added focus `independence_wave_free_port_manifest` at `x = 28`, `y = 8`.
- Added package and formation event-log helpers:
  - `independence_wave_record_free_port_manifest_package_log_entry`
  - `independence_wave_record_free_port_authority_formation_log_entry`

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Validation

- `git diff --check` passed on touched files.
- Unsupported comparison-operator scan passed on touched files.
- Brace counts are balanced on touched script files.
- Localisation BOM check preserved `efbbbf` for both touched English localisation files.
- Localisation `:0` key scan found no matches.
- New free-port event-log constants, scripted localisation branches, and localisation keys are present.
- Focus coordinate check found only `independence_wave_free_port_manifest` at `x = 28`, `y = 8`.
- Flag/country/history scope check showed no changes under `gfx/flags`, `common/country_tags`, `common/countries`, `history/countries`, or `history/states`.

## Remaining risks and follow-up

- The route reuses existing Event 006 free-city board art and decision/focus icon families. Bespoke free-port seals, merchant-council portraits, animated route art, and unique future flag work remain asset follow-up items.
- Non-port city-state, canal authority, oil protectorate, and border-buffer packages remain future work.
- No commit was made because the Event 006 worktree remains broadly dirty and this tranche is not cleanly separable from earlier untracked Event 006 files.
