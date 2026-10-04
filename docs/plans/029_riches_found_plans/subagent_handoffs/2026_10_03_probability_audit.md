# Event 029 AI probability audit handoff

Date: 2026-10-03.

Disposition: `blocked` for MCP probability conclusions and same-scenario comparisons. The source review and scenario registry are complete for the bounded owner-patch surfaces below. The full 39-scenario probability pass is not complete, and no balance or probability claim is made.

The user authorized the full Event 029 scenario package, all 39 named Surface A–L scenarios, and Surfaces M/N. The user also directed the RF_FOREIGN distant-naval and empty-candidate comparisons and the RF_REPEATABLE_RECIPIENT_STATE_POOL stale-pointer case. This handoff preserves those inputs and the source evidence without selecting or changing weights.

## Scenario fixture and immutable source identities

The named scenario registry is [2026_10_03_scenarios.json](../evidence/2026_10_03_scenarios.json), SHA-256 `32f9d5f6f83a96436173a027bc93120c8d471cad970ded8bce051119b20a1183`. It contains all 39 original scenario IDs, the four named foreign scenarios, the supplemental `RF_FOREIGN_EMPTY_CANDIDATES` case, `RF_REPEATABLE_RECIPIENT_STATE_POOL`, and Surface M's ten accepted incident-pool families. The 39-ID count was read back from the saved JSON. No scenario hash exists because `probability_evaluate` and `probability_compare` did not return an analysis.

The six pre-edit snapshots were SHA-256 checked against `evidence/2026_10_03_reference_review.md` before source review:

| Source identity | Snapshot SHA-256 | Current source SHA-256 |
| --- | --- | --- |
| `events/029_riches_found.txt` | `618f87c3bf88f6791ad6785ed73faf1c4d6d49332bee47b3b078c476cb8604e4` | Not re-hashed for this bounded comparison. |
| `common/decisions/029_riches_found_decisions.txt` | `1a485534b48a59d780a53c09642e4618659c69f8fcedda9f735cca412f886a14` | Not re-hashed for this bounded comparison. |
| `common/scripted_effects/029_riches_found_effects.txt` | `a991dde1db89165ced86dbf714228975113d012163d073723c898873941e987c` | `1bc4a8ac4c8cf512ba5c5fd91421d7545d67f0ccd91e1d9c7c2ec67b4ae522dd` |
| `common/scripted_effects/029_riches_found_incident_effects.txt` | `01648014f105c149509f789be9ae3d30e013545921203ba867cbbd16d5c2f9fc` | `521ce7e756a352f2a6d24496b4bbcaf9d582f15ebb3a79c6219d03ff73498cad` |
| `common/mtth/029_riches_found_mtth.txt` | `32c989917b468b76c5a6a98a4190b0d490c38651f1be429eadd667b2927acb5f` | Not re-hashed for this bounded comparison. |
| `common/script_constants/029_riches_found_constants.txt` | `499394210e8818a5d1f94c6153e27dc7d8c69f378dc871622806975a610f0` | Not re-hashed for this bounded comparison. |

The live trigger source `common/scripted_triggers/029_riches_found_triggers.txt` has current SHA-256 `01c6e98c08f5dd87ded870e4de189f8a0e56503ba8fdec7467473850eb6b9cf` and has no corresponding immutable snapshot in the supplied `2026_10_03_before` set. Preserve a before copy if that file is patched.

## MCP evidence and exact blockers

The parent supplied a successful pre-edit `hoi4.probability_inspect` for `common/decisions/029_riches_found_decisions.txt`: code `PROBABILITY_SOURCE_DISCOVERED`, source hash `0f70e76d1dd0c1b13cab670173a89b9eaa1d9500f2380a810c1a48b015953fd7`, revision `bfda944ca879c510d241794903dee459d92f35fb74b7dc350b5c188bf3c35301`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b51bd817d8acbc390eb28f44251b69119dbaa57d704227b72e978cb4ec664c9e/153aa92c6aab913062324f97deb29b1f408a15f0e64937a00db73dc86dbcc3aa/probability-inspect-0f70e76d1dd0.json`.

That adapter classified 101 timed entries as `mission_ai_will_do` and one selector as `decision_ai_will_do`; the source structure is 92 decisions and nine missions. Retain this adapter/source mismatch. A decision or mission `ai_will_do` is a willingness score race, not a click probability.

My bounded `probability_inspect` call for adapter `decision_ai_will_do` on `common/decisions/029_riches_found_decisions.txt` remained pending without output for more than 188 seconds and was terminated client-side. It returned no artifact, revision, or source hash, so it is not evidence that the route is unavailable.

My follow-up `probability_inspect` call used adapter `random_list`, `refresh = true`, and the immutable core-effects snapshot path `docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__scripted_effects__029_riches_found_effects.txt`. The tool returned this exact error: `tool call failed for hoi4_agent_tools/hoi4.probability_inspect: timed out awaiting tools/call after 600s`. No artifact or analysis revision was returned.

The user separately reported that reference context and three cited reads succeeded, while the exact `has_manpower` search and expanded context timed out at 600 seconds. This corroborates slow service behavior but does not substitute for probability evidence.

`probability_evaluate`, `probability_sweep`, and `probability_compare` were not called after the required source inspection timed out. Their live routes are exposed, but no completed same-scenario analysis is available. `probability_render` was not called because there is no new analysis ID to render. No MCP finding is presented as source-only balance evidence.

The connected schema exposes `scenarioSet` as `unknown`. The saved fixture therefore contains only the confirmed `scenarioSet.id` and scenario `id` fields. It deliberately omits speculative controls, typed scope bindings, candidate overrides, target pointers, or scenario values. This preserves scenario identity but does not bind the specified campaign states; every numerical, normalized, or rank conclusion remains unresolved until the live route accepts the needed inputs.

## Owner-applied core-effects changes

In the immutable core-effects snapshot, `riches_found_prepare_random_event_fire` set `riches_found_prefire_ready = 1` whenever both regular prefire event targets existed, even if the current eligible-country pool was empty. The current source resets readiness to zero, only runs selection when the current pool count is positive, requires the pool to remain nonempty, rechecks the saved owner with `riches_found_is_eligible_discovery_country`, and rechecks that the saved state is valid and owned and controlled by that exact owner before setting readiness to one. It clears the temporary pool after validation.

The current source does not show the separately specified per-invocation freshness receipt. `riches_found_save_prefire_state` still only saves `riches_found_prepared_mine_state` and `riches_found_prefire_state`; I found no invocation-local marker that it selected a state during this call. The empty-pool case is source-gated by the current pool count, but same-owner stale state acceptance is not disproved by the source. Keep `RF_REPEATABLE_RECIPIENT_STATE_POOL` unresolved until the receipt contract is present or the engine adapter proves freshness.

The owner also corrected `riches_found_begin_contract` so the exclusive request must equal one and the contract type must equal `exclusive_concession` before the exclusive flag and history are set. `riches_found_extend_limited_contract` now calls `riches_found_refresh_mine_state` through `CONTROLLER` from the state scope, matching the helper's country-scope contract. These are source-level behavior changes, not probability changes.

No compare between the immutable core-effects snapshot and the current source was completed. The requested future comparison source objects are `before.path = docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__scripted_effects__029_riches_found_effects.txt` and `after.path = common/scripted_effects/029_riches_found_effects.txt`, with the same `RF_FOREIGN_*` and `RF_REPEATABLE_RECIPIENT_STATE_POOL` scenario IDs from the saved fixture. The pool and external state are incomplete, so no numeric probability should be claimed even if the route later returns source-structural changes.

## Foreign partner source audit

`riches_found_prepare_scored_foreign_partner` in `common/scripted_effects/029_riches_found_incident_effects.txt` enumerates countries, filters out the controller, special and nonhuman countries, capitulated countries, and countries at war with the controller, then retains the highest score. It does not sample in proportion to score. The strict `greater_than` replacement keeps the first encountered candidate on a tie, but traversal order and the complete live candidate pool are not exposed by this audit.

The foreign score table is source-only: base `20`, major `35`, large industry `25`, medium industry `10`, neighbor `45`, same faction `30`, positive relations `20`, hostile relations `-20`, wartime need `15`, controller weakness `20`, contract network `20`, overseas access `10`, severe crisis `-35`, and exclusive conflict `-80`, with a minimum of `1`. The convoy threshold is `20`; the opinion thresholds are `25` and `-25`. These are score components, not probabilities. No scenario trace or ranking was returned by MCP.

The exact omitted RF_FOREIGN_02 branch is in `common/scripted_triggers/029_riches_found_triggers.txt::riches_found_foreign_target_is_valid`: it only searches `any_neighbor_state` for an ordinary, non-capitulated land-state controller. The scored selector separately admits a non-neighbor when the candidate is a major, has more than 20 convoys, and the mine has `riches_found_port_route_valid`, `riches_found_port_route`, or `riches_found_island_mine`. The availability gate has no matching maritime branch, so this distant naval candidate cannot make the foreign action valid through that trigger even though the scored selector can include it. This is an exact source mismatch and an unresolved scenario outcome.

The hostile-rival scenario also remains unresolved. A rival at peace can pass the selector through the neighbor branch because low opinion is a score penalty rather than a candidate veto; a rival at war is excluded. The scenario must distinguish those states before the expected zero or near-zero outcome can be tested.

The foreign selector now clears the published pointer and availability flag, resets its best score to zero, and publishes a new partner only when a fresh best score is positive and the saved target exists. `riches_found_begin_contract` also requires the published flag and variable to match the saved regular event target. This fails closed at source level when the current pass finds no positive-scoring partner, while the stale regular event target itself remains present. Global candidate completeness is still unresolved because no country-by-country eligibility evidence was supplied.

No compare between the immutable incident-effects snapshot and current source was completed. The requested future comparison inputs are `before.path = docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__scripted_effects__029_riches_found_incident_effects.txt` and `after.path = common/scripted_effects/029_riches_found_incident_effects.txt`, with `RF_FOREIGN_01_NEAR_ALLIED_MAJOR`, `RF_FOREIGN_02_DISTANT_NAVAL_POWER`, `RF_FOREIGN_03_HOSTILE_RIVAL`, `RF_FOREIGN_04_EXISTING_EXCLUSIVE_CONCESSION`, and `RF_FOREIGN_EMPTY_CANDIDATES` from the same saved fixture. The complete country pool and external factors remain unresolved.

## Weighted-surface inventory and result classification

| Surface and exact source | Source values or score form | Candidate and external-factor completeness | Classification and finding |
| --- | --- | --- | --- |
| Event option policy race, `events/029_riches_found.txt`, `chaosx.nr29.1.a` through `.e` | Five source bases are public development `150`, state extraction `125`, concession `115`, militarized `90`, and predatory `15`, with additive modifiers in source constants. | The local five-option pool is source-complete conditional on the event firing. The event firing race, country and mine state, and modifiers are not evaluated. | Exact source values; scenario rankings, normalized option shares, and global event probability are unresolved. |
| Decision and mission `ai_will_do`, `common/decisions/029_riches_found_decisions.txt` | Source contains 92 decisions and nine missions. The parent inspect counts 101 timed entries under the mission adapter and one selector under the decision adapter. | Per-category candidate pools, availability, `FROM` state, costs, strategy factors, and external state are not fully bound. | Score-only adapter family with source/adapter mismatch; no scenario score or click probability is established. |
| Recipient country selection, `common/scripted_effects/029_riches_found_effects.txt::riches_found_prepare_random_event_fire` | `random_scope_in_array` selects uniformly from the eligible-country temporary array. | The actual countries and each country's currently valid states are campaign-dependent and unavailable to the adapter. | Conditional uniform-selection source rule only; exact shares, repeat frequency, and starvation are unresolved. |
| State selection, `common/scripted_effects/029_riches_found_effects.txt::riches_found_prepare_selected_discovery_country` | `riches_found_state_selection.strong_weight = 80`; `broad_weight = 20`. These are the two `random_list` branch weights, not a final state probability. | Preferred and valid state membership, branch overlap, and owner/controller state are not evaluated. | Proportional branch inputs known from source; exact state probabilities unresolved. |
| Incident random lists, `common/scripted_effects/029_riches_found_incident_effects.txt` | Source includes claims, rush, development, corruption, foreign interference, raid actor, raid target, raid severity, raid incident, collapse, Gold Disease, supernatural, contract outcome, and due-review random-list calls. | Candidate validity, prior-incident memory, current mine flags, caps, cadence, recovery, and terminal state are not bound. | Surface M incomplete and unresolved. No `probability_sequence` manifest is complete. |
| Foreign scored partner selector, `common/scripted_effects/029_riches_found_incident_effects.txt::riches_found_prepare_scored_foreign_partner` | Deterministic maximum of the foreign score described above, not probability-proportional sampling. | The world country pool, partner state, convoy stocks, opinions, factions, controller state, and mine access are incomplete. | Score-only source observation; target ranking, dominance, and probability unresolved. |
| Evolution timing, `common/mtth/029_riches_found_mtth.txt` | Three MTTH entries have 90-day bases. Their modifiers include pressure, order, legitimacy, war, multiple mines, private/exclusive capture, audit state, disease, controlled closure, excavation, and sealed integrity. | Scenario states and scheduled changes are not bound; the live MTTH adapter inspect timed out. | Timing distribution and cumulative chance unresolved. No event timing claim is made from the 90-day base. |

No dominance, starvation, rank reversal, excessive repetition, or snowball result is engine-proven for these surfaces. The only exact findings are source structure, source values, and the documented owner edits. No random simulation or sequence analysis was run because no supported uncertain-input distribution or complete custom-pool transition manifest was available.

## Recommended owner follow-up

1. Add or verify an invocation-local fresh-state receipt in `common/scripted_effects/029_riches_found_effects.txt::riches_found_save_prefire_state`, reset it at the start of `riches_found_prepare_random_event_fire`, and require it together with the current pool and owner/state validation before publishing ready state.
2. Align `common/scripted_triggers/029_riches_found_triggers.txt::riches_found_foreign_target_is_valid` with the scored selector's remote maritime eligibility branch for major countries with sufficient convoys and an accessible port or island mine, then compare the exact `RF_FOREIGN_*` fixture when the probability route returns.
3. Decide whether hostile-at-peace neighbors are valid concession candidates. If they are not, separate the hostile case with an eligibility gate rather than inferring a zero from the `-20` score modifier.
4. Preserve the current source snapshots and this exact fixture for the eventual `probability_compare` calls. Do not claim a score delta, candidate probability, or completed RF_FOREIGN or Surface N audit from the source comparison alone.

## Skipped analyses and remaining blockers

- The 39 named scenarios were saved, but not evaluated. Full candidate families and scenario state bindings remain unresolved.
- Surface M candidate lists were not returned by MCP because `probability_inspect` on the baseline core-effects source timed out after 600 seconds.
- The requested core-effects and incident-effects `probability_compare` calls were not attempted after the mandatory inspection timed out and the connected nested scenario input contract remained unconfirmed.
- Threshold sweeps were not run because no completed evaluation established a supported variable path, complete candidate pool, or accepted scenario-state binding.
- No comparison ID, scenario hash, new artifact URI, or rendered evidence exists for the owner-applied patches.
- The foreign availability trigger has no preserved pre-edit snapshot. It has not been patched in this turn, and its maritime gate remains the source-level blocker for `RF_FOREIGN_02_DISTANT_NAVAL_POWER`.
- The current prefire helper lacks the requested per-invocation receipt in the source reviewed here. Same-owner stale-target behavior remains unresolved.
- No gameplay source was edited. The audit is incomplete and should resume with the same named fixture and real before/after source paths when the probability service completes its mandatory routes.
