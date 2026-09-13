# Event 029 decision parser repair plan

Disposition: implemented for the 113 accepted scalar/trigger-name fields; weighted brace repair remains unresolved.
Acceptance basis: the parent reviewed the reported first causes and explicitly accepted 92 same-value static AI political-power hint substitutions and 21 `has_command_power` to `command_power` corrections, preserving strict greater-than comparisons.
The parent assigned implementation ownership only for `common/decisions/029_riches_found_decisions.txt` and this plan/addendum, with immediate guarded backup required.
The missing AI-modifier closing brace is not accepted for implementation until separate probability evidence and parent review.
This document was written before applying any Event 029 gameplay change.

## Error count and first causes

The supplied `logs/launch_08/logs/error.log` contains 114 primary diagnostics attributed to this decision file: 92 malformed scalar tokens, 21 invalid `has_command_power` triggers, and one invalid nested `modifier` trigger.
There are 136 filename-attributed text lines because each of the 22 invalid-trigger diagnostics is followed by a paired `Unknown trigger-type` report.
Those paired lines are not additional source defects.

| First cause | Primary count | Exact affected field or construct | Repair disposition |
| --- | --- | --- | --- |
| Unsupported `constant:` scalar in static hint | 92 | `ai_hint_pp_cost` | Accepted, same-value file-local aliases |
| Nonexistent command-power trigger name | 21 | `has_command_power > constant:riches_found_decision_cost.command_*` | Accepted, rename to documented `command_power` only |
| Missing close before a sibling AI modifier | 1 | `decision_riches_found_temporary_closure.ai_will_do`, lines 3741–3746 | Pending probability baseline/compare and parent acceptance |

There is no evidence of parameterized scripted-helper calls in this file.
All `riches_found_*` helper calls inspected are boolean calls; the only matching `riches_found_* = {` root is the category `riches_found_mine_management`.
Neither this decision file nor its direct scripted trigger file contains dollar-parameter placeholders.
`FROM`, `ROOT`, `NOT`, and similar uppercase scopes/operators are ordinary HOI4 constructs and must not be rewritten as unsupported parameter calls.

## Accepted tranche A: 92 static political-power hints

The source table is `common/script_constants/029_riches_found_constants.txt`, category `riches_found_decision_cost` at line 520.
The exact current values are `pp_light = 10` at line 526, `pp_standard = 25` at line 528, and `pp_heavy = 40` at line 530.
Introduce exactly three file-local declarations near the decision file header:

```txt
@RICHES_FOUND_AI_HINT_PP_LIGHT = 10
@RICHES_FOUND_AI_HINT_PP_STANDARD = 25
@RICHES_FOUND_AI_HINT_PP_HEAVY = 40
```

Add a source comment that these aliases mirror the named shared cost keys because `ai_hint_pp_cost` requires a static numeric amount.
Replace only each `ai_hint_pp_cost = constant:riches_found_decision_cost.pp_<tier>` with the corresponding alias.
Keep shared constants unchanged for payment predicates, payment effects, localisation, and all other fields.
Do not replace `days_remove`, `add_political_power`, `base`, `factor`, or variable values merely because they also reference constants; the supplied errors identify only the hint consumer here.

| Tier | Value | Count | Original source lines |
| --- | --- | --- | --- |
| light | 10 | 11 | 70, 147, 313, 551, 632, 706, 1661, 2123, 4428, 4665, 5041 |
| standard | 25 | 40 | 228, 393, 473, 784, 863, 940, 1022, 1108, 1190, 1348, 1430, 1585, 1737, 1894, 2206, 2394, 2494, 2586, 2665, 2988, 3064, 3139, 3301, 3383, 3557, 3640, 3716, 4031, 4266, 4350, 4587, 4890, 5259, 5555, 6621, 6693, 6842, 6915, 7067, 7213 |
| heavy | 40 | 41 | 1268, 1514, 1810, 1973, 2050, 2301, 2747, 2832, 2912, 3220, 3472, 3797, 3874, 3952, 4111, 4188, 4510, 4743, 4818, 4965, 5112, 5188, 5332, 5408, 5484, 5627, 5703, 5778, 5860, 5941, 6031, 6105, 6177, 6250, 6326, 6402, 6475, 6549, 6768, 6992, 7139 |

These are static resource-saving hints, not normalized selection probabilities or `ai_will_do` weights.
The accepted representation repair preserves their intended values exactly.

## Accepted tranche B: 21 command-power affordability checks

Replace the identifier `has_command_power` with `command_power` at exactly these original lines: 224, 2827, 3215, 3378, 3467, 3635, 3792, 4261, 4346, 4661, 4738, 5403, 5479, 6026, 6101, 6173, 6398, 6763, 6988, 7135, and 7208.
Each occurs in a custom cost trigger, in the acting-country decision context.
There is no project scripted-trigger declaration named `has_command_power`.
Installed vanilla trigger documentation explicitly defines `command_power` in COUNTRY scope.

The exact cost tier counts are five `command_light = 5`, fifteen `command_standard = 10`, and one `command_heavy = 15`, sourced from the current shared table at lines 542, 544, and 546.
Keep the existing `>` operator and constant reference unchanged.
Thus exactly 5/10/15 command power remains insufficient where the original intended predicate required more than that value.
Do not convert this repair to an inclusive gate, change affordability design, or alter the matching negative command-power debit.

## Unresolved weighted brace defect

The only invalid `modifier` diagnostic points at original line 3742 inside `decision_riches_found_temporary_closure`, whose definition starts at line 3671.
At line 3741, the pressure-severe AI modifier opens three blocks but closes only its `check_variable` and `FROM` blocks; the modifier itself remains open.
Therefore the democratic-government modifier at line 3742 is parsed as a trigger inside the pressure modifier rather than as another modifier of `ai_will_do`.
The close on line 3743 currently closes the pressure modifier, line 3744 closes `ai_will_do`, and the extra-looking line 3746 closes the decision.
The category remains open correctly for `decision_riches_found_quarantine`; deleting an arbitrary final brace would damage that structure.

The proposed local repair, pending review, is to move one closing brace from line 3746 to the end of line 3741 and align line 3742 as a sibling modifier.
This would preserve the exact pressure predicate, democracy predicate, factors, and base while making the two intended modifiers independently evaluable.
It still changes currently malformed weighted structure, so it requires the repository's probability evidence pass before an owner applies it and a same-scenario comparison after the change.
No factors or tuning targets are being proposed.

Expected structural result for the final two modifiers:

```txt
modifier = { factor = constant:riches_found_decision_ai.urgent_factor FROM = { check_variable = { var = riches_found_extraction_pressure value = constant:riches_found_decision_threshold.pressure_severe compare = greater_than } } }
modifier = { factor = constant:riches_found_decision_ai.high_factor has_government = democratic }
```

This block is a proposal only and is excluded from the accepted 113-field implementation.
The probability auditor has been assigned a bounded read-only baseline and virtual comparison for this single decision, using pressure below/at/above the severe threshold and democratic/non-democratic cases with other modifiers fixed.
Its evidence belongs in `event29_closure_probability_baseline.md` in this QA directory.
Malformed source must not be treated as a trustworthy live-game probability baseline.

## Required references consulted

Skills used: chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-subagents.
The required offline core wiki pages were previously read and kept as the syntax references for these repairs.
The field-specific references rechecked here are offline Decision modding line 319 for static `ai_hint_pp_cost`, Data structures Constants for numeric file-local macros, and Triggers Scripted triggers for boolean helper invocation.

Installed `common/decisions/_documentation.md` was consulted; it documents decision trigger contexts and evaluation but lacks a field-specific hint declaration.
Installed `documentation/script_concept_documentation.md`, Script Constants, documents the file-local `@` macro and limits `constant:` support to compatible consumers.
Installed `documentation/triggers_documentation.md:2205` documents `command_power > 1.5` in COUNTRY scope.
Installed `common/decisions/CZE.txt:1863` uses a literal political-power hint next to custom-cost gates and debits; installed `common/decisions/AUS.txt:491` uses `command_power > 25`.
The direct Event 029 shared cost and trigger definitions were inspected; no new generic helper or definition change is required.

## MCP and validation limits

A narrow read-only trace for `chaosx.nr29.1`, downstream depth 1, 12 nodes, 20 edges, helper expansion requested, returned `EVENT_INSPECTED_PARTIAL` and focused analysis.
Revision: `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07f1938d769ef093012560ed5862b05101bc231b1e305c78e0839538c7fa8102/b2044bccde92ba8401aebb229cd88060739be070d97c4d563457f37a7cf720c9/event-trace-1102e50fad94.json`.
Focused mode reports zero indexed helpers and defers helper projections/lifecycle passes; it cannot establish decision-parser or weighted-helper correctness.

Before accepted implementation, archive the immediate decision bytes under `pre_patch_event29_decisions/common/decisions/029_riches_found_decisions.txt` in this QA directory and guard against concurrent source/table changes.
Validate the 92 tier mappings and 21 operator-preserving trigger substitutions, then reverse only those transformations and remove the alias header to require byte-for-byte equality with the archived original.
This proves that every decision ID, weighted block, payment debit, extra gate, timer, effect, and unrelated construct remains unchanged.
Confirm the weighted brace defect remains untouched and recorded pending; do not claim the file is fully repaired while that diagnostic remains.

No gameplay simplification or broad Event 029 redesign is proposed.
The accepted tranche addresses 113 primary source errors; the weighted modifier defect remains a separate incomplete item.
No game, desktop, process, staging, or commit operation is authorized or performed by this plan.

## Implemented accepted tranche, 2026-09-05

The parent accepted implementation after first-cause review; the plan above was written first, followed by the exact 113-field patch.
Only `common/decisions/029_riches_found_decisions.txt` was changed in gameplay.
It now contains three documented file-local hint aliases with unchanged values 10, 25, and 40, used at all 92 hint sites.
All 21 command-power custom-cost checks now use `command_power`, retaining their existing strict `>` and shared constant tokens.
No shared tuning definitions, helper bodies, scopes, effect/debit blocks, decision IDs, AI weights, weighted conditions, timers, or other files were altered.

The immediate original is archived at `pre_patch_event29_decisions/common/decisions/029_riches_found_decisions.txt` under this QA directory.
The patch guarded both decision bytes and the source cost table against concurrent edits before writing.
`event29_decision_parser_validation.json` records the exact 92 hint mappings, 21 trigger locations/tiers, and before/after hashes.
Before SHA256: `28d9c69f8ab222c8fea1123ef85814fa55b66a5884c5fba7b8252bd77e527739`.
After SHA256: `2fd18aba5b34587c2594c148f8c55a7a0468ae9b37f5965af2a9b3693c922491`.
Validation passed: reversing exactly the 113 accepted field substitutions and removing only the new alias/comment header reproduces the complete original bytes, including the intentionally deferred malformed weighted block.
The six-line alias header shifts the original source line references in this plan by six lines without changing their relative positions.

The refreshed post-patch narrow event trace returned `EVENT_INSPECTED_PARTIAL`, focused analysis, with the same direct-event revision as the earlier trace.
Post-patch artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1a3b0d0e6edda0af089af81fbd5de03520fa19b57fbd2d07228aa5a6eae8a62/d740e207784a615bab670422e512d79e47ae6514dc05b7e1d4b77e2cfa73e335/event-trace-1102e50fad94.json`.
Its limited direct-event coverage is expected and does not prove decision-parser acceptance.

The initial probability discovery for the deferred brace defect used `decision_ai_will_do` and returned `PROBABILITY_SOURCE_DISCOVERED` with `identifier_not_found` for that adapter.
The same report identifies the decision under `mission_ai_will_do` with one identifier match, so the read-only auditor was told to use the matching service adapter rather than claim the source was absent.
Discovery artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41a8783fa84cbd7d4d12025ccde6d98aaab1f649c0195795ade7dfe825b3b13e/52d7138f3564f5be95b24d5c4f07d18e1831ab38979e5d57208edcf6aa5e349a/probability-inspect-fc67637b8ef1.json`.
The auditor's separate baseline/virtual comparison remains pending and does not block delivery of the accepted independent fields.

Remaining primary defect: the nested modifier at original line 3742, now line 3748, remains unchanged by explicit parent instruction.
Therefore the overall file repair is incomplete until that weighted syntax defect is accepted, patched, and compared under the required evidence workflow.
The 113-field tranche uses no gameplay simplification or unapproved fallback.
