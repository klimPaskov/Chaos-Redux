# CBRN occupation probability post-retirement audit

Status: Read-only audit complete for current-source candidate removal and retained-weight spot checks; historical probability comparison remains unresolved because the connected compare route cannot consume the saved baseline artifact as a source snapshot.

The audit covers the Sarin and Soman occupation attack decisions removed from `common\decisions\cbrn_occupation_decisions.txt`, their AI weight blocks, and retained coercive-law compatibility, protected occupation law, and protective aid weights.

The only file written by this audit is this handoff.

## Sources and source identity

The current decision file has local SHA-256 `E27AE3DD51EF07618943DB9BF2A8B4BD06C63F9CD3A7E4504DAAAE2F3B994115` at current Git HEAD `4fa083c4e6f5572a19b88b3f06c4d83562a07e18`.

The baseline fixture records local source SHA-256 `1BAFEF19B302C711F4628F0FA5C96F73F6B68426DEBA15C32B672DBABAB8FE4C`, Git HEAD `ac9195c785f7ae4d21a1e6edb7b85eda1e9ba4ea`, MCP source revision `497f931aefdfae640eb56799cf7985b198e034a6883299627802d95b568844f3`, and MCP source hash `5786d0c9f0836750d8b5662129942a612dbef0c18cbed2010d0f1284e0c45080`.

Current MCP inspections read `mod:common/decisions/cbrn_occupation_decisions.txt` and report source hash `d6e746de81b168ed24aa0857fbb5085bbbf54fb4450ef46648e49b67a9f1a4f9`. The route returned different sourceRevision values across calls while preserving that same sourceHash; each returned revision is recorded below without asserting they identify the same revision.

The current source diff removes the two nerve-suppression decision blocks and updates the file overview. The retained decision AI blocks are unchanged in the reviewed diff. The current shared constants in `common\script_constants\cbrn_occupation_constants.txt` still define coercive authorization base 25, protected administration base 80, protective aid base 40, and protective-aid factors 5 for own core, 2 for allied core, and 2 for trauma.

Current source review confirms `cbrn_authorize_coercive_security` remains hidden with `visible = { always = no }` while retaining base AI weight 25 and a zero factor when its route requirement fails. The protected-law decision retains base 80 and a defensive-profile factor of 3. Protective aid retains base 40 and the own-core, allied-core, and trauma factors listed above.

The deleted decisions had separate Sarin and Soman AI blocks and used the 21-day operation preparation duration identified by the parent. Current `common` sources contain no reference to the removed decision IDs or the decision-specific `cbrn_occupation_ai_can_prepare_nerve_suppression` helper. Generic Sarin/Soman stock predicates remain in `common\scripted_triggers\cbrn_occupation_triggers.txt`; this audit did not treat those retained subsystem predicates as decision AI candidates.

## Baseline and scenarios

The baseline scenario set is `CBRN_OCCUPATION_DEAD_PATH_BASELINE_20260925`, scenario `cxt_unbound_current_hook_closed`, actor `CXT`, with empty actor state and flags and an empty `occupied_target_state` placeholder as FROM.

The fixture baseline candidate pool is `cbrn_nerve_suppression_sarin` and `cbrn_nerve_suppression_soman`, complete for the two pre-edit candidates in that source. Its result is `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-1abf5e1a9760548f0f6dafaa`, scenario hash `dfe95b973183387fea01db3c7a848ca783a4a35183b13a9118e2d026b9d6fe20`, candidate-pool hash `2bd4e4bf2e8b3001e32e2c5919d6a075c56adbd248e7a44e2e0aeb745970150b`, 2 candidates, 96 unresolved items, and 0 diagnostics.

The baseline artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ade97d81d643ed5d353fd51af5ccd023c757f6da81472de42a25efba8cd3ddef/25d62dd6cdb350b0f3c4471d0fa83658de156b9958091628e8798754c580ae60/probability-1abf5e1a9760548f0f6dafaa.json`. The fixture says a direct resource read during its capture failed with “Artifact provenance manifest is unavailable.”

External inputs were incomplete in the baseline and remain unbound in the reused scenario. The fixture specifies no CXT flags, country variables, technology, equipment stock, command power, wartime relations, policies, or readiness values, and no owner, state variables, compliance, resistance, occupation, or target conditions for FROM. The baseline's exact unresolved input categories were FROM, check_variable, command_power, custom_trigger_tooltip, has_equipment, has_tech, has_variable, has_war, has_war_with, and original_tag.

The baseline note states that the current-version operation-condition hook is closed by `cbrn_occupation_current_version_condition_hook_verified = { always = no }`. This explains why the pre-edit actions were dormant in the supplied scenario, but the partial baseline does not prove a campaign-wide selection probability.

The current evaluator rejects the fixture's original top-level `FROM` property with `Unrecognized key: "FROM" at scenarioSet.scenarios[0]`. I then used the currently documented adapter shape `scopes.FROM = { id = "occupied_target_state", state = {} }`, preserving the same scenario and target values. The resulting scenario hash exactly matches the baseline hash above.

## Current MCP evidence

The first post-edit call was `hoi4.probability_inspect` for `mission_ai_will_do`, source `common/decisions/cbrn_occupation_decisions.txt`, and the same Sarin/Soman pool. It returned `PROBABILITY_SOURCE_DISCOVERED`, requested and suggested adapter `mission_ai_will_do`, discovery reason `candidate_pool_not_found`, 0 matches for the retired pool, and 7 other candidates across the discovered adapters: 6 under `decision_ai_will_do` and 1 under `mission_ai_will_do`. The only mission-adapter example was `cbrn_deploy_protective_aid`. Its sourceRevision was `92ad9be59470fab4fb4dceb07291bcda508698be477bc79862330ede947f3fac`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9beab53a323d1db59b6b4f976576ab6bef2c6a7ddb3375215da8f0267963709f/3b6b7477a90c6561ebd3ddaf9dad5aae261ba4cc52ba2231b194eb4aa34b3da7/probability-inspect-d6e746de81b1.json`.

The schema-correct post-edit evaluation of the retired pair returned `PROBABILITY_SURFACE_EMPTY` with “No weighted blocks matched this request.” The blocker listed 0 candidate-pool matches for both retired IDs and showed the remaining adapter split as six decision entries and one aid mission entry. No post-edit numeric weight or probability was returned, and the empty surface must not be described as zero selection probability.

A current `decision_ai_will_do` inspection for `cbrn_authorize_coercive_security` and `cbrn_adopt_protected_occupation` returned `PROBABILITY_SOURCE_INSPECTED`, 2 candidates, `poolComplete = true` for that requested pair, 12 required inputs, and 0 unresolved inputs at discovery time. Its sourceRevision was `7bec7f8573b6c1c7421b026ba8b181d211304334175fec1ba8675621e162ef22`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2c7543761e485a8a744840a8c48a155a2e584bbba6fb6f1675f5cc402e6a3e9/5ef58642eda76908d74f3883255a59faf3373aba738616e1609d94b6a5f3a8ee/probability-inspect-d6e746de81b1.json`.

The current decision evaluation used the complete six-entry decision pool found in this file: `cbrn_admit_accidental_release`, `cbrn_adopt_protected_occupation`, `cbrn_authorize_coercive_security`, `cbrn_destroy_contaminated_records`, `cbrn_permit_inspection`, and `cbrn_seal_state`. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-bd7a90d99a43562d87076844`, adapter `decision_ai_will_do`, 6 candidates, 59 unresolved items, 0 diagnostics, sourceRevision `395d94b946f9d136b6d4942282281eab171921a23b3108fcf3775b21341db05d`, and the same source and scenario hashes stated above. The analyzer validation marked uncertainty visibility passed and reported all 59 unresolved or bounded items explicitly.

The decision analysis JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c23cead78ee6ed17c60aa8f7b2dd8bb46de64e119f125ac8f46d0d05959d312/8bb36e1f8bdc8896bd63ff0267e92891f2fa64b93e3256a75a76dba67d4da9ea/probability-bd7a90d99a43562d87076844.json`. Rendered ranking, waterfall, and unresolved evidence is available at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbc459026c7afdb5d976fa35527e0c69c2fb5b4920bdf222e017efe1bf9ad388/1b5c3dce6dd007f67f417d0adf7835f4b73f87fd147e9fc0a009b0b209b0d25d/probability-probability-bd7a90d99a43562d87076844-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c60d2ec81a5b66531f077e4715390a6a1948486f0e1d8508fc629bd8e84de99c/e53796b0cb0f7a5c55d4537e644c1cbb89baf80e4768f14d694791720a3a04bc/probability-probability-bd7a90d99a43562d87076844-waterfall.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3001f024cb63dc88eb4e3c8d2f151bc3aa5abc819e916613476533a64d192ca6/4141fe28a116d8b8f7b4bcf44b8e7b38728120f482a9a69980a3e25bd1ff70df/probability-probability-bd7a90d99a43562d87076844-unresolved.svg`.

The aid `mission_ai_will_do` inspection for `cbrn_deploy_protective_aid` returned `PROBABILITY_SOURCE_INSPECTED`, 1 candidate, `poolComplete = true`, and 2 required inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16994e073d28bd982dc7eb566c5e47928d2a2a4ddba97c5df6522d326653bf58/bad4cb74b337c99cf9407891291166deb97767a7a755bfb5f8749c90e10a3da1/probability-inspect-d6e746de81b1.json`.

The current aid evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-ea7966e7c008978c7898f616`, 1 candidate, 5 unresolved items, 0 diagnostics, sourceRevision `f83f542388bb99c8953a8308dff9066700433aeca3076648346e2371547414fd`, and the same scenario hash. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93390c13613e3e8277d8f517b705d1a246f56a471dfdfd01d3e9fc544b56a6eb/ee5351ecf281114d170c68b8e9cefd04b98cf1cd74f1d3e67aef17c6ec03ceb6/probability-ea7966e7c008978c7898f616.json`. Rendered ranking, waterfall, and unresolved evidence is available at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/abef11b72f351af687c01d14fe0a0bcc417b597078ed5286d8a851c17150f320/b44726a82c5331d20fab413543bdce9bbcb9c638f0c31fbad0969eb9e1805a16/probability-probability-ea7966e7c008978c7898f616-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b038e117eac78f1a9e4fd7732c4c268e248c39a4d0b84393ff647e516897f624/be6e3a41dee35322a45abd9d80eac0b9898c1dcb346eb17c5ed46cf5a8460281/probability-probability-ea7966e7c008978c7898f616-waterfall.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3e5cc9fd3a6ed0c7d5fe88226f21b97eb4f1c2934f5af5edaaee4dbb1815619/ddccceb5884b37d7680ae9a133ccffcb9a100a60214013dbedf74ad1dba55037/probability-probability-ea7966e7c008978c7898f616-unresolved.svg`.

## Compare and skipped analyses

One `hoi4.probability_compare` attempt used the same named scenario, retired candidate pool, baseline artifact, and baseline/current source identities. It returned input validation errors: `sourceRevision` and `sourceHash` are unrecognized under `before` and `after`; `beforeManifest` requires an `id`, object `selection`, array `candidates`, and array `transitions`, and rejects the supplied probability-artifact fields. No comparison ID or comparison artifact was produced.

The compare tool metadata requires nonempty `before.path` and `after.path` strings. The supplied fixture retains a baseline analysis artifact but no historical source snapshot path that this route accepts. I did not compare the current file against itself or claim that the baseline artifact is a valid before-source manifest.

A baseline render attempt returned `PROBABILITY_ANALYSIS_NOT_CACHED` because its analysis ID was produced by a different server process. No baseline rendered view was produced.

No sweep was applicable because this patch has no retained numeric parameter or threshold change to vary. No simulation was run because no uncertain-input distributions were declared. No sequence analysis was applicable because the audited surface is not a declared custom pool. No MTTH, focus, event, GUI, technology, doctrine, or AI-strategy surface is part of this deletion.

The connected tool list exposed the live probability inspect, evaluate, compare, render, sweep, simulate, and sequence schemas. It did not expose a separate HOI4 version or health endpoint. No helper-expansion, job, or native-task route was used, so their additional client-negotiation workflow was not invoked.

## Findings and recommendations

The current source discovery exactly establishes that neither retired Sarin/Soman ID remains a weighted candidate in the inspected decision file. It does not establish a numeric zero selection probability or an after/before probability delta.

The baseline and current retained-surface analyses are score evidence only and remain unresolved for campaign behavior. The six-entry decision result has 59 unresolved inputs, and the one-entry aid result has 5. They do not establish score dominance, starvation, rank reversal, repetition, click probability, campaign probability, or exploit safety.

No weight patch is recommended from this evidence. Preserve the accepted hidden coercive-law compatibility gate and protected-law and aid weights as reviewed. The coercive-law base remains positive while the decision is explicitly invisible; its contribution to an active AI candidate pool is unresolved by this partial trace and should not be represented as a campaign risk or as a probability claim.

To close the historical compare requirement, provide an immutable pre-edit source snapshot at a path the connected compare route accepts, then rerun the same named scenario with a supported typed target binding if quantitative score deltas are needed. Keep that result separate from any normalized selection probability until the full candidate pool and external factors are complete.

## References consulted

Read `AGENTS.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, and `.agents\skills\chaos-redux-mtth\SKILL.md`.

Consulted the offline wiki snapshots for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

Opened the installed vanilla documentation Markdown bundle and reviewed the decision-weight-relevant script concept, modifier, and trigger documentation.

Read-only audit only; no gameplay, AI, scripted-trigger, constant, localisation, asset, or runtime file was changed.