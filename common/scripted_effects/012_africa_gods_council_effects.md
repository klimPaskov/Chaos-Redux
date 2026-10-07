# Event 012 Final Council shipment API

The participant can pledge the existing 1,000 infantry equipment while retaining 500, or spend the existing 25 political power to speak at the Council.
The amounts remain owned by `gods_of_africa_council` in `012_africa_gods_constants.txt`.
These choices appear after any ordinary demand, negotiation, reconciliation or final ultimatum has ended.
No existing clock or settlement deadline is paused or extended.

## Scope and ownership

All helpers execute in participant COUNTRY scope with boolean calls and no parameters.
`gods_of_africa_council_pledge` remains the public focus-payoff entry point and delegates to `gods_of_africa_pay_council_pledge`.
The first affordable attempt freezes the participant and receiver scope identities, origin, generation, authority epoch, total, unpaid balance and reserve.
The scope references and `.id` values are compared for identity and are never treated as country ordinals or used in arithmetic.
There is no inferred shipment amount: a fresh quote uses the Council constants, and a current pledge uses its frozen unpaid balance and reserve.

`gods_of_africa_council_pledge_can_be_paid` is the shared click-time preflight for phase, current participant history, clear native accounting, retry time, positive unpaid balance and actual stock above reserve.
The decision presents those same requirements with player-facing tooltips.
The affordability helper uses separate temporary variables for a new quote and a current pledge so branch evaluation cannot overwrite the other quote.
The scripted-localisation getters read the matching frozen amount and reserve, never a stale display cache or a caller's temporary variables.

## Native transfer and credit

The synchronous owner sets `gods_of_africa_council_pledge_transfer`, supplies the shared contribution inputs, calls `gods_of_africa_begin_material_transfer`, and sends rifles only when that helper authorizes emission.
The recipient is a regular event target saved from the frozen pledge host scope.
The shared contribution guard admits this precise Council context as voluntary infantry support; the ordinary voluntary-aid guard explicitly excludes the Council purpose flag.
The shared source-stock check uses the Council's frozen balance plus reserve, preserving the ordinary aid lane's existing capacity requirement.
The receipt carries `gods_of_africa_material_receipt_council` as provenance alongside the existing voluntary flag.

The owner calls `gods_of_africa_complete_material_transfer` immediately after native `send_equipment`.
Its consumed receipt credits the participant's actual stock loss, bounded by the requested amount, to total and voluntary infantry contributions and the campaign subset when its existing proof passes.
This follows the accepted L3 donor-loss policy; it does not invent a new receiver-equality rule.
Africa's common-defence reserve increases only by measured receiver gain, bounded by that consumed donor amount.
No nominal quantity is credited to the reserve.

A positive short delivery reduces only the unpaid balance; a later click pays that balance and retains the frozen reserve.
Zero delivery consumes no material credit and opens the existing seven-day undelivered retry interval for this Council action.
An unreadable or identity-drifted transfer retains the shared evidence and grants neither Council credit nor another payment permission.
The Council owner does not clear that unresolved evidence.

`gods_of_africa_complete_council_pledge` consumes live terms before publishing the Council voice, pledge flag, one aid-history entry and the existing World Order history update.
It requires a current pledge with zero remaining balance.
No partial or empty shipment publishes those final outcomes.
The existing ordinary-demand denominator, contract counts, demand deadline and voluntary-aid cooldown are untouched.

## Speech and cleanup

The political speech requires clear native accounting even when live pledge terms are absent or stale.
An uncharged quote may be replaced by that speech, but a partly paid pledge cannot be abandoned through the alternative price.
The speech preserves its original political-power payment and outcome and then clears the uncharged quote.

`gods_of_africa_clear_council_pledge` removes only the live pledge flag, transfer-purpose flag, frozen terms and Council retry date.
It runs on invalid-participant archival, participant cleanup, unifier-loss cancellation, permanent defiance and the guarded successful settlement finalizer.
It also runs when the pledge completes or an eligible speech replaces an uncharged quote.
Measured contributions, durable Council voice/history and unresolved shared native receipts are preserved.
No refund or successor-host delivery is inferred from cancellation; supplies already sent remain sent.

Usage remains `gods_of_africa_council_pledge = yes` from the existing participant decision.
No new asset is required: the pledge and speech retain their existing decision icons.
All price, reserve, retry and explanatory strings remain in `012_africa_gods_l_english.yml`; the amount/reserve getters live in `012_africa_gods_council_scripted_localisation.txt`.

## Evidence and limits

Acceptance basis is the full-Gods goal and accepted L27 Council shipment, combined with the accepted L3 measured-contribution contract and October 7 decision audit.
Installed `documentation/effects_documentation.md:6550–6558` documents the native COUNTRY transfer; vanilla `common/scripted_effects/USA_scripted_effects.txt:403–418` supplies its `equipment` spelling.
Offline `Effects - Hearts of Iron 4 Wiki.md:2254` documents partial native delivery rather than negative source stock.
The shared contribution helper API records the native measurement contract and its limits.
Independent source review, named Council probability scenarios and parent integration evidence belong to the October 7 Council handoffs under `docs/plans/012_africa_plans/subagent_handoffs/`.
Those source/MCP checks do not prove native stock deltas or decision-row appearance.

No broader Council expansion or new mechanic is proposed.
