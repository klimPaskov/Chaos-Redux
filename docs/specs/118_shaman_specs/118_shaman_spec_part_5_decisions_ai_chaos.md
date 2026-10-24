# Shaman, Part 5: Decisions, AI, history and Chaos

All labels are working labels, not final localisation.
This part fixes the visible action budget and the complete proposed weighted rules so that implementation can be audited against a definite design.

## A staged ordinary decision category

Use one ordinary event category with a static regional picture and native decisions and missions.
Its header names the visitor's home, current purpose, Local Cooperation and the next relevant date.
Put detailed outcome history in the existing Event Details and history surfaces.
Idle contact can collapse to a single quiet status entry and the peaceful end-contact action.

| Phase | Primary actions shown | Active missions | Exit |
| --- | --- | ---: | --- |
| Audience | Peaceful refusal, welcome, persecution | 0 | Accepted audience result or 30-day refusal default |
| Choose rite | Select land target, select military target when eligible, end contact | 0 | Commit within 90 days or offer expires |
| Review target | Up to three candidate rows, browse next page, return | 0 | Select a candidate, then review its quote |
| Confirm rite | Harmless cancel, normal work, urgent work when eligible | 0 | One accepted transaction |
| Rite in progress | Review current commitment, cancel work | 1 | Due date, cancellation or authority loss |
| Rite aftermath | Practical aftercare when eligible, end contact, review result | At most 1 | One completed follow-up or window expiry |
| Contact idle | Review contact, end contact | 0 | Eligible evolution or vision opportunity |
| Vision unanswered | Investigate once, limited preparation, full preparation, dismiss | At most 1 inquiry | One response or response deadline |
| Vision preparation | Review, upgrade when eligible, withdraw response | At most 2, inquiry plus preparation | Work and presence complete or deadline |
| Vision observed | Review result, reconciliation if eligible, end contact | At most 1 | 120-day cooldown or final closure |

Target browsing replaces the current action page.
It does not append every state to the main category.
A free review action opens information and cannot reselect, recharge or reroll a request.
No phase needs more than five primary rows or two simultaneous missions.
Mission timers, dates, costs, state names and observed result counts are ordinary facts, not additional persistent mechanic meters.

Native category pictures are appropriate for this surface.
The actual consumer, dimensions and static reference family must be inspected before art production.
The package does not require a separately scripted mechanic window to display one value and a few staged choices.

## Decision and mission inventory

| Working ID | Owner and visibility | Requirement and timing | Success, failure and cleanup |
| --- | --- | --- | --- |
| D01 Audience handling | Selected host, opening report only | Valid frozen home and generation | Welcome, peaceful close or one persecution reaction |
| D02 Land selection | Welcomed host during 90-day offer | One eligible local state and supported need | Save provisional target only, no payment |
| D03 Warrior selection | Same offer | Actual local hostile frontier and two eligible divisions | Save selected one-to-three-state set |
| D04 Rite confirmation | One provisional target | Same live quote and complete affordability at click | Consume entitlement once and start M01, stale confirmation is free |
| M01 Rite work | Same actor and generation | 21 days normal or 7 days urgent | Frozen result, defined conversion, or exact cancellation settlement |
| D05 Aftercare | One inconclusive or adverse result | Commit within 30 days, 14-day work | One practical contribution and cooperation change, no new rite |
| D06 End contact | Welcomed host | Harmless direct choice when idle, explicit cancellation confirmation if paid work exists | Close future opportunities, settle existing work exactly once |
| D07 Inquiry | One active vision | 40 political power, 5 or 3 days | Actual corroborating, mixed or contradicting evidence, no authenticity reveal |
| D08 Limited response | One unanswered vision | Current quote and enough work time | Start M02, one modest credit |
| D09 Full response | One unanswered or limited vision | Current quote, enough time and military presence feasibility | Start or upgrade M02, no duplicate credit |
| D10 Dismiss vision | One unanswered vision | No payment | Observe source for later result, no imposed punishment |
| M02 Preparation | Vision actor, target and source receipt | 7/14 days normal or 3/7 days imminent follow-up | Full, partial military response, unused readiness or cancellation |
| M03 Military presence | Full military response only | Two eligible divisions, seven consecutive days before deadline | Completes with paid work, resets local consecutive count if presence breaks |
| D11 Reconciliation | Active persecution aftermath or the original still-open panic receipt | One 30-day offer, its specified 14 or 30 day work | Remove only this event's remaining disruption and record closure |

M03 is projected as an objective inside M02 where native decision presentation permits it.
It must not become a third independent visible timer merely to expose a hidden counter.
The mission checks a real action, not a click on an acknowledgement.

All target names use live map localisation.
All costs use appropriate native texticons and one authoritative quote.
Separate nonconsumed conditions such as troop presence or a road requirement from spendable costs.
Give each unavailable action one leading practical reason, with complete details in its tooltip.

## Confirmation and payment rules

Every irreversible confirmation has harmless cancellation as its first option.
Native popup availability is checked again on click, since the original availability can become stale.
The immutable intent contains the action family, encounter and action generation, actor, state set, source identity, route mode, quote and due date.

One action lock prevents simultaneous confirmations for the same entitlement.
Withdrawing a request leaves its old-popup tombstone until that popup cannot act.
A newer request receives a new generation.
The old popup can only cancel itself.
It can never operate on the newer target.

Shared discounts are applied before the quote is saved.
Availability and payment compare against the exact positive quote, including rounding.
The event cannot show a discounted price and debit the ordinary price.
Timed production burdens use an event-owned modifier or native mission term with the exact receipt.
Cleanup removes only that burden.

A lost target before dispatch costs nothing.
During work, dispatched material and elapsed production are spent, held material is refunded once and future burdens stop.
At completed work the materials are spent and unused readiness is a real opportunity cost.
A state transfer never sends an equipment refund to the conqueror.

## AI information and decision principles

AI uses the same geography, actual crisis, time, affordability, inquiry findings and public uncertainty as the player.
Hidden identity, hidden rite result and hidden natural-hypothesis support are forbidden inputs to selection or response scores.
The AI cannot choose a successful branch because the result has already been stored.

Eligibility is evaluated before weights.
Impossible candidates have zero weight and cannot enter a random selector.
Peaceful refusal, cancellation or dismissal retains positive fallback weight where applicable.
Native decision `ai_will_do` is a willingness score.
It is not reported as an exact click probability or time-to-click distribution.

### Audience weights

The complete audience pool starts with welcome 80, peaceful refusal 20 and persecution 0.
A currently active local civilian crisis multiplies welcome by 2.
A relevant hostile frontier multiplies it by 1.5.
Strained starting relations multiply welcome by 0.75 and refusal by 2.
Resource scarcity multiplies refusal by 2.
Scarcity means the cheapest useful valid rite would consume more than 25 percent of either relevant available stockpile after shared prices.

Persecution receives weight 5 only when an actual existing government-policy source establishes active coercion against local independent institutions.
Mere ideology or culture is insufficient.
If no such policy predicate is implemented, its AI weight stays zero while the player choice remains available.
Persecution's weight does not read the visitor's hidden type.

Native audience sampling normalizes the eligible weights.
A non-eligible response has weight zero.
If all non-refusal responses become invalid, refusal has weight 1 or greater.
The normal benign complete pool therefore gives 80 percent welcome and 20 percent refusal.
That figure does not apply to modified cases.

### Choosing a rite and target

Land and military selection use scores to prioritize real need.
Start land at 40 when a usable calm reserve benefit exists, 100 for a real crisis or repair need, and 180 for an owner-classified severe civilian crisis.
Start military at 100 only when all local-frontier and troop gates hold.
Multiply military by 1.5 when the focus state is a capital or the home state, and by 0.5 if the operational window is likely to close before normal completion.
A war elsewhere supplies no military score.

Multiply a rite score by 0.5 under the same 25-percent-stockpile scarcity test, and by zero if it is unaffordable.
Within land modes, use severity scores 4 for severe active famine or disease, 3 for serious current damage, 2 for other actionable crises, and 1 for calm reserves.
Tie-break with larger currently usable benefit, then the home state.
Do not add population weight after the benefit already reflects population.

For normal versus urgent work, normal has weight 80 and urgent 20 when both are meaningful.
If the recorded threat arrives before normal completion but after urgent completion, set normal to 0 and urgent to 100.
If neither can help in time, decline or choose another valid state before commitment.
AI cannot pay for an already obsolete operation.

### Vision response weights

When the AI reaches the response-choice report, native event `ai_chance` or one equivalent explicit probability-proportional selector samples the complete eligible response pool.
Do not implement these numbers as a highest-score-wins rule.
The complete response pool starts with dismiss 35, limited 45 and full 20.
Apply the following factors in order, then remove invalid or unaffordable responses.

| Observable condition | Dismiss | Limited | Full |
| --- | ---: | ---: | ---: |
| Owner-classified severe natural threat or a threatened capital frontier | ×0.5 | ×1 | ×4 |
| Corroborating completed inquiry | ×0.5 | ×1 | ×2 |
| Contradicting completed inquiry | ×3 | ×1 | ×0.25 |
| Scarcity at the full-response quote | ×2 | ×0.5 | ×0.25 |
| Full work or troop condition cannot finish in time | ×1 | ×1 | ×0 |
| Limited work cannot finish in time | ×1 | ×0 | ×0 |

Corroborating and contradicting cannot both apply.
A contradiction does not erase a severe official threat.
Their combined factors are deliberately reviewable.
A paid inquiry is considered only once, with willingness 60 if at least five normal days, or three emergency days, can be spent while leaving full preparation feasible.
That score becomes 0 when political power is insufficient or the inquiry cannot change any available response.
Inquiry does not consume the response choice.

AI aftercare willingness is 80 when an adverse burden remains, 50 when useful conventional relief remains after an inconclusive result, and 0 when there is no applicable effect.
Affordability is mandatory.
Reconciliation uses willingness 70 while real panic or unrest remains, or a still-open original panic receipt has a recoverable cooperation loss.
It is 0 when neither an active burden nor recoverable cooperation remains.
End-contact willingness is 10 when idle and 60 when cooperation is strained after two completed poor outcomes.
These are native willingness scores only.

## Named balance scenarios

The probability review must calculate the exact complete pools where possible and classify the remaining outputs honestly.

| Scenario | Declared conditions | Required conclusion |
| --- | --- | --- |
| P01 Ordinary welcome | No crisis, no relevant front, workable relations, ample stocks | Audience 80/20/0 |
| P02 Crisis and frontier | Active civilian crisis and relevant front, workable relations, ample stocks | Audience weights 240/20/0, with exact normalization |
| P03 Occupied scarcity | Strained relations and scarce stocks, no crisis/front, no coercive-policy predicate | Audience weights 60/80/0 |
| P04 Three rite bands | Base hidden distribution, normal pace, strong/workable/strained cooperation | All identity rows nonnegative and mixed totals exact |
| P05 Urgent rite | Same three bands with urgency | Five points move from effective to adverse, no row negative |
| P06 Severe corroborated warning | Severe threat, corroborating inquiry, ample stocks, both responses feasible | Dismiss/limited/full weights 8.75/45/160 |
| P07 Severe contradicted scarcity | Severe threat, contradicting inquiry, scarce full quote | Weights 105/22.5/5, verify the intended dismissal preference |
| P08 Expiring warning | Neither work period can finish | Dismiss only, no paid response |
| P09 Local war relevance | Host at war elsewhere, no eligible local frontier | Military score zero |
| P10 Natural hypothesis support | Base hidden distribution at 400 and at 600 | 57 and 60 percent source support, never called accuracy |
| P11 Evolution cadence | All combinations of the three 0.75 modifiers | Median range and clamping, eligibility time separated from wall time |
| P12 Multi-major targeting | Three eligible hosts, one calm, one crisis, one crisis plus front | Host weights 1/1.5/2, complete-pool shares only for this fixture |

No old Shaman gameplay implementation was found in the inspected registry or event filenames.
There is no genuine before/after balance baseline.
Compare the declared design variants with each other and label them as candidate comparisons, never as measured changes to a running event.

## Chaos impact map

Baseline visit, welcome, target selection, payment, ordinary successful aid, peaceful refusal, evolution activation, logging and unused readiness add zero Chaos.
The event uses the shared Chaos History owner for the following actual consequences.

| Consequence | Proposed change | Gate and repeat guard | Overlap and reversal |
| --- | ---: | --- | --- |
| Exceptional rite produces a positive delivered anomalous effect | +6 | One encounter flag, only after a real effect starts or reserve credit adds a positive amount | No separate award for later installments |
| Adverse rite produces an actual local setback | +3 | One encounter flag, measured spoilage or a real active harmful modifier | Subsequent famine deaths remain the famine owner's consequence |
| Persecution causes actual local disruption | +2 | Only the reaction branch that installs a valid local consequence | No award for choosing persecution if no reaction occurs |
| First natural vision yields a matching useful preparation or exact source-supported consequence | +4 | Once per encounter, owner outcome receipt and meaningful threshold required | Does not duplicate disaster escalation, Deaths or event 013's outcome |
| A false alarm creates actual local panic | +2 | Once per encounter, only after the defined reaction occurs | False warning without panic adds zero |
| Practical aftercare contains an event-owned adverse burden | -1 | Once per encounter and only if that burden previously earned positive Shaman Chaos | Cannot reduce more Shaman Chaos than this encounter added |
| Reconciliation ends event-owned persecution disruption or panic | -1 | Once per encounter, actual remaining burden removed after work | Same encounter-owned positive balance cap |

Use named proposed reason keys under the event's owner namespace.
Allocate numeric reason identifiers only after checking the current shared constants and reservations.
None are silently reserved by this document.
Cultural profile and government nationality never scale the Chaos amount.

The safe gross positive envelope is +12 for a welcomed encounter or +2 for the separate persecution branch.
Deferred delivery means a tighter total should not be claimed from cooperation alone.
Negative changes can never exceed that encounter's already recorded positive Shaman balance.

The magnitude is deliberately local.
The mutually exclusive initial choices and finite three-vision cap bound the chain.
A conventional famine improvement or ordinary defensive success does not become anomalous merely because it belongs to Shaman.
If an exceptional outcome's food credit cannot deliver any reserve before expiry, it earns no manifestation Chaos.

Record one source transaction for each change.
Deaths, actual disease mortality, combat casualties, world tension, contamination and disaster escalation stay with their existing owners.
A shared-source suppression rule takes precedence over an event-owned award if both describe the same anomalous physical occurrence.
Negative changes only contain this encounter's recorded destabilization.
They do not reverse the shared historical death count.

## History and Event Details

The root history entry is recorded after host, profile and home selection.
It identifies the government as the actor and the home state in the detail payload.
The evolution writes one later row with the same actor.
A changed controller does not rewrite historical authorship.

Store compact result entries for audience handling, rite family and target, committed quote, pace, delivered outcome, aftercare, each issued vision, the selected response, owner adjudication and closure reason.
History distinguishes a requested benefit from actual delivery and a modelled consequence reduction from an observed population or building change.

Event Details explains the premise and evolving relationship in player-facing prose.
It does not list every coefficient in the catalog description.
A separate mechanics tooltip carries local scope, costs, timers and current effects.
The coding agent writes final localisation from Part 6's directions, preserving dynamic country and state names and the distinction between conditional and verified outcomes.
