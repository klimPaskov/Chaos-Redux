# Event 006 probability inventory handoff — 2026-09-12

Status: read-only weighted-logic audit. No gameplay, AI, event, focus, decision, mission, technology, doctrine, localisation, or tuning files were changed. This handoff does not claim balance or completion.

## Contract and references

Scope: Event 006 Independence Wave outer allocator, nested 126-package pool, formable Congress random list, root/support event ai_chance, decisions/missions, focus AI, AI strategy factors, MTTH, random lists, and declared custom pools.

Read before audit: AGENTS.md; .agents/skills/chaos-redux-subagents/SKILL.md; .agents/skills/chaos-redux-events/SKILL.md; .agents/skills/chaos-redux-mtth/SKILL.md; .agents/skills/chaos-redux-decisions-missions/SKILL.md; .agents/skills/chaos-redux-focus-trees/SKILL.md; .agents/skills/chaos-redux-event-planning/SKILL.md; docs/specs/006_independence_wave_specs/; docs/plans/006_independence_wave_plans/006_source_of_truth_map.md; current Event 006 weighted handoffs; the required offline Paradox wiki pages; and relevant vanilla documentation under C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/.

The HOI4 MCP workspace was mod_chaos_redux_ea3b2d67c2c0. The first weighted call was the mandatory read-only probability_inspect for common/scripted_effects/006_independence_wave_effects.txt.

## Source inventory

| Surface | Source and identifiers | Inventory |
|---|---|---|
| Outer allocator | common/scripted_effects/006_independence_wave_effects.txt; independence_wave_select_one_automatic_package; lines 3563–3590 | One random_list with fourteen regional entries and an explicit zero-total/pool-exhaustion path. |
| Nested regional pool | common/scripted_effects/006_independence_wave_package_region_effects_registry.txt; regional selectors 01–14 | Fourteen lists with 126 package entries. Regional counts R1–R14: 9, 9, 8, 8, 12, 12, 5, 3, 7, 7, 5, 13, 19, 9. |
| Package score | common/scripted_effects/006_independence_wave_package_planner_effects.txt; independence_wave_calculate_candidate_allocation_weight; lines 585–803 | Attestation and earliest-chaos-band gates precede base score. Source terms include base 100, sponsored +100, registered +25, new region +30, new host +20, prior package −80, prior region −25, prior host −20, low-chaos signature −35, high-chaos +45, evolution terms, rarity factor, and minimum floor 1. Score is not probability. |
| Formable Congress | common/scripted_effects/006_independence_wave_formable_registry_effects.txt; independence_wave_formable_resolve_congress; around lines 2481–2490 | Complete two-entry random_list: success and failure, with failure fallback. |
| Event options | events/006_independence_wave.txt and events/006_independence_wave_support_events.txt | Root file adapter discovery: 22 candidates and 13 required inputs. Support file: 154 candidates and 45 required inputs. Root chaosx.nr6.1 is hidden/immediate and has no player option race. |
| Decisions/missions | common/decisions/006_independence_wave_decisions.txt; 006_independence_wave_frontier_decisions.txt; 006_independence_wave_siberian_decisions.txt; 006_independence_wave_balkan_decisions.txt | Decision candidates: 13. Mission candidates: 64, 23, 88, and 86. ai_will_do is a willingness score race, not a click probability. |
| Focus AI | common/national_focus/006_independence_wave_focus.txt; independence_wave_focus_tree | 184 focus candidates and 17 required inputs. |
| Strategy/MTTH/research/doctrine | common/ai_strategy/006_independence_wave_ai_strategy_registry.txt; common/mtth/chaosx_mtth_variables.txt | No ai_strategy_factor, technology_ai_will_do, doctrine_ai_will_do, or event MTTH adapter surface discovered. MTTH variable definition remains source-only. |
| Other random lists | Event 006 source scan | Only outer, regional, and formable random_list surfaces found. The scenario registry is deterministic ranking/navigation, not a probability-proportional pool. |

## Inspect receipts

Outer random_list inspect: PROBABILITY_SOURCE_INSPECTED; poolComplete=true; 14 candidates; 14 required; 0 unresolved; revision fa97953a5f8a1d617e6a3036bc856fd08628fac7c4b7a75d673cef7c1a4b0442; source hash 4ea923eb3654271e1214a8edad62fdf10e69343b8474c378a0e37ce6b6653e8b; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f34736c0e9a1a6789647a582ba4a940986fd90712b11c3c27eac62a4b835f480/8ab3ee76d6e63878a45f1d7405ac88db5de0402e43f1a582c4a7ea06fc899a53/probability-inspect-4ea923eb3654.json.

Nested regional random_list inspect: PROBABILITY_SOURCE_INSPECTED; poolComplete=false; 126 candidates; 126 required; 1 unresolved; source hash 17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36d2dc64082e27464e51ad9484644613521cbacbeccb3003ac91b46207bb417b/deb0bffc4d37eac0d6d62dc74693638bbc4bf307b389e3ecf5120a4c4ee7ebb7/probability-inspect-17e35c209602.json.

Formable random_list inspect: PROBABILITY_SOURCE_INSPECTED; poolComplete=true; 2 candidates; 2 required; 0 unresolved; source hash 8c18afa88066f345b418685a014396a60188666382391cacfb0ec551cea6ba2f; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/addd397d69bdffa106d3f4e281d07b70622ef3a1f459f552c72e5f74d8c7523f/fc36d10ed76dd96c1b8074e6cc3e86fc0cb998089e39e09f7c746ac36e821e3d/probability-inspect-8c18afa88066.json.

Root event-option inspect: PROBABILITY_SOURCE_INSPECTED; poolComplete=false; 22 candidates; 13 required; 1 unresolved; revision 45a979f580e9770f677b6101cd1c36ccd45e88d8e7d9165e916bc9396358ca9e; source hash 1257ea0e633018078f75a4b22931bd46666d1ed8e72d22f6708262b9ffe5d961.

Support event-option inspect: poolComplete=false; 154 candidates; 45 required; 1 unresolved; revision 563a4604818cab9424face31bbe2109715ecbbac6e57a7fec8cfb99c7b512a4c; source hash 4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437.

Core decision inspect: poolComplete=false; 13 candidates; 88 required; 0 unresolved; revision 3e94f62d03a42a9ca0f1e85802fc5abe6aad0d2b33314b2e98df670225c625fe; source hash 7e718e475504f643c709f67b439e13dd28701f2e07896605c929848121891dfd. Core mission inspect on the same source: poolComplete=false; 64 candidates; 52 required; 0 unresolved.

Frontier, Siberian, and Balkan mission inspect counts: 23/19, 88/19, and 86/17 candidates/required inputs respectively; all poolComplete=false and unresolved=0.

Focus inspect: poolComplete=false; 184 candidates; 17 required; 0 unresolved; revision 84bdede92c3698755546b635a1b6b374dffe635e08e390084f90521ea2c09544; source hash d4970a31fc37dc20a72a88f0424eb21920d2727318674b01b82eba64f1ee576b.

AI strategy inspect: PROBABILITY_SOURCE_DISCOVERED; discoveryReason=no_weighted_surfaces; candidates=0; requiredInputs=0; unresolved=0; revision 8fa4e8c7d2d3c8a243c887dee8889af46a27077f5d0b49052d2e0a1d29271c03; source hash b84ee2ca17f45793196641dd0d383779fb2e36ab29da6a1ee2d90912ec82deb6.

MTTH inspect: PROBABILITY_SOURCE_DISCOVERED; discoveryReason=no_weighted_surfaces; candidates=0; requiredInputs=0; unresolved=0; source hash 6bacd42706fe373dd237216ee650ef89ab40ebde5500969c167563836c16b5b4.

Technology and doctrine inspect on the Event 006 strategy source both returned no_weighted_surfaces with candidates=0 and requiredInputs=0.

custom_weighted_pool inspect for planner, registry, and outer effects returned zero declared candidates and poolComplete=false. Planner evaluate returned PROBABILITY_SURFACE_EMPTY with candidatePool=[] and availableAdapters=[].

## Exact random-list evaluations

Outer E006_ALLOCATOR_LADDER_2026_09_12 used one-day horizon and explicit states for uniform, calm R1=525/R2=175, rising R1=850/R2=325/R14=150, and all-zero regions.

Result: PROBABILITY_ANALYZED; analysis probability-d8077b81be227d0e4bb5d0d4; four scenarios; 56 rows; 0 unresolved; 24 diagnostics; source revision fa97953a5f8a1d617e6a3036bc856fd08628fac7c4b7a75d673cef7c1a4b0442; source hash 4ea923eb3654271e1214a8edad62fdf10e69343b8474c378a0e37ce6b6653e8b.

JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08b1ecab3db1a56a867d0983a3d82c6ff32c72f6b274643e1d3321bc971e3e6e/63a98d26e7ed418b52cc720f09840a44d94768ce214f3f9aa3a0811c7bc8ab6a/probability-d8077b81be227d0e4bb5d0d4.json.

Exact synthetic normalization: uniform gives 1/14 each; calm gives 3/4 and 1/4 for R1/R2; rising gives 34/53, 13/53, and 6/53 for R1/R2/R14. All-zero emits PROBABILITY_ALL_ELIGIBLE_VALUES_ZERO with conditional_probability=null. These are exact only for declared synthetic states, not campaign probabilities.

Rendered two-scenario outer contract E006_ALLOCATOR_RENDER_LADDER_2026_09_12: analysis probability-50819b9b1c89f27bc744633a; scenario hash a0453933cba7bccba36393d8b33385ec247324ac8b06362216b0fa85c75de38a.

Rendered outer JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc6c7c0515448cb16380b61543cfa35e136e50b756e2434ee508e23b07793993/7f2eda60f6f04509fbac24d5e071bfb5fa914c3264e68408b742b1f158696315/probability-50819b9b1c89f27bc744633a.json.

Rendered ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af40e393748419ebdc19f683ffdb4654e162e26fddbdd756178ee872952425a5/1214afb2ad217b3eb82a473682b8214c2538810d8d5857c60bdeee9cbe2342be/probability-probability-50819b9b1c89f27bc744633a-ranking.svg.

Outer sensitivity sweep E006_ALLOCATOR_SENSITIVITY_2026_09_12 completed as probability-43e33e7aab169c71ea0b7742, scenario hash 5e086c30e648a11cd814bad739f60365ec03c993d95bd7f82f11497e5d761a80, six sweep points, zero unresolved, and 11 diagnostics. Sensitivity SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5699c282f5d2e479ac5d43de27d41a355a2ecc665f31d6ffc62db01bda6b5b2f/58764e5748d7cc0c9f679ce86d42fab60db8273413caa2f9fbb286171dbf1199/probability-probability-43e33e7aab169c71ea0b7742-sensitivity.svg.

Formable E006_FORMABLE_RENDER_2026_09_12 completed as probability-7ef4a69061f0b0b236322bc9, source hash 8c18afa88066f345b418685a014396a60188666382391cacfb0ec551cea6ba2f, scenario hash f5ce2b7c6ee5fa0f83aa2ad8030f7afc8d9d98af8724e31d77c078a711bca88f, three scenarios, six rows, and 0 unresolved. Balanced gives 1/2 and 1/2; one-sided fixtures give deterministic one/zero branches.

Formable rendered JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ced16085bb33181c568f44e4817c157aedb4c13cef3e63b1bdad2e1a3962b15/fd6cbde2e7c89598431ac34df7f03a884c45df980793c97126e6d3ddd31a3677/probability-7ef4a69061f0b0b236322bc9.json.

Formable rendered ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/062c7494fc2edac55fb318aa78f222ca2316ec9b52de98caaa06ef454dce3d2d/d3b12c2ed0c7f73ed8b609cd341e1ae7331436df2382e4893d7ca9aa80ab2aeb/probability-probability-7ef4a69061f0b0b236322bc9-ranking.svg.

## Partial typed-fixture evaluations

All of these used state={} and therefore remain bounded or unresolved.

Nested 126 list E006_NESTED_126_TYPED_EMPTY_2026_09_12: probability-e2d2c4ce204acd93c105cb71; scenario hash f8b868935bdd74d1ed5eb841865ecfc4eaf8149c7dbd8d5be4e2209527202448; 126 candidates; 127 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80cd36106cee01931747d69f26f8906ed6f4779539ffd30b3f8c3c5051abf8d4/da8f579e4c760fca4949e5e64de1d10bc98b01ae3c3da73af074b54893e5447e/probability-e2d2c4ce204acd93c105cb71.json.

Root event options E006_ROOT_EVENT_TYPED_EMPTY_2026_09_12: probability-b81dc675d0a639a11cfd71d9; scenario hash f439d099d909503b2e9e092660b534a479b4bae4ea8bfd6bdb5a7f5d3826bb78; 22 candidates; 24 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41430f27756b98dace6e849445dfc90b89d57949e40705aacabc9d883b691f7b/4e3f662e5bec59feeaa7152397482d94d17860f5ec47ce3266eda77253572701/probability-b81dc675d0a639a11cfd71d9.json.

Support event options E006_SUPPORT_EVENTS_TYPED_EMPTY_2026_09_12: probability-a21dadaa45aba87136b89460; scenario hash 46a0734a3fcf4cbb19a18da61a7d2d6064a95129ed4be3e19cab1d6fb7d32174; 154 candidates; 6,876 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5b0d581c68325ef5d7df2a9976d7cd1315c542eba2df4f0e1f753e641be120c/265531bcc4d1a0f9c5b2cea352cf11b5d75959330088f74db82b5353381a6870/probability-a21dadaa45aba87136b89460.json.

Core decisions E006_CORE_DECISIONS_TYPED_EMPTY_2026_09_12: probability-bc842c8c3b5243124392fb1a; scenario hash 65e18d232801c141dcc228ac3a787264d3f38369370e60a250f232b0afacb5dd; 13 candidates; 11,720 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d68f60837dd1fcbcfe63da398abb3f8ef808282669b82aff6a532b33b70691e9/9da064a3079d1ede657b7157a4742e785a300949150f3b6dda988ddc0c313719/probability-bc842c8c3b5243124392fb1a.json.

Core missions E006_CORE_MISSIONS_TYPED_EMPTY_2026_09_12: probability-a0e5bffafb1c038ba0c2052c; scenario hash 7a768667940f4d904a3e1ea6ad4a7e21653c878c0c1288563b6199715038b082; 64 candidates; 1,849 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce41c02441670d77fc3f3408769f9f24c9cbfed591ebda1e6d04940aec269498/32554def6bded0ad6bb679042608ac058628e7379c0aa9bed489e4dbdcdf0040/probability-a0e5bffafb1c038ba0c2052c.json.

Frontier missions E006_FRONTIER_MISSIONS_TYPED_EMPTY_2026_09_12: probability-8286af9c711d086b5ea70683; scenario hash df60f2122c279336c41352cb72c3f0d630ad73f99b59ee6c4481776a5366b29c; 23 candidates; 664 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2819efeb5234e4027c0f226616a281b7ea3ec4ed293d5d98dffcf20ec66510d6/b482544a2fe1d180df630b70672d28969e1e8b35e19516da444fa596c20c79de/probability-8286af9c711d086b5ea70683.json.

Siberian missions E006_SIBERIAN_MISSIONS_TYPED_EMPTY_2026_09_12: probability-5201e37642af85a1127bbb4d; scenario hash e6730184ea9aaa7f246aaa203962af94dee759fe1a53b4382e38ca39326881f1; 88 candidates; 2,482 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e157a87b4d4d9a7cf78c31a81c1941ca3d48e788a95e0662a92d7e4327b90af2/a34947057e80e0bb3da7bdd77db613938d0036ef7bf68e64e724c3348dde1118/probability-5201e37642af85a1127bbb4d.json.

Balkan missions E006_BALKAN_MISSIONS_TYPED_EMPTY_2026_09_12: probability-d3effe8bbb85f8053ee75da8; scenario hash 1fc625102e11ce0089302c289a1c29ac1c638807bddc69ea8c3156ea71f20c5c; 86 candidates; 1,124 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd69df92c81cb14605f74f2a3386d4c2200fa4465c18a3f5ce897425fa63bbc3/da2316f1e64e66b1e8a9dc58316c5df32a959fda58cee14cdf4ddc500472d75c/probability-d3effe8bbb85f8053ee75da8.json.

Focus AI E006_FOCUS_AI_TYPED_EMPTY_2026_09_12: probability-62935827f8c3fd0488bdd388; scenario hash 42995cef6618aff225f0dd21fb5c372857a9f923a306b2b48cd106e94aebb14f; 184 candidates; 3,413 unresolved. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c080565868b942ec4e77f10843aeb7e5fcb20e4bc9cb7184a20619490f843c57/bcc92141baeb4d54f6ab1fd93736da4af87406a722cac8444b4a67bd3e262ded/probability-62935827f8c3fd0488bdd388.json.

## Constants and structural evidence

Decision score constants are blocked=0, very_low=2, low=5, standard=10, high=25, urgent=100, with factors 0.5, 2, and 5 at common/script_constants/006_independence_wave_constants_registry.txt lines 1254–1269.

Focus constants are none=0, cautious=5, standard=10, high=25, urgent=100, preferred factor 2, strong-preference factor 4, prerequisite boost 1.5, avoid factor 0.1, and war-avoid factor 0.25 at lines 1743–1762.

Evolution MTTH constants are base 300 days, minimum 90, maximum 720, chaos factors 1.15, 1, 0.85, 0.7, 0.55, and thin/dense network factors 1.25/0.8 at lines 1403–1418. The event MTTH adapter returned no weighted surface for the variable-definition file, so no timing distribution is claimed.

Event inspect returned EVENT_INSPECTED_PARTIAL, revision 4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d, graph hash 24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819, with deferred workspace helper/lifecycle analysis. Event overview render returned layout hash 3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d.

Focus inspect returned revision 6427270db259cb431d9d0d7e34ca02e4b0b9fce49c4504b334e90aa8f7501895, 184 focuses, 196 connectors, layout hash a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7, and one non-blocking long-connector warning. Focus render returned the same layout hash.

## Findings, next action, and skips

Exact: outer 14-entry and formable two-entry normalization under declared synthetic states.

Bounded/partial: nested 126 list, root/support ai_chance, decisions, missions, and focus AI. MCP found source candidates but withheld normalized probabilities because complete runtime pools and typed gate inputs are absent.

Score-only: package allocation modifiers, incomplete ai_chance traces, ai_will_do, focus ai_will_do, and source MTTH constants.

Unresolved: campaign dominance, starvation, rank reversal, repetition, cooldown/recovery/reset/terminal sequence behavior, unsafe snowballing, and exact MTTH timing.

Next safe owner action: provide a typed manifest for all 126 package candidates and rerun the same named scenarios before any weight patch. Include country/anchor/host existence and control, reservations, content attestation, prior package/region/host arrays, confidence, chaos band, target count, capacity, Event 005 collision state, attempt cap, pool-exhaustion fallback, cooldown/removal/reset, and terminal states. Then provide complete visible pools and gate state for root/support events, decisions/missions, and focus AI and rerun the same scenario IDs.

probability_simulate was skipped because no explicit uncertain distributions, correlations, or seed were declared.

probability_sequence was skipped because no complete custom-pool cadence, cooldown, recovery, cap, removal, reset, and terminal-state manifest exists.

probability_compare was skipped because this read-only audit has no accepted before/after source or candidate patch. A same-source comparison would not be meaningful.

No weight patch, gameplay change, fallback implementation, or balance claim was made. No live HOI4 execution was performed.

