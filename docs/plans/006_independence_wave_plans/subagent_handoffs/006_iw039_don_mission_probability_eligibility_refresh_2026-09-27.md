# IW-039/DON Mission AI Probability Eligibility Refresh — 2026-09-27

Status: **PARTIAL; eligibility-complete probability analysis blocked by scenario-fixture capability.** This is a read-only audit of exactly two `mission_ai_will_do` surfaces. No gameplay source was edited, no score target is recommended, and no quantitative balance conclusion is made.

## Audited surfaces and source identity

| Mission ID | Weighted source | Activation and terminal source |
| --- | --- | --- |
| `independence_wave_don_hold_millerovo_charter` | `common/decisions/006_independence_wave_don_decisions.txt:16-56` | Same file, activation `:20-25`, `available :26`, cancel/success/failure `:28-53`; package and charter predicates in `common/scripted_triggers/006_independence_wave_don_package_triggers.txt:21-36,70-102,203-215`. |
| `independence_wave_don_review_emergency_host_staff` | `common/decisions/006_independence_wave_don_decisions.txt:58-98` | Same file, activation `:62-68`, `available :69`, cancel/success/failure `:71-95`; package, anchor, and review predicates in `common/scripted_triggers/006_independence_wave_don_package_triggers.txt:21-36,70-73,162-176`. |

Local SHA-256 values: `common/decisions/006_independence_wave_don_decisions.txt` = `8DE0F0C80F037AAD9CEF3CEA029E39F6565C2581B731B32ED53499C682D47280`; `common/scripted_triggers/006_independence_wave_don_package_triggers.txt` = `9210544B79906E08511D2D92FA2BBDB12ED560C61E6EC1573050F9D9DF330A9D`; `common/scripted_triggers/006_independence_wave_triggers.txt` = `4369FF83271DD91FA07BC80F56CCB2AE66F5D8810BDB3B50EAD5A5BC20D06CA5`; `common/scripted_triggers/005_006_liberations_collision_triggers.txt` = `6C6CC4955DEA18EC4EB9FE9201E208B208A67C8A7D7F68BF586A6ED86E8CBEEC`; `common/script_constants/006_independence_wave_constants_registry.txt` = `A4DB75F959CCEF960F0AF9D1DDAFBAB58221B1747FB80CB133E9B5768D20F8AD`.

The current `hoi4.source_lookup` result for both mission identifiers was revision `d1a4a075c73dcf84d43f9631b38c26f22df8c48eecd8bbf759656ff1cbf13abe`; it reports the expected mod definitions at lines 16-56 and 58-99, `overridden=false`, and `sourceShadowed=false`.

## Required probability inspection

The first successful probability operation was `hoi4.probability_inspect` with adapter `mission_ai_will_do`, source `{ path: "common/decisions/006_independence_wave_don_decisions.txt" }`, and exactly the two mission IDs above. Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

It returned `PROBABILITY_SOURCE_INSPECTED`, source revision `634d3ef5ee354663e4b957057a048ece15ab906a91d6286ab059d173067e8921`, source hash `346113c1a872c67343480eee65b6fde763690ea9494b92cfa6a8945e251b8712`, `poolComplete=true`, `candidates=2`, `availableCandidates=0`, `requiredInputs=0`, and `unresolved=0`. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dee6d6eeef7b28a577499caef065171901f996a89abe822b2a78e86c1f4a2026/e9874e12175a0e857f1db9d8506070ae08407f673416312fbe8d87df897a830f/probability-inspect-346113c1a872.json`.

This is a complete inventory of the two requested mission IDs in the inspected file; it is not proof that either mission is eligible in a scenario, nor that they form a simultaneous selection pool. `availableCandidates=0` is not interpreted as an engine failure: both source blocks explicitly use `available = { always = no }`, while their `activation` predicates and current mission lifecycle are separate.

## Scenario construction and exact blocker

The live tool declaration exposes `scenarioSet: unknown` rather than a nested typed schema. The current connected scenario contract documented in `.agents/skills/chaos-redux-subagents/SKILL.md:288-290` accepts only `{ id, scenarios = [{ id, actor, state: flat primitive map, flags: string[], scopes: record of { id, state } }] }`; it rejects invented fixture or variable-declaration records. That contract has no field for the currently active mission or a mission ID bound to `has_active_mission`.

The two intended scenario IDs are `IW039_DON_CHARTER_ACTIVE_ELIGIBLE` and `IW039_DON_EMERGENCY_REVIEW_ACTIVE_ELIGIBLE`. Neither was submitted, so neither has a scenario payload, scenario hash, evaluation ID, or evaluation artifact. The required active-mission state cannot be expressed through the supported `actor`, flat `state`, `flags`, or typed `scopes` fields without inventing a fixture property or misrepresenting a mission as a country flag.

| Intended scenario ID | Status | Candidate-pool completeness | External-factor completeness |
| --- | --- | --- | --- |
| `IW039_DON_CHARTER_ACTIVE_ELIGIBLE` | Blocked before submission; no valid fixture. | Inspect inventories both requested source IDs, but no stage-valid selection pool was evaluated. | Incomplete/unbound: current charter mission, package-generation variables, event-target setup, and state-245 ownership/control/capital are not representable by the documented fixture contract. |
| `IW039_DON_EMERGENCY_REVIEW_ACTIVE_ELIGIBLE` | Blocked before submission; no valid fixture. | Inspect inventories both requested source IDs, but no stage-valid selection pool was evaluated. | Incomplete/unbound: the route flag is representable, but active review mission, package-generation variables, event-target setup, and state-245 ownership/control/capital are not. |

The source explicitly tests current mission state in `is_independence_wave_don_charter_open` (`has_active_mission = independence_wave_don_hold_millerovo_charter`, `006_independence_wave_don_package_triggers.txt:90-97`) and `is_independence_wave_don_emergency_review_open` (`has_active_mission = independence_wave_don_review_emergency_host_staff`, `:162-171`). The missing mission field is not the only campaign state the fixture cannot faithfully establish. `is_independence_wave_don_package` requires original-tag and package-generation variables, a matching current generation, active-origin classification, and `is_iw039_dhc_runtime_preflight_clear` (`006_independence_wave_don_package_triggers.txt:21-36`; `006_independence_wave_triggers.txt:9-14`). Complete setup additionally checks prepared package variables, event-target pointers, aligned global arrays, membership flags, and setup receipts (`006_independence_wave_don_package_triggers.txt:38-63,256-266`). The active charter/review lifecycle also relies on state 245 ownership, control, and capital scope (`:70-73,90-97,162-171`). The fixture contract does not provide typed Clausewitz variable or event-target bindings for these compound predicates.

The emergency route flag `independence_wave_don_emergency_host_staff` itself can be represented in the supported `flags` array, but that cannot cure the missing active-review-mission state or establish the package and anchor predicates. Therefore both named cases stop before evaluation under the user's eligibility-complete requirement. The previous `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostics are not reused as evidence of source failure.

The accepted Event 006 scenario context supplied for this audit is preserved: state 245/Millerovo is the required anchor and capital; state 238 is optional compact territory; state 218 is outside Event 006; SOV 219 is protected; and Event 005 DHC is mutually exclusive in either event order. The source gates align with that context: state 245 is checked as owned/control anchor and capital (`006_independence_wave_don_package_triggers.txt:47-60,70-73`); the cross-package runtime preflight checks DHC and the state-218/state-238 collision conditions (`005_006_liberations_collision_triggers.txt:88-119`).

## Source score trace and result classification

Both `ai_will_do` blocks contain only `base = constant:independence_wave_decision_ai.urgent` and no source-level modifiers (`006_independence_wave_don_decisions.txt:55,98`). The current central constant resolves to `urgent = 100` in `common/script_constants/006_independence_wave_constants_registry.txt:1254-1269`. This is the exact source base expression and its declared constant, not an MCP-computed final score.

| Mission | Base | Modifier trace | Peace/war distinction | MCP result classification |
| --- | --- | --- | --- | --- |
| `independence_wave_don_hold_millerovo_charter` | `constant:independence_wave_decision_ai.urgent` (`100` in source constants) | None in the mission block. | No war-state modifier exists in this expression. | Exact source expression; score-only. Scenario eligibility, final evaluated score, rank, and selection outcome unresolved. |
| `independence_wave_don_review_emergency_host_staff` | `constant:independence_wave_decision_ai.urgent` (`100` in source constants) | None in the mission block. | No war-state modifier exists in this expression. | Exact source expression; score-only. Scenario eligibility, final evaluated score, rank, and selection outcome unresolved. |

No peace/wartime pair was evaluated because the source score expressions do not distinguish those states and the mandatory active-mission input is unsupported. No raw-score evaluation, ranking, timing distribution, normalized selection probability, or click probability is claimed. The offline AI-modding reference describes `ai_will_do` as a weighted score race in the documented cases and distinguishes event `ai_chance` probability-proportional sampling; that distinction is applied here without inferring a mission click probability.

## Eligibility, lifecycle, and risk findings

- Charter mission activation requires a live IW-039 package and completed IW-039 setup, with charter complete/failed flags absent (`006_independence_wave_don_decisions.txt:20-25`). It cancels on package/setup/anchor loss, charter completion/failure, or `has_independence_wave_don_charter_success_conditions`; success is resolved by `cancel_effect`, while timeout fails the charter (`:28-53`). The success helper requires the complete focus/package contract, railhead and petition receipts, service quota, charter ratification, government receipt and route, plus emergency review completion when emergency staff was chosen (`006_independence_wave_don_package_triggers.txt:203-215`).
- Emergency-review activation requires a live package, no charter failure, the emergency-host-staff route flag, and neither review terminal flag (`006_independence_wave_don_decisions.txt:62-68`). It cancels on package/anchor loss, review completion/failure, or charter failure; timeout marks review failure and fails the charter (`:71-95`). The review-open helper requires the active review mission, setup, route flag, no terminal review flags, and anchor control (`006_independence_wave_don_package_triggers.txt:162-171`).
- Source-level terminal flags gate reactivation after completion/failure. This is bounded evidence against straightforward repeat activation after terminal state, not a runtime repetition or exploit audit.
- AI validity remains unresolved at the MCP eligibility layer. The source activation gates are explicit, but the adapter has not bound the dynamic package identity, active mission, and exact anchor state needed to establish an eligible candidate.
- Dominance, starvation, rank reversal, and simultaneous competition are unresolved. These missions represent different lifecycle stages, and no eligible scenario or common active selection race was evaluated.
- No excessive-repetition or snowball claim is made. Mission timeout and terminal effects were read as source gates only; no sequence analysis or runtime behavior was tested.

## Skipped analyses, recommendation, and remaining uncertainty

`hoi4.probability_evaluate` was not called because the supported scenario contract cannot encode the required active mission and compound package state. The invalid prior evaluation `probability-e81b18b350dc33835b26d0eb` used scenario hash `07e91117b7e347fb6667b6fa42c7da3a8db74ce7def28e950797eaccdb9ceac7`; its fixtures lacked active-mission state and the emergency-host-staff flag. Its `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` rows are fixture-limited and not treated as source failure. Prior JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/527e639c04543a956e4612e9514cbd55e0f300290cced632343e4cfd50f5344e/522f2b2ccb2ddfc8b2b611d25d8ea140a58e1f56a7141adf05d1093780c86267/probability-e81b18b350dc33835b26d0eb.json`; prior unresolved render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/a38e861648ae0572390f4578b79754af98a6f6df4303624b23dc2905012759f5/probability-probability-e81b18b350dc33835b26d0eb-unresolved.svg`.

`hoi4.probability_sweep` was skipped because there is no valid evaluated scenario or declared score factor/threshold path; neither source weight has modifiers. `hoi4.probability_render` was not run because no eligible evaluation analysis ID was created; the prior unresolved render belongs to the invalid fixtures cited above. The current inspect JSON is the only new MCP artifact. `hoi4.probability_simulate` was skipped because no uncertain inputs or distribution were declared. `hoi4.probability_sequence` was skipped because these are not a complete declared custom pool with cadence and state transitions. `hoi4.probability_compare` was not run as explicitly instructed; no score source changed.

No numeric weight target is recommended. To complete the requested probability pass, the MCP scenario route needs an explicit supported active-mission field and typed bindings for the package-generation and state/event-target predicates, after which the two missions can be evaluated in separate stage-valid scenarios. Until then, the source-supported `urgent` bases do not establish AI balance, ordering, or selection probability.

## References

- Offline wiki `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:26-37`, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`: explains MTTH-style `ai_will_do` scoring, score races in documented cases, and the distinction from event-option `ai_chance` sampling.
- Offline wiki `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:357-374`, revision `7713b9bcee5f381d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`: defines decision `ai_will_do` as an MTTH block and describes the score construction pattern.
- Installed documentation `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`: documents decision trigger scopes and availability checks; it does not document mission active-state fixture fields or mission `ai_will_do` score normalization.
- Scenario schema contract: `.agents/skills/chaos-redux-subagents/SKILL.md:288-290`.

## Work boundary

Only this handoff was created. No gameplay/spec/workbook file was edited. No tests were run, HOI4 was not launched, and no commit was created, as requested.
