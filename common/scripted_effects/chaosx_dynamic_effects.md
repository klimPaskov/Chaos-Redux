# chaosx_dynamic_effects

This registry documents the public helpers declared in `common/scripted_effects/chaosx_dynamic_effects.txt` and the shared gateways identified below. It is limited to reusable contracts with callers across multiple systems or event families.

Event-owned orchestration, validation, adapters, and lifecycle helpers belong in their owning source file and reference document. The owner index below keeps those APIs discoverable without copying their contracts into this registry.

## table_of_contents

- [calculate_economy_scaled_factory_grant](#calculate_economy_scaled_factory_grant)
- [damage_state_building_dynamic](#damage_state_building_dynamic)
- [damage_buildings_in_random_states](#damage_buildings_in_random_states)
- [get_random_sea_region](#get_random_sea_region)
- [clear_special_chaos_country_civilian_effects](#clear_special_chaos_country_civilian_effects)
- [refresh_world_threat_state](#refresh_world_threat_state)
- [union_compatible_researched_technologies_from_donor](#union_compatible_researched_technologies_from_donor)
- [call_natural_disaster](#call_natural_disaster)
- [apply_state_population_gain_without_recruitable_manpower_gain](#apply_state_population_gain_without_recruitable_manpower_gain)
- [apply_state_population_loss_without_recruitable_manpower_gain](#apply_state_population_loss_without_recruitable_manpower_gain)
- [apply_exact_state_civilian_population_loss](#apply_exact_state_civilian_population_loss)
- [stockpile_debit_helpers](#stockpile_debit_helpers)
- [cbrn_debit_motorized_stockpile_oldest_first](#cbrn_debit_motorized_stockpile_oldest_first)
- [chaosx_convert_days_to_date_offset](#chaosx_convert_days_to_date_offset)
- [chaosx_convert_date_offset_to_days](#chaosx_convert_date_offset_to_days)
- [chaosx_report_forced_event_failure](#chaosx_report_forced_event_failure)
- [owner_owned_apis](#owner_owned_apis)
- [maintenance_notes](#maintenance_notes)

## calculate_economy_scaled_factory_grant

Purpose: convert the current country's civilian and military factory total into a bounded grant count.

Scope: country.

Inputs: positive `economy_scaled_factory_grant_step`, `economy_scaled_factory_grant_min`, and `economy_scaled_factory_grant_cap` temporary variables.

Output: `economy_scaled_factory_grant_count` temporary variable.

Defaults: the result starts at zero, counts complete step-sized blocks, stops at the cap, and rises to the supplied minimum when necessary.

Side effects: none beyond temporary working variables. The effect does not grant buildings.

Example:

```txt
set_temp_variable = { economy_scaled_factory_grant_step = 10 }
set_temp_variable = { economy_scaled_factory_grant_min = 1 }
set_temp_variable = { economy_scaled_factory_grant_cap = 5 }
calculate_economy_scaled_factory_grant = yes
```

## damage_state_building_dynamic

Purpose: apply a caller-selected building type and numeric damage amount in the current state through `meta_effect`, which supplies literal damage text to `damage_building`.

Scope: state.

Inputs: required caller-set temporary variables `dynamic_building_damage_type`, containing a building token such as `token:infrastructure`, and `dynamic_building_damage_amount`, containing the numeric damage amount.
The helper reads both inputs without changing them.

Output: one native `damage_building` effect in the current state with the requested building type and amount.
There is no output variable.

Defaults: none.
The caller must initialize both inputs before use in the same effect chain.
The amount can be initialized once before a bounded group of calls when no intervening effect overwrites it.
An unset input is a caller error, and zero is an explicit amount rather than an absence sentinel.
The helper applies no explicit arithmetic rounding, clamp, scaling, repair modifier, or replacement amount.
Numeric interpolation uses the engine default formatter, matching the existing shared damage helper.
Exact serialization of arbitrary fractional or large amounts requires runtime validation.

Side effects: building damage only.
The native effect retains its state-building lookup and, for province buildings, its search for the first matching province building in the current state.
The helper performs no random selection or scope change and writes no variables, flags, or event targets.
Temporary inputs last for the caller's effect chain, so no persistent cleanup is required.
Callers must overwrite inputs before an independent operation that requires different values.

Example, inside the state already selected by the caller:

```txt
set_temp_variable = { dynamic_building_damage_amount = constant:my_system_tuning.building_damage }
set_temp_variable = { dynamic_building_damage_type = token:infrastructure }
damage_state_building_dynamic = yes
set_temp_variable = { dynamic_building_damage_type = token:arms_factory }
damage_state_building_dynamic = yes
```

Call sites: `common/scripted_effects/033_acid_rain_effects.txt` and `common/scripted_effects/031_random_terror_effects.txt`.
Building selection, damage tuning, and eligibility remain caller-owned.

References: vanilla `documentation/effects_documentation.md` sections `damage_building` and `meta_effect`, vanilla `common/scripted_effects/00_scripted_effects.txt` effect `SF_PARA_sabotage_effect`, and the building-token interpolation in `natural_disaster_damage_selected_building` in `common/scripted_effects/013_natural_disasters_effects.txt`.
The shared `damage_buildings_in_random_states` helper uses the same unformatted numeric interpolation.
The offline Data structures and Localisation pages document building tokens and `GetTokenKey`.

## damage_buildings_in_random_states

Purpose: damage a configurable number of eligible buildings in a configurable share of the current country's owned and controlled states.

Scope: country.

Inputs: `buildings_to_damage_per_state`, `percent_of_states_to_target`, `damage_modifier`, and optional `state_population_percent` temporary variables.

Outputs: direct state building damage and, when `state_population_percent` is above zero, a proportional population reduction in each selected state.
The reduction is the state population in thousands times that share, applied as a negative `add_manpower` amount.

Defaults: the helper counts the country's controlled states from zero and targets that count times `percent_of_states_to_target`, rounded and never below one while at least one controlled state exists.
A `percent_of_states_to_target` of zero becomes `0.1`, a `damage_modifier` of zero becomes `0.25`, and a `buildings_to_damage_per_state` below one becomes `3`.
Each target is chosen from the country's owned and controlled states that hold at least one targetable building, and building types that are unavailable in a selected state receive no random weight.
A missing or zero `state_population_percent` leaves population unchanged.

Side effects: mutates buildings or population in randomly selected controlled states and uses temporary selection variables.

This helper does not register deaths in the shared Deaths ledger, because the population branch changes manpower directly.
Callers that need ledger registration use `apply_exact_state_civilian_population_loss`.
The helper currently has no callers and is kept as a documented shared hook.

Example:

```txt
set_temp_variable = { buildings_to_damage_per_state = 2 }
set_temp_variable = { percent_of_states_to_target = 0.25 }
set_temp_variable = { damage_modifier = 1 }
set_temp_variable = { state_population_percent = 0.01 }
damage_buildings_in_random_states = yes
```

## get_random_sea_region

Purpose: select one strategic-region ID from the shared curated sea-region pool.

Scope: any scope.

Inputs: none.

Output: `global.rand_sea_region`.

Defaults: every branch writes a region ID. Repeated entries preserve the pool's existing weighting.

Side effects: replaces `global.rand_sea_region`.

Example:

```txt
get_random_sea_region = yes
```

## clear_special_chaos_country_civilian_effects

Purpose: remove transient civilian penalties from a special Chaos country when a bounded caller decides cleanup is due.

Scope: country.

Inputs: none.

Outputs: clears `mass_panic` and removes `galaxies_mix` when present.

Defaults: absent flags or ideas produce no change. The registry does not enable a periodic whole-world caller.

Side effects: mutates the scoped country's flag and idea state.

Example:

```txt
if = {
	limit = { is_special_chaos_country = yes }
	clear_special_chaos_country_civilian_effects = yes
}
```

## refresh_world_threat_state

Purpose: rebuild the mod-wide existential-threat aggregate after an owning system activates or deactivates its source.

Scope: any scope.

Inputs: none. Each threat system sets or clears its own registered global source flag before calling the effect.

Registered sources: `world_threat_source_zombies`, `world_threat_source_holy_realm`, `world_threat_source_mengele`, `world_threat_source_fury`, `world_threat_source_death`, `world_threat_source_cannibalism`, `world_threat_source_black_plague`, `world_threat_source_resources_found_caves`, `world_threat_source_brilliant_scientist`, `world_threat_source_sov_nuclear_bombs`, and `world_threat_source_random_terror`.

The `world_threat_source_sov_nuclear_bombs` source counts only while none of `fallout_transition_active`, `fallout_active`, `world_end_final_silence`, and `world_end_final_silence_completed` is set, so the nuclear-bomb source stops contributing once fallout or the Final Silence takes over.

Outputs: `global.world_threat_source_count` and the `world_in_threat` global flag.

Defaults: no active source produces a count of `0` and clears `world_in_threat`.

Side effects: rebuilds the aggregate count and flag only.

Example:

```txt
if = {
	limit = { my_threat_is_active = yes }
	set_global_flag = world_threat_source_my_threat
}
else = {
	clr_global_flag = world_threat_source_my_threat
}
refresh_world_threat_state = yes
```

## union_compatible_researched_technologies_from_donor

Purpose: add every compatible missing researched technology from a donor country without removing the recipient's existing research.

Scope: country recipient.

Input: `event_target:technology_union_donor`, saved as the donor country before the call.

Output: missing donor technologies are granted to the recipient with popups disabled.

Defaults: technologies already held by the recipient are skipped. Flexible and streamlined production remain mutually exclusive, as do the concentrated and dispersed industry branches.

Side effects: newly granted technologies execute the normal `set_technology` behavior. The effect does not change research slots, remove technologies, clear the donor target, or annex the donor.

Example:

```txt
FROM = { save_event_target_as = technology_union_donor }
union_compatible_researched_technologies_from_donor = yes
```

## call_natural_disaster

Purpose: provide the stable country-scope gateway for callers that need to start a natural-disaster sequence.

Scope: country.

Contract: callers set the documented `natural_disaster_call_*` temporary inputs and any required regular event targets, then call `call_natural_disaster = yes`. The gateway delegates validation, target resolution, delayed work, impact, reports, aftermath, and cleanup to the Event 013 owner.

Outputs: `natural_disaster_call_result`, `natural_disaster_call_reject_reason`, `natural_disaster_call_sequence_id`, `natural_disaster_call_primary_job_count`, `natural_disaster_call_skipped_primary_count`, and the documented resolved-target proofs.

Defaults: invalid or incomplete input fails closed and queues no work. The gateway resets public call inputs after each call while leaving result and proof outputs available to the caller.

Full input, target, origin, authority, and scaling details are documented in [`natural_disasters_overview`](../../docs/events/013_natural_disasters/overview.md).

Example:

```txt
set_temp_variable = { natural_disaster_call_family = constant:natural_disaster_family.earthquake }
set_temp_variable = { natural_disaster_call_target_mode = constant:natural_disaster_target_mode.random_valid }
call_natural_disaster = yes
```

## apply_state_population_gain_without_recruitable_manpower_gain

Purpose: add real state population without keeping the recruitable manpower that HOI4 credits to the owner and controller at the moment of a positive state-scope `add_manpower`, so the new people become recruitable through the engine's ordinary recruitable-population rules instead of arriving as an instant reserve.

Scope: state.

Inputs: `state_population_gain_request`, the requested number of people as a temporary variable.

Outputs: `state_population_gain_applied`, the measured rise in state population in people, never above the request and never below zero, and `state_population_gain_reconciled`, the observed recruitable credit removed from the owner and distinct controller.

Defaults: a missing or non-positive request applies nothing and returns zero. The request is rounded to whole people.

Side effects: one positive state population mutation, then removal of only the observed positive `manpower_k` credit of the owner and, when different, the controller, each capped at the applied amount. The request is reset to zero after the call. Callers must use `state_population_gain_applied`, never the request, for every ledger update.

Owner-specific precedents with the same measured contract are `camp_occ_apply_population_credit` and `civilian_transfer_apply_destination_credit`. Event 037 Mysterious People is the first caller.

Example:

```txt
set_temp_variable = { state_population_gain_request = 25000 }
apply_state_population_gain_without_recruitable_manpower_gain = yes
set_temp_variable = { my_measured_gain = state_population_gain_applied }
```

## apply_state_population_loss_without_recruitable_manpower_gain

Purpose: remove real state population without retaining the recruitable-manpower credit that HOI4 attaches to a negative state-scope `add_manpower` effect.

Scope: state.

Inputs: positive `state_population_transaction_loss` and one-shot `state_population_transaction_contract_supplied = 1` temporary variables.

Output: `state_population_transaction_reconciled_gain`, the observed recruitable-manpower credit removed from the owner and distinct controller.

Defaults: a missing proof or loss produces a zero-value transaction. The requested loss is clamped to zero or above and rounded.

Side effects: applies one negative state population mutation, reconciles only observed positive credit up to the requested loss, and clears the one-shot inputs.

Example:

```txt
set_temp_variable = { state_population_transaction_loss = 25000 }
set_temp_variable = { state_population_transaction_contract_supplied = 1 }
apply_state_population_loss_without_recruitable_manpower_gain = yes
```

## apply_exact_state_civilian_population_loss

Purpose: apply one exact civilian population loss against a protected population floor while returning the amount actually removed.

Scope: state.

Inputs: `state_civilian_population_loss_requested`, `state_civilian_population_loss_minimum_remaining`, `state_civilian_population_loss_reason`, `state_civilian_population_loss_log_deaths`, `state_civilian_population_loss_target_country`, `state_civilian_population_loss_has_target_country`, and one-shot `state_civilian_population_loss_contract_supplied` temporary variables.

Outputs: `state_civilian_population_loss_applied` and `state_civilian_population_loss_result`.

`state_civilian_population_loss_result` is `0` when no population was removed and `1` when an observed positive amount was removed.
`state_civilian_population_loss_applied` is the measured pre-transaction state population minus the measured post-transaction state population, expressed in people and never below zero.
The protected floor is rounded upward to a whole person and the requested transaction is rounded and clamped to whole civilians available above it.
Fractional availability is floored so rounding cannot cross the caller's protected minimum.
Callers must initialize both output temporary variables before invoking the helper so their returned values survive the scripted-effect boundary.

Defaults: missing contract inputs produce a zero-value request with the unknown Deaths reason, no valid target, and a zero population floor.

A state whose owner or controller is nonhuman also produces the same zero-value transaction through `state_uses_normal_civilian_systems`.
Both outputs remain zero, the shared casualty ledger receives no record, and public inputs are cleared normally.

Side effects: applies one state-scope population transaction, reconciles observed recruitable-manpower credit, reads back the state population, optionally registers only the observed positive loss through `chaos_meter_register_deaths`, and clears all public inputs before return.
Deaths registration uses `chaos_deaths_apply_state_pop = 0` and `chaos_deaths_record_state_ledger = 1`, so the state ledger, global ledger, cause history, and normal shared Chaos progression use the measured amount without another population mutation.
An engine transaction that removes zero population returns zero and creates no death record.

The applied amount is registered through `chaos_meter_register_deaths` only when `state_civilian_population_loss_log_deaths` is above zero and either the Deaths ledger is enabled (`settings_chaos_deaths_disabled` is not set) or one of the fallout states `fallout_air_cleanliness_disabled`, `fallout_transition_active`, `fallout_active`, `fallout_manual_scenario_active`, `fallout_manual_sweep_active`, or `fallout_manual_countdown_active` is set.
When Deaths logging is disabled or the log flag is zero, the same population-first transaction still runs, but nothing is written to the Deaths ledger.
The result is still determined by the observed population decrease, not by the logging policy.

Example:

```txt
set_temp_variable = { state_civilian_population_loss_requested = 25000 }
set_temp_variable = { state_civilian_population_loss_minimum_remaining = 10000 }
set_temp_variable = { state_civilian_population_loss_reason = constant:chaos_meter_deaths_reason.unknown }
set_temp_variable = { state_civilian_population_loss_log_deaths = 1 }
set_temp_variable = { state_civilian_population_loss_target_country = OWNER }
set_temp_variable = { state_civilian_population_loss_has_target_country = 1 }
set_temp_variable = { state_civilian_population_loss_contract_supplied = 1 }
set_temp_variable = { state_civilian_population_loss_applied = 0 }
set_temp_variable = { state_civilian_population_loss_result = 0 }
apply_exact_state_civilian_population_loss = yes
```

## stockpile_debit_helpers

Purpose: remove dynamically calculated positive amounts from supported equipment and fuel stockpiles.

Scope: country.

Helpers: `remove_support_equipment_from_stockpile`, `remove_motorized_equipment_from_stockpile`, `remove_convoys_from_stockpile`, `remove_trains_from_stockpile`, `remove_plague_bombs_from_stockpile`, `remove_infantry_equipment_from_stockpile`, and `remove_fuel_from_stockpile`.

Inputs: `equipment_stockpile_removal_amount` for equipment helpers or `fuel_stockpile_removal_amount` for `remove_fuel_from_stockpile`.

Defaults: no amount is inferred. A zero input performs a zero-value transaction.

Side effects: each helper negates its temporary amount in place and applies the matching stockpile debit through the supported engine effect.

Example:

```txt
set_temp_variable = { equipment_stockpile_removal_amount = 250 }
remove_support_equipment_from_stockpile = yes

set_temp_variable = { fuel_stockpile_removal_amount = 500 }
remove_fuel_from_stockpile = yes
```

## cbrn_debit_motorized_stockpile_oldest_first

Purpose: debit a requested number of CBRN trucks from the country's real motorized stockpile, taking `motorized_equipment_0` before `motorized_equipment_1`, and report how many trucks were actually removed.

Scope: country.

Input: caller-set temporary `cbrn_motorized_stock_debit_requested`, expressed as a nonnegative whole truck count. The helper reads this input without changing it.

Outputs: temporary `cbrn_motorized_stock_debit_completed` is the total removed from both models; temporary `cbrn_motorized_stock_debit_remaining` is the unmet part of the nonnegative request. Both are overwritten on every call.

Defaults: an unset request has no inferred value and is a caller error. A zero or negative request removes zero trucks. Each model's available stock is floored at zero, and each debit is limited to that model's actual stock and the remaining request. The caller must round any calculated price before showing and passing it so the display and debit use the same whole count.

Side effects: removes up to the requested number of `motorized_equipment_0` and then `motorized_equipment_1` from the scoped country's stockpile. It writes only temporary working variables and the two outputs; it creates no persistent flags, variables, or event targets and needs no cleanup. The helper does not grant the operation or enforce affordability: the caller must check full affordability before debiting, then use `completed` for consumption records and block the operation if any request remains.

Example, inside the paying country scope after the caller has calculated and displayed the same integer cost:

```txt
set_temp_variable = { cbrn_motorized_stock_debit_requested = my_system_motorized_cost }
cbrn_debit_motorized_stockpile_oldest_first = yes
add_to_variable = { my_system_motorized_paid = cbrn_motorized_stock_debit_completed }
```

The separate `remove_motorized_equipment_from_stockpile` helper is a legacy archetype debit and has no actual-payment output. CBRN callers that need exact payment should use this model-specific helper.

## chaosx_convert_days_to_date_offset

Purpose: convert a day count into the date-variable encoding so it can be added to `global.date` or to a stored copy of it.
Date variables count one game hour as 0.00001, so one day is 0.00024 date units, and adding a raw day count to a stored date moves it decades instead of days.

Scope: any scope. Temporary variables are unscoped, and the helper reads no scope data.

Input: caller-set temporary `chaosx_date_days`, a day count. The helper reads it without changing it.

Output: temporary `chaosx_date_offset`, the matching date-unit offset. It is overwritten on every call.
The caller must set `chaosx_date_offset` before the call, for example to `constant:chaosx_date_units.zero`, because a temporary variable first created inside a scripted effect may not survive the effect's return, while one defined before the call is carried in and modified in place.

Defaults: an unset input reads as zero and returns a zero offset.
Whole-day inputs, positive or negative, convert exactly.
Fractional days are converted at the engine's one-hour date resolution and round up to the next whole hour, so a due date built from the offset never lands before the requested duration has passed.
Negative inputs produce a negative offset for comparisons against past dates.

Side effects: none beyond temporary variables. The helper writes the private working value `chaosx_date_unrounded_hours`, which is not an output, and changes no date, flag, country, state, or persistent variable.

Constants: category `chaosx_date_units` in [`chaosx_date_units_constants.txt`](../script_constants/chaosx_date_units_constants.txt), using `hours_per_day`, `hour_step`, and `hours_per_date_unit`.
The day count is multiplied by `hours_per_day` and divided by `hours_per_date_unit`, so the int schema needs no five-decimal literal, and the five-decimal variable precision represents every whole-hour result exactly.

Example, storing a due date a tuned number of days ahead:

```txt
set_temp_variable = { chaosx_date_days = constant:my_system_tuning.due_days }
set_temp_variable = { chaosx_date_offset = constant:chaosx_date_units.zero }
chaosx_convert_days_to_date_offset = yes
set_variable = { my_system_due_date = global.date }
add_to_variable = { my_system_due_date = chaosx_date_offset }
```

Keep native `days =` fields, mission durations, timed flag durations, AI scores, and MTTH values in days.
Convert only the value that is written into or compared with a stored date, and copy an already encoded stored date without converting it again.

## chaosx_convert_date_offset_to_days

Purpose: convert a date difference, such as a stored due date minus `global.date`, into a whole-day count for native `days =` delays and day-based displays.

Scope: any scope. Temporary variables are unscoped, and the helper reads no scope data.

Input: caller-set temporary `chaosx_date_offset`, a difference between two date-variable values. The helper reads it without changing it.

Output: temporary `chaosx_date_days`, whole days rounded up and never below zero. It is overwritten on every call.
The caller must set `chaosx_date_days` before the call, for example to `constant:chaosx_date_units.zero`, because a temporary variable first created inside a scripted effect may not survive the effect's return.

Defaults: an unset input reads as zero and returns zero days.
Any partial day rounds up to the next whole day, so a delayed event or timed effect that waits the returned number of days resolves on or after the stored date, never before it.
A date that has already passed returns zero.

Side effects: none beyond temporary variables. The helper writes the private working value `chaosx_date_unrounded_days`, which is not an output, and changes no date, flag, country, state, or persistent variable.

Constants: category `chaosx_date_units`, using `hours_per_date_unit`, `hours_per_day`, `day_step`, and `zero`.
The offset is multiplied by `hours_per_date_unit` into whole hours and divided by `hours_per_day`; a remainder of even one hour leaves a fraction of at least one twenty-fourth, which the round-up step always detects.

Example, waking a worker on the stored due date:

```txt
set_temp_variable = { chaosx_date_offset = my_system_due_date }
subtract_from_temp_variable = { chaosx_date_offset = global.date }
set_temp_variable = { chaosx_date_days = constant:chaosx_date_units.zero }
chaosx_convert_date_offset_to_days = yes
set_temp_variable = { my_system_wake_days = chaosx_date_days }
```

Pass the returned day count to a field that accepts a variable, such as the `days` of a delayed `country_event`, or through `meta_effect` where a native field accepts only literal text.
Calling this helper overwrites `chaosx_date_days`, so copy a day input that another consumer still needs before the call.

References: the offline Data structures page, Game variables table, `date` row, documents one game hour as 0.00001 and the zero point of the encoding, and its Variables section documents the five-decimal variable precision and the scripted-effect temporary variable lifetime rule.
Installed `documentation/dynamic_variables_documentation.md` describes `date` as a comparable date value, and `documentation/script_concept_documentation.md` and `common/script_constants/documentation.md` define the schema-first constant groups and `constant:` access in variable operations.

## chaosx_report_forced_event_failure

Purpose: send one plain-text country report to the player who requested an event through Settings when the owning event cannot apply.
Source: `chaosx_forced_event_feedback_effects.txt`, with the native report in `events/chaosx_forced_event_feedback.txt` and the shared catalogue in `common/script_constants/chaosx_forced_event_feedback_constants.txt`.

Scope: COUNTRY, including a target country handling a request made by another country.
Input: caller-set temporary `chaosx_forced_event_failure_reason = constant:forced_event_feedback_reason.<key>`, choosing `no_country`, `no_state`, `no_target`, `already_active`, `unavailable`, or `dispatch_failed`.
Set that input in the calling effect block immediately before `chaosx_report_forced_event_failure = yes`.
The helper reads the input without changing it.
This hook follows the existing caller-set variable convention used by the shared helpers.
An unrecognized numeric value selects the generic dispatch-failed description.
Select the most specific applicable reason and coordinate additions to the shared catalogue and report with the Settings owner.

Requester lifecycle: `chaosx_begin_manual_event_request = yes` saves the requesting country as regular `event_target:chaosx_manual_event_requester`, clears `chaosx_manual_event_failure_shown` and the previous batch marker, and sets requester flag `chaosx_manual_event_requested` for `constant:forced_event_feedback_timing.request_window_days` through a temporary day variable.
The COUNTRY begin helper takes no input and has no gameplay or timer effect.
Single-event dispatch calls it before owner preflight.
Event Logs Fire Selected calls it once before the loop, sets a timed `chaosx_manual_event_batch_requested` marker and a synchronous `chaosx_manual_event_batch_dispatch` guard, then clears the dispatch guard after the loop.
Member dispatches retain the same requester and shown flag, so repeated rejected members create one plain batch summary rather than one popup per member.
The timed batch marker remains available to entry-event callbacks and native report description selection.
The hook requires that target to exist, remain a human country, carry the request flag, and have no report receipt.
It never guesses the requester from ROOT, FROM, or the current country.
Regular targets travel into events fired by the chain and automatically disappear when the chain finishes, avoiding a global pointer shared by multiple players.
Owner callbacks must stay in that originating chain and inside the request window.

Outputs and side effects: writes normal requester variable `chaosx_manual_event_failure_reason`, sets `chaosx_manual_event_failure_shown` before dispatch, and immediately fires `chaosx_forced_event_feedback.1` for the requester.
It changes no owner gameplay, request flag, global state, or event-log entry.
Natural firing, missing or expired request context, an AI requester, or a repeated failure in the same request produces no report.
The first reported failure wins until the dispatcher begins another request.
The report's acknowledgement performs no cleanup so dismissing it cannot reset the receipt of a later request.
The dispatcher owns receipt reset and may clear the reason variable before a subsequent request.

Native conditional `desc` blocks choose a reason localisation key instead of re-reading a mutable country variable through scripted localisation on each text evaluation.
Multiple outstanding reports still require live confirmation that the engine retains the selected description for each event instance.
The two-day country guard is not a unique asynchronous request identifier, so overlapping delayed requests from the same player require a future owner-managed generation token.

Example inside an owner event's country-scope failure branch:

```txt
set_temp_variable = { chaosx_forced_event_failure_reason = constant:forced_event_feedback_reason.no_country }
chaosx_report_forced_event_failure = yes
```

The dispatcher must establish the target and flags before this call.
Settings supplies the request context, and its dispatcher or an owner event calls the hook from an actual failure branch.
No icon or additional visual asset is required for this native text report.
Detailed reference evidence and integration limits are recorded in `docs/plans/shared_interface_plans/subagent_handoffs/forced_feedback_hook_20261005.md`.

## chaosx_recruit_character

Purpose: attach one defined character to the country that runs it, during play.
Source: `chaosx_runtime_recruit_effects.txt`.

Scope: COUNTRY.
Input: caller-set temporary `chaosx_recruit_character_token = token:<character_id>`, set immediately before `chaosx_recruit_character = yes`.
The character id must be listed in `common/synchronized_dynamic_tokens/chaosx_runtime_tokens.txt`.
The helper builds `recruit_character = <id>` with a meta effect, so the effect is parsed when it executes rather than at game load.
The engine still advises that `recruit_character` belongs in country history when a mechanic recruits during play; the Malta, Time Traveler, Lawrence and Fallout mechanics recruit their characters in response to events, decisions and focuses.
Side effects: none beyond the native recruitment.

Example:

```text
set_temp_variable = { chaosx_recruit_character_token = token:malta_pope }
chaosx_recruit_character = yes
```

## owner_owned_apis

The following APIs are useful to other systems but are not declared in this registry. Use the named owner source and documentation for their contracts. This index is deliberately not a second copy of those event or subsystem implementations.

| capability | authoritative_source | reference |
| --- | --- | --- |
| `gods_of_africa_funded_repairs` | [`012_africa_gods_industry_effects.txt`](012_africa_gods_industry_effects.txt) and [`012_africa_gods_industry_integration_effects.txt`](012_africa_gods_industry_integration_effects.txt) | [COUNTRY/STATE funding, finite service, scoped removal, pure preflights and receipt API](012_africa_gods_industry_effects.md) and [contract, report and history integration](012_africa_gods_industry_integration_effects.md) |
| `gods_of_africa_strength_inputs` | [`012_africa_gods_strength_inputs_effects.txt`](012_africa_gods_strength_inputs_effects.txt) and [pure proofs](../scripted_triggers/012_africa_gods_strength_inputs_triggers.txt) | [COUNTRY census, cached armies, secured-core collection, ROOT-independent identity, selected component blends and cleanup API](012_africa_gods_strength_inputs_effects.md) |
| `ordinary_biological_incubation` | [`biological_lifecycle_effects.txt`](biological_lifecycle_effects.txt) | [incubation scheduling API](../../docs/systems/cbrn_warfare/biological_warfare/biowarfare_system.md#incubation-scheduling-api) |
| `event021_calendar_conversion` | [`021_random_civil_war_date_effects.txt`](021_random_civil_war_date_effects.txt) | [`date_effects`](021_random_civil_war_date_effects.md) |
| `event021_exact_front_ledger` | [`021_random_civil_war_front_ledger_effects.txt`](021_random_civil_war_front_ledger_effects.txt) | [`front_ledger_effects`](021_random_civil_war_front_ledger_effects.md) |
| `cbrn_state_mask_escrow` | [`cbrn_state_escrow_native_effects.txt`](cbrn_state_escrow_native_effects.txt) and [`cbrn_protection_effects.txt`](cbrn_protection_effects.txt) | [measured concrete-model reservation/refund API](cbrn_scripted_effects.md#measured-native-state-escrow-primitives) |
| `test_country_facilities_and_projects` | [`chaosx_test_country_effects.txt`](chaosx_test_country_effects.txt), [`chaosx_test_country_special_project_effects.txt`](chaosx_test_country_special_project_effects.txt), and [`chaosx_test_country_triggers.txt`](../scripted_triggers/chaosx_test_country_triggers.txt) | [`chaosx_test_country`](../../docs/testing/chaosx_test_country.md) |
| `independence_wave_ledger` | [`006_independence_wave_iberian_package_effects.txt`](006_independence_wave_iberian_package_effects.txt) | [`independence_wave_effects`](006_independence_wave_effects.md) |
| `independence_wave_federal_governance` | [`006_independence_wave_ready_formable_contracts_effects.txt`](006_independence_wave_ready_formable_contracts_effects.txt) | [signature governance API](../../docs/events/006_independence_wave/signature_modules.md#signature-governance-api) |
| `independence_wave_package_incident_dispatch` | [`006_independence_wave_package_incident_effects.txt`](006_independence_wave_package_incident_effects.txt) | [appointment and shown-report API](../../docs/events/006_independence_wave/systems/package_incident_lifecycle.md) |
| `independence_wave_form48_display` | [capture and bound-carrier predicates](../scripted_triggers/006_independence_wave_form48_display_triggers.txt), called by `GetIndependenceWaveForm48Ledger` | [COUNTRY display API: caller-owned pointer/six values, frozen binding, rejection/N/A, temporary-only side effects and usage](../../docs/plans/006_independence_wave_plans/subagent_handoffs/form48_dynamic_display_20261008.md#display-api) |
| `independence_wave_diplomatic_targets` | [`is_independence_wave_current_diplomatic_target`](../scripted_triggers/006_independence_wave_diplomatic_target_triggers.txt) and the existing registration writer | [COUNTRY predicate: ordinary foreign branch, frozen identity tuple, paired generation row, held anchor, defaults, side effects and usage](../../docs/events/006_independence_wave/systems/diplomatic_targets.md) |
| `custom_technology_grants` | [`016_brilliant_scientist_custom_technology_api_effects.txt`](016_brilliant_scientist_custom_technology_api_effects.txt) | [`custom_technology_api`](016_brilliant_scientist_custom_technology_api_effects.md) |
| `portal_transit_equipment_output` | [`016_portal_transit_batch_effects.txt`](016_portal_transit_batch_effects.txt) | [neutral physical output and paid KRG transaction contract](016_portal_transit_batch_effects.md) |
| `private_paleogenetics_deployment` | [`016_mengele_paleogenetics_deployment_effects.txt`](016_mengele_paleogenetics_deployment_effects.txt) and [`016_mengele_paleogenetics_deployment_triggers.txt`](../scripted_triggers/016_mengele_paleogenetics_deployment_triggers.txt) | [actor-bound paired construction and retained payment](016_mengele_paleogenetics_deployment_effects.md) |
| `private_paleogenetics_staffing` | [`016_mengele_paleogenetics_staff_effects.txt`](016_mengele_paleogenetics_staff_effects.txt) and [`016_mengele_paleogenetics_staff_triggers.txt`](../scripted_triggers/016_mengele_paleogenetics_staff_triggers.txt) | [actual workforce allocation, training fee and bounded release](016_mengele_paleogenetics_staff_effects.md) |
| `transit_state_province_membership` | [`016_transit_state_province_catalog_triggers.txt`](../scripted_triggers/016_transit_state_province_catalog_triggers.txt) | [lazy pure STATE membership query](../scripted_triggers/016_transit_state_province_catalog_triggers.md) |
| `conventional_technology_packages` | [`016_conventional_technology_api_effects.txt`](016_conventional_technology_api_effects.txt) and [`016_conventional_technology_api_triggers.txt`](../scripted_triggers/016_conventional_technology_api_triggers.txt) | [`conventional_technology_api_effects`](016_conventional_technology_api_effects.md) |
| `biological_operations` | [`016_brilliant_scientist_biological_operations_effects.txt`](016_brilliant_scientist_biological_operations_effects.txt) and [`016_brilliant_scientist_biological_operations_triggers.txt`](../scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt) | [`biological_operations`](../../docs/events/016_brilliant_scientist/systems/biological_operations.md) |
| `portal_beachhead_lifecycle` | [`016_brilliant_scientist_raid_effects.txt`](016_brilliant_scientist_raid_effects.txt) and [`016_brilliant_scientist_raid_triggers.txt`](../scripted_triggers/016_brilliant_scientist_raid_triggers.txt) | [`portal_raider_api`](../../docs/events/016_brilliant_scientist/systems/portal_raider_api.md) |
| `clone_system` | [`clone_system_effects.txt`](clone_system_effects.txt) | [`clone_equipment_and_infantry`](../../docs/systems/3d_model_pipeline/clone_equipment_and_infantry.md) |
| `alien_infantry` | [`016_alien_infantry_api_effects.txt`](016_alien_infantry_api_effects.txt) and [`016_alien_infantry_api_triggers.txt`](../scripted_triggers/016_alien_infantry_api_triggers.txt) | [`alien_infantry_api_effects`](016_alien_infantry_api_effects.md) |
| `project_bridge` | [`016_mengele_project_bridge_effects.txt`](016_mengele_project_bridge_effects.txt) and [`016_mengele_project_bridge_triggers.txt`](../scripted_triggers/016_mengele_project_bridge_triggers.txt) | [`project_system`](../../docs/events/016_brilliant_scientist/systems/projects.md) |
| `universal_cost_framework` | [`chaosx_universal_cost_effects.txt`](chaosx_universal_cost_effects.txt), [`chaosx_universal_cost_triggers.txt`](../scripted_triggers/chaosx_universal_cost_triggers.txt), and [`chaosx_universal_cost_exact_triggers.txt`](../scripted_triggers/chaosx_universal_cost_exact_triggers.txt) | [`universal_cost_modifier`](../../docs/systems/universal_cost_modifier.md) and [exact quotation contracts](../scripted_triggers/chaosx_universal_cost_exact_triggers.md) |
| `black_friday_sale_prices` | [`026_black_friday_price_table_effects.txt`](026_black_friday_price_table_effects.txt) | [`sale price table`](026_black_friday_price_table_effects.md) |
| `national_policy_native_costs` | [`national_policy_cost_effects.txt`](national_policy_cost_effects.txt) and [`national_policy_cost_modifiers.txt`](../dynamic_modifiers/national_policy_cost_modifiers.txt) | [Native law PP ownership, live doctrine eligibility, mutually exclusive sale totals, initialization, cleanup, and law-family accounting](national_policy_cost_effects.md) |
| `black_friday_simple_costs` | [`026_black_friday_triggers.txt`](../scripted_triggers/026_black_friday_triggers.txt), [`026_black_friday_effects.txt`](026_black_friday_effects.txt), and [`026_black_friday_scripted_localisation.txt`](../scripted_localisation/026_black_friday_scripted_localisation.txt) | [`simple custom-cost API`](026_black_friday_simple_cost_api.md) |
| `unit_family_registry` | [`019_infantry_spawn_unit_registry_effects.txt`](019_infantry_spawn_unit_registry_effects.txt) | [`chaos_unit_family_registry`](../../docs/systems/cbrn_warfare/chaos_unit_family_registry.md) |
| `famine_runtime` | [`famine_core_effects.txt`](famine_core_effects.txt) and [`famine_adapter_effects.txt`](famine_adapter_effects.txt) | [`famine_system`](../../docs/systems/famine_system.md) |
| `asteroid_mineral_control` | [`028_asteroid_incoming_mineral_effects.txt`](028_asteroid_incoming_mineral_effects.txt) and [`028_asteroid_incoming_mineral_triggers.txt`](../scripted_triggers/028_asteroid_incoming_mineral_triggers.txt) | [current-controller mineral API](028_asteroid_incoming_mineral_effects.md) |
| `riches_found_capital_rail_endpoints` | [riches_found_state_has_capital_rail_connection and riches_found_state_can_connect_capital_rail](../scripted_triggers/029_riches_found_rail_triggers.txt) | [Parameter-free, read-only STATE predicates](../../docs/events/029_riches_found/railhead_connection_contract.md) |
| `riches_found_seal_receipts` | [native-boundary effects](029_riches_found_seal_receipt_effects.txt) and [manual-payment/receipt predicates](../scripted_triggers/029_riches_found_seal_receipt_triggers.txt) | [Event 029 actor/mine/family receipt, controller epoch, exact refund, and caller-storage contract](../../docs/events/029_riches_found/seal_receipt_contract.md) |
| `migration_runtime` | [`migration_core_effects.txt`](migration_core_effects.txt), [`migration_adapter_effects.txt`](migration_adapter_effects.txt), and [`migration_reception_preparation_effects.txt`](migration_reception_preparation_effects.txt) | [`migration_system`](../../docs/systems/migration_system.md) and [exact paid preparation contract](migration_reception_preparation_effects.md) |
| `humanitarian_validation` | [`humanitarian_validation_triggers.txt`](../scripted_triggers/humanitarian_validation_triggers.txt) | [`famine_system`](../../docs/systems/famine_system.md) and [`migration_system`](../../docs/systems/migration_system.md) |
| `humanitarian_legacy_decision_costs` | [`humanitarian_legacy_cost_effects.txt`](humanitarian_legacy_cost_effects.txt) and [`humanitarian_legacy_cost_triggers.txt`](../scripted_triggers/humanitarian_legacy_cost_triggers.txt) | [display-only country quote contract](humanitarian_legacy_cost_effects.md) and [inclusive component/profile predicates](../scripted_triggers/humanitarian_legacy_cost_triggers.md) |
| `humanitarian_physical_transport_costs` | [`migration_transport_cost_effects.txt`](migration_transport_cost_effects.txt) and [`migration_transport_cost_triggers.txt`](../scripted_triggers/migration_transport_cost_triggers.txt) | [payer/action/state payment, saved refund, geography and display contract](migration_transport_cost_effects.md) |
| `humanitarian_panel_actions` | [`humanitarian_gui_action_effects.txt`](humanitarian_gui_action_effects.txt), [`famine_gui_action_effects.txt`](famine_gui_action_effects.txt), and [`migration_gui_action_effects.txt`](migration_gui_action_effects.txt) | [exact actor/state/action generation, shared native/GUI gates, sparse due work, cooldowns and production refunds](humanitarian_gui_action_effects.md) |
| `great_depression_start_or_deepen` | [`035_great_depression_effects.txt`](035_great_depression_effects.txt) and [`035_great_depression_triggers.txt`](../scripted_triggers/035_great_depression_triggers.txt) | [`gateway contract`](035_great_depression_effects.md) and [`great_depression`](../../docs/events/035_great_depression.md) |
| `great_depression_register_inherited_region` | [`035_great_depression_region_effects.txt`](035_great_depression_region_effects.txt) | [`regional companion`](035_great_depression_region_effects.md) |

## maintenance_notes

Add a helper here only when its contract is neutral and its callers cross subsystem or event-family boundaries. Give it a descriptive name based on its behavior, not the event that first needed it.

Keep one-event orchestration, event-specific selectors, lifecycle state, and private adapters in the owning source file. A cross-event public gateway may remain in this registry while delegating its owner-specific runtime to the owning source file.

When a shared helper changes, update its contract here and audit every call site. When an owner API changes, update the owner documentation and keep its index row limited to source and reference links.

## chaosx_apply_non_ai_crisis_pressure_to_next_timer

Purpose: apply optional, slight player crisis pressure to the shared event interval for every scheduled event.
Owner: `chaosx_crisis_pressure_effects.txt`; tuning: `crisis_pressure_constants.txt`.
Scope: country.
Input/output: normal `event_timer_days`; temporary scratch output `crisis_pressure_timer_factor`.
Defaults: unchanged when the acting country is AI or its crisis-pressure flag is absent.
Side effects: multiplies the current next-event interval by the live Chaos tier's 0.98–0.95 factor; no targets, flags, costs or periodic hooks.
The caller retains rounding and its minimum interval clamp.
Usage: `chaosx_apply_non_ai_crisis_pressure_to_next_timer = yes` after ordinary timer scaling in `calculate_next_timer_value`.

## Human-country state modifier API

Purpose: apply existing human-system state modifiers as native country-targeted state instances, so every currently existing country that uses normal civilian systems keeps its intended value and nonhuman countries receive no instance.
The helper bodies live in this registry because their callers cross famine, migration, health-pressure and other state-system boundaries.
The modifier definitions, values, icons and lifecycle decisions remain with their existing owners.

| Helper | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `add_human_state_dynamic_modifier` | STATE | Caller-owned temporary `human_state_modifier_request`, a synchronized token of the existing native modifier ID, and numeric `human_state_modifier_requested_days` | Removes the old exact instances, then applies that modifier to existing normal-civilian countries if this state uses normal civilian systems. Records the unchanged per-modifier expiry and deduplicated state/country arrays, then forces the state modifier refresh. |
| `remove_human_state_dynamic_modifier` | STATE | Caller-owned temporary `human_state_modifier_request` | Removes the exact legacy unbound instance and exact views for every recorded country, then clears only this modifier's expiry field. |
| `human_state_modifier_bind_existing_country` | STATE | Caller-owned temporary `human_state_modifier_request` and existing regular country target `human_state_modifier_new_country` | Binds that exact new country only while the state's saved modifier expiry is permanent or still in the future, using the unchanged remaining native days. Adds the country to the state's existing deduplicated recipient array. |
| `refresh_human_state_modifier_country` | COUNTRY | Current existing normal-civilian country and the existing global state registry | Publishes the existing registration/cleanup flags and regular new-country target, then invokes the binding helper for all 23 existing modifier IDs on registered states and forces their modifier refresh. |

All public calls use `= yes`.
The caller passes a modifier token with `set_temp_variable = { human_state_modifier_request = token:<modifier_id> }` rather than a dollar parameter block.
Dynamic names use native `meta_effect`, with `[MODIFIER]` bound through `GetTokenKey` to a helper-local frozen token.
The modifier IDs must be present in `common/synchronized_dynamic_tokens/chaosx_tokens.txt` before these runtime token reads are consumed.
No dummy idea or alternative modifier definition is created.

Defaults: there is no default modifier or duration.
An absent or zero modifier request performs no native modifier operation and consumes the input envelope.
For an add call, zero or a negative supplied day count retains the existing permanent branch, while a positive count retains the existing native timed branch.
Every direct caller initializes the exact token and, for add, the existing numeric duration source in the caller's current chain.
The add helper freezes both inputs before invoking removal, so nested cleanup cannot erase its chosen token or duration.
Add, remove and bind reset both temporary request fields to the shared zero constant on success and rejection.
There is no persistent public result, and these input fields end with their current effect chain.

The saved state variable remains `human_state_modifier_<modifier_id>_until`, with zero for a permanent instance and otherwise the original date-unit expiry.
The add helper predeclares `chaosx_date_offset` before the existing conversion helper, allowing its output to survive a child return and retaining the requested expiry rather than a stale value.
Conversion rounds a partial hour upward under the shared date API, while the native timed modifier receives the original positive day count.
`human_state_modifier_countries` remains a shared, deduplicated state array of recorded recipients across modifier families.
`global.human_state_modifier_states` remains the existing deduplicated registry.
Removing one modifier retains these shared arrays and every other modifier's expiry or bound view.
Recorded-country cleanup resets and explicitly binds its private `human_state_modifier_cleanup_break`, so an inherited nonzero `break` cannot truncate removal.
The refresh traversal preserves its existing state-registry membership filter and does not admit unrelated states.
No periodic hook, CXT grant, world iterator or modifier value is introduced by this API contract.

Scope targets: `human_state_modifier_state`, `human_state_modifier_cleanup_state` and `human_state_modifier_new_country` remain regular event targets confined to their originating effect chain.
Native `scope =` on add, presence and removal uses the same exact country pointer.
The add gate remains `state_uses_normal_civilian_systems`, recipient enumeration remains `exists` plus `uses_normal_civilian_systems`, and country refresh retains those same country requirements.
The internal bind helper assumes the existing validated regular new-country target supplied by refresh and grants no independent country eligibility.

```text
# In the existing state effect, preserve its existing duration source.
set_temp_variable = { human_state_modifier_request = token:famine_state_famine }
set_temp_variable = { human_state_modifier_requested_days = 0 }
add_human_state_dynamic_modifier = yes

# A separate state cleanup chain initializes its own exact modifier input.
set_temp_variable = { human_state_modifier_request = token:famine_state_famine }
remove_human_state_dynamic_modifier = yes

# In an existing validated country birth/identity hook.
refresh_human_state_modifier_country = yes
```

References: installed `effects_documentation.md` sections `add_dynamic_modifier`, `remove_dynamic_modifier`, `meta_effect`, `for_each_scope_loop` and `set_temp_variable`, installed `triggers_documentation.md` section `has_dynamic_modifier`, offline Data structures temporary-variable and token sections, and offline Modifiers' dynamic-modifier section.
Installed documentation's country-targeted state semantics remain authoritative where the offline description of `scope =` differs.
The current scratch handoff records exact source lines/revisions, token IDs, pre-edit/index snapshots, 89 literal consumer migrations and meaningful source cases.
Source cases model native recipient facts, token resolution and modifier primitives, and do not establish native rendering or engine timing.
Future extension should reuse the exact modifier token, expiry field and shared registries rather than introducing a second lifetime or country-view owner.

## Synchronous human-system retirement

`clear_nonhuman_country_human_systems` is COUNTRY-scoped and accepts no numeric inputs.
It reads the actual nonhuman classifier, requires an existing country and uses `human_system_nonhuman_cleanup_current_@THIS` as a cheap idempotent receipt.
The receipt is country-targeted so another tag cannot inherit its completed transition state.
It returns no value and preserves immutable event and casualty history.
Its side effects retire human health, custody, social-pressure and office-investigation spirits and current clinical traits, clear live medical progress flags and genocide foreign pressure, retire owned bilateral human sanction/camp relations, revoke inherited human CBRN occupation policy, detach every recorded human state-modifier view for this country, and force affected state/country modifier refresh.
The boundary settles only the final prior-human military loss interval through the meter-owned consumed receipt, then rebases casualty eligibility.
Immediately after that settlement and before setting the cleanup receipt, it calls `camp_rework_retire_nonhuman_country_missions` in `camp_repression_colonial_country_effects.txt`.
This private COUNTRY-scoped helper accepts no inputs or defaults, returns no value, and is called only after the transition owner has established the nonhuman classification.
It removes active `fr_gurs_legacy_review`, `bel_concession_reform_mandate`, `fr_refugee_pressure_response`, `bel_congo_resource_quota_cycle`, `bel_congo_transport_corridor_project`, and `bel_colonial_strike_response` missions with `remove_mission`, which does not run completion or timeout outcomes.
It also removes the active timed `fr_close_camp_legacy_sites` decision with `remove_decision`, which skips its removal outcome and retires its native consumer-goods modifier immediately.
It clears private refugee/strike routes and target IDs, retires the settlement commitment idea, and clears the legacy closure attempt.
Repeated cleanup finds no active mission or closure decision and leaves the same cleared state.
Stored Civil Administration review progress is preserved, while nonhuman eligibility prevents its monthly work and new settlement.
The intended use is the existing transition call `clear_nonhuman_country_human_systems = yes` immediately after an identity-marker write; callers should not invoke the normal mission outcome helpers for cleanup.
It does not create population loss, current nonhuman death accounting, gameplay costs, recovery achievements or refunds.
The receipt and return-snapshot contract is documented in [Military casualty eligibility lifecycle](../../docs/systems/chaos_meter/chaos_meter_deaths_mechanic.md#military-casualty-eligibility-lifecycle).
The declaration lists the exact affected ideas and country modifiers rather than suppressing every political or military spirit.

Direct call sites follow classifier marker writes in the Zombie, weaponized-zombie, Death, cave, nonhuman derivative, Kruger population and Rat Nation/King owner packages and triggerable scenarios.
Human return marker removal calls `refresh_human_state_modifier_country`, which clears the nonhuman receipt and publishes `human_state_modifier_registered_@THIS`.
The event-style startup, release, liberation, puppet, government-change and state-control hooks are in `common/on_actions/human_system_boundaries_on_actions.txt`.
Country birth uses the existing registered-state membership filter, existing expiry and exact native country scope.
No periodic world-country hook is introduced.

`condemnation_clear_nonhuman_country_relations`, `condemnation_retire_nonhuman_relation_pair` and `condemnation_clear_monitoring_pair` remain with their owner in [condemnation_sanctions_effects.txt](condemnation_sanctions_effects.txt) and [system contract](../../docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md).
The occupation-specific cleanup remains with [cbrn_occupation_effects.txt](cbrn_occupation_effects.txt) and [occupation contract](../../docs/systems/cbrn_warfare/cbrn_occupation_and_nerve_suppression.md#human-holder-boundaries).
Every new global registry entry, per-modifier expiry and recorded country view remains owned by the state-modifier API above.
Its targets are regular chain-lifetime event targets and there is no new global event target to clear.
The shared registry is retained when one modifier ends because other families can still own views on the same state.
Future human-system extensions should reuse this transition boundary and add only their exact owned cleanup fields.


## Native warfare law integration

The family permission, law-change callback, exact-pair confirmed-use receipt, Event 023 boundary and cleanup contracts are documented in [national_policy_warfare_effects.md](national_policy_warfare_effects.md).
Native family laws are authoritative, and the combined C/B compatibility value grants no final permission.
