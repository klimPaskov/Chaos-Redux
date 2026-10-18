# Demilitarization: army cohesion and desertion

Desertion must change the strength of real fielded divisions. The player should be able to inspect the affected formation and see the result. Severe spontaneous demobilisation can remove a formation, but it must never masquerade as combat deaths or a generic deduction from the national manpower pool.

All labels are working design labels, not final localisation. The values below are initial balance targets. Their consequences must survive implementation validation.

## One public value

Army Cohesion is the only persistent event-specific public value. It runs from 0 to 100 and appears as a number, a qualitative band, and the main current cause of strain.

Show native facts such as current army size, remaining legal states, and the next review date as ordinary status. They are not additional event scores. Keep selection weights, loss budgets, cooldowns, and personnel-return receipts internal.

Initial cohesion is 75. Subtract 5 when fewer than one third of controlled states remain usable for deployment and subtract a further 10 for a Total opening. The starting floor is 50. Existing mutiny, low stability, and low war support influence subsequent reviews rather than causing an invisible extra opening deduction.

| Cohesion | Working band | Review incident chance | Maximum partial loss from one selected division | Country incident personnel budget |
| --- | --- | ---: | ---: | ---: |
| 70–100 | Orderly service | 10% | 2% of its actual present manpower | 0.25% of eligible fielded manpower |
| 45–69 | Strained service | 35% | 5% | 0.75% |
| 25–44 | Widespread departures | 65% | 8% | 1.5% |
| 0–24 | Formation breakdown | 90% | 12% | 3% |

These are conditional review probabilities. A successful incident spends its country personnel budget across valid selected formations. Per-formation limits bound concentration. They do not multiply the country's total budget.

## Review rhythm

A country receives one review after each 14 accumulated peacetime days. Its first review is 14 peacetime days after local enrolment. There is one current review identity per country.

At war entry, save the remaining interval. At last-war peace, resume that remaining interval. Duplicate callbacks and save loading must not advance the clock. A pending review revalidates the country's existence, current war state, and target army before it can commit a loss.

Apply cohesion changes before determining the current band for that review:

| Current condition | Cohesion change per review |
| --- | ---: |
| Under the active Desertion Crisis | −3 |
| Fewer than one third of controlled states are usable | −3 |
| Total Demilitarization active locally | −3 |
| Native stability below 40% | −2 |
| Native war support below 25% | −2 |
| Existing relevant mutiny or military-collapse crisis | Up to −4, combined maximum |
| Stability at least 60%, war support at least 35%, usable space at least one third, and no linked military crisis | +4 |
| Active service-conditions programme | +4 |
| Ordinary review deductions above | Subject to the 12-point combined negative cap |

The combined ordinary negative review adjustment is capped at 12 before programme gains. Do not count several labels for the same outside crisis as separate penalties. The stability, war-support, and space factors are conditions with existing game meaning.

An orderly country with room and good national conditions can stabilise without permanent expenditure. A cramped country under Total needs sustained choices. Consolidation can temporarily improve cohesion, while the geographic pressure remains.

Round and clamp cohesion only after the full adjustment. The player sees the dominant causes and can inspect all active contributors in a tooltip.

## Which soldiers are at risk

Use divisions whose legitimate personnel owner is the peaceful country. They must exist, contain actual soldiers, and be under a verified ownership relationship. Include domestic fielded formations, including those relocated by the territorial rule.

Exclude a division actively fighting, trapped in combat, being transferred through an unresolved ownership operation, or controlled through a foreign expeditionary arrangement whose personnel accounting cannot be resolved safely. Volunteer and expeditionary cases must be evaluated through actual ownership and combat context, not the current event ROOT.

An excluded division does not make the entire owner immune. The remaining eligible army is still reviewed. The visible report must not claim the excluded troops deserted.

Recruitment queues, unfielded manpower, air wings, and ships are not substitutes for fielded-division targets. A garrison manpower statistic alone is also insufficient.

### Cohort size and selection

At the review's commitment point, snapshot eligible fielded manpower and calculate the band's country budget in whole soldiers, rounded down. The budget is independent of division count.

Select without replacement, weighted by actual present manpower. A formation specifically marked by an existing compatible military-crisis owner receives a relative factor of 2. Use at most that one factor, even if several owners describe the same formation. Other descriptive circumstances do not add unnamed weights. Crowding already affects country cohesion and does not add a uniform multiplier that would cancel within the selection pool.

Apply up to the band's per-formation cap, then continue selecting valid formations until the country budget is spent or the eligible pool is exhausted. The last selected formation takes only the remaining budget. Do not impose a separate one, three, or six division ceiling. Splitting the same soldiers among more divisions changes traversal and distribution, not the intended total personnel loss.

Use actual present manpower rather than template capacity. A partial loss cannot reduce a formation below 60% of its manpower at the start of the current review. Full dissolution uses its separate process.

Calculate every unit percentage cap from that same committed review snapshot, rounded down to whole soldiers. Also preserve at least the ceiling of 60% of its start-review manpower. The applied debit is bounded by the remaining country budget, that unit cap, and its current actual personnel above the protected floor. Rounding remainder can pass only to still-valid unvisited candidates in the same incident. If no candidate can accept one soldier, close with the remainder unspent. The budget is division-count invariant, while exact realised equality remains subject to indivisible soldiers, eligible targets, and native proof.

Preserve a bounded continuation if the roster exceeds the engine's loop capacity. Every physical unit debit has its own child receipt under the same country incident. A callback never rerolls the country incident or refreshes its budget.

Small rounding results below one soldier produce no physical debit and no consequential credit. If a target disappears or changes ownership before commitment, skip it and continue only through still-valid unvisited candidates. Unspent budget expires when the review closes or war begins. Do not carry it into a later review or use the vanished target's receipt for another formation.

### Formation age and continuity

For decisions and achievements, a mature formation has at least 60 continuous days of verified service identity under the legitimate owner. Cadre retention uses a shorter 28-day minimum. Use native creation history when trustworthy, otherwise count from the first recorded observation as a conservative lower bound.

Renaming preserves the same genuine identity. A split, merge, reconstruction, or foreign transfer must not fabricate age or copy one formation's achievement identity to several units. Until a native continuity rule is proven, a new resulting identity starts its own observed age. This is part of GATE-05, not a nominal name comparison.

## Personnel and equipment accounting

Deserters and spontaneously demobilised soldiers are alive. They leave the fielded army and are temporarily unavailable for organised service. A measured personnel debit creates a matching Event 114 return obligation for 90 calendar days later.

The return obligation uses exactly the actual personnel removed. It does not use the requested amount, template maximum, theoretical missing strength, or a second population calculation. After 90 days, the same measured number can re-enter the country's recruitable manpower once. Reinforcement then follows the normal game process.

A partial desertion leaves equipment with the surviving formation. It does not create equipment in the national stockpile, delete gear by percentage, or add compensating equipment.

For a full spontaneous dissolution, all actually present personnel enter the same delayed return system. Recover 80% of the formation's actual equipment to its legitimate stockpile, with 20% lost as unaccounted service property. Rounding and equipment variants must preserve accounting. The original formation and its accumulated experience are gone.

For each discrete actual equipment variant, recover its actual count multiplied by 0.8 and rounded down. Record the rest of that same count as unrecoverable. Never transfer a rounding remainder into another variant or create a more valuable model to approximate the percentage. Verify the native unit of account before applying this integer rule to any fractional native holding.

A voluntary consolidation is different. It returns the actual personnel and equipment through the ordinary verified disband semantics immediately, with no Event 114 delayed return. The player deliberately sacrifices the formation's independent existence and experience.

| Outcome | Fielded army | Recruitable manpower | Equipment | Deaths and civilian population |
| --- | --- | --- | --- | --- |
| Partial desertion | Measured loss from selected formations | Matching return after 90 calendar days | Stays in surviving formation | Unchanged |
| Spontaneous full dissolution | One eligible formation disappears | Actual personnel return after 90 days | 80% actual recovery, 20% actual loss | Unchanged |
| Voluntary consolidation | Selected legitimate formation disbands | Native actual immediate refund | Native actual immediate refund | Unchanged |
| War entry | No restored personnel or recreated formation | Due receipts retain their dates | No compensation grant | Unchanged |

The implementation must prove a native path that changes actual fielded manpower without turning the departure into a combat casualty or duplicating a native refund. A manpower-pool deduction, recruitment modifier, attrition penalty, or generic organisation hit is not the specified effect.

A country-succession transaction must settle each pending return exactly once. Preserve the original debtor identity and a verified successor where one exists. If native annexation already transfers the same manpower entitlement, mark that entitlement consumed instead of paying it again. An unresolved succession recipient remains quarantined for reconciliation, with no speculative grant to a random surviving country.

Personnel-return receipts are military service accounting. They do not call the civilian population-transfer ledger or the civilian Deaths helper.

## A formation begins to dissolve

A whole-formation crisis requires all of the following:

- Cohesion has been below 25 at two consecutive completed reviews.
- An eligible formation represents at most 20% of current eligible fielded manpower.
- At least one other eligible fielded formation will remain.
- The country has not suffered an Event 114 spontaneous dissolution in the previous 56 accumulated peacetime days.
- No other endangered-formation notice is already open.

Select one eligible formation using the same manpower-weighted basis. Open a 14 peacetime-day muster mission. The report identifies the formation and observable failures of attendance. It gives the player the concrete deadline and response conditions without labelling the prose as a warning.

The notice does not itself remove soldiers or generate Chaos. The formation can still suffer an ordinary partial incident within the national review ceiling.

The player can resolve the notice by completing the cadre programme for that formation or by reaching cohesion 35 and maintaining a valid formation through the due check. Voluntary consolidation also closes the notice, but receives only its own intended outcome and never a spontaneous-loss recovery credit.

At the due check, a valid cadre completion or cohesion of at least 35 resolves the notice successfully. If the valid target remains and cohesion is 25–34, the muster fails without a dissolution roll. If cohesion is below 25 and every target condition remains valid, the failed muster causes one 25% dissolution roll. Settle the −5 cohesion failure cost once after this classification, outside the ordinary review's 12-point cap. The cost itself cannot move a 25–34 result into a new dissolution roll. The result does not immediately create another notice.

Every failed muster that leaves the formation intact, including the 25–34 case, ends the current notice and grants a 28 peacetime-day notice cooldown. This produces tension without repeated instant retries against the same unlucky unit.

### Interrupted notices

War pauses the remaining notice interval. A notice cannot dissolve a formation while its country is at war. After peace, the target must still be a legitimate eligible unit and the country must still meet the severe-state conditions.

If the target dies in combat, voluntarily disbands, merges, transfers owner, or disappears through another event, close the notice with the true disposition. Do not replace it silently with a fresh target at the same deadline.

A control or location change alone does not reset the clock. Save and load preserves both the target identity and the already committed random outcome, if one exists.

## Service-condition idea family

Use one staged idea family. Replace its current form rather than stacking three spirits.

| Current cohesion | Idea direction and starting mechanical burden |
| --- | --- |
| 45 or more | Uncertain service routines. Army organisation −10% and training time +15% while the peacetime crisis is active. |
| 25–44 | Departures disrupt formations. Army organisation −20% and training time +25%. |
| Below 25 | Officers cannot rely on formation attendance. Army organisation −30% and training time +35%. |

These penalties supplement actual personnel losses. They never serve as their replacement.

At war, suspend the Event 114 service penalties immediately. Retain the underlying cohesion and personnel history. On return to peace, select the correct form from the preserved value after the current state is revalidated.

The idea tooltip explains that soldiers already lost do not return merely because wartime penalties disappear. Actual personnel returns continue on their own calendar dates.

## An empty or temporarily ineligible army

If no eligible fielded formation remains, retain cohesion, history, cooldowns, pending returns, and remaining review time. Cancel programmes whose required army or target no longer exists. No empty-pool incident, automatic recovery award, or renewed-pressure shock occurs. Clear consecutive-severe and clean-review streaks when the eligible army becomes empty. Empty time cannot accumulate danger or recovery credit.

A country that previously had an enrolled army resumes from that preserved cohesion when eligible forces return. It does not receive another initial 75. A country that has never had an eligible army receives its one initialisation on first valid enrolment. Use native army-change notifications where verified, supplemented by one guarded country-local quiet check every 14 calendar days for already registered empty-army actors. This check never iterates the world and does not advance the frozen review interval.

A revived country identity retains its prior 114 history and consumed receipts where identity continuity is verified. A new successor can have its own initial service condition while any transferred personnel obligations remain single-owner transactions.

## Recovery

Two consecutive clean reviews at cohesion 70 or more establish a stable service period. A clean review has no Event 114 partial debit, spontaneous dissolution, or unresolved endangered-formation notice.

The player may then pursue the longer containment and achievement goals. This status does not clear the territorial rule or delete the loss history. A future repeat or deterioration can create another service problem without pretending that the previous one never happened.

Recovery rewards depend on actual earlier losses and sustained service. Deliberately constructing and disbanding sacrificial units cannot create a spontaneous-loss receipt, a Chaos reversal, or an achievement shortcut.

