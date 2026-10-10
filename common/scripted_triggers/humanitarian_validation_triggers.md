# Humanitarian object validation

These neutral predicates validate the objects used by the separate famine, migration, and civilian-transfer owners.
They do not establish food pressure, persecution, a route, a cohort, a population transaction, or a policy consequence.

| Predicate | Scope and inputs | Result and defaults | Side effects |
| --- | --- | --- | --- |
| `humanitarian_country_is_valid` | Country scope, including a stored country or chain-local country target. | True only for a valid scope whose country actually exists and satisfies the shared special-country and normal-human-civilian classifiers. The Holy Realm is the one registered special country that passes, because its refuge, relief and reception run through the ordinary famine and migration owners. A dormant or annexed country fails even when its database scope remains resolvable. | None. |
| `humanitarian_state_is_valid` | State scope with current native `state_population_k`, OWNER, and CONTROLLER. | Requires a valid state scope, positive civilian population, and valid existing human owner and controller countries. Missing or invalid required objects fail closed. | None. |

`scope_exists` alone does not prove that a stored country exists in the game.
Installed trigger documentation states that variable scopes are always valid scopes and distinguishes country `exists` from scope existence.
The country predicate therefore requires both scope validity and `exists = yes` before applying the existing exclusions.

Usage in a state-scoped owner effect:

```text
if = {
	limit = {
		humanitarian_state_is_valid = yes
		OWNER = { humanitarian_country_is_valid = yes }
	}
	# The owner must still validate its own receipt, route, and transaction.
}
```

The predicates do not discover replacement countries or repair stale targets.
Existing owners retain responsibility for registry retirement, control-change cleanup, target refresh, and every transaction-specific proof.
