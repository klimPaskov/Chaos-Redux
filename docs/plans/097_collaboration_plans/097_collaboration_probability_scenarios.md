# Probability and AI review scenarios

Status: prescribed review, not executed. No HOI4 probability MCP action ran in this task. Python arithmetic checks are not a substitute.

## Required route

The named `chaosx_ai_probability_auditor` must discover the live service and schemas, then inspect the relevant implemented source with `hoi4.probability_inspect`. Use evaluate, sweep, simulate, compare, sequence, and render only when appropriate to the inspected surface.

Pass complete option or list pools for normalization. For a sequence model, explicitly include cadence, recovery, cap halving, cooldowns, removals, resets, player timer behavior, cluster routing, and terminal conditions. Missing parts make the sequence unresolved rather than exact.

A compare request must contain matching before/after source descriptions or complete manifests under identical scenarios. An analysis ID is not a source identifier. Preserve actual source revisions and label results as exact, bounded, sampled, score-only, or unresolved.

## Scenario matrix

| ID | Scenario | Question and expected design behavior |
| --- | --- | --- |
| P01 | Baseline live eligible pool | What is 097's normalized selection chance under the complete real pool? No hard-coded percentage is supplied here |
| P02 | First repeatable occurrence | Verify actual post-fire weight and halved recovery maximum using the shared implementation |
| P03 | Recovery at 0, 5, 15, and 30 months after firing | Recovery follows shared +20 steps and its current halved cap, never a new event-owned monthly pulse |
| P04 | Several repeated occurrences | Verify cap halving and any shared rounding, without changing fire-once siblings |
| P05 | Intelligence cluster with 039, 052, and 097 | Prove a repeatable 097 does not permanently consume the cluster or make 039 repeatable |
| P06 | All native pairs capped | Automatic 097 availability must reflect a genuine no-op where native detection supports it |
| P07 | One newly released country | Its first present-day layer can restore meaningful availability, not historical catch-up |
| P08 | Chaos 199/200, 399/400, 599/600, 799/800 | Inspect evolution eligibility boundary and actual shared timing, not immediate guaranteed activation |
| P09 | Late first appearance at advanced Chaos | One grant using actual active enabled capabilities, no replay of lower-stage layers |
| P10 | Each evolution individually disabled | Later enabled behaviors remain independently correct and disabled effects do not leak |
| P11 | Every evolution disabled | Baseline repeatable event still functions |
| P12 | Multiple human timers and acknowledgments | Distinguish separate legitimate occurrences from replayed recipient events |
| P13 | AI government base case | Score 50, retain direct occupation if legally available |
| P14 | AI garrison pressure | Score 75, prefer native installation |
| P15 | AI garrison pressure with essential direct control | Score 45, retain |
| P16 | AI treaty role with and without an unsafe front | Score 70 or 45, respectively, with authoritative treaty role |
| P17 | Invalid native government bundle at high preference score | Legality rejects creation regardless of preference |
| P18 | Unknown AI input or unavailable score surface | Unresolved integration, never silently assume the favorable value |

## What not to analyze as a random choice

The global grant is mandatory. Early handovers and qualified Fifth Column awards are conditional automatic consequences. Report acknowledgment does not control their probability. Do not add random refusal merely to create an AI chance table.

The government policy in Part 7 is a strategic preference score. It is not automatically an event-option weight. Its eventual native representation must be inspected before making a probability claim.

## Required output

Return inspected source and revision, complete scenario inputs, actual tool actions, probability or score outputs, unresolved fields, and clear findings about contradictions or accidental multipliers. Keep editing outside the read-only auditor's scope unless the parent explicitly assigns an allowed narrow patch.
