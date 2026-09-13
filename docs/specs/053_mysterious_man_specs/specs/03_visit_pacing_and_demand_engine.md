# 3. Visit Pacing and Demand Engine

## Scheduling model

Event 53 uses country-scoped delayed follow-up events attached to the selected target. It must not use a daily, weekly, or monthly whole-world scan.

After every completed visit, the event calculates one dynamic interval and queues one future country event. A visit is considered completed after the payment transaction succeeds or the selected consequence adapter returns a final accepted receipt.

No next visit is scheduled while a consequence transaction is still reserving targets, releasing countries, starting wars, or reconciling state changes.

## Recommended interval bands

The following ranges are tuning anchors for implementation. Final values should be centralized in Event 53 script constants and tested against popup frequency.

| Active behavior tier | Base interval range |
| --- | --- |
| Baseline | 120 to 210 days |
| Evolution I behavior | 100 to 180 days |
| Evolution II behavior | 75 to 150 days |
| Evolution III behavior | 60 to 120 days |

The absolute interval floor is 45 days. No modifier may reduce the final interval below that floor.

These bands should remain independent from the global random-event timer. Event 53 follow-ups are part of one Fire-Once chain and should not consume normal event slots.

## Dynamic interval factors

The scheduler can shorten the base interval through bounded factors:

- active evolution behavior
- total completed visits
- consecutive refusals
- total refusals
- long chain age

Consecutive refusals should have the strongest visit-history effect. The reduction should reach a cap after several refusals so the chain never becomes rapid popup spam.

Recommended behavior:

- first refusal applies a small reduction
- several consecutive refusals can reduce the selected tier's interval by roughly one-quarter to one-third
- a payment clears the consecutive-refusal streak
- total historical refusals can retain a smaller permanent pressure
- repeated payments do not need to shorten the interval because they already increase later demand strength

Random variance should remain broad enough that the player cannot calculate the exact return date.

## Popup-load protection

The scheduler must prevent duplicate Event 53 popups. Before opening a visit, it proves that:

- the target still exists
- the target marker is unique
- the target is human-controlled
- no Event 53 visit is already present
- no Event 53 consequence is still resolving
- no demand remains locked from an earlier visit

If human control is absent, the visit enters the pause path. If another Event 53 transaction is active, the event reschedules a short bounded retry without reducing the main interval again.

## Demand-tier rules

### Baseline

Political Power is the only demand type.

### Evolution I behavior

One valid demand type is selected from:

- Political Power
- Command Power
- Army Experience
- Navy Experience
- Air Experience
- infantry equipment
- support equipment
- artillery
- trucks
- trains
- convoys
- fuel
- manpower
- temporary civilian industrial capacity
- temporary military industrial capacity
- Stability
- War Support

Each valid demand type receives one ballot. Demand-type selection is uniform among the current valid types. A type that does not sensibly apply to the target is absent.

### Evolution II behavior

The same demand families remain available. Amounts use stronger progression multipliers and higher caps. The event still asks for one main thing.

### Evolution III behavior

The same demand families remain available. The amount can consume a very large reserve, impose a major temporary industrial burden, or demand a large political sacrifice. The event still locks one demand type and one amount.

## Demand-type validity

Validity answers whether the resource system meaningfully applies. It does not guarantee affordability.

Examples:

- Navy Experience is invalid for a country with no navy, no dockyards, no naval production, and no active naval institution.
- Convoys are invalid for a country with no port, no overseas territory, no convoy-capable trade, and no convoy stockpile.
- Air Experience is invalid only when the country has no meaningful air system or route to one.
- An equipment type is valid when the country's military can use the matching archetype and the stockpile debit helper supports it.
- Temporary civilian capacity is valid when the country has enough civilian industry for a meaningful timed burden.
- Temporary military capacity is valid when the country has enough military industry for a meaningful timed burden.
- Stability and War Support remain conceptually valid, but the payment option becomes unavailable when the locked deduction would cross the protected payment floor.

A valid but unaffordable demand is intentional. It forces refusal.

## Amount calculation model

Every demand family receives its own documented calculator. The general form should include:

1. a demand-family minimum
2. a structural country anchor
3. a current reserve or current value anchor where relevant
4. visit progression
5. payment-history progression
6. refusal-history progression
7. active evolution behavior
8. a demand-family cap
9. player-facing rounding

The calculator should use the greater of a structural floor and a bounded share of current holdings when this prevents stockpile dumping from trivializing future demands.

A country should not be able to lower a future equipment demand to nearly zero by discarding its stockpile before the visit. Industry, fielded-force scale, recent production, or another stable capacity measure can support the structural floor.

The amount is locked before the popup appears. It must not recalculate when the player hovers, closes another window, changes production, or chooses an option.

## Progression factors

### Visit progression

Later visits become more costly through a bounded multiplier. The first few visits should show clear growth. The curve should flatten before values become numerically absurd at low Chaos.

### Payment progression

Every successful payment increases a persistent compliance factor. This is the main implementation of the rule that repeated compliance makes later demands more painful.

The compliance factor applies to future amounts only. It does not shorten the current visit, alter the consequence roll, or create a hidden chance of punishment after payment.

### Refusal progression

Refusals can raise future amounts modestly and shorten future intervals. Their main risk remains the immediate consequence. Demand growth from refusals should stay lower than demand growth from repeated payments so refusal is not punished twice through an excessive permanent tax.

### Chaos progression

Higher active evolution behavior increases the amount range and cap. Evolution activation itself does not add Chaos.

## Recommended demand tuning anchors

These anchors describe desired scale. They are not final hardcoded values.

| Demand family | Early meaningful range | High-tier direction | Important cap or floor |
| --- | --- | --- | --- |
| Political Power | 75 to 180 for an ordinary established state | several hundred for a strong government | amount must remain a real choice, not automatic total removal |
| Command Power | 15 to 40 | up to 60 | never exceed 60 |
| Army, Navy, or Air Experience | 10 to 35 | 30 to 80 where reserves support it | round to readable whole values |
| Infantry equipment | meaningful national reserve share with a country-size floor | major reserve loss | do not debit deployed equipment through an unsafe path |
| Support equipment | meaningful national reserve share | major reserve loss | use the supported stockpile helper |
| Artillery | meaningful national reserve share | major reserve loss | select a supported artillery token or owner adapter |
| Trucks | meaningful transport reserve share | severe logistics loss | use the supported motorized helper |
| Trains | several trains for small networks, more for large networks | network-threatening loss | never request a fractional train |
| Convoys | meaningful maritime reserve share | overseas-network-threatening loss | invalid for a country with no meaningful convoy system |
| Fuel | several weeks of ordinary consumption or a reserve share | strategic reserve collapse | avoid token fuel values |
| Manpower | a bounded share of free manpower with a structural floor | a large mobilisation sacrifice | debit free manpower, not state population |
| Civilian capacity | 5 to 12 percent equivalent burden | 15 to 30 percent equivalent burden | timed burden, no permanent factory deletion |
| Military capacity | 5 to 12 percent equivalent burden | 15 to 30 percent equivalent burden | timed burden, no permanent factory deletion |
| Stability | 3 to 8 points | 8 to 20 points | payment cannot cross the protected floor |
| War Support | 3 to 8 points | 8 to 20 points | payment cannot cross the protected floor |

## Temporary industrial capacity

A demand for civilian or military industrial capacity represents compelled use, diversion, or unexplained loss of access for a fixed period.

It should use a timed burden scaled from the relevant factory base. It should not delete factories, transfer factories to an invisible country, or create a permanent map change.

The player-facing effect must state the duration and practical burden. The internal implementation can use a timed national spirit, dynamic modifier, consumer-goods pressure, factory-output reduction, or another verified engine pattern that matches the intended capacity type.

The burden must be removed exactly once when its duration ends, even if the country changes ideology, faction, subject status, or capital.

## Payment affordability

The payment option is enabled only when the target can pay the full locked amount through a safe supported transaction.

No partial payment exists. No overdraft exists. No automatic conversion between resources exists.

Examples:

- a Political Power demand requires at least the locked amount
- an equipment demand requires the supported stockpile to contain the locked amount
- a Stability demand requires enough current Stability to remain at or above the protected payment floor after deduction
- a temporary industrial demand requires the target still to possess enough relevant industry for the burden to remain meaningful and valid

When the option is disabled, its tooltip should state the exact missing amount or blocked floor in concise terms. The refusal option remains available.

## Payment transaction

A successful payment performs this order:

1. revalidate target and locked demand proof
2. revalidate affordability
3. debit the exact displayed amount once
4. store a payment receipt
5. increment total paid visits
6. clear consecutive refusals
7. increment total visits
8. clear locked demand state
9. set latest-visit history
10. calculate and schedule the next interval

A transaction failure cannot silently become a payment. If affordability changed while the popup was open, the payment stance routes to inability-to-pay refusal after a clear transition, or the popup safely refreshes before outcome application. The implementation should choose the engine-safe pattern that does not duplicate either outcome.

## Refusal transaction

A refusal performs this order:

1. revalidate target and visit proof
2. increment total refusals and consecutive refusals
3. increment total visits
4. call the authoritative consequence selector once
5. wait for an accepted adapter receipt
6. store the selected package ID and receipt
7. clear locked demand state
8. set latest-visit history
9. calculate and schedule the next interval

The pool should read the refusal count after the current refusal is registered when severity formulas use refusal history.

## Demand presentation

The popup should show one icon or texticon for the requested resource when the event surface supports it. The amount should use readable rounding and the project's normal resource formatting.

The description should identify the secure location, establish that the man is already present, and state the demand without explaining the formula. Later visits can briefly acknowledge that security changes have failed to matter.

The pay stance should communicate direct compliance. The refusal stance should communicate a clear rejection without making the government sound certain that it can resist the consequence.

Final wording belongs to implementation and localisation review.
