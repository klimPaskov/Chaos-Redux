# Plans, audits, and handoffs

This directory is the working documentation area. Accepted design belongs in `docs/specs/`, and current event behavior belongs in `docs/events/`.

## Folder convention

- Event work uses `<event_id>_<slug>_plans/`.
- Shared systems and workflows use descriptive `<slug>_plans/` directories.
- Subagent handoffs remain under `subagent_handoffs/`.
- New dated files use `YYYY-MM-DD_<scope>_<type>.md`.
- Historical audit and handoff filenames are preserved to avoid breaking evidence references.
- Large packages should provide `documentation_state.md`, `source_of_truth_map.md`, or an equivalent current-state index.

## Shared plan groups

- `chaos_meter_plans/`
- `gfx_icon_flag_mapmode_cleanup_plans/`
- `repo_cleanup/`
- `world_end_scenarios_plans/`
- `chaos_redux_3d_model_workflow_skill_handoff/`

The duplicate Event 003 plan directories and the current-state contradictions identified in several long-running event packages require explicit design dispositions. They are preserved rather than merged or deleted during structural cleanup.

