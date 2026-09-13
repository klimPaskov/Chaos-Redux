# Event 043: Monsters from the Deep

## Part 3: Shared monster mechanics and lifecycle

## Shared mechanic surface

Every full monster country uses one event-owned decision category and two public values.

- **Hunger** measures the pressure to feed.
- **Sea Bond** measures the country's active connection to salt water, lairs, and its apex.

The category should show the current band, current exact value for a human monster player, the next important threshold, and the most useful current actions. It should not display every contributor or hidden weight.

Ordinary countries use a separate response category defined in Part 6.

## Hunger

### Scale

Hunger runs from `0` to `100`.

| Band | Range | Public meaning |
| --- | ---: | --- |
| Sated | `0-19` | The country can consolidate and save earned reinforcement receipts |
| Restless | `20-39` | Normal operating state |
| Ravenous | `40-59` | Feeding becomes more valuable and selected support actions cost more |
| Starving | `60-79` | Combat recovery and political control weaken, destructive feeding pressure rises |
| Frenzied | `80-100` | The country risks uncontrolled choices, pact strain, and severe apex penalties |

The labels are working directions. Final localisation should be creature-aware where useful.

### Hunger growth

Hunger should rise from:

- time without a meaningful feeding event
- operating near the current inland limit
- holding disconnected deep territory
- maintaining more support formations than current lairs can sustain
- losing a lair
- losing a port
- failing a named hunt or coastal objective
- suffering a major defeat
- entering an extended war without securing coastal population or port control
- using selected apex powers
- betraying a pact when that betrayal creates a costly surge
- terminal preparation for creatures whose route demands sacrifice

The country should not gain Hunger every day through an unrestricted global pulse. Event-owned processing can update registered active monsters on a weekly or ten-day cadence, driven through one bounded scheduler.

### Hunger reduction

Hunger should fall from:

- taking and holding a new port
- capturing a coastal capital
- winning a large coastal battle
- completing a hunt mission
- using a feeding decision against a controlled populated coastal state
- destroying enemy convoys or ships when the creature's route supports maritime feeding
- consuming a stored feeding reserve
- receiving a pact contribution
- completing a creature-specific focus
- dismantling an unsustainable support formation through an intentional event action when that option fits the route

Routine state ownership must not generate endless passive feeding. A port or coastal capital gives a one-time receipt and a bounded lair contribution. Repeat feeding from the same population requires real remaining population and escalating local damage.

### Hunger consequences

Hunger changes play through staged effects.

At Ravenous:

- reinforcement actions become more expensive
- lair development slows
- pact acceptance becomes less reliable
- aggressive AI weights rise

At Starving:

- organization recovery falls
- Sea Bond decays faster when ports are lost
- support formations take stronger inland penalties
- one emergency feeding family becomes visible
- pact betrayal risk rises for eligible AI

At Frenzied:

- the apex suffers a meaningful recovery and control penalty
- some compact benefits suspend
- the country receives one bounded crisis choice
- AI prefers immediate coastal feeding targets
- expensive long-term projects become invalid
- a human player must choose between destructive feeding, contraction, or sacrificing a support formation

A frenzied country must not automatically delete population without a player-facing or AI-resolved event action. The event can force a crisis decision deadline, then resolve a default outcome if no choice is made.

### Hunger and balance

Hunger is not a mana store. Most actions do not spend Hunger as a positive currency.

A feeding action lowers Hunger while killing civilians and damaging a state. A brood action may require Hunger below a threshold, use an earned reinforcement receipt, and then raise Hunger because the new formation needs sustenance. This creates a readable loop without turning Hunger into a shop balance.

## Sea Bond

### Scale

Sea Bond runs from `0` to `100`.

| Band | Range | Public meaning |
| --- | ---: | --- |
| Severed | `0-19` | The monster is isolated from its maritime base |
| Failing | `20-39` | Combat and recovery penalties are severe |
| Unsteady | `40-59` | The country can fight but must restore coastal access |
| Anchored | `60-79` | Normal intended strength |
| Tidal | `80-100` | Lairs and connected ports support the apex at full strength |

### Sea Bond sources

Sea Bond rises from:

- controlling the original lair
- controlling registered additional lairs
- controlling connected ports
- keeping the apex in or near valid coastal territory
- maintaining a continuous legal path from the apex to a lair
- winning defensive battles around a lair
- completing coastal-consolidation focuses
- holding creature-specific terrain such as Jiaolong river mouths or Cipactli lowlands
- receiving bounded pact support
- Cthulhu terminal effects

Sea Bond falls from:

- losing the original lair
- losing all ports in a theatre
- operating the apex beyond current range
- having the apex encircled
- holding disconnected territory
- losing registered lairs
- human completion of a sea-tether mission
- failure of a route-specific coastal objective
- prolonged forced retreat inland
- selected anti-monster operations

### Calculating Sea Bond

The event should calculate a target Sea Bond from current proven conditions, then move the public value toward that target on a bounded pulse. This prevents instant oscillation when one port changes hands for a few hours.

The calculation can use hidden components:

- original lair status
- active lair count
- port count inside legal range
- coastal state count
- apex current state depth
- apex encirclement or supply state
- connected coastal path proof
- pact support
- creature resistance profile
- temporary human disruption
- terminal override

The category tooltip can list the three largest current causes in plain language. It should not show a raw ten-line equation.

### Sea Bond consequences

Low Sea Bond should affect:

- attack
- defense
- breakthrough
- organization
- recovery
- movement
- planning
- apex special-power access
- support-spawn eligibility
- Hunger growth
- retreat preference

It should not directly remove manpower or equipment. Monster formations use neither normal system.

At Severed Sea Bond, the apex becomes killable by a prepared ordinary coalition. It remains dangerous and should not turn into an ordinary weak infantry division.

### Sea Bond and Cthulhu

Cthulhu's Dominion sets the united country's Sea Bond to a terminal band or replaces ordinary decay with a minimal residual system. Surviving apexes can operate across the interior.

The terminal route may keep one public Sea Bond value as a world-scale supernatural anchor. It must not require the player to track one value per surviving apex after unification.

## Hidden reinforcement receipts

Support formations are created from earned receipts, not from a passive daily loop.

A receipt records one proven accomplishment, such as:

- first capture of a port
- first capture of a coastal capital
- control of a required lair group
- completion of a brood focus
- destruction of a major enemy formation
- successful hunt
- feeding reserve threshold
- pact contribution
- evolution arrival package
- terminal reinforcement milestone

A receipt has:

- owner country
- source type
- source state or target when relevant
- date
- support family permission
- strength tier
- consumed status
- one-use proof

The player normally sees a qualitative line such as `A brood can be raised from the lair`. The raw receipt ledger remains hidden.

### Receipt limits

- one objective cannot issue the same receipt twice
- losing and recapturing one port cannot farm unlimited support
- a repeat source needs a cooldown, escalating cost, and remaining population or target proof
- a consumed receipt cannot return after save and reload
- terminal transfer must reconcile unused receipts once
- remnant conversion either clears or converts eligible receipts into a smaller remnant pool
- scenario setup creates only the receipts named by its intensity package

## Supporting formations

Monster countries cannot use normal recruit and deploy.

The six shared families are:

- Riptide Shoal
- Abyssal Raider
- Reefbreaker
- Trench Stalker
- Venom Brood
- Drowned Colossus

A creature can use three primary families and one or two later secondary families. It should not gain unrestricted access to all six.

Support formations:

- require zero ordinary manpower
- require no normal equipment
- cannot be trained through the normal interface
- appear only through Event 043-owned effects
- use event-owned sustainment and caps
- follow inland-depth penalties
- have bespoke model, sound, and counter packages
- remain visually weaker and smaller than an apex
- can be destroyed permanently
- may be disbanded only through a deliberate event action when that action exists
- do not independently trigger country capitulation

The unit registry must declare each family as a standalone provider or an explicitly parent-owned family under Event 043. CXT test-country coverage is required for every subunit definition.

## Support cap

The active support cap should scale from:

- lair count
- controlled coastal states
- evolution package
- focus route
- pact contributions
- terminal state
- difficulty and scenario intensity
- existing living support formations

The cap is not a public third meter. It appears in decision availability and a concise tooltip.

A country over cap after losing territory does not instantly delete units. It gains Hunger and Sea Bond pressure, loses reinforcement access, and receives an option to consolidate or sacrifice formations. Prolonged over-cap status may apply stronger penalties.

## Feeding and real population

Feeding removes real state population through the shared exact civilian-population loss transaction.

Every feeding effect must:

1. calculate the requested loss dynamically
2. protect the configured minimum remaining population
3. identify the Event 043 death reason
4. name the responsible monster country
5. apply the loss once
6. log the actual amount in the shared Deaths system
7. return the applied amount
8. base Hunger relief and reinforcement receipts on the applied amount
9. avoid recruitable-manpower credit
10. publish migration or famine adapters only when their independent contracts require it

A fixed `add_manpower = -X` state effect is forbidden.

### Feeding scale

Feeding severity should consider:

- current state population
- state urban and industrial importance
- existing evacuation
- current Hunger band
- creature profile
- prior feeding in the same state
- local fortification or shelter
- human countermeasures
- current Chaos tier
- evolution package
- protected population floor

The event should prefer percentage and bounded absolute floors or caps. One universal fixed death number would make tiny islands and major cities behave incorrectly.

### Repeated feeding

A state remembers:

- first feeding date
- total Event 043 deaths
- latest responsible monster
- local devastation stage
- evacuation status
- cooldown
- remaining valid feeding capacity

Repeated feeding gives less Hunger relief as population falls. It increases devastation and can make the state unsuitable for another lair.

### Devastation

Feeding may also damage:

- infrastructure
- railways
- ports
- naval bases
- factories
- supply hubs
- local stability through state modifiers

Damage must be bounded and related to the selected action. A population-focused action should not automatically erase every building.

## Lairs

A lair is a registered state, not every controlled coast.

### Lair requirements

A new lair requires:

- controlled valid saltwater coast
- legal inland depth
- no rival monster lair
- no active human purification mission
- enough local population or maritime resources
- available lair slot
- route permission
- one unconsumed lair receipt or a substantial action cost

### Lair benefits

A lair can provide:

- Sea Bond
- Hunger stabilization
- spawn access
- defensive modifier
- focus or decision target
- movement between route-linked lairs
- pact support point
- terminal coastal-control score

### Lair destruction

Human countries can neutralize a lair by:

- retaking the state
- completing a purification mission after retaking it
- holding it for a confirmation period
- destroying the registered monster support presence

Retaking the state immediately removes most benefits. The lair record clears after confirmation and cleanup. The original monster remembers the loss for Hunger and AI behavior.

A monster can rebuild only through a new legal action. Lair status cannot oscillate every hour with control changes.

## Apex unit identity

Every full monster country receives one division with one unique apex battalion.

The apex division:

- has a stable identity flag or unit identifier
- contains the unique creature battalion
- needs no manpower
- needs no equipment
- cannot be trained
- cannot be copied
- cannot be duplicated by focus, decision, event, console setup, or scenario launch
- cannot be converted into another template
- cannot be split
- cannot be merged away
- cannot be voluntarily deleted
- cannot be recreated after destruction
- transfers once into Cthulhu's Dominion if alive
- remains individually tracked after transfer

Implementation must prove the engine mechanism for these restrictions. If one restriction cannot be enforced, the event remains incomplete until the user approves an alternative.

## Apex combat target

An apex should dominate ordinary coastal battles. It should not be a map-wide invulnerable unit.

Baseline planning target:

- wins against six to ten ordinary contemporary infantry divisions on favorable coast
- can break a defended port with support
- survives twelve to sixteen divisions only with favorable terrain, Sea Bond, support, and supply
- becomes vulnerable when encircled, severed, deep inland, heavily bombed, or attacked by prepared specialist forces
- cannot be permanently pinned by one cheap division
- cannot cross a whole continent before adaptation
- cannot be killed casually through one air strike or attrition tick
- can die through a real concentrated campaign

Raw values need installed-game combat testing. Armor, piercing interaction, width, supply, air vulnerability, terrain, retreat, and AI behavior must be tested together.

## Apex powers

Each creature may gain one or two focus-unlocked powers. Powers should use cooldowns, visible conditions, and costs.

Examples include:

- Kraken port-crush attack
- Scylla pursuit burst
- Leviathan temporary armor stance
- Hafgufa prepared ambush
- Umibozu port-silencing storm
- Jiaolong flood corridor
- Bakunawa eclipse offensive
- Akkorokamui regeneration window
- Lusca blue-hole emergence
- Cipactli many-mouth feeding
- Ipupiara coastal terror

Powers cannot create a second apex or bypass the event's population transaction.

## Apex death detection

Apex death must be detected through an event-owned robust method.

The detection contract needs:

- stable unit identity
- a maintained living-apex marker
- one death receipt
- save and reload safety
- no false death during template or controller transitions
- no duplicate surrender call
- exact responsible war context when available
- terminal transfer awareness
- scenario awareness

The system should prefer a verified engine callback or unit-leader or division existence pattern over a broad polling scan. If polling is unavoidable, it must process only registered active apex identities on a bounded cadence.

## Pre-terminal apex death

When a full monster apex dies before Cthulhu unification:

1. mark the creature permanently dead
2. clear living-apex and terminal eligibility
3. stop its unique focus tree
4. stop new unique-route decisions
5. issue one surrender transaction against current enemies
6. remove or disable its apex leader presentation
7. choose full extinction or Abyssal Remnant state
8. convert surviving support units to remnant ownership or resolve them safely
9. clear or convert lairs
10. remove pact membership
11. update world threat and terminal readiness
12. apply the bounded Event 043 Chaos reduction
13. send relevant reports
14. record achievement and aftermath checks

The country must not recreate the apex during the surrender or peace sequence.

## Abyssal Remnants

A tag can survive as an Abyssal Remnant when territory, war structure, subjects, or surviving units make total removal unsafe or narratively useful.

A remnant receives:

- generic nonhuman leader
- generic remnant focus tree
- reduced decision category
- no apex powers
- no terminal leadership
- no ability to form or lead a full pact
- limited support reinforcement
- severe range and Sea Bond limits
- cleanup and surrender routes
- persistent actual-nonhuman classification

A remnant can join Cthulhu only as generic forces and territory if the terminal route explicitly permits it. It cannot contribute a dead apex to the living-apex count.

## Conventional capitulation with living apex

The event needs an explicit rule for a full monster country that capitulates while its apex still exists.

Preferred design:

- the apex retreats with surviving support formations to one valid controlled coastal state if such a state exists
- if no controlled valid coastal state exists, the full country is defeated
- the apex does not transfer to an ordinary human occupier as a normal division
- a peace conference cannot create a human puppet ruled by the creature
- a surviving escaped apex can establish one last remnant lair only through a bounded defeat event and only once

This route must be tested against faction wars, subjects, exile mechanics, civil-war transfers, and peace conferences. If HOI4 cannot support the preferred retreat safely, the implementation must choose a clear full-defeat rule and report it before use.

## Monster leaders

The named apex creature rules the country.

The country does not use:

- human political advisors
- elections
- ordinary party competition
- generic human commanders
- normal recruitable generals
- a symbolic human council

Route choices can create nonhuman lieutenants or brood authorities only when the focus tree gives them a gameplay role. They should be institutional names or impossible entities, not invented grounded people.

The leader portrait is a fictional high-chaos nonhuman portrait. It needs a static `156x210` texture and a real frame-sheet animated presentation with a static fallback.

## Economy and production

A monster country should have a stripped event economy.

Factories in controlled territory can affect:

- lair development speed
- repair of captured ports
- human resistance pressure
- terminal coastal score
- selected route effects

They do not produce rifles, tanks, aircraft, or ordinary monster equipment.

The country should not use normal trade, lend-lease, production licences, research sharing, manpower laws, or ordinary conscription. Shared classifiers and targeted visibility triggers must keep irrelevant systems hidden or unusable.

Captured dockyards can support blockade and lair decisions through scripted values. They should not create a conventional monster navy unless a later accepted expansion defines one.

## Research and doctrine

Event 043 adds no technology tree or doctrine tree in this specification.

Monster strength comes from focus routes, ideas, decisions, unit definitions, lairs, and evolutions. Adding a full research tree would increase UI and asset scope without solving the core campaign loop.

The countries can start with zero research slots. Any unavoidable engine requirement must be documented.

## Diplomacy

Full monsters can:

- declare Event 043 conquest wars
- make pacts with other full monsters
- join an event-owned abyssal faction
- receive or send event-owned reinforcement support
- merge under Cthulhu
- create limited subjects through the Apex Dominion route when a rival monster is defeated but preserved

They cannot use ordinary human diplomatic actions unless explicitly enabled.

Ordinary countries should generally refuse:

- guarantees
- military access
- nonaggression pacts
- trade agreements
- faction invitations
- lend-lease
- attachés
- volunteers to the monster
- ideology diplomacy

Monster pacts use event-owned actions because ordinary diplomacy cannot express the staged rules safely.

## Interaction with civilian systems

Full monsters, remnants, and Cthulhu's Dominion are actual nonhuman countries.

They are excluded from ordinary:

- famine host logic
- migration reception logic
- humanitarian invitation logic
- civilian treaty membership
- human CBRN doctrine decisions
- camp and repression packages
- ordinary population-growth grants
- normal diplomatic sanctions where a human society is required

Their controlled human population remains real. Event 043 feeding, evacuation, occupation, and deaths use state-level transactions and human origin countries where appropriate.

A nonhuman controller does not make civilians nonhuman.

## Migration integration

A threatened human controller can evacuate a coastal state through the independent Migration system when:

- a full monster threatens or borders the state
- a valid safer destination exists
- the route and reception proofs pass
- the same population is not already removed through feeding

Migration moves survivors. Feeding deaths use the Deaths transaction. The two systems exchange versioned receipts so the same people are not debited twice.

A monster country cannot receive ordinary refugee cohorts.

## Famine integration

Monster attacks can worsen local food security through port loss, route damage, isolation, and population displacement. Event 043 should submit bounded incident facts to Famine when its public contract allows them.

Event 043 does not write famine stages directly. It does not create a second monster-specific famine meter.

## Air Cleanliness and CBRN

Normal monster attacks do not automatically add Air Contamination.

Venom, ink, storms, and supernatural environmental effects are Event 043 mechanics. They are not chemical or biological warfare unless a specific cross-event route uses the shared CBRN system with the required evidence.

Monster countries are excluded from ordinary CBRN production and doctrine. Human anti-monster operations can use existing technologies and units where valid, but Event 043 should not hand out advanced weapons for free.

## Runtime scheduler

The event should use one sparse active-country array.

Recommended bounded cadence:

- immediate refresh on emergence
- immediate refresh on state gain or loss
- immediate refresh on apex death
- immediate refresh on pact transition
- one weekly or ten-day event-owned country pulse for Hunger, Sea Bond, support cap, and frontier validation
- one longer monthly event-owned strategic pulse for terminal and regional coverage
- registered threatened-state processing only where a mission, lair, feeding cooldown, or evacuation receipt exists

No new unrestricted `on_daily`, `on_weekly`, or `on_monthly` every-country iteration is permitted without explicit user approval.

## Save and reload

Every persistent state needs recovery behavior.

On load or bounded repair:

- rebuild active monster array from stable markers
- verify one apex per living full monster
- verify dead identities stay dead
- verify lair arrays point to valid states
- verify pact records agree across members
- verify Cthulhu transfer receipts
- remove stale decisions and missions
- recalculate public Hunger and Sea Bond toward valid targets
- clear scenario bypass flags
- refresh world threat
- repair only provable missing presentation state

The repair path must not recreate an apex merely because its marker is missing. Missing proof fails closed and produces a debug finding.

## End of Part 3

Part 4 defines the sixteen country packages, their apex roles, shared support families, terminal country, remnants, tags, and asset identity.
