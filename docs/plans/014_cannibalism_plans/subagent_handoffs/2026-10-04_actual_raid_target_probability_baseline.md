# Event 014 Actual Raid-Target Probability Baseline

Disposition: Read-only pre-patch baseline; target-pool and map-binding conclusions remain unresolved. This is not engine acceptance.

The parent selected the existing cannibalism_march_raid_supply_depot decision for a state-targeted hostile supply-node strike and real target receipt. The source proposal remains unapplied, and numeric supply-node damage is still pending parent choice. The accepted change keeps Larder 35, command power 10, the >9.99 command gate, 30-day re-enable, existing operation duration and recovery contracts, and AI score expression unchanged.

The fresh probability inspect was limited to that one decision in common/decisions/014_cannibalism_decisions.txt. It found one decision candidate and no numeric input paths; the source AI expression is base 60 with a 2.50 multiplier at war. The earlier owner evidence retains the two named score fixtures and raw values 60 in peace and 150 at war, classified as exact raw willingness scores with an incomplete target candidate pool. A fresh evaluation attempt returned partial with both submitted scenario-candidate instances excluded and five unresolved items, so it does not replace the earlier score evidence.

The current decision is untargeted: it has no state_target, target_trigger, selected-state capture, or target outcome. Its complete-country-decision result does not represent the per-state target pool proposed for the after patch. No selection probability is claimed.

## Frozen pre-patch sources and current logic

The raid proposal’s current_source_snapshot manifest records the exact capture labelled 14f045+GenGuard. Its decisions, effects, triggers, constants, and localisation hashes match the earlier ten-file Larder freeze; no before source was overwritten to absorb cap-owner work.

The current decision is cannibalism_march_raid_supply_depot at decisions lines 2569-2588. It is visible in the March Warlord phases, requires the March Host and March actions flags, and its availability only checks cannibalism_warlord_can_pay_march_operation_cost. It has no target-state gate or active-operation rejection gate.

The cost trigger at scripted_triggers lines 4980-4990 requires the command to be open, March Host origin, March actions open, Larder at least the 35 cost, and command power greater than 9.99. The operation effect at scripted_effects lines 17109-17120 pays those costs, adds the country-scoped March Supply Raid Operation for 30 base days plus existing route bonuses, and applies the existing recovery contract. It does not damage a selected state or publish a target receipt.

The AI expression at decisions line 2587 remains base 60, with the existing 2.50 war factor. Decision AI scores are willingness scores and must not be reported as click probabilities. No new weight, target score, or damage amount was selected.

The current generation guard remains the exact frozen cannibalism_current_actor_generation_matches trigger at scripted_triggers lines 2635-2641. The proposed raid receipt still needs the owner’s actor-generation and target-owner-generation checks; no receipt or raid target generation state currently exists.

## Declared target fixture contract

The existing score fixture names are event014_march_raid_supply_depot_peace_costs_satisfied and event014_march_raid_supply_depot_war_costs_satisfied.

The future target fixture cases are listed in evidence/raid_probability_baseline.json. They remain synthetic declared cases without concrete state IDs or typed scope bindings: peace with no eligible target, war with an adjacent hostile supply node, distant target, self or allied target, impassable target, missing supply node, node at damage cap, active operation, short and exact cost, and stale Event 014 controller generation.

The bounded map lookup used lookupOnly=true with query supply_node and limit 5; it returned zero query matches and zero inspected states. The server reported 1,081 states and 2,067 map source paths, with 64 paths inline. No second map query was made, and no target IDs, adjacency pairs, owners, controllers, damage states, or generation values were invented.

Before the patch, every target-specific case has no selected state because the current decision is untargeted. Its country-level AI score can be examined in peace/war, while valid/invalid target selection and target receipts are not measurable from the current source. The cost-short/exact states can be declared at the source boundaries, but the fresh scenario attempt did not establish the tool’s state bindings. Preserve that as unresolved.

## Candidate-pool and MCP evidence

The source inspect artifact, fresh partial evaluation, previous owner score artifacts, four-case Larder sweep hash, bounded map lookup, source hashes, revisions, reference citations, and the separate probability-render cache error are retained in evidence/raid_probability_baseline.json.

The current probability inspect reports one candidate because the before decision has one untargeted decision definition. The after patch changes this into a state-targeted candidate family; the MCP has not enumerated that family. The owner evidence also records the prior target-pool inspection as incomplete and empty.

The fresh evaluation used the two existing fixture IDs and submitted actor CBA, the March flags, Larder 35, command power 10, date 1936.1.1, and the peace/war state. The MCP reported both instances ineligible with five unresolved inputs. Do not infer that the prior 60/150 scores were disproved; retain the prior owner evidence and use this new attempt only as an input-binding gap.

A separate probability_render call returned PROBABILITY_ANALYSIS_NOT_CACHED even though the evaluation emitted ranking, waterfall, and unresolved artifacts. The owner proposal’s bounded resource reads also returned “Artifact provenance manifest is unavailable”; that is an artifact-access limitation, not balance evidence.

No further all-map or whole-decision inventory is requested. The earlier exact-ID decision inspection remains a partial global index, and no repeat was made.

## Recommended owner implementation checks

1. Keep the same decision ID, cost amounts and types, cost gate, cooldown, operation duration, focus recoveries, and AI expression.
2. Filter target candidates to enemy-controlled, passable states with a supply node and a directly neighboring passable state controlled by the March Host; reject self-owned and allied targets.
3. Recheck target validity and both Event 014 generations at transaction time before payment. If a post-debit check fails, refund the exact stored quote and suppress the modifier, recoveries, and success receipt.
4. Add an active-operation rejection gate before payment so overlapping operations cannot double-charge.
5. Apply the pending parent-selected numeric supply-node damage to the exact target state and record the actual state, strike result, date, attacker generation, and target-owner generation through the accepted Event 014 data owner.
6. Preserve the receipt on aborted attempts, clear it on existing actor-slot/generation reset, and render its actual result without claiming depot seizure or supply capture.
7. After the owner reports the full patch complete, run probability_compare through this auditor with the two existing score fixture IDs plus the same target fixture contract. If the target candidate pool or typed state-scope inputs remain unsupported, report the comparison as incomplete and keep selection probabilities unresolved.

No source, weight, damage value, GUI, or candidate target was changed or chosen. No comparison was started.

