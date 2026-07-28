# Event 006 IW-035 — Livonia vanilla-route overlay adapter

## Status

`PARTIAL` — bounded source implementation is present, but the adapter is not admitted as a complete Event 006 country package or as proof that the full route-overlay matrix is complete.

## Source contract

IW-035 observes the vanilla Lithuanian focus `LIT_claim_livonia_monarchy` in `common/national_focus/lithuania.txt` around lines 4633–4706. That route keeps the living `LIT` tag, sets cosmetic identity `LIVONIA`, and adds Baltic cores; it does not create a dynamic country. The adapter therefore gates on `tag = LIT` plus `has_cosmetic_tag = LIVONIA` and uses a narrow `on_daily_LIT` hook. It does not register a tag, create history, transfer a state, change autonomy, overwrite the Lithuanian focus tree, or create a flag, portrait, or advisor asset.

## Files added

- `common/script_constants/006_independence_wave_iw035_livonia_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw035_livonia_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw035_livonia_effects.txt`
- `common/ideas/006_independence_wave_iw035_livonia_ideas.txt`
- `common/on_actions/006_independence_wave_iw035_livonia_on_actions.txt`
- `common/decisions/categories/006_independence_wave_iw035_livonia_categories.txt`
- `common/decisions/006_independence_wave_iw035_livonia_decisions.txt`
- `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`

## Implemented surface

The exact living cosmetic carrier receives three visible values — Rail Coordination, Civic Legitimacy, and Coastal Security — with centralized caps, gains, losses, and AI weights. Five actions spend concrete command power, manpower, trains, infantry equipment, support equipment, and army experience: Baltic rail ledgers, coastal watch, an expiring Livonian corridor mission, a Baltic municipal charter, and a federal coastal compact. Four lifecycle ideas expose contested administration, coordinated rail authority, municipal charter, and federal coastal settlement. The corridor mission has explicit availability, timeout, cancellation, failure, completion, AI, and anchor-control effects. The adapter records a narrow overlay-active flag plus state-12/archetype/force profile for future shared systems.

## Preservation and safety

The route is additive and only activates while the country is still `LIT` with cosmetic tag `LIVONIA`. On route loss it removes its ideas, clears its active flags, and pauses the watch state. No country creation, state assignment, autonomy rewrite, free-unit loop, or unconditional Event 006 focus-tree load is performed.

## Validation evidence

- New script blocks and localisation were checked for balanced braces/quotes; the localisation file is UTF-8 with BOM.
- The touched scripts contain no unsupported literal `<=` or `>=` operators.
- `hoi4.probability_inspect` read the decision source with the `decision_ai_will_do` adapter and returned `PROBABILITY_SOURCE_INSPECTED` with validation passed, four discovered weighted candidates, and no unresolved source diagnostics. The `mission_ai_will_do` read likewise passed with one weighted mission candidate and no unresolved source diagnostics. Both pools require a world-state scenario for runtime evaluation and no such evidence is claimed.
- No HOI4 process was launched. No live save/load, runtime, AI, or scenario evidence is claimed.

## Remaining acceptance work

This bounded adapter does not yet provide a safe way to insert the shared Event 006 focus framework into a meaningful living LIT tree. Network, patron, league, formable, host-survival, save/load cleanup, symbol/leader clearance, and live carrier evidence remain open. The overall route-overlay acceptance item therefore remains unchecked; nine other exact vanilla route-overlay adapters are still absent, and the Event 006 completion audit remains `HOLD/PARTIAL`.
