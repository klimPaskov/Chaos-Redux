# Equipment Choice
## Part 6. Difficult military achievements

The three achievements reward using the shipment opportunity to solve a military problem or sustain unfamiliar formations.
They require natural deliveries, human control, valid country identity, and exact material receipts.
Their working titles below guide the final naming and artwork.
Final localisation is authored during implementation.

All three achievements are visible in the shared achievement list from the beginning of an eligible campaign.
Their estimated design difficulty is Hard for EC-ACH-01, Hard for EC-ACH-02, and Very Hard for EC-ACH-03.
The estimates reflect the required battlefield and multiple-shipment conditions and are not measured completion rates.
The shared achievement framework remains the authority for global eligibility, game settings, and registry placement.
Manual, forced, and test-country deliveries never qualify.
A receipt preserves that origin through country relays, timeouts, staged arrivals, and recovery from partial delivery.
A country passing to AI control or a player switching away from the tracked country invalidates its active challenge.
An ordinary government or cosmetic tag change with the same identity preserves it.

## EC-ACH-01. Rearmed under fire

Proposed registry ID: `123_equipment_choice_rearmed_under_fire`.

Start a challenge from a naturally delivered infantry, fire-support, or armoured package while the receiving player country is at war.
The selected primary equipment family must have had a verified fielded deficit of at least 25% at the offer snapshot.
Freeze the original deficit and war context at offer creation for eligibility.
Capture the fielded baseline immediately before the first successful physical delivery of the tracked primary row, then record the actual final primary-family grant, recipient identity, and completed-delivery date.
A zero-delivery attempt does not establish that baseline.
Define one battalion equivalent from an existing compatible battalion's actual need for that primary family and freeze that reference need.
The original deficit and final grant must each contain at least one such battalion equivalent to open the challenge.
A transport-only or reserve-only package cannot open the challenge.

Within 90 days of completed delivery, the country's fielded amount of the tracked family must grow by at least the greater of one frozen battalion equivalent and the rounded-up smaller of 25% of the actual grant or 50% of the original deficit.
While that threshold is met, win a land battle with a commanding army that contains the tracked equipment family.
Use the native victorious-army or commander-army callback and verify the actual compatible equipment in that army.
The country must still be at war and still controlled by the same eligible player.

The condition demonstrates receipt, restored fielded capacity, and a relevant battlefield result.
Equipment is fungible, so the achievement does not claim serial-level proof that a particular gifted rifle fired in that battle.
Stockpile decline, lend-lease, production alone, another army's victory, or a battle before the fielded threshold cannot complete it.

Icon direction: a repaired field equipment ledger beside a substantial, visible rifle-and-gun consignment, with one clear campaign ribbon motif.
Use an original compact subject that reads at 64 by 64.

## EC-ACH-02. Two services, one delivery

Proposed registry ID: `123_equipment_choice_two_services_one_delivery`.

Start from a natural combined immediate offer at Overflowing Arsenals or Impossible Arsenals.
Choose two distinct land-combat groups from infantry and support, fire support, and the armoured mobility profile.
Both consignments must complete under the same firing and recipient receipt.
Their primary families must be distinct.
Record each primary family's fielded quantity immediately before its first successful physical row delivery and record its actual final grant.
Freeze one existing compatible battalion-equivalent equipment requirement per primary family.

Within 120 days, field at least the greater of one frozen battalion equivalent or the rounded-up 25% of each actual primary-family grant above the corresponding recorded baseline.
Then win a land battle with a commanding army containing both tracked families after all Event 123 handling components caused by this delivery have expired.
A later unrelated handling component does not erase the original expiry proof, while a repeated callback cannot fabricate it.
The challenge tests a large mixed reserve, actual integration, and a successful battle after its own handling burden ends.

The challenge cannot be completed by receiving two separate firings, choosing a transport-only profile, trading the supplies away, or merely possessing two national stockpiles.
Both fielded thresholds are checked at the victorious-army callback.
A partially delivered second category remains incomplete.

Icon direction: two distinct supply columns meeting at a single military formation emblem, with rifles and artillery or armour represented through a clean paired composition.

## EC-ACH-03. Army of borrowed impossibilities

Proposed registry ID: `123_equipment_choice_borrowed_impossibilities`.

Receive two different adopted unusual families through two separate natural Equipment Choice firings while lacking the corresponding owner production permissions at both delivery snapshots.
Both must use valid complete cargo and fielding receipts.
The first completed family opens a 365-day challenge window.
The second must arrive and be fielded before that window closes.

Within the window, win a land battle with a commanding army containing at least one existing neutral-template equivalent of each tracked family's equipment needs.
Check every unusual and ordinary row required by those two template equivalents.
Either prove the two compatible formations separately, or form one aggregated victorious-army requirement vector that sums duplicate equipment types across both families.
For robots and paleogenetic creatures, the combined requirement includes 120 support equipment.
Two independent tests against the same 60 support equipment cannot satisfy that vector.
Apply the same no-double-counting rule to any shared rows in the other achievement checks.
Both families must remain outside their owner production permissions at the qualifying battle.
The country may use its finite stock through normal reinforcement and training, and it must supply the required personnel and time.

This achievement requires two natural opportunities, two actual specialist forces, mixed military use, and a victory without converting the gift into a research or production unlock.
A single unusual package, an Event 042 receipt without an Event 123 delivery, owner technology obtained before the qualifying battle, or a country-wide stock count cannot complete it.
If a shared battlefield query cannot prove the exact two-family equipment requirements in the victorious army, this achievement remains blocked for implementation until a truthful evidence contract exists.
Do not weaken it to a generic battle victory.

Icon direction: two recognizable existing unusual equipment motifs around a single finite supply crate, with a disciplined military composition and no invented faction insignia.

All three achievements depend on a verified victorious-army or commander-army callback and a truthful equipment query.
Treat that shared battlefield-evidence contract as an implementation acceptance gate for all three.
An unavailable query cannot be replaced by a generic national stockpile or unrelated battle-victory condition.

## Tracking and expiry

Use separate challenge records for the three achievements.
A later offer cannot overwrite an active qualifying record.
The original challenge may continue, and a later eligible receipt may open a new attempt after an earlier attempt expires.
At most one active attempt per achievement and country is necessary.

Achievement windows include the completed-delivery timestamp and the exact deadline timestamp.
An expiry callback closes a record only after that deadline, so callback ordering at the deadline cannot preempt an otherwise qualifying battle.
Start, update, finish, and expire records through the relevant delivery, handling-expiry, battle, player-control, and country-lifecycle hooks.
A country-owned expiry callback is sufficient for each active attempt.
There is no achievement-specific periodic world scan.
Record exact disqualification reasons for developer review and keep achievement outcome idempotent.

Keep the three full-colour achievement subjects distinct.
For each, generate aligned completed, grey, and not-eligible outputs using the existing achievement templates and deterministic overlay pipeline.
The achievement prompt and source evidence describe the actual validation limits.
