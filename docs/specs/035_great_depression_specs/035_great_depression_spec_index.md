# Event 35 Great Depression 2.0 specification index

## Catalog identity

- Event ID: `35`
- Event name: Great Depression 2.0
- Event type: Minor Repeatable
- Status at planning time: To Be Reworked
- Chaos level: 1
- Cluster: Negative Economy
- Cluster member severity: Low
- Direct source event: Event 34 Industrial Boom


## Reading and environment boundary

Every file supplied with this task was read in full, including the three catalog exports, all twenty subagent definitions, and every Markdown file in the accepted Event 34 planning package. The live public repository was inspected for Event 34 and Event 35 migration context.

The Windows-only offline Paradox wiki snapshot, installed Hearts of Iron IV documentation, installed vanilla game files, and local HOI4 MCP server were not mounted in this ChatGPT environment. This package therefore does not claim engine-syntax validation, vanilla-precedent inspection, MCP event-chain evidence, or live-game validation. The coding prompt makes those checks mandatory before implementation.

## Design promise

Great Depression 2.0 places one major country or player-controlled country inside a long economic crisis that changes production, construction, logistics, politics, and state development. The player manages one public value, `Depression Severity`, through a compact decision category and a small set of state recovery projects. An independent firing begins as a severe but recoverable national depression. A collapse from Event 34 begins from the same reusable crisis package, inherits the boom's evolution floor, and converts the failed boom's regions, reserves, projects, and management history into the opening depression state.

The event remains playable at maximum Severity. Deep failure causes industrial paralysis, closures, unrest, political transformation, and possible civil conflict through bounded conditions. It does not erase the country through one threshold. Recovery requires sustained improvement, reopened Depression Centers, and a final proof period. Repeat firings remember reforms and scars without becoming a renewable factory deletion or permanent reward exploit.

## Specification files

1. `035_great_depression_spec_part_1_core.md`
   - Event identity, target selection, independent and inherited entry, baseline phases, crisis outcomes, and active-crisis rules.
2. `035_great_depression_spec_part_2_severity.md`
   - Depression Severity scale, hidden contributors, thresholds, trend, shocks, relief, relapse, and tuning model.
3. `035_great_depression_spec_part_3_decisions_missions.md`
   - Decision category, six recovery philosophies, timed objectives, dynamic costs, visibility, AI equivalents, and cleanup.
4. `035_great_depression_spec_part_4_centers_recovery_repeatability.md`
   - Depression Centers, local state progression, closures, reopening, permanent scars, recovery legacies, and repeatability controls.
5. `035_great_depression_spec_part_5_financial_contagion.md`
   - Evolution I exposure network, secondary-country pressure, foreign intervention, full-crisis conversion, and spread controls.
6. `035_great_depression_spec_part_6_social_collapse.md`
   - Evolution II strikes, occupations, riots, radical movements, emergency governments, coups, separatism, civil conflict, and political aftermath.
7. `035_great_depression_spec_part_7_second_great_depression.md`
   - Evolution III worldwide pressure, international stages, supplier booms, global recovery, and worldwide news role.
8. `035_great_depression_spec_part_8_inheritance_connections_chaos_cluster.md`
   - Event 34 handoff, reusable crisis API, cross-event adapters, conflict precedence, Chaos accounting, and Negative Economy cluster behavior.
9. `035_great_depression_spec_part_9_ai_probability_balance.md`
   - AI profiles, target selection, action ranking, probability scenarios, balance goals, exploit controls, and performance limits.
10. `035_great_depression_spec_part_10_presentation_assets_text.md`
    - Presentation hierarchy, player-facing writing direction, report and news roles, visual asset inventory, accessibility, and Evolution III worldwide-news direction.
11. `035_great_depression_spec_part_11_achievements_acceptance.md`
    - Achievement contracts, edge cases, acceptance scenarios, completion evidence, and improvement-loop closure.

## Supporting files

- `035_great_depression_decision_map.md`
- `035_great_depression_state_lifecycle_map.md`
- `035_great_depression_ai_probability_matrix.md`
- `035_great_depression_chaos_impact_map.md`
- `035_great_depression_reusable_crisis_api.md`
- `035_great_depression_research_notes.md`
- `035_great_depression_repository_crosscheck.md`
- `035_great_depression_source_reading_ledger.md`
- `035_great_depression_subagent_review.md`
- `035_great_depression_package_manifest.md`

## Prompt files

- `035_great_depression_asset_prompt.md`
- `035_great_depression_achievement_prompt.md`
- `035_great_depression_decision_mission_prompt.md`
- `035_great_depression_coding_prompt.md`
- `035_great_depression_super_event_prompt.md`
- `035_great_depression_goal_prompt.md`

## Consolidated reading copy

- `035_great_depression_full_spec.md`

This file combines the index and all eleven source specification parts in their canonical order. Supporting maps, research, prompts, and ledgers remain separate to keep the design source readable.

## Presentation choice

The main mechanic uses the ordinary decision interface with a strong category picture, one Depression Severity meter or compact progress display, a trend indicator, the next threshold, up to three material causes, and a phased action list. A separate event-owned scripted GUI is not the planned baseline because the player has one public value and no more than five primary actions in one phase. The implementation agent may escalate to a dedicated window only after direct inspection proves that the ordinary category cannot present the severity state, selected Depression Center, and active mission clearly. Such a change requires a recorded design exception and the event UI workflow.
