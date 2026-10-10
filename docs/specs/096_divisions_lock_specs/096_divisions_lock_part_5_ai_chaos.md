# Event 096: AI policy and Chaos consequences

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

## 1. Campaign behavior

The AI can retain its force and accept a prolonged lock.
Demobilization is a deliberate policy choice under conditions where it can help.
This event must not quietly dismantle an army fighting a war because a repeated willingness roll eventually selected a destructive outcome.

Use one country-local AI policy.
Human decision objects do not also run an independent native AI willingness loop.
The policy and human actions call the same eligibility and exact-removal resolver, with stricter AI survival conditions.

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

No difficulty setting changes F, A, the minimum week, or the hard release rule.
AI behavior can differ through its actual strategic situation, not a hidden national allowance exemption.

## 2. Inputs and score policy

Let e be max(0, F/A minus 1), as defined in Part 2, and E be min(e, 2).
The allowance floor of ten guarantees a positive denominator.

Use three hard hold inputs:

- T is true when the country is at war, capitulated, or the installed documented AI-threat input reports a threat.
  The candidate input is country `ai_attitude_is_threatened`, together with the ordinary war and capitulation predicates.
  Verify the adapter.
- O is true when at least one other registered native country-lock hold remains.
  Per-template restrictions alone are not equivalent to a country-wide hold.
- G is true when a valid seven-day capacity history has positive growth and, at unchanged current F, the measured rate would close the current gap within thirty days.
  This is an AI heuristic, not an allowance bonus or a promise to the player.

With missing history, zero growth, or falling capacity, G is false.
Clear or rebase the trend samples when the regime changes, so a coefficient change is not mistaken for economic growth.
A one-time territorial gain can temporarily influence the heuristic, but the rolling history removes it when it is no longer recent.
The hard release check always uses actual current capacity.

Use a linear endpoint estimator over eight consecutive complete daily observations, spanning seven elapsed days under the same actor, grant, and regime.
Let delta_A = A_now minus A_seven_days_ago.
G is true only while oversized, delta_A is positive, and `7 * (F_now - A_now) <= 30 * delta_A`.
Equality qualifies.
Missing observations, a new grant, political succession, or a regime change restart the sampling window.
No interpolated observation supplies missing history.
This is a thirty-day straight-line heuristic, not a claim that a past gain will repeat or a forecast shown to the player.

If T, O, or G is true, choose the retain posture without a removal roll.
Otherwise the complete proposed posture pool is:

| Candidate | Relative score | Additional gates |
| --- | ---: | --- |
| Retain current force | 40 | Always valid while the country is held and oversized |
| One-formation action | 20 + 40E | At least one exact eligible safe formation, AI survival rules pass |
| Severe batch | 10 + 50E | e at least 0.75, at least two eligible safe formations, batch and AI survival rules pass |

These are relative design scores in one complete proposed pool.
They are not percentages, independent daily action chances, or native `ai_will_do` rates.
The future probability audit must establish the actual adapter and its external factors.

At e equal to 0.5, the first two scores tie at forty.
At e equal to 1, both removal scores are sixty.
At e at least 2, the scores saturate at one hundred and one hundred ten, while retaining the army still has a nonzero score.
Saturation affects policy preference, not the live allowance or raw batch-size excess.

## 3. One explicit posture state machine

The first permitted AI posture review occurs no earlier than two days after application and no earlier than two days before the current minimum-release day.
With an ordinary seven-day opening, this is day five.
This gives the country time to receive immediate capacity changes before choosing a sacrifice.

Each posture review chooses exactly one outcome.
Retain becomes sticky.
One-formation or batch authorizes one bounded attempt through the shared resolver at that review's legal action time.
It never authorizes an open-ended sequence of later removals.

After an actual successful removal that leaves the country oversized, schedule a fresh posture review after:

**d_AI = clamp(ceiling(10 / (1 + e)), 2, 10) days.**

Use the refreshed post-action e.
The next review may select retain.
If the attempt fails, becomes invalid, or removes nothing, enter sticky retain until a material change.
If it reaches allowance, stop the AI action path and apply the ordinary release predicate.

Sticky retain is not rerolled because an ordinary timer tick passed.
Reconsider it only after:

- a new genuine firing or applicable evolution change
- a change in T, G, or O
- the eligible safe pool changing between empty and nonempty
- an absolute change of at least ten percent in F or A relative to the values stored at the last posture choice

The ten-percent test is inclusive.
Smaller changes accumulate against the stored baseline because that baseline is not rewritten on every refresh.
A zero-force baseline uses an explicit transition from zero rather than division by zero.
Reset the baseline after a real posture choice.

A material change can request a review but cannot bypass a pending confirmation, the country's transaction guard, or its next legal AI action day.
A new veto takes effect immediately, cancelling or invalidating a pending AI removal.
A newly permissive state schedules reconsideration at the next legal action boundary.

Human and AI authority share one request slot.
Control handover invalidates any pending request.
A human does not inherit an AI authorization, and an AI does not execute a previous human confirmation.
Save and load preserve posture, baselines, due days, request states, and consumed receipts.

## 4. AI safety and native evidence

AI removal uses the same ownership, combat, and source-provider exclusions as human removal.
It additionally cannot remove its final owned fielded formation, a formation identified by a verified provider or campaign rule as essential, or more formations than its remaining safe pool allows.
A batch is bounded by the lesser of its confirmed k and the exact pool that preserves those conditions.

Country-wide war and threat vetoes deliberately provide a robust first layer.
Do not invent a generic native critical-front getter.
If a campaign-safety predicate or exact owner relationship cannot be established, it cannot be bypassed with a positive score.

Native selection odds, cumulative action sequences, uniform unit sampling and MTTH distributions are checked by `chaosx_ai_probability_auditor` under the current [probability-owner workflow](../../../.claude/skills/chaos-redux-subagents/SKILL.md#mcp-evidence-in-handoffs); the fixtures are in Part 8.

## 5. Chaos measures material consequences

The event's unnatural global interruption of military establishment can add Chaos.
The Peace cluster describes its strategic tendency toward demobilization and restraint.
It does not require every immediate consequence to lower Chaos.

Keep a persistent Event 096 family accounting window of ninety game days, with at most thirty positive Chaos points in that window.
A genuine new firing does not reset a still-open window.
Counters, contributions, and reason receipts survive save and load.
If a concrete consequence is larger than the remaining budget, grant only the remaining amount.
All authored changes below are multiples of five.

| Consequence | Change | Repeat guard and overlap |
| --- | ---: | --- |
| A genuine dispatch newly removes country-wide editing access from at least one country | +20 | Once per dispatch; zero for duplicate delivery, or when every participant was already locked by another owner; family budget applies |
| The first participant relocked by a failed evolved review | +5 | Once per firing; budget applies |
| Failed evolved reviews have relocked at least a quarter of the firing's participating countries | +5 | Once per firing; a country counts once however often it relapses; budget applies |
| The whole firing cohort is restored by legitimate compliance after a positive manifestation | -5 | Once per firing; no credit when disappearance, manual clear, settings cancellation or invalid succession caused apparent completion |
| Continued excess, optional demobilization, evolution eligibility, activation, logging or review-credit allocation | 0 | Duration and status are not fresh disruptions; no per-unit reward |
| Ordinary conquest, battle deaths, construction or population growth | 0 from Event 096 | Shared systems already own those causes |

A country whose editing was already unavailable through another registered country-wide owner does not count as newly deprived merely because Event 096 adds another hold.
Retaining another owner's lock after Event 096 compliance is not an attributable restoration of access.

Restoration is evaluated through maintained completion receipts, not a recurring global army scan.
If a genuine repeat replaces an unfinished grant, retire that grant's unfinished restoration eligibility without a negative award and preserve any Chaos already paid.
The replacement grant can qualify independently only through its own manifestation and full legitimate completion.
Political succession carries a country's relapse-counted status to its successor and branches, so a split cannot produce a second first-relapse contribution, and a vanished country or invalid successor disqualifies the restoration credit.

The positive window cap prevents rapidly repeated selections or deliberate relock cycles from driving the world through several Chaos tiers.
The once-only negative credit and its positive-manifestation prerequisite prevent demobilization clicks, toggles, and empty cohorts from farming Chaos reduction.

## 6. Required named policy scenarios

The core matrix includes peaceful small and large countries at the same relative excess, a threatened country without a war, an ongoing war, a capitulated actor, a rapidly growing industrial base, another lock owner, zero eligible units, protected Event 019 units, robot and rat armies, a last-unit case, repeated dispatches, all evolution transitions, settings changes, and save/load in every posture.

For each, record the actual complete pool, source revision, F and A, raw e and capped E, N_owned, k, T/G/O, posture baselines, pending request, owner receipts, due day, and external AI modifiers.
Score rankings can be checked arithmetically, but claims about actual probability require the native inspect, evaluate, sweep, and compare workflow.
Sequence analysis must distinguish sticky retain from successive separately selected demobilization actions.
