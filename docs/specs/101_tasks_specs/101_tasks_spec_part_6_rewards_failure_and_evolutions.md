# Event 101: Rewards, failure and evolutions

## Quote the consequence before the commitment

Each assignment selects a complete outcome package.
Its reward and penalty belong to the task's own subject, are scaled from the committed country and workload, and are shown before the player starts pursuing the task.
The resolver does not draw a second random reward after success.

The ordinary result has one signature temporary effect and, where it fits, one one-time grant such as experience, political power or a bounded confidence adjustment.
The task does not award another permanent currency.
Temporary effects can be strong because they require a real commitment and expire.

The quoted package uses the current legal native modifier or owner effect that actually represents the intended benefit.
Modifier names in this specification are semantic directions.
The implementation must verify the exact engine keys, scope, sign and stacking behavior before wiring them.

## What makes a reward felt

A quote is accepted for a task only when it passes these checks.

1. The reward acts on the system the task was about. A construction task speeds construction, a supply task improves supply and a relief task makes relief cheaper. A generic attack or production bonus is never the default.
2. The reward has a live consumer at quote time. The country has queued construction, a running production line, an active front, an available relief action or whatever else the effect will touch within its first 30 days. Otherwise the generator picks another valid quote or defers that candidate.
3. The reward is strong enough to change what the player does next. The scale anchors below set the minimum. A one or two percent nudge is never a reward.
4. The reward does not repeat what the underlying system already paid. Captured territory, built factories, delivered aid and owner recovery stay with their owners.

A setback follows the same subject and passes the same live-consumer check, so the player feels it at the next relevant decision.
The setback never destroys completed work.

## Outcome grades

Use three internal quote grades.
They are not another player-managed score.
The native tooltip conveys the task's actual stakes without exposing the calculation.

| Grade | Qualification | Typical payoff scale |
| --- | --- | --- |
| Standard | A meaningful baseline task within the ordinary capacity budget | Strong short-term benefit matching the work |
| Demanding | Higher Stakes is active, or the task has a verified larger or pressured commitment | Larger benefit and stronger bounded failure |
| Exceptional | Chaos Tasks is active and the task resolves a substantial live episode or comparable difficult commitment | Major temporary benefit with a longer useful window |

An evolution does not automatically make a trivial task Exceptional.
Actual workload, exposure, uncertainty and contribution must support the grade.
A late easy delivery in a nearly resolved crisis remains a small or ineligible task even at Chaos 800.

Let `D` be the original task duration in days.
The initial benefit duration is `ceil5(clamp(60, 150, 30 + 0.5 × D))`.
A verified pressured task can add 25 percent, rounded up to five days, with a final ceiling of 180 days.
The initial penalty duration is `ceil5(clamp(30, 90, 20 + 0.25 × D))`.
The percentages and ceilings are design tuning anchors, not measured balance.

## Scale anchors

One table sets the magnitude of the signature effect for each family and grade.
The next section names the effect for each card.

| Family | Reward Standard | Reward Demanding | Reward Exceptional | Setback Standard | Setback Demanding | Setback Exceptional | One-time grant |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Offensive | 10 percent | 15 percent | 20 percent | 10 percent | 15 percent | 20 percent | Relevant army experience |
| Defensive | 10 percent | 15 percent | 20 percent | 10 percent | 15 percent | 20 percent | Relevant army experience |
| Military preparation | 15 percent | 20 percent | 25 percent | 10 percent | 15 percent | 20 percent | Experience in the prepared branch |
| Industrial | 15 percent | 20 percent | 25 percent | 10 percent | 15 percent | 20 percent | None, no routine free factory or building |
| Diplomatic | 25 percent | 35 percent | 50 percent | 25 percent | 35 percent | 50 percent | Bounded political-power return |
| Crisis | Fitted to the owner outcome | Larger recovery package | Up to 30 percent in one recovery capability | Family limit for the grade | Family limit for the grade | Family limit for the grade | At most one owner-approved secondary benefit |

Diplomatic percentages reduce the cost or burden of the matching diplomatic action.
Other percentages change the speed, throughput, efficiency or gain named for the card.

## Signature effect by card

Every card has its own reward and setback.
Cards in the same family therefore pay differently.
The table names the semantic effect and the decision the player feels.

| Card | Signature reward | Signature setback |
| --- | --- | --- |
| O1 Secure a front objective | The secured states gain compliance faster and repair their infrastructure faster | Slower offensive planning and command preparation |
| O2 Capture a key position | Better supply throughput in the position's region | Reduced experience gain for the army |
| O3 Open a corridor | Faster railway repair and higher supply throughput along the corridor | Slower railway repair on the front the corridor was meant to serve |
| O4 Defeat a hostile force | Faster organization recovery for the army that won | Slower organization recovery outside combat |
| D1 Hold a threatened state | Faster infrastructure repair and fortification work in the held region | Slower training of replacement units |
| D2 Preserve the seat of government | Faster political-power gain and stability recovery | Slower political-power gain, never a combat penalty |
| D3 Keep a route working | Higher supply throughput on that route | Slower repair of that route's links |
| M1 Field an equipped formation | Faster training of the next divisions | Slower training |
| M2 Produce military materiel | Faster production-efficiency growth for the produced category | Slower efficiency growth for that category |
| M3 Establish regional defenses | Faster fortification and anti-air construction in the protected region | Slower fortification construction in that region |
| M4 Make a branch ready | Faster repair and reinforcement for that air or naval branch | Slower repair for that branch |
| I1 Expand productive capacity | Faster construction of the same building type | Slower construction of that type |
| I2 Improve a regional bottleneck | Faster infrastructure construction and railway repair | Slower infrastructure construction |
| I3 Complete a supply improvement | Higher supply throughput near the supported front | Slower railway construction |
| I4 Strengthen a useful base | Faster construction and repair of the same port or airfield type | Slower base construction |
| P1 Establish working relations | Cheaper relation maintenance and improvement | Higher relation-maintenance burden |
| P2 Supply useful support | The partner's opinion of the recipient rises through the owning diplomatic system | Higher friction on further aid actions |
| P3 Protect a vulnerable partner | Cheaper guarantees and protective commitments | Higher cost for the same commitments |
| P4 Secure a cooperative arrangement | Cheaper alliance, access and support actions | Higher cost for those actions |
| L1 Relieve a famine state | Relief actions cost less political power | Relief actions cost more political power |
| L2 Settle displaced people | Faster local integration in host states | Slower local integration |
| C1 to C6 | The related recovery package fitted by the owner contract in Part 5 | One distinct administrative setback coordinated with the owner |

Rules that apply to the whole table.

- An offensive logistics objective uses supply or planning support and does not always receive the same attack modifier.
- Defensive failure uses preparation or coordination effects, never a direct combat-strength cut.
- Preparation rewards match the branch. Air readiness gives air experience, naval readiness gives naval experience, and army production gives army preparation. The reward never creates equipment or unit types.
- Industrial success never repeatedly spawns factories. The effect scales with the economy it benefits, and a large national reward requires a large useful commitment.
- A diplomatic reward must not return more than the task's independently valued cost when the task could be repeated through a reversible relationship loop.

## One-time grants

Scale the experience amount from relevant usable capacity.
The starting formula is `round5(clamp(15, 50, 15 + 2 × F))`, where `F` is the number of relevant usable military factories or dockyards.
A land country whose fielded forces exceed its domestic industry can use the larger of that value and one capacity unit per 25,000 qualified fielded manpower.
Demanding multiplies the result by 1.5 and Exceptional by 2, then rounds to five with a final ceiling of 100 experience.
Verify experience headroom before assignment, and do not quietly lose most of the quoted reward at the native cap.

If the relevant experience pool is nearly full, select a package with a longer useful temporary benefit before assignment and show that version.
At resolution, a cap reached through subsequent play clamps the actual experience grant.
The temporary component still pays, and the report must not claim a larger grant than the engine applied.

For diplomacy, a political-power return is based on 10 to 30 days of the recipient's normal positive political-power income, rounded to five and capped at 150.
It can repay part of a meaningful diplomatic commitment.

## Failure packages

Failure applies one principal bounded setback from the table above.
A Demanding or Exceptional failure may add a confidence loss when that fits the task and remains inside the country's existing crisis safety limits.

The normal task never imposes a direct army attack or defense reduction while the country is close to capitulation.
It uses preparation or coordination effects, which matter without deleting the ability to hold the front.
This is a quote-time policy and a resolution-time safety check, not a free cancellation.

Confidence loss, when used, is 5 percentage points of stability or war support for a Demanding task and at most 10 points for an Exceptional task.
It never applies both.
The task-specific loss is clamped so it does not push that value below 25 percent or through a higher documented owner crisis threshold that the task would itself trigger.
A country already below the floor receives no further task-specific point loss, and its principal temporary setback remains.

A failure cannot directly transfer territory, spawn a hostile country, create a civil war, force a law or ideology change, delete a unit, wipe fuel, confiscate the whole stockpile or remove completed construction.
Underlying wars and crises keep their own consequences.

The task and owner must not both charge the same consequence as though it happened twice.
A crisis adapter records the owner's expected failure effects and the distinct incremental task effect, and checks combined native stacking at resolution.
Where the owner already reaches the relevant safety floor, the task uses its prequoted distinct administrative channel or clamps the additional harm.
It never surprises the player with a different severe penalty selected after failure.

## Useful incomplete work

The default partial-success threshold for divisible work is 60 percent of the required useful result, rounded up to the next complete work unit.
A specific task can require a higher coherent threshold or a mandatory anchor, and the exact condition appears in its initial tooltip.

Partial success gives no full reward.
It removes the optional confidence loss and halves the principal penalty duration, rounded up to five days with a minimum of 15.
The principal intensity remains recognizable, which avoids tiny modifier fragments.

The player keeps useful buildings, produced equipment, delivered aid and captured territory because the campaign already owns those results.
The task records the partial outcome separately and does not claim the work was undone.

Strict protection, one-state capture and other indivisible tasks are binary unless their card names a useful intermediate result.
Time spent attempting a task is not partial work, and a destroyed or returned result does not count at expiry.

## Deadline boundary and result order

The deadline is an exact stored day boundary in the task country's authoritative game clock.
Work timestamped at or before the stored boundary can count, and work completed after it cannot be backdated by a later mission check.

At every potential terminal call, use this order.

1. Validate actor identity, human control and the current task generation.
2. Ingest fresh eligible owner or native evidence through the boundary.
3. Apply an irreversible strict-loss disqualification if the task's forbidden event occurred first.
4. Resolve full success if its complete timely predicate holds.
5. At expiry, resolve declared partial success if it holds.
6. Resolve ordinary failure, or the exact external cancellation cause when the objective was removed independently.

The implementation must verify native hourly and daily callback ordering.
Owners whose success receipts can arrive late need a synchronous deadline query or a supported ordering guarantee.
An already-resolved failure cannot be reopened by a stale success callback.
A native timeout is a signal to check the current deadline, not permission to fail whichever new task uses the same mission ID.

## Rest, stacking and control changes

The ordinary post-resolution rest period is `ceil5(clamp(30, 90, 0.25 × original D))`.
Success, partial success and ordinary failure all use it.
It controls eligibility, while the shared repeatable scheduler still determines later firing.

Neutral cancellation gives no ordinary rest period or outcome effect.
It preserves the consumed-offer signature and a reentry date no earlier than the original deadline.
This is an anti-reroll validity rule, not a hidden failure penalty.

At most one positive and one negative Event 101 temporary package may be active on a country.
Keep each earned component with its own original magnitude and expiry.
For an identical statistic and sign, apply the strongest component that is still live, and when it expires let a weaker unexpired component resume for its own remaining time.
Never combine an old stronger magnitude with a newer expiry, add award durations together or erase an earned weaker component early.
This rule affects only Event 101 effects.

For example, a 20 percent benefit earned through day 100 and a later 10 percent benefit earned through day 140 produce 20 percent through day 100, then 10 percent through day 140.
They never produce 20 percent through day 140.
The implementation uses a small bounded private receipt collection and one native aggregate per sign.

Each sign exposes only one principal temporary capability at a time.
For positive effects, the most recent unexpired award chooses the capability, then the strongest still-live component for that capability applies.
For negative effects, the highest unexpired quote grade chooses the capability, with the newest award breaking equal-grade ties, so a small new failure cannot hide an older Exceptional setback.
Other earned capabilities are suppressed, keep their original expiries and can resume only while unexpired.

The outcome tooltip names the capability that is active and explains the replacement rule in one line.
A quote must have a useful live or later unexpired window.
If existing effects would mask its entire value, select a related valid quote or defer that candidate.
Immediate experience and political-power grants use their own one-time receipts.

Changing human players within the same co-op country while at least one human remains does not reset the task.
Losing all human control closes it neutrally and retires that active mission and subscription.
Earlier settled rewards and penalties keep their legitimate expiries.
Returning human control does not recreate the old reward opportunity or remove an earlier failure.
Cosmetic country changes preserve the task, and a new country object that reuses a tag does not inherit it.

## No task extensions

The selected design has no paid extension, deadline purchase or reroll button.
The initial estimate includes setup, access, consolidation and uncertainty.
Partial success recognizes useful work, and genuine external invalidity closes through its own rule.

This choice keeps the simple assignment-to-result loop and avoids a second time-purchase system.
A future extension would need its own accepted purpose, price, one-use receipt, owner deadline limit, native timer synchronization and updated achievements.

## Evolution I: Higher Stakes, 200+

**New behavior.** Future tasks can demand 25 percent more feasible work, choose a more significant local objective or require a longer useful consolidation interval.
The generator increases only the dimensions it can justify from the country's capacity, and recalculates the deadline and reward at the same time.

**Payoff and risk.** Qualified tasks use the Demanding outcome grade.
The larger reward and failure are explicit.
A country that cannot support the larger objective keeps a smaller feasible task or becomes ineligible for that candidate.
Higher Stakes never removes minimum reserves or practical access.

**Before first firing.** If the evolution is enabled and the shared pre-fire evolution rule activates it, the first assignment uses the evolved generator.

**While a task is active.** Record the evolution through the shared owner, but change only future assignments.

## Evolution II: Trials Under Pressure, 400+

**New behavior.** The generator increasingly selects a task from a pressure already acting on the country.
Existing wars, exposed positions, shortages, rebellions and recovery programmes receive the weight adjustments in Part 2.

**Payoff and risk.** Pressure can increase the benefit duration by 25 percent and support a Demanding grade.
It does not multiply the workload again.
Deadlines include the actual disruption, and ordinary failure keeps the high-pressure safety policy.

**Before first firing.** The first task can be drawn from a real current pressure when enabled.
A country at peace with no qualifying pressure still receives an ordinary feasible task.

**While a task is active.** A newly arising crisis does not replace the current objective, and the next firing evaluates the new situation.

## Evolution IV: Chaos Tasks, 600+

**New behavior.** Verified Chaos-owner tasks receive strong selection preference.
The workload multiplier can reach 1.50 when Higher Stakes is also active.
Unusual objectives remain tied to real owner actors, phases, weaknesses and response routes.

**Payoff and risk.** A substantial qualifying task can use an Exceptional quote.
The temporary effect can be much stronger but stays within the outcome and safety limits.
An ordinary small task does not become Exceptional because the global Chaos value is high.

**Before first firing.** The initial task may use a registered eligible Chaos adapter.
Missing or disabled owners contribute no candidate, and the event must still have meaningful ordinary families when the campaign lacks a suitable active episode.

**While a task is active.** Preserve the existing task and quote.
If its crisis owner evolves, follow the owner's continuity contract.
An equivalent continuing episode keeps its subscription, and a genuinely replaced episode closes neutrally unless timely success was already earned.

## Activation, toggles and history

The three evolutions use the shared enable controls and event-history framework.
Initial MTTH tuning is 90 days after ordinary eligibility, adjusted through the actual shared evolution rules and current context.
The exact source integration and timing evidence belong in the implementation handoff.
Pre-first-fire activation follows the shared rule rather than a second delay.

Store separate stable internal identifiers for the supplied I, II and IV tracks.
The catalog's Evolution IV field remains the 600+ design, and no Evolution III is invented.
If the shared implementation needs a dense storage index, it maps that index explicitly to the public ordinal.

Turning an evolution off prevents future evolved assignments under that track, and an already committed task finishes under its quoted rules.
Turning Event 101 off prevents new tasks.
Existing tasks remain visible and settle unless a separately authorized global stop or human-authority loss requires neutral closure.
A UI toggle cannot become a free reset of a difficult active task.

Assignment, evolution eligibility, evolution activation, task progress, ordinary construction, success, partial success and failure add zero direct Chaos.
Wars, casualties, owner crises and other actual world changes continue through their existing Chaos sources, and Event 101 does not log them again.
