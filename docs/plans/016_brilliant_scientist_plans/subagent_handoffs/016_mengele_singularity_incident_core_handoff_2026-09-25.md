# Event 016 Private Singularity Incident Core Handoff

## Scope and acceptance basis

The parent assigned this bounded deterministic Singularity component incident core and retained native reward callbacks, recovery decision wiring, cleanup integration, the research gate, and the weighted dispatcher.
The accepted boundaries come from `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md` and `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` as identified in the parent assignment.
This handoff records implementation evidence for this slice only and does not claim completion of the Event 016 portfolio.

## Files changed

- `common/scripted_effects/016_mengele_singularity_incident_effects.txt` adds deterministic record, clear, exact direct-cost begin/cancel/finish, and cleanup effects.
- `common/scripted_triggers/016_mengele_singularity_incident_triggers.txt` adds strict provider, Prototype selector, incident, receipt, admission, and callback predicates.
- `common/dynamic_modifiers/016_mengele_singularity_incident_modifiers.txt` adds one private command-power and stability penalty modifier.
- `common/scripted_effects/016_mengele_singularity_incident_effects.md` documents every helper, state field, cost axis, and parent call site.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_singularity_incident_core_handoff_2026-09-25.md` records implementation, validation, and follow-up ownership.

No other source, decision, localisation, native project, stage helper, constant, or random weight was edited by this subagent.
No commit was created.

## Helper map and call sites

The country-scoped recording API is `brilliant_scientist_mengele_record_singularity_incident`, with temporary `mengele_event016_requested_stage` fixed to Prototype and strict `brilliant_scientist_mengele_singularity_incident_provider_is_valid` authorization.
It returns temporary `mengele_event016_singularity_incident_recorded`, creates one active private incident, increments permanent incident history once per new incident, and adds `brilliant_scientist_mengele_singularity_incident` only when absent.
The intended call site is the future parent-owned `brilliant_scientist_mengele_dispatch_singularity_incident` after each authenticated native risky reward outcome.
The strict stage trigger is `brilliant_scientist_mengele_singularity_incident_stage_is_valid`, and the active incident trigger is `brilliant_scientist_mengele_singularity_incident_is_active`.

The recovery admission APIs are `brilliant_scientist_mengele_singularity_incident_recovery_can_pay_direct_costs`, `brilliant_scientist_mengele_singularity_incident_recovery_can_pay`, `brilliant_scientist_mengele_singularity_incident_recovery_can_start`, and `brilliant_scientist_mengele_singularity_incident_recovery_can_debit`.
The future native decision must use `recovery_can_start` for availability, `recovery_can_pay` for four-burden cost presentation, and `recovery_can_debit` indirectly through its begin effect after the native factory reservation may have started.
The receipt predicates are `brilliant_scientist_mengele_singularity_incident_recovery_is_active` and `brilliant_scientist_mengele_singularity_incident_recovery_receipt_is_current`.
The transaction APIs are `brilliant_scientist_mengele_begin_singularity_incident_recovery`, `brilliant_scientist_mengele_cancel_singularity_incident_recovery`, and `brilliant_scientist_mengele_finish_singularity_incident_recovery`, returning temporary started, cancelled, and finished results respectively.
The native decision's `complete_effect`, `cancel_effect`, and `remove_effect` should call those APIs in that order of roles.
`brilliant_scientist_mengele_clear_singularity_incident` removes only the transient flag and modifier, while `brilliant_scientist_mengele_cleanup_singularity_incident` refunds a complete unsettled receipt before clearing the transient incident.
The parent should call cleanup before broader provider teardown and review native decision removal ordering.

## Constants, state, and cleanup

The existing technical response constants supply 60 days, two civilian factories, 35 Political Power, 300 Support Equipment, and 500 fuel, with no new tuning table or constants.
The native decision must own the two-factory reservation and its release, while the helper stores and debits only the three direct costs.
The private penalty reuses the established Singularity values `brilliant_scientist_project_modifier.accident_penalty_major` for `command_power_gain` and `.accident_penalty_standard` for `stability_factor`.
Transient country state is `mengele_event016_singularity_incident_active`, `mengele_event016_singularity_incident_recovery_active`, and the three `mengele_event016_singularity_incident_recovery_cost_*` variables.
Permanent country state is `mengele_event016_singularity_incident_history`, `mengele_event016_singularity_incident_history_count`, `mengele_event016_singularity_recovery_history`, and `mengele_event016_singularity_recovery_history_count`.
Cancellation snapshots a complete receipt, clears it before refunding, and retires malformed orphan fields without fabricating a refund.
Successful completion consumes the receipt and clears the penalty before permanent recovery history increments.
Repeated cancellation or cleanup cannot refund a settled receipt, and no event target is needed for this country-local transaction.
Cleanup retains learned knowledge, native project completion, the six-component ledger, provider stages, incident history, and recovery history.

## Migration and parent integration

The six risky reward options in `common/special_projects/projects/016_brilliant_scientist_projects.txt` currently call the Kruger pressure and accident helpers, while the six native project outputs register their components through the existing component adapter.
The parent must authenticate each actual risky reward and route its Mengele provider branch to the future audited dispatcher while preserving the Kruger branch for Kruger providers.
The parent must set the private Prototype selector at that boundary and clear it after dispatch, without reading or modifying the component ledger in this incident core.
The parent must add one native recovery decision with admission, cost presentation, duration, factory reservation, begin, cancel, and finish wiring plus player-facing localisation for the new penalty and decision.
The parent must add `brilliant_scientist_mengele_cleanup_singularity_incident` to provider closure, defeat, and terminal teardown paths before provider identity is invalidated.
The parent owns a dedicated probability baseline audit and compare through `chaosx_ai_probability_auditor` before implementing `brilliant_scientist_mengele_dispatch_singularity_incident` or changing any random weight.
Factory release, native callback scope, and potential cancellation/finish ordering remain integration risks until the decision and callback owner validates them.

## References and validation

The required eleven offline Paradox wiki core pages, their decision, idea, and special-project sections, the relevant vanilla documentation, and a vanilla dynamic-modifier precedent were consulted before editing.
The existing computation incident effect, trigger, modifier, and documentation files and the shared dynamic-helper registry were inspected before designing this owner-local core.
A task-specific source check confirmed the Prototype-only selector, strict provider delegation, three-cost receipt, clear-before-refund order, established Singularity penalty fields, absence of the dispatcher, and absence of writes to foreign project or component fields.
No game launch or live engine test was performed, and no decision timer or callback was executed because those call sites remain parent-owned.
The required read-only `hoi4.event_inspect` roots request timed out after 180 seconds, and a second focused trace request for `{kind:event,eventId:chaosx.nr16.1}` with depth one also timed out after 180 seconds.
Neither MCP request returned a revision, diagnostic artifact, or coverage result, so source review does not substitute for event-route evidence.

## Simplifications, omissions, and blockers

The weighted dispatcher and `random_list` are intentionally absent pending the independent probability baseline and owner patch/compare cycle.
The recovery decision, localisation, risky callbacks, and program cleanup call sites remain parent integration work under the assigned ownership boundary.
The exact MCP event inspection blocker is `timed out awaiting tools/call after 180s` for both read-only requests, and no artifact reference was returned.
The deterministic helper core is ready for parent review, while end-to-end Singularity incident behavior remains incomplete until the parent wires and validates those surfaces.
