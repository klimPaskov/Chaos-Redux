# Air Winter Strategic Bombing Pressure Proof

This tranche adds a small recent strategic-bombing input to the Air Winter state pressure score. Hearts of Iron IV was not launched, so this file records static source and documentation evidence only.

## Engine surface

The installed trigger documentation lists `days_since_last_strategic_bombing` as a state-scope trigger. The same build uses that trigger in vanilla `events/MTG_Britain.txt` and Chaos Redux already uses it in the Deaths pass. This is the exact state fact used by the new pressure input.

The Deaths constants define three existing windows. Hot means fewer than three days, warm means fewer than ten days, and recent means fewer than thirty-one days. The Air Winter calculation reads those shared windows instead of defining a second clock.

## Implemented path

`air_winter_calculate_state_pressure` resets `air_winter_strategic_bombing_pressure` on every valid monthly state update. A state inside the recent window receives `constant:air_winter_pressure.strategic_bombing_recent`. The warm and hot windows replace that value with their stronger tier. The result is added to the ordinary state pressure score and clamped to `constant:air_winter_pressure.strategic_bombing_maximum`.

The constants are deliberately small. Recent bombing adds 0.50 pressure, warm bombing adds 1.25 pressure, and hot bombing adds 2.00 pressure. The maximum is 2.00. These values can move a state toward a phase threshold without creating a second civilian-loss receipt.

The existing Deaths pass remains the only strategic-bombing mortality path. The Air Winter pressure input does not call a Deaths effect, apply population loss, or add a bombing modifier. This avoids compounding an already accepted bombing casualty tick with a second direct mortality channel.

State initialization, migration, Fallout suspension, and administrative reset all initialize or clear the new ledger variable. A Fallout shutdown therefore cannot leave a live Air Winter pressure receipt behind.

## Exact boundaries

The pressure is state-local because the documented trigger is state-local. It can affect phase movement, exposure, building pressure, supply pressure, and the existing military-operation phase modifiers through the normal monthly lifecycle.

The installed documentation does not expose the state of an active ordinary land battle through a state trigger or state combat callback. Active-combat pressure remains absent rather than being approximated with war status, occupation, controller mismatch, or border predicates.

General air-operation modifiers remain country scoped. This tranche does not claim strategic-region confinement for those fields.

## Review status

Static source review covers the constants, state lifecycle, shared bombing windows, Fallout cleanup, and existing Deaths ownership. Runtime timing, modifier readback, save recovery, multiplayer behavior, and threshold feel remain unobserved because Hearts of Iron IV was not launched.
