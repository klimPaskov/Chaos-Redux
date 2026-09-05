# Event-system documentation

This directory documents shared random-event selection, eligibility, weighting, clustering, rescue pressure, manual scenario setup, and Event Logs behavior.

These pages separate source descriptions and retained historical reports from acceptance evidence. They do not certify current engine behavior, weighted outcomes, GUI rendering, or live-game state unless a named artifact and limitation are provided.

## Navigation

- [`event_chaos_levels.md`](event_chaos_levels.md) defines the minimum Chaos tier attached to each registered event.
- [`dynamic_major_event_weights.md`](dynamic_major_event_weights.md) defines active-pool scaling for major-event weight growth.
- [`crisis_rescue.md`](crisis_rescue.md) defines bounded rescue weighting for registered countries near capitulation.
- [`individual_crisis_targeting.md`](individual_crisis_targeting.md) defines the three-package country cap, load-aware target pressure, lifecycle providers, and global exemptions.
- [`event_clusters_spec.md`](event_clusters_spec.md) retains the Dynamic Severity-Aware Cluster Overhaul contract candidate pending an attributable acceptance record.
- [`event_clusters.md`](event_clusters.md) is the implementation-facing event-cluster runtime reference.
- [`triggerable_scenarios.md`](triggerable_scenarios.md) defines the shared manual scenario registry, controls, launch gates, and setup behavior.
- [`events_log_window.md`](events_log_window.md) defines the main Event Logs window, tabs, history records, actor state, and shared navigation behavior.
- [`events_log_evolutions_and_clusters.md`](events_log_evolutions_and_clusters.md) defines evolution records, event-detail projections, and the cluster-facing log and sorting contract.
- [`events_log_world_end_scenarios.md`](events_log_world_end_scenarios.md) defines the public world-end scenario catalog, persistent branch toggles, and shared detail data.

Event-framework mechanics belong here when they apply across event chains. Event-specific prerequisites, routes, outcomes, log rows, detail text, and evolution content remain in the owning event package.

## Review and unresolved contracts

The [shared documentation review](../../plans/repo_cleanup/subagent_handoffs/2026-09-05_shared_events_documentation.md) records the complete eleven-file reading set, retained tool evidence, and parent-reviewed repairs.
The cluster candidate and world-end catalog identify unresolved unlock, severity, pacing, example-input, visibility, and retirement claims beside their affected contracts.
Historical plan dispositions are recorded in the [shared-plan review](../../plans/repo_cleanup/subagent_handoffs/2026-09-05_shared_plan_dispositions.md).
