# BOOM

## Catalog entry

- Event ID: `47`
- Event name: BOOM
- Type: Minor Repeatable
- Status: To Be Reworked
- Chaos level: 1
- Cluster: Various Anomalies, pending a stable cluster ID
- Member severity: Severe

## Event promise

One state is destroyed by an explosion with no known source. The event never identifies an attacker, weapon owner, launch point, scientific cause, supernatural cause, or later solution. Governments may investigate, accuse, deny, and speculate in the writing, but the event itself never confirms any theory.

The blast resembles a very large thermonuclear detonation. That resemblance belongs to the visual presentation. The event does not use the nuclear-strike mechanic and does not create any of the records or consequences tied to nuclear weapons.

BOOM is intentionally direct. The player sees the location, the blast occurs, the damage is applied, reports reach the affected countries and the wider world, and the incident closes. A later firing starts a separate incident.

## Incident lifecycle

Each Event 47 firing follows one bounded sequence:

1. Determine the active blast profile from enabled evolution state.
2. Build the complete pool of eligible primary states.
3. Select all required epicenters before any damage is applied.
4. Build and freeze every blast ring for every epicenter.
5. Resolve overlap so each state receives one final intensity zone.
6. Move each human player's camera to the first epicenter that their client is meant to observe.
7. Play the standalone mushroom-cloud effect at the first epicenter.
8. Apply the first epicenter and regional damage package.
9. Show the first incident report.
10. Resolve later epicenters under Evolution II without moving the camera again.
11. Send bounded location reports for later epicenters.
12. Send one global soundwave report to each normal country for the incident as a whole.
13. Commit one Event History entry and one repeatable-event pacing transaction for the Event 47 firing.
14. Clear every temporary target, ring, overlap, report, and receipt value owned by the incident.

The sequence is atomic from the event system's point of view. Two or three explosions under Evolution II still count as one Event 47 firing.

## Primary-state eligibility

Selection is state-based and uniform across the final eligible pool. The event must not select a country first and then select one of that country's states, since that would overrepresent small countries and underrepresent large countries.

A primary state is eligible when all of these conditions are true:

- It is a valid land state with an owner.
- Its owner currently uses ordinary civilian systems.
- The state has at least 25,000 civilian population before the event applies its protected floor.
- The state can safely receive real population loss and building damage.
- It is not inside a temporary map, transfer, or lifecycle state that makes ownership, population, or building mutation unreliable.
- It is not already selected as another primary state in the same incident.

War status, ideology, faction, major status, player control, continent, and diplomatic alignment do not change ordinary eligibility or selection weight.

A human special country remains eligible when it uses normal civilian systems. A country that is currently nonhuman is excluded from primary selection because ordinary civilian mass-casualty reporting does not fit its population model.

The 25,000 population threshold is a tuning anchor. It prevents the primary selector from wasting an enormous global incident on an almost empty state. The final value should be centralized and tested against the current map.

## Repeat target rules

Every firing rebuilds its pool from the current world. Past Event 47 targets receive no permanent immunity and no extra weight.

A later incident may hit:

- the same country again
- the same continent again
- a state adjacent to an earlier target
- the same state again when it still meets the eligibility contract

No persistent BOOM target ledger is needed beyond Event History and ordinary Deaths records.

## Frozen blast geometry

The baseline blast contains two zones:

- Epicenter: the selected primary state
- First ring: every directly adjacent land state

The first ring is deduplicated before any effect begins. Sea adjacency, invalid map links, impassable non-state areas, and duplicate paths do not create extra applications.

All geometry is frozen before damage starts. Destruction, ownership changes, capitulation, unit loss, or population reduction caused by the first state must not change which states receive the remaining effects.

A neighboring state's civilian mortality applies only when its owner uses normal civilian systems. Building and force disruption can still apply to a valid neighboring state whose owner uses a different civilian model, provided those mutations are safe for that state.

An island or isolated state with no valid land neighbor still receives the full epicenter package. The event does not search for a substitute first ring.

## Civilian mortality contract

Civilian deaths remove real state population. A country manpower penalty, recruitable-population modifier, local manpower modifier, casualty estimate, or BOOM-only counter does not satisfy this requirement.

For every affected state:

1. Read current civilian population.
2. Calculate the requested loss from the final blast zone and local dynamic factors.
3. Clamp the request against the protected remaining population floor.
4. Call the shared exact state civilian population loss transaction.
5. Read the amount actually applied.
6. Register that same applied amount once through Deaths with the Event 47 cause.
7. Use the applied amount for incident totals and reports.
8. Commit a state receipt so the incident cannot debit that state twice.

The protected minimum remaining population is 1,000. This preserves a valid state population floor while allowing the blast to destroy almost the entire population of a small state.

### Baseline mortality

| Zone | Starting mortality band | Dynamic adjustment | Hard maximum |
| --- | ---: | ---: | ---: |
| Epicenter | 55% to 75% | Up to 5 percentage points for very high population and urban concentration | 80% |
| First ring | 8% to 18% | Up to 4 points for urban concentration and up to 4 points of reduction from strong terrain shielding | 22% |

The random point inside each band is rolled once per state. Local adjustment is applied after the band roll and before the protected floor.

High population and urban concentration increase the proportion exposed because dense settlement and connected infrastructure place more people inside the destructive footprint. Strong mountain or severe terrain shielding can reduce first-ring losses. It never reduces epicenter mortality below the rolled baseline.

Owner ideology, war status, industrial strength, and military power do not protect civilians from the opening blast. Existing event-specific or shared civilian protection may reduce losses only when that protection explicitly applies to sudden blast exposure and can do so without importing nuclear fallout logic.

## Building destruction contract

BOOM damages levels that already exist. It never creates buildings, converts destroyed capacity into another type, or applies a generic country penalty as a substitute for state damage.

Damage is based on the current built level of each valid building family. A building type with zero levels receives no transaction. Every fractional result is rounded through one consistent rule and capped at the levels present.

### Baseline building damage

| Building family | Epicenter damage share | First-ring damage share |
| --- | ---: | ---: |
| Infrastructure, railways, supply nodes and routes | 70% to 100% | 20% to 45% |
| Civilian factories, military factories, dockyards, refineries, synthetic plants | 60% to 90% | 15% to 35% |
| Airbases and naval bases | 60% to 90% | 20% to 45% |
| Anti-air, radar, land forts, coastal forts and other valid strategic buildings | 50% to 85% | 20% to 45% |

Rail and supply damage is a hard part of the event. If the engine cannot safely damage one named infrastructure family through the current supported route, implementation must report that family as blocked. A silent replacement with a country modifier is not acceptable.

Terrain may reduce first-ring building damage slightly where the physical barrier is relevant. It does not protect communications, rail links, or exposed regional networks from all shock damage.

## Military forces inside the blast

The event disrupts forces physically present in affected states. It does not damage a country's whole army and does not choose frontline formations outside the blast zone.

### Baseline land-force effect

| Zone | Strength loss | Organization loss |
| --- | ---: | ---: |
| Epicenter | 35% to 60% | 70% to 100% |
| First ring | 8% to 20% | 30% to 60% |

Strength loss represents personnel, weapons, vehicles, local depots, and command elements caught in the blast. Organization loss represents broken communications, panic, blocked roads, lost officers, and unit separation.

Military deaths enter the shared Deaths system only when the engine provides an exact observed personnel-loss value. The event must not infer military deaths by multiplying division strength percentages by a guessed manpower total. When exact accounting is unavailable, the gameplay disruption still applies and no invented military-death number is recorded.

Air and naval forces are affected primarily through damage to their bases and local infrastructure. Direct destruction of aircraft or ships is allowed only if the implementation finds a safe state-local engine path that provides exact scope and avoids country-wide loss.

## The nonnuclear isolation contract

The BOOM effect must remain isolated from every nuclear system. The incident does not:

- consume nuclear stockpiles
- call a nuclear launch or detonation effect
- name a nuclear attacker or victim relationship
- increase nuclear-use history
- create nuclear condemnation
- create fallout
- create Air Cleanliness pressure
- trigger nuclear war logic
- trigger nuclear diplomacy or retaliation
- satisfy nuclear achievements, decisions, focuses, missions, or scripted checks
- appear in a nuclear responsibility ledger

The event may use a standalone visual asset that resembles a thermonuclear mushroom cloud. If the only available visual route requires calling the nuclear gameplay path, the visual is blocked until a safe standalone route is available.

## The sound heard around the world

One impossible pressure wave is reported across the planet for each Event 47 firing. Under Evolution II, the several explosions belong to one incident and create one global soundwave report per country.

The soundwave is presentation. It can mention pressure instruments, shattered windows, microphones, animals, distant thunder, ground vibration, or brief atmospheric changes. It applies no global combat penalty, stability loss, war support loss, production penalty, or permanent modifier.

The event gives the world knowledge of the blast without giving it an explanation.

## Incident closure

After the last report, Event 47 leaves only ordinary world consequences:

- reduced state population
- damaged buildings
- disrupted or weakened local formations
- Deaths records
- Event History
- any later famine, migration, occupation, supply, or war effects that naturally follow from the changed world

There is no BOOM meter, investigation value, recurring modifier, reconstruction category, source hunt, or hidden cause progression. The repeatable event can return through its normal weight and cap rules.
