# Law Upgrade
## Part 6. War Support, combined effects, and reversal

## Current willingness to sustain mobilization

War Support is the only public support variable used by this event. There is no second morale, compliance, or emergency-legitimacy meter.

The event grants its War Support before evaluating the new laws' penalties. The grant is 10, 25, 50, or 50 percentage points according to the applied profile. It is never the sum of every unlocked profile.

War Support stops at its ordinary maximum. An 80% country receiving 50 percentage points ends at 100%, with no stored overflow and no substitute reward.

## Penalty relationship

Let `W` be current War Support expressed between 0 and 1.

For a penalty whose magnitude is `L` at 0% support and `H` at 100% support:

`penalty(W) = H + (L - H) × (1 - W)`

Here `L` is the larger loss and `H` is the smaller, still severe loss. For a training-time increase, the result is the amount added to normal duration. For Stability, the result is a percentage-point reduction.

The relationship is continuous and monotonic. Raising support cannot worsen one of these penalties. Lowering support cannot leave behind protection earned at the moment of entry.

| Current War Support | Economy civilian-construction loss | Conscription output loss | Conscription training-time increase |
| --- | ---: | ---: | ---: |
| 0% | 95% | 95% | 250% |
| 25% | 90% | 91.25% | 212.5% |
| 50% | 85% | 87.5% | 175% |
| 75% | 80% | 83.75% | 137.5% |
| 100% | 75% | 80% | 100% |

The intermediate fractions are mathematical results, not additional hand-tuned balance endpoints. Tooltips may display a suitable precision while payment and effect calculations retain their required precision.

## Refreshing the relationship

Current penalties must update after a War Support change, after a relevant law change, and after a change between war and peace. The opening event's own refresh happens before its results are presented.

An ongoing holder must not retain a stale support tier beyond one game day. The implementation uses the existing owner lifecycle or bounded active-holder mechanism, not a new independent global daily scan.

The visible law details must report the effective value being applied. A tooltip cannot show the new value while the country still suffers a different old value.

## Combined effects of both extreme laws

When the two laws affect the same capacity, combine their own remaining-capacity factors multiplicatively.

This prevents a +100% economy output bonus and an 80% conscription output loss from becoming a net +20% reward. At full support, their combined military-factory contribution is `2.00 × 0.20 = 0.40`, representing 40% of the reference capacity before unrelated effects.

The aggregate below describes only Event 82's two extreme-law contributions. It is not a promise that the entire engine calculation, including every unrelated idea, technology, country system, shortage, and damage modifier, uses this multiplication.

| Capacity with both laws, while at war | 0% support | 50% support | 100% support |
| --- | ---: | ---: | ---: |
| Military factory output | 10% | 25% | 40% |
| Dockyard output | 8.75% | 21.875% | 35% |
| Military factory construction | 20% | 45% | 70% |
| Dockyard construction | 17.5% | 39.375% | 61.25% |
| Civilian factory construction | 0.5% | 3.375% | 8.75% |
| Infrastructure construction | 1.5% | 7.3125% | 17.5% |
| Repair capacity | 3% | 10.125% | 21% |
| Research speed | 4% | 12.9375% | 26.25% |
| Political Power gain | 37.5% | 51.5625% | 67.5% |
| Population growth | 0.05% | 0.825% | 2.5% |
| Combined Stability penalty | -90 pp | -70 pp | -50 pp |

The percentages in the capacity rows are remaining capacity, not loss. For example, 8.75% civilian construction means a 91.25% loss of the reference capacity.

Stability penalties add as percentage-point contributions and then obey the ordinary bounds on national Stability. They are not multiplicative remaining-capacity effects.

Only the two extreme laws' own terms are combined by this rule. Event 82 must not cancel or rewrite unrelated national modifiers to force a particular final output percentage.

At peace, remove the economy law's wartime benefits before forming the combined result. The conscription output penalty and both laws' civilian penalties remain.

## What this means for reversal

At full support while at war, leaving Totalen Menschen!!! and keeping Totalen Krieg!!! changes the law-owned military output factor from 0.40 to 2.00. Leaving Totalen Krieg!!! and keeping Totalen Menschen!!! changes it from 0.40 to 0.20.

The first route is usually the stronger immediate equipment-production recovery. The second still restores civilian capacities damaged specifically by the economy law and may be justified by a country that needs the exceptional recruitment ceiling.

This asymmetry is intentional. The two exits must not produce indistinguishable outcomes.

## Manual reversal actions

There are exactly two Event 82 manual reversal actions.

| Available while holding | Result |
| --- | --- |
| Totalen Krieg!!! | Restore Total Mobilization |
| Totalen Menschen!!! | Restore Scraping the Barrel |

They appear in one small native decision category while either extreme law is held. The existing law panel shows the current law, current penalties, and where its reversal is performed.

These actions are the authoritative manual exit route. Direct selection of a lower law must not provide a cheaper bypass or skip the required immediate predecessor. The player can make further ordinary law changes after completing the extreme reversal.

No additional cooldown, duration, manpower fee, Stability fee, War Support minimum, ideology gate, peace requirement, or technology gate is attached to these actions.

A country may leave while at war, at peace, at low support, after Chaos has fallen, or after the evolution has been disabled.

## Exact doubled price

Let `C` be the current ordinary payable price of the corresponding adjacent law change, resolved with the country's ordinary modifiers, active applicable discounts, and normal rounding.

The manual extreme-law reversal price is:

`R = 2 × C`

The doubling applies to the resolved ordinary price. It is not a fixed extra 150 Political Power, and it is not a second independently discounted purchase.

| Current ordinary adjacent price | Extreme-law reversal price |
| --- | ---: |
| 150 PP | 300 PP |
| 75 PP | 150 PP |
| 113 PP | 226 PP |
| 0 PP | 0 PP |

If both laws are held, each reversal has its own price. Reversing one does not pay for the other. Changes in national modifiers between the two actions can change the second action's current price.

A displayed estimate must be refreshed when its inputs change. On confirmation, the action recalculates the current price, checks the complete amount, and either performs one paid law change or does nothing.

The displayed accepted price, the amount actually charged, and the recorded result must agree. A failed affordability check never removes the law or charges a partial fee.

## Ordinary costs and exceptional removals

The quoted adjacent price is the price of the relevant one-step law transaction before Event 82's exceptional exit multiplier. It is not a multi-step route to a much weaker law.

Voluntary entry into an extreme law uses the ordinary one-step price and the gates in Part 3. Forced entry by Event 82 is free.

A separate event that forcibly demobilizes a country is not a manual purchase. It uses its owner's explicit forced-change policy, with no hidden Event 82 exit fee. Annexation and country destruction also do not charge Political Power.

The event must not attach a fee to every removal of the idea regardless of cause.

## Leaving and returning

Removing either law removes only that law's continuing effects and recomputes any remaining extreme-law contribution. War Support is not refunded or removed. Previous casualties, spent Political Power, and lost economic time are not undone.

A later Event 82 firing can return the country from the normal cap to the extreme endpoint if the applied profile includes Evolution III.

Re-entry creates no new population, no duplicate permanent penalty, no replayed historical achievement, and no repeatable Chaos reward from an already-consumed one-time milestone.
