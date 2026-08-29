# Event 006 SCN-008 publication-boundary patch handoff — 2026-08-29

Date: 2026-08-29

Status: READY FOR PARENT EVENT PATCH.

## Scope

This bounded patch covers the SCN-008 scenario effect, the scenario-ledger decision category, and the three scenario-ledger navigation decisions. No event source was edited because `events/006_independence_wave.txt` remains parent-owned.

## Changed files and identifiers

- `common/scripted_effects/006_independence_wave_scenario_effects.txt`: `independence_wave_trigger_scenario`, `independence_wave_scenario_freeze_summary`, and `independence_wave_scenario_reset_summary` publication/cleanup contract.
- `common/decisions/categories/006_independence_wave_categories.txt`: `independence_wave_scenario_ledger_category` visibility gate.
- `common/decisions/006_independence_wave_decisions.txt`: `independence_wave_scenario_ledger_previous`, `independence_wave_scenario_ledger_next`, and `independence_wave_scenario_ledger_close` visibility gates.

The only new handoff artifact is this dated markdown file. No generated files, localisation, assets, or unrelated gameplay files were touched.

## Before and after behavior

Before this patch, the scenario failure branch froze blocked rows and dispatched `chaosx.triggerable_scenarios.80` without `chaosx.nr6.2`, while the result event could set `independence_wave_scenario_ledger_visible` from a non-empty blocked array. The ledger category and controls trusted the country visibility flag alone.

The existing `independence_wave_scenario_committed` flag is intentionally reused as the generation-local publication receipt; no new receipt was invented. The success branch now requires committed plan phase, the current scenario plan id matching `global.liberation_plan_id`, Independence Wave plan ownership, the shared `liberation_release_joint_plan_executed` commit receipt, and no execution/scenario/finalization failure flags before setting the scenario receipt.

Only that success branch dispatches `chaosx.nr6.2` followed by the delayed `chaosx.triggerable_scenarios.80`. The shared commit receipt is intentional: `liberation_release_begin_plan` clears it, and `liberation_release_commit_plan` sets it only after finalization, so it closes the gap between a nominal committed phase and a successful transaction.

The failure branch explicitly clears `independence_wave_scenario_committed`, retains the existing failure freeze only as transient diagnostic construction, and calls `independence_wave_scenario_reset_summary` before returning. The reset clears the country ledger flag, indices, summary arrays, and summary dates, so a failed or rolled-back generation leaves no publishable ledger state and no `.80` dispatch.

The category and all three navigation decisions now require the scenario committed receipt, reject both scenario failure flags, and still require the existing country ledger flag. A stale country flag therefore cannot expose the category or controls without a current successful scenario receipt.

## Validation

- `python .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- `python .tools/audit_event6_allocator.py` passed the Event 006 allocator and SCN-008 ranked-registry checks.
- `python .tools/audit_event6_gui_matrix.py` passed the Event 006 statehood-ledger semantic source matrix; it does not claim production rendering.
- A narrow static assertion passed: the scenario-effects file has one `.80` dispatch, it follows `chaosx.nr6.2`, the failure branch has no `.80` dispatch and clears the receipt, and the category plus all three ledger controls require the committed non-failed receipt.

The mandatory `hoi4.gui_inspect`, `hoi4.gui_render`, and event/probability MCP routes were unavailable in this runtime; no engine or production-render evidence is claimed. HOI4 was not launched.

## Parent follow-up and remaining boundary

The parent event patch and source census are recorded in the completion section below.
The only remaining boundary is the unavailable required event MCP inspection; no parent gameplay patch is pending in this tranche.

No simplification, fallback wording, asset substitution, or unrelated source change was made in this tranche.

## Parent event completion

The parent-owned event surface is now closed for the same publication contract.
`events/006_independence_wave.txt:chaosx.triggerable_scenarios.8` no longer dispatches `.80` from its invalid-queue failure branch.
`chaosx.triggerable_scenarios.80` has a committed, non-failed scenario trigger, and option `.a` requires the same committed receipt instead of a non-empty blocked array.
The only `.80` dispatch in the source is the successful `independence_wave_trigger_scenario` branch, immediately after `chaosx.nr6.2`.
The only `independence_wave_scenario_ledger_visible` setter remains option `.80.a`, under that committed trigger.

Parent validation after the event patch passed the strict allocator, country API, flag, FORM-16, SCN-008 scenario matrix, and GUI semantic source matrix audits.
The mandatory HOI4 event, GUI, and probability MCP routes remain unavailable, so this handoff contains source/static evidence only and makes no engine or live-save claim.
