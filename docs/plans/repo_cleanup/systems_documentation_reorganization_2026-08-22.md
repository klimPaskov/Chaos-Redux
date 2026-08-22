# Shared-system documentation reorganization

## Scope

This pass reorganized `docs/systems/` by subsystem ownership, repaired direct references to relocated documents, and added navigation indexes to every current systems subfolder.

The pass changed documentation only. It did not edit gameplay script, localisation, scripted localisation, interface definitions, scripted GUI files, GFX definitions, assets, spreadsheets, or interface layout.

## Resulting structure

`event_system/` is the only new subfolder added under `docs/systems/`. It owns shared event eligibility, weighting, crisis rescue, clusters, triggerable scenarios, Event Logs, evolutions, and public world-end scenario catalog documentation.

The existing `3d_model_pipeline/`, `air_cleanliness/`, `cbrn_warfare/`, `chaos_meter/`, `chaosx_settings/`, and `comfyui_portrait_pipeline/` folders remain the other subsystem owners. Each current systems folder and nested CBRN folder has a README index.

Independent cross-cutting contracts remain at the systems root when a dedicated one-document subfolder would not improve navigation. These include achievements, shared country release and startup compatibility, HOI4 agent-tools integration, main-menu and map-mode contracts, the provider-neutral autonomous robot family, and world-threat aggregation.

## Relocations

The existing content-preserving relocations into the 3D model pipeline, Air Cleanliness, CBRN Warfare, Chaos Meter, and Chaos Redux settings folders were retained and indexed. This includes moving the former top-level `docs/biological_warfare/` and `docs/chemical_warfare/` documents into the existing `docs/systems/cbrn_warfare/` hierarchy.

The following event-framework documents moved into `docs/systems/event_system/`:

- crisis-rescue weighting
- dynamic major-event weights
- event Chaos levels
- event-cluster implementation and preserved source prompt
- triggerable scenarios
- the Event Logs window
- Event Logs evolutions and clusters
- Event Details world-end scenarios

Three misplaced documents left `docs/systems/`:

- `black_plague_rat_route_modules.md` moved to `docs/events/020_black_plague/rat_route_modules.md` because Event 020 owns the route lifecycle.
- `decision_category_presentation_audit.md` moved to `docs/plans/repo_cleanup/decision_category_presentation_audit.md` because it is a dated audit rather than a shared mechanic contract.
- `gfx_icon_flag_mapmode_cleanup.md` moved to `docs/plans/repo_cleanup/gfx_icon_flag_mapmode_cleanup.md` because it is a cleanup registry and evidence record rather than a shared mechanic contract.

The shared formable-state puzzle contract remains under `docs/formables/formable_state_puzzle_system.md`, where its existing README identifies it as shared formable infrastructure.

The provider-neutral autonomous robot contract moved from `docs/shared_autonomous_robot_system.md` to `docs/systems/shared_autonomous_robot_system.md` because it is shared by multiple events.

The obsolete duplicate `docs/systems/chaos_unit_family_registry.md` was removed after verifying that `docs/systems/cbrn_warfare/chaos_unit_family_registry.md` is the existing canonical copy and updating its consumers.

## Reference maintenance

Direct repository references to relocated shared-system documents were rewritten to their current paths. This included current mechanics documentation, helper documentation, event documentation, plans, specifications, handoffs, and the `chaos-redux-events` skill.

One Events 21+ document received a path-only shared-system reference correction: `docs/specs/032_missiles_specs/032_missiles_system_connections.md`. No Event 21+ event-specific design or implementation content was audited or changed.

The `chaos-redux-events` skill now points to the current Event 006 country registry and the current triggerable-scenarios contract.

## Deliberately retained unresolved references

Twelve path mentions in dated Event 006 handoffs still name retired or never-created system documents for the Danubian Confederation and Transylvania packages. They were preserved as historical evidence because replacing them without a verified one-to-one authority would rewrite the meaning of those audits.

The Event 026 implementation crosswalk still names the unimplemented `docs/systems/universal_cost_modifier.md`. Event 026 is outside the Events 1-20 event-specific cleanup boundary, so this pass did not create, relocate, or reinterpret that document.

## Rejected organization candidates

Separate `events_log/`, `country_lifecycle/`, and `interface/` folders were not retained after the user limited this pass to one new systems subfolder. Event Logs were folded into `event_system/`, while country-lifecycle and shared-interface contracts remain at the systems root.

Single-document folders for achievements, world threat, development tooling, and shared autonomous robots were not added because they would increase directory depth without improving ownership clarity.

## Validation boundary

Validation checks the final folder set, README coverage, local README links, direct relocated-path references, exact move preservation where no path text changed, and Git rename detection. It does not claim in-game evidence because no gameplay or interface source changed.

The final staged change contains 193 Markdown files: 87 detected renames, one verified duplicate removal, 12 new README or handoff documents, and 93 modified indexes or reference consumers. All modified files except the intentionally rewritten `docs/systems/README.md` are line-for-line path substitutions or navigation-link updates.

The README audit checked 85 README files and 315 local links with no broken target. Every current subfolder under `docs/systems/`, including nested CBRN folders, contains a README.

The systems-document audit checked 109 Markdown files and 109 relative local links with no broken target.

The stale-path scan found no active consumer of the 88 retired relocation paths. Two deliberate mentions remain in this report to record the old autonomous-robot path and the removed duplicate unit-family registry path.

The direct-path scan found 15 intentionally unresolved mentions: twelve references in dated Event 006 handoffs, two mentions of the Event 026 planned `universal_cost_modifier.md` path including this report, and the duplicate-path record in this report. No current implementation or navigation document depends on those missing paths.

The staged diff contains only Markdown files and no Event 21+ event-specific file, gameplay file, localisation file, interface definition, scripted GUI definition, GFX definition, spreadsheet, or asset. Git rename review and `git diff --cached --check` completed successfully.
