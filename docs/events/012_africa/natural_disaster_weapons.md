# Event 012 hostile nature calls

Event 012 reuses the existing high-chaos actions `petition_the_rain` (69) and `defy_the_drought` (70) as bounded hostile nature weapons when a full action resolves against the exact selected enemy country.

Both actions use the shared timed-country/country target contract so human and AI selection pass the same selected enemy into the action record and Event 013 call.

## Runtime contract

`africa_natural_disaster_weapon_actor_is_eligible` is a host-country scripted trigger in `common/scripted_triggers/012_africa_triggers.txt`.

It requires Evolution III, a completed priority-member package with ecological pressure above the covenant threshold, or a documented covenant-nature package through `africa_covenant_route_committed`, `africa_covenant_favour_and_wrath`, `africa_covenant_write_warfare_doctrine`, or `africa_covenant_route_capstone`.

`africa_natural_disaster_weapon_target_is_valid` is evaluated on the existing `event_target:africa_action_target` and requires a distinct country that is at war with the Event 012 host.

`africa_natural_disaster_weapon_cost_is_available` checks the additional political-power and command-power reserve and rejects a host-side cooldown or in-flight reservation.

`africa_reserve_natural_disaster_weapon_cost` runs before the shared action quote is paid and stores the reservation in `africa_active_action_natural_disaster_cost_reserved` on the existing action record.

`africa_call_hostile_natural_disaster_from_action` runs only on a full result for action 69 or 70.

The helper saves the selected action target as `natural_disaster_call_target_country`, then calls the public Event 013 `call_natural_disaster = yes` wrapper in the exact selected-country scope.

The caller sets `natural_disaster_call_caller_type = hostile_actor`, Event ID 12, a random Event 013 family, random family group, selected-country mode, target-supplied proof, a single sequence, meaningful news, affected-country reporting, normal aftermath, family chaining, and Event 013 history logging.

Event 013 may reject the random family when the selected enemy has no eligible controlled state, so the selected-country target remains exact without silently widening to another country.

Severity is severe for `petition_the_rain`, regional for `defy_the_drought`, a fully promoted priority sovereign package, or the documented warfare-doctrine path, and catastrophic for the covenant route capstone.

`africa_prepare_hostile_natural_disaster_strength` converts the live host route floor, reserved nature-call payment, drought action, ecological wrath bands, and continental war-readiness bands into actor strength, then adds a bounded selected-target factory/state adjustment so a major enemy is not normalised to the same impact envelope as a minor enemy.

The helper writes the Event 013 public scales before `call_natural_disaster = yes`: deaths increase by 0.20 per strength point above the base, building damage by 0.18, warning chance by 0.05, recovery burden by 0.15, and supply disruption by 0.20.

The warning increment is deliberate signal visibility rather than damage; higher-impact calls give the affected country a larger warning multiplier while deaths, damage, recovery burden, and supply disruption still rise with strength.

All five scales are clamped to Event 013's shared 0.25 to 4.00 range, so a stronger Africa actor produces a quantitatively stronger random disaster without changing Event 013's family pool, exact target, sequence policy, or rejection behavior.

The caller supplies all three hostile-actor proof inputs at one: `natural_disaster_call_caller_cost_checked`, `natural_disaster_call_caller_cooldown_checked`, and `natural_disaster_call_target_legitimacy_checked`.

## Outputs and cleanup

The host stores Event 013 result, reject reason, sequence ID, resolved family, primary job count, and skipped-primary count in `africa_last_natural_disaster_call_*` variables.

The host also stores the attempted call's calculated strength in `africa_last_natural_disaster_call_strength`, including when Event 013 rejects the exact target because no eligible controlled state exists.

Accepted calls set `africa_natural_disaster_call_accepted`, mark the numeric resolved-primary-country target with `africa_natural_disaster_targeted`, and copy the current `africa_host_generation` onto that target. The same accepted result records the member-disaster disqualifier when the target is already a current-generation Charter member or cooperative partner, and records the neutral-African disqualifier when the target is an African sovereign with an outside relationship.

When the marked target later capitulates directly to the same Event 012 host generation, the `on_capitulation` owner calls `africa_achievement_record_weather_army_defeated` on that distinct target and opens the weather-war milestone through `africa_achievement_record_weather_war_won`. A host transfer, peace conference, or third-party victory cannot satisfy this owner.

The target receipt flags used by scripted localisation are cleared when a new Rain or Drought action record starts, so a later result cannot inherit an earlier call's wording.

Rejected calls set `africa_natural_disaster_call_rejected` and record a bounded wrath increase as a backfire.

Accepted calls have a 20 percent bounded backfire chance that records `africa_natural_disaster_backfire_recorded` and increases ecological wrath. After the host meter is clamped, reaching `africa_achievement_ratio.ecological_rampage_threshold` records `africa_achievement_ecological_wrath_collapse`, which is a lifetime disqualifier for the weather achievement.

Every attempted call starts the 180-day `africa_natural_disaster_weapon_cooldown` flag.

The normal `africa_cleanup_action` path clears `africa_natural_disaster_weapon_reserved` and the active reservation variable while retaining the action ledger's existing target cooldown, arrays, state flags, generation checks, and capacity restoration.

No global Event 013 target or recurring world loop is introduced.

## Tuning and player-facing surfaces

`common/script_constants/012_africa_action_constants.txt` contains the `africa_natural_disaster` integer caller ledger and the `africa_natural_disaster_strength` fixed-point ladder for route floors, pressure/war bands, target-size thresholds, and the five Event 013 scale increments.

`localisation/english/012_african_union_l_english.yml` documents the hostile-war gate, extra ritual payment, cooldown, and backfire in the existing action descriptions and adds accepted/rejected call strings.

`common/scripted_localisation/012_africa_scripted_localisation.txt` selects those accepted/rejected strings from the target receipt flags while retaining the normal action result text when no hostile call was made.

The shared Event 012 action ledger icon and existing action decision surfaces remain the only UI assets; no new icon, sprite, GFX definition, tag, model, or entity is required.

The two selector decisions are visible only for an eligible nature host that is at war; resource, exact-target, and cooldown checks remain authoritative when the action starts.

## AI parity

`africa_ai_selected_target_is_candidate_for_action` has a dedicated branch for actions 69 and 70 that uses the same host eligibility, war, cost, cooldown, and exact enemy-target gate as human execution.

The generic bounded-roster fallback excludes both actions, so the AI cannot select a peaceful or non-nature target and rely on a weaker downstream failure.

## Limitations and follow-up

The implementation deliberately reuses actions 69 and 70 and does not reinterpret `weaponise_fictional_pathogen` (73) as a weather family because Event 013 has no pathogen family.

Partial and failed Event 012 action outcomes do not call Event 013; only a full action result consumes the reserved hostile nature payment.

The Event 013 wrapper and contract files are unchanged and remain the source of truth for family availability, target-state eligibility, scale bounds, sequence planning, result semantics, and report/news presentation.

The Event 012 `strange-force` actions remain outside this integration and retain their existing documented formation-consumer gap.

## Strength boundary

Disaster severity is earned through the existing promotion, constitutional, ecological, war-readiness, payment, and target-size receipts. It is never derived from ethnicity, a tribal label, or an unreviewed cultural stereotype. A promoted sovereign or covenant route can therefore deliver a stronger call because its documented political and ecological authority is higher, while every call still targets one selected enemy and remains bounded by the Event 013 contract.
