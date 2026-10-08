# Event 096: evolutions and inspection waves

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

## 1. Shared rules

The four supplied evolution names and Chaos requirements are retained. They modify one coherent system. Every regime uses the same structural force, live capacity, optional decisions, release predicate, lock ownership, and safe transaction.

Chaos thresholds make an active evolution eligible. They are not deadlines or automatic active-event upgrades. A pre-fire evolved opening and an evolution during an ongoing incident are separate entry paths.

Ordinary lifecycle transitions, including the end of the minimum week, becoming oversized, demobilizing, unlocking, and passing an inspection, are not evolution stages.

| Regime | Chaos eligibility | Allowance multiplier | Future reviews granted by one firing | Relock condition during a review |
| --- | ---: | ---: | --- | --- |
| Base | Base event eligibility | 1.00 | None | A new genuine firing is needed |
| I: Stricter Limits | 200+ | 0.85 | None | Same as base |
| II: Military Reinspection | 400+ | 0.80 | One | F greater than 1.25A and F at least 1.15 times the watch baseline |
| III: Rolling Restrictions | 600+ | 0.70 | Three, plus one if peak excess is at least 1 | F greater than 1.15A |
| IV: Global Demobilization | 800+ | 0.55 | Four, plus up to two from the integer part of peak excess | F greater than 1.05A |

Peak excess is the highest raw e observed during the current firing's country episode. It is not capped for recordkeeping. Define B_base = B_I = 0, B_II = 1, B_III = 3 + indicator(peak e at least 1), and B_IV = 4 + min(2, floor(peak e)). The indicator is one when true and zero otherwise. Thus Evolution III grants three or four reviews, and Evolution IV grants four, five, or six.

These are bounded inspection budgets, not fixed lock durations. A country may remain in its first lock much longer than the entire review program because its force remains above allowance. No review deletes a unit automatically.

## 2. Both entry paths

### Pre-fire evolved opening

At a genuine firing, determine the highest enabled regime whose threshold is satisfied by current Chaos. Enter that regime directly. Historical activation from an already closed grant does not bypass a current threshold. An 800+ opening therefore applies the Evolution IV allowance and future-review contract from the start. It does not wait through four long upgrade timers before delivering its high-Chaos version.

If a prior grant is still active, preserve any stricter already activated and still-enabled regime when the repeat coalesces that obligation. The repeat uses the higher of that retained regime and the current-Chaos opening regime. This is continuity of an existing active restriction, not permanent cross-incident evolution memory. The shared registry may retain historical records without changing this mechanical selection rule.

The opening still affects every current country, starts a seven-day floor, and preserves the fielded army. Deliver one coherent opening report describing the current regime. Register inherited lower-stage progression according to the shared evolution registry, without multiplying the allowance reductions or producing four redundant country popups.

### Active-event evolution

While at least one valid participant is locked or in an evolved watch, an enabled next stage can become eligible at its Chaos threshold. Use the project's active evolution MTTH route with a 90-day tuning anchor. The final installed-version adapter must establish the actual timing distribution. Do not present ninety days as a guaranteed wait or a measured native mean.

Advance at most one new active stage in a single evolution completion. A sudden Chaos jump can make later stages eligible but does not execute an unreviewed cascade in one callback. The direct pre-fire opening already supplies the high-tier immediate route.

Initial dynamic MTTH factors are:

| Condition | Factor on the 90-day anchor |
| --- | ---: |
| At least half of the firing's recorded entry-force weight is currently in an oversized hold | 0.75 |
| At least one active participant currently has e at least 1 | 0.75 |
| Current Chaos is at least 200 above the next stage's threshold | 0.80 |
| No participant remains oversized, but a valid evolved watch remains | 1.50 |

Combine applicable factors and bound the final factor between 0.25 and 2. These are candidate MTTH factors for native audit. Entry-force weights are fixed historical weights for this pacing input. The current held or oversized status comes from participant refreshes. Do not relabel this aggregate as a live world military-strength census.

If the threshold ceases to be satisfied, stop eligibility for an unactivated stage. Activated regimes do not regress merely because Chaos drops. An explicit settings change can disable their effects under Section 7.

Activation tightens the allowance for currently held participants on their next guarded immediate or local refresh. It invalidates requests based on the old regime. A previously released cohort participant is not instantly relocked by the activation callback. A newly added reinspection capability first opens a genuine watch window with a fresh baseline and delay.

If every participant has finished and the director has closed, an old queued evolution cannot resurrect the incident. A later firing can use a new evolved opening.

## 3. Evolution I: Stricter Limits

The first evolution reduces the generosity of the capacity calculation to 85 percent. The floor remains seven days. A country that was near compliance can now have a larger gap to close, while a powerful country still receives a much larger allowance than a minor.

For an active country, refresh the allowance immediately through the existing country route. If its minimum week has ended and it is still compliant, release it. Do not impose a new week solely because the coefficient changed. If it is oversized, retain the current hold and show the changed allowance.

For a pre-fire opening, apply the stricter allowance from the first comparison. This evolution has no post-release watch. Its harsher duration follows the larger live capacity gap. It does not add an arbitrary extension timer.

Narrative direction: a revision of inspection standards that makes previously tolerated establishments harder to justify. The evolution log should communicate the standards change. Its activation or log has zero direct Chaos effect.

## 4. Evolution II: Military Reinspection

The second evolution reduces the multiplier to 80 percent and grants one delayed review after release. It targets rapid rebuilding far beyond current capacity.

At the start of a watch window, record F_watch as the actual current force and record the start day. For a normal release, that is the release-day force. If this capability is activated after a country had already finished its initial hold, use its force at the new watch's activation. Do not treat months of earlier ordinary growth as rapid expansion inside a newly created window.

At the review, refresh F and A. Relock only if both F is greater than 1.25A and F is at least 1.15 times F_watch. A country that is slightly above allowance but has not crossed both conditions avoids a renewed hold. A capacity loss alone does not satisfy the rapid-growth condition in this regime.

The distinction is intentional. A currently held country can release only at F at most A. An already released country has a separate, higher reacquisition threshold. The latter is not permission to release a held country at 1.25A.

Whether it passes or fails, the review consumes its single credit. A failure starts a new seven-day hold, then releases through the ordinary compliance predicate. The same credit cannot schedule another review after that release.

Narrative direction: provisional restoration of design access followed by a check for rapid rebuilding. The player should understand the difference between being unlocked now and the watch still being active.

## 5. Evolution III: Rolling Restrictions

The third evolution reduces the multiplier to 70 percent and permits three or four future reviews for the current firing. The extra review reflects a country whose peak force reached at least twice its allowance.

Reviews now compare current capacity directly. Relock when F is greater than 1.15A, even if the deterioration came from lost land, population, or factories rather than new formations. A country can pass some reviews, fail another after a defeat, and later recover through growth or voluntary demobilization.

A passed review consumes a credit and begins the next watch if credits remain. A failed review consumes a credit and returns the country to a minimum-week hold. Remaining reviews wait until it unlocks again. An oversized locked country does not burn through its review budget while waiting for compliance.

Narrative direction: recurring inspections that different countries pass or fail according to their own circumstances. The evolution does not create synchronized global unlock dates or synchronized relock waves.

## 6. Evolution IV: Global Demobilization

The final supplied evolution reduces the multiplier to 55 percent and permits four to six future reviews. It uses a narrow five-percent relock margin and shorter watch intervals.

The event can now keep a country's establishment frozen through long stretches of war and rebuilding. It still does not compel administrative disband, destroy a surviving army, force a peace treaty, or levy an unrelated resource tax. A country that can materially support its force can still satisfy the current calculation.

Narrative direction: relentless international or anomalous military scrutiny, with the contrast between frozen establishment documents and continuing operations. Preserve the event's administrative identity and restrained presentation rather than introducing a separate catastrophe mechanic.

## 7. Watch timing, credits, and settings

At each watch start, compute the delay from the selected regime and the current firing's peak excess, capped at two for this timing input:

| Regime | Delay in game days |
| --- | --- |
| II | Ceiling of `clamp(30 / (1 + min(peak e, 2)), 10, 30)` |
| III | Ceiling of `clamp(24 / (1 + min(peak e, 2)), 8, 24)` |
| IV | Ceiling of `clamp(15 / (1 + min(peak e, 2)), 5, 15)` |

The due day is watch-start day plus that computed delay. Do not recompute it as today plus delay on each refresh, which would push the appointment forward forever. A later active regime may bring an existing review forward according to its original watch start, but never earlier than the next game day. A newly opened watch always receives its full fresh delay.

Consume one credit before resolving each actual review. Keep a per-firing count of spent reviews. When a higher regime or a higher observed peak increases that firing's target B, remaining credits become the greater of the old remaining credits and B minus already spent credits, bounded below by zero. A relapse does not reset the budget.

A genuine repeat firing gives a new grant and a new current-state target. Its pending future review count becomes the greater of the old remaining count and the new target, not their sum. The repeat starts or renews the country lock and pauses watches. Old callbacks cannot spend or restore credits belonging to the new grant. Historical spent-review records used by achievements and anti-farm guards remain distinct from the new operational counter.

Disabling evolutions removes effects of disabled stages and cancels reviews that no enabled active regime supports. Recalculate A under the highest still-enabled applicable regime, or base if none remains. Keep a running seven-day floor. If the country is then compliant and its floor has elapsed, release it.

Re-enabling a stage during the same still-active director uses preserved spent-credit receipts, not a fresh free grant. Re-enabling after full closure waits for a new firing. An explicit clear-active-effects operation retires all Event 096 watches and holds without compliance rewards.

### Political succession, splits, and mergers

A verified successor inherits the original firing lineage, regime, observed peak, target, spent-credit history, and remaining obligation. A split may carry the outstanding local obligation into each legitimate continuing branch, including a surviving predecessor, but every branch starts with the predecessor's already-spent history. It does not receive a new grant or a reset review budget. Copy consumed receipt identities so delivery of an old callback cannot repeat an already resolved review.

An inherited watch keeps its original start and absolute due day. Preserve its Evolution II baseline through Part 5's force partition, rather than replacing it with a fresh current-force baseline that forgives growth already observed inside the watch. An inherited hold receives Part 1's first-application floor. Once it legitimately releases, any remaining review starts a normal new watch.

For a merger, keep the strictest still-applicable active regime and the maximum remaining count rather than summing counts. If any merged obligation is held, hold the resulting actor, keep the latest unexpired inherited floor, and also apply a fresh seven-day floor if this is that actor's first hold. Otherwise retain the earliest pending watch appointment. A held actor pauses any retained watch appointment until release, after which one normal watch begins. Keep one logical evaluator and one future watch chain.

Underlying lineage and consumed-credit receipts remain distinct even when multiple grants merge into one operational maximum. Do not reconstruct them from a guessed sum of spent counters. A later regime target can add only the unspent amount justified by its own retained lineage, then coalesces through the maximum rule. Disjoint historical weights and compatible watch baselines combine once, under Part 5. None of these transfers is a new Chaos manifestation or a new achievement attempt.

The actual political or provider transaction must identify the relationship and provide a complete transfer snapshot. No generic successor getter or native transfer hook has been proved here. If that adapter cannot meet these rules, the affected portion of G3 remains blocked. No speculative transfer may authorize removal, attribution, or successful restoration.

## 8. Consequences and connections

Military Madness can improve combat performance while the establishment remains frozen. It does not inflate the allowance through a combat-strength variable. If it changes real template structure or grants units, F follows that change.

The Offensive can make the AI want to retain its army and pursue growth. Event 096 does not override another event's strategic identity by forcing it to demobilize. Its war and security veto in Part 5 keeps the AI from random army liquidation during a survival conflict.

Territorial, population, industrial, and army-grant events need no hardcoded pairwise allowance bonus. They change the same live inputs. Provider callbacks are useful for prompt refresh, but a bounded local reconciliation must also catch changes that lack a specific callback.

Each actual renewed hold can contribute to the bounded Chaos consequence policy in Part 5. Eligibility, stage activation, logging, credit allocation, a passed inspection, and simply staying above the limit give no direct Chaos by themselves.
