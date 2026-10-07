# Event 098 New Ore: Decisions, agreements, and mission handoff

Use `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-mtth`, and the current shared cost documentation. Read every source-spec part, especially parts 3, 4, 8, and 9. Read the research notes before selecting native cost, targeting, or lifecycle helpers. The accepted scope is ordinary targeted decisions, short diplomatic events, and one contextual state-defense objective.

## Interaction structure

Implement the part 3 action families and part 4 escalation/defense choices. The ordinary category exposes current effective ore armor and directly controlled deposit count, with an eligible static picture, native state selection/highlighting, and readable records. Keep three to five contextually useful primary actions, six at most. The full set of valid deposits must remain reachable. AI gets its own complete registered target set and never depends on a human's selected state.

The practical route coverage is inspect, request, offer, respond/confirm, renew, buy back, abandon, reassign, demand, prepare after refusal, withdraw the dispute, defend a source, and resolve the defense mission. Commercial, security, and faction allocation are separate families within those actions, with the exact payments and commitments from part 3.

Each decision record must specify actor, target scope, appearance, availability, exact blocked reason, cost quote, immediate and delayed consequences, success/failure/cancellation, dates, repeat guard, AI behavior, and cleanup. Source and participant identities remain bound to the original episode when the player changes selection or a nested event changes ROOT/FROM.

## Agreement state and consent

Distinguish a proposal, its single counteroffer, final confirmation, current paid term, at most one paid future renewal period, protected paid access, normal expiry, voluntary abandonment, buyback, consensual source reassignment, and terminal invalidation. These are bounded records, not a new player-managed diplomatic score system.

Revalidate supplier control, recipient, source, relationship, country/source limits, actual quote, and affordability at final confirmation. No proposal gives access or transfers compensation. Commit payment and activation as one logical action. A failed activation returns only actual paid components, once, and releases any place.

Each source has two foreign places, three after Deep Vein. Each supplier has six distinct foreign customers at most, and each recipient has two source agreements at most. Duplicate source/country contracts do not stack or take another place. Direct access overrides foreign access. Two foreign licences use only the strongest valid benefit.

A capture, war between parties, or invalid actor terminates the named source agreement. An unchanged controller survives a legal ownership change. Terminated agreements never revive merely because an earlier controller returns. A consensual source reassignment preserves both current and future paid periods and cannot rescue an already terminated contract retroactively.

Before a voluntary event-controlled peaceful sale or cession by the supplying controller, settle all affected actual unused paid periods through buyback. Other already-effective non-hostile native transfers still end source agreements immediately, but unsettled prepaid delivery triggers the supplier-wide 720-day zero AI acceptance of new prepaid commercial/security deals. Distinguish actual hostile capture and imposed wartime peace from friendly side deals during an unrelated war. Reacquisition and new offer terms cannot erase the recorded failure.

Honor protected commercial/security paid periods when the supplier causes a non-hostile qualification loss or attribution cannot be established. This protection includes a future period already confirmed while qualified. A proven recipient breach ends its access. Current requirements must be valid to purchase another renewal. Faction allocation requires continued faction membership and contains no prepaid equipment income.

Continuous renewal adds one future period beginning at current expiry and charges no adaptation XP again. Buyback refunds the unused fraction of actual current-period equipment plus the entire actual future-period amount before it begins. It spends supplier stock. Capture/war risk applies to both periods as disclosed at confirmation. Keep period-specific receipts so discounted amounts and dates never become reconstructed guesses.

## Exact costs and native payment

Implement the calibrated anchor and factor tables from parts 3 and 9. Commercial is support equipment plus trucks plus one eligible adaptation XP type. Security is infantry equipment plus support equipment plus one eligible adaptation XP type, along with its real native commitment. Faction uses its adaptation XP and scarce export place. Continuous renewal omits the already expended adaptation cost.

Relevant pricing capacity is controlled military factories plus dockyards, independent of queue assignments. Apply grade, one bargaining factor, term, and premium choice exactly as specified. Use the bounded XP factors and real historical experience qualification. A final price is fixed at confirmation for its period.

Resolve concrete supported equipment tokens, variants, removal behavior, and real supplier credits through verified native/source evidence. Receiver credit must equal actual payer debit after discounts. Do not create an undiscounted shipment because a helper's displayed base cost was higher. Record actual successful components before any nested call can overwrite their context.

Use the universal cost framework's inclusive affordability and quote contract with the correct country payer. Inspect its implementation before relying on rounding or exact matching. The research found a material documentation/code mismatch in ceiling and comparator behavior. Prove below/equal/above boundaries and fix the owning helper through the authorized owner if needed. Do not carry a known mismatch into Event 098.

All displayed prices, custom availability, debit, and refund must consume the same normalized quote. A native custom cost tooltip does not itself spend resources. Army and Navy branches spend one XP type, not both. Every action uses at most four spendable types and the planned maximum here is three. Command Power costs stay within the project ceiling and this event's tighter ranges. Follow the short inline cost text contract, with full explanation in the proper tooltip.

## Demand and preparation

Implement the concrete failed-negotiation requirement, interested and capable actor, reachable real source, valid ordinary diplomacy, exact payment capacity, one demand episode, response deadline, and pair cooldown from part 4. Same-faction and subject/overlord coercion routes are excluded as specified. A claim affects cost and priority without granting control or access.

Supplier acceptance proceeds through normal final confirmation. An unaffordable or over-cap accepted request closes as uncompleted acceptance, with no new refusal credit. The delivered attention cost remains spent. An actual refusal or unanswered demand gives the requester a choice to withdraw or undertake ordinary war-goal preparation.

Use the real supported native war-goal form and truthful description of its scope. A limited-state purpose cannot be described as a guaranteed limited settlement when the available war goal is broader. Prove exact cleanup of Event 098-owned preparation without removing unrelated native goals or orders. War is never declared automatically by this event.

Supply, naval reach, relative force, factions, guarantees, truces, and ordinary political rules remain meaningful. Ore-oriented AI must use verified state-defense and offensive-target consumers. A generic country hostility value alone is not state-targeting evidence.

## One meaningful defense objective

The source-defense mission requires actual current control and a real enemy front or credible incoming operation. It costs the declared bounded CP, commits an appropriately equipped friendly force, and uses the part 9 threat-dependent 120–270-day period. Success keeps continuous control through the due date while the threat remains real, then grants the correct Army or Navy XP once.

Losing control fails the objective immediately. The ore benefit transfers normally. If the threat ends first, close neutrally with no success reward. Record the country/state 720-day repeat guard. Timing uses actual dates and stored episode identity. Extend or update a native timer only through the supported idempotent remaining-duration contract.

Inspect the actual mission engine behavior. Its availability or completion predicates must not auto-complete merely because the source was controlled at activation. Match success, failure, timeout, and cancellation scopes to exact native documentation and the closest working project precedent.

## Visibility, localisation, and tests

Write final player text from the source directions, including the real material terms, control risk, protected period, future renewal payment, early buyback, and precise failure reason. Keep Event Details descriptive and place actual numeric effects in their proper tooltips and decisions. No internal receipt, index, or actor-binding implementation detail belongs in the player flow.

Use current decision allowed/visible/available and target predicates in their actual refresh phases. Permanent startup filters must not contain changing eligibility. Bound frequent work to selected or registered candidates. Scope country helpers explicitly when a state-target context makes ROOT a state. Avoid whole-world scans inside per-frame or daily target predicates.

Deploy `chaosx_decision_mission_auditor` for a read-only audit and `chaosx_ai_probability_auditor` for the full named weighted scenarios. Start probability work with `hoi4.probability_inspect`, then evaluate, sweep, and compare. Render useful event/GUI/probability evidence through available project routes. Do not claim engine or visual validation from source text alone.

Pass A14–A35 and A41–A49 where applicable, including exact-affordability equality, partial payment, two paid periods, supplier fault protection, target changes, direct-to-foreign fallback, unreachable AI, native timer behavior, and save/reload. Keep all route implementations and failures in the parent route-coverage table. Return exact files changed, review evidence, unresolved native constraints, and a bounded handoff under `docs/plans/098_new_ore_plans/subagent_handoffs/`.
