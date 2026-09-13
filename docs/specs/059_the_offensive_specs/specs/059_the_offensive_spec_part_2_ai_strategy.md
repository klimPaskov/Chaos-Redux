# Event 059: The Offensive

## Part 2: AI strategy design

## Design goal

The AI should become visibly more active, coherent, and opportunistic while remaining constrained by material reality. The event should make wars harder because opponents use their armies and opportunities more decisively. It should not make wars harder through hidden combat bonuses or uncontrolled declarations.

The intended result is a change in strategic choices:

- fewer long periods of avoidable inactivity on viable fronts
- clearer concentration on useful attack sectors
- more attempts to exploit local weakness
- better alignment between offensive plans, production, air support, logistics, and naval access
- stronger willingness to use existing claims, war goals, faction obligations, and intervention opportunities
- higher but bounded tolerance for uncertainty and loss at later evolutions

## Strategy layers

The event is divided into four independent behavior layers.

| Layer | Main purpose | Main surfaces |
| --- | --- | --- |
| Baseline Offensive Posture | Make current wars more active and coherent | Fronts, concentration, production, air support, viable invasions, existing war goals |
| Relentless Offensives | Increase pressure and operational persistence | Plan continuation, reserve commitment, follow-up attacks, recovery timing |
| Predatory Powers | Increase use of strategic and diplomatic war opportunities | Claims, war goals, weak targets, calls to arms, intervention, additional wars |
| Total Offensive | Increase operational scale and accepted strategic risk | Theater count, operation size, reserve margin, ambitious invasions, parity attacks |

Each evolution changes its own channel. Disabling one evolution must remove its future contribution without allowing a higher evolution to recreate the same behavior under another name.

Evolution III can strengthen an active Predatory Powers layer. It must not gain Evolution II's extra-war behavior when Evolution II is disabled. Evolution III can launch larger operations without inheriting Evolution I's longer persistence when Evolution I is disabled.

## Offensive opportunity model

The event should evaluate a proposed offensive through several hidden components. These components are internal design factors and should not become a player-facing meter.

### Operational feasibility

Operational feasibility answers whether an attack can be supported.

Important inputs include:

- current and projected local supply
- organisation and strength of assigned formations
- equipment replacement trend
- available trained manpower
- fuel stock and fuel trend
- rail, port, convoy, and transport capacity
- air support and airfield access
- naval access for amphibious operations
- terrain and weather burden
- strategic distance from supply sources
- readiness of reserves

A severe failure in supply, fuel, manpower, transport, or replacement capacity should override aggression. Moderate weakness should reduce scope, shorten duration, or redirect the operation toward a smaller objective.

### Local advantage

Local advantage estimates whether the chosen sector can be moved.

Useful inputs include:

- friendly combat power in the sector
- enemy combat power and reinforcement access
- exposed flanks and narrow salients
- weak links between enemy formations
- nearby reserves on each side
- available armour, artillery, engineers, and air support
- river, mountain, urban, fort, and weather penalties
- nearby ports, rail junctions, supply hubs, and victory points
- distance to a defensible follow-up line

The baseline should act on clear advantage and some uncertain but promising situations. Evolution I should accept more uncertainty when follow-up support is available. Evolution III can accept parity or limited local inferiority when the strategic reward is high and the safety floors remain intact.

### Strategic value

Strategic value determines whether success would matter.

High-value objectives include:

- an enemy capital or major victory point
- a supply hub or rail junction supporting a large front
- a port needed for a landing or isolated army
- an airfield that changes regional air access
- an exposed bridgehead or salient
- a route that separates enemy forces
- a state tied to an active claim, core, war goal, focus route, or event objective
- a resource or industrial region important to the current war
- a position that protects an ally or closes a dangerous enemy front

The event should discourage attacks that consume large resources for provinces with little operational value.

### Strategic capacity

Strategic capacity limits how many operations and wars a country can support at once.

It should consider:

- country size and major status
- number and length of active fronts
- total fielded forces and available reserves
- industrial replacement capacity
- fuel and logistics
- homeland threat
- number and intensity of existing wars
- faction obligations
- active naval and air commitments
- current casualties and recent failed operations

The baseline should not expand strategic capacity artificially. It should use existing capacity more actively. Evolution III can raise the share of available capacity committed to offensive action, but it cannot create capacity that does not exist.

### Political and legal opportunity

This component matters chiefly to Evolution II.

Important inputs include:

- existing claims, cores, war goals, and scripted objectives
- faction and alliance obligations
- calls to arms
- guarantees and non-aggression arrangements
- subject status
- ideology and current country route
- relations, rivalry, and existing diplomatic hostility
- target isolation
- target involvement in another war
- comparative strength and expected ally response
- world tension and any rules required by the current game state

The event should accelerate the use of legal opportunities. It must not create legal authority where none exists.

## Front behavior

### Priority front selection

The AI should select a limited set of fronts where extra aggression can produce a useful result. Priority should rise when a front has:

- good supply
- a local force advantage
- a weak or exposed enemy sector
- a valuable operational objective
- available reserves
- air support
- a route to continue after the first gain
- a clear relation to the country's existing war goals or strategic plan

Priority should fall when a front has:

- severe supply failure
- impassable or highly unfavorable terrain without a strong advantage
- no meaningful objective
- excessive distance from reinforcement
- recent repeated failures
- a homeland crisis elsewhere
- a more urgent front competing for the same reserves

The event should not give every front the same increased aggression. Concentration is part of the design.

### Attack start behavior

At baseline, the AI should begin attacks sooner when preparations are adequate. It can accept slightly lower local superiority than ordinary behavior when the target is weak, isolated, or strategically valuable.

Evolution I should reduce avoidable hesitation on fronts that remain supplied and reinforced. Evolution III should allow attacks at parity in selected high-value sectors, especially when air support, armour, surprise, or enemy overextension improves the expected result.

A hard safety veto must still stop attacks that would consume the country's last effective reserve, break its replacement system, or expose its capital and critical ports.

### Continuation and pause behavior

The baseline should reinforce success and continue into nearby valuable objectives when the operation remains viable. It should not stop immediately after taking one low-value province if the enemy line is still disordered.

Evolution I should make the AI sustain pressure through a full operational cycle. It should commit follow-up forces, repair the supply route, and continue until one of these occurs:

- the planned objective is secured
- the enemy establishes a stable defensive line
- local supply falls below the safe band
- losses exceed the operation's acceptable burden
- reserves are required by a more urgent front
- weather or terrain makes continuation materially worse
- the home front is threatened

A pause should rebuild organisation, supply, and reserves. It should not become indefinite front inactivity.

### Failure response

Aggression must learn from failure within the current operation.

Repeated costly attacks against the same fortified or undersupplied sector should lower its priority. The AI should redirect reserves, seek another axis, improve air or supply support, or wait for a better opportunity. Evolution III permits greater risk, but it must not turn repeated failure into a reason to repeat the same attack without change.

## Reserve and homeland policy

The event should reduce excessive idle reserves while preserving a hard defensive core.

Protected needs include:

- the national capital and essential industrial regions
- core ports exposed to invasion
- an active enemy landing or airborne threat
- a critical secondary front
- high-resistance occupation needs already required by the base game
- a mobile reserve able to answer a breakthrough

The size of the protected reserve should scale with country size, geography, front count, enemy naval reach, and current threat. Evolution I can commit more reserve to an active breakthrough. Evolution III can accept a thinner reserve when the operation offers a decisive result. Neither can empty critical home defense.

## Production and force composition

### Capacity-first adaptation

The event should change ratios within a country's feasible force model.

A country with strong heavy industry, fuel access, armour technology, and replacement capacity can place more emphasis on tanks, motorised formations, mechanised formations, self-propelled support, and air-ground cooperation.

A country with modest industry can emphasize artillery, engineers, support companies, trucks, and a small mobile reserve.

A poor country should protect rifle, support-equipment, and manpower needs before building expensive attack formations.

### Replacement floors

Offensive equipment priorities must not consume all replacement capacity. The AI should preserve a minimum stock or replacement flow for:

- infantry equipment
- support equipment
- artillery already used by field divisions
- trains and convoys
- garrison needs
- active aircraft replacement
- existing armoured formations
- naval repair and replacement obligations where relevant

Evolution I can raise production for sustaining pressure. Evolution III can accept a smaller reserve stock during a decisive campaign. A country with a collapsing stockpile should return to replacement production before expanding offensive formations.

### Template and role preferences

The event can increase the value of formations suited to breakthrough, exploitation, assault support, and mobile reserve roles. It should use verified country and technology conditions.

It should not:

- give countries free templates
- overwrite unique event or country templates
- force every country toward the same width or battalion composition
- create equipment that the country cannot research or produce
- replace historical or route-specific military identity with one generic army

### Logistics as offensive preparation

Trains, trucks, convoys, ports, railways, airfields, and supply access are part of the offensive posture. When the AI has a valuable operation but lacks logistics, it should be more willing to prepare the enabling capacity instead of attacking immediately into failure.

This can include greater priority for:

- repairing a damaged supply route
- improving the rail connection to a main front
- protecting or expanding convoy capacity
- assigning airfields to the main theater
- securing a port before expanding a landing
- retaining trucks and trains needed by active armies

The event should not grant buildings or equipment. It changes what the AI values.

## Air strategy

Air allocation should follow the main operation.

The AI should prefer to:

- contest air regions covering a priority front
- assign close air support where ground attacks are active
- move aircraft away from quiet regions when the transfer is useful and safe
- protect transport and invasion routes
- preserve home air defense when enemy bombing creates a major threat
- avoid assigning aircraft beyond useful range or without adequate fuel

A country with too few aircraft should concentrate them on one decisive region. A major can support several fronts if it retains reserve and fuel. Evolution III can commit a larger share of aircraft to active offensive zones, but it cannot ignore a severe homeland air threat.

## Naval invasion strategy

Naval invasions should follow a complete feasibility chain.

### Target quality

A target becomes more attractive when it offers:

- a port or immediate route to a port
- weak coastal defense
- connection to an existing front
- isolation of enemy forces
- a strategic island or chokepoint
- access to a valuable supply, industrial, or air region
- a way to relieve an ally or bypass an otherwise static front

### Launch gate

The AI should not launch until it has enough transport, convoys, route access, operational naval or air cover, a viable landing force, and a follow-up supply plan.

The baseline can shorten excessive delay once those requirements are met. Evolution I should maintain follow-up pressure and reinforcement after a landing. Evolution III can attempt a larger or second landing axis when capacity and home defense permit it.

### Failure control

After a failed landing, the AI should reassess target, escort, force size, and supply. It should not repeat the same unsupported landing on a short loop.

## War pursuit and intervention

### Baseline boundary

The baseline makes the AI more decisive with existing objectives. It should not be a global declaration generator.

### Evolution II boundary

Predatory Powers opens the deliberate opportunity layer. AI governments can more strongly pursue:

- existing claims and cores
- available war goals
- scripted expansion objectives
- intervention in wars that affect their faction, rivals, or regional position
- calls to arms that offer a strategic gain
- weak and isolated enemies already connected to a valid diplomatic path
- enemies exposed by another war

Target selection should favor relevance over raw weakness. An isolated claimed state, hostile rival, faction enemy, strategic port, resource region, or encircled opponent is more suitable than a distant weak country with no relation to the AI's route.

### Additional-war restraint

A country should consider another war only when:

- the legal path exists
- existing wars leave enough strategic capacity
- the target is materially weaker or strategically exposed
- likely enemy allies are understood
- supply routes are practical
- the new front does not create an immediate homeland crisis
- expected gains fit the country's route and interests

Evolution III can raise the accepted risk and support more than one opportunity, but it must not create unlimited war stacking.

## Peace and war termination

The event does not make an AI country reject every settlement or fight after normal defeat. It can make the country less willing to become passive while it still has a credible path to improve the war. Capitulation, peace conferences, scripted settlements, White Peace, and event-owned peace systems retain their own rules.

A peace event that ends a war should not be undone by an immediate arbitrary redeclaration. A new war still requires a valid path, target evaluation, and any normal cooldown or diplomatic restriction.

## Country identity protection

The Offensive must not erase country-specific strategy.

Country focus routes, scripted objectives, event actors, naval doctrines, defensive identities, faction duties, and special target restrictions remain authoritative. The event is a generic layer that changes intensity and willingness inside valid behavior.

Examples of protected identity include:

- a country scripted to defend a narrow frontier before a dated crisis
- a naval country whose strategic plan depends on blockade and island control
- a special Chaos actor with unique enemies or forbidden targets
- a subject whose diplomacy belongs to its overlord
- an event country whose survival route requires consolidation before expansion

Where the generic layer conflicts with a hard owner rule, the owner rule wins.

## Performance rule

The event must not use a new unbounded daily, weekly, or monthly sweep over all countries, fronts, wars, or states.

Preferred evaluation paths include:

- native AI strategy plan evaluation
- one-time global activation
- bounded new-country and release hooks
- existing shared event hooks that already evaluate control or country creation
- native war, front, production, and target scoring surfaces

Any recurring evaluation introduced for the event must be country-local, bounded, justified by the engine surface, and proven not to duplicate native AI work.
