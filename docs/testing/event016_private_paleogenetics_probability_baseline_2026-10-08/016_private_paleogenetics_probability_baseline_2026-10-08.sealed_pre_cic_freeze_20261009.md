# Private Paleogenetics probability baseline and matched comparison — 2026-10-08

Status: bounded audit delivered on 2026-10-09 for parent review and commit of the paired Deployment tranche. The mandatory comparison of the four existing stage actions is complete under the unchanged eight-case fixture. The result is partial and score-only; full Paleogenetics, Event016, global AI balance, and live-engine acceptance remain open.

Ownership: this audit changed only this handoff and its unique evidence directory, `docs/testing/event016_private_paleogenetics_probability_baseline_2026-10-08/`. No gameplay, assets, models, focus files, index, Git state, or HOI4 process were changed. Staffing, transport, demobilization, and breeding remain outside this bounded audit as explicitly queued parent work.

## Evaluated source identities

The authoritative before decision is `before/common/decisions/016_mengele_paleogenetics_stage_decisions.txt` under the evidence directory: 13,922 bytes, SHA-256 `4bf57705a70d201a8e44a2fec8de571d6e556bbe22830a1a2773df7617dcb941`. The before manifest preserves nine decision/helper/constants/documentation copies, including the prepatch Paleogenetics decision-trigger hash `a457bd6f889ea2ef163ea4f0d536aab8213377737dde496a63f2f35a8d8bcf0a`. Its manifest SHA-256 is `1a6b346328885a17942c1467dda484c94e96a491c38c846139b0c3a9487828b8`.

The final current after point is `after_20261009_native_tech_final/source_manifest.json`: 16 source copies, manifest SHA-256 `92ad580b3991a45a89887d1f725cdaa9467e1e513880b7dd9d106b8b00928502`. All 16 copies and their live logical files matched that manifest at sealing. The earlier `after/` and `after_20261009/` snapshots remain historical and were not overwritten.

| Final logical source | Raw SHA-256 |
|---|---|
| `common/decisions/016_mengele_paleogenetics_stage_decisions.txt` | `0ad338e3597d2f855b80282c505acda4cf6fceba5e468de8204de0fb97a41653` |
| `common/decisions/016_mengele_paleogenetics_site_selection_decisions.txt` | `cfd888f424460669e24c0b9e78afb65c2082169e7f480ef71a16b0d0594b9d65` |
| `common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt` | `5863eb3de1256da1bb4efb51c236bb3653e49e9dfed3715eb88a83297b6c1ea6` |
| `common/scripted_triggers/016_mengele_paleogenetics_deployment_triggers.txt` | `e91c16b6e6e3cbac98402f2793fbc2d50679f57dedb40cbbcce4855efd1eb429` |
| `common/scripted_effects/016_mengele_paleogenetics_deployment_effects.txt` | `e63d9796f7c4d60f397d28a36c36ddc62d86fa4d339ea03513a907e7591be2b8` |
| `common/scripted_effects/016_mengele_project_stage_effects.txt` | `1ba88b35ca82d5a03364d2b2e19ba689fa29603af3173228f02841c74eaac4a7` |
| `common/script_constants/016_mengele_paleogenetics_deployment_constants.txt` | `89658928cf2db2cc7d602b5306f25c58c9ccd42b6882bc4a556453810fb3b0c8` |
| `common/script_constants/016_brilliant_scientist_project_constants.txt` | `a95301ed9cbc7bb8fcb751885165f62ae5aa8c6b315eadb0c5cdaf79350ce131` |

The final admission helper requires the selected distinct pair and actual `has_tech = brilliant_scientist_paleogenetic_formations_tech`, matching the core debit preflight. Its cancellation helper also checks Prototype and technology loss. Deployment retains 130 PP, 975 aggregate support equipment, 1,500 fuel, four native CIC, and 480 days. Its source-bound native-entry marker prevents the direct affordability helper from counting the already reserved native factories twice. Decision availability still owns the four-free-CIC check.

The new clear-selection visibility is `choice_is_open` plus the OR of either selected reserve or selected hatchery variable. It therefore exposes manual clearing of partial selection; its authored AI base remains zero. Neutral Prototype operational access remains independent of paid paired Deployment.

## Weighted surfaces and adapter scope

The initial required `decision_ai_will_do` inspect of the before stage file returned `PROBABILITY_SOURCE_DISCOVERED`, `requested_adapter_empty`, and suggested `mission_ai_will_do`. The matching mission inspect found four candidates with `poolComplete=true`: `mengele_event016_paleogenetics_theory`, `mengele_event016_paleogenetics_prototype`, `mengele_event016_paleogenetics_deployment`, and `mengele_event016_paleogenetics_weaponization`. This establishes the pool for the selected file, not the full Biological Programs category or the game's decision competition.

| Existing timed stage | Source base | War factor | Cautious factor and source threshold |
|---|---:|---:|---|
| Theory | 5 | 2 | 0.50 when project-available CIC does not exceed 1 |
| No-DLC Prototype | 10 | 2 | 0.50 when project-available CIC does not exceed 2 |
| Deployment | 5 | 2 | 0.50 when project-available CIC does not exceed 4 |
| Weaponization | 5 | 2 | 0.50 when project-available CIC does not exceed 6 |

These are `brilliant_scientist_project_board.ai_medium = 5`, `ai_high = 10`, `brilliant_scientist_project_ai.preferred_factor = 2`, and `cautious_factor = 0.50`. All four before/after `ai_will_do` blocks were text-identical. Their bases are willingness scores; they are not percentages or click probabilities. The adapter version is `hoi4-1.19.2.v1`, with raw-score and eligibility support, `normalizedProbability=false`, `timeDistribution=false`, and a documented runtime selection boundary. The installed game was verified as Operation Postern 1.19.2.0, checksum d245.

The four new instantaneous actions use `decision_ai_will_do`: `mengele_event016_paleogenetics_select_reserve`, `mengele_event016_paleogenetics_select_hatchery`, `mengele_event016_paleogenetics_clear_site_selection`, and `mengele_event016_paleogenetics_recover_deployment`. Their authored bases are 5, 5, 0, and 5 respectively. The map selections require `scope.FROM`; the after inspect found four definitions. A first inspect with the explicit new candidate list returned `INTERNAL_ERROR`; the minimal source-only retry succeeded. This is retained as a recovered request failure, not an unavailable probability adapter.

Before-side inspect with those four new IDs against the frozen stage source returned zero decision-adapter candidates and `candidatePoolMatches=0`. The new site-selection file is absent from the captured before source set, consistent with the parent's new-file declaration. There is no valid numeric before score for these additions, and no zero baseline or numeric before/after comparison was invented for them.

## Frozen eight-case fixture and retained baseline

The original fixture is preserved verbatim at `016_private_paleogenetics_probability_baseline_2026-10-08.scenarios.json`: 17,114 bytes, local SHA-256 `c48d2a513d404d1f7c150e6b62079f6d2d354e8b50798158f9b183dece014331`. Its canonical MCP scenario hash is `698d26b94d12afdb4739a13e7c0645a58a09a6ec484d8d9be0d9e0e19b6c5a58`.

The eight IDs are `PALEOGENETICS_PEACE_SPARE`, `PALEOGENETICS_WAR_SPARE`, `PALEOGENETICS_EXACT_4_CIC`, `PALEOGENETICS_BELOW_4_CIC`, `PALEOGENETICS_PROVIDER_LOST`, `PALEOGENETICS_PREDECESSOR_ABSENT`, `PALEOGENETICS_FAMILY_BUSY`, and `PALEOGENETICS_COMPLETED`. They declare actor MCL, source flags and variables, resource reserves, stage receipts, and factory counts 7/4/3. No candidate overrides or closed-world assertion were supplied. Exact-four and below-four isolate Deployment's factory threshold with generous direct wallets.

The retained baseline evaluate `probability-1d94ce7b69cabda16c877081` remains the existing baseline evidence: `PROBABILITY_ANALYZED_PARTIAL`, 32 candidate/scenario rows, 27 excluded, 64 unresolved findings, five unresolved candidates, and zero definitely eligible candidates. Its analyzer source hash is `a453b5f25de050ec2823b7cdeebc6bf61ef9ccf23e1a0e2969f8c6231e257ee1`; source revision is `d3e4986669fd7d84b6695ffd1d2722bf8ee56a049ca98debda11888e6f20dae6`. Its raw 3,127,516-byte JSON is locally retained and verified as SHA-256 `ad38d083f27887375e642f132b0d347b71302addf332135a401529f951b4b0f5`.

In the following retained output table, `?` means unresolved eligibility and `F` means the tool classified the candidate ineligible. Zero is the evaluator's gate-adjusted raw value, not an authored zero weight. Every conditional probability is null.

| Frozen case | Theory | Prototype | Deployment | Weaponization |
|---|---:|---:|---:|---:|
| Peace/spare | 5 ? | 0 F | 0 F | 0 F |
| War/spare | 10 ? | 0 F | 0 F | 0 F |
| Exactly four CIC | 0 F | 0 F | 2.5 ? | 0 F |
| Below four CIC | 0 F | 0 F | 0 F | 0 F |
| Provider lost | 0 F | 0 F | 5 ? | 0 F |
| Deployment predecessor absent | 0 F | 10 ? | 0 F | 0 F |
| Family busy | 0 F | 0 F | 0 F | 0 F |
| Completed | 0 F | 0 F | 0 F | 0 F |

The raw artifact proves the primary decision bytes were frozen, but shared helpers remained current: it resolved `016_mengele_paleogenetics_stage_decision_triggers.txt` at hash `faf2918801bf4abb9a09a1ad616ef1c7030c10376b511c779d95723d3130002a`, differing from the captured before helper hash. That revision already contained `brilliant_scientist_mengele_paleogenetics_selection_is_valid`. Preserve this actual provenance: the table is a partial frozen-primary-source evaluation with contemporary helpers, not a historical whole-workspace eligibility proof.

The retained fixture's provider-lost case declares the registry flag false in `state` while its positive flag list still includes that flag. This conflict was not silently changed, because the mandatory comparison reuses the exact fixture. Its provider-loss intent therefore remains unresolved. Qualified DLC/native-project/equipment fields also did not bind the native `has_dlc`, `is_special_project_completed`, and compound `has_equipment` predicates.

The original sweep `probability-c9008f4a17997b613487faa1` used the same eight-case hash and four source paths for available project CIC, PP, support, and fuel with five steps and requested rank reversals. It returned 32 sweep points and the same partial 27 excluded/64 unresolved/five unresolved-candidate summary. Its 3,184,791-byte JSON is locally verified as `6f09224a4839db9354a97dfa5e42de0f4a58937eb32430c4648fccb0351c7c92`. Theory and Prototype cautious modifiers were not active in the supplied cases; their equality thresholds 1/2 are outside this matrix. Weaponization was never eligible in these supplied states, which does not prove campaign starvation.

## Final mandatory matching comparison

The completed final request is `016_private_paleogenetics_probability_baseline_2026-10-08.compare_final_native_tech_20261009.request.json`; its completed result is the matching `.receipt.json`. The call used adapter `mission_ai_will_do`, only the four existing stage IDs, the unchanged eight-case fixture, and logical gameplay path `common/decisions/016_mengele_paleogenetics_stage_decisions.txt` on both sides with distinct frozen `snapshotPath` values and raw `expectedSourceHash` values 4bf57705…before and 0ad338e3…after as listed above.

Final analysis ID: `probability-4420c19347c2d41540afe09f`. Result: `PROBABILITY_ANALYZED_PARTIAL`; 32 rows; `comparisonChanges=0`; zero definitely eligible; 29 excluded; three unresolved candidates; 69 unresolved findings; four diagnostics; six direct visual resources. Scenario hash exactly matches the frozen baseline: `698d26b94d12afdb4739a13e7c0645a58a09a6ec484d8d9be0d9e0e19b6c5a58`. Analyzer source hash: `f8bd9870506f50d010bbc514128b96565e5b84806e3478a450025f236e4935b2`. Source revision: `d0964439bf2ca33992b634c1c9fb0708737b3a584317631dc1de9ad048ce8037`.

The final tool reports no changed comparison rows. This is concrete bounded compare evidence plus exact source preservation of the weight blocks. It does not certify the intentional admission changes: shared helpers/constants are current on both sides, and the frozen fixture has no selected pair or fully bound native technology input. Deployment and Weaponization received `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostics in these eight states; Theory/Prototype received inactive-cautious-modifier diagnostics. Do not interpret these as tuning targets or compensate with higher AI weights.

Final raw JSON URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63b62558c773ddd8722fd2dec82701abc974181465ec3e21ddaea10ae1385e6a/19bab0a115ced48962700105c43f94243b5202095d0b04e7f7bbab3b83b2043f/probability-4420c19347c2d41540afe09f.json`. Returned size: 3,415,405 bytes; tool-declared SHA-256: `63b62558c773ddd8722fd2dec82701abc974181465ec3e21ddaea10ae1385e6a`. The local completed receipt preserves all JSON/SVG/PNG resource URIs and metadata.

The pre-native-tech comparison `probability-0ba834fb0c50de5565842951` is superseded only as final-source proof. It also reported zero changes, 29 excluded, three unresolved candidates, and 68 unresolved findings, source revision `822b21bcb08da9fb48ca939cd1e31fa73f120e62338622cab3de821ddc9cb97e`. Its raw JSON remains locally verified under `superseded_pre_native_tech_probability-0ba834fb0c50de5565842951.json`: 3,381,100 bytes, SHA-256 `5e7f11f06d8bd03a1e049ccec6b5d3322f6fa5877cb20e2e07d52246b5c081a4`. Its historical comparison SVG is 439 verified bytes, SHA-256 `2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49`. These files were preserved separately and are not relabeled as the final native-tech result.

## Separate after-only new-action assessment

The separate fixture is `016_private_paleogenetics_probability_baseline_2026-10-08.new_actions_20261009.scenarios.json`: 198,468 bytes, local SHA-256 `f8e6c36b36aeaab00b21ec35ed1db7bbb51b5fd786444910464b7badf09859e8`; MCP scenario hash `fc9bb4857667169554a70ec19a83c79e74cd21d19202aad1480a619e9194a512`. Its 16 IDs cover valid reserve selection; unowned, uncontrolled, zero-infrastructure and full target states; distinct and duplicate hatchery targets; reserve-only and hatchery-only clearing; a complete selected pair; genuine declared partial paid recovery; active timer; wrong actor; mismatched actual support; construction fault; and retained identity without pending authority.

Scope pointers are declared as named STATE/COUNTRY scope identities, not guessed integer country ordinals or state-pointer arithmetic. FROM, ROOT, RESERVE and HATCHERY scopes are explicit. Paid recovery seeds action1/family10/stage3, serial1, frozen pair/quantity fields, positive matching recorded/actual direct costs, delivered reserve proof, and actual aligned native receipt arrays with family index9. Current wallets and free CIC are depleted in the recovery phases. No eligibility override was supplied and undeclared state was not asserted closed.

After-only evaluate `probability-47f0d1d3ed81188d8f35f5cd` completed under `decision_ai_will_do`: `PROBABILITY_ANALYZED_PARTIAL`, 64 rows, 10 classified eligible, 25 excluded, 29 unresolved candidates, 54 unresolved findings, zero diagnostics, four direct visual resources. Analyzer source hash `6208f2bfef2e89d68e958d73b6c70988256602f1929e062d235fd80f12d5fda2`; source revision `5e3a8c0e09a9ec3828469749957502def9d860ffe636b7fe51d57219ff284a82`. Its request source pins raw new-file hash `cfd888f424460669e24c0b9e78afb65c2082169e7f480ef71a16b0d0594b9d65`.

Raw new-action JSON URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73fa4cff909b84541eabf44f648d9b44b214213d7f4d9c14a3d6da61417ad0a8/f04e8a0ea18242198da658a3a5898c52dc5f31af53625239722636de71704aee/probability-47f0d1d3ed81188d8f35f5cd.json`. Returned size 4,054,839 bytes and SHA-256 `73fa4cff909b84541eabf44f648d9b44b214213d7f4d9c14a3d6da61417ad0a8`. Individual final 16-case rows could not be locally extracted, so the aggregate eligible count is not assigned to named rows or promoted to engine acceptance.

The first new-action sweep returned `PROBABILITY_SWEEP_RANGE_REQUIRED` because selection states lacked recorded-payment/serial numeric paths. The bounded retry uses only the six recovery states; this is an auxiliary fixture, not a replacement for either the eight matching cases or the 16 after-only cases. Its local SHA-256 is `5aac8015d8dc67ee45c849f437a44417b5b3fbc6da51431dc8eec3e3edcfb3a3`, and MCP scenario hash is `b2a7f966804308abd4d3bc1d8d905b371f46160a7f35f5dcd713d69697786027`.

Recovery sweep `probability-604f18ff1c952b7d66dbdb68` completed: 24 candidate rows, 12 sweep points over actual support and serial, nine excluded, 15 unresolved candidates, 34 unresolved findings, zero definitely eligible, zero diagnostics. Its 1,379,448-byte raw JSON is locally verified as `ea0693f2110bbeac967d856859eadd1d2d542e903f961ac2238f0a9dca4c5440`. The source hash/revision equal the after-only evaluate source above.

| Auxiliary recovery state | Returned recovery raw value | Eligibility |
|---|---:|---|
| Authenticated declared partial receipt | 5 | unresolved |
| Active paid timer | 0 | false |
| Wrong stored actor | 5 | unresolved |
| Mismatched measured support | 0 | false |
| Construction fault | 0 | false |
| Identity fields without pending flag | 0 | false |

The wrong-actor score is not evidence that the source permits the wrong payer: actor identity, temporary-variable and variable-scope predicates remain unresolved. The two selection candidates also retained positive unresolved values in pending recovery cases, despite source `choice_is_open` visibility forbidding selection while pending. The probability result therefore does not establish native phase reachability. The clear action retains authored base0; no automatic AI reset or positive clearing weight is claimed. Rank numbers in this incomplete target/state model do not establish native target-choice probabilities.

Exact remaining auxiliary unresolved constructs include scoped trigger `88`, `check_variable` token/pointer operands, `set_temp_variable`, `modulo_temp_variable`, dynamic scopes `var:mengele_event016_paleogenetics_paid_reserve` and `var:mengele_event016_paleogenetics_paid_hatchery`, and compound `free_building_slots`. No factor, pointer or gate was forced true to resolve them.

## Structural evidence and artifact delivery

A narrow `hoi4.decision_inspect` request named only `mengele_event016_paleogenetics_select_reserve` and three valid/unowned/uncontrolled target states. The first attempt was rejected before analysis for fixture-only `label` and `prevalence`; the corrected request completed as `DECISION_ANALYZED_PARTIAL`, three scenarios, source revision `331e2230de71882b14cfd44e242c4681fe5c2a82779fd715dfffebc9b16ae8fa`. The service's internal inventory counts are not an audit claim over its other decisions. Its declared 894,177-byte artifact hash is `3cf76ea41b8e19918a9ce0c84936da9a8fec688f88f8e26717862fe7d4584027`; retrieval failed partway, so no complete local artifact is claimed. The completed request was awaited through exact exec handle11; native-app interruption was never treated as proof of failure.

Current live schemas for probability inspect/evaluate/sweep/compare/render and decision inspect were read. The server-status resource reported HOI4 Agent Tools `3.10.0`, stdio, at `2026-10-09T08:24:35.496Z`. No native MCP task/job or helper-expansion route was used. The artifact template confirms exact SHA/provenance-addressed resources with byte ranges and continuation metadata. Byte-range reads were restricted to 32,768-byte chunks after detecting truncation of larger returned blobs.

Artifact delivery is recorded in `016_private_paleogenetics_probability_baseline_2026-10-08.artifact_delivery_20261009.json`. Final-compare and new-action JSON/SVG reads returned exact MCP error `-32603: Artifact provenance manifest is unavailable`; one narrower metadata=manifest retry for each JSON returned the same error. Their completed receipts, URIs, tool-declared hashes/sizes, and requests remain deliverable. No local raw bytes or verified local hash is claimed for those unavailable resources.

Explicit render attempts for the final compare, 16-case new-action evaluate, and narrowed recovery sweep returned `PROBABILITY_ANALYSIS_NOT_CACHED` with no fresh render resources. These cache/delivery limits do not undo completed compare/evaluate/sweep calls. The direct analyses had already generated visual-resource links. No unchanged render was queried repeatedly.

The narrowed recovery sensitivity and unresolved SVGs were downloaded and byte-verified: sensitivity 1,756 bytes, SHA-256 `db89f6ef00d0ff4bd4204bad21996ccdf760cd408e8a848b5d1a9ac5753c4034`; unresolved 10,436 bytes, SHA-256 `d293d8e3f23b323fa3647c3756dd4f174ddca1ee11ad2cf0f38114a915809475`. They remain alongside the locally verified baseline JSONs and superseded compare artifact. Parent-owned event-impact timeout/narrow-retry and live event-render status are separate structural delivery context and are not interpreted as probability-route failures.

## Parent source tests, limits, and recommendation

Read source evidence: `docs/testing/event016_private_paleogenetics_20261008/parent_core_result.json` records 51 cases; its file SHA-256 is `4c140a08aa3ccf70e1ffc590fe7568422b8e529b95afe1f99d4e4ccc9f7ed84a`. Its recorded source hashes match the final current files, including the stage-trigger hash5863eb3d…. `parent_frontend_result.json` records 29 frontend/CXT cases and 51 core cases, file SHA-256 `59e42507b4c3ecef7bc330db7cc80765a0f98effff2389cf9e9b4bbab5f456d4`; its recorded source hashes also match current files. This is the parent's retained 80-case source-test evidence, not a rerun or native observation by this auditor. The earlier `core_results.json` has the pre-native-tech stage-trigger hash and remains historical.

Those tests exercise direct-resource boundaries, native CIC3/4/5 source admission, literal callback entry, pair output, partial selection reset, entitlement admission/cancellation, recovery, faults, and read-only CXT observations. Their declared limits include opaque modeled pointers, aggregate wallets, modeled slots/deltas, two external provider-helper fixtures, and no native clock/reservation/callback, delayed recount, concrete equipment-provenance, or unique-building-identity proof.

No AI weight change or balance target is recommended. The identical weighted expressions and completed matching compare satisfy the bounded weighted-source comparison requirement; the result does not prove the new native admission/recovery states are fully modeled. Dominance, starvation, cross-family rank reversal, repetition frequency, and campaign snowball remain unresolved outside the requested pools and declared states. Simulation and sequence analysis were not applicable because no uncertain distribution or complete cadence/state-transition pool was declared.

The concrete remaining analysis improvement is an interpreter-supported typed-state/receipt/slot fixture that binds the current pair and native technology gates; if the parent expands it, both before and after must be re-evaluated under that same revised fixture while retaining this eight-case proof. Correct the provider-lost flag/state conflict only in such a new version, not by changing the preserved matching fixture. Do not retune AI scores to compensate for unresolved native input binding.

## Reading and reference evidence

Applied repository guidance: `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and the relevant Event016 source/docs; no skills were modified. Read the current accepted `016_private_paleogenetics_deployment_acceptance_2026-10-08.md`, existing Paleogenetics stage handoff/system documentation, and `common/scripted_effects/016_mengele_paleogenetics_deployment_effects.md`. The similarly named private Transit acceptance is Teleportation and was not used to set Paleogenetics prices or scope.

Live reference context/search/read covered offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:357-374`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; `AI modding - Hearts of Iron 4 Wiki.md:26-37`, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`; and `Data structures - Hearts of Iron 4 Wiki.md:1551`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`. No Paradox wiki web access was used.

Installed-game references read through MCP: `common/decisions/_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`; `documentation/triggers_documentation.md:6757-6765`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; `dynamic_variables_documentation.md:608-611`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`; and `modifiers_documentation.md:2202-2206`, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`.

Focused source lookup located Deployment at `common/decisions/016_mengele_paleogenetics_stage_decisions.txt:117-156`, workspace-index revision `eda74ea79a795477a56f05ec434909fc40fab8948939850f2745a8c58b4b0364`, and its visibility/provider triggers at source-location revision `3e838d36c2b45f8bf1aab646e02c160f36079c159004adfeb18a5f1b8ed6811f`. Historical lookup revisions are retained as delivery context; frozen raw snapshots are authoritative for before/after identity.

No gameplay simplification was made by this audit. The report is ready for the parent's paired-tranche review/commit with every partial input and retrieval limit above carried forward.
