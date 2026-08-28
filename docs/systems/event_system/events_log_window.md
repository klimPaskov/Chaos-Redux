# Chaos Redux Event Logs Window

## Purpose

The Event Logs window tracks fired automatic events and cluster activations in a dedicated popup.

The window also exposes inspection and controlled manual-trigger surfaces without moving cluster logic into unrelated settings panels.

The shared detail path distinguishes current catalogue state from immutable historical snapshots.

The Status tab retains the current counters and live-values panel for current major gain, baseline major gain, accumulated major weight, recovery rate, cap reduction, default weight, and timer modifier.

## System flow

1. toggle_events_log_popup opens or closes the window and defaults to History.
2. open_events_log_events_tab opens the same window directly on Events.
3. The popup exposes Status, History, Evolutions, Events, and Clusters.
4. Opening History calls rebuild_events_log_history_view.
5. Opening Evolutions calls rebuild_events_log_evolution_view.
6. Opening Events calls rebuild_events_log_events_view.
7. Opening Clusters calls rebuild_events_log_cluster_view.
8. Opening a catalogue row uses current state, while opening a fired row uses its stored history context.

## History tab behavior

History lists fired event rows and successful cluster activation rows.

History filters remain All, Major, Minor Repeatable, and Minor Fire Once.

History sorts remain By Index, By Event ID, and By Actor, with Ascending and Descending order.

Rows without actors are appended after actor rows in actor sorting.

Clicking an event row opens the shared Event Details popup with the selected fired-on date, log number, actor, and history context.

Clicking a successful cluster row opens immutable cluster details with its saved activation and member snapshots.

A member event appears in normal history only when that member actually dispatches.

A delayed member that becomes invalid is represented in the cluster snapshot as skipped with N/A and its canonical event-system reason.

If a fired event has a mapped actor, the shared detail popup shows that actor as a clickable flag beside the title.

Event 17 stores the second country reference for the faction leader chosen by that exact firing, and its History row and Event Details text use the selected history sequence rather than current faction memory.

If Event 17's stored leader no longer exists, the selected minor remains visible and neutral result text identifies the lost leader instead of substituting a later live faction.

## Events tab behavior

Each event row shows the live selection weight from the ordinary event system.

A disabled event or an already-fired unique event displays zero because that state is stored and intentional.

A normal automatic-pool eligibility failure displays N/A and a red first-reason tooltip.

The event row shows ID, Type, Weight, Chaos lvl, and Fired on the top line.

The enabled checkbox remains independent from Event Chaos availability.

The Events tab filter options are All, Enabled, Disabled, Repeatable, Fire-Once, and Major.

The Events tab sort options are By Event ID, By Fired, By Weight, and By Chaos Level.

By Fired hides events with zero logged firings.

The view rebuilds when a new event is logged while the tab is open.

The Fire Selected button uses the ordinary manual event dispatch path and retains its existing Force Trigger Mode rules.

Manual event dispatch does not automatically become cluster forcing.

A manual cluster force must enter through the separate cluster Settings or cluster-details route.

The ordinary bulk event path prefilters disabled events, Chaos-locked events outside Force Trigger Mode, already-fired major or fire-once events, Event 12 without its manual context, and Event 17 without a dispatchable faction context.

Per-event readiness gates still apply inside the shared fire helper, and the bulk button is disabled when no selected event is currently fireable.

## Event Chaos Level and cluster presentation

Ordinary event-system eligibility is resolved before cluster activation.

A trigger rejected by the event system does not roll its cluster and continues through ordinary standalone handling.

Cluster member severity adds a separate floor of Low T0 Calm World, Medium T1 Gathering Storm, High T2 Rising Chaos, or Severe T3 Chaos Tier.

The effective member minimum is the greater of that severity floor and the declared row minimum.

High and Severe non-trigger rows require another pass-one base-eligible member, while trigger rows and sole configured members are exempt.

Event Chaos Level assignments remain unchanged.

Event Details shows the event's existing Chaos Level separately from cluster member severity and effective minimum.

The severity corrections are Fury as Medium, Tensions Rising as Low, and Black Plague as Severe.

The shared evaluate_event_pool_candidate_unavailability resolver owns the ordered automatic-pool reason contract used by both normal selection and the Events tab.

Its reasons cover Event Chaos Level, active or disabled Zombie Outbreak state, World Revolution unlock, Holy Realm refuge host, Fury target, Tensions Rising world tension, White Peace pair, Utopia host, Brilliant Scientist lifecycle and host gates, Secret Alliance target and lifecycle gates, Cannibalism lifecycle and origin gates, Random Faction dispatch context, Resources Found discovery fields, Independence Wave liberation capacity, Africa Is One lifecycle and host gates, and Black Plague lifecycle and origin gates.

Disabled events and already-fired unique events remain zero without an N/A reason because they are state-controlled rather than dynamically unavailable.

The Chaos-level sort compares aligned tier entries, so event-to-level associations remain intact in either order.

Normal Event Details and bulk manual firing respect the Event Chaos Level, while Force Trigger Mode may bypass that event-system requirement according to its existing force context.

Event Details resolves cluster membership from the shared cluster registry and presents a single member severity directly or a minimum-to-maximum severity range when one event owns multiple logical rows.

Events outside the cluster registry omit the cluster line.

## Event Details world-end catalogue

The shared Event Details popup places World End Scenarios below the evolution preview.

The list contains one row per registered terminal branch owned by the selected event.

Multiple branches owned by one event remain separate rows, while hidden registered identities retain their metadata-controlled visibility and unregistered routes remain absent.

World-end rows use the existing Event Details rhythm, text bounds, and checkbox alignment.

Each row shows its title, owner event, and enabled or active status, and clicking it opens the dedicated world-end scenario details popup.

The scenario checkbox writes only to global.disabled_world_end_scenarios and does not change event enablement, evolution state, or sibling scenario state.

A disabled entry is excluded at its natural automatic terminal-readiness gate, while existing Chaos, world-state, route, and super-event conditions remain authoritative.

The complete world-end registry and wiring contract is documented in events_log_world_end_scenarios.md.

## Clusters tab behavior

The Clusters tab lists the registered cluster catalogue, not only fired clusters.

History lists only successful cluster activations.

Cluster filters are All, Available, Unavailable, Enabled, and Disabled.

Cluster sort modes are By Cluster ID, By Type, By Roll, By Unlock Tier, By Member Count, and By Fired.

Sort order is Ascending or Descending.

By Roll is the live automatic-pool-weighted mean of distinct eligible trigger events.

    by_roll = sum(trigger_event_weight × trigger_activation_chance) / sum(trigger_event_weight)

Only trigger events that are eligible in the current automatic pool and have positive live weight contribute to the mean.

A cluster with no eligible positive-weight trigger event displays N/A for By Roll.

The catalogue and Settings activation summary use Varies by member when one cluster-level value cannot represent all member rows.

Cluster details expose the member role, severity, declared minimum, effective minimum, ordinary event-system availability, base chance, final chance, roll, status, canonical reason, primary-trigger state, and batch context when available.

A unique event detail shows the current trigger-specific activation chance.

A duplicate staged event ID shows Varies by row because one event ID can represent multiple logical rows.

Cluster rows and cluster details keep enable state separate from cluster-only availability gates.

Disabling a cluster blocks automatic activation but does not grant an event-system bypass to manual forcing.

The cluster footer checkbox toggles registered clusters without changing individual event enablement.

Clicking a member row opens the ordinary event detail without replacing the selected cluster or its history context.

## Current and historical chance behavior

Automatic activation chance uses the current tier base, trigger severity factor, eligible logical-count factor, fatigue factor, and previous-participation factor.

The computed automatic chance is rounded and clamped to 1 through 90 before the activation roll.

Optional member chance uses the current tier and member-severity table, the eligible logical-count factor, and 0.95 decay for each accepted optional row in the current batch.

Optional chance is rounded and clamped to 1 through 100.

The trigger and required rows show 100 percent and Guaranteed after eligibility succeeds.

Ineligible and invalidated rows show N/A rather than zero.

Manual cluster details show Manual and no roll instead of a fabricated automatic chance.

Historical details preserve the saved activation and member values.

Queued member status, canonical reason, final chance, and roll remain provisional until their successful activation batch completes.

After batch settlement, historical values never recompute from current tier, fatigue, event definitions, live weights, or availability.

## Dispatch order and state boundaries

The trigger fires first synchronously after ordinary eligibility.

Required rows follow after ordinary eligibility.

Optional rows follow in Low, Medium, High, then Severe order, with random order within each severity.

Opening duplicate rows for Events 6, 9, and 13 have explicit stable primary trigger rows.

Every activation has a stable batch identity.

Queued records preserve cluster, batch, logical row, trigger, history, and event-specific context.

Delayed dispatch rechecks ordinary event-system fireability immediately before firing.

A failed delayed recheck invalidates the row with N/A and the first canonical reason without substituting another row or batch context.

Overlapping batches remain isolated.

A successful cluster activation applies one pacing and one cooldown update for the complete batch.

Automatic fatigue increases by one after a successful activation and decreases by one after a valid failed activation roll.

Gated attempts, failed preflight, and manual forcing leave automatic fatigue and previous-participation memory unchanged.

## Evolutions and world-end details

The Evolutions tab logs registered evolution entries after they actually unlock and does not inherit cluster activation chance.

Zombie evolution logs are written only for the main zombie country and not for dynamic outbreak tags.

Evolution filters remain All, Major, and Minor, driven by the stored event type for each evolution entry.

Evolution sorts remain By Index, By Tier, By Stage, and By Actor, with Ascending and Descending order.

Actor flags render only when an evolution entry has an actor.

Evolution rows show tier and stage and remain inspection rows without enable or disable checkboxes.

The main Evolutions tab resolves actor-scoped rows back to the player scope before writing detail state, so their click behavior remains aligned with non-actor rows.

World-end rows remain owned by their scenario registry and do not become cluster member rows unless the cluster registry explicitly includes them.

Cluster details do not expose hidden world-end routes through unregistered members.

## Stored actors

History actor flags render only when the aligned history view has an actor entry.

Evolution actor flags render only when the aligned evolution view has an actor entry.

Non-actor rows are sanitized to actor zero and has-actor zero.

The secondary history actor is sequence-bound result context and does not replace the primary actor flag.

Event 17 sets the paired secondary-actor presence entry only when its faction signature succeeds.

A missing secondary country with that stored presence bit is a lost result, while a history row without a stored secondary actor remains unresolved.

## Data structures

Events-tab metadata arrays include global.events_log_events_view_fired_entries, global.events_log_events_view_enabled_entries, global.events_log_events_view_unique_entries, global.events_log_events_view_weight_entries, global.events_log_events_view_chaos_level_entries, and global.events_log_events_view_unavailability_reason_entries.

Source history arrays include global.events_log_history_sequence_entries, global.events_log_history_date_entries, global.events_log_history_event_id_entries, global.events_log_history_event_type_entries, global.events_log_history_actor_entries, global.events_log_history_has_actor_entries, global.events_log_history_secondary_actor_entries, and global.events_log_history_has_secondary_actor_entries.

Derived history view arrays include global.events_log_view_sequence_entries, global.events_log_view_date_entries, global.events_log_view_event_id_entries, global.events_log_view_event_type_entries, global.events_log_view_actor_entries, global.events_log_view_has_actor_entries, global.events_log_view_secondary_actor_entries, and global.events_log_view_has_secondary_actor_entries.

Selected history and Event Details actor state includes events_log_history_selected_secondary_actor, events_log_history_selected_has_secondary_actor, global.events_log_open_event_detail_secondary_actor_entries, and global.events_log_open_event_detail_has_secondary_actor_entries.

Event Details cluster metadata uses global.events_log_open_event_detail_chaos_level_entries, global.events_log_open_event_detail_cluster_id_entries, global.events_log_open_event_detail_cluster_min_danger_entries, and global.events_log_open_event_detail_cluster_max_danger_entries.

World-end registry and Event Details state use global.world_end_scenario_registry_*_entries, global.disabled_world_end_scenarios, global.events_log_event_detail_world_end_*_entries, and events_log_selected_world_end_*.

Source evolution arrays include global.events_log_evolution_sequence_entries, global.events_log_evolution_date_entries, global.events_log_evolution_type_entries, global.events_log_evolution_event_type_entries, global.events_log_evolution_tier_entries, global.events_log_evolution_stage_entries, global.events_log_evolution_actor_entries, and global.events_log_evolution_has_actor_entries.

Derived evolution view arrays include global.events_log_evolution_view_sequence_entries, global.events_log_evolution_view_date_entries, global.events_log_evolution_view_type_entries, global.events_log_evolution_view_event_type_entries, global.events_log_evolution_view_tier_entries, global.events_log_evolution_view_stage_entries, global.events_log_evolution_view_actor_entries, and global.events_log_evolution_view_has_actor_entries.

Cluster history arrays include global.events_log_cluster_sequence_entries, global.events_log_cluster_date_entries, global.events_log_cluster_id_entries, global.events_log_cluster_type_entries, global.events_log_cluster_tier_entries, global.events_log_cluster_trigger_event_id_entries, global.events_log_cluster_actor_entries, global.events_log_cluster_has_actor_entries, global.events_log_cluster_member_count_entries, global.events_log_cluster_fired_count_entries, global.events_log_cluster_skipped_count_entries, global.events_log_cluster_activation_chance_entries, global.events_log_cluster_activation_roll_entries, global.events_log_cluster_activation_manual_entries, global.events_log_cluster_activation_batch_id_entries, and global.events_log_cluster_eligible_count_entries.

Cluster member history arrays include global.events_log_cluster_member_cluster_sequence_entries, global.events_log_cluster_member_event_id_entries, global.events_log_cluster_member_status_entries, global.events_log_cluster_member_danger_entries, global.events_log_cluster_member_unavailability_reason_entries, global.events_log_cluster_member_row_id_entries, global.events_log_cluster_member_role_entries, global.events_log_cluster_member_severity_entries, global.events_log_cluster_member_declared_min_tier_entries, global.events_log_cluster_member_effective_min_tier_entries, global.events_log_cluster_member_base_chance_entries, global.events_log_cluster_member_final_chance_entries, global.events_log_cluster_member_roll_entries, global.events_log_cluster_member_trigger_entries, and global.events_log_cluster_member_batch_id_entries.

Cluster catalogue arrays include global.events_log_cluster_view_sequence_entries, global.events_log_cluster_view_date_entries, global.events_log_cluster_view_id_entries, global.events_log_cluster_view_type_entries, global.events_log_cluster_view_tier_entries, global.events_log_cluster_view_trigger_event_id_entries, global.events_log_cluster_view_actor_entries, global.events_log_cluster_view_has_actor_entries, global.events_log_cluster_view_member_count_entries, global.events_log_cluster_view_fired_count_entries, global.events_log_cluster_view_skipped_count_entries, global.events_log_cluster_view_unlock_tier_entries, global.events_log_cluster_view_roll_chance_entries, global.events_log_cluster_view_available_entries, global.events_log_cluster_view_enabled_entries, and global.events_log_cluster_view_unavailability_reason_entries.

Cluster detail arrays mirror the member snapshot fields through global.events_log_cluster_detail_member_event_id_entries, global.events_log_cluster_detail_member_status_entries, global.events_log_cluster_detail_member_danger_entries, global.events_log_cluster_detail_member_unavailability_reason_entries, global.events_log_cluster_detail_member_row_id_entries, global.events_log_cluster_detail_member_role_entries, global.events_log_cluster_detail_member_severity_entries, global.events_log_cluster_detail_member_effective_min_tier_entries, global.events_log_cluster_detail_member_base_chance_entries, global.events_log_cluster_detail_member_final_chance_entries, global.events_log_cluster_detail_member_roll_entries, and global.events_log_cluster_detail_member_trigger_entries.

Probability memory uses global.event_cluster_probability_state_cluster_id_entries, global.event_cluster_probability_state_fatigue_entries, global.event_cluster_probability_state_success_count_entries, global.event_cluster_probability_state_manual_count_entries, global.event_cluster_probability_state_last_optional_fired_entries, global.event_cluster_probability_state_last_optional_eligible_entries, global.event_cluster_probability_state_last_participation_ratio_entries, global.event_cluster_probability_state_last_activation_chance_entries, global.event_cluster_probability_state_last_activation_roll_entries, global.event_cluster_probability_state_last_activation_tier_entries, global.event_cluster_probability_state_last_activation_result_entries, global.event_cluster_probability_state_last_effective_member_count_entries, global.event_cluster_probability_state_last_trigger_row_id_entries, and global.event_cluster_probability_state_last_history_sequence_entries.

Pending state uses event_cluster_pending_member_event_id_entries, event_cluster_pending_member_batch_index_entries, event_cluster_pending_member_batch_id_entries, event_cluster_pending_member_cluster_id_entries, event_cluster_pending_member_row_id_entries, event_cluster_pending_member_trigger_entries, and event_cluster_pending_member_history_sequence_entries, with event_cluster_pending_member_index and event_cluster_pending_batch_id as cursors.

The event_cluster_probability_state version keeps probability memory append-only and non-destructive for existing saves.

## Scripted localisation

The Event Logs localisation helpers include GetEventsLogHistoryTypeView, GetEventsLogEventTypeView, GetEventsLogHistoryEventName, GetEventsLogEventChaosLevelColored, GetEventsLogEventAvailabilityReason, GetEventsLogFilterType, GetEventsLogSortMode, GetEventsLogSortOrder, GetEventsLogEvolutionFilterType, GetEventsLogEvolutionSortMode, GetEventsLogEvolutionSortOrder, GetEventsLogEvolutionTypeView, GetEventsLogEvolutionTierView, GetEventsLogEvolutionStageView, and the cluster-specific detail and chance selectors owned by the same Event Logs localisation path.

These helpers are defined in common/scripted_localisation/chaosx_scripted_localisation_events_log.txt.

## Interactions with existing systems

common/scripted_effects/chaosx_event_cluster_effects.txt owns cluster definitions, row metadata, two-pass eligibility, chance calculation, batch preparation, queue state, cluster history, catalogue state, and cluster Settings helpers.

common/scripted_effects/chaosx_logic_effects.txt owns ordinary random-event selection, event-system availability, event fired-state handling, and the one-time cluster pacing call.

common/scripted_effects/chaosx_settings_effects.txt owns normal manual event firing and the Settings entry points.

common/scripted_effects/chaosx_events_log_effects.txt owns shared history and Event Details state.

common/scripted_guis/chaosx_scripted_gui_events_log.txt owns Event Logs click routing.

common/scripted_localisation/chaosx_scripted_localisation_events_log.txt and localisation/english/chaosx_gui_l_english.yml own the visible names, labels, reasons, chance summaries, and detail text.

interface/chaosx_events_log_popup.gui owns the reusable layout.

Event-name localisation reuses the existing chaosx.event_name.* keys.

Shared Event Details metadata also derives from the history arrays for fired, log, and actor context and the evolution arrays for the latest reached stage.

When a history row should show an actor, the actor must exist before the fired-event handler records the row.

Event immediates run after the generic log recorder for normal random firing, so actor preparation may need to happen in a pre-fire helper.

Event 17's pre-fire helper supplies random_faction_target_country as the primary actor, and random_faction_bind_history_sequence stores the exact history sequence after the generic row is inserted.

A successful Event 17 join stores the pending leader, and the bind and finalize helpers write that leader only when both the leader and matching sequence are present.

The Event Logs scripted GUI copies both selected actors from the clicked derived row before rebuilding Event Details.

## Shortcuts

Ctrl+Shift+E toggles the Event Logs window.

Ctrl+E opens the Event Logs window on the Events tab.

Ctrl+Shift+T shows the Event Timer window.

## Future extensions

Future Event Logs work may add a per-country actor filter or cross-links between cluster and evolution records, provided those additions preserve the current history and source-of-truth boundaries.

## UI and asset wiring

No new visual assets are required.

The window reuses existing Event Logs and Settings buttons, checkboxes, fonts, flags, row backgrounds, and Chaos tier colours.

The existing visual consumers include interface/chaosx_events_log_popup.gui, GFX_flag_small2, GFX_diplo_countrylist_flag_frame, GFX_sort_button_100x29, GFX_chaosx_sort_button_100x29_2, GFX_chaosx_arrow_left, GFX_chaosx_arrow_right, GFX_chaosx_chaos_meter_entry, GFX_chaosx_checkbox_checked, and GFX_chaosx_checkbox_unchecked.

If future Event Logs work needs an additional sprite, place it under gfx/interface/ and register it in the existing Chaos Redux Event Logs GFX file without changing the current cluster contract.

## External validation limitation

The HOI4 MCP probability, event, and GUI routes currently fail with ARTIFACT_MANIFEST_INTEGRITY_FAILED and the message Artifact provenance manifest does not match its immutable address.

This documentation records source and contract evidence only and does not claim engine evidence from those routes.
