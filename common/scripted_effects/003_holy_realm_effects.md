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

## Refuge reception and refuge credit

`holy_realm_open_refuge_reception`, `holy_realm_register_refuge_reception` and `holy_realm_close_refuge_reception` run in country scope and write the Realm's reception policy through the migration owner's `migration_decision_set_policy` (humanitarian open, controlled and closed).
The formation event's three refuge choices, `THR_open_refuge_roads` and `THR_close_refuge_roads` call them.
The Realm never writes a migration ledger, and `humanitarian_country_is_valid` admits the Holy Realm so the migration owner accepts the request.
`THR_open_refuge_roads` and `THR_close_refuge_roads` read `migration_reception_policy_is_humanitarian_open` instead of a private refuge flag.

`holy_realm_collect_refuge_credit` runs from the daily doctrine pulse and reads the migration-owned `migration_integrated_population`.
Each full block of `holy_realm_refuge.integration_people_per_credit` people who settled since the last payment eases Compassion Drift and raises Spiritual Legitimacy once, up to `credits_per_pulse_cap` blocks per pulse.
The Realm keeps its own paid total in `holy_realm_refuge_credited_population`, whose first value is the integrated total on the first pulse, so earlier integrations never pay.

## Condemnation for coercion

`holy_realm_condemn_coercion` runs in the Realm's country scope with `holy_realm_condemnation_gain` and, when there is one, `condemnation_victim_country`.
It submits an atrocity-bucket public source through `condemnation_add_source`.
`THR_prepare_forced_integration` (victim named) and `THR_mandate_kneeling_province` call it with the `holy_realm_condemnation` gains.

## Foreign answers to the final warnings

`holy_realm_foreign_prepare_containment`, `holy_realm_foreign_send_final_envoy` and `holy_realm_foreign_evacuate_cities` run in the country scope of a foreign responder and are the three options of `chaosx.nr3.76`.
Containment is also the effect of `THR_build_mountain_containment` and raises the Realm's Final Silence Pressure and balance toward Final Silence.
The envoy lowers the Realm's pressure, moves its balance toward the Vow and earns its goodwill.
Evacuation submits a flight request through `migration_request_flight_pressure` for the capital and the large-city states (`holy_realm_foreign_marked_city_state`), using the share in `holy_realm_event.evacuation_population_share`.
A disruption of the final network lowers Final Silence Pressure further for a country that prepared containment.

## Manual Final Silence terminal sequence

`trigger_final_silence_scenario` in `chaosx_triggerable_scenarios_effects.txt` calls `holy_realm_prepare_final_silence` and the existing state-wave helpers in country scope.
This manual route is separate from `holy_realm_complete_terminal_final_silence`, whose natural ritual still requests Fallout.

- Inputs: the launcher country and `triggerable_scenarios_final_silence_type`, defaulting to the nuclear type through scenario initialization.
- Setup: the wrapper establishes Holy Realm identity, armed doctrine, doctrine memories, Pressure and Mandala Reach from `triggerable_scenario_final_silence` constants, and the temporary thermonuclear selection flag.
- Outputs and side effects: preparation sets `world_end`, `world_end_final_silence`, the variant flag, zeroes the global wave counter, invokes existing world-end faction cleanup, records Chaos and condemnation, reports unconventional use, locks contamination at `100%`, refreshes threat, and presents terminal super-event slot `9` through the shared audio route.
- State processing: the four regional waves use the existing `holy_realm_final_silence` tuning. Nuclear losses are `75%` and thermonuclear losses are `95%`. Non-Realm target states receive Deaths, fallout, building removal, wasteland and strike receipts. Realm states receive visual strikes and fallout without the lethal wave processing.
- Callbacks: `.nr3.73` supplies foreign witness reports, `.nr3.82` advances the wave after `wave_days`, `.nr3.84` drains visual strikes, `.nr3.90` reports completion, and `chaosx.triggerable_scenarios.5` acknowledges the manual launch.
- Cleanup: a fresh manual launch clears stale completed/interrupted terminal receipts before preparation, including the receipt left by a superseded natural Fallout request. The temporary scenario thermonuclear flag is cleared after scheduling. Strike and visual-queue state flags retain their original duplicate-processing guards. `holy_realm_interrupt_final_silence` retains the original interruption cleanup. No new event target is introduced.
- Fallout coexistence: its legacy migration excludes `air_contamination_final_silence_locked`, preserving this sequence across recovery. The gradual-air Fallout evaluator also excludes this lock, including after the original interruption path clears `world_end`. The manual wrapper cancels an uncommitted Fallout envelope and retires preterminal sweep/countdown callbacks before preparing the old terminal sequence. Normal Fallout completion and its own manual scenario remain unchanged.

Example: choose scenario `4` and the nuclear or thermonuclear type, then confirm the launch through `trigger_selected_chaosx_scenario`.
The intensity slider does not alter the canonical Final Silence sequence.
