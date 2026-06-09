# Event 006 Kurdistan Mountain Package Tranche Handoff

Status: implemented as a bounded country-package depth tranche. Event 006 remains incomplete overall; the completion audit in `2026_06_01_event006_completion_audit_remaining_gaps_after_rump.md` still blocks any final completion claim.

## Implemented

- Added KUR package identity constants, event-log types, tuning values, and a mountain-assembly formable family.
- Added KUR reduced-release anchor preference for Kurdish mountain districts before the generic anchor search.
- Added `independence_wave_package_kurdistan`, setup variables, and the `independence_wave_kurdish_mountain_assembly_spirit`.
- Added KUR package triggers for mountain control, registry opening, pass-district mapping, proclamation, and integration failure.
- Added two shared-tree focus hooks:
  - `independence_wave_kurdish_mountain_registry`
  - `independence_wave_kurdish_pass_districts`
- Added Formation Ledger decisions and post-formation mission:
  - `independence_wave_open_kurdish_mountain_registry`
  - `independence_wave_map_kurdish_pass_districts`
  - `independence_wave_proclaim_kurdish_mountain_assembly`
  - `independence_wave_integrate_kurdish_mountain_assembly`
- Added event-log labels for the Kurdish Mountain Registry package milestone and Kurdish Mountain Assembly formation milestone.
- Updated Event 006 implementation docs and the country-package spec matrix.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Assets and Flags

- No country flag artwork was created or edited.
- No new sprite asset was required. The package reuses the existing local land council and border commission decision/focus icon families and a current Event 006 idea picture.

## Validation

- Brace balance returned `balance=0` and `min=0` for all touched script, localisation, and docs files.
- No `<=` or `>=` tokens found in touched Event 006 surfaces.
- `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml` both retain UTF-8 BOM.
- No `:0` localisation keys found in the touched localisation files.
- `git diff --check` passed for the touched files.
- New KUR focus/decision/event-log localisation keys were present.

## Remaining Risk

- This did not close the full Event 006 country-package requirement. The completion audit still lists package depth, scripted GUI/value-display surfaces, report/news assets, strange/Evo V package depth, catalog alignment, and final audits as blockers.
- The package uses existing vanilla KUR tag/cores and existing Event 006 art. If final package presentation art or country flag/cosmetic work is required later, route it through an asset subagent before gameplay wiring.
