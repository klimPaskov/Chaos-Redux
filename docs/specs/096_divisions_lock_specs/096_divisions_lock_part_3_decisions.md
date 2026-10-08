# Event 096: voluntary decisions and transactions

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

## 1. The player's control

Use one ordinary decision category with two primary actions. The first requests one random eligible formation. The second requests a dynamically sized severe-excess batch. Keeping the army and growing the country is the default behavior when neither action is used. It does not need a third button.

Both actions are optional and have no political-power, command-power, stability, equipment, or manpower fee. The removed fielded formation is the substantive sacrifice. Do not add a reward for clicking, an artificial allowance purchase, or repeated containment points.

A decision click opens a confirmation. It never removes a unit immediately. The player authorizes a bounded random removal, not a named target. Selection occurs only after the final eligibility check, so reopening or cancelling a confirmation cannot preview and reroll a selected unit.

The native country lock stays held throughout. There must be no temporary interval in which the player can edit templates or recruit through a general unlock.

## 2. Action contract

The identifiers below are proposed internal identifiers. Their associated player-facing wording is direction only.

| Field | One-formation action | Severe-excess action |
| --- | --- | --- |
| Proposed ID | `division_inspection_disband_one` | `division_inspection_disband_batch` |
| Purpose | Reduce a modest excess or take a smaller deliberate risk | Reduce a substantial structural excess without excessive repeated clicking |
| Visible | Current Event 096 hold and F greater than A | Current hold and severe excess, or a pending batch receipt that still needs resolution |
| Available | Fresh valid calculation, a removable owned formation, no pending request or daily execution guard | Same, e at least 0.75, and at least two currently eligible formations |
| Authorized bound | One | k calculated below and frozen in the request |
| Spendable resource cost | None | None |
| Completion | Confirmed exact random removal, followed by immediate refresh | Confirmed bounded sequence, stopping early when required |
| Repeat | At most one successful Event 096 demobilization transaction per country per game day | Shares the same guard |
| Cancellation or timeout | No removal and no resource charge | Same |
| Native AI decision execution | Suppressed in favor of the single policy in Part 5 | Same |

Ordinary frame-driven category visibility and availability read the last complete published snapshot for the current actor, grant, and regime, plus cheap current lifecycle, request, and eligibility guards. They never scan states, formations, or global participants every UI frame. A stale, missing, or incomplete snapshot temporarily withholds availability and requests the existing local refresh. Opening a request and committing it require fresh complete calculations. A cached display is never destructive authorization.

Let N_owned be the current number of genuinely owned fielded land divisions. It excludes borrowed formations and non-land units. It is used only to size the optional action, never to measure F or set A.

**k = min(10, max(2, ceiling(0.10 multiplied by e multiplied by N_owned))).**

Clamp the displayed authorized bound to the current eligible count. If fewer than two eligible formations remain, the batch is unavailable. This produces a two-formation batch for small forces and a larger batch for a very large oversized army. The ten-formation ceiling bounds the destructive transaction and keeps the confirmation's risk legible.

A twenty-division country at e equal to 0.75 requests up to two. A one-hundred-division country at the same excess requests up to eight. A four-hundred-division country at e equal to 1 requests up to ten. These are action examples, not national army caps. A player can always choose the one-formation action instead.

The one-successful-transaction-per-day guard prevents duplicate execution from rapid clicks and gives the game a clean refresh boundary. Failed or cancelled requests do not consume it. No extra progress meter or repeated financial payment is attached to this guard.

## 3. The eligible population

All burden-bearing formations remain in F, including units that cannot be removed by these actions. The removal pool is narrower.

| Formation condition | Pool treatment |
| --- | --- |
| Owned, fielded, ordinary formation under the acting country's removal authority | Eligible if native disband preconditions pass |
| Merely stationed on the acting country's land | Location alone provides no eligibility |
| Borrowed expeditionary or other foreign-owned formation | Excluded |
| Sent expeditionary, volunteer, or exile formation under a foreign operational or source-owner transaction | Excluded until the legitimate authority relationship permits removal |
| Event-owned formation with a ledger, protected identity, or required lifecycle callback | Excluded unless its provider supplies a verified exact compatible removal transaction |
| Active combat or a native state that forbids administrative disband | Excluded |
| Quiet front assignment or unthreatened garrison duty | May remain eligible for a human action, so the confirmation must communicate the possible military consequence |
| The player's final owned formation | May be removed only through a current explicit human confirmation while F is still above A |
| The AI's final owned formation or known essential defense | Excluded by the stricter AI policy |
| Robot, rat, or other unusual identity | No identity-only immunity. Apply actual ownership and protection rules |

Do not claim a generic combat, encirclement, template-lock, or source-ledger predicate exists until verified. The retrieved division trigger list does not establish all of them. This is part of the exact safe-removal gate in Part 7. If the required pool cannot be proved for a class of formation, that class cannot be selected by guesswork.

Human confirmation deliberately permits strategic risk. Event 096 does not promise to identify every critical front for the player. The initial firing leaves all orders unchanged, while an explicitly chosen removal naturally changes which formations remain to carry them out.

The player does not receive a target selector, a candidate roster to choose from, or a preselected identity to reroll. Eligibility can change through ordinary gameplay, but the event itself always samples the current eligible records uniformly. A smaller eligible pool naturally changes the distribution. Do not market this as an inability to influence the pool through any game action.

If every remaining formation is protected or otherwise ineligible, keep the live excess and explain the blocked reduction route. Growth, return of foreign arrangements, legitimate provider transactions, or a later change in eligibility can resolve the situation. Do not fake an empty army or forgive excess merely because the pool is empty.

## 4. Confirmation state

Use a native country event or an existing supported confirmation surface. Its first and default option is the cancelling path. A native timeout, window dismissal where supported, or loss of authority must never authorize removal. The project references describe ordinary event timeout behavior around thirteen days, but the installed behavior must be checked and the cancelling option must remain safe regardless of duration.

One country has at most one live request slot. Store the following durable request fields before opening the popup:

| Field | Meaning |
| --- | --- |
| Request identity | Unique request serial within the country |
| Inspection context | Firing grant, local episode and current regime revision |
| Actor | Exact acting country and current valid control authority |
| Action | One-formation or batch |
| Requested bound | The exact up-to count the player saw |
| Final-formation permission | Whether the human confirmation explicitly disclosed and authorized a possible zero-owned-fielded-army outcome |
| Request state | Pending, invalidated, executing, completed, or cancelled |
| Creation and expiry state | Supports cleanup without granting timeout consent |

The force and allowance displayed when the popup opened are informative snapshots, not permission to act against stale values. The confirmation explains that the bound may stop early after compliance, loss of eligibility, or a changed authority condition. It must accurately describe ordinary equipment and manpower treatment once native disband semantics have been proved.

When the current one-formation action or authorized batch can remove the final owned fielded land formation, the confirmation must explicitly disclose that the country can be left with no owned fielded land army. Use qualitative consequence wording without a new public counter or a selected-unit preview. Freeze whether that consequence was disclosed and authorized in the request. If intervening changes introduce a final-formation risk that the original confirmation did not disclose, invalidate before the first removal or stop before the now-final removal in an already valid partial batch. A new confirmation is required for that new risk. AI never receives final-formation permission.

A repeat firing, relevant evolution change, release, country invalidation, or control handover invalidates the request. Retain its identity and frozen fields until the old popup terminates. Do not clear and reuse the same variables while an old option can still read them. Invalidate first, then let its cancelling or terminal path retire it. The active category indicates that the old request must resolve before a fresh one is opened.

Native events do not automatically prove immutable parameter capture. The implementation must demonstrate how the popup refers to the correct receipt and how authority changes are detected. A condition that is true only when the popup opens is insufficient, because options can be clicked later.

## 5. Commit sequence

1. Prove the request is still pending, matches its exact actor and current inspection context, and has not been consumed. Verify that the player or AI authority taking the action is the authority permitted by that request.
2. Refresh the complete force and capacity calculation. Verify the Event 096 hold remains active and F is greater than A. An already compliant country takes no further loss, even if the floor is still running.
3. Verify the action remains available. For a batch, recompute its fresh allowable bound before the first removal. If it is below the bound presented in the request, invalidate the request instead of silently replacing it with another action. A changed pool that merely limits safe execution later still uses the documented up-to stop rule.
4. Mark the receipt executing before consuming randomness or mutating a unit. Apply the country transaction guard.
5. Build the currently eligible pool, choose one record uniformly, prove that exact formation is still eligible, and invoke the proven exact administrative disband operation under the retained lock.
6. Refresh F and A from the actual live country. Record the actual number removed. Do not subtract a guessed average formation weight or claim the full requested count succeeded.
7. Before another removal, stop if F is at most A, the bound is exhausted, the eligible pool is empty, the source-owner contract fails, the actor becomes invalid, or the transaction guard is lost. The severe-excess threshold authorizes the transaction at its first commit. Crossing below it during a successful batch does not itself change the already authorized upper bound.
8. Finalize the receipt exactly once. Set the daily execution guard only after at least one actual removal. Refresh release eligibility immediately. Retire or preserve the native popup receipt according to its terminal state without exposing a new request to an old option.

Sampling is without replacement because a removed unit leaves the live pool. Membership can change between removals, so rebuild or revalidate it each time. The maximum ten-step sequence stays well below the project loop ceiling. It never clears an unrelated iteration queue or drops an unvisited suffix.

If a partial batch encounters a legitimate stop, retain the completed removals and report the actual outcome. Do not invent transactional rollback by respawning approximate formations. A duplicate completion callback sees a consumed receipt and performs no further mutation.

## 6. What administrative disband means

The selected design seeks ordinary administrative demobilization with the installed game's legitimate return of actual surviving manpower and equipment. It does not award the template's paper establishment, duplicate stockpile variants, replace a destroyed formation, or add casualties to a death system.

The available reference proves that country `delete_unit` has a refundable `disband = yes` option, but its filters can remove multiple units. It separately documents exact division-scoped `destroy_unit = yes`, without establishing its refund behavior. Neither fact proves that an arbitrary randomly selected formation can be safely and exactly demobilized with refunds under the country lock.

Before implementation signoff, prove an exact supported operation or an equally exact provider-owned transaction, including equipment variants and zero-human formations. Do not use an empty `delete_unit` block, a shared-template deletion, or fabricated `destroy_unit` parameters. If exact administrative semantics cannot be delivered, report that design capability as blocked. Silently converting the action into equipment destruction would be an unapproved design reduction.

## 7. Presentation and cleanup

The category shows force, allowance, and one contextual time value. It has no dedicated mission. The lock has a floor and a condition, not a deadline that can fail and delete troops. During an evolved watch the two removal actions are hidden, because this event is no longer holding the country's templates.

The confirmation's requested count is the fourth permitted value. Do not add a public eligible-unit counter, deficit percentage, individual formation price, pressure stockpile, extension debt, or parallel progress bar. Describe why an action is unavailable in words tied to actual failed conditions.

Country disappearance, explicit clear-active-effects, completion, and successor transfer stop future execution and invalidate requests. Durable achievement and event-history receipts remain. Cleanup never removes a unit, changes an order, grants a refund, clears another owner's native hold, or rewards a request that did not execute.
