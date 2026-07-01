# Event 011 Secret Alliance Spec, Part 2 Evolutions, Openings, Reveal, and War

## Baseline progression versus evolutions

Baseline progression is the ordinary hidden pact lifecycle. Evolutions are the campaign-wide escalation tracks that change how the pact behaves. Baseline operations should not be logged as evolutions.

The pact can progress internally through quiet founding, hidden meetings, invitation attempts, covert actions, active sabotage, public exposure, and war preparation. Evolutions change the available ceiling, member rules, major participation, decision visibility, and pre-fire opening strength.

## Evolution entry model

Each evolution has two entry paths when relevant.

Active-event evolution means the pact already exists and receives new behavior. The implementation should update current pact members, current values, decision visibility, AI behavior, and incident pools without requiring Event 011 to fire again.

Pre-fire evolved opening means Event 011 has not fired yet. If the chaos state already permits a stronger opening, the first event firing starts at the correct later package instead of always beginning with a calm baseline.

## Baseline opening package

Working label: quiet compact

Opening conditions:

- ordinary Event 011 firing in calm or early chaos state
- at least three valid founders
- target is not in an invalid terminal state

Opening content:

- selects three minor founders
- assigns Convener, Financier, and Provocateur roles
- initializes secrecy, cohesion, readiness, suspicion, evidence, and counter-readiness
- starts the hidden incident pool
- starts invitation checks with low tempo
- records the event in the event log with vague public detail

Baseline risk:

- very low direct economic damage
- small relation and trade friction
- no direct player retaliation category yet
- no formal faction
- no public member list

## Evolution I

Working label: coordinated minor expansion

### Active-event change

Evolution I represents the pact learning that secret coordination works. More minor countries begin joining, and operations become easier to notice. The pact still avoids direct war and still hides its formal identity.

Unlock direction:

- Gathering Storm tier or equivalent chaos threshold
- pact has existed long enough for at least one hidden meeting cycle
- at least one successful operation or one successful invitation attempt increases chance
- target expansion, world tension, or recent target wars increase chance

Immediate active changes:

- raises the member cap for minor members
- improves invitation chance for factionless minors
- unlocks medium-noise incidents such as trade refusals, press coordination, diplomatic cooling, and small covert aid to target rivals
- allows one member to become a suspected actor without full proof
- raises the chance that foreign ministries and newspapers use similar language about the target
- adds a low chance of a pact member quietly guaranteeing another member or improving relations with other members

Player-facing direction:

The player should notice more countries acting strangely, but the text should not name the pact. It should point to repeated habits, synchronized public language, couriers, travel patterns, and unexplained local hostility.

### Pre-fire opening

If Event 011 first fires after Evolution I is available, it should start with three founders and one or two extra invited minors if valid candidates exist. The opening report should be more noticeable than baseline, but it should still avoid naming the pact.

## Evolution II

Working label: patroned conspiracy

### Active-event change

Evolution II moves the event from atmospheric irritation into a playable investigation and counteraction system. One major country can join if a valid major exists. If no valid major exists, a strong regional minor can become the visible patron role instead.

Unlock direction:

- Rising Chaos tier or equivalent chaos threshold
- pact readiness or cohesion has crossed a middle threshold
- at least four live members or one especially strong founder
- target is distracted by war, low stability, low war support, high condemnation, or diplomatic isolation
- major candidate has a reason to fear or exploit the target

Major participation rules:

- the major must not be at war with the target
- the major should not be in the target faction
- prefer majors outside factions or faction leaders who can act without dragging their own faction before reveal
- a major in a faction can become a hidden patron only if implementation can prevent accidental faction-wide war before reveal
- if no safe major exists, skip the major and strengthen the Convener instead

Immediate active changes:

- unlocks the target decision category
- exposes visible values for suspicion, evidence, counter-readiness, and pact readiness
- starts suspect country cards or suspect decision targets
- enables active sabotage incidents
- enables assassination attempt events as temporary disruption, not random permanent leader deletion unless a later implementation specifically supports it
- enables border provocations when a pact member neighbors the target
- enables covert arms shipments between members
- gives the major patron a unique pressure package if it joins
- allows the player to negotiate, investigate, expose, reinforce, or retaliate

### Pre-fire opening

If Event 011 first fires at Evolution II, the pact can be founded by a valid major patron. In this opening:

- the patron is selected first
- two or three minors are selected as initial client members
- the pact starts with higher cohesion and readiness
- the player receives a stronger suspicious report and the decision category appears soon after the opening
- the pact should still be secret at first
- no formal faction appears until reveal conditions are met

### Evolution II incident pool

| Incident family | What happens | Main value impact | Counterplay |
| --- | --- | --- | --- |
| Industrial sabotage | factories or infrastructure receive limited damage | raises suspicion and readiness | industry protection decisions reduce damage |
| Railway confusion | target rail or supply state suffers temporary disruption | raises suspicion and delays player response | rail guard mission and train cost reduce risk |
| Agent disappearances | counter-intelligence staff or foreign liaison paths are compromised | raises evidence if investigated | embassy sweep can convert this into proof |
| Provoked border clash | neighbor member creates border incident | raises readiness and war chance | border watch mission can flip it into evidence |
| Foreign press chorus | multiple states use the same anti-target narrative | raises suspicion and diplomatic isolation | public counterbriefing lowers member confidence |
| Covert exile funding | hostile exiles or parties receive support | raises internal pressure | counter-network work can expose financier |

## Evolution III

Working label: exposed pact crisis

Evolution III is the public crisis stage. The pact can be seen directly through event UI and map presentation. It may form a public diplomatic alignment before the war trigger, but the formal war faction still becomes fully active when war begins or when the pact issues its final ultimatum.

Unlock direction:

- Chaos Tier or equivalent late chaos threshold
- pact readiness is high
- evidence is high enough that the pact cannot stay hidden
- target has taken noisy retaliation decisions
- a member war scare was avoided but not settled
- major patron has joined or pact member count is high

Immediate active changes:

- the pact name becomes visible as Anti-[target country] Pact through dynamic localisation
- suspected and confirmed members appear in the decision category or scripted GUI
- player receives the direct war option
- pact receives final war-preparation decisions and missions
- another major can join if the player has not weakened the pact and a valid major candidate exists
- member cap rises again
- sabotage becomes high intensity but less deniable
- pact war countdown can begin if readiness is high

### Pre-fire opening

If Event 011 first fires when Evolution III is already available, it must not begin at Evolution III instantly. It should start with the Evolution II opening package, then escalate to Evolution III after a short but real delay. This preserves the feeling that the player uncovers the conspiracy rather than receiving the whole crisis in one popup.

The delay should be dynamic:

- shorter when chaos is high, target is weak, or a major patron exists
- longer when target stability is high, target has strong allies, or too few valid members exist
- delayed further if the player quickly gains evidence or splits a member away

## Reveal rules

### War reveal

The pact reveals immediately when any live pact member and the target enter the same war against each other.

This includes:

- a pact member declaring on the target
- the target declaring on a pact member
- a pact member joining a war against the target
- a target ally call that creates direct target-member war
- a scripted border escalation that becomes real war

War reveal effects:

- set the pact revealed state
- set the formal faction name to Anti-[target country] Pact
- create or rename the faction using dynamic target localisation
- invite all live pact members into the faction if they are not blocked by engine constraints
- make all live members join the war against the target
- fire the reveal super-event
- convert hidden member ideas into public war ideas
- replace hidden incident decisions with wartime decisions
- remove or lock negotiation actions that no longer fit
- preserve a few split-pact actions only if they represent wartime diplomacy

### Investigation reveal

The player can reveal the pact before war if evidence crosses the exposure threshold and the player takes a public exposure decision.

Investigation reveal effects:

- confirms the members known through evidence
- reveals some or all remaining members based on evidence quality
- reduces pact secrecy sharply
- creates diplomatic backlash against the pact
- can force low-confidence members to leave
- may create a public Anti-[target country] Pact alignment without immediate war
- may start an ultimatum timer if pact readiness is high
- does not fire the same super-event unless the reveal also creates a formal faction or war-level crisis

### Pact self-reveal

At Evolution III, the pact can reveal itself if readiness is high and the player has not already exposed it. This can happen through a public declaration, coordinated demands, or an ultimatum.

Self-reveal effects:

- public faction label appears
- pact readiness rises
- target gets direct war and negotiation options
- members with low confidence may hesitate if the player has built leverage
- war begins after the countdown unless the player fractures the pact, yields to limited terms if that route is implemented, or launches first

## War stage design

The pact war should feel like a prepared ambush if the player ignored the system and like a manageable coalition fight if the player acted well.

### Pact war advantages if player neglected the crisis

- member armies receive temporary coordination bonuses
- border members receive preparation bonuses
- major patron sends equipment, volunteers, or direct war support
- target receives a temporary surprise disruption idea
- target allies have lower willingness to join if diplomatic isolation is high
- pact members have higher war support and opinion of each other

### Player advantages if counterplay succeeded

- members with low confidence may leave before war
- some members may stay neutral on reveal
- target starts with counter-readiness bonuses
- border defenses, rail guards, and protected industry reduce opening penalties
- player receives temporary intelligence advantage against confirmed members
- pact cohesion starts lower
- major patron may refuse to join or join late

### Victory outcomes

The event should support several endings:

| Ending | Conditions | Result direction |
| --- | --- | --- |
| Quiet fracture | pact cohesion collapses before public reveal | event ends with minor rewards for counter-intelligence and diplomacy |
| Public exposure without war | player exposes pact and enough members leave | target gains credibility and members suffer diplomatic penalties |
| Limited crisis settlement | public pact accepts negotiated limits | pact dissolves or becomes dormant with long cooldown cleanup |
| Reveal war victory | target defeats the pact | target gains anti-conspiracy legacy, members receive aftermath penalties, pact is permanently destroyed |
| Reveal war defeat | target capitulates or loses key war goals | pact members receive rewards based on role and claims, target suffers humiliation and instability |
| Stalemate | war lasts too long without decisive result | recurring war fatigue events lower cohesion and can create negotiated peace |

Defeat of the pact does not need a defeat super-event unless implementation later finds the war became a near-global crisis. The required super-event is the reveal and formation moment.

## Member cleanup rules

A member should leave or be removed when:

- it is annexed
- it becomes a target subject
- it joins the target faction before reveal
- it enters a terminal world-threat state
- it becomes a special nonhuman country
- it is defeated in the pact war and no longer controls any relevant territory
- it leaves through negotiation, bribery, exposure, or internal collapse

If member count falls below two before reveal and no major patron remains, the pact should enter fracture cleanup. If member count falls below two after reveal, the war continues only if a formal war exists. Otherwise the alignment dissolves.
