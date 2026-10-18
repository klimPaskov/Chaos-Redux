# Seeding, matches and championships

## 1. What the draw guarantees

Every accepted, still eligible entrant appears once in the locked competition tree.
Every advancement follows a link published at lock.
A result changes the identity occupying that link, never the graph itself.
The ordinary valid completion has one final winner, one ratified champion and one award receipt.
Exceptional closure can leave the title vacant or the edition interrupted, with no invented winner or reward.

The main draw supports 2, 4, 8, 16 and 32 slots.
A field of zero or one cannot form a competitive edition.
It closes as `insufficient_field`, releases remaining reservations and returns refundable unspent entry commitments according to the actual-payment ledger.
It does not award a title, count a defense or manufacture a defeated opponent.

All formulas and weights below are design anchors, not measured native balance.
The implementation must reproduce their declared semantics with verified engine operations and the probability checks in Part 06.

## 2. Ranking and published seeds

Compute each eligible entrant's seed score at roster lock from five normalized 0 to 100 inputs.

| Input | Weight | Meaning and protections |
| --- | ---: | --- |
| Recognized contender quality | 45% | Publicly established ability and credible scouting. It can underestimate an unknown talent and is distinct from the hidden exact match attributes |
| Recent form | 20% | Most recent actual contested results and dated fitness evidence. A bye is not a played win |
| Tournament record | 15% | Prior ratified edition performance, adjusted for opponent quality and sample size |
| Reputation | 10% | Bounded sporting standing based on real accomplishments and final sanctions |
| Preparation evidence | 10% | Completed legal preparation and readiness evidence, with diminishing returns and no direct multiplication by funding tier |

An entrant with no prior tournament record starts at a neutral 50 for the missing record input, not zero.
Unknown reputation starts at a neutral 50 unless authored prior career evidence supports another value.
Recent form uses an authored neutral baseline until actual dated evidence exists.
All three inputs have an evidence key so a later correction can identify what was used.
Title history cannot push the normalized inputs above 100.

Order by total seed score, then recognized quality, then recent form, then persistent wrestler ID.
The final ID tie break is deterministic and disclosed as administrative ordering.
It does not alter match attributes or probability.
The ranking routine receives one snapshotted entrant array and cannot make a different draw for a player country.

Every entrant receives an opening rank and corresponding original seed label for inspectability.
The narrative may call an unfamiliar low-ranked entrant unseeded or an outsider, but the interface retains their exact opening position.
Previous champions, national wealth and major status do not reserve a title route.
Organized corruption can distort the bounded pre-lock preparation or credential evidence only under Part 04's recorded scheme rules.
It cannot rewrite the published seed array after lock.

## 3. One tree for every field size

Let `N` be the final locked entrant count and `P` the smallest power of two at least `N`.
Create the balanced seed line for `P` leaves.
Start with `[1, 2]`.
When doubling a line of length `m`, replace each seed `s` with `[s, 2m + 1 - s]`.
Seed numbers greater than `N` are explicit empty leaves.

This puts seeds 1 and 2 in opposite halves, places the leading four in different quarters when quarters exist, and gives the highest seeds the necessary first-round byes.
The opening bracket contains no empty-versus-empty pairing under this construction.
Later double vacancies remain possible through actual withdrawals or disqualifications.

For `N <= 32`, this tree is the main draw.
For `N > 32`, the first `q = log2(P / 32)` levels are qualifiers and the remaining levels are the 32-slot main draw.
Every accepted applicant appears in the same immutable tree.
No separate allocation of 24 direct entrants and eight qualifier places is used.
The leading seeds receive fair byes where the tree requires them, not an unpublished exemption from an arbitrary qualifier pool.

The main draw's 32 incoming routes are established at lock.
If opening seed 33 defeats seed 32 for a route, that wrestler still displays opening seed 33 in the main draw.
Do not assign a new seed based on the defeated wrestler or reseed the surviving 32.
Qualifiers remain visible and archived after the main competition begins.

| Locked entrants | Tree leaves | Qualifier rounds | Contested qualifiers in an intact field | Main slots | Total contested bouts in an intact field |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 2 | 0 | 0 | 2 | 1 |
| 3 | 4 | 0 | 0 | 4 | 2 |
| 12 | 16 | 0 | 0 | 16 | 11 |
| 17 | 32 | 0 | 0 | 32 | 16 |
| 32 | 32 | 0 | 0 | 32 | 31 |
| 33 | 64 | 1 | 1 | 32 | 32 |
| 47 | 64 | 1 | 15 | 32 | 46 |
| 64 | 64 | 1 | 32 | 32 | 63 |
| 65 | 128 | 2 | 33 | 32 | 64 |
| 128 | 128 | 2 | 96 | 32 | 127 |
| 257 | 512 | 4 | 225 | 32 | 256 |

Absent exceptional exits, a knockout with `N` entrants needs `N - 1` contested bouts.
Above 32 entrants, qualification needs `N - 32` contested bouts and leaves 32 unique survivors.
Byes are structural records and consume neither a match random roll nor a contested-win reward.
They occupy their scheduled round and do not cause an early extra round for a privileged entrant.

Registration close reserves the complete next-power-of-two tree's round slots for the admitted field then known.
All countries share the preparation duration published at announcement.
The default 90-day fixture closes entry on day 20, locks the roster on day 110, and opens the earliest competition slot on day 120.
With another published preparation duration, lock is `20 + preparation_days` and `competition_open_date = lock + 10`.
Every further reserved round slot is five days later.
At lock, align the actual tree's rounds with the trailing slots for the same round sizes.
Leave any unused leading slots as rest and preserve the originally published main-round and final dates.
Thus a 65-person registration reduced to 32 uses its published round-of-32 date on default day 130 as its first expected contest, while a reduction to two uses the final date on day 150.
Store the earliest competition slot, the derived first expected contest and the first actual played contest separately.
The last can remain unset when exceptional withdrawals prevent all contests.
Do not grant a late entrant after the entry gate, reopen training, or change dates to produce a preferred opponent.

The mathematical check covers fields 2 through 512.
That is tested design coverage, not a maximum eligible-country cap or proof of native capacity.
Implementation must count the actual supported world's candidates, chunk construction under the verified engine loop limit, and test that maximum.
If production or storage capacity is short, report and repair the content defect before making the feature available.
Do not silently drop accepted countries.

## 4. Match identity and preparation lock

A match has an edition ID, stable match ID, stage, round, two incoming sources, original date, revised date if any, one fixed outgoing destination and one current official result.
Each attempt has a separate immutable attempt receipt.
Initial leaf slots point to locked entrant IDs or explicit emptiness.
Every later slot points to the official output of one particular earlier node.

The upcoming bout opens when both incoming branches are settled.
The participant pair freezes one day before its scheduled contest.
Before that point, a timely ruling may amend an earlier branch under Section 8.
After it, the pair cannot be replaced by a newly selected wrestler or a revived defeated entrant.
Player and AI match approaches lock at that same boundary.
A late interface submission is refused without charging or changing the submitted plan.
No response uses the saved default approach, initially Balanced.

Pre-bout briefing is a separate small existing-resource preparation action from Part 02.
It can interpret known style and reduce unfamiliarity within the total preparation bonus cap.
It cannot expose the opponent's secret approach, hidden wrongdoing or future random roll.
Pre-lock training affects the wrestler's retained preparation.
Post-lock recovery and briefing affect the future bout only, never earlier seeds or results.

## 5. Six attributes and four approaches

All six attributes retain distinct internal 0 to 100 values.
The effective value is base ability plus completed seasonal gains and actual valid assistance, bounded to 0 to 100.
Only committed, unexpired assistance enters the snapshot.
Funding, national population, division count, player control and reputation do not add a second hidden strength multiplier.

Each approach forms a weighted ability score.

| Approach | Strength | Technique | Endurance | Speed | Toughness | Adaptability | Practical role |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Overpower early | .30 | .20 | .12 | .15 | .13 | .10 | Best for controlled early power, with greater later strain and exposure to counters |
| Technical counters | .12 | .30 | .15 | .18 | .10 | .15 | Rewards technique, reactions and reading an aggressive opponent |
| Conserve energy | .15 | .22 | .28 | .10 | .15 | .10 | Accepts less early pressure to preserve condition and benefit from endurance |
| Balanced | .20 | .22 | .18 | .14 | .13 | .13 | A robust default for a broad profile and uncertain opposition |

Every row sums to one and no single attribute receives more than .30.
Speed helps sudden attacks and escape timing but cannot replace sustained grappling technique or endurance.
Toughness reduces attrition and injury in addition to contributing to ability.
Adaptability limits unfamiliar-style penalties and improves the value of genuine scouting.

Use a small antisymmetric approach adjustment.
Counters gain up to four effective score points against Overpower, Overpower against Conserve, and Conserve against Counters.
The reversed pairing has the opposite adjustment.
Balanced and same-approach pairings have zero adjustment.
This cycle is an explicit gameplay abstraction whose small magnitude prevents a hidden approach guess from overwhelming ability and condition.
The profile and briefing explain the qualitative tradeoffs without revealing a secret opponent choice.

For each entrant, calculate:

`S = weighted_effective_attributes + study_bonus - unfamiliarity_penalty - condition_penalty - injury_penalty`

Use these anchor bounds:

| Component | Anchor and context |
| --- | --- |
| Study bonus | 0 to 8 total effective points from completed valid study and opponent briefing, with no repeated purchase stacking |
| Unfamiliarity penalty | 0 to 6, proportional to actual unusual style and reduced by Adaptability and suitable prior study |
| Condition penalty | `.12 × (100 - Readiness) + .18 × Strain` |
| Injury penalty | 0 when medically clear, 5 for a manageable minor injury, 12 for a medically permitted moderate injury. Serious unfitness prevents the bout |
| Approach adjustment | One antisymmetric `C` between -4 and 4 for the pair, not an independent bonus to both entrants |

Let `Delta = S_A - S_B + C`.
The design target is:

`P(A wins) = .04 + .92 / (1 + exp(-Delta / 12))`

This is a specification equation, not claimed native script syntax.
The coding owner must select a verified monotonic lookup or supported fixed-point approximation with documented error, exact complement symmetry and preserved caps.
Do not assume that an `exp` effect exists.
The probability auditor must compare the implemented calculation against this reference.

| Effective advantage | Favorite win chance | Opponent win chance |
| ---: | ---: | ---: |
| 0 | 50.00% | 50.00% |
| 12 | 71.26% | 28.74% |
| 24 | 85.03% | 14.97% |
| 40 | 92.83% | 7.17% |
| 60 | 95.38% | 4.62% |

These caps apply only when two fit, eligible entrants actually contest the bout.
A withdrawn or disqualified entrant has no random chance to advance.
An enhanced specialist can have a favorable matchup while still losing through weakness, strain, technical counters or the bounded upset chance.
An equal opponent remains equal regardless of country size or human control.

The authoritative resolver freezes all allowed inputs, commits the random attempt once, and records the resulting winner before choosing descriptive result detail.
Opening a report, reloading, paying again or changing a viewing tab cannot create a new roll.
The implementation stores enough evidence to explain the resolved probability and later adjudication without displaying secret rolls to the player.

### A compromised official cannot manufacture a decisive pin

When an actual recorded scheme supplies official bias, calculate `p_clean` without that official adjustment and `p_biased` with it from the same frozen inputs.
Other actual legal or illegal physical assistance is unchanged in both calculations.
Use one complete three-branch winner pool, partitioned at those two thresholds.
For bias favoring A, the branch weights are `p_clean` for an unaffected A win, `p_biased - p_clean` for an official-dependent A win, and `1 - p_biased` for an unaffected B win.
For bias favoring B, the weights are `p_biased` for an unaffected A win, `p_clean - p_biased` for an official-dependent B win, and `1 - p_clean` for an unaffected B win.
Equal thresholds collapse to the ordinary two-outcome draw.
Round both thresholds into the same total integer weight scale before subtracting, so all branches are nonnegative and sum exactly to that scale.

This is one random winner selection, not two bouts or a reroll against a preferred result.
The middle branch records that official intervention changed the winner.
Its method pool contains only a narrow referee decision and a long referee decision, with anchor weights 60 and 40.
It cannot become a decisive pin or clear submission after the winner is chosen.
The unaffected branches use the normal result-method table because that winner did not require official bias.
Keep the causal audit flag hidden until actual evidence permits disclosure.
Investigation and later sanctions still follow the real scheme and case records.

## 6. Result methods and attrition

Choose the winner first.
Then choose a result method conditional on that winner and the same input snapshot.
The method must never secretly reverse the winner already committed.

| Winning wrestler's signed effective advantage over the opponent at freeze | Convincing win | Pin or submission | Narrow decision | Long referee decision |
| --- | ---: | ---: | ---: | ---: |
| At least 24 | 55 | 30 | 10 | 5 |
| At least 12 but below 24 | 40 | 30 | 20 | 10 |
| Nonnegative but below 12 | 15 | 35 | 35 | 15 |
| Below 0, an underdog winner | 10 | 45 | 30 | 15 |

These complete weights sum to 100 per named fixture.
Pin versus submission uses the actual winner's technique, speed and approach within that already selected method family.
No invented point score is shown unless the implementation defines and records a supported scoring model.
A convincing result, technical submission and long decision receive different writing and fatigue outcomes.
An upset is a derived report and career tag when the winner's frozen win probability was at most .30, not a separate way to reroll the bout.

The baseline Strain gain for each contestant is:

`clamp(20 + 10_if_long + 5_if_overpower - 10_if_conserve - (Endurance - 50)/10, 10, 35)`

Readiness falls by 5 after a normal contested bout and by 10 after a long contest.
Clamp both meters to 0 to 100 and record one attrition receipt per actual attempt.
The five-day round interval restores Readiness by 5 and reduces Strain by `clamp(10 + (Endurance - 50)/10, 5, 15)` when safe ordinary recovery is available.
A deliberate post-lock rest choice can provide an additional five Strain reduction at the cost of the opponent briefing opportunity for that interval.
No extra recovery is granted by repeatedly reopening the panel.
Travel disruption, injury and actual assistance can alter these bounded recovery terms under their recorded effect contract.

A healthy ordinary bout uses an injury candidate fixture with weights 940 no new injury, 50 manageable injury and 10 serious injury.
This is a 1,000-weight reference fixture, not a universal frequency claim.
High Strain, low Toughness, an existing injury, unsafe treatment or an extraordinary mismatch changes eligible weights through declared modifiers.
The full active pool and denominator must be recorded by the future probability audit.
There is no per-frame, report-opening or idle global injury roll.

Manageable injuries use dated recovery and the stated score penalty.
Serious injury stops further wrestling until medical clearance and normally causes withdrawal from the current short competition.
Winning an injury-affected final does not by itself erase a legitimate title.
Ordinary athlete injury does not subtract an invented army or civilian casualty total.

## 7. Withdrawals, vacancies and interruption

| Situation | Authoritative handling | Advancement, reward and archive |
| --- | --- | --- |
| One empty initial leaf | Structural bye at its scheduled node | Real entrant advances, no contested win, opponent or random roll |
| One entrant withdraws or is finally disqualified before the contest | Walkover or disqualification ruling | Opponent advances with the precise reason. No normal bout roll or upset credit |
| Both entrants unavailable | Double withdrawal or double disqualification | Node has no winner. Its output becomes an explicit vacancy |
| A later node receives one real entrant and one vacancy | Vacant-branch advancement | Real entrant advances without a played win |
| A later node receives two vacancies | Vacant node | Propagate vacancy until a real branch or the final is reached |
| Contest stopped with no official winner | No contest, then one same-entrant retry if five days remain in the edition's shared exceptional delay allowance | Preserve original attempt and attrition. Create one legitimate retry attempt with new date and receipt, never reseed or add a new entrant |
| Repeated no contest, unsafe retry or exhausted delay allowance | Unresolved branch becomes vacant | No lottery winner. Preserve both attempts and ruling |
| Final has one valid entrant and one vacancy | Sole surviving finalist receives the published walkover title | Reduce award using actual contested depth. No final upset, pin or defense-bout credit |
| Final has no valid entrant | `champion_status = vacant` | No championship payment or positive champion achievement |
| Venue ceases to be safe | Use one actual alternate suitable existing venue if available, preserving the draw and charging only actual permitted costs | All exceptional delays combined remain at most 10 days. If no safe completion exists, close interrupted with no title |

The shared exceptional delay allowance belongs to the edition.
Venue changes, inquiries and no-contest retries cannot each claim a separate ten-day extension.
Any date changes move affected downstream rounds consistently and preserve the minimum published recovery interval.
Unrelated already completed bouts remain unchanged.

Pre-lock replacement is the only route to a different nominated wrestler.
After lock, a country cannot replace an injured, defeated or disgraced entrant with a stronger reserve.
A timely correction to the original contest can restore its actual original opponent under Section 8.
That is a correction inside the locked tree, not admission of a new person.

If a sponsoring country disappears before lock, its entry withdraws unless an existing recognized exile representation and valid host path already satisfy Part 01.
After lock, an already arrived, living and otherwise eligible athlete can continue as unsponsored when the host remains safe and their owner record does not prohibit it.
Use the saved approach and ordinary neutral recovery.
The annexing country gains no control, new candidate, diverted award or ownership of the old participant record.
A dead, missing, unsafe or owner-invalid athlete cannot continue merely because their portrait exists.

## 8. Inquiries and local result corrections

Keep the original attempt, observed outcome, evidence, ruling and current official standing as separate records.
An allegation opens a case, not a guilty result.
Part 02 governs investigation cost, evidence, safe defaults and the distinction between cleared, unproven and proven claims.

| Ruling time | Permitted effect | Boundary |
| --- | --- | --- |
| Before the affected bout begins | Enforce eligibility, remove prohibited assistance, replace an official or disqualify a proven offender | Same locked entrants and fixed route. No paid result assignment |
| After the bout, before its successor's participant freeze | Overturn that bout when the rulebook and evidence justify it. Restore only its original clean opponent to the existing outgoing slot | Append an amendment and preserve the original receipt. Recompute no unrelated match |
| After the successor's participants freeze | Apply prospective disqualification, suspension, reputation loss or title review | Do not revive a previous loser into a frozen bout, replay a legitimate successor or move a different branch |
| During the ten-day final settlement | Ratify the clean final winner, award the direct clean finalist if a proven final violation legally changes the final, or declare the title vacant | One initial championship payment receipt after settlement. No title to an arbitrary semifinalist |
| After championship ratification | Amend standing under the same direct-final evidence rule, revoke the offending holder's remaining recognition and record sanctions | Never pay a second edition prize. Do not roll back unrelated bouts or seize already spent resources |

An earlier ineligible appearance discovered after successor freeze can cause prospective removal and a vacancy.
It does not automatically establish that every earlier opponent would have won a replay.
Direct final fraud can justify transferring the official title to the original clean finalist.
Broader late invalidity without a lawful clean final recipient leaves the title vacant.
A result has one current official version and an append-only amendment chain, never two current winners.

Positive achievements and ordinary edition rewards evaluate after the settlement window.
A later amendment changes archive standing and future eligibility.
Previously granted platform or persistent achievement unlocks need not be technically retractable and must not be promised as such.
Their internal evidence record retains the dated rule version under which they were awarded.

## 9. Championship recognition and economy

The champion receives a bounded Political Power award and a temporary national recognition effect when a valid sponsoring country still exists.
There is no wrestling currency.
The athlete and historical affiliation can retain a title even if no extant country is eligible to receive its national resource reward.
Do not redirect payment to an annexer or a later unrelated reuse of the tag.

Compute the normal award from locked field breadth and the actual path:

`breadth = clamp(log2(max(2, N))/5, .4, 1.2)`

`difficulty = .7 + .6 × mean_recognized_quality_of_contested_opponents/100`

`depth = .4 + .6 × clamp(contested_wins/5, 0, 1)`

`ordinary_PP = round_to_5(clamp(60 × breadth × difficulty × depth, 10, 90))`

When there were no contested opponents, use the lowest difficulty term .7.
This prevents an all-walkover path from receiving the reward of a demanding full draw.
Use recognized quality snapshotted for the actual bout, not a later reputation inflated by the same title.
Implement logarithms through a verified field-size table if necessary.
Awards are gains, so do not pass them through a purchase-discount helper.

| Additional recognition | Evidence | Anchor |
| --- | --- | ---: |
| Title defense | Same wrestler held a ratified non-vacant title in the immediately preceding completed edition and wins this valid edition | +10 PP |
| First minor-country giant-killer title | Country was a minor at this edition's lock, had no prior ratified title, and champion beat at least two major-country opponents in actual contested bouts with frozen win chance at most .30 | +15 PP |
| Earned rivalry conclusion | Champion defeats an actual recorded prior rival in a contested bout this edition | +5 PP once |

Cap the combined championship PP at 110.
The normal 32-person five-win path with middling opponent quality starts around 60 PP before exceptional recognition.
The two-person path earns much less.
A larger field can increase breadth but not create an unbounded payout.
Exact tuning uses the full scenario comparisons in Part 06.

The national recognition effect is one event-owned tier with a 90-day duration and an anchor of +5% Political Power gain.
Defending or extraordinary recognition changes its descriptive tier and receipt, never stacks several copies of the same economic modifier.
Do not add stability, war support, army combat bonuses or permanent industrial capacity simply because a match was won.
National Obsession can add its own bounded, evidenced public reaction under Part 04 without a second title payment.

A clean runner-up with at least one contested win can receive a modest 10 PP recognition, scaled up to 20 for a deep strong field.
It has its own one-time placement receipt and no champion modifier, title count or defense flag.
Qualifying losses and ordinary entry do not receive farmable recurring participation money.
Refunds return only the actual unused refundable amount, not a prize.

## 10. Career and archive effects

Record the champion identity, standing version, award recipient, actual prize, title conditions and effective dates.
Record every entrant, qualifying path, original seed, bout, bye, walkover, withdrawal, major upset, injury, rivalry and public sanction.
Retain original names, portrait version keys and affiliation flag/name keys captured for the edition.
A later portrait improvement may be offered as a present-day profile asset while the archive retains its original approved identity presentation key.
Never substitute another face for the same person or a current regime's flag for a frozen historic one.

Career reputation grows most from actual high-quality contested wins and sustained results, with diminishing returns.
A title affects record, recognition and future seed evidence, not the six physical attributes automatically.
Permanent training gains follow Part 02's small once-per-edition limits.
Suspensions and injuries expire through dated owner state.
Retirement preserves the history and frees a future nomination place without recycling the person ID.

The default history view is compact and paged by edition.
Selecting one edition loads its bounded relevant arrays and details.
Paging is a presentation optimization, not permission to delete older records or drop qualifiers.
The next edition starts with clean operational arrays and new IDs while retaining previous careers and archive references.

## 11. Design evidence and implementation gates

The parent reran the supplied mathematical checker successfully.
It verifies the seed permutation, opposite halves, top-four quarters, high-seed byes, absence of an empty-versus-empty initial pairing, `N - 1` intact-field bouts and `N - 32` qualifying bouts for every `N` from 2 to 512.
It also verifies probability symmetry, monotonicity and the .04 to .96 limits over a wide score range, plus explicit double-absence handling.
Part 11 records the exact evidence and its limits.

Before implementation acceptance, prove arbitrary upset propagation, save/load during every commit boundary, duplicate callbacks, annexed sponsors, all vacancy paths, timely and late amendments, native fixed-point probability agreement and single-award behavior.
The mathematical checker does not establish native syntax, GUI behavior, engine random persistence or multiplayer authority.
