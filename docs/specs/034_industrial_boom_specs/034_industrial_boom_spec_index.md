# Event 34 Industrial Boom specification index

## Catalog identity

- Event ID: `34`
- Event name: Industrial Boom
- Event type: Minor Repeatable
- Status at planning time: To Be Reworked
- Chaos level: 1
- Cluster: Not assigned
- Direct consequence event: Event 35 Great Depression 2.0

## Design promise

Industrial Boom gives one major or player-controlled country an economic acceleration strong enough to alter its production plan immediately. The player may exploit that acceleration, consolidate it into lasting development, or push it into collapse. The event is managed through one public value, `Overheating`, a compact decision category, a small set of state projects, and a controlled-landing objective. Failure hands the same country into Event 35 through one shared depression crisis package. The boom remains repeatable without becoming an uncapped source of permanent factories or building slots.

## Specification files

1. `034_industrial_boom_spec_part_1_core.md`
   - Event identity, target selection, first firing, player experience, baseline phases, event flow, success and failure outcomes.
2. `034_industrial_boom_spec_part_2_overheating.md`
   - Public value, hidden simulation, thresholds, trend display, shocks, relief, incidents, and pacing.
3. `034_industrial_boom_spec_part_3_decisions_missions.md`
   - Decision category presentation, core actions, timed objectives, costs, visibility, state targeting, and AI equivalents.
4. `034_industrial_boom_spec_part_4_regions_legacy_repeatability.md`
   - Industrial Regions, state project progression, reserves, protection, controlled landing, permanent legacy, and repeat-firing controls.
5. `034_industrial_boom_spec_part_5_evolutions.md`
   - Speculative Mania, The Industrial Miracle, Runaway Industrialization, active-event entry, evolved openings, incidents, and containment.
6. `034_industrial_boom_spec_part_6_event_35_inheritance.md`
   - Direct depression handoff, evolution inheritance, starting severity, existing-depression behavior, state memory, and cleanup.
7. `034_industrial_boom_spec_part_7_connections_chaos_cluster.md`
   - Cross-event adapters, Chaos impact map, generic system hooks, cluster analysis, and conflict rules.
8. `034_industrial_boom_spec_part_8_ai_probability_balance.md`
   - AI behavior, target selection, decision ranking, probability scenarios, balance ranges, and tuning goals.
9. `034_industrial_boom_spec_part_9_presentation_assets_text.md`
   - Presentation choice, event and decision text direction, visual asset inventory, icons, category art, reports, and accessibility.
10. `034_industrial_boom_spec_part_10_achievements_acceptance.md`
    - Achievements, edge cases, exploit controls, acceptance scenarios, completion evidence, and anti-bloat conclusion.

## Supporting files

- `034_industrial_boom_decision_map.md`
- `034_industrial_boom_ai_probability_matrix.md`
- `034_industrial_boom_research_notes.md`
- `034_industrial_boom_repository_crosscheck.md`
- `034_industrial_boom_source_reading_ledger.md`
- `034_industrial_boom_subagent_review.md`
- `034_industrial_boom_package_manifest.md`

## Prompt files

- `034_industrial_boom_asset_prompt.md`
- `034_industrial_boom_achievement_prompt.md`
- `034_industrial_boom_decision_mission_prompt.md`
- `034_industrial_boom_coding_prompt.md`
- `034_industrial_boom_goal_prompt.md`

## Presentation choice

The main mechanic uses the ordinary decision interface with a strong static category picture, one Overheating meter or equivalent compact progress display, a trend indicator, and the next threshold. A separate scripted GUI is rejected at planning stage because the mechanic has one public value and at most five primary actions. The implementation agent should escalate to a dedicated event-owned window only when direct inspection proves that the normal category cannot present the meter and state selector clearly. Such a change requires a recorded design exception and the event UI workflow.
