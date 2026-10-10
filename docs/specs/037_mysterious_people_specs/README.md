# Event 037: Mysterious People specification package

This package is the design source for Event 037, a repeatable global anomaly: people with homes, families, and histories appear in every inhabited state, and each wave has to be settled before the next one arrives.
The player manages one value, Overpopulation Pressure, through a stance, a few settlement actions, and one mission, while hunger and flight from crowded states run through the existing Famine and Migration systems.

Workflow owners: [event integration](../../../.claude/skills/chaos-redux-events/SKILL.md), [decisions and missions](../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md), and [asset production](../../../.claude/skills/chaos-redux-event-assets/SKILL.md).

## Status

Event 037 is in the active Events 1 to 40 milestone.
The legacy two-event stub (manpower for one random country and an alien headline) is retired, and every mechanic in this package is implemented (2026-10-10).
Implementation handoffs are in `docs/plans/037_mysterious_people_plans/`, and the implementation record is `docs/events/037_mysterious_people/overview.md`.

The implementation entry point is [the coding prompt](prompts/037_mysterious_people_coding_prompt.md).

## Acceptance basis

- User requirements: the workbook row, which fixes the name Mysterious People, Minor Repeatable, Chaos level `1`, cluster `15` (Sudden Abundance), and the To Be Reworked status.
- Design: the global civilian-population design came from an imported planning handoff whose acceptance label carried no attributable approval record.
  Parent acceptance, 2026-10-10 (release orchestrator, under the user's 2026-10-10 brief section 2.2 authority, recorded in the release ledger): the redesign is accepted as the Event 037 premise, since it keeps the same core of unexplained new people; origin-targeted repression actions stay removed because the shared camp system offers no such target; the `population_surge` pressure source stays a proposal.
  Disposition: `accepted and queued` for the Event 037 implementation owner, who must prove gradual manpower growth (Implementation question 1).
- The 2026-10-10 audit changes in the changelog were made under the user's 2026-10-10 audit brief, which authorized substantial rework to remove redundant values, repetitive decisions, and micromanagement.

## Package map

| File | Owns |
| --- | --- |
| [Part 1, core](specs/037_mysterious_people_spec_part_1_core.md) | Identity, legacy stub, promise, core loop, firing, valid states, mystery firewall, log and cluster role, direct Chaos |
| [Part 2, population and ledger](specs/037_mysterious_people_spec_part_2_population_and_ledger.md) | Gain helper, grant model, newcomer share, unsettled backlog, settlement, counts, ownership, runtime cadence |
| [Part 3, pressure and evolutions](specs/037_mysterious_people_spec_part_3_pressure_and_evolutions.md) | Pressure formulas, visible values, Newcomers modifier, Famine and Migration thresholds, evolutions |
| [Part 4, decisions, mission, AI](specs/037_mysterious_people_spec_part_4_decisions_missions_and_ai.md) | Category, stances, actions, costs, mission, visibility budget, AI, cleanup |
| [Part 5, events and flavour](specs/037_mysterious_people_spec_part_5_events_flavour_and_reactions.md) | Event map, manifestation report, flavour pool with options, writing direction |
| [Part 6, system connections](specs/037_mysterious_people_spec_part_6_system_connections.md) | Ownership table, proportional losses, no origin-targeted actions, unconnected systems, multiplayer |
| [Part 7, assets, achievements, catalog](specs/037_mysterious_people_spec_part_7_assets_achievements_and_catalog.md) | Asset inventory, three achievements, Event Details, log detail, documentation set |
| [Balance matrix](quality/037_mysterious_people_balance_matrix.md) | Worked numbers for grants, pressure, settlement, consequences, and balance cases |
| [Probability scenarios](quality/037_mysterious_people_probability_scenarios.md) | Named scenarios for every weighted surface |
| [Acceptance criteria](quality/037_mysterious_people_acceptance_criteria.md) | Pass or fail checks and validation scenarios |
| [System flow](diagrams/037_mysterious_people_system_flow.md) | Runtime flow, ownership, invariants |
| [Research boundary](research/037_mysterious_people_research_boundary.md) | Useful research and its limits |
| [Catalog and cluster alignment](handoffs/037_mysterious_people_catalog_and_cluster_alignment.md) | Workbook row, replacement wording, cluster record |
| [Coding prompt](prompts/037_mysterious_people_coding_prompt.md) | Entry point, work order, subagent routing |
| [Goal prompt](prompts/037_mysterious_people_goal_prompt.md) | Compact goal statement |
| [Ledger prompt](prompts/037_mysterious_people_population_ledger_and_adapters_prompt.md) | Delegation to the scripted-system architect |
| [Decision prompt](prompts/037_mysterious_people_decision_mission_prompt.md) | Decision implementation and audit focus |
| [Asset prompt](prompts/037_mysterious_people_asset_prompt.md) | Asset routing and paths |
| [Achievement prompt](prompts/037_mysterious_people_achievement_prompt.md) | Achievement implementation focus |

## Main design decisions

- Newcomers are real state population, created through a neutral gain helper that removes the engine's instant recruitable gain so armies grow as people settle.
- Each state stores a newcomer share rather than a count, so every ordinary loss and proportional move keeps the ledger correct without adapters in other systems.
- Unsettled newcomers are the only pressure input Event 037 owns, settled at a monthly rate the player raises through stance and projects.
- One national value (Overpopulation Pressure) and one modifier (Newcomers) carry every national effect.
- Famine and Migration receive requests through their public entry points only, at fixed hotspot pressure thresholds.
- Recurring work touches only countries with unsettled newcomers and at most three hotspots each (the three most crowded eligible states), and the only world-wide pass happens once per firing.

## Scope boundaries

Event 037 has no food value, refugee system, relief action, or movement decision, because Famine and Migration already own them.
It has no origin-targeted action, no canonical origin, no scripted GUI, no focus tree, no country tag, no super-event, no world-end scenario, and no portraits, flags, animation, audio, or 3D assets.
Any later expansion needs a specific observed gameplay gap.

## Open questions

### Conflicts with recorded requirements or imported design

1. Premise replacement (decided 2026-10-10: accepted, see Acceptance basis; the workbook row is updated with the implementation).
   The workbook row still describes the legacy premise, a major country receiving millions of unexplained recruits.
   This package replaces it with a global civilian-population event.
   The user should confirm the replacement before the workbook row changes and before the design is marked accepted.
2. Origin-targeted persecution (decided 2026-10-10: stays removed, see Acceptance basis).
   The imported concept let governments at the highest evolution persecute the newcomers through closed settlement zones, forced relocation, forced labor, and systematic killing aimed at them.
   This audit removed those actions because the shared camp system never offers a protected-class target selector, and it kept persecution as politics through Restricted Registration, the origin register event, and flight.
   The user decides whether origin-targeted routes should return, which would also need a change to the camp system's boundary.

### Proposals awaiting acceptance

1. A dedicated `population_surge` value in `humanitarian_pressure_source`, so Famine and Migration reports can name crowding as a cause.
   It touches shared constants, so the coding prompt falls back to the existing `event` source unless the Famine and Migration owners accept it.

### Implementation questions

1. Whether recruitable manpower grows gradually after the instant gain is removed is an engine-proof gate (Part 2).
   If it does not, the timed recruitable-population fallback described there needs user approval.
2. The inhabited-state threshold, grant table, settlement rate, and pressure scale are planning anchors to tune against the installed state-population distribution.

## Changelog

### 2026-10-10 orchestrator review

- Recorded the parent acceptance of the redesigned premise and the removal of origin-targeted repression actions.

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Corrected the cluster record: Event 037 is a Medium member of Sudden Abundance (catalog cluster `15`, not yet registered in the runtime), not a Low member of Various Anomalies, which is live at ID `11` with Events 42 and 47, and removed the provisional cluster ID `9`.
- Recorded the legacy runtime stub, its retirement, and the existing `037_mysterious_population` file stem and folders that the implementation keeps.
- Replaced the original planning-environment claims (no repository, wiki, MCP, workbook, or subagent access, uploaded-file hashes, Codex TOML definitions, `AGENTS.md`, `fork_turns`, and the `.agents/skills` mirror) with the current Claude workflow, `CLAUDE.md`, and `.claude/skills`.
- Named the real repository surfaces the design depends on: `humanitarian_state_is_valid`, the loss helper and the two owner-specific credit precedents, `famine_apply_pressure_request`, `migration_request_flight_pressure`, the civilian transfer primitive, and `on_state_control_changed`.
- Renamed the achievement IDs to the repository's `037_` pattern and moved event-owned asset paths to the existing slug.
- Made one owner per topic and turned the coding, goal, decision, ledger, asset, and achievement prompts and the acceptance criteria into pointers to the owning part, removing restated rules, MCP gates, and completion rules that `CLAUDE.md` already owns.
- Deleted `quality/037_mysterious_people_package_manifest.md` (stale checksums), `quality/037_mysterious_people_source_reading_manifest.md` (upload hashes and environment limits), `quality/037_mysterious_people_parent_improvement_review.md` (its rationale now lives in Scope boundaries and Main design decisions), and `handoffs/037_mysterious_people_subagent_routing.md` (now the routing table in the coding prompt).
- Reflowed every file to one sentence per line.

Pass 2, design improvement:

- Replaced the per-state integration meter, the hidden-population and registration-confidence mechanics, and the absolute provenance ledger with one newcomer share and one unsettled backlog per state, which removes the need for loss adapters in about fifteen other systems and keeps the ledger inside real population automatically.
- Gave Overpopulation Pressure a concrete formula and cut the visible values to three in the header and four in a hotspot tooltip, dropping trend, next threshold, strongest positive and negative factors, and integration labels.
- Folded the demographic dividend and strain into one Newcomers modifier with concrete scaling.
- Replaced the open-ended "sparse registry" with a bounded monthly host pulse over countries with unsettled newcomers and at most eight hotspots each, since a global event would otherwise register nearly every state.
- Cut the decision list from about twenty actions and four missions to two stances, five actions, and one mission, removing everything that only redirected to Famine or Migration (agricultural support, emergency food channels, military logistics, foreign relief, planned settlement, redistribution, national food program, settlement compact, corridor and settlement missions) and the one-time Population Office gate and Employ the New Workforce button.
- Removed origin-targeted closed zones, forced relocation, forced labor, and extermination to match the camp system's no protected-class selector rule (see Open questions).
- Connected Famine and Migration through fixed hotspot thresholds with worked magnitudes, and stated where Event 037 deliberately has no connection (Condemnation, CBRN, fallout, Air Cleanliness, world threat).
- Trimmed the flavour pool from thirty-four outlines to seventeen events with concrete options, merged the national report into the manifestation report, and moved scenes away from records and archives toward people and places.
- Reduced direct Chaos to four milestones by dropping the `1%` and single-firing milestones, which fired alongside others, and the guarded recovery, which cost a crisis-cycle tracker for `-2` Chaos.
- Rewrote the achievements around the remaining values and cut the asset inventory to the icons that have a consumer.

## Implementation status (2026-10-10)

The orchestrator accepted the audited design as the event premise on 2026-10-10, with origin-targeted actions kept out and the `population_surge` source left as a proposal.
The design is implemented under the `037_mysterious_population` file stem, and `docs/events/037_mysterious_people/overview.md` is the implementation record.
Recruitable manpower: installed documentation does not prove gradual recovery after the instant gain is removed, so the Newcomers modifier carries a `conscription_factor` that keeps unsettled newcomers out of the recruitable target until they settle (the Part 2 fallback, recorded in the overview).
Sudden Abundance is registered in the runtime as cluster 15 with Event 037 as its Medium member; the other catalogue members join when their packages register member rows.
Live campaign validation is user-owned.
