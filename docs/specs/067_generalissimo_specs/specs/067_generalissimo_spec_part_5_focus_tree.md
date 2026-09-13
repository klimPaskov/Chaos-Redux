# Event 067 Generalissimo Focus Tree

## Tree role

The dedicated focus tree begins when the Generalissimo becomes the effective ruler through peaceful submission, civil-war creation, or civil-war victory.

The tree must remain available after reunification. It should feel like the government of a military commander who can organize a country around several different structures, military strategies, economies, and foreign ambitions.

The tree must not be one vertical ladder of stronger army bonuses. The Generalissimo is already exceptionally powerful. The tree decides what kind of state grows around him, how officers share or lose power, what economy sustains the army, how the government treats civilians, and what order it pursues abroad.

## Host-adaptive design

The same tree can load for any valid host, but it must adapt through dynamic targets, conditional branches, and scripted localisation.

Host adaptation includes:

- capital and backup-capital anchors
- primary arsenal region
- major supply region
- exposed frontier region
- major port region when one exists
- air-command region when one exists
- subject relationships
- faction membership
- existing wars
- army size and equipment identity
- naval and air relevance
- existing military industry
- host government legacy

The tree must not assume one continent, one ideology, one historical border, or one named enemy.

## Tree size and pacing

The final focus count should be large enough to support every route as a real campaign. The expected range is roughly 65 to 90 focuses after host-conditional branches and world-end extensions are included.

The implementation agent determines the final count after MCP inspection and rendering. It may not reduce a branch to one or two generic focuses merely to fit a target count.

Duration guidance:

- 7 days for route handoffs, emergency government choices, and focus-tree state switches
- 35 days for opening consolidation, strategic forks, immediate reforms, and decision-family unlocks
- 70 days for major institutions, industrial programs, doctrine projects, and diplomatic structures
- longer commitments only when the public cost and payoff justify them

The opening should reach the first political and military choices quickly. Several generic stability or political-power focuses before the first route choice are prohibited.

## First-glance lane architecture

The tree should reserve clear horizontal lanes or compact branch regions in this order:

1. Opening and post-coup consolidation at the center
2. Political structure above the center
3. Army and service command to one side
4. Economy and logistics to the opposite side
5. Internal government below the political routes
6. Foreign policy and expansion beyond the military side
7. Postwar integration beneath the opening trunk
8. Hidden world-end extension outside the ordinary visible area until unlocked

The exact left and right choice can change after rendering. The major branch families must remain recognizable at normal zoom.

## Architecture map

```text
Opening consolidation
    -> Secure the military government
    -> Restore a functioning state
    -> Choose the structure of rule
         -> Personal Command
         -> Officer Directorate
         -> National Emergency Council

Opening consolidation
    -> Rebuild the chain of command
         -> Decisive Command
         -> Army of the Nation
         -> Fortress Command
         -> Conditional naval command
         -> Conditional air command

Opening consolidation
    -> Inventory the state
         -> Arsenal State
         -> Mobilized Construction
         -> Shared logistics and supply branch

Choose the structure of rule
    -> Military administrators
         -> Rule through garrisons
         -> Rule through service
         -> Shared courts, civil administration, and officer settlement

Secure foreign recognition
    -> Officer Solidarity and client juntas
    -> Fortress Sovereignty and armed neutrality
    -> Supreme Strategic Sphere and regional hegemony

Civil-war victory or peaceful transfer
    -> Postwar integration
         -> Officer settlement
         -> Regional reconstruction
         -> Subject and faction settlement
         -> Permanent government form

The Generalissimos' World active
    -> Hidden world-order extension
         -> International Command
         -> Rival generalissimo diplomacy
         -> Suppress civilian resistance
         -> Global military order capstone
```

## Opening consolidation branch

The opening branch solves immediate state problems and reveals the main routes.

### Opening state

The country begins with:

- the Generalissimo as ruler and commander
- Government at Gunpoint
- Army of the Generalissimo
- Command Economy Under Mobilization
- Command Cohesion
- one or more post-coup integration missions when a civil war occurred
- unresolved officer and civilian authority questions

### Working focus groups

#### Secure the Capital Command

**Role**

Opening stabilization and capital protection.

**Unlocks**

- capital security decisions
- headquarters selection
- first Command Cohesion mission

**Effects direction**

- improves capital defense and command
- does not grant free permanent forts everywhere
- can add limited anti-air, headquarters, or garrison support when the state can use it

#### Issue the Oath of Command

**Role**

Defines which officers remain in service.

**Unlocks**

- officer reconciliation and purge decisions
- initial commander transfer cleanup

**Tradeoff**

Broad inclusion raises Cohesion faster but keeps potential rivals. A narrow oath protects personal rule and reduces officer depth.

#### Restore the Ministries

**Role**

Reopens ordinary administration under military supervision.

**Unlocks**

- civilian administration decisions
- reduced penalties from Government at Gunpoint

**Reward style**

Administrative recovery, decision access, and idea modification instead of a flat political-power reward.

#### Reopen the Rail Command

**Role**

Repairs the military logistics network.

**Unlocks**

- rail repair
- supply-hub repair
- train and motorization decisions

**Geography**

Uses the saved capital, arsenal, and frontier regions.

#### Decide the Fate of the Old Government

**Role**

Determines treatment of former ministers, parties, monarchs, assemblies, and senior officials according to the host's previous system.

**Choices**

- co-opt technical administrators
- exclude former political leaders
- conduct selective trials

The focus should trigger a choice event or unlock decisions. It must not assume every host had the same institutions.

#### Choose the Shape of Command

**Role**

Political route lock.

**Duration**

A short route handoff.

**Outcomes**

- Personal Command
- Officer Directorate
- National Emergency Council

The three routes are mutually exclusive.

#### Define the Generalissimo's Strategy

**Role**

Military strategy lock.

**Outcomes**

- Decisive Command
- Army of the Nation
- Fortress Command

The military choice is separate from the political structure. A player can combine any political route with any military strategy unless a specific focus has a clear compatibility gate.

## Political structure route family

### Personal Command

#### Narrative role

The military state becomes an extension of the Generalissimo's personal authority. Officers advance through loyalty to him, civilian institutions become administrative tools, and every major decision passes through his staff.

#### Mechanical role

- highest direct military bonuses
- fastest command decisions
- strongest personal-guard and intervention tools
- lower tolerance for officer rivalry
- greater diplomatic isolation
- severe dependence on the Generalissimo remaining active

#### Main focus groups

##### Build the Personal Secretariat

Creates a central staff that coordinates government and armed forces. It upgrades Government at Gunpoint into a more effective personal regime form while increasing the cost of later institutional compromise.

##### Oaths to the Generalissimo

Replaces branch loyalty with personal loyalty. It improves Cohesion quickly when the officer corps is already loyal and creates a larger penalty when Cohesion later collapses.

##### The Guard Above the Army

Unlocks the Generalissimo Guard institution and related decisions. It uses ordinary host units and equipment. It should not create repeated free elite divisions.

##### Command Above Law

Places military directives above ordinary legal review. It strengthens emergency action and suppression, while increasing resistance, condemnation exposure, or diplomatic penalties when harsh actions are used.

##### A Nation in Uniform

Links schools, veterans, public organizations, and administration to the leader cult. It changes mobilization and training decisions and should alter visible country identity.

##### The Staff of One Man

Centralizes strategic planning and foreign policy. It improves war-plan execution while reducing the independence of advisers and regional commanders.

##### Permanent Personal Rule

Capstone that establishes the final personal military state.

Required payoff:

- strongest complete version of the personal regime idea
- Personal Command flag family
- enhanced direct-command decisions
- foreign officer-cult support
- major diplomatic and internal tradeoffs
- achievement tracking

#### Failure state

Low Command Cohesion under Personal Command can trigger regional officer conspiracies, command paralysis, or a second military challenge. It should not default to another full civil war after every temporary drop.

#### AI profile

Militarist, personalist, highly aggressive, or victorious Generalissimo AI should favor this route. AI with weak industry and strong officer rivalry should avoid it.

### Officer Directorate

#### Narrative role

The Generalissimo remains first among the officer corps, but senior commanders receive formal seats and collective responsibility. The route values military unity, negotiated command, and institutional survival.

#### Mechanical role

- best Command Cohesion stability
- stronger commander and service-branch depth
- weaker peak personal bonuses than Personal Command
- stronger succession and internal dispute handling
- better foreign acceptance among other military governments

#### Main focus groups

##### Convene the General Staff Council

Creates the Directorate and opens council appointment decisions using valid existing commanders.

##### Seats for the Service Branches

Balances army, navy, and air representation according to host relevance. A landlocked country receives no empty naval seat.

##### The Vote Behind Closed Doors

Establishes a military decision process. It slows some emergency actions but reduces arbitrary officer conflict.

##### Rotate the Regional Commands

Builds a formal rotation system and improves Cohesion. It also reduces the Generalissimo's ability to use one loyal regional bloc against the rest.

##### Protect the Unity of the Army

Creates tools for mediation, officer arbitration, and controlled retirement.

##### The Directorate Economy

Places production under boards that represent several service branches. It improves resource allocation and reduces the personal-regime civilian burden.

##### Collegial Military Rule

Capstone that formalizes the Officer Directorate.

Required payoff:

- Officer Directorate flag family
- stable Cohesion tools
- improved adviser and commander roster
- officer-council foreign diplomacy
- reduced risk of internal military collapse
- lower direct personal bonuses than Personal Command

#### Failure state

Very low Cohesion can produce reshuffles, forced retirements, and leadership contests. The Generalissimo remains ruler unless a specific route outcome changes that accepted premise. The system should avoid routine coups that remove the event's central character.

#### AI profile

Professional military AI, countries with many skilled commanders, and states facing several service-branch demands should favor this route.

### National Emergency Council

#### Narrative role

The armed forces remain above civilian politics, while selected civilian administrators, economists, jurists, regional leaders, or party figures return under an emergency charter.

#### Mechanical role

- best stability and economic normalization
- strongest diplomatic acceptance
- lower peak military bonuses
- improved civilian resistance management
- controlled path toward limited institutions without removing the Generalissimo

#### Main focus groups

##### Draft the Emergency Charter

Defines military supremacy and the limited authority of civilian institutions.

##### Recall the Administrators

Reuses valid host officials or institutional boards. It improves administration and reduces the penalty from Government at Gunpoint.

##### Courts Under Emergency Law

Creates a legal framework for military rule. It offers better resistance and condemnation control than arbitrary repression.

##### Regional Civil Councils

Uses local administration to raise compliance and repair damaged regions.

##### A Controlled Political Life

Allows bounded parties, assemblies, monarchic institutions, or public councils according to host legacy. It does not restore an ordinary democratic focus tree.

##### The Army as Constitutional Guardian

Defines the Generalissimo as permanent military guardian while civilian government resumes selected functions.

##### The Permanent Emergency Settlement

Capstone that formalizes the National Emergency Council.

Required payoff:

- National Emergency Council flag family
- strongest stability and reconstruction package
- access to civilian diplomatic partnerships
- lower resistance and sanction risk
- reduced personal military peak
- achievement tracking

#### Failure state

If Cohesion falls and civilian resistance remains high, the government can suffer cabinet paralysis, officer backlash, or emergency-charter suspension.

#### AI profile

Stable, economically damaged, diplomatically isolated, or defensive AI should favor this route. An AI seeking rapid conquest should normally avoid it.

## Military strategy route family

### Shared command reforms

Every strategy begins with a shared reform group:

- reorganize headquarters
- standardize operational reporting
- restore officer training
- review division templates
- secure army communications
- establish a Generalissimo command mission system

These focuses should modify Army of the Generalissimo and unlock decisions. They should not each add a separate national spirit.

### Decisive Command

#### Role

Concentrated offensive operations, armor, mobile forces, artillery coordination, air-ground support, and short decisive wars.

#### Focus groups

- identify the main striking force
- rebuild mobile supply
- concentrate artillery and armor
- command reserve breakthroughs
- establish operational exploitation groups
- integrate air support when available
- prepare a named campaign mission
- capstone for decisive warfare

#### Rewards

- template conversion and training decisions
- host-compatible mobile or armored production support
- planning and breakthrough effects
- temporary campaign power windows with fuel and supply costs
- limited elite guard growth

#### Tradeoff

High fuel, equipment, and supply demand. Failed offensives reduce Cohesion and strain the command economy.

### Army of the Nation

#### Role

Large trained armies, reserve systems, officer schools, infantry support, replacement flow, and national military service.

#### Focus groups

- national reserve rolls
- expand officer schools
- standardize infantry equipment
- train regional commands
- integrate veterans
- support artillery and engineers
- deepen mobilization
- capstone for mass national command

#### Rewards

- mobilization and training decisions
- reserve formation missions
- manpower and equipment conversion
- improved reinforcement and organization
- route-specific unit templates based on host equipment

#### Tradeoff

Civilian labor and production burdens. Rapid expansion without equipment lowers Cohesion and unit quality.

### Fortress Command

#### Role

Defense in depth, capital protection, supply resilience, anti-air, rail security, and planned counterattack.

#### Focus groups

- map the command zones
- fortify the capital approaches
- secure rail junctions
- protect supply hubs
- build anti-air and radar where supported
- prepare mobile counterattack reserves
- integrate border commands
- capstone for fortress-state defense

#### Rewards

- state-targeted construction decisions
- dynamic frontier missions
- entrenchment, planning, and supply effects
- strategic reserve decisions

#### Tradeoff

High construction burden and lower offensive tempo. Fortification should not appear in irrelevant interior states.

## Conditional service branches

### Naval Command

The branch appears only when the naval relevance gate passes.

Possible focus groups:

- reconcile the admirals
- secure the naval bases
- centralize convoy command
- protect military imports
- create a marine command
- direct dockyard production
- project the Generalissimo's order overseas

The branch supports the chosen military and foreign-policy routes. It should include actual dockyards, naval bases, convoy systems, marine decisions, or fleet missions where relevant.

### Air Command

The branch appears when the air relevance gate passes.

Possible focus groups:

- unify air command
- secure the air bases
- expand ground support
- protect military industry
- train command liaison officers
- improve radar and interception
- establish strategic air reserves

It should support real air production, bases, radar, missions, and ground operations.

## Economy Under Command

### Shared economic opening

The branch begins with:

- inventory the arsenals
- reopen strategic factories
- map resource shortages
- repair transport administration
- choose the main economic method

The route choice is between Arsenal State and Mobilized Construction. The shared logistics branch remains compatible with either.

### Arsenal State

#### Role

Permanent military production priority, armament boards, repair networks, conversion, and strategic resources.

#### Focus groups

- place factories under command
- reopen armament boards
- prioritize key equipment families
- expand military factories in the saved arsenal region
- secure domestic resources
- improve repair and conversion
- integrate MIOs when the DLC exists
- capstone for the permanent arsenal state

#### Tradeoff

Higher civilian burden, consumer pressure, and diplomatic dependence on resource imports.

### Mobilized Construction

#### Role

Fast strategic construction, rail, supply hubs, infrastructure, airfields, forts, and temporary national projects.

#### Focus groups

- military construction corps
- emergency rail rebuilding
- expand the frontier supply network
- fortify strategic approaches
- build air and naval infrastructure where relevant
- establish temporary construction surges
- manage post-surge exhaustion
- capstone for the mobilized construction state

#### Tradeoff

Temporary power windows consume civilian capacity, fuel, trains, and equipment. The route needs an aftermath and cannot be a permanent free construction surge.

### Shared logistics branch

The shared branch should include:

- train production and repair
- motor transport allocation
- fuel reserves
- supply-hub command
- port and convoy support when relevant
- logistics officer schools
- strategic stockpile decisions

It modifies Command Economy Under Mobilization instead of creating a stack of new ideas.

## Military administrators and internal rule

### Shared administrative branch

Focus groups:

- appoint regional military administrators
- reopen courts and local offices
- map resistance and loyalty
- establish veterans' organizations
- define military police limits
- supervise strategic industry

The branch then chooses a primary method.

### Rule Through Garrisons

#### Role

Direct occupation, military policing, curfews, and command-zone administration.

#### Rewards

- stronger suppression and security
- faster control of rebellious regions
- garrison and logistics decisions

#### Costs

- higher resistance risk after overuse
- greater manpower and equipment burden
- condemnation exposure when abuses occur
- weaker diplomatic acceptance

The route must not create concentration-camp or extermination mechanics. Those belong to the separate camp and repression system.

### Rule Through Service

#### Role

Military public works, veteran administration, civil-defense training, and local service in exchange for political control.

#### Rewards

- better stability and compliance
- construction and reconstruction decisions
- lower resistance
- slower but durable Cohesion

#### Costs

- civilian factory and manpower commitments
- lower immediate suppression
- slower personal centralization

### Shared finishers

- national command schools
- a permanent military civil service
- integrated regional headquarters
- settlement of old government institutions

The political structure route changes the final form of these institutions.

## Foreign policy and expansion

### Opening recognition group

The branch begins with:

- secure foreign recognition
- settle faction status
- define the treatment of subjects
- establish military attaché channels
- choose the external doctrine

The external routes are mutually exclusive because they define different long-term orders.

### Officer Solidarity and Client Juntas

#### Role

Build an international network of military governments and support foreign officer takeovers.

#### Focus groups

- exchange staff missions
- recognize military governments
- cultivate officer contacts
- support a foreign military takeover
- guarantee friendly juntas
- create joint command exercises
- found the International Command when membership gates are met
- capstone for the officer order

#### Membership gates

The faction or bloc requires:

- several independent military governments
- at least one meaningful major or regional power
- compatible diplomatic status
- no active conflict between founding members
- adequate Command Cohesion

#### Costs and risks

- equipment and officer commitments
- intelligence exposure
- dependency among client regimes
- foreign backlash
- rival junta leadership contests

### Fortress Sovereignty and Armed Neutrality

#### Role

Turn the country into a heavily defended military state that avoids broad ideological alignment.

#### Focus groups

- declare strategic neutrality
- guarantee the command frontier
- build border and air defenses
- secure imports and convoys
- establish deterrent mobilization
- mediate regional military crises
- create a defensive compact only when several partners qualify
- capstone for the sovereign fortress state

#### Costs and risks

- expensive construction
- reduced intervention options
- trade dependence
- slower expansion

### Supreme Strategic Sphere

#### Role

Build a regional order through ultimatums, military guarantees, protectorates, and limited wars.

#### Focus groups

- identify the strategic sphere
- pressure exposed neighbors
- demand military access or guarantees
- prepare limited border campaigns
- establish protectorates
- settle conquered regions
- challenge a rival major only after readiness gates
- capstone for regional command

#### Target generation

Targets come from current borders, nearby sea zones, threats, faction position, and host strength. The branch cannot assume historical claims that do not belong to the host.

#### Postwar handling

Every war route must offer:

- military protectorate
- client junta
- restored civilian state under guarantee
- annexation only for valid claims or cores
- staged integration for occupied foreign territory

No free core ladder is allowed.

## Postwar integration branch

This branch appears after peaceful submission or civil-war victory. Some focuses can begin during the civil war, while final settlement requires control of the host.

### Focus groups

#### Reunify the Armed Forces

Integrates surviving formations, removes duplicates, and begins officer settlement.

#### Restore the National Supply Network

Repairs rails, hubs, ports, and stockpiles in war-damaged regions.

#### Settle the Officer Question

Chooses reconciliation, selective retirement, or broad purge. Each choice changes Cohesion and long-term officer quality.

#### Reopen the Provinces

Restores administration and reduces postwar resistance through route-specific tools.

#### Resolve the Subject Commands

Settles subject loyalty, autonomy, and military obligations.

#### Determine the Faction Settlement

Rejoin, leave, lead, or replace the prior faction according to current diplomacy and route.

#### Proclaim the Permanent Government

Convergence focus that requires one political structure, one military strategy, a stable Cohesion threshold, and adequate postwar integration.

The final effect applies the route flag, final idea forms, country identity, and long-term decision set.

## World-end extension

The world-end branch is hidden until The Generalissimos' World begins.

### Generalissimo-led extension

Possible focus groups:

- convene the international general staff
- recognize aligned military governments
- divide theaters of responsibility
- suppress rival generalissimos
- coordinate global production
- break the Civil Authority Compact
- establish client commands
- proclaim a global military order

### Rival-junta interaction

The original Generalissimo does not automatically control every military government. The branch must include diplomacy, coercion, war, and recognition choices that can fail.

### Final payoff

The capstone requires a real world-order threshold, such as leadership of the dominant military bloc, control or alignment of several majors, and defeat of the main civilian coalition. It should not fire after one successful coup abroad.

## Focus and decision integration table

| Focus family | Decision or mission family unlocked |
| --- | --- |
| Opening consolidation | Capital security, officer oath, rail restoration, ministry recovery |
| Personal Command | Personal guard, leader-centered mobilization, direct intervention, officer loyalty |
| Officer Directorate | Council appointments, service arbitration, command rotation, officer mediation |
| National Emergency Council | Civil administration, regional councils, legal settlement, controlled political life |
| Decisive Command | Offensive preparation, fuel commitment, striking-force conversion, campaign mission |
| Army of the Nation | Reserve mobilization, officer schools, equipment drives, regional levies |
| Fortress Command | Dynamic fortification, supply defense, strategic reserve, frontier missions |
| Naval Command | Fleet security, convoy command, marine preparation, naval intervention |
| Air Command | Airbase security, ground-support allocation, radar, air reserve |
| Arsenal State | Armament boards, factory direction, equipment priorities, resource programs |
| Mobilized Construction | Rail, supply, fort, airbase, port, and infrastructure projects |
| Rule Through Garrisons | Garrison allocation, curfew, military police, emergency control |
| Rule Through Service | Public works, reconstruction, civil defense, veteran administration |
| Officer Solidarity | Staff missions, coup support, junta recognition, faction formation |
| Fortress Sovereignty | Guarantees, border readiness, defensive compact, trade security |
| Supreme Strategic Sphere | Ultimatums, protectorates, limited wars, postwar settlement |
| Postwar Integration | Officer reconciliation, regional repair, subject settlement, final government |
| World-end extension | International Command, rival-junta pressure, civilian-coalition war, global order |

## Idea lifecycle audit

| Idea | Start or unlock | Mitigation path | Upgrade path | Failure path | Final forms |
| --- | --- | --- | --- | --- | --- |
| Government at Gunpoint | Junta start | Restore ministries, regional councils, postwar integration | Political structure route | Low Cohesion, harsh administration, unresolved civil war | Personal military state, Officer Directorate, National Emergency Council |
| Army of the Generalissimo | Junta start | Officer settlement and service balance | Military strategy route | Defeat, supply collapse, officer rivalry | Decisive Command, Army of the Nation, Fortress Command |
| Command Economy Under Mobilization | Junta start | Restore transport and civilian administration | Arsenal State or Mobilized Construction | Shortages, exhausted construction, resource crisis | Permanent arsenal, strategic construction state, normalized emergency economy |
| Army Reconstruction | Government victory only | Aftermath decisions | Civilian reserve or reconciled army | Broad purge or unresolved mutiny | Reformed civilian command or lasting command weakness |

The tree should modify these ideas instead of creating a new national spirit for every focus.

## Focus filter taxonomy

Every focus needs current supported search filters that match its primary role.

Required categories:

- Political
- Industry
- Army
- Navy
- Air
- Diplomacy
- Expansion
- Special Mechanic
- Postwar Reconstruction
- World-End Route

A focus can carry more than one filter when appropriate, but each visible focus must have one clear branch home.

## Focus Navigation

The final tree needs navigation shortcuts for spatially separate major regions:

- Political Structure
- Military Command
- Economy and Logistics
- Internal Government
- Foreign Policy
- Postwar Integration
- World-End Command when revealed

Conditional naval and air branches may receive their own shortcut if rendering places them far from the army region. Hidden branches must not appear in navigation before reveal.

## Focus inlay window

A small read-only focus inlay is justified because Command Cohesion and regime structure directly affect focus availability.

The inlay shows:

- Generalissimo portrait
- current political structure
- Command Cohesion meter
- current Cohesion band
- one next important threshold or blocked route reason
- current flag or regime emblem

The inlay contains no gameplay buttons. Decisions remain in the decision system so AI has the same action path.

The implementation must reserve clear tree space and use the current focus inlay database, GUI, and tree attachment pattern. It must use `hoi4.focus_render`, `hoi4.gui_inspect`, and `hoi4.gui_render` for combined review.

## Route-specific AI

### Personal Command AI

Positive factors:

- high aggression
- high war support
- strong Generalissimo victory record
- high Cohesion
- few rival commanders
- active conquest goals

Negative factors:

- severe diplomatic isolation
- low stability
- strong officer rivalry
- economic collapse

### Officer Directorate AI

Positive factors:

- several skilled commanders
- meaningful navy and air services
- medium Cohesion
- need for stable long-term military rule
- several friendly military governments

Negative factors:

- no officer depth
- very low Cohesion
- immediate existential war requiring personal emergency control

### National Emergency Council AI

Positive factors:

- damaged economy
- high resistance
- need for foreign recognition
- defensive strategy
- prior democratic or constitutional institutions

Negative factors:

- rapid expansion plan
- very high military aggression
- active world-end leadership bid

### Military strategy AI

- Decisive Command favors equipment-rich, fuel-rich, offensive states.
- Army of the Nation favors manpower-rich states with moderate industry.
- Fortress Command favors threatened, defensive, resource-poor, or strategically exposed states.
- Naval Command receives weight only when the naval gate passes.
- Air Command receives weight from air industry, air bases, and strategic need.

### Foreign-policy AI

- Officer Solidarity favors several reachable military governments and a viable faction network.
- Fortress Sovereignty favors encircled, neutral, defensive, or diplomatically isolated states.
- Supreme Strategic Sphere favors strong regional powers with valid nearby targets and adequate logistics.

Every route weight is a probability surface and requires the audit scenarios in the probability matrix.

## Reward quality rules

The tree should use:

- decision-family unlocks
- missions
- idea upgrades
- commander and adviser changes
- dynamic state construction
- template conversion
- equipment and manpower commitments
- faction and subject decisions
- claims or war goals only through valid route logic
- country identity and flag changes
- doctrine and research bonuses
- map and supply improvements

The tree should avoid:

- repeated political power rewards
- repeated small stability or war-support rewards
- one new national spirit per focus
- free division spam
- generic claims on every neighbor
- free cores on occupied foreign territory
- token naval or air branches
- several focuses that do nothing except increase the same modifier

## Focus-tree acceptance review

Before completion, the focus implementation must:

1. Inspect the tree with `hoi4.focus_inspect`.
2. Render the complete tree at normal in-game zoom.
3. Identify every major branch, root, fork, and payoff from the render alone.
4. Rewrite layout or route logic where branches are unclear.
5. Confirm no overlaps, line crossings, fake branches, long unnecessary connectors, or hidden-route leaks.
6. Verify focus filters and navigation entries.
7. Review the focus inlay together with the tree.
8. Route weighted focus choices through the probability auditor.
9. Run `chaosx_focus_tree_auditor` after the main implementation.
10. Produce a route coverage table matching every route in this specification.
