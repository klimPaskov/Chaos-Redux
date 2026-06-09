# Event006 Audit Follow-Up Runtime Cleanup

Date: 2026-06-05
Owner: parent agent
Scope: Event006 Independence Wave runtime cleanup after the 17:00 completion audit.

## Changes

- Removed stale Kuban/Altai package AI gates from `common/ai_strategy/006_independence_wave.txt`.
- Removed stale Kuban/Altai national spirits from `common/ideas/006_independence_wave_ideas.txt`.
- Replaced the resolver temp-variable truce duration in `events/006_independence_wave.txt` with file-scoped `@INDEPENDENCE_WAVE_RELEASE_TRUCE_DAYS = 180`, because vanilla documentation only shows literal `set_truce days` usage and no local precedent proved variable support for that field.
- Removed the now-unused `independence_wave_resolver.release_truce_days` script constant so there is only one tuning source for the release truce.
- Kept `KUB` and `ALT` only as explicit candidate exclusions in `common/scripted_triggers/006_independence_wave_triggers.txt`.

## Validation

- Brace balance passed for:
  - `events/006_independence_wave.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/ai_strategy/006_independence_wave.txt`
  - `common/ideas/006_independence_wave_ideas.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `localisation/english/006_independence_wave_l_english.yml`
- `git diff --check` passed for the touched runtime files.
- KUB/ALT scan over active Event006 gameplay/localisation surfaces now reports only the intended scripted-trigger exclusions.

## Remaining Risks

- No in-game validation was run.
- The Event006 catalog spreadsheet was aligned in the same parent follow-up for the 50-focus shared tree and the KUB/ALT correction.
- Event005-side origin separation received a focused static audit in `2026_06_05_parent_event006_event005_origin_separation_audit.md`.
- A final full Event006 completion audit is still required before a source-pack completion claim.
