# Event log, evolution, and cluster wiring

### Evolution implementation

The implementation must preserve the design split between baseline stages and evolutions.

Baseline progression can use whatever state, flags, variables, decisions, or events the mechanic needs. Do not record every normal stage as an evolution unless the spec deliberately treats it as an evolution track.

For actual evolutions, the usual pattern is:

1. the evolution condition becomes available from the current campaign state
2. the evolved incident, track, or milestone fires through MTTH-based dynamic pacing rather than instantly, and it can take a good amount of time: the base should be around 90 days, but it can be more or less depending on the evolution. Some happen instantly, for example for events that haven't fired yet, which makes the initial firing more intense
3. set the shared evolution context variables
4. record the evolution log entry through the shared pipeline
5. unlock or adjust the new behavior, tag, decision set, focus branch, or rare variant
6. do not change Chaos for the evolution state itself. Any Chaos change must come from a separate concrete consequence

Event evolutions that gate content must respect the enable and disable UI. If an evolution is disabled, the gated path must have a clean alternate route or must be safely skipped. Do not leave required baseline progression locked behind a disabled evolution.

The shared context is:

- `events_log_evolution_event_id`
- `events_log_evolution_type`
- `events_log_evolution_stage`
- `events_log_evolution_tier`
- `events_log_evolution_actor` when the milestone belongs to a specific country

Then:

- gate the milestone with `is_current_evolution_enabled = yes`
- call `record_events_log_evolution_entry = yes`
- If a helper sets a `*_recorded` flag or unlocks follow-up content, set the shared evolution context before its `limit` and include `is_current_evolution_enabled = yes` in that same limit. Disabled evolutions must not set recorded flags that later stages, decisions, reports, or focus branches read.
- When a logged evolution has an actor, save the country as `events_log_evolution_actor` and set `events_log_evolution_has_actor = 1` immediately before `record_events_log_evolution_entry = yes`. Regular event targets cannot be manually cleared and can leak through an effect chain, so no-actor records must rely on the shared logger's default `events_log_evolution_has_actor = 0` behavior instead of raw `has_event_target`.

Implementation design rules:

- `event_id` ties the evolution to the parent event.
- `type` separates parallel mutation tracks inside the same event.
- `stage` is the milestone inside one mutation track, not the ordinary event stage.
- `tier` is display-oriented. Do not use it as a substitute for real logic state.
- When a track uses stage-specific incidents, wire the stage-specific display text across every event-log view that can show it: list/current view, history/detail view, event-detail view, selected-detail title, selected-detail body, and any stage-number or roman-numeral helpers needed by the highest stage.
- Use dynamic factor models for evolution chance, pacing, intensity, and aftermath.
- If an evolution creates a persistent country, make the country playable or meaningful enough for its expected lifetime.

### Event-log UI surfaces

Before changing evolution log display, identify the exact surface and keep the change scoped to that surface. Patch the actual GUI/localisation/scripted data path. Do not record a process note as a substitute for fixing the visible row.

- **Main Evolutions tab** uses `global.events_log_evolution_view_*`, `events_log_evolution_index`, and `events_log_evolution_entry_*` templates. This is a global logged-evolution history surface. Rows should visibly show the log index, date, source event, evolution name, tier, and stage.
- **History details related evolutions** uses `global.events_log_history_detail_evolution_*`, `events_log_history_detail_evolution_index`, and `events_log_history_detail_evolution_entry`. This is the selected-event filtered logged-evolution history surface. Rows should use the same visible metadata as the main Evolutions tab.
- **Event details evolution catalog** uses `global.events_log_event_detail_evolution_*`, `events_log_event_detail_evolution_index`, and `events_log_event_detail_evolution_entry`. This is a catalog/preview surface, not a history log. Do not add fake log indexes, fake dates, or history-only metadata here.

When adding evolution row metadata, reuse the arrays for that row surface: main rows read the `global.events_log_evolution_view_*` arrays rebuilt by `rebuild_events_log_evolution_view`, while selected-history rows read the `global.events_log_history_detail_evolution_*` arrays rebuilt by `events_log_rebuild_history_details_view`. The required row metadata is sequence, date, source event, type/name, tier, stage, actor, and enabled state. If the user reports row alignment, patch `interface/chaosx_events_log_popup.gui` row sizes, button bounds, and text widths for the affected surface in the same change.

Event-log defaults must keep unreworked events disabled by default. An event that is still waiting for a rework should stay out of the reworked-event default enable allowlist so startup seeds it into `global.disabled_events` and it appears unchecked. When an event is reworked and ready for normal selection and log use, add its ID back to that allowlist in the same change as the event registration and log wiring.

### 5. Event log integration

Events must appear in Chaos Redux’s event log, so wire the full log contract in the same change.

Script ownership:

- Put history/evolution recording, actor sanitizing, default actor mapping, Event Details catalog rows, event-detail evolution previews, and History/Evolutions/Events tab rebuild logic in `common/scripted_effects/chaosx_events_log_effects.txt`.
- Keep random selection, fired-event handlers, timers, and event type accounting in `common/scripted_effects/chaosx_logic_effects.txt`. Those effects should call the shared Event Logs recorders rather than defining log arrays themselves.
- Keep settings controls and generic event firing helpers in `common/scripted_effects/chaosx_settings_effects.txt`. Do not add new event-log history/evolution display logic there unless the settings window itself is changing.
- Keep button click routing in `common/scripted_guis/chaosx_scripted_gui_events_log.txt`, and layout changes in `interface/chaosx_events_log_popup.gui`.

Required name plumbing:

- add or update visible event-name loc in `localisation/english/chaosx_event_names_l_english.yml`
- update event-name selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- update debug-name selectors in `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`

Required actor plumbing when a flag should appear:

- update `events_log_set_default_actor_for_current_event` in `common/scripted_effects/chaosx_events_log_effects.txt`
- use a default actor only when the event should show a meaningful actor before or without a fired history row
- if fired history should override the default actor, keep the history-context flow intact
- for random-event history rows, remember that the generic fired-event handler records the row before the target event's `immediate` block runs. If the actor is created or refreshed inside that event, move that preparation into a shared pre-fire helper and call it before `record_events_log_history_entry`
- for evolution rows with actors and no-actor entries, follow the `events_log_evolution_actor` and `events_log_evolution_has_actor` rule under [Evolution implementation](#evolution-implementation)

Required detail-view plumbing:

- update the event-details text selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- update the actual user-facing text in `localisation/english/chaosx_gui_l_english.yml`
- if new generic event-log behavior is needed, wire it through:
  - `common/scripted_effects/chaosx_events_log_effects.txt`
  - `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
  - `interface/chaosx_events_log_popup.gui`

Do not hardcode one-off GUI behavior if it should be reusable by later events.

Public world-end rows are part of the shared Event Details data path. In `common/scripted_effects/chaosx_events_log_effects.txt`, register them through `initialize_world_end_scenario_registry`, rebuild them with `events_log_rebuild_event_detail_world_end_scenarios`, persist disabled scenario IDs in `global.disabled_world_end_scenarios`, and toggle the selected row through `events_log_toggle_selected_world_end_scenario_disabled`. Keep automatic branch gates in `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt`. Route row, selection, and detail clicks through `common/scripted_guis/chaosx_scripted_gui_events_log.txt`. Keep titles, details, and status selectors in the existing Event Details scripted-localisation and GUI-localisation files. Change `interface/chaosx_events_log_popup.gui` only when the shared row or detail layout itself needs a reusable control.

When it's impossible for an event to fire due to conditions (the actor country doesn't exist, prerequisite not fulfilled, etc), always show `N/A` in the event list in place of a `0` for the weight.

### 6. Event cluster integration

Event clusters are a catalogue layer above normal random events. The Clusters tab must show every registered cluster, while History shows only clusters that actually fired.

Core files:

- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt` when event-log view state changes
- `common/scripted_effects/chaosx_settings_effects.txt` when settings controls or generic event firing helpers change
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt` when cluster log UI behavior changes
- `interface/chaosx_events_log_popup.gui` when cluster list/details layout changes
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`

To add a new cluster:

1. Add an ID in `event_cluster_id`.
2. Add any cluster-specific tuning group, for example `event_cluster_<slug> = { unlock_tier cooldown_days }`.
3. Register the cluster in `initialize_event_cluster_definitions` by pushing aligned entries into `global.event_clusters`, `global.event_cluster_type_entries`, and `global.event_cluster_unlock_tier_entries`.
4. Map member events in `event_belongs_to_cluster`, from normal event ID to cluster ID.
5. Add ordered member rows in `load_event_cluster_members`.
6. Add or update cluster name/type/description scripted localisation and GUI localisation.
7. If it needs custom runtime setup, add that branch to `event_cluster_prepare_runtime_context`.
8. If it needs a custom cooldown or one-time state, update `mark_event_cluster_fired_state` and any availability logic in `can_event_cluster_fire`.

Member attributes are parallel arrays in `load_event_cluster_members`:

- `temp_event_cluster_member_event_id_entries`: normal event ID.
- `temp_event_cluster_member_role_entries`: `event_cluster_member_role.required` or `event_cluster_member_role.optional`.
- `temp_event_cluster_member_chance_entries`: participation chance for optional members, usually from `event_cluster_member_participation`.
- `temp_event_cluster_member_min_tier_entries`: minimum chaos tier for that member.
- `temp_event_cluster_member_danger_entries`: display severity in cluster details.

To change a member's behavior, edit those attributes together. Do not reorder one array without the others.

Member severity uses four values:

- Low
- Medium
- High
- Severe

Cluster firing rules:

- Automatic cluster firing happens from `try_fire_event_cluster_for_selected_event` after a member event is selected.
- Automatic firing respects cluster unlock tier, cooldown, one-time state, member eligibility, optional participation rolls, and runtime context.
- Manual firing from Settings uses `force_fire_event_cluster_by_temp_id`. It bypasses tier, cooldown, disabled-state, and member availability checks. Runtime context can still fail if the event cannot build the required scopes.
- Cluster history rows are recorded by `record_events_log_cluster_entry`. Cluster catalogue rows are rebuilt by `rebuild_events_log_cluster_view`.

When inlining a multi-condition scripted trigger inside `NOT`, keep the conditions in an explicit `AND` block; sibling conditions in `NOT` use NOR semantics.
Preserve the original rejection behavior when either a shared precondition or the native legality check fails.
For temporary diagnostics inside a state-scoped effect, check country flags through the intended country scope, such as `ROOT`, rather than the state scope.
