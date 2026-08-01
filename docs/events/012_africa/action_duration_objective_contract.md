# Event 012 action duration and objective contract

## Purpose

The 102-row action matrix keeps one of the four existing shared targeted missions for engine and UI stability, but each action now carries its own matrix duration range, nominal day value, and objective class. The shared duration band remains only the mission routing key.

## Runtime contract

`africa_prepare_action_contract` runs at the end of `africa_prepare_action_profile` and reads the requested action ID. It writes temporary profile fields for the minimum duration, maximum duration, nominal duration, response window, and objective class. `africa_requote_selected_action_against_action_target` copies those fields into the normal quote snapshot so the launch revalidation and payment path use the same immutable values.

`africa_create_action_record` copies the quote snapshot to the selected target as `africa_active_action_duration_minimum`, `africa_active_action_duration_maximum`, `africa_active_action_duration_days`, `africa_active_action_response_days`, and `africa_active_action_objective`. The target also records `africa_active_action_started_at_war` before the mission begins. The existing `africa_action_record_active` gate prevents a second record for the same target, so a later quote cannot overwrite a live mission's timer.

The four targeted missions read `FROM.africa_active_action_duration_days`. The decision target is the `FROM` scope for a targeted decision, while vanilla confirms country-scoped mission-timer variables; this exact `FROM` timer form still requires runtime parser confirmation. It avoids `add_days_mission_timeout`, which has no target argument and would modify the wrong record when several target missions share one ID. Offer-response actions delay the existing `chaosx.nr12.210` event by the target's `africa_active_action_response_days` value.

## Objective classes

`peace_or_timeout` completes an active action when a target that was already at war reaches peace. It is used for the aid corridor, volunteer deployment, and blockade rows. `war_preparation` completes the intervention preparation when the target is at war with the executing host. `response_window` marks the eight existing offer-response rows; those rows resolve through the delayed response event, while the mission timeout remains the refusal path. All other rows use `none`, so their existing timeout, event, or result kernels remain authoritative until a narrower external success predicate exists.

`africa_action_contract_should_cancel` handles target capitulation or loss of scope and routes through the existing cancellation cleanup. Event-active and generation guards remain in each mission's current cancel trigger.

## Inputs, outputs, and side effects

- Input: temporary `africa_requested_action_id` plus the existing profile duration band and kernel.
- Quote outputs: `africa_quote_duration_minimum`, `africa_quote_duration_maximum`, `africa_quote_duration_days`, `africa_quote_response_days`, and `africa_quote_objective`.
- Target outputs: the corresponding `africa_active_action_*` variables and `africa_active_action_started_at_war`.
- Side effects: mission activation uses the target duration; response events are delayed; cleanup clears every new target variable along with the existing mission flags and arrays.
- No world-wide on-action, new currency, asset, event ID, target array, or parallel mission family is introduced.

## Tuning and validation

The `africa_action_contract` script-constant category stores every matrix row's minimum, maximum, nominal, and objective values. Nominal values are deterministic midpoint values for bounded ranges; the two qualitative rows use explicit 365-day annual review and 720-day multi-year defaults. The two-continent union records its 360-to-900-day preparation window, then settles immediately when that preparation mission resolves.

Static validation confirms 102 profile dispatch blocks, 102 duration contracts, and no `var:FROM` mission or response syntax. Vanilla precedents reviewed for country-scoped mission timers are `ETH.ETH_war_escalation_length`, `SOV.SOV_operation_countenance_mission_days`, and `CHI.CHI_holding_state_mission_time_var`; none is an exact `FROM` targeted-mission timer. Live engine behavior, save migration, and UI rendering remain parent-owned and are not claimed here.

## Future extension

Rows that need recurring annual review, multi-stage formation checkpoints, or project-specific completion predicates can add a new objective enum and a narrow external setter without changing the shared quote, revalidation, outcome, or cleanup kernels. A future change should preserve the per-target timer snapshot and same-target active-record gate.
