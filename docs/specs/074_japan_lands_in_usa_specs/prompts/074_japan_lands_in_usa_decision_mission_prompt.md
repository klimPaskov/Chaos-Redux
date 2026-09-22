# Decision and mission implementation prompt: Event 074

Implement the action and mission contract in `docs/specs/074_japan_lands_in_usa_specs/design/074_japan_lands_in_usa_spec_part_4_decisions_and_campaign.md`.
Read Parts 2, 3, 5 and 6, the capability and acceptance references, current `AGENTS.md`, `chaos-redux-decisions-missions`, events, subagents and MTTH skills in full before coding.
Keep working plans and the audit under `docs/plans/074_japan_lands_in_usa_plans/`.

Use native decision categories with no new full-window GUI or resource wallet.
Japan has J01 receive forces, J02 repair unloading, J03 repair a transport corridor and J04 prepare an offensive.
The United States has U01 mobilize five paid formations, U02 prepare a city, U03 prioritize rail, U04 prepare a counterattack and U05 protect a port.
Implement exactly their targets, costs, preparation periods, completion limits and cancellation rules.
No action can charge more than four spendable cost types.
Use no more than three inline texticon cost values, with the complete fourth cost in the tooltip when required.

J01 and U01 are reserve-then-deliver transactions.
Debit the exact effective reservation at the start, record it, consume it once on valid delivery and never debit it again.
A legal precompletion cancellation refunds that recorded reservation once and creates no army.
The other seven actions are paid field work whose costs remain spent if combat, route loss or war ending cancels unfinished benefits after work starts.
A rejected click before commencement changes nothing.
Native PP cost and a custom PP debit must not both charge the same cost.
Respect universal cost modifiers consistently and refund historical paid amounts rather than later recalculated prices.

Follow-on force is a finite lifetime grant, not a purchasable unlimited army.
U01 uses an actual defensive template manifest and American manpower, infantry equipment, support equipment and Political Power.
Both systems require safe final deployment and save-safe completion receipts.
No unit appears in an overrun province or through an enemy connection.
Paid corridor projects modify actual legal routes, and completed repairs cannot repeatedly refresh a maximum-level landing bonus.
Prove local operational modifier scopes before implementing J04 or U04.

Implement J-M1 consolidation, J-M2 connection of separated pockets, J-M3 inland advance, U-M1 connected defense and U-M2 recovery of the original coast.
Show at most two simultaneous missions per actor.
Keep the immutable opening footprint, real continuous-hold tests, absolute deadlines and ordinary project waiting dates.
Mission rewards may accelerate a still-authorized batch or project only under the explicit schedule.
They do not increase a ceiling or revive grants after permanent support closure.
Do not reset hold deadlines on reload, retargeting or active evolution.
Distinguish success, genuine failure, invalidated target and cancellation.

Only working access and remaining special support are persistent public operational readings.
Show exact project allowance and blocked reasons contextually in tooltips.
Keep final writing concise, geographical and accurate without using the planning labels as finished copy.
Read the native category picture and icon references before wiring them.

Spawn `chaosx_decision_mission_auditor` with `fork_turns="none"`, passing this prompt, all named paths, user constraints, allowed write scope and the exact cost, timing and target questions.
Spawn the probability auditor for the action-weight and timing scenarios in the capability file.
Neither role may report an unexecuted test as passed or substitute manual weight estimates for the required tools.

Deliver the completed actions and missions, cost and scope evidence, lifetime allowance reconciliation, final localisation, assets/consumer coverage, and the T-cases relevant to decisions, supply, saves and evolutions.
Report blocked native consumers or transaction behavior concretely instead of dropping the affected action.
