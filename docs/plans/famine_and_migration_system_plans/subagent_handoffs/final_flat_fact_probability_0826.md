# Final Flat-Fact Probability Review — 2026-08-26

## Scope and verdict

This is a read-only review of the separate famine and migration weighted mechanics.

No gameplay, decision, mission, scripted-effect, scripted-trigger, constant, localisation, or runtime source was patched by this review.

The flat-fact recovery is a real evidence improvement, but it is not a balance certification.

Famine unresolved coverage improved from the historical 23 unresolved rows to 15 unresolved rows, an 8-row reduction.

Migration unresolved coverage improved from the historical 77 unresolved rows to 60 unresolved rows, a 17-row reduction.

The remaining rows are unresolved engine-state or candidate-pool evidence, not proof of zero weight, invalidity, starvation, dominance, or rank order.

## Audited weighted surfaces and source boundary

The decision/mission sources are:

- `common/decisions/famine_decisions.txt`
- `common/decisions/migration_decisions.txt`

The dynamic target-pool blockers remain associated with:

- `common/scripted_effects/migration_destination_selection_effects.txt`
- `common/scripted_triggers/migration_destination_selection_triggers.txt`
- `common/scripted_effects/famine_opposition_effects.txt`
- `common/scripted_triggers/famine_opposition_triggers.txt`
- `common/scripted_effects/famine_relief_effects.txt`
- `common/scripted_triggers/famine_relief_triggers.txt`

Famine and migration remain separate mechanics, candidate races, and source namespaces.

## Supplied MCP evidence

The supplied probability evidence uses the HOI4 `mission_ai_will_do` score surface.

This adapter reports willingness-score traces and does not provide a normalized selection denominator or a time distribution.

### Famine bounded probe

- Analysis id: `probability-acdb8db6e41121b5801a5d80`.
- Scenario hash: `0ab0466d4da6f3950206156def98d561a522717a17db93575af37fe7a2bb195e`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebd1c9608f8ff8b85df55c2527689407f216bf1781a4680c3e88ba0bc9782f92/441ef293c1c795e1194c61fd46486ee9ecfe3fd3cdbc432f56c6720ca9a6bec9/probability-acdb8db6e41121b5801a5d80.json`.
- Classification: bounded, score-only, unresolved.
- The probe isolates the special decision target `FROM` as unresolved; it does not establish a zero score or an invalid decision.

### Event-target probe

- Analysis id: `probability-ad1c19a77bd881519d917f59`.
- Scenario hash: `4774fe73c9de6d07eb939c91c6ca51eed96fe6490b8471fbc146423da4f4333a`.
- Supplied event-target map: `{FROM: 'state:1'}`.
- The event-target map is schema-valid, but `FROM` still does not resolve.
- Classification: bounded, score-only, unresolved special-scope binding.
- No artifact URI for this probe was supplied, so no URI is invented here.

### Full famine flat-fact matrix

- Analysis id: `probability-ee3074ce9bf0db80f330bf06`.
- Source hash: `729c115b88697b86b2e70988fc1b093361a9220c673a94f2451b68f7613a5e74`.
- Scenario hash: `638129d61ba378c2ecf61a438d17216d7a2dc976dcbd2e3e92b5e552e99fca6e`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e860826d78756ed13c6c7e608cb2778834fae16206807e319e4892bca3e23f2d/339223bb1fe22ee11a649ed0e6ae3417667561d1ec0eaa172215868d8d1c2cc8/probability-ee3074ce9bf0db80f330bf06.json`.
- Coverage: 4 scenarios and 40 rows, with 15 unresolved rows and 2 informational diagnostics.
- Scenario ids: `prob_famine_relief_dense`, `prob_famine_relief_blocked_island`, `prob_soviet_extraction`, and `prob_requisition_donor`.
- Classification: score-only, partial, unresolved external/scoped state.

The 40 rows represent the declared famine decision candidates across the four scenarios, but the unresolved scoped and compound inputs prevent a runtime-complete eligibility conclusion.

### Full migration flat-fact matrix

- Analysis id: `probability-967ff4fb246a0c8c86c5eeb4`.
- Source hash: `84fa372dc07e66a1b07c299486834ce3112db3b03b8ecae2e8ca2022f014665a`.
- Scenario hash: `8c8eb15e528b68603c943cfcf1b47708c56bd1e792b95059293dd62c1aa1da23`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95f14549a35b5e562b9bb71d9ccd9255232396329e62f6080eaabc8d722260e7/049cb1d0bc519eda59b00e99c4af4c59c8f7c93aaa0b3d3afd1bf7a56953d6ec/probability-967ff4fb246a0c8c86c5eeb4.json`.
- Coverage: 11 scenarios and 198 rows, with 60 unresolved rows and 7 informational diagnostics.
- Scenario ids: `prob_humanitarian_border`, `prob_capacity_exhausted_border`, `prob_outbreak_reception`, `prob_nuclear_evacuation`, `prob_genocide_escape`, `prob_authoritarian_pushback`, `prob_destination_selection_internal`, `prob_destination_selection_persecution`, `prob_corridor_acceptance`, `prob_forced_return`, and `prob_integration`.
- Classification: score-only, partial, unresolved external/scoped state.

The 198 rows broaden migration decision coverage, but they do not certify runtime target validity or a complete dynamic destination/response pool.

No rendered ranking, matrix, sensitivity, timing, or unresolved URI beyond the supplied JSON artifact URIs is asserted in this handoff.

## What is now proven

The flat-fact pass proves that the larger famine and migration scenario matrices can be represented and analyzed as bounded MCP evidence with the supplied source and scenario hashes.

It proves a measurable reduction in unresolved rows: famine 23 to 15 and migration 77 to 60.

It proves that the supplied event-target declaration is accepted by the scenario schema.

It also proves that schema acceptance is not the same as scope resolution, because the special `FROM` target remains unresolved after `{FROM: 'state:1'}` was supplied.

The evidence does not prove any expected humanitarian ordering, exact score race, valid candidate, invalid candidate, rank reversal absence, starvation absence, dominance absence, repetition safety, timing safety, or exploit safety.

## Remaining exact unresolved classes

The following blockers remain active and must not be collapsed into a single numeric result.

1. Special decision target binding: `FROM` remains unresolved even with the schema-valid event-target mapping `{FROM: 'state:1'}`.
2. Scoped trigger resolution: any eligibility or modifier branch that depends on a scoped target remains unresolved when the adapter cannot bind that target.
3. Compound trigger resolution: compound availability, target, cost, route, policy, and state conditions remain unresolved where the flat fixture cannot evaluate the compound expression.
4. Dynamic destination candidate enumeration: the runtime destination set is not a complete declared candidate pool, so internal-versus-foreign and safe-host-versus-persecutor rankings cannot be certified.
5. Dynamic opposition candidate enumeration: the political outcome channels do not expose a complete runtime candidate-to-weight pool, so absent-ideology zeroing and local-support/blame ordering cannot be certified.
6. Dynamic famine relief-donor enumeration: donor states, route validity, stock/headroom, protection, and target validity are not a complete normalized pool, so donor ranking cannot be certified.
7. External state completeness: route geometry, ownership/control, capacity, policy, ideology, exposure, relations, equipment, and other live state needed by the named scenarios are not all proven by the flat fixtures.
8. Cadence and terminal-state completeness: no complete custom-pool cadence, cooldown, recovery, removal, reset, cap, timer, and terminal-state manifest is supplied for a sequence certification.

The unresolved classes above explain why a matrix can contain many rows while still lacking an exact runtime candidate set.

## Scores, rankings, timing, and probability classification

The adapter result is a willingness-score surface, not a click-probability surface.

No exact normalized probability can be reported because the adapter does not provide normalization and the effective runtime candidate pools are incomplete or unresolved.

No exact timing distribution or cumulative timing claim can be reported because this adapter has no time-distribution model and no complete cadence/state transition contract was supplied.

No dynamic target-pool certification can be reported because destination, opposition, and relief-donor candidates are not fully enumerated with their validity gates and weights.

No base-value, modifier-trace, or rank conclusion is upgraded to exact or bounded balance evidence merely because a flat fact was accepted.

Any unresolved or zero-like matrix cell must remain classified as unresolved rather than interpreted as a true zero willingness or dead choice.

The named scenario expectations remain open: famine relief ordering, blocked-island route ordering, Soviet extraction/concealment ordering, humanitarian border ordering, capacity-exhaustion policy ordering, outbreak reception ordering, evacuation ordering, corridor acceptance ordering, return ordering, integration ordering, and donor/opposition/destination rankings are not certified by these artifacts.

## Balance and patch disposition

No gameplay or source weight patch is warranted from this evidence.

The unresolved-count reduction is evidence quality progress, not evidence of a bad or good balance target.

The next actionable work is analyzer/fixture and manifest completion: bind special and ordinary scopes, resolve compound triggers, declare complete dynamic destination/opposition/donor candidate pools, and provide their validity gates and selection cadence.

After those prerequisites exist, an owner-applied weight or gate change must be compared under the same named scenarios before any balance conclusion is considered.

Do not tune source constants merely to make unresolved rows nonzero.

## Skipped or unavailable evidence

- No source patch was applied.
- No exact normalized probability or timing analysis is available from the supplied score-only artifacts.
- No complete dynamic target-pool certification is available.
- No custom-pool sequence certification is available because a complete cadence and state-transition manifest is absent.
- No event-target artifact URI was supplied for `probability-ad1c19a77bd881519d917f59`.
- No unsupported completion claim is made for famine or migration.

## Final disposition to parent

Accept the flat-fact pass as a bounded evidence-quality improvement: famine unresolved 23 to 15 and migration unresolved 77 to 60.

Retain the special `FROM` blocker despite schema-valid event-target input, all scoped/compound trigger blockers, and all three dynamic destination/opposition/relief-donor pool blockers.

Keep famine and migration as separate mechanics.

Do not claim exact normalized probability, exact timing, complete target-pool ranking, or balance closure.

