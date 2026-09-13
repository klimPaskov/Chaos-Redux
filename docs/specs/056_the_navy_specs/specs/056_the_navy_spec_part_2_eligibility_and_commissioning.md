# Event 056: Eligibility and Commissioning

## Recipient eligibility

A country qualifies for the current firing when all of these conditions are true:

- the country exists as an active country scope
- it directly owns and controls at least one coastal state
- the coast can support a legal naval commissioning location
- the country can participate in ordinary naval warfare under its owning systems
- the country has not already been processed during the same firing

Direct control matters. A landlocked overlord does not qualify merely because a subject owns ports. A government in exile does not qualify through an occupied homeland it cannot use. A country with a subject-owned coast waits until it directly gains usable coast or the subject receives its own package.

## Usable coastline

A usable coastline is a directly owned and controlled coastal state that meets one of two conditions:

1. It contains a functioning naval base that can receive the package.
2. It can host a limited emergency commissioning facility without producing an invalid or absurd placement.

The second route exists for countries that genuinely have coast but no completed naval base. It does not turn an inland country into a recipient.

A coastal state is rejected when it is under enemy control, trapped inside an invalid occupation state, currently unsuitable for ship creation, or otherwise unable to host the fleet safely.

## Country edge cases

| Country situation | Result | Design reason |
| --- | --- | --- |
| Ordinary coastal major | Eligible | It participates normally and receives one package. |
| Ordinary coastal minor | Eligible | Small size does not remove the event's premise. |
| Island country with at least one usable port | Eligible | Island status is a normal naval case. |
| Country with coast but no naval base | Conditionally eligible | A bounded emergency facility can support delayed commissioning. |
| Fully landlocked country | Ineligible for this firing | It can qualify after directly gaining coast. |
| Landlocked overlord with coastal subject | Ineligible through the subject | The subject is evaluated independently. |
| Coastal subject | Eligible independently | Subjects receive their own package and make their own handling choice. |
| Government in exile with no controlled coast | Ineligible | It has no legal commissioning location. |
| Capitulated country controlling a valid coastal enclave | Conditionally eligible | It qualifies only if normal naval ownership and ship creation remain legal. |
| Civil-war participant with its own coast | Eligible independently | Each active side is a separate naval actor. |
| Civil-war participant without coast | Ineligible for this firing | It cannot use the opposing side's ports. |
| Special Chaos country permitted to use ordinary fleets | Eligible | The owning system's naval rules take priority. |
| Special Chaos country that cannot use ordinary fleets | Ineligible | The event must fail closed instead of creating unusable units. |
| Country annexed during delayed commissioning | Delivery cancelled | No fleet transfers to an unrelated successor without an explicit valid rule. |
| Country that loses every commissioning port before delivery | Re-evaluate once | The event can choose another valid owned port, otherwise the delayed package is cancelled. |

## Newly coastal countries

A country skipped because it was landlocked remains a valid future recipient. When a later firing finds that the country directly owns and controls usable coast, it receives a package under its current repeat count, which will normally still be zero.

This is an important repeatable payoff. It gives territorial change a visible connection to Event 56 without granting fleets outside a normal firing.

A newly coastal country does not receive a delayed package from an earlier event. It waits for the next repeat.

## Commissioning port selection

The event selects ports after package identity and scale are known. A submarine force, carrier group, and convoy escort reserve can use the same selection framework, but their preferred port qualities differ.

The selector should prefer:

- higher naval base capacity
- reliable land supply
- direct ownership and control
- distance from active land combat
- lower immediate hostile air and naval exposure
- proximity to the country's home territory and main naval theater
- sufficient nearby air capacity for carrier or naval aircraft support
- repair access appropriate to the fleet's heaviest ships

The selector must not guarantee an ideal strategic base. It prevents clearly broken placement while allowing the event to remain awkward.

### Home-port preference

A country's best secure home port is the normal first choice. Overseas bases can be used when the home coast cannot support the package or when a package must be split.

The event should avoid placing an entire fleet in an isolated colonial port merely because it has one more naval base level than the home region. Strategic reach, safety, and connection to owned territory should be considered together.

### Hostile exposure

A valid port can still be dangerous. The event may use a threatened port when the country has no safer choice, but the personal report must make the risk clear.

A port inside active land combat or under enemy control is never valid.

## One to three commissioning ports

Small packages use one port whenever possible. Medium packages can use one or two. Large packages can use up to three.

Splitting should follow fleet function:

- carriers and heavy surface ships stay with sufficient escorts
- submarines can form one or more dedicated groups
- convoy escorts stay near the convoy reserve or relevant home port
- invasion-support ships remain grouped around their transport and bombardment role
- minelayers and patrol ships can form a separate denial group

The event should not scatter a package across many ports. Three is the maximum because the recipient must be able to understand the result and reorganize it without searching the whole map.

## Emergency commissioning facility

A country with controlled coast but no usable naval base can receive an emergency facility when a safe coastal state exists.

The facility has a narrow purpose:

- establish the minimum port access required for the package
- create a short commissioning delay
- prevent ships from appearing in an invalid location
- leave the country with a modest permanent naval foothold rather than a fully developed port

The emergency facility does not grant a major port complex. Event 55 remains the event that can create broad infrastructure and logistics support.

The personal report should identify the state and explain that the fleet cannot enter service until the facility is ready.

## Package support

Every package may include support that is necessary for its identity to function. Support is part of the package budget, not an unlimited extra reward.

Possible support includes:

- convoys
- fuel reserve
- carrier aircraft
- naval bombers
- a short commissioning readiness effect
- a bounded emergency naval base level
- temporary repair support
- a small stock of naval support equipment where an owning system defines one

The support mix follows the fleet identity. A destroyer swarm should not receive a large carrier-air package. A carrier force should not arrive without a credible route to field aircraft.

## Aircraft handling

Carrier aircraft are included when carriers are the defining asset or a substantial secondary component. The aircraft should be compatible with the active content and available equipment framework.

Aircraft placement follows this order:

1. Fill valid carrier capacity where the engine and content permit direct assignment.
2. Place remaining compatible aircraft in the nearest valid controlled airbase.
3. Place unresolved legal aircraft into stockpile for the recipient.
4. If no compatible aircraft can be granted, mark the carrier package as partially unsupported and make phased commissioning more attractive.

The event does not grant air technologies merely to make the package work.

## Fuel reserve

Every combat package includes a fuel reserve scaled to its expected short operating window. This gives the recipient time to reorganize and decide how to use the fleet.

The reserve should not sustain a large navy indefinitely. Carrier and capital packages receive more fuel than coastal defense or convoy packages, but their continuing consumption also remains higher.

The grant must respect practical storage behavior. Excessive fuel that cannot be stored should not be used to inflate package value.

## Admirals and command

The event should use existing admirals and the normal command system. It must not generate a named admiral for every recipient.

A country without an admiral can still receive ships. The commissioning report can represent temporary naval staff coordination through a short readiness effect if needed. Any later commander acquisition should use ordinary country systems or an existing shared naval mechanism.

This avoids a large portrait, character, localisation, and roster burden that adds little to the event's core play.

## Human commissioning choices

The following names are working design labels, not final option localisation.

### Full Commissioning

The country places the complete package into service immediately.

Player-facing result:

- all deliverable ships enter active service
- the full convoy, aircraft, and fuel support package is granted
- the country receives the strongest short commissioning-readiness support
- repair queues and port load begin immediately
- the whole operational fuel burden becomes active at once

This choice should appeal to countries at war, island states under threat, powers with fuel and repair capacity, and players who want the fleet's immediate military value.

It should never add a hidden long-term punishment. Its cost is the ordinary burden of operating everything now.

### Phased Commissioning

The country introduces the package in stages.

Player-facing result:

- screens, submarines, patrol ships, and urgent convoy support enter service first
- some heavy ships or carriers remain in a bounded reserve or delayed commissioning state
- the initial fuel and repair burden is lower
- the second tranche enters service after a clear period if a valid port still exists
- support tied to delayed ships arrives with that tranche

The player should know which part is available now and which part is delayed. The delayed tranche cannot disappear without a report explaining why.

This choice should appeal to peacetime countries, recipients with weak ports, low-fuel countries, and states that need time to provide aircraft or repair capacity.

### Break Up the Package

This choice appears only when the fleet contains enough heavy or auxiliary value to make partial dismantling meaningful.

Player-facing result:

- the country keeps the fleet's defining operational core
- bounded excess hull value is converted into convoys, fuel, repair support, and limited naval experience
- the total combat fleet is smaller
- the recipient avoids part of the immediate sustainment burden
- achievements that require full operational use can be disqualified

The country cannot dismantle the entire gift. It cannot repeatedly convert small packages into an efficient resource farm. The conversion rate must be deliberately worse than receiving and using the ships.

This choice should appeal to land-focused states, fuel-starved countries, countries with no useful ocean theater, and recipients whose new fleet duplicates an already dominant capability.

## Delayed commissioning

Delayed work applies only to affected recipients. The event must not maintain a global periodic process after the firing.

A delayed tranche resolves through one bounded follow-up. At resolution:

- confirm the recipient still exists
- confirm at least one valid commissioning port remains
- use the original package identity and reserved composition
- prevent a second delivery if the follow-up repeats
- deliver the reserved support only once
- cancel cleanly if no valid result remains

If the original port has been lost, one re-selection is allowed. The system should not chase changing ports indefinitely.

## Package cancellation and partial delivery

A recipient can receive less than the planned package when legal content, port conditions, or global safety limits prevent full delivery.

The event should preserve these priorities:

1. defining ships or support that establish the package identity
2. minimum screens needed for a coherent force
3. essential aircraft or convoy support
4. secondary combat ships
5. surplus auxiliary ships

If even the defining core cannot be delivered, the country is skipped and the event records a clear internal reason. It should not receive a misleading report about a fleet that never appears.

## Multiplayer presentation

The global world report appears once through the shared event flow.

Every eligible human-controlled country receives its own commissioning report. Each human chooses independently. One player's choice does not alter another player's package.

A player who controls more than one country through an unusual setup should still receive one personal handling flow per processed human recipient, with duplicate protection.

The event log remains global. Personal package detail can be retained for each human recipient without creating separate global pacing entries.

## Cleanup

After each recipient is resolved, temporary selection state should be cleared. After the whole firing, the eligible-country list, package-allocation state, skipped-country reasons, and global budget workspace should be discarded except for the bounded history and achievement facts defined in the core specification.

The event must not leave active commissioning choices for annexed countries, invalid ports, or already delivered tranches.
