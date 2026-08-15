# Event 006 settled Join Wave and formable state-puzzle probability audit

Date: 2026-08-09 (MCP runs completed while the shared worktree was still changing)

Mode: read-only `chaosx_ai_probability_auditor` audit. No gameplay, AI, GUI, localisation, or runtime files were edited, staged, or committed.

## Disposition

The settled Join Wave conversion is deterministic in source. The report event has two visible options with no explicit `ai_chance`, and package probing is a fixed 28-entry first-success chain. It is therefore incorrect to describe package selection as a normalized probability pool.

The formable state-puzzle additions do not introduce a new random selector. They add a shared territory gate to player and AI formation commits, plus family-specific prerequisites and an AI willingness/host-stability helper. Their `ai_will_do` values are scores used in an AI decision race, not click probabilities. The MCP adapter could not evaluate complete typed world states, so this audit does not claim normalized selection, dominance, starvation, timing, or balance for the formable decisions.

## Required source and reference review

Reviewed `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`.

Reviewed the required offline wiki pages in `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.

Reviewed the relevant vanilla documentation files `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

The offline Event Modding page states that an unset event `ai_chance` is assumed to be weight 1, with proportional normalization only after a complete option pool is known. The Decision Modding and AI Modding pages distinguish `ai_will_do` MTTH-like scores from event-option chance. The Effects page documents `random_list` as an explicit weighted selector. These rules are applied below without inventing weights where MCP did not expose a complete pool.

## Audited source surfaces

### Join report and deterministic package probe

* `events/006_independence_wave_join.txt:9-26`, event `chaosx.nr6.36`.
* `common/scripted_effects/006_independence_wave_join_effects.txt:190-222`, helper `independence_wave_join_probe_attested_package`.
* `common/scripted_effects/006_independence_wave_join_effects.txt:234-338`, package probe, eligibility, plan creation, and probe entry.
* `common/scripted_triggers/006_independence_wave_join_triggers.txt`, source eligibility and reduction threshold helpers.
* `common/script_constants/006_independence_wave_constants.txt`, join thresholds and package identifiers.

`chaosx.nr6.36` has two visible options, `chaosx.nr6.36.b` (decline) and `chaosx.nr6.36.a` (accept). Neither option contains an `ai_chance` block. The event trigger requires `independence_wave_join_offer_pending` and the current plan. The source therefore supplies no option-specific AI modifier trace; an unset option is only a default weight under vanilla semantics, not an independently proven 50/50 result from this audit.

The package probe sets `independence_wave_join_probe_success` to `no_candidates`, tries each package, and advances to the next package only while the previous attempt still reports `no_candidates`. The exact current static order is: `IW-001`, `IW-002`, `IW-004`, `IW-006`, `IW-007`, `IW-008`, `IW-009`, `IW-010`, `IW-012`, `IW-014`, `IW-017`, `IW-018`, `IW-019`, `IW-023`, `IW-024`, `IW-026`, `IW-027`, `IW-028`, `IW-029`, `IW-030`, `IW-031`, `IW-033`, `IW-041`, `IW-070`, `IW-071`, `IW-072`, `IW-173`, and `IW-184`.

This is a deterministic priority race. If multiple package wrappers could succeed in the same world state, the earliest successful ID wins and later IDs are not sampled. That is an exact source-level ordering finding, not a probability or balance claim.

### Formable state-puzzle gates and AI scores

* `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:631-697`, `can_independence_wave_commit_selected_formable`.
* `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:699-718`, `has_independence_wave_selected_formable_state_puzzle_territory`.
* `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:720-746`, method-specific commit-cost gate.
* `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:748-766`, `should_independence_wave_ai_pursue_selected_formable`.
* `common/decisions/006_independence_wave_formable_registry_decisions.txt:10-228`, ten registry decisions and their `ai_will_do` blocks.
* `common/decisions/006_independence_wave_decisions.txt:3328-3435`, discovery, congress, and `independence_wave_proclaim_military_union`.
* `common/decisions/006_independence_wave_form05_decisions.txt:261-300`, `independence_wave_form05_proclaim_island_league`.
* `common/scripted_triggers/006_independence_wave_form05_triggers.txt:489-494`, the dedicated FORM-05 proclamation gate.
* `common/script_constants/006_independence_wave_decision_constants.txt:244-259`, score constants (`low=5`, `high=25`, `urgent=100`, `modifier_major=5`, `modifier_double=2`, `minimum=0`).
* `common/script_constants/006_independence_wave_formable_constants.txt:146-157`, AI willingness bands (`never=0`, `rare=1`, `low=2`, `moderate=3`, `high=4`).

The shared commit gate requires a regional power, matching family, selected state-puzzle territory, family-specific reviewed proof, `independence_wave_formable_transaction_ready`, `formation_ready` state, congress approval, commit readiness, and absence of pending/active flags. The AI helper additionally requires AI scope, commit readiness, a special FORM-48/FORM-39 pursuit path or at least moderate willingness, no severe instability, and no German-dominance avoidance. Player and AI therefore use the same hard territory/formation gate; AI receives an additional willingness score gate.

The registry decisions use high/low bases and multiply by `minimum` when `should_independence_wave_ai_pursue_selected_formable` is false. Route flags can apply `modifier_double` or `modifier_major`. The hidden method decision has a `minimum` base. These are scores only; they are not normalized click probabilities.

`independence_wave_proclaim_military_union` uses `base = high` and a `minimum` factor when the AI pursuit helper is false. Its `visible` and `available` blocks call the shared commit gate; `available` and `custom_cost_trigger` also require the method-specific cost gate.

FORM-05 proclamation uses an urgent base and a severe-host-threat `modifier_major` factor. Its hard availability gate requires runtime readiness, first charter stage, FORM-05 state-puzzle territory, no global mix-identity flag, cost payment, light-factory capacity, and no active project. The source contains no proportional selector around this score.

## Probability MCP evidence

All calls used workspace `mod_chaos_redux_ea3b2d67c2c0`. Artifact URIs below are the durable MCP evidence; source revisions and scenario hashes are preserved exactly.

### A. Join report options (`event_option_ai_chance`)

`hoi4.probability_inspect` on `events/006_independence_wave_join.txt` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `dde93c81dde160027888bc0c284e55d4763d64f24163aded9397624e292b3407`, source hash `4a850ea7516df5353273250a40da30255429cb63a3d79a2fe8964f679266b15d`, three discovered candidates, zero available candidates, and one unresolved item. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54c6430a5b7b811eed05cc6b6110a80e5a64b040b5c1dbec5d1a1d18fa60296b/45cad0b0026d1fe90482fa0a874a0dc746e5bd5e77041d15204b2df3212085e1/probability-inspect-4a850ea7516d.json`.

Named evaluation set: `E6_JOIN_REPORT_OPTION_SCENARIOS_2026_08_09`, scenarios `JOIN_REPORT_PENDING_SOURCE_ELIGIBLE`, `JOIN_REPORT_SOURCE_INVALID`, and `JOIN_REPORT_EXPIRING`. The scenario states were intentionally empty because the adapter did not expose the pending-plan helper inputs; no external factor was silently assumed.

`hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-43efc5e23e1a527e8e47241d`, source revision `2bcafb746f05a10402381bdae5b46473aabcc8c49af1c21b17506570b22db6f3`, source hash `4a850ea7516df5353273250a40da30255429cb63a3d79a2fe8964f679266b15d`, scenario hash `25b2a19650dd3bb14679c4a460f60b082b7696083a7f5c9200149580eda65904`, nine candidate rows, one unresolved item, and `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. Normalized probabilities were withheld. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fed62af0c8adbd69843bbd82951b2f8825ca8dd8ecbf057bd666afd6b08aa9b8/169fc1162abc1f6526cdf6843057e9e3beb79a46c9898b0b5d26b9f833194fa4/probability-43efc5e23e1a527e8e47241d.json`.

Evaluation render resources were produced at ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4fd1c52f7555676e29502713533c2d28d3bb781c6d5e0c917b76a78b3cd6426/76a1e220e298dea69d6197d841a81592e78b166c89f1218efe755fefabb656de/probability-probability-43efc5e23e1a527e8e47241d-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6badf3e9715d192d5aebfc707da230d1fd9b46e08634f3e6514c61187e8adfa/dc800493f437c7139a2bebd0ba4a5bf77ffdf1428db9232657c8ef01b53f883d/probability-probability-43efc5e23e1a527e8e47241d-matrix.svg`, and unresolved view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e257f15049e6a4d2b5c5a50fb052e3a223dfa063df08ec7004c29297eab9ae2/92cd7efaf689685ccf5b805069f3fa2ad3f94287adcad4fbfb2ab542cff8a161/probability-probability-43efc5e23e1a527e8e47241d-unresolved.svg`.

The later `hoi4.probability_render` call returned `PROBABILITY_ANALYSIS_STALE`: analysis revision `2bcafb746f05a10402381bdae5b46473aabcc8c49af1c21b17506570b22db6f3` no longer matched current revision `2b24e3837b3104d8a083d97600c2efbaaf56a05115381189e7074a382fd1b4b`. The evaluation artifacts above remain the evidence at their recorded revision; rerun after the owner stops changing source before treating the render as current.

Classification: source-default/score-only and unresolved for normalized chance. No exact accept-versus-decline probability is claimed.

### B. Join package chain (`random_list`, `custom_weighted_pool`, `direct_random`)

`hoi4.probability_inspect` on `common/scripted_effects/006_independence_wave_join_effects.txt` with `random_list` returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, and no unresolved items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1020596abe91312d8db34c5565816fbe32da6fde9b0cf6ae7af8fe0f6a232a87/efcc9c5d710ff335ae01fdf929b197585c8fd6bf327be55561142cac5bb7782a/probability-inspect-1eb53b50f458.json`.

The same source with `custom_weighted_pool` returned zero candidates and no unresolved items, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/311c02570fcfb96066b483501148c6205c4208b6a7a8106d3893e449de841678/41f5e100361c04832b11ffc221eb0ba515eaef950e866d72ccdbc85a7b72d157/probability-inspect-1eb53b50f458.json`. The `direct_random` probe likewise returned `no_weighted_surfaces`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34e2f8adf90255911ac917135cb3d471f429241373a385ad2fc288ca1e94e867/f15f7207745dea8d0f8cdb43342797599b2ba1aa1a006630f1f0cb6fd6bc8d4b/probability-inspect-1eb53b50f458.json`.

Named deterministic scenario set: `E6_JOIN_DETERMINISTIC_SCENARIOS_2026_08_09`, with `JOIN_SOURCE_OPEN` (`source_eligible=true`, `all_owned_state_footprint=true`) and `JOIN_SOURCE_NO_PACKAGE` (`source_eligible=true`, `all_owned_state_footprint=false`). This historical pre-IW-031 run declared the then-current 27-ID candidate pool. `hoi4.probability_evaluate` against `random_list` returned the exact blocker `PROBABILITY_SURFACE_EMPTY` with message `No weighted blocks matched this request` and no artifact.

The historical pre-IW-031 `custom_weighted_pool` evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-caa943037c0c14a1ff21dc01`, source revision `f2329493b0f1bf795d860fbf33c01040e587859105611c902d243f1b30243583`, source hash `1eb53b50f45857345d47d2b6eb65afa79934e9a23949a809f442c787a42730de`, scenario hash `30ac58a8bfced26663732ff5f864ab4991545828af69998417a22bac406bbbe2`, zero resolved candidates, 27 unresolved candidates, and `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. Normalized probabilities were withheld. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d82d7fafebf4c75c01677e6b959c6c443756332896086084f19cb90279c472ab/1a29e7d41e8164fb73c1a332e3ed69a3f12ee45cbcb084c4262cfd201107ef0/probability-caa943037c0c14a1ff21dc01.json`.

Ranking, matrix, and unresolved views were rendered by the evaluate call: ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1e11d09464a018b78cd53427004a4f2cd0c08cea209a97dc6f874218e71f788/04c9d4641473d34642b6a1dfbef9347ed2fefb48882fb6ca6eb7ac3238551191/probability-probability-caa943037c0c14a1ff21dc01-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/936d1d77ca30ee9e4ed1bb9167c9e7f2cdadc70e88d5ec139f885b34941102a7/331ff75f28e9d358a355b89854fef31da73242f67ddc167d910a14e6a5bac9c7/probability-probability-caa943037c0c14a1ff21dc01-matrix.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8ffaad5488fbc46c478da2d253e49ea1f395d6f283e0986fe905fd2f1d1d6f9/f2be358dcbb765d1451d6b8efe15b6c75ef6bacc2a7ee4d5c39405766679f3a3/probability-probability-caa943037c0c14a1ff21dc01-unresolved.svg`.

Classification: deterministic order is exact from source and the empty weighted-surface result is exact from MCP. Package validity, state ownership, host capacity, and all wrapper triggers were not representable in the custom pool adapter, so no exact package probability, timing distribution, or simulation is available.

### C. Formable registry decision `ai_will_do`

`hoi4.probability_inspect` on `common/decisions/006_independence_wave_formable_registry_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `5fb1b6e46f062f967de785bf3ec55473de28795d189a81a301092a9ee95e79a1`, source hash `3a2eaa6dd5222a1362f5c97fc812b4a0b82b77a9c7c2b7fb92c17b4cd6b89756`, ten candidates, 39 required inputs, and no unresolved inspect items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/542250df10d5b7029c5c3dce98ede05fa5d20500cf3edfa94aae99ee03abe04e/2b1ecede0b354eaa432b132ef9587bc371c1b6fe741867e2e70d846496329324/probability-inspect-3a2eaa6dd522.json`.

Named scenario set: `E6_FORMABLE_REGISTRY_DECISION_SCENARIOS_2026_08_09`, with `FORMABLE_REGISTRY_PROFILE_READY`, `FORMABLE_REGISTRY_HOST_CRISIS`, `FORMABLE_REGISTRY_ROUTE_LOCKED`, and `FORMABLE_REGISTRY_NO_VALID_TARGET`. The state objects were empty, so flags, variables, family proofs, costs, host threats, and selected territory were not assumed.

Evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-d33e5fa2f4c95ca8d33ec023`, source revision `862b27f02d3845c884840fa239269033e303cbdeef2b6c8727480ec76dded6d9`, source hash `3a2eaa6dd5222a1362f5c97fc812b4a0b82b77a9c7c2b7fb92c17b4cd6b89756`, scenario hash `15265cb483a39b4bcc39d62081a98fd1b7fcb1dfb2118b18b780a778be446a4c`, 40 rows, 3,239 unresolved items, and 15 diagnostics. The four post-method decisions and all five route-method decisions were reported never eligible in the empty states. This is an expected bounded result of omitted state, not proof that those source decisions are dead in a valid campaign state. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f62a29fb811af87a5f13ac82209f1897269fab76b39b619ac0df4e6b3661e5b3/3580b5d92810459a62bb2e27ced61916670a9b00fbbd1be4c3de254123cc271d/probability-d33e5fa2f4c95ca8d33ec023.json`.

Rendered ranking artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e33fbb169dc544e2cf35f5945fd252dac3d9dff49e397235defb209d01467b2e/930e0682cfdbe83ef94b44133aa4f9a473a15de37e287df49fc99a07605f7400/probability-probability-d33e5fa2f4c95ca8d33ec023-ranking.svg`; unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7495a8d34a96e25fcd5d44174bb833957e9f3c008689a4f6d5cf2814e2cfbea2/c9a32be590231ab04a12f326117dc23a0a171dfb1bd849ab1c23da35e4b864d6/probability-probability-d33e5fa2f4c95ca8d33ec023-unresolved.svg`.

The same-source `hoi4.probability_compare` capability receipt used adapter `decision_ai_will_do`, both `before` and `after` path `common/decisions/006_independence_wave_formable_registry_decisions.txt`, the ten-candidate pool, and the same named scenario set. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-d7f77a5642a1e26ae39a37f0`, source revision `09b603496f95569235a7852d1e0dce864f1527f9b1e866ed68f91f10e8b16b3f`, source hash `3a2eaa6dd5222a1362f5c97fc812b4a0b82b77a9c7c2b7fb92c17b4cd6b89756`, scenario hash `a838962775c28f6d2fce84a7bdda650e739f0cd6350b5b68aeaa9f5423cd17d9`, 40 rows, 3,239 unresolved items, 15 diagnostics, and `comparisonChanges=0`. This is a same-source capability receipt only, not a before/after patch comparison. Comparison artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/84dd57aa5c352cf4060154f2fe947f58ff095af77489e74b0f2ac78aa0b3a5ce/probability-probability-d7f77a5642a1e26ae39a37f0-comparison.svg`.

The required sweep was attempted with adapter `decision_ai_will_do`, the ten-candidate pool, the same scenario set, `state.war_support`, three steps, pairwise comparison, and rank-reversal search. MCP returned exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED`: every sweep path requires a scenario range, numeric alternatives, or a numeric state value. No sensitivity or rank-reversal conclusion is made.

Classification: score-only/bounded. No normalized AI decision probability, route dominance, or starvation claim is valid from these empty-state runs.

### D. Shared formable commit decision and FORM-05 mission

`hoi4.probability_inspect` on `common/decisions/006_independence_wave_decisions.txt` with `decision_ai_will_do` returned source revision `862b27f02d3845c884840fa239269033e303cbdeef2b6c8727480ec76dded6d9`, source hash `f84a0e082f6a8b5c518eb769478676e6b78bc23157a39b0303f9947b729aa583`, ten discovered candidates, 79 required inputs, and no unresolved inspect items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6cc7b9bb6fe676a675cf59ca8e69d36bfaee5eac2b061a26f6791a96547d4ca5/e40c5999c9e642ab5214a3a2b4d1243703146a96227fd182d6cb3d85598fa3f6/probability-inspect-f84a0e082f6a.json`.

Named scenario set: `E6_FORMABLE_COMMIT_GATE_SCENARIOS_2026_08_09`, with `FORMABLE_READY`, `FORMABLE_HOST_CRISIS`, `FORMABLE_ROUTE_LOCKED`, and `FORMABLE_NO_VALID_TARGET`. Empty state objects omitted all family, territory, transaction, congress, cost, and host values. Evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-0a79f4cd753ca58de8e6132e`, source revision `fb5e848da435ab7e69b2ae4e47bed266937759c180a70cba331eceab620a3388`, source hash `f84a0e082f6a8b5c518eb769478676e6b78bc23157a39b0303f9947b729aa583`, scenario hash `daf0712deb2f9de611a4b5a65be7a8f935139ebb9d7f21fc8f4673e44315dbde`, 40 rows, 2,831 unresolved items, and eight diagnostics. `independence_wave_proclaim_military_union` was never eligible in these empty states. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93919224bf991eec4ecaf2c48284a1a54705a71060bfbd4d4d8e885badb01d06/15b677b640e2b143309e01e58e039a8f7c8ebf34bb9d23c80d8bb37af522b43f/probability-0a79f4cd753ca58de8e6132e.json`.

Rendered ranking artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1181720dca51b79afbb8aaaf6338c7e14d4fffa50ffdc45c6f8258d20c5667d/845d6bf2d387498ce9484289c2d10b70ad63869952455db81cec47481e7f738a/probability-probability-0a79f4cd753ca58de8e6132e-ranking.svg`; unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f66ebaf4ff3b417e15c6cf8275d394246ab53d700508a6efd4406089e36a2cf/7777e3207769576a3a07c9501bb78a6b15d34919fb27a12c0c3c2121642f769e/probability-probability-0a79f4cd753ca58de8e6132e-unresolved.svg`.

The FORM-05 decision file does not expose the requested decision adapter. `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_DISCOVERED` with suggested adapter `mission_ai_will_do`, zero decision candidates, and 14 available mission candidates. Mission inspect returned source revision `fb5e848da435ab7e69b2ae4e47bed266937759c180a70cba331eceab620a3388`, source hash `8e0437a09a516789041c57acb84041feeae05ea96ff926a25abcf8300a4ec210`, 14 candidates, and 24 required inputs. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf58259578087ef9f49276233354e3f0ea89637b5317b23c54b424cf712c1d20/259e8fad1391278e4849fcc3c30205c322246c56e3757ce792d7403d86ce795c/probability-inspect-8e0437a09a51.json`.

Named mission scenario set: `E6_FORM05_STATE_PUZZLE_GATE_SCENARIOS_2026_08_09`, with `FORM05_CHARTER_OPEN`, `FORM05_INVITATION_PENDING`, `FORM05_CARRIER_ACTIVE`, and `FORM05_NO_VALID_TARGET`. Empty state objects intentionally left charter progression, carrier identity, territory, costs, and host threats unresolved. Mission evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-1acaeb4c024617e224bf7eee`, source revision `fb5e848da435ab7e69b2ae4e47bed266937759c180a70cba331eceab620a3388`, source hash `8e0437a09a516789041c57acb84041feeae05ea96ff926a25abcf8300a4ec210`, scenario hash `e82cdbb6456e98a87c3b57020763da1091fce330a9e6c8417beb4123025ec66b`, 56 candidate rows, 319 unresolved items, and 17 diagnostics. The never-eligible FORM-05 proclamation and petition/accept/withhold rows are bounded empty-state results, not a source dead-route finding. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d4700c668ee3e4a421f6eaaefed9daf9efdde5c95110ce82061a33bfbd2989d/81b0f8fd86c35e2e25799710a38d6c752ca4f81d3b7743234462567c7dd7d53d/probability-1acaeb4c024617e224bf7eee.json`.

Rendered ranking artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/918e05e6c0e9e77cd08b5c01ae50842cdab5d7216d24466a18d5114354b22554/425c562e1cc9dec39b699fd1a45b740cc172d10385bec4a2442c3672d29bf95d/probability-probability-1acaeb4c024617e224bf7eee-ranking.svg`; unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90c52d19040f275ba71f05662edaf64224deb48deeb3bf1ec29be8886f297376/6b5cc7f166dc4825ff3228eed926e3bc7a9745086a589b16203edb6f48c0087d/probability-probability-1acaeb4c024617e224bf7eee-unresolved.svg`.

Classification: score-only/bounded for the shared commit and FORM-05 mission. No normalized AI probability is claimed.

## Structural MCP evidence

`hoi4.event_inspect` scanned `chaosx.nr6.36` with selector `{kind=event,eventId=chaosx.nr6.36}`, returning `EVENT_INSPECTED_PARTIAL`, revision `fa5988c7ac2c0f3f5c10506fbb0b87e129c99f7f2e61fafba6c2825440fd4c20`, graph hash `928327287e388669d1426545c79aefc05975ff5059080d5e2a96112109b985b0`, seven selected nodes, 41,131 omitted nodes, and no blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccb650f1926442f58dfdfdbb67e6ee526fbbbcc2013aa80f3fe27bfb716aa8ce/9d02deba15c561ac6229be0a0186c7c8ad5c8a1c6496a9cfb9eb00f4c57f537f/event-scan-fa5988c7ac2c.json`.

`hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash. SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8caa5319fb31eb93dace28f9a289ce456578c820b87c49830a8e703876cd6a61/29893f3e9d825ed439d1db6ca3f47d60670483bd707b54fa7f439f413f1603d5/event-overview-fa5988c7ac2c.svg`.

`hoi4.gui_inspect` inspected `chaosx_independence_wave_formable_state_puzzle_window` under scenario `E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09` and related locked/full-list scenario IDs. It returned `GUI_INSPECTED`, shared revision `8fbe25086b3c9c3d3875243115b8146e9b47a2093bcdf71333ac009e5e6b91d8`, 93 inspected elements, and diagnostics dominated by workspace-wide duplicate symbols and visible overlaps: 1,551 `GUI_VISIBLE_OVERLAP`, 144 invalid scripted-context diagnostics, and 3,597 index symbol collisions in the bounded diagnostic set. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/499a116fd93bea3ac9cee53e5351a829959354fde8fddbfa18c97ea0608dd504/ef8e60f6e29c9c7c6a81bfdf493e0e9b5f9e7967d269a629008dbaa7b1120c0e/gui-inspect.8fbe25086b3c9c3d.json`.

`hoi4.gui_render` returned `GUI_RENDERED` for the normal/locked/disabled/empty-list/full-list states at 1920x1080 and 1366x768. SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e754ba9e1bae29b05ae013092399118afcfe42cedf62d2833fe9/5c0db49a95a7bd5ef39bd6f4e1ca7779305f10871c9615c5647da533b3ae3570/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The current category attachment source contains 17 `independence_wave_formable_state_puzzle_scripted_gui` attachments across the registry, transaction, FORM-01/02/03/04/05/08/09/12/13/16/39/48, IW-043, and IW-058 category files. Structural GUI diagnostics are not probability evidence and are not used to infer AI weights.

## Dominance, starvation, repetition, and exploit-risk assessment

* Join package order has deterministic priority dominance: any simultaneously valid earlier package suppresses every later package. This is exact source behavior, not a normalized probability result. If this priority is intentional, document it; if fairness is intended, the owner should replace it with an explicit declared selection mechanism and then provide a complete candidate pool for probability analysis.
* The report options have no explicit option weight. Their source-default disposition is exact, but MCP did not prove a complete candidate pool or a current normalized choice. Do not claim a click probability.
* Formable `ai_will_do` scores are guarded by hard availability and state-puzzle gates. The empty-state MCP runs cannot establish dominance, starvation, timing drift, repetition, or exploit safety for valid campaign states.
* The shared commit gate is fail-closed on missing territory, family proof, transaction readiness, congress vote, costs, or host conditions. This is a source-level safety property; whether any family is accidentally starved requires a typed family-by-family state matrix that the current adapter did not receive.
* FORM-05 has a high urgency score and a severe-host-threat multiplier, but its runtime and state-puzzle triggers remain hard gates. No probability or snowball claim follows without typed states and a complete mission pool.

## Skipped analyses and exact reasons

`hoi4.probability_simulate` was not run because no explicit uncertain input distribution, seed, cadence, or terminal-state model was declared. Sampling would invent campaign uncertainty.

`hoi4.probability_sequence` was not run because the Join probe is not a custom weighted pool with declared cadence, cooldown, removal, reset, and terminal transitions. The source chain is deterministic first-success.

The registry sweep was attempted and returned `PROBABILITY_SWEEP_RANGE_REQUIRED` because `state.war_support` had no numeric range or alternatives in the named scenarios. No threshold or rank-reversal result is reported.

A true before/after comparison is unavailable because this settled audit has no approved pre-change source path. The same-source registry comparison above is explicitly a capability receipt (`comparisonChanges=0`) and must not be treated as a patch delta.

## Recommended owner follow-up (not applied)

1. Preserve the 28-entry Join order as an explicit priority contract or replace it with a declared weighted/random mechanism. If replaced, rerun `probability_inspect`, `probability_evaluate`, `probability_sweep`, and `probability_compare` with the complete package pool and typed package-validity states.
2. For the report options, retain explicit equal/default behavior only if intentional, and rerun the event-option adapter after the source settles so the complete candidate pool and current revision are captured.
3. Build a typed state matrix for each of the 14 state-puzzle family helpers, including selected family, selected territory, transaction phase, congress outcome, resource costs, AI willingness, host threat, and pending/active flags. Re-run registry, shared commit, and FORM-05 mission analyses under the same named scenario IDs.
4. Obtain an approved pre-change source snapshot before requesting a real `probability_compare`; do not use same-source comparison as a balance claim.
5. Treat the GUI overlap/context diagnostics as a separate structural/UI handoff. They are not evidence that the state-puzzle gate or AI scores are probabilistically wrong.

## Remaining uncertainty

The MCP analyzers proved the absence of weighted random surfaces in the Join package source and exposed the exact score/gate structure of the formable decisions. They did not prove normalized option probabilities or valid-world-state AI rankings because candidate pools and external state were incomplete and the worktree changed between analyses and render requests. Parent review should carry this audit as exact deterministic/source evidence plus bounded score evidence, not as a quantitative balance certification.

## Historical Join rerun after scoped retry addition, before IW-031 promotion (2026-08-10)

The Join source subsequently added hidden scoped retry event `chaosx.nr6.40` at `events/006_independence_wave_join.txt:54-74`, including retry-flag clearing and a fresh peak-baseline capture before rechecking source eligibility and the reduction threshold. The visible `chaosx.nr6.36` option block remains unchanged at lines 20-25, with no `ai_chance`; IW-031 was promoted later, extending the package order to the current 28 entries at `common/scripted_effects/006_independence_wave_join_effects.txt:234-264`.

Current `hoi4.probability_inspect` for `event_option_ai_chance` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `70b99a6a792141fa0f244b4cb2cc3c3c8a6f4eb6c8b0a99bdd27e6c1ae396d9a`, source hash `fd24e2856be51edf2c26ce40745659d86dffb4e1ec21f4edf5710216c6597d72`, three discovered candidates, zero available candidates, and one unresolved item. Current artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4054ccf4a6e3bf5567625b4d439102593235bd3d47fa8ebf5e5790a8684e0f66/833ecb8944cf6aa5e691840584d59be8480cdf14e53b10bed431fb49348e0c2b/probability-inspect-fd24e2856be5.json`.

Current `event_option_ai_chance` evaluation used named scenario set `E6_JOIN_REPORT_OPTION_SCENARIOS_2026_08_10` with `JOIN_REPORT_PENDING_SOURCE_ELIGIBLE`, `JOIN_REPORT_SOURCE_INVALID`, and `JOIN_REPORT_EXPIRING`. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-580208381c0032e784802a4d`, source revision `6c39d65e16db3e131fcc3a54b2c2eea283b49ffaac9eaaa40d4066180c206028`, source hash `fd24e2856be51edf2c26ce40745659d86dffb4e1ec21f4edf5710216c6597d72`, scenario hash `f653220538228e6b7c1899fb7635185fa3ccc7071edfbab8f6fbb6deff9939a2`, nine candidate rows, one unresolved item, and `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. Normalized option probabilities remain withheld. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/529728161da8c964cfadbf9f1457f285f289ee41282b4bdeecc139b2de23175f/c4e2fdf2dfa049b6ba18f6809c0fbdd197550b29562cbf1910ec8cd6df946623/probability-580208381c0032e784802a4d.json`; ranking artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5ff6d2f633a0716e1333b2aa529191d4687628fe288b7fe088d4794cae99bf7/f5bac0cf43b9384e18bdd1315f73e4c8ec9dd8238dcf7dba07026f8e58df0fbd/probability-probability-580208381c0032e784802a4d-ranking.svg`; unresolved artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e257f15049e6a4d2b5c5a50fb052e3a223dfa063df08ec7004c29297eab9ae2/77fa50a0651ca0fd0725b3b7dee6ebd1fa2a75f5698c90ae1c2d02bc3eabf5c2/probability-probability-580208381c0032e784802a4d-unresolved.svg`.

Current `random_list` inspection of `common/scripted_effects/006_independence_wave_join_effects.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, source revision `d6d1c74ecc266c94d1488424de0e1341a5ac8b13abd63eb0115ff411f5f2db88`, and source hash `2d7858fcf7bd37e42c4af91cfa33cf35c6149597bf33658fe00d23b8c1d77cc2`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4eecdd63587aa38739e0f325c653024db5b1c11857dfe4da7ad9f1f2b329cfbb/b48f1053ea4e9af95e3c17de76bf8d082c98d5d89218e5da9032321362d74f2d/probability-inspect-2d7858fcf7bd.json`.

Current `custom_weighted_pool` inspection returned `PROBABILITY_SOURCE_INSPECTED`, source revision `1f3e902fc871b89e839a42934ebb4eac02d2eb34b5ea072a0a257a698188c6d0`, source hash `2d7858fcf7bd37e42c4af91cfa33cf35c6149597bf33658fe00d23b8c1d77cc2`, zero candidates, and no unresolved items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c26748fc2e743a93d4cf9b780ca7c4e5807ef116737a9fa010bb297e75a64788/920f09e1ddfa739b98e434bb116948fc6f6dd8582f1fe19242d70051af57ef7f/probability-inspect-2d7858fcf7bd.json`.

Current `direct_random` inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, source revision `d4d21d488c6b2032b8d522529fddb2d81306471c60e4a9974580c4b6bf844583`, and the same source hash `2d7858fcf7bd37e42c4af91cfa33cf35c6149597bf33658fe00d23b8c1d77cc2`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/486f9c5945535118d3623ab0651929718275e387a4a1d093bc03f9d669a7fb5d/892220bf8166d3789b6e60c1a5c58555a16d9d87bbe32627ac6634b7841b3ca2/probability-inspect-2d7858fcf7bd.json`.

Using the complete pre-IW-031 27-ID source pool and named scenario set `E6_JOIN_DETERMINISTIC_SCENARIOS_2026_08_10` (`JOIN_SOURCE_OPEN` and `JOIN_SOURCE_NO_PACKAGE`), the pre-promotion `hoi4.probability_evaluate` against `random_list` returned the exact blocker `PROBABILITY_SURFACE_EMPTY` with message `No weighted blocks matched this request` and no artifact. This receipt is historical; the retry event adds no weighted selector and does not change the deterministic first-success disposition.

Current structural evidence was refreshed after the retry addition. `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL`, revision `d0c3016e0598be2a37c11abe8b7674a20c737a74e01216fe8fa12c3bfa100c25`, graph hash `b41902d0fa8c3f8aa8e5f2d99ef5a5d600631a3696f694309f39ccded2f2786c`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a893f9c9ff437e7d683e7ed08d27f19c1b2aae6ae56ca8f7fbb5cc0f6f93f57d/a9eaefcc9ab40fc5849265976e6211b41f627df9f8c184ea3dc74effe95be67a/event-scan-d0c3016e0598.json`. `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash; current SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e12beb0faed241c19cc6c51eca1b5344573ec2cf8a7b62328abad5d75c341b5b/a0d0788929b432821fa860fe96810109dfc574ebaeee6f2e6222589c696fd3d3/event-overview-d0c3016e0598.svg`.

Rerun classification: exact source-level deterministic ordering and exact MCP absence of weighted random surfaces remain confirmed after adding `chaosx.nr6.40`. The visible option pool remains incomplete in the event-option adapter, so no normalized accept/decline probability is claimed.

## Current-FS IW-031 promotion refresh

IW-031 was promoted into the Join probe after IW-030. The current source order is the 28 IDs `IW-001`, `IW-002`, `IW-004`, `IW-006`, `IW-007`, `IW-008`, `IW-009`, `IW-010`, `IW-012`, `IW-014`, `IW-017`, `IW-018`, `IW-019`, `IW-023`, `IW-024`, `IW-026`, `IW-027`, `IW-028`, `IW-029`, `IW-030`, `IW-031`, `IW-033`, `IW-041`, `IW-070`, `IW-071`, `IW-072`, `IW-173`, and `IW-184`. The scoped retry event and visible `.36` option block are unchanged by this promotion. The parent allocator receipt reports 28 package entries against the 25-entry capacity band; that capacity count is deterministic source/planner evidence, not a weighted-selection probability.

The earlier `E6_JOIN_DETERMINISTIC_SCENARIOS_2026_08_10` random-list evaluation recorded above used the pre-promotion 27-ID pool and remains historical evidence only. It must not be reused as the current candidate-pool receipt. No new evaluation was run in this minimal refresh; the current source inspections below are the authoritative non-weighted disposition for the 28-ID pool.

Current `hoi4.probability_inspect` with adapter `random_list` returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, source revision `9ede898c06ef145ad7ec666eb2df9e620dc0fb834620cedbd8d11d838172ff49`, and source hash `88d8bed1f17d5fbfd111c35301d74a1d552c342cf9ac5d75b97283dab853c506`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2550c68d021e074c17689c8abd06f406b16037fa08e70cbb5704ff242ed24b7a/4b23dca00e82bfa82f209d5eb9067e7e23f2145e26ac05ef7e608239b1987ba3/probability-inspect-88d8bed1f17d.json`.

Current `hoi4.probability_inspect` with adapter `custom_weighted_pool` returned `PROBABILITY_SOURCE_INSPECTED`, the same source revision `9ede898c06ef145ad7ec666eb2df9e620dc0fb834620cedbd8d11d838172ff49`, the same source hash `88d8bed1f17d5fbfd111c35301d74a1d552c342cf9ac5d75b97283dab853c506`, zero candidates, `poolComplete=false`, and no unresolved items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2b11c2cc6463b47b27f30bd567782d66ad7a8794d029b6380bb04ced0178674/4e00b50542ee7b0d5bfe1710b985531f0f8d194ed75fff23ce9f6348bf90909a/probability-inspect-88d8bed1f17d.json`.

Rerun classification: the current 28-ID Join probe remains an exact deterministic first-success chain with no MCP-recognized weighted surface. The complete 28-ID order is source evidence, not a normalized probability pool; no current package-selection probability is claimed without a current typed evaluation manifest.
