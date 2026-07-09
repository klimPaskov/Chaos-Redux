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

There is no country-pair exemption. The full source, tier, sanctions, and UI model is documented in `docs/systems/condemnation_sanctions.md`.

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
