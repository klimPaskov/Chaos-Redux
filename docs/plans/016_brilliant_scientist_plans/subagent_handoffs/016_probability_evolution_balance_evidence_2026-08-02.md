# Event 016 evolution and foreign-AI probability evidence

Date: 2026-08-02

## Scope

This is a read-only weighted-logic evidence tranche for the four logged evolution events and the foreign operation decision surface. It does not change gameplay, choose a new balance target, produce an asset, or create a model. It records the analyzer's bounded results so future tuning can use named states without presenting incomplete pools as normalized probabilities.

## Evolution surface

`hoi4.probability_inspect` inspected `events/016_brilliant_scientist_evolutions.txt` with the `event_option_ai_chance` adapter. The source was accepted with 18 discovered candidates, 9 required inputs, and one unresolved source input. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31d98b6469875bb8374ad5d798fa076e2041d5a53962232dd4211fc6bc77a282/34a92a927d28d6c1346babf9102e2ab8bd9a2a265394eaf003b76bcfcc07243a/probability-inspect-991079c10600.json`.

The four-state evaluation used the named scenario set `event016_evolution_route_matrix` with public-university peaceful, secret-militarized wartime, industrial-colonial, and refugee-threatened states over a 365-day horizon. The adapter returned `PROBABILITY_ANALYZED_PARTIAL`, 72 candidate-state projections, and 47 unresolved or bounded analysis items. Because the candidate pool is not proven complete, the result is a modifier and ranking diagnostic, not a normalized click chance or an MTTH claim. The authoritative JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c78cdc232be5cdd73e1cd687d97f0d8cdba02617f8836541ef28bd7d442c7c16/191482b99cb0041808abc41e75d27a5cc63bb185649b720063d49514c90bf65b/probability-765fc96522ac314a39e4a77c.json`; linked ranking and matrix SVG/PNG views are retained with that result.

The analyzer explicitly kept unsatisfied host-archetype and evolution modifiers visible rather than assuming that a supplied state activated them. This is a useful input-model limitation: the next scenario pass must use the adapter's accepted state vocabulary for country flags and evolution ledger variables before any ordering claim is made.

## Foreign-operation surface

`hoi4.probability_inspect` inspected `common/decisions/016_brilliant_scientist_foreign_decisions.txt` with the `decision_ai_will_do` adapter. The source parsed cleanly with three discovered weighted candidates, eight required inputs, and zero unresolved source diagnostics. The pool is intentionally incomplete because target eligibility and world state are runtime-dependent, so no normalized decision probability is claimed. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bae41df915a513cf153c204919f8ebdc1c6c59313194abbe4e39cdbdc99b5072/283bd2341f14df0bdffa667ba24975599746eeeed8d681fac59cbdb1a97f177d/probability-inspect-0ae25e42fffa.json`.

## Disposition

The existing static balance matrix remains the authoritative arithmetic envelope for stage time, capacity, cost, force caps, foreign gates, formation floors, and terminal thresholds. This evidence closes one requested validation surface at the source and scenario-model level while leaving campaign research timelines, AI completion rates, force-production samples, rebellion distributions, live terminal timing, and in-game GUI or event playback user-owned. No gameplay simplification or fallback was introduced, and all seven Event 016 3D packages remain deferred.
