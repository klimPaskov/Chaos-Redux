# Event 016 final containment decision postreview

Date: 2026-09-02. This is a bounded, read-only source audit of the eight containment and sovereignty decisions at the postpatch snapshot below. No gameplay file was changed by this subagent.

Baseline: commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`.

## Severity-sorted findings

### P1 — resolved: affordability now gates selection and cost display

At the final snapshot, each of the eight decision definitions calls the same action-specific affordability helper from both `available` and `custom_cost_trigger` in `common/decisions/016_brilliant_scientist_containment_decisions.txt`. The eight helpers are `brilliant_scientist_can_pay_containment_release`, `brilliant_scientist_can_pay_containment_exile`, `brilliant_scientist_can_pay_containment_arrest`, `brilliant_scientist_can_pay_containment_shutdown`, `brilliant_scientist_can_pay_containment_charter`, `brilliant_scientist_can_pay_containment_military_seizure`, `brilliant_scientist_can_pay_containment_foreign_containment`, and `brilliant_scientist_can_pay_containment_concession` in `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`.

Every helper includes the positive Political Power and Stability checks from `brilliant_scientist_can_pay_containment_base`; Exile checks 20 convoys, Arrest 600 Support Equipment, Shutdown 200 motorized/trucks, Charter 600 Support Equipment, Military Seizure 6,000 Infantry Equipment, Foreign Containment 20 Command Power, and Concession 300 Support Equipment. The comparisons remain inclusive `greater_than_or_equals`, and Release correctly has no anchor.

The earlier review treated reliance on `custom_cost_trigger` alone as an explicit-gate and engine-behavior documentation risk, not as a confirmed runtime bypass. The offline Decision Modding reference establishes that `custom_cost_trigger` selects normal/blocked/hover localization and that custom cost itself does not debit anything, while `available` is the decision selection gate (`paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:99,299-317`). The shared helper call now makes the selection gate explicit without adding a fifth cost or changing any payment value, AI formula, route requirement, timer, or receipt behavior.

### P2 — visual acceptance remains unproven

The eight cost rows are source-level icon-first strings, with three entries for Release and four for every other response, but no `hoi4.gui_inspect` or `hoi4.gui_render` artifact is available for the final 320px decision cost textbox. Source review cannot certify wrapping, clipping, spacing, asset resolution, or click-region behavior. This is an acceptance limitation rather than a source-localization defect.

### P3 — malformed multi-clause density is outside this tranche

With the intended mutually exclusive response-clause flags, the ordinary board exposes at most five primary rows, and `brilliant_scientist_containment_action_is_visible` keeps only the selected row visible during an active timer (`common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt:8-22`). A malformed state with multiple clause flags could expose more rows, but that is not a normal-board defect in this postreview scope.

## Cost and requirement audit

The current spendable boundary is four axes at most: Political Power, upfront Stability, one physical or operational anchor where applicable, and the timed consumer-goods factor. The consumer-goods modifier is a commitment for the native decision timer, not a second factory-efficiency penalty. No other equipment, manpower, experience, fuel, train, or hidden payment remains in the inspected decision/effect path.

| Action | Timer | Immediate spend | One anchor | Timed commitment | Non-cost requirements |
| --- | ---: | --- | --- | --- | --- |
| Release Kruger | 21 days | 25 Political Power, 2% Stability | None | +3% consumer goods | Low coercive risk and no military/foreign response |
| Arrange Exile | 30 days | 40 Political Power, 3% Stability | 20 convoys | +3% consumer goods | Valid persisted recipient and containable private network |
| Arrest Kruger | 30 days | 55 Political Power, 5% Stability | 600 Support Equipment | +6% consumer goods | Open board; recorded response selects the coercive route |
| Close the Directorate | 45 days | 65 Political Power, 7% Stability | 200 motorized/trucks | +6% consumer goods | Open board; recorded response selects the coercive route |
| Ratify the Charter | 45 days | 75 Political Power, 4% Stability | 600 Support Equipment | +10% consumer goods | Charter response, viable marked territory, and viable host |
| Seize the Laboratories | 21 days | 85 Political Power, 10% Stability | 6,000 Infantry Equipment | +10% consumer goods | Military-seizure response and open board |
| Allied Containment | 30 days | 65 Political Power, 6% Stability | 20 Command Power | +6% consumer goods | Foreign-response policy and faction membership |
| Concede Authority | 30 days | 50 Political Power, 8% Stability | 300 Support Equipment | +10% consumer goods | Concession response and proven institutional capture |

The authoritative values are centralized in `common/script_constants/016_brilliant_scientist_containment_constants.txt:46-119`; the decision rows and dynamic cost strings use the matching constants. The gates equal the displayed anchor amounts and use inclusive comparisons. The systems document now reflects this exact table (`docs/events/016_brilliant_scientist/systems/containment.md:20-39`).

## Payment math and transaction identity

`brilliant_scientist_begin_containment_action` receives positive Political Power and Stability values, records the action ID and start date, negates each value through a temporary payment variable, and applies the reductions (`common/scripted_effects/016_brilliant_scientist_containment_effects.txt:511-523`). This avoids unsupported unary negation on a variable token.

The seven anchor actions debit exactly one negative constant in their decision `complete_effect`; Release has no anchor. There is no regular `cost` field, and custom cost text is display-only, so the source contains one base debit and one anchor debit per action rather than duplicate charges. The action/anchor pairings and begin parameters are in each decision's `complete_effect`, `brilliant_scientist_begin_containment_action`, and (where applicable) `add_equipment_to_stockpile` or `add_command_power` blocks in `common/decisions/016_brilliant_scientist_containment_decisions.txt`.

The active receipt is the action ID, not a generic boolean alone. Completion resolves only when `brilliant_scientist_containment_action_is_live` matches the action ID (`common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`, identifier `brilliant_scientist_containment_action_is_live`), and cancellation clears the lock only when its supplied ID still owns the receipt (`common/scripted_effects/016_brilliant_scientist_containment_effects.txt`, identifier `brilliant_scientist_cancel_containment_action`). Closing or invalid-route reopening clears the active ID and action flag while retaining the start-date history (`common/scripted_effects/016_brilliant_scientist_containment_effects.txt`, identifiers `brilliant_scientist_close_sovereignty_board` and `brilliant_scientist_reopen_invalidated_sovereignty_board`). An old native timer therefore cannot settle or clear a newer action receipt at source level.

All eight `ACTION` parameters match their constants in `complete_effect`, `cancel_effect`, and guarded `remove_effect`. Positive PP/Stability parameters resolve through the parameterized begin helper, and the `constant:category.key` values used by `days_remove` are supported by the vanilla SIA precedent, for example `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\SIA.txt:406,441,479,516,571,606,644,679`. The vanilla script-constant documentation also explicitly permits fixed-point `constant:` access in scoped variables.

## Lifecycle, cancellation, and exploit notes

Selection spends preparation immediately and the preparation tooltip states that it is not refunded on interruption or invalid final revalidation (`localisation/english/016_brilliant_scientist_containment_l_english.yml:28-29`). The native timed modifier owns the consumer-goods commitment, while `brilliant_scientist_containment_action_is_live` gates both cancellation and settlement. The eight `cancel_trigger` blocks wrap the localized `brilliant_scientist_containment_interrupted_tt` and do not expose internal flags (`common/decisions/016_brilliant_scientist_containment_decisions.txt`, identifiers `cancel_trigger` and `brilliant_scientist_containment_interrupted_tt`; `localisation/english/016_brilliant_scientist_containment_l_english.yml:28`).

The source relies on native decision timer ordering to remove the timed modifier after the live predicate becomes false and the wrapped `NOT = { ..._is_live }` cancellation condition becomes true; no same-tick engine trace was run. This remains an evidence limitation, not a second source defect, because the owner added the live country, receipt, authorization, completion, and world-end predicates and the native `days_remove`/cancel pattern is documented by the vanilla decision precedent.

The former P1 availability bypass is closed at source: an underfunded action now fails the same affordability helper in `available` before selection, while the duplicate call in `custom_cost_trigger` keeps the normal/blocked row accurate. The receipt identity and sunk-preparation rules do not show a free-payment loop or stale-timer double settlement in this source review.

## Cognitive load, localisation, AI, and route clarity

The decision names and availability tooltips are concise and describe causal requirements separately from the cost row. Each cost has normal, blocked, and hover keys, and each spendable value is represented with the corresponding text icon: `£pol_power`, `£stability_texticon`, `£consumer_goods_texticon`, `£convoy_texticon`, `£support_equipment_text_icon`, `£motorized_equipment_text_icon`, `£infantry_equipment_text_icon`, or `£command_power` (`localisation/english/016_brilliant_scientist_containment_l_english.yml:19-101`). No raw nested trigger dump or literal resource-name cost was found.

The final presentation pass defines exactly 23 country-scope `defined_text` helpers in `common/scripted_localisation/016_brilliant_scientist_containment_scripted_localisation.txt`; the eight aggregate cost rows reference exactly those 23 helpers, and every normal and `_blocked` fragment key resolves in the English localization.

| Action | Helper-to-fragment bindings and boundary input | Icons and timed factor | Displayed entries |
| --- | --- | --- | ---: |
| Release Kruger | `GetContainmentReleasePoliticalPowerCost` → `release_pp_cost`/`release_pp_cost_blocked` from `political_power` vs `release_political_power`; `GetContainmentReleaseStabilityCost` → `release_stability_cost`/`release_stability_cost_blocked` from `stability` vs `release_stability` | PP, Stability, and +3% consumer goods use `£pol_power`, `£stability_texticon`, and `£consumer_goods_texticon` | 3 |
| Arrange Exile | `GetContainmentExilePoliticalPowerCost` → `exile_pp_cost`/`exile_pp_cost_blocked`; `GetContainmentExileAnchorCost` → `exile_anchor_cost`/`exile_anchor_cost_blocked` from `num_equipment@convoy_1` vs `exile_convoy_gate`; `GetContainmentExileStabilityCost` → `exile_stability_cost`/`exile_stability_cost_blocked` | PP, convoys, Stability, and +3% consumer goods use the matching PP, convoy, Stability, and CG icons | 4 |
| Arrest Kruger | `GetContainmentArrestPoliticalPowerCost` → `arrest_pp_cost`/`arrest_pp_cost_blocked`; `GetContainmentArrestAnchorCost` → `arrest_anchor_cost`/`arrest_anchor_cost_blocked` from `num_equipment@support_equipment` vs `arrest_support_gate`; `GetContainmentArrestStabilityCost` → `arrest_stability_cost`/`arrest_stability_cost_blocked` | PP, Support Equipment, Stability, and +6% consumer goods use the matching icons | 4 |
| Close the Directorate | `GetContainmentShutdownPoliticalPowerCost` → `shutdown_pp_cost`/`shutdown_pp_cost_blocked`; `GetContainmentShutdownAnchorCost` → `shutdown_anchor_cost`/`shutdown_anchor_cost_blocked` from `num_equipment@motorized_equipment` vs `shutdown_truck_gate`; `GetContainmentShutdownStabilityCost` → `shutdown_stability_cost`/`shutdown_stability_cost_blocked` | PP, motorized/trucks, Stability, and +6% consumer goods use the matching icons | 4 |
| Ratify the Charter | `GetContainmentCharterPoliticalPowerCost` → `charter_pp_cost`/`charter_pp_cost_blocked`; `GetContainmentCharterAnchorCost` → `charter_anchor_cost`/`charter_anchor_cost_blocked` from `num_equipment@support_equipment` vs `charter_support_gate`; `GetContainmentCharterStabilityCost` → `charter_stability_cost`/`charter_stability_cost_blocked` | PP, Support Equipment, Stability, and +10% consumer goods use the matching icons | 4 |
| Seize the Laboratories | `GetContainmentMilitarySeizurePoliticalPowerCost` → `military_seizure_pp_cost`/`military_seizure_pp_cost_blocked`; `GetContainmentMilitarySeizureAnchorCost` → `military_seizure_anchor_cost`/`military_seizure_anchor_cost_blocked` from `num_equipment@infantry_equipment` vs `seizure_infantry_gate`; `GetContainmentMilitarySeizureStabilityCost` → `military_seizure_stability_cost`/`military_seizure_stability_cost_blocked` | PP, Infantry Equipment, Stability, and +10% consumer goods use the matching icons | 4 |
| Allied Containment | `GetContainmentForeignContainmentPoliticalPowerCost` → `foreign_containment_pp_cost`/`foreign_containment_pp_cost_blocked`; `GetContainmentForeignContainmentAnchorCost` → `foreign_containment_anchor_cost`/`foreign_containment_anchor_cost_blocked` from `command_power` vs `foreign_command_power_gate`; `GetContainmentForeignContainmentStabilityCost` → `foreign_containment_stability_cost`/`foreign_containment_stability_cost_blocked` | PP, Command Power, Stability, and +6% consumer goods use the matching icons | 4 |
| Concede Authority | `GetContainmentConcessionPoliticalPowerCost` → `concession_pp_cost`/`concession_pp_cost_blocked`; `GetContainmentConcessionAnchorCost` → `concession_anchor_cost`/`concession_anchor_cost_blocked` from `num_equipment@support_equipment` vs `concession_support_gate`; `GetContainmentConcessionStabilityCost` → `concession_stability_cost`/`concession_stability_cost_blocked` | PP, Support Equipment, Stability, and +10% consumer goods use the matching icons | 4 |

Every helper uses `compare = greater_than_or_equals`, so the normal fragment is selected at the exact displayed boundary and the fallback red fragment at one unit below it; this is source-level trigger evidence, not a live render. The scripted-localisation file contains no unsupported `£`, `§`, or dynamic-value formatting markers, and the targeted binding check found no unresolved helper or fragment name.

The eight surfaces are timed decisions, not separate missions; there is no per-action active-mission duplication to report. The shared sovereignty deadline mission is lifecycle context rather than one of these eight action rows. Durations, success/failure routes, and invalidation re-opening behavior remain unchanged by the cost consolidation.

AI weights and causal score logic were not changed in this tranche. Each decision's `ai_hint_pp_cost` remains aligned to its action's PP constant in `common/decisions/016_brilliant_scientist_containment_decisions.txt`. The separate probability owner is comparing the retained 17 scenarios; no probability certification is claimed here.

## Evidence, hashes, and acceptance limits

Required offline Paradox wiki pages, the relevant vanilla decision and script-constant documentation, and the vanilla decision precedent were consulted before this source review. No game, logs, or live save was used.

Current SHA-256 snapshot:

| File | SHA-256 |
| --- | --- |
| `common/decisions/016_brilliant_scientist_containment_decisions.txt` | `DFA2789A664E7DB9F9D4B1F06CA7EBDFC46B5E1D4EF7AA9D3A0D239007D687B3` |
| `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt` | `6DA95559E0616FFDDD6E12D61CFD964113AEBCFA6B1828012612F5D10D2936A3` |
| `common/scripted_effects/016_brilliant_scientist_containment_effects.txt` | `C3FD09241961536A55F54CBE27F14D711F0EB3CC4EC85C0B73E74FD05C391D1A` |
| `common/script_constants/016_brilliant_scientist_containment_constants.txt` | `3952E57D93B802C848078FDD028F7CCD301D6FD34E26777F7BC1924396BD31AD` |
| `localisation/english/016_brilliant_scientist_containment_l_english.yml` | `CBEE27800636E86189D36A958BA6930EE56238B77C9AE762986122BD81E1D749` |
| `common/scripted_localisation/016_brilliant_scientist_containment_scripted_localisation.txt` | `0A67ABD2627AF9E8854C6CAF5FDF861D9AC0E4F0B2D993E10741A9FD0E695F60` |
| `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` | `96DFB995B18B0BD85D3D1AC25864AD289E7C38CB0F2E027F1E3272A60A530A0A` |
| `docs/events/016_brilliant_scientist/systems/containment.md` — parent reconciled payment-colour note | `DA0BE6F599197E16CD250FD5E01608DAE8F8912FCD3DD7ABD247A2025A57C823` |

No GUI/MCP render artifact is claimed: the parent's `hoi4.gui_inspect` attempt for `decision_item` timed out at 180 seconds, and no final `hoi4.gui_render` comparison is available. The parent event trace also timed out at 180 seconds, and the separate probability comparison is still owned by its assigned auditor. These limitations do not overturn the resolved source disposition, but they prevent live visual or engine-ordering certification.

Subagent disposition: audit complete; only this handoff file was written. No gameplay patch, balance change, or commit was made.
