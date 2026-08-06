# IW-026 Macedonia weighted-logic audit — current source — 2026-08-06

## Scope and verdict

This is a read-only HOI4 MCP probability audit of `common/ai_strategy/006_independence_wave_macedonia.txt` and `common/decisions/006_independence_wave_macedonia_decisions.txt` for Event 006 IW-026 Macedonia.

The decision and mission sources are parser-clean and expose one ordinary decision plus eleven mission candidates, but both runtime pools are incomplete without typed MAC world state.

The MAC `ai_strategy_factor` adapter is unavailable for this source and returned the exact blocker `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`.

No strategy ranking, normalized mission selection probability, live-AI timing, dominance, starvation, rank-reversal, repetition, or exploit-safety claim is justified by this audit.

The package can be source-attested for weighted-surface discovery only; typed-AI evidence remains blocked and the balance gate stays HOLD/PARTIAL.

No gameplay, AI, decision, mission, strategy, localisation, effect, trigger, or runtime file was changed.

## Current source identity

The workspace was `mod_chaos_redux_ea3b2d67c2c0` and the repository HEAD when inspected was `554f676d3764323172317f9ccb7cb889a213a717`.

| Source | Local raw SHA-256 | MCP source revision | MCP source hash |
| --- | --- | --- | --- |
| `common/ai_strategy/006_independence_wave_macedonia.txt` | `0c682be6f779ee08e1a00e8be47bdc2b5df8ff3ffed478440449421ed7e140d4` | unavailable because the adapter found no surface | unavailable |
| `common/decisions/006_independence_wave_macedonia_decisions.txt` | `bedea3b3850ad65b1d9e3a7f1735770d34c7dc931f01288a15d39677a8ebce21` | `604872d115d06176a88558e06b324b56892ee273e79091d5df76fe357c8a973e` | `9d4afb0135117104c8e7624dc132730cf50e390737cc74b8a6bedf13861c59cf` |

The MCP source identity is the authoritative identity for the probability artifacts; the local raw hashes are recorded only to tie the read-only receipt to the current worktree.

## Weighted surfaces and MCP inspection

### MAC strategy factors

The mandatory call was `hoi4.probability_inspect` with adapter `ai_strategy_factor` and source `{ "path": "common/ai_strategy/006_independence_wave_macedonia.txt" }`.

- Result code: `PROBABILITY_SURFACE_EMPTY`.
- Status: `error`.
- `filesScanned`: empty.
- `diagnostics`: empty.
- Artifacts: none.
- Exact blocker: `No weighted blocks matched this request` with `adapterId = ai_strategy_factor`.

This is an adapter-discovery failure, not evidence that the source has no AI strategy blocks.

### MAC ordinary decision AI

The mandatory call was `hoi4.probability_inspect` with adapter `decision_ai_will_do` and source `{ "path": "common/decisions/006_independence_wave_macedonia_decisions.txt" }`.

- Result code: `PROBABILITY_SOURCE_INSPECTED`.
- Validation: passed.
- Discovered candidates: `1`.
- Required inputs: `10`.
- Unresolved source diagnostics: `0`.
- `poolComplete`: `false` because runtime eligibility is state-dependent.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d1ad65fae9e8c9db7110fa565acd255179fe2f11e84a615b5ca38cb16c6186ed/b9712e77f622559238f7674edaad19c8dd768edd8ed7aab6f0458ce58099755d/probability-inspect-9d4afb013511.json`.

The single discovered ordinary decision is `independence_wave_mac_codify_vardar_settlement`.

### MAC mission AI

The mandatory call was `hoi4.probability_inspect` with adapter `mission_ai_will_do` and the same source path.

- Result code: `PROBABILITY_SOURCE_INSPECTED`.
- Validation: passed.
- Discovered candidates: `11`.
- Required inputs: `13`.
- Unresolved source diagnostics: `0`.
- `poolComplete`: `false` because runtime eligibility is state-dependent.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2403be674528a7719f4e4f1596c11b30e3f3aa4af8262489c71142c854c793d/b55393c502718f3a760427e217ea6e4eb8937ae361b076e342d8016f098fddae/probability-inspect-9d4afb013511.json`.

The complete declared mission candidate pool supplied to evaluation was:

`independence_wave_mac_hold_vardar_council_together`, `independence_wave_mac_reopen_vardar_depots`, `independence_wave_mac_screen_veteran_networks`, `independence_wave_mac_convene_community_council`, `independence_wave_mac_settle_yugoslav_ledgers`, `independence_wave_mac_ratify_municipal_charter`, `independence_wave_mac_convene_mountain_workers`, `independence_wave_mac_restore_village_autonomy`, `independence_wave_mac_establish_mountain_commission`, `independence_wave_mac_accept_rail_patron_compact`, and `independence_wave_mac_open_danube_network`.

The decision evaluation pool contained the one discovered ordinary decision.

## Named scenarios and evaluation evidence

All named scenarios below intentionally used `state = {}` because the installed adapter cannot safely infer MAC package state from prose and no typed fixture was supplied.

The empty state means that package identity, setup completion, capital control, former-host scope, ledgers, route flags, resource affordability, active-project lock, league phase, war state, cooldown state, and prior one-shot flags were not asserted.

### Decision scenario set

Scenario set: `E6_MAC_DECISION_SCENARIOS_CURRENT_2026_08_06_AUDIT`.

Scenarios: `MAC_FOUNDING_CALM`, `MAC_HOST_CRISIS`, `MAC_ROUTE_LOCKED`, and `MAC_NO_VALID_TARGET`.

Candidate pool: the complete one-entry ordinary-decision pool listed above.

Evaluation result:

- Result code: `PROBABILITY_ANALYZED_PARTIAL`.
- Analysis id: `probability-c4c55d64391410e432b56303`.
- Scenario hash: `4ba2163247e1ac8748d1da763f0fcfb9476765663d4cf17c25af8b6950dc4376`.
- Four scenarios and four candidate rows.
- `17` unresolved or bounded items.
- One diagnostic: `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for `independence_wave_mac_codify_vardar_settlement` across all four supplied scenarios.
- Classification: bounded, score-only, and partial; not an exact selection probability.

Evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1aa797c7d5bbd34b7009a56416c21c4b9bc37ffa49db4a1f856197e17b02046/97bd81f7bc8cbea40217e3aa8657017d951675bb5fb659244d1fc95a04425b6/probability-c4c55d64391410e432b56303.json`.

Rendered decision ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b8c654d524456d78be18f8c83ccd4eb60b9f0ada3e2c454c5e63dcda2d0de66/8196c0e06fd9b69822966fdffabb275d2329281f5e18312d2a923bdff995865e/probability-probability-c4c55d64391410e432b56303-ranking.svg`.

Rendered decision unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/319e23fa23d5ef2d446bb63dd70e19c8863d68061119c2110658eec92613c532/166fbc23fbd6a2841e5bccc6a8a7b97d033ddcc1524305120778813696181a63/probability-probability-c4c55d64391410e432b56303-unresolved.svg`.

### Mission scenario set

Scenario set: `E6_MAC_MISSION_SCENARIOS_CURRENT_2026_08_06_AUDIT`.

Scenarios: `MAC_FOUNDING_CALM`, `MAC_HOST_CRISIS`, `MAC_ROUTE_LOCKED`, and `MAC_NO_VALID_TARGET`.

Candidate pool: the complete eleven-entry mission pool listed above.

Evaluation result:

- Result code: `PROBABILITY_ANALYZED_PARTIAL`.
- Analysis id: `probability-0aed88e4788e810660967a16`.
- Scenario hash: `3d8d1bf109cd84ad80e80dcf4f60d55c15f5c7748c7499f2f0f9ddff3de49fdb`.
- Four scenarios and forty-four candidate rows.
- `64` unresolved or bounded items.
- Diagnostics: `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for `independence_wave_mac_hold_vardar_council_together` and `independence_wave_mac_open_danube_network` across all four supplied scenarios.
- Classification: bounded, score-only, and partial; not a normalized mission-selection probability or timing distribution.

Evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f83666f02c264317f79b054c12c671f1bfe584cfa063a058c299ef9fa580707f/2e0739e71ad3faa6cc5d560e082946fe27b6f03121cf3be1ea37f8543267ae2a/probability-0aed88e4788e810660967a16.json`.

Rendered mission ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2eedab24a05993e11021f334f48a3dd3f84e9266fe0f7c04fc556e4665bffab/b694d8e4e77ec31eea6dbc74ed14d30be3ec82a10426829abb2a23766238384a/probability-probability-0aed88e4788e810660967a16-ranking.svg`.

Rendered mission unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf856bc4ee647bfa6f27ccf877f1e1248fcb6b27de094984676ee2bd1aacd376/a9657dfd0e9a1e35701d93e9e66fb1c6789a9913c8ef4587297ba5b3f17676ed/probability-probability-0aed88e4788e810660967a16-unresolved.svg`.

The passive founding mission intentionally uses `available = { always = no }`, so its never-eligible warning in an empty typed state is not proof of starvation or a broken AI action.

The Danube warning is also not a source conclusion because its package, stable-ledger, network-member, league-route, live-league-phase, capital-control, cost, and active-project gates were not represented in the supplied state.

## Same-source comparison and sweep status

### Same-source comparison

`hoi4.probability_compare` used adapter `mission_ai_will_do`, the same MAC source path as both `before` and `after`, the complete eleven-entry pool, and scenario set `E6_MAC_MISSION_COMPARE_SCENARIOS_CURRENT_2026_08_06_AUDIT` with the same four scenario ids and empty states.

- Result code: `PROBABILITY_ANALYZED_PARTIAL`.
- Analysis id: `probability-542f36abadbd376e171057ff`.
- Scenario hash: `34ae0f47d01e22a717c3581d6027c013032508b100128d3e86b8391fb31b4caf`.
- Four scenarios, forty-four candidate rows, `64` unresolved items, and two never-eligible diagnostics.
- `comparisonChanges = 0`.

This is a same-source capability receipt, not a before/after patch comparison and not evidence that the weights are balanced.

Rendered comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/bea0682975d174c8f91cb53b01c3add5930d580891544adbd1afdc8f5d8638da/probability-probability-542f36abadbd376e171057ff-comparison.svg`.

### Sweep

The required sensitivity/rank-reversal pass was attempted with adapter `mission_ai_will_do`, the complete eleven-entry pool, the four named MAC scenarios, and sweep path `state.war_support` with `findRankReversals = true`, `pairwise = true`, and three steps.

- Exact result code: `PROBABILITY_SWEEP_RANGE_REQUIRED`.
- Exact blocker: `Every sweep path requires a scenario range, numeric alternatives, or numeric state value`.
- Details: `scenarioId = MAC_FOUNDING_CALM`, `path = state.war_support`.
- Artifacts: none.

No threshold, sensitivity, or rank-reversal conclusion is made.

## Source-level score and validity review

The following are source facts only and are not normalized probabilities.

### AI strategy layers

`independence_wave_mac_vardar_survival` is allowed only for `original_tag = MAC` and enables when the MAC package, IW-026 setup, and MAC AI profile flags are present.

Its strategy values are `build_army = 92`, infantry production factor `36`, artillery production factor `20`, support production factor `48`, infrastructure construction `68`, and bunker construction `86`.

`independence_wave_mac_host_restraint` enables for a living former host while host ledgers are unsettled and applies `avoid_starting_wars = -235`.

`independence_wave_mac_settled_vardar` enables after `independence_wave_mac_compact_stabilized` and applies `build_army = 108` plus `avoid_starting_wars = -430`.

`independence_wave_mac_emergency_commission` enables after `independence_wave_mac_emergency_government` and applies `build_army = 118` plus bunker construction `86`.

All four layers use `abort_when_not_enabled = yes`.

Offline AI guidance states that negative AI-strategy values reduce desire and that strategy values modify downstream AI scores; it does not turn these factors into a click probability.

The adapter did not expose any of these layers, so overlap between survival, settled, emergency, and former-host states cannot be ranked or timed by MCP.

### Decision and mission willingness blocks

`independence_wave_mac_codify_vardar_settlement` is the only ordinary decision candidate and uses the shared `independence_wave_decision_ai.high` base.

The eleven mission blocks use shared `urgent`, `high`, or `standard` bases, with wartime `modifier_double` on veteran-network screening and the emergency mountain commission, a doubled former-host settlement score when the severe-host-threat trigger is absent, and standard/high scores on the remaining route, administration, diplomatic, network, and settlement actions.

The source has package, capital-control, route, former-host, cost, one-active-local-project, one-shot, cancellation, and `fire_only_once` gates in the relevant blocks.

These gates prove intended AI validity structure at source level, but the MCP scenarios did not supply the values and scopes needed to prove any candidate eligible or ineligible in live play.

## Balance-risk classification

| Risk surface | Evidence classification | Finding |
| --- | --- | --- |
| Strategy dominance | unresolved | `ai_strategy_factor` returned `PROBABILITY_SURFACE_EMPTY`; no strategy ranking exists. |
| Decision dominance | bounded/score-only | The ordinary adapter exposes one candidate, so no ordinary-decision race is available to rank. |
| Mission dominance/starvation | bounded/score-only | Eleven candidates were declared, but runtime eligibility and external factors are incomplete. |
| Rank reversal | unresolved | Sweep was blocked by `PROBABILITY_SWEEP_RANGE_REQUIRED`. |
| Timing distribution | unresolved | No complete timing state, MTTH surface, or mission cadence model was supplied. |
| Repetition/farming | unresolved by probability | Source has one-shot flags and local active-project guards, but live cleanup and cross-system concurrency were not modeled by this probability pass. |
| Exploit risk | unresolved by probability | Cost/resource, route withdrawal, capital control, former-host, and league-phase transitions require typed runtime fixtures. |

The `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` warnings for the passive founding mission and Danube network action are diagnostics of the empty submitted states, not proof of permanent source starvation.

## Recommendations to the owner

1. Keep numeric strategy tuning blocked until a supported `ai_strategy_factor` adapter or explicit typed strategy manifest can evaluate the four MAC layers under named package, host, compact, emergency, war, and settled states.
2. Provide a typed scenario fixture for MAC package identity and setup completion, anchor state 106 ownership/control, former-host existence and war, civic/defence ledgers, route flags, government flags, resource affordability, active-project decisions, one-shot flags, and global league phase.
3. Re-run the same named decision and mission scenario ids with populated states, then run `hoi4.probability_sweep` with declared numeric ranges for the actual tunable inputs and `findRankReversals = true`.
4. Run a real `hoi4.probability_compare` only after an owner-applied source change and an approved baseline snapshot are available; reuse the same scenario ids and preserve the scenario hash.
5. Treat the package as source-attested weighted-surface discovery, not balance-complete AI evidence, until these typed MCP blockers are closed.

## Skipped analyses and exact reasons

- `hoi4.probability_simulate` was not run because no uncertain input distribution, confidence target, sampling method, or seed was declared; simulation cannot replace missing package scopes.
- `hoi4.probability_sequence` was not run because no complete declared custom weighted pool, cadence, cooldown/recovery, cap, removal/reset, timer, or terminal-state contract exists in the scoped source.
- No direct-random or custom weighted-pool surface was found in the two scoped files.
- No event, focus, GUI, technology, or doctrine structural MCP call was applicable to this AI-strategy/decision-only scope.
- No live Hearts of Iron IV process was launched.

## Files changed

Only this audit handoff was added:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw026_macedonia_probability_audit_current_2026_08_06.md`

No gameplay or runtime file was edited.
