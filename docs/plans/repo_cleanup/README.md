# Repository cleanup plans and evidence

This directory contains the source prompts, bounded cleanup records, migration plans, completion evidence, and preserved audits for repository-wide Chaos Redux maintenance.

## Cleanup authority and completion

- [`chaos_redux_repo_cleanup_master_prompt.md`](chaos_redux_repo_cleanup_master_prompt.md) is the cleanup scope and acceptance contract.
- [`chaos_redux_repo_cleanup_goal_prompt.md`](chaos_redux_repo_cleanup_goal_prompt.md) records the goal invocation.
- [`repo_cleanup_completion_report_2026-08-22.md`](repo_cleanup_completion_report_2026-08-22.md) records the completed broad cleanup pass and its remaining boundaries.

## Current maintenance records

- [`shared_system_migration_plan_2026-08-22.md`](shared_system_migration_plan_2026-08-22.md) records broad migrations that were reviewed and deferred instead of being partially implemented.
- [`systems_documentation_reorganization_2026-08-22.md`](systems_documentation_reorganization_2026-08-22.md) records the shared-system documentation ownership pass.
- [`git_storage_cleanup_2026-08-22.md`](git_storage_cleanup_2026-08-22.md) records the bounded stale Git-storage cleanup.
- [`event_003_006_bounded_cleanup_2026-08-22.md`](event_003_006_bounded_cleanup_2026-08-22.md) and [`event_013_020_bounded_cleanup_2026-08-22.md`](event_013_020_bounded_cleanup_2026-08-22.md) record bounded event-specific cleanup work.
- [`subagent_handoffs/events_1_20_catalog_description_sync.md`](subagent_handoffs/events_1_20_catalog_description_sync.md) and [`subagent_handoffs/events_1_20_catalog_dead_localisation_cleanup.md`](subagent_handoffs/events_1_20_catalog_dead_localisation_cleanup.md) record the catalog synchronization and its dead-localisation closure.
- [`subagent_handoffs/remaining_safe_cleanup_2026-08-24.md`](subagent_handoffs/remaining_safe_cleanup_2026-08-24.md) records the final reference-proven duplicate localisation and stale-comment cleanup.

## Preserved audits and supporting records

- [`decision_category_presentation_audit.md`](decision_category_presentation_audit.md) preserves the decision-category presentation inventory outside the shared-system source-of-truth folder.
- [`gfx_icon_flag_mapmode_cleanup.md`](gfx_icon_flag_mapmode_cleanup.md) preserves the GFX, icon, flag, map-mode, and division-symbol registry outside the shared-system source-of-truth folder.
- [`interface_audit_2026-07-22.md`](interface_audit_2026-07-22.md) records the earlier interface audit.
- [`chaos_redux_multi_system_fix_spec.md`](chaos_redux_multi_system_fix_spec.md) preserves the older multi-system implementation specification.
- [`subagent_handoffs/`](subagent_handoffs/) contains bounded audit, documentation, spreadsheet, localisation, probability, country, decision, focus, and helper handoffs.

Plans and audits in this directory do not replace current implementation documentation in `docs/systems/` or event-owned documentation in `docs/events/`.
