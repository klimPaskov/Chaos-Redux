# Event 006 final AI and probability audit (current)

Date: 2026-08-06.

Audit owner: `chaosx_ai_probability_auditor`.

Scope: read-only refresh of the Event 006 allocator, crisis mission, shared decision and mission, generic-focus AI, Karelia/Crimea package AI, AI-strategy, and SCN-008 scenario-selection surfaces after the current source revision and ordinary super-event IDs 23/24 were confirmed by the parent. No gameplay, AI, event, focus, decision, mission, strategy, localisation, asset, spreadsheet, or runtime file was changed by this audit.

## Verdict

Event 006 remains **HOLD / PARTIAL** for weighted-AI completion.

The allocator and Region 04 random-list pools are structurally complete, but their dynamic world-state weights are not computable from the supplied typed scenarios, so no exact package or region selection probability is claimed.

The decision, mission, focus, and crisis analyses are bounded score traces only because the candidate pool and state-dependent eligibility are incomplete; they are not click probabilities, timing distributions, or live AI behavior proofs.

No current MCP evidence proves dominance, starvation, rank reversal, repetition, timing safety, capacity safety, or save/load persistence.

## Required references

The audit read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-planning/SKILL.md`, and the relevant Event 006 specifications and prior handoffs.

The offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding were consulted alongside the relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

The whole-event source of truth remains `docs/events/006_independence_wave/overview.md` and `docs/events/006_independence_wave/systems/triggerable_scenario.md`.

## MCP provenance

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Current source revision for the refreshed surfaces: `eb05663f2b2ff2c07bf2bf6bfab4a70536737957a92a0537fa365d3ca3cb2eb5`.

`hoi4.probability_inspect` was run first for every weighted surface that exposed an installed adapter.

`hoi4.probability_evaluate` was then run for the named allocator, shared decision, shared mission, crisis mission, and generic-focus scenario sets.

Evaluation outputs requested JSON plus ranking and unresolved views; the returned ranking, matrix, and unresolved resources are the required rendered evidence where available.

No sweep, simulation, or sequence run was performed because the required dynamic state, uncertainty declarations, cadence, and terminal-state contracts were not available; running them would create false precision.

## Fresh source inspections

| Surface and adapter | Source and hash | MCP result | Artifact |
| --- | --- | --- | --- |
| Outer package allocator `random_list` | `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`; `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83` | `PROBABILITY_SOURCE_INSPECTED`; 14 candidates; 14 required inputs; `poolComplete=true`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b54f1e1f664f58ef125741a05de2403773909d43bd1abb34164d9ed5deaa61a/048d371d596771d5d6a49943f779a764b99b4c9ee6cff5030f2dafea12e21978/probability-inspect-bc6f7ff8598d.json` |
| Outer allocator `custom_weighted_pool` probe | same source and hash as outer allocator; adapter-specific source revision `49538c9f2d17b015a2e1587a4bcc67adb6c2e57a74a584ded08a791fdd3464d4` | `PROBABILITY_SOURCE_INSPECTED`; 0 custom-pool candidates; 0 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/539234c3741b94363923a3f17b6f7faba271dc8a093d27dde358a61787d5a61a/2b5a2bb2d6e56a71af60144c2c23a9ddb0a8d47c0a1df67428df790214ac4d44/probability-inspect-bc6f7ff8598d.json` |
| Region 04 package allocator `random_list` | `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt`; `e8f1792fa6b12a426551789a259fb67b570cb5194059ccc17e433ade122af2eb` | `PROBABILITY_SOURCE_INSPECTED`; 8 candidates; 8 required inputs; `poolComplete=true`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86e99056f9e18996c708a18ad6cfe0e03878ff679f086b43bf5826459c39c8fd/fe9e9a7e0250e2b6075a9c8b20630d61fa8bbe47d069cfea0a73f1855d3bd60c/probability-inspect-e8f1792fa6b1.json` |
| Region 04 `custom_weighted_pool` probe | same source and hash as Region 04 allocator; adapter-specific source revision `49538c9f2d17b015a2e1587a4bcc67adb6c2e57a74a584ded08a791fdd3464d4` | `PROBABILITY_SOURCE_INSPECTED`; 0 custom-pool candidates; 0 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/817c085679076d0237d35f9331618106b7890bbd5bb9440182f9e25bd9e1e733/e6b590a0625cef1316af25d6226627c1d8a595c4adb9d3cae0a8a45029d9e22c/probability-inspect-e8f1792fa6b1.json` |
| Shared decisions `decision_ai_will_do` | `common/decisions/006_independence_wave_decisions.txt`; `f84a0e082f6a8b5c518eb769478676e6b78bc23157a39b0303f9947b729aa583` | `PROBABILITY_SOURCE_INSPECTED`; 10 decision blocks; 61 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b89cde389fbe5258215278312a740c9d59c96bf546cb7c255b5e949fb8d9272e/cc307c272b6c3dd1bec83caf0c1dc33632b7dfcff828b9454fdc4e1a0a5aca8c/probability-inspect-f84a0e082f6a.json` |
| Shared missions `mission_ai_will_do` | same source and hash as shared decisions | `PROBABILITY_SOURCE_INSPECTED`; 54 mission blocks; 38 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6d072cfc356bdb7096c61d56741b8c4cb996969ae7ab73fca8abe3b342b1b80/948e3df8d8651f7f64baf60b5939df7ace35c5f64f5265089efed317138d5a6b/probability-inspect-f84a0e082f6a.json` |
| Crisis decisions `decision_ai_will_do` | `common/decisions/006_independence_wave_crisis_decisions.txt` | `PROBABILITY_SURFACE_EMPTY`; exact blocker: `No weighted blocks matched this request`; this file exposes a mission, not a decision AI block | None |
| Crisis mission `mission_ai_will_do` | same crisis source; `da54a4d80e283031be0c9e42fb95fb69d09881ee9715b9cf4ffd4a3ac0b562c0` | `PROBABILITY_SOURCE_INSPECTED`; 1 mission candidate; 7 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b01652711ed678f07435e0742b9ecc8c7e675be643fa56784cd05b37cc15850c/f61695a16175aaf98b7d6d2971609db498a37245f38194c1bfcf441451f6babf/probability-inspect-da54a4d80e28.json` |
| Generic focus AI `national_focus_ai_will_do` | `common/national_focus/006_independence_wave_focus.txt`; `cea5fad03a09ed6b8da5af791b34f3c92b94d52ea38ce3159310ab02319272e8` | `PROBABILITY_SOURCE_INSPECTED`; 184 focus candidates; 15 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb19d588a83287edb3746eda8e9aeeea659abe33c1ef2f22009c2ba86249d755/24573ee47ccf5123d0076bc1505101f96ec6b87e4daa4f273a1e6dd394ecf931/probability-inspect-cea5fad03a09.json` |
| Generic strategy `ai_strategy_factor` | `common/ai_strategy/006_independence_wave_generic.txt` | `PROBABILITY_SURFACE_EMPTY`; exact blocker: `No weighted blocks matched this request` | None |
| SCN-008 navigation `decision_ai_will_do` | `common/decisions/006_independence_wave_scenario_decisions.txt`; `fcd8a24fbe89d3511d695a873797c426e8bce81f77179b4b6b392e0b0c2a58f7` | `PROBABILITY_SOURCE_INSPECTED`; 3 navigation decisions; 1 required input; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/112f4b1e449388b0b457049e4f82e099da86f079a7d2d41370a54a831303f7b0/add964af81e64495a31d33c8cbfa952e9405ea62b424321a48414937b2df8d20/probability-inspect-fcd8a24fbe89.json` |
| KAR/CRI decisions `decision_ai_will_do` | `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`; `e5af5906af8821ee07434e025b363309d87e94ca103be95fd7b75ad27d6c4abb` | `PROBABILITY_SOURCE_INSPECTED`; 2 recognized decision candidates; 12 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8fbf4efad0f958f4784816a4e1a3e0fe5ab209a48f65cd13db9dce364fba37f/46b3d52ff18c5d0fe5072b76ef3e8faa7a9901965336dffea9322a9bba23127c/probability-inspect-e5af5906af88.json` |
| KAR/CRI missions `mission_ai_will_do` | same source and hash as KAR/CRI decisions | `PROBABILITY_SOURCE_INSPECTED`; 20 recognized mission candidates; 14 required inputs; `poolComplete=false`; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9eb2a83f7c4edc42df7124ecd1ddcf64334c106f31578ce6a7ef962f43666f53/8643363b436e7a78ae64606ed225c36f888f1fd74056cc5d904150f4203c2969/probability-inspect-e5af5906af88.json` |
| KAR/CRI strategy `ai_strategy_factor` | `common/ai_strategy/006_independence_wave_karelia_crimea.txt` | `PROBABILITY_SURFACE_EMPTY`; exact blocker: `No weighted blocks matched this request` | None |

The crisis inspect artifact URI above is `b01652711ed678f07435e0742b9ecc8c7e675be643fa56784cd05b37cc15850c/f61695a16175aaf98b7d6d2971609db498a37245f38194c1bfcf441451f6babf`; the MCP resource name is `probability-inspect-da54a4d80e28.json`.

## Named scenario evaluation evidence

### Outer allocator

Scenario set: `E6_ALLOCATOR_REQUIRED_SCENARIOS_CURRENT` with `R04_ALL_OPEN`, `R04_KAR_BLOCKED`, `R04_CRI_BLOCKED`, `R04_BOTH_OPEN_LOW_CAPACITY`, and `CAPACITY_20_WITNESS`.

The supplied state objects were empty records, so package attestation, host and anchor reservation, capacity, ledgers, opening confidence, prior-package penalties, and Event 005 collision state were not supplied.

Evaluation: analysis ID `probability-7022cc688d861641dc62f68a`, scenario hash `ddcea1f98dc935a96ee14b2854526e11e62b915fa438c94e8c3245cd320fdcf5`, 5 scenarios, 70 candidate rows, 14 unresolved items, 0 diagnostics, classification `partial/unresolved`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e619c64dd41a79e92e50de152f3f1961922f975804f21559b7173ba160c89007/dab3a5bed381949ddf1b644b6859f6491515c788ed76cdabe00add0859f169cc/probability-7022cc688d861641dc62f68a.json`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16bc8af109817ccaae8640360a2f9e5326bead388b3f2d92cc25bfd4eda663f7/20b407c4c9e776a158a43581c7e47e0e3720a979f1b45cfde11ad911609f159f/probability-probability-7022cc688d861641dc62f68a-ranking.svg`.

Rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41ed57dff8318b64a08cb7ada90f0d404b9c3ede173e3bf1edc1c6af12ad8929/934143572e2cfe2ee1ac29dbb1d9751001d7fb005ba37d2a021c5c89c9fb6aca/probability-probability-7022cc688d861641dc62f68a-matrix.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/b8a9afff88893e346528e8ce17bee60af35da352d7ee6d9c6748f0060558f7de/probability-probability-7022cc688d861641dc62f68a-unresolved.svg`.

Classification: structural pool completeness is **exact**, but normalized region/package probabilities and dominance/starvation claims are **unresolved**.

### Shared decision AI

Scenario set: `E6_SHARED_DECISION_SCENARIOS_CURRENT_2026_08_06` with `E6_SHARED_OPEN_CALM`, `E6_SHARED_HOST_CRISIS`, `E6_SHARED_ROUTE_LOCKED`, and `E6_SHARED_NO_VALID_TARGET`.

The empty state records do not provide route flags, targets, hosts, reservations, package identity, ledgers, costs, or external modifiers.

Evaluation: analysis ID `probability-9f13e191d036a7047654e3ec`, scenario hash `1df471de297c267f3cc488f1a23f6df8922b8a8a3bfb2af5ccd10a46c2ec6a1a`, 4 scenarios, 40 candidate rows, 1,990 unresolved items, 8 diagnostics, classification `partial/bounded score-only`.

The 8 diagnostics are unsatisfied modifier notices for `independence_wave_accept_arms_limit_recognition`, `independence_wave_accept_limited_claims`, `independence_wave_adopt_charter_pillar`, `independence_wave_proclaim_military_union`, `independence_wave_raise_emergency_units`, `independence_wave_recognize_new_independence_wave_country`, and `independence_wave_sponsor_member_coup` under empty-state coverage; they are not proof that those blocks are dead in a typed game state.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b79fb0dca7ef1671c8fadac953e452ce0ebd129ef9a958fbcca96e1dacbbb1b/35b5cb5c903a4e7e05b9d1cd3c528c6b334c99642a2f5a8214e4b64f531b7062/probability-9f13e191d036a7047654e3ec.json`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80fe9da3b07673f9b8b85e216ff7a20093a3ce352f25972754740c9c9e1f2713/7dc27aecc4f2cf5c58e1a71d85db1373aca3348f6a4119905bd8a6feb94daa85/probability-probability-9f13e191d036a7047654e3ec-ranking.svg`.

Rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4305271e8306f47b1c6c796cd312f8b351bfbd11520f7dbc5f7af84249b38132/8e864e07170b7a6737d2e4fe54aafdfb8ce69346680ee667fc161b318218e376/probability-probability-9f13e191d036a7047654e3ec-matrix.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d28dad62fd282de3f1b6c36db8df83546ab934cd4abdf82790866fbe6296d50/ebecc47fe5bd48517719d5b12e0437354c8107ce7683c332120bf6568aed884c/probability-probability-9f13e191d036a7047654e3ec-unresolved.svg`.

### Shared mission AI

Scenario set: `E6_SHARED_MISSION_SCENARIOS_CURRENT_2026_08_06` with `E6_SHARED_MISSION_OPEN`, `E6_SHARED_MISSION_HOST_CRISIS`, `E6_SHARED_MISSION_ROUTE_LOCKED`, and `E6_SHARED_MISSION_NO_VALID_TARGET`.

Evaluation: analysis ID `probability-8950045661d66cea9adf4cf6`, scenario hash `7285f72c125307881faf9b07e13de472af62cd1c88b77988edf291dddf75e123`, 4 scenarios, 216 candidate rows, 486 unresolved items, 20 diagnostics, classification `partial/bounded score-only`.

The 20 diagnostics are primarily unsatisfied modifiers under empty-state scenarios plus intentional never-eligible notices for `independence_wave_register_population` and `independence_wave_secure_provisional_capital`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a309127743ffdc6ae38993c92883ef481cd118232adcd5d4df37309c581ebe2/2099e8cf2205809140991606adce63d97bc7de10e20b84b3da45145cd06223f6/probability-8950045661d66cea9adf4cf6.json`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/323f18ddb75b77b583185a291f1fcd0e57b8e3f8569806eec122fa09fb275a64/1bd738c2db0e52e6150d6dba515e04e8170e6099bf22438ae33ba0830dbf49b0/probability-probability-8950045661d66cea9adf4cf6-unresolved.svg`.

### Crisis mission AI

Scenario set: `E6_CRISIS_MISSION_SCENARIOS_CURRENT_2026_08_06` with `CRISIS_PRESSURE_OPEN`, `CRISIS_REQUESTER_LOST`, `CRISIS_RETRY_EXHAUSTED`, and `CRISIS_NO_PRESSURE`.

Evaluation: analysis ID `probability-adfb7e57ec7ba9495504a95e`, scenario hash `3db379f661d07101bb0738e1e9c03f83398b573f5c3bf4836b2d0f3bab062a78`, 4 scenarios, 4 candidate rows, 7 unresolved items, 0 diagnostics, classification `partial/bounded score-only`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35dbaef73101b242fdfffd8de397ca6d4704e3cd6e55827a3a930c41a3dd3b8d/678a3182ec2a33a37e03d921167819fc6f299bbb16c584aa0c3bbfde350fe119/probability-adfb7e57ec7ba9495504a95e.json`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0840d6e64171c4fd404da9ec5b05548de689afd14a0ff1d7de19c519ac039137/694e7d1374f6fc59d263f269a61b243453c0fa6c114a4f79b551f9d1e085138e/probability-probability-adfb7e57ec7ba9495504a95e-ranking.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd4a49c275611c8b777e968b61871d981623784a06461f4a7914eca3e42d91c6/b779943618331adb67c5d5e993216ef6ce790ded60b5ed41887e487ca2ec0178/probability-probability-adfb7e57ec7ba9495504a95e-unresolved.svg`.

### Generic focus AI

Scenario set: `E6_FOCUS_SCENARIOS_CURRENT_2026_08_06` with `FOCUS_OPEN_CALM`, `FOCUS_HOST_CRISIS`, `FOCUS_ROUTE_LOCKED`, and `FOCUS_NO_VALID_ROUTE`.

Matching structural MCP evidence: `hoi4.focus_inspect` resolved `independence_wave_focus_tree` at revision `546c98db483766b344e60de2873cfa04109c483af9bb36f5927baea1677b7517` and layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, with 184 focuses, 193 connectors, zero crossings, zero node intersections, one long connector, and five Event 006 layout warnings; its validation remained false only because fourteen unrelated vanilla continuous-focus icon diagnostics were included.

Focus-inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b4c6222e5fb6bbad277c6a60917cf7f25bb483880abf67abf9805d1ebf7fbcf/8d127eada28690038ee5c796cef7acb803beadf4ce18340ac97e8d018435b73a/focus-inspect.546c98db483766b3.json`.

Matching focus render produced a source-linked SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/404ca2cba18bab163a954d97be67d1b697b9db76e3387814fcbb74cadbf1566d/independence_wave_focus_tree.focus.svg`.

Evaluation: analysis ID `probability-a409c793623379895e9836f0`, scenario hash `935efc79a0eccbfaf28ee9c6f1dfaa6c8f7ac793a592efbdf04d497fb0a44a01`, 4 scenarios, 736 candidate rows, 1,033 unresolved items, 226 diagnostics, classification `partial/bounded score-only`.

The supplied state was empty, so the 1033 unresolved items and 226 diagnostics mostly represent route prerequisites, country flags, host threat, living-former-host state, and other runtime gates that were not declared.

The MCP emitted `MCP_INLINE_COLLECTIONS_TRUNCATED` for the large diagnostic collection and retained the bulk evidence in the linked JSON artifact.

The 184-focus inspection and evaluation do not establish a complete runtime focus candidate pool, focus-click probability, focus timing, rank reversal, or route starvation.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88aa01e4bc17de2edbc5295ed68cb68d7795a9808d6254ebfef2790208297dbc/99d638fb24c30218e2871b181a159149623059cb1c9edee84ecb69ed563dd3d5/probability-a409c793623379895e9836f0.json`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bed2709e70ea0632e1313934233b82d1615355b956a840884e32fea39ff79139/84c9712c1448721146137865b190a5b8f5a56c4ee923752d8fd3fbf5a778670e/probability-probability-a409c793623379895e9836f0-ranking.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9eb0edc98dd27d749dceb875ef30db0097ae4f38d2707885ca6a388649105f6f/a39d2e081715298b0681919ec45c415f95385a61306c75fc191e27a46240cebc/probability-probability-a409c793623379895e9836f0-unresolved.svg`.

### SCN-008 scenario selection

`common/scripted_effects/006_independence_wave_scenario_effects.txt` exposes deterministic `independence_wave_scenario_type_previous` and `independence_wave_scenario_type_next` controls and fixed intensity tuning through `constant:independence_wave_scenario_registry.bound_package_count`.

Fresh `hoi4.probability_inspect` with `direct_random` returned `PROBABILITY_SURFACE_EMPTY` with the exact blocker `No weighted blocks matched this request`.

Fresh `hoi4.probability_inspect` with `random_list` against the same scenario-effects source returned the same exact blocker.

Therefore SCN-008 is not a probability-proportional type-selection surface in the current source; its three navigation decisions are UI/ledger controls with `base = 0`, and no exact scenario-type or intensity selection probability can be claimed.

## KAR/CRI package AI evidence

The source owner patch currently gates the 20 regular KAR/CRI actions with `independence_wave_kc_ai_foundation_ready`, applies lower-ledger preference factors of `2`, and applies reserve-floor factors of `0` alongside war/peace and diplomatic gates in `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`.

The two founding missions use `available = { always = no }` and are intentionally passive activation-backed timers, so their never-eligible diagnostics are expected rather than a missing AI route.

The prior typed scenario set remains `PACKAGE_KAR_FOUNDING`, `PACKAGE_CRI_FOUNDING`, `PACKAGE_KAR_WAR`, and `PACKAGE_CRI_SETTLED` with scenario hash `f5ea20a48811380030e56b5865d0cba9057f6ef9ae9eb99b2e6f2c994745f922`.

Prior typed evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df4c3967503207d39bc464d65e2e83ff047faea28270c66d01026744eaec949a/3fe05b06a5d82d269e0e92dd7de538ce4296e3d871ec3ebfe3ba6b0ab266ddb5/probability-873a83b5767ac818381d7b06.json`.

That prior evidence is bounded typed score evidence, not current live runtime probability evidence, because the state records were empty and did not declare package flags, ledgers, resources, capital, costs, or route state.

The fresh same-path `hoi4.probability_compare` probe used the four named KAR/CRI scenarios and returned analysis ID `probability-1be75775d7818b372781cd3a`, scenario hash `963d47813b73830dfae00ee2d18e69b7a0c62ff6d7de211bef4c6ea0ba0f9def`, 80 candidate rows, 667 unresolved items, 12 diagnostics, and `comparisonChanges=0`.

Same-path compare JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/404d2fda3b07c2a89c297f2a710f3b393beb12a7f4611fd8ae1f4069947d7b7a/333c3c81703da15c011240db6b9446ec22a35de218637050f0eae0a1b4035d8f/probability-1be75775d7818b372781cd3a.json`.

Same-path compare ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69eaff358ec86b88486bdfb94e9fa1b93053fe8b9ef8996ad681ad5730972023/5ad1a8027a76c6651bf1367d29efea949bca1c7e95db1d28bbdaec2daea2fc2d/probability-probability-1be75775d7818b372781cd3a-ranking.svg`.

The cached-baseline probe was rejected before analysis with `MCP error -32602`, `Unrecognized key: analysisId` at `before`; the installed route accepts source objects with `{ path = ... }` but not cached `{ analysisId = ... }` objects.

The prior compare capability probe is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc9dbecaf5a3967108998eaef6dda013ca4d5c7329edfc20906b7b8b7c04b6ff/c3b86f9738e71f157e159b21554febfe72e5678324cc0d384ea7246230fe8375/probability-1f9d31215f9ea367038586da.json` and reports `comparisonChanges=0` for identical final paths; it is not a patch comparison.

An exact before/after compare was not possible because the installed compare route accepts only source objects with `{ path = ... }`, rejects the cached baseline forms, and no pre-patch source path exists in the workspace.

## Findings by risk category

### Validity and candidate pools

The outer allocator and Region 04 pools are complete at the `random_list` adapter level, with 14/14 and 8/8 candidates respectively.

The `custom_weighted_pool` adapter found zero candidates in both allocator sources, so these surfaces are not declared custom pools to the installed MCP route; treating them as custom pools would be an unsupported inference.

All AI decision, mission, focus, and scenario-control pools remain runtime-dependent and therefore incomplete for normalized probability.

The crisis decision adapter is unavailable because no decision weighted block exists in that crisis file; the crisis mission adapter is the supported surface.

The generic and KAR/CRI `ai_strategy_factor` adapters are unavailable with the exact MCP blocker `No weighted blocks matched this request`, so strategy ranking is unresolved.

### Dominance, starvation, rank reversal, and repetition

No exact dominance, starvation, rank-reversal, or repetition result is proven for any surface.

The source contains zero-factor gates and dynamic eligibility that can intentionally remove candidates, but the missing typed state prevents distinguishing intended route exclusion from accidental starvation.

No claim is made that any `ai_will_do` score is a click probability.

### Timing and sequence

No MTTH timing distribution, custom-pool cadence, cooldown, recovery, cap, removal, reset, or terminal-state sequence was evaluated in this refresh because no complete state-transition contract was supplied.

The allocator analysis cannot support a safe capacity-20 claim or a package repetition claim without reservation and prior-selection state.

### Structural event evidence

Fresh read-only `hoi4.event_inspect` scan mode against `events/006_independence_wave.txt` returned `EVENT_INSPECTED_PARTIAL` with revision `04e76dcf50aebd2f59c678621af2f35f23cb37c45cce1ae2247f61362df19b6f`, graph hash `e8d3d7ed4e48cda3100b9924d95d950ea65f248f74111e49e6f02fc9ec57c2b5`, 9464 events, 14614 options, 8145 unresolved nodes, 2119 diagnostics, and 0 blocking diagnostics.

Event-inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a8b5ccc37bc9b8f1d57f2aa8deeeda8e35d13926f9db99072292d090c40e4eb/df5efcd3368642e5f7d477ba487a1c84d272c873d694f36e339bd86758c262e2/event-scan-04e76dcf50ae.json`.

Matching read-only `hoi4.event_render` overview returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash.

Rendered event overview SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54f1a5fee2486a6d7f5570317749b5ee270b2d1d7537d4f54c64639d0c34107c/c144124e76ffbe2ec731ae35d06998944702621b4cc31f3922ffcc21baf04e71/event-overview-04e76dcf50ae.svg`.

The structural result is partial because the large workspace deferred helper and lifecycle projections; it is source-navigation evidence only and not runtime completion proof.

That structural receipt does not replace the weighted probability evidence above.

## Highest-impact owner-patch candidate

No gameplay weight change is justified by the current MCP evidence because every candidate balance conclusion is still state-incomplete.

If the owner requires one queued patch candidate, prioritize a source-owned, MCP-recognizable strategy projection for `common/ai_strategy/006_independence_wave_karelia_crimea.txt` and `common/ai_strategy/006_independence_wave_generic.txt`, or an equivalent explicit scenario-state bridge, so the existing KAR/CRI reserve-floor and lower-ledger intent can be evaluated against complete typed host, route, ledger, resource, capital, reservation, and package-attestation states.

Do not tune the numeric factors until that adapter/state bridge yields a valid before/after `hoi4.probability_compare` with the same named scenarios.

As a concrete owner process fix, preserve a pre-patch source snapshot or separate pre-patch path before the next AI-weight change so the compare route can accept `{ path = ... }` for both sides; the current cached analysis cannot be supplied as `before`.

These are queued owner recommendations only and were not applied; current evidence does not support a gameplay numeric patch.

## Skipped analyses and exact blockers

`hoi4.probability_sweep` was skipped because the supplied scenarios do not contain complete dynamic inputs and a threshold sweep would be false precision.

`hoi4.probability_simulate` was skipped because no uncertain inputs or seeds were explicitly declared.

`hoi4.probability_sequence` was skipped because no complete custom pool, cadence, state transitions, or terminal states were declared.

No valid pre-patch `hoi4.probability_compare` was possible because there is no pre-patch source path and the installed route rejects cached analysis IDs, artifact URIs, and source hashes as `before`/`after` objects; the fresh same-path probe with `comparisonChanges=0` is retained above as a capability receipt only.

Scenario selection probability was skipped after both `direct_random` and `random_list` inspections returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request` for `common/scripted_effects/006_independence_wave_scenario_effects.txt`.

No gameplay, AI, event, focus, decision, mission, strategy, or runtime patch was applied.
