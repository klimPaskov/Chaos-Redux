# 011 Secret Alliance, part 2, mechanics and decisions

## Mechanic overview

The hidden phase becomes interesting when the player has tools that carry risk. Secret Alliance should not be a passive debuff or a pure random sabotage chain. The player should build a dossier, protect key systems, pressure suspected states, and prepare military responses. Every important action should have a real cost or opportunity cost.

The player-facing decision category should appear in Evolution II or when evidence crosses a high threshold before Evolution II. It should be directionally called a conspiracy dossier, but final localisation should choose an in-world name based on the player's ideology or government tone.

The category should show:

- current evidence band
- current preparedness band
- current diplomatic isolation band
- known suspects and suspected rings where available
- risk of premature reveal
- current public pressure after the pact appears
- warning if a neighboring suspected member can trigger border escalation

A custom scripted GUI is useful if the implementation can support it cleanly. The dossier should be compact, with target cards for suspects and meter strips for Evidence, Preparedness, Pact Cohesion, and War Clock. If a custom GUI would add clutter, the decision category header and target decisions can carry the information through scripted localisation.

## Value model

### Evidence

Evidence is the player's proof that the incidents are coordinated. It grows through investigations, successful missions, intercepted couriers, foreign leaks, border captures, and careless pact actions. It falls only through specific failures, destroyed files, false leads, or player decisions that trade secrecy for stability.

High Evidence should:

- unlock suspect naming
- reduce diplomatic penalties from public accusations
- weaken outer-ring members
- allow targeted negotiations
- allow public exposure before war
- reduce surprise penalties at reveal
- improve the player's preparedness conversion into combat and security bonuses

Low Evidence should:

- make accusations costly
- make negotiations vague
- let pact members deny involvement
- increase the chance that neutral countries believe the pact's propaganda
- make premature exposure strengthen pact cohesion

Evidence factors:

- stronger gain if the player has an agency, encryption advantage, high stability, or high legitimacy
- lower gain if the player has low stability, active civil unrest, poor intel, or many active wars
- higher gain from neighbor incidents because borders leave physical traces
- higher gain after sabotage incidents that damage named industry or infrastructure
- higher gain if a pact member has low stability or low cohesion

### Preparedness

Preparedness measures how ready the player is for sabotage, border pressure, surprise faction reveal, and sudden multi-front war.

Preparedness should come from concrete action:

- guarding industrial centers
- securing rail and supply hubs
- spending infantry equipment and support equipment on internal security
- assigning troops to border watch missions
- building counterintelligence capacity
- investing army XP into emergency defense plans
- using convoys and fuel to secure sea routes
- building anti-air or radar if air sabotage is a major incident family

Preparedness should not be only a political power sink.

High Preparedness should:

- reduce sabotage damage
- lower surprise penalties
- slow the War Clock after Evolution III
- make public exposure safer
- unlock targeted border actions
- improve defensive bonuses during the first months of the revealed war
- lower pact confidence because members see the player is ready

Low Preparedness should:

- increase sabotage severity
- make the reveal war more dangerous
- cause short panic or mobilization penalties
- let the pact gain first-strike tempo

### Diplomatic isolation

Diplomatic isolation is the pact's success at convincing third parties that the player is dangerous. It should not always be negative. If the player has strong evidence and exposes the pact carefully, isolation can shift onto pact members instead.

Isolation grows from:

- ignored propaganda campaigns
- failed public accusations
- player aggressive wars
- player atrocities or condemnation from other systems
- pact major patron influence
- repeated incidents where the player retaliates without proof

Isolation falls from:

- proven evidence
- careful diplomacy
- neutral observers
- negotiated withdrawals
- inviting third-party inspection
- pact member defections

High player isolation should make neutral countries less willing to support the player and more willing to join the pact as sympathizers. High pact isolation should cause members to defect, delay war, or remain outside the revealed faction.

### Pact cohesion

Pact cohesion measures trust among members. It is not the same as readiness. A pact can be ready but divided, or cohesive but slow.

Cohesion grows from:

- successful sabotage
- player overreaction
- major patron funding
- shared ideology
- shared border fear
- player weakness
- diplomatic victories against the player

Cohesion falls from:

- investigations that expose member names
- negotiated exits
- failed sabotage
- uneven costs among members
- captured couriers
- major patron arrogance
- contradictory ideology among members
- player public proof that embarrasses them

Low cohesion should not instantly end the event. It should make invitations harder, delay reveal, make outer rings defect, and reduce the number of members that join the war.

### Pact readiness and War Clock

Pact readiness exists in the hidden stage. War Clock exists after public pressure has begun, usually Evolution III. Readiness becomes War Clock when the pact is public or close to open conflict.

Readiness grows from:

- time
- high chaos
- major patron membership
- player being at war elsewhere
- player border weakness
- successful sabotage
- low player preparedness
- additional members

Readiness falls from:

- player preparedness
- loss of cohesion
- member exposure
- negotiated pause
- failed border provocation
- major patron restraint

War Clock should not instantly trigger war when Evolution III begins. It should give the player a final active phase with war preparation, public exposure, preemptive strike options, and last-chance diplomacy.

## Decision category phases

| Phase working label, not final localisation | Visibility | Player role |
| --- | --- | --- |
| Hidden reports | Before category | Read event reports and suffer small incidents |
| Dossier opens | Evolution II or high evidence | Investigate, harden, identify suspects, prepare borders |
| Counter-network | Mid Evolution II | Target suspects, turn liaisons, pressure members, reduce cohesion |
| Public confrontation | Evolution III | Expose, threaten, mobilize, attempt last talks, choose war timing |
| Revealed war | After faction reveal | War preparedness and pact-collapse aftermath decisions |

## Investigation decision family

Investigation decisions build Evidence and sometimes identify suspects. They should cost agency attention, command resources, equipment, stability, or time depending on the action.

### Trace courier routes

Meaning: follow suspicious diplomatic bags, rail tickets, telegraph traffic, or port contacts.

Requirements and costs:

- intelligence agency or a weaker emergency equivalent
- political attention as a small part of the cost
- trains, convoys, fuel, or command power based on route type
- higher cost if the player is fighting a large war

Success:

- raises Evidence
- may identify a liaison or armed associate
- may reveal which region the pact uses for meetings

Failure:

- raises exposure risk
- may increase pact cohesion because members know they are being watched
- may damage diplomatic relations with an innocent country if the target was wrong

### Intercept field radios

Meaning: locate and seize illegal transmitters, mobile sets, or codebooks.

Requirements and costs:

- infantry equipment or support equipment for raids
- army XP or command power for coordination
- chance modified by encryption, decryption, radar, agency upgrades, and current stability

Success:

- high Evidence gain
- can reveal a full signatory when the incident family comes from the Saboteur role
- reduces immediate sabotage chance

Failure:

- creates a false lead or local panic
- may lower stability or increase internal security strain

### Turn a courier

Meaning: recruit, bribe, threaten, or protect a low-level courier tied to the pact.

Requirements and costs:

- political power, money-equivalent market burden, or civilian factory burden
- high Evidence or a confirmed suspect
- stability threshold, legitimacy, or agency strength

Success:

- identifies a member ring
- lowers pact cohesion
- can open negotiation with an outer-ring country

Failure:

- courier disappears
- pact readiness increases
- one suspect becomes harder to investigate for a cooldown period

### Convene a neutral inquiry

Meaning: ask foreign observers, lawyers, envoys, or a trusted neutral to inspect the pattern.

Requirements and costs:

- relations or non-hostility with at least one credible neutral
- enough Evidence to avoid embarrassment
- diplomatic cost, convoys if overseas observers travel, and temporary consumer goods burden

Success:

- lowers player isolation
- raises pact isolation if a member is exposed
- can make a liaison withdraw before reveal

Failure:

- raises player isolation
- gives the pact time to burn evidence

## Counter-sabotage decision family

These are defensive actions. They should build Preparedness and reduce incident damage, but they also strain the country.

### Guard named industrial centers

Meaning: protect the most valuable industrial states or event-selected sabotage targets.

Requirements and costs:

- infantry equipment and support equipment
- manpower committed to guard work
- optional command power if active during war
- higher cost for large industry

Success:

- increases Preparedness
- reduces factory and infrastructure sabotage
- can catch saboteurs for Evidence

Tradeoff:

- temporary production efficiency or construction penalty because guard checks slow work
- internal security strain rises if overused

### Secure rail and depot lines

Meaning: protect rail hubs, supply hubs, and critical transport states.

Requirements and costs:

- trains, support equipment, fuel, and divisions placed in key states when possible
- stronger if the player actually controls and connects the routes

Success:

- reduces rail sabotage
- improves first-war supply readiness
- can open a timed mission to hold the guarded corridor

Failure:

- if ignored and sabotage hits, temporary supply penalties should be meaningful

### Harden ports and cipher rooms

Meaning: protect naval access, code rooms, docks, and overseas routes.

Requirements and costs:

- convoys, navy XP or command power, fuel, and support equipment
- more useful for island, coastal, and overseas empires

Success:

- lowers overseas sabotage
- reduces risk of convoy loss incidents
- increases chance of identifying the Banker or Saboteur role

### Emergency counterintelligence sweep

Meaning: rapid search of embassies, party offices, clubs, military depots, and telegraph nodes.

Requirements and costs:

- high internal security strain if repeated
- stability cost risk
- command power, support equipment, and agency requirement or fallback

Success:

- strong Evidence and Preparedness gain
- can damage pact cohesion

Failure or overuse:

- stability loss
- resistance or party backlash
- diplomatic isolation increase if foreign diplomats are mistreated

## Diplomatic pressure decision family

Diplomatic pressure should be safer when evidence is high. It should be dangerous when the player acts from suspicion only.

### Quiet demarche to a suspect

Meaning: send a private warning to a suspected country.

Requirements and costs:

- suspected or named country
- enough diplomatic reach
- cost based on relations, player isolation, and evidence

Success:

- lowers member confidence if the target is guilty
- may shift a liaison away from full membership
- may pause incidents from that country

Failure:

- if target is guilty, pact cohesion may rise
- if target is innocent, relations suffer

### Offer a face-saving exit

Meaning: give an outer-ring participant a route to leave before reveal.

Requirements and costs:

- confirmed liaison or armed associate
- high Evidence and lower player isolation
- economic concession, trade concession, guarantee, non-aggression pact, or temporary market burden

Success:

- removes a member from outer ring
- reduces future invitation capacity
- lowers pact cohesion

Tradeoff:

- can look weak to aggressive pact members
- may raise readiness if full signatories panic

### Public accusation with dossier

Meaning: expose the pact or a member publicly before the pact reveals itself.

Requirements and costs:

- Evidence threshold
- preparedness recommended but not always required
- diplomatic cost and risk of false proof if evidence is marginal

Success:

- raises pact isolation
- can trigger early partial reveal
- may stop outer-ring countries joining the faction

Failure:

- raises player isolation
- strengthens pact cohesion
- speeds Evolution III or War Clock

### Secret bargaining with the Convener

Meaning: seek a backchannel settlement with the country hosting the hidden meetings.

Requirements and costs:

- identified Convener or high Evidence
- not in open war with pact
- concessions may include non-aggression pact, border restraint, trade, withdrawal from a region, or public pledge

Success:

- delays reveal
- lowers cohesion
- may split the pact

Failure:

- Convener shares the talks with members
- player isolation rises
- major patron can use the talks as proof of player fear

## Border and military decision family

Border decisions appear when a suspected or confirmed member neighbors the player, or when a coastal, island, or overseas route creates a clear military contact point.

### Border watch mission

Meaning: place supplied divisions in named border states and hold them for a duration.

Objective:

- use a timed mission that checks actual unit presence, supply, and state control
- duration should vary by border length and chaos tier

Success:

- increases Preparedness
- reduces border incidents
- can capture evidence

Failure:

- border incident severity rises
- pact confidence grows

### Controlled border incident

Meaning: stage a limited response against a confirmed pact member without starting a full war.

Requirements and costs:

- confirmed member or very high evidence
- neighbor or valid border state
- army XP, command power within safe limits, infantry equipment, support equipment, and divisions in position

Success:

- reduces member confidence
- can delay War Clock
- can reveal the pact early if the member calls for help

Failure:

- can trigger reveal
- can start war if the pact is ready
- raises isolation if evidence is weak

### Preemptive war authorization

Meaning: after Evolution III or public pact appearance, the player can choose war timing.

Requirements and costs:

- public pact or confirmed full signatory network
- preparedness or evidence thresholds can reduce penalties

Result:

- gives player a controlled war option before the pact chooses the moment
- if used recklessly, neutral sympathy can shift toward the pact

## Sabotage incident family

Pact sabotage should be meaningful but not campaign-ending by default. Severity should scale with evolution, pact readiness, player preparedness, and member role.

Incident types:

- factory fire
- rail switch sabotage
- dockyard accident
- false military orders
- officer assassination or attempted assassination
- convoy document leak
- border depot theft
- airfield fuel contamination
- propaganda strike
- party office bombing
- telegraph or radio outage

Each sabotage incident should have:

- visible in-world report direction
- hidden actor source when possible
- evidence chance
- preparedness mitigation
- escalation effect on pact confidence or player isolation
- cleanup after reveal so hidden incidents do not keep firing as if the pact is still secret

## Missions

Missions should require the player to act. Avoid passive stockpile checks.

### Protect the line of communication

A timed mission to secure named rail, port, or supply states after suspicious movement is detected.

Success should increase Preparedness and reduce the next sabotage incident. Failure should damage supply, infrastructure, or readiness.

### Guard the conference shadow

A timed mission to identify a meeting route by securing travel nodes, ports, or airfields tied to suspicious diplomatic movement.

Success should reveal a suspect or ring. Failure should burn the evidence trail.

### Keep the border quiet

A timed mission for neighboring pact suspects. The player must place divisions in named border states without launching an uncontrolled escalation.

Success should lower border tension and increase Preparedness. Failure should increase the chance of a provocation.

### Secure the officer corps

A timed mission after threats, blackmail, or assassinations. The player must spend support equipment, command resources, and possibly keep stability above a threshold.

Success should prevent officer killings and may uncover foreign contacts. Failure should create a temporary command penalty or remove a lesser commander only when the implementation has safe targeting.

## Costs and sacrifices

The decision set should use a broad cost palette:

- infantry equipment for guards and border security
- support equipment for counterintelligence and raids
- trains for rail security
- convoys for overseas routes and observers
- fuel for patrols and rapid response
- army XP for defense plans and border incidents
- navy XP for sea-route security when relevant
- air XP for airfield security and surveillance when relevant
- command power for limited emergency orders, always conservative
- manpower committed to guard work
- stability when sweeps or public accusations cause fear
- war support when the public feels threatened
- civilian factory burden for inquiry commissions and security work
- diplomatic relations, guarantees, or trade concessions for negotiated exits

Political power can appear as a supporting cost for diplomatic and cabinet work. It should not be the only cost for major actions.

## Success, failure, and partial success

The player should not get binary perfection. Many actions should have partial results.

Examples:

- A courier is captured but the handler escapes. Evidence rises, but pact readiness rises too.
- The rail line is secured, but factories lose output from guard delays. Preparedness rises, production strain rises.
- A public accusation exposes one member but convinces others that the player will strike first. Pact isolation rises, cohesion among full signatories also rises.
- A border mission prevents a provocation but ties down divisions at a bad moment.
- A negotiated exit removes an outer-ring member but costs the player trade concessions.

## Clutter control

The decision category should never show every possible target and action at once. Use phases, selected suspects, ring visibility, and active mission caps.

Recommended display rules:

- show two to four core actions at any time
- show targeted suspect decisions only for named suspects
- show border actions only when a valid neighbor exists
- show emergency actions only after severe sabotage or Evolution III
- hide obsolete hidden-phase actions after public reveal
- keep AI target evaluation separate so AI can act without human selector clutter

## Optional dossier UI

A scripted GUI dossier would improve the mechanic if implementation resources allow it. It should be a compact panel opened from the decision category.

The UI should show:

- Evidence meter
- Preparedness meter
- Pact Cohesion estimate
- War Clock when public pressure begins
- suspect cards with ring status, evidence level, and action buttons
- warning frame when a border member can trigger reveal
- animated seal or file stamp only when it communicates state

State-driven animation ideas:

- dossier seal closed, active, urgent, public, and compromised states
- suspect card glow for confirmed members
- warning pulse for imminent reveal or high War Clock
- meter shimmer only when a value changes or crosses a band

Static presentation is acceptable if a full GUI would distract from the map and decision loop. The asset prompt still includes animated planning for a dossier seal and warning frame so the implementation can choose the right surface.
