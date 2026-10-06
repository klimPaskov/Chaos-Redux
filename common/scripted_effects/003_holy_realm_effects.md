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

## Refuge news publisher

`holy_realm_publish_refuge_news` runs in a country scope after the Holy Realm is formed and broadcasts `chaosx.news.9` once per campaign.
It sets `holy_realm_refuge_news_sent` before sending the major news event so repeated or forced formation branches cannot broadcast a second copy.
It has no inputs or outputs, and its only side effect is the global news receipt flag and a two-day delayed news broadcast.

## Pilgrimage escort cancellation

`holy_realm_cancel_pilgrimage_route_escort` runs in country scope when the targeted escort mission is cancelled or expires without its two divisions in the selected state.
It refunds the saved Political Power quote, Command Power, and Support Equipment, withdraws the mission's Black Friday purchase receipt when the source sale is still open, frees the teaching seat, clears the active-escort state, and applies the existing Defilements and Sangha Cohesion penalties.
Its active-state guard makes cleanup and refunds idempotent.
The caller records the native Black Friday price and sale receipt when the mission starts and calls this effect from both `cancel_effect` and the timeout failure branch; successful completion clears the saved amounts without refunding them.

Inputs are the country's active escort flag, saved PP quote, saved sale-credit flag/sequence, and the centralized escort CP/support-equipment constants.
It has no outputs.

## Bodhisattva Bhumi milestone rewards

`holy_realm_advance_bodhisattva_bhumi` awards its Political Power, Command Power, and Stability milestones once when the Bodhisattva first crosses the configured Bhumi thresholds.
The flags `holy_realm_bhumi_authority_reward_received`, `holy_realm_bhumi_awakened_reward_received`, and `holy_realm_bhumi_stability_reward_received` prevent later teaching and council actions from paying the same milestone again.
The thresholds and rewards are defined in `common/script_constants/003_holy_realm_constants.txt` under `holy_realm_buddhahood`.
# Manual refuge failure

`holy_realm_report_unavailable_refuge_host` runs in the requesting country scope after an explicit Settings request fails the refuge-host gate.
It sends `chaosx.nr3.5` and marks the shared `chaosx_manual_event_failure_shown` flag so the generic dispatcher does not send a second report.
It has no numeric inputs or outputs, creates no Realm, and changes no resources.
The Settings dispatcher owns the request context and invokes this helper only for a manual no-host or already-formed request.
The recipient is the existing human `chaosx_manual_event_requester` target, and its shared failure receipt prevents a second report from the generic dispatcher.

## Manual entry preparation

`holy_realm_prepare_event_fire` runs in country scope inside the Settings dispatch chain before its event gate and log entry.
Inputs are `event_id`, `events_log_manual_event_detail_trigger`, the caller-initialized `event_single_fire_allowed` output, and the existing requester target.
For an explicit Event 003 request, an already-formed Realm or the absence of an admitted host sets `event_single_fire_allowed` to zero and sends the owned failure report once.
Otherwise it saves the regular `holy_realm_prefire_refuge_host` target through the canonical selector.
The root event revalidates and reuses this target, and the Event Log can name that host before formation.
Other event ids and automatic requests have no preparation side effects.

```text
set_temp_variable = { event_single_fire_allowed = 1 }
holy_realm_prepare_event_fire = yes
```
