# Event 006 AI probability audit continuation — 2026-09-12

Status: read-only weighted-logic audit, bounded and incomplete. No gameplay, AI, event, focus, decision, mission, technology, doctrine, localisation, asset, or tuning source was changed. The only write in this continuation is this handoff. No staging or commit was performed.

## Audit contract and snapshot

The audit covers the Independence Wave outer allocator, all discovered regional and formable random lists, package scoring, root and support event `ai_chance`, decisions and missions, focus `ai_will_do`, AI strategy factors, MTTH/evolution timing, research/doctrine adapters, and declared custom pools.

Required references were read before review: `AGENTS.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-mtth/SKILL.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-focus-trees/SKILL.md`; `.agents/skills/chaos-redux-event-planning/SKILL.md`; Event 006 specifications and plans; the required offline Paradox wiki pages; and relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

The HOI4 MCP workspace is `mod_chaos_redux_ea3b2d67c2c0`. Repository HEAD at the snapshot is `916646784f17088b84209ca9d61ad0abc3a7e3e9`, with 4,010 pre-existing worktree status entries observed before this handoff was written. Because concurrent edits are present, the file hashes below are the audit-time snapshot and must be rechecked before any owner-applied patch.

## Source snapshot and weighted inventory

| Surface | Exact source and identifier | Local SHA-256 | Inventory or source-only result |
|---|---|---|---|
| Outer allocator | `common/scripted_effects/006_independence_wave_effects.txt`; `independence_wave_select_one_automatic_package` | `398D0182651BE1A201E3348BC254578BE948A9261B02A192E864C1B05E068A99` | One 14-entry `random_list` and explicit zero-total/pool-exhaustion path. |
| Nested package pools | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`; regional selectors 01–14 | `8C2ECFAE511097357CC3C4456548A71FB2CE8A78E23537C5087ECE9B2ADBE6E7` | Fourteen lists and 126 package entries. Region counts R1–R14 are 9, 9, 8, 8, 12, 12, 5, 3, 7, 7, 5, 13, 19, 9. |
| Package score | `common/scripted_effects/006_independence_wave_package_planner_effects.txt`; `independence_wave_calculate_candidate_allocation_weight` | `2409C0D5FD7381630581FF5C2CCFD30509922AECCE0800419B53C0D8AE22E6B9` | Source terms include base 100, sponsored +100, registered +25, new region +30, new host +20, prior package −80, prior region −25, prior host −20, low-chaos −35, high-chaos +45, evolution terms, rarity factor, and minimum floor 1. This is a score, not a probability. |
| Formable Congress | `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`; `independence_wave_formable_resolve_congress` | `F4B14B3CF8AD7933D56515CC9FF6FADFB7C65899B0CA18B749F22C128F1A8884` | Two-entry success/failure `random_list` with failure fallback. |
| Root events | `events/006_independence_wave.txt` | `9C89405800DFAA484FECBE4E08DE108B5F8E028E1D2973FCBEAA3B3A8BCF5368` | 22 event-option candidates discovered; 13 required inputs. `chaosx.nr6.1` is hidden/immediate and does not itself provide a player option race. |
| Support events | `events/006_independence_wave_support_events.txt` | `F8DB738666DC14003DC3240DD027DA3DDD8EC3F67EE85465B9C8F580B4265021` | 154 event-option candidates discovered; 45 required inputs. |
| MTTH/evolution source | `common/mtth/chaosx_mtth_variables.txt` | `C7952F822164CA6A52DBE3F4D749D7978F49EC82103628AE91897996484150BC` | Source constants found, but the probability adapter discovered no evaluable MTTH surface. |
| AI strategy source | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | `60FCBCCAD8DF110F1E050DC35D33D8EB2C397721567CF6AC4580DF345F444E0F` | No `ai_strategy_factor` surface discovered by the adapter. |
| Focus AI | `common/national_focus/006_independence_wave_focus.txt`; `independence_wave_focus_tree` | `1A0C335DD495D792F5FE713D27D6A3DFABB601824F550A030A4969B43C8C80CA` | 184 focus candidates and 17 required inputs. Supplemental focus sources are `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` (SHA-256 `36EB8E620731A0F5160A22433AA5E5DAF5BC2C85B95055618E94BF0C45A9CFB2`) and `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` (SHA-256 `B233A77CDD8EB1AFDDDE1A7A085CF972DF2A19452BF54583C388A243710399`). |
| Decisions and missions | `common/decisions/006_independence_wave_decisions.txt`; `006_independence_wave_frontier_decisions.txt`; `006_independence_wave_siberian_decisions.txt`; `006_independence_wave_balkan_decisions.txt` | Decision-file hashes were not needed for the bounded continuation; source paths are exact. | Decision candidates: 13. Mission candidates: 64, 23, 88, and 86. These are willingness score races, not click probabilities. |
| Research/doctrine | Event 006 strategy and focus sources, inspected with technology/doctrine adapters | N/A | No Event 006 technology or doctrine weighted surface discovered. |
| Other random/custom pools | Event 006 source scan plus `custom_weighted_pool` adapter | N/A | Only outer, regional, and formable `random_list` surfaces were found. Planner, registry, and outer custom-pool inspections returned zero declared candidates; no complete cadence manifest exists. |

## Fresh mandatory probability inspections

The mandatory first call for this continuation was a read-only `hoi4.probability_inspect` of `common/scripted_effects/006_independence_wave_effects.txt` with adapter `random_list` and `refresh=true`.

Fresh outer receipt: `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=true`; 14 candidates; 14 required inputs; 0 unresolved; `sourceRevision=d7ae194c4905d644b7a4a3a7f2e3c323ddc218c480010722b30e98b286bc1c44`; MCP `sourceHash=4ea923eb3654271e1214a8edad62fdf10e69343b8474c378a0e37ce6b6653e8b`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f4c3255c8c03099d3c65139066002be53137a2953e0f550224d1c6d76bf57d3/8e4ab66f375c1b7b22d1c9b5110bae221a4d98462b7952c26cef84c25590d44e/probability-inspect-4ea923eb3654.json`.

Fresh support-event receipt: `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=false`; 154 candidates; 45 required inputs; 1 unresolved; 0 available candidates; `sourceRevision=a694eeafc3beb5ebe2273e2173d1f455daf8a9b00f2156fcba1ba78ebde8e39a`; MCP `sourceHash=4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/650f5c1145ff2401fcffc86ce307b107fe83a869b8b273a1a3270be6a2056702/d676f91beada017483ee6cedd874c4152bd2a988db859360a1550d161fe30458/probability-inspect-4d7ed5adb1d7.json`.

Fresh calls for `random_list` on `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` and `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`, and `event_option_ai_chance` on `events/006_independence_wave.txt`, returned the exact MCP blocker `INTERNAL_ERROR` with message `Unexpected internal error`, no files scanned, and no artifact. A sequential retry of those three calls did not return within the bounded continuation window and was terminated; this is a service/adapter blocker, not evidence of an empty pool. The prior successful receipts for those same surfaces are retained below and in `006_event6_probability_inventory_2026-09-12.md`.

## Prior probability receipts retained for this audit

The following artifacts are valid read-only evidence from the same Event 006 audit date and are repeated so the parent can reproduce the bounded conclusions without relying on prose summaries.

| Surface or analysis | Receipt, scenario, and classification |
|---|---|
| Outer inspect | Prior `PROBABILITY_SOURCE_INSPECTED`; 14/14 complete; revision `fa97953a5f8a1d617e6a3036bc856fd08628fac7c4b7a75d673cef7c1a4b0442`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f34736c0e9a1a6789647a582ba4a940986fd90712b11c3c27eac62a4b835f480/8ab3ee76d6e63878a45f1d7405ac88db5de0402e43f1a582c4a7ea06fc899a53/probability-inspect-4ea923eb3654.json`. The fresh receipt above has the same MCP source hash but a newer source revision. |
| Nested regional inspect | `poolComplete=false`; 126 candidates; 126 required; 1 unresolved; MCP source hash `17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36d2dc64082e27464e51ad9484644613521cbacbeccb3003ac91b46207bb417b/deb0bffc4d37eac0d6d62dc74693638bbc4bf307b389e3ecf5120a4c4ee7ebb7/probability-inspect-17e35c209602.json`. |
| Formable inspect | `poolComplete=true`; 2 candidates; 2 required; 0 unresolved; MCP source hash `8c18afa88066f345b418685a014396a60188666382391cacfb0ec551cea6ba2f`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/addd397d69bdffa106d3f4e281d07b70622ef3a1f459f552c72e5f74d8c7523f/fc36d10ed76dd96c1b8074e6cc3e86fc0cb998089e39e09f7c746ac36e821e3d/probability-inspect-8c18afa88066.json`. |
| Root event inspect | `poolComplete=false`; 22 candidates; 13 required; 1 unresolved; prior revision `45a979f580e9770f677b6101cd1c36ccd45e88d8e7d9165e916bc9396358ca9e`; MCP source hash `1257ea0e633018078f75a4b22931bd46666d1ed8e72d22f6708262b9ffe5d961`. No current fresh artifact was produced because the fresh call hit `INTERNAL_ERROR`. |
| Support event inspect | Prior revision `563a4604818cab9424face31bbe2109715ecbbac6e57a7fec8cfb99c7b512a4c`; the fresh receipt above supersedes its adapter revision while retaining the same MCP source hash. |
| Outer exact evaluation | Scenario id `E006_ALLOCATOR_LADDER_2026_09_12`; analysis `probability-d8077b81be227d0e4bb5d0d4`; 4 scenarios, 56 rows, 0 unresolved, 24 diagnostics; one-day horizon; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08b1ecab3db1a56a867d0983a3d82c6ff32c72f6b274643e1d3321bc971e3e6e/63a98d26e7ed418b52cc720f09840a44d94768ce214f3f9aa3a0811c7bc8ab6a/probability-d8077b81be227d0e4bb5d0d4.json`. Classification: exact only for the declared synthetic states. |
| Outer rendered ranking | Scenario id `E006_ALLOCATOR_RENDER_LADDER_2026_09_12`; analysis `probability-50819b9b1c89f27bc744633a`; scenario hash `a0453933cba7bccba36393d8b33385ec247324ac8b06362216b0fa85c75de38a`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc6c7c0515448cb16380b61543cfa35e136e50b756e2434ee508e23b07793993/7f2eda60f6f04509fbac24d5e071bfb5fa914c3264e68408b742b1f158696315/probability-50819b9b1c89f27bc744633a.json`; ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af40e393748419ebdc19f683ffdb4654e162e26fddbdd756178ee872952425a5/1214afb2ad217b3eb82a473682b8214c2538810d8d5857c60bdeee9cbe2342be/probability-probability-50819b9b1c89f27bc744633a-ranking.svg`. |
| Outer sensitivity sweep | Scenario id `E006_ALLOCATOR_SENSITIVITY_2026_09_12`; analysis `probability-43e33e7aab169c71ea0b7742`; scenario hash `5e086c30e648a11cd814bad739f60365ec03c993d95bd7f82f11497e5d761a80`; 6 sweep points, 0 unresolved, 11 diagnostics; sensitivity SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5699c282f5d2e479ac5d43de27d41a355a2ecc665f31d6ffc62db01bda6b5b2f/58764e5748d7cc0c9f679ce86d42fab60db8273413caa2f9fbb286171dbf1199/probability-probability-43e33e7aab169c71ea0b7742-sensitivity.svg`. Classification: exact synthetic sensitivity, not campaign balance. |
| Formable rendered analysis | Scenario id `E006_FORMABLE_RENDER_2026_09_12`; analysis `probability-7ef4a69061f0b0b236322bc9`; scenario hash `f5ce2b7c6ee5fa0f83aa2ad8030f7afc8d9d98af8724e31d77c078a711bca88f`; 3 scenarios, 6 rows, 0 unresolved; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ced16085bb33181c568f44e4817c157aedb4c13cef3e63b1bdad2e1a3962b15/fd6cbde2e7c89598431ac34df7f03a884c45df980793c97126e6d3ddd31a3677/probability-7ef4a69061f0b0b236322bc9.json`; ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/062c7494fc2edac55fb318aa78f222ca2316ec9b52de98caaa06ef454dce3d2d/d3b12c2ed0c7f73ed8b609cd341e1ae7331436df2382e4893d7ca9aa80ab2aeb/probability-probability-7ef4a69061f0b0b236322bc9-ranking.svg`. |

## Scenario results and completeness

The exact outer ladder used one-day horizon and explicit synthetic states: uniform, calm with R1=525/R2=175, rising with R1=850/R2=325/R14=150, and all-zero. Uniform normalization was 1/14 for each of 14 entries; calm was 3/4 for R1 and 1/4 for R2; rising was 34/53 for R1, 13/53 for R2, and 6/53 for R14; all-zero returned `PROBABILITY_ALL_ELIGIBLE_VALUES_ZERO` with `conditional_probability=null`. These are exact declared-fixture results, not campaign selection probabilities.

The formable analysis was exact only for its declared two-candidate fixtures: balanced success/failure was 1/2 and 1/2, while one-sided fixtures were deterministic one/zero branches. It does not prove the upstream formable gates or campaign frequency.

Typed-empty evaluations for incomplete surfaces were deliberately retained as bounded diagnostics, not numeric balance claims: nested 126 list `E006_NESTED_126_TYPED_EMPTY_2026_09_12` had 126 candidates and 127 unresolved; root options `E006_ROOT_EVENT_TYPED_EMPTY_2026_09_12` had 22 candidates and 24 unresolved; support options `E006_SUPPORT_EVENTS_TYPED_EMPTY_2026_09_12` had 154 candidates and 6,876 unresolved; core decisions `E006_CORE_DECISIONS_TYPED_EMPTY_2026_09_12` had 13 candidates and 11,720 unresolved; core missions `E006_CORE_MISSIONS_TYPED_EMPTY_2026_09_12` had 64 candidates and 1,849 unresolved; frontier missions had 23 candidates and 664 unresolved; Siberian missions had 88 candidates and 2,482 unresolved; Balkan missions had 86 candidates and 1,124 unresolved; and focus AI `E006_FOCUS_AI_TYPED_EMPTY_2026_09_12` had 184 candidates and 3,413 unresolved. Full JSON artifact URIs for each typed fixture are preserved in `006_event6_probability_inventory_2026-09-12.md`.

Candidate-pool completeness is therefore: outer complete for the inspected source; formable complete only for the two-entry list; nested incomplete; root/support event options incomplete; decisions/missions incomplete; focus incomplete; AI strategy, MTTH, technology, and doctrine surfaces absent from the adapter; and custom pools incomplete/undeclared. External-factor completeness is incomplete for all campaign-facing races because country/anchor/host existence and control, reservations, content attestation, prior package/region/host arrays, confidence, chaos band, targets, capacity, Event 005 collision state, attempt caps, and terminal/cooldown state are not fully typed in the adapter scenario.

## Structural MCP evidence

The prior read-only `hoi4.event_inspect` was `EVENT_INSPECTED_PARTIAL`, revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, with deferred workspace helper/lifecycle analysis. The event overview render layout hash was `3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d`.

The prior read-only `hoi4.focus_inspect` returned revision `6427270db259cb431d9d0d7e34ca02e4b0b9fce49c4504b334e90aa8f7501895`, 184 focuses, 196 connectors, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, and one non-blocking long-connector warning. The matching focus render returned the same layout hash. Structural evidence confirms source topology only and does not replace probability evidence.

## Findings by classification

Exact: outer 14-entry normalization under the four declared synthetic states and formable success/failure normalization under the three declared fixtures.

Bounded: nested package pool, root/support event options, decisions, missions, and focus AI. The MCP found candidates but withheld campaign-normalized probabilities because the complete runtime pools and typed gate inputs are absent.

Score-only: package allocation score terms, decision and mission `ai_will_do`, focus `ai_will_do`, incomplete event-option traces, and source MTTH constants. A score race is not a click probability, and a package score is not probability-proportional sampling evidence.

Unresolved: campaign dominance, starvation, rank reversal, repetition, timing drift, safe resource behavior, cooldown/recovery/removal/reset/terminal sequencing, and exact MTTH timing. Positive source weights on route-incompatible or dead candidates cannot be classified as safe or unsafe without typed validity gates.

## Skipped analyses and exact blockers

`hoi4.probability_simulate` was skipped because no explicit uncertain input distributions, correlations, or seed were authorized for the missing campaign state.

`hoi4.probability_sequence` was skipped because no complete custom-pool manifest declares cadence, cooldown, recovery, cap, removal, reset, and terminal states.

`hoi4.probability_compare` was skipped because this is a read-only baseline continuation with no accepted before/after source or candidate patch. A same-source comparison would not establish a tuning effect.

The fresh regional, formable, and root inspections returned `INTERNAL_ERROR` / `Unexpected internal error` with no artifact, and the bounded retries stalled. The MCP service therefore did not provide a fresh receipt for those three surfaces in this continuation. This is recorded as an adapter/service blocker; no numeric claim is substituted.

An outer evaluation attempt using scenario id `E006_CONTINUATION_EMPTY_2026_09_12` was interrupted after the MCP returned an empty artifact list without a usable structured status, so it is not treated as evidence. The prior fully receipted outer evaluation, sweep, and render listed above remain the only numeric evidence.

## Recommended next owner action

Before any weight patch, provide a typed manifest for all 126 package candidates and rerun the same named outer, nested, and formable scenarios against the fresh outer revision `d7ae194c4905d644b7a4a3a7f2e3c323ddc218c480010722b30e98b286bc1c44`. The manifest should include country/anchor/host existence and control, reservations, content attestation, prior package/region/host arrays, confidence, chaos band, target count, capacity, Event 005 collision state, attempt cap, pool-exhaustion fallback, cooldown/removal/reset, and terminal states.

Then provide complete visible candidate pools and gate state for root/support events, decisions/missions, and focus AI, and rerun `probability_evaluate`, `probability_sweep`, and `probability_render` with the same scenario IDs where applicable. After an owner-applied source change, run `probability_compare` with identical scenario hashes and record rank reversals, starvation, dominance, timing, and repetition outcomes. Do not promote the exact synthetic ratios above into campaign balance targets.

Next-owner recommendation: the parent implementation owner should resolve adapter/service failures and supply typed scenario manifests; the probability auditor should then rerun the receipts before any AI-weight or timing change. This audit remains HOLD/PARTIAL and does not authorize a source patch.
