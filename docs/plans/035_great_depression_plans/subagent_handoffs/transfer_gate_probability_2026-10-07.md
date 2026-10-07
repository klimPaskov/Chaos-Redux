# Event 35 Transfer-Gate Probability Audit — 2026-10-07

## Status

Baseline source-gate finding delivered to the parent before the accepted selector-helper OR patch. This is a bounded read-only handoff, not completion of the larger Event 35 goal.

The parent owns the gameplay edit. This auditor made no gameplay, AI, event, decision, trigger, effect, localisation, test, or other repository-source changes.

The final after-source copy has arrived and the mandatory same-case `hoi4.probability_compare` was attempted. The connected `decision_ai_will_do` adapter returned terminal `PROBABILITY_SURFACE_EMPTY` when given the before/after scripted-trigger snapshots because neither snapshot contains weighted blocks. The comparison is therefore unresolved, not pending and not timed out. Do not substitute the earlier partial evaluation below as though it were this fixture's native scenario projection.

## Audited surface and source identity

The targeted decision is `great_depression_select_depression_center` in `common/decisions/035_great_depression_decisions.txt`, lines 409–438. Its `target_trigger` and `available` both call `great_depression_center_is_valid_selector_target`; the selector effect dispatches to `great_depression_select_center`.

The exact immutable baseline helper is `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt`, frozen at `docs/plans/035_great_depression_plans/audit_inputs/transfer_gates_2026_10_07/before/surface_triggers.txt`, SHA-256 `6A829ADEA9C72D08B62B2510082FD67253B3633D11CE49F14D402CD6E05D6F8C`. The live helper file matched those frozen bytes when checked.

The decision source SHA-256 at baseline inspection was `C99B4C5498494D187E3E81712756F20FE812E7DB7713D756A2FF6E9B25279067`. No immutable before-copy of that decision file was supplied in this transfer-gate folder; the gate patch target is the frozen trigger file, and the selector's AI expression is unchanged.

The immutable source-contract fixture is `docs/plans/035_great_depression_plans/audit_inputs/transfer_gates_2026_10_07/scenarios.json`, ID `E35_TRANSFER_GATE_20261007`, SHA-256 `16BBEEF25DB57F94F4F6FDC70C38BFCACE1FF8208D5AB77C84688250E142DBAE`. It explicitly says it is not a native scenario wrapper.

## Baseline predicate trace

At `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt:753–789`, `great_depression_center_has_current_registration` requires a coherent active crisis, a state episode variable equal to the actor's active episode, and exact membership in `ROOT.great_depression_center_state_ids`.

The baseline `great_depression_center_is_valid_selector_target` retains the ownership, control, center-flag, not-liquidated, viable-population, and factory predicates. Its hidden eligibility branch is `current registration OR (transfer receipt AND open transfer contract AND coherent crisis AND center_count < registry_cap)`.

Therefore an open transfer's already-listed returning state is rejected at full capacity when its state episode does not yet match the actor episode: the current-registration branch fails, and the transfer branch unconditionally requires spare capacity. The accepted relationship is to allow an exact existing recipient-array row OR spare capacity inside the receipt/open-contract branch; this preserves the transfer contract guard and does not admit the stale closed-transfer case.

| Scenario | Fixture state | Baseline source-predicate result | Expected after | Finding |
| --- | --- | --- | --- | --- |
| `XFER-EXISTING-AT-CAP` | Existing row; count 4 of cap 4; receipt/open true; actor episode 35, state episode 77 | Excluded: current registration fails the episode equality, and the transfer branch fails the strict spare-capacity predicate | Selectable | Confirmed source-gate defect |
| `XFER-EXISTING-BELOW-CAP` | Existing row; count 2; receipt/open true; actor episode 35, state episode 77 | Selectable through the transfer branch because count 2 is below cap 4 | Selectable | Preserved behavior |
| `XFER-NEW-AT-CAP` | No existing row; count 4; receipt/open true | Excluded because the state is not currently registered and there is no spare capacity | Not selectable | Correct cap behavior to preserve |
| `XFER-NEW-BELOW-CAP` | No existing row; count 2; receipt/open true | Selectable through the transfer branch because capacity remains | Selectable | Preserved behavior |
| `XFER-FOREIGN-CONTROLLER` | Existing row; count 4; state owner AAA, controller BBB | Excluded by the unchanged `is_controlled_by = ROOT` filter before the hidden row/cap branch | Not selectable | Correct controller filter to preserve |
| `XFER-STALE-EPISODE` | Existing row; count 4; actor episode 35, state episode 77; receipt/open false | Excluded: current registration fails episode equality and the transfer receipt/open guard is false | Not selectable | Correct stale/closed-transfer behavior to preserve |

The fixture's common bindings are actor `AAA`, state `121`, actor episode `35`, state episode `77`, transfer open and receipt true, population `8,000k`, three civilian factories, state owner/controller `AAA`, and registry cap `4`, with per-case overrides shown by the table. These are explicit source-contract fixture values, not claims about a live save, a native wrapper, or current campaign state.

The proposed boolean OR must remain subordinate to both the transfer receipt and open-contract predicates. The `XFER-STALE-EPISODE` expected false result is why bare array membership outside that transfer guard would be incorrect.

## AI score versus gate eligibility

The selected-center decision's `ai_will_do` is static `base = constant:great_depression_ai_weight.blocked`. The parent identifies this as the existing zero/static AI score and reports no coefficient changes. The baseline defect is target visibility/selectability through a boolean predicate, not a weighted-score change.

The connected decision AI adapter explicitly reports `selectionRule = score_only` and `normalizedProbability = false`. No click probability, normalized selection probability, or selector-pool ranking claim is made here.

## Native MCP evidence and limits

The connected probability workflow was started with `hoi4.probability_inspect` for `decision_ai_will_do` on `common/decisions/035_great_depression_decisions.txt`. It terminated `PROBABILITY_SOURCE_INSPECTED`; the tool reported 79 candidates, `poolComplete=false`, zero available candidates without scenario bindings, zero discovered required inputs, and zero unresolved source references. This broad decision count is not needed to establish the discrete helper finding.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c88c5e50cd1c196dea78cea9e8c5a7918870e0b63aecccbfcff2f5f5fe534496/afb5f1303249751e89087c9f3307039feb250d48636e758738d4417bcf835fb9/probability-inspect-b37d305b9a56.json`, declared SHA-256 `c88c5e50cd1c196dea78cea9e8c5a7918870e0b63aecccbfcff2f5f5fe534496`, size 6,875,115 bytes, source revision `215d6d3e95989fd278852c8841d72430c6480d083ba6d3b5f46e21cfbb289336`, parser source hash `b37d305b9a56cddf574f4c235e2840e8e6682b216988f11c354061574f3fdf3d`.

A six-ID `hoi4.probability_evaluate` call terminated `PROBABILITY_ANALYZED_PARTIAL` for the target decision only. It returned `score_only`, six candidate-scenario rows, six unresolved candidates, zero resolved eligible/excluded candidates, and 11 unresolved analysis items; the unresolved traces include missing actor and `has_cosmetic_tag` inputs. It did not return a raw score value for the rows, and it proves neither gate eligibility nor a normalized probability. Its constructed state map predates discovery of the immutable `E35_TRANSFER_GATE_20261007` fixture and is not a valid comparison baseline for that fixture.

Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2f0dea5fbe613fa715d79961e2753974829de5f4003f9e012ca9934cbf4a1ac/3e0142df16201bf9c66c367347ddd3133afad75dd0573dc7cdc1dda2137328be/probability-b6c8fb7ad9f7c24cb5da762e.json`, declared SHA-256 `c2f0dea5fbe613fa715d79961e2753974829de5f4003f9e012ca9934cbf4a1ac`, size 382,414 bytes, analysis ID `probability-b6c8fb7ad9f7c24cb5da762e`, scenario hash `63a84ca7e87d99c70218245aa501a52dd96dac4f4f02139d9e29143c28411cd8`, source revision `fa6bed0a15f1cf882ee3389ca7e3401d5adcfbafef3b3a02a02890a8651caa1f`.

The evaluate call returned ranking, waterfall, and unresolved render artifacts, but these are not meaningful rankings of selectable choices because the only selected candidate's eligibility remained unresolved and the adapter is score-only. No separate `probability_render` call was made.

After-source `hoi4.probability_inspect` was narrowed to candidate `great_depression_select_depression_center`. It terminated `PROBABILITY_SOURCE_INSPECTED` with one candidate and `poolComplete=true` for that selected candidate, zero required inputs, and zero unresolved source references; it still reports the score-only adapter and does not establish a full decision-selection pool or target-gate result. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab78c044e7503b74da1436797b28dcda5076c72f6a4d577bd7fe5fff6c42b63f/759450baa4def485359d52d3b23b8b1b0f084374c3b1d8a896de55a1f3a15989/probability-inspect-b37d305b9a56.json`, declared SHA-256 `ab78c044e7503b74da1436797b28dcda5076c72f6a4d577bd7fe5fff6c42b63f`, size 14,456 bytes, source revision `02fab2168c20db9b53435faac0f538f3432cdbba7eab7ef9c04ba1b2962d4f26`, parser source hash `b37d305b9a56cddf574f4c235e2840e8e6682b216988f11c354061574f3fdf3d`.

The same-case compare request used adapter `decision_ai_will_do`, selected candidate `great_depression_select_depression_center`, the six IDs in `E35_TRANSFER_GATE_20261007`, and the immutable full helper snapshots as before/after sources. The first attempt was rejected because the live schema does not accept a custom `sourceContract` field in a scenario row. One narrower retry removed that field and retained only accepted `id`, `actor`, and `state` scenario fields; it terminated with `PROBABILITY_SURFACE_EMPTY`, message `No weighted blocks matched this request`, because the logical source path was `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt`. No comparison artifact or numeric delta was produced. This is a source-kind limitation, not a timeout; no timeout retry or same-live-file substitution was made.

The after snapshot is the complete 2,672-line helper file, not a delta excerpt: `docs/plans/035_great_depression_plans/audit_inputs/transfer_gates_2026_10_07/after/surface_triggers.txt`, SHA-256 `27BC69FC602B9C553E6A9E95820595BF16D6F5CC251C1588D75311C2E7F201FA`, 106,633 bytes. The live `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` matched those after bytes at verification. The full before-to-after diff has two change groups:

1. `great_depression_center_is_valid_selector_target`: under the existing transfer-receipt/open-contract and coherent-crisis guards, the registry condition is now `exact state in great_depression_center_state_ids via PREV OR center_count below cap`.
2. `great_depression_reopen_depression_center_context_is_valid` and `great_depression_reopen_depression_center_objective_is_met`: the authorized reopen path additionally requires coherent project duration, excludes the protection project type, matches the exact project authorization, requires a positive mission authorization and a future recorded deadline, and requires the completed project receipt to match that authorization. This F1/F5 timing-context correction is present in the same full after snapshot and is unrelated to the six selector cases.

The decision source still has raw SHA-256 `C99B4C5498494D187E3E81712756F20FE812E7DB7713D756A2FF6E9B25279067`, equal to its baseline identity. Its static `ai_will_do` expression is unchanged; the compare route could not evaluate that decision block from trigger-only snapshot paths. The fixture provides source-contract booleans and values, but native target scope, transfer/state flags, owner/controller, and array binding are not represented by a live probability schema in the supported call. The adapter result for those boolean cases must remain unresolved rather than being promoted to native projection.

A corrected `hoi4.decision_inspect` request for the six IDs reached terminal `DECISION_ANALYZED_PARTIAL`, not timeout, with a whole-installation inventory of 8,310 decisions and 2,070 categories, 100 unresolved definitions, and incomplete coverage. Its synthetic actor/state bindings were not the source-contract fixture, so this broad result is not used to prove any case. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/265085cf58c3f95decc23fc47f281de88de5bd3d2d550dba41d0f0b8acf6e1ca/4e2c81b99c8e597379bc6e84c3697d8e634a1003afff7e0b39b9b8a4291c0324/decision-12a36f80982545a1c5382c04.json`, declared SHA-256 `265085cf58c3f95decc23fc47f281de88de5bd3d2d550dba41d0f0b8acf6e1ca`, size 5,002,009 bytes, report hash `12a36f80982545a1c5382c0408be803a6c19f5fc66cbcd000a7517d1abeb7ae9`, source revision `8ae6541434c0a2a85e07c56e4e42dc12f312745c69364d26e582ba8a3d11fa77`.

The bounded `hoi4.source_lookup` at trigger line 765 completed with source revision `02a1d657a69c64464d1f4c0d85be4ba0465e0bbfd4ac1eec328bb6b2392b39ea`, `complete=true`, and owner `great_depression_center_is_valid_selector_target` at lines 765–789.

## References

The installed vanilla decision documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md`, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. It defines target-root and target-trigger scope/cadence and the `any_controlled_state` selection behavior.

The installed vanilla trigger documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, `is_in_array`, lines 5672–5685, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`. The source uses the documented array-membership trigger.

Offline wiki search surfaced Decision modding, “State targeted decisions,” lines 576–595, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, and Data structures, `is_in_array`, line 1147, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`. The bounded wiki section reads were not completed before this urgent handoff; no wiki-specific claim is based on un-read text.

## Compare boundary and remaining work

The after copy is preserved and was not overwritten. The compare route's terminal surface-empty result means the weighted delta is unresolved at the probability adapter boundary; source identity independently supports that the selected decision's static AI expression is unchanged, while the selector-gate effect remains the bounded source-predicate result in the table above.

No `probability_sweep` was run because the only changed selector predicate is a boolean target-eligibility gate, the AI score is static, and the connected score adapter does not accept the scripted-trigger file as a weighted surface. Sweeping the unrelated decision score would not test the count/array gate. No `probability_render` was run after compare because compare returned no analysis artifact.

The parent owns the selector helper edit and the separate duration work. No Event 35-wide completion claim is made. No game launch, runtime test, or native campaign observation was performed. The parent's duration `event_inspect`/`event_render` pending cell 187 was not called, duplicated, or altered by this auditor.
