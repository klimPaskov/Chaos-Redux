# Event 006 Focus AI Probability Audit — 2026-09-25

## Scope and outcome

This is a read-only audit of the current Event 006 national-focus AI score pool. The audited surface is `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt` (184 focus candidates). This handoff is the only file created for this audit; no gameplay source was edited and no commit was made.

The probability analyzer did not establish profile-specific focus rankings or selection probabilities. The source candidate list was supplied in full, but the engine-eligible pool and required external factors remained unresolved for all seven requested scenarios. All scenario-level balance conclusions below are therefore **unresolved**. Reported source weights and one modifier trace are **exact score evidence** only; they are not click probabilities.

## Sources reviewed

- `common/national_focus/006_independence_wave_focus.txt` — Event 006 focus tree and its 184 `ai_will_do` entries.
- `common/script_constants/006_independence_wave_constants_registry.txt` — `independence_wave_focus_ai` score constants.
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` — Event 006 AI strategy profiles; the probability adapter discovered no weighted surfaces in this file.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt` and `common/scripted_triggers/006_independence_wave_triggers.txt` — reviewed for the focus eligibility and setup/route state requirements.
- Accepted scenario design: `docs/specs/006_independence_wave_specs/matrices/006_ai_strategy_matrix.csv` and `docs/specs/006_independence_wave_specs/diagrams/006_focus_tree_lane_map.md`.
- Prior evidence: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_gap_inventory_2026-09-03.md`, `006_event6_focus_mcp_review_2026-09-20.md`, `006_event6_probability_fixture_schema_probe_2026-09-20.md`, and `006_event6_probability_refresh_2026-09-20.md`.
- Offline Paradox wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding were consulted. The required vanilla documentation folder was read, with `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `common/script_constants/documentation.md` used for the relevant behavior. No Paradox wiki web pages were used.
- Vanilla focus precedent reviewed: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/abdacom_shared_branch.txt`, whose actual focus AI block uses `ai_will_do = { base = 2 }`. Vanilla country tag data confirms `SCO` is a defined tag at `common/country_tags/00_countries.txt:129`; the Event 006 source also contains Scotland focus content. `SCO` below is only a valid schema anchor, not a claim that every matrix profile is Scotland.

The MCP evidence metadata references `docs/research/probability-adapter-evidence.md`, but that file is absent from the repository. This did not prevent the connected calls; the live tool results, source review, offline wiki, and vanilla documentation were used. It remains a documentation gap in the supplied evidence chain.

## MCP evidence and provenance

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

### Probability source inspection

The audit began with `hoi4.probability_inspect` on adapter `national_focus_ai_will_do`, source `common/national_focus/006_independence_wave_focus.txt`.

- Result: `PROBABILITY_SOURCE_INSPECTED`; 184 candidates; 17 required input categories; zero unresolved inputs at source-inspection time; `poolComplete=false` and zero available candidates for the empty inspection fixture.
- Source revision: `36b6c41fc98be4fa3f005e0660ef069b3b53cd8dc5fcd245de2434844b5d59b0`.
- Source hash: `d4970a31fc37dc20a72a88f0424eb21920d2727318674b01b82eba64f1ee576b`.
- Selection semantics: `uniform_score_race` at next-focus selection cadence. The adapter supports normalized score shares, raw scores, and eligibility, requires a complete pool, and has no time-distribution or sequence capability. It warns that ordered AI strategy plans can override focus weighting and that prerequisite-completion multipliers/external focus factors require explicit scenario inputs.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8b9b1d88e04cca3605e9e8e4b9668018133dc459a55cf9fa4ced3d9c4ffae89/7065771fc05dc34934dff1b85c75b2d24dd684539698858b6a9df2d539aea2ce/probability-inspect-d4970a31fc37.json`.

The inspected required-input inventory included `BEL`, `HOL`, `LUX`, `capital_scope`, `check_variable`, `custom_trigger_tooltip`, `event_target:independence_wave_setup_anchor_state`, `event_target:independence_wave_setup_former_host`, `exists`, `focus.external_factors_complete`, `has_completed_focus`, `has_cosmetic_tag`, `has_variable`, `has_war`, `is_in_array`, `original_tag`, and `var:independence_wave_former_host`.
A separate `hoi4.probability_inspect` used adapter `ai_strategy_factor` on `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`. It returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, zero required inputs, and zero unresolved items; revision `0c84050309c26b105695d9f01ba49b3e49a96bab30f58d215938333c899b1af3`; source hash `b84ee2ca17f45793196641dd0d383779fb2e36ab29da6a1ee2d90912ec82deb6`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9eaf12fe8241a03f101b99e6bb0147aa0275c32304a57f98ec1bca49c5b6d5a/543bdb7ac2d00fecdf70502557b0b14ea3fd6e8e205815dcdc335ec4d8395999/probability-inspect-b84ee2ca17f4.json`. Source review shows those Event 006 strategy profiles affect military/equipment production, construction, and war restraint; the adapter did not identify focus-score factors in this file. This does not satisfy the focus adapter's separate requirement to declare ordered strategy plans and other external factors complete.

### Focus structure and render

`hoi4.focus_inspect` and `hoi4.focus_render` were run for `independence_wave_focus_tree`.

- Current inspect result: `FOCUS_INSPECTED`, 184 focuses, 196 connectors; inspect revision `519001605a2e45334e8a30932ef9ce0f39f3ca5f5a2876ebdee4de14705458c4`; layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
- The task-provided expected MCP revision was `a634332e13a8b44e25db76bf1bf537dc72ee4e8d7d43adf64057443d1ccda7c5`. The live inspect returned a different revision (`519001...`) while matching the supplied 184-focus/196-connector counts and layout hash. This revision mismatch is recorded rather than silently treating the revision strings as interchangeable.
- The focus render returned the same layout hash. Its only noted layout warning was the 10-column, 1-row connector from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine`. The report also surfaced missing vanilla localization `continuous_restrict_freedom_desc`; neither finding establishes an AI weighting defect.
- Focus inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4167eb3cdb5b8d2c967a16a52d9628f0c7e0757f99c91ee45462c4068f659e14/85d9574e86c258f977cee7032d0039b832878d9b38fc7bfd40a3bbec31001cfc/focus-inspect.519001605a2e4533.json`.
- Rendered HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2b282094ed9cf36d4fb4add8a8b80205a8cd8d12e2e396c2e4f1f9f48302602/ca5d3e729d6c11d1c3b6d62d9b0fe52e1921275e6f42d74c2af338f4f392497b/independence_wave_focus_tree.focus.html`.
- Rendered SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/352b090f1cd955f9cbb30a41e0ae581761c08f51f20d788d63598a7bd7d4c3e2/03fb7b9cfde3477904a192536a3899c4a74cb19a3046515d1f799e4a47e030e6/independence_wave_focus_tree.focus.svg`.
- Focus JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a69a5d66e7de39546898dcbc68294f03be58a2e72fe7ecdf0e77c298a22d7cd0/aabcced5a240cad4830ce318ac4131d867ae8d91067cbcbf1f5fc03a559420c1/independence_wave_focus_tree.focus.json`.

### Seven named scenario evaluations

`hoi4.probability_evaluate` was run for all seven required IDs and included all 184 focus IDs as the explicit candidate pool in each scenario. The supplied matrix defines qualitative behavior profiles rather than executable campaign state. The adapter schema was honored with primitive-only fields and no invented Clausewitz variables: each scenario used `actor:"SCO"`, `state:{}`, `flags:[]`, and `scopes:{}`. Consequently these are label-only incomplete fixtures, not valid profile simulations. No gameplay flags were added to make them pass.

The final rendered evaluation is `analysisId=probability-3171192372db1e0c84a0d3d1`, with source revision `38016aad7f9e8b5d0ddfbe186a7a5f57338ecc3466f013a1385e6b255731a629`, source hash `d4970a31fc37dc20a72a88f0424eb21920d2727318674b01b82eba64f1ee576b`, and scenario hash `ad36e3f2b022567a5d590bf706d234f03671aa9a231c0b15fb8b93f1f39f9756`. Result: `PROBABILITY_ANALYZED_PARTIAL`, seven scenarios, 1,288 candidate rows, 3,324 unresolved items, and 225 diagnostics. The 1,288 rows are 184 candidates × 7 scenarios; row coverage does not mean eligible-pool completeness.

| Scenario ID | Accepted matrix mapping | Fixture supplied | Candidate-pool status | External-factor coverage | Classification |
|---|---|---|---|---|---|
| `fragile_survival` | AI-01 | `SCO`; empty state, flags, scopes | 184/184 source candidates supplied; engine eligible pool incomplete | Missing campaign variables, current focus completion/prerequisite state, route gates, scopes, and external focus factors | Unresolved |
| `constitutional_settlement` | AI-02 | `SCO`; empty state, flags, scopes | 184/184 source candidates supplied; engine eligible pool incomplete | Same missing inputs; no executable settlement-state definition in the accepted matrix | Unresolved |
| `patron_dependent_state` | AI-06 | `SCO`; empty state, flags, scopes | 184/184 source candidates supplied; engine eligible pool incomplete | Same missing inputs, including patron variables and anchor/former-host targets; AI-07 client alternative is not a separate requested scenario | Unresolved |
| `league_internationalist` | AI-08 | `SCO`; empty state, flags, scopes | 184/184 source candidates supplied; engine eligible pool incomplete | Same missing inputs; league alignment and focus strategy-plan context are undeclared | Unresolved |
| `radical_high_chaos` | AI-09 | `SCO`; empty state, flags, scopes | 184/184 source candidates supplied; engine eligible pool incomplete | Same missing inputs, including chaos/route state and focus strategy-plan context | Unresolved |
| `former_host_revanchist` | AI-14 | `SCO`; empty state, flags, scopes | 184/184 source candidates supplied; engine eligible pool incomplete | Same missing inputs, including former-host identity/targets, war state, completed focuses, and external focus factors | Unresolved |
| `formable_pursuer` | AI-20 | `SCO`; empty state, flags, scopes | 184/184 source candidates supplied; engine eligible pool incomplete | Same missing inputs; formable identity, validity, target, and current route/completion state are undeclared | Unresolved |

The accepted matrix supplies the profile mapping above, but it does not encode actor tag choices, numeric variable values, flags, scope targets, completed-focus histories, or a declaration that the adapter’s external factors are complete. The identical `SCO` anchor is therefore not evidence that the requested profiles share an actor or state. Exact selection shares cannot be asserted with this incomplete pool and external context.

### Rendered probability evidence

`hoi4.probability_render` produced partial ranking, matrix, waterfall, and unresolved views from the final evaluation. The fragile-survival ranking view displayed only the first 100 of 184 candidates and no score rows because no candidate was eligible in the empty fixture. This is a fixture result, not proof of zero real-world selection probability, a dead focus, or starvation.

- Evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1093c31aab54613116abf995663714b7eb025c153355d022ef15220474ca07ba/20cbd24554e5005d82c0ef280c183a0bed8db7aafc62208ddfe4f626708bdb07/probability-3171192372db1e0c84a0d3d1.json`.
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1eb9ca746979edb1746d35ca81b0f995b81c03a5ea51297c715bb54836baf3dd/15882e77c591c99dc2e1747c3a5da1f1cb2a1c885506dd5069f081af7c958ab7/probability-probability-3171192372db1e0c84a0d3d1-ranking.svg`.
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b1d7188ecbf6039e416ea86749e1e0b4fd49f4303c47c4ba2634d34efd8a6c2/ac909631f6a1eaea2b3ca3d8631d0d2406bf0fc335c52fadace0899e2d7e4600/probability-probability-3171192372db1e0c84a0d3d1-matrix.svg`.
- Waterfall SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef22acb0dbfe5ef9c722894caa156b56f9734503cc0e7efc9ab12a0a48b0beb8/9180287b4038f12e50bca21b1b5568d22515719b32d266086e9f0257f4ee4ead/probability-probability-3171192372db1e0c84a0d3d1-waterfall.svg`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/179a72c3370ecbd99a2fd478ec536582af3d8fdd619cd6f7ecb268f58b436b3c/8aa755643f5f09e6f468528b9aa1046578c35517eb8d4b979b2a5bd9d8bd3908/probability-probability-3171192372db1e0c84a0d3d1-unresolved.svg`.

The waterfall for `independence_wave_accept_advisers_and_credits` under `fragile_survival` could not resolve eligibility predicates `has_independence_wave_patron_client_route = yes`, `has_country_flag = independence_wave_route_patron_client`, and `check_variable`. Its score base was `constant:independence_wave_focus_ai.high` (25). The displayed zero raw row is caused by unresolved eligibility and must not be interpreted as an actual zero score or probability.

## Exact source score evidence

The current constants in `independence_wave_focus_ai` are `cautious=5`, `standard=10`, `high=25`, `urgent=100`, `preferred_factor=2`, `strong_preference_factor=4`, `prerequisite_boost=1.5`, `avoid_factor=0.1`, and `war_avoid_factor=0.25`. The source comment describes the prerequisite multiplier as mirroring the vanilla 1.5 nudge for just-completed declared prerequisites where represented in `available`.

Across the 184 focus AI blocks, the source bases are: 112 `high`, 57 `urgent`, 12 `standard`, and 3 `cautious`. Ninety-two are base-only and 92 have modifiers, with 124 modifier blocks in total. Modifier occurrences are 30 `prerequisite_boost`, 48 `strong_preference_factor`, and 46 `preferred_factor`. These counts describe configured score expressions, not relative selection rates.

Representative exact source expressions:

- `independence_wave_prepare_capital_administration`: base `urgent` (100); `strong_preference_factor` (×4) when `has_independence_wave_severe_instability = yes`.
- `independence_wave_consolidate_constitutional_state`: base `urgent` (100), no focus AI modifier.
- `independence_wave_accept_protected_future`: base `urgent` (100), no focus AI modifier.
- `independence_wave_accept_advisers_and_credits`: base `high` (25); the scenario waterfall has unresolved patron-client eligibility.
- `independence_wave_propose_development_compact`: base `high` (25); `preferred_factor` (×2) when `independence_wave_focus_economy_port_island` is present.
- `independence_wave_proclaim_radical_sovereignty`: base `urgent` (100), subject to its route and availability gates.
- `independence_wave_demand_recognition_or_conflict`: base `urgent` (100), subject to its route and availability gates.
- `independence_wave_prepare_union_congress`: base `high` (25), no focus AI modifier.

The focus-tree country factor is base zero, then adds `urgent` when `independence_wave_full_focus_framework` and `is_independence_wave_event6_local_content_active` are true. This changes the tree assignment factor; it is not a probability that a focus will be clicked. No direct uses of `avoid_factor` or `war_avoid_factor` were found within the 184 candidates in `independence_wave_focus_tree`. This boundary matters: the same source file declares additional `shared_focus` nodes after the tree block, beginning at line 3408, and several Iceland route consumers outside this 184-candidate pool do use those factors: `independence_wave_ice_choose_constitutional_route`, `independence_wave_ice_restore_traditional_authority`, `independence_wave_ice_establish_emergency_command`, and `independence_wave_ice_accept_patron_mandate`. Those separate country-tree consumers were not evaluated as part of the requested pool, so no conclusion is made about their weights. For the audited 184 candidates, the absence of direct avoid factors alone does not establish that war or route risks are mishandled because eligibility and external strategy context were not evaluated.

## Unresolved inputs and diagnostics

The analyzer reported the following blockers in the scenario fixtures:

- `FOCUS_EXTERNAL_FACTORS_UNDECLARED`: exact focus selection requires the scenario to declare ordered strategy-plan and prerequisite factors complete.
- `check_variable` requires declared variable and comparison values; empty-state fixtures provide neither.
- `exists` is undeclared.
- `has_variable` is undeclared.
- Event-target scopes `event_target:independence_wave_setup_former_host` and `event_target:independence_wave_setup_anchor_state` are undeclared.
- Numeric setup inputs are absent: `independence_wave_setup_package_id`, `_region`, `_depth`, `_territory_level`, `_force_level`, `_chaos_band`, `_archetype`, `independence_wave_active_patron_count`, `independence_wave_strongest_patron_influence`, and `independence_wave_former_host`.
- Focus completion, prerequisite availability, original/cosmetic tag checks, war state, external focus factors, and route/target validity are not modeled by the empty fixtures.

These are fixture and adapter coverage gaps. They do not prove the focus weights are wrong or that a focus is impossible in game.

## Sweep, compare, simulation, and sequence

`hoi4.probability_sweep` was attempted for `state.independence_wave_setup_force_level` and `state.independence_wave_setup_chaos_band` with five steps and pairwise/rank-reversal analysis. It returned `PROBABILITY_SWEEP_RANGE_REQUIRED`: “Every sweep path requires a scenario range, numeric alternatives, or numeric state value”; the first path named was `state.independence_wave_setup_force_level` in `fragile_survival`. No sweep points, thresholds, sensitivities, or rank reversals were produced. The second path was not evaluated after the first-path failure. No numeric range was invented to satisfy the tool.

No `hoi4.probability_compare` was run because this audit contains no owner gameplay patch or before/after candidate. No simulation was run because there were no explicitly declared uncertain inputs and no complete scenario fixture. No sequence analysis was run because the focus adapter declares `sequence=false` and this is not a declared custom weighted pool with cadence and state transitions.

## Findings by requested risk category

- **AI validity:** unresolved. Source eligibility gates and route conditions exist, but the scenario actor, setup state, focus completion history, and scope targets were not executable in the fixture.
- **Dominance:** unresolved. The source has high/urgent bases and several multipliers, but the complete eligible candidate pool and outside focus modifiers are unknown.
- **Starvation or dead/hidden/blocked focus risk:** unresolved. Empty-fixture ineligibility is not evidence of real campaign starvation or positive weight on an impossible focus.
- **Rank reversal:** unresolved. The sweep did not run because no numeric sweep range was defined.
- **Timing drift or duration:** not measured; the adapter does not provide time-distribution support for this focus-selection surface.
- **Repetition and terminal behavior:** not measured; the adapter has no sequence support here, and a complete pool cadence/transition contract was not declared.
- **Unsafe snowball or exploit risk:** unresolved. External focus strategy factors, state progression, and scenario transitions were not modeled.
- **Probability interpretation:** focus weights participate in a score race under the adapter’s `uniform_score_race` rule. A raw score or normalized share from an incomplete pool would not establish an engine click probability; no exact probability claim is made.

## Recommended follow-up (no fix applied)

No weight adjustment is supported by this evidence, so preserve current AI weights. For a future probability pass, supply adapter-valid campaign fixtures for each of the seven profiles, grounded in implemented Event 006 setup variables and real tags/flags/scopes/completed-focus states; declare strategy-plan and prerequisite external factors complete only when their values are actually represented. Cover the existing numeric variables and targets listed above without inventing new gameplay state. Then rerun `probability_evaluate` for the same scenario IDs and use `probability_sweep` with explicit source-grounded numeric alternatives for force and chaos bands.

When fixtures are available, review `independence_wave_prepare_reclamation_command`, `independence_wave_demand_recognition_or_conflict`, `independence_wave_discover_regional_identity`, and the radical-route candidates in fragile-survival and settled-state scenarios. This is a proposed review focus, not a confirmed defect or a requested balance target. Keep the 184-candidate source pool complete while separately declaring which candidates are actually eligible under each scenario.

## Completion and limits

Completed: read-only source/spec/precedent review; mandatory probability inspection; all seven named partial evaluations with the complete 184-ID source candidate list; required sweep attempt; probability render; structural focus inspect/render; separate Event 006 strategy-factor adapter inspection; and this scenario-specific evidence handoff.

Blocked/unresolved: profile-specific rankings, exact or bounded selection probabilities, sensitivity/rank reversal, real starvation/dominance, timing, repetition, and snowball risk. The exact blocker is incomplete campaign state and undeclared external focus factors, plus the sweep route’s requirement for a numeric range. The live focus inspect revision also differs from the task-provided revision while counts and layout hash match.

No gameplay weights were changed, no tests or live game were run, and no commit was made. Skills used: `chaos-redux-subagents` and `chaos-redux-focus-trees`; no skills were created or updated.


## Addendum: DM-53 `revealed_by_league_state` gate

### Scope and source behavior

This read-only follow-up evaluates DM-53 `independence_wave_discover_regional_identity` in category `independence_wave_formables_category`, with the selected formable profile mode `revealed_by_league_state`. No gameplay source or weight was changed.

Relevant source surfaces are `common/decisions/006_independence_wave_decisions.txt` (DM-53 visibility, availability, and `ai_will_do`), `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` (`has_independence_wave_formable_discovery_gate` and `can_independence_wave_discover_selected_formable_family`), `common/scripted_effects/006_independence_wave_focus_effects.txt` (`independence_wave_focus_allow_league_route`), and `common/script_constants/006_independence_wave_constants_registry.txt` (`independence_wave_decision_ai`, `independence_wave_value`, and `independence_wave_formable_discovery`). The accepted DM-53 entry is `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`; the gate concern and prior source trace are also recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_tree_audit_2026-09-25.md`.

The source sets DM-53 `visible = { can_independence_wave_discover_selected_formable_family = yes }`. For mode value 4 (`revealed_by_league_state`), that helper accepts any of three flags: `independence_wave_league_member`, `independence_wave_league_route_available`, or `independence_wave_formable_league_reveal_ready`. The route-available helper sets `independence_wave_league_route_available` directly. Thus, at the source-expression level, toggling that flag changes the league-state subgate from false to true when the other two OR branches are false. The complete DM-53 visibility helper still requires recognized-or-later state, the discovery unlock, a registered and valid selected family, commit readiness, no prior discovery, and no transaction lock. The decision's separate `available` trigger checks whether the standard administration cost can be paid.

DM-53's score expression is separate: base `constant:independence_wave_decision_ai.high` = 25, with modifier factor `constant:independence_wave_value.minimum` = 0 when commit readiness is false. The `independence_wave_league_route_available` flag does not appear in this `ai_will_do` expression. Therefore the flag has **no direct effect on the configured raw score formula**; holding readiness and all other inputs fixed, the source score is unchanged when only this flag changes. This is exact source score evidence, not a probability or an MCP-resolved effective score.

### Preserved scenarios and gate probes

The original seven focus scenario IDs were included unchanged, with the same label-only fixtures (`actor:"SCO"`, `state:{}`, `flags:[]`, `scopes:{}`). They remain incomplete campaign scenarios and do not claim that all seven profiles are Scotland. Two additional source-grounded predicate probes differed only in the route flag; both set the real mode variable to 4.

| Scenario ID | Fixture | Candidate-pool and external-factor coverage | Classification |
|---|---|---|---|
| `fragile_survival` | Preserved baseline fixture | DM-53 was not matched by the decision adapter; full campaign and cost state absent | Unresolved |
| `constitutional_settlement` | Preserved baseline fixture | Same | Unresolved |
| `patron_dependent_state` | Preserved baseline fixture | Same | Unresolved |
| `league_internationalist` | Preserved baseline fixture | Same | Unresolved |
| `radical_high_chaos` | Preserved baseline fixture | Same | Unresolved |
| `former_host_revanchist` | Preserved baseline fixture | Same | Unresolved |
| `formable_pursuer` | Preserved baseline fixture | Same | Unresolved |
| `dm53_gate_closed_probe` | `state:{independence_wave_formable_discovery_mode:4}`, `flags:[]` | Isolates the route flag; recognized stage, unlock, family selection/registration, readiness, discovery/lock state, and cost remain undeclared | Unresolved |
| `dm53_gate_route_flag_probe` | Same state; `flags:["independence_wave_league_route_available"]` | Same missing inputs; only the route flag differs from the prior probe | Unresolved |

The combined nine-scenario evaluation hash is `cbde5675da5cea383f346f4a37e884d2498d1524c7057667c3b55765b22013ba`. The original seven IDs are preserved from the focus baseline; the new hash covers those seven plus the two predicate probes.

### HOI4 MCP probability evidence

The required first inspection used adapter `decision_ai_will_do` on `common/decisions/006_independence_wave_decisions.txt`.

- It returned `PROBABILITY_SOURCE_INSPECTED`, source revision `bc1ad11ff529b6d29a1ee06fd0c661d23e3661772642c4f7260e1c9abdd672f4`, source hash `b2970b16f0dd076971b1b8b09a16b132fe206b5e6bf7eff38a835509306078d8`, 13 decision candidates, 89 required inputs, `poolComplete=false`, and zero available candidates on the empty fixture.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/166d0190348495538ac7f33f8085ee36d97f925866d4e0a766d42922355f2764/c808623180f704290df45c74d9cffef97399990622fa8bf403ea64704baba9ae/probability-inspect-b2970b16f0dd.json`.

A candidate-filtered decision inspection for `independence_wave_discover_regional_identity` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=candidate_pool_not_found`, `suggestedAdapter=mission_ai_will_do`, 13 decision-adapter candidates with zero identifier matches, and 72 mission-adapter candidates with one identifier match. This is the exact route mismatch: the source defines DM-53 as a decision, but this probability service did not admit it to the `decision_ai_will_do` candidate pool.

- Filtered inspection revision: `fb40a1e96386531e7d7a7e956537c977c0234679024fc96ca19fc44f50815582`; source hash remains `b2970b16f0dd076971b1b8b09a16b132fe206b5e6bf7eff38a835509306078d8`.
- Mismatch artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2dd814ec1a50081e05f1c205de5b99741e849325d4b80a98cd58fc92d8d24085/c6144275283c55e267b9ea17194b8cb9209d615e57820c0d70ffd8aa5a25fbf7/probability-inspect-b2970b16f0dd.json`.

Following the adapter's own recommendation, a read-only `mission_ai_will_do` inspection of the same source and one candidate found `poolComplete=true` for that one-candidate mission-adapter pool, one candidate, four required inputs, and zero unresolved items at inspect time. Revision: `417941c7a15cfcec8b9feb62c3da05f9ca32a9ed55c979abf96e18a6186ee083`; source hash: `b2970b16f0dd076971b1b8b09a16b132fe206b5e6bf7eff38a835509306078d8`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1554e18a1b512a7976cec8b521fe3ffae4b5596ced834a00ae3e893ec4e4c3d1/180e52724989e4f34b98d4aa978d889ea946afa3c0080dd83d056020d9b8f36f/probability-inspect-b2970b16f0dd.json`. This does not make the target a mission in the game or resolve the decision-adapter mismatch.

`hoi4.probability_evaluate` first requested `decision_ai_will_do` and returned `adapterId=mission_ai_will_do`, analysis ID `probability-445283fef8971fa738830cb5`, source revision `bbf2ef356a56474ffe291e8c9e712004aa6f6c028eb1a66b238777ce3feea986`, the same source hash and scenario hash below, nine candidate rows, four unresolved items, and zero diagnostics. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/602a48ec90509a61d38fa92b1edcdf35928f0a3a745146d3acfeef2a7b9db0c2/4a2502fafe2737894bfbbcbf70798d56287aa770373749de431fefbccd085e6c/probability-445283fef8971fa738830cb5.json`. The explicit mission-adapter evaluation then analyzed the one selected target across all nine scenarios. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-45572dd64aaa310076363799`, source revision `dc05221e6c11a20c83814b244ab5c632d6db7f13c7a63a1b3f3e14474bbea198`, source hash `b2970b16f0dd076971b1b8b09a16b132fe206b5e6bf7eff38a835509306078d8`, scenario hash `cbde5675da5cea383f346f4a37e884d2498d1524c7057667c3b55765b22013ba`, nine candidate rows, four unresolved items, and zero diagnostics. No exact AI candidate-availability result, resolved score trace, normalized probability, or rank was established.

- Evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd35ed8d0c34d13889a6f1b5931402af2272584b34519f35c6192720a880dc7d/a60c6af8ad028cf03dc0b35716f62a3900d8d54e5f2cd917e3de55de05730c57/probability-45572dd64aaa310076363799.json`.
- Evaluation waterfall SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d90da4a070b4b2d9639b2c37fe5f73c87bbdb95fd370ea252fd3207245dc778c/75054bf7f5a9915b4bc28762cb9c3502bcb04e6c55021d668e1ba422f7046b4d/probability-probability-45572dd64aaa310076363799-waterfall.svg`.
- Evaluation unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0f6adc21cb857429d90ded57c4d5e0722b817a56fa0635c28c81a850a042fb0/38f43d5f6e17ff936321b2dbd71f8bae7b1d6d55a3dae591c25e7c29d5e7a574/probability-probability-45572dd64aaa310076363799-unresolved.svg`.

`hoi4.probability_render` was called in the same tool execution, but returned `PROBABILITY_ANALYSIS_STALE`: analysis revision `dc05221e...` differed from current workspace revision `7e4ca17ed248df956a60b3ee97dde20a958d4568273bf90478966cf47bdaee7f`. It returned no visual resources. The SVG links above are the partial evaluation's generated views, not a successful fresh render.

A sweep of the boolean path `flags.independence_wave_league_route_available` returned `PROBABILITY_SWEEP_RANGE_REQUIRED`: “Every sweep path requires a scenario range, numeric alternatives, or numeric state value”; the first reported path was that Boolean flag in `fragile_survival`. No sensitivity or rank-reversal result exists, and no numeric or Boolean values were invented to bypass the tool requirement. No comparison was run because no owner patch exists. No simulation was run because no uncertain inputs were declared and the fixture is incomplete; no sequence applies to this decision surface.

### Conclusion and remaining uncertainty

**Weighted score:** exact source evidence says the route-available boolean is not a factor in DM-53's `ai_will_do` expression, so it does not directly alter the configured score. The score formula is 25 when commit-ready and zero under the explicit not-ready modifier; scenario-specific effective score remains unresolved by MCP.

**AI candidate availability:** unresolved. The source gate's league-state branch does become true from `independence_wave_league_route_available` alone, provided every other visibility condition passes. However, the probability service rejected DM-53 from `decision_ai_will_do`, routed it to `mission_ai_will_do`, and returned four unresolved items for the incomplete nine-scenario fixtures. Therefore this audit cannot prove whether HOI4's AI decision candidate pool changes when the visibility flag toggles. The source-level change to the decision's visibility gate is exact; the engine-level AI-pool consequence is not established.

The seven campaign-profile fixtures still need real actor tags, selected-family/profile variables, discovery unlock/registration, recognized-stage and commit-readiness state, discovery/transaction flags, and administration-cost state before an exact DM-53 availability/score evaluation is possible. Keep the weights unchanged pending a decision-adapter route that recognizes this candidate and a fresh renderable analysis. Skills used for this addendum: `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-focus-trees`.

### Post-patch comparison (2026-09-25)

The parent-applied visibility change in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` replaces the transient `independence_wave_league_route_available` eligibility branch for `revealed_by_league_state` with durable evidence: the regional-conference receipt, active charter-vote receipt, actual League membership, or explicit formable-reveal receipt. The DM-53 `ai_will_do` block is unchanged. No source file was edited by this audit.

The before snapshot was reconstructed read-only from `HEAD` and the after snapshot from the current working tree. Both comparison inputs included the same DM-53 decision block and the same relevant registry helper/constants, differing only in the helper's pre-/post-patch gate logic. `hoi4.probability_compare` does not accept the prior `analysisId` as its before-source input, so this source-pair comparison was used against the recorded pre-patch baseline.

The exact same scenario set and fixtures were reused, with scenario hash `cbde5675da5cea383f346f4a37e884d2498d1524c7057667c3b55765b22013ba`: `fragile_survival`, `constitutional_settlement`, `patron_dependent_state`, `league_internationalist`, `radical_high_chaos`, `former_host_revanchist`, `formable_pursuer` (each retains the original actor `SCO`, empty state/flags/scopes fixture), `dm53_gate_closed_probe` (actor `SCO`, state `{independence_wave_formable_discovery_mode:4}`, no flags/scopes), and `dm53_gate_route_flag_probe` (same, with only `independence_wave_league_route_available` added to flags). The seven original focus scenario IDs were preserved unchanged.

### Comparison result and limits

The current read-only `mission_ai_will_do` inspection matched one target, `independence_wave_discover_regional_identity`, with a one-candidate mission-adapter pool and four required inputs. This is only an adapter fallback; the decision adapter previously returned `candidate_pool_not_found` for DM-53. The fallback does not model the complete HOI4 decision pool or establish decision visibility as AI candidate availability.

The compare returned `PROBABILITY_ANALYZED_PARTIAL`, analysis/comparison ID `probability-31fab038f8e2e979b5f6d34d`, adapter `mission_ai_will_do`, source revision `d2f883bc9d92d3e18f516923f52add938682874f52cd806b59b2ab8039cf23e2`, input source hash `88cbe98d2f6b0550d0b24ae16ddf0d5f10f5abfa9ff179b0e9a293f115ac6396`, and the exact requested scenario hash. It analyzed nine scenario/candidate rows, reported four unresolved items, zero diagnostics, and `comparisonChanges=0`. Since coverage is partial and four inputs remain unresolved, the zero-change counter is only the adapter's partial output; it does not prove equal AI candidate availability or equal effective weighted scores and supports no quantitative balance claim.

The comparison call returned these rendered artifacts:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/451eb55d18417c07bcb047b4be4f71f30b856a4670c029c1e070857ffb6996d9/df8fa495f4f5d7a0c1f9be0935c16e3bdfb3bc0846f65738c002b7fe1b80818a/probability-31fab038f8e2e979b5f6d34d.json`.
- Comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/6135b7eab9f7bba01a8a2a9809638921b1af45e9d22638d178e9e31413c55f0a/probability-probability-31fab038f8e2e979b5f6d34d-comparison.svg`.
- Waterfall SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d90da4a070b4b2d9639b2c37fe5f73c87bbdb95fd370ea252fd3207245dc778c/d9fc8c5f36a3a39098a3d9ef9b33c57b225f36981a117854700a65c958abd262/probability-probability-31fab038f8e2e979b5f6d34d-waterfall.svg`.
- Unresolved-input SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0f6adc21cb857429d90ded57c4d5e0722b817a56fa0635c28c81a850a042fb0/63d361770a2082ff9165c248050f26b1123aab4d80f883182cdd4f3a0c409d20/probability-probability-31fab038f8e2e979b5f6d34d-unresolved.svg`.

An explicit follow-up `hoi4.probability_render` call was attempted with that comparison ID and scenario hash. It failed with `PROBABILITY_ANALYSIS_NOT_CACHED`: “Render requires an analysis ID produced by this server process.” No render artifacts were returned by that route. The comparison's generated SVG artifacts above remain available; the failed render is not represented as successful fresh rendering.

### DM-53 determination

**Decision candidate availability:** source-level gate behavior changes. Before the patch, `independence_wave_league_route_available` by itself could satisfy the `revealed_by_league_state` branch when the other DM-53 visibility conditions passed. After the patch, that flag alone no longer satisfies this branch; one of the durable conference/charter/membership/reveal receipts must do so. Whether this source visibility change changes the engine AI decision candidate pool remains unresolved because the probability service does not recognize DM-53 under `decision_ai_will_do` and the fallback adapter is a mission-score adapter with incomplete inputs.

**Weighted score:** the `ai_will_do` source expression is unchanged and does not reference `independence_wave_league_route_available` or the replacement receipt flags, so there is no direct configured-score change from this gate patch. Scenario-specific effective score equality is not established by MCP; the partial compare's `comparisonChanges=0` is insufficient evidence for a quantitative conclusion.

No weights or other source were changed, no commit was made, and no AI availability or balance claim is inferred from incomplete adapter coverage.

