# Nuclear Chaos Ladder

## What This Adds

Nuclear and thermonuclear weapon use adds direct chaos on a global diminishing ladder.

The first nuclear or thermonuclear use adds `+10` chaos, the second adds `+5`, the third adds `+3`, the fourth adds `+2`, and the fifth and every later use adds `+1`.

Both nuclear and thermonuclear strikes share the same counter. A campaign that uses one nuclear bomb and then one thermonuclear bomb receives the first and second ladder values, not two separate first-use bonuses.

## System Flow

`common/on_actions/chaosx_on_actions_chaos_meter.txt` calls `chaos_meter_on_nuke_drop` from `on_nuke_drop`.

`common/scripted_effects/chaos_meter_effects.txt` then:

1. initializes `global.chaos_meter_nuclear_uses` if an older save does not have it,
2. increments the global nuclear-use counter,
3. maps the current count to the ladder values in `common/script_constants/chaos_meter_constants.txt`,
4. records the strike through `add_chaos_meter_value`,
5. keeps the existing nuclear or thermonuclear history reason,
6. applies deaths and fallout, registers the nuclear source with the shared condemnation system, and notifies the Air Cleanliness Treaty use hook.

The tuneable values live in `chaos_meter_delta.nuke`:

- `first = 10`
- `second = 5`
- `third = 3`
- `fourth = 2`
- `fifth_plus = 1`

## Condemnation Integration

The chaos ladder and condemnation gain are separate. Every strike records either `nuclear_strike` or `thermonuclear_strike` context in the public nuclear bucket.

Nuclear condemnation tuning lives in `common/script_constants/condemnation_sanctions_constants.txt`. A normal strike starts at `55`, adds `0.55` per million people, applies shared state-density scaling, and then applies extra `1.15`, `1.35`, or `1.65` population-band multipliers above `5`, `10`, or `20` million people. A capital adds `35`, and a state with more than `8` industrial complexes adds `20`. Strikes against a non-belligerent or an ally or subject each apply `1.50`. Thermonuclear use multiplies that calculated base by `2.25`. Measured civilian deaths then add one point per `10,000` up to `100`, and fallout intensity adds `0.50` per point up to `50`. Major severity applies to a normal strike, while doomsday severity applies to the thermonuclear result.

There is no country-pair exemption. The full source, tier, sanctions, and UI model is documented in `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md`.

## Detonation profile lifetime

Detonation profile metadata is single-use.
After deaths, fallout, condemnation and treaty processing have consumed a native detonation's profile, the shared hook clears Event 23's atomic, test, partial-yield, accident and demonstration markers.
This prevents a later Soviet detonation from another source inheriting a completed test profile.
It adds no second consequence call and changes no consequence coefficient.

## Non-yield Event 23 test accidents

`chaos_meter_on_non_yield_test_accident` in `common/scripted_effects/chaos_meter_effects.txt` is the shared consequence endpoint for a Soviet test device destroyed in a high-explosive or preparation accident without nuclear yield.
Event 23 alone chooses the physical severity and the exact target state, authorizes the action, reserves and commits the device, and decides whether a rare low-integrity accident is a true yield.
This effect does not choose a severity threshold or a target and cannot commit a device.

The caller invokes it in SOV country scope after `sov_nuclear_bombs_execute_shared_action` has accepted and committed the non-detonating test accident and before clearing the action context.
Required country inputs are `sov_nuclear_bombs_action_type = test`, `sov_nuclear_bombs_action_outcome = test_result_accident`, the country flag `sov_nuclear_bombs_action_non_detonating` with `sov_nuclear_bombs_action_detonating` absent, the scope-valued `sov_nuclear_bombs_action_state`, its matching `sov_nuclear_bombs_action_state_id`, `sov_nuclear_bombs_action_nonce`, `sov_nuclear_bombs_last_action_nonce`, `sov_nuclear_bombs_action_transaction_sequence`, `sov_nuclear_bombs_last_action_result = accepted`, and `sov_nuclear_bombs_last_action_accepted`.
The reservation must be closed, with no native delivery pending.
There are no optional inputs or fallback defaults, and invalid or incomplete context has no effects.
The global Chaos Meter disabled setting also skips this endpoint, matching the native `on_nuke_drop` shared-hook gate.
The endpoint never reads a newly selected state or reroutes a target.

For example, after the Event 23 transaction has accepted and committed:

```text
if = {
	limit = { has_country_flag = sov_nuclear_bombs_last_action_accepted }
	chaos_meter_on_non_yield_test_accident = yes
}
```

The endpoint records `chaos_meter_non_yield_accident_nonce` on SOV before applying consequences, so a repeated or older call skips the entire profile.
It increments `global.chaos_meter_nuclear_accident_uses`, records the shared accident Chaos reason and existing accident delta, registers one exact selected-state civilian Deaths transaction with the `nuclear_accident` reason and evacuation adjustment, and seeds the selected state's existing accident-strength radiological contamination modifier if Air Cleanliness is enabled.
The monthly Air system accounts for that state source through its normal ledger and Chaos conversion.
It submits one discovered `observer_report` accident source to shared condemnation with measured deaths and the accident contamination value.
The effect clears its temporary target pointer and accident-context flag after registration.
It does not increment combat nuclear uses, request a native nuke drop, invoke the Air Cleanliness Treaty's unconventional-weapon-use penalty, set `used_unconventional_weapon`, or request terminal Fallout.
The treaty penalty requires weapon use, which this physical accident is not.

The accident death and local radiological contamination coefficients are the existing shared accident constants, not newly chosen Event 23 numbers.
They still need a dedicated physical calibration review because the same coefficients also describe the true-yield accident path.
No probability weight, low-integrity threshold, or Evolution timing base is changed here.

For a true-yield test accident, the native `on_nuke_drop` callback remains the sole shared consequence path.
Both test and accident context flags are present on that path, so `chaos_meter_register_nuclear_condemnation` now gives accident context priority over ordinary test context.
The ordinary successful and partial-yield test classifications retain their existing order and values.

## Player-Facing References

The welcome event chaos-source text displays the full nuclear ladder using cached globals populated by `initialize_welcome_event_variables`.

Chaos history entries continue to use:

- `chaos_meter.history.reason.nuke.base`
- `chaos_meter.history.reason.nuke.thermonuclear`

## Icons and GFX Wiring

No new sprites are required for this feature.

The change reuses the existing Chaos Meter history UI and existing nuclear/thermonuclear reason localisation.

## Future Plans

1. Add a separate settings control for the nuclear chaos ladder.
2. Show the current nuclear-use count in the Chaos Meter status tab.
3. Add a tooltip line to nuclear strike interfaces if the engine exposes a reliable pre-strike hook for the projected next chaos gain.
