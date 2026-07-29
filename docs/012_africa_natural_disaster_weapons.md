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

The caller supplies all three hostile-actor proof inputs at one: `natural_disaster_call_caller_cost_checked`, `natural_disaster_call_caller_cooldown_checked`, and `natural_disaster_call_target_legitimacy_checked`.

## Outputs and cleanup

The host stores Event 013 result, reject reason, sequence ID, resolved family, primary job count, and skipped-primary count in `africa_last_natural_disaster_call_*` variables.

Accepted calls set `africa_natural_disaster_call_accepted` and mark the numeric resolved-primary-country target with `africa_natural_disaster_targeted`.

The target receipt flags used by scripted localisation are cleared when a new Rain or Drought action record starts, so a later result cannot inherit an earlier call's wording.

Rejected calls set `africa_natural_disaster_call_rejected` and record a bounded wrath increase as a backfire.

Accepted calls have a 20 percent bounded backfire chance that records `africa_natural_disaster_backfire_recorded` and increases ecological wrath.

Every attempted call starts the 180-day `africa_natural_disaster_weapon_cooldown` flag.

The normal `africa_cleanup_action` path clears `africa_natural_disaster_weapon_reserved` and the active reservation variable while retaining the action ledger's existing target cooldown, arrays, state flags, generation checks, and capacity restoration.

No global Event 013 target or recurring world loop is introduced.

## Tuning and player-facing surfaces

`common/script_constants/012_africa_action_constants.txt` adds the `africa_natural_disaster` integer tuning category with caller Event ID 12, 35 political power, 10 command power, a 180-day cooldown, a 20 percent backfire chance, and a five-point wrath backfire.

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

The Event 013 wrapper and contract files are unchanged and remain the source of truth for family availability, target-state eligibility, sequence planning, result semantics, and report/news presentation.

The Event 012 `strange-force` actions remain outside this integration and retain their existing documented formation-consumer gap.
