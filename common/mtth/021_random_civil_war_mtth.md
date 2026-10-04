# Event 021 evolution delay contracts

The three entries in `021_random_civil_war_mtth.txt` provide one sampled delay to the bounded evolution scheduler. The scheduler chooses the first active theater actor and evaluates `mtth:random_civil_war_evolution_i_days`, `mtth:random_civil_war_evolution_ii_days`, or `mtth:random_civil_war_evolution_iii_days` in that country scope; an absent selection falls back to the scheduler host. These are stored due-date delays, not native event daily MTTH hazards.

## Dynamic actor predicates

`event021_evolution_has_extra_active_actor` in `../scripted_triggers/021_random_civil_war_successor_triggers.txt` accepts the sampled country with a crisis id and returns true when the durable `global.random_civil_war_front_actors` roster contains two distinct active registered opposition actors from that crisis, each still fighting its own valid immediate opponent. It reads actor crisis, front-registration, front-id, role, and relation receipts. It has no outputs or side effects. An absent crisis id or incomplete live actor proof returns false. Example: `event021_evolution_has_extra_active_actor = yes` inside an MTTH modifier.

`event021_evolution_has_active_event6_actor` accepts the same scope and returns true when one registered, active, same-crisis actor with `random_civil_war_event6_front_active` still fights its immediate opponent. That live role flag is set on primary Event 006 openings and secondary Event 006 fronts; `random_civil_war_event6_secondary_origin` identifies only the latter and is not used as an eligibility gate here. The predicate does not rewrite Event 006 package identity or history and has no outputs or side effects. Example: `event021_evolution_has_active_event6_actor = yes` inside an MTTH modifier.

The Evolution I extra-actor and no-extra-actor factors use complementary results from the first predicate. Evolution II uses the Event 006 predicate for its independence-front and no-exposure clauses, and the extra-actor predicate for its multifront clause. The no-exposure clause still checks the existing border and sponsor routes. A dormant Event 006 route alone is no longer counted as a live extra participant.

## Tuning and lifecycle

All bases, factors, thresholds, and due-date clamps remain in `common/script_constants/021_random_civil_war_constants.txt`; this migration changes no coefficient. The two predicates read the current global registry and actor receipts at sampling time, so there is no new variable, flag, target, cached count, or cleanup task. The parent owns actor registration, front closure, and sibling preservation. The successor roster worker derives its local count from aligned active rows and never removes a global row while traversing it.

The selected actor must have `random_civil_war_crisis_id`. If the scheduler falls back to a country without that receipt, both predicates fail closed. The probability adapter did not discover these `common/mtth` entries as evaluable candidates in the saved baseline, so effective delay and same-scenario comparison remain unresolved until the connected route exposes a scenario set.
