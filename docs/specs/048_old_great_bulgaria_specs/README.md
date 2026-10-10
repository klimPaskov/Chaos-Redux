# Event 048: Old Great Bulgaria

## Specification pack status

This package is the source design for Event 048, Old Great Bulgaria.

It expands the supplied rough concept into a complete planning handoff for event flow, evolutions, focus-tree architecture, decisions, integration, formables, politics, diplomacy, AI behavior, regional reactions, assets, achievements, super-events, Chaos effects, event-cluster behavior, cleanup, implementation order, and acceptance evidence.

The pack preserves the supplied event promise summarized in `source/048_user_brief_summary.md`:

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

`source/048_user_brief_summary.md` records the supplied premise and evolution thresholds.
The original brief is not retained here, and that normalized summary does not establish acceptance of every planner expansion.
Claims lacking an attributable original user or parent decision remain unresolved.
Package-generation source reports, the independent structural audit, and improvement closure are historical evidence, not current implementation, tool health, or final approval.

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
The seven maintained parts replace the removed combined copy, whose body exactly duplicated those parts.

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

## Open questions

- The Event 045 settlement link (Part 2 and Part 4) depends on the Third Balkan War package keeping its claim and settlement owner; recheck it when Event 045 is implemented.
- Regional reactions (Part 5) name a "regional containment alignment" without a defined mechanic; the implementation should either express it through ordinary guarantees and faction invitations or drop it.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:
- Part 7 no longer claims the workbook lacks the cluster: cluster 6 and Medium severity are already in the workbook and the live registry; only the details and evolution columns remain to apply.
- Replaced `AGENTS.md` with `CLAUDE.md`, removed the Codex `fork_turns` lines, and reduced the goal prompt to a pointer at the coding prompt.
- Deleted `quality/package_file_manifest.csv` and `quality/package_metadata.json`, a hash inventory and a metadata copy that went stale with every edit and repeated the README.

Pass 2, design improvement:
- Settled the open "candidate one-shot Chaos" rows: Event 048 owns no Chaos source, because a formation award would count the same conquests twice.
- Gave the integration choice a real cost in shared systems: military-first pacification uses a harsher occupation law that the famine owner already reads, while civil administration and autonomy avoid it; conquest refugees come from the existing capture adapter.
- Recorded two loose ends (Event 045 dependency, undefined containment alignment) as open questions.
