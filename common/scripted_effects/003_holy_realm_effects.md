# Holy Realm refuge-host selector

`holy_realm_select_weighted_refuge_host` runs in a country scope and publishes the regular country target `holy_realm_prefire_refuge_host`.
Its admission contract is the existing `can_host_holy_realm_refuge` trigger.
Tibet has priority while it exists and is admitted.
Bhutan and Nepal are admitted only when Tibet does not exist, and native `random_country` gives each admitted alternate the same chance.
This matches the route specification and the host-selection branches in the recorded repository revision `916646784f17088b84209ca9d61ad0abc3a7e3e9`.

The selector has no inputs, modifies no political or country setup state, and supplies no target when no country is admitted.
The root event validates both target presence and current admission before consuming it, preventing an empty selection from consuming a stale inherited pointer.
Regular target lifetime remains the native effect-chain lifetime.

Example:

```text
holy_realm_select_weighted_refuge_host = yes
if = {
	limit = {
		has_event_target = holy_realm_prefire_refuge_host
		event_target:holy_realm_prefire_refuge_host = { can_host_holy_realm_refuge = yes }
	}
	event_target:holy_realm_prefire_refuge_host = { country_event = { id = chaosx.nr3.2 days = 1 } }
}
```
