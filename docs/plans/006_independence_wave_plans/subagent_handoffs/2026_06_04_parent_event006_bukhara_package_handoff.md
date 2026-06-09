# Event 006 Bukhara Package Handoff

Date: 2026-06-04
Owner: parent Codex

## Scope

Implemented the Event 006 Bukhara historical-return starter package using vanilla `BUK` data. No flag files, country files, history files, or new visual assets were edited.

## Evidence

- Vanilla tag: `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt` maps `BUK` to `countries/Bukharan Republic.txt`.
- Vanilla country history: `~/projects/Hearts of Iron IV/history/countries/BUK - Bukharan Republic.txt` sets capital `830`.
- Vanilla state cores: state `830` and state `742` both contain `add_core_of = BUK`.

## Changed Files

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Implemented Identifiers

- Package flag: `independence_wave_package_bukhara`
- Package id: `constant:independence_wave_package.bukhara`
- Formation family: `constant:independence_wave_decision.formation_family_oasis_assembly`
- Seed trigger: `can_independence_wave_seed_bukhara_package`
- Package trigger: `is_independence_wave_bukhara_package`
- Formation decisions:
  - `independence_wave_open_bukhara_oasis_council`
  - `independence_wave_register_bukhara_oasis_charter`
  - `independence_wave_proclaim_bukhara_oasis_assembly`
  - `independence_wave_integrate_bukhara_oasis_assembly`
- Focuses:
  - `independence_wave_bukhara_oasis_council`
  - `independence_wave_bukhara_oasis_charter`
- Idea: `independence_wave_bukhara_oasis_council_spirit`
- Event-log types:
  - `bukhara_oasis_formation_type`
  - `bukhara_council_package_type`

## Notes

- The package is chaos tier IV/V only and is gated through the Event 006 candidate path, not Event 005.
- The release anchor is state `830` Bukhara. State `742` Stalinabad is registered as a later claim/proof target by the oasis-charter decision.
- Startup, AI, achievement, focus, decision, scripted localisation, event-log, and documentation surfaces were updated in the same tranche.
- Final visual asset work remains future package polish; existing vanilla flags and existing Event 006 icons are used for this tranche.
