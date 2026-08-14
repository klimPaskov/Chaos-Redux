# IW-044 Tatarstan AI/probability audit (2026-08-13)

## Scope and disposition

This is a read-only audit of the admitted IW-044 Tatarstan package. It covers `common/decisions/006_independence_wave_tatarstan_decisions.txt`, `common/ai_strategy/006_independence_wave_tatarstan.txt`, and the shared focus surface `common/national_focus/006_independence_wave_focus.txt` as consumed by TAT. No gameplay, AI, focus, decision, localisation, or runtime source was edited.

Current Event 006 authority is preserved: 31 content-attested packages, 28 compatible reservation groups, 162 unattested selectable rows, and 39 runtime adapters. FORM-07, FORM-08, FORM-16, and FORM-48 remain fail-closed; ordinary super-event 23 remains blocked and super-event 24 is unchanged.

The next shared/system AI tranche is justified as an evidence-completion tranche, not as a tuning-number decision. The current MCP run proves the source candidate inventory and score-only formulas but cannot prove live ranking, dominance, starvation, repetition, timing, or normalized selection probabilities because typed campaign fixtures are absent and the strategy adapter exposes no weighted surface.

## Audited source surfaces

- IW-044 mission/decision AI: `common/decisions/006_independence_wave_tatarstan_decisions.txt`.
- IW-044 strategy factors: `common/ai_strategy/006_independence_wave_tatarstan.txt`.
- Shared focus AI race consumed by TAT: `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`.
- Package/source authority: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw044_tatarstan_package_completion_2026_08_13.md`.

The package completion handoff confirms dormant vanilla TAT/state 249 reuse, Alemasov preservation, Civic Concord and River Security ledgers, four mutually exclusive routes, the 600-day founding mission, ten costed projects, former-host settlement, network/ambition registration, p44 river-frontier forces, and cleanup-safe lifecycle.

## Mandatory MCP inspection evidence

All weighted surfaces began with `hoi4.probability_inspect` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

### IW-044 missions

`mission_ai_will_do` inspection returned `PROBABILITY_SOURCE_INSPECTED`, source revision `91863468ab1c4cd7fe77881e9b9b1950c650b64c8ad516750a53ad5cde2e11a6`, source hash `fc2e09b238bd9aaaa328fb2cc8b7c942869d7f4618c4b8d8e63f03de2a48aeb2`, 11 candidates, `poolComplete=false`, 0 available candidates, 15 required inputs, and 0 inspect-unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ac49ebc59a868cb72f5f7e5b47c1413af624517236293ae41f46768bad13c21/df17f4502f32b2ae55637bacdbad9685c39db81a1eac3d1966499665cd31f734/probability-inspect-fc2e09b238bd.json`.

The complete source-enumerated mission pool is:

`independence_wave_tat_hold_river_compact_together`, `independence_wave_tat_secure_river_depots`, `independence_wave_tat_integrate_border_guards`, `independence_wave_tat_register_community_compacts`, `independence_wave_tat_settle_former_host_ledgers`, `independence_wave_tat_ratify_constitutional_autonomy`, `independence_wave_tat_adopt_agrarian_compact`, `independence_wave_tat_convene_socialist_councils`, `independence_wave_tat_establish_river_emergency_command`, `independence_wave_tat_codify_durable_sovereignty`, and `independence_wave_tat_open_volga_river_network_corridor`.

The requested `decision_ai_will_do` adapter found no decision surface and redirected to the mission adapter: `PROBABILITY_SOURCE_DISCOVERED`, `requested_adapter_empty`, 0 decision candidates, 11 available mission candidates. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c4d29d4290905adbe2224e505d14c8da38f7fe672a17c0dddc4dc8df7aa6ef1/9645d2d293c445e89fad4d17a1d1bd7316319708afe743176e316496c56e9d54/probability-inspect-fc2e09b238bd.json`.

### IW-044 strategy

`ai_strategy_factor` inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, 0 candidates, 0 required inputs, and 0 unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44c541ffcb9e9da3ff74a207ffaf220080f0779ac2abf9fbdeb870cec6debd22/0aa0f24e1651da83d603c9bc78d73801b3b07ffc360a82151b72b97890c70219/probability-inspect-213b76937d1b.json`.

Source review finds four gated strategy blocks: river survival, former-host restraint, settled compact, and emergency guard. Their static values are 86 army, 40 infantry production, 50 support production, 24 artillery production, 70 infrastructure, 82 bunker defense, 118 emergency army, and -260/-430 founding/settled war restraint. These are source values only; the adapter cannot evaluate activation or effective overlap.

### Shared focus race

`national_focus_ai_will_do` inspection returned `PROBABILITY_SOURCE_INSPECTED`, source revision `91863468ab1c4cd7fe77881e9b9b1950c650b64c8ad516750a53ad5cde2e11a6`, source hash `c46802f6db53a1dd2099b4450eab8c99eabb48f841b575a59a146a31c2948bc7`, 184 candidates, `poolComplete=false`, 0 available candidates, and 15 required inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16c35929bd3d74f1c10d4cdffffc0307c128b1161e93eff9e37eb21804db964d/e01b3b04101aad9d1af7033858fc7c4a921831bff6d82c74ee54cc1de45ba7a7/probability-inspect-c46802f6db53.json`.

The shared focus adapter models an independent score race, not weight-divided-by-sum probability. TAT package hooks are source-gated by `original_tag = TAT` and `is_independence_wave_tat_package = yes`; the full available focus pool, prerequisites, bypasses, mutual exclusions, route flags, and package state were not resolved by the empty fixture.

## Named scenarios and evaluation

Scenario set id: `TAT_IW044_CURRENT_EMPTY_2026_08_13`.

Scenario ids: `TAT_FOUNDING_PEACE`, `TAT_FORMER_HOST_THREAT`, `TAT_LEDGER_STABLE_ROUTE_LOCK`, `TAT_NETWORK_READY`, `TAT_RESOURCE_STARVED_RESERVE_FLOOR`, and `TAT_IMPOSSIBLE_FORMABLE_AMBITION`.

The candidate pool supplied to the evaluator was complete relative to the 11 mission IDs discovered by inspection. Each scenario intentionally used `state = {}` because typed campaign fixture fields were not accepted by the recovered route. Therefore the runtime-available pool and external factors were incomplete, and no exact selection probability is claimed.

`hoi4.probability_evaluate` with adapter `mission_ai_will_do`, raw-value metrics, a 600-day horizon, and the six scenarios returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-e7ee0794c9e0e46a0bbb0e9b`, source revision/hash matching the inspection, scenario hash `8b3e849d966de6b970eebe84e8a968b235f58d5c67867d13048ef4cba095f763`, 66 candidate/scenario rows, 116 unresolved items, and 11 diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96053937bac4339b88c5a9be15e29823795def47503e65c3a26da842b7b0225d/26042b0bf2e292b219d69ed6080f21af1e2fbe34f2dafc4accbd3d9551a44300/probability-e7ee0794c9e0e46a0bbb0e9b.json`.

All 11 candidates were reported `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` across the empty fixtures. This is exact only for the supplied empty fixtures and is not evidence that any mission is permanently impossible in a live campaign. The adapter withheld normalized probabilities.

### Rendered evaluation evidence

- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dcc00958432a892fa9e8bf45987a60d626607c69248a6f717f6ced49f1eba33/002b069f3bb86574479a724aedae359e6b0215dda4ae1b362c21eb9cfbfce37a/probability-probability-e7ee0794c9e0e46a0bbb0e9b-ranking.svg`.
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73394381cdc42a58706420883b7ea6a7c009530238f4ebe3ba011a7205621221/c9081a0844b57d45578406af8603282ab7c19e3bab9c650f42c45e25c502766b/probability-probability-e7ee0794c9e0e46a0bbb0e9b-ranking.png`.
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1141c18aa9c3b8efa89e7e53bbb13326625a3679c3c4e97aad21361e3e3831f0/e7acdb81c4a36ad8481a15d2bcfe177de387b12db48a813e11e2160add53d8d3/probability-probability-e7ee0794c9e0e46a0bbb0e9b-matrix.svg`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9e28d4193507909a10c518c8509aacc9034d96ef0d442caf490d422235c5801a/c1d767fcda3135fe96095faf24febce9a5e4c14a9ca8e2d5f80ddffc2f4fc8d2/probability-probability-e7ee0794c9e0e46a0bbb0e9b-unresolved.svg`.

### Current/current comparison

`hoi4.probability_compare` used the same current TAT source on both sides, the same 11-candidate pool, and the same six scenarios. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-ed3f59fbffe8d741b6a5ff91`, scenario hash `8b3e849d966de6b970eebe84e8a968b235f58d5c67867d13048ef4cba095f763`, 116 unresolved items, 11 diagnostics, and `comparisonChanges=0`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c80980a1db36798d4c5c27b6d28bf1b6d9837aca1c309b2ac5293f09ba1eedea/df95b1a1fa344ca85b63891c7e539df249ec60fe67ab9124a0d94941ca3e2059/probability-ed3f59fbffe8d741b6a5ff91.json`. Comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/5960c8467c38e4e5e4c82ffb30be0771306c2c39021f7212e6d19c718727737b/probability-probability-ed3f59fbffe8d741b6a5ff91-comparison.svg`.

This is a capability/current-current receipt only, not evidence of a before/after balance change.

### Sweep blocker

The requested `hoi4.probability_sweep` over `state.has_war` and `state.has_independence_wave_severe_host_threat` returned the exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED` for `TAT_FORMER_HOST_THREAT/state.has_war`: every sweep path requires a scenario range, numeric alternatives, or numeric state value. No sensitivity, threshold, or rank-reversal result is claimed.

## Structural MCP evidence

`hoi4.focus_inspect` on `independence_wave_focus_tree` returned `FOCUS_INSPECTED`, revision `381140acd320a1be19bab9d19285c85165412d71eba85e04be4c9f3027179eb1`, 184 focuses, 206 connectors, zero connector crossings, zero node intersections, and 12 long connectors. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a2683548930c07d7818181c7e4e32d72e46c8531235859a4736c061b8613531/09034164f27392fc1fbc251531f8845f8ed42268d815ce3da9895088cdd8bf9e/focus-inspect.381140acd320a1be.json`.

`hoi4.focus_render` returned HTML/SVG/JSON artifacts with layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`; SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c51a07eee7fcbe60e40231211902e20aa68aff6e2313b7484db6ee1705a5bf19/8f5105e6ba58d35db6fd73dd5a11d3aa64c1cb6d99484a92040aa31bb57df6bc/independence_wave_focus_tree.focus.svg`.

Focus structural evidence does not replace the unresolved focus probability pass. The inspect also reported 14 blocking diagnostics, including three unrelated vanilla continuous-focus icon errors and layout warnings; no focus rewrite was run.

## Score-only source trace

The TAT mission source uses the shared decision constants `standard = 10`, `high = 25`, `urgent = 100`, and `modifier_double = 2` from `common/script_constants/006_independence_wave_decision_constants.txt`.

- Founding compact mission: urgent base, but `available = { always = no }`; it is a lifecycle mission and must not be treated as a clickable selection.
- Depot security, community compacts, constitutional autonomy, durable sovereignty: high base.
- Border-guard integration: high base, doubled while `has_war = yes`.
- Former-host settlement: standard base, doubled when `NOT = { has_independence_wave_severe_host_threat = yes }`; its availability also requires former-host validity/peace or the designed fallback path, depot state, unsettled-host state, capital/package gates, and cost/active-project gates.
- Agrarian compact and network corridor: standard base.
- Socialist councils: high base.
- River emergency command: urgent base, doubled while `has_war = yes`.

These are willingness scores, not probabilities. The MCP did not prove which candidate wins the score race after all availability and external factors are populated.

## Findings and implementation-ready acceptance targets

1. No live-balance conclusion is proven. The empty fixtures make every mission never-eligible in the supplied scenarios, while `poolComplete=false` and zero available candidates prevent normalized ranking or timing claims.
2. No strategy-factor conclusion is proven. `ai_strategy_factor` returns no weighted surface for the four source strategy blocks, so activation, overlap, war-restraint dominance, and starvation remain unresolved.
3. No focus-race conclusion is proven. The shared focus adapter discovers 184 source candidates but no available candidates under the empty fixture.
4. Source gating is materially non-flat and route-aware: urgent/high/standard tiers, war-sensitive doubling, former-host-threat inversion, route exclusivity, founding/settled/network gates, capital/state control, cost affordability, active-project serialization, and cleanup gates are all part of the candidate validity contract.
5. A next AI tranche should first supply typed fixtures for the six named scenarios. Each fixture must declare TAT setup/package identity, phase, state-249 ownership/control and capital control, both ledgers and thresholds, route flags/government, project readiness, cost/civilian-factory affordability, active-project/cooldown state, former-host existence and war state, severe-host-threat state, founding settlement and compact resolution, network/League membership, ambition/formable validity, and reserve-floor/resource state.
6. After fixture support, rerun `probability_evaluate` with the same scenario IDs and complete 11-entry pool; classify results as exact, bounded, score-only, sampled, or unresolved. Use `probability_sweep` only with explicit boolean/numeric alternatives for `has_war` and severe-host threat, and preserve any range-required blocker.
7. Any owner-applied source change requires a true before/after `probability_compare` using the same six scenario IDs and candidate pool. The current/current comparison above must not be presented as a balance improvement.
8. Do not claim AI starvation, dominance, rank reversal, repetition, unsafe snowball, or exploit safety until the adapters expose complete available pools and state transitions. Do not hand-calculate probabilities.

## Skipped analyses and blockers

- `probability_sweep`: blocked with `PROBABILITY_SWEEP_RANGE_REQUIRED`; no scenario ranges or numeric alternatives were accepted.
- `probability_simulate`: skipped because no uncertain-input distributions or seed were declared.
- `probability_sequence`: skipped because IW-044 does not provide a complete custom weighted-pool manifest with cadence, cooldown/recovery, removal/reset, cap, timer, and terminal states for this audit.
- No exact probability, cumulative timing, rank reversal, dominance, starvation, repetition, or live-runtime AI claim is made.
- No source patch, tuning-number choice, attestation promotion, formable opening, super-event change, or runtime validation was performed.

No simplification or gameplay fallback was applied; this handoff remains bounded pending typed fixture and adapter support.
