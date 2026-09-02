# Event 016 project-stage probability audit

Date: 2026-09-02.

Status: prepatch baseline and one bounded post-owner comparison secured; compare is partial because eligibility/helper semantics remain unresolved.

Scope: read-only audit of the 60 project-stage decisions in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`.

This handoff does not claim Event 016 acceptance, normalized decision probabilities, or engine-equivalent eligibility.

## Audited surface and source identities

The audited decision surface is `brilliant_scientist_directorate_category` in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`.

The source contains 15 `brilliant_scientist_integrate_<family>_prototype` decisions and 45 `brilliant_scientist_advance_<family>_<theory|deployment|weaponization>` decisions.

The relevant helper context is `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_triggers.txt`, and `common/script_constants/016_brilliant_scientist_project_constants.txt`.

The retained before source is commit `c25a4f4a944a408fb4b6dfc1dd0601cc3b551956`.

Retained git blob identities are decision `71c5d41c30ef4972e8546860b42e6b623b0dd15a`, project effects `d15329425736e06f9eb4a3610914005cea8985d6`, project triggers `fd2bd74e2e499ea6aaef7eea9eadaec3eeda581d`, shared Event 016 triggers `f3bf146cc1cf99ec6303cfc050d410eb2fb24f6a`, and project constants `097c03ffe4ae9e441f6f0f298a2602c7aa70ca07`.

Pre-owner working-tree raw SHA-256 values at baseline capture were decision `23b9ca7d73d8f2cc8ca6207f695ba08c8d4abed3695ba8c3fb35960d3fbb67fd`, project effects `95173bd46b66f73117087a8f2491f9acae6ad73b3706225e076e9ff05a7aed76`, and project triggers `74a299497b179cf5531ab0db7bf0a249c2f82640fa0dda3159573adf87849c09`.

At baseline capture, `git diff --ignore-space-at-eol c25a4f4a944a408fb4b6dfc1dd0601cc3b551956` was empty for the decision, project effects, and project triggers, so the working-tree differences in the latter two were line-ending-only at that checkpoint; the later owner patch changed the relevant project lifecycle sources.

The evaluator provenance resolves the score helper `brilliant_scientist_has_low_project_capacity` from `common/scripted_triggers/016_brilliant_scientist_triggers.txt` with current source hash `ef9b7964617cb6b73cf5bc230fd31751081a0ffc21cca999575dbb45f3853636` and the project constants with current source hash `3c25f2eb7d9b3874d99c31d7cf1f0362c6a949018d6783733cfb0ab5d8831ce6`.

The source-defined score constants are `ai_low = 1`, `ai_medium = 5`, `ai_high = 10`, `preferred_factor = 2`, and `cautious_factor = 0.5` in `common/script_constants/016_brilliant_scientist_project_constants.txt`.

## Required MCP inspection

The mandatory first call was `hoi4.probability_inspect` against workspace `mod_chaos_redux_ea3b2d67c2c0`, source path `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, identifier `brilliant_scientist_directorate_category`, and the complete 60-candidate pool.

The first adapter probe with `decision_ai_will_do` returned `PROBABILITY_SOURCE_DISCOVERED` with `candidate_pool_not_found` and suggested `mission_ai_will_do`; no analysis was taken from that probe.

The corrected mandatory inspect with `mission_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED` and `status=ok`.

Inspect source hash was `5585b82f571a57e90600753ff5eccaaa69745332363afcfbb4f62ca9897a7a25`, source revision was `32fb14635fc877d401eb68dfe4f2913131ebac5e893367333eac60f3d6882613`, the pool was complete at 60 candidates, and required scenario inputs were `check_variable`, `custom_trigger_tooltip`, and `has_war`.

The inspect adapter descriptor is `mission_ai_will_do`, selection rule `score_only`, with eligibility and raw-score capability, but `normalizedProbability=false`, `completePoolRequired=false`, and no time-distribution or sequence capability.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f38389016de5082807a0ec2d7e4db946a5221f06c1792b297bc802401b6b424/0098db5ed1b7782fb0f5bc6326b097678cf99c171d274583810fe6aa2b91a8ce/probability-inspect-5585b82f571a57e90600753ff5eccaaa69745332363afcfbb4f62ca9897a7a25.json`.

## Retained fixture and candidate pool

The exact scenario fixture is [E016_PROJECT_STAGE_LIFECYCLE_2026_09_02.scenarios.json](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_PROJECT_STAGE_LIFECYCLE_2026_09_02.scenarios.json>).

The fixture contains the strict MCP `probabilityScenarioSet` body with seven named scenarios, each declaring host, primary-facility, capacity, stage-entry, technology, industrial, manpower, political-power, equipment, resources, Exposure, danger, war-role, and terminal-state inputs.

The seven exact scenario IDs are `E016_PROJECT_STAGE_PEACE`, `E016_PROJECT_STAGE_DEFENSIVE_WAR`, `E016_PROJECT_STAGE_OFFENSIVE_WAR`, `E016_PROJECT_STAGE_RESOURCE_SHORTAGE`, `E016_PROJECT_STAGE_HIGH_EXPOSURE`, `E016_PROJECT_STAGE_DANGEROUS_PROJECT`, and `E016_PROJECT_STAGE_TERMINAL_SELECTION`.

The complete candidate pool passed to MCP contains exactly 60 unique IDs.

The 15 prototype IDs are `brilliant_scientist_integrate_computation_prototype`, `brilliant_scientist_integrate_materials_prototype`, `brilliant_scientist_integrate_biomedical_prototype`, `brilliant_scientist_integrate_teleportation_prototype`, `brilliant_scientist_integrate_cloning_prototype`, `brilliant_scientist_integrate_robotics_prototype`, `brilliant_scientist_integrate_paleogenetics_prototype`, `brilliant_scientist_integrate_xenobiological_synthesis_prototype`, `brilliant_scientist_integrate_alien_arms_prototype`, `brilliant_scientist_integrate_temporal_prototype`, `brilliant_scientist_integrate_singularity_prototype`, `brilliant_scientist_integrate_electronics_prototype`, `brilliant_scientist_integrate_rocketry_prototype`, `brilliant_scientist_integrate_high_energy_prototype`, and `brilliant_scientist_integrate_biological_weapons_prototype`.

The 45 advance IDs are the Cartesian set `brilliant_scientist_advance_<family>_<stage>` for each family `computation`, `electronics`, `materials`, `rocketry`, `high_energy`, `biomedical`, `teleportation`, `cloning`, `robotics`, `paleogenetics`, `xenobiological_synthesis`, `biological_weapons`, `alien_arms`, `temporal`, and `singularity`, and each stage `theory`, `deployment`, and `weaponization`.

The MCP candidate-pool hash for this exact ordered pool is `7554739e83717a355c61872e6a521ae444aeb42b9e9a08984bfb349d75248478`.

## Bounded prepatch evaluation

The one corrected bounded call was `hoi4.probability_evaluate` with adapter `mission_ai_will_do`, the exact fixture above, the complete 60-candidate pool, metric `raw_value`, and outputs `json`, `ranking`, `matrix`, and `unresolved`.

An initial request was rejected because the strict MCP scenario-set schema does not allow an extra `candidatePool` property; the fixture was corrected to the strict scenario-set body and the unchanged complete pool was passed through the tool's `candidatePool` argument.

The first evaluate attempt was rejected before analysis with `PROBABILITY_SOURCE_STALE` because the inspect hash `5585…` is the service-normalized hash while `expectedSourceHash` checks raw workspace bytes; the corrected source object used raw decision SHA-256 `23b9ca7d73d8f2cc8ca6207f695ba08c8d4abed3695ba8c3fb35960d3fbb67fd` and the same fixture.

The corrected evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, `status=ok`, seven scenarios, 420 candidate rows, 105 top-level deduplicated unresolved items, and zero diagnostics.

Analysis ID: `probability-1e1820c44d4143b5478752d0`.

Scenario hash: `e1f7151feebd31e36dfb88153f96ba0391f51d207de2219a70c12cd5d5d7ccb8`.

Source revision in the result: `5e12578466a4f31b3b450033c6331fdeac9458967a6bc760541c596b918cc907`.

Source hash in the result: `5585b82f571a57e90600753ff5eccaaa69745332363afcfbb4f62ca9897a7a25`.

Cache key: `1e1820c44d4143b5478752d0c2d72c82e3cc10632f8ecc345b635f76eb4823dc`.

Authoritative JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1643a2679a9e1b2e54d44163467d97d3e7219048f5b4bc4d4ccdbe982ef96f15/eaa45732e2d3cce6cef3b8c9f2ff615cf6cd17d7b662b4c917d295c8dcaebf9f/probability-1e1820c44d4143b5478752d0.json`.

JSON artifact SHA-256: `1643a2679a9e1b2e54d44163467d97d3e7219048f5b4bc4d4ccdbe982ef96f15`.

Rendered ranking evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/144adea6e8f5e9a6a548fd315e60250c12216c266dd82719d973251121f8f896/f6fa00c36a23d4df1a3ec4ae333d5130ed3a137f0a31d72f9247ef6333ed845a/probability-probability-1e1820c44d4143b5478752d0-ranking.svg`.

Rendered matrix evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c18566a82b1b8f367939ce53ca6302645cfb346046c7d6d0f500d6208424aefd/466cf3243b4d34f91b831bfd99052323701becfd9bfa932e2c9f4256fe55a7dc/probability-probability-1e1820c44d4143b5478752d0-matrix.svg`.

Rendered unresolved evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b2ea2a3797105eb07b1e2e79458439b97ca23be83c54b402eb242f68b7fa06c/ce75f04a577901d159d8041463e90abac90d68f612a6d6f3ff5b1b5580dc8769/probability-probability-1e1820c44d4143b5478752d0-unresolved.svg`.

All seven scenario rows have `poolComplete=true` and `supportLevel=score_only`.

All 60 candidates in every scenario have `eligibility=unresolved`; therefore no candidate is proven eligible or ineligible and no selection probability is valid.

The 45 advance candidates have `rawValue=null` because the `brilliant_scientist_has_low_project_capacity` modifier condition remains unresolved in the trigger evaluator.

The 15 prototype candidates resolve to raw score 10 in every scenario and receive artifact ranks 1 through 15 only because they tie at 10 and the analyzer preserves deterministic candidate order; those ranks are not engine selection ranks while eligibility is unresolved.

For the advance candidates, the trace resolves the base groups as 15 candidates at `ai_low=1`, 12 at `ai_medium=5`, and 18 at `ai_high=10`.

In the three `has_war=no` scenarios, the war factor is explicitly false; in the four `has_war=yes` scenarios, the preferred factor is explicitly applied, producing trace values 2, 10, and 20 before the unresolved cautious modifier for the low/medium/high base groups.

Resource shortage, high Exposure, danger, stage-entry, and terminal-state inputs produced no additional score trace changes in this source because the project-board AI blocks only expose the war factor and low-capacity cautious factor; this is source/evaluator evidence, not a balance recommendation.

## Bounded post-owner comparison

The one bounded `hoi4.probability_compare` call used the exact retained commit `c25a4f4a944a408fb4b6dfc1dd0601cc3b551956` decision bytes as the `before.inlineClausewitz` source object and the current `common/decisions/016_brilliant_scientist_directorate_project_board.txt` path as the `after` source with raw `expectedSourceHash=6d58f497f4cb2e76537b15904acb51b75b117af0319259cb5f87d7a6b94f596b`.

The compare reused the unchanged fixture [E016_PROJECT_STAGE_LIFECYCLE_2026_09_02.scenarios.json](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_PROJECT_STAGE_LIFECYCLE_2026_09_02.scenarios.json>), scenario hash `e1f7151feebd31e36dfb88153f96ba0391f51d207de2219a70c12cd5d5d7ccb8`, and the same complete 60-candidate pool with hash `7554739e83717a355c61872e6a521ae444aeb42b9e9a08984bfb349d75248478`.

The compare returned `PROBABILITY_ANALYZED_PARTIAL`, `status=ok`, analysis ID `probability-017b22b7e749254a8f109dd8`, 420 rows, 165 top-level unresolved items, and zero diagnostics.

Compare metadata reported `comparisonChanges=0`, `adapterChanged=false`, `assumptionsChanged=false`, `regressions=[]`, and `scenarioChanges=[]`; this is bounded evidence that no score, rank, adapter, or declared-regression change was detected by the partial adapter result, not proof of unchanged engine eligibility or lifecycle behavior.

The compare cache key is `017b22b7e749254a8f109dd84fb3bc24b61b113f41e58e5ccc6324c952fce091`.

The compare result source revision is `d8b310666f681a1d6c211cc911aa7fa5efb51fc3ad7be4f2bef8f1cecd0119e5` and its normalized after-source hash is `ca9dc1e52f0120268e45c5e1790211ef3eecca82ea33b39dfd13bf5ddd8a77fa`.

The post-owner raw SHA-256 values observed for the relevant working-tree sources are decision `6d58f497f4cb2e76537b15904acb51b75b117af0319259cb5f87d7a6b94f596b`, project effects `af93ccabcb059f99bed1aedf3d47b4f9816e471e6e16ccb96df0f3964743640b`, and project triggers `5b82cb6b8a816db6039f7eab08637ca62c9fbe667487e140ddd11a89216a05e8`.

The authoritative compare JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f3e91d12209bb88335f25a3dd12d8f2eadf87bf2fa73217ef82fda37d95ae4d/0950d22770d78865cc267d92ccf6c13e28eb23d49785b91a77ebc1eaec82f387/probability-017b22b7e749254a8f109dd8.json` with artifact SHA-256 `6f3e91d12209bb88335f25a3dd12d8f2eadf87bf2fa73217ef82fda37d95ae4d`.

The rendered compare ranking evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01bdc85756e7190826cbbf8854eb4842c8dea797f8b5bcacbda7af8758c2843d/f24f8ac25a9edebe1fea81e8b90954c14c8bae908dd3b9d3cb32a52a77b5a2b9/probability-probability-017b22b7e749254a8f109dd8-ranking.svg`.

The rendered compare matrix evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c18566a82b1b8f367939ce53ca6302645cfb346046c7d6d0f500d6208424aefd/3025bc8685a58260a0e01c5281078c330d9925b76316c7e818d3d6b054d565bb/probability-probability-017b22b7e749254a8f109dd8-matrix.svg`.

The rendered compare-delta evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/3d51273938a77826f8ea54ca97e41735ad59cd2bceef8ef3247667a1a2146977/probability-probability-017b22b7e749254a8f109dd8-comparison.svg`.

The rendered unresolved evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfed145daced0646ce128ae59207857e02fdd4895ed5fb0c95502ebf21e9a2c9/331e34166721316a255f34e20ec70701ba55398e71d455e6280f302c5404a57c/probability-probability-017b22b7e749254a8f109dd8-unresolved.svg`.

All seven compare scenario rows remained `supportLevel=score_only` with unresolved eligibility evidence; the unresolved grouping was `custom_trigger_tooltip=120` and `check_variable=45`.

The `before.inlineClausewitz` object contains the exact retained decision bytes, but both comparison sides expanded helper references from the current workspace helper definitions rather than retaining separate prepatch helper bytes. This shared-current-helper context means the comparison does not isolate historical helper-definition changes and cannot establish full before/after lifecycle or eligibility equivalence.

No additional compare call is warranted for this bounded pass because the requested single source-object comparison completed; any subsequent project-helper or decision-source change requires a fresh compare with the same fixture and pool.

## Candidate-pool and external-factor completeness

The candidate pool is complete for the named 60 decisions, as confirmed by inspect and evaluate.

The seven scenario bodies declare the requested explicit external factors and state values, but the evaluator does not implement all native Clausewitz predicates and nested scope relations used by availability.

The dominant unresolved path is the nested `custom_trigger_tooltip` availability wrapper on all 60 decisions.

The second unresolved path is the compact `check_variable` form in `brilliant_scientist_has_low_project_capacity`, which is not parsed as a declared `var` and `value` pair by the evaluator.

Native `has_equipment`, `has_resources_in_country`, facility ownership/control, technology membership, stage constants, and other nested readiness conditions are not engine-proven by this pass even when corresponding fixture keys are declared.

The fixture's facility and host scopes are declared to make the intended scope inputs reviewable, but they must not be read as proof that the engine's `event_target`, `OWNER`, `PREV`, state-control, or facility predicates evaluate as intended.

No candidate override, synthetic normalized pool, hand-built simulator, or unrequested uncertain-input simulation was used.

## Findings

Finding P1, exact source score structure: the 15 prototype integration decisions use a flat `ai_high` base of 10 with no visible score modifiers in the decision file.

Finding P2, exact source score structure: each of the 45 advance decisions uses one of `ai_low=1`, `ai_medium=5`, or `ai_high=10`, multiplies by `preferred_factor=2` when `has_war=yes`, and has a `cautious_factor=0.5` modifier guarded by `brilliant_scientist_has_low_project_capacity`.

Finding P3, bounded score evidence: the four war-role scenarios differ from their peace counterparts only in the resolved `has_war` modifier; the declared defensive/offensive role labels themselves do not alter the current AI trace.

Finding P4, unresolved eligibility: no scenario proves the real available candidate pool because every candidate retains an unresolved `custom_trigger_tooltip` availability path.

Finding P5, unresolved low-capacity sensitivity: the requested capacity values are present in the fixture, but the current helper syntax prevents exact low-capacity modifier evaluation; no starvation or dominance claim is permitted.

Finding P6, no probability claim: `mission_ai_will_do` is explicitly `score_only` and the complete pool does not enable normalized probabilities for this adapter.

## Follow-up without applying changes

The owner patch for receipt-owned finish/cancel and prototype once-only behavior has been covered by the bounded comparison above; no weighted source change was part of that patch.

Any subsequent compare must use the retained commit source as the before source object and the frozen postpatch source as the after source object, not an analysis ID and not a substituted scenario body.

If the owner expects capacity-sensitive AI evidence, expose the low-capacity helper in an evaluator-supported trigger form or provide a documented native analyzer binding before interpreting score intervals.

If the design expects resource, Exposure, danger, or stage-state effects on project AI, add an explicitly approved weighted modifier plan to the decision source before asking for balance conclusions; no such weight change is authorized in this tranche.

## Remaining work and blockers

The bounded post-owner `hoi4.probability_compare` completed with partial evidence and no detected score/rank/declared-regression changes; it does not resolve native eligibility or helper provenance.

Exact engine eligibility remains unresolved for all 60 candidates due custom-tooltip availability, native resource/equipment predicates, facility target/control scopes, technology membership, and stage constants.

Exact low-capacity score sensitivity remains unresolved because the evaluator reports `check_variable requires declared var and value` for the compact helper syntax.

No timing distribution, sequence, simulation, or normalized probability analysis was applicable to this score-only adapter.

No gameplay, weights, localisation, source, or runtime files were edited; only this handoff and the named MCP scenario fixture were written.
