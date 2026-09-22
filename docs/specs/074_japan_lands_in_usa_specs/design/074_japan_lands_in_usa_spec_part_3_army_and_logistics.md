# Part 3: The army, stockpiles, and limited special support

## Opening force

The package supplies newly created forces and their initial equipment and manpower.
It does not transfer an existing Japanese army out of China or remove equipment from Japan's pre-event formations.
The opening must work when Japan has no spare manpower, little fuel, and almost no navy.
The extra resources are an intentional event grant, accounted for once.

All figures below are proposed tuning anchors.
They require supply, combat, performance, and AI tests on the installed game.
The design does not claim that these numbers already produce a balanced campaign.

| Force element | Baseline | Pacific Army | The Western Invasion | Invasion of America |
| --- | ---: | ---: | ---: | ---: |
| Line infantry divisions | 20 | 40 | 65 | 100 |
| Assault infantry divisions | 5 | 10 | 20 | 30 |
| Mobile divisions | 5 | 10 | 15 | 20 |
| Immediate total | 30 | 60 | 100 | 150 |
| Additional finite follow-on divisions | 10 | 15 | 25 | 30 |
| Lifetime division ceiling before campaign scaling | 40 | 75 | 125 | 180 |
| Fighters, including unbased reserve aircraft | 200 | 400 | 700 | 1,000 |
| Close-air-support aircraft, including reserves | 100 | 200 | 400 | 600 |
| Maximum special-support age from the original landing | 180 days | 240 days | 300 days | 360 days |

The immediate total is present at the opening.
The follow-on allowance is separate and never substitutes for missing initial divisions.
Higher-tier armies have more assault strength and several usable directions of advance, but they remain ordinary armed forces that take losses.

## Bounded campaign adjustment

Freeze one campaign-scale factor when the event successfully commits.
Use the United States' total deployed division count at that moment, not its current coast garrison and not Japan's current strength.
Begin at a factor of 1.00 for 100 American divisions or fewer.
Add 0.05 for each complete additional 50 divisions, up to a hard maximum of 1.50.
This is a coarse late-campaign adjustment, not an estimate of combat power.

Round the scaled immediate and lifetime division totals to the nearest five, with exact half-way ties rounded upward.
Allocate the immediate total across the three roles while preserving that total, using the original role proportions and batches of five.
Round ordinary stockpile grants to useful fixed lots, and never round a positive infantry or artillery grant to zero.
Structural values such as port counts, formation composition, and the number of army groups do not need artificial multiples-of-five rounding.

The factor remains frozen for every later evolution and reinforcement calculation.
The player cannot increase the grant by raising American divisions after the landing, moving a garrison, destroying Japanese ships, or deliberately emptying a stockpile.
Equipment quality follows the validated campaign-era and available equipment profile.
It does not receive a second independent army-size multiplier.

At the maximum factor, the opening totals are 45, 90, 150, and 225 divisions.
The maximum lifetime ceiling is 270 divisions at tier III.
These are ceilings for this event's grants, not a restriction on Japan's ordinary recruitment.

## Formation quality

Line infantry is a solid, supply-conscious formation built from ordinary infantry with artillery and support services where the selected package supports them.
Assault infantry adds artillery weight and useful engineers, antiaircraft support, or logistics within a validated ordinary template.
The mobile component provides exploitation and rapid corridor defense without making the entire army dependent on trucks and fuel.

Do not use mass special-forces formations as a shortcut around national special-forces limits.
Do not create a new custom battalion, equipment family, model, or counter for an army that can use existing ordinary Japanese assets.
A base-game formation set must provide the complete baseline and all three tiers.
DLC variants may improve presentation or equipment choice only after their actual prerequisites and consumers are checked.

New divisions begin fully staffed and equipped, at full organization, with a trained or experienced opening profile.
Proposed experience anchors are 25, 35, 45, and 55 percent of the native creation experience scale, subject to checking what those values mean in the current engine.
If a creation field cannot directly provide the promised readiness, the implementation must establish that readiness through a verified method before the event is accepted.
Do not hide a zero-organization opening behind a report describing veteran troops.

For exceptional saves in which Japan has lost normal technologies, choose a validated ordinary grant-only equipment and template profile.
Do not restore the country's whole research tree, reset a Research Failure, or grant current American technology wholesale.
Any infantry-heavy low-technology profile must retain the promised combat role and be separately tested.
An untested removal of artillery or transport is a simplification, not an approved equivalent.

## Embedded equipment and national reserves

Compute the exact manpower and equipment carried by the generated formation set from its verified templates.
Keep that embedded manifest separate from loose reserve equipment.
The spawning method must prove whether it consumes national pools or creates carried equipment directly.
Compensate only an actual debit and never grant the same embedded requirement through both paths.

The following loose reserve table is additional to the carried equipment in the new army.
It is the lifetime ceiling for this component at the active tier, not a recurring monthly grant.

| Loose reserve | Baseline | Pacific Army | The Western Invasion | Invasion of America |
| --- | ---: | ---: | ---: | ---: |
| Infantry equipment | 20,000 | 45,000 | 80,000 | 125,000 |
| Artillery | 2,000 | 4,000 | 7,500 | 12,500 |
| Support equipment | 3,000 | 6,000 | 10,000 | 16,000 |
| Trucks | 1,500 | 3,500 | 6,000 | 10,000 |
| Trains | 25 | 50 | 75 | 100 |
| Convoys | 150 | 300 | 500 | 750 |
| Fuel | 200,000 | 450,000 | 800,000 | 1,250,000 |
| Additional replacement manpower | 25% of opening formation manpower | 30% | 35% | 40% |

Deliver 60 percent of each loose reserve allowance with the opening and retain 40 percent for bounded follow-on releases through working access.
The retained share is divided into four equal lots nominally due on days 30, 60, 90, and 120 from the landing.
A due lot waits for working access and expires if support closes.
After an active evolution, recalculate the cumulative amount due at the episode age, subtract material already issued, and issue only the positive difference through legal access.
No production or combat loss increases that difference.
Round indivisible items consistently and assign the remainder to the retained portion so the lifetime ceiling is exact.
Replacement manpower is a national grant and must be described that way.
Convoys are ships in the national pool, not proof of an operational supply route.

Japan can use national reserves in another theater.
That is an engine and player-choice consequence of national stockpiles.
The front's guaranteed opening strength comes from the fully prepared army and local support, not an invented claim that those national reserves are ring-fenced inside American warehouses.

## Air support

Base aircraft only at airfields that Japan can actually operate and that have safe available capacity.
Increase or repair legal airfield capacity inside the footprint when necessary, within the normal building cap.
Keep excess aircraft in the national reserve until a usable field becomes available.
Never place the whole tier III air package into a small airfield and count the resulting overcrowded wings as effective support.

Use valid fighter and ground-support configurations for the active game and DLC set.
Do not create a bare aircraft archetype that the current designer system cannot deploy.
The intended opening mission mix is air superiority over the occupied coast and close support over the active front.
Japan's aircraft still depend on normal range, weather, fuel, airfield access, and enemy interception.

## Command and organization

Reuse available Japanese commanders and their existing identities.
The AI should assign capable leaders to the new armies and organize the tier II and III force into several armies with a sensible army-group structure.
Higher tiers should receive priority access to better available commanders and sufficient ordinary command resources to organize the larger theater.

Do not duplicate a named officer, revive a dead character, change the head of government, replace a portrait, or forcibly strip a human player's existing army of its commander.
For a human Japan, present the force clearly enough that it can be assigned without hunting through unrelated units.
The force must remain functional when no named commander is available.
Commander availability never becomes a strategic event gate.

## Physical bridgehead preparation

Every detached initial pocket needs a working access point, legal unit positions, sufficient local distribution, and a route from the port toward its first front.
Prepare ports and existing transport infrastructure once at landing.
Repairs and new construction remain real map changes and can later be damaged or captured.
Do not periodically restore their levels or erase damage caused by the United States.

Choose port and supply capacity from the actual demand of the issued formations.
The initial supply test should accommodate the opening army with modest headroom when Japanese overseas supply has been deliberately disabled.
That headroom is a design acceptance target, not a guessed modifier value.
The implementation must measure supply reach and distribution, not just add a large number to a state and assume it reaches every division.

Maintain support only in the recorded Japanese operating area.
It must not improve the supply of American defenders, neutral occupiers, or Japanese armies in Asia.
Partial-state control is an important test because a state-wide controller modifier can behave differently from a unit-specific benefit.
Use only a proven scope and remove support when the qualifying control is lost.

## Support taper

For the first 30 days after each pocket is established in the initial bundle, the special local contribution is at its full validated level.
It falls to 75 percent during the next 30 days and 50 percent after that, ending at the tier's absolute support age.
An active evolution can raise the authorized level and extend the absolute expiry to its higher tier, but it does not reset the original landing date or begin a fresh opening grace period.
New districts conquered in ordinary combat receive normal supply and may benefit from a paid transport project, not an automatic copy of the strongest landing subsidy.

The army never becomes immune to supply or encirclement penalties.
The temporary contribution exists to make the exceptional arrival credible, while the taper makes continued conquest depend on infrastructure and player decisions.

When a disconnected pocket loses all working access, pause its remaining deliveries immediately.
Its remaining local contribution tapers to zero over seven days.
Access restored through normal combat within 30 days can resume only its unspent allowance and remaining time.
After 30 continuous days without any working Pacific access for the expedition, special support ends permanently for the episode.
The surviving army remains in play.

## Follow-on force

Release the finite follow-on allowance in batches of five divisions, normally no more frequently than once every 30 days after the previous request.
The first request becomes available after the initial 30 days.
Mission J-M1 may once bring the next request date forward by 15 days, never before its own completion and never before day 15 of the episode.
This is the only permitted timing exception and does not shorten the ten-day organization period.
Each batch requires a retained working access point with room and supply, or a land connection from the receiving district to such a point.
The player can call it through a decision and the AI has a high willingness to do so when the condition is useful.
A consolidation mission can advance the availability of one still-unissued batch, but cannot add to the lifetime ceiling.

Ordinary follow-on formations are issued ready to fight using the same embedded-equipment accounting as the opening.
Unused deliveries expire when special support ends.
They are not refunded as an extra national army or transferred to Japan's home islands.
Losing a port does not trigger a compensating landing somewhere else.

## Permanent consequences

Captured and constructed buildings remain ordinary map assets after special support ends.
The new divisions and issued equipment remain normal Japanese property unless normal game rules remove them.
Temporary landing support and reserved future deliveries end at support closure.
Paid field operations and mainland AI priority can continue while the actual front remains, as defined in Part 5.
Their eventual campaign cleanup is separate from the end of exceptional supply.
Do not delete surviving divisions or remove unrelated Japanese equipment to approximate a return to normal war.
