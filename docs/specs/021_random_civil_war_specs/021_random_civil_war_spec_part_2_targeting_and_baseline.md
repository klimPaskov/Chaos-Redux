# Targeting and Baseline Opening

## Hidden Fracture Pressure

Event 021 uses a hidden country-level score called `Fracture Pressure`.

It measures how easy it is for a viable organized opponent to turn domestic conflict into armed conflict. It should never be reduced to stability alone, ideology popularity alone, or a random equal chance for every country.

Fracture Pressure is recalculated when:

- Event 021 builds its automatic target pool
- a country enters the Evolution III review queue
- a major preventive action succeeds or fails
- a relevant territory, capital, depot, or rail condition changes
- a war ends
- a settlement is signed
- an active Event 021 crisis reaches a bounded review point
- a country is created, transformed, annexed, or released
- a nearby Event 021 war begins or ends during Evolution II or III

It does not require an unrestricted daily scan of every country.

## Pressure components

| Component | Conditions that raise pressure | Conditions that lower pressure |
| --- | --- | --- |
| Political stability | low stability, rapid government change, failed coup, collapsing coalition, severe legitimacy loss | high stability, a durable coalition, trusted institutions, recent constitutional settlement |
| War exhaustion | long external war, low war support during war, heavy casualties, convoy loss, lost cores, repeated strategic defeat | recent peace, successful defense, restored manpower, functioning demobilization |
| Political competition | one strong excluded opposition, several organized rival blocs, rapid ideology swing, banned movement with real support | broad governing coalition, opposition integrated into legal politics, low organized support |
| Political exclusion | removal of a large regional or ideological bloc from power, destroyed autonomy, dissolved institutions, recent loss of representation | negotiated access, local institutions, power-sharing, recognized autonomy |
| Territorial control | occupied home states, high resistance, isolated regions, lost rail links, disconnected administration | secure cores, connected administration, viable local government, restored communications |
| Military loyalty | officer purges, divided commands, unpaid or undersupplied formations, encircled military districts, politically split units | integrated command, supplied armies, trusted officers, successful loyalty objectives |
| State capacity | weak infrastructure, noncontiguous territory, no dependable route to the periphery, broken civil service | functioning rail and supply, administrative reach, protected arsenals, responsive regional services |
| Regional identity | complete Event 006 package, historic regional institutions, coherent territorial claim, autonomy movement | accepted local settlement, integrated institutions, no safe package or region |
| Country scale | many states, many military districts, several viable capitals, several distinct regions | microstate or one-state structure, which routes to a limited takeover |
| Nearby conflict | active Event 021 front across a border, related armed network, arms route, returning cadres, competing sponsors | controlled border routes, successful mediation, demobilized neighboring movements |
| Event memory | harsh settlement, unresolved partition, surviving front, old arms stock, exiled claimant, prior recurrence | long peace, reintegration, disarmament, trusted guarantees |
| Other Chaos Redux systems | documented command fracture, liberation pressure, occupation strain, mutiny history, active human crisis actor nearby | successful containment or resolved shared condition |
| Chaos state | access to later evolutions, wider global fracture climate | Calm World and no nearby or historic crisis |

The model must distinguish political diversity from organized conflict. Ethnic, regional, ideological, religious, or class diversity by itself adds no pressure. A group matters only when it has a plausible political grievance or goal, organizational capacity, leadership, territorial or institutional access, and a valid actor package.

## Target weighting

The automatic picker builds a weighted pool of valid countries.

Weight should reflect:

- Fracture Pressure
- opening viability
- availability of at least one distinct actor
- country-specific cooldown
- recent regional variety
- recent archetype variety
- whether a major is currently allowed
- whether the player country is valid
- global active-front capacity
- current scenario or cluster reservations
- country generation and successor grace
- whether Event 006 offers a complete relevant package

The highest pressure country should not always be selected. The pool needs enough randomness to create campaign variety, but pressure ordering must remain visible in probability tests.

A stable country can remain in the pool at low weight. If selected, it receives a smaller opening.

A player country uses the same rules. It should not be protected merely because it is human, and it should not receive an artificial weight boost merely because it is human.

## Baseline target policy

Before Evolution I:

- minor countries are the normal target pool
- majors are excluded from ordinary automatic selection
- countries already fighting a serious external war remain eligible when war exhaustion is a meaningful cause and the opening remains playable
- countries with one state or unsafe island geography use a same-tag takeover route
- subjects can be targeted when their domestic politics and overlord relationship support a valid crisis
- ordinary human Event 006 countries are eligible after their creation grace period
- a country already in a compatible small domestic crisis can receive an Event 021 escalation only through an explicit adapter, not through a second blind firing

## Opening severity

After target selection, Event 021 derives an opening severity from Fracture Pressure, country scale, territory viability, military loyalty, actor capacity, and current war context.

| Severity | Typical conditions | Opening direction |
| --- | --- | --- |
| Limited | stable government, compact opposition, intact command, weak regional organization | small region or failed-coup theater, modest defections, short crisis pressure |
| Serious | visible political division, local organization, some military doubt, viable regional base | one connected opposition region, usable capital, regular force package, active crisis decisions |
| Severe | low stability, long war, occupied cores, strong exclusion, divided command | large viable region, meaningful force share, depot and rail pressure, foreign attention |
| Critical | major structural failure, several organized blocs, broad command collapse, high chaos | one powerful baseline opponent, or an immediate Evolution I multi-front opening when that evolution is active |

Baseline normally creates one primary opponent. A critical baseline target receives a strong opponent, not several weak actors. Multiple fronts belong to Evolution I.

## Baseline archetypes

The dispatcher selects one valid archetype after it has chosen the country and severity.

### Ideological uprising

An organized non-ruling ideology challenges the government.

Preferred conditions:

- meaningful ideology popularity
- legal exclusion or recent repression
- coherent regional or urban base
- available political leadership
- compatible military or militia support

The actor should have a distinct public program. It must not exist only to switch the ruling ideology.

Possible goals:

- replace the national government
- establish a revolutionary government
- restore a constitutional order
- overthrow a dictatorship
- defend a threatened ruling coalition from a rival takeover
- create a temporary coalition and call elections after victory

### Rival legal government

A second government claims constitutional, dynastic, parliamentary, judicial, military, or electoral legitimacy.

Preferred conditions:

- disputed succession
- failed government transition
- dissolved parliament
- competing constitutional authority
- exile or regional government that remains inside home territory
- leadership split inside the ruling bloc

This route uses the same national identity unless a verified cosmetic route is required. It should feel different from a generic ideological revolt because its claim is about legal continuity and institutions.

### Regional secession

A coherent region demands autonomy, federation, or independence.

Preferred conditions:

- connected territory
- valid regional capital
- political institutions or organized movement
- historical, cultural, legal, economic, or administrative identity
- defensible leadership
- no complete Event 006 package that should own the identity instead

A temporary regional actor cannot remain indefinitely with a vague generic identity. It needs a defined postwar disposition, such as autonomy, merger, reintegration, promotion into a complete package, or rejection before permanent independence.

### Event 006 independence actor

A complete human Event 006 package rises inside the selected country.

Preferred conditions:

- Event 006 registry contains a valid package
- package territory is compatible with the current host
- tag is free or safely reusable
- leader, flags, focus tree, forces, AI, decisions, and assets are complete
- no protected collision prevents a viable homeland
- the package remains human

The Event 006 contract is defined in Part 7.

### Broad command schism

Military districts, command staffs, arsenals, or formations break from the government without the event being centered on one named warlord.

Preferred conditions:

- low military loyalty
- large army
- officer purges or command rivalry
- isolated formations
- vulnerable arsenals
- severe war exhaustion
- weak civilian authority

Its public goal can be emergency rule, restoration of order, replacement of civilian leadership, defense of an old constitution, or a temporary military council.

This route must remain distinct from Event 127 Warlords and Event 131 Widespread Mutiny.

### Same-tag takeover

A one-state country, very small island country, or unsafe map structure cannot support a normal territorial split.

The event instead creates:

- a public loyalty contest
- armed cells or mutinous units
- a timed control mission
- foreign sponsor pressure
- a possible leader, ruling-party, law, subject, or ideology change
- a failed-coup or successful-takeover outcome
- limited casualties and disruption appropriate to the scale

It must not create a second invalid tag, zero-state actor, or impossible capital.

## Leader and identity resolution

Every opposition route must resolve leadership before the map changes.

Preferred order:

1. a valid existing character whose ownership and role permit transfer
2. an existing institutional council or legal body with appropriate identity
3. a valid Event 006 leader from the complete package
4. an established engine generic civil-war route that does not require a new custom portrait, after local precedent is verified
5. another archetype or another target

A grounded polity must not receive an invented face. A real character must not be cloned across live countries. A blocked leader blocks that actor unless another defensible leadership route exists.

Ordinary claimants should reuse the parent country's flag or a verified existing civil-war variant. Event 021 does not authorize a library of generic generated flags.

## Territory planning

The framework plans every territorial change before it commits ownership or control.

A planned opposition region should:

- be connected where geography permits
- contain a viable capital or emergency capital
- contain enough population and industry to sustain the assigned role
- have a usable route to supply
- avoid isolated single-province fragments
- avoid taking unrelated third-party occupied territory
- respect Event 006 package state maps and collision rules
- leave the parent country a viable remnant
- preserve at least one parent capital route
- avoid immediate automatic capitulation unless the selected outcome is a same-tag takeover
- prefer coherent administrative, military, regional, rail, or geographic groupings
- reserve every selected state before another front can claim it

The allocator should plan the full opening in one transaction. It should not transfer states one at a time while later choices depend on the already changed map.

## Parent remnant protection

The original government must retain enough territory to remain playable.

Protection should consider:

- at least one state
- capital or safe replacement capital
- minimum industrial and population base
- supply route
- access to a port when the remaining geography requires it
- a meaningful force package
- no instant trapped capital
- no complete loss of every core state through a random roll

A scenario or severe evolved opening can create a desperate remnant, but the result must still be a real belligerent.

## Force allocation

The event must not blindly split half the army.

Force allocation should consider:

- current unit location
- controlling region
- commander and officer ties
- ideology or claimant affinity
- command district
- supply status
- encirclement
- naval base or airbase control
- depot access
- severity
- state population and local support
- existing Event 006 force profile
- current external war
- minimum viable parent and opposition force

The opening may transfer or create:

- local militia
- defecting regulars
- border guards
- capital defense units
- railway guards
- port guards
- mountain detachments
- cavalry
- sailors
- foreign-trained cadres
- package-specific Event 006 formations

A force package needs enough equipment and manpower to function. It should also carry realistic weaknesses, such as poor training, low supply, limited support equipment, officer shortages, or dependence on one depot.

## Stockpile, air, and naval allocation

Stockpiles follow territory, units, arsenals, depots, and severity.

The opposition should not receive a fixed percentage of all equipment without context. It should receive enough basic equipment to operate, then depend on captured depots, local production, foreign aid, and reinforcement decisions.

Air and naval assets should split only when:

- the actor controls relevant airfields, ports, or commands
- the engine route is safe
- the transfer produces useful gameplay
- the parent retains a viable force
- the identity of the actor supports those assets

A landlocked regional uprising should not receive a decorative navy. An island command schism can receive ships when it controls their base and command.

## Opening State Authority

`State Authority` is the one main visible crisis value.

Range:

- `70-100`: Cohesive
- `40-69`: Contested
- `15-39`: Failing
- `0-14`: Collapse

These are working stage labels.

State Authority represents:

- administrative reach
- command obedience
- control of railways and depots
- cooperation of local officials
- ability to deliver orders and supply
- credibility of the current or successor government

It changes through:

- capital control
- mission results
- rail and depot control
- supplied formations in named regions
- negotiations
- repression
- civilian administration
- foreign intervention
- settlement terms
- victory
- loss of key territory

High authority improves containment and reduces additional-front pressure. Low authority worsens supply, mission difficulty, defection, recurrence, and the chance of active-war Evolution I escalation.

Fracture Pressure remains hidden. The player sees the causes that they can act on through concise tooltips and decisions, not the raw target formula.

## Baseline crisis ideas

Event 021 should have no more than three event-owned national spirits active on one country.

| Working idea | Role | Lifecycle |
| --- | --- | --- |
| Fractured Command | military coordination, loyalty, command, and reinforcement strain | worsens when fronts multiply, improves through integration, removed or replaced after settlement |
| War-Torn Administration | production, civil service, transport, and reconstruction pressure | changes with territory and mission outcomes, replaced by reconstruction or removed after full recovery |
| Unsettled Settlement | postwar recurrence, legitimacy, disarmament, and constitutional memory | appears only after the war, changes by settlement type, eventually removed through durable peace |

Short side effects should use timed or dynamic modifiers. The design should not create a separate national spirit for every action, sponsor, front, or battlefield incident.

## Baseline outcomes

A baseline crisis can end through:

- government military victory
- opposition military victory and national succession
- recognized independence
- negotiated autonomy
- coalition or constitutional settlement
- armistice and temporary partition
- merger into a complete related Event 006 package
- escalation into Evolution I when a new front becomes viable

The outcome system is detailed in Part 3.
