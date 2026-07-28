# Event 006 IW-059 — Mesopotamia vanilla-formable overlay adapter

## Status

`PARTIAL` — the bounded additive source adapter is implemented and statically checked, but it is not admitted as a complete Event 006 country package or as proof that the full route-overlay matrix is complete.

## Source contract

IW-059 observes the vanilla `neo_mesopotamia_decision` formable in `common/decisions/formable_nation_decisions.txt` around lines 17655–17838. The vanilla route keeps the carrier's original tag, assigns the `neo_mesopotamia` cosmetic identity, adds the listed Mesopotamian cores, and sets `neo_mesopotamia_formed_flag`. The adapter therefore requires that formed flag, the cosmetic identity, and one of vanilla's allowed original tags (`KUR`, `IRQ`, `SYR`, `PAL`, `EGY`, `KUW`, `LEB`, or `ASY`). It never creates a tag, transfers a state, rewrites autonomy, or replaces the carrier's existing tree or history.

## Files added

- `common/script_constants/006_independence_wave_iw059_mesopotamia_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw059_mesopotamia_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw059_mesopotamia_effects.txt`
- `common/ideas/006_independence_wave_iw059_mesopotamia_ideas.txt`
- `common/decisions/categories/006_independence_wave_iw059_mesopotamia_categories.txt`
- `common/decisions/006_independence_wave_iw059_mesopotamia_decisions.txt`
- `common/on_actions/006_independence_wave_iw059_mesopotamia_on_actions.txt`
- `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`

## Implemented surface

The formed carrier receives three visible values — River Logistics, Civic Legitimacy, and Provincial Autonomy — with centralized caps, route-specific gains/losses, concrete military and economic costs, and AI weights. Five actions cover a Baghdad civic cabinet, Tigris depot security, river officer integration, a timed Baghdad river-guard mission, and a constitutional compact that also records minority guarantees. Four lifecycle ideas expose contested administration, integrated river authority, minority guarantees, and the constitutional compact. The mission requires control and a garrison in state 291 and has explicit activation, availability, timeout, cancellation, failure, completion, and narrow pause/resume handling. The adapter records state 291, the river/corridor archetype, and river-jungle force profile for shared Event 006 systems.

## Preservation and safety

No decision creates units, country tags, flags, portraits, advisors, history, or focus content. The adapter is invoked only by exact original-tag daily hooks for the vanilla-allowed carriers and suspends its overlay if the formed identity is lost. It does not bypass vanilla formable cores or the global formation flag.

## Validation evidence

- All eight new source files have balanced braces and quotes and no unsupported literal `<=` or `>=` operators.
- The localisation file is UTF-8 with BOM.
- `python -B .tools/audit_event6_allocator.py` passes the exact 3/4/5/7/10 allocator, World Collapse 10, scenario modes/intensities, reservation order, and Event-005 collision order.
- `hoi4.probability_inspect` with `decision_ai_will_do` found four weighted decision candidates, validation passed, and zero unresolved source diagnostics. The `mission_ai_will_do` read found one weighted mission candidate with validation passed and zero unresolved diagnostics. Both pools require a world-state scenario for runtime evaluation; no runtime claim is made.
- No HOI4 process was launched. No live save/load, AI, scenario, package-admission, or formation evidence is claimed.

## Remaining acceptance work

The shared Event 006 focus framework has not been safely inserted into the meaningful carrier tree. Network, patron, league, host-survival, formable-readiness, symbol/leader clearance, save/load cleanup, and live carrier evidence remain open. IW-059 remains a non-selectable overlay-only route and does not close the remaining vanilla overlay matrix.
