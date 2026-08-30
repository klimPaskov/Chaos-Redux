# Genocide Crisis Black Friday Adapter Handoff

Status: REJECTED / BLOCKED.

This tranche is not safely complete because the bounded write set cannot provide the required delayed settlement, exact cancellation refund, and pending-achievement confirmation/retraction for the Germany expansion commitment.

Audit date: 2026-08-30.

## Scope and disposition

The audited owner surface is `genocide_crisis_category` in `common/decisions/genocide_crisis_decisions.txt` and the reachable voluntary actions in that category, including the partial predecessor Event 26 adapter.

The exact predecessor custom-cost rows were:

| Row | Ordinary components | Resource kinds | Intended primary family | Disposition |
| --- | --- | --- | --- | --- |
| `germany_expand_occupied_poland_camp_system` | PP 25; dynamic expansion manpower; dynamic support equipment; dynamic trains | `political_power`, `manpower`, `support_equipment_1`, `train_equipment_1` | `state_project` | Rejected and restored to ordinary behavior |
| `sov_expand_gulag_network` | PP 10; command power 5 | `political_power`, `command_power` | `state_project` | Rejected and restored to ordinary behavior |
| `sov_purge_camp_administrators` | PP 10; command power 5 | `political_power`, `command_power` | `political_power` | Rejected and restored to ordinary behavior |

The row `germany_transfer_prisoners_to_experiment_site` is also reachable and was audited, but it has no `custom_cost_trigger` or `custom_cost_text` pair and received no predecessor adapter.

That action uses native political power 35, army experience 5, manpower, `support_equipment_1`, and `train_equipment_1` across its trigger and complete-effect path, which is five spendable component types and therefore exceeds the four-type decision-surface limit without an approved simplification.

No other genocide-crisis voluntary rows were changed.

## Exact actions and callsites

The predecessor changed the following decision callsites and they were removed:

- `germany_expand_occupied_poland_camp_system.custom_cost_trigger` and its `available` gate were restored to the original dynamic manpower, support-equipment, and train checks.
- `germany_expand_occupied_poland_camp_system.complete_effect` was restored to `camp_rework_germany_start_occupied_poland_expansion_mission_in_from = yes`.
- `sov_expand_gulag_network.custom_cost_trigger` and its `available` gate were restored to the original strict political-power and command-power checks.
- `sov_expand_gulag_network.complete_effect` was restored to the original native debits and `genocide_build_gulag_network_in_from = yes` call.
- `sov_purge_camp_administrators.custom_cost_trigger` and its `available` gate were restored to the original strict political-power and command-power checks.
- `sov_purge_camp_administrators.complete_effect` was restored to the original native debits and `genocide_soviet_purge_camp_administrators_in_from = yes` call.
- The predecessor-only `genocide_black_friday` constants block was removed from `common/script_constants/genocide_crisis_constants.txt`.
- The predecessor-only `genocide_black_friday_can_pay_*` trigger block was removed from `common/scripted_triggers/genocide_crisis_triggers.txt`.
- The predecessor-only `genocide_black_friday_pay_*` effect block was removed from `common/scripted_effects/genocide_crisis_effects.txt`.

The net result against the repository baseline is no gameplay diff in the four owner script files.

## Cost behavior and examples

Ordinary behavior is preserved after the rejection.

For a future valid adapter, every positive integer component must use the universal quote result and the same quote in the display, affordability check, debit, receipt, and refund path.

An illustrative Germany expansion bundle of PP 25, manpower 20,000, support equipment 10, and trains 2 would quote as follows under positive-cost ceiling:

| Mode | PP | Manpower | Support equipment | Trains |
| --- | ---: | ---: | ---: | ---: |
| Normal | 25 | 20,000 | 10 | 2 |
| 50% sale | 13 | 10,000 | 5 | 1 |
| 75% sale | 19 | 15,000 | 8 | 2 |

The manpower, support-equipment, and train values in that table are illustrative because the owner constants are dynamic.

For either Soviet row, the ordinary PP/command-power pair is 10/5, the 50% quote is 5/3, and the 75% quote is 8/4 under the same ceiling rule.

The predecessor Germany display key `camp_cost_expansion_non_pp` omitted political power, so its visible cost could not equal the four-component paid bundle.

The predecessor Soviet display key `sov_gulag_network_cost` was static at PP 10 and command power 5, so it could not truthfully display either sale tier.

No localisation was changed because the adapter was rejected.

## Receipt, settlement, and refund contract

The required future path is one payer-scoped transaction allocated by `black_friday_allocate_owner_transaction`.

It must quote and preflight every component before paying any component.

It must pay each native resource kind through the universal payment path and record each actual paid component under that same transaction.

For an immediate Soviet action, settlement and the single primary-family achievement record may occur only after all payment and the action effect succeed, with exact stored-component refund on failure.

For `germany_expand_occupied_poland_camp_system`, the payment must remain pending when the cancellable mission starts.

The mission timeout success callback must settle the stored transaction and confirm its pending achievement.

The mission failure and cancellation callbacks must refund the exact stored actual-paid values and retract the pending achievement.

The permitted write set does not include those callbacks or their owner effect file.

The predecessor instead settled and recorded the Germany transaction at mission launch.

It also paid sale-priced manpower, support equipment, and trains and then called `camp_rework_germany_start_occupied_poland_expansion_mission_in_from`, whose existing implementation calls `camp_rework_consume_expansion_resources` and consumes the ordinary resource bundle again.

Its attempted difference credit therefore made the net resource debit ordinary rather than the quoted sale price, while the transaction was already settled before a possible cancellation.

This violates displayed/paid equality, delayed settlement, exact refund, and pending-achievement behavior.

## Decision lifecycle and contract preservation

The affected category remains `genocide_crisis_category` for Germany and `gulag_and_mass_repression_system` for the Soviet rows.

The restored rows retain their original visibility, `state_target = any_controlled_state`, `on_map_mode = map_and_decisions_view`, route checks, state responsibility checks, cooldown `constant:genocide_timing.decision_cooldown`, reserve checks, project-cap checks, and AI blocks.

The Germany expansion continues to start `germany_occupied_poland_camp_expansion_mission` through the original helper.

That mission is owned by `common/decisions/camp_repression_major_country_decisions.txt`, uses `@CAMP_GERMANY_POLAND_EXPANSION_DAYS`, is duplicate-gated by its active mission and state-project flag, cancels on `germany_auschwitz_complex_dismantled`, reports failure through `camp_rework_germany_fail_occupied_poland_expansion_mission`, reports success through `camp_rework_germany_complete_occupied_poland_expansion_mission`, and reports cancellation through `camp_rework_germany_cancel_occupied_poland_expansion_mission`.

Those callbacks are outside this owner tranche.

The Germany transfer action is a direct action and does not provide a cancellable mission settlement callback that can be adapted inside this write set.

## Cognitive-load and GUI notes

The affected surfaces use the standard decision UI and no owner-authored `scripted_gui` or dedicated GUI window was found in the genocide files.

There is therefore no in-scope GUI layout surface for `hoi4.gui_inspect` or `hoi4.gui_render` in this tranche.

The three predecessor custom rows are three visible primary actions, and the Germany expansion launches one active mission.

The category contains additional genocide actions outside this tranche, but no category layout or visible-action redesign was made.

The current ordinary Germany custom cost string exposes three non-PP values and leaves the PP significance implicit in the native decision cost.

The current ordinary Soviet cost string exposes two values clearly, but it is static and cannot express a sale quote.

No new value dump, tab, category, scripted GUI button, or tooltip was added.

## AI validity, target, and route locks

No AI weight, target rule, route lock, cooldown, reserve rule, action limit, or state-target contract was changed.

The affected Germany AI block retains its site-cap and project-cap modifiers.

The Soviet expansion and purge AI blocks retain their repression-route and focus-hook modifiers.

The Germany state target remains `FROM` after the original decision resolves, and the Soviet state target and route checks remain unchanged.

A probability audit was requested through `hoi4.probability_inspect`, but the MCP call timed out after 180 seconds.

Because no AI values were changed, no probability patch or compare claim is made.

No live gameplay proof is claimed.

## Issue list sorted by severity

1. Critical: the cancellable Germany mission's timeout, failure, and cancellation callbacks are outside the exact write set, so delayed settlement, exact cancellation refund, and pending achievement confirm/retract cannot be implemented safely here.
2. Critical: the predecessor Germany adapter paid sale-priced non-PP components and then invoked the ordinary resource-consuming mission-start helper, breaking actual-paid equality.
3. High: the predecessor settled the Germany transaction and recorded its achievement at launch instead of leaving it pending through the mission.
4. High: the predecessor Germany display omitted the political-power component.
5. High: the predecessor Soviet display remained static at ordinary PP/command-power values during an active sale.
6. High: `germany_transfer_prisoners_to_experiment_site` has five spendable component types across its path and cannot be reconciled with the four-type surface limit inside this write set.
7. Medium: the transfer action has no custom-cost display or universal receipt path and remains ordinary behavior.
8. Low: standard decision UI evidence is not applicable because no owner-authored scripted GUI surface exists.
9. Low: the weighted-logic MCP audit timed out, so there is no live probability artifact.

## Validation

The required source and skill references were read before editing, including AGENTS.md, the decisions/missions and subagent skills, the events skill, the complete Event 26 specification package, the required offline wiki pages, and the relevant vanilla documentation.

Read-only source checks confirmed that the four owner gameplay files contain no remaining `genocide_black_friday` identifiers or predecessor adapter marker blocks.

The restored decision rows contain their original cost and custom-cost callsites.

The target-file diff is empty after removing the predecessor additions.

No shared Event 26, universal-cost, allowlist, inventory, registry, catalog, mission-owner, or on-action file was edited.

The only new file from this tranche is this handoff.

No source-only check is treated as live engine proof.

## Required follow-up and blockers

This tranche must remain blocked until the parent grants a write-set extension or supplies an existing bounded callback route that reaches the Germany mission's timeout, failure, and cancellation effects.

The follow-up must add the pending transaction identifier to the mission lifecycle, settle and confirm only on successful timeout, and refund and retract on failure or cancellation.

The follow-up must keep the Germany expansion's four components in one receipt and must avoid calling the ordinary resource-consuming start helper after sale-priced payment unless its resource consumption is explicitly bypassed.

The follow-up must add truthful dynamic sale localisation for Germany and both Soviet rows with texticons for every spendable value.

The follow-up must decide how the Germany transfer's five spendable components are brought within the four-type surface limit without silently discounting or deleting a required component.

No implementation claim is made for Event 26 integration in this owner after rejection.

