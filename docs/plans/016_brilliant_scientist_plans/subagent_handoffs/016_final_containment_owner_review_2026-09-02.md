# Event 016 containment cost and timer checkpoint

## Boundary and disposition

This checkpoint implements the containment cost-surface and action-receipt portion of the accepted final-completion contract.
It does not close the entire Directorate/containment tranche, the event's presentation work, or the full goal.
The parent promoted the payment contract into `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` before editing gameplay.
The baseline is commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`.

The decisions/missions skill's four-cost limit counts upfront Stability and each industrial burden, not just equipment types.
The former responses used between four and ten cost axes; this checkpoint retains Political Power, upfront Stability, one temporary consumer-goods burden, and at most one material or Command Power payment.
Secondary equipment, manpower, fuel, Army Experience, and the separate factory-efficiency penalty are removed outright, not hidden in follow-up effects.
The Political Power, Stability, consumer-goods factor, and duration values are unchanged.
This is a deliberate cost consolidation; it is not a claim that the old and new total economic prices are equivalent.

| Response | Political Power | Stability points | One optional payment | Consumer-goods factor | Days |
| --- | ---: | ---: | --- | ---: | ---: |
| Release | 25 | 2 | None | +3% | 21 |
| Exile | 40 | 3 | 20 convoys | +3% | 30 |
| Arrest | 55 | 5 | 600 Support Equipment | +6% | 30 |
| Shutdown | 65 | 7 | 200 trucks | +6% | 45 |
| Charter | 75 | 4 | 600 Support Equipment | +10% | 45 |
| Military seizure | 85 | 10 | 6,000 Infantry Equipment | +10% | 21 |
| Foreign containment | 65 | 6 | 20 Command Power | +6% | 30 |
| Concession | 50 | 8 | 300 Support Equipment | +10% | 30 |

## Implementation ownership

- `common/decisions/016_brilliant_scientist_containment_decisions.txt`: eight compact custom-cost surfaces, Political Power AI hints, one-time selection payments, selected-row visibility, receipt-owned cancellation and completion.
- `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`: inclusive common affordability, selected-action visibility, live receipt checks, and separation of causal eligibility from payment gates.
- `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`: action-specific receipt, shared Political Power/Stability debit, matching cancellation, and receipt cleanup on board closure/reopening.
- `common/script_constants/016_brilliant_scientist_containment_constants.txt`: consolidated positive gates/payments and matching negative equipment/Command Power spends.
- `localisation/english/016_brilliant_scientist_containment_l_english.yml`: shortened names, concise causal requirements, interruption explanation, dynamic icon-backed cost rows, and explicit non-refundable preparation text.
- `common/scripted_localisation/016_brilliant_scientist_containment_scripted_localisation.txt`: per-payment affordability colour selection, keeping sufficient resources normal when another payment is short.
- `docs/events/016_brilliant_scientist/systems/containment.md`: exact payments, helper contract, timer ownership, icon references, and persistent-history behavior.
- `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`: accepted containment closure contract.

The eight outcome routes, their causal resolver, and all eight `ai_will_do` blocks remain unchanged.
The active action ID is an enum-valued ordinary variable rather than a second boolean flag.
The in-progress flag continues to block simultaneous action starts.
An action can complete only while its own ID still matches the active receipt, the country hosts Kruger, the board remains unresolved, and no world end is active.
Cancellation clears only its matching receipt; closure and invalid-route reopening clear the current receipt explicitly.
Permanent outcome history and the historical start date are preserved.
Preparation is sunk; native decision modifiers own removal of the temporary consumer-goods burden.

## Parent source review

The parent checked all eight decisions against the baseline source and the promoted table.
Political Power is no longer charged by both native `cost` and a manual effect: these decisions use custom costs and a single shared selection debit, with the native AI planning hint retained.
Exact displayed Political Power, Stability, and anchor amounts satisfy the inclusive `check_variable` gates; this is source inspection, not an executed game scenario.
The specialist found that the first draft placed those checks only in `custom_cost_trigger` rather than explicitly in selection eligibility.
The parent corrected this by introducing one payment trigger per action and invoking that same trigger from both `available` and `custom_cost_trigger`.
The availability copy is a hidden trigger because the complete cost is already displayed in its own row; no payment is concealed from the player.
Each action calls the begin helper once and applies zero or one anchor deduction once.
Every equipment/Command Power gate matches the magnitude of its negative spend constant.
No additional manpower, fuel, experience, secondary-equipment, or factory-efficiency charge remains in the eight action paths.
The cost rows contain three entries for release and four for each other action.
The initial source assertions checked all 100 containment-cost references in the pre-colour-split source against the centralized definitions.
The final presentation check traced all 23 per-payment helpers to 46 normal/red fragments and the eight cost rows, confirming exact matching variable/constant pairs and three or four displayed entries.
Each colour predicate uses the same inclusive amount boundary as its corresponding selection payment; these are source assertions, not an executed visual scenario.
The source assertions found no change to the eight AI score blocks.

Installed vanilla decision documentation and the Austrian custom Command Power/Political Power decision precedent support the custom-cost/manual-payment structure.
Installed dynamic-variable documentation distinguishes stockpile `num_equipment@...` from equipment in armies.
The existing Great Depression decision implementation provides a repository precedent for custom costs with constant-backed Political Power hints.
The installed decision row provides a 330-pixel name region and a 320-pixel cost/timer region; shortening names and limiting entries targets that consumer but does not substitute for a rendered layout review.

## Specialist and MCP evidence

The bounded baseline source review is recorded in `016_final_containment_decision_review_2026-09-02.md`.
The final source review and weighted comparison are recorded in their matching containment postreview and probability handoffs.
The source reviewer accepted the explicit selection-gate correction, action-receipt lifecycle, and final 23-helper per-payment colour binding pass.

The mandatory weighted baseline uses the complete eight-candidate `mission_ai_will_do` pool and 17 scenarios in `E016_CONTAINMENT_COST_CLOSURE_2026_09_02`.
Its analysis `probability-65461ff54d419584271d2512` is partial and score-only: 136 candidate rows, 28 unresolved entries, and one diagnostic.
It does not prove affordability, click timing, native timer behavior, or normalized selection probabilities.
The probability handoff retains the exact source objects, scenario bodies/hash, artifact links, and adapter limitations.
The exact 17-scenario JSON fixture is retained beside that handoff, with SHA-256 `8bba36e6fdf9ca86b74e7e38a2b811c9766c317b702da70bb1c6597ef6f28278`.
Final `probability_compare` analysis `probability-3940462a3287d0e28d957172` preserves scenario hash `4a4611db1bd408349d42d455c9c29e22440c1219348239df5198126e05359312` and reports `PROBABILITY_ANALYZED_PARTIAL`.
Its 136 changed cells all record newly unresolved `available.hidden_trigger` eligibility, with no reported nonzero raw-score or rank delta.
The aggregated unresolved count is 44; all after-state candidates remain unresolved, so this is not proof of unchanged live eligibility or affordability.
The retained baseline intentionally includes simultaneous response flags as an artificial score fixture; it is not a normal live sovereignty board.

The parent also attempted a bounded downstream Event Inspector trace for `brilliant_scientist_arrest_kruger`, with helper expansion, depth 2, 24 nodes, and 48 edges.
The call failed with `tool call failed for hoi4_agent_tools/hoi4.event_inspect; timed out awaiting tools/call after 180s`.
No event artifact or acceptance result was returned.
Source review is not substituted for the missing event comparison.
The parent also called `hoi4.gui_inspect` for the installed native `decision_item` consumer in workspace `mod_chaos_redux_ea3b2d67c2c0`.
It returned `tool call failed for hoi4_agent_tools/hoi4.gui_inspect; timed out awaiting tools/call after 180s`, without an inspection artifact.
No native-row render or visual acceptance is claimed.

The parent removed two malformed `.23` and host-reaction comparison-SVG links from the earlier evolution probability handoff after bounded source recovery failed.
Their valid JSON and other evidence links remain; no fabricated replacement link was supplied.

## Assets, omissions, and remaining gates

No model, geometry, sound, portrait, scripted GUI, focus, super-event, or achievement was added or changed.
Cost rows reuse verified registered vanilla Political Power, Stability, consumer-goods, convoy, Infantry Equipment, and Command Power texticons plus existing repository Support Equipment and motorized texticons.
The existing containment decision icons were not replaced; dedicated Event 016 presentation assets remain part of the open presentation tranche.
No unregistered sprite or new placeholder was introduced by this checkpoint.

The native cost row has not received a production visual render in this checkpoint.
Exact affordability, stale-timer interruption, and industrial-modifier removal have source-level review only unless a specialist handoff explicitly supplies stronger evidence.
The missing Event Inspector artifact, unresolved weighted eligibility, broader causal formation/foreign-operation validation, and final catalog/presentation alignment remain open.
This report makes no repository-wide or in-game completion claim.

Skills used for this checkpoint: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and `chaos-redux-mtth` for the weighted audit discipline.
The skill maintainer added the reusable shared-affordability/manual-payment rule under the existing decisions skill's cost-localisation section, without Event 016-specific content.
Its dedicated handoff is `016_final_custom_cost_skill_note_2026-09-02.md`.
