# Event 014 Terminal Event Details Handoff

## Outcome

Event 014 has two separate public world-end rows in Event Details:

- Scenario ID `6`, `The World Is the Larder`
- Scenario ID `7`, `No Thaw Will Come`

Each row has its own registry identity, source-event mapping, default-enabled persistent toggle, row click, selected detail panel, title, premise, end-state text, status, terminal flag mapping, and super-event ID. Event 014 was not added to any event cluster.

No fallback, collapsed event-level switch, placeholder row, or shared sibling toggle was used.

## Files and identifiers

### Shared parent-owned dependencies preserved and completed

- `common/script_constants/world_end_scenario_registry_constants.txt`
  - Parent-owned untracked registry constants file.
  - Event 014 IDs are `world_end_scenario_id.world_is_the_larder = 6` and `world_end_scenario_id.no_thaw_will_come = 7`.
  - Owner is `world_end_scenario_owner_event.cannibalism = 14`.
  - Matching super-event IDs are `50` and `53`.
- `common/scripted_effects/chaosx_logic_effects.txt`
  - Clears transient Event Details world-end view arrays at event-system initialization.
  - Calls `initialize_world_end_scenario_registry`.
- `common/scripted_effects/chaosx_events_log_effects.txt`
  - Owns the aligned registry, per-scenario default seeding, persistent disabled array, Event Details rebuild arrays, current-state evaluation, row selection, detail selection, toggle behavior, and close/reset behavior.
  - Adds `global.world_end_scenario_registry_public_details_ready_entries` as the reusable public-row opt-in. All unrelated registry identities remain intact with readiness `0`. Only Event 014 IDs `6` and `7` use readiness `1` in this task.
  - Adds per-ID seeding through `global.seeded_world_end_scenarios`. Rebuilding the registry does not clear `global.disabled_world_end_scenarios` and cannot overwrite a prior player choice.
  - Uses `cannibalism_world_end_ordinary` and `cannibalism_world_end_wendigo` as the distinct active-state proofs for Event 014.
  - Sets the source event before a selected-detail toggle rebuild, so toggling from the detached detail panel rebuilds the correct Event 014 rows.
- `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt`
  - `world_end_cannibalism_ordinary_scenario_enabled` reads only scenario ID `6`.
  - `world_end_cannibalism_wendigo_scenario_enabled` reads only scenario ID `7`.
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
  - Routes world-end row open, row toggle, selected-detail close, and selected-detail toggle clicks.
  - Binds `global.events_log_event_detail_world_end_scenario_id_entries` to `events_log_event_detail_world_end_dynamic_list`.
  - Keeps active scenarios locked against later toggle changes.
- `interface/chaosx_events_log_popup.gui`
  - Enlarges the existing Event Details entry to hold a reusable world-end list.
  - Adds `events_log_event_detail_world_end_entry` and `events_log_world_end_scenario_details_window`.
  - Adds row and selected-detail checkbox controls without event-specific layout duplication.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  - Maps registry IDs, owner IDs, row status, selected status, and selected details through the reusable world-end selectors.
- `localisation/english/chaosx_gui_l_english.yml`
  - Adds the Event Details row, toggle, selected-detail, status, and Event 014 scenario prose.
  - `The World Is the Larder` and `No Thaw Will Come` describe their premise and end state without listing effects, variables, thresholds, or hidden route requirements.

### Event 014 terminal gates

- `common/scripted_effects/014_cannibalism_super_event_effects.txt`
  - `cannibalism_try_start_ordinary_world_end` now requires `world_end_cannibalism_ordinary_scenario_enabled = yes` at the terminal effect boundary.
  - Readiness and focus bookkeeping remain outside the toggle, so disabling the branch skips the ending rather than breaking the route's completed state.
- `common/scripted_triggers/014_cannibalism_wendigo_triggers.txt`
  - `cannibalism_wendigo_can_lock_terminal_form` now requires `world_end_cannibalism_wendigo_scenario_enabled = yes`.
  - Countdown progress can remain at its completed state and be reconsidered on a later pulse if the row is re-enabled.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_terminal_event_details_2026-07-12.md`
  - This handoff.

## Persistence and independence proof

The registry seeds each scenario ID once by recording it in `global.seeded_world_end_scenarios`. Both Event 014 entries are default enabled, so neither ID is inserted into `global.disabled_world_end_scenarios` during first seeding.

Toggling a row adds or removes only `events_log_selected_world_end_scenario_id`. ID `6` and ID `7` therefore cannot change one another, the parent Event 014 enable state, or any evolution state. Registry and view rebuilds read the persistent disabled array but never clear it.

The `public_details_ready` field is the reusable later-event contract. A branch may be classified `public` in the stable registry without appearing in Event Details until its row, toggle, selectors, player-facing prose, and terminal gate are all complete. A later event pass must set its own registry entry to readiness `1` only after finishing those surfaces.

## Click and selection proof

The Event Details rebuild creates eleven aligned view arrays, including scenario ID, owner, enabled, active, available, scenario flag, super-event ID, title key, details key, and availability helper. The GUI list uses the scenario ID array and the shared row index.

- Row body click calls `events_log_open_selected_world_end_scenario_detail`.
- Row checkbox clicks call `events_log_select_world_end_scenario_from_row`, then `events_log_toggle_selected_world_end_scenario_disabled`.
- The selected detail panel stores ID, owner, flag identity, super-event ID, title key, details key, and availability helper before opening.
- The selected detail panel checkbox uses the same toggle helper and explicitly restores the owner event ID before rebuilding its rows.
- Closing Event Details or the parent Event Log clears selected transient detail state without clearing persistent toggle state.

## Terminal and Chaos gate proof

The new toggle checks are conjunctions at the existing terminal boundaries. They do not replace or weaken any terminal rule.

Ordinary route:

- `cannibalism_try_start_ordinary_world_end` reads only scenario ID `6`.
- It still calls `cannibalism_can_complete_ordinary_world_end`.
- That trigger still requires no active `world_end`, no `world_end_disabled`, `global.chaos_meter_value` strictly greater than `constant:cannibalism_evolution_threshold.world_end_chaos`, and the existing unified-host world-state thresholds.
- `constant:cannibalism_evolution_threshold.world_end_chaos` remains `1000`.
- The terminal effect still sets `world_end`, `world_end_cannibalism`, and `cannibalism_world_end_ordinary`, then emits super-event ID `50`.

Wendigo route:

- `cannibalism_wendigo_can_lock_terminal_form` reads only scenario ID `7`.
- It still calls `cannibalism_wendigo_can_start_countdown` and retains the completed-progress and route checks.
- The countdown trigger still requires no active `world_end`, no `world_end_disabled`, and Chaos strictly greater than the same `1000` threshold, plus the existing Wendigo world-state checks.
- The terminal lock still sets `world_end`, `world_end_cannibalism_wendigo`, and `cannibalism_world_end_wendigo`, then emits super-event ID `53`.

Disabling one branch therefore removes only that branch. It does not disable Event 014, its sibling ending, world-end selection globally, or any existing world-state condition.

## Secrecy proof

Both Event 014 registry entries remain classified `public`, but the Event Details rebuild excludes IDs `6` and `7` until `cannibalism_reveal_complete` exists. Before the reveal:

- neither scenario row is added to the dynamic list
- the Event 014 world-end header is hidden because the list is empty
- the Event 014 empty-state line is also hidden
- no click can populate the selected scenario detail panel
- no Hannibal Lecter or Wendigo identity can be resolved on a visible Event Details surface

After the reveal, the two rows appear independently and their distinct public titles and details become selectable.

## Validation

- Registry alignment: all nine registered identities populate the same eleven registry fields. Event 014 IDs `6` and `7` each have owner `14`, public visibility, readiness `1`, default-enabled state, distinct sort values, distinct super-event IDs, and separate title/detail identities.
- View alignment: the rebuild clears and appends the same eleven Event Details world-end arrays.
- Constant resolution: every `constant:world_end_scenario_id.*` reference in the registry effects, shared toggle triggers, and scripted-localisation selectors resolves to one of the nine keys in the parent-owned constants file.
- Control routing: row open, row toggles, detail close, and detail toggles have matching scripted-GUI and interface element names.
- Localisation: the English GUI localisation file retains its UTF-8 BOM and contains no duplicate keys.
- Structural review: all touched Clausewitz/scripted-GUI/interface files have balanced braces, and the scoped diff has no whitespace errors.

## Remaining risks and parent integration notes

- `common/script_constants/world_end_scenario_registry_constants.txt` and `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt` are concurrent untracked shared dependencies. They must be staged with this closure.
- `common/scripted_effects/chaosx_logic_effects.txt`, the shared Event Details effects/GUI/localisation/layout files, and several unrelated scenario gate additions were written concurrently in the shared worktree. This handoff reviewed and preserved that baseline. The parent must keep those files together during final ownership and staging review.
- Unrelated registry identities deliberately remain `public_details_ready = 0`. Their stable IDs and metadata are preserved, but their public rows are not part of this Event 014 completion.
- No runtime game session was launched in this subagent pass. The implementation was validated through the concrete data paths and file-level integration checks listed above.
