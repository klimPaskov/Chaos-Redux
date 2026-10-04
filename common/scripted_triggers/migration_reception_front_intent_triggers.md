# Receiver-front reception intent triggers

Source: [migration_reception_front_intent_triggers.txt](migration_reception_front_intent_triggers.txt).
Effects and storage: [migration_reception_front_intent_effects.md](../scripted_effects/migration_reception_front_intent_effects.md).

All predicates are hidden Boolean triggers.
They change no persistent state; some set unscoped temporary identity values that their callers own.

| Trigger | Scope | Purpose |
|---|---|---|
| `migration_reception_front_intent_arrays_are_aligned` | FRONT state | The row set is initialized with the current schema and all six arrays have the same length. |
| `migration_reception_front_intent_problem_qualifies` | Receiving COUNTRY, with event target `migration_reception_front_intent_origin` | The receiver already has a migration problem phase or enough incidents, or the request is large enough to reveal one. A tiny first request cannot reveal anything through intent alone. |
| `migration_reception_front_intent_identity_is_current` | ORIGIN state, with the six `migration_reception_front_intent_identity_*` temporaries | The origin's live evacuation contract matches the row exactly: front, generation, requester, receiver, cohort, a single live cohort with the requested amount, and a pending offer (requested or prepared) or an accepted operation (agreed) still within its deadline. |
| `migration_reception_front_intent_identity_front_is_current` | FRONT state, with the identity temporaries | The front is valid, owned and controlled by the recorded receiver, both actors exist, and a prepared row still has proven shelter and medical services. |
| `migration_reception_front_intent_cached_identity_is_current` | FRONT state | Loads the cached row into the identity temporaries and checks the front and the one exact origin. |
| `migration_reception_front_intent_is_visible_to_player` | FRONT state, `ROOT` is the viewing player | The viewer owns or controls the front and the cached row is current. |
| `migration_reception_front_intent_has_actual_map_context` | Any state | The state already has a real migration role (trapped, displaced, hosting, overcrowded, evacuating, returning, resettling, an outgoing evacuation corridor or its recent terminal). Intent never replaces that role. |

## Map-mode reader contract

The map-mode colour block and the scripted localisation run with the viewing player as `ROOT` and enter the rendered state as `FROM`, as described in the installed `common/map_modes/documentation.md`.
Readers call only `migration_reception_front_intent_is_visible_to_player` and `migration_reception_front_intent_has_actual_map_context`.
Those use the state's cached scalars, the six array lengths and one exact lookup of the cached origin state, including that origin's bounded neighbour check.
They never walk the rows, resolve a cohort, observe food, recalculate capacity or write anything persistent.
A foreign or public viewer fails the first check, so private intent, headcounts and capacity never leak.
