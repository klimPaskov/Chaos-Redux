# Parent Handoff: Event 006 Playable Wrap-Up Urgent Fixes

## Scope

This parent pass focused on urgent runtime blockers for the Event 006 Independence Wave playable wrap-up. It did not attempt full polish, full package deletion, new flag production, scripted GUI interactivity, or a complete final-completion claim.

## Files changed

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Runtime changes

- Event 006 candidate eligibility now excludes `KUB` and `ALT` at the shared `can_independence_wave_use_candidate_tag` gate.
  - This prevents Kuban and Altai from being selected by the Independence Wave ordinary/special candidate passes.
  - Existing stale KUB/ALT decision, focus, localisation, and constant surfaces were not removed in this pass, because deleting those surfaces broadly is a larger cleanup and not required to stop the tags releasing.
- Event 005 Soviet Collapse setup and event-created focus-tree loading now skip countries with `chaosx_release_origin_independence_wave`.
  - `soviet_collapse_setup_breakaway_country` no longer applies Event005 breakaway setup to Event006-origin countries.
  - `soviet_collapse_load_event_created_focus_tree` no longer loads Event005 republic/breakaway focus trees onto Event006-origin countries.

## Evolution log status

- Event 006 still records actual evolution logs through one call site in `events/006_independence_wave.txt`.
- The only real evolution logger is `independence_wave_record_tier_evolution_log_entry`.
- Validation found exactly four `record_events_log_evolution_entry = yes` calls in that helper:
  - Gathering Storm release pattern
  - Rising Cascade release pattern
  - Old Names release pattern
  - Impossible Statehood release pattern
- Calm World is not logged as an Event006 evolution stage.

## Validation

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_localisation/chaosx_scripted_localisation_events_log.txt localisation/english/chaosx_gui_l_english.yml`
- Brace-balance check over the same gameplay/localisation files:
  - `events/006_independence_wave.txt`: balance `0`
  - `common/scripted_effects/006_independence_wave_effects.txt`: balance `0`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`: balance `0`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: balance `0`
  - `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: balance `0`
  - `localisation/english/chaosx_gui_l_english.yml`: balance `0`, UTF-8 BOM present
- Unsupported comparison-operator search over the same script/localisation files returned no matches.
- `rg -n "record_events_log_evolution_entry|independence_wave_record_tier_evolution_log_entry"` confirmed only four Event006 evolution log writes and one Event006 event call site.
- `tmp/hoi4-error-logs/` currently contains only `watchdog.log`; no current `error.log` was present during this pass.

## Remaining risks

- Event006 still has stale KUB/ALT focus, decision, localisation, constants, and record-helper surfaces. They are blocked from new wave selection by the shared candidate gate but should be removed or marked superseded in a later cleanup if the user wants zero KUB/ALT content remaining.
- The Event006 scripted GUI remains display-oriented, not fully interactive.
- Decision tooltip cleanup has had targeted passes, but no full final decision audit was rerun after this patch.
- The worktree contains many unrelated uncommitted changes, including existing Event005/Event006 work. No commit was made from this dirty state.
