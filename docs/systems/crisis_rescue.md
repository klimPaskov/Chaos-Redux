# Crisis Rescue Event Weighting

The crisis-rescue registry gives selected event chains a bounded weight floor when their registered country approaches capitulation.

The implementation lives in `common/scripted_effects/crisis_rescue_effects.txt`. It remains separate from the generic dynamic-effect registry because it owns one event-system subsystem, its aligned country and event-ID arrays, and its registration lifecycle.

## Runtime flow

1. `initialize_crisis_rescue_registry` clears the aligned registry arrays and calls `register_default_crisis_rescue_targets`.
2. A country registers through `register_crisis_rescue_target` after supplying a positive `crisis_rescue_event_id` temporary variable.
3. `apply_crisis_rescue_event_weight_adjustments` walks only the registered countries.
4. A country that satisfies `chaosx_near_capitulation_crisis_rescue_candidate` receives the temporary rescue-pressure marker.
5. Its mapped event weight is raised only when it is below the floor derived from `global.default_event_weight` and `constant:chaosx_crisis_rescue.event_weight_multiplier`.

## Script contract

Scope: the event-system coordinating scope.

Inputs:

- `global.crisis_rescue_countries`
- `global.crisis_rescue_event_ids`
- `global.default_event_weight`

Outputs and side effects:

- May update a registered event through `set_event_weight`.
- Sets `chaosx_near_capitulation_rescue_pressure` on a country currently receiving the floor.
- Does not scan unregistered countries or create a separate timer.

Example registration:

```txt
TIB = {
	set_temp_variable = { crisis_rescue_event_id = constant:holy_realm_event_log.event_id }
	register_crisis_rescue_target = yes
}
```

## Assets

This subsystem has no dedicated icons or sprites. It changes event selection weights without adding a player-facing interface.

## Future plans

Additional rescue candidates should register through the existing aligned arrays. A future UI surface could expose active rescue pressure, but it should read the same registry rather than introduce a parallel mechanic.
