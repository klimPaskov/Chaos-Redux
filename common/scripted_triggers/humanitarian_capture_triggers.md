# Hostile capture triggers

Source: [humanitarian_capture_triggers.txt](humanitarian_capture_triggers.txt).
Consumer: [humanitarian_capture_effects.md](../scripted_effects/humanitarian_capture_effects.md).

All four predicates are hidden Boolean triggers with no side effects.

| Trigger | Scope | True when |
|---|---|---|
| `humanitarian_capture_is_hostile` | Captured STATE, with event targets `humanitarian_capture_new_controller` and `humanitarian_capture_owner` | The new controller now holds the state, is at war with its owner, and is not the owner, a faction partner, the owner's overlord or the owner's subject. |
| `humanitarian_capture_state_is_eligible` | STATE | The state has more than `humanitarian_capture_pressure.minimum_state_population_k` thousand people and its `humanitarian_capture_cooldown_until_date` is absent or reached. |
| `humanitarian_capture_occupier_shares_owner_ideology` | New controller COUNTRY, with event target `humanitarian_capture_owner` | Both countries have the same ruling ideology. |
| `humanitarian_capture_occupier_ideology_is_hostile` | New controller COUNTRY, with event target `humanitarian_capture_owner` | The occupier is fascist or communist and does not share the owner's ruling ideology. |
