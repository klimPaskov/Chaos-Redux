# Shaman, Part 3: True Sight

All labels are working design labels, not final localisation.
This part defines the sole evolution requested in the brief.

## The changed relationship

True Sight begins at Chaos 400 or above through the eligibility and timing rules in Part 1.
The visitor starts naming places and consequences with unsettling specificity.
A warning identifies one state in the home region, a concrete danger, a time window and a preparation that could help.
The government can investigate the evidence, make a limited response, make a full response or dismiss it.

The event is still regional.
A visitor from one community does not become an omniscient global intelligence service.
A government fighting far from that home gains no distant combat prediction.
A warning can be correct but only partly preventable.
Preparing can also consume material and industrial capacity without useful effect.

The opening rite and True Sight are separate entitlements.
Welcoming the visitor is required.
Completing a successful rite is not.
A government that experienced an inconclusive or adverse rite can retain contact and later face the choice of whether to believe a warning.

## Existing forecasts remain intact

Event 013 already presents an exact official forecast after a disaster is accepted, including the state, family, severity and scheduled date.
Shaman must preserve that information.
It does not conceal an existing warning, postpone official notice or receive credit merely for repeating the forecast.

True Sight contributes a focused hypothesis about a consequence and an extra preparation opportunity.
Examples of design direction include the principal danger to civilians in a named flood state, damaging shaking at an exposed industrial district, or a specific follow-up that is already queued.
Officials can compare the vision with the public forecast.
The account can still leave uncertainty about whether the visitor inferred the danger, guessed correctly or saw it.

The existing disaster job snapshots are not future simulation results.
They contain current or previous fields.
Nothing in this design treats them as a stored future casualty count.
An owner-approved projection may expose accepted job facts and current exposure.
It must describe any inferred consequence as conditional.

## Cadence and limits

Only one vision can be active for the encounter.
Do not issue a new vision while rite selection, rite work, its aftercare offer or work, or a reconciliation job still occupies the contact.
The government can close an unused aftercare offer to become idle.
Inquiry and the matching preparation may overlap only within the same issued vision.
A valid opportunity may be issued once True Sight is active and the contact is idle.
After a vision resolves, the next opportunity has a 120-day cooldown.
The government can receive at most three issued visions.
The third closes new vision opportunities immediately after its result.
Any earned 30-day aftercare or reconciliation offer remains available through its original window, and paid follow-up work can finish.
Natural retirement then closes the contact.
Completed finite services retain their original expiry and owner processing, while no new grant can be created.
Voluntary dismissal or authority loss instead uses the explicit cancellation policy.

A canceled or void vision still uses its issued slot.
It reports why it could not be judged and does not count as a correct or false warning for achievements or cooperation.
This finite rule prevents repeated target changes from generating endless replacement offers.
An opportunity that fails validation before it is shown does not use a slot or start the cooldown.

There is no daily world search.
The contact registers with relevant bounded owner notifications and an existing eligible-host scheduler.
Candidate checks examine only the profile's reviewed states, their exact accepted disaster jobs and directly adjacent frontier states.
During an active troop commitment, a bounded daily check may read the selected state and its local divisions.

If no candidate exists, the contact remains idle without a fabricated warning.
The government sees that there is no actionable vision.
The event does not call `call_natural_disaster`, start a war or create an enemy attack to fill the vacancy.

## Candidate families

### Accepted natural danger

A natural candidate requires an already accepted Event 013 sequence and a uniquely identified queued job affecting a currently eligible state in the home region.
A normal primary job must be 21 through 60 days away.
A queued follow-up can be 8 through 20 days away and uses the shorter emergency response schedule.
The queue owner must still be able to provide a valid read-only projection.

The vision records the source sequence, job, state, family, planned date, revision and one consequence hypothesis.
The hypothesis names one component.
At launch the supported components are civilian loss, civilian-building damage, and an already queued disease or famine follow-up that exposes its own prevention receipt.
A component with no supported observation and mitigation contract cannot be selected.

For a civilian-loss hypothesis, the qualifying modelled threat is a positive pre-Shaman loss request of at least the greater of 100 civilians or 0.01 percent of the state's living civilian population at issue.
For civilian-building damage, the owner must publish a normalized damaged-level equivalent and the qualifying request is at least one such level.
These thresholds are developer criteria for distinguishing a meaningful threat from a trivial numerical result.
They are not a promise to show an exact casualty prediction to the player.

An already queued follow-up qualifies when the exact disease or famine job reaches its owner's execution or prevention boundary.
A possible chain that has not been queued does not establish a future event.
Current exposure can support an explicitly conditional warning, but cannot be scored as proof that an incident was destined to occur.

### Vulnerable military frontier

A military candidate requires a current war, a host-controlled focus state in the region, and an adjacent state controlled by a current enemy.
It also requires a visible vulnerability: damaged infrastructure or civilian transport in that state, fewer than two eligible host divisions present, or a prior control loss and recapture within the preceding 30 days recorded by an actual state hook.

The warning is conditional: the frontier is exposed during the next 30 days.
It names the state and the vulnerability.
It does not announce an enemy AI order, a guaranteed encirclement or an exact battle outcome.
The selected vulnerability is recorded at issue and shown as the practical basis for preparation.

The observable threatened outcome is loss of the named state to a current enemy within the window, or a supported local combat or supply-consequence receipt if its engine owner can expose one.
The minimal complete implementation uses state-control loss, which has a verified event hook.
It does not claim to predict hidden operational intentions.

## Selecting the warning

When both families have candidates, use weight 70 for natural danger and 30 for military danger.
When only one family has candidates it receives the full selection.
Within the selected family, use the three highest-priority eligible candidates.
Rank by imminent due date or danger window, then source severity, then the home state as a tie-break.
Resolve remaining ranking ties by ascending state ID, then the owner's stable source identity.
Select among those candidates with weights 3, 2 and 1.
A smaller pool uses only its existing weights.

The candidate pool is built before the warning is issued and persisted with its generation.
Opening the category or inspecting its text cannot reselect a threat.
No other candidate can inherit the original payment or hidden interpretation.

A natural warning then receives a hidden source-support draw.
The probabilities of a hypothesis consistent with the accepted job and current exposure are 20 percent for a deceptive claimant, 55 percent for a capable local practitioner and 85 percent for an extraordinary practitioner.
The mixed encounter probability is 57 percent.
This is source support, not a 57 percent probability that the predicted consequence will happen.

At Chaos 600 or above, the extraordinary practitioner's source-support probability rises to 95 percent, making the mixture 60 percent.
Other profiles are unchanged.
Culture and government ideology do not affect these weights.
Each warning's support draw is frozen once.

A supported hypothesis chooses an eligible component identified by the owner projection.
An unsupported hypothesis chooses a plausible alternative component or an overstatement within the same real hazard and state.
It never invents an accepted job or hides a contradictory official forecast.
The unsupported component can still occur by coincidence.
Final adjudication uses the actual owner receipt, not the hidden source-support flag.

Military warnings do not use those probabilities as outcome accuracy.
Their future depends on the war and the government's behavior.
The hidden interpretation affects which already observed vulnerability the visitor emphasizes and the wording direction.
Actual loss, preservation and preparation remain separately recorded facts.

## The warning card

The ordinary decision category and report show the following information in connected prose and compact rows:

- The visitor's home and the named target state.
- The identified danger and the predicted time window.
- The practical information officials currently possess, including any matching official forecast.
- What limited and full preparation do, their exact quote, work duration and readiness expiry.
- Which outcome cannot be fully prevented.
- Whether the warning is conditional or supported by an accepted source event.

The last item concerns the public source event, not the hidden source-support draw.
The player never receives a hidden authenticity percentage.
The interface does not reveal a false vision by removing its preparation options or assigning it a different internal deadline style.

## Investigating evidence

The government can investigate once per vision for 40 political power.
A normal inquiry takes five days.
For a queued follow-up warning it takes three.
It can run before a response is chosen but cannot extend the disaster date or the frontier window.
Its confirmation explains how much preparation time will remain.

The inquiry reads only authorized current source facts, local reports and the official forecast.
It returns corroborating evidence, mixed evidence or contradicting evidence.
The categories are determined by actual observable agreement with the named hypothesis, not by an independent roll that claims a nonexistent fact.
Contradiction can identify a mismatch between the asserted component and the current job, a route already secured, or a frontier vulnerability already repaired.
Corroboration is evidence of plausibility and does not prove supernatural power.

No paid inquiry reveals the hidden identity or guarantees future accuracy.
It is useful because the player can change the scale of response using real information.
The AI consumes the same public result and never reads hidden source support when choosing whether to pay.
The 40 political power is consumed when a valid inquiry starts.
Cancellation, an unfavorable finding or later source invalidation does not refund it.
A same-transaction failure before the inquiry starts refunds only its measured debit once.
A stale inquiry confirmation charges nothing.

## Preparation choices

The government selects at most one response.
Upgrading a limited response to full is permitted once before the full-response deadline.
The upgrade charges only the remaining quoted material difference, replaces the timed burden, and preserves already elapsed work.
It does not stack two credits or restart the warning.
Downgrading after dispatch is not a refund route.

At the first paid response, save both the limited and full quotes, S, transport mode, price version, original issue and work-start dates, all dispatch and held balances, and the intended absolute readiness expiry.
An upgrade uses that immutable quote pair and the same source revision.
Its additional debit is the positive full-minus-limited difference for each resource.
It dispatches half of that additional amount, rounded up, and holds the rest.
Already consumed limited materials remain consumed.
No original payment is replayed or refunded.

The upgrade is atomic.
Revalidate affordability, remaining time, unconsumed owner credit, original authority and exact source before charging the delta.
Register a pending upgrade through the owner using the same logical response receipt.
Existing unconsumed limited protection remains usable until the full work and any military presence requirement complete.
Only then may the owner atomically replace it with full protection.
If provisional upgrade registration fails in the starting transaction, restore the limited receipt and refund only the new measured delta once.
If completion later fails after real work, keep any valid limited receipt and return only still-held upgrade material.
A consumed limited credit cannot be upgraded.
Credited work is actual completed work on this response, capped at the limited work requirement.
New completion is the upgrade date plus the full work requirement minus credited work days.
Use 14 total days normally or seven for an imminent follow-up.
Idle days after limited completion supply no credited work.
The full deadline and one-day-before-impact rule remain binding.
Military presence counts only observed consecutive days, never inferred earlier presence.

From upgrade to completion use the full production burden, replacing the limited burden.
Earlier elapsed time retains its actual limited burden.
Do not charge a retroactive industrial debit or count idle days as work.
The remaining work timer is synchronized to the newly computed absolute due date.
The readiness end date remains the original family limit.
Withdrawing after upgrade refunds only currently held material from the combined receipt.
A stale second upgrade returns the existing result without another debit or extension.


For natural warnings, S follows the land population scale in Part 2.
For the one-state military warning, S is 1.

| Response | Material quote | Production commitment | Work | Result |
| --- | --- | --- | --- | --- |
| Dismiss | None | None | Immediate | No Shaman protection, existing owner preparation remains available |
| Limited | 50 × S support equipment and 10 × S trucks | +5 percent × S consumer-goods factor | 7 days | One modest component credit or local readiness package |
| Full | 100 × S support equipment and 25 × S trucks | +10 percent × S consumer-goods factor | 14 days | One stronger component credit or local readiness package |

For a queued follow-up warning with 8 through 20 days remaining, limited work takes three days and full work takes seven.
Their prices and strength are unchanged.
The shorter work is an emergency mobilization against an already accepted imminent threat and is an explicit short-mission exception.
A completion must occur at least one full day before the source's execution boundary.
Late choices are unavailable, with the last useful date shown.

Apply Part 2's verified transport-mode substitution to both response quotes.
Each omitted truck becomes two additional support-equipment units.

These consumer-goods changes are factors, not percentage points of total factories.
Their actual industrial effect depends on the country's existing economy.
A country cannot evade the commitment by keeping the confirmation open until after its quote changes.

Material dispatch and cancellation follow the rite's half-dispatched, half-held rule.
The production burden lasts through the work period only.
Natural-danger readiness then remains until the end of the recorded danger window plus seven days, capped at 67 days after issue.
Military readiness instead uses the explicit limits in its section below.
Equipment is fully consumed at completed preparation.
Unused readiness expires without a full refund.
A response is therefore costly even when the danger never arrives.

## Natural-disaster protection

An accepted preparation adds a separate, one-shot, owner-owned credit for the named consequence component.
Limited protection requests a 10 percent reduction of the residual consequence request after ordinary owner mitigation.
Full protection requests 25 percent.
It does not modify Event 013's existing preparation score or repeat its coefficient.

Let B be the source owner's consequence request before all warning mitigation, and D its request after existing mitigation but before Shaman.
Let r be 0.10 or 0.25.
The additional credit is the smaller of r × D and the positive part of D minus 0.25 × B.
Final requested loss is D minus that credit.
This limits Shaman's combined contribution to a 75 percent reduction from B while preserving any stronger mitigation that the owner had already legitimately produced.
If D is already below 25 percent of B, Shaman adds zero and never increases it.

The owner may impose a stricter family cap.
A disaster with an unavoidable component keeps that component.
The owner uses one existing consequence roll and publishes its pre-credit request, post-credit request and measured actual applied effect.
The arithmetic difference is modelled reduction.
It is not an observed count of lives or factories saved in a second universe.

For an already queued disease or famine follow-up, a component credit applies only through that follow-up's own preparation and prevention contract.
Full protection can contribute one substantive preparation step or its documented equivalent, but cannot unconditionally erase the chain.
If the owner has no compatible contribution seam, that component is not issuable until the required adapter is implemented.

Every credit is keyed to encounter, vision, actor, state, sequence, job, component and revision.
It can be consumed once.
Later visions cannot cover the same physical job again.
State transfer, source cancellation and an owner revision that invalidates the hypothesis clear the unused credit without retargeting.
A military hostile state-control loss is first recorded as its threatened observed outcome, then authority cleanup runs.
Non-hostile transfers are void.
Loss of the home state still closes contact after preserving any already observed military outcome.
Existing disaster queues retain their original dates and Event 013 continues to own relief and aftermath.

## Military readiness

Limited preparation grants +1 local supply and +25 percent local land-fort construction speed until the earlier of 30 days after completion and day 45 after issue.
Full preparation requires two eligible host divisions with at least 50 percent strength to remain in the target state for seven consecutive days before the deadline.
It grants +2 local supply and the verified defensive-preparation effect from Part 2, at the effective strength, until day 45 after issue.
Its confirmation shows the resulting duration from the scheduled completion date.

The full response is a paid commitment to hold and prepare a specific frontier.
The player moves troops normally.
Leaving the state before the seven-day requirement completes resets consecutive presence.
A completion gate checks both the paid work and troop presence.
Work completion stops the production burden, but held equipment stays in refundable escrow until the combined success or partial resolver.
Do not consume it early merely because the work timer ended.
If time runs out with paid work complete but the troop condition incomplete, deliver the limited package and record a partial response.
Return the smaller of the actual held material and the positive full-minus-limited quote difference, once per stockpile.
Already dispatched material is spent.
This may leave a small wasted dispatch amount above the limited quote, which the partial-result report must identify.

A full commitment does not freeze divisions, deduct manpower, make units invulnerable or guarantee control.
The temporary state effects apply only to the original host while it controls the state.
If an initial military rite is already active there, use the stronger component with the later permitted expiry, capped by each receipt's original expiry.
Do not add both supply or entrenchment values together.

If the frontier disappears through peace or an enemy control change before the deadline, the result is unused readiness.
It is not a verified successful prediction.
Completed physical fortifications remain ordinary buildings.
Temporary readiness runs to its recorded expiry unless actor or state authority is lost.

## Adjudication

The source outcome and the government's response are separate axes.

| Result | Required evidence | Cooperation and record |
| --- | --- | --- |
| Supported threat, preparation useful | Exact natural owner component crossed its threshold or a queued follow-up reached its boundary, and the matching credit produced positive accepted modelled reduction | +10 cooperation, record source result and response separately |
| Threat occurred, response absent or late | The same source evidence, with no usable Shaman credit | No automatic cooperation reward, show the observed cost and ordinary relief options |
| Threat prevented by a proven owner action | Owner receipt identifies the exact canceled or reduced component and the action responsible | Record prevention and its actual owner, credit Shaman only for its own contribution |
| Warning disproved | The exact source executed within its window but the named threshold did not occur | A paid response loses 10 cooperation, a dismissed warning loses none |
| Military preparation completed and state held | Seven-day presence and paid work proven, target held through the 30-day warning window | Record useful readiness and preserved state, do not assert a prevented enemy offensive |
| Void or unobservable | Source canceled for unrelated reasons, non-hostile military target transfer, natural target transfer, host lost before an observable outcome, incompatible revision, unavailable owner receipt or warning could no longer be observed | No accuracy score or cooperation change, apply the payment and cleanup policy |

Military warnings use conditional wording.
A no-loss result is classified as readiness unused or state held under preparation.
The implementation must not count every preserved frontier as a proven correct prophecy.
This distinction is mandatory in achievements and reports.

A fully prepared false natural alarm can cause a brief local panic only when cooperation is strained immediately after applying the false-alarm cooperation loss.
Snapshot that order once.
Thus a paid false alarm can move cooperation from 40 to 30 and make the panic check eligible.
The single reaction chance is 20 percent.
Its consequence is 14 days at -10 percent local civilian production in the target state.
It does not cause national instability or deaths.
A limited response does not carry this extra panic roll.
One reconciliation offer keyed to the original panic receipt remains available for 30 days, including after its temporary modifier expires.
At the Part 2 aftercare political-power quote and 50 × S support equipment, it restores 10 cooperation after 14 days.
It removes only any genuinely remaining event-owned panic.
Since ordinary panic already lasts 14 days, this response usually repairs cooperation rather than shortening that modifier.
It earns no negative Chaos for a burden that expired before completion.
It does not erase the false result.

## Hard cases

If a genuine forecast prompts preparation and the owner proves prevention, the result is averted danger.
It is never labeled false simply because the disaster did less damage.
If another system independently cancels the source without a matched prevention receipt, the result is void or unused readiness.
Shaman receives no credit for work it did not do.

If an unrelated disaster strikes the same state, it cannot consume the saved protection or satisfy the vision merely because its date is close.
The exact job identity governs natural predictions.
A vision about a specific queued follow-up does not match the parent disaster or a second outbreak.

If an attack was never ordered, the system cannot know the enemy's unrealized intention.
It reports the observed frontier and preparation facts.
If a large disaster contains unavoidable harm, preparation can reduce only the owner's supported components.
The report explains the remaining harm without inventing an impossible total prevention path.

Save and load preserve the issued hypothesis, target, quote, response, due date and consumed credit.
Turning the evolution setting off stops unissued opportunities and withdraws an issued but unpaid response offer without changing its source threat.
A paid inquiry can finish, but it cannot open a new preparation after disablement.
An already paid, valid preparation resolves under its frozen contract and then closes.
Further upgrades are new commitments and are unavailable while disabled.
It cannot vanish silently or charge again when the setting returns.

## Boundary ordering

At a due boundary, first preserve any source outcome already recorded by its physical owner.
Next validate the current actor, state, source identity, semantic revision and response readiness.
Then apply or retire the credit, adjudicate once, settle held payment and finally clean up presentation.
A military hostile control-loss hook records the threatened outcome before it retires the old controller's binding.
A report delivered later cannot rewrite that ordering.

A revision that changes the physical job, consequence family, date beyond the frozen window or allowed component invalidates an unanswered offer or unused credit.
A formatting-only or equivalent owner revision may preserve it only when the owner returns an explicit same-job equivalence proof.
Never silently adopt a replacement job.
One-day-before-impact completion uses the owner's actual execution boundary.
Completion on the impact date is late, regardless of popup or callback ordering.

Inquiry and reconciliation political power is consumed on valid commitment.
Reconciliation equipment is likewise consumed upfront, outside the half-held preparation rule.
Later cancellation or authority loss returns neither, while a same-transaction start failure reverses only its own measured debit.
A stale confirmation always charges nothing.

If the source owner advances a job's execution date, recheck the one-day-before-impact cutoff immediately.
An unready response cannot receive retrospective protection.
Settle its held material under cancellation, record late or unused readiness, and retain elapsed costs.
A completed ready credit may remain only with an explicit same-job proof and valid component.

The final observation cutoff is the recorded danger-window end plus seven days.
A missing receipt at that cutoff closes as unobservable.
A later owner receipt may append a factual history correction, but cannot reopen payment, grant a second response or retroactively create an achievement or Chaos award.
No late callback may turn an already settled void request into a fresh entitlement.
