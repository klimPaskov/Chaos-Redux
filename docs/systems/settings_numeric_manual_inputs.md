# Settings Numeric Manual Inputs

## Overview

This settings update adds typed numeric entry to the editable value boxes in the Chaos Redux settings window.

The following fields now support direct keyboard entry:

- Timer Interval minimum days
- Timer Interval maximum days
- Chaos Meter preview value
- Advanced Settings recovery rate
- Advanced Settings cap reduction
- Advanced Settings major event weight

The Event ID box already used a separate manual-entry path and remains on that existing system.

## How It Works

1. Clicking a value box activates manual entry for that specific field.
2. While the field is active, digit keys append into a temporary numeric buffer.
3. `Enter` applies the typed value to the staged settings value.
4. `Del` clears the current typed buffer without applying it.
5. Clicking arrows, tier buttons, reset buttons, or apply buttons clears the active manual-entry buffer so the visible value always returns to the live staged value.

The typed input is still staged in the same way as the arrow controls:

- Timer values change `settings_timer_min_days` and `settings_timer_max_days`, then still require the existing `Update Timer` button to apply to the live timer.
- Chaos value changes `settings_chaos_meter_value`, then still requires the existing chaos update button to apply to the live chaos meter.
- Advanced values change the staged advanced settings variables, then still require the existing advanced apply button to push them into the live system.

## Validation Rules

- Timer minimum is clamped to `5` and cannot exceed the staged timer maximum.
- Timer maximum is clamped to the staged timer minimum and now supports values up to `999`.
- Chaos value is clamped between `0` and `1500`.
- Recovery rate is clamped to the configured advanced bounds.
- Cap reduction is entered as a whole-number percent and is converted back into the internal `0.0-1.0` factor.
- Major event weight is clamped to the configured advanced bounds.

## Interaction With Existing Systems

- The display text for each editable field switches to a temporary `...` placeholder when a field is focused and empty.
- Once digits are typed, the display shows the buffered value until `Enter` is pressed or the buffer is cleared.
- The timer interval limit constant now exposes a maximum of `999`, so both arrow controls and typed entry use the same ceiling.

## Icons And Assets

No new art assets are required for this feature.

- Existing box sprites remain in `gfx/interface/`
- Existing sprite wiring remains in `interface/chaosx.gfx`
- Hidden keyboard shortcut buttons reuse existing box sprites and do not need dedicated art

## Future Plans

- Replace the hidden shortcut-button approach with native editable fields if HOI4 ever exposes moddable scripted callbacks for custom `editBoxType` elements.
- Add optional visual focus styling so the currently active manual-entry field is more obvious.
- Extend typed entry to any future advanced settings fields if they are surfaced in the UI.
