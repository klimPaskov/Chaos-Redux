# Reception preparation predicates

These read-only predicates install nothing and debit no resources.

| Helper | Scope | Inputs and result |
| --- | --- | --- |
| `migration_reception_preparation_target_cost_is_affordable` | COUNTRY | Mandatory temporary `migration_transport_target` exact STATE pointer, same inclusive support and standard fuel/conditional convoy quote, used by the effect with its saved preparation target. |
| `migration_reception_preparation_is_visible` | COUNTRY | Exact parent-owned pending reception issue, or existing active/emerging material origin problem with insufficient current capacity; quiet countries and resolution-only countries fail. |
| `migration_reception_preparation_is_affordable` | COUNTRY | UI wrapper with exact selected FROM state, support equipment at least its constant and inclusive standard transport fuel/conditional sea-convoy quote, with no political-power requirement. |
| `migration_reception_preparation_state_is_safe` | STATE | Positive human state, current food receipt at stable stage, native route facts and all existing hazards clear, and consistent candidate flag/array membership. |
| `migration_reception_preparation_can_change_state` | STATE | At least one missing or undersized valid shelter or medical service.
Unchanged installed services fail, and preparation consumes the current admission law. |
| `migration_reception_preparation_target_is_valid` | STATE | ROOT is the acting receiver; exact owned/controlled safe state, visible issue and civilian factories; pending requests accept only their exact mirrored front. |

The emerging branch requires the existing reveal threshold and an actual owned displacement state with positive flight/trapped pressure.
It permits first internal paid preparation without exposing a quiet country.
The state safety gate retains the original explicit `NOT migration_population_trapped` exclusion.
Food observation is effect-owned and is never performed in a visibility/target trigger.
The paid effect independently reobserves and rechecks these facts at execution, so a UI cache does not authorize spending or admission.
No threshold, service guarantee or public meter is added.
The selected-state cost contract is documented in `../scripted_effects/migration_transport_cost_effects.md`.

The UI wrapper initializes `migration_transport_target = FROM` before its bare helper call.
The paid effect initializes that pointer from the saved exact preparation state.
The target-cost predicate initializes all three standard profile amounts from their existing constants before calling the shared affordability helper.
These inputs are temporary and unscoped, and no trigger publishes persistent gameplay state.

## Explicit action context

Scope-sensitive bodies have one `_in_context` implementation reading the mandatory unscoped temporary COUNTRY pointer `humanitarian_action_actor` and STATE pointer `humanitarian_action_target`.
The original helper name is a compatibility wrapper initializing those inputs from ROOT and FROM before a bare `= yes` call when no explicit context is proven.
A caller that supplies an explicit envelope also initializes temporary `humanitarian_action_context_proven = 1`, so nested legacy wrappers retain that exact actor and target.
Panel gates initialize the actor from their country context and the target from the exact selected state, and an immediate country event establishes the actor as ROOT for deep owner helpers.
These helpers accept no named arguments, have no implicit scope defaults, and publish no additional gameplay output beyond their documented owner body.
These adapters do not change tuning or create independent transaction owners.
See [the shared action lifecycle](../scripted_effects/humanitarian_gui_action_effects.md) for caller, pending, and cleanup contracts.
