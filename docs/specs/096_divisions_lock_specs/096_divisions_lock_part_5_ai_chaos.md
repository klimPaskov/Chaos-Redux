# Event 096: AI policy and Chaos consequences

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

## 1. Campaign behavior

The AI can retain its force and accept a prolonged lock. Demobilization is a deliberate policy choice under conditions where it can help. This event must not quietly dismantle an army fighting a war because a repeated willingness roll eventually selected a destructive outcome.

Use one country-local AI policy. Human decision objects do not also run an independent native AI willingness loop. The policy and human actions call the same eligibility and exact-removal resolver, with stricter AI survival conditions.

| Situation | Intended AI response |
| --- | --- |
| At war, capitulated, or the verified AI threat input reports a security threat | Retain force, both removal actions forbidden |
| Another registered country-lock owner would still prevent editing after this event releases | Retain force, both removal actions forbidden |
| Measured capacity growth is sufficient to close the gap under the stated projection | Retain force while that condition remains true |
| Stable peaceful slight excess with safe ordinary formations | Prefer patience in the relative score pool, but permit a deliberate one-formation action |
| Stable peaceful severe excess with a sufficient safe pool | Permit the severe batch as a meaningful option |
| No provably eligible safe formations | Retain force without repeated empty attempts |
| Within allowance | No reduction action, release when the minimum floor allows it |
| Special country whose provider protects its formations | Still measure its army, retain it unless the provider supplies a compatible action |

No difficulty setting changes F, A, the minimum week, or the hard release rule. AI behavior can differ through its actual strategic situation, not a hidden national allowance exemption.

## 2. Inputs and score policy

Let e be max(0, F/A minus 1), as defined in Part 2, and E be min(e, 2). The allowance floor of ten guarantees a positive denominator.

Use three hard hold inputs:

- T is true when the country is at war, capitulated, or the installed documented AI-threat input reports a threat. The candidate input is country `ai_attitude_is_threatened`, together with the ordinary war and capitulation predicates. Verify the adapter.
- O is true when at least one other registered native country-lock hold remains. Per-template restrictions alone are not equivalent to a country-wide hold.
- G is true when a valid seven-day capacity history has positive growth and, at unchanged current F, the measured rate would close the current gap within thirty days. This is an AI heuristic, not an allowance bonus or a promise to the player.

With missing history, zero growth, or falling capacity, G is false. Clear or rebase the trend samples when the regime changes, so a coefficient change is not mistaken for economic growth. A one-time territorial gain can temporarily influence the heuristic, but the rolling history removes it when it is no longer recent. The hard release check always uses actual current capacity.

Use a linear endpoint estimator over eight consecutive complete daily observations, spanning seven elapsed days under the same actor, grant, and regime. Let delta_A = A_now minus A_seven_days_ago. G is true only while oversized, delta_A is positive, and `7 * (F_now - A_now) <= 30 * delta_A`. Equality qualifies. Missing observations, a new grant, political succession, or a regime change restart the sampling window. No interpolated observation supplies missing history. This is a thirty-day straight-line heuristic, not a claim that a past gain will repeat or a forecast shown to the player.

If T, O, or G is true, choose the retain posture without a removal roll. Otherwise the complete proposed posture pool is:

| Candidate | Relative score | Additional gates |
| --- | ---: | --- |
| Retain current force | 40 | Always valid while the country is held and oversized |
| One-formation action | 20 + 40E | At least one exact eligible safe formation, AI survival rules pass |
| Severe batch | 10 + 50E | e at least 0.75, at least two eligible safe formations, batch and AI survival rules pass |

These are relative design scores in one complete proposed pool. They are not percentages, independent daily action chances, or native `ai_will_do` rates. The future probability audit must establish the actual adapter and its external factors.

At e equal to 0.5, the first two scores tie at forty. At e equal to 1, both removal scores are sixty. At e at least 2, the scores saturate at one hundred and one hundred ten, while retaining the army still has a nonzero score. Saturation affects policy preference, not the live allowance or raw batch-size excess.

## 3. One explicit posture state machine

The first permitted AI posture review occurs no earlier than two days after application and no earlier than two days before the current minimum-release day. With an ordinary seven-day opening, this is day five. This gives the country time to receive immediate capacity changes before choosing a sacrifice.

Each posture review chooses exactly one outcome. Retain becomes sticky. One-formation or batch authorizes one bounded attempt through the shared resolver at that review's legal action time. It never authorizes an open-ended sequence of later removals.

After an actual successful removal that leaves the country oversized, schedule a fresh posture review after:

**d_AI = clamp(ceiling(10 / (1 + e)), 2, 10) days.**

Use the refreshed post-action e. The next review may select retain. If the attempt fails, becomes invalid, or removes nothing, enter sticky retain until a material change. If it reaches allowance, stop the AI action path and apply the ordinary release predicate.

Sticky retain is not rerolled because an ordinary timer tick passed. Reconsider it only after:

- a new genuine firing or applicable evolution change
- a change in T, G, or O
- the eligible safe pool changing between empty and nonempty
- an absolute change of at least ten percent in F or A relative to the values stored at the last posture choice

The ten-percent test is inclusive. Smaller changes accumulate against the stored baseline because that baseline is not rewritten on every refresh. A zero-force baseline uses an explicit transition from zero rather than division by zero. Reset the baseline after a real posture choice.

A material change can request a review but cannot bypass a pending confirmation, the country's transaction guard, or its next legal AI action day. A new veto takes effect immediately, cancelling or invalidating a pending AI removal. A newly permissive state schedules reconsideration at the next legal action boundary.

Human and AI authority share one request slot. Control handover invalidates any pending request. A human does not inherit an AI authorization, and an AI does not execute a previous human confirmation. Save and load preserve posture, baselines, due days, request states, and consumed receipts.

## 4. AI safety and native evidence

AI removal uses the same ownership, combat, and source-provider exclusions as human removal. It additionally cannot remove its final owned fielded formation, a formation identified by a verified provider or campaign rule as essential, or more formations than its remaining safe pool allows. A batch is bounded by the lesser of its confirmed k and the exact pool that preserves those conditions.

Country-wide war and threat vetoes deliberately provide a robust first layer. Do not invent a generic native critical-front getter. If a campaign-safety predicate or exact owner relationship cannot be established, it cannot be bypassed with a positive score.

The archive records a read-only probability specialist's abstract score and posture review in its earlier planning environment, where no HOI4 probability routes were exposed.
This is historical capability evidence; discover current routes and follow the current [probability-owner workflow](../../../.agents/skills/chaos-redux-subagents/SKILL.md#mcp-evidence-in-handoffs) for future native work. The old three-unit batch proposal was superseded by Part 3's size-scaled maximum of ten, and the original timer-driven retain reroll was replaced by sticky retain. Native selection odds, cumulative action sequences, uniform unit sampling, and MTTH distributions remain unrun. Required fixtures are in Part 8 and the research record.

## 5. Chaos measures material consequences

The event's unnatural global interruption of military establishment can add Chaos. The Peace cluster describes its strategic tendency toward demobilization and restraint. It does not require every immediate consequence to lower Chaos.

Keep a persistent Event 096 family accounting window of ninety game days, with at most thirty positive Chaos points in that window. A genuine new firing does not reset a still-open window. Counters, contributions, and reason receipts survive save and load. If a concrete consequence is larger than the remaining budget, grant only the remaining amount. All authored changes below are multiples of five.

For manifestation and relapse coverage, use the relevant firing's recorded entry-force weights. They are historical attribution weights, not a new live public metric. A country whose editing was already unavailable through another registered country-wide owner does not count as newly deprived merely because Event 096 adds another hold.

| Consequence | Direction and initial magnitude | Dynamic basis | Repeat guard and overlap | Reversal treatment |
| --- | --- | --- | --- | --- |
| Actual initial loss of country-wide editing access | Positive, 5, 10, 15, or 20 | Newly deprived entry-force share of the firing's total positive entry force, rounded up by quartile | Once per genuine dispatch, zero for duplicate delivery, family positive budget applies | Eligible for the single restoration credit below |
| First material evolved relocks across at least 10 percent of entry-force weight | Positive 5 | Previously released countries actually regain a hold through failed evolved review | Each country contributes its first relapse only for this firing, threshold awarded once, budget applies | No per-country automatic refund |
| First material evolved relocks across at least 25 percent of entry-force weight | Positive 5 | Broader actual relapse coverage | Separate once-only threshold, same country weights cannot be repeatedly added, budget applies | Same |
| Full administrative restoration of a firing cohort that produced a positive manifestation | Negative 5 | All still-required holds and reviews have ended by legitimate compliance, with actual restoration of access attributable to Event 096 | Once for the firing, no credit if disappearance, manual clear, settings cancellation, or invalid succession caused apparent completion | Never repeatedly credit the same country's unlock/relock cycle |
| Continued excess without a new material consequence | Zero | Duration alone is not a fresh disruption | No daily, weekly, or monthly farming | Not applicable |
| Optional demobilization action | Zero directly | The action changes force and may help achieve genuine cohort restoration | No per-unit reward and no resource-action loop | No compensating free units |
| Ordinary conquest, battle deaths, normal construction, or population growth | Zero from Event 096 | Shared systems already own those causes | Do not duplicate generic war or death Chaos | Their own systems handle any reversal |
| Evolution eligibility, MTTH completion, activation, logging, or review-credit allocation | Zero directly | Status is not itself a concrete consequence | Separate receipts from consequence accounting | No arbitrary refund on disabling a stage |

If the total positive entry force is zero, the force-weighted manifestation is zero rather than an undefined ratio. If no actual editing access was lost, do not invent a manifestation award. Retaining another owner's lock after Event 096 compliance is not an attributable restoration of access.

Restoration is evaluated through maintained completion receipts, not a recurring global army scan. A vanished country or invalidated successor can close scheduling but disqualifies the restoration reward. A manually cleared or disabled inspection also closes work without claiming successful containment. A genuine repeat has its own compliance history, while the family window still bounds positive feedback.

If a genuine repeat replaces an unfinished grant, retire that grant's unfinished restoration eligibility without a negative award. Preserve any Chaos already paid, its fixed entry denominator, and all once-only reason receipts. The replacement grant can qualify independently only through its own actual manifestation and full legitimate completion. It cannot later cash the superseded grant's completion as well. Duplicate dispatch delivery does not retire a valid grant.

### Conserved historical attribution through succession

Keep a source-lineage identity for every retained entry-force share, credited consequence, and Evolution II watch baseline. These are historical records, not current national capacity. A political split must not copy the predecessor's entire force weight into every branch.

At the actual transfer, first obtain a complete post-transfer F for every legitimate continuing branch, including any surviving predecessor. If their total is positive, partition each retained historical force share and the retained Evolution II baseline in proportion to those forces. The allocated fixed-point shares must sum exactly to their source amount. Assign indivisible remainders by a documented deterministic country-ID order. Freeze the partition after transfer rather than reweighting it every day. Carry each source share's already-credited status to its children. Already credited relapse contributions remain credited and cannot become new unclaimed weight after a split.

At a merger, combine disjoint shares once and preserve source-lineage identities to prevent duplicate contribution. Combine the associated watch baseline shares only for lineages that retain a watch. When a merged hold later releases into a new watch, the ordinary fresh release baseline replaces those old watch baselines. Historical entry-force and Chaos receipts never reset for that reason.

If every continuing branch has zero force, move its retained force weight to an inactive retired share. Keep that share in the original fixed denominator, with zero future manifestation or relapse contribution. Retired, unresolved, or incomplete continuity cannot produce a successful restoration reward. Active plus retired shares conserve the original attributable amount. Credited status is an independent once-only bit on a share, not another amount added to the conserved weight. A credited active share may still contribute to current pacing, but never to a second first-relapse award.

The same conserved lineage weights feed the active-evolution pacing aggregate. Only currently oversized held branches contribute their assigned active share. A merger or split does not increase the original world-entry denominator. Exact political relationships, snapshot completeness, and fixed-point partition behavior are native lifecycle gates. No guessed relationship, division-count proxy, human-manpower proxy, or duplicate force attribution is acceptable.

The positive window cap prevents rapidly repeated selections or deliberate relock cycles from driving the world through several Chaos tiers. The once-only negative credit and its positive-manifestation prerequisite prevent demobilization clicks, toggles, and empty cohorts from farming Chaos reduction.

## 6. Required named policy scenarios

The core matrix includes peaceful small and large countries at the same relative excess, a threatened country without a war, an ongoing war, a capitulated actor, a rapidly growing industrial base, another lock owner, zero eligible units, protected Event 019 units, robot and rat armies, a last-unit case, repeated dispatches, all evolution transitions, settings changes, and save/load in every posture.

For each, record the actual complete pool, source revision, F and A, raw e and capped E, N_owned, k, T/G/O, posture baselines, pending request, owner receipts, due day, and external AI modifiers. Score rankings can be checked arithmetically, but claims about actual probability require the native inspect, evaluate, sweep, and compare workflow. Sequence analysis must distinguish sticky retain from successive separately selected demobilization actions.
