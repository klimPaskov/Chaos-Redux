# 011 Secret Alliance, part 1, core event design

## Working identity

Secret Alliance is a hidden diplomatic and intelligence crisis aimed at the current player country. It starts as a private agreement among three foreign countries that are not at war with the player. At first the player sees scattered incidents that can be explained away as normal world disorder. Over time the incidents begin to rhyme. Delegations travel through neutral capitals. Industrial fires occur near sensitive plants. Border officers go missing. Newspapers in unrelated countries begin repeating the same accusations. The player should feel watched before the enemy admits that it exists.

The public name after reveal is dynamic: `Anti-[player country] Pact`. This dynamic name is not meant to be a generic string pasted into every text surface. It should be presented as a faction identity once the pact is revealed, and as a suspected target phrase only when the player has enough evidence.

## Playable promise

The event should make the player manage uncertainty. The strongest part of the concept is that the enemies have already decided to act, but the player does not know who they are. The early game is not about clicking a war button. It is about reading signs, deciding how much to spend on internal security, choosing whether to accuse foreign governments with incomplete proof, and preparing for a future war that might be real.

The player loop is:

1. Subtle incidents begin in the player's country and along foreign diplomatic routes.
2. Hidden pact members gain coordination, evidence exposure, and war readiness in the background.
3. The player can ignore the pattern, investigate it, harden industry, secure borders, pressure suspected countries, or attempt backchannel talks.
4. Investigation builds evidence and identifies suspected members.
5. Countermeasures increase player preparedness and can reduce pact cohesion.
6. Reckless exposure can drive the pact closer together, especially before enough evidence exists.
7. War, border escalation, or Evolution III makes the pact visible.
8. Once revealed, the pact forms an open faction against the player and becomes a conventional diplomatic and military problem with memory of the hidden phase.

## Event temperament

Secret Alliance should be tense, not instantly apocalyptic. The baseline incident belongs to the space between diplomacy, espionage, and war. The final reveal can be dramatic enough for a super-event because it changes the player's understanding of many previous incidents. The design should avoid turning the hidden phase into a simple countdown that always ends the same way.

The pact members should have motives. Some fear the player. Some want territory. Some resent ideology. Some are pushed by a major patron. Some believe the player is a future conqueror. Some are opportunists who join because the pact looks strong. This variety lets the same system produce different campaigns.

## Eligible target and member principles

The target is the active player country at the time the event fires. The design assumes the event is player-facing and should not create an anti-AI pact unless the implementation intentionally adds an AI-player equivalent for multiplayer or observer contexts.

Initial members should be three valid countries selected from the world. The best candidates are minor countries outside factions, not at war with the player, not subjects of the player, not dependent on the player, and not already locked into a major scripted crisis. The event should prefer candidates that have a plausible reason to fear, resent, rival, or profit from opposing the player.

Initial selection should avoid:

- countries at war with the player
- player subjects, puppets, integrated puppets, and protected dependencies
- faction members where a hidden separate pact would conflict with their faction obligations
- countries already inside event-owned special country systems that should not be repurposed
- countries too weak to survive a revealed war unless the pact has a major patron
- countries without a valid diplomatic route to the player unless the design needs a remote sponsor
- nonhuman or terminal chaos actors, unless a later event explicitly allows strange cross-event interference

Initial selection should prefer:

- minors not in factions
- countries sharing a land or sea region with the player
- countries with claims, cores, ideological rivalry, damaged relations, border tension, or recent diplomatic conflict with the player
- countries that have been harmed by player conquest, puppeting, guarantees, sanctions, embargoes, raids, or faction leadership
- countries whose ideology is opposed to the player's ruling ideology
- countries that have high war support, low fear of escalation, or strong foreign patron access

The implementation should score candidates rather than use pure random selection. Randomness gives replay value, but the pact should not feel arbitrary when the player inspects the evidence later.

## Pact roles

The initial three members should receive hidden roles. Roles define what incidents they prefer, how much evidence they leak, and how they behave when the pact is revealed.

| Role working label, not final localisation | Member type | Hidden behavior | Reveal behavior |
| --- | --- | --- | --- |
| Convener | Best diplomat or safest capital among the members | Hosts meetings, manages invitations, lowers cohesion loss | Tries to become faction leader unless a major patron exists |
| Saboteur | High industry, intelligence agency, or close route to player | Creates industrial, rail, port, and convoy incidents | Focuses on strategic bombing, raids, and border pressure |
| Agitator | Ideological rival or propaganda-capable country | Spreads accusations, supports internal unrest, reduces player diplomatic standing | Pushes war justification and refuses early compromise |
| Border Hand | Neighbor or near-neighbor | Creates border incidents, missing patrols, troop probes, and local scares | Opens border-war and limited-war escalation routes |
| Banker | Wealthier neutral, trade hub, or market actor | Funds other members, bribes officials, increases pact readiness | Provides production and lend-lease support to pact members |
| Patron | Major or strong regional power, mainly Evolution II onward | Raises membership ceiling, hides minor members, arms them, pressures neutrals | Takes or contests faction leadership and accelerates war planning |

Not every campaign needs every role. The first three members should cover at least two roles so the hidden phase produces mixed incident types.

## Hidden membership rings

The pact should not treat every member as equally committed from the first day. Use membership rings so the player can reveal the network gradually.

| Ring working label, not final localisation | Meaning | Player evidence state | War behavior |
| --- | --- | --- | --- |
| Full signatory | Bound by the hidden anti-player pact | Can be proven with enough evidence | Joins the revealed faction and joins war |
| Armed associate | Receives plans, arms, or intelligence but has not signed full terms | Evidence can identify support channels | May join faction on reveal if confidence is high |
| Liaison | Sends diplomats or observers | Evidence can expose contact but not full commitment | May withdraw if player exposes early with strong proof |
| Sympathizer | Politically aligned outsider | Appears in rumours and press networks | Can be invited later, rarely forced into war |

This ring system lets the player weaken the pact before reveal. A successful investigation should not always prevent the pact, but it can reduce how many outer-ring countries become full enemies.

## Baseline flow

Baseline starts with three hidden minor signatories. The pact is slow and subtle. It should not announce itself through a decision category immediately. The player sees a small chain of report-style incidents or normal events that use uncertain information.

Baseline incident families:

- unexplained industrial fires near sensitive factories
- missing cargo or convoy documents
- border patrol disappearances when a pact member borders the player
- foreign newspapers repeating similar accusations against the player
- trade delegations meeting in unrelated capitals
- arrests of low-level couriers with unclear papers
- sudden increase in espionage pressure
- diplomatic notes that avoid naming the pact but repeat the same formula
- officers or engineers resigning after suspected blackmail
- minor sabotage of rail hubs, ports, depots, or airfields

Baseline effects should be noticeable only after repeated incidents. The first incident can be dismissed. The third or fourth should make the player suspect a pattern. The design should avoid a single early popup that tells the player exactly what is happening.

## Player knowledge states

Player knowledge should be stored as a readable progression, not as an all-or-nothing flag.

| Knowledge state working label, not final localisation | What the player sees | Gameplay surface |
| --- | --- | --- |
| Uneasy pattern | Reports repeat across regions but no country is named | Event reports, small temporary effects |
| Suspected channel | One country or route is suspicious but not proven | Event detail can show partial dossier direction |
| Named suspect | A country appears in evidence, still deniable | Decision category can show suspected target actions |
| Confirmed member | Evidence identifies a member or full signatory | Player can pressure, expose, sanction, or prepare targeted action |
| Public pact | The hidden network becomes an open faction | Faction appears, super-event fires, war logic opens |

The player should never be required to memorize hidden events. The decision category that appears in Evolution II should summarize current evidence, suspected countries, preparedness, and risk in a compact player-facing way.

## Core values

The event should use dynamic values. These values can be displayed through decision category text, scripted localisation, ideas, event details, and the optional dossier UI described in later files.

| Value working label | Owner | Meaning |
| --- | --- | --- |
| Evidence | Player | How much proof the player has gathered about the pact |
| Preparedness | Player | Readiness against sabotage, border incidents, intelligence pressure, and surprise war |
| Exposure risk | Player and pact | Risk that an action reveals the pact before either side is ready |
| Diplomatic isolation | Player | How much the pact has damaged third-party trust in the player |
| Internal security strain | Player | Cost of hardening the state and hunting cells |
| Pact cohesion | Pact network | Whether members trust each other and remain committed |
| Pact readiness | Pact network | How close the pact is to open action |
| Pact aggression | Pact network | How willing members are to sabotage, threaten, or provoke |
| Member confidence | Per pact country | How likely a member is to invite others, escalate, or stay in the faction after reveal |
| War clock | Pact network | Public war pressure after Evolution III or reveal-adjacent escalation |

## Event Details direction

The Event Details window should describe the premise as a hidden pattern around the player country. It should not list mechanic values, exact rewards, or hidden member identities. It should make clear that the incident is about a possible coordinated foreign effort that begins with deniable contacts and unexplained pressure.

The details text should change once the pact is public. Before reveal, it should speak from the player's uncertain perspective. After reveal, it should describe the public Anti-[player country] Pact and acknowledge that earlier incidents are now being reinterpreted.

## Event log and evolution log direction

The event log should show Secret Alliance as a fired minor fire-once event after the hidden pact is created. Evolution logs should record only the actual evolutions, not ordinary baseline incidents. Baseline stages are normal event progression and should remain separate from evolution entries.

Evolution names should be direction-only until localisation is written. They should distinguish these concepts:

- Evolution I: more minor members enter the hidden network
- Evolution II: a major patron or major founder becomes part of the pact structure
- Evolution III: the pact becomes public enough to appear on the map and moves toward open war

## Interaction with player history

The pact should feel more likely when the player has become frightening. Selection and pacing should react to:

- player conquest and annexation history
- player faction leadership and alliance size
- player wars against minors
- player world tension contribution
- player ideology and ideological enemies
- player bordering many small states
- player recent use of unconventional warfare, if the broader Chaos Redux system tracks condemnation
- player intervention in civil wars, puppeting, or forced regime changes
- player strength relative to nearby minors

A peaceful player can still be targeted, but the pact should be slower, more defensive, more likely to include nervous neutrals, and more vulnerable to negotiation.

## Localisation direction for early incidents

Early text should show observed fear and uncertainty directly. It should not announce that the event is a warning or tell the player that a pact exists. It should use concrete details: missing engineers, copied slogans, courier routes, damaged switchboards, abrupt embassy meetings, warehouses locked by police, border villages seeing unfamiliar uniforms, and newspapers using identical phrases.

Option tone should vary by route and state:

- calm government: cautious administrative response
- militarist government: suspicion, raids, border readiness, and threats
- democratic government: inquiry, parliamentary pressure, and public proof concerns
- communist government: counter-subversion and workers' security language
- fascist government: purges, reprisal threats, and public spectacle
- neutral or monarchist government: cabinet secrecy, court envoys, and pressure through old diplomatic channels

The final implementation should write actual localisation from this direction. This spec intentionally avoids pasteable event titles, option text, and descriptions.
