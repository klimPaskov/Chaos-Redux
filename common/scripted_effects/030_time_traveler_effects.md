# Time Traveler prefire selection

`time_traveler_select_weighted_prefire_host` runs in the calling country and builds a temporary country pool using the existing individual-crisis adjusted ticket weight.
It clears the pool at entry and exit, initializes the existing unscoped temporary `time_traveler_prefire_ready` output to zero, and sets that output to one only when a real country is selected and saved as the regular `time_traveler_prefire_host` event target.
An empty pool therefore reports failure even if the effect chain inherited an earlier target pointer.
Regular targets retain their native effect-chain lifetime; this helper introduces no global pointer.

`time_traveler_prepare_random_event_fire` delegates to the selector and exposes the same readiness output to the dispatcher.
The root event accepts an existing, extant host below the crisis cap, otherwise selects again, and schedules the visible event only after a successful readiness result.
Ticket counts, load adjustment, reservation duration, and visible-event timing remain owned by their existing constants and callers.

Example in a country scope:

```text
time_traveler_prepare_random_event_fire = yes
if = {
	limit = { check_variable = { time_traveler_prefire_ready = constant:individual_crisis_targeting.one } }
	country_event = { id = chaosx.nr30.1 }
}
```
