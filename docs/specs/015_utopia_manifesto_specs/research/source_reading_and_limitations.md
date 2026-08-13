# Source Reading and Limitations

## Supplied project source pack

The planning run fully processed the following supplied files.

### Repository rules and mechanics

- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`

### Project skills

- `chaos-redux-event-planning.md`
- `chaos-redux-events.md`
- `chaos-redux-event-assets.md`
- `chaos-redux-frame-animation.md`
- `chaos-redux-super-events.md`
- `chaos-redux-improvement-loop.md`
- `chaos-redux-subagents.md`
- `chaos-redux-focus-trees.md`
- `chaos-redux-decisions-missions.md`

### Catalogs

- `chaos_redux_events_catalog.csv`
- `chaos_redux_clusters_catalog.csv`
- `chaos_redux_scenarios_catalog.csv`

The event catalog row for ID 15 currently reads:

| ID | Name | Details | Type | Cluster | Status |
| --- | --- | --- | --- | --- | --- |
| 15 | World Tension Subsides | Reserved | Minor Repeatable | none | To Be Reworked |

This package replaces that classification with Minor Fire-Once, no cluster, and the Utopia Manifesto design.

### Custom subagent definitions

- `chaosx_repo_explorer.toml`
- `chaosx_improvement_loop_planner.toml`
- `chaosx_scripted_system_architect.toml`
- `chaosx_focus_tree_auditor.toml`
- `chaosx_decision_mission_auditor.toml`
- `chaosx_country_package_auditor.toml`
- `chaosx_localisation_auditor.toml`
- `chaosx_event_completion_auditor.toml`
- `chaosx_documentation_curator.toml`
- `chaosx_spreadsheet_doc_worker.toml`
- `chaosx_asset_source_researcher.toml`
- `chaosx_generated_event_art.toml`
- `chaosx_icon_artist.toml`
- `chaosx_super_event_text_researcher.toml`
- `chaosx_super_event_audio_researcher.toml`
- `chaosx_skill_maintainer.toml`

## External research read

The research pass used Thomas More's *Utopia* as the primary literary source, then used institutional and historical material on cooperatives, worker cooperatives, garden cities, and New Harmony to sharpen the playable design. The detailed bibliography is in `bibliography.md`.

## Environment limitations

The following required implementation sources were not available in the mounted environment:

- the full Chaos Redux repository
- `paradox_wiki/`
- the Hearts of Iron IV vanilla installation and documentation
- approved reference mod installations
- a runtime capable of spawning the supplied project subagents

Because of that limitation, this package does not claim:

- exact live-repository file discovery
- exact reusable helper discovery
- exact vanilla syntax or GUI precedent verification
- exact state-ID mapping
- exact focus-tree replacement compatibility with every installed tree
- actual execution of any project subagent
- actual spreadsheet workbook modification
- actual asset generation, source downloading, DDS conversion, or audio conversion

The package includes exact prompts and a bounded orchestration order so those tasks can be performed reproducibly in the implementation environment.

## Simplification statement

The design itself was not shortened into a popup-only or focus-only outline. It includes the event chain, eligibility, focus architecture, decision loop, ideas, occupations, integration, formable identity, evolutions, AI, assets, super-event direction, achievements, catalog handoff, prompts, and completion criteria.

The only substantive omissions are repository-specific facts that could not be verified without the missing repository and game reference files. Those are listed in `handoffs/unresolved_verification_blockers.md`.
