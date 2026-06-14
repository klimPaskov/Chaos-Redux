# Event 009 White Peace Scripted-System Handoff

## Files Changed

- `common/script_constants/009_white_peace_constants.txt`
- `common/scripted_triggers/009_white_peace_triggers.txt`
- `common/scripted_effects/009_white_peace_effects.txt`
- `docs/plans/009_white_peace_plans/subagent_handoffs/scripted_system_architect.md`

Parent integration note: this handoff began as the scripted-system architect's draft and was reviewed, corrected, and extended by the parent implementation. The helper names below describe the final parent-owned Event 009 helper surface after integration.

## Helper Contracts

- `prepare_white_peace_runtime_context`: global/root effect. Resets Event 009 runtime variables, counts on-demand war pressure, determines stage, calculates dynamic cap, selects branch, and saves regular event targets `white_peace_primary` and `white_peace_partner` when a safe pair exists. Outputs `global.white_peace_*` count/cap/status variables, `global.white_peace_selected_stage`, `global.white_peace_selected_branch`, `global.white_peace_selected_pair_cap`, and `event_cluster_actor`.
- `calculate_white_peace_dynamic_cap`: global/root effect. Rebuilds Event 009 availability and weight pressure from current active wars, safe minor pairs, minor-only pressure, major candidates, and stage state. Writes `global.white_peace_environment_cap`, `global.white_peace_effective_cap`, and `global.white_peace_effective_dynamic_cap`. The environment cap is clamped to `constant:white_peace_weight.max_environment_cap` (`1500`).
- `can_country_be_white_peace_target`: country trigger. Excludes non-existing/no-war countries, capitulated countries, civil-war participants, subjects, faction leaders, special chaos/nonhuman actors, protected actors, and recent settlement memory.
- `can_pair_receive_white_peace`: country trigger with PREV as the proposed paired country. Requires an active war between both countries, both country gates, no same-tag relation, no faction relation, safe capital control, and major involvement only at stage II/III.
- `score_white_peace_pair`: country effect with PREV as paired country. Writes temp `white_peace_pair_score`; favors minor/minor, no-major-war, independent, non-faction, capital-safe pairs.
- `select_weighted_white_peace_primary_candidate` / `select_weighted_white_peace_partner_for_current_primary`: scoped-pool selection helpers. They add country scopes to temporary arrays in proportion to `white_peace_pair_score`, then use `random_scope_in_array` so pair selection is weighted after vetoes rather than pure random.
- `apply_white_peace_pair`: country effect scoped to `white_peace_primary`, using event target `white_peace_partner`. Captures long-war state before the peace effect, runs `white_peace = { tag = event_target:white_peace_partner message = white_peace_status_quo_settlement }`, adds the custom opinion modifier on both sides, marks memory, increments settlement counters, queues delayed no-winner tracking on the partner with the primary preserved as `FROM`, and contributes to pending capped Chaos reduction.
- `mark_recent_white_peace_pair`: country effect scoped to `white_peace_primary`, using event target `white_peace_partner`. Sets timed country memory and exact reciprocal `recent_white_peace_pair_<tag>` memory on both participants. Uses file-local duration mirrors because timed flag `days =` fields are safer with `@` literals.
- `apply_white_peace_current_context`: executes the saved branch from the one-option report event, suppresses the normal per-country on-peace Chaos change during Event 009 settlements, applies one or several safe pairs within the branch cap, then applies the branch-level capped Chaos reduction and records the reached evolution milestone.
- `fire_white_peace_report_event`: opens the correct visible one-option report variant from the saved global branch context before the settlement effect runs.
- Event history entries use the shared `on_repeatable_event_fired` -> `record_events_log_history_entry` path. `events_log_set_default_actor_for_current_event` maps Event 009 history rows to `white_peace_primary`.
- `record_white_peace_evolution_if_needed`: global/root effect. Sets shared event-log evolution variables for Event 009 and records stage I/II/III once when `is_current_evolution_enabled = yes`.

## Constants And Tuning

- Added `white_peace_event_log`, `white_peace_weight`, `white_peace_stage_multiplier`, `white_peace_stage_pressure`, `white_peace_branch`, `white_peace_branch_weight`, `white_peace_settlement_cap`, `white_peace_memory`, `white_peace_pair_score`, `white_peace_chaos_delta`, and `white_peace_skip_reason`.
- Dynamic cap follows the spec model: active war pressure, safe minor pair pressure, minor-only pressure, clutter bonuses, repeatable cap ratio, stage multiplier, optional recent broad penalty, and a hard environment cap of `1500`.
- Timed memory constants are duplicated as file-local `@WHITE_PEACE_*_DAYS` values in the effects file for timed flag compatibility.
- Random-list branch weight keys are mirrored as file-local `@WHITE_PEACE_BRANCH_*` values because random-list labels need load-time literals; their source tuning table remains `white_peace_branch_weight`.

## Event Targets And Cleanup

- Uses regular event targets only: `white_peace_primary` and `white_peace_partner`.
- No global event targets were added, so no manual target cleanup is required.
- Persistent cleanup is handled by timed flags:
  - `recent_white_peace_country`
  - `recent_white_peace_pair_<tag>` on both participants
  - `recent_major_white_peace_country`
  - `recent_broad_white_peace`

## Assumptions

- Candidate scanning is on-demand and intended for the picker, Event Details, cluster detail, or manual test firing paths. No daily/weekly/monthly all-country loop was added.
- Unique war counting is approximated by active-war country and pair pressure because this helper layer has no safe unique-war iterator. The counts are still enough to gate no-war/no-safe-pair and keep the cap dynamic.
- The parent will wire call sites in `events/009_white_peace.txt` and shared picker/cluster/detail files. Those files were intentionally not edited.

## Validation

- Verified helper identifiers requested by the parent exist in the scoped helper files.
- Checked the effects/triggers against vanilla docs for `white_peace`, event targets, timed country flags, `has_war_with`, `has_capitulated`, and script constants.
- Verified no new daily/weekly/on-action polling was added.

## Remaining Risks And Follow-Up

- Peace cluster/event-list availability reads `global.white_peace_skip_reason`, which is refreshed during Event 009 candidate checks and cluster display refreshes.
