# Event 006 IW-025 — Vojvodina vanilla-route overlay adapter

## Status

`PARTIAL` — bounded source implementation is present, but the adapter is not admitted as a complete Event 006 country package or as proof that the full route-overlay matrix is complete.

## Source contract

IW-025 observes the vanilla Yugoslav route that creates a dynamic country from `HUN`, adds the Vojvodinian anchor core, transfers state 45, assigns the cosmetic carrier `vojvodina`, and puppets the carrier. The source is the vanilla `create_dynamic_country` block in `common/national_focus/yugoslavia.txt` around lines 1558–1576. The implementation does not register a tag, create history, transfer a state, change autonomy, overwrite the vanilla Yugoslav focus tree, or create a flag, portrait, or advisor asset. Vanilla dynamic-country carriers are constrained to the `D01`–`D50` range, so the adapter shares the existing narrow D01-D50 hook table with IW-022 and exact identity triggers instead of using a world iteration.

## Files added

- `common/script_constants/006_independence_wave_iw025_vojvodina_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw025_vojvodina_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw025_vojvodina_effects.txt`
- `common/ideas/006_independence_wave_iw025_vojvodina_ideas.txt`
- `common/decisions/categories/006_independence_wave_iw025_vojvodina_categories.txt`
- `common/decisions/006_independence_wave_iw025_vojvodina_decisions.txt`
- `localisation/english/006_independence_wave_iw025_vojvodina_l_english.yml`

The existing `common/on_actions/006_independence_wave_iw022_dalmatia_on_actions.txt` now calls both route refresh effects from every D01-D50 hook. A second definition of the same on-action key was deliberately avoided so one adapter cannot shadow the other.

## Implemented surface

The exact HUN-origin carrier receives three visible values — River Logistics, Provincial Legitimacy, and Border Mobility — with centralized caps, gains, losses, and AI weights. Five actions spend concrete command power, manpower, trains, infantry equipment, support equipment, and army experience: Danube depot survey, mounted frontier reserve, an expiring Vojvodina border-watch mission, a municipal minority charter, and a federal agrarian compact. Four lifecycle ideas expose contested administration, coordinated grain authority, municipal guarantees, and federal frontier settlement. The watch mission has explicit availability, timeout, cancellation, failure, completion, AI, and anchor-control effects. The adapter records a narrow overlay-active flag plus the state-45/archetype/force profile for future shared systems.

## Preservation and safety

The route is additive and only activates while `is_dynamic_country = yes`, `original_tag = HUN`, and `has_cosmetic_tag = vojvodina` are all true. On route loss it removes its ideas, clears its active flags, and pauses the watch state. No country creation, state assignment, autonomy rewrite, free-unit loop, or unconditional Event 006 focus-tree load is performed.

## Validation evidence

- New script blocks and localisation were checked for balanced braces/quotes; the localisation file is UTF-8 with BOM.
- The touched scripts contain no unsupported literal `<=` or `>=` operators.
- `hoi4.probability_inspect` read the decision source with the `decision_ai_will_do` adapter and returned `PROBABILITY_SOURCE_INSPECTED` with validation passed, four discovered weighted candidates, and no unresolved source diagnostics. The `mission_ai_will_do` read likewise passed with one weighted mission candidate and no unresolved source diagnostics. Both pools require a world-state scenario for runtime evaluation and no such evidence is claimed.
- No HOI4 process was launched. No live save/load, runtime, AI, or scenario evidence is claimed.

## Remaining acceptance work

This bounded adapter does not yet provide a safe way to insert the shared Event 006 focus framework into a meaningful living YUG tree. Network, patron, league, formable, host-survival, save/load cleanup, and live carrier evidence remain open. The overall route-overlay acceptance item therefore remains unchecked; ten other exact vanilla route-overlay adapters are still absent, and the Event 006 completion audit remains `HOLD/PARTIAL`.
