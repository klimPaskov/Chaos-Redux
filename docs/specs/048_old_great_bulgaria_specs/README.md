# Event 048: Old Great Bulgaria

## Specification pack status

This package is the source design for Event 048, Old Great Bulgaria.

It expands the supplied rough concept into a complete planning handoff for event flow, evolutions, focus-tree architecture, decisions, integration, formables, politics, diplomacy, AI behavior, regional reactions, assets, achievements, super-events, Chaos effects, event-cluster behavior, cleanup, implementation order, and acceptance evidence.

The pack preserves the accepted event promise:

- Bulgaria receives an immediate and extreme military, industrial, logistical, and political surge.
- Bulgaria gains a large event-owned focus tree whose opening becomes playable within weeks.
- Greater Bulgaria is available at baseline.
- Evolution I strengthens the San Stefano campaign.
- Evolution II unlocks the Bulgarian Empire route.
- Evolution III unlocks the trans-Black-Sea Old Great Bulgaria route.
- Claims may be immediate, but cores require control, integration, or a formation milestone that proves administration.
- The event adapts to the current owner of each target and avoids redundant wars.
- Bulgaria remains an ordinary human country and keeps access to normal civilian systems.

## Source hierarchy

Use the sources in this order:

1. The supplied Event 048 rough concept.
2. The files under `specs/`.
3. The geographic and historical limits under `research/`.
4. The route, AI, Chaos, asset, and acceptance matrices.
5. The implementation prompts.
6. Existing Chaos Redux mechanics and repository conventions.
7. Vanilla Hearts of Iron IV precedents and the offline Paradox wiki during implementation.

When a later implementation detail conflicts with the event promise above, the event promise takes priority unless the design is explicitly revised.

## Pack map

### Main specifications

- `specs/048_old_great_bulgaria_spec_part_1_core.md`
- `specs/048_old_great_bulgaria_spec_part_2_event_flow_and_evolutions.md`
- `specs/048_old_great_bulgaria_spec_part_3_focus_tree_architecture.md`
- `specs/048_old_great_bulgaria_spec_part_4_decisions_integration_formables.md`
- `specs/048_old_great_bulgaria_spec_part_5_politics_diplomacy_ai.md`
- `specs/048_old_great_bulgaria_spec_part_6_assets_super_events_achievements.md`
- `specs/048_old_great_bulgaria_spec_part_7_chaos_cluster_cleanup_validation.md`
- `048_old_great_bulgaria_full_spec.md`

### Research and geography

- `research/048_old_great_bulgaria_historical_research.md`
- `research/048_old_great_bulgaria_geographic_state_groups.md`

### Diagrams and matrices

- `diagrams/048_old_great_bulgaria_focus_tree_lane_map.md`
- `diagrams/048_old_great_bulgaria_formable_progression.md`
- `matrices/048_old_great_bulgaria_focus_registry.csv`
- `matrices/048_old_great_bulgaria_decision_mission_registry.csv`
- `matrices/048_old_great_bulgaria_formable_requirements.csv`
- `matrices/048_old_great_bulgaria_state_group_registry.csv`
- `matrices/048_old_great_bulgaria_ai_scenarios.md`
- `matrices/048_old_great_bulgaria_chaos_impact_map.md`
- `matrices/048_old_great_bulgaria_asset_manifest_plan.md`
- `matrices/048_old_great_bulgaria_route_coverage.md`
- `matrices/048_old_great_bulgaria_idea_lifecycle.csv`
- `matrices/048_old_great_bulgaria_achievement_matrix.csv`
- `matrices/048_old_great_bulgaria_evolution_matrix.csv`
- `matrices/048_old_great_bulgaria_regional_reaction_matrix.csv`

### Quality and handoff

- `quality/048_old_great_bulgaria_design_acceptance.md`
- `quality/048_old_great_bulgaria_improvement_loop_closure.md`
- `quality/048_event_catalog_patch.csv`
- `source_manifest.md`

### Implementation prompts

- `prompts/048_old_great_bulgaria_focus_tree_prompt.md`
- `prompts/048_old_great_bulgaria_decision_mission_prompt.md`
- `prompts/048_old_great_bulgaria_asset_prompt.md`
- `prompts/048_old_great_bulgaria_super_event_prompt.md`
- `prompts/048_old_great_bulgaria_achievement_prompt.md`
- `prompts/048_old_great_bulgaria_coding_prompt.md`
- `prompts/048_old_great_bulgaria_goal_prompt.md`

## Public mechanic budget

The player tracks two persistent custom values:

1. **National Momentum**
2. **Imperial Administration**

Everything else remains a hidden calculation or a short qualitative status.

No third persistent custom meter should be added without revising this specification.

## Presentation decision

Event 048 does not need a full custom mechanic window.

The event uses:

- a compact decision-category status header
- normal decisions and timed missions
- a selected-target flow for territorial pressure
- an exact territorial state-puzzle display for formable proof
- focus-tree navigation for the large replacement tree
- ordinary report, news, and super-event presentation at major milestones

This choice keeps the event readable and leaves the map, army, focuses, and decisions as the main play surfaces.

## Implementation-time locks

Several items must be locked against the installed game and current repository before code is accepted:

- exact Hearts of Iron IV state IDs
- exact state-puzzle geometry and projection
- current Bulgarian character ownership and portrait reuse
- exact vanilla focus, decision, event, flag, railway, supply, and unit precedents
- final focus coordinates and connector paths
- final numeric balance after scenario evaluation
- final super-event quotes and audio sources
- final asset dimensions where the active consumer differs from the project reference family

These are evidence gates, not permission to reduce the design.

## Completion boundary

This package is a specification. It does not claim gameplay implementation, in-game validation, final art, final audio, exact state-ID locking, or catalog workbook updates.

The coding agent must report any missing route, state group, AI behavior, decision family, asset, achievement, super-event, evolution, or formable requirement as an omission. Silent fallback content is forbidden.
