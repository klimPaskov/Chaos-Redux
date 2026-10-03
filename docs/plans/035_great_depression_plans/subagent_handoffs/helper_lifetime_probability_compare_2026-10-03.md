# Event 35 Helper Lifetime Probability Comparison

Status: final comparison disposition observed. The first raw-fixture request was schema-invalid and did not complete a domain comparison. The documented comparison on cell 35 returned `PROBABILITY_SURFACE_EMPTY`, with no source adapter or numeric delta. Inspect 31 timed out, and its one narrower retry on cell 37 completed with `PROBABILITY_SOURCE_DISCOVERED` and `no_weighted_surfaces`. No comparison or inspect retry in this tranche remains running. Numerical probability and ranking deltas remain unresolved.

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

## Settled documented encoding follow-up

The parent correctly identified that the first raw-fixture schema error was not a probability route outage.
It was an invalid encoding and did not complete a domain comparison.
This follow-up read the configured installation without changing tooling.

The repository MCP registration is `.codex/config.toml`: command `hoi4-agent-tools.cmd`, cwd this Chaos Redux repository, startup timeout 120 seconds, tool timeout 600 seconds.
The command resolves to `C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd`, which launches `node_modules\hoi4-agent-tools\dist\bin\stdio.js`.
That configured package reports version 3.6.0 in package.json.
The global config also names the launcher but has a different timeout, so the repository registration was retained as the relevant configuration identity.
A separate connected-process version/health response was not obtained, and no job, helper-expansion, or native-task negotiation was assumed.

`list_mcp_resources` returned no static resources.
The resource-template route returned the existing artifact byte-range template.
The installed documentation supplied the missing schema contracts:

- `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\docs\probability.md`, SHA-256 `A392933E376396FE135E25711F513FE3B0F5F09D03847455C1A95948FED030C8`.
- `schemas\probability-scenario-set.schema.json`, SHA-256 `2AB6CC512ED9D3C0EBEEBCF469BE96010654FFF1C18647F121E8A8A8532C8962`.
- `schemas\probability-compare-input.schema.json`, SHA-256 `B5FF6669A1867220E0DDCEF0F92C508486AA27E0F15DFAC884FA7C5DF75CF1CC`.
- The installed scoped-dynamic-pools example and `docs\research\probability-adapter-evidence.md` were read.
- The project Event 006 schema-probe handoff from 2026-09-20 supplies prior successful state/scopes encoding evidence but remains explicitly partial and is not treated as proof of this source's semantics.

The schema documents a set ID, per-scenario primitive state maps, typed scope bindings, primitive arrays, and scopePools.
The documented pool modes are enumeration, uniform, and proportional categorical.
There is no deterministic highest-score mode.
The adapter evidence explicitly lists arbitrary effects calculating later weights among unsupported constructs.
Accordingly the source-driven score calculation and temporary-call-frame retention cannot be made native by assigning a fabricated weight or normalizing the state scores.

All eleven v3 scenario IDs were preserved in an in-memory schema wrapper with set ID `E35_HELPER_LIFETIME_CTR35_V3_DOCUMENTED_DECLARATIONS`.
Every original scenario field, candidate, neighbor, baseCandidate field, expected outcome field, and bindingContract was retained by lossless dotted leaf-path flattening into a nonempty primitive state map.
Primitive arrays remain arrays.
Numeric state IDs remain in the saved facts and are converted to strings only for the schema's scope-candidate identifier field.
ROOT and PREV bind the exact declared country tags with nonempty state declarations.
Each per-scenario candidate catalog uses typed state entries and enumeration only, with the actual `every_controlled_state.limit` filter copied from the frozen lifetime-after source.
No candidate weight, guessed runtime getter, eligibility override, empty state, numeric score, or probability was invented.

This wrapper carries the original facts but does not claim that each raw domain key is an implemented engine-semantic input path.
Population, registry, neighbor relationships, and effect-derived scores remain unresolved where the source adapter requires a different documented semantic path.
Expected outcomes are retained as declared fixture data and are not substituted for real source predicates.
The same wrapper is used for both before and after.

The installed source schema also documents logical `path`, preserved `snapshotPath`, exact `expectedSourceHash`, identifier, and line selectors.
Its hash pattern requires lowercase hexadecimal.
An initial inspect with uppercase expectedSourceHash was rejected with `MCP error -32602: Invalid string: must match pattern /^[a-f0-9]{64}$/u at source.expectedSourceHash`.
Only the hash casing was corrected.
The subsequent bounded inspect uses the frozen lifetime-after file, logical effects path, verified lowercase B9E hash, and identifier `great_depression_score_center_candidate`.
It ran on cell 31, distinct from the older observation-lost broad inspect 64, and terminated with `timed out awaiting tools/call after 600s`. The single narrower retry added documented source line 1322 to the same source, snapshot, identifier, and hash. Its final result on cell 37 is `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`, with zero available adapters/candidates. No running inspect was duplicated.

A new mandatory compare uses the documented wrapper and logical effects path with before snapshot 3B065 and frozen after snapshot B9E, both with verified lowercase hashes and identifier `great_depression_register_initial_centers`.
Selecting the registrar includes the changed caller-storage site rather than comparing the unchanged scorer body alone.
It ran on cell 35 and returned a terminal domain error `PROBABILITY_SURFACE_EMPTY` rather than a scenario schema error. The blocker message is `No weighted blocks matched this request`, with `availableAdapters = []` and native discovery `candidatePool = []`. The blocker identifies the genuine before snapshot, expected hash, logical effects path, and registrar identifier. No weighted source candidate was admitted, so no before/after numerical evaluation occurred.

That native empty candidate catalog is a source-adapter discovery result. It does not say that the saved state catalog is empty or that no center is eligible in the game. The saved facts, eleven IDs, actual target filter, and candidate catalogs were retained in the documented request.

The compare result has no artifacts, comparison ID, analyzer revision, scenario hash, score trace, or renderable analysis. No documented compare timeout occurred, so a timeout retry of that comparison is not applicable. Inspect retry 37 is now observed terminal, and its discovery artifact and revision are retained below.
These distinct documented requests do not restart the uncertain earlier inspect.
Preserve their observation handles and do not infer operation failure from a later observer loss.

The parent testing-finalized notice has arrived. The separate reclosure comparison has now settled with an explicit helper-source adapter limitation in `reclosure_probability_compare_2026-10-03.md`. This updates the earlier waiting status without changing the lifetime snapshots or fixtures.

The final parent repair handoff records successful exists search and section read in workspace ea3b2d67c2c0, section ID `1e3f8f4659110cd807c118f6cab4611811385a392f866b9d72a4a8039ae10cf8`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`. This supersedes the earlier reported pending reference-read status. Older parent cell 22 remains observation-lost and unknown. Neither parent handle was polled or duplicated by this auditor.

The probability snapshot selector freezes the selected file only. Installed documentation explicitly states that shared helpers and constants still come from the configured workspace. This is not a complete historical workspace or campaign snapshot, and any dependency mismatch must remain unresolved in returned source evidence.

## Settled documented compare response

The exact structured response from the schema-supported request is retained below.
This is an explicit unresolved source-adapter outcome, not a completed numeric comparison or a route outage.

```json
{
  "artifacts": [],
  "blockers": [
    {
      "code": "PROBABILITY_SURFACE_EMPTY",
      "details": {
        "availableAdapters": [],
        "candidatePool": [],
        "source": {
          "expectedSourceHash": "3b065e7fc529fa4e8a98b7caf60656ecc2fd22970944b966329986b85d1b1403",
          "identifier": "great_depression_register_initial_centers",
          "path": "common/scripted_effects/035_great_depression_effects.txt",
          "snapshotPath": "docs/plans/035_great_depression_plans/audit_inputs/helper_lifetime_2026_10_03/035_great_depression_effects_before.txt"
        }
      },
      "message": "No weighted blocks matched this request"
    }
  ],
  "changedFiles": [],
  "code": "PROBABILITY_SURFACE_EMPTY",
  "data": {},
  "diagnostics": [],
  "filesScanned": [],
  "proposedFiles": [],
  "status": "error",
  "validation": {
    "checks": [],
    "passed": false
  },
  "workspaceId": "mod_chaos_redux_ea3b2d67c2c0"
}
```

## Final narrower inspect receipt

The exact terminal structured result from retry 37 is retained below.

```json
{
  "artifacts": [
    {
      "description": "Weighted-source adapter inventory and candidate examples",
      "mimeType": "application/json",
      "name": "probability-inspect-b770cb213e73.json",
      "sha256": "45595582fd2eb50f46cab18025136dbad0a53eabfb62b8c919295bea6693b5b6",
      "size": 349,
      "uri": "hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45595582fd2eb50f46cab18025136dbad0a53eabfb62b8c919295bea6693b5b6/6ebd8516b69f1d22e4c7931478cb2f88a784f6f088596e76337f09e38e2e1b01/probability-inspect-b770cb213e73.json"
    }
  ],
  "blockers": [],
  "changedFiles": [],
  "code": "PROBABILITY_SOURCE_DISCOVERED",
  "data": {
    "adapterRequiredInputPaths": [],
    "adapters": 11,
    "availableAdapters": [],
    "availableCandidates": 0,
    "candidateExamples": [],
    "candidates": 0,
    "discoveryReason": "no_weighted_surfaces",
    "requiredInputPaths": [],
    "requiredInputPathsTruncated": false,
    "requiredInputs": 0,
    "sourceHash": "b770cb213e7315c5e9273ffcbb713f9b8a1f69a2d1bc0ddf655d14f17d59d8b9",
    "sourceRevision": "3f7b0cb139ba23c4924e26dca3a1557ced542291e1fd3aae033291109f59c61b",
    "unresolved": 0
  },
  "diagnostics": [],
  "filesScanned": [
    "mod:docs/plans/035_great_depression_plans/audit_inputs/reclosure_2026_10_03/035_great_depression_effects_before.txt"
  ],
  "proposedFiles": [],
  "status": "ok",
  "validation": {
    "checks": [],
    "passed": true
  },
  "workspaceId": "mod_chaos_redux_ea3b2d67c2c0"
}
```

Its analyzer revision is `3f7b0cb139ba23c4924e26dca3a1557ced542291e1fd3aae033291109f59c61b` and analyzer source hash is `b770cb213e7315c5e9273ffcbb713f9b8a1f69a2d1bc0ddf655d14f17d59d8b9`.
The discovery artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45595582fd2eb50f46cab18025136dbad0a53eabfb62b8c919295bea6693b5b6/6ebd8516b69f1d22e4c7931478cb2f88a784f6f088596e76337f09e38e2e1b01/probability-inspect-b770cb213e73.json`, declared size 349 bytes.
Resource read returned `Mcp error: -32603: Artifact provenance manifest is unavailable`.
The completed tool response is retained, but unread artifact contents and a numerical comparison were not invented.
Zero candidates and no weighted surfaces do not prove campaign balance or full fixture eligibility.
