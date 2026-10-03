# Event 35 Helper Lifetime Probability Comparison

Status: parent patch is source-reviewed, but mandatory MCP comparison returned a schema validation error. Numerical probability and ranking deltas remain unresolved.

## Before and after identities

The genuine before-source is `docs/plans/035_great_depression_plans/audit_inputs/helper_lifetime_2026_10_03/035_great_depression_effects_before.txt`, SHA-256 `3B065E7FC529FA4E8A98B7CAF60656ECC2FD22970944B966329986B85D1B1403`.
The MCP comparison after path was `common/scripted_effects/035_great_depression_effects.txt`, captured after the lifetime patch at SHA-256 `B9E01DE3EB2CC97FA31E73188745AF77A1EEF28F07D86AC51AC0346385AA28A9`.
Those after bytes are preserved independently at `docs/plans/035_great_depression_plans/audit_inputs/reclosure_2026_10_03/035_great_depression_effects_before.txt`, so later owner reclosure edits cannot substitute for this lifetime after-state.
This was not a current-to-current comparison.

The parent-confirmed interim hash before the two weighted additions was `6DA8BF85559ACD08FD6E36ACDBE886C88DB006D90031C876531FCB684BA8987C`.
The baseline report's mistaken effects value was a transcription error that copied the trigger suffix.
The corrected interim value is attributed to the parent's historical capture, not to current-file hashing.
The supporting trigger file independently rehashed with Get-FileHash and certutil to `FE2DC15DC22EA0D8F9336C7120412B1DA66CF7F7348D43E7EE1D7A72BC1566CA`.
The constants hash remains `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`.

## Source delta and conditional storage contract

A read-only diff between the two preserved effects files contains exactly four caller initializations and one comment.
There is no changed score formula, modifier, coefficient, candidate gate, state-ID tie break, or ticket-building loop in that diff.
This proves the source delta only and does not establish native execution.

| Caller and output | Before under conservative return cleanup | After under the same model |
| --- | --- | --- |
| `great_depression_select_independent_target`: `great_depression_independent_target_weight` | Scorer first creates the scalar in its own frame, which is discarded before caller ticket construction | Caller creates storage with zero, scorer overwrites it, and the helper assignment remains after return |
| `great_depression_register_initial_centers`: `great_depression_center_candidate_score` | Scorer first creates its scalar, which is discarded before caller score comparisons | Caller creates storage with the existing invalid-score constant, scorer overwrites it, and the score remains after return |
| `great_depression_initialize_new_crisis`: `great_depression_center_registration_failed` | Registrar creates its status internally, which is discarded before caller abort gate | Caller-owned initial one provides the fail-closed seed and retains the registrar's changes |
| `great_depression_deepen_active_crisis`: `great_depression_deepening_value` | Resolver creates its amount internally, which is discarded before severity and trend consumers | Caller-owned zero retains the resolver's existing assignment |

This model keeps separate caller and callee temporary frames, discards both scalar and array storage first created in a returning callee, and retains changes to inherited caller storage.
Scoped persistent variables and registries are tracked separately.
No flat global temporary dictionary, implicit missing-variable zero, or invented engine read behavior is used.
The initial zero and invalid-score seeds do not replace the formulas because both scoring helpers begin by assigning their output.
For identical inputs the intended helper formulas are equal before and after, while output retention differs under the declared conservative model.
This is bounded source-contract evidence conditional on that model, not an analyzer result or a live-game observation.

The independent selector uses weighted ticket replication followed by random array selection.
The center selector uses a deterministic maximum score with first-valid-candidate presence and an unchanged state-ID tie break.
Neither a willingness score nor this center ranking is an exact click probability.

## Preserved scenarios and completeness

The original report-only lifetime fixture remains untouched at SHA-256 `8B921CD7205797D1314E3BF778328AEBA1911E6DE9E13498366E1286524E1E84`.
The saved center v2 fixture remains `F348094B23CD57F16C067DB32C5C7F4BD2E6CE780145E3C6B4808346743C63C3`.
The saved center v3 fixture remains `2C92489F1C2764C729096B2FF88505A3E8F653D204E6F92F76B1627B4134BF66`.

The submitted v3 fixture preserved these exact IDs: `CTR35-ROOT-ACTOR`, `CTR35-ROOT-DIFFERENT`, `CTR35-FOREIGN-ROOT-NEIGHBOR`, `CTR35-NO-CENTER-NEIGHBOR`, `CTR35-CAPITAL`, `CTR35-TINY-CAPITAL`, `CTR35-NEGATIVE-TIE`, `CTR35-FORBIDDEN-PRIMARY+validother`, `CTR35-RESERVED-OTHER-EPISODE+validother`, `CTR35-ALL-RESERVED-OR-FORBIDDEN`, and `CTR35-FROZEN-FORBIDDEN-CLEARED-LIVE`.
The first seven are also the v2 IDs.
Each corresponding fixture declares a complete bounded state pool for its own domain contract, including the singleton tiny-capital case and two-state cases.
The entire saved v3 JSON object was passed unchanged as the scenarioSet for live validation.
No actor, state, eligibility, candidate override, or engine-state fields were synthesized.
The MCP rejected that domain encoding, so native external-factor coverage and the score/rank comparison remain unresolved for all eleven IDs.

The original independent-target scenarios `TGT-01` through `TGT-10` still lack a supplied complete country-pool fixture and full candidate factors.
Every TGT numerical probability and selection-rank conclusion remains unresolved.
No fake country pool, nominal normalization, distribution, cadence, seed, or sequence model was added.

## MCP calls and exact outcome

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
The post-patch probability inspect was issued before comparison with adapter `custom_weighted_pool` and the actual effects source.
Its original observation handle was cell 64.
On resume, observing it returned `exec cell 64 not found`.
That is observation loss, not proof the server operation failed.
No duplicate inspect request was sent.

The live exposed compare schema accepts before and after source objects, required scenarioSet, optional adapter and outputs.
Its nested scenarioSet was exposed as unknown.
The mandatory `hoi4.probability_compare` request used genuine before/after paths, the unchanged saved v3 object, outputs `json`, `comparison`, and `unresolved`, and refresh enabled.
Adapter was omitted because no deterministic center-race adapter had been confirmed, and no weighted sampling interpretation was imposed.
The request returned the following terminal input validation error before a source analysis result:

```text
MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Invalid input: expected string, received undefined at scenarioSet.id
Invalid input: expected record, received undefined at scenarioSet.scenarios[0].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "capital", "actorCenterRegistryStateIds", "candidatePool", "neighborStates", "actorActiveEpisodeId", "otherActiveEpisodeIds" at scenarioSet.scenarios[0]
Invalid input: expected record, received undefined at scenarioSet.scenarios[1].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "capital", "actorCenterRegistryStateIds", "candidatePool", "neighborStates", "actorActiveEpisodeId", "otherActiveEpisodeIds" at scenarioSet.scenarios[1]
Invalid input: expected record, received undefined at scenarioSet.scenarios[2].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "capital", "actorCenterRegistryStateIds", "candidatePool", "neighborStates", "actorActiveEpisodeId", "otherActiveEpisodeIds" at scenarioSet.scenarios[2]
Invalid input: expected record, received undefined at scenarioSet.scenarios[3].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "capital", "actorCenterRegistryStateIds", "candidatePool", "neighborStates", "actorActiveEpisodeId", "otherActiveEpisodeIds" at scenarioSet.scenarios[3]
Invalid input: expected record, received undefined at scenarioSet.scenarios[4].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "capital", "actorCenterRegistryStateIds", "candidatePool", "neighborStates", "actorActiveEpisodeId", "otherActiveEpisodeIds" at scenarioSet.scenarios[4]
Invalid input: expected record, received undefined at scenarioSet.scenarios[5].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "capital", "actorCenterRegistryStateIds", "candidatePool", "neighborStates", "actorActiveEpisodeId", "otherActiveEpisodeIds" at scenarioSet.scenarios[5]
Invalid input: expected record, received undefined at scenarioSet.scenarios[6].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "actorCenterRegistryStateIds", "candidatePool", "neighborStates", "actorActiveEpisodeId", "otherActiveEpisodeIds" at scenarioSet.scenarios[6]
Invalid input: expected record, received undefined at scenarioSet.scenarios[7].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "actorActiveEpisodeId", "otherActiveEpisodeIds", "actorCenterRegistryStateIds", "candidatePool", "neighborStates" at scenarioSet.scenarios[7]
Invalid input: expected record, received undefined at scenarioSet.scenarios[8].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "actorActiveEpisodeId", "otherActiveEpisodeIds", "actorCenterRegistryStateIds", "candidatePool", "neighborStates" at scenarioSet.scenarios[8]
Invalid input: expected record, received undefined at scenarioSet.scenarios[9].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "actorActiveEpisodeId", "otherActiveEpisodeIds", "actorCenterRegistryStateIds", "candidatePool", "neighborStates" at scenarioSet.scenarios[9]
Invalid input: expected record, received undefined at scenarioSet.scenarios[10].state
Unrecognized keys: "root", "candidateOwner", "centerNeighborOwner", "expectedAdjacencyPenalty", "actorActiveEpisodeId", "otherActiveEpisodeIds", "actorCenterRegistryStateIds", "event34SnapshotRegionStateId", "event34SnapshotRegionConversionForbidden", "greatDepressionRegionCallStateId", "greatDepressionRegionCallConversionForbidden", "recipientSourceStateId", "candidatePool", "neighborStates" at scenarioSet.scenarios[10]
Unrecognized keys: "surface", "selection", "baseCandidate", "bindingContract" at scenarioSet
```

The settled result is a schema gap.
The error reveals a required set ID and per-scenario state record but does not define how to represent the fixture's actor, state relations, registry, episode, adjacency, or raw candidate pool.
Adding empty state records would discard the relevant facts.
Moving those facts into guessed fields would invent an analyzer model.
Neither repair was attempted.

The result was not a timeout, so the required narrower-on-timeout retry was not applicable.
There is no comparison ID, analyzer revision, analyzer source hash, scenario hash, artifact URI, rank delta, numeric modifier trace, or rendered comparison.
Render cannot run without an analysis ID.
Evaluate/sweep were not used to bypass the rejected mapping.
Simulation and sequence were not applicable to these fixed storage contracts.
Native AI validity, dominance, starvation, rank reversal, repetition, timing drift, and exploit-risk conclusions remain unresolved.

## References and scope

Offline Data structures, Variable types, lines 435-442, especially line 440, supplies the temporary lifetime rule used by the conservative model.
Installed effects documentation, set_temp_variable, lines 7820-7826, supplies assignment syntax and scope support.
The vanilla `common/scripted_effects/SWE_scripted_effects.txt`, lines 228-239, was read and preinitializes `tooltip_folkhemmet_intactness` before the calculation helper.
These precedents corroborate caller storage but do not replace MCP probability evidence.
The already-read events, subagents, and planning skills governed the audit.
Parent reference-search handle 22 is untouched and its final result is not assumed.

Only this report and the narrow baseline hash correction belong to this comparison write set.
The original before snapshot and existing fixtures were not edited.
No gameplay, index, commit, HOI4 launch, logs request, or external-tooling modification occurred.

