# Event 014 Cannibalism, Part 1: Core Design

## Event promise

Cannibalism begins in an army that has been damaged by war, hunger, isolation, and command failure. The first reports should feel like a military institution breaking under pressure. Soldiers vanish from burial details. A field kitchen keeps receiving meat after the livestock convoy stops. Patrols refuse to recover bodies from certain positions. Officers discover that a platoon has changed its ration rolls to remove dead men who were never buried.

The ordinary campaign story is containable. A capable government can restore supply, rotate units, identify the compromised formations, prosecute commanders, protect vulnerable prisoners and civilians, and extinguish the crisis before it crosses a border. A weak or cynical government can hide the evidence, exploit terror, abandon isolated troops, or feed prisoners into the system. Those choices turn the incident into a durable cult.

At higher chaos the cult acquires doctrine, symbols, logistics, and a common military language. Remote islands and cut-off territories become self-contained societies. Cannibal warlords appear. Their states consume population, recruit from the ruins, and attack neighboring countries. A concealed supreme coordinator exists behind the mature network, but no player-facing surface may confirm his identity before the Evolution III reveal.

The final route is a special chaos-country campaign. Hannibal appears, unifies the warlords, communes, islands, cells, and controlled territory, and turns population consumption into a global war economy. If the existing Wendigo country survives to the unification moment, the network can merge with it and produce Wendigo Hannibal. Both completed terminal routes are deliberately absurd and overpowered. The alternate Wendigo route is stronger and becomes effectively unstoppable after its final transformation locks.

## Identity and classification

- Event ID: `14`
- Type: Minor Fire-Once
- Cluster: none
- First host: one random eligible ordinary country at war
- Persistent scope: country-level infection that can spread to other countries after the one global entry event
- Default campaign expectation: limited military crisis, local containment, no global cult
- Rare campaign expectation: organized network, territorial fracture, cannibal countries
- High-chaos expectation: Hannibal reveal and unification
- Terminal expectation: ordinary Hannibal world-end or Wendigo Hannibal world-end

Event 14 fires once through the normal random-event system. Spread, recurrence, country collapse, warlord creation, and unification belong to the event's persistent system. They do not make Event 14 repeatable.

The event does not belong to a cluster. Wars created by Event 7 or other content can improve eligibility through ordinary world conditions, but Event 14 should not be attached to a cluster for guaranteed co-firing.

## The hidden identity contract

Hannibal is an internal implementation fact before Evolution III. His character can be prepared in hidden system state during Evolution II, but every visible surface remains uncertain.

Before the reveal, the following surfaces must not contain his name, a pun on his name, a personal title, a recognizable face, a silhouette that will later match his portrait, or language that proves one supreme leader exists:

- entry and follow-up events
- news and report events
- Event Details
- event-log rows and evolution rows
- decision categories and decisions
- focus names and descriptions
- national spirits and tooltips
- scripted GUI labels, meters, buttons, and alerts
- country names and faction names
- achievements and achievement descriptions
- triggerable scenario name, type labels, and details
- loading tips, debug-facing player text, and music documentation visible in game

Evolution II may show shared symbols, matching orders, synchronized attacks, identical prisoner practices, repeated maps, and common training methods. Public interpretation should remain divided among imitation, captured manuals, traveling officers, radio coordination, and a hidden command structure. No public text settles the question.

The internal specification may use `Hannibal`, `hidden supreme leader`, and `Hannibal network` where implementation and asset production require precision. The reveal flag is the hard boundary. After that flag exists, player-facing surfaces can name Hannibal and display the final portrait.

## Core playable values

### Field Hunger

Field Hunger measures the material and institutional pressure that makes the initial breach possible. It should be visible after the entry event and use red presentation.

Field Hunger rises through:

- low supply in active theaters
- divisions operating while encircled or cut off
- long war duration
- severe military casualties
- convoy losses that interrupt overseas garrisons
- low equipment ratios
- occupied territory with damaged infrastructure
- famine, locust, disaster, plague, or related Chaos Redux pressure where the connection is natural
- deliberate ration diversion
- abandoned prisoners and displaced civilians

Field Hunger falls through:

- restored rail and port supply
- convoy escort and emergency shipping
- unit rotation
- equipment and food relief decisions
- replacing compromised commanders
- evacuating isolated formations
- local stabilization and recovery missions

High Field Hunger does not prove a cult exists. It represents the conditions in which survival acts, predatory killing, concealment, and recruitment become possible.

### Command Integrity

Command Integrity measures whether military and civil institutions can identify, isolate, and punish compromised personnel. It should use blue presentation.

Command Integrity rises through:

- transparent investigation
- protected burial and medical details
- reliable ration audits
- officer replacement
- military police deployment
- successful rotation missions
- prosecution supported by evidence
- protection of witnesses and prisoners

Command Integrity falls through:

- denial
- mass disappearance of evidence
- officers sharing spoils
- field executions without investigation
- deliberate terror exploitation
- repeated mission failure
- unit abandonment
- local surrender to warlord rule

Low Command Integrity makes every suppression action less reliable. Harsh action taken with weak integrity can kill witnesses, punish innocent units, and drive organized cells deeper underground.

### Cult Cohesion

Cult Cohesion becomes visible with Evolution I. It measures how far the behavior has become doctrine, ritual, membership, and ideology. It should use purple presentation.

Cult Cohesion rises through:

- repeated successful predation
- shared rites and symbols
- officer participation
- prisoner exploitation
- terror battalion programs
- hidden state protection
- contact with foreign cells
- surviving attempted suppression

Cult Cohesion falls through:

- cell infiltration
- witness protection
- amnesty that separates frightened followers from organizers
- seizure of ritual stores and records
- destruction of communication links
- capture of warlords
- successful rehabilitation

High Cult Cohesion enables spread even when Field Hunger later falls. A well-fed cult can continue because it no longer treats hunger as the reason.

### Network Reach

Network Reach becomes visible during Evolution II through an uncertain coordination interface. It is a global event value that measures linked cells, communes, islands, warlord states, transport routes, and shared command methods. It should use dark crimson presentation.

Network Reach rises through:

- infected countries
- active state cells
- cannibal communes
- cannibal islands
- warlord countries
- captured ports and rail hubs
- successful foreign seeding actions
- common military victories
- population consumption milestones

Network Reach falls through:

- simultaneous multi-country crackdowns
- destroyed island routes
- captured warlords
- liberated controlled states
- broken radio and courier chains
- destruction of network anchor sites
- elimination of an infected country before it spreads

Network Reach alone does not reveal Hannibal. The Evolution III reveal requires enough network reach, enough independent nodes, sufficient consumed population, high chaos, and a viable unification host.

## Cannibal-country values

### Larder Stores

Larder Stores are a consumable war resource generated through population consumption, prisoner murder, captured enemy losses, raids, and controlled feeding states. The resource must be visible to cannibal countries and must decay.

Larder Stores pay for:

- warband recruitment
- special units
- emergency reinforcement
- long-distance operations
- infiltration cells
- terror actions
- warlord gifts and submission bargains
- final unification actions

Larder Stores cannot be gained from wastelands, zombie territory, states without meaningful population, or heavily contaminated areas that the event marks unusable. Repeated consumption in one state has sharply diminishing returns because the population is physically being removed.

### Frenzy

Frenzy is the tempo of violence, victory, and ritual confidence. It rises through battlefield success, captured capitals, active feeding, and successful terror. It falls through peace, starvation, defeat, liberated states, and failed assaults.

Frenzy affects offensive behavior, reinforcement speed, resistance to morale damage, and AI aggression. Excessive Frenzy can also cause uncontrolled consumption, officer duels, and premature attacks. It should be a strong tool with a real risk rather than a passive bonus stack.

### Network Alignment

Network Alignment measures how readily a cannibal country accepts the mature network's shared orders. It becomes public only during Evolution II, using wording that does not identify a leader.

High alignment unlocks coordinated offensives, shared recruitment, foreign cells, and eventual peaceful absorption. Low alignment unlocks independent warlord branches, manipulation, resistance, and civil conflict during unification.

## Eligibility for the first host

The first host must be an ordinary country at war. The selection model should prefer countries where a plausible breakdown exists.

Strong positive factors:

- war has lasted long enough to damage institutions
- major casualty burden relative to population
- sustained low supply
- overseas or island garrisons
- encircled formations
- damaged railways and ports
- low stability
- depleted equipment and manpower
- occupied foreign territory
- military prisons or large prisoner populations
- high global chaos

Negative factors:

- short, successful war with full supply
- very high stability and command cohesion
- no active army
- no meaningful population or territory
- existing special chaos-country classification
- actual nonhuman classification
- terminal world-end state
- already active Cannibalism system in that same country through spread

The model should choose a real country and a real high-risk theater or state. If no valid target exists, the event weight should display `N/A` in the event list rather than attempting to fire against an invalid scope.

## Ordinary baseline stages

Baseline stages are expected event flow. They are not evolution entries.

| Stage | Internal role | Player experience | Exit paths |
| --- | --- | --- | --- |
| 0 | Eligibility pressure | No public content | Event fires when a valid host is selected |
| 1 | First field evidence | Disturbing military report and immediate crisis idea | Restore supply, investigate, deny, exploit |
| 2 | Confirmed predation | Named formations and states become compromised | Clean containment, underground cells, public panic |
| 3 | Containment campaign | Decision category and timed objectives become central | Local victory, prolonged crisis, spread |
| 4 | Ritual persistence | Cult Cohesion exists if Evolution I is active | Suppression, exploitation, foreign seeding |
| 5 | Territorial fracture | Communes, islands, or controlled states appear | Liberation, negotiated surrender, warlord emergence |
| 6 | Warlord phase | Cannibal countries become military actors | Defeat, independence, network alignment |
| 7 | Network convergence | Multiple nodes act with common direction | Break network, force unification conditions |
| 8 | Reveal and unification | Hannibal becomes public and unifies viable actors | Ordinary terminal route, Wendigo route, global defeat |
| 9 | Terminal or aftermath | World-end or costly global victory | Campaign end-state or reconstruction system |

A campaign can end at Stage 3 with successful containment. Later stages require failures, exploitation, spread, evolutions, and world conditions.

## Local victory and worldwide victory

### Local victory

A country achieves local victory when:

- all active country cells are removed
- all compromised state modifiers are below the active threshold
- no cannibal commune or warlord country controls its core or occupied territory
- the final stabilization mission succeeds
- the country has not chosen an unresolved exploitation policy that preserves cells

Local victory removes the active national crisis, closes ordinary suppression decisions, begins state recovery, and sets a durable local-defeat memory.

A locally cured country is protected from passive relapse caused by its old cells. It can still face the system again through direct external action, such as invasion by a cannibal country, foreign cell seeding, captured prisoners, returning expeditionary forces, or occupation of a cannibal-controlled state. This creates the user's intended case where a country that defeated the crisis can later fight the cannibals militarily.

### Worldwide victory

The event system is globally defeated only when every one of the following is absent:

- infected ordinary country
- active country cell
- active state cell
- cannibal commune
- cannibal island
- cannibal-controlled state modifier
- cannibal warlord country
- unified Hannibal country
- active foreign seeding mission
- pending transformation or unification process

Worldwide victory sets a global defeated memory, clears the world-threat source, stops all event-owned pulses, and prevents spontaneous reactivation. A manual triggerable scenario can still create the system later because manual scenarios are sandbox tools.

## Spread principles

Spread must follow understandable routes instead of random global infection.

Valid spread channels:

- retreating compromised units cross a border
- prisoners are transferred to another country
- military convoys reach an overseas garrison
- allied units share a supply region
- an occupied state changes controller
- a cult cell is deliberately exported
- a warlord country captures territory
- a cannibal island raids shipping
- foreign volunteers return home
- a military prison or deportation site receives infected personnel

Every spread event should have a source, destination, and visible clue. Foreign countries should receive their own containment category and must fight the crisis independently.

## Player experience by campaign scale

### One-country horror

The player sees supply failure, missing soldiers, compromised units, and hard containment choices. The system ends after stabilization.

### Regional cult crisis

Several countries have cells. Players coordinate border controls, prisoner transfers, convoy routes, and intelligence. Local victories matter, but foreign failures can return the threat.

### Warlord war

Cannibal communes and countries control territory. Ordinary countries fight liberation wars and state recovery. Cannibal players manage Larder Stores, Frenzy, recruitment, raids, and network alignment.

### Global unification crisis

Hannibal is revealed and a major chaos country emerges. Warlord politics, absorption, global warfare, population consumption, and terminal routes dominate the campaign.

## Event-log and Event Details direction

Event Details should describe the premise, not mechanical effects. It should present a wartime country facing evidence of cannibalism among units, with the possibility that the behavior can spread if institutions fail. It must avoid naming Hannibal, promising a cult country, or revealing the world-end branches.

The event history actor is the first host country. Later country infection events create normal history entries inside the Event 14 chain. Evolution logs record true mutation milestones:

- Evolution I: behavior becomes ritual and ideology
- Evolution II: cells become an organized transnational network
- Evolution III: the hidden supreme coordinator is revealed and the network unifies

Evolution I and II log wording must remain spoiler-safe. Evolution III can name Hannibal because the reveal occurs in the same milestone.

## Core failure and cleanup rules

The design must account for:

- annexed infected countries
- tag switching
- civil wars
- puppeting and subject transfer
- states changing owner and controller
- warlord country capitulation
- island states with no valid release tag
- player ownership of a country selected for absorption
- Wendigo country already being player-controlled
- Deaths system disabled
- evolutions disabled by settings
- a world-end flag already existing

When an evolution is disabled, ordinary baseline containment still works. Evolution-gated content is skipped cleanly. A disabled Evolution I cannot become a required step for ordinary victory. A disabled Evolution II cannot leave hidden network flags that later force country creation. A disabled Evolution III prevents Hannibal unification and terminal routes while leaving warlord wars and containment functional.
