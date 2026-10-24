# 120 Widespread Mutiny, Part 1: The army refuses

## Event identity

| Field | Design decision |
| --- | --- |
| User-confirmed event identity | Event 120, Widespread Mutiny (24 October 2026) |
| Historical catalog reference | 131 |
| Proposed type | Minor Repeatable |
| Proposed starting Chaos level | 1 |
| Proposed cluster | Domestic Unrest, cluster 16 |
| Proposed base cluster severity | Low |
| Historical requested catalog state | To Be Reworked (pre-migration intake recorded Unavailable) |
| Proposed evolution | Brothers Across the Trenches, eligible at Chaos 600+ |

The proposed type and starting level are retained in this design. If accepted, a routine outbreak is a limited military emergency. A badly handled outbreak can grow into a territorial revolt. That growth is a consequence of the campaign and the response, rather than the default result of drawing a Low event.

The event identity and event ID are confirmed by the user's 24 October 2026 decision, “Adopt uploaded IDs and migrate the catalog.” The parent owns and is performing the catalog migration, including preservation of the displaced Massive Volcano Eruption and historical catalog-131 Widespread Mutiny records in the migration record. This decision does not accept the proposed mechanics, values, evolution or linked-event work. Shared registry allocation remains parent-owned.

All added route, action, phase, achievement and asset labels in this package are working labels. The supplied event and evolution titles retain the user's wording. Final player-facing text is written during implementation from the directions in Part 7.

## The central choice

The government still has an army on paper, but part of that army no longer accepts its orders. Soldiers identify a concrete grievance and retain the weapons, training and connections that make their refusal matter. The player decides how much military capacity to release, how much authority to concede, and whether loyal troops can impose a settlement without widening the revolt.

Each outbreak should make three facts immediately legible: which formations are affected, what they currently refuse to do, and when the next consequence can occur. The opening never disguises a permanent formation loss as a temporary national modifier.

The historical direction favors differentiated grievances, concrete delivery and councils with explicit institutional duties. The research dossier explains the evidence and its limits. The design distinguishes material relief, representation and political rupture, with revolutionary outcomes arising from actual escalation. [Historical research, S01, S04 and S08](120_widespread_mutiny_research.md)

## Who can be affected

The normal entry anchor is native war support at or below 35. Every eligible country is considered, including AI minors, subjects, countries with one division, player countries and special actors whose soldiers are human. A long war is an aggravating factor, not a mandatory admission requirement. Peacetime countries can face overdue discharge, disputed deployment or unresolved mobilization grievances.

A country needs at least one actual eligible land formation and authority over a meaningful response. A wholly stateless exile with no independently administered forces cannot receive an impossible territorial crisis. Its soldiers serving elsewhere remain eligible through the recorded owner and commanding host. The response identifies both authorities and gives each only the powers it holds.

Eligibility follows the formation's actual character. Human troops in a mixed or unusual country remain eligible. An actual nonhuman force is eligible only when its owning system supplies a compatible disobedience contract. A special-country label alone cannot decide whether soldiers have leave, morale or civilian obligations.

Expeditionary and subject formations retain their legal owner. The host can provide relief, change an assigned task or offer a safe withdrawal where its authority permits. It cannot permanently demobilize, transfer or confiscate a borrowed formation. A parent country cannot charge the host twice for the same equipment or personnel. These cases use the ownership contract in Part 5.

Naval and air personnel can appear as contextual supporters in ports and bases. The formation outcomes in this design concern land formations. A land army mutiny never silently transfers fleets, air wings or strategic stockpiles through a broad civil-war effect. Any independently requested future naval mutiny would require its own exact vessel and crew contract.

## A worldwide draw with local consequences

The ordinary event draw creates one bounded snapshot of eligible countries. One eligible primary country is selected using its outbreak weight. That country receives an outbreak. Each other eligible country receives an independent outbreak check. A minor's presence in the candidate pool does not depend on its army being large enough to outrank a major.

The same calculation supplies a primary-country weight and an additional-country chance. Those uses have different probability semantics. The primary weights are normalized only across the complete eligible pool. An additional-country value is a direct percentage chance for this single event draw.

Let `r5(x)` round a nonnegative value to the nearest multiple of five, with a half-step rounded upward. The initial tuning proposal is:

`H = clamp(15 + r5((35 - W) / 2) + 10L + 15S + 10K + 10B + 15X - 10R, 5, 70)`

| Input | Meaning at the snapshot |
| --- | --- |
| W | Native war support, between 0 and 35 for a normal candidate |
| L | A relevant war has lasted at least 180 days and the country's forces have faced combat in the last 30 days |
| S | The candidate cohort has suffered severe supply failure for at least 10 of the previous 20 days |
| K | Verified recent military losses reach 5% of the country's deployed army manpower at the start of the preceding 30-day window |
| B | A relevant military promise was broken within 180 days |
| X | Event 114 has a live, compatible Desertion Crisis affecting this candidate |
| R | A relevant delivered military settlement completed its country recovery and closed within the preceding 180 days |

The flags are binary. Severe supply means a verified supply ratio below 50% for the actual candidate formation or an explicitly documented equivalent operational source. A mere missing reader does not count as severe supply. Recent casualties are a measured increase over a recorded interval, excluding desertion, demobilization, transfer and administrative deletion. The initial denominator is retained so mobilization cannot rewrite past loss severity.

The implementation must verify the current readers before adopting this formula. The numerical anchors are authored design proposals. They are not measurements of historical mutiny frequency or claims about the native engine.

Only countries without an active Event 120 incident and without its 90-day settlement protection enter a fresh draw. Ongoing incidents progress through their own callbacks. A repeat draw cannot replace their actors, reroll the same deadline, add free troops or reapply the opening loss. The shared Minor Repeatable selection and recovery rules remain authoritative for the event's global weight.

The primary actor is known before the shared history record is written. A worldwide occurrence records its affected-country count and offers country-specific detail, with a bounded report for the player. The user should not receive a popup for each remote AI minor.

## Two values, actual formations

The whole event uses two persistent custom numeric values. Neither is spendable.

| Value | Range and meaning | What changes it | What the player can infer |
| --- | --- | --- | --- |
| Disaffection | 0 to 100, willingness to reject the present military settlement | Conditions, losses, unmet demands, reliable relief, coercion and peace | Higher values make desertion, spread and organized resistance more likely |
| Agreement confidence | 0 to 100, belief that the relevant authorities and delegates will deliver their commitments | Fulfilled promises, observed delivery, missed deadlines, bad-faith attacks and accepted guarantees | Higher values make a negotiated return more reliable and durable |

Native war support, current force strength, equipment, supply, time remaining and the current phase are supporting facts. The evolution and council country reuse the same two meanings. They do not add a fraternity currency, council legitimacy bar, hidden diplomatic influence purse or another progress meter on a different screen.

Country values summarize a shared incident. Each cohort has a recorded phase, demand, exact membership, deadline and outcome history. These are lifecycle facts. Cohort behavior depends on the country values plus its local conditions. A settled cohort is never punished because an unrelated region remains unsettled.

Initial Disaffection is:

`D0 = clamp(35 + r5((35 - W) / 2) + 10L + 10S + 10K + 10B + 10X - 10R, 25, 70)`

Initial Agreement confidence is 40, increased by 20 after a relevant delivered settlement and reduced by 20 after a broken promise. It is clamped between 0 and 80 at entry. An imported Event 114 incident uses the worse live Disaffection and preserves the actual promise history. It does not receive a fresh favorable confidence reset.

## Selecting the affected cohort

The event selects geographically coherent formations sharing a supply route, deployment grievance or command relationship. It prefers the formations that actually experienced the pressure. It does not select a random elite armor division on another continent because that division is convenient to script.

The initial target budget is 5% of deployed army manpower, with a contextual increase to 10% when at least two of long war, supply failure and recent heavy losses are present. This is a selection budget, not a promise that every native division can be split into exact fractions. Membership is chosen from actual formations with their live manpower and equipment. The preview reports the resulting count and strength.

A country can hold at most three active regional cohorts. Baseline spread aims to keep affected deployed manpower at or below 30% of the incident's opening army strength before a separately warned organized revolt. Growth in the national army does not enlarge that opening cap. Repeated draws cannot fill the cap again.

Whole-formation granularity is handled explicitly. If the smallest eligible formation exceeds the budget, one such formation can receive the opening readiness disruption, with a cap of 50% of its current organization removed and no automatic personnel or equipment removal at entry. This allows a one-division country to participate without destroying its army on the first message. A later voluntary demobilization can still remove its last formation, but the confirmation states that consequence and the AI weighs national defense.

The opening refusal is selective. The affected troops reject new offensive commitments or a named disputed deployment while retaining a reduced ability to defend themselves. Their exact current formation identities, equipment, strength, experience and ownership remain part of the incident. The technical feasibility gate for enforcing orders is in the implementation handoff. A national attack penalty is insufficient evidence that this behavior exists.

## Demand families

One primary demand and, at most, one supporting demand drive a cohort. A new demand must arise from changed circumstances, rather than being added when the player has almost finished the existing mission.

| Family | Observable premise | Satisfying response | Distinct aftermath |
| --- | --- | --- | --- |
| Leave and rotation | Extended continuous duty or a broken leave schedule | Withdraw and rest the named formations for the promised period, with a replacement or accepted front risk | Experienced formations return after real downtime |
| Supply and treatment | Sustained lack of equipment, transport, billets or a secure route | Deliver the relevant support and demonstrate recovery | A repaired route helps the army beyond the incident |
| Fair demobilization | War has ended, deployment was extended, or discharge order is disputed | Publish and execute a fair release schedule | Fewer active soldiers, equipment returns and a protected reintegration period |
| Representation and discipline | Delegates are excluded or abusive command is disputed | Recognize a bounded negotiating channel and change the relevant command practice | A service compact or a strained command settlement |
| Refusal of a renewed offensive | Recent losses and low confidence in another attack | Postpone the named commitment, rotate the cohort or negotiate a smaller obligation | Operational delay with a more reliable surviving force |

Regional and colonial variants change the factual grievance, interlocutors and deployment context. Religion, ethnicity and nationality are never generic numerical causes of mutiny. Distrusted orders, unequal treatment and an actual political conflict can be researched contextual causes. [Historical research, S10](120_widespread_mutiny_research.md)

## Progression and cadence

The first response window is normally 30 days. It becomes 20 days for an already organized emergency imported from an active crisis and 45 days when the disclosed solution requires a verified remote transport route. An ordinary opening cannot escalate before its displayed first deadline simply because the starting value is high. Direct violence or an explicit broken compact can accelerate the case after a new warning.

Every 10 days, an active country incident reviews its recorded cohorts and makes exactly one country-level update. The review reads actual elapsed time and current relevant conditions. Repeated callbacks on the same day give no additional progress or harm. Each positive condition below counts at most once when any unresolved cohort qualifies. A relief reduction requires every unresolved cohort sharing that grievance to be covered, with at least one such cohort. The currently viewed cohort never determines this aggregation.

| Condition during a review | Disaffection change |
| --- | --- |
| War support remains below 25 | +5 |
| Severe cohort supply failure persists | +5 |
| A new verified heavy-loss interval has occurred | +5 |
| A promised milestone is overdue and authority still exists to deliver it | +10 |
| Agreement confidence is 20 or lower | +5 |
| Promised leave is actually being honored | -10 |
| Supply has remained restored for 10 days | -5 |
| A relevant peace or disengagement has been sustained for 10 days | -5 |

The net change is clamped between -20 and +20 per review. These pressure terms apply only while at least one relevant cohort remains unresolved. After every cohort has a lawful disposition and there is no live breach, the recovery review instead reduces Disaffection by 5 every 10 days. Low national war support alone cannot keep a settled incident open forever.

A completed compact can additionally reduce Disaffection once by 20. Successful loyal-force containment reduces it once by 25 through restored control, while its confidence cost remains. A fulfilled major promise raises Agreement confidence by 20. A first verified material delivery raises it by 10. A missed deadline lowers it by 20. An attack under a parley guarantee lowers it by 30. All changes require distinct receipts, so deliveries and callbacks cannot farm confidence.

| Phase | Entry and real behavior | Exit |
| --- | --- | --- |
| Refusal | Opening cohort rejects the named duty and loses bounded readiness | Delivered relief, negotiated release, suppression or an unmet deadline |
| Desertion | Disaffection at least 60 after the response deadline, with the relevant grievance still unresolved | Amnesty and delivery, completed demobilization, or organized resistance |
| Organized mutiny | Disaffection at least 80 plus a failed or refused settlement, or a failed crackdown | Binding compact, warlord defection, bounded armed revolt or military defeat |
| Recovery | A compact, completed containment or lawful release gives every affected formation a final disposition | 90 days of observed compliance, or a new material breach |

These phases are ordinary progression. Their existence does not require an evolution or a higher Chaos tier. Part 3 adds the specific 600+ transformation.

## Spread, relief and recurrence

An unresolved incident can form another cohort after an eligible review. Spread requires Disaffection of at least 60 and expiry of the opening response deadline. A new cohort needs a real shared link such as the same logistical corridor, a transferred grievance, known delegates or a nearby compatible formation. There is at most one spread check per country per 20 days, and no check while a funded settlement is being delivered on schedule. Reject a prospective whole cohort if its admission would exceed the 30% opening-army cap. The one-formation opening exception cannot be reused to enlarge spread.

The proposed spread chance is 10% at Disaffection 60 to 79 and 25% at 80 or above, increased by 10 percentage points for a newly broken promise and reduced by 10 for Agreement confidence of 70 or above. A newly broken promise means a distinct breach recorded since the previous eligible spread check. Its bonus is consumed by the next eligible check, succeeds or fails, expires after 20 days, and cannot stack with another breach. The final chance is clamped between 0% and 45%. The current shared human-crisis pressure policy can modify this once through its verified owner contract. It cannot create an extra event-local difficulty toggle or be charged again through both the timer and the same outcome roll.

Successful containment of one cohort leaves other cohorts intact. Countries outside the incident remain unaffected by its local cleanup. Country settlement closure occurs after all dispositions and the recovery mission complete. It starts one 180-day history-influence window, whose first 90 days also protect against a fresh ordinary draw. The remaining 90 days retain the delivered-settlement recurrence modifier without draw protection. A later breach can reopen the existing history. It cannot reset the earlier losses or pretend that demobilized formations have returned.

Related design: [Responses and formation outcomes](120_widespread_mutiny_spec_part_2_responses.md), [Brothers Across the Trenches](120_widespread_mutiny_spec_part_3_evolution.md), and [Ownership, connections and Chaos](120_widespread_mutiny_spec_part_5_connections.md).
