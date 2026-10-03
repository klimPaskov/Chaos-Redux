# Normal Food Observation Probability Baseline Audit — 2026-10-03

## Baseline disposition

The pre-change source baseline is established for the ordinary famine food-observation and migration destination path. It establishes a qualitative source-level reachability defect: an ordinary untracked state cannot publish the required famine food receipt through the current migration consumer, so its destination candidate fails closed. This is not MCP proof, a numeric baseline, or a probability result.

The probability adapter returned no metadata after two 600-second inspection timeouts, including a narrower retry. No base score, candidate ranking, normalized probability, timing result, or current scenario hash was returned. The owner may continue only with that certification limit explicit. The destination consumer, adjacent prepass, publisher eligibility, and retirement changes remain outside this baseline and need a same-scenario compare if later wired.

This audit was read-only. I did not change gameplay source, weights, candidate checks, scenario fixtures, or the frozen before copies. The current pure component/score extraction and observer helper definition are parent-owned working changes. The observer helper has no gameplay call site, so it does not change the current destination candidate set.

## Frozen source identities

The parent-provided baseline directory is docs/plans/famine_and_migration_system_plans/validation_baselines/normal_food_observation_20261003/. I verified these before/current identities. This table keeps the frozen pre-edit bytes distinct from the current working source.

| Source | Frozen before SHA-256 | Current SHA-256 | Identity |
| --- | --- | --- | --- |
| famine_core_effects.txt | 9E57983FF15737321F4F31B2471F3BEA4B438432EF8F521E4DA0C87906F42B1F | 3A884AC20E39AE3775101C0690364D67AC3BA3130CE264F6AB496E56FACEC18E | Changed after snapshot; shared component and score extraction reviewed below. |
| famine_adapter_effects.txt | 05E5855A19BE1B4999BD52F61E8D2208C288005E0A2B7F0F26B5D698E9C460F1 | 5BD58ECC46D794B0C63933D1C0ECD327A999B1290475D672AF69BAE6229CA100 | Changed after snapshot; contains the unwired food observation helper. |
| famine_core_triggers.txt | 9ABA0F437AEA85B1F371E9257FF20C22291AD3E88EEF575805719403E53EE6E9 | 9ABA0F437AEA85B1F371E9257FF20C22291AD3E88EEF575805719403E53EE6E9 | Byte-equal before/current. |
| migration_adapter_effects.txt | 679856D9FDDECF00A780DBB8BEA2954927607EDFD5F60FE278752F8AF9A65AF4 | 0CD3091AA4998C7266FE66114D5E5C0B82A4D01E6DAC42F26A596DEF0F144193 | Changed after snapshot; includes later parent-owned integration hunks. |
| migration_destination_selection_effects.txt | F20084BF1FE1B12A885710B0A3E081E251F3AEFD3505ACA4C65925421CAEB9FF | F20084BF1FE1B12A885710B0A3E081E251F3AEFD3505ACA4C65925421CAEB9FF | Byte-equal before/current. |
| migration_destination_selection_triggers.txt | 3C4AAC5707EC80279477005E22980723CC5846ABA200228395A16C117B06141D | 3C4AAC5707EC80279477005E22980723CC5846ABA200228395A16C117B06141D | Byte-equal before/current. |
| migration_decisions.txt | 279487DC7F2FCEF921F7294FD207BA8C1C33F871C652280EBB31D2D1FD2A3E8B | 279487DC7F2FCEF921F7294FD207BA8C1C33F871C652280EBB31D2D1FD2A3E8B | Byte-equal before/current; no decision weight changes. |
| migration_capacity_effects.txt | 62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B | 62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B | Byte-equal before/current. |
| migration_core_triggers.txt | 00031F2DBCC7549E0D1FD2EBD40613809EB97332D9CD4B8EC68F8266BC7864FE | 00031F2DBCC7549E0D1FD2EBD40613809EB97332D9CD4B8EC68F8266BC7864FE | Byte-equal before/current. |

The official scenario fixture is docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv, SHA-256 0CA5707ADE8C5565623F1F965B54411523C1EFE25E1AA3909311ECF9B1A4279D.

## MCP inspection and evidence

The live probability schemas expose custom_weighted_pool, mission_ai_will_do, probability_inspect, probability_evaluate, and probability_compare. Both inspections below used the declared custom_weighted_pool adapter and a mod-relative source object for common/scripted_effects/migration_destination_selection_effects.txt.

1. The first metadata inspect narrowed candidatePool to migration_destination_selection_calculate_candidate_weight. It returned: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; timed out awaiting tools/call after 600s.
2. The smaller retry narrowed candidatePool to migration_select_internal_safe_route_destination. It returned the same actual 600-second timeout.

Neither call returned a source revision, source hash, scenario hash, analysis id, status object, blockers, candidate list, artifact URI, or rendered evidence. The adapter route is exposed, but these source inspections did not complete.

The candidatePool values above name a source helper and one selector. They are not a complete runtime neighbor-state candidate pool. The destination script discovers candidates with every_neighbor_state and filters them through state validity, food safety, route, owner/controller, border, policy, reception capacity, persecution, camp, contamination, fallout, bombing, and history gates. No complete current state list or external-factor fixture was supplied, so normalized pool analysis cannot be claimed.

No probability_evaluate, probability_sweep, probability_compare, probability_simulate, probability_sequence, or probability_render result was produced in this baseline. Evaluation and comparison were not attempted after the inspect timeouts because no complete dynamic pool or supported country/state scenario binding was available. The prior scenario schema evidence accepted flat state fields and eventTargets but rejected nested typed scopes, variables, and externalFactors; its schema-valid FROM = state:1 example did not bind the decision target. The current probability_inspect timeout supplied no newer fixture schema.

The latest historical source evidence is the Aug 26 migration score matrix, not this pre-change baseline: analysis probability-967ff4fb246a0c8c86c5eeb4, scenario hash 8c8eb15e528b68603c943cfcf1b47708c56bd1e792b95059293dd62c1aa1da23, source hash 84fa372dc07e66a1b07c299486834ce3112db3b03b8ecae2e8ca2022f014665a, 198 rows and 60 unresolved, score-only and partial. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95f14549a35b5e562b9bb71d9ccd9255232396329e62f6080eaabc8d722260e7/049cb1d0bc519eda59b00e99c4af4c59c8f7c93aaa0b3d3afd1bf7a56953d6ec/probability-967ff4fb246a0c8c86c5eeb4.json. That analysis included the internal and persecution scenario IDs, but its source hash predates the frozen October files and it is not a before/after comparison for this observation work.

Historical destination pool inspection reported four declared entries without dynamic neighbor candidates at source hash 8169d9fb45fde0b399097d3f252c64fe6be7ba7e21a1e5952531ea8b34ddc65d; artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a96188c86331f555ef4b3f706f85901555ec6e1f49b823694cc61e6599a7a368/2767d7dd3053467a2d425326ee7de011247498bd0dd14e7415ab86e4d41a82f2/probability-inspect-8169d9fb45fd.json. This is historical evidence only, not a current inspection.

## Current weighted surface and source-only baseline

The audited weighted surface is the custom migration destination selector, not a changed ai_will_do score. The four current selector entry points in migration_destination_selection_effects.txt are migration_select_general_safe_evacuation_destination, migration_select_internal_safe_route_destination, migration_select_foreign_transit_destination, and migration_select_third_country_resettlement_destination. The current decision source migration_decisions.txt remains byte-equal to the frozen file; its 18 ai_will_do candidates were not re-evaluated in this pass.

Within one pool, migration_destination_selection_run_weighted_pool totals positive weights for candidates that pass migration_destination_selection_candidate_is_valid, draws a uniform random value scaled by the total, then subtracts each candidate weight until it binds a destination. This is probability-proportional sampling within one eligible pool; no numeric base weight or modifier trace was returned by MCP.

Internal versus foreign evacuation is not a single normalized race. migration_select_general_safe_evacuation_destination runs the internal_safe_route pool first and only runs foreign_safe_evacuation if the internal pool returns no destination. Therefore any positive eligible internal pool suppresses every foreign safe-evacuation candidate. The fixture prob_destination_selection_internal says a safe internal state should outrank foreign options when capacity and route are adequate; source structure implements that as hard sequential priority. Its foreign-side selection has no denominator while internal candidates remain. This is a source-level dominance/starvation condition, not an MCP probability or ranking result. No balance target is selected here.

The official scenario prob_destination_selection_persecution expects a safe different-ideology host to outrank a same-ideology persecutor and the persecutor to have zero weight under an active targeted threat. The source trigger excludes unsafe/persecuting destinations before candidate weight is calculated. Exact candidate completeness, external persecution proof, host validity and capacity remain unproven by MCP, so the expected ordering is not certified numerically.

Current source reachability is fail-closed. The frozen migration_consume_famine_food_safety effect calls famine_publish_migration_food_safety and validates the versioned receipt; it does not call the new observation helper. The publisher requires existing famine stage, pressure, production, transport, and governance variables and invalidates when they are missing. The ordinary destination selector calls the consumer for the origin and every adjacent neighbor before its candidate gates. An ordinary untracked healthy state therefore has no first food receipt in the frozen path and cannot be an eligible destination. This conclusion is source-level reachability evidence only, not native engine execution or probability evidence.

The current famine_observe_migration_food_context definition in common/scripted_effects/famine_adapter_effects.txt is not called from any gameplay source under common/. It does not change the current destination pool. The parent-owned pure extraction separates famine_rebuild_food_components, famine_calculate_food_score, and famine_apply_current_blockade_components; the normal evaluator calls the shared calculations in the original order, while the observation helper calls the current-blockade component helper without advancing blockade exposure. The reviewed effect diff preserves the existing formula expressions and constant references; this is source review, not an MCP comparison.

The observer does not call famine_update_reserve, famine_decay_pressure, famine_apply_mortality, famine_transition_food_stage, famine_refresh_dynamic_modifiers, or famine_publish_migration_food_safety. It calculates from existing owner inputs, current context, existing reserve relief, and current components. A new quiet-state observation creates neutral missing-value ledger defaults through famine_initialize_state, including zero reserve ledgers, zero death total when absent, exposure zero, stable candidate, and current-date timer defaults. It does not create positive stock or apply a death. Repeated-query tests must distinguish these neutral state-field initializations from physical stock/death effects; a stricter prohibition on writing reserve or timer ledgers would require a narrower initializer.

The material branch does have a visibility side effect through an existing shared helper. famine_register_active_state sets famine_food_security_active, famine_decision_problem_is_active treats that flag as a problem, and famine_decision_category.visible calls that trigger. Therefore a newly material observation can reveal the famine category even though the observer does not directly refresh modifiers or call a category helper. If the accepted no-category-effect boundary means category visibility must wait for ordinary famine evaluation, the current material registration path conflicts with it and needs a separate pending-registration path or a parent-approved exception before wiring.

The source-only case matrix below preserves the accepted review cases without inventing fixture keys, target tags, states, or neighbor candidates.

| Scenario or case ID | Expected result | Candidate/external completeness and evidence |
| --- | --- | --- |
| prob_destination_selection_internal | A valid safe internal destination has strict precedence; unsafe candidates have no weight. | Official CSV case. Dynamic neighbors, food receipts, capacity, route, control, and safety inputs are incomplete; no current MCP result. |
| prob_destination_selection_persecution | A safe foreign host may be considered; a proven active persecutor is excluded before weighting. | Official CSV case. No current complete foreign host list or typed persecution target state; no current MCP result. |
| quiet-untracked | First quiet observation can create a stable pressure-model assessment but no food receipt until the caller publishes it; no service, stock, death, category, or capacity grant. | Parent acceptance case. Helper has no caller; source-only, not an executed scenario. |
| material-first | Material score at stable stage invalidates the destination receipt and registers only the exact state for normal simulation. | Parent acceptance case. Current helper sets famine_food_observation_pending_material, but retirement does not test that flag; see blocker below. |
| retired-quiet | A retired quiet state can be observed again without permanent famine scheduling or a destination grant before publication. | Parent acceptance case. No current supported typed state fixture or MCP trace. |
| known-catastrophic | Existing catastrophic state and all valid causes/stage/inputs remain intact; missing durable inputs fail closed. | Parent acceptance case. The helper rejects an incomplete non-stable crisis and otherwise preserves existing values; source-only. |
| repeated-query-no-stock-death | Repeated observation does not replenish stock, advance exposure/decay/stage hysteresis, apply mortality, or repeat a death. | Parent acceptance case. Source helper omits those effects; initial neutral ledger/timer fields may be created; no MCP trace. |

## Material-first retirement blocker

famine_record_food_assessment sets famine_food_observation_pending_material when the current stage is stable and the calculated food score reaches the supply-strain threshold. The observation helper then registers that exact state and leaves the food result fail-closed. famine_calculate_food_score writes famine_food_security_score and the temporary requested stage; it does not set famine_food_pressure or commit a stage.

The frozen famine_state_can_retire trigger at famine_core_triggers.txt:128-138 accepts a state when its stage is stable, food pressure is not positive, reception demand is not positive, and no blockade candidate is active. It does not check famine_food_observation_pending_material. A first material observation can therefore be registered while stage remains stable and pressure is zero, then be retired by the normal evaluator before the stage candidate hysteresis matures. The same registration also sets the category-reveal flag described above. These are source-level blockers to wiring the accepted observer until retirement retains the pending material assessment and category visibility is kept within the accepted boundary or explicitly accepted by the parent. No retirement patch was applied in this audit.

Food observation also does not resolve the separate reception-service cycle. The current capacity and decision gates still require actual shelter/medical service proof and a valid country capacity before ordinary reception and cross-border destination routes become eligible. The parent accepted no synthetic services from population, infrastructure, or this observation. The observer alone cannot certify a dormant foreign host as selectable.

## Exact unresolved evidence and next compare boundary

The inspect requests establish only a connected-call timeout. They yielded no source revision or analysis artifact, so current base weights, modifier traces, candidate ranking, normalized probabilities, rank reversals, timing distributions, dominance, starvation absence, repetition safety, and exploit safety remain unresolved. The historical 18-candidate mission_ai_will_do matrix is a willingness-score surface and is not a click probability or a current destination pool result.

probability_evaluate was not run because the live inspect produced no metadata and the required complete dynamic destination candidate set and country/state bindings are absent. probability_sweep was not run because there are no resolved score ranges or candidate pool to sweep. probability_compare was not run: the observation helper is still unwired and no weighted candidate/target behavior patch is being audited yet; the destination before/current files are byte-identical; the only changes so far are source helper extraction/definition additions, not a weighted target comparison; and no current supported scenarioSet encodes the internal/foreign candidates without invented neighbor states. A later consumer/prepass/publisher/retirement patch must use the frozen before paths and the actual after paths under the same supported internal/foreign scenario IDs, plus the quiet-untracked, material-first, retired-quiet, known-catastrophic, and repeated-query no-stock/death cases where the live schema supports them. Do not compare byte-identical selector sources to claim a delta, and do not substitute an August artifact for this baseline.

probability_simulate was not run because no uncertain input distributions, correlations, or seeds were declared. probability_sequence was not run because the destination pool is not a complete cadence/transition/terminal-state manifest. probability_render was not run because no current ranking, matrix, comparison, sensitivity, or unresolved-view artifact was returned.

The current MCP errors are exact: hoi4.probability_inspect timed out awaiting tools/call after 600s for both the single weight-helper inspection and the smaller single internal selector inspection. The next valid attempted comparison is outstanding until the owner produces a supported fixture and complete candidate contract; no current route or schema is inferred from these source results.

## Skills and mutation record

Skills used: chaos-redux-subagents and chaos-redux-decisions-missions. The MTTH skill was not applicable because no MTTH entry is part of this weighted destination surface. No skill files were changed.

This audit wrote only this report. No gameplay file, AI weight, target gate, destination source, fixture, or frozen baseline was modified. No game was launched and no logs were read.
