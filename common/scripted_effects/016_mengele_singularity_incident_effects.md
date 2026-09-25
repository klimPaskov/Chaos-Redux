# Event 016 Private Mengele Singularity Incident Core

## Purpose and boundary

This owner-local core tests an authenticated native risky reward for a private Singularity component incident and manages one exact technical recovery receipt.
It does not authenticate a particular component, alter the six-component registry, or settle any project stage.
The strict provider trigger delegates to `brilliant_scientist_mengele_project_stage_provider_is_valid`, and the incident selector accepts only `constant:brilliant_scientist_project_stage.prototype` in temporary `mengele_event016_requested_stage`.
The native risky reward callback and component proof remain parent-owned.

## Helper and trigger map

| API | Scope and inputs | Outputs | Side effects and intended call site |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_dispatch_singularity_incident` | Country scope; actual native risky reward, valid provider, temporary Prototype selector, no active incident or recovery. | Temporary `mengele_event016_singularity_incident_dispatched`. | Uses the existing Prototype capacity and accident factor to build a clamped private pressure and its safe complement; the six native risky options call this instead of Kruger's accident dispatcher. |
| `brilliant_scientist_mengele_singularity_incident_provider_is_valid` | Country scope; existing strict provider state. | Boolean trigger. | Delegates to the stage provider gate; native callback, record, recovery, and modifier. |
| `brilliant_scientist_mengele_singularity_incident_stage_is_valid` | Country scope; temporary `mengele_event016_requested_stage`. | Boolean trigger true only for Prototype. | None; record helper. |
| `brilliant_scientist_mengele_singularity_incident_is_active` | Country scope; private active flag. | Boolean trigger. | None; recovery and modifier. |
| `brilliant_scientist_mengele_singularity_incident_recovery_is_active` | Country scope; private active flag and all three direct-cost variables. | Boolean trigger for a complete receipt. | None; cancel and finish. |
| `brilliant_scientist_mengele_singularity_incident_recovery_can_pay_direct_costs` | Country scope; Political Power, Support Equipment, and fuel. | Inclusive affordability trigger. | None; admission and callback recheck. |
| `brilliant_scientist_mengele_singularity_incident_recovery_can_pay` | Country scope; direct costs and free civilian factories. | Four-axis affordability trigger. | None; native decision cost presentation. |
| `brilliant_scientist_mengele_singularity_incident_recovery_can_start` | Country scope; incident, provider, empty receipt, direct costs, and free civilian factories. | Admission trigger. | None; native decision visibility or availability. |
| `brilliant_scientist_mengele_singularity_incident_recovery_can_debit` | Country scope; incident, provider, empty receipt, and direct costs. | Completion-callback trigger. | Excludes the factory recheck because the native decision may have already reserved them. |
| `brilliant_scientist_mengele_singularity_incident_recovery_receipt_is_current` | Country scope; complete private receipt. | Callback guard. | None; cancel and finish. |
| `brilliant_scientist_mengele_record_singularity_incident` | Country scope; authenticated risky Prototype outcome, valid provider, no active private incident or recovery. | Temporary `mengele_event016_singularity_incident_recorded`. | Sets private active flag, permanent incident flag/count, and private penalty modifier; called by the private random-list branch. |
| `brilliant_scientist_mengele_clear_singularity_incident` | Country scope; no selector. | None. | Removes private active flag and penalty modifier; recovery success and cleanup. |
| `brilliant_scientist_mengele_begin_singularity_incident_recovery` | Country scope; native decision completion callback after admission. | Temporary `mengele_event016_singularity_incident_recovery_started`. | Debits and receipts three direct costs once; future recovery decision. |
| `brilliant_scientist_mengele_cancel_singularity_incident_recovery` | Country scope; exact active receipt when present. | Temporary `mengele_event016_singularity_incident_recovery_cancelled`. | Clears receipt before refund once, retires malformed orphan fields without inferred refund, and clears the incident if provider is invalid; native decision cancellation and parent cleanup. |
| `brilliant_scientist_mengele_finish_singularity_incident_recovery` | Country scope; complete receipt, active incident, valid provider. | Temporary `mengele_event016_singularity_incident_recovery_finished`. | Consumes receipt, removes penalty, and increments permanent recovery history once; native decision timer completion. |
| `brilliant_scientist_mengele_cleanup_singularity_incident` | Country scope; no selector. | None. | Cancels exact direct receipt, removes the active native decision to release its factory reservation, and clears transient incident state; parent program and terminal cleanup. |

## Constants and tuning

The existing `brilliant_scientist_project_board.response_technical_*` constants supply 60 days, two civilian factories, 35 Political Power, 300 Support Equipment, and 500 fuel.
The native recovery decision owns the duration and temporary civilian-factory reservation, while this core receipts and debits only the three direct resources.
The private Prototype pressure is `constant:brilliant_scientist_project_board.capacity_prototype` multiplied by `constant:brilliant_scientist_accident.prototype_stage_factor`, clamped between the existing accident minimum and maximum.
The companion safe weight is the maximum minus the private pressure, so the two `random_list` entries preserve a complete 0–100 pool.
The private modifier uses `brilliant_scientist_project_modifier.accident_penalty_major` for command power gain and `brilliant_scientist_project_modifier.accident_penalty_standard` for stability, matching the existing Singularity incident penalty.
The temporary results use the existing `brilliant_scientist_value.zero` and `.one` constants, and payment sign uses `brilliant_scientist_directorate_value.negative_one`.
No new constant category or weighted table belongs in this deterministic tranche.

## State, cleanup, and migration

Transient state is `mengele_event016_singularity_incident_active`, `mengele_event016_singularity_incident_recovery_active`, and the three `mengele_event016_singularity_incident_recovery_cost_*` variables.
Permanent state is `mengele_event016_singularity_incident_history`, `mengele_event016_singularity_incident_history_count`, `mengele_event016_singularity_recovery_history`, and `mengele_event016_singularity_recovery_history_count`.
No event target is needed because the incident, direct receipt, and native decision lifecycle remain in country scope.
Each of the six native risky component rewards sets the private Prototype selector, calls `brilliant_scientist_mengele_dispatch_singularity_incident`, then clears the selector; the Kruger branch retains its original pressure and incident path.
`mengele_event016_singularity_incident_recovery` uses the four-axis admission trigger, direct-debit begin effect, cancellation effect, finish effect, two-factory reservation, and 60-day timer.
`brilliant_scientist_mengele_cleanup_provider_receipts` calls private incident cleanup before invalidating the provider, and cleanup removes the native decision after settling direct costs so its factory reservation ends.
Vanilla `documentation/effects_documentation.md` specifies that `remove_decision` does not run the decision's `remove_effect`, so cleanup settles the direct receipt explicitly before that removal.
Cleanup preserves learned technology, permanent incident/recovery history, native project history, and the existing component registry.

## Limitations and validation

The independent probability baseline for the former shared dispatcher is recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_singularity_accident_probability_baseline_2026-09-25.md`.
The same-scenario post-change comparison and event inspection are separate validation gates and must be reported from their actual MCP results.
Player-facing recovery and penalty localisation lives in `localisation/english/016_mengele_singularity_incident_l_english.yml`.
The original deterministic-core source review and event-inspection timeout are recorded in the matching subagent handoff.
No game launch or live runtime validation was performed.
