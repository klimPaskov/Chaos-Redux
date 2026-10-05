# Hostile capture adapter

Source: [humanitarian_capture_effects.txt](humanitarian_capture_effects.txt).
Predicates: [humanitarian_capture_triggers.md](../scripted_triggers/humanitarian_capture_triggers.md).
Tuning: [humanitarian_capture_constants.txt](../script_constants/humanitarian_capture_constants.txt), category `humanitarian_capture_pressure`.
Caller: `on_state_control_changed` in `common/on_actions/humanitarian_runtime_on_actions.txt`.

Ordinary wars, including wars started by event owners such as civil wars and collapse wars, create refugees and occupation hunger through this adapter without editing those owners' files.

## `humanitarian_handle_hostile_capture`

Scope: the STATE whose controller just changed (`FROM.FROM` of `on_state_control_changed`).
Input: event target `humanitarian_capture_new_controller`, saved from the callback's `ROOT` before the state scope is entered.
Output: temporary `humanitarian_capture_result`, 1 when the capture was answered; callers that read it declare it first.

The flight calculator declares `famine_occupation_profile` before resolving occupation conduct, so the returned conduct survives the helper call and can override ideology affinity.

Steps:

1. Save the state's owner as `humanitarian_capture_owner`.
2. Require `humanitarian_capture_is_hostile`: the new controller holds the state, is at war with the owner, and is not the owner, a faction partner of it, its overlord or its subject.
3. Require `humanitarian_capture_state_is_eligible`: the state has more than `minimum_state_population_k` thousand people and is past its capture cooldown.
4. Start the per-state cooldown: `humanitarian_capture_cooldown_until_date` becomes today plus `cooldown_days`, converted to date units through `chaosx_convert_days_to_date_offset`.
5. Compute the flight request with `humanitarian_capture_calculate_flight_request`.
6. When the request reaches `minimum_request_people`, submit it through `migration_request_war_pressure` with proven request and actor flags.
7. Queue one `famine_enqueue_food_observation_assessment`, so the famine owner reads the occupation law and decides whether a real food problem exists.
8. Clear the request envelope on every exit.

The adapter adds no famine stage and no deaths, moves nobody and grants no route or capacity.
Flight pressure is handled afterwards by the existing spontaneous movement, reception and trapped-population owners, which apply their own route, floor and death rules.
A liberation, meaning the owner regains control, or a handover to an ally adds no flight; the existing return paths act on their own.
The only per-callback work is the changed state's own checks and one food-observation registration; there is no world, country or registry scan.

## `humanitarian_capture_calculate_flight_request`

Scope: the captured STATE with both capture event targets saved.
Output: temporary `humanitarian_capture_request_people`, declared by the caller.

`request = population * base_population_fraction * clamp(multiplier, minimum_multiplier, maximum_multiplier)`, capped at the population above `protected_origin_share`.

The multiplier starts at `neutral_multiplier` and is adjusted once for conduct and once for ideology:

| Evidence | Adjustment |
|---|---|
| Protective occupation profile | `protective_conduct_adjustment` |
| Extraction or forced-labour profile | `harsh_conduct_adjustment` |
| Collective punishment, population transfer or exterminatory profile | `brutal_conduct_adjustment` |
| Shared ruling ideology and no harsh conduct | `shared_ideology_adjustment` |
| Fascist or communist occupier of a country with another ideology | `hostile_ideology_adjustment` |

Conduct comes from `famine_resolve_occupation_profile`, which reads the state's current occupation law; a state without occupation data resolves to no profile and only ideology applies.
Harsh conduct overrides the calming effect of a shared ideology, following the specification's rule that actual policy outweighs abstract ideology.
The base share follows the committed `on_nuke_drop` population-fraction precedent.

## Presentation

The request records `war` as the state's latest pressure source, which the migration map mode and reports already label.
No new localisation, icon or report is needed.
