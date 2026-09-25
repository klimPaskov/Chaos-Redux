# Event 006 REG-04 KAR/CRI Decision Callback Audit

Disposition: unresolved. Four of eight ledger-changing paid completions report a newly reached compact; railheads, transit, return commission, and customs still lack that coverage. The required probability evidence was not available by the audit cutoff.

Accepted basis: the user's in-session approval (“i approve everything”), Part 4's highlighted-country group requirement, Part 5's Level 2/REG-04 requirements, and `docs/plans/006_independence_wave_plans/006_event6_reg04_eastern_packages_focus_groups_improvement_addendum_2026-09-25.md`.

## Findings by severity

1. High: `independence_wave_kar_reopen_forest_railheads` (`common/decisions/006_independence_wave_karelia_crimea_decisions.txt:55-73`), `independence_wave_kar_negotiate_border_transit` (original block at `:139-159`), `independence_wave_cri_organize_return_commission` (original block at `:192-211`), and `independence_wave_cri_open_black_sea_customs` (original block at `:245-265`) call their successful completion effects without capturing pre-reward ledger state or calling `independence_wave_kc_report_new_stability_compact` afterward.
2. High: the `chaosx_ai_probability_auditor` was spawned read-only for `independence_wave_kar_form_ski_guard`, `independence_wave_kar_convene_language_commission`, `independence_wave_cri_survey_land_claims`, and `independence_wave_cri_screen_peninsular_services`. Three waits timed out without a final result or artifact, so no scenario-specific probability evidence is available; the other four decisions' weights were not routed before the user-directed cutoff.
3. Low, patched: the four branch-linked success callbacks granted their existing companion gain when the matching focus was already complete, but displayed only the base reward tooltip. Each callback now shows its existing localized companion tooltip only when the matching focus, active group gate, paid receipt, and unawarded marker conditions all match the helper's reward gate.

## Eight completion callbacks

| Package | Decision and completion effect | Compact transition report |
| --- | --- | --- |
| KAR | `independence_wave_kar_reopen_forest_railheads` → `independence_wave_iw033_complete_railheads` | Missing. |
| KAR | `independence_wave_kar_form_ski_guard` → `independence_wave_iw033_complete_ski_guard` | Present: pre-reward capture precedes the receipt/base reward; report follows the matching companion helper. |
| KAR | `independence_wave_kar_convene_language_commission` → `independence_wave_iw033_complete_commission` | Present: pre-reward capture precedes the receipt/base reward; report follows the matching companion helper. |
| KAR | `independence_wave_kar_negotiate_border_transit` → `independence_wave_iw033_complete_transit` | Missing. |
| CRI | `independence_wave_cri_survey_land_claims` → `independence_wave_iw041_complete_survey` | Present: pre-reward capture precedes the receipt/base reward; report follows the matching companion helper. |
| CRI | `independence_wave_cri_organize_return_commission` → `independence_wave_iw041_complete_return` | Missing. |
| CRI | `independence_wave_cri_screen_peninsular_services` → `independence_wave_iw041_complete_screen` | Present: pre-reward capture precedes the receipt/base reward; report follows the matching companion helper. |
| CRI | `independence_wave_cri_open_black_sea_customs` → `independence_wave_iw041_complete_customs` | Missing. |

For each missing row, add `independence_wave_kc_capture_focus_ledgers_before_reward = yes` before the existing successful completion effect and `independence_wave_kc_report_new_stability_compact = yes` after it. Preserve the existing completion effect, payment, duration, cancellation trigger, and failure effect.

## Verified callback and lifecycle details

The four wired companion pairs are guarded by the exact completed branch focus in the decision file: KAR Ski Guard / `independence_wave_kar_commission_border_ski_guard`, KAR Language Commission / `independence_wave_kar_guarantee_language_appeals`, CRI Land Survey / `independence_wave_cri_ratify_land_hearings`, and CRI Services Screen / `independence_wave_cri_audit_peninsular_service_rolls`. Their focus completion rewards independently call the same one-shot helpers when the paid receipt already exists, covering either completion order; each helper checks its exact receipt and award marker before adding the matching `minor_gain`. The opposite branch uses a distinct focus, receipt, helper, and marker.

`independence_wave_kc_capture_focus_ledgers_before_reward` snapshots the package's two ledgers. Successful completion helpers publish their existing receipt flags before applying base ledger effects, and refresh the stabilized flag after clamping. `independence_wave_kc_report_new_stability_compact` compares the snapshot with the post-reward stabilized state and shows the compact tooltip only for a newly reached threshold. Existing inventory callbacks remain separate from these decision completions.

The four wired decisions retain their existing standard duration, paid `complete_effect`, controlled-capital and single-active-project requirements, and package/capital cancellation behavior. Cancellation continues to call `independence_wave_kc_apply_failure`; the successful base reward helpers are unchanged. The four uncovered decisions retain their original short or long duration and cancellation behavior in the current source.

For the eight scoped decisions, visible costs use at most three spendable types each and have icon coverage: command power plus trains for railheads and transit; command power, infantry equipment, and support equipment for ski guard and services screen; command power and manpower for the language commission, land survey, and return commission; and command power, convoys, and fuel for customs. Their decision cost keys are in `localisation/english/006_independence_wave_karelia_crimea_l_english.yml` (railheads through customs entries at lines 97-120 in the inspected source). No fifth cost is hidden in the audited callback changes.

These are four visible paid actions per active package within this bounded slice, below the six-action limit; the rest of the category was not audited here. No mission is among the eight callbacks. The decision success tooltips describe the existing base ledger effects. This pass did not audit every availability-tooltip string or the wider category's text density.

## Patch and validation

Changed source: `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`. The four pre-existing callback additions were present in the shared working tree at audit start. This audit added only the four conditional companion `custom_effect_tooltip` calls and aligned their limits with the matching focus-group gate, receipt flag, and one-shot marker; it did not add weights or change costs, durations, base rewards, cancellation, or failure behavior.

Changed handoff: this file. The companion text keys already exist in `localisation/english/006_independence_wave_focus_l_english.yml`: `independence_wave_kar_commission_border_ski_guard_companion_tt`, `independence_wave_kar_guarantee_language_appeals_companion_tt`, `independence_wave_cri_ratify_land_hearings_companion_tt`, and `independence_wave_cri_audit_peninsular_service_rolls_companion_tt`.

Validation was a source and diff review of the eight decision blocks, matching receipt/reward helper order, branch gates, costs, and localized cost icons before the final tooltip-guard patch. The final guard patch was applied after the user's stop instruction and was not re-read or runtime-tested. No tests were run and Hearts of Iron IV was not launched. The probability audit produced no result before the cutoff, so AI willingness and scenario evidence remain unresolved and must not be inferred from source alone.

The accepted focus MCP limitation remains: `hoi4.focus_inspect` reported 184 direct nodes and its render omitted root-level imported `shared_focus` nodes, so it cannot certify this shared attachment or focus layout. The accepted record is in the improvement addendum's read-only MCP baseline section; the direct artifacts are [focus inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb08f0ddfbc30d82ca5f729736445c9381d548c502195b3e5c97413c1bf7538d/38aaef5cc169dc705ff3f8077a3727ecbeef162ec7b36cb331c89f8b6cfcb039/focus-inspect.150b4ac59bee7.json) and [focus render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e6262aa14491369c6a08adbe9c6679f01651774b5392b7034ca3909b8baec64/d8ceb18d4c4db176214b11ceea5cd3c5221d6a973df9325cf1f67ee19af7aa97/independence_wave_focus_tree.focus.html). No duplicate direct-focus fallback was introduced.

No broader Event 006 completion claim is made. The four transition hooks were integrated after the audit cutoff; the decision probability audit remains unresolved. Related focus, effect, trigger, and localization files were active elsewhere in the shared working tree at the audit cutoff, so the handoff did not stage or commit them independently.

## Parent integration update (2026-09-26)

Parent review confirmed all eight successful paid ledger-gain callbacks now capture pre-reward values and report newly reached stability after their original completion effects, including the four callbacks named above. The four paired branch decisions retain the audit's group/focus/receipt/marker tooltip guards and display the companion explanation when payment occurs after its focus. Costs, timers, base rewards, failure, and cancellation paths were left intact. The decision probability route remains unresolved: the auditor's bounded MCP waits returned no probability artifact, and no AI weights were changed or compared. The latest source and MCP status are recorded in the [current source-of-truth map](../006_source_of_truth_map.md); this integration does not change the Event 006 **HOLD / PARTIAL** status.
