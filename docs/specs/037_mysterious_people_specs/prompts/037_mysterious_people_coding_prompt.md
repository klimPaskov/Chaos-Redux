# Coding prompt: Implement Event 037 Mysterious People

This is the implementation entry point for Event 037.
Read the [package README](../README.md) first for status, acceptance basis, and open questions, then the seven spec parts.
`CLAUDE.md` owns reference reading, MCP use and retry limits, coding style, localisation rules, subagent rules, completion reporting, and commits, and this prompt does not repeat them.

## Starting point

The runtime holds only the legacy stub described in [Part 1](../specs/037_mysterious_people_spec_part_1_core.md#legacy-runtime).
Every mechanic in the package is pending.
Keep the existing file stem `037_mysterious_population` for `events/`, `localisation/english/`, `gfx/event_pictures/`, `gfx/interface/decisions/`, and a new `interface/037_mysterious_population.gfx`, and use the `mysterious_people_` prefix for event-owned identifiers.

## Work order

1. **Engine proof and helper.**
   Confirm how state `add_manpower` changes state population and recruitable manpower, using `camp_occ_apply_population_credit` and `civilian_transfer_apply_destination_credit` as precedents.
   Add the neutral gain helper from [Part 2](../specs/037_mysterious_people_spec_part_2_population_and_ledger.md#positive-population-helper) and document it.
   Check whether recruitable manpower then grows gradually, and report the result before relying on it.
2. **Ledger and world transaction.**
   Delegate to `chaosx_scripted_system_architect` with the [ledger prompt](037_mysterious_people_population_ledger_and_adapters_prompt.md).
   Review its handoff and own the integration.
3. **Event chain.**
   Replace the stub with `chaosx.nr37.1` to `.5`, the flavour pool `.10` to `.26`, and the rewritten `chaosx.news.42` ([Part 5](../specs/037_mysterious_people_spec_part_5_events_flavour_and_reactions.md)).
   Wire registration, Event Details, history detail, evolution previews, and debug names with the `chaos-redux-events` skill.
4. **Pressure, modifier, and adapters** ([Part 3](../specs/037_mysterious_people_spec_part_3_pressure_and_evolutions.md)).
   Add the `population_surge` pressure source constant only if the Famine and Migration owners accept a new source, and use `event` otherwise.
5. **Evolutions** with the shared evolution system and the `chaos-redux-mtth` skill.
6. **Decisions and mission** with the [decision prompt](037_mysterious_people_decision_mission_prompt.md).
7. **Assets** with the [asset prompt](037_mysterious_people_asset_prompt.md).
8. **Achievements** with the [achievement prompt](037_mysterious_people_achievement_prompt.md).
9. **Documentation and catalog.**
   Write `docs/events/037_mysterious_people/overview.md` and route the workbook update through the [catalog handoff](../handoffs/037_mysterious_people_catalog_and_cluster_alignment.md).

## Subagent routing

Follow `.claude/skills/chaos-redux-subagents/SKILL.md` and give every subagent a self-contained prompt.

| Stage | Subagent | Scope |
| --- | --- | --- |
| Ledger and adapters | `chaosx_scripted_system_architect` | The ledger prompt |
| Before and after any weight change | `chaosx_ai_probability_auditor` | The [probability scenarios](../quality/037_mysterious_people_probability_scenarios.md) |
| After decisions exist | `chaosx_decision_mission_auditor` | The decision prompt |
| After text exists | `chaosx_localisation_auditor` | All Event 037 localisation |
| Assets | `chaosx_generated_event_art`, `chaosx_icon_artist` | The asset prompt |
| After final localisation | `chaosx_spreadsheet_doc_worker` | The catalog handoff |
| Near completion | `chaosx_event_completion_auditor`, then `chaosx_improvement_loop_planner` | The whole package |

## Completion

Check every item in the [acceptance criteria](../quality/037_mysterious_people_acceptance_criteria.md) and the [balance cases](../quality/037_mysterious_people_balance_matrix.md#required-balance-cases).
Report the engine-proof result for recruitable manpower, any open question still unanswered, and any simplification under the `CLAUDE.md` completion rules.
