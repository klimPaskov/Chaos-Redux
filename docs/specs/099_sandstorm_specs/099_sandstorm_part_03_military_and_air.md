# Sandstorm: military and air consequences

## Combat identity

The storm makes armed forces lose usable visual reference.
Scouts struggle to identify opposing positions, commanders lose track of friendly formations, and units cannot reliably read roads, landmarks or the direction of an assault.
Defensive lines become harder to recognize and support.
Artillery observers cannot confidently identify targets or correct fire.
Radio can carry an order while the recipient still cannot establish where to go or where friendly troops are.

The result is a strong reduction in the ability to turn existing manpower and equipment into effective coordinated action.
The storm does not grant a generic defensive advantage.
Both attacking and defending forces suffer, including defenders firing at approaching troops and attackers operating from an adjacent clear state into an obscured battle area.
Ground already held may remain strategically valuable, but the weather itself does not make its defenders more accurate or better coordinated.

## Ground-force balance targets

The table specifies proposed combined observable changes attributable to Sandstorm at full local exposure.
These are outcome targets relative to comparable clear conditions, not promises that identically named engine modifiers exist in state scope.
Partially covered engagements and short transits receive appropriately reduced exposure.
The implementation must account for native weather and shared effects before adding its own contribution.

| Capability | Weakening | Normal | Severe | Extreme |
| --- | --- | --- | --- | --- |
| Coordination effectiveness | −20% | −45% | −70% | −85% |
| Useful reconnaissance | −30% | −60% | −80% | −95% |
| Planning acquisition | −25% | −50% | −75% | −90% |
| Effective use of an existing plan | −15% | −35% | −60% | −80% |
| Ground movement | −15% | −35% | −55% | −70% |
| Organization recovery | −20% | −50% | −75% | −90% |
| Effective attack output for both combatants | −15% | −40% | −65% | −80% |
| Effective defense and breakthrough | −10% | −20% | −40% | −55% |

Coordination, reconnaissance and planning are distinct tactical consequences even if the engine eventually requires a carefully documented combination of local consumers to express them.
The final battle and unit tooltips must explain the actual effects implemented.
A map tint or a national intelligence penalty alone cannot fulfill those requirements.
The code handoff treats unresolved local scope as a release gate.

## Organization during exposure

Poor navigation, separation, repeated stops and failed contact slowly erode current organization while a formation remains exposed.
The initial drain targets 0.5, 1.5, 3 and 5 percentage points of maximum organization per exposed day from weakening through extreme conditions.
Movement and active combat raise this weather drain by up to 50 percent.
Stationary organized shelter reduces it by up to 30 percent when a verified local response applies.
Weather drain stops at ten percent of the unit's own maximum organization.
Combat and ordinary game systems can still take the unit below that level.

The weather operation only lowers current organization.
It cannot set a unit to a fraction that heals one already below the target.
It also cannot delete all organization on first contact.
Duration integration makes a six-hour transit less disruptive than three days spent under a severe wall.
When the storm leaves, the drain and recovery penalty end.
The organization already lost recovers normally and is never restored from a pre-storm snapshot.

## Movement, routes and supply

Movement penalties follow the affected ground.
Troops should be able to leave the front, although escape may be slow.
Strategic redeployment becomes unreliable inside the strongest sections, with any restriction limited to the actual covered area and verified native behavior.
The implementation should preserve a usable way to retreat and avoid creating an accidental permanent movement lock.

Storm supply disruption is local and combines obscured roads, buried access points, reduced loading, damaged rail segments and vehicle maintenance.
The baseline local supply-throughput loss targets 15, 35, 60 and 80 percent across the four intensity bands.
A marked essential corridor recovers part of the weather-related loss at real cost.
It does not repair destroyed rail levels or ignore enemy control and capacity rules.
The supply owner continues to determine how local damage propagates beyond the storm.

Dust can increase equipment wear and ordinary attrition where the native consumer supports local, nationality-neutral application.
The initial extra equipment-attrition target is modest in weakening conditions and serious after several severe days, with a maximum combined Sandstorm increment of five percentage points before protection.
This is a secondary military consequence.
It must not become an additional scripted military death pool duplicating the game's normal losses.

## Which forces are affected

Weather exposure includes the state's controller, occupier, owner when operating there, allies, enemies and permitted neutral transit.
Country allegiance does not confer visibility immunity.
Orders purchased by one country improve only that country's eligible forces and carry the specified sacrifice.
They do not remove the underlying storm from opponents.

A division partly crossing the ribbon receives the actual available geographic exposure estimate.
An attacker outside the affected state still needs the penalty associated with fighting into its obscured target area.
A defending unit that is also covered must not receive two complete weather bundles from the same battle.
Forces elsewhere under the same general remain unaffected.
Occupied states are a mandatory validation case because owner-relative and controller-relative modifiers can disagree there.

## Air operations

Low visibility and uncertain navigation reduce practical detection, interception, close support, bombing accuracy, reconnaissance and safe takeoff or landing.
Dust ingestion threatens engines and systems at exposed bases and during affected flights.
The qualitative visibility and ingestion hazards follow the [primary aviation research](099_sandstorm_research_and_evidence.md#r2-particle-behavior-sight-and-aviation).
These effects follow the actual operating area and airfield exposure.
Both sides flying in that area suffer.

| Air capability | Weakening | Normal | Severe | Extreme |
| --- | --- | --- | --- | --- |
| Effective mission output | −25% | −55% | −80% | −95% |
| Detection and target acquisition | −20% | −50% | −75% | −90% |
| Weather-related accident rate relative to the comparable clear baseline | ×1.25 | ×2 | ×3.5 | ×5 |

The accident figure is a multiplier on an observed comparable baseline, not a percentage of the entire national aircraft stock destroyed each day.
The delivered tuning must apply a meaningful per-operation or per-exposed-wing bound and demonstrate it with actual sorties and losses.
Only planes that fly through affected operating areas or use affected airfields qualify.
A zero clear-weather accident baseline requires a reviewed native interpretation rather than multiplying zero and claiming increased risk.

Air coverage projects the same moving footprint onto relevant strategic regions and airfields.
Where native region resolution is coarser, the contribution must reflect the covered portion and be described honestly.
Aircraft operating wholly outside the footprint retain their ordinary conditions.
Ocean dust must affect air operations over the sea as well as subsequent landfall.
The implementation cannot satisfy this with a country-wide air penalty that also damages unrelated fronts.

Existing radar and navigation aids may preserve some capability, but they do not make dust physically transparent or remove engine ingestion.
Night and other native weather interactions need combined floors so additive modifiers do not produce negative efficiency or unintended immunity.
The extreme air-output target leaves only a small practical residual rather than guaranteeing that every flight crashes.

## Counterplay and limits

Field command preparation preserves some coordination and organization by accepting slower, more cautious movement.
Machinery and airfield preparation protect equipment by reducing use and committing maintenance capacity.
Mask issue can reduce the bodily and respiratory component of military exposure if the shared owner provides a valid dust interpretation.
It does not restore reconnaissance, visual identification or attack accuracy.

The player may choose to exploit an opponent's dependence on air support, time a withdrawal or avoid an offensive until the wall clears.
Those are strategic uses of a shared hazard.
The design should not deliberately help the initiating country, reveal hidden enemy plans or award combat statistics for weather damage.

## Military acceptance scenes

One battle must compare both combatants before, during and after exposure, including an attacker starting outside the affected state.
Another must use an occupied state with a different owner and controller and allied forces present.
A moving unit must enter and leave without carrying the penalty to a distant theater.
A low-organization unit must never gain organization from the exposure operation.
Air evidence must compare missions wholly outside, partly inside and wholly inside the same land and sea footprint for both sides.
Existing weather, native battle losses and storm-specific contributions must remain distinguishable in that evidence.
