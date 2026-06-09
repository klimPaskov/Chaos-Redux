# Event 006 Playable Wrap-Up Handoff

## Scope

Parent wrap-up pass for the urgent Event 006 Independence Wave functionality issues reported on 2026-06-05.

The pass focused on technical playability:

- the entry event must be able to release countries when fired;
- the event-log UI must show Independence Wave entries correctly;
- evolution entries must be release-scale stages, not per-release progression spam;
- documentation cleanup had to cover all Event 006 docs, not only the immediate KUB/ALT correction context.

## Parent Changes

### Candidate resolver

File: `events/006_independence_wave.txt`

- Removed the small random candidate scan cap from the four `every_possible_country` candidate-pool passes.
- The event now builds a full eligible possible-country pool and iterates it until `global.independence_wave_actual_release_count` reaches `global.independence_wave_release_count_target`.
- This addresses the failure mode where firing `chaosx.nr6.1` could sample only unsuitable tags and release nobody even though valid republics existed elsewhere.

File: `common/script_constants/006_independence_wave_constants.txt`

- Removed the unused candidate scan-cap constant from the Independence Wave tuning constants.

### Evolution logs

Files:

- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/chaosx_gui_l_english.yml`

Current runtime behavior:

- `events/006_independence_wave.txt` calls `independence_wave_record_tier_evolution_log_entry = yes` only after `global.independence_wave_actual_release_count > 0`.
- `common/scripted_effects/006_independence_wave_effects.txt` contains exactly four `record_events_log_evolution_entry = yes` calls for Independence Wave, all inside `independence_wave_record_tier_evolution_log_entry`.
- Release dossier, package, and formation helpers still prepare log variables/event targets, but they do not call `record_events_log_evolution_entry`.

The four actual evolution stages are now displayed consistently in the main evolution list, selected evolution view, selected history detail view, and event-detail evolution list:

1. Gathering Storm Release Pattern: four to six releases instead of the calm baseline of three to five.
2. Rising Cascade Release Pattern: five to nine releases, covering Rising Chaos and Chaos Tier pressure.
3. Old Names Release Pattern: eight to twelve releases at Totalen Chaos, with historical/local-polity package pressure.
4. Impossible Statehood Release Pattern: ten to sixteen releases at World Collapse, with strange package pressure.

No Calm World evolution entry is recorded.

### Decision tooltip tranche

Files:

- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`

Added custom trigger/effect tooltip coverage to the most visible early-aftershock, congress, compact, and major-patron decisions. This was a targeted pass, not a full decision UX completion audit.

## Documentation Subagent

Spawned `chaosx_documentation_curator` with docs-only scope and `fork_context=false`.

Handoff:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_160045_documentation_curator_wrapup_cleanup.md`

The curator cleaned broad Event 006 documentation, corrected stale KUB/ALT active-scope claims, removed stale report/news asset blockers, and aligned docs with release-scale evolution stages.

## Validation

Completed checks:

- Required offline Paradox wiki pages and vanilla docs were consulted before script/doc edits.
- `git diff --check` passed for the touched Event 006 script, localisation, and current docs paths.
- Brace-balance check passed for:
  - `events/006_independence_wave.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  - `common/decisions/006_independence_wave_decisions.txt`
  - `localisation/english/006_independence_wave_l_english.yml`
  - `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml` still has UTF-8 BOM.
- Independence Wave actual evolution-entry call count is four.
- `tmp/hoi4-error-logs/` currently contains `watchdog.log` only; no `error.log` was present during this wrap-up validation.

## Remaining Non-Blocking Gaps

These are not resolved in this wrap-up pass:

- Full decision tooltip/effect-feedback coverage is still incomplete for lower-priority package/formable decisions.
- Several country packages and focus paths remain broader-content polish rather than technical playability blockers.
- No in-game runtime confirmation was performed by the parent; validation was static/script-level.
- No commit was created because the worktree contains extensive unrelated and pre-existing dirty/untracked changes across Event 005, Event 006, docs, assets, and generated files.
