# Events Log Evolutions, Events List, and Detail Windows

## Purpose

This UI exposes History, Evolutions, Events, and Clusters tabs for fired entries, progression milestones, defined event chains, and the event cluster catalogue.

It also provides clickable detail windows for history entries, evolution entries, event-list entries, and cluster catalogue or history entries.

The cluster detail window is a current-state view for catalogue rows and an immutable snapshot view for successful history rows.

The shared event detail window also carries authored gameplay text for Zombie Outbreak and War Contagion, with stage previews for their event-owned evolution paths.

Event 17 detail text preserves the selected minor and original faction leader from the exact history sequence, uses neutral lost-result wording when the leader was deleted, and uses unresolved wording when no leader was bound for that history row.

Event 17 exposes ordered previews for Regional Bloc Race, Pressured Neutrality, and Collapse of Neutrality, while its history evolution rows show only stages that actually recorded.

Evolution detail rows use their specific stage title and retain the generic evolution label only as fallback text.

The workbook Evo I through Evo V fields mirror the complete description bodies shown by the evolution detail popup, while titles remain in the title selector.

## Step-by-step behavior

1. Opening the popup initializes history, evolution, event-list, and cluster controls.
2. Clicking History rebuilds the fired history view.
3. Clicking Evolutions rebuilds the recorded evolution view.
4. Clicking Events rebuilds the event catalogue from the normal event registry and live metadata.
5. Clicking Clusters rebuilds the cluster catalogue from the registered cluster definitions.
6. The Events row checkbox changes event enable state without changing Event Chaos availability.
7. Cluster row and detail checkboxes change cluster enable state without granting event-system bypasses.
8. Clicking an event row opens the shared event detail window.
9. Clicking a cluster catalogue row opens current cluster details.
10. Clicking a successful cluster history row opens its saved cluster details.
11. Clicking a cluster member opens ordinary event details while preserving the cluster context.
12. The Events and Clusters footer bulk checkbox controls only the active tab's registry.
13. Event detail windows show current event metadata for catalogue rows and selected history metadata for fired rows.
14. Evolution rows remain inspection rows and do not inherit cluster activation chance.
15. World-end rows remain controlled by the world-end registry and are independent from cluster member rows.

Evolution rows can open their own evolution detail popup, and event detail evolution previews remain clickable when the selected event exposes logged or preview stages.

The evolution detail popup shows the evolution title, summary, logged actor link, and an authored portrait panel only when the selected evolution family and stage have an authored portrait mapping or intentional placeholder treatment.

The zombie evolution detail path also exposes its stage-specific modifier breakdown.

World-end detail rows remain below the evolution preview and preserve independent scenario toggles and terminal-readiness gates.

## Events tab sorting and filtering

The Events tab filters All, Enabled, Disabled, Repeatable, Fire-Once, and Major.

The Events tab sorts By Event ID, By Fired, By Weight, and By Chaos Level.

By Fired hides events with no logged firing.

Sorting uses aligned event metadata and stable event-ID tie handling.

A normal event-system eligibility failure displays N/A instead of zero and reports the first canonical reason.

Disabled events and already-fired unique events retain zero because their state is intentional.

## Clusters tab sorting and filtering

The Clusters tab filters All, Available, Unavailable, Enabled, and Disabled.

The Clusters tab sorts By Cluster ID, By Type, By Roll, By Unlock Tier, By Member Count, and By Fired.

Sort order is Ascending or Descending.

By Roll is the live automatic-pool-weighted mean of distinct eligible trigger events.

    by_roll = sum(trigger_event_weight × trigger_activation_chance) / sum(trigger_event_weight)

Only distinct trigger events that pass current automatic-pool eligibility and have positive live weight contribute.

When no eligible positive-weight trigger exists, the cluster displays N/A.

Random Stuff is the exception because it has no fixed trigger rows.

Its By Roll value is the live precise whole-pool activation chance. It opens at 0.30 percent at tier 3, rises gradually after valid misses, and can exceed one percent during a long dry streak.

The catalogue and Settings activation summary use Varies by member where member rows have different computed chances.

A unique event detail shows the current trigger-specific activation chance.

A duplicate staged event ID shows Varies by row because one event ID can represent multiple logical rows.

Cluster member rows expose role, severity, declared minimum, effective minimum, ordinary event-system availability, starting chance, final chance, roll, status, and canonical reason.

The Random Stuff catalogue has no permanent member rows and shows the current 3-to-5-event batch size plus the current authoritative eligible-pool count.

Its history rows show the exact uniformly selected event IDs with role Random Draw, severity Not Used, the event's independent minimum tier, and their final delayed-dispatch result.

Member rows display trigger and required guarantees as 100 percent and Guaranteed after eligibility.

Manual rows display Manual and no roll.

Ineligible or invalidated rows display N/A and retain their canonical reason.

## Cluster eligibility and dispatch

The ordinary event-system eligibility contract applies to automatic triggers, manual triggers, required rows, optional rows, and delayed rows.

A selected trigger rejected by the ordinary event system does not roll a cluster and continues through ordinary standalone handling.

The cluster can narrow eligibility with its own unlock, cooldown, enable, severity, two-pass support, and participation rules.

Required status guarantees participation after eligibility and never bypasses event-system fireability.

Manual cluster forcing may bypass cluster-only gates and the automatic activation roll, but it cannot dispatch a trigger or member rejected by the equivalent event-system force context.

The trigger fires first synchronously after eligibility.

Required rows follow after eligibility.

Optional rows normally follow Low, Medium, High, then Severe severity bands, with random order inside each band. The band-preservation chance falls dynamically from 90 percent at Calm World to 80 percent at World Collapse.
Other multi-band batches invert one random adjacent severity boundary, so a higher-severity member can precede a lower-severity member.

The optional participation chance uses the current tier and severity table, the eligible-count factor, and 0.95 decay per accepted optional row.

The decay count increases only after an optional row is accepted in the current batch.

High and Severe non-trigger rows require another pass-one base-eligible row.

Trigger rows and sole configured members are exempt from that support requirement.

Random Stuff instead receives one guarded dynamic attempt after a successfully fired ordinary automatic minor event at tier 3 or above.

It samples uniformly without replacement from the positive-weight candidates returned by the ordinary all-events evaluator, ignoring major or minor type, severity, and weight magnitude.

The first selected event fires synchronously and the rest use the shared delayed recheck queue.

Manual Random Stuff activation bypasses its cluster gates but retains strict event-system eligibility and does not update its automatic drought, success, or cooldown memory.

## Stable state and history

Events 6, 9, and 13 have explicit stable primary trigger rows for their opening duplicate groups.

Every activation receives a stable batch identity.

Queued cluster state preserves cluster, batch, logical row, trigger, history, and event-specific runtime context.

Delayed dispatch rechecks ordinary event-system fireability immediately before firing.

An invalid delayed row is skipped and invalidated with N/A and its first canonical reason.

Overlapping batches remain isolated and cannot borrow a target, actor, history sequence, staged payload, or row context.

Probability state is versioned and non-destructive.

Only a successful cluster activation creates a cluster history row.

The history row snapshots activation chance, activation roll, trigger, tier, batch, actor, and valid context.

Each member snapshot stores chance, roll, role, severity, effective minimum, status, and canonical reason.

Queued member settlement fields remain provisional in the successful activation's history row until that batch completes.

After batch settlement, historical values never recompute from current Chaos tier, fatigue, member definitions, live weights, or event-system availability.

Automatic fatigue and previous-participation memory exclude manual forcing.

A successful fixed-member cluster activation applies one pacing and one cooldown update regardless of member count.

For Random Stuff, the ordinary minor event that opened the attempt already supplied the single pacing update, while the successful bonus batch supplies only its 240-day cluster cooldown.

## Detail-window selection state

The selected cluster state includes events_log_selected_cluster_sequence, events_log_selected_cluster_id, events_log_selected_cluster_type, events_log_selected_cluster_tier, events_log_selected_cluster_unlock_tier, events_log_selected_cluster_roll_chance, events_log_selected_cluster_available, events_log_selected_cluster_enabled, events_log_selected_cluster_unavailability_reason, events_log_selected_cluster_date, events_log_selected_cluster_trigger_event_id, events_log_selected_cluster_actor, events_log_selected_cluster_has_actor, events_log_selected_cluster_member_count, events_log_selected_cluster_fired_count, and events_log_selected_cluster_skipped_count.

The cluster source and detail arrays retain stable row, role, severity, effective minimum, chance, roll, trigger, batch, status, and reason values.

The selected detail view uses current values for catalogue rows.

The selected detail view uses saved values for successful history rows.

## Data integration

Events-list metadata arrays include global.events_log_events_view_fired_entries, global.events_log_events_view_enabled_entries, global.events_log_events_view_unique_entries, global.events_log_events_view_weight_entries, global.events_log_events_view_chaos_level_entries, and global.events_log_events_view_unavailability_reason_entries.

Cluster catalogue arrays include global.events_log_cluster_view_id_entries, global.events_log_cluster_view_type_entries, global.events_log_cluster_view_tier_entries, global.events_log_cluster_view_trigger_event_id_entries, global.events_log_cluster_view_member_count_entries, global.events_log_cluster_view_unlock_tier_entries, global.events_log_cluster_view_roll_chance_entries, global.events_log_cluster_view_available_entries, global.events_log_cluster_view_enabled_entries, and global.events_log_cluster_view_unavailability_reason_entries.

Cluster member history arrays include global.events_log_cluster_member_cluster_sequence_entries, global.events_log_cluster_member_event_id_entries, global.events_log_cluster_member_status_entries, global.events_log_cluster_member_danger_entries, global.events_log_cluster_member_unavailability_reason_entries, global.events_log_cluster_member_row_id_entries, global.events_log_cluster_member_role_entries, global.events_log_cluster_member_severity_entries, global.events_log_cluster_member_declared_min_tier_entries, global.events_log_cluster_member_effective_min_tier_entries, global.events_log_cluster_member_base_chance_entries, global.events_log_cluster_member_final_chance_entries, global.events_log_cluster_member_roll_entries, global.events_log_cluster_member_trigger_entries, and global.events_log_cluster_member_batch_id_entries.

Probability-state arrays include global.event_cluster_probability_state_cluster_id_entries, global.event_cluster_probability_state_fatigue_entries, global.event_cluster_probability_state_success_count_entries, global.event_cluster_probability_state_manual_count_entries, global.event_cluster_probability_state_last_optional_fired_entries, global.event_cluster_probability_state_last_optional_eligible_entries, global.event_cluster_probability_state_last_participation_ratio_entries, global.event_cluster_probability_state_last_activation_chance_entries, global.event_cluster_probability_state_last_activation_roll_entries, global.event_cluster_probability_state_last_activation_tier_entries, global.event_cluster_probability_state_last_activation_result_entries, global.event_cluster_probability_state_last_effective_member_count_entries, global.event_cluster_probability_state_last_trigger_row_id_entries, and global.event_cluster_probability_state_last_history_sequence_entries.

Pending queues include event_cluster_pending_member_event_id_entries, event_cluster_pending_member_batch_index_entries, event_cluster_pending_member_batch_id_entries, event_cluster_pending_member_cluster_id_entries, event_cluster_pending_member_row_id_entries, event_cluster_pending_member_trigger_entries, and event_cluster_pending_member_history_sequence_entries.

Detail selection variables include events_log_selected_event_id, events_log_selected_event_type, events_log_history_selected_actor, events_log_history_selected_has_actor, events_log_history_selected_secondary_actor, events_log_history_selected_has_secondary_actor, events_log_selected_evolution_type, events_log_selected_evolution_tier, events_log_selected_evolution_stage, events_log_selected_evolution_event_id, events_log_selected_evolution_event_type, events_log_selected_evolution_actor, events_log_selected_evolution_has_actor, events_log_selected_evolution_has_portrait, events_log_selected_evolution_date, events_log_selected_cluster_sequence, events_log_selected_cluster_id, events_log_selected_cluster_type, events_log_selected_cluster_tier, events_log_selected_cluster_unlock_tier, events_log_selected_cluster_roll_chance, events_log_selected_cluster_available, events_log_selected_cluster_enabled, events_log_selected_cluster_actor, events_log_selected_cluster_has_actor, events_log_selected_cluster_member_count, events_log_selected_cluster_fired_count, and events_log_selected_cluster_skipped_count.

The shared event detail view also uses global.events_log_view_cluster_id_entries, global.events_log_view_cluster_sequence_entries, and global.events_log_view_cluster_type_entries for selected event cluster metadata.

## Generic evolution-disable contract

Evolution controls set events_log_evolution_event_id, events_log_evolution_type, and events_log_evolution_stage before checking is_current_evolution_enabled.

Disabled stages are stored as dynamic global flags, so new evolution chains reuse the same toggle infrastructure.

## Evolution and world-end separation

Evolution preview rows represent progression milestones and use their existing enablement and display rules.

Evolution history rows show only milestones that actually recorded.

World-end entries remain terminal scenario registry rows and preserve their independent toggle and selection rules.

Neither surface supplies cluster activation chance or optional participation values.

## Shortcuts

Ctrl+Shift+E toggles the Event Logs window.

Ctrl+E opens the Event Logs window directly on the Events tab.

Ctrl+Shift+T shows the Event Timer window.

## UI assets and wiring

The window reuses existing Event Logs and Settings sprites, buttons, checkboxes, fonts, flags, row backgrounds, and Chaos tier colours.

No new visual assets are required.

The layout and click routing remain in interface/chaosx_events_log_popup.gui and the existing Event Logs scripted GUI and localisation paths.

Existing evolution detail portrait consumers include GFX_portrait_ZZZ_leader_2, GFX_portrait_ZZZ_leader_3, GFX_portrait_ZZZ_leader_4, GFX_portrait_communist_rebels, GFX_portrait_THR_refuge_bodhisattva, GFX_portrait_THR_bodhisattva_pramudita, GFX_portrait_THR_arhat_administration, GFX_portrait_THR_buddha_mandate_animated, GFX_portrait_THR_divine_sovereignty, GFX_portrait_THR_empty_seat_animated, GFX_portrait_DTH_zol, GFX_portrait_DTH_zol_world_end_animated, GFX_soviet_collapse_evolution_portraits_animated, GFX_portrait_unknown, and GFX_fury_leader_flame_overlay_animated.

No new art is needed for the cluster catalogue, cluster details, or the current event, evolution, and world-end catalog surfaces.

Evolution families without a portrait treatment keep the wide text body, while an authored portrait or intentional placeholder is selected only through the existing stage mapping.

## External validation limitation

The 2026-09-05 curator's read-only MCP evidence and its limits are recorded in [event_clusters_spec.md](event_clusters_spec.md#12-artifact-ownership-and-external-validation). The required narrow event and GUI inspections stalled before returning a result in that probe, so this document does not claim current engine or branch-specific visual acceptance.
