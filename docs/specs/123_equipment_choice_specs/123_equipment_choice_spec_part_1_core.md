# Equipment Choice
## Part 1. The shipment and the national choice

Each firing brings a substantial, unexplained military consignment within reach of every active country.
Each government chooses the material it will receive.
The player compares concrete equipment quantities against current military needs, and the AI makes the same choice through the same eligibility and delivery rules.
A small army can equip a meaningful reserve, while a large army receives enough material to change a real procurement decision.

Equipment Choice is a Minor Repeatable event with proposed Chaos level 1.
Event 123 is the catalog identity, with former catalog ID 135 retained as provenance.
Sudden Abundance and Military Preparation each include it at Medium severity.
The two evolutions are Overflowing Arsenals at 200+ Chaos and Impossible Arsenals at 600+ Chaos.
All labels in this package are internal working labels and describe writing intent.
The implementation author writes the final localisation.

## The first firing

The national report shows an unexpected supply opportunity, its current selection deadline, and the presence of several distinct equipment consignments.
An ordinary decision category contains the actual choices.
Each category choice shows the exact models, complete variants where needed, quantities, immediate use, reserve use, and any relevant fuel or manpower requirements.
The report opens the category and never grants the cargo itself.

The baseline choice is one of five groups.
A country's offered manifest is prepared when that firing reaches it.
Its industrial circumstances, war pressure, equipment access, and useful consumers determine the contents and size.
Countries receive separate manifests and choose independently.
A major's choice never fixes a subject's package.
Human control does not confer a larger budget or a privileged equipment pool.

| Working group | Military purpose | Contents that the player compares |
| --- | --- | --- |
| Infantry and support | Reequip ordinary formations and establish a durable reserve | Infantry equipment and support equipment, matched to usable national models |
| Fire support | Strengthen gun formations and air defence | Artillery and anti-air equipment, with an anti-tank share where it is useful and fieldable |
| Mobility and armour | Improve transport or equip a viable armoured force | A transport profile or a complete tank profile, with ordinary support material |
| Aircraft | Reinforce a useful air role | Complete fighter, ground-attack, or bomber equipment matched to a valid deployment path |
| Maritime logistics | Support existing or plausible sea supply | Convoys and relevant land logistics equipment, with the actual convoy share shown |

These groups are different strategic destinations for a common value allowance.
They do not all contain the same number of objects.
A thousand rifles, a hundred tanks, and a hundred aircraft have different equipment values and practical consequences.
Part 2 defines how the value allowance becomes real cargo.

## Who receives a choice

The firing takes one snapshot of active country identities.
It includes independent countries, subjects, countries at war, civil-war participants already present, human special countries, and actual nonhuman countries.
A special-country classifier alone cannot remove an entitlement.
A country that appears later joins the next firing.

A valid government in exile retains its own entitlement when the engine provides a persistent country and stockpile scope.
Lack of a controlled port, airbase, capital, factories, or a land connection can remove an inappropriate package profile, and it can alter the size floor or reserve-use description.
It does not cancel the country's infantry or compatible military reserve opportunity.
Technical hosts and inactive database tags are outside the active-country snapshot.
The testing country participates only through the explicit testing path.

For a special military economy, consult its existing owner contract before building the manifest.
Prioritize equipment consumed by its actual formations or by a documented compatible force.
Where it currently has no fieldable equipment consumer, retain two reserve choices only when each has a documented permitted future consumer or ordinary transfer use.
The player sees that these are reserves for later compatible forces or ordinary permitted transfers.
The AI chooses the reserve with the broadest permitted future use and the smallest existing surplus.
Do not invent a unit unlock, production permission, human manpower source, or diplomatic transfer merely to make the reserve appear immediately useful.
This exceptional reserve profile must be explicit in the implementation's country-profile review.
That review must prove at least two distinct permitted-use manifests for every active military profile.
If an owner contract allows neither compatible future consumption nor an ordinary transfer, record that exact profile as a useful-choice blocker.
A permanently unusable stockpile does not fulfill the universal choice requirement, and the country must not be silently excluded.
A claim that every active country has an immediately usable combat package requires evidence beyond the universal entitlement itself.

## The selection window

A normal offer remains open for 14 days.
A country already at war has 10 days, with a 14-day window restored when no currently usable combat category is available.
These are centralized tuning anchors, chosen to keep a repeatable boon brief while allowing the player to inspect the army and stockpile.
The manifest states the exact deadline.

At expiry, the quartermaster selects the highest-utility legal package using the same evaluation used by AI countries.
Expiry preserves the substantial shipment.
It cannot quietly discard the country's reward.
The report and category explain this automatic selection before the deadline.
A player may leave an offer pending while the game is paused.
Reopening the category, opening Event Details, switching interface pages, or reopening the report does not resample it.

Every natural firing creates its own entitlement even when an earlier one remains unresolved.
The category presents the oldest uncommitted offer first.
Other offers retain their own original deadlines and can resolve automatically without waiting for the visible head.
A later firing never overwrites an earlier manifest.
At the shared two-day minimum event spacing, a 14-day window requires support for at least eight overlapping offer records, including the boundary firing.
A debug burst must preserve an unprocessed suffix and resolve it in bounded batches, without silently dropping records or changing the ordinary campaign limit.

## Choices after Overflowing Arsenals

When an offer is created with Evolution I active, the player first chooses one of three delivery formats.
This short format phase has three actions.
Choosing a format commits the format, then opens the category choices.
Its quantities and handling implications are visible before that commitment.

| Format | Material allowance | Category choice | Delivery timing | Main tradeoff |
| --- | --- | --- | --- | --- |
| Concentrated | Three baseline allowances | One group | At commitment | Concentrates the largest single-category reserve |
| Combined immediate | 1.8 baseline allowances in each consignment | Two different groups | Both together after the second selection | Provides a 20% larger total allowance than concentrated delivery, with greater absorption pressure. Unusual-family caps still limit actual cargo |
| Combined staged | 1.5 baseline allowances in each consignment | Two different groups | First at commitment, second after the quoted staging delay | Preserves a large mixed shipment while reducing the immediate load |

The second selection cannot repeat the first group.
If every distinct second group becomes illegal before any delivery, return the offer to format selection without consequences.
Preserve its allowance, frozen profiles, unusual family, origin, and deadline.
If only one legal group remains, concentrated delivery can be confirmed through a fresh quote.
Once any material has arrived, correction follows the original same-group remainder contract and cannot restart the format.
Both selections are made before either part of a combined format is released.
After the last required selection, a native confirmation shows the complete immutable delivery quote.
Its first option cancels without consequences, and its second option confirms the actual grant.
A single-category choice uses the same confirmation.
Cancelling returns to the existing offer without changing its frozen family, quantities, or format.
While that confirmation is visible, expiry records a pending automatic-resolution request and waits for the popup to close.
It never overwrites the visible quote or grants a competing package.
After the popup closes, an expired still-uncommitted offer resolves through the common automatic path.
The staged format records both exact consignments at commitment.
Its second cargo arrives automatically, with its original models and quantities.
The country does not pay again or select again.

The staging delay uses one deterministic pass.
Start with 15 days and subtract five days when the first consignment is the transport or maritime-logistics profile.
Using that provisional schedule, calculate the greater projected R for its two arrivals under Part 3.
If that provisional maximum is greater than three, add five days.
Clamp the result to 10 through 20 days, then freeze the schedule and calculate the final binding quote.
Do not iterate the delay again when the final schedule changes the load window.
A combined staged delivery contributes only 75% of its value to the handling calculation for each arrival, representing planned unloading and distribution.
This reduces pressure without reducing the real equipment received.
The immediate format receives its larger total allowance because the country accepts concentrated delivery work.

A timed-out format uses the AI's format decision.
A timed-out combined offer preserves any already selected first group and chooses the best different second group.
The player can never gain a free first consignment by abandoning the second selection.

## Choices after Impossible Arsenals

An Evolution II offer retains the three formats and the conventional groups.
It can add one unusual-cargo group, bringing the maximum number of simultaneous category actions to six.
That group contains one specific existing Chaos Redux equipment family, selected and frozen when the offer is created.
The player sees its exact stock, complementary equipment, available fielding route, recruitment needs, and possible temporary setback.
The two-category formats can combine this group with one conventional group.

Unusual equipment remains physically real after any setback expires.
The receiving country gains the finite material and the narrow consumer access needed by the accepted fielding contract.
Its scientific projects, production capabilities, and originating event history keep their own progression.
Part 3 provides the complete family and setback design.

## What the player follows

The category keeps two event-specific persistent displays: the current offer's remaining selections and the current handling condition with its latest relevant expiry.
The current offer date, exact deadline, selected delivery format, and next staged arrival are contextual receipt information.
Equipment quantities are ordinary stock and manifest data.
There is no spendable event currency.

The category disappears when no selection, scheduled delivery, or handling condition remains.
A compact delivery receipt remains available through the shared Event Log detail.
It records the receiving country, firing, evolution, format, selected groups, delivered quantities, automatic-selection status, and any actual setback.
The global history records the universal firing once.
National receipts explain each country's outcome without adding a second global firing.

## Campaign consequences

A successful choice changes what the country can equip, reinforce, or reserve through normal military systems.
It can redirect ordinary production planning without providing free fuel, trained personnel, experience, factories, or operational orders.
The player has an immediate reason to inspect shortages and a later reason to revisit force composition.
Repeated firings give new choices from changed circumstances and equipment access.

Overflowing Arsenals turns this into a capacity decision.
A country can concentrate on an urgent shortage, take a wider simultaneous windfall, or stage the mixed load.
Impossible Arsenals adds unfamiliar military possibilities and a clear temporary handling risk.
The ordinary categories remain useful at every stage, including for countries that value predictable reinforcement more than a new specialist formation.
