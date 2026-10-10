# Event 101: Rewards, failure and evolutions

## Quote the consequence before the commitment

Each assignment selects a complete outcome package. Its reward and penalty are related to the task, scaled from the committed country and workload, and shown before the player starts pursuing it. The resolver does not draw a second random reward after success.

The task's ordinary result has at most two material channels: a temporary benefit or setback and, where appropriate, a bounded experience, political or confidence adjustment. The task does not award another permanent currency. Temporary effects can be strong because they require a real commitment and expire.

The quoted package uses the current legal native modifier or owner effect that actually represents the intended benefit. Modifier names in this specification are semantic directions. The implementation must verify the exact engine keys, scope, sign and stacking behavior before wiring them.

## Outcome grades

Use three internal quote grades. They are not another player-managed score. The native tooltip can convey the task's actual stakes without exposing the calculation.

| Grade | Qualification | Typical payoff scale |
| --- | --- | --- |
| Standard | A meaningful baseline task within the ordinary capacity budget | Strong short-term benefit matching the work |
| Demanding | Higher Stakes is active, or the task has a verified larger or pressured commitment | Larger benefit and stronger bounded failure |
| Exceptional | Chaos Tasks is active and the task resolves a substantial live episode or comparable difficult commitment | Major temporary benefit with a longer useful window |

An evolution does not automatically make a trivial task Exceptional. Actual workload, exposure, uncertainty and contribution must support the grade. A late easy delivery in a nearly resolved crisis remains a small or ineligible task even at Chaos 800.

Let `D` be the original task duration in days. The initial benefit duration is `ceil5(clamp(60, 150, 30 + 0.5 × D))`. A verified pressured task can add 25 percent, rounded up to five days, with a final ceiling of 180 days. The initial penalty duration is `ceil5(clamp(30, 90, 20 + 0.25 × D))`.

The percentages and ceilings below are design tuning anchors. The actual workload, affected country and duration create the scale. They are not claims of measured balance in the current engine.

## Reward packages

| Family | Standard | Demanding | Exceptional | Related secondary benefit |
| --- | --- | --- | --- | --- |
| Offensive | 10 percent improvement to the selected offensive or logistics capability | 15 percent | 20 percent | Relevant military experience scaled to the usable branch |
| Defensive | 10 percent improvement to organization recovery or another verified defensive preparation capability | 15 percent | 20 percent | Relevant military experience |
| Military preparation | 15 percent improvement to matching training, repair or branch preparation | 20 percent | 25 percent | Experience in the prepared branch |
| Industrial | 15 percent improvement to the chosen construction or production activity | 20 percent | 25 percent | No routine free factory or building |
| Diplomatic | 25 percent reduction in the matching diplomatic preparation or relation-maintenance burden | 35 percent | 50 percent | A bounded political-power return or a distinct owner-supported relation benefit |
| Crisis | The appropriate family package fitted to the owner outcome | A larger useful recovery package | Up to 30 percent in one justified recovery capability | At most one separate owner-approved secondary benefit |

For offensive tasks, a direct combat benefit is allowed only when the quote is valuable and bounded for the actual operation. A logistics objective should use supply or planning support. It should not always receive the same generic attack modifier. Defensive tasks should help the country recover and prepare after its successful protection window.

Preparation rewards match the branch. Air readiness receives air experience and the appropriate air preparation benefit. Naval readiness receives naval experience and a supported repair or preparation benefit. An army-production task uses army-related preparation. The reward does not create new equipment or unit types.

Scale the experience amount from relevant usable capacity. The starting formula is `round5(clamp(15, 50, 15 + 2 × F))`, where `F` is the number of relevant usable military factories or dockyards. A land country whose fielded forces exceed its domestic industry can use the larger of that value and one capacity unit per 25,000 qualified fielded manpower. Demanding multiplies the result by 1.5 and Exceptional by 2, then rounds to five with a final ceiling of 100 experience. Verify experience headroom before assignment. Do not quietly lose most of the quoted reward at the native cap.

If the relevant experience pool is nearly full, select a package with a longer useful temporary benefit before assignment and show that version. At resolution, a cap reached through subsequent play clamps the actual experience grant. The temporary component still pays. The report must not claim a larger actual grant than the engine applied.

For diplomacy, a political-power return is based on 10 to 30 days of the recipient's normal positive political-power income, rounded to five and capped at 150. It can repay part of a meaningful diplomatic commitment. It must not repay more than the task's independently valued cost when the task itself could be repeated through a reversible relationship loop.

Industrial success gives a useful temporary improvement rather than repeatedly spawning factories. Its value scales naturally with the economy benefiting from it. The task still measures a real project in a named place. A large national reward requires a correspondingly large useful commitment.

## Failure packages

Failure applies one principal bounded setback. A demanding failure may add a confidence loss when that fits the task and remains inside the country's existing crisis safety limits.

| Family | Principal consequence | Standard intensity | Demanding intensity | Exceptional intensity |
| --- | --- | ---: | ---: | ---: |
| Offensive | Reduced planning gain or command preparation | 10 percent | 15 percent | 20 percent |
| Defensive | Reduced military preparation, or political coordination under extreme battlefield pressure | 10 percent | 15 percent | 20 percent |
| Military preparation | Slower relevant training, repair or preparation | 10 percent | 15 percent | 20 percent |
| Industrial | Slower relevant construction or production programme | 10 percent | 15 percent | 20 percent |
| Diplomatic | Higher relation-maintenance burden or a task-specific relation setback | 25 percent burden | 35 percent burden | 50 percent burden |
| Crisis | One distinct administrative or recovery setback coordinated with the owner | Standard family limit | Demanding family limit | Exceptional family limit |

The normal task never imposes a direct army attack or defense reduction while the country is close to capitulation. It uses preparation or coordination effects, which matter without immediately deleting the ability to hold the front. This is a quote-time policy and a resolution-time safety check, not a new free cancellation.

Confidence loss, when used, is 5 percentage points of stability or war support for a Demanding task and at most 10 points for an Exceptional task. It never applies both. The task-specific loss is clamped so it does not push that value below 25 percent or through a higher documented owner crisis threshold that the task would itself trigger. A country already below the floor receives no further task-specific point loss. Its principal temporary setback remains.

A failure cannot directly transfer territory, spawn a hostile country, create a civil war, force a law or ideology change, delete a unit, wipe fuel, confiscate the whole stockpile or remove completed construction. These consequences would exceed an ordinary repeatable task's role. Underlying wars and crises can still have their own consequences independently.

The task and owner must not both charge the same consequence as though it happened twice. A crisis adapter records the owner's expected failure effects and the distinct incremental task effect. It checks combined native stacking at resolution. Where the owner already reaches the relevant safety floor, the task uses its prequoted distinct administrative channel or clamps the additional harm. It never surprises the player with a different severe penalty selected after failure.

## Useful incomplete work

The default partial-success threshold for divisible work is 60 percent of the required useful result, rounded up to the next complete work unit. A specific task can require a higher coherent threshold or a mandatory anchor. The exact condition appears in its initial tooltip.

Partial success gives no full reward. It removes the optional confidence loss and reduces the principal penalty duration to half, rounded up to five days with a minimum of 15. The principal intensity remains recognizable. This avoids producing tiny modifier fragments.

The player keeps useful buildings, produced equipment, delivered aid and captured territory because the campaign already owns those results. The task records the partial outcome separately. It does not claim the construction or aid was undone.

Strict protection, one-state capture and other indivisible tasks are binary unless their card names a useful intermediate result. Time spent attempting a task is not automatically useful partial work. A destroyed or returned result does not count toward the threshold at expiry.

## Deadline boundary and result order

The deadline is an exact stored day boundary in the task country's authoritative game clock. Work timestamped at or before the stored boundary can count. Work completed after it cannot be backdated by a later mission check.

At every potential terminal call, use this order:

1. Validate actor identity, human control and the current task generation.
2. Ingest fresh eligible owner or native evidence through the boundary.
3. Apply an irreversible strict-loss disqualification if the task's forbidden event occurred first.
4. Resolve full success if its complete timely predicate holds.
5. At expiry, resolve declared partial success if it holds.
6. Resolve ordinary failure, or the exact external cancellation cause when the objective was removed independently.

The implementation must verify native hourly and daily callback ordering. Owners whose success receipts can arrive late need a synchronous deadline query or a supported ordering guarantee. An already-resolved failure cannot be reopened by a stale success callback. A native timeout is a signal to check the current deadline, not permission to fail whichever new task happens to use the same mission ID.

## Rest, stacking and control changes

The ordinary post-resolution rest period is `ceil5(clamp(30, 90, 0.25 × original D))`. Success, partial success and ordinary failure all use it. It controls eligibility, while the shared repeatable scheduler still determines later firing.

Neutral cancellation gives no ordinary rest period or outcome effect. It preserves the consumed-offer signature and a reentry date no earlier than the original deadline. This prevents immediately reconnecting or invalidating the same offer to draw a replacement. It is an anti-reroll validity rule, not a hidden failure penalty.

At most one positive and one negative Event 101 temporary package may be active on a country. Keep each earned component with its own original magnitude and expiry. For an identical statistic and sign, apply the strongest component that is still live. When it expires, a weaker unexpired component may resume for its own remaining time. Never combine an old stronger magnitude with a newer expiry, add award durations together or erase an earned weaker component early. This rule affects only Event 101 effects, not unrelated native or crisis modifiers.

For example, a 20 percent benefit earned through day 100 and a later 10 percent benefit earned through day 140 produce 20 percent through day 100, then 10 percent through day 140. They never produce 20 percent through day 140. The implementation uses a small bounded private receipt collection and one native aggregate per sign.

Each sign exposes only one principal temporary capability at a time. For positive effects, the most recent unexpired award chooses the capability, then the strongest still-live component for that same capability applies. For negative effects, the highest unexpired quote grade chooses the capability, with the newest award breaking equal-grade ties. This prevents a small new failure from hiding an older Exceptional setback. The strongest live component for the selected negative capability then applies.

Other earned capabilities are suppressed, retain their original expiries and can resume only while still unexpired. They do not add together or receive extra time. The outcome tooltip explains this replacement rule and identifies the capability that would be active. A quote must have a useful live or later unexpired window. If the existing effects would mask its entire value, select a related valid quote or defer that candidate. Immediate experience and political-power grants still use their own one-time receipts within the two-channel outcome budget.

Changing human players within the same co-op country while at least one human remains does not reset the task. Losing all human control closes it neutrally and retires that active mission and subscription. Earlier settled rewards and penalties keep their legitimate expiries. Returning human control does not recreate the old reward opportunity or remove an earlier failure. Cosmetic country changes preserve the task. A new country object that reuses a tag does not inherit it.

## No task extensions

The selected design has no paid extension, deadline purchase or reroll button. The initial estimate includes setup, access, consolidation and uncertainty. Partial success recognizes useful work. Genuine external invalidity closes through its own rule.

This choice preserves the simple assignment-to-result loop and avoids a second time-purchase system. A future explicit design change could add an extension, but it would need its own accepted purpose, price, one-use receipt, owner deadline limit, native timer synchronization and updated achievements. The current package requires none of those actions or assets.

## Evolution I: Higher Stakes, 200+

**New behavior.** Future tasks can demand 25 percent more feasible work, choose a more significant local objective or require a longer useful consolidation interval. The generator must increase only the dimensions it can justify from the country's capacity. It recalculates the deadline and reward at the same time.

**Payoff and risk.** Qualified tasks use the Demanding outcome grade. The larger reward and failure are explicit. A country that cannot support the larger objective retains a smaller feasible task or becomes ineligible for that candidate. Higher Stakes never removes minimum reserves or practical access.

**Before first firing.** If the evolution is enabled and the shared pre-fire evolution rule activates it, the first assignment uses the evolved generator.

**While a task is active.** Record the evolution through the shared owner, but change only future assignments. Do not enlarge an existing required quantity or penalty.

## Evolution II: Trials Under Pressure, 400+

**New behavior.** The generator increasingly selects a task from a pressure already acting on the country. Existing wars, exposed positions, shortages, rebellions and recovery programmes receive the weight adjustments in Part 2.

**Payoff and risk.** Pressure can increase the benefit duration by 25 percent and support a Demanding grade. It does not multiply the workload again. Deadlines include the actual disruption, and ordinary failure retains the high-pressure safety policy.

**Before first firing.** The first task can be drawn from a real current pressure when enabled. A country at peace with no qualifying pressure still receives an ordinary feasible task.

**While a task is active.** A newly arising crisis does not replace the current objective. The active task can finish or close through its existing rules. The next firing evaluates the new situation.

## Evolution IV: Chaos Tasks, 600+

**New behavior.** Verified Chaos-owner tasks receive strong selection preference. The workload multiplier can reach 1.50 when Higher Stakes is also active. Unusual objectives remain tied to real owner actors, phases, weaknesses and response routes.

**Payoff and risk.** A substantial qualifying task can use an Exceptional quote. The temporary effect can be much stronger, but remains within the outcome and safety limits. An ordinary small task does not become Exceptional simply because the global Chaos value is high.

**Before first firing.** The initial task may use a registered eligible Chaos adapter. Missing or disabled owners contribute no candidate. The event must still have meaningful ordinary families when the campaign lacks a suitable active episode.

**While a task is active.** Preserve the existing task and quote. If its own crisis owner evolves, follow the owner's continuity contract. An equivalent continuing episode can retain its subscription. A genuinely replaced episode closes neutrally unless timely success was already earned. No larger task is imposed midway.

## Activation, toggles and history

The three evolutions use the shared enable controls and event-history framework. Initial MTTH tuning is 90 days after ordinary eligibility, adjusted through the actual shared evolution rules and current context. The exact source integration and timing evidence belong in the implementation handoff. Pre-first-fire intensity activation follows the shared rule rather than inventing a second delay.

Store separate stable internal identifiers for the supplied I, II and IV tracks. The catalog's Evolution IV field remains the 600+ design. No Evolution III text or invented stage is added. If the shared implementation needs a dense storage index, it must map that index explicitly to the public ordinal rather than silently renumbering the evolution.

Turning an evolution off prevents future evolved assignments under that track. An already committed valid task finishes under its quoted rules. Turning Event 101 off prevents new tasks. Existing tasks remain visible and settle unless a separately authorized global stop or human-authority loss requires neutral closure. A UI toggle cannot become a free reset of a difficult active task.

Assignment, evolution eligibility, evolution activation, task progress, ordinary construction, success, partial success and failure add zero direct Chaos in this design. Wars, casualties, owner crises and other actual world changes continue through their existing Chaos sources. Event 101 does not log those changes again.
