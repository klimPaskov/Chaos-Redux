# Event 026 Black Friday — CBRN occupation adapter handoff

Audit date: 2026-08-30.

Owner: CBRN occupation decisions only.

Status: REJECTED FOR GAMEPLAY PATCH; no decision, constants, effects, triggers, or localisation gameplay files were changed.

The requested complete owner adapter cannot be added safely inside the assigned write set without either discounting only part of a logical action, inventing a replacement payment surface, or changing the existing CBRN occupation lifecycle.

## Exact write result

The only file written by this tranche is this handoff:

- `docs/plans/026_black_friday_plans/subagent_handoffs/cbrn_occupation_adapter.md`

The assigned gameplay files remain unchanged:

- `common/decisions/cbrn_occupation_decisions.txt`
- `common/script_constants/cbrn_occupation_constants.txt`
- `common/scripted_effects/cbrn_occupation_effects.txt`
- `common/scripted_triggers/cbrn_occupation_triggers.txt`
- `localisation/english/cbrn_occupation_l_english.yml`

No shared Event 026 files, universal-cost files, inventories, registries, catalogs, allowlists, categories, dynamic modifiers, or other owner files were edited.

## Decision and commitment inventory

| Identifier | Current reachability | Existing payment surface | Current lifecycle callsites | Disposition |
| --- | --- | --- | --- | --- |
| `cbrn_authorize_coercive_security` | Unreachable because `visible` is `always = no` at `common/decisions/cbrn_occupation_decisions.txt:25`. | Native `cost = 75` at `:22`. | `cbrn_occupation_authorize_coercive_security` at `common/decisions/cbrn_occupation_decisions.txt:43`. | Not a reachable player or AI candidate; retain migration-only route. |
| `cbrn_adopt_protected_occupation` | Reachable when `cbrn_occupation_protected_administration_authorization_requirements` passes. | Native political-power cost at `common/decisions/cbrn_occupation_decisions.txt:55`. | `cbrn_occupation_authorize_protected_administration` at `:72`; fire-once lifecycle at `:57`. | Native Strategy A surface; do not add a second scripted debit. |
| `cbrn_nerve_suppression_sarin` | Currently unreachable because `visible` and `target_root_trigger` require `cbrn_occupation_country_can_prepare_nerve_suppression`, which requires `cbrn_occupation_action_conditions_are_supplied`; `cbrn_occupation_current_version_condition_hook_verified` is explicitly `always = no` at `common/scripted_triggers/cbrn_occupation_triggers.txt:339`. | Custom cost at `common/decisions/cbrn_occupation_decisions.txt:92-96`. | Preparation flag starts at `:131`; release calls `cbrn_occupation_execute_nerve_suppression` at `:154`; direct payload and operation debits occur at `common/scripted_effects/cbrn_occupation_effects.txt:321-331`. | Blocked pending a verified condition receipt and a safe multi-component adapter. |
| `cbrn_nerve_suppression_soman` | Same fail-closed reachability as Sarin. | Custom cost at `common/decisions/cbrn_occupation_decisions.txt:203-207`. | Preparation flag starts at `:242`; release calls `cbrn_occupation_execute_nerve_suppression` at `:265`; direct payload and operation debits occur at `common/scripted_effects/cbrn_occupation_effects.txt:321-331`. | Blocked pending a verified condition receipt and a safe multi-component adapter. |
| `cbrn_deploy_protective_aid` | Reachable when the supplier and selected occupied state pass their existing target gates. | Native political-power cost at `common/decisions/cbrn_occupation_decisions.txt:312`, two civilian-factory commitment units in the decision modifier at `:315-317`, and a dynamic respirator stockpile debit during release. | The project flag starts at `:341-352`; release calls `cbrn_occupation_execute_external_protective_aid` at `:357-363`; the dynamic debit is performed by `cbrn_distribute_requested_external_masks_to_state` from the out-of-scope CBRN protection effects file. | No safe owner adapter in this tranche. |
| `cbrn_seal_state` | Reachable after an owned exact nerve-suppression record exists and the state has no response or discovery record. | Native political-power cost at `common/decisions/cbrn_occupation_decisions.txt:412`. | Immediate target-state effect dispatches `cbrn_occupation_apply_requested_coverup_action` at `:430-440`. | Native Strategy A surface; do not add a second scripted debit. |
| `cbrn_destroy_contaminated_records` | Reachable under the existing exact-record and route gates. | Native political-power cost at `common/decisions/cbrn_occupation_decisions.txt:459`. | Immediate target-state effect dispatches `cbrn_occupation_apply_requested_coverup_action` at `:477-487`. | Native Strategy A surface; do not add a second scripted debit. |
| `cbrn_admit_accidental_release` | Reachable for an undisclosed exact nerve-suppression record. | Native political-power cost at `common/decisions/cbrn_occupation_decisions.txt:503`. | Immediate target-state effect dispatches `cbrn_occupation_apply_requested_coverup_action` at `:521-531`. | Native Strategy A surface; do not add a second scripted debit. |
| `cbrn_permit_inspection` | Reachable for an owned unresolved exact nerve-suppression record. | Native political-power cost at `common/decisions/cbrn_occupation_decisions.txt:550`. | Immediate target-state effect dispatches `cbrn_occupation_apply_requested_coverup_action` at `:568-578`. | Native Strategy A surface; do not add a second scripted debit. |

## Severity-sorted issues

### Critical

1. `cbrn_deploy_protective_aid` is a mixed logical transaction with a native political-power debit, a two-civilian-factory commitment, and an owner-controlled dynamic equipment debit. The shared native payment helper has no civilian-factory reservation or refund branch, and the assigned write set does not include the decision category, shared framework, or CBRN protection distribution helper needed to create one.
2. The protective-aid equipment amount is not available as a stable ordinary cost before release. `cbrn_distribute_requested_external_masks_to_state` calculates target need, applies state and supplier modifiers, selects from multiple concrete respirator models, and debits stock inside the same effect. Quoting a guessed aggregate would make the display and actual paid receipt disagree; quoting after the helper runs would debit before all components are preflighted.
3. The two nerve actions have seven qualifying spendable components before considering the delayed route: the selected Sarin or Soman payload, gas-mask equipment, decontamination equipment, CBRN instrument equipment, support equipment, motorized equipment, and Command Power. This exceeds the four-cost-type ceiling and cannot be repaired by hiding components in the existing tooltip.
4. The nerve payload is a dynamic equipment type consumed by `cbrn_try_debit_action_payload`, while the other six components are paid by `cbrn_occupation_pay_operation_costs`. The shared helper supports neither the dynamic payload type nor arbitrary concrete CBRN equipment IDs, so a local adapter would need owner-specific debit and exact owner-specific refund for each component.

### High

1. Nerve payment happens only at the delayed `remove_effect`, after a 21-day preparation flag, while the custom cost is shown at decision selection. A correct adapter must quote at display, re-quote immediately before release, preflight all components, debit once, record actual paid amounts, and refund a partially paid receipt if any later owner or ledger step rejects. The current release chain has no transaction id, receipt, settlement, or refund callsite.
2. The nerve execution chain intentionally fails closed until the exact-state condition hook is verified. Adding a payment adapter before that hook is live would create a new payment path for a decision that cannot currently resolve its action conditions, with no safe evidence that the owner effect can settle or refund it.
3. Converting the protective-aid or native political-power actions to `custom_cost_trigger` would remove the engine-managed `cost` surface. Leaving native `cost` in place while adding a scripted political-power debit would double-charge. The existing Event 026 native sale ideas already carry the native `political_power_cost` factor and must remain the sole owner of those native rows unless a separate transaction design is approved.
4. The current CBRN nerve cost localisation is not compliant with the icon-first budget: `localisation/english/cbrn_occupation_l_english.yml:19` spells out seven resource names in prose. Fixing it truthfully requires either a complete four-or-fewer cost redesign or a supported custom icon for a bundled resource, neither of which is in this write scope.

### Medium

1. The ordinary CBRN occupation category has no dedicated scripted GUI. The Event 026 specification explicitly keeps existing decision and status surfaces, so no `chaosx_event_ui_worker` handoff is appropriate.
2. The category description and operation tooltips expose several effects and requirements in long prose. They were not rewritten because no gameplay cost surface was safely changed and the required source set does not include a new presentation design.
3. The current decision probability MCP discovered nine decision candidates but only six `decision_ai_will_do` candidates were evaluable without a scenario; the three state-targeted candidates were reported as not found by the adapter. This is a tooling boundary, not evidence that the state-targeted AI candidates are absent from source.

## Cost and requirement clarity audit

The cost-count audit uses actual debits and commitments rather than only localisation text.

| Logical action | Spendable components found | Count | Texticon/display state | Result |
| --- | --- | ---: | --- | --- |
| Protected-occupation authorization | Political Power | 1 | Native engine cost and native sale modifier. | Strategy A source path; no owner B adapter added. |
| Sarin suppression | Sarin payload, gas masks, decontamination equipment, CBRN instruments, support equipment, motorized equipment, Command Power | 7 | Existing custom text is seven-component literal prose at `cbrn_occupation_l_english.yml:19`. | Reject; exceeds the four-type limit and lacks safe dynamic payload/payment/refund support. |
| Soman suppression | Soman payload, gas masks, decontamination equipment, CBRN instruments, support equipment, motorized equipment, Command Power | 7 | Same custom cost text as Sarin. | Reject for the same reason. |
| Protective aid | Political Power, two Civilian Factories committed for the project, and a dynamic number of concrete respirator units from the supplier stockpile | At least 3 logical types and multiple possible equipment components | Requirements text names the factory and reserve; no truthful pre-release component quote exists. | Reject; factory reservation and dynamic distribution are not transaction-adaptable in scope. |
| Seal, destroy, admit, inspection | Political Power | 1 each | Native engine cost. | Strategy A source path; no owner B adapter added. |

The existing target, route, reserve, project, cooldown, action-limit, and AI rules were preserved because no gameplay files were altered.

## Decision lifecycle notes

- `cbrn_authorize_coercive_security` remains a fire-once migration declaration with `visible = always no`.
- `cbrn_adopt_protected_occupation` remains fire-once and keeps its existing authorization requirements and law effect.
- Sarin and Soman retain their 21-day preparation, exact state target, state reservation flag, target-loss cancellation, and 270-day re-enable value; no payment was inserted into their delayed release path.
- Protective Aid retains its 21-day project, two-factory modifier, target-state gate, cancellation checks, and 90-day re-enable value; no partial PP-only adapter was inserted.
- Coverup actions retain their immediate exact-state dispatch, 30-day re-enable value, route checks, and AI modifiers.

## Cognitive-load notes

- The category contains eight visible candidate actions when the protected and aid routes are available, but only one of the nine declarations is intentionally hidden. This can exceed the six-primary-action guidance in a state where the four coverup actions and both targeted routes coexist.
- The coverup actions are a coherent response family, but the category description and operation text ask the player to track evidence, attribution, contamination, trauma, Condemnation, target loss, and multiple equipment reserves.
- The operation cost row is a raw seven-number dump with literal resource names and no current discounted values.
- The protective-aid requirements show the factory commitment and a reserve snapshot, but the actual population-scaled equipment debit is only explained after selection and cannot currently be quoted before commitment.
- Native political-power values are rendered by the engine and have clear significance; the custom operation and aid values do not have a verified truthful sale display.

## Mission quality notes

No missions or selectable mission declarations are owned by `cbrn_occupation_decisions.txt`.

The targeted decisions behave as delayed decision projects rather than missions.

Their owner, category, state region, target requirement, duration, success, failure, cancellation, and duplicate-risk evidence is listed below.

| Decision | Owner/category | Target and duplicate guard | Duration | Success/failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| Sarin/Soman suppression | Country / CBRN occupation measures | Any controlled exact occupied non-core state; state preparation flag and route gates prevent duplicate target use. | 21-day preparation plus existing active/cooldown lifecycle. | Release calls the shared chemical dispatcher; fail-closed condition and payment proofs currently reject without mutation. | A future adapter must not create a second receipt if the delayed release is retried. |
| Protective aid | Supplier country / CBRN occupation measures | Any eligible foreign occupied state; project flag, protection project flag, core/controller, emergency, and gap checks prevent duplicate use. | 21-day project plus 90-day re-enable. | Release calls the external distribution helper; missing supplier, target, or usable stock leaves the effect without a success proof. | A future adapter must bind the exact supplier and target and settle/refund once. |

## AI validity and route-lock notes

- No AI weights or route checks were changed.
- Native political-power actions retain their existing AI blocks and are not double-wired through custom costs.
- Sarin and Soman retain invalid-target, compliance-agreement, inspection-agreement, route, condemnation, protection, stock, and condition locks.
- Protective Aid retains own-core, allied-core, trauma, supplier-stock, factory-availability, target-control, emergency, and occupied-gap behavior.
- The probability MCP source inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90e6cec54c61f6583a9735e0c391f34f6c4a78d521825d9ec15e47ef711ce00d/a13cdb61a5b5f0d90b3fd33ad1d111a707aa7b9ebc9917935e7176612694e140/probability-inspect-ed5007c16b10.json` with source discovery status `PROBABILITY_SOURCE_INSPECTED`, six decision-AI candidates, `poolComplete = false`, and three state-targeted candidates reported as `CANDIDATE_NOT_FOUND` by the adapter.
- No probability comparison was run because no AI weight patch was made.

## Localisation and tooltip gaps

- `cbrn_nerve_suppression_operation_cost` at `localisation/english/cbrn_occupation_l_english.yml:19` is a seven-component literal resource-name string and cannot be made truthful by changing only the sale percentage.
- Its blocked string at `:20` is broad prose rather than a component-specific blocked reason.
- Its tooltip at `:21` describes reserves but not a quoted sale amount and cannot safely promise release-time payment behavior until the owner transaction exists.
- Protective Aid requirements and completion tooltips describe the factory and dynamic respirator behavior, but no pre-release exact equipment quote exists.
- No localisation was changed, so no new key mismatch was introduced.

## Cleanup and exploit-risk notes

- The present nerve execution path directly debits payload and then the six operation resources at `common/scripted_effects/cbrn_occupation_effects.txt:321-357`; it has no receipt to refund after a downstream dispatch failure.
- A future adapter must not debit payload before all component affordability checks pass.
- A future adapter must not refund ordinary or quoted amounts; it must refund the stored actual paid amount per component and settle exactly once after the chemical action or aid delivery is irreversible.
- A future adapter must preserve `cbrn_occupation_clear_transient_action_inputs` and all existing state flags; transaction scratch must not become persistent CBRN state.
- No exploit-prone partial adapter was introduced.

## Concrete recommended follow-up

1. Assign a parent-approved CBRN cost design before reopening this tranche. The design must either reduce each nerve action to at most four real spendable types without deleting the intended protection package, or add a supported bundled-resource contract and icon outside this owner write set.
2. Add a dry-run or quote-only path to the CBRN distribution owner that returns the exact concrete respirator components and amounts without debit. This must include target population, state infrastructure, occupation multiplier, supplier modifiers, filter condition, model ordering, and reserve floors.
3. Add a shared factory-commitment reservation/credit contract before adapting Protective Aid. The contract must preserve the engine project reservation, save/reload state, cancellation, timeout, and exact commitment count.
4. Once the exact-state nerve condition hook is verified, adapt the delayed release path with one transaction id per logical action, one component row per real spendable component, all-component preflight, owner-specific custom-equipment debit/credit, actual-paid receipts, one primary achievement family, and a single settlement or refund path.
5. Re-run the decision/mission auditor and probability auditor after a future gameplay patch. The current probability source inspection is baseline evidence only.
6. Re-run `hoi4.gui_inspect` and `hoi4.gui_render` for `cbrn_occupation_measures_category` after the MCP timeout is resolved; the required calls timed out and provide no visual evidence.

## Validation performed and skipped

Performed:

- Read `AGENTS.md`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` in full.
- Read the full Event 026 specification package under `docs/specs/026_black_friday_specs/`.
- Consulted the required offline Paradox wiki pages, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI Modding.
- Consulted the installed Vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including decision cost/custom-cost behavior, script constants, triggers, effects, modifiers, variables, event targets, and text icons.
- Inspected every declaration and owner callsite in the assigned CBRN occupation decision, constants, effects, triggers, and localisation files.
- Confirmed the existing Event 026 native sale ideas contain `political_power_cost` factors and that the shared scripted payment helper lacks factory commitment and arbitrary concrete CBRN equipment branches.
- Ran the read-only probability source discovery and inspection route described above.
- Attempted the mandatory read-only `hoi4.gui_inspect` for `windowName = decision_category` and `scenario.id = cbrn_occupation_measures_category`; it timed out after 180 seconds.
- Attempted the mandatory read-only `hoi4.gui_render` for the same category at 1920x1080 with normal, disabled, and long-text states; it timed out after 180 seconds.
- Confirmed the assigned gameplay files had no pre-existing diff before writing this handoff and that the only new file is the handoff itself.

Skipped:

- No source gameplay patch was attempted because the blockers above make a complete, truthful, four-or-fewer-component adapter unsafe.
- No probability compare was run because no AI weight or candidate rule changed.
- No live game, save/reload, tooltip, refund, multiplayer, or achievement proof was run or claimed.
- No shared Event 026 or universal-cost file was edited.

## Remaining blockers and completion statement

This tranche is explicitly incomplete as a gameplay integration and is rejected for implementation under the current contract.

The parent should not claim CBRN occupation cost coverage from this handoff.

The native political-power rows have a shared Strategy A source path but no owner-level receipt/refund evidence; the custom nerve rows are currently hidden by the fail-closed condition hook and have an over-budget seven-component payment; Protective Aid is reachable but requires a dry-run distribution quote and a factory-commitment transaction contract.

No simplification or fallback was used.
