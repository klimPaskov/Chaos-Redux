# Event 006 Protected Mandate Tranche Handoff

Date: 2026-06-04

## Scope

Implemented generic Protected Mandate gameplay for Event 006 protectorate-package releases.

No country tags, country history, state history, or flag assets were created or changed.

## Gameplay wiring

- Protectorate-package releases now receive `independence_wave_package_protectorate_mandate`, `independence_wave_package.protectorate_mandate`, and `formation_family_protected_mandate`.
- Added `independence_wave_protectorate_mandate_spirit`, reusing the existing patron-cabinet idea art.
- Added triggers for treaty audit, guarantee review, protected mandate proclamation, and integration failure when the mandate becomes a subject or patron leverage reaches the dangerous threshold.
- Added Formation Ledger decisions:
  - `independence_wave_audit_protectorate_treaties`
  - `independence_wave_review_protectorate_guarantees`
  - `independence_wave_proclaim_protected_mandate`
  - `independence_wave_integrate_protected_mandate`
- Added focus `independence_wave_protectorate_treaty_audit` at `x = 28`, `y = 9`.
- Added protectorate AI strategy `independence_wave_protectorate_mandate_restraint`.
- Added package and formation event-log helpers:
  - `independence_wave_record_protectorate_treaty_package_log_entry`
  - `independence_wave_record_protected_mandate_formation_log_entry`

## Files changed

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

- `git diff --check` passed on touched files.
- Unsupported comparison-operator scan passed on touched files.
- Brace counts are balanced on touched script files.
- Localisation BOM check preserved `efbbbf` for both touched English localisation files.
- Localisation key format scan found no old-style numeric markers.
- New protected-mandate event-log constants, scripted localisation branches, and localisation keys are present.
- Focus coordinate check found only `independence_wave_protectorate_treaty_audit` at `x = 28`, `y = 9`.
- Flag/country/history scope check showed no changes under `gfx/flags`, `common/country_tags`, `common/countries`, `history/countries`, or `history/states`.

## Remaining risks and follow-up

- The route reuses existing Event 006 sponsored-cabinet art and idea icon family. Bespoke protectorate seals, treaty-broker portraits, animated route art, and unique future flag work remain asset follow-up items.
- Canal authority, oil protectorate, border-buffer, and non-port city-state variants remain future package work.
- No commit was made because the Event 006 worktree remains broadly dirty and this tranche is not cleanly separable from earlier untracked Event 006 files.
