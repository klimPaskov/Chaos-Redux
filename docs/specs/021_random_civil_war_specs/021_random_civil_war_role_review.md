# Event 021 Skill and Subagent Role Review

## Purpose

This note records how the supplied project skills and custom subagent contracts were applied to the Event 021 plan. It does not claim that the subagents ran in this planning environment.

## Skills applied

### Repository rules

`AGENTS.md` established the source-reading requirement, event ownership rules, Event 006 carrier reuse, no unapproved fallbacks, dynamic tuning, event-log alignment, authoritative workbook rule, MCP gates, and completion reporting.

### Event implementation

`chaos-redux-events` established:

- complete random-event registration
- active and prefire evolution paths
- Event Details and evolution-log coverage
- triggerable scenario behavior
- no-target `N/A`
- actor, decision, idea, AI, country, asset, documentation, and spreadsheet alignment
- full cleanup and completion proof

### Event planning

`chaos-redux-event-planning` established:

- idea-first specification style
- deep branch, decision, country, AI, asset, and achievement mapping
- source-spec packaging under `docs/specs/`
- separate prompt files
- a goal prompt under 4000 characters
- a single repository-ready ZIP as the main delivery

### Decisions and missions

`chaos-redux-decisions-missions` established:

- one main visible value
- no more than four spendable cost types per action
- three to five primary actions per phase
- one to three active missions
- map, force, supply, diplomacy, and time-based objectives
- category-picture preference before custom GUI
- compact tooltips and readable dynamic values
- no fairy-dust rewards

### Focus trees

`chaos-redux-focus-trees` established:

- existing countries keep meaningful existing trees
- generic Event 021 claimants do not receive a copied generic tree
- Event 006 actors receive their Event 006 tree
- incompatible completed rewards and dead routes must be blocked
- focus MCP work is conditional on actual focus-file changes
- no Event 021 focus inlay window is justified

### Assets

`chaos-redux-event-assets` established:

- final report, news, category-picture, icon, idea, mission, and achievement families
- separate source art for separate UI roles
- Event 006 ownership of Event 006 flags and portraits
- no invented real-person portraits
- generated period-documentary art for fictional generic scenes
- final PNG, DDS, manifest, handoff, and runtime placement requirements
- no unrequested asset families

### Frame animation

`chaos-redux-frame-animation` was reviewed and produced a negative design result. Event 021 does not need animation. No visual state requires a real per-frame package, and transform-only motion would be invalid.

### Super-events

`chaos-redux-super-events` was reviewed and produced a negative design result. Event 021 has no accepted super-event. Evolution III uses a news event and shared world-threat state.

### Improvement loop

`chaos-redux-improvement-loop` was applied during the revision from the July 25 package. It reduced clutter, removed the custom interface and animation, kept the deeper playable systems, and set a clear closure condition.

### Subagents

`chaos-redux-subagents` established:

- every project subagent must use `fork_context=false`
- context-complete prompts are required
- broad design work belongs to the improvement planner
- narrow reusable script belongs to the scripted-system architect
- weighted behavior requires the probability auditor
- patching agents require handoffs
- parent integration and completion claims remain mandatory

### Dynamic trigger and effect registries

The shared registries established:

- use `is_actual_nonhuman_country` for universal immunity
- do not use `is_special_chaos_country` as the blanket gate
- Event 006 helpers remain shared and package-owned
- new reusable public helpers need documentation
- Event 021 should not duplicate package initialization

### 3D model and portrait workflows

The 3D and portrait skills were reviewed and produced negative design results.

- no custom 3D unit, building, vehicle, aircraft, ship, or creature is required
- no new generic portrait family is authorized
- grounded Event 006 identities remain under the Event 006 portrait and asset contracts

## Custom subagent routing

### Required during implementation

- `chaosx_repo_explorer` for the initial cross-system map
- `chaosx_scripted_system_architect` for the reusable fracture framework
- `chaosx_ai_probability_auditor` before and after weighted logic changes
- `chaosx_decision_mission_auditor` after the decision system is implemented
- `chaosx_country_package_auditor` after ordinary and Event 006 actor integration
- `chaosx_localisation_auditor` after broad player-facing text is written
- `chaosx_documentation_curator` after implementation handoffs accumulate
- `chaosx_event_completion_auditor` before completion
- `chaosx_improvement_loop_planner` once near completion, unless the current accepted plan remains unresolved
- `chaosx_spreadsheet_doc_worker` after final in-game wording exists

### Conditional during implementation

- `chaosx_focus_tree_auditor` only if focus files or focus loading change
- `chaosx_generated_event_art` for report, news, and category-picture art
- `chaosx_icon_artist` for decision, mission, idea, category, and achievement icons
- `chaosx_asset_source_researcher` only when a final image must depict a real historical artifact or scene
- `chaosx_portrait_creator` only when a separately accepted grounded or fictional character portrait is required
- `chaosx_skill_maintainer` only when implementation discovers a reusable workflow or repeated rule worth preserving

### Not routed by this package

- `chaosx_event_ui_worker`, because no event-owned custom GUI is accepted
- `chaosx_3d_model_pipeline`, because no 3D asset is accepted
- `chaosx_super_event_text_researcher`, because no super-event is accepted
- `chaosx_super_event_audio_researcher`, because no super-event is accepted

## Planning-environment limitation

The custom subagent contracts were read in full, but the planning environment did not expose the Codex subagent runtime. No subagent was actually spawned.

The package includes context-complete prompts so the implementation agent can route the required work with `fork_context=false`.
