# Event 35 affordability and weighted comparison after owner patch

## Status

This is a read-only, incomplete MCP comparison handoff for six Event 35 doctrine-choice decisions. Source review confirms the owner patch adds the existing affordability predicate to each decision's `available` block. The probability inspection, both comparison attempts, named-scenario evaluation, and after-source sweep all timed out after 600 seconds. All engine-model conclusions remain unresolved.

No gameplay, AI, decision, mission, fixture, asset, or workbook file was changed. This handoff is the only file created by this audit.

## Audited surface and exact inputs

The weighted surface is `decision_ai_will_do` for this complete six-choice doctrine family only:

- `great_depression_choose_emergency_public_works`
- `great_depression_choose_rescue_strategic_industry`
- `great_depression_choose_stabilize_finance_and_trade`
- `great_depression_choose_austerity_and_retrenchment`
- `great_depression_choose_direct_state_planning`
- `great_depression_choose_let_the_market_clear`

The named scenario ids are `AFF35-PP-BELOW`, `AFF35-PP-EQUAL`, `AFF35-PP-ABOVE`, `AFF35-QUOTE-MISSING`, `AFF35-ACTION-LOCKED`, and `AFF35-DOCTRINE-LOCKED`, from fixture id `EVENT35_AFFORDABILITY_2026_10_03`.

The candidate pool is complete for the six doctrine-choice decisions in `common\decisions\035_great_depression_decisions.txt`. It is not the full Event 35 decision pool. The other 68 ordinary paid decisions and all 15 missions were not included or evaluated. No claim about those candidates is made here, and this six-entry pool does not justify a normalized Event 35 selection probability.

| Source | Windows path | SHA-256 |
| --- | --- | --- |
| Immutable before source | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\035_great_depression_plans\audit_inputs\affordability_2026_10_03\035_great_depression_decisions_before.txt` | `2CB7B2538E5329772320A858CE7E3B06B5065E858FD4506C6F96DC75AF77C185` |
| Owner-patched after source | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\035_great_depression_decisions.txt` | `42D0520152DB1C15C32B627D309CF7AB91EF33106E40162F96066B52712D0ED3` |
| Identical saved scenario fixture | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\035_great_depression_plans\audit_inputs\affordability_2026_10_03\scenarios.json` | `4512EB75C67071B120FC439833A6669A10EF3065179B87F7672D79189038EFDD` |

The MCP comparison inputs use these real, distinct mod-relative paths: `before.path = docs/plans/035_great_depression_plans/audit_inputs/affordability_2026_10_03/035_great_depression_decisions_before.txt` and `after.path = common/decisions/035_great_depression_decisions.txt`. The fixture bytes and on-disk fixture were left unchanged.

## Source delta and owner-patch review

The local before/after diff is 74 inserted lines and zero deleted lines. All six audited decisions now place `hidden_trigger = { great_depression_can_pay_doctrine_choice = yes }` inside `available`, alongside their existing action-slot and doctrine-choice gates; their `custom_cost_trigger` already called the same predicate. The six source blocks are at lines 19, 56, 92, 128, 165, and 201 of the after source.

The owner reports that the full 74 ordinary paid decisions received the existing custom-cost predicate inside `available`, that the 15 missions are unchanged, and that all 75 `ai_will_do` blocks are byte-identical to before. The observed source diff supports that account: it contains only the 74 added gate lines and no deletions. These source facts do not substitute for the requested MCP comparison.

The intended source-level effect is that ordinary decision availability and the custom-cost display gate now share the same affordability predicate. Whether the engine model removes or retains each candidate under the six cases, and how it treats its unchanged willingness score, has not been demonstrated by MCP.

The shared predicate is defined in `common\scripted_triggers\035_great_depression_decision_surface_triggers.txt`. `great_depression_can_pay_four_type_cost` requires the external action slot to be open and all cost quote variables to be ready; `great_depression_can_pay_doctrine_choice` adds the inclusive political-power check. `great_depression_can_choose_doctrine` also requires `great_depression_can_manage`, an unassigned doctrine, and no doctrine-lock flag; each candidate helper additionally rejects its own completed-choice receipt. Thus the owner gate composes the affordability check with the existing action-slot and doctrine-selection requirements rather than replacing them.

## Source-defined score values and modifier trace

Every doctrine-choice block uses base `constant:great_depression_target_weight.base`, whose source value is 10. The fixture sets `great_depression_ai_profile = 1` (Relief Coalition). The profile additions are source constants in the order Relief Coalition / Strategic Mobilizer / Financial Stabilizer / State Coordinator / Fiscal Retrencher / Liquidation Gambler. They are not MCP-evaluated totals.

| Candidate | Profile additions in order above | Other additive modifiers | Source zeroing conditions |
| --- | --- | --- | --- |
| `great_depression_choose_emergency_public_works` | 14 / 8 / 12 / 10 / 8 / 6 | affordability 6; blockade or trade failure 8; high social strain 16 | doctrine locked |
| `great_depression_choose_rescue_strategic_industry` | 4 / 14 / 8 / 12 / 4 / 2 | affordability 6; wartime industry need 10 | doctrine locked |
| `great_depression_choose_stabilize_finance_and_trade` | 12 / 10 / 14 / 6 / 12 / 14 | affordability 6; high financial pressure 8 | doctrine locked |
| `great_depression_choose_austerity_and_retrenchment` | 8 / 6 / 12 / 6 / 14 / 10 | affordability 6; high fiscal pressure 8 | extreme social strain; doctrine locked |
| `great_depression_choose_direct_state_planning` | 10 / 12 / 8 / 14 / 6 / 4 | affordability 6; blockade or trade failure 10 | doctrine locked |
| `great_depression_choose_let_the_market_clear` | 6 / 4 / 12 / 4 / 10 / 14 | affordability 6; high private capacity 5 | last viable center at risk; extreme social strain; doctrine locked |

The affordability entries above are willingness-score modifiers, not availability predicates and not probabilities. The modifier is `great_depression_ai_action_is_affordable`. Because the `ai_will_do` blocks were not changed, the owner patch does not itself change authored score values. No final score, rank, timing, or selection probability was returned.

## Scenario inputs and source-bounded traces

The fixture declares France (`FRA`), the crisis episode and severity, doctrine and profile state, cost quotes, current political power, stability, war support, manpower, and civilian-factory values. The quote is 25 political power in five cases and is deliberately absent in `AFF35-QUOTE-MISSING`. The three boundary cases use political power 24, 25, and 26.

`closedFlags: true` was rejected by the prior `probability_evaluate` schema with `-32602: Unrecognized key: "closedFlags"`. The submitted comparison payload therefore omitted only that field from each transient scenario object; every other fixture value was retained. Unlisted flags remain unknown and must not be treated as false.

External inputs are incomplete for score evaluation. The shared AI-affordability trigger checks every positive refreshed quote against political power, manpower, fuel, train equipment, convoys, support equipment, available civilian factories, stability, and war support. The fixture supplies `manpower_k`, while the trigger calls `has_manpower`; equivalence in this adapter was not established. Current fuel, train, convoy, and support-equipment stock values are not declared. The doctrine eligibility path also includes `uses_normal_civilian_systems`, whose actor-country classification was not established by the fixture. Unknown flags can affect blockade/trade-failure, social-strain, and center-risk modifiers. No missing value or flag was invented.

| Scenario | Source-bounded before/after implication | MCP classification |
| --- | --- | --- |
| `AFF35-PP-BELOW` | At PP 24 against quote 25, the shared paid predicate's political-power subcondition fails. Before, `available` omitted that predicate; after, it is present in `available`. | Unresolved for engine availability, raw score, candidate ranking, and selection. |
| `AFF35-PP-EQUAL` | At PP 25 against quote 25, the political-power subcondition passes inclusively if quote readiness and the action-slot gate pass. | Unresolved for engine availability, raw score, candidate ranking, and selection. |
| `AFF35-PP-ABOVE` | At PP 26 against quote 25, the political-power subcondition passes if quote readiness and the action-slot gate pass. | Unresolved for engine availability, raw score, candidate ranking, and selection. |
| `AFF35-QUOTE-MISSING` | The omitted political-power quote makes quote readiness and the shared paid predicate fail at source level; the after source includes that predicate in `available`. | Unresolved for engine availability and raw score. |
| `AFF35-ACTION-LOCKED` | The action-lock flag closes the source action-slot gate. The unchanged six AI-weight blocks have no explicit action-lock zeroing modifier. | Score-only source risk; MCP raw score and candidate-selection behavior unresolved. |
| `AFF35-DOCTRINE-LOCKED` | Doctrine value 1 and the lock flag close doctrine-choice eligibility; every doctrine-choice weight has a source factor of zero when doctrine is locked. | Source-defined zero-factor branch; MCP score and selection unresolved. |

For every row, the six-candidate pool is complete only for the doctrine-choice family and incomplete for the wider Event 35 decision category; the other 68 ordinary decisions were excluded. External inputs remain incomplete in every case because unlisted flags are unknown, current fuel/train/convoy/support-equipment stocks are absent, actor classification for `uses_normal_civilian_systems` is not established, and the `manpower_k` to `has_manpower` mapping is unresolved. `AFF35-QUOTE-MISSING` additionally omits the political-power quote by design. The action-lock and doctrine-lock flags are explicitly present only in their named cases.

These are source traces only. The new `available` gate is a bounded source-level correction to the affordability mismatch. It is not proof of a clickable decision result or an actual payment transaction.

## Ranking, probability, and risk findings

`ai_will_do` values are score-race inputs. They are not click probabilities and are not normalized by this audit. The offline AI-modification reference distinguishes `ai_will_do` score selection from event-option `ai_chance` probability-proportional sampling. There is no exact, bounded, or sampled ranking result yet.

The PP 24 / 25 / 26 fixtures cover the declared affordability boundary, but no MCP sensitivity or rank-reversal result is available. Dominance, starvation, rank reversal, numeric score change, repetition frequency, and timing drift are unresolved. The doctrine value and lock receipt constrain repeat selection in source, but no repetition scenario was evaluated. The pre-patch source mismatch represented a possible affordability/availability inconsistency; this pass does not establish a runtime exploit. The after source aligns the two source predicates for the six audited decisions.

## MCP evidence ledger

The connected tool inventory was rechecked after the parent reported restored MCP capabilities. It exposes `hoi4.probability_inspect`, `hoi4.probability_compare`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_render`, `hoi4.source_lookup`, and the reference context/search/read routes. `hoi4.script_validate` remains absent. Tool presence is not evidence of a successful analysis.

1. The audit began with read-only `hoi4.probability_inspect` for adapter `decision_ai_will_do`, source `common/decisions/035_great_depression_decisions.txt`, and the six-candidate pool. It returned: `tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 600s`. No workspace revision, artifact URI, coverage result, or required-input report was returned.
2. A first `hoi4.probability_compare` was submitted with distinct before/after paths, the six candidates, and the same six scenarios. It returned: `tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: timed out awaiting tools/call after 600s`. No comparison id, scenario hash, revision, result, or artifact URI was returned.
3. After the parent reported the artifact-template route and restored HOI4 tool inventory, the live list was revalidated; all probability and reference routes listed above were exposed. The terminal first compare was not duplicated while pending. A fresh compare was then submitted with the same source paths, candidate pool, and fixture payload (again omitting only `closedFlags`) and outputs `json`, `comparison`, `ranking`, `matrix`, `waterfall`, and `unresolved`. It terminated with: `tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: timed out awaiting tools/call after 600s`. Its local execution cell was `43`. No comparison id, scenario hash, revision, result, or artifact URI was returned.
4. `hoi4.probability_evaluate` was submitted for the after source, the same six candidates, and all six named scenarios, requesting raw values, ranking, matrix, waterfall, and unresolved outputs. It terminated with: `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate; Caused by: timed out awaiting tools/call after 600s`. Its local execution cell was `55`. No score trace, analysis id, scenario hash, revision, or artifact URI was returned.

5. `hoi4.probability_sweep` was submitted for the after source, the same six candidates and scenarios, and `state.political_power` with three steps and rank-reversal detection. It requested threshold and sensitivity views. It terminated with: `tool call failed for hoi4_agent_tools/hoi4.probability_sweep; Caused by: timed out awaiting tools/call after 600s`. Its local execution cell was `57`. No sensitivity result, ranking, analysis id, scenario hash, revision, or artifact URI was returned.

No `hoi4.probability_render` call has been made because no completed analysis id or artifact exists. These incomplete analyzer routes are not completed checks. Do not substitute hand arithmetic or source-only claims.

`hoi4.probability_simulate` was not applicable because the fixture declares fixed scenario values and no uncertain-input distributions or seed. `hoi4.probability_sequence` was not applicable because this is a native decision-weight score race, not a manifest-declared custom pool with cadence and state transitions.

The earlier baseline also records a `hoi4.decision_inspect` timeout after 600 seconds. It was not repeated in this follow-up. The parent-supplied live-menu log `docs\testing\live_qa\20261003_full_playtest\logs\cycle1\error.log` contains no Event 35-labelled errors, but it predates the owner affordability patch and is not runtime affordability evidence.

## References

- Offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, lines 285–340, SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`: custom-cost display is not a payment; manual debit and AI political-power hints are separate.
- Offline `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md`, lines 28–42, SHA-256 `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818`: `ai_will_do` score race versus `ai_chance` sampling.
- Installed vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md`, lines 1–30, SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`: `available` is the current takeability gate.
- Prior handoff `docs\plans\035_great_depression_plans\subagent_handoffs\affordability_probability_baseline_2026-10-03.md`: source constants, shared gates, original fixture caveats, and the exact earlier MCP timeouts.

## Recommendations and remaining work

- Retain the shared `great_depression_can_pay_doctrine_choice` gate in `available` and `custom_cost_trigger` for the six audited doctrine decisions. Source review shows the predicates now align; no balance retune is supported by the available evidence.
- Do not infer or tune score weights from the source table. Complete the same-scenario MCP comparison, named evaluations, and PP-threshold sweep when the probability route returns, with explicit actor classification and resource/flag inputs where the adapter requires them.
- Keep the six-choice scope separate from the other 68 paid decisions and 15 missions. Those candidates need their own complete pools and scenarios before any Event 35-wide claim.

No gameplay patch was applied. The exact operational blocker is that `hoi4.probability_inspect`, both `hoi4.probability_compare` calls, `hoi4.probability_evaluate`, and `hoi4.probability_sweep` returned `timed out awaiting tools/call after 600s`; this includes the fresh comparison after the tool inventory was restored. The MCP routes are exposed, but none of these calls produced analyzer evidence. All analyzer-dependent findings remain unresolved, and the other 68 ordinary paid decisions and 15 missions remain outside this audit.
