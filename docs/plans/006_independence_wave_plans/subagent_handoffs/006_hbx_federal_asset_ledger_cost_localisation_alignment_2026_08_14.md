# Event 006 HBX federal-asset ledger cost-localisation handoff

Date: 2026-08-14

Scope: One bounded cost-text selector correction for the admitted HBX California package.

## Disposition

`independence_wave_hbx_settle_federal_asset_ledger` now uses the existing factory-aware diplomatic cost localisation.

No new cost, effect, AI, admission, Join, asset, or workbook behavior was designed.

## Exact change

File: `common/decisions/006_independence_wave_pacific_decisions.txt:119`.

Identifier: `independence_wave_hbx_settle_federal_asset_ledger`.

Before: `custom_cost_text = independence_wave_cost_diplomatic_standard`.

After: `custom_cost_text = independence_wave_cost_diplomatic_standard_factory`.

The decision already used `can_pay_independence_wave_diplomatic_standard_cost` for availability and `custom_cost_trigger`.

The decision already reserved `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT` through `civilian_factory_use`.

The selector change therefore makes the card disclose the factory commitment already present in the source.

## Localisation reuse

The selector reuses the existing triplet in `localisation/english/006_independence_wave_decisions_l_english.yml`:

- `independence_wave_cost_diplomatic_standard_factory`.
- `independence_wave_cost_diplomatic_standard_factory_tooltip`.
- `independence_wave_cost_diplomatic_standard_factory_blocked`.

The triplet displays standard Command Power, convoy-or-train capacity, and the dynamic `independence_wave_decision_cost.civilian_factory_light` value.

No localisation file was changed in this tranche.

## HBX lifecycle notes

HBX owns this project in the Pacific package category and its requirement is a living former host, a stable HBX coastal command, no other active project, and no completed or in-progress settlement focus.

The project uses the existing long Pacific project duration, pays the existing diplomatic-standard helper on completion, and invokes the existing federal-asset focus and project tooltip on removal.

It cancels when the package or living former host disappears and applies the existing Pacific project failure effect.

Its existing high AI weight and severe-host-threat modifier are unchanged.

The one-factory commitment remains light and is not altered by this patch.

## Safety and boundaries

This is a player-facing disclosure fix for a cost already applied by the source.

It does not change the diplomatic trigger, factory modifier, duration, success effect, failure cleanup, AI, package admission, deterministic Join, portraits, flags, or workbook.

The worktree already contained unrelated Pacific-file edits that convert other factory modifiers to file-scoped constants; those concurrent edits were preserved and were not included in this handoff's intended patch.

DM-42 is not touched by this change and remains outside this handoff.

## Probability evidence

The current mandatory `hoi4.probability_inspect` pass for `common/decisions/006_independence_wave_pacific_decisions.txt` used the `mission_ai_will_do` adapter and returned `PROBABILITY_SOURCE_INSPECTED`.

Receipt: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/770059f028d7af21d7ddb7e0ee76134c6784da9872a9711d8949d0e0e9fca4f9/d8d8a5af12b5b05fc7a48ca79810c13a6ca1efd40e2f3362b3131301d6dcc1c3/probability-inspect-9b4a668f779a.json`.

The inspect saw source revision `7d379ab9956e5d7dbb8156f6191d1c3f5a3db6f567aedfc7542632eedfd53879`, source hash `9b4a668f779a0d7b6c13ae9340258d29e7196fc3aee97b42d0d71168d1d5de83`, 28 candidates, 17 required inputs, zero unresolved items, and `poolComplete=false`.

The decision adapter discovery receipt was also successful with the same source revision and 28 available mission candidates: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/49765a35f550d79063e30bb5350e4597d3139bdcf3160f885386f43a4aeb77ea/b0c3fe3a25a170f15beb4dff9e9e32351d01716b8cc001e0184295ff2890ba25/probability-inspect-9b4a668f779a.json`.

No AI field changed, so no probability evaluate or before/after compare was run.

The incomplete pool limits quantitative AI claims and is recorded rather than treated as a balance result.

HBX uses the ordinary decision framework and does not introduce or modify a decision-owned scripted GUI, so no GUI rewrite was attempted.

## Validation

- Confirmed the HBX block retains the diplomatic-standard availability and cost trigger, factory-light modifier, long Pacific duration, diplomatic payment helper, focus completion hook, cancellation gate, failure effect, and high AI weight.
- Confirmed the HBX source contains exactly one factory-aware selector for this project.
- Confirmed all three reused factory-aware localisation keys exist globally and reference `civilian_factory_light`.
- Confirmed the English localisation source remains UTF-8 BOM from the prior localisation patch.
- Ran focused `git diff --check` after isolating this selector change.

Live HOI4 execution, save/load, and runtime card rendering were skipped because this is a cost-text-only change and live consumer validation remains parent/user-owned.

## Remaining issues

The Pacific worktree retains the parent-owned constant-token cleanup in the same source file and must not be reverted or folded into this narrow selector commit.

The probability pool remains incomplete, and Event 006 whole-event admission remains governed by the current authority boundary.
