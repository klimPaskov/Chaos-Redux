# IW-038 Ruthenia weighted-logic final audit

Audit date: 2026-08-10.

Scope: read-only weighted audit of the current Event 006 IW-038 Ruthenia mission/decision surface, the RUT AI-strategy source, and the five RUT helper hooks in the shared national-focus tree. No gameplay source, AI source, decision source, focus source, localisation, asset, or runtime file was changed. No staging or commit was performed.

## Disposition

The source is structurally gated and fail-closed, but quantitative balance is unresolved. The mission adapter discovers the complete eleven-entry RUT timed-project pool and the focus adapter discovers the five audited hook nodes when their scoped candidate pools are supplied. Both scenario evaluations are partial because the declared scenarios used explicit empty `state = {}` records: package identity, setup flags, ledgers, capital ownership, resources, route flags, host relation, network phase, and focus prerequisites were not typed into the MCP fixture. The AI-strategy adapter has no recognized weighted surface. The same-source compare is a capability receipt only (`comparisonChanges=0`), not a before/after balance proof.

## Audited source surfaces

| Surface | Source and identifiers | Source review |
| --- | --- | --- |
| RUT mission and project AI | `common/decisions/006_independence_wave_ruthenia_decisions.txt:15-568`; category `independence_wave_rut_mountain_compact_category`; eleven IDs listed below | One passive founding mission plus ten serialized paid projects. Mission AI scores use the shared `independence_wave_decision_ai` constants. |
| RUT strategy factors | `common/ai_strategy/006_independence_wave_ruthenia.txt:21-70`; `independence_wave_rut_mountain_survival`, `independence_wave_rut_host_restraint`, `independence_wave_rut_settled_compact`, `independence_wave_rut_emergency_guard` | Four guarded strategy layers are present in source, but the installed `ai_strategy_factor` probability adapter recognizes no weighted blocks. |
| Five RUT focus hooks | `common/national_focus/006_independence_wave_focus.txt:99-184`, `:1402-1418`, `:1672-1688` | The five helper calls are guarded by `original_tag = RUT` and `is_independence_wave_rut_package = yes`; no RUT-owned focus node or additive tree is introduced. |
| Gating dependencies | `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt:8-202`; shared cost triggers in `common/scripted_triggers/006_independence_wave_decision_triggers.txt:233-280` | Package identity, setup, crisis failure, stable compact, route-government, capital, host, network, league, active-project, resource, and settlement gates are source-visible but not all representable in the typed MCP scenario fixture. |

## Candidate pools and source inspections

The workspace reported `mod_chaos_redux_ea3b2d67c2c0`.

### Mission adapter

The canonical candidate pool supplied to every mission evaluation and compare was:

`independence_wave_rut_hold_mountain_compact_together`, `independence_wave_rut_secure_mountain_depots`, `independence_wave_rut_integrate_border_guards`, `independence_wave_rut_register_community_compacts`, `independence_wave_rut_settle_former_host_ledgers`, `independence_wave_rut_ratify_constitutional_autonomy`, `independence_wave_rut_adopt_agrarian_compact`, `independence_wave_rut_convene_socialist_councils`, `independence_wave_rut_establish_mountain_emergency_command`, `independence_wave_rut_codify_durable_sovereignty`, and `independence_wave_rut_open_carpathian_network_corridor`.

`hoi4.probability_inspect` with adapter `mission_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `6588b3da4828ee0383f597dc0db437239d74b4a09aa4c6ee9dea15eabc21ba8e`, source hash `108598448343f3734ae41acbb1c2ab43280748b5755a0c74a50aed4102df8c77`, eleven candidates, `poolComplete=true`, fifteen required inputs, and zero unresolved inspect items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d95740b5b72653098d1866346dfe8abec0efe4e20e8404eab45229a2b8890657/1fa733801fbdab75ce2a32ebe6aed3a6a2c6cbdfa900b1f28b16db8692f1dc78/probability-inspect-108598448343.json`.

The same source requested with adapter `decision_ai_will_do` returned `requested_adapter_empty` and suggested `mission_ai_will_do`; no ordinary `ai_will_do` decision candidate is exposed because every selectable RUT project has `days_remove` and is classified by the adapter as a mission. The passive founding mission is included in the mission pool and has `available = { always = no }` by design.

### AI-strategy adapter

`hoi4.probability_inspect` with adapter `ai_strategy_factor` against `common/ai_strategy/006_independence_wave_ruthenia.txt` returned `PROBABILITY_SOURCE_DISCOVERED`, discovery reason `no_weighted_surfaces`, source revision `760110344e054f6aa11fdf3c0dcb63f81722af6ba27f2dd95ae104eef09d87c4`, source hash `9a8e1fd82c852791e595f60ede20ea3071dfd1fea3636031807225d190a3b64e`, zero candidates, zero required inputs, and zero unresolved items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f36eca3f68dbb563304c5723f1cb262d72229eb32ec5a56bc1c93731a9f6d5a9/cde96607b697c6f06696fc4bce41520efec2ebc3396e0f2c37d46cc537887f27/probability-inspect-9a8e1fd82c85.json`.

The required `hoi4.probability_evaluate` retry for this adapter returned the exact blocker `PROBABILITY_SURFACE_EMPTY` with message `No weighted blocks matched this request`. No normalized strategy probability, strategy ranking, dominance, or starvation claim is possible from this adapter.

### National-focus adapter

The scoped candidate pool for this audit was the five focus nodes that contain RUT helper calls:

`independence_wave_prepare_capital_administration`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states`.

`hoi4.probability_inspect` with adapter `national_focus_ai_will_do`, this five-ID pool, and `common/national_focus/006_independence_wave_focus.txt` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `579d829e4947a23487d3d80052484fe845db23c8584e0f7444f2a1955e4ffc1e`, source hash `b99f27a367d6760b97059253bc6f04d734698ca296755e800e6c790b47b4bfa2`, five candidates, `poolComplete=true` for the declared hook scope, five required inputs, and zero unresolved inspect items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f77ab04f519688121ccc34300d9e199c8c813a81e78e44c64ec222fc2a3bd69f/13a6b7ca0b7a66c2728e516e6d061da0832c15c7f2f21bbe5b6bb3ff2bf086b5/probability-inspect-b99f27a367d6.json`.

The first unscoped focus inspection returned `INTERNAL_ERROR`; the narrowed five-ID retry succeeded. This is retained as an MCP capability limitation for unscoped shared-tree discovery, not as a source conclusion.

## Scenario contract

Scenario set ID: `E6_IW038_RUT_WEIGHTED_SCENARIOS_CURRENT_2026_08_10`.

The same six scenario IDs and candidate pool were used for the mission evaluation, focus evaluation, and current/current mission compare:

| Scenario ID | Intended campaign state | Declared external state | Completeness |
| --- | --- | --- | --- |
| `RUT_FOUNDING` | Active IW-038 founding crisis before stable ledgers and route government | `state = {}` | Incomplete; package identity, setup, anchor, capital, ledgers, route, host, resources, and timer state unresolved. |
| `RUT_PROJECT_READY_PEACE` | Project-ready RUT in peace with living former host | `state = {}` | Incomplete; readiness, affordability, former-host target, and war relation unresolved. |
| `RUT_PROJECT_READY_WAR` | Project-ready RUT at war | `state = {}` | Incomplete; `has_war`, capital control, security resources, and route state unresolved. |
| `RUT_HOST_LOSS_FALLBACK` | Former host gone or at war, with local fallback expected only after depots | `state = {}` | Incomplete; host existence/war, depot flag, unsettled ledger, and capital state unresolved. |
| `RUT_ROUTE_LOCKS` | Each of four route flags tested against the one-government lock | `state = {}` | Incomplete; constitutional/traditional/popular-council/emergency flags and government flags unresolved. |
| `RUT_NETWORK_READY` | Founding settlement, crisis resolution, stable compact, network member, and league route available | `state = {}` | Incomplete; all settlement/crisis/stability/network/league/capital/cost inputs unresolved. |

The empty states are intentional disclosure of the adapter limitation. They do not assert that any package or route gate is true, and they cannot be used to claim exact eligibility or probability in a live campaign.

## Mission evaluation

`hoi4.probability_evaluate` used adapter `mission_ai_will_do`, the complete eleven-entry pool, the six scenarios above, `metrics = [raw_value]`, and a 600-day horizon. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-e2009ec2891aa9559706fa13`, source revision `6edf2cfeb997b07ac2f343f2086934e718856cb0e71399b60b343a12eb96568c`, source hash `108598448343f3734ae41acbb1c2ab43280748b5755a0c74a50aed4102df8c77`, scenario hash `d728411c97a5b7c6bc07922a6bf660ba47697f10fbb1b8b29574fab19390a72a`, 6 scenarios, 66 candidate rows, 116 unresolved items, and 11 diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e659ecf25469357dd37bc845f340f91cb66a137f6673c9f9b93320d1afe1dd5f/7c1e8ad42cdb89d930500eddef8c4b62b159c7eefd2f00bdd16053bdc2a846c7/probability-e2009ec2891aa9559706fa13.json`.

The analyzer emitted `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for all eleven mission IDs across the empty-state scenarios. This is an adapter result under the empty fixture, not proof that the RUT projects are dead. The founding mission's `available = { always = no }` is a deliberate passive-mission contract and should not be treated as AI starvation. The ten paid projects are serialized by `has_independence_wave_rut_active_package_project`, capital control, project readiness, resource affordability, one-shot completion flags, route locks, and crisis-failed cancellation gates.

Rendered resources emitted by the evaluate call included ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac5ab77703d039ab4c8206fa6f343221aa8bba97a93890dd8e92305351b46fcd/58b9280ae2069067bd57b4a920af5ce0fe711382a9bbb99f6746db3701cdb064/probability-probability-e2009ec2891aa9559706fa13-ranking.svg` and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df45b35b51a064d52bbc06c5996dfc121b4178b50654bd1876e95f062b84786c/399832e38a02901ffa9c0b32135d009bdb248753c0475ed167c96d418ce5bcc4/probability-probability-e2009ec2891aa9559706fa13-unresolved.svg`.

## Focus evaluation

`hoi4.probability_evaluate` used adapter `national_focus_ai_will_do`, the five-hook pool, the same six scenarios, raw-value metrics, and the 600-day horizon. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-11277a3906f0cb314b7a1f4d`, source revision `d0ff232d39693403643b9ce27c7bea329d6f0ac1151950180210b7dd53f93458`, source hash `b99f27a367d6760b97059253bc6f04d734698ca296755e800e6c790b47b4bfa2`, the same scenario hash `d728411c97a5b7c6bc07922a6bf660ba47697f10fbb1b8b29574fab19390a72a`, 6 scenarios, 30 candidate rows, 20 unresolved items, and 5 diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86d720129b149449154048245c9ed6309478b84b534eb94c0f93cb60a331686a/87eb9965d088f1858d0040c72bf30853400bedf31f716a40cf569c7b9af4fbc5/probability-11277a3906f0cb314b7a1f4d.json`.

The analyzer emitted `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for all five hooks under the empty state. This does not mean the shared focuses are unreachable in game. Source review confirms the normal `can_use_independence_wave_full_focus_framework` gate, focus prerequisites, and package helper guards. The focus adapter models a score race among available focuses, not weight divided by the sum of weights; because the complete shared-tree candidate pool was intentionally narrowed to the five RUT hook nodes, no whole-tree focus ranking or selection probability is claimed.

Rendered resources emitted by the evaluate call included ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34ae028c12e7fcd15a237b962d5999dc81bc486a473fdc9b55104c1407191967/843503e2b2c609603d1fcd37089d1dfc4e104d29fc9acdfa686477dee1c4a4b6/probability-probability-11277a3906f0cb314b7a1f4d-ranking.svg` and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa04efa4272b4400e2f79e9f7a9b77922f0b599322f496c604d5d090d0ed979f/25280ad0ab5e7c4231dc57d0b139fa5881e1ec833b21336eb4073af8705ac7db/probability-probability-11277a3906f0cb314b7a1f4d-unresolved.svg`.

## Strategy and score traces

The strategy source is score evidence only. Exact authored values from `common/ai_strategy/006_independence_wave_ruthenia.txt` and `common/script_constants/006_independence_wave_ruthenia_constants.txt` are:

| Strategy layer | Source score(s) | Runtime gates |
| --- | --- | --- |
| `independence_wave_rut_mountain_survival` | `build_army = 86`; infantry production `40`; artillery `24`; support `50`; infrastructure `70`; bunker `82` | `original_tag = RUT`, active package, IW-038 setup complete, RUT AI profile. |
| `independence_wave_rut_host_restraint` | `avoid_starting_wars = -260` | Active package, setup complete, living former host, host ledgers unsettled. |
| `independence_wave_rut_settled_compact` | `build_army = 86`; `avoid_starting_wars = -430`; infrastructure `70` | Active package and `independence_wave_rut_compact_stabilized`. |
| `independence_wave_rut_emergency_guard` | `build_army = 118`; bunker `82` | Active package and emergency government. |

The `corridor_priority = 84` constant exists in `006_independence_wave_ruthenia_constants.txt:90` but is not consumed by the RUT strategy file. This is a source-level tuning mismatch, not an MCP probability result. Either wire it through an owner-approved strategy factor or document it as intentionally unused.

Decision score bases are exact source constants: urgent `100` for the passive founding mission and emergency command, high `25` for depots, guards, communities, constitutional autonomy, socialist councils, and durable sovereignty, and standard `10` for former-host settlement, agrarian compact, and Carpathian network. War doubles border-guard and emergency-command scores. Former-host settlement doubles when severe host threat is absent. Focus score bases are urgent `100` for the three opening hooks, high `25` for former-host and network hooks, with a `1.5` prerequisite boost on the latter two; the opening root adds a `4` multiplier under severe instability and the oath adds a `2` multiplier during war. These are willingness/score traces, not click probabilities.

## Sweep and compare

The required mission sweep used the complete eleven-entry pool, the six named scenarios, path `state.war_support`, three steps, pairwise sensitivity, and rank-reversal search. MCP returned the exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED` with details `scenarioId = RUT_FOUNDING`, `path = state.war_support`, and message `Every sweep path requires a scenario range, numeric alternatives, or numeric state value`. No threshold, sensitivity, or rank-reversal conclusion is made. A retry with numeric `war_support` values in the scenario state was rejected by the same blocker because the adapter did not recognize those untyped fixture fields.

The mandatory current/current capability compare used adapter `mission_ai_will_do`, both `before` and `after` as `common/decisions/006_independence_wave_ruthenia_decisions.txt`, the same eleven-entry pool, the same six scenario IDs, and the same scenario hash. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-51c96259bef4fc3beeb629a0`, source revision `d0ff232d39693403643b9ce27c7bea329d6f0ac1151950180210b7dd53f93458`, source hash `108598448343f3734ae41acbb1c2ab43280748b5755a0c74a50aed4102df8c77`, 66 rows, 116 unresolved items, 11 diagnostics, and `comparisonChanges=0`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/228258e7427cc812373f563cd7133f783dee32c25c41b6e9cda4c427e2d7373b/bb1fc25b23095bead3c6a9432aeeb4032687c8add706864391e315af96fc605b/probability-51c96259bef4fc3beeb629a0.json`. Comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/17b7f244eec4cca5b2fd2f581130e9a61ab257fd7c5fa744443fd0e738cdf792/probability-probability-51c96259bef4fc3beeb629a0-comparison.svg`.

This compare proves only that the installed compare route can process identical current sources under the declared scenario contract and sees zero source delta. It is not evidence that the source is balanced, and there is no accepted historical baseline for IW-038.

The follow-up `hoi4.probability_render` requests returned `PROBABILITY_ANALYSIS_STALE` after the workspace revision advanced. Their exact warning was `Workspace sources changed after this analysis; run the analysis again before rendering`, with mission analysis revision `6edf2cf...` versus current revision `e4c7f570...`, and compare analysis revision `d0ff232...` versus current revision `43a1d6e5...`. The evaluate and compare artifacts above remain valid receipts at their recorded revisions; do not present the stale render attempts as current rendered evidence. Focus render artifacts from the structural pass are current for the focus source snapshot recorded below.

## Structural focus MCP evidence

`hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, returned `FOCUS_INSPECTED`, revision `7c899015792852c37ca2b7ef0511bd9073545fbd522e2eb48a3e527d71ffa620`, 184 focuses, 193 connectors, layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, zero connector crossings, and zero node intersections. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a566e5cd10493ec2ed8c7248eb69fc73a1e7d1bd06d547add81fc8485092ae9a/b72822e1cd2d5755a7709250bf892528f27c9b36bec99c9923d8ffc1c0317694/focus-inspect.7c899015792852c3.json`.

`hoi4.focus_render` returned `FOCUS_RENDERED` with the same layout hash. SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/ce59ea33f611f19cb7826fa8ab6dfd84dba6a2a7257928d3784f3f215a79975d/independence_wave_focus_tree.focus.svg`; HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9181237deb74eb7421b6d49e6ed68c5a30acdf7fc0e0b0ad0a3693a9340095d/18f3c6d71d7c5163e711da78b3abd52fa7d5b5d30505b80d015cdba27679df46/independence_wave_focus_tree.focus.html`.

The structural pass reports fourteen diagnostics, all outside the five RUT hooks: nine missing installed-vanilla continuous-focus sprites and five shared-tree layout warnings. No diagnostic names a RUT focus node, helper, prerequisite, or route.

## Validity, dominance, starvation, repetition, and exploit-risk findings

- Source validity is fail-closed for package identity, setup, crisis failure, capital control, route government, stable ledgers, host war/fallback, network membership, league route, active project, costs, and one-shot completion flags. The adapter did not prove these gates under typed runtime state.
- The founding mission is intentionally passive (`available = { always = no }`) and uses an activation-backed timed crisis. Its never-eligible diagnostic in the empty fixture is not a starvation finding.
- Paid-project selection is not a normalized categorical probability in the current source. The ten projects have independent willingness scores and hard availability gates; no exact click probability is claimed.
- Route choice is mutually exclusive through `has_independence_wave_rut_route_government`. The four route projects have no positive score when their route flags are unavailable, but the adapter could not evaluate those flags.
- War multipliers correctly raise guard/emergency willingness, while host settlement receives a restraint multiplier when severe threat is absent. Whether these modifiers cause rank reversal or dominance in valid campaign states remains unresolved because sweep ranges and typed state are unavailable.
- Repetition is bounded by `has_independence_wave_rut_active_package_project` and completion flags. Durable sovereignty and Carpathian corridor completion flags prevent duplicate success rewards. The former-host fallback has separate depot/unsettled-host gates. These are exact source-level exploit protections, not probability evidence.
- No free-resource, repeatable unit, war-goal, core, or factory loop is visible in the audited weighted surfaces. The timed project costs and bounded failure effect are real resource exchanges; runtime balance still requires typed scenario evaluation.

## Recommended fixes (not applied)

1. Supply an approved typed scenario fixture for package identity, setup-complete, state-73 ownership/control, capital scope, civic/mountain ledger values, route flags/government flags, former-host existence and war, network/league phase, active-project state, resource affordability, and founding-settlement completion. Re-run the same six IDs and candidate pools.
2. Add a supported numeric range or alternatives for a real tunable input before rerunning `hoi4.probability_sweep`; retain `findRankReversals = true` and pairwise sensitivity. Do not infer thresholds from the failed `state.war_support` path.
3. Obtain an accepted pre-change source snapshot before requesting a real `hoi4.probability_compare`. The current/current receipt must remain labelled capability-only.
4. Decide whether the unused `independence_wave_ruthenia_ai.corridor_priority = 84` is intentional. If not, wire it through an owner-approved strategy factor and repeat inspect/evaluate/compare; if intentional, document the reason in the RUT AI source or package docs.
5. Keep the narrowed five-hook focus pool separate from any future whole-tree focus race. A whole-tree selection claim requires the complete available focus pool and route-aware state.

## Skipped analyses and exact reasons

- `decision_ai_will_do` evaluation: skipped after inspect returned `requested_adapter_empty` and suggested `mission_ai_will_do`; all selectable RUT projects were evaluated through the mission adapter.
- `ai_strategy_factor` probability evaluation: attempted and blocked exactly by `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`.
- Mission and focus sweeps: mission sweep attempted and blocked exactly by `PROBABILITY_SWEEP_RANGE_REQUIRED`; no valid numeric range was accepted. Focus sweep was not repeated after the shared range blocker because no supported numeric focus input was declared.
- Simulation: skipped because no uncertain input distributions or seed contract was declared and the typed state fixture is incomplete.
- Sequence: skipped because this source is not a declared custom weighted pool with a cadence/recovery/cooldown/removal/reset manifest; the timed project lifecycle is ordinary decision/mission state.
- Probability render retries: returned `PROBABILITY_ANALYSIS_STALE` after the workspace revision advanced. The stale warning is preserved above; no stale render is used as current evidence.
- GUI inspection/render: skipped because IW-038 uses the ordinary decision category shell and introduces no event-owned scripted GUI.
- Live HOI4 launch, save/load, and runtime consumer testing: not performed; repository rules reserve that validation for the user.

## Completion statement

This handoff is a read-only probability audit, not a balance approval. It proves the current source-level candidate pools, authored score traces, hard route/resource gates, and MCP adapter limitations. It does not prove exact selection probabilities, timing distributions, dominance, starvation, rank reversals, or campaign balance. No gameplay file was edited, staged, or committed.
