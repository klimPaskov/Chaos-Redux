# Event 026 CBRN doctrine owner adapter handoff

Status: rejected and blocked. This tranche has no gameplay adapter and must remain blocked until the owner receives a design-safe resolution for the corridor purchase and the required probability/GUI evidence can be completed.

## Scope and changed files

The assigned write set was `common/decisions/cbrn_doctrine_decisions.txt`, the directly paired `cbrn_doctrine` constants/effects/triggers/localisation files, and this handoff.

Only this handoff was changed. `common/decisions/cbrn_doctrine_decisions.txt`, `common/script_constants/cbrn_doctrine_constants.txt`, `common/scripted_effects/cbrn_doctrine_effects.txt`, `common/scripted_triggers/cbrn_doctrine_triggers.txt`, and `localisation/english/cbrn_doctrine_l_english.yml` were not edited.

No shared Event 026 or universal-cost file, inventory, registry, catalog, allowlist, category, interface, or other owner surface was edited.

## Exact audited voluntary actions

The following reachable rows were audited as voluntary payments or commitments, but none received gameplay changes in this closed tranche.

- `cbrn_complete_delayed_establishment`: ordinary `35` political power plus helper-paid `10` command power; a mixed native-cost remediation purchase.
- `cbrn_begin_hazard_assault_training`: the decision row declares zero cost, but its completion helper pays `100` gas masks and `10` army experience; it is therefore a real mixed purchase.
- `cbrn_set_defensive_preparation_policy`: ordinary `15` political power and `0` command power.
- `cbrn_set_retaliation_authority_policy`: ordinary `25` political power plus `5` command power.
- `cbrn_set_limited_battlefield_policy`: ordinary `50` political power plus `15` command power.
- `cbrn_set_strategic_release_policy`: ordinary `75` political power plus `25` command power.
- `cbrn_set_unrestricted_policy`: ordinary `100` political power plus `40` command power.
- `cbrn_commission_sealed_tank_crews`: ordinary `25` political power plus commitment-paid `5` command power.
- `cbrn_commission_persistent_shell_filling`: ordinary `25` political power plus commitment-paid `5` command power.
- `cbrn_commission_nerve_suppression`: ordinary `25` political power plus commitment-paid `5` command power.
- `cbrn_commission_biological_security_assault`: ordinary `25` political power plus commitment-paid `5` command power.

The following rows are not voluntary purchases and were intentionally left unchanged: `cbrn_convene_institutional_review`, `cbrn_chaos_warfare_establishment_mission`, `cbrn_hazard_assault_training_mission`, `cbrn_claim_protective_foundation`, `cbrn_claim_delivery_integration`, `cbrn_claim_theater_exploitation`, and `cbrn_claim_terminal_command`.

## Rejected custom-cost row and exact blocker

`cbrn_assign_decontamination_corridor` is the owner’s one existing custom-cost row and remains rejected and blocked.

Its ordinary payment has seven distinct spendable types: `5` political power, `4` command power, `40` decontamination equipment, `100` gas masks, `20` support equipment, `2` motorized equipment, and `300` fuel.

The decision and missions skill imposes a hard maximum of four distinct spendable cost types for one decision or gameplay-changing GUI action. Adapting this row without dropping or merging costs is therefore impossible under the tranche contract.

The irreversible payment path also crosses the excluded `cbrn_hq_effects` owner through `cbrn_hq_debit_decontamination_stock_oldest_first`. Calling the existing `cbrn_apply_theater_decontamination_assignment` after a universal quote would debit the resources a second time, while bypassing it would require reimplementing another owner’s oldest-first stockpile behavior. Removing costs or changing that route would alter the accepted logistics mechanic and exceeds this owner’s authority.

This row must remain on its existing ordinary path. It must not be registered, catalogued, or allowlisted by this tranche.

## Adapter coverage decision

The eleven mixed-cost rows above are technically candidate surfaces for a shared adapter: their native components can be quoted with `universal_cost_quote_integer`, preflighted before debit, paid with `universal_cost_pay_component`, receipted with `universal_cost_record_transaction`, settled after irreversible completion, and refunded from the stored actual-paid receipt if completion fails.

The training row additionally requires an owner-owned external gas-mask payment and an exact external refund acknowledgement before the shared transaction can become fully refundable.

The policy rows require prepayment to be coordinated with `cbrn_change_chaos_warfare_use_policy` so its existing helper does not debit command power twice.

The technology commission rows settle at commitment because their existing localisation and cancellation contract says the commitment is not refunded when the commission later becomes invalid.

Those are implementation findings, not completed adapter coverage. No shared transaction, display quote, active payment, receipt, refund, or settlement call was added.

## Required invariants for a future implementation

A future adapter must use the same owner-side candidate and all existing route, target, cooldown, reserve, project, prerequisite, cancellation, and AI rules.

The custom-cost trigger and completion effect must use the same active-source test and the same integer upward-ceiling quote, including exact display/paid agreement and ordinary-cost modifiers.

Every component must be affordability-preflighted before the first debit, and the transaction must record the actual paid amount only after the owner payment succeeds.

The logical action must have one primary achievement family and must settle only after the irreversible success point.

No reward, penalty, duration, cooldown, upkeep, casualty, reserve, project, or non-consumed requirement may be discounted.

## Lifecycle and surface audit notes

The category is an ordinary decision category, not a named Event 026 dedicated scripted GUI. No new GUI was appropriate within this bounded owner tranche.

The category can expose more than six gated primary rows over its lifecycle, but the rows are phased by doctrine, milestone, failure, and technology flags. The establishment and training missions are non-selectable and do not create a purchase pool; each has a single owner, category, requirement path, timeout duration, success/failure effect, and no duplicate activation intended by the existing guards.

Player-facing ordinary cost strings currently mix literal resource names and spendable values on several affected rows. The required icon-first localisation cleanup was not applied because this tranche was stopped before gameplay edits; it remains an open issue even for the rejected corridor row.

The adapted candidate rows use at most two spendable types each, while the corridor uses seven and violates the four-type budget. The relevant icons are `£pol_power`, `£command_power`, `£army_experience`, `£gas_mask_equipment_text_icon`, `£decontamination_equipment_text_icon`, `£support_equipment_text_icon`, `£GFX_motorized_equipment_text_icon`, and `£GFX_fuel_texticon`.

Existing AI weights, route gates, target checks, and cooldowns were not changed. A future custom-cost implementation must add the documented ordinary political-power hint where the engine otherwise cannot reserve a custom cost, without changing the existing AI willingness factors.

Existing cleanup and exploit guards were not changed. The future adapter must keep transaction ids payer-scoped, prevent duplicate receipts/refunds, preserve the technology no-refund commitment contract, and leave the corridor’s oldest-first stockpile debit owned by its current helper.

## Validation and blockers

Required repository, decision/missions, subagent, Event 026 specification, offline Paradox wiki, and installed Vanilla documentation intake was completed before the stop request.

The scoped pre-handoff status and diff check showed no changes in any of the five gameplay/localisation files or this handoff path.

The mandatory `hoi4.gui_inspect` call for window `cbrn_operations_category` with scenario id `cbrn_doctrine_category_audit` timed out at the MCP 180-second boundary and returned no artifact.

The mandatory `hoi4.gui_render` call for the same ordinary decision category, including 1920x1080 and 1366x768 states, timed out at the MCP 180-second boundary and returned no artifact.

The mandatory `chaosx_ai_probability_auditor` route was started with `fork_context=false` and then stopped at the user’s explicit stop request before it returned probability evidence. No probability result or live proof is claimed, and no AI-weight compare was run.

No live Hearts of Iron IV session was launched or claimed.

## Remaining blockers and next action

The tranche is incomplete and explicitly rejected, not silently partial.

The parent must either provide an accepted design that reduces the corridor to four or fewer spendable types while preserving its intended logistics mechanic, or leave the corridor blocked and route it to the appropriate owner for a broader design decision.

Only after that decision, and after the required probability and GUI MCP routes return usable evidence, may the eleven candidate rows receive the shared-framework adapter.

No plan handoff beyond this rejection was written.
