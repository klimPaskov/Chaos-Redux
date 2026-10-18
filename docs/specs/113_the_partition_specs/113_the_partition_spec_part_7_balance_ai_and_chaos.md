# 113 The Partition: Balance, AI, and Chaos

The event should create a difficult choice whose answer changes with the campaign.
Conceding a frontier can be rational when the target is isolated and overmatched.
Defense can be rational when its geography and protection make the coalition's war expensive.
Claimant disagreement can create a third route when neither immediate surrender nor immediate war is attractive.

All balance numbers in these specifications are proposed starting anchors.
They are not measured engine probabilities or a claim of tested campaign balance.
The named scenario matrix defines what later analysis and play evidence must establish.

## Cost authority and units

Every paid action has one current quote used by its display, affordability condition, confirmation, debit, and any refundable commitment.
Affordability includes equality with the quoted amount.
A price shown before a material game change is refreshed before payment.
A stale actor, proposal, state list, or legal action rejects the click before any debit.

Political power and experience use their ordinary resource units.
Stability and war-support costs use percentage points, with correct native conversion.
Equipment, trains, fuel, and command power use the exact supported native resource or equipment type.
A train archetype and a particular train model are not silently interchangeable.
The implementation must inspect the current universal-cost owner and an exact adapter for each required type.

The complete resource vector for one action can contain at most four distinct spendable types.
This includes new reservations or treaty promises accepted by that same action.
A fifth cost cannot be hidden in a tooltip, delayed award, confirmation, or second mandatory step.
Ratification may refer to a previously completed aid receipt without paying or crediting it again.
Any newly funded promise must be included in that actor's displayed approval and the four-type budget.

The ordinary presentation shows at most three inline resource values with verified texticons.
An action with a fourth type uses the detail panel while retaining the complete count and total on final review.
Non-consumed prerequisites, territorial sacrifices, and likely war consequences are displayed separately from the spendable cost string.
Raw resource names are not substitutes for missing runtime texticons.

### Proposed scaling

Let F be the target's physically owned civilian and military factories at the current quote.
The material scale is the ceiling of F divided by 15, clamped to a minimum of 1 and a maximum of 5.
This scale applies to arms deliveries, transport deliveries, and reconstruction material costs.
It does not multiply a target's stability sacrifice or the cost of every diplomatic click.

Political and preparation effort can use an intensity factor of 1 at baseline, 1.25 in Partition Fever, and 1.50 in Grand Partitions.
This factor applies to C2, C3, C6, T1, T2, and P4.
Native guarantee prices remain native prices.
Military preparation actions T3, T4, C5, and P5 keep their listed CP or XP anchors and rely on actual readiness and opportunity cost rather than escalating every cost with Chaos.

The universal-cost framework then applies current supported modifiers to the resulting base quote.
Positive PP, CP, and XP are rounded up to a multiple of 5, with CP capped at 60 for an event-owned action.
Equipment is rounded to a multiple of 5, fuel to a multiple of 500, and train quantities to a multiple of 5.
Positive costs retain at least one supported quantum.
Zero remains zero.
The stability sacrifice remains 5 percentage points unless the actual shared owner has an applicable verified adjustment.

The material delivery received by the target equals the donor's actual debit after the quote is finalized.
This preserves conservation even when a shared price modifier changes the payable quantity.
The UI explains the final actual delivery amount before approval.
There is no fixed advertised delivery paired with a lower hidden debit.

### Payment and refund classes

| Class | Actions | When paid | Refund rule | Contribution rule |
| --- | --- | --- | --- | --- |
| Diplomatic effort | C2, C3, T1, T2, P4, reconciliation | When a valid material offer or request is submitted | Consumed even if honestly refused or unanswered | Submission alone never proves a successful settlement |
| Consumed preparation | C5, C6, T3, T4, P5, reconstruction activation | After complete current validity and affordability checks | Consumed after the preparation actually starts | Records preparation, not troops, delivery, war entry, or victory |
| Material transfer | P2 and P3 | Through a verified payer-to-recipient transfer | Only actually paid, undelivered refundable components, exactly once | Actual delivered quantity and identity required |
| Native diplomatic action | P1 and any native war-entry charge | Through the actual native action | Native rule applies, with no invented duplicate event refund | Native relationship or entry must exist |
| Territorial obligation | T5 and claimant ratification | No resource tax for signing, actual states transfer on schedule | Territory is outside resource-refund authority | Each actual state award is recorded once |

A pledge's 25 CP is the complete Event 113 preparation cost for P5.
Any charge imposed by a later native diplomatic war-entry action is displayed and accepted in that separate native action.
Actual fighting consumes the normal campaign's manpower, equipment, and supply through war, rather than through a hidden extra event-button price.

## Pacing and mission capacity

Event 113 and its attached Event 101 objective expose at most three active native missions per country across every wave.
The intended maximum is one target-owned mission, one incoming protection-request mission, and one Partition Task.
The target-owned slot changes between ultimatum, handover, and reconstruction phases.
It does not contain all three simultaneously.

Each country can receive only one unanswered protection request at a time.
New requests to a busy recipient are unavailable before the sender pays.
Claimant and protector commitments in other crises appear as dated status rows in the dossier, not duplicate native missions.
War observation is a crisis status, with native war information and relevant Task progress where applicable.

The handover has one authoritative crisis outcome and one target-owned native mission while the target exists.
Recipients see mirrored status rows, which cannot independently pay rewards or resolve the handover.
A surviving observer maintains the same outcome record after target extinction.
The 10-day due dates are execution milestones for the accepted schedule, not another opportunity to infer consent.

The AI revisits registered active opportunities on a proposed five-day cadence and at material changes.
It services already accepted obligations by earliest due date, then its own target response, then new discretionary offers.
Ties use the oldest unanswered opportunity, followed by the stable crisis identifier.
Every registered opportunity is revalidated within the same five-day service cycle even when a different action is chosen.
An unaffordable action remains visible as blocked but cannot monopolize later evaluations.
After one purchase, resources and the remaining pool are refreshed before another opportunity can spend.
Human actions revalidate immediately when selected.
Target selection runs only for a new firing.
Maintenance traverses registered crises, participants, and scheduled awards, with bounded work and retained unprocessed entries.
It does not scan the world every day or week for new victims.

## Weighted selection and AI surfaces

Each surface has its own selection meaning.
Random target selection, a decision score competition, an event option, and an MTTH clock must not be assigned one shared probability formula.
The implementation begins with `hoi4.probability_inspect`, then evaluates the named scenarios, sweeps thresholds, and compares changes with the actual adapter.
No exact percentage is promised for a pool that depends on all current countries or uninspected external factors.

Human-facing notification popups are informational and safe by default.
AI political choices use one authoritative action path for the current actor, crisis, and phase, with the same legality, quote, and effect rules as the human controls.
GUI AI and native decision AI must not both purchase the same action independently.
The preferred implementation uses the event's bounded native decision opportunities as that AI path and lets the dossier call the same owned action contracts.

### Target and claimant selection factors

The proposed target weight is 100 × I × D × 0.75 raised to L after all hard gates pass.
I is the strongest actual interest among feasible claimant-state pairings, with 2 for a core, 1.50 for a claim, and 1.25 for strategic interest.
D is 0.25 when at least one capable defensive guarantee or faction commitment is operational, and 1 otherwise.
L is the target's already active shared local-crisis count before this crisis is reserved.
Use each component once, then round the final positive weight to the nearest multiple of 5 with halves rounded upward and a minimum of 5.
A hard-invalid target keeps weight zero.
Multiple alternative coalitions do not give the same target multiple lottery tickets.

Draw the requested opening quota uniformly from the current form's count range.
Select distinct targets by weighted sampling without replacement from the currently feasible target pool.
Each tentative selection must leave a compatible completion to the requested count when that count is feasible under the shared actor and target constraints.
If it is infeasible, first establish the largest compatible count below it and use that count for the same selection process.
The implementation must retain the finite opening candidate set and resolve conflicting claimant assignments before announcement.
It may distribute bounded search work across an internal preparation queue, but must not publish an unverified package or silently treat an unfinished search as a shortage of eligible countries.

Claimant willingness considers the actual expected share, its military and economic ability, nearby defenders, the burden of other commitments, faction relationships, and disagreement with other beneficiaries.
A hard-invalid state, actor, border, or diplomacy route always has zero weight.
An eligible but risky opportunity can remain possible without becoming dominant.

Those factors are reviewable design anchors.
The full candidate population, feasible-completion restrictions, exact source implementation, and external hooks must be supplied to the probability adapter before an implementation can claim a selection probability.

### Target action priorities

| Action | Proposed neutral score | Strong reasons to increase it | Strong reasons to reduce it |
| --- | ---: | --- | --- |
| T1 Counterproposal | 100 | A feasible less damaging map, divided claimants, time to negotiate | No feasible alternative, repeated unchanged rejection, handover already accepted |
| T2 Seek protection | 75 | Credible existing relationship, reachable capable protector, sufficient time | Every candidate incapable or already overcommitted, impossible legal promise |
| T3 Emergency defense | 50 | Real army can exploit terrain and entrenchment, refusal likely | Equipment needed to keep fielded divisions supplied, no relevant defense opportunity |
| T4 Supply preparation | 25 | Real logistics constraint on the threatened front | Adequate supply already, unaffordable transport or fuel |
| T5 Limited acceptance | 75 | Severe credible overmatch, no effective protection, acceptable remnant, relatively limited loss | Strong defense, critical access loss, coalition fracture, better valid counterproposal |
| T6 Refuse | 50 | Strong defense or protection, implausible enforcement, unacceptable economic loss | Isolated overmatch and a survivable modest settlement |

Voluntary complete partition is outside this ordinary acceptance score and has zero AI weight by default.
This is a firm behavior rule until an exceptional case is separately accepted.
The event can still end in complete partition through war.

### Claimant action priorities

| Choice | Proposed neutral score | Expected behavior |
| --- | ---: | --- |
| Ratify a feasible share | 100 | Favor a meaningful connected gain with affordable risk and compatible partners |
| Revise a share | 50 | Increase for a real unsatisfied claim or changed military balance, reduce after costly failed bargaining |
| Invite a neighbor | 25 | Increase when its participation adds credible strength and a feasible share, reduce when it mainly creates overlap |
| Withdraw or reduce | 50 | Increase sharply for credible protection, poor readiness, collapsing cohesion, or an unaffordable larger war |
| Authorize enforcement | 50 | Increase for substantial interest, readiness, at least one willing partner, and weak defense, reduce for disputed terms and other fronts |
| Contest a rival | 25 | Increase for a major denied interest after failed talks and a legal affordable conflict, reduce when withdrawal achieves the same aim cheaply |

Claimants never authorize an invalid war because their score is high.
The military comparison is an assessment of actual available strength, access, supply, and current fronts.
A raw division count alone is insufficient.
The installed engine's supported strength signals and strategy routes must be inspected before the implementation chooses its exact calculation.

### Protector priorities

Protectors favor an existing relationship, a strategically important independent target, credible ability to help, and a cost proportionate to the likely result.
They prefer mediation or aid when direct intervention would produce a much larger war with poor prospects.
A rival of the claimants can intervene despite ideological distance from the target when its strategic interest is strong.
An overcommitted country must be willing to decline rather than promise assistance that the event treats as already delivered.

The AI distinguishes creating a guarantee, fulfilling a delivery, proposing diplomacy, accepting diplomacy, preparing a front, and entering war.
Those require the appropriate native desire or strategy and their own completion checks.
All temporary strategies have a crisis owner and explicit removal conditions.
The event does not leave permanent attack desire against a target that became a major or whose crisis closed.

### Human-crisis pressure

The existing non-AI crisis-pressure owner is used where its current caller contract applies.
The proposed intensity is mild for the baseline, standard for Partition Fever, and severe for Grand Partitions.
It can increase supported incident opportunities and shorten eligible incident cooldowns within their hard floors.
The actual helper outputs and context must be inspected before use.

It cannot create an eligible target, bypass a major check, change a signed map, shorten a promised response deadline, debit resources, or cause an unapproved declaration.
The challenge comes from more persistent political pressure and harder choices, with the same consent and outcome rules.

## Required AI scenario matrix

| Scenario ID | Surface and declared campaign situation | Required ordering or behavior | Evidence still required |
| --- | --- | --- | --- |
| AI01 Isolated border concession | Declared small target is outmatched in available strength and supply, two legal ready attackers, modest viable loss, no protector | Feasible T1 and T5 each outrank T6 in this fixture, with T1 through T6 all enumerated | Complete target-action pool and quote-aware score trace |
| AI02A Reachable protector | Unprotected target has one capable legal recipient and sufficient time | Target T2 gains priority over its otherwise identical no-recipient state | Paired target pools with recipient and route gates |
| AI02B Existing guarantee | The same target already has the operational guarantee | Duplicate P1 and duplicate T2 request are unavailable, target T6 rises and claimant C5 falls relative to AI01 | Separate target, claimant, and protector pools |
| AI03A Lost intervention route | An accepted pledge loses its only legal entry route before war | Future intervention credit disappears, target reassesses missing support | Dated route transition and all affected pools |
| AI03B Failed delivery | An approved material obligation passes its due date without delivery | No contribution receipt, target and claimants use actual stockpiles | Payment, due-date, and recipient-state trace |
| AI03C Declined due intervention | War begins and a pledged protector explicitly declines legal entry | Broken commitment recorded once, actual war roster controls strength assessment | Dated entry opportunity and rejection trace |
| AI04 Split coalition | Two claimants overlap on a critical state, cohesion below 25 | C5 is unavailable until at least two members explicitly renew a valid common enforcement basis | Hard-gate test followed by a separate cohesion-band score sweep |
| AI05 Genuine core compromise | One narrow core claim, one broad opportunistic demand | A feasible narrow compromise has a meaningful route to acceptance | Full claimant pools and claim-type factors |
| AI06 Defensible larger minor | Grand Partitions target with real army, supply, and defensible access | Defense remains viable, no scripted surrender or forced AI extinction | Strength-signal and front-burden sensitivity |
| AI07 Overcommitted major | Major has three accepted active claimant or protector commitments and receives a fourth offer | Fourth acceptance is invalid, pending invitations alone consume no commitment slot | Hard-gate trace and existing-action service check |
| AI08 Exact reserves | Payer has exactly the quote, then one native quantum less | First purchase allowed, second unavailable, no partial benefit | Cost owner boundary evidence |
| AI09A New-firing thresholds | Chaos 0, 1, 195, 200, 595, and 600 in the same feasible world | Correct firing gate and requested quota range, then actual feasible count | Complete opening pools and separate quota trace |
| AI09B Active-batch thresholds | Dated crossings through 200 and 600, including a later drop | Correct sequential MTTH eligibility and latched active form, original target count unchanged, zero activation Chaos | Transition schedule and evolution timing distribution |
| AI10 Promotion during consent | Target becomes major with a popup open | All authored victim-facing action weights become zero and stale action rejects | Event and probability trace at the changed state |
| AI11 Merged war | Two target wars become one broader conflict | Narrow unsafe peace unavailable, each target outcome remains separate | War provenance and settlement proof |
| AI12 Thin pool | Zero, one, and fewer than rolled complete target packages | Zero is unavailable, short pools produce their actual feasible count | Full declared candidate set and opening reconciliation |
| AI13 Material proposal change | New recipient or larger state set after signatures | Old signatures and approvals cannot execute | Stale-context and action-pool comparison |
| AI14 Price change | A supported universal cost modifier changes after display | New quote governs confirmation and debit, with no old-price benefit | Quote, payment, and refund comparison |
| AI15 Opportunity starvation | Multiple valid crises, repeated five-day checks, limited resources | Every opportunity evaluated each cycle, due obligations precede new discretionary purchases, blocked actions cannot monopolize service | Complete action race, due dates, tie order, and cadence evidence |
| AI16 Human pressure | Matched human and AI fronts at each intensity | Only the documented pressure dimensions differ, hard protections remain identical | Shared helper trace and threshold sweep |
| AI17 Shared firing and repeated waves | Complete random-event caller pool, repeat timer, weight reduction, recovery, and dated Event 113 opportunities | One pacing change per actual wave, no duplicate firing credit per target, repeat Chaos receipts remain crisis-specific | Shared caller inspection and campaign sequence |
| AI18 Claimant and protector action families | Separate phase-valid C1 through C6 and P1 through P6 pools, including dispute and narrowed aid | Each hard gate and meaningful competing route exercised | Complete actor-specific pools and score-only comparisons where appropriate |
| AI19 Variant opportunities | V1 through V8 each present alone and with simultaneous factual branches | Factual prerequisites gate each branch, mandatory reactions always occur, one transition cannot produce duplicate consequences | Event-driven branch register and transition trace |
| AI20 One action authority | Human dossier and native AI decision point to the same current opportunity | First valid action consumes the opportunity, second callback cannot charge or repeat it | Shared action receipt and same-date execution trace |

All numerical probability, dominance, and timing conclusions remain unresolved until the required HOI4 tools and complete current sources are available.
The planning audit may assess whether the scenarios are complete enough to test.
It cannot replace their required engine-backed results.

## Chaos impact map

The direct event contributions describe coordinated coercion, a coerced border change, a broken signed agreement, and the eventual containment of this particular attempt.
Ordinary war, peace, annexation, guarantees, faction changes, casualties, and World Tension remain with their shared source owners.
Every direct contribution is tied to a concrete crisis record and can occur only once for its defined consequence.

| Consequence | Proposed direct Chaos | Actual trigger | Repeat guard and overlap rule | Reversal or containment |
| --- | ---: | --- | --- | --- |
| Public coordinated ultimatum | +5 per actual target crisis | At least two accepted claimants publish a valid exact demand to a living eligible minor | One opening receipt keyed to the immutable crisis identifier, no credit for failed assembly or empty slots, no added World Tension for the same announcement | Eligible for that crisis's single containment reduction |
| Substantial escalated demand | +5 maximum per crisis | Claimants publish a valid larger demand that adds at least 25 percentage points of the opening population to demanded land, or changes a limited offer into a complete offer | One escalation receipt, actual new coercive proposal required, evolution activation alone gives zero | No refund for withdrawing and resubmitting the same escalation |
| Coerced partial border change | +5, or +10 when actual lost population or physical industry reaches 50% of the opening total | A concluded limited or interrupted settlement leaves the target alive with actual transferred territory | One cession receipt per crisis, actual result measured after execution, complete annexation route uses generic annexation instead | A later durable settlement may receive the one containment reduction |
| Broken ratified settlement | +5 maximum per crisis | A signatory restarts aggression or refuses a due material treaty obligation during the 45-day follow-through | One breach receipt, this premium measures the broken agreement, the actual war uses the generic war source | Ending the new fighting does not replay this receipt |
| Durable full prevention or durable limited settlement | −5 maximum per crisis | The applicable proven outcome holds for 45 days with no remaining award, aggression, or broken obligation | One containment receipt, never larger than this crisis's actual direct positive contribution, never paid for a popup, pledge, or mere timeout | Once consumed it cannot be earned again by reopening the same crisis |
| Evolution eligibility, activation, or log | 0 | Form or content becomes available | Never routed as a destabilizing consequence | None |
| War, peace, annexation, capitulation, guarantee, faction change, deaths, or World Tension | 0 additional direct copy | Shared owner observes its actual event | Retain normal shared accounting and avoid a second Event 113 copy | Shared owner decides its own reversal |
| Interrupted work with no completed transfer or breach | 0 | No relevant world consequence occurred | Cleanup and retry do not manufacture a source | None |

For a target whose opening industrial total is zero, the industrial loss ratio is ignored.
All Chaos loss ratios use the crisis opening state snapshot and each state's opening population and physically owned civilian plus military factories, including damaged factories.
Awarded states count at most once regardless of later construction, population drift, controller changes, or handover installments.
The population test remains available.
The cession premium is assessed from distinct actual awarded states, not from the number of callbacks or draft versions.
An eventual full partition does not also receive a new partial-cession premium at that terminal outcome.
A previously concluded partial loss and a genuinely later native annexation remain separate historical consequences, with no replay of the earlier premium.

The direct opening amount scales naturally with the actual number of targets.
A full eight-country wave can therefore contribute more political instability than a two-country attempt, while still counting as one event firing for pacing.
Later larger demands and actual losses add pressure only when they happen.
Successful defense and stable compromise can contain that pressure without turning repeated easy negotiations into a source of unlimited negative Chaos.

The receipt identity is the immutable crisis identifier plus consequence kind, retained with the terminal outcome history after active work ends.
A later legitimately selected crisis after 540 days has new receipts and may produce new consequences.
A reopened panel, renewed demand, evolved form, claimant replacement, or restored saved game of the same crisis does not create a new receipt identity.
There is no additional lifetime family cap on positive consequences, since separate later coerced partitions remain separate destabilizing events.
This intentionally cumulative design must be tested over repeated waves with the actual shared firing schedule.
Each crisis can reduce direct Chaos by at most 5 and never below its own recorded net direct contribution of zero.
It cannot offset unrelated shared war, annexation, or other event sources through its containment receipt.

