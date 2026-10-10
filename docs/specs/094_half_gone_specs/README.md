# Event 094 Half gone specification package

Date: 2026-10-05.

**Status: proposed design, not implemented.** Event 094 keeps its To Be Reworked status; the [companion plans](../../plans/094_half_gone_plans/) hold the original brief, reading inventory, decision register, owner blockers, requirement coverage, validation scenarios and Python reference tests.

## Authority

User decisions: the Event 094 identity, one-country targeting class, the dynamic half-loss of reserve equipment, the 200/400/600/800 category expansions, current-value repeat behavior, the Various Anomalies Medium assignment, and the unresolved mystery.
Proposed design awaiting acceptance: category weights, rounding rules, recovery costs, presentation thresholds, achievements and Chaos tuning.

## Read order

| Part | Design |
| --- | --- |
| 1 | [Half gone](094_half_gone_spec_part_1_core.md) |
| 2 | [Equipment and reserves](094_half_gone_spec_part_2_equipment_and_reserves.md) |
| 3 | [Evolutions and national values](094_half_gone_spec_part_3_evolutions_and_national_values.md) |
| 4 | [Half the population](094_half_gone_spec_part_4_half_the_population.md) |
| 5 | [Characters and continuity](094_half_gone_spec_part_5_characters_and_continuity.md) |
| 6 | [Recovery and government response](094_half_gone_spec_part_6_recovery_and_ai.md) |
| 7 | [Connections and extraordinary recovery](094_half_gone_spec_part_7_connections.md) |
| 8 | [Presentation and assets](094_half_gone_spec_part_8_presentation_and_assets.md) |
| 9 | [Achievements](094_half_gone_spec_part_9_achievements.md) |
| 10 | [Balance, repeat behavior, and acceptance](094_half_gone_spec_part_10_balance_and_acceptance.md) |

## Separate prompts

[Main coding prompt](094_half_gone_coding_prompt.md), [asset prompt](094_half_gone_asset_prompt.md), [super-event prompt](094_half_gone_super_event_prompt.md), [achievement prompt](094_half_gone_achievement_prompt.md), [decision prompt](094_half_gone_decision_mission_prompt.md), and [goal prompt](094_half_gone_goal_prompt.md).

The goal prompt is bounded to 4,000 characters including its final newline. It is separate from the design, and no temporary conversation-continuation prompt is included.

## Revision log

### 2026-10-10 spec audit

- Condensed the README: removed the archive install instructions and the 5 October reading and execution narrative (kept in the companion plans), and the stale claim that the Doctor Wu and Deal with the Devil owner packages were unavailable; Part 7 already links both.
- Replaced the goal prompt's Codex-specific `fork_turns` wording with the repository's subagent routing.
- Pass 2 review retained the design: one loss rule widened by evolutions, a finite four-response aftermath with real opportunity costs, and no duplicated penalties or Deaths credit for disappearances.
