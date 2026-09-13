# Event 016 containment parameter syntax repair plan and implementation handoff

Disposition: implemented, with engine validation limits below.
Acceptance basis: on 2026-09-05 the parent reviewed this complete plan and explicitly accepted pure trigger comparisons, NOT/AND grouping, preserved eight affordability wrappers, and immediately initialized begin/cancel temporary inputs within the user's safe Event 016 error-repair authorization.
The assignment began as read-only design; the parent subsequently instructed implementation in the three named gameplay files plus this plan and handoff evidence.
No files were staged or committed, and no game, desktop, or process operation was performed.

## Finding and recommendation

The supplied launch_07 error log reports invalid `ACTION`, `POLITICAL_POWER`, and `STABILITY` tokens at the containment decision call sites, including lines 18 and 42–44.
The five affected helpers expect `$ACTION$`, `$POLITICAL_POWER$`, or `$STABILITY$` substitution, but their callers are parsed as ordinary trigger/effect blocks.
Use boolean scripted-helper calls, pure action-specific comparisons in decision triggers, and immediately initialized temporary inputs for effect helpers.
Keep all existing action constants, inclusive affordability checks, costs, recipient checks, route flags, timing, modifiers, tooltips, AI blocks, settlement functions, and cancellation behavior.

The initial parent assertion that temporary setters cannot appear in triggers was corrected during this task.
Installed `documentation/triggers_documentation.md:7482` explicitly documents `set_temp_variable` in any scope, and installed `common/scripted_triggers/GER_scripted_triggers.txt:152–153` uses it.
Consequently, temporary-input trigger helpers are supported in principle, provided every invocation initializes inputs and negation wraps an explicit conjunction.
They are not recommended for this narrow repair: two affordability setters replace two comparisons without reducing duplication, while action setters replace one literal comparison and create additional evaluation-order and scratch-variable dependencies.
Pure comparisons are the shorter, lower-risk implementation here; this recommendation does not claim that trigger setters are unsupported.

## Exact helper map and edits

All helpers below retain COUNTRY scope.

| Helper | Inputs and output | Proposed change and side effects | Consumers |
| --- | --- | --- | --- |
| `brilliant_scientist_containment_action_is_visible` | No inputs; common visibility boolean | Remove only its final action-selection OR block; retain current host, incomplete resolution, no world end, and deadline/request checks; no mutation | Eight decision visible blocks add their own action-selection OR |
| `brilliant_scientist_containment_action_is_live` | No inputs; common live-action boolean | Remove only the `$ACTION$` equality; retain current host, no world end, incomplete resolution, and in-progress checks; no mutation | Sixteen decision cancel/remove trigger uses add exact action equality |
| `brilliant_scientist_can_pay_containment_base` | Removed after migration | Replace its eight calls with the exact PP and stability comparisons inside the existing per-action predicates, then delete its unused declaration | Only eight per-action affordability predicates |
| `brilliant_scientist_can_pay_containment_<action>` | No inputs; inclusive affordability boolean | Keep each existing name and material/command gate; use literal references to that action's shared PP/stability constants; no mutation | Existing available and custom_cost_trigger calls remain boolean and unchanged |
| `brilliant_scientist_begin_containment_action` | Required temps `brilliant_scientist_containment_action`, `brilliant_scientist_containment_political_power_cost`, `brilliant_scientist_containment_stability_cost`; no defaults | Replace three dollar-parameter reads with these temps; retain receipt flag, active-action variable, start date, payment scratch calculation and debits in identical order | Eight complete_effect blocks initialize all three temps immediately before `= yes` |
| `brilliant_scientist_cancel_containment_action` | Required temp `brilliant_scientist_containment_action`; no default | Replace `$ACTION$` read with that temp; retain equality guard, lock removal, and receipt removal; no refund and no new persistent state | Eight cancel_effect blocks initialize the action temp immediately before `= yes` |

Update comments on the four retained shared helpers to document the new contract and the mandatory caller-owned action check.
Document the event-owned temporary-input API in the matching owner documentation or this QA handoff, and link it from the existing owner API index only if that index currently points at stale contract documentation.
Do not move Event 016 helpers into the shared dynamic-effect registry.

### Trigger call templates

For each decision, replace its current parameterized visible call with the following, substituting its own action constant for `release` and leaving additional row-specific conditions in place:

```txt
brilliant_scientist_containment_action_is_visible = yes
OR = {
	NOT = { has_country_flag = brilliant_scientist_containment_action_in_progress }
	check_variable = { brilliant_scientist_active_containment_action = constant:brilliant_scientist_containment_action.release }
}
```

Replace each parameterized live call in remove_effect.limit with this conjunction:

```txt
brilliant_scientist_containment_action_is_live = yes
check_variable = { brilliant_scientist_active_containment_action = constant:brilliant_scientist_containment_action.release }
```

Replace each negated live call inside cancel_trigger.custom_trigger_tooltip with exactly this grouping:

```txt
NOT = {
	AND = {
		brilliant_scientist_containment_action_is_live = yes
		check_variable = { brilliant_scientist_active_containment_action = constant:brilliant_scientist_containment_action.release }
	}
}
```

Do not place the two conditions directly inside NOT, because Clausewitz NOT with multiple children does not express the intended negation of their conjunction.
Keep `cancel_if_not_visible = no` and the current interruption tooltip wrapper.

Within each existing per-action payment predicate, replace its base-helper block with:

```txt
check_variable = { var = political_power value = constant:brilliant_scientist_containment_cost.release_political_power compare = greater_than_or_equals }
check_variable = { var = stability value = constant:brilliant_scientist_containment_cost.release_stability compare = greater_than_or_equals }
```

Use the original action-specific constants; preserve all additional equipment or command-power comparisons verbatim.

### Effect call templates

Inside the existing hidden_effect at decision selection:

```txt
set_temp_variable = { brilliant_scientist_containment_action = constant:brilliant_scientist_containment_action.release }
set_temp_variable = { brilliant_scientist_containment_political_power_cost = constant:brilliant_scientist_containment_cost.release_political_power }
set_temp_variable = { brilliant_scientist_containment_stability_cost = constant:brilliant_scientist_containment_cost.release_stability }
brilliant_scientist_begin_containment_action = yes
```

The begin helper stores `brilliant_scientist_containment_action` into the existing persistent receipt and copies the two positive cost temps into the existing `brilliant_scientist_containment_payment` scratch value before the existing negative-one multiplication and debit.
All material debits remain after that call, and military seizure's war-support effect stays in its current location.

Each cancel_effect becomes:

```txt
cancel_effect = {
	set_temp_variable = { brilliant_scientist_containment_action = constant:brilliant_scientist_containment_action.release }
	brilliant_scientist_cancel_containment_action = yes
}
```

The existing remove_effect action-temp initialization and resolver call remain unchanged after the repaired live-action limit.
Do not add defaults, refunds, new start guards, or timestamp cleanup as part of this syntax repair.

## Complete action mapping

All listed cost prefixes belong to `constant:brilliant_scientist_containment_cost`, and action values belong to `constant:brilliant_scientist_containment_action`.

| Decision ID | Action and PP/stability prefix | Additional payment gate/debit retained |
| --- | --- | --- |
| `brilliant_scientist_release_kruger` | `release` | None |
| `brilliant_scientist_exile_kruger` | `exile` | `exile_convoy_gate` / `exile_convoy_spend`, convoy_1 |
| `brilliant_scientist_arrest_kruger` | `arrest` | `arrest_support_gate` / `arrest_support_spend`, support_equipment |
| `brilliant_scientist_shutdown_directorate` | `shutdown` | `shutdown_truck_gate` / `shutdown_truck_spend`, motorized_equipment |
| `brilliant_scientist_ratify_sovereign_charter` | `charter` | `charter_support_gate` / `charter_support_spend`, support_equipment |
| `brilliant_scientist_launch_military_seizure` | `military_seizure` | `seizure_infantry_gate` / `seizure_infantry_spend`, infantry_equipment |
| `brilliant_scientist_request_foreign_containment` | `foreign_containment` | `foreign_command_power_gate` / `foreign_command_power_spend`, command power |
| `brilliant_scientist_concede_institutional_authority` | `concession` | `concession_support_gate` / `concession_support_spend`, support_equipment |

## Tuning, event targets, cleanup, and migration

No constants or balance targets are added or changed.
No event target is added or removed; exile recipient checks remain unchanged.
Temporary inputs are initialized immediately at every effect call, are unscoped, and do not introduce persisted state.
Existing finish/reopen cleanup and cancellation receipt equality remain unchanged.
Cancellation of a stale timer cannot clear a newer action receipt; removal cannot settle a different action.
This preserves existing receipt idempotence; it does not claim the begin effect itself becomes safe for arbitrary repeated external calls.

The implementation touches only `common/decisions/016_brilliant_scientist_containment_decisions.txt`, `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`, and `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`, plus narrowly required owner contract documentation.
Repository-wide searches of runtime TXT/GUI/GFX files found all consumers of these five helpers in those three files only.
Migrate all 8 visibility calls, 16 live calls, 8 base payment calls, 8 begin calls, and 8 cancel calls atomically, then remove the obsolete base helper.

## Evidence and meaningful validation

Required offline wiki core pages were consulted, particularly Effects:1270 scripted effects and Triggers:1003 scripted triggers, which document boolean helper calls.
Installed vanilla `documentation/script_concept_documentation.md` Script Constants and `common/script_constants/documentation.md` confirm scoped-variable constant access.
Installed effects documentation was consulted for temporary variable assignment, multiplication, political-power and stability effects, and triggers documentation for temporary variable assignment.
Existing `common/scripted_effects/chaosx_dynamic_effects.txt` and its matching markdown establish the project's immediately initialized temporary-input effect convention and event-owned helper boundary.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents; none changed.

MCP event trace for `chaosx.nr16.1`, depth 1, 12 nodes, and 20 edges returned `EVENT_INSPECTED_PARTIAL`, focused analysis, revision `4520c3ceb2ac2ff2148d4a7228cd8878f66ba12464a692526456f94fa064899f`.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b983968e6122ff7ab086a4a2454c3e87d89a1e0a223554bb3907d48167f6a728/986d56f837e73cd6982ac4092f667d5cec8178330f3114518157ab74bd9aaeb6/event-trace-4520c3ceb2ac.json`.
Because focused analysis deferred helper projections and lifecycle passes, a full-analysis state_flow call followed with the same event selector and narrow bounds.
It returned `EVENT_INSPECTED`, full analysis, 19,112 indexed helpers, revision `95690b83dbc974ecf7dc8386de220deefae81d2c8f862910662071ef27f03cb9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ac392107f083c98b34904472a57cebe6865ab70a672419e1da8b7e62cfa1036/00348f99f68a15d8db9d480a08516daeaf50ec5c87419c596cf6f3dc65c5205b/event-state_flow-95690b83dbc9.json`.
The full analyzer reports 3,918 blocking diagnostics across its indexed graph; this is not a passing lifecycle certificate, and the full artifact has not been exhaustively reviewed for this bounded proposal.
No MCP route was unavailable; two initial selector-schema errors were corrected before the successful calls.

Parent implementation validation should compare each migrated literal constant against its original argument, verify all eight affordability predicates still serve both selection and cost display, and compare every untouched additional gate and debit.
Use a source-level truth table for open board/no action, matching active action, different active action, completed resolution, host loss, and world end.
Check cancel and remove separately: a mismatched receipt must trigger cancellation without clearing the current receipt, and must prevent resolution.
Check affordability exactly at, just below, and above each PP/stability/material threshold.
Check that each complete_effect initializes all inputs and debits each payment once, and that a second cancel against a cleared receipt cannot restore or debit anything.
AI weights and weighted predicates are unchanged by this design; a probability audit is outside this syntax-only proposal.
Post-patch evidence and static checks are recorded below; no in-game execution, desktop operation, process operation, staging, or commit was performed.

## Simplifications, omissions, and blockers

No gameplay simplification is proposed.
The source syntax repair is implemented and source-validated; engine acceptance remains unverified.
Pure predicate factoring deliberately duplicates only one action comparison per consumer and two constant checks per action; it preserves shared lifecycle logic and action affordability wrappers.
MCP evidence remains diagnostic and does not establish engine acceptance of the proposed patch.

## Implementation handoff, 2026-09-05

Changed gameplay files are exactly the three files listed in the migration section.
The accepted eight visibility calls, sixteen live checks, eight payment-base calls, eight begin calls, and eight cancel calls were migrated.
The unused parameterized affordability base was removed, and retained helper comments document their input, output, caller requirements, and side effects.
All eight existing affordability wrappers remain shared by selection and custom-cost display.
No constants, localisation, assets, AI weights, payment amounts, additional gates, material debits, timers, modifiers, resolver functions, event targets, or cleanup semantics were changed.
The concurrent exile-recipient work, including the existing clear_temp_variable line, was preserved.

Before editing, the current diff was reviewed and all three original byte sequences were archived under `pre_patch_containment/common/` with their original relative paths.
The implementation refused to overwrite the files if their bytes changed between snapshot and write.
`containment_parameter_repair_validation.json` records before/after SHA256 values and the exact eight action/PP/stability mappings.
`containment_parameter_repair.diff` records only this worker's changes against those immediately preceding originals, excluding the concurrent exile-recipient changes.

The source-level evaluator compared the intended parameter-substituted original predicates with the actual repaired predicates for 9,216 cases covering host status, completed resolution, world end, active deadline/request, in-progress status, all nine receipt values, and enabled/disabled row-specific conditions.
All 27,648 visibility, cancel-trigger, and remove-limit comparisons matched.
All 198 affordability cases at, just below, and just above the actual PP, stability, and material/command thresholds matched the original intended comparisons and inclusive-gate expectations.
All 72 action/receipt cancellation pairs preserved mismatched receipts and made repeated cancellation inert after matching receipt removal.
Structural comparisons verified every unchanged decision field, every additional debit, military seizure's war-support effect, immediate begin input initialization, cancel input initialization, and every unrelated effect body against the archived originals.
These are source-level checks of intended behavior; the invalid original parameter syntax itself cannot serve as a working engine baseline.

The refreshed post-patch narrow MCP trace returned `EVENT_INSPECTED_PARTIAL`, focused analysis, with the same direct-event revision `4520c3ceb2ac2ff2148d4a7228cd8878f66ba12464a692526456f94fa064899f` and graph hash `5e3d139e6f05e68b3a6113d31899826893cdcd622d7328cf49b05b1daa10c66f`.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/854073bd34561e387b1f3c4b3bbde2b42a3e7871c0bc94a198fd08abad3453da/98bcdef1a7e2aaab028a4db0cf7e0cdacbc1357a6395e68cdf3ec205235a549f/event-trace-4520c3ceb2ac.json`.
The unchanged direct-event graph is expected because the edited helpers and decisions are excluded from focused analysis; it does not validate these changes.
The parent explicitly limited post-patch MCP work to narrow evidence, so another full workspace helper expansion was not requested.
A read-only comparison using the reported focused revision on both sides returned `EVENT_REVISION_NOT_CACHED`: "Requested event graph revision is not cached".
The first compare request included an unsupported `kind` field; after removing that field, the request reached the service and produced the exact cache blocker above.
No compare artifact was produced, and no focused comparison is claimed as helper validation.

Residual issue: `common/scripted_effects/016_brilliant_scientist_containment_effects.txt:63` retains `clear_temp_variable = brilliant_scientist_containment_exile_recipient_preserved`, which the parent explicitly excluded from this repair pending supported cleanup analysis.
The confirmed ACTION/POLITICAL_POWER/STABILITY parameter constructs no longer occur in the three repaired files, but disappearance of their launch-time diagnostic cascade has not been verified by game execution.
No fallback or gameplay simplification was used.

## Launch_08 static hint follow-up

The eight same-value ai_hint_pp_cost compatibility aliases are implemented and documented in [containment_hint_repair_addendum.md](containment_hint_repair_addendum.md), with immediate-byte backup and validation evidence.
