# Site-cost AI saving-hint audit

## Disposition

This is a read-only final audit of six generic camp-repression actions after the owner’s fixed AI saving metadata patch.

No gameplay, AI weight, cost helper, scripted effect, trigger, GUI, localisation, runtime, or configuration file was edited by this audit, and no commit was created.

The audited source is `common/decisions/camp_repression_generic_decisions.txt`.

The owner patch adds only numeric `ai_hint_pp_cost` metadata and leaves every `ai_will_do` expression unchanged.

The preserved hints are 30 for `generic_redirect_labor_to_construction`, 30 for `generic_redirect_labor_to_resource_extraction`, 60 for `generic_restricted_contaminated_site_escalation`, 25 for `generic_destroy_evidence_before_retreat`, 45 for `generic_inspect_active_site`, and 60 for `generic_dismantle_detention_network`.

The local immutable before snapshot is `ai_hint_evidence/decisions.before` with SHA-256 `cca4e61e1bbac5f51b088ebb6651e4485eb7fe04cf00da0dd884b83e684efe2c`.

The hint-audited after snapshot is `ai_hint_evidence/decisions.after` with SHA-256 `57381cb7a82232b6fff03b35c4d00a95f42b25e4d62be965267a722f890546a5`.
A subsequent concurrent integration uses boolean cost helper calls with an explicit state-id temporary; the parent preserved it separately in `ai_hint_evidence/decisions.integrated` and `state_binding_integration.patch`.
Parent source review confirms every current `ai_will_do` expression is identical to the hint-audited snapshot, and every external quote, gate, and payment call initializes its explicit state input.
This later binding change is not misrepresented as part of the six-field metadata-only comparison.

## Audited surfaces

| Identifier | Source block | Adapter | Custom payment surface | Preserved hint |
| --- | --- | --- | --- | ---: |
| `generic_redirect_labor_to_construction` | `cost = 0`, `custom_cost_trigger = camp_rework_can_pay_site_labor` | `decision_ai_will_do` | site labor payment through dispatcher | 30 |
| `generic_redirect_labor_to_resource_extraction` | `cost = 0`, `custom_cost_trigger = camp_rework_can_pay_site_labor` | `decision_ai_will_do` | site labor payment through dispatcher | 30 |
| `generic_restricted_contaminated_site_escalation` | `cost = 0`, `custom_cost_trigger = camp_rework_can_pay_site_restricted` | `decision_ai_will_do` | restricted site payment through dispatcher | 60 |
| `generic_destroy_evidence_before_retreat` | `cost = 0`, `custom_cost_trigger = camp_rework_can_pay_site_evidence` | `decision_ai_will_do` | evidence payment through dispatcher | 25 |
| `generic_inspect_active_site` | `cost = 0`, `custom_cost_trigger = camp_rework_can_pay_site_inspect` | `decision_ai_will_do` | inspection payment through dispatcher | 45 |
| `generic_dismantle_detention_network` | `cost = 0`, `custom_cost_trigger = camp_rework_can_pay_site_dismantle` | `mission_ai_will_do` | dismantlement payment through dispatcher | 60 |

The five decision candidates were evaluated as one declared decision pool.

The dismantlement action was evaluated through the mission adapter because the installed MCP source index classifies this block as a mission surface.

The saved before inspection outputs are [decision-inspect-before.json](ai_hint_evidence/decision-inspect-before.json), [decision-inspect-before.manifest.json](ai_hint_evidence/decision-inspect-before.manifest.json), [mission-inspect-before.json](ai_hint_evidence/mission-inspect-before.json), and [mission-inspect-before.manifest.json](ai_hint_evidence/mission-inspect-before.manifest.json).

The decision inspection reported five requested candidates and the mission inspection reported the one requested dismantlement candidate; the source-wide category contains additional candidates outside this bounded audit pool.

## Scenario contract

The scenario file is [site_cost_ai_scenarios.json](ai_hint_evidence/site_cost_ai_scenarios.json).

The scenario set id is `CAMP_REPRESSION_SITE_COST_AI_HINTS_2026_09_05`.

The four named scenarios are `SITE_COST_ADEQUATE_L1`, `SITE_COST_SHORTFALL_L1`, `SITE_COST_ADEQUATE_L5`, and `SITE_COST_SHORTFALL_L5`.

Adequate fixtures declare an AI CXT actor on 1936-01-01, fascist government, peace, clear cooldowns, generic-kit activation, site level 1 or 5, positive political power, manpower, command power, equipment, trains, and civilian-project capacity, zero overstretch, and true boolean candidate overrides.

Shortfall fixtures keep the actor, date, route, and site level but set political power, manpower, command power, equipment, trains, and civilian-project capacity to zero, set the equipment/hidden affordability flags false, and set every audited candidate override false.

The declared actor, original tag, date, ideology, war state, route, cooldown state, site level, resources, cap flags, `FROM` marker, and candidate overrides are recorded in the scenario file.

The candidate pool is complete for the six requested actions, but it is not the complete category pool discovered by MCP.

The five-action decision pool is therefore complete only at the declared audit boundary, and the one-action mission pool is complete only at the declared dismantlement boundary.

No random seed, cadence transition, timer transition, uncertain distribution, custom sequence, or terminal-state transition was declared because these adapters expose score selection rather than a timing or normalized sampling model.

The flat scenario schema accepts the declared primitive values and boolean candidate overrides.

Nested `FROM` target scope, dynamic site-cost helper execution, equipment/resource payment arithmetic, and the full country/state helper chain are outside the adapter’s executable state model.

The overrides deliberately isolate the score comparison from those unavailable dynamic gates.

## MCP provenance

The HOI4 MCP workspace is `mod_chaos_redux_ea3b2d67c2c0`.

The installed game target is Operation Postern 1.19.2.0 (d245), and the probability adapter version is `hoi4-1.19.2.v1`.

The parent supplied the required read-only baseline `hoi4.probability_inspect` artifacts, so this subpass did not duplicate inspection.

The final decision evaluation is recorded in [decision-evaluate-after.json](ai_hint_evidence/decision-evaluate-after.json).

Its MCP result is `PROBABILITY_ANALYZED`, analysis id `probability-5f8ab204fba95fea36c9e473`, source revision `76562bb002e0b76daf1ef60b7572ce7449900ebb8a02481d905bed8e3f73f6ce`, MCP canonical source hash `39a9c8bbbe794d9317c04a7126224ad634115407bb00ef8f5acbc0424b8d2802`, scenario hash `d494e5e0ab58a71f084cc444d84ae2390519b3784d4388ebc209d8179eedcd92`, four scenarios, twenty candidate rows, zero unresolved items, and zero diagnostics.

The authoritative decision evaluation JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5b5469f3ecd905ff9b22c61103428c1e9c1760c161778dc941ea79e9a6d5edd/697d1887a30fd6660a4009417e8778f5433c53aa58eb42277c4914dfc3c1cb0b/probability-5f8ab204fba95fea36c9e473.json`.

The evaluation emitted ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46f361606efbf64b7aa08a1a9812bdea72d50499b82a773d3633add2701c56de/66c1e7eaf9e714f1fa6435a086b9d4832363dbc4f8b39353a406870f7d38fa58/probability-probability-5f8ab204fba95fea36c9e473-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce0d870d8a17abbcd3d00a9b8a3df901c54d5c2e1e4009091459db2dedcd282178ffaaab4df81f90e631a0ad0aa45f/8137770078381dd7c87c66330451a6dc5ade68de44302da0a126db4a75bcb560/probability-probability-5f8ab204fba95fea36c9e473-matrix.svg`, and unresolved view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/a10bd7a33ded5abd0535f3986c465a2cf89b83729c793fa557dcb95f954efae7/probability-probability-5f8ab204fba95fea36c9e473-unresolved.svg`.

The final mission evaluation is recorded in [mission-evaluate-after.json](ai_hint_evidence/mission-evaluate-after.json).

Its MCP result is `PROBABILITY_ANALYZED`, analysis id `probability-21b58d7fe90a028c60b94e69`, the same source revision `76562bb002e0b76daf1ef60b7572ce7449900ebb8a02481d905bed8e3f73f6ce`, the same MCP canonical source hash `39a9c8bbbe794d9317c04a7126224ad634115407bb00ef8f5acbc0424b8d2802`, the same scenario hash `d494e5e0ab58a71f084cc444d84ae2390519b3784d4388ebc209d8179eedcd92`, four scenario rows, zero unresolved items, and zero diagnostics.

The authoritative mission evaluation JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66ef32480c404541684d6eb1a49ee679cb19472f8a1a5e9efc5ae1f871acef8e/13986d78e840337d45483b134d61a06b1377cae686838ca2ea531321af7541c2/probability-21b58d7fe90a028c60b94e69.json`.

The final decision comparison is recorded in [decision-compare-before-after.json](ai_hint_evidence/decision-compare-before-after.json).

It compares the immutable before inlineClausewitz snapshot against the current after source path with the same four scenarios and the same five-candidate pool.

The decision comparison returned `PROBABILITY_ANALYZED`, analysis id `probability-106de88327953c2bff1c206f`, the same source revision and scenario hash, twenty candidate rows, zero unresolved items, zero diagnostics, and `comparisonChanges = 0`.

The authoritative decision comparison JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83054fe8def0ee409c8e17a19875caa2fc16a0158e79c58b6fde6c9b68dcb22c/2a4b13a579ca7646d78ae93508a3d5d97915c21926378f83ca372232bbb1a1e4/probability-106de88327953c2bff1c206f.json`.

Its emitted comparison view is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/2748c30a6a827e6b0e4825ad2b39f1514e451e8485c63f3aa4d9f206d28a24a3/probability-probability-106de88327953c2bff1c206f-comparison.svg`.

The final mission comparison is recorded in [mission-compare-before-after.json](ai_hint_evidence/mission-compare-before-after.json).

It compares the same immutable before inlineClausewitz snapshot against the current after source path with the same four scenarios and the one-candidate dismantlement pool.

The mission comparison returned `PROBABILITY_ANALYZED`, analysis id `probability-afcac70df34b643d593d6168`, the same source revision and scenario hash, four candidate rows, zero unresolved items, zero diagnostics, and `comparisonChanges = 0`.

The authoritative mission comparison JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91bf673224cf234da9889049c03c4612611daabb11c1c185a397e0bfbd18a698/e6e02f4d01959e6c549407f4ba3a95afc6c23461a714e19debc8fdf3e6381e60/probability-afcac70df34b643d593d6168.json`.

Its emitted comparison view is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/b59553bddfa4f2e64cb9c51896c6086e1f19b1657f9056aafeb352aec2de16c8/probability-probability-afcac70df34b643d593d6168-comparison.svg`.

## Score evidence

The probability adapters explicitly identify both surfaces as `score_only`.

They expose raw willingness scores and eligibility, with `normalizedProbability = false` and `timeDistribution = false`.

No reported score is a click probability, and no denominator or categorical selection rate is inferred.

The source-level base traces are:

| Identifier | Base | Source-local modifiers | Declared fixture outcome |
| --- | ---: | --- | --- |
| `generic_redirect_labor_to_construction` | 25 | factor 0 when `camp_rework_country_under_ai_project_cap` is false; factor 0 at or above the overstretched threshold | cap true and overstretch 0 in adequate fixtures; shortfall is controlled by the explicit false candidate override |
| `generic_redirect_labor_to_resource_extraction` | 25 | factor 0 when `camp_rework_country_under_ai_project_cap` is false; factor 0 at or above the overstretched threshold | same as construction |
| `generic_restricted_contaminated_site_escalation` | 12 | factor 0 when the restricted-method cap fails; factor 0 for condemnation 25; factor 0 when overstretch is above the high band | restricted cap true, no condemnation flag, and overstretch 0 in adequate fixtures |
| `generic_destroy_evidence_before_retreat` | 55 | factor `factor_losing_war` when the country is not fascist | fascist government is declared, so this non-fascist modifier is inactive in the intended profile |
| `generic_inspect_active_site` | 85 | factor 0 for fascist government when `camp_rework_crisis_exposed` is absent | the declared fascist/no-crisis profile suppresses this AI score even when the synthetic candidate override marks eligibility true |
| `generic_dismantle_detention_network` | 85 | factor `factor_postwar_reform` when `has_war = no` | peace is declared, so the postwar reform factor is active in the mission trace |

The source constants resolve `generic_authoritarian_activation = 25`, `generic_radicalized = 12`, `generic_reform = 85`, and `evidence_destruction = 55`.

The source retains the existing losing-war and postwar-reform factors; the owner patch did not alter those expressions or their constants.

The compare result reports zero changes for every audited row across all four scenarios on both adapters.

This proves unchanged source-local score arithmetic for the supported MCP model.

It does not prove that the live engine applies or ignores `ai_hint_pp_cost`, because the probability adapters do not model the engine’s custom-cost saving hint.

## Validity, dominance, starvation, and exploit findings

The six blocks retain explicit route, target, availability, custom-cost, and cooldown gates in the source.

The synthetic adequate/shortfall overrides make the intended affordability boundary visible to the adapter without pretending that the adapter executed the dispatcher’s selected-site payment helpers.

Adequate and shortfall rows therefore provide bounded fixture evidence for the comparison boundary, not a live payment proof.

The decision comparison reports no score, eligibility, or rank change caused by the six hint fields.

The mission comparison reports the same result for dismantlement.

No dominance or starvation conclusion is valid for actual decision selection because the category pool is incomplete and the adapters do not normalize scores.

Within the declared source-local score model, the labor actions retain their 25-point bases, restricted escalation retains 12, evidence destruction retains 55 before its existing conditional factor, inspection retains 85 before its fascist/no-crisis zero factor, and dismantlement retains 85 before its existing postwar factor.

No rank reversal is reported by either comparison.

The absence of rank reversal is a comparison result for the declared rows and fixtures, not a statement about every camp-repression candidate or a normalized click race.

No timing drift, repetition, cooldown, recovery, reset, removal, or terminal-state conclusion is available from these calls because both adapters report `timeDistribution = false`.

No positive weight on an impossible target is proven or disproven by this saving-hint pass.

The custom-cost helper, selected-site target, resource payment, and dispatcher paths remain the owner’s engine/runtime responsibility.

The fixed hints do not debit political power and do not replace `custom_cost_trigger`, `custom_cost_text`, or the manual dispatcher payment.

## Recommended fixes without applying them

Keep the six numeric `ai_hint_pp_cost` fields in `common/decisions/camp_repression_generic_decisions.txt` attached to the exact identifiers listed above.

Keep the corresponding `cost = 0` plus `custom_cost_trigger` and dispatcher payment contract aligned for each selected site.

If a later live engine check shows that a custom-cost decision’s saving behavior still differs from its former nominal PP burden, investigate the engine hint interpretation for that exact decision id and preserve this same scenario set for any new probability comparison.

Do not retune any `ai_will_do` base or modifier from this pass, because both adapter comparisons report zero score changes.

## Skipped analyses and blockers

The parent supplied the required baseline inspect artifacts, so this subpass did not repeat `hoi4.probability_inspect`.

The first decision evaluate request was rejected with `MCP error -32602` because unsupported diagnostic keys `zeroWeight` and `unresolved` were passed.

The corrected path-shaped evaluate request succeeded.

An earlier path plus non-source identifier request returned `PROBABILITY_SURFACE_EMPTY` with `identifierMatchCount = 0`; the accepted request used the exact source path and the expected after hash.

No `hoi4.probability_sweep` was run because no raw weight, modifier, threshold, or timing target changed and the parent explicitly limited this pass to evaluate and compare.

No `hoi4.probability_simulate` was run because no uncertain input distribution or approved seed was declared.

No `hoi4.probability_sequence` was run because no complete custom-pool cadence/state-transition manifest was declared.

No separate `hoi4.probability_render` call was needed because evaluate and compare emitted the ranking, matrix, comparison, and unresolved resources listed above.

No event, focus, GUI, technology, doctrine, or map structural MCP route applied to these six decision/mission score surfaces.

The probability adapter’s custom-cost saving-hint interpretation remains unresolved even though the source-local before/after score comparison is complete.

No live HOI4 launch or gameplay validation was performed.

## References and skills

The required repository instructions were read from `AGENTS.md`.

The `chaos-redux-subagents` and `chaos-redux-decisions-missions` skills were applied.

The required offline Paradox wiki core pages and the vanilla decision/AI/script documentation were consulted before this audit.

No gameplay file, localisation file, spreadsheet, asset, runtime file, or skill file was changed.

No simplification was applied to the requested six-action source comparison; the only evidence boundary is the MCP adapter’s documented score-only treatment and its unsupported live saving-hint semantics.
