# Event 35 affordability and weighted eligibility baseline

## Status

This is a read-only, incomplete MCP baseline for the six initial doctrine-choice decisions. Source review identifies an availability/affordability contract gap, but no engine-backed weight trace, ranking, threshold result, or live-game behavior is claimed.

This audit edited no gameplay, AI, cost, fixture, or source file. The only output created by this audit is this handoff.

The parent reports a separate civilian-commitment cleanup in `events/035_great_depression.txt` and non-weighted scripted-effect helpers. Those edits were outside this weighted audit; the decision source remains byte-identical to the supplied immutable snapshot.

The parent reports that 89 custom-cost entries exist across Event 35: 74 ordinary paid decisions lack the explicit affordability predicate in `available`, 15 missions include it, and center selection is uncharged. This pass covers six of the 74 ordinary decisions only; the remaining ordinary decisions, the missions, center selection, targeted candidates, and non-doctrine candidates are outside this result.

## Audited surface and immutable inputs

The weighted surface is `decision_ai_will_do` for the six candidates below, with a separate source-level review of each decision's `available` and `custom_cost_trigger` blocks.

The live decision source `common/decisions/035_great_depression_decisions.txt` and the immutable pre-edit snapshot `docs/plans/035_great_depression_plans/audit_inputs/affordability_2026_10_03/035_great_depression_decisions_before.txt` are byte-identical at SHA-256 `2CB7B2538E5329772320A858CE7E3B06B5065E858FD4506C6F96DC75AF77C185`.

The supplied scenario fixture is `docs/plans/035_great_depression_plans/audit_inputs/affordability_2026_10_03/scenarios.json`, SHA-256 `4512EB75C67071B120FC439833A6669A10EF3065179B87F7672D79189038EFDD`, fixture id `EVENT35_AFFORDABILITY_2026_10_03`.

The six candidate pool is complete for the initial doctrine-choice family in the decision source, but it is not the full Event 35 decision category or the parent-reported 74-entry set. No normalized selection probability is justified from this six-entry subset.

| Candidate id | Source-defined profile additions in order Relief / Mobilizer / Financial / Coordinator / Retrencher / Liquidation | Other positive weight modifiers | Zeroing modifiers |
| --- | --- | --- | --- |
| `great_depression_choose_emergency_public_works` | 14 / 8 / 12 / 10 / 8 / 6 | affordability 6; blockade or trade failure 8; high social strain 16 | doctrine already locked: factor 0 |
| `great_depression_choose_rescue_strategic_industry` | 4 / 14 / 8 / 12 / 4 / 2 | affordability 6; wartime industry need 10 | doctrine already locked: factor 0 |
| `great_depression_choose_stabilize_finance_and_trade` | 12 / 10 / 14 / 6 / 12 / 14 | affordability 6; high financial pressure 8 | doctrine already locked: factor 0 |
| `great_depression_choose_austerity_and_retrenchment` | 8 / 6 / 12 / 6 / 14 / 10 | affordability 6; high fiscal pressure 8 | extreme social strain or doctrine already locked: factor 0 |
| `great_depression_choose_direct_state_planning` | 10 / 12 / 8 / 14 / 6 / 4 | affordability 6; blockade or trade failure 10 | doctrine already locked: factor 0 |
| `great_depression_choose_let_the_market_clear` | 6 / 4 / 12 / 4 / 10 / 14 | affordability 6; high private capacity 5 | last viable center at risk, extreme social strain, or doctrine already locked: factor 0 |

Every row has the same source-defined base `great_depression_target_weight.base = 10`. The profile labels resolve to numeric ids in `common/script_constants/035_great_depression_constants.txt`: Relief Coalition is 1, Strategic Mobilizer 2, Financial Stabilizer 3, State Coordinator 4, Fiscal Retrencher 5, and Liquidation Gambler 6. The fixture sets `great_depression_ai_profile = 1`, so Relief Coalition is the declared profile assumption. The values above are source constants, not MCP-evaluated totals; no manual sum or final ranking is reported.

The shared AI-weight ladder is `blocked = 0`, `minor = 2`, `light = 4`, `modest = 5`, `standard = 6`, `strong = 8`, `elevated = 10`, `preferred = 12`, `dominant = 14`, `priority = 16`, `urgent = 18`, and `decisive = 20`.

## Source and eligibility findings

All six `available` blocks require `great_depression_action_slot_is_open = yes` and their decision-specific `great_depression_can_choose_* = yes` trigger. Those six scripted triggers converge on `great_depression_can_choose_doctrine`, which requires a coherent active crisis, `uses_normal_civilian_systems`, no transition-pending flag, the unassigned doctrine value, and no doctrine-lock flag.

None of the six `available` blocks calls `great_depression_can_pay_doctrine_choice`. Each `custom_cost_trigger` does call that exact predicate. `great_depression_can_pay_doctrine_choice` requires the shared external action slot, all cost quote variables to be ready, and `NOT = { has_political_power < great_depression_cost_political_power }`. The political-power comparison is inclusive at equality. The decision source therefore has the identified source contract gap: display/affordability is gated by `custom_cost_trigger`, while ordinary availability does not explicitly repeat that predicate.

The fixed `ai_hint_pp_cost` is 25. The fixture declares a political-power quote of 25 in five cases and omits that quote in `AFF35-QUOTE-MISSING`; no MCP trace verified the engine's custom-cost or AI-hint interpretation for these cases.

The `great_depression_ai_action_is_affordable` modifier is an additive score bonus, not an eligibility gate. Its scripted trigger requires cost quotes to be ready and checks each non-zero quote against political power, manpower, fuel, trains, convoys, support equipment, civilian factories available for projects, stability, and war support. The fixture supplies political power, stability, war support, `manpower_k`, and available civilian factories, but it does not declare fuel stock, train equipment stock, convoy stock, or support-equipment stock. It uses `manpower_k` while the trigger calls `has_manpower`; the adapter's equivalence for this fixture was not established. Consequently, the shared affordability bonus cannot be accepted as evaluated for any of the six cases.

The fixture sets `closedFlags = true`, but the live `probability_evaluate` schema rejected that key for all six cases. The corrected evaluation request omitted only `closedFlags` and retained the supplied positive flags and state values. Unlisted flags therefore remain unresolved assumptions in that submitted scenario set. This matters to blockade/trade-failure, social-strain, and center-risk modifiers. The fixture does supply the active flag and the episode, severity, and evolution variables used by `great_depression_active_crisis_is_coherent`; `uses_normal_civilian_systems` is a scripted helper that also depends on actor-country classification.

At source level, the three political-power boundary cases set current political power to 24, 25, and 26 against the declared quote of 25. The shared paid predicate rejects the below-quote case and passes its political-power subcondition at equality and above, subject to the separate action-slot and quote-readiness checks. Since `available` omits the paid predicate, its source expression is identical across those three PP values. Whether the engine blocks the action through custom-cost UI behavior despite this source omission was not resolved by MCP.

The missing-quote case makes `great_depression_costs_are_ready` false by omitting `great_depression_cost_political_power`; the paid custom-cost predicate therefore fails at source level. The `available` source expression still has no direct cost predicate. The AI affordability bonus also depends on quote readiness, while the base and profile additions remain authored in the candidate weight blocks.

In `AFF35-ACTION-LOCKED`, the explicit action-lock flag makes `great_depression_action_slot_is_open` false and also closes the shared paid-cost gate. The six AI-weight blocks do not include an explicit action-lock factor. The source thus permits non-zero authored willingness terms alongside a blocked availability gate; the actual raw score and AI selection consequence remain unresolved.

In `AFF35-DOCTRINE-LOCKED`, the fixture sets doctrine value 1, which maps to Emergency Public Works, and sets the doctrine-lock flag. `great_depression_can_choose_doctrine` rejects the choice, and every doctrine-choice weight has a source modifier that multiplies by the `blocked = 0` factor when the doctrine is already locked. This is a source-defined suppression path; no MCP score trace was returned.

Each doctrine-choice completion effect sets a doctrine value and doctrine-lock/choice-complete flags, assigns the corresponding AI profile, sets the doctrine-choice cost family, and calls `great_depression_commit_country_action`. That helper calls the manual payment effect. This supports source-level payment-path alignment but does not prove an engine transaction or a clickable decision.

## Scenario outcomes and classification

| Scenario id | Declared boundary | Source trace | MCP result classification |
| --- | --- | --- | --- |
| `AFF35-PP-BELOW` | PP 24, quote 25 | Paid predicate's PP subcondition fails; `available` omits the predicate | unresolved for actual availability, raw score, and selection |
| `AFF35-PP-EQUAL` | PP 25, quote 25 | Paid predicate's PP subcondition passes inclusively if the action slot and quote readiness pass; `available` omits it | unresolved for actual availability, raw score, and selection |
| `AFF35-PP-ABOVE` | PP 26, quote 25 | Paid predicate's PP subcondition passes if the action slot and quote readiness pass; `available` omits it | unresolved for actual availability, raw score, and selection |
| `AFF35-QUOTE-MISSING` | political-power quote omitted | Quote readiness and the shared paid predicate fail at source level; `available` omits that predicate | unresolved for actual availability and raw score |
| `AFF35-ACTION-LOCKED` | action-lock flag present | Availability and custom-cost action-slot gates fail; the AI weights lack an action-lock zero factor | score-only source risk; MCP raw score and engine selection unresolved |
| `AFF35-DOCTRINE-LOCKED` | doctrine value 1 and doctrine-lock flag present | Doctrine eligibility fails; authored AI weight includes a zero factor for an assigned doctrine | source-defined zero-factor branch; MCP trace unresolved |

No exact or bounded MCP result, sampled result, rank order, rank reversal, dominance, starvation, or numeric sensitivity is available. The rows above classify source expressions only. The AI modifier values are willingness scores, not click probabilities; the offline AI-modification reference describes `ai_will_do` as a score race and distinguishes `ai_chance` probability-proportional sampling.

Repetition risk appears constrained in the source: a doctrine can be chosen only while the doctrine value is unassigned and the completion effects set the doctrine and lock receipt. No repeated-choice result was tested. Exploit risk is limited to a possible mismatch between the visible custom-cost gate and `available`; whether a player or AI can complete an unaffordable choice is not established without the native decision scenario result. It is not reported as a proven runtime exploit.

## MCP evidence ledger

The first probability call was `hoi4.probability_inspect` with adapter `decision_ai_will_do` and source `common/decisions/035_great_depression_decisions.txt`. It was submitted once before candidate-level evaluation. Its `functions.exec` cell handle was `14`; polling returned `cell 14 belongs to a stale code-mode host generation`. No final status, workspace revision, artifact URI, candidate coverage, or required-input list was retrievable. The current decision source and immutable snapshot have the same verified SHA-256 above.

A bounded `hoi4.decision_inspect` request targeted `great_depression_choose_emergency_public_works` with the six declared scenarios. Its handle was `22`; polling returned `cell 22 belongs to a stale code-mode host generation`. No availability/cost artifact or revision was returned.

The first `hoi4.probability_evaluate` request was rejected with MCP error `-32602`: `Unrecognized key: "closedFlags" at scenarioSet.scenarios[0]` through `[5]`. A single corrected request removed only that unsupported field, used the immutable snapshot path, adapter `decision_ai_will_do`, all six candidate ids, all six scenario ids, `raw_value`, and ranking/matrix/waterfall/unresolved outputs. It timed out with `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate; Caused by: timed out awaiting tools/call after 600s`. No analysis id, scenario hash, revision, or artifact URI was returned. The evaluation was not retried.

One `hoi4.probability_sweep` request used the same snapshot, six candidates, and corrected scenario set, with path `state.political_power`, three steps, and rank-reversal detection. It timed out with `tool call failed for hoi4_agent_tools/hoi4.probability_sweep; Caused by: timed out awaiting tools/call after 600s`. Its handle was `g2:7`. No result, analysis id, scenario hash, revision, or artifact URI was returned. The sweep was not retried.

`hoi4.probability_render` was not called because no completed analysis id exists. `hoi4.probability_compare` was not called because this is a baseline request and no distinct changed after-source exists. Simulation was not applicable because no uncertain-input distribution or seed was declared. Sequence analysis was not applicable because this is not a declared custom pool with cadence and transitions.

## References and remaining work

The offline Decision modding reference, `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 285–340, documents custom-cost display lookup and the need for a separate manual debit; SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.

The offline AI modding reference, `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`, lines 28–42, distinguishes the `ai_will_do` score race from `ai_chance`; SHA-256 `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818`.

Installed `common/decisions/_documentation.md`, lines 1–30, describes `available` as the immediate decision-taking gate; SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`. Vanilla `common/decisions/AUS.txt`, lines 982–996, is the cited custom-cost precedent; SHA-256 `619F5E7D922C7900C2CFE31B54DC37D32B7583DEDAE9F33336A430D753362EF0`.

Recommended owner patch for the six audited decisions: add the identical existing `great_depression_can_pay_doctrine_choice = yes` predicate to each corresponding `available` block in `common/decisions/035_great_depression_decisions.txt`, alongside the existing action-slot and doctrine-choice gates. Do not infer that this resolves the other paid decisions; the parent-reported remaining ordinary entries need their own complete candidate coverage and scenario evidence. After the owner applies a distinct source patch, run `hoi4.probability_compare` on the same named scenarios and preserve the new source hash, returned comparison id, scenario hash, and rendered evidence.

The final rank, affordability eligibility under the six cases, rank reversal at the PP threshold, action-lock score behavior, and broad Event 35 dominance/starvation remain unresolved until the MCP calls return or the route becomes available. No source-only conclusion in this report substitutes for that evidence.
