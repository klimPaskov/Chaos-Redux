# Event 007 Fury Specification

## Catalog identity

- Event ID: `7`
- Event name: `Fury`
- Type: minor repeatable
- Cluster: Wars
- Status: source specification for rework
- Replaces: obsolete `expansionism` placeholder

## Core promise

Fury is a repeatable war spark where one small AI country suddenly becomes an expansion actor. The country is not chosen from a fixed list. Luxembourg and Uruguay are only examples of the kind of country that can be selected. The system should search the current campaign, find a valid small non-island AI minor with land neighbors, turn it into a Fury country, and let it fight outward until it runs out of valid neighboring targets or is destroyed.

The event should stay simple in play. The depth comes from target selection, AI behavior, reinforcement, postwar integration, evolutions, and focus or decision support. It should not become a giant diplomacy simulator.

## Hard design rules

1. The player must never become a Fury country.
2. The scripted Fury war target should not be a player country.
3. Fury is repeatable.
4. Fury chooses dynamic campaign candidates, not a hardcoded country list.
5. Fury belongs to the Wars cluster.
6. The first Fury war begins without warning.
7. A Fury country keeps expanding only while valid weaker AI land neighbors exist.
8. If the Fury country capitulates, its Fury state ends and all event-specific loops clean up.
9. If no valid neighbors remain, Fury enters the no-neighbor branch instead of fabricating impossible local wars.
10. The event should be threatening without giving the player a free power path.
11. Automatic weekly unit spawning is an opening surge only. It must end after the first few months of the Fury campaign, then later force growth must come from focuses, decisions, missions, captured resources, shared reserves, or special route unlocks.

## Candidate selection

The selector should build a weighted pool of countries that match all required rules.

Required candidate rules:

- is AI controlled
- is not a major
- is not a player subject when that would indirectly empower the player
- is non-island by practical campaign logic, meaning it has at least one valid land neighbor and does not depend on naval invasion to start the event
- owns few states, with one state strongly preferred
- has at least one weaker AI land neighbor
- is not already marked as Fury
- is not a special chaos country that should be excluded from ordinary political or civilian systems
- is not in a blocked world-end, scripted peace, or scripted country-package state
- is not a country whose current event package should not be overwritten by a shared runtime tree

Preferred weighting:

| Factor | Weight direction |
| --- | --- |
| One owned state | strong bonus |
| Two or three owned states | smaller bonus |
| Borders several weaker AI neighbors | bonus |
| Already at war | penalty, unless chaos is high |
| Strong faction backing | penalty |
| Capital isolated by impassable terrain | penalty |
| Surrounded by players only | disqualify |
| Already has a major custom crisis role | disqualify or heavy penalty |

The selector should not select the same country again while it already has Fury state. A repeat fire should seek another valid small AI minor.

## Target selection

A Fury target is a weaker AI land neighbor. The target must be weaker enough that the first war can plausibly move. It should not be an instant suicide pick against a faction-backed regional power.

Required target rules:

- AI controlled
- not a player
- shares a land border with the Fury country
- not a Fury country unless the world-end branch explicitly allows Fury rival wars
- not a major under ordinary Fury rules
- not protected by a scripted no-war state
- not in a blocked scripted peace or event-protected transition

Target scoring should compare:

- divisions
- deployed manpower
- military factories
- civilian factories
- controlled states
- capital distance
- terrain difficulty
- supply access
- faction and guarantee risk
- current wars and front pressure
- whether the target has recently lost territory

The first target should be the easiest valid neighbor. Later targets may be harder if Fury momentum is high, evolutions are active, or the Fury country has won several wars.

## Baseline flow

### 1. Ignition

A valid AI minor is selected. It receives the `Fury Impetus` national spirit, the shared Fury runtime focus tree or additive branch, the Fury decision category, and a small dynamic starting force. A report event can tell players that an odd military mobilisation has been noticed in a small country, but it should not expose the full chain too early.

### 2. The first strike

After a short delay, the Fury country declares war on its weakest valid AI land neighbor without warning. The target receives a short defensive reaction event and a small emergency mobilisation chance so the first war is not always a pure stomp.

### 3. Opening reinforcement pulse

Fury receives weekly new divisions only during an opening reinforcement window. This is the first surge that lets a tiny country survive the first campaign. It should last only the first few months after ignition, then stop even if the Fury country is still at war.

The pulse should be handled by a targeted Fury timer for active Fury countries, not by an unconditional global weekly scan. The timer begins when the country becomes Fury and ends when the opening window expires, the Fury country capitulates, the Fury state is cleaned up, or the country enters a no-neighbor consolidation state.

After the opening window ends, Fury must rely on ordinary country growth and event systems:

- focus-tree military branches
- recruitment and depot decisions
- integration and garrison decisions
- captured industry and manpower
- shared reserves from a Fury Pact or cooperation route
- limited route-specific emergency mobilisations
- special evolution-locked decisions or missions

The opening pulse must not restart or extend just because Fury wins another war. Victories can unlock new decisions, improve focuses, add captured equipment, or raise momentum, but they should not create an infinite free-unit loop. A focus or decision may start a separate limited mobilisation project, but that project needs its own cost, duration, cooldown, AI rules, and cleanup.

Opening pulse strength is dynamic:

| Factor | Effect |
| --- | --- |
| Higher chaos | stronger opening pulse and better templates, but still finite |
| Evolution I | slightly larger opening pulse and better quality |
| Evolution II | shared reserve decisions after the pulse, not endless free weekly units |
| Evolution III | stronger all-front opening packages, still capped by the opening window |
| Low manpower | fewer spawned units, more militia templates |
| Low equipment | weaker units or equipment debt penalty |
| Captured capital during the opening window | one short temporary boost, not a pulse reset |
| High occupation strain | weaker pulse until administration decisions are used |
| Poor supply | fewer motorized or artillery-heavy units |
| Heavy losses | emergency militia chance but weaker training |

### 4. First victory

When the Fury country defeats its first neighbor, a news event fires. This is the moment where the world stops treating the incident as a border war. The news event should name the defeated neighbor, mention the speed or surprise of the campaign, and add the first visible Fury history row.

Effects after first victory:

- Fury receives a momentum boost.
- Fury gains compliance in captured territory.
- Fury unlocks first integration decisions.
- Nearby AI neighbors become more alert.
- Major powers may consider guarantees or containment if the country is close.
- Fury can seek the next weaker AI neighbor after a delay.

### 5. Rolling campaign

After each victory, the Fury country waits a short dynamic delay, selects another valid weaker AI land neighbor, and declares again. The delay should shrink with high momentum and Evolution III, but grow when the Fury country has high occupation strain, low equipment, high resistance, or multiple active fronts.

The loop repeats until one of these conditions ends it:

- Fury capitulates.
- Fury has no valid AI land neighbor left.
- world-end branch activates.
- event cleanup removes Fury because of invalid state.

### 6. No-neighbor branch

If Fury has no valid AI land neighbors left, it does not get fake targets. It enters a contained aftermath state:

- the decision category changes to integration and consolidation
- expansion decisions disappear
- the focus tree reveals the `No Frontier Left` branch
- the country can spend resources to core captured land
- it can build continental logistics and a hardened border
- if it is now large enough and chaos is high enough, the world-end branch may become possible

### 7. Capitulation cleanup

If Fury capitulates:

- remove Fury ideas
- cancel Fury missions
- remove active Fury country flag
- clear Fury event targets and variables
- record defeat in the event log if it had reached first victory or major threshold
- stop the opening reinforcement pulse and prevent it from restarting through victory loops
- hide the runtime tree or route where safe
- leave normal occupation outcomes to the war system

## National spirits and values

### Fury values

| Value | Meaning | Moves through |
| --- | --- | --- |
| Fury momentum | confidence and tempo after victories | victories, focus progress, failed attacks, occupation strain |
| Occupation strain | burden of holding conquered land | captured states, resistance, coring decisions, losses |
| Integration capacity | ability to turn captured land into a working state | administration focuses, decisions, compliance, stability |
| Fury coordination | ability to cooperate with other Fury countries | Evolution II, shared focuses, faction decisions |

The player does not need a full scripted GUI unless implementation finds the decision header too cramped. A decision category header with scripted localisation is enough for the baseline.

### Ideas

| Idea | Use |
| --- | --- |
| Fury Impetus | baseline military drive, temporary opening pulse marker, war support, faster planning, occupation penalties |
| Veteran Fury Impetus | Evolution I upgrade, better opening-pulse quality, lower reinforcement weakness |
| Joint Fury Command | Evolution II upgrade, enables partner coordination and shared reserve decisions |
| All-Front Command | Evolution III upgrade, enables multiple simultaneous neighbor wars |
| Continental Mandate | no-neighbor or world-end preparation, replaces basic expansion bonuses with integration and foreign ignition tools |

The ideas should be upgraded or replaced. Do not stack many permanent Fury ideas at once.

## Compliance, occupation, and coring

Fury should not instantly core everything. It should get enough compliance to reduce the worst occupation drag, then use decisions and focuses to integrate captured states.

Captured-state handling:

- first victory grants a one-time compliance push in the defeated neighbor's core territory
- later victories grant smaller compliance pushes unless an administration route was taken
- resistance remains a real cost if Fury expands too fast
- coring requires state control, compliance, garrison support, equipment, manpower, and time
- the General Staff route cores more slowly and causes more resistance
- the March Administration route cores more reliably but slows war tempo

Coring decisions should be target-state decisions, with an active cap so the decision category does not become a wall of state buttons.

## Evolutions

Evolutions are not ordinary stages. They change how future Fury firings behave.

### Evolution I, Marches Learn

The world has seen enough small-state wars that the next Fury ignition is more organized.

Changes:

- initial Fury divisions are stronger
- opening-pulse units are slightly more numerous
- `Veteran Fury Impetus` replaces the basic idea
- focus tree unlocks the `Veteran Marches` branch
- early target selection can choose a slightly stronger first neighbor
- first victory news text becomes less confused and more alarmed

Containment:

- killing the Fury country before first victory reduces the chance of this evolution appearing again soon
- nearby countries that mobilize early can slow the next Fury ignition

### Evolution II, Two Sparks

Two Fury countries can appear from one event firing. They do not have to be on the same continent, though ordinary weighting should avoid putting both too close unless the continent has enough valid small countries.

Changes:

- two AI minors become Fury countries
- Fury countries can form or join the `Fury Pact`
- cooperation mechanics unlock
- shared reserves, synchronized target timing, and non-aggression between Fury countries become possible
- the focus tree unlocks `Joint Campaign Office`
- major powers become more willing to contain Fury when two exist at the same time

Containment:

- defeating one Fury country weakens partner coordination
- isolating the two Fury countries on separate continents reduces shared reserve effects

### Evolution III, All Fronts Open

Three Fury countries can appear from one firing. Fury countries are stronger and declare on all valid weaker AI neighbors at once.

Changes:

- three AI minors become Fury countries
- initial divisions are stronger and more numerous
- finite opening pulse can produce all-front formations
- declarations hit every valid weaker AI land neighbor at the same time
- the focus tree unlocks `All Fronts Open` and high-chaos military branches
- occupation strain grows faster
- world-end branch becomes more likely if any Fury country becomes large or runs out of neighbors

Containment:

- all-front wars can overextend Fury
- high occupation strain can slow future declarations
- AI targets with defensive focus and supply control can stop the snowball

## Super-events and news

### First victory news event

Trigger:

- a Fury country defeats its first declared neighbor

Role:

- public reveal that this is more than a local border conflict

Image direction:

- black-and-white news photo style, small capital street or border crossing, troops entering an administrative building, no readable generated text

### Fury becomes a major super-event

Trigger:

- a Fury country crosses the major-country threshold, becomes major by vanilla logic, or reaches a documented custom threshold of states, factories, and divisions
- fires once per campaign for the first Fury major

Role:

- a minor actor has become a campaign-shaping power

Working title directions:

- `No Longer Minor`
- `The Small State Ascends`
- `A New Major Marches`

The final title, quote, remark, and music must be researched through the super-event workflow.

### World-end super-event

Trigger:

- world-end conditions are met for Fury and no other world-end is active

Working title direction:

- `War Without Borders`

Role:

- terminal campaign state where Fury no longer belongs to one continent

## World-end scenario, War Without Borders

This branch should exist, but it must be gated tightly because Fury is a minor repeatable event by default.

Conditions:

- chaos value is above the required world-end threshold
- at least one Fury country has conquered its local expansion area or has no valid AI land neighbors left
- that Fury country is already large enough to matter
- no global world-end branch is active
- Evolution II or Evolution III has occurred, or Fury has reached a major threshold
- the Fury country has not capitulated

Effects:

- set the Fury world-end flag
- the main Fury country becomes the Fury world-end leader
- Fury begins appearing in other continents through valid AI minor candidates
- new Fury countries join the main Fury faction if valid
- the new Fury countries are still selected dynamically
- players are still not selected as scripted Fury countries or direct scripted targets
- the world-threat framework should recognize Fury as a threat source if the implementation already supports that extension

The world-end branch should not automatically conquer the world. It changes the campaign into an expanding multi-continent war system.

## Repeatability behavior

Because Fury is minor repeatable, each firing should be self-contained but remember the larger evolution state.

Normal repeat fire:

- select one AI minor
- start one Fury campaign

Evolution II repeat fire:

- select two AI minors
- use distance and continent weighting to avoid impossible clutter

Evolution III repeat fire:

- select three AI minors
- allow all-front behavior for each

Repeat protection:

- do not select active Fury countries
- do not select countries that were recently Fury and were destroyed unless a high-chaos resurrection rule is deliberately added later
- do not let repeat fires, victories, or prolonged wars farm free units for the same tag
- do not let a Fury subject or puppet path give the player indirect free cores or units
- do not let the opening reinforcement window refresh unless the country has lost Fury state, passed all cooldown or recent-Fury checks, and is selected again through a valid repeat firing

## Player-facing response

The player cannot become Fury through the event. Player agency comes from reaction:

- guarantee threatened neighbors before Fury reaches them
- intervene manually in ordinary war systems
- join coalitions or factions if diplomacy allows
- support containment through future shared world-threat systems when implemented

## Achievements

Achievements should reward response and containment, not playing as Fury.

Priority achievements:

| ID | Title | Core requirement |
| --- | --- | --- |
| achievement_fury_no_second_neighbor | No Second Neighbor | Stop a Fury country after it defeats the first neighbor but before it declares on a second |
| achievement_fury_before_the_headlines | Before the Headlines | Defeat or force capitulation of a Fury country before its first victory news event |
| achievement_fury_sparkbreaker | Sparkbreaker | Defeat a Fury country that has reached the major super-event threshold |
| achievement_fury_three_extinguished | Three Extinguished | During Evolution III, all three Fury countries are defeated before any becomes major |
| achievement_fury_no_borderless_war | No Borderless War | Prevent the Fury world-end branch after a Fury country reaches no-neighbor state |
| achievement_fury_pact_shattered | Pact Shattered | Destroy the Fury Pact after Evolution II before it completes a shared campaign objective |
| achievement_fury_let_them_march | Let Them March | Observe a Fury country conquer its continent without being at war with it, then defeat it later |
| achievement_fury_containment_doctrine | Containment Doctrine | Keep every active Fury country below major threshold for a long high-chaos period |

## Documentation and catalog needs

Update these player-facing records after implementation:

- event doc under `docs/events/007_fury.md`
- event log name and detail text
- evolution detail entries for all three evolutions
- super-event research notes and docs
- asset manifest
- event catalog workbook row for Event 7

The workbook currently has old placeholder content for row 7. The implemented event should use the new Wars-cluster Fury identity from this spec, not the old placeholder.
