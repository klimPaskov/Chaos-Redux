# Event 26: Black Friday

## Event identity

| Field | Specification |
| --- | --- |
| Event ID | `26` |
| Event name | Black Friday |
| Event class | Minor Fire-Once |
| Minimum chaos | Gathering Storm, 200 chaos |
| Evolution | Seventy-Five Percent Off at Chaos Tier, 600 chaos |
| Geographic scope | Global |
| Event actor | Actorless world event |
| Active duration | One in-game day, ending on the next daily tick |

## Playable promise

The event creates a brief global purchasing window. Governments, armed forces, intelligence services, ministries, and commercial suppliers all treat the same Friday as a clearance sale. A player who has saved resources can compress several expensive choices into one day. A player who has spent heavily before the event still gains lower prices on any actions that remain available.

The event must change real costs. A reduced number shown in a tooltip without an equal reduction in the payment effect is a defect. A hidden payment reduction with an unchanged displayed price is also a defect.

The sale does not grant resources. It changes the price of eligible actions. Existing availability rules, cooldowns, laws, route locks, target rules, required technologies, unit requirements, state control, and action limits remain intact.

## Player flow

### Before selection

Event 26 remains outside the live pool below 200 chaos. At 200 chaos or higher, it participates as a normal fire-once event with its current fire-once weight.

### Reservation

When the random-event picker selects Event 26, the event enters a global reserved state. No sale begins at this point. The visible event popup is held until an eligible Friday.

The reservation removes Event 26 from further random selection without marking it as fired. The random event timer continues normally after the selection has been resolved.

### Friday activation

On the first Friday when the world is at 200 chaos or higher, the event activates. If the random picker selects Event 26 on an eligible Friday, the selection path may activate it immediately on that same in-game day.

The event snapshots the active discount at activation time:

| Chaos at activation | Discount | Payment ratio |
| --- | --- | --- |
| 200 to 599 | 50 percent off | 50 percent of the current payable cost |
| 600 or higher | 75 percent off | 25 percent of the current payable cost |

Later chaos changes during the active day do not change the snapshot. Enabling or disabling Evolution I after activation also does not change the snapshot.

### Active day

Every registered cost surface reads the same global sale snapshot. Costs recalculate from their current ordinary value, then apply the Black Friday payment ratio and the registered rounding rule.

The player can use any otherwise valid purchase or commitment. The event does not create a separate store, a new decision category, or a list of special sale-only purchases.

### Expiry

The sale ends on the next daily tick. Only the Black Friday source is removed. Ordinary cost modifiers, surcharges, discounts, route bonuses, laws, ideas, and campaign state remain unchanged.

Actions opened before expiry must revalidate their price when taken. A transaction that committed payment during the sale keeps the price it paid. A transaction that had only displayed a quotation must use the current price after expiry.

## What qualifies as a sale cost

A qualifying cost is a voluntary payment or commitment made to begin, complete, or purchase an action. Examples include political power, command power, experience, equipment, fuel, convoys, trains, manpower, factory commitments, agency payments, and registered custom currencies.

A penalty is not a sale cost. Casualties, attrition, event damage, occupation losses, condemnation, contamination, mission failure effects, upkeep, research time, focus duration, construction time, and enemy-inflicted losses do not receive a discount unless the owning system explicitly models them as a voluntary purchase and registers that transaction.

## Strategic role

Black Friday is a high-impact minor event with very short duration. Its strength comes from timing and preparation. It should not add direct chaos, stability, war support, equipment, factories, or political power.

The event is allowed to be powerful because it is fire-once, requires at least 200 chaos, waits for a Friday, and lasts one day. The design does not add a global purchase cap. Existing action limits and reserve checks control how much a country can exploit.

## Information available to the player

The Friday popup communicates:

- the sale applies globally for the current day
- the active discount is 50 percent or 75 percent
- positive costs have a minimum payable unit
- ordinary requirements and cooldowns still apply
- the sale ends on the next daily tick

Cost tooltips should show the active sale price and the undiscounted current price when the owning UI can present both cleanly. The event status should be visible through Event Details and a short temporary status marker for human-controlled countries.

## Tone and writing direction

The event should use brisk period commercial language mixed with government procurement absurdity. The player should see crowded shops, hurried purchasing offices, officers trying to secure supplies, ministries advancing appointments, and suppliers issuing new price sheets.

The humour should come from the same discount reaching military, political, and intelligence purchases. The text should avoid modern online-shopping language, current company names, modern shopping carts, social-media references, and exaggerated meme phrasing.

The event option should be a short dry reaction from a government or purchasing office. It should acknowledge the opportunity without becoming a generic confirmation button.
