# Event 016 Mengele Computation Stage and Incident Probability Handoff

Date: 2026-09-02

Status: prepatch absence boundary retained and postpatch inspect/evaluate evidence captured; source comparison remains unavailable because the new stage-decision and private incident/recovery surfaces had no before bytes.

## Scope

This bounded read-only audit covers the planned Mengele Computation stage decisions and private incident/recovery decisions/effects, plus the existing native Computation project and provider-helper context needed for a later same-scenario comparison.

The existing native baseline remains separate and is not overwritten: [E016_MENGELE_COMPUTATION_BASELINE_2026_09_02.scenarios.json](E016_MENGELE_COMPUTATION_BASELINE_2026_09_02.scenarios.json) has SHA256 `3c197628aa74eb4dba902f771ec0eba18e2dcf66cf0b1f886858a5632d5bb99e`.

In-scope source paths are `common/decisions/016_mengele_computation_stage_decisions.txt`, `common/decisions/016_mengele_computation_incident_decisions.txt`, `common/scripted_effects/016_mengele_computation_incident_effects.txt`, `common/special_projects/projects/016_brilliant_scientist_projects.txt`, `common/scripted_triggers/016_mengele_project_bridge_triggers.txt`, `common/scripted_effects/016_mengele_project_bridge_effects.txt`, and the current provider selector in `common/scripted_effects/016_brilliant_scientist_project_effects.txt`.

## Immutable before boundary

Retained commit: `5f31c83ce66f1c00fbf21f7a120f7ba2d1f25d55`.

At capture, all three planned new files were absent from both the worktree and that commit. Their exact before state is therefore absence, with no source bytes or source hashes available:

| Surface | HEAD `5f31c83` | Worktree at capture | Before bytes |
| --- | --- | --- | --- |
| `common/decisions/016_mengele_computation_stage_decisions.txt` | absent | absent | none |
| `common/decisions/016_mengele_computation_incident_decisions.txt` | absent | absent | none |
| `common/scripted_effects/016_mengele_computation_incident_effects.txt` | absent | absent | none |

The existing stage helper files are not new in this boundary. At capture, `common/scripted_triggers/016_mengele_project_stage_triggers.txt` had raw SHA256 `dbff215edc95e072d58b19eb04e3f752900674ff38e9f6f784619938e53555cc` and Git blob `84edecc0dd678c56b94b6a899da396f0eb66a070`; `common/scripted_effects/016_mengele_project_stage_effects.txt` had raw SHA256 `712781c74d12c7bc3dd848c6dc7055143edf12a4610cfc6191e321ce8a8bf566` and Git blob `a841ff5a92aee3c9bf0de865356aa30e6aa7274b`. These are context snapshots, not replacements for the absent new-file before bytes.

The existing context files were concurrently modified at capture. Their observed raw SHA256/Git blob pairs were: `common/special_projects/projects/016_brilliant_scientist_projects.txt` `aa71a84ef96abbc22261a0a51ef81b1f7aff80e0f2099d2de867061521dfb1ab` / `c083314cf56f15c1015bcd959123a77d5238e053`; `common/scripted_triggers/016_mengele_project_bridge_triggers.txt` `7695cbfbe6f7f52d6c94df441dc0b4cb91fa39f59ee4af367898dad4bb8eed41` / `06746dff4ffd0c79a98c09b1b1630f5f34b09040`; `common/scripted_effects/016_mengele_project_bridge_effects.txt` `e75b87304ef185112fc74801424d4417d34f3057d78f20467ebd758ec3910302` / `f9bb47c05eae7d265d8d18a3204a1cd582b520ac`; and `common/scripted_effects/016_brilliant_scientist_project_effects.txt` `f931b452c7f27b6793936ae181e08c291f053672415a0e232e4a168ecf1b1760` / `25b5ed45435c92128f512f39df4a04b7cd34bfdd`. These pairs are included only to identify the helper/native context seen by the baseline and must not be treated as a clean prepatch snapshot for future comparison.

## Required MCP baseline inspection

The probability service was called before any evaluation or comparison with workspace `mod_chaos_redux_ea3b2d67c2c0` and `refresh: true`.

| Call | Result | Artifact/revision |
| --- | --- | --- |
| `probability_inspect(adapter: decision_ai_will_do, source: {path: common/decisions/016_mengele_computation_stage_decisions.txt})` | `PROBABILITY_SOURCE_NOT_FOUND`; `artifactCount=0`, `filesScanned=[]`, `proposedFiles=[]` | none |
| `probability_inspect(adapter: decision_ai_will_do, source: {path: common/decisions/016_mengele_computation_incident_decisions.txt})` | `INTERNAL_ERROR`; `artifactCount=0`, `filesScanned=[]`, `proposedFiles=[]`, blocker message `Unexpected internal error` | none |
| `probability_inspect(adapter: custom_weighted_pool, source: {path: common/scripted_effects/016_mengele_computation_incident_effects.txt})` | `PROBABILITY_SOURCE_NOT_FOUND`; `artifactCount=0`, `filesScanned=[]`, `proposedFiles=[]` | none |

The missing-source results are exact absence evidence for this prepatch boundary. The incident-decision `INTERNAL_ERROR` produced no source, candidate, scenario, or analysis artifact and is not evidence that the file exists or has a weighted surface. The one bounded inspection was not retried.

No `probability_evaluate` was run because there was no source-backed candidate pool, and the owner explicitly requested no comparison until the new implementation is frozen. No `probability_render`, sweep, simulation, or sequence analysis is available or claimed.

## Separate exact fixture

The durable fixture is [E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json](E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json) with SHA256 `9a6548a02519ec1d92a53cc246996a2b552604e04e74d7c115ec999bb33f532b` and 14 named scenarios.

The scenarios are `E016_MENGELE_STAGE_THEORY_PEACE_NATIVE_EXACT`, `E016_MENGELE_STAGE_THEORY_PEACE_NATIVE_ONE_SHORT`, `E016_MENGELE_STAGE_PROTOTYPE_WAR_NATIVE_EXACT`, `E016_MENGELE_STAGE_PROTOTYPE_WAR_NATIVE_ONE_SHORT`, `E016_MENGELE_STAGE_DEPLOYMENT_PEACE_NODLC_EXACT`, `E016_MENGELE_STAGE_DEPLOYMENT_WAR_NODLC_ONE_SHORT`, `E016_MENGELE_STAGE_WEAPONIZATION_PEACE_NATIVE_EXACT`, `E016_MENGELE_STAGE_WEAPONIZATION_WAR_NATIVE_ONE_SHORT`, `E016_MENGELE_INCIDENT_ACTIVE_THEORY_NATIVE`, `E016_MENGELE_INCIDENT_ACTIVE_WEAPONIZATION_NODLC`, `E016_MENGELE_INVALID_PROVIDER_PROTOTYPE_NATIVE`, `E016_MENGELE_INVALID_PROVIDER_DEPLOYMENT_NODLC`, `E016_MENGELE_STAGE_PROTOTYPE_PEACE_NODLC_EXACT`, and `E016_MENGELE_STAGE_WEAPONIZATION_PEACE_NODLC_ONE_SHORT`.

Coverage is explicit for all four stages, peace and war, native and no-DLC presentations, exact-payment and one-support-equipment-short cases, an already-active incident no-roll case, and invalid-provider no-roll cases. The fixture also declares predecessor completion receipts for each stage. The stage labels, capacities, accident factors, payment cases, and incident expectations are fixture inputs for later source evaluation; they are not engine-state proof.

## Parent-approved incident expectation

The following values are the approved intrinsic design expectation from stage capacity multiplied by the stage accident factor. They are not MCP-derived probabilities, because the incident effect/decision source was absent during the baseline.

| Stage | Capacity input | Accident factor | Expected incident roll | Complement/no-roll |
| --- | ---: | ---: | ---: | ---: |
| Theory | 10 | 0.5 | 5% | 95% |
| Prototype | 10 | 1.0 | 10% | 90% |
| Deployment | 15 | 1.25 | 18.75% | 81.25% |
| Weaponization | 15 | 1.6 | 24% | 76% |

The approved design has no Kruger Exposure modifier. `private_incident_active=true` must suppress another roll, and an invalid provider must have no roll regardless of stage or payment state. Those are contract assertions to verify after source freeze, not verified engine behavior in this baseline.

## Existing native and helper context

The existing native project identifier is `sp_brilliant_scientist_computational_engine`. Its current source block uses base AI `constant:brilliant_scientist_project_ai.base`, a wartime preferred factor, and a cautious factor when `FROM` is the current host with low project capacity. Its unique prototype reward is `sp_brilliant_scientist_computational_engine_reward_unreadable_notation`, with the existing reward weight and cautious/risky options. Any later cautious-factor restriction to Kruger must be compared separately against the original native fixture; this new stage/incident fixture must not replace it.

The existing stage helper context exposes `brilliant_scientist_mengele_project_stage_provider_is_valid`, `brilliant_scientist_mengele_computation_stage_request_is_valid`, `brilliant_scientist_mengele_computation_stage_predecessor_is_valid`, `brilliant_scientist_mengele_computation_stage_can_pay`, and receipt helpers. The helper reads provider identity, the Mengele registry/program lifecycle, current-host and terminal flags, the global terminal/world-end flags, the active incident guard, stage selectors, predecessor receipts, and stage-specific payment inputs. These hidden inputs are represented only where the fixture explicitly declares them; unresolved helper expansion remains a later MCP limitation to report rather than infer.

The bridge helper `brilliant_scientist_can_research_mengele_computation_prototype` currently routes through the stage-provider helper and Theory receipt, and excludes completed prototype/native computation. The bridge/native files were concurrently modified when the absent-source baseline was captured, so this context is not a postpatch result.

## Result classification and remaining work

The absent-file facts are exact source-boundary evidence. The fixture and the four-stage table are bounded contract/design evidence. No weighted score, option race, normalized probability, incident cadence, or engine eligibility result is established.

The candidate pool is unresolved because the new decision IDs and private incident/recovery decision structure did not exist at the retained before boundary. Native special-project research selection and unique prototype-option behavior remain governed by the separate prior native handoff and are not silently reclassified as decision probabilities.

After the owner freezes the new files, run one mandatory `probability_inspect` against the actual stage and incident decision sources, then a bounded `probability_evaluate` over this exact fixture. If the adapter exposes a complete pool, compare the four stage scores and any private incident pool without flattening them into a single chance. If the adapter remains unavailable or helper expansion is incomplete, preserve the exact blocker and classify the result unresolved. A later `probability_compare` must use source objects and this unchanged scenario body; do not use analysis IDs or replace the original native fixture.

No gameplay files, weights, localisation, assets, or source configurations were edited. Only this handoff and its separate fixture were added.

## Postpatch source capture and probability evidence

The authored postpatch surfaces are present as untracked source files in the current worktree. Their current raw SHA-256/Git blob pairs are `common/decisions/016_mengele_computation_stage_decisions.txt` `f6f4898c8fbb2c63715c050018466435c0700effcf0422dd5aed67ea21cbad1f` / `f1b1ed37598eb54733acdea273a1bbb316f70d7a`, `common/decisions/016_mengele_computation_incident_decisions.txt` `2393f9f2e7816021f9fbc62bb0000cde985c916e26f9230d7cc867269e96a5b1` / `3347dd3ba73a0faa92a48fe78d15a16e7805641a`, `common/scripted_effects/016_mengele_computation_incident_effects.txt` `d233630f74ad19125dc7a70157c2b6ed419923f5c467f6befbbe272a0afef81a` / `4721f6486456f04a01bc72fb4cdc85c79d2429e3`, and `common/scripted_triggers/016_mengele_computation_incident_triggers.txt` `be9365a5b0c1f71670e5450c19a470adabceb84f5fca8d85de9b376dd92c3c12` / `c0b9c9d4872bd45f0153ee13644f099d787723e5`. The repository HEAD at capture was `b06059aeda0a127dfa96d0bda0ca62e11012eaf6`; the retained before boundary remains commit `5f31c83ce66f1c00fbf21f7a120f7ba2d1f25d55`.

The before state is exact absence, not an empty scenario or synthetic source. All three planned new surfaces (`016_mengele_computation_stage_decisions.txt`, `016_mengele_computation_incident_decisions.txt`, and `016_mengele_computation_incident_effects.txt`) were absent from the retained before commit and had no before bytes. Therefore no valid source-object `probability_compare` can be constructed for these new files, and no before/after score or eligibility delta is claimed. The existing native Computation project remains governed by its separate baseline and is not silently folded into this absent-source comparison.

The durable fixture remains [E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json](E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json), unchanged at SHA-256 `9a6548a02519ec1d92a53cc246996a2b552604e04e74d7c115ec999bb33f532b`. The stage and recovery evaluations used the exact 14-scenario body and scenario hash `6f170f301309d4445836ab432a6077c53aa747b9f12e7855d61b2d349d0139bc`, including valid and invalid providers, all four stages, exact and one-short payment cases, active-incident no-roll cases, peace/war, and native/no-DLC presentation flags.

### Stage decision inspect and evaluation

The mandatory postpatch `probability_inspect` on `common/decisions/016_mengele_computation_stage_decisions.txt` requested `decision_ai_will_do` for the four stage IDs and returned `PROBABILITY_SOURCE_DISCOVERED` with `requested_adapter_empty`. The suggested `mission_ai_will_do` adapter exposed exactly four candidates and matched all four requested IDs; no inspect-time unresolved inputs were reported. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb047887b310eb30bdfe9ae7db45d0ef988e5a48eb4cc98bf63d946858419e37/ca60487e8e34f74200840905934f93179cb284b9ddeb5dd70020cf7418f93f36/probability-inspect-d1005a4f1fe4.json`. Inspect source revision was `b6381aa8d67439418f88cb4a4fba53a3921b3f8963b4a3c6d503e3ffb9710ddf` and normalized source hash was `d1005a4f1fe4f79ec7e76ad39fc53e4d42287b825ea6345e8a0e267e34c5a620`.

The bounded `mission_ai_will_do` evaluation used the same four-candidate pool, exact fixture, `raw_value` and `conditional_probability`, and `refresh=true`. It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-7f04747310acf8b5d2359d4e`, source revision `b6381aa8d67439418f88cb4a4fba53a3921b3f8963b4a3c6d503e3ffb9710ddf`, normalized source hash `d1005a4f1fe4f79ec7e76ad39fc53e4d42287b825ea6345e8a0e267e34c5a620`, 14 scenarios, 56 candidate rows, four aggregate unresolved definitions, and zero diagnostics. The authoritative JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08e19edb02e9667e2115a688cf9a1a787d30e11d19abe1a1af63c550d011c61e/6b5aba4c2914831ece71ab2168d58c50704e5d8d1bd1a0f8c5b4a94ba5144d7b/probability-7f04747310acf8b5d2359d4e.json`. The ranking, matrix, and unresolved renders are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76e16b063f2d559b3dd9bbf218aff88ef9ae9f264decea8d9764dc06d4fe12c3/0181725a255547ca3132d4ab0acf542c4de41fbf11d24b9adeffeb32e515354c/probability-probability-7f04747310acf8b5d2359d4e-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa08e485f8ba387d6bde34092bb091ffb68f5a743977959ef6ec2e02b388c3aa/698adc1af5310aec609afcb5fac4d63aaa717003c3a0a977280d684101fae272/probability-probability-7f04747310acf8b5d2359d4e-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff533157f6ca6cd0e2a50a792511e83f12bf960c67ae80b54a53445a7bdb9e9f/500d96846496f4c6fa9bc0d6250176fb2731199c8fef1bd2736f1ee0b2faa41b/probability-probability-7f04747310acf8b5d2359d4e-unresolved.svg`.

Every stage row was `score_only` with `normalizedProbability=false`; the requested conditional-probability metric was not a categorical selection result. The four candidates tied at raw 10 in every peace row and raw 20 in every war row, including one-short, invalid-provider, and active-incident fixture rows. The trace shows the unchanged base 10 and wartime factor 2. Candidate rank order was a deterministic tie order, not a stage preference. All four stage candidates remained eligibility `unresolved` with two unresolved `custom_trigger_tooltip` items per row, so the adapter did not prove current-stage visibility, provider validity, predecessor receipts, payment sufficiency, active-incident suppression, or terminal-state behavior. Positive scores in invalid or non-current-stage rows must not be read as positive in-game availability.

### Incident recovery decision inspect and evaluation

The mandatory postpatch `probability_inspect` on `common/decisions/016_mengele_computation_incident_decisions.txt` requested `decision_ai_will_do` for `mengele_event016_computation_incident_recovery` and returned `PROBABILITY_SOURCE_DISCOVERED` with `requested_adapter_empty`. The suggested `mission_ai_will_do` adapter exposed and matched the one recovery candidate with no inspect-time unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26f11dae063923db482a8303026edd609374ad423f27f453eca1c6ac61674df3/3e290857688463f09f32a970683b32beffd7cdc66483411ae2f08a551840c4c8/probability-inspect-b6f6000ad195.json`. Inspect source revision was `f98d739043423ab3dbad016529deeec1cca30da19293286bde3076ea32174138` and normalized source hash was `b6f6000ad19562ba6dddb234e5b061d647fca546ac914e4086b58f3120b14f52`.

The bounded `mission_ai_will_do` evaluation used the same recovery candidate, exact fixture, and metrics. It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-f68e2fe0fd1f211bf077ef62`, source revision `f98d739043423ab3dbad016529deeec1cca30da19293286bde3076ea32174138`, normalized source hash `b6f6000ad19562ba6dddb234e5b061d647fca546ac914e4086b58f3120b14f52`, 14 scenarios, 14 candidate rows, one aggregate unresolved definition, and zero diagnostics. The authoritative JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b37a29a9b7935be656fc5898153e262371c58d5a3137437ac43fb506df994d49/da1ddb1b812f403ed24da25570a96b03b926667be4a3265a3a2de7b01a3d9331/probability-f68e2fe0fd1f211bf077ef62.json`. The ranking, matrix, and unresolved renders are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66e3f9b4bc6fe7dffa6734bc9b5863c6284f51bdf4a30b1be3e61af05d43b9d3/51916c3f9f7033bf982e4c374fc42913516bc54617bc53011582c1fc56d67f37/probability-probability-f68e2fe0fd1f211bf077ef62-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48b202af3e79e695dae619b82ab90bed21617ff3a2c5b10fc3fec59c461d9c34/0eb9cee8eb5760763d37aa86b85c4a9484d5d8cf5f1ae5d8081c10314fb584b9/probability-probability-f68e2fe0fd1f211bf077ef62-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48692d5a1b9a3220206984e7bbbf14433e03c0b1d1ddd32b4b69fc3348b1a74d/7e8a3d3629afd01a29050304237b5ded98d725d749cb26bc2349c495c4e6e57f/probability-probability-f68e2fe0fd1f211bf077ef62-unresolved.svg`.

The recovery decision scored raw 25 in all 14 scenarios, with `score_only` support and `normalizedProbability=false`; this is its unchanged urgent-AI base and not the incident occurrence chance. Every row remained eligibility `unresolved` with two unresolved `custom_trigger_tooltip` items, so active-incident, provider, recovery receipt, payment, and terminal cancellation behavior remain unproved. No recovery-selection probability is claimed.

### Private incident random-list surface

The required postpatch `probability_inspect` on `common/scripted_effects/016_mengele_computation_incident_effects.txt` used `custom_weighted_pool` and returned `PROBABILITY_SOURCE_INSPECTED`, but `poolComplete=false`, zero candidates, zero available adapters, and two `CANDIDATE_NOT_FOUND` unresolved items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96eac4ad9ee354117780b13e871621c86a0070de21c39fa09196c0ba2375e40e/fe522cea887970ab0974cec5544244684d313ca276de4773043975c62881afc2/probability-inspect-5180295e91d1.json`. Its source revision was `915375f63b384ae735234b4a889caa2eb5546bb6519b831c686acd2273c7998c` and normalized source hash was `5180295e91d11c35f89c3fe4ae6b537079d63b1329c07d9f6f85dc36278e24af`.

The source contains a dynamic `random_list` with the stage pressure and explicit complement branch, but the installed custom-pool adapter recognizes only manifest-defined pools and did not expose this random list as a candidate pool. No `probability_evaluate`, normalized incident chance, cadence, or sequence result is available for this surface. The approved design table remains a contract expectation only: Theory 5%, Prototype 10%, Deployment 18.75%, and Weaponization 24%, with complements and one-active-incident suppression; those values are not MCP-derived in this postpatch pass.

## Postpatch classification and blockers

The inspect and evaluate artifacts prove that the four stage decision IDs and one recovery decision ID are discoverable through the installed mission-score adapter, and that their unchanged score formulas produce ties at 10/20 and recovery 25 under the declared scenarios. They do not prove normal decision eligibility, stage-specific candidate removal, payment boundaries, provider identity, private incident suppression, or callback/receipt semantics. The random-list inspect proves source discovery but not a complete custom weighted pool.

No source-backed before/after comparison is claimed because the retained before side is absence, not a source object. The four-stage and recovery score outputs are current postpatch score-only evidence, not normalized probabilities. No gameplay source, AI weight, cost, timer, or balance value was changed by this audit; only this handoff and its pre-existing fixture were touched.
