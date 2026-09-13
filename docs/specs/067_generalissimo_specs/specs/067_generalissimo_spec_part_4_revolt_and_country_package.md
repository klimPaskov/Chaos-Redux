# Event 067 Revolt and Country Package

## Revolt purpose

The revolt converts the political danger accumulated through the event into a military conflict whose opening strength reflects the player's earlier decisions.

The civil war should answer these questions visibly:

- How much of the army believes the Generalissimo will win?
- Which regional commands and bases are already loyal to him?
- Who controls the capital, arsenals, railways, airfields, and ports?
- Which commanders follow him?
- How much equipment did the government move beyond his reach?
- Did the government create a loyal reserve?
- Did the government preserve faction and subject support?

The setup must not use one fixed territorial split or one fixed army percentage for every host.

## Revolt triggers

The military revolt begins immediately after any of these outcomes:

- failed arrest
- failed capture
- failed assassination
- failed final removal attempt
- refusal of the Evolution III ultimatum
- the manual scenario's immediate-war type

The same setup effect should serve every route. Scenario input can override the opening strength within the accepted intensity bands, but it must not create a separate weaker civil-war implementation.

## One canonical junta side

The revolt creates one primary Generalissimo junta side.

The preferred implementation is the engine's dynamic civil-war country creation so the junta can inherit the host's territorial identity, technology base, equipment family, cores, and current strategic context.

The junta is identified through stable event-owned markers, including:

- Generalissimo junta country
- Event 067 origin host
- revolt sequence identity
- regime structure
- Generalissimo character ownership
- focus-tree eligibility
- Command Cohesion ownership

A fixed country tag is not part of the accepted design. A fixed tag may be considered only if the dynamic country cannot support the required character, focus, flag, country-leader, or victory behavior. That result would require a documented engine proof and a complete tag collision audit before implementation continues.

## Revolt strength score

The setup uses a hidden normalized revolt strength score. The score combines Generalissimo Influence with the institutions and assets that have joined him.

Recommended contribution structure:

| Component | Relative importance | Design purpose |
| --- | --- | --- |
| Generalissimo Influence | Highest | Represents expected success and broad willingness to join |
| Officer loyalty | High | Determines commander and division alignment |
| Formal command authority | High | Determines access to operational plans and active armies |
| Regional-command support | Medium | Determines territorial nuclei and bases |
| Loyal formation support | Medium | Determines elite and capital-adjacent units |
| Military-industry reach | Medium | Determines factories and stockpile share |
| Internal-security reach | Medium | Determines coup coordination and capital pressure |
| Government counterweight strength | Negative high | Preserves government divisions, headquarters, and command |
| Dispersed arsenals and guard formations | Negative medium | Reduces concentrated rebel strength |
| Recent failed removal | Positive modifier | Gives the junta immediate coordination and urgency |

The implementation may adjust relative weights after probability and scenario audits. Influence must remain the largest single public predictor.

## Army division share

The normal civil-war target bands are:

| Influence band | Typical junta division share before hidden adjustments |
| --- | --- |
| 0 to 24 | 15 to 25 percent |
| 25 to 44 | 25 to 35 percent |
| 45 to 64 | 35 to 50 percent |
| 65 to 84 | 50 to 65 percent |
| 85 to 100 | 65 to 80 percent |

Hidden components move the result within or slightly across a band. A loyal reserve, officer purge, dispersed guard, and secured capital can reduce the share. Supreme Command, protected loyal officers, a failed arrest, and a completed campaign mission can increase it.

The junta should not receive every division. The government needs a viable force unless the event resolves through peaceful submission.

### Division transfer priority

When the engine permits controlled transfer, junta selection should favor:

- divisions in loyal regional-command states
- elite formations tied to the Generalissimo
- armies under loyal officers
- units near military headquarters
- units in major military-base states
- units with high organization and equipment when the network is strong

Government selection should favor:

- the loyal reserve
- units in secured capital and arsenal states
- formations under commanders who resisted him
- divisions deliberately dispersed through counterweight decisions

If the civil-war engine handles unit division internally, owner helpers should influence the overall split and add only the minimum correcting package needed to preserve the accepted result bands. The event must not duplicate transferred divisions by spawning copies.

## Dynamic force package

The junta's initial force package should be based on the host's real army.

Required inputs include:

- host division count
- trained manpower
- infantry equipment stockpile
- support equipment stockpile
- artillery, motorized, armor, and other common host equipment
- host templates
- current doctrine and technologies
- revolt strength score
- selected territory
- current external war
- scenario intensity when relevant

### Template selection

The junta should use valid host templates where possible.

Priority order:

1. existing host infantry template with a sustainable equipment profile
2. existing host mobile or armored template when equipment permits
3. existing host garrison or reserve template for rear areas
4. event-owned emergency template built from ordinary host equipment only when no usable host template exists

The event must not create a new sub-unit or equipment archetype.

### Minimum viable force

If the engine's civil-war split would leave the junta without enough divisions to hold its initial territory, a bounded emergency guard package may be created. Its size scales with host population, industry, equipment, and revolt strength.

The emergency package must debit or divide real manpower and equipment. It is not a free division reward.

### Government force protection

The same setup must ensure the original government keeps a viable army. A very high revolt strength can make the government weaker, but the event should not delete its ability to fight through an invalid unit split.

## Commander and officer split

The Generalissimo always transfers to the junta first.

Other commanders are selected through officer loyalty and current relationships.

Positive transfer factors:

- appointed by the Generalissimo
- protected through one of his demands
- command of a loyal regional area
- command of a division or army aligned with the junta
- military or authoritarian political traits
- poor relationship with the current government where a supported marker exists

Negative transfer factors:

- identified as part of the loyal reserve
- previously rotated or investigated
- command of the capital defense
- active government or civilian leadership role
- event-owned conflict that makes transfer invalid

The event must not clone a commander. A transferred character is removed from the government roster before joining the junta.

### Event 019 claimant commanders

A valid Event 019 claimant can:

- join the Generalissimo
- remain with the government
- create a separate rival military camp when Event 019's owner contract permits it

The Generalissimo remains the only Event 067 character and the leader of the primary junta. A claimant can never be silently converted into him.

## Territory selection

The junta should begin with one coherent command nucleus and may gain additional connected regions at high strength.

The setup must avoid checkerboard civil wars, isolated single-province pockets without supply, and random ownership that ignores military infrastructure.

### State scoring

Eligible host core states receive a hidden loyalty score from:

- army headquarters or major military presence
- air bases
- naval bases
- military factories
- supply hubs
- rail junctions
- infrastructure
- major victory points
- strategic location near the capital
- decisions that gave the Generalissimo regional authority
- loyal commanders or guard formations
- distance from secured government command states

Government countermeasures reduce the score in named states.

### Nucleus selection

The primary nucleus should:

- contain at least one valid capital candidate
- contain enough population and industry to sustain a force
- have a supply connection or a viable port
- form a connected state group where geography permits
- avoid taking every important state from the government at medium strength

High revolt strength can add one or two secondary connected command regions. Secondary regions should connect by land or reliable sea route, or they should have enough port and local strength to survive as an island command.

### Dynamic host size rules

| Host size | Territorial target |
| --- | --- |
| Small valid host | One compact nucleus with a viable government remainder |
| Medium host | One main nucleus and an optional secondary military region |
| Large or continental host | One main nucleus plus one or two connected command regions |
| Archipelagic host | Port-centered regions with naval access and no unsupported inland pocket |
| Landlocked host | Rail and supply-hub regions with no naval assumptions |

Countries that cannot sustain two viable sides are invalid normal targets.

## Capital handling

### Junta capital

Priority order:

1. highest valid victory point inside the primary junta nucleus
2. state with the strongest military headquarters or base score
3. state with a supply hub and sufficient population
4. port state with a viable sea route for an archipelagic host

The selected state should be saved as the junta capital anchor for later focuses, decisions, and missions.

### Government capital

The original government keeps its existing capital when that state remains under government control.

If the junta receives the former capital, the government relocates to:

1. highest victory point in a controlled core state
2. strongest supply-connected administrative state
3. strongest port state when no land-connected alternative exists

Both sides must have valid capitals after setup.

## Industry and stockpile split

The junta receives factories based primarily on selected territory. Military-industry reach can modify stockpile and production transfer.

### Stockpiles

The transfer can include:

- infantry equipment
- support equipment
- artillery
- motorized equipment
- armor where available
- aircraft where available
- trains
- convoys
- fuel

The amount is a bounded share of real host stockpiles. The share uses revolt strength, military-industry reach, dispersed arsenal countermeasures, and the selected territory's military infrastructure.

The event must not grant a large stockpile independently of host resources except for the small emergency minimum needed to avoid unarmed spawned divisions.

### Factories

Factory control follows territory. A limited temporary production modifier may represent staff seizure, sabotage, or disorganization during the first weeks.

The event must not copy factories to both sides.

## Navy split

A meaningful navy split occurs only when the host has a navy and the Generalissimo has naval support.

Inputs include:

- number and type of ships
- naval bases in junta territory
- admiral loyalty
- Maritime Command overlay
- internal-security and communications control
- government action to secure the fleet

Low support can leave the navy with the government. High support can transfer a substantial fleet share to the junta.

Ships must transfer through a safe supported engine route. If exact ship transfer cannot be controlled, the implementation should rely on the civil-war engine and adjust naval loyalty through admirals, bases, and temporary readiness effects. It must not duplicate ships.

## Air-force split

Air wings and aircraft stockpiles use:

- air bases in junta territory
- air commander or high-command loyalty where available
- revolt strength
- operational mandate
- government action to disperse aircraft

The result should leave both sides able to use the aircraft they receive. Air wings should not be stranded without bases when the setup can avoid it.

## External wars

The revolt does not create a free peace with existing enemies.

The implementation must inspect the civil-war precedent for war inheritance and preserve a coherent result:

- the government remains the internationally recognized original belligerent at opening
- the junta fights the government immediately
- external enemies may continue fighting one or both sides according to engine behavior and explicit diplomatic decisions
- the event should not silently remove guarantees, wars, or faction obligations without a defined outcome
- the Generalissimo can seek recognition, arms, or a limited truce through decisions after the revolt begins

An external enemy may exploit the split, recognize the junta, support the government, or remain hostile to both. These choices need AI logic and must not create automatic faction abuse.

## Faction handling

### Original government

The original government normally remains in its existing faction during the opening phase.

If it was faction leader, it keeps leadership at setup. A defeated or capitulated government can lose leadership through the normal faction rules.

### Junta

The junta normally begins outside the faction. It may receive recognition, military access, volunteers, or membership through explicit outcomes.

A faction should not automatically accept a rebellious military government simply because it controls many divisions.

### Faction decisions

Faction leaders can receive a bounded response event with options to:

- support the legal government
- recognize the junta
- refuse involvement
- seek a temporary military settlement

The response considers ideology, relations, war situation, strategic dependence, and the Generalissimo's strength.

## Subject handling

Direct subjects normally remain aligned with the recognized original government at revolt start.

A limited subject can recognize the junta when:

- the Generalissimo previously controlled its military relationship
- the subject has high military dependence on the host
- the junta controls the host capital
- revolt strength is very high
- the subject's government is itself military or unstable

No subject is annexed automatically.

After junta victory, subjects receive a settlement outcome that can preserve the relationship, demand autonomy, or enter the Generalissimo's military order.

## Peaceful submission package

Peaceful submission transforms the host without creating a second country.

Required changes:

- Generalissimo becomes country leader
- he remains an active commander
- ruling government becomes a military junta through the appropriate ideology and party package
- Generalissimo Influence closes
- Command Cohesion opens
- the Generalissimo focus tree becomes active
- event-owned junta decisions replace the crisis category
- the complete ruler trait family is applied
- the starting junta ideas are applied
- existing technology, equipment, stockpiles, cores, claims, subjects, and armed forces remain
- incompatible old political decisions are closed or safely bypassed
- the host keeps a readable national territorial name
- a route-appropriate junta flag is applied

Peaceful submission should produce higher starting Command Cohesion than a civil-war victory because the officer corps did not split.

## Civil-war junta country identity

The civil-war side should preserve the host's readable territorial identity. The map should remain understandable when the event occurs in any major country.

The regime identity is shown through:

- Generalissimo country leader
- ruling party and ideology
- event-owned country flags
- one of the event-owned junta flag families
- dedicated focus tree
- starting ideas
- decision categories
- diplomatic behavior
- Event Details and news text

A universal country name that makes several world-end countries share an identical map label is discouraged. The implementation should use the dynamic civil-war country's inherited or host-derived name where possible.

## Junta flag families

Three fictional flat flag families support the three political structures in the focus tree:

1. Personal Command
2. Officer Directorate
3. National Emergency Council

The civil-war junta begins with the Personal Command flag because the revolt is organized around the Generalissimo. A later political route can adopt another family.

Every flag requires normal, medium, and small sizes. The final designs use ImageGen under the flat flag workflow and must not contain readable text, waving fabric, perspective, scenery, gradients, or copied real extremist symbols.

## Ideology and ruling party

The opening junta uses non-aligned military rule unless a verified engine or country-specific constraint requires another broad ideology.

The focus tree can later produce:

- a personal military dictatorship
- a collegial officer directorate
- a military-led emergency council with limited civilian institutions

These are political structures, not a quota of communist, democratic, fascist, and non-aligned branches. The tree should not add shallow ideology paths simply to fill every ideology.

## Starting ideas

The junta begins with no more than three major Event 067 ideas.

### Government at Gunpoint

**Role**

Represents disrupted administration, uncertain legitimacy, and military emergency rule.

**Opening form**

- political and administrative penalties
- resistance or stability pressure
- faster emergency decisions
- stronger military control

**Lifecycle**

- Personal Command converts it into a permanent personal regime form
- Officer Directorate converts it into a collegial military-state form
- National Emergency Council reduces its penalties and restores limited civilian administration
- defeat or reunification cleanup removes obsolete forms

### Army of the Generalissimo

**Role**

Represents direct command, officer loyalty, and the exceptional commander package.

**Opening form**

- strong organization, planning, reinforcement, and army experience effects
- effect scales or changes with Command Cohesion
- tied to the Generalissimo being active and ruling

**Lifecycle**

- military strategy branches convert it into Decisive Command, Army of the Nation, or Fortress Command forms
- it is removed if the Generalissimo is permanently defeated

### Command Economy Under Mobilization

**Role**

Represents military control over production and logistics.

**Opening form**

- military production and repair support
- civilian burden, consumer pressure, or efficiency disruption
- faster emergency logistics projects

**Lifecycle**

- Arsenal State strengthens military output at a continued civilian cost
- Mobilized Construction improves infrastructure and logistics with a temporary exhaustion cycle
- National Emergency Council can normalize part of the economy

## Command Cohesion

Command Cohesion replaces Generalissimo Influence after the takeover. Only one of the two values is visible at a time.

Command Cohesion measures whether senior officers, regional commands, service branches, and military administrators accept the current structure.

### Suggested bands

| Cohesion | State | Consequence |
| --- | --- | --- |
| 0 to 24 | Fractured command | High officer conflict, weak focus and decision access, risk of regional command crisis |
| 25 to 49 | Contested command | Basic government works, but route actions are expensive and military coordination is uneven |
| 50 to 74 | Unified command | Normal route access and strong military coordination |
| 75 to 100 | Command state | Strongest junta actions, foreign officer support, and route capstones |

### Cohesion sources

Cohesion rises through:

- civil-war victory
- officer settlement
- successful command missions
- secure regional headquarters
- balanced service appointments
- military victories
- focus-route consolidation
- effective supply and production

Cohesion falls through:

- rival officer purges
- lost capitals or headquarters
- severe defeats
- low equipment and supply
- contradictory route decisions
- ignored service branches
- excessive personal favoritism under the Directorate route
- civilian resistance under harsh rule

The value must change decisions, focus availability, military effects, foreign policy, and crisis outcomes.

## Starting research and technology

The junta inherits the host's researched technologies and research slots. It does not receive free advanced technology.

The focus tree can grant:

- doctrine research bonuses
- military research bonuses
- equipment research bonuses
- host-relevant naval or air research bonuses

No new technology, doctrine folder, or mutually exclusive technology branch is created by Event 067.

## Laws, economy, and production

The junta should inherit valid host laws and production lines where possible.

The setup may shift political laws toward emergency military rule when the engine and DLC allow it. It must not grant free Total Mobilization or another top law without meeting a route condition or paying a defined cost.

Production lines and MIO relationships should remain valid. A DLC-dependent MIO action is optional and cannot be required for the core path.

## Starting manpower, equipment, fuel, trains, and convoys

Civil-war creation divides existing resources. Peaceful submission preserves them.

The junta must begin with enough manpower and equipment to field its inherited or generated divisions. The setup should never use a large arbitrary grant that ignores the host's actual stockpile.

Fuel, trains, and convoys matter when the host's army or geography needs them. An island or naval host requires enough convoys and access to sustain the starting territory.

## Reinforcement pathways

The junta must have credible ways to build more forces after the opening split.

### Officer Class Mobilization

Converts manpower, infantry equipment, support equipment, and army experience into trained divisions based on valid host templates.

### Requisition the Arsenals

Uses controlled military factories, regional command states, and equipment costs to restore captured or damaged stockpiles.

### Regional Command Levies

Raises bounded local formations from controlled core states. Availability depends on Command Cohesion, local control, and equipment.

### Integrate Defecting Formations

Transfers or recreates formations that defect through events, subject choices, or government collapse. Every transfer must avoid unit duplication.

### Foreign Officer Missions

Receives equipment, volunteers, advisers, or license support from friendly military governments. This route creates diplomatic dependence and foreign influence.

### Generalissimo Guard

Creates a small elite formation family using ordinary host equipment and valid existing sub-units. It is a route-specific template and institution, not a custom unit type.

## Navy and air development

The focus tree and decisions adapt to the host.

### Naval relevance gate

A naval branch appears only when the country has:

- a controlled port
- a meaningful coastline or overseas role
- a navy or credible naval production path

The branch can cover naval-command loyalty, convoy protection, dockyard direction, marine forces, and regional intervention.

Landlocked countries do not receive token naval focuses.

### Air relevance gate

An air branch appears when the country has an air force, air bases, or enough industry to build one. It supports ground operations, logistics, interception, and command integration.

## Intelligence and internal security

The no-DLC package uses ordinary decisions, country modifiers, and event outcomes.

With a relevant intelligence DLC, the junta can gain optional operations and agency interactions, such as:

- cultivate officer contacts abroad
- support a military takeover
- protect the Generalissimo
- infiltrate rival commands

These additions cannot replace the no-DLC decisions.

## Advisors and command staff

The event should reuse valid host commanders and officials when they join the junta.

New portrait-bearing advisers are not required merely to fill slots. Institutional boards can be represented through ideas and decisions when no suitable existing character exists.

The original Generalissimo portrait is the only mandatory new character portrait.

## Victory and reunification

### Junta victory

When the junta defeats the government:

- the winning junta retains its country identity
- the host's cores and claims remain
- the dedicated focus tree remains active
- the Generalissimo remains country leader and commander
- his complete ruler trait family remains
- Command Cohesion receives a victory increase
- temporary civil-war setup modifiers are replaced by postwar integration forms
- subjects and faction relationships enter a settlement sequence
- former government leaders are handled through route-appropriate exile, retirement, imprisonment, or reconciliation outcomes
- no second Generalissimo is created

### Peaceful submission

The country enters the same long-term tree with stronger starting Cohesion and less physical destruction. It does not receive the civil-war victory rewards that represent battlefield consolidation.

## Government victory

When the original government defeats the junta:

- the Generalissimo is captured or killed and permanently removed
- his commander role is unavailable
- Generalissimo Influence closes
- the world-end branch loses normal readiness
- loyal commanders are tried, retired, reconciled, or reabsorbed through aftermath decisions
- transferred divisions and stockpiles are reconciled through the civil-war outcome
- temporary junta country markers are cleared
- the government receives an Army Reconstruction aftermath

### Army Reconstruction aftermath

The government chooses among:

- broad purge
- selective trials
- officer reconciliation
- civilian reserve reform

Each route has distinct military and political costs. No route restores full pre-crisis military efficiency instantly.

## Postwar integration

A victorious junta must repair the host instead of receiving only a victory popup.

Required postwar decision families include:

- restore rail and supply command
- disarm isolated government formations
- reconcile or purge officers
- reopen armament plants
- integrate government-held regions
- settle subject and faction relations
- rebuild air and naval command
- establish the chosen political structure

The decisions should phase out as integration completes.

## Country package matrix

| Surface | Peaceful submission | Civil-war junta at start | Junta after victory | Government after victory |
| --- | --- | --- | --- | --- |
| Country tag | Original host | Dynamic civil-war country | Winning dynamic junta country | Original host |
| Country name | Host territorial identity | Host-derived civil-war identity | Host territorial identity under junta | Original host identity |
| Leader | Generalissimo | Generalissimo | Generalissimo | Original or lawful successor |
| Commander | Generalissimo active | Generalissimo active | Generalissimo active | Generalissimo removed |
| Focus tree | Generalissimo tree | Generalissimo tree | Generalissimo tree | Original host tree |
| Public value | Command Cohesion | Command Cohesion | Command Cohesion | No Event 067 value after aftermath |
| Starting ideas | Three junta ideas | Three junta ideas | Upgraded postwar forms | Army Reconstruction aftermath |
| Forces | Existing full host army | Dynamic share and emergency minimum | Reunified forces after integration | Surviving government forces after integration |
| Technology | Preserved | Inherited civil-war technology | Preserved | Preserved |
| Stockpile | Preserved | Dynamic real share | Reunified subject to losses | Reunified subject to losses |
| Subjects | Preserved pending settlement | Normally remain with government | Settlement sequence | Preserved pending settlement |
| Faction | Preserved pending route | Normally outside | Route-dependent | Preserved unless war outcome changes it |
| Flag | Personal Command opening flag | Personal Command flag | Route flag | Original flag |

## DLC compatibility

The complete crisis, revolt, country package, focus tree, decisions, AI, and world-end branch must function without DLC.

DLC can add:

- intelligence-agency operations
- military-industrial organization interactions
- medals or officer-corps presentation
- expanded subject or occupation choices
- additional naval or air systems

A missing DLC must hide or replace only the optional enhancement. It cannot block normal progression, removal, civil war, reunification, or world-end readiness.
