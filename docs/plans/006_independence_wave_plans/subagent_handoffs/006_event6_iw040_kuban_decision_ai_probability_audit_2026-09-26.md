# IW-040 KUB Government-Choice Decision AI Probability Audit

Audit date: 2026-09-26.

Disposition: **bounded and unresolved**. This is a read-only audit. No gameplay source or AI weight was edited. The MCP evaluation described below used an incomplete constructed fixture and is retained only as a failed fixture probe, not as campaign or balance evidence.

## Scope and source surface

The audited decision identifiers are **independence_wave_kub_ratify_constitutional_autonomy**, **independence_wave_kub_adopt_agrarian_compact**, **independence_wave_kub_convene_socialist_councils**, and **independence_wave_kub_establish_mounted_emergency_command** in **common/decisions/006_independence_wave_frontier_decisions.txt**.

Related source reviewed:

- **common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt** for **is_independence_wave_kub_government_choice_open**, **has_independence_wave_kub_active_government_project**, **has_independence_wave_kub_route_government**, the stability ledger, and route costs.
- **common/scripted_triggers/006_independence_wave_focus_triggers.txt** for the four route triggers and their route-variable checks.
- **common/scripted_triggers/006_independence_wave_decision_triggers.txt** for shared equipment, manpower, command-power, and army-experience cost gates.
- **common/scripted_effects/006_independence_wave_kuban_package_effects.txt** for the founding-project failure effect.
- **common/script_constants/006_independence_wave_constants_registry.txt** for the AI weights, route costs, project durations, 600-day mission duration, and stability threshold.
- **common/ai_strategy/006_independence_wave_ai_strategy_registry.txt** for KUB's conditional survival, host-restraint, settled-compact, and emergency-guard strategies.
- **docs/specs/006_independence_wave_specs/matrices/006_ai_strategy_matrix.csv** and **docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md**.

The offline wiki pages consulted were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. The installed vanilla **common/decisions/_documentation.md** and **common/ai_strategy/_documentation.md** were consulted. The separate game **documentation\\*.md** directory was enumerated but not read in full; no claim here relies on its unreviewed pages.

Skills applied: **chaos-redux-subagents**, **chaos-redux-decisions-missions**, **chaos-redux-event-planning** for the supplied AI matrix, and **chaos-redux-mtth**.

## Current source and baseline comparison

The working-tree diff against Git HEAD changes the four decisions' visibility and availability gates. The existing ai_will_do blocks for these four identifiers do not appear in that diff. The current MCP source hash is **f678c9a236daab7488f7af1634e2bc18a927bc549bcd2e8269b79c923e1f8254**. The inspect returned source revision **3b133820f63d127ee94cf6b0f5f44b5dc726ebd64552512c78a291e4de66d053**; the final evaluate/render returned source revision **e4245b08b671d5eaeb8a1aeb7b658094d0a2bbcd71e04a230ba61c6c1e381b99** with the same source hash. Both revision IDs are retained because the server returned different revisions for the same source hash.

The Git baseline gate required **is_independence_wave_kub_project_ready**, which itself requires **independence_wave_kub_compact_crisis_resolved**. The founding mission can resolve only after a government route is selected and the compact is stable, so the old visibility gate hid the actions needed to satisfy the mission. The baseline availability check also used **has_independence_wave_kub_active_package_project**, which includes the active founding mission.

The current gate uses **is_independence_wave_kub_government_choice_open**: IW-040 package identity, setup-complete flag, the active founding mission, unresolved and not failed crisis flags, and no government route already selected. Each decision adds its route trigger for visibility. Availability adds the applicable cost, capital control, and **NOT = { has_independence_wave_kub_active_government_project = yes }**. That helper serializes only the four government projects through their **has_decision** membership. Source review therefore supports the intended deadlock opening and one-government-project-at-a-time gate; it does not prove runtime feasibility.

A MCP probability_compare was **not called**. The pre-change source is available as a Git baseline, but there is no distinct baseline source path bound in the HOI4 MCP workspace. The installed probability contract uses nonempty before/after source paths and rejects sourceRevision/sourceHash fields; comparing the current file to itself would be invalid. No comparison ID exists.

## MCP evidence and outcomes

Workspace: **mod_chaos_redux_ea3b2d67c2c0**.

| Tool | Outcome | Evidence and limits |
| --- | --- | --- |
| hoi4.probability_inspect on the current decision source | PROBABILITY_SOURCE_DISCOVERED, status ok. | The requested decision_ai_will_do adapter was empty; the tool suggested mission_ai_will_do (requested_adapter_empty). It reported 23 source candidates and four matches to the requested identifiers. Source revision/hash are recorded above. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67f45463362026d728c400fccd38a560c0654e8b6254d1870fb9993e204ea52a/d5d8e202de3c3b6ad5701ac84016c0a4011bc05b06702ecfc5949888d7aa70bf/probability-inspect-f678c9a236da.json. |
| hoi4.probability_inspect with mission_ai_will_do and the four IDs | PROBABILITY_SOURCE_INSPECTED, status ok. | poolComplete=true, candidates=4, availableCandidates=0, requiredInputs=15, unresolved=0 at inspection stage. The availableCandidates=0 field is not evidence that the decisions are dead in a campaign. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bedf9ef054d41a2f658f2675a28d1d4be6fb71676270e120c1f34d9a5124b6f/276584df13c25e448150043bb8a00556c158df8716c8707a256aedab6120d7f6/probability-inspect-f678c9a236da.json. |
| hoi4.probability_evaluate | Returned PROBABILITY_ANALYZED_PARTIAL, status ok, but with an invalid/incomplete constructed fixture. | The requested decision adapter was again resolved as mission_ai_will_do. Final analysis ID **probability-b464c12a489ad1c4fc2ceeff**; source revision **e4245b08b671d5eaeb8a1aeb7b658094d0a2bbcd71e04a230ba61c6c1e381b99**; source hash **f678c9a236daab7488f7af1634e2bc18a927bc549bcd2e8269b79c923e1f8254**; scenario hash **4d6cf1f6e9a56ac69d895b9d5ce79103e64abb682d22b0d63a61b04fe72a5e59**; 15 scenarios, 60 candidate rows, 90 unresolved items, four diagnostics, eight visual resources. All four PROBABILITY_OUTCOME_NEVER_ELIGIBLE warnings are fixture-bound and must not be treated as source defects. |
| hoi4.probability_sweep | Returned error PROBABILITY_SWEEP_RANGE_REQUIRED; no artifact. | Exact message: “Every sweep path requires a scenario range, numeric alternatives, or numeric state value.” The requested path was **state.independence_wave_kub_rada_cohesion**, scenario **IW040_KUB_GOV_NONE_SELECTED_ALL_ROUTES_OPEN**. Flat state values did not bind the Clausewitz variable used by check_variable. |
| hoi4.probability_render | First attempt returned PROBABILITY_ANALYSIS_NOT_CACHED; a sequential render of the immediately preceding evaluation then returned PROBABILITY_ANALYZED_PARTIAL, status ok. | The successful render is for analysis **probability-b464c12a489ad1c4fc2ceeff** and scenario hash **4d6cf1f6e9a56ac69d895b9d5ce79103e64abb682d22b0d63a61b04fe72a5e59**. Rendered JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3a9558d900b6a758c5b598debcbda9d17bec697632b5b5d0d26d62830d1e820/94a43920b07619a0199738614b10f3a150d34cc145e67cd214770421721f1ef3/probability-b464c12a489ad1c4fc2ceeff.json. Ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f5b92267ff7cccdce08f347ba889ab5c8c63c4a49409b87bcf3c366750c0132/851418ac3dc99bdeb731ac8101fcf16d715b296b2ca87a255f393d9b0eba0eff/probability-probability-b464c12a489ad1c4fc2ceeff-ranking.svg. Matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c432bcb13791a1ed1cae8c7fb8f12d464ee6e076ce086a0992cca50c62c833f8/e5b51ea296daf806eb87720b2907ff76a01bc6ba6279917ac1f19f72cedec3bc/probability-probability-b464c12a489ad1c4fc2ceeff-matrix.svg. Waterfall SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c26b1fd858df7253bf245545d1635e863c431c0b4a27fd197ae573f69f08b0e0/67562736a8a9d3918954a6d29b4a7ad668cbb234c3fe150937cf1df3ea5e7ad1/probability-probability-b464c12a489ad1c4fc2ceeff-waterfall.svg. Unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1894a47e4c6a5cbb173f8fab78dbf65f6c88a479549eb0bdd3aa4f9db060a02d/71af49fc172383ce3bd54f5908a3e2d29b5e2695796d158b362dd22362525f0c/probability-probability-b464c12a489ad1c4fc2ceeff-unresolved.svg. |
| hoi4.probability_compare | Not called. | No distinct MCP-bound before source; see baseline note above. |
| hoi4.probability_simulate / hoi4.probability_sequence | Not called. | No declared uncertain input distributions, and these are ordinary decisions rather than a complete custom weighted pool with cadence and transitions. |

### Constructed fixture disclosure and exact blockers

Before the interruption, the evaluate call used scenario set **IW040_KUB_GOV_CHOICE_AUDIT_2026-09-26_v2** with these IDs: **IW040_KUB_GOV_NONE_SELECTED_ALL_ROUTES_OPEN**, **IW040_KUB_ROUTE_CONSTITUTIONAL_OPEN**, **IW040_KUB_ROUTE_AGRARIAN_OPEN**, **IW040_KUB_ROUTE_SOCIALIST_OPEN**, **IW040_KUB_ROUTE_EMERGENCY_OPEN**, **IW040_KUB_ACTIVE_GOVERNMENT_PROJECT_SERIALIZATION**, **IW040_KUB_LEDGER_STABLE_60_60**, **IW040_KUB_LEDGER_UNSTABLE_59_59**, **IW040_KUB_STATE234_CONTROLLED**, **IW040_KUB_STATE234_UNCONTROLLED**, **IW040_KUB_ROUTE_COSTS_SUFFICIENT**, **IW040_KUB_ROUTE_COSTS_INSUFFICIENT**, **IW040_KUB_FOUNDING_MISSION_SUCCESS_CONDITION_STABLE_CONTROLLED_GOVERNMENT**, **IW040_KUB_FOUNDING_MISSION_FAILURE_TIMEOUT_600D**, and **IW040_KUB_EMERGENCY_ROUTE_OPEN_AT_WAR**.

These were synthetic schema probes with assumed flags, primitive state values, scope IDs, and scenario labels. In particular, the former-host scope was supplied as SOV without a typed former-host variable binding, and the active-project and timeout cases had labels but no representable decision-membership or mission-clock state. They are **not valid campaign scenarios**; disregard the NEVER_ELIGIBLE diagnostics and all implied scenario outcomes.

The connected adapter accepts only **scenarioSet = { id, scenarios = [{ id, actor: string, state: flat primitive map, flags: string[], scopes: record of { id: string, state: primitive map } }]**. The prior 2026-09-20 fixture probe recorded these exact validation limits, and the fresh inspection/evaluation did not close them: scenario-level fixture, variables, vars, values, inputs, factors, actors, targets, and scopeExpectations are not accepted; scenarioSet.variables returns **MCP error -32602: Input validation error for tool hoi4.probability_evaluate: Unrecognized key: "variables" at scenarioSet**. Top-level flags must be string arrays. A primitive state entry does not declare a Clausewitz numeric variable. Exact prior trace errors were **check_variable requires declared var and value**, **Scenario does not declare numeric variable <name>**, and **Trigger <name> cannot compare the declared scenario value**.

The KUB inputs still requiring a supported typed fixture are:

- Package identity/setup variables, including the **independence_wave_package_id** check and the relevant IW-040 setup-variable declarations.
- **has_active_mission = independence_wave_kub_hold_mounted_compact_together** and membership for each of the four **has_decision** checks in **has_independence_wave_kub_active_government_project**.
- The four route flags together with the numeric **independence_wave_government_route** variable and the chosen-government flags.
- Numeric **independence_wave_kub_rada_cohesion** and **independence_wave_kub_mounted_readiness** variables for the two **>= 60** stability checks.
- Full cost-trigger state: civilian-project capacity, command power, manpower, army experience, convoy/train stockpiles, and infantry/support equipment. Primitive comparator strings do not bind the compound **has_equipment** conditions as a complete campaign fixture.
- Capital and state 234 ownership/control scopes tied to the actual KUB anchor, plus the live event-target/variable relationship for the anchor.
- Former-host validity through **var:independence_wave_former_host**, including the former-host existence/tag checks and **liberation_release_protected_state** ownership relationship.
- Mission elapsed/remaining days and terminal timing. The accepted schema has no mission clock or scheduled state-transition field.

The current inspect reports 15 required adapter inputs; the final evaluation reports 90 unresolved items. Its structured summary does not provide a per-item list, so the JSON artifact is required for detailed trace retrieval. Do not interpret the count as a complete typed scenario.

## Source score and gate findings

The exact source constants are:

| Decision | ai_will_do trace | Source score |
| --- | --- | ---: |
| Constitutional autonomy | base = constant:independence_wave_decision_ai.high; no local modifier. | 25 |
| Agrarian compact | base = constant:independence_wave_decision_ai.standard; no local modifier. | 10 |
| Socialist councils | base = constant:independence_wave_decision_ai.high; no local modifier. | 25 |
| Mounted emergency command | base = constant:independence_wave_decision_ai.urgent; multiply by modifier_double when has_war = yes. | 100; 200 while at war |

These are AI willingness scores, not click probabilities. The wiki describes ai_will_do as an MTTH-style score race; ai_chance event-option selection is a separate probability-proportional mechanism and is not used by these decisions. The MCP evaluation's requested adapter was relabeled mission_ai_will_do, and its structured result did not inline usable candidate raw-value rows. The source constants above are exact source evidence; the score ranking is only source-bounded.

If all four are eligible and no external score modifier changes them, the raw source-score ordering is emergency command above the constitutional/socialist tie above agrarian. War increases only the emergency score. This is not a normalized selection distribution, a probability rank, or proof the AI will complete any route. The evaluator's never-eligible warnings are invalid-fixture artifacts, not evidence that these source decisions are dead.

The KUB government-choice gate itself does not require state 234 control, but each decision's availability requires the capital to be controlled. The founding mission's success condition separately requires stable ledgers, a selected government route, state 234 owned and controlled by KUB, and the capital controlled by KUB. The stable threshold is 60 for both ledgers; the founding mission timeout is 600 days.

Decision project durations are 75 days for the short constitutional/socialist choices, 180 days for the long agrarian choice, and 120 days for the standard emergency choice. The visible/available gates have no remaining-mission-time condition. A late-start deadline interaction is therefore a scenario question; no AI or deadline feasibility conclusion is valid without typed mission time and decision-membership inputs.

KUB's AI strategies include mounted survival, pre-settlement host restraint, post-stabilization restraint, and emergency guard behavior. They steer army/production or war-starting behavior and are not direct modifiers in these four ai_will_do blocks. They can still alter campaign circumstances such as war and resource availability.

## Spec alignment, validity, and risk

**006_ai_strategy_matrix.csv** describes actor profiles rather than mapping IW-040 to one profile. Profiles for viable states, armed states, traditional restoration, and popular councils describe potentially relevant routes, but the matrix does not select a KUB profile or specify the intended ordering among these four government choices.

Part 7 says decision willingness should consider stockpile reserve, front need, supply, production recovery, mission urgency, host threat, League obligations, expected recognition or legitimacy gain, and patron dependency. The four audited blocks encode none of those directly; only emergency command responds to war. This is a design-to-source alignment question for the parent, not authority to change weights.

- **Availability:** The route gates and cost/capital/project checks are source-present. Full engine validity remains unresolved because the adapter cannot bind route variables, active mission/decision membership, and compound costs.
- **Dominance:** Emergency command has the highest raw source score (100, or 200 at war). This is score-only evidence; no dominance probability is proven.
- **Starvation:** No starvation conclusion is supported. The lower willingness scores could lose in an AI score race, but the complete engine pool and selection behavior were not evaluated.
- **Rank reversal:** No sweep result exists. Source review shows the emergency modifier only raises its own score under war, but external campaign factors and actual candidate eligibility remain unresolved.
- **Repetition/serialization:** The four-way active-project helper blocks parallel government projects, and a selected route closes the choice gate. Repeated retry behavior after cancellation and timing near mission expiry remain unresolved.
- **Exploit/snowball risk:** No probability-level exploit conclusion is supported. The immediate source concern is deadline feasibility of projects started late, not a proposed weight target.

## Recommended follow-up, without changing weights

1. Keep all four weights unchanged until the adapter can provide typed IW-040 campaign state and decision/mission membership.
2. Add or locate a supported fixture contract for the exact package, route, ledgers, four active-decision memberships, resource/equipment stockpiles, state 234/capital scopes, former-host pointer, and mission clock. Rerun the four-candidate evaluation only with that complete fixture.
3. Map IW-040 to an AI actor profile in **006_ai_strategy_matrix.csv**, or record an accepted reason that no single profile applies, and define which Part 7 decision-willingness factors should apply to these four choices.
4. Include remaining-time scenarios for the 75/180/120-day government projects against the 600-day mission. Decide whether a deadline-aware gate or AI rule is needed only after the typed scenario evidence establishes actual feasibility.
5. Once a distinct MCP-readable baseline source and complete scenario set exist, compare baseline/current with the same named scenarios; do not compare the current source to itself.

## Skipped analyses and completion boundary

- No valid baseline/current probability_compare was possible because no distinct MCP-bound baseline path exists.
- The sensitivity/rank sweep was attempted and blocked by PROBABILITY_SWEEP_RANGE_REQUIRED.
- The first render attempt was blocked by PROBABILITY_ANALYSIS_NOT_CACHED; a sequential render retry succeeded and produced the artifacts listed above.
- Simulation was not run because no uncertain inputs or distributions were declared. Sequence analysis was not run because this is not a complete custom weighted pool with cadence and state transitions.
- No live game, runtime test, or HOI4 launch was performed.
- No source or AI weight was edited. This report is the only requested output file.
