# Event006 Event005 Origin Separation Audit

Date: 2026-06-05
Owner: parent agent
Scope: Event005-side audit for paths that could accidentally apply Soviet Collapse systems to Event006-origin countries.

## Findings

- `soviet_collapse_setup_breakaway_country` is guarded with `NOT = { has_country_flag = chaosx_release_origin_independence_wave }`.
- `soviet_collapse_load_event_created_focus_tree` is guarded with `NOT = { has_country_flag = chaosx_release_origin_independence_wave }`.
- Direct Event005 high-chaos successor focus loads exist inside bespoke successor setup effects, but their spawn triggers require the target tag to not exist. An existing Event006-origin overlap tag is therefore not a valid high-chaos spawn target through those trigger paths.
- Direct scans found only the two expected Event006-origin references in Event005 script, both in the guard positions above.

## Validation

- Searched Event005 effects, triggers, decisions, focus trees, and events for:
  - `chaosx_release_origin_independence_wave`
  - `independence_wave`
  - `soviet_collapse_setup_breakaway_country`
  - `soviet_collapse_load_event_created_focus_tree`
  - direct `load_focus_tree` successor paths
- Sampled the high-chaos successor caller blocks and matching `can_soviet_collapse_spawn_*` triggers.

## Remaining Risks

- This was a static script audit only; no in-game mixed Event005/Event006 scenario was run.
- Future Event005 edits that bypass the existing spawn triggers should keep the same Event006-origin exclusion rule.
