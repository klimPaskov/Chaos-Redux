# Event 006 Parent Tranche: Release Gate, Mapuche Log Mapping, Border Expansion

## Scope

Parent patch for urgent Event 006 playability and event-log display fixes.

## Changed Files

- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/chaosx_gui_l_english.yml`

## Behavior Changes

- Host capital reservation now protects the host capital even when the current release candidate has a core there.
- The pre-release safety trigger no longer requires the host to already own a non-candidate-core state. This allows the existing reduced-footprint helper to mask extra candidate cores, release one non-capital anchor state, and preserve the host.
- Border Commission target owner validation now allows a safe transfer from a two-state owner, provided the target is not a capital and not host-survival reserved.
- Mapuche formation and package event-log types now resolve in the evolution list, history detail, event detail, selected title, and selected body grouping.
- Added GUI localisation for the Mapuche Congress Formation and Mapuche Land File event-log type labels.

## Existing Supporting Behavior Confirmed

- Successful releases call `independence_wave_setup_released_country`.
- Released countries receive startup manpower, infantry/support equipment, an unlocked provisional guard template, starting guard divisions, one arms factory, and the shared `independence_wave_liberation_provisional_tree`.
- Reduced-footprint releases set `independence_wave_reduced_territory_start`, file the border survey automatically, restore masked cores, and can use the Border Commission recovery path for further territorial expansion.
- The shared focus tree includes military buildup, army-building decisions, and Border Commission unlocks; no republic-specific stacked focus blocks were added in this tranche.

## Validation

Pending in parent after this handoff:

- Brace balance checks for touched script files.
- Unsupported operator scan for touched Event 006 files.
- Localisation BOM and duplicate key checks for touched localisation.
- `git diff --check`.

## Notes

- No `tmp/hoi4-error-logs/error.log` file was present in the workspace during this tranche; only `tmp/hoi4-error-logs/watchdog.log` was found.
- No commit was made because the worktree already contains many unrelated modified and untracked files from the broader active Event 006/Event 005 work.
