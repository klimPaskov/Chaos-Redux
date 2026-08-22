# Event-system documentation

This directory documents shared random-event selection, eligibility, weighting, clustering, rescue pressure, manual scenario setup, and Event Logs behavior.

## Navigation

- [`event_chaos_levels.md`](event_chaos_levels.md) defines the minimum Chaos tier attached to each registered event.
- [`dynamic_major_event_weights.md`](dynamic_major_event_weights.md) defines active-pool scaling for major-event weight growth.
- [`crisis_rescue.md`](crisis_rescue.md) defines bounded rescue weighting for registered countries near capitulation.
- [`event_clusters.md`](event_clusters.md) is the current event-cluster runtime contract.
- [`event_clusters_spec.md`](event_clusters_spec.md) preserves the original event-cluster design prompt and acceptance intent.
- [`triggerable_scenarios.md`](triggerable_scenarios.md) defines the shared manual scenario registry, controls, launch gates, and setup behavior.
- [`events_log_window.md`](events_log_window.md) defines the main Event Logs window, tabs, history records, actor state, and shared navigation behavior.
- [`events_log_evolutions_and_clusters.md`](events_log_evolutions_and_clusters.md) defines evolution records, event-detail projections, and cluster-facing log behavior.
- [`events_log_world_end_scenarios.md`](events_log_world_end_scenarios.md) defines the public world-end scenario catalog, persistent branch toggles, and shared detail data.

Event-framework mechanics belong here when they apply across event chains. Event-specific prerequisites, routes, outcomes, log rows, detail text, and evolution content remain in the owning event package.
