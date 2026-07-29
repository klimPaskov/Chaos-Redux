# Fallout tag preservation, technology regression, and fracture proof

## Source proof

The request snapshot stores every live country scope in `global.fallout_pretransition_countries`. `fallout_verify_pretransition_tags_preserved` checks that every frozen scope still exists and records the current transition generation before map return. No Fallout-owned effect calls `delete_country`. The postcondition does not require the old owner or old borders, so a tag can survive as a one-state remnant.

`fallout_reset_old_world_diplomacy` white-peaces every enemy pair and removes civil-war targets before the government phase. Its official readback requires no wars, no civil wars, no faction, no subjects, no exile, no truce, and no other proven old-world relation. The additional `fallout_transition_wars_stopped_complete` receipt stores the transition generation and is required by the full reset validator.

`fallout_regress_country_technology` runs over every frozen country before successor allocation. It uses the documented `set_technology` zero form to unresearch advanced families, restores the basic survival floor, and grants the emergency floor to majors and special Chaos countries. The country receipt and the global phase flag are required by map return.

The fracture effect builds a live conflict ledger from reserved Independence Wave template tags. It copies a template only when the tag is not live, transfers one random non-capital severe state from a random war-scarred multi-state country, sets a neutral emergency government, applies the Fallout package receipts, and runs the same technology regression. The effect does not load an Independence Wave focus tree.

## Engine-sensitive boundary

The offline Effects and Technology Modding references support `set_technology = { technology = 0 }`, but note failures for mutually exclusive technologies and database-object unlocks. The installed vanilla documentation does not provide a native `reset every technology` iterator, so the regression list is explicit and reviewed rather than pretending that a variable-only reset exists.

The installed documentation and existing mod precedents support `create_dynamic_country`, `reserve_dynamic_country`, `transfer_state`, `add_state_core`, `random_country`, `random_owned_state`, and event targets. They do not prove that a copied Independence Wave template, random border output, and successor package readback remain valid through the complete Fallout transaction. The fracture release flag is therefore unset by default. Enabling it without live proof is a blocker, not an acceptable static-border fallback.

## Runtime proof still required

- one complete Fallout transition with every original tag still live after map return
- one complete transition with all old wars stopped before state ownership changes
- major and special Chaos technology readback showing the emergency floor
- ordinary country readback showing the four-technology floor and advanced-tech removal
- two Fallout triggers with different fracture source states and different borders
- dynamic output has no Independence Wave focus tree and receives Fallout-owned package and AI wiring

Hearts of Iron IV was not run.
