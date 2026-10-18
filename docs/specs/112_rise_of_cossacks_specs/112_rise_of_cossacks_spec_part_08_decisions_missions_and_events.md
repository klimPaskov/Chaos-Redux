# Part 08. Decisions, missions, commitments, and event content

## How the player uses the system

The host's decision interface answers four practical questions.
What threatens the country now.
What agreement or project is currently being pursued.
What resources and conditions that work requires.
What the host can do next.

The interface uses ordinary decision categories.
The two public values are Host Cohesion and Settlement Legitimacy.
A selected great project adds its exact state puzzle and a compact requirements summary.
There is no separate management window, new custom currency, or page of permanently visible inactive projects.

The primary category shows at most five ordinary primary actions, plus at most one eligible emergency or status row.
The program index remains reachable and does not expand every inactive route into the main view.
At most three event-owned missions are active at once.
The project index, host contacts, and completed agreements remain accessible through filtered categories.
Filtering reduces clutter without deleting content or hiding an active cost.
Every active mission remains reachable from the current primary category.

## Common action contract

Each implemented action must define its owner, target, visibility, availability, actual price, execution recheck, effects, receipt, cooldown, cancellation, and AI route.
A visible historical idea can be unavailable for a concrete reason.
An unavailable target is not silently replaced after the player pays.

A country, state, unit, character, partner, or cohort target has a stable identity and generation where required.
A display row cannot store only the current array index.
The final execution checks the same target that was quoted.
A changed legal owner or controller is handled according to the action's explicit policy.

The cost line uses at most three inline resource values.
A gameplay-changing action can use at most four distinct spendable resource types in total.
Non-consumed conditions such as Cohesion 60, a controlled state, a willing partner, or an existing factory are clearly requirements.
They are not prices.
No individual action exceeds 60 Command Power.

Base prices in this specification are proposed tuning before accepted shared modifiers.
The implementation computes one exact quote, checks affordability using that quote, and deducts that quote once.
It must prove below, exactly at, and above every material affordability boundary.
A rounded display cannot conceal a different actual deduction.

Administrative Political Power and time already spent are normally sunk costs.
Actual unspent escrow can be refunded only from its recorded balance.
Undelivered equipment can be returned only if it was actually reserved or debited and has not been lost or delivered elsewhere.
The action must never promise a refund that the implementing helper cannot measure.

## Common mission contract

A mission is an objective the country is actively pursuing.
It completes automatically when its actual success conditions are satisfied.
The player does not buy the same outcome again through a separate completion button.

Ordinary mission durations are at least 90 days.
Medium institution and training work normally allows 120 to 180 days.
Major constitutional or settlement work normally allows 180 to 365 days.
A shorter emergency timer is allowed only for a clearly identified military emergency.
The initial home-defense effect can last 60 days without making the entire first survival mission a 60-day ordinary project.

Every mission has a defined activation moment and a native timer.
An extension uses the documented signed mission-timeout adjustment rather than removing and reactivating the mission.
A country change or reload never resets elapsed time.
The completion check has precedence over failure when a valid objective is achieved exactly at its stated deadline.
That boundary needs a real engine test.

The initial survival objective is to remain a viable host for 90 days.
Its mission permits a 120-day window so the engine can observe the successful anniversary without a same-tick timeout ambiguity.
Loss of the country or an unreconciled opening transaction invalidates it.
A temporary loss of an incidental province does not count as extinction while the capital and country remain viable.

Voluntary expansion uses the readiness rules in part 03.
Defense, negotiation, relief, and recovery remain available when those readiness conditions fail.
A player whose army is exhausted must still have actions that can improve the situation.

## Action catalog

The codes below are specification references, not allocated runtime decision IDs.
Where a named regional or great-project action already has its exact price and mission in parts 04 through 06, that owning section remains the numerical authority.
The central catalog supplies routing and cleanup, not a second conflicting price.

| Code | Working action family | Owner and target | Base cost and duration | Outcome and repeat rule |
| --- | --- | --- | --- | --- |
| A01 | Choose the provisional response and fund the first civil settlement | Principal host, displaced authority and real founding-state representatives | The response itself is free after successful spawn, while its Provisional Civil Settlement sub-objective costs 35 Political Power through one shared quote | One immediate compact reward and the finite day 30, 60 and 90 civil checkpoints in part 03, without a charter, conquest or offensive-readiness gate |
| A02 | Convene and ratify a charter | Principal host and its actual representatives | Charter-specific price and 120 to 180-day mission from part 04 | One current charter, later changes use a real constitutional reform |
| A03 | Establish the first workshops | Host and its founding state | 60 Political Power, 90-day mission, founding zero-capacity and valid-slot rules | One ordinary military factory or the admitted non-duplicating alternative, one receipt |
| A04 | Register cadres and service | Host and selected actual formations | 40 Political Power and 20 Army Experience, 120 days | M01 capability, once |
| A05 | Develop a military school | Host, selected formation, and any required instructors | M02 through M06 exact prices and 150 to 180-day objectives | Training and template capability, no free duplicate army |
| A06 | Open a specific host contact | Host and one discovered genuine community or state | 35 Political Power, 90-day mission | One contact and response, 180-day retry after refusal unless facts materially change |
| A07 | Adopt a first additional tradition | Host and an accepted provider | 50 Political Power and 20 Army Experience, 150 days | One adopted tradition after actual training or institutional exchange |
| A08 | Adopt a second additional tradition | Mature host and a different accepted provider | 75 Political Power and 30 Army Experience, 180 days | Second and final additional tradition slot |
| A09 | Retrain the current military emphasis | Host and the affected formation | 20 Army Experience, 120 days | Replaces the selected emphasis, 180-day elective cooldown |
| A10 | Negotiate recognition or service terms | Host and legal owner, controller, or eligible sponsor | 60 Political Power, 120-day negotiation | An actual accepted diplomatic settlement or a recorded refusal |
| A11 | Arrange a measured arms contract | Host and an actual supplier | Exact supplier quote, 120 to 180-day delivery objective | Actual equipment receipt, no gift after failed delivery |
| A12 | Invite an exile or historical candidate | Host and one verified available person or cohort | 60 Political Power, 120 days unless the owning route states otherwise | Accepted return or refusal, no duplicate character |
| A13 | Ratify one host or regional charter | Host and one genuine partner | 50 Political Power, 150-day mission | Specific treaty or membership with preserved partner agency |
| A14 | Settle one acquired state | Host and an owned and controlled state | 60 Political Power and 100 support equipment, 180 days | A completed local settlement and eligible integration proof, once per state and generation |
| A15 | Prepare a refuge or return destination | Receiving country, actual destination, and identified cohort | 50 Political Power and 150 support equipment, 180-day objective | Capacity and guarantee receipt, no population grant |
| A16 | Execute an accepted civilian movement | Exact source, destination, route, and cohort | The accepted measured transport and protection quote, bounded by four resources | One actual transfer through the sole state-ledger owner |
| A17 | Respond to The Hosts Answer | Principal host and a single valid opportunity | Outcome-specific cost and deadline from part 07 | Rising, defection, volunteers, or aligned host with a unique receipt |
| A18 | Prepare a native raid | Native actor and exact eligible military target | Native preparation costs from part 03 | One native RAID_INSTANCE, no parallel scripted second raid |
| A19 | Repair a material charter breach | Responsible country and affected signatory | 60 Political Power plus the actual undelivered obligation if payable | One negotiated repair and probation period, no repeatable free meter purchase |
| A20 | Review an emergency mandate | Host and the body that granted authority | 60 Political Power, 120-day mission | Ratification, demobilization, or constitutional change with the relevant response |
| A21 | Settle veterans and reconstruction | Host and selected accepted state or service agreement | 60 Political Power plus the actual construction or support objective, 180 days | Postwar economic and political settlement, finite per qualifying war settlement |
| A22 | Choose a principal great project | Host and one discovered project | Selection free, preparation uses part 05 | One principal project, no reward on selection |
| A23 | Change an elective unfinished great project | Host and its current commitment | 50 Political Power, 180-day elective cooldown | Ends future preparation benefits while preserving actual assets and obligations |
| A24 | Complete a national or federal settlement | Host and exact required geography or members | Part 05's final act and objective | One formation receipt, no repeated country initialization |
| A25 | Consolidate a durable regional settlement | Host and its home or refuge agreement | 75 Political Power, 180-day mission | Complete regional endpoint with normal continuing play |
| A26 | Suspend or abandon an invalidated project | Host and its own unfinished project | No new charge for external invalidation | Cancels owned work, refunds only actual unspent escrow |
| A27 | Request one civil-program extension | Host and one eligible active ordinary civil or regional program | 20 Political Power, up to 60 days once before failure | Native timer adjustment with the same one-extension receipt used by an alternative free route-loss suspension |
| A28 | Negotiate orderly withdrawal from a patron | Host and its actual sponsor | 50 Political Power, 120-day negotiation | Agreed exit, revised terms, or explicit breach, with no automatic peace |
| A29 | Hold the charter's succession procedure | Host and its authorized institution | Charter-specific cost, ordinary 90-day window unless an immediate interim office is required | A functioning interim office and a grounded accepted successor |
| A30 | Review an existing agreement | Host and its actual treaty or cohort receipt | Free information action | Shows terms, contributions, breaches, deadlines, and closure status without gameplay reward |

A06 cannot reveal every distant community at the opening.
Contacts follow the geography, migration, diplomacy, and evolution rules.
A14 cannot core a state simply because the player can afford 60 Political Power.
Its full integration requirements appear below.
A27 permits one bounded delay of an eligible ordinary civil or regional-program mission.
An external route-loss suspension of up to 90 days is the alternative defined in part 04 and consumes the same one-extension guard.
It cannot follow or precede the paid extension on that same mission.
Native raid preparation, counterpart response windows and distinct crisis-specific evacuation or physical-recovery windows keep their own owners.

## Founding civilian settlement

The A01 Provisional Civil Settlement is the opening administrative bridge defined in part 03.
It uses the existing founding mission and the same lineage receipt, with no additional mission slot.
The immediate accepted compact grants Cohesion plus 5 and Legitimacy plus 2 once.
Its funded checkpoints require actual provisional representation, honored home protection and civilian livelihood, then continuing guarantees.
Their finite budgets are up to Cohesion plus 5 and Legitimacy plus 8, then plus 5 and plus 8, then Legitimacy plus 7, limited by the positive gap to Cohesion 60 and Legitimacy 50.
The ordinary first-council reward is included inside the first checkpoint.
These checks do not grant people, equipment, Political Power, buildings or another core.
A controlled viable home and living force suffice for defensive administration, without requiring a second formation or offensive equipment readiness.
The minimum clamped starting meters 35 and 25 can reach 50 and 50 after the accepted compact and all three honored checkpoints, without passive recovery.
That supplies the civilian-charter threshold and first-settlement prerequisite before a 30-day ratification hold.
Interrupted work retains completed receipts and can resume its unpaid or unfinished work after the initial mission closes.
A higher modified quote can delay funding, and the later assembly timer starts only when convened.
The founding recovery fee is an explicit exception to the AI's ordinary discretionary 20 Political Power reserve.

## Detailed integration mission

A14 applies to later acquired territory.
It is distinct from A01 and cannot charge again for the founding state's already completed provisional settlement or block the initial charter.
A local settlement is a political agreement backed by actual control and administration.
It is not a universal conversion of military occupation into a core.

The country must own and control the target state and have a viable administrative route.
There must be a relevant host connection, accepted civic inclusion, or a route-specific legal settlement.
The player selects one service or civic model allowed by the country's charter.
The target cannot be in an active transfer or custody transaction.

The 180-day mission needs an accepted local institution, adequate protection, and completion of the actual reconstruction or service promise.
For a relevant occupied or non-core state, resistance and compliance must meet the implemented thresholds.
The proposed target is resistance below 25 percent and compliance at least 40 percent where native values are applicable.
A normal core where resistance is not applicable does not fail because its value is absent.
A bad scope is not treated as a benign missing value.

The country needs Settlement Legitimacy at least 60 at completion.
A coercive route can maintain control and establish a provisional administration with lower legitimacy.
That grants a bounded local administration outcome and leaves core integration pending.
It cannot bypass the gate through a different button.

The mission grants an integration receipt only after every condition passes.
A core is added only if the state's explicit geographic and civic policy authorizes one.
Some agreements instead grant an autonomous relationship, transit, representation, or an accepted service district.
The selected state puzzle and tooltip must show the actual result.

A target lost before completion cancels the mission and removes its temporary owned setup.
Political Power spent on administration is not returned.
Undelivered support equipment is returned only where escrow actually held it.
The state keeps completed physical buildings under its current owner.
Reacquisition can reopen a new settlement process without repeating any old grant.

## Diplomatic response contracts

### The displaced authority

The first response occurs after the host physically exists.
Its purpose is to decide the relationship with the new country.
The event does not ask the old authority for permission to spawn the already authorized rising.

A limited recognition offer specifies the border and the host's status.
A service offer specifies recruitment, command, deliveries, appointment rights, and withdrawal.
A punitive response uses a valid native war or war-goal route and preserves existing war relationships.
If the engine cannot safely create the occupied-state version, that initial variant stays unavailable.

The old authority's AI values recognition more when a costly war or near-capitulation makes another front dangerous.
It values a service arrangement when actual mobile forces are useful and deliveries are affordable.
It values a punitive route when the state can be recovered at acceptable cost and its current commitments allow it.
No option is always selected because of one ideology label.

### An invited host

The invitation states whether it asks for contact, volunteers, common defense, federation, subject status, or full merger.
These are distinct decisions.
Accepting contact never implies consent to the strongest relationship.

A prospective member can demand local command, representation, land guarantees, nonintervention, arms, or a defined exit rule.
It can refuse.
A counteroffer changes the actual proposed contract and quote.
The inviter must accept that new contract before any physical contribution moves.

A partner's consent is valid only while the agreed political authority still exists or a successor has explicitly adopted the agreement.
Annexation, capitulation, a hostile controller, or a conflicting treaty triggers review.
The old affirmative flag cannot bind a government that no longer exists.

### A sponsor

The sponsor must have actual equipment, transport, political capacity, and a reason to support the host.
The host can accept a limited contract, negotiate a narrower obligation, or decline.
A declined sponsor does not become an enemy automatically.

An offensive service obligation identifies the actual war, theater, unit commitment, and deadline.
The host can fulfill it, obtain a waiver, or breach it.
The sponsor cannot demand an unlimited portion of the host's army through a generic opinion event.
The AI refuses an obligation that makes its minimum home defense impossible unless a separately explicit desperate survival decision justifies it.

## Commitments and visible memory

The system records actual agreements as discrete commitments.
A commitment includes its parties, territorial scope, accepted terms, due dates if any, completed contributions, breach conditions, and closure.
This is memory of a political promise, not a third numerical resource.

At most six time-sensitive commitments require active principal-host attention at once.
Long-term signed charters remain in the bounded partner registry.
A charter can contain several explicit clauses without turning each clause into a permanent player meter.
Only the currently due actionable clauses surface as missions or response events.

The event log records when a promise was made and what actually happened.
A player can inspect why a partner suspended transit or why a mandate is overdue.
The response must point to the earlier commitment.
It cannot invent an unrelated grievance to force a random penalty.

## Event content inventory

This is a finite writing plan.
Titles and subjects are working briefs.
The implementation writer supplies final prose only after the mechanics and exact recipients are stable.
No paragraph in this section is pasteable localisation.

| Family | Required distinct situations | Mechanical purpose and writing direction |
| --- | --- | --- |
| Opening, 4 reports | Founding host, displaced authority, optional human country switch, nearby observer | Establish immediate facts, identity, scale, and choices without explaining hidden future routes |
| Survival, 4 reports | First organized defense, material shortage, first workable arsenal, survival anniversary | Show the people and work behind a playable country and connect each report to actual state |
| Charter, 6 reports | Council membership, service burden, emergency command, sponsor terms, ratification, first breach | Make the distribution of rights and authority concrete and show the relevant tradeoff |
| Regional institutions, 12 reports | One distinct founding or contact treatment for each H01 through H12 tradition family | Use accurate geography, institutions, and ordinary civilian life without making every family a sovereign state |
| Training and industry, 6 reports | Cadres, plastun school, support arms, common standards, motorization, mature repair or education | Tie modernization to real resources and actual formations |
| Return and exile, 5 reports | First contact, return mandate dispute, receiving settlement, interrupted passage, successful sanctuary or evacuation | Preserve civilian agency and the actual fate of the cohort |
| Wider resurgence, 5 reports | First signal, aligned rising, unit defection, volunteers, newly organized host | Keep all response origins distinct and identify real support and obligations |
| Great-project preparation, 8 reports | One for each GP01 through GP08 | Explain the selected political question and next practical requirement |
| National settlement, 5 reports | Union, Russia, Horde, Ukraine, regional or network settlement | Announce an achieved institutional outcome with the actual status and contested claims |
| Postwar and succession, 8 reports | Mandate review, pensions and farms, city representation, service demands, partner exit, leadership succession, imperial legitimacy, final reconstruction | Reuse earlier promises and provide a recovery or negotiated ending |
| Defeat and aftermath, 4 reports | Capital loss, annexation terms, exile integration, bounded restoration | Preserve continuity and close processors without resetting the initial event |

The total writing plan is 67 distinct report situations.
Several use one illustration subject from the finite eighteen-report-art inventory when the scene and tone genuinely fit.
Image reuse does not permit mechanically different outcomes to share inaccurate prose.
Reports for the same family have recipient-specific variants only where the reader's knowledge or choices differ.

The six newspaper scene families cover initial regional upheaval, the wider answering hosts, a durable confederation, Russian succession, a Golden Horde claim, and a major settlement or refuge outcome.
A newspaper event is conditional on actual scale and observer relevance.
It must not announce world history because a single volunteer detachment arrived.

The three super-events are reserved for the durable Union of Hosts, Cossack Russia, and Golden Horde milestones.
Their exact qualification and production briefs are in the super-event prompt.
The initial Minor Fire-Once rising uses an ordinary report and an appropriately scoped news response.

## Flavor with consequence

Local flavor should name a real kind of work, institution, or dispute.
Useful subjects include repairing a crossing, allocating seasonal service, admitting a town delegation, maintaining a communal fishery, returning a regimental banner, training foot scouts, protecting an evacuation route, or deciding who can issue orders after the war.

A flavor event can be purely reflective when it marks a real completed milestone.
If it offers gameplay choices, each choice needs a truthful consequence.
A decorative option must not secretly spend resources or alter a treaty.
Repeated narrative incidents cannot serve as an unlimited Political Power, Cohesion, or Legitimacy farm.

Historical responsibility is handled through the actual institution and its decisions.
The writing can acknowledge exclusion, conquest, repression, and collaboration without assigning one moral or political identity to every Cossack.
A fictional twentieth century government must be described as a proposed revival with its own choices.

## AI and interface equivalence

The AI and player share all eligibility, cost, target, completion, and cleanup helpers.
AI preferences choose among legal actions.
They do not substitute for availability.
The AI can use a valid recovery path without meeting expansion readiness.

A focus that unlocks a program must state that it unlocks the program.
It cannot claim to have already trained the army, delivered the arms, ratified a treaty, or integrated the state.
The decision and mission text then explains the concrete remaining work.
This distinction is essential for the large route structure.

Every price, progress condition, and action result uses the same current source values as the engine effect.
Missing localization, missing target, empty lists, long names, target changes, and completed actions each have explicit visual states.
The selected formable state remains visible as unmet when ownership or consent changes.

## Acceptance criteria

The decision audit must trace all thirty action families and the route-specific actions they route to.
The mission audit must prove automatic completion, exact deadline behavior, signed extensions, refund limits, cancellation, save and reload, target rebinding, and no repeated rewards.
The event audit must cover all 67 report situations with a recipient and trigger matrix.

No price is accepted until display, affordability, debit, and effect agree.
No partner response is accepted until refusal and invalidation work.
No mission is accepted if the AI can only complete it by bypassing its human contract.
The final writing audit checks mechanics, dynamic names, source attribution where needed, and the absence of invented final quotations.


## Exact formation answer dispatch

The Hosts Answer uses the five-way pool in part 07, including an exact formation-defection outcome at weight 10 when its verified native transfer and actual unique unit are eligible.
This outcome can be valid even when the source free-manpower pool is empty, because the people and equipment are already inside the selected formation.
The unit, its experience, strength, equipment and accepted command ownership must reconcile before WR40 reports success.
A personnel-only contribution is a different outcome and cannot satisfy the exact-unit transfer receipt.

## Postwar owner and recovery precedence

A20 and A21 follow the more specific original P or GP promise contract where one exists.
One review cannot charge two prices or impose two losses for the same work because a regional program and a great project both refer to it.
The default eight-project table in part 05 supplies exact objectives and uses A20 at 60 Political Power and 120 days or A21 at 60 Political Power and 180 days.
Without a more specific repair contract, A19 recovery costs 60 Political Power, allows 150 days and requires 30 consecutive days of the repaired agreement honored.
It restores only the same receipt's actual unrecovered loss and newly accepted cooperation.

## Completion and active-project capacity

Successful great-project completion releases its active preparation place while retaining the completed receipt and all live agreements.
A compatible next project pays its own stages without abandoning the completed network.
A23's 50 Political Power and 180-day elective-change rule applies only to funded unfinished preparation.
An incompatible national identity still needs its actual constitutional transition, and no project switch refreshes consumed rewards.
