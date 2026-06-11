# 007 Fury shared focus tree specification

## Tree role

Fury uses a shared focus tree loaded onto the selected AI Fury country. The tree is a behavioral tree for a dynamic actor, not a national history tree. It must feel useful for Luxembourg, Uruguay, or any other eligible small AI country without relying on their exact history.

Working tree id: `fury_focus_tree`.

The tree should be compact enough to work for a repeatable minor event, but deep enough that a Fury actor that survives for years has meaningful branches.

## Tree loading rules

Preferred rule:

- load the shared Fury tree when the selected country has a generic or light focus tree.

Fallback rule:

- if the selected country has a bespoke tree, the Fury tree can still load because Fury is a takeover behavior, but the event doc must mark this as intentional.

Safety rule:

- never load the Fury tree for a player country.
- if a player later takes control of a Fury country through tag switching, the tree can remain, but ordinary random play must not grant it to the player.

## Tree architecture map

The tree should use a trunk with several branches.

```text
Opening trunk
  The Country Starts Running
  The War Office Without A Door
  Seize The Depots
  Draw The Next Border
  First War Office Orders

Branches from the trunk
  Internal Fury branch
    War Directorate path
    Civil Mobilization path
    Compliance Administration path

  Army of the March branch
    Fury Columns
    Depot Cadres
    Storm Columns
    Logistics Under Movement

  Expansion branch
    One Border At A Time
    Weak Neighbor Doctrine
    Capital First Plans
    Settlement Office
    No Neighbor Left

  Occupation and Integration branch
    Census of the Taken States
    Compliance Offices
    Rail and Registry
    Core by Administration
    Core by March

  Fury Cooperation branch
    unlocked by Evolution II or scenario pact type
    Shared War Tables
    Partition Before Victory
    Fury Pact Command
    The Other Fire Answers

  Fury Rivalry branch
    unlocked by Evolution II hostile type
    Deny The Other March
    No Second Fury
    Claim The Same Map
    Absorb The Rival Fire

  Evolution I branch
    Harden the Columns
    Depot Officers Without Leave
    Forced March Tables

  Evolution III branch
    Every Border At Once
    Three War Offices
    Storms On All Fronts
    No Target Is First

  World-end branch
    The Last Neighbor Has Fallen
    Carry The Orders Overseas
    Continental Ignitions
    The World In Fury
```

The implementation can adjust exact focus count and coordinates, but it should preserve this branch logic.

## Opening trunk

The opening trunk establishes the Fury identity and the first war.

| Focus direction | Role | Reward style |
| --- | --- | --- |
| The Country Starts Running | route opener | adds or confirms `National Fury`, sets initial momentum |
| The War Office Without A Door | command structure | unlocks decision category and first target preparation |
| Seize The Depots | military logistics | adds equipment, support equipment, and a depot decision |
| Draw The Next Border | expansion intent | increases target scoring, unlocks war declaration helper |
| First War Office Orders | first-war commitment | starts or improves first war logic, adds AI attack weight |

The trunk should avoid generic stability and political power rewards. It should grant concrete systems, units, stockpiles, target handling, and decisions.

## Internal Fury branch

This branch defines what runs the Fury country.

### War Directorate path

Narrative role: an impersonal command body takes over state decisions.

Mechanical role:

- improves target speed.
- increases army command power and attack planning.
- reduces diplomacy.
- increases overextension risk.
- can replace current leader with a fictional institutional leader named `The War Directorate`.

Asset note:

- if leader replacement is implemented, use a generated institutional council portrait. Do not use a random gendered portrait.

### Civil Mobilization path

Narrative role: the state turns public life into mobilization.

Mechanical role:

- raises manpower.
- improves normal recruitment and capped reserve-spawned unit quality.
- consumes stability or war support.
- unlocks missions that require holding capital, depots, or rail hubs.
- supports coring through population registration rather than harsh occupation.

Tradeoff:

- stronger recruitment, weaker long-term stability if wars stall.

### Compliance Administration path

Narrative role: conquest becomes an administrative machine.

Mechanical role:

- improves compliance growth.
- unlocks coring decisions.
- reduces resistance damage.
- slows capped reserve draw or quality slightly because administrators are diverted to occupation work.
- improves conquered factory use.

Tradeoff:

- slower early pace, stronger long-term consolidation.

## Army of the March branch

This branch improves the finite reinforcement reserve system without making it a free infinite reward. Focus rewards may improve template quality, initial stockpiles, reserve draw efficiency, or add capped reserve refills, but they must not create an uncapped weekly division loop.

### Focus groups

| Group | Purpose | Unlocks |
| --- | --- | --- |
| Fury Columns | baseline infantry growth | better template and capped reserve draw quality |
| Depot Cadres | captured depot use | capped garrison reserve refills and equipment capture |
| Storm Columns | evolved assault force | stronger capped reserve-spawned units after Evolution I or III |
| Logistics Under Movement | supply survival | supply grace, trains, truck costs, rail repair decisions |
| Officer Tables | command layer | commanders, army XP, planning speed, AI aggression |

### Reward rules

Use varied rewards:

- templates.
- capped reserve refills or one-time units.
- army XP.
- equipment stockpiles.
- support equipment.
- trucks or trains when logistics path is chosen.
- commander or officer corps spirit when appropriate.
- temporary attack modifiers tied to current wars.
- decisions that convert occupied depots into capped reserve refills or one-time units.

Avoid repeating `add two infantry divisions` in many focuses. Each unit focus should name what institution creates the unit or reserve refill, and every refill must be capped by script constants. No focus may create an infinite free-unit source.

## Expansion branch

This is the core branch. It should make Fury better at choosing, attacking, defeating, and absorbing neighbors.

### Sequential path

Baseline path focuses on one target at a time.

Focus directions:

- `One Border At A Time`.
- `Weak Neighbor Doctrine`.
- `Capital First Plans`.
- `Cut The Rail Before The War`.
- `Settlement Office`.
- `The Next Neighbor`.

Effects:

- improves target scoring.
- unlocks target-preparation decisions.
- adds temporary war bonuses against weaker targets.
- speeds postwar settlement.
- increases momentum from first conquest.
- allows faster next-target selection after victory.

### No-neighbor path

Unlocked when a Fury actor has no valid AI land neighbor in its continent.

Focus directions:

- `The Last Neighbor Has Fallen`.
- `Maps Beyond The Coast`.
- `Officers Without A Frontier`.
- `The Continent Is Too Small`.

Effects:

- enables reach buildup.
- unlocks overseas or other-continent seed decisions only if world-end conditions are near.
- raises the chance of the world-end branch if global chaos threshold is met.
- otherwise creates a contained Fury state with reduced reserve-spawned unit quality and internal overextension problems.

The no-neighbor path should be a threshold, not automatic world-end. It becomes terminal only under world-end conditions.

## Occupation and integration branch

This branch controls compliance and coring.

### Focus groups

| Focus direction | Purpose |
| --- | --- |
| Census of the Taken States | unlocks first integration decision family |
| New Registry Offices | compliance growth and local support |
| Rail and Registry | ties coring to rail, supply, and state control |
| Garrison the Names | creates garrison cadres and resistance reduction |
| Core by Administration | slower, cheaper, compliance-heavy coring |
| Core by March | faster, harsher, more overextension and resistance |

### Coring design

Fury should not get instant cores on every conquest. It can core conquered states through decisions when compliance, control, and administrative work are in place.

Coring costs should use:

- infantry equipment.
- support equipment.
- manpower.
- command power.
- stability or war support risk.
- local compliance.
- time.
- control of rail or capital state in the target area.

Political power can be part of the cost, but not the only cost.

## Fury Cooperation branch

Unlocked by Evolution II or the triggerable pact type.

### Path role

The branch lets multiple Fury actors cooperate.

Focus directions:

- `The Other Fire Answers`.
- `Shared War Tables`.
- `Partition Before Victory`.
- `Joint Cadre Transfers`.
- `One Pact, Many Capitals`.
- `Fury Pact Command`.
- `No Border Between War Offices`.

Mechanics:

- creates or joins Fury faction.
- adds Fury Pact Cohesion.
- lets stronger Fury send one-time aid to weaker Fury.
- coordinates target regions.
- avoids immediate Fury-on-Fury wars.
- opens shared reserve decisions.
- can help trigger world-end branch if main Fury actor has no neighbors.

Tradeoff:

- pact cohesion can fail.
- target disputes can reduce momentum.
- faction visibility raises anti-Fury response.

## Fury Rivalry branch

Unlocked by Evolution II hostile type or hostile triggerable scenario type.

### Path role

The branch treats other Fury actors as threats.

Focus directions:

- `No Second Fury`.
- `Claim The Same Map`.
- `Officers Rewrite Each Other`.
- `Absorb The Rival Fire`.
- `Last Fury Standing`.

Mechanics:

- allows Fury-on-Fury targeting after ordinary valid neighbors are exhausted.
- grants momentum from defeating another Fury.
- increases overextension and instability.
- disables pact cooperation.
- can unlock a harsher world-end route if one Fury absorbs the others.

Tradeoff:

- faster snowball for the winner.
- higher chance Fury actors destroy each other before world-end.

## Evolution I branch

Unlocks when Hardened Fury is active.

Focus directions:

- `Harden the Columns`.
- `Depot Officers Without Leave`.
- `Forced March Tables`.
- `Occupation as Recruitment`.
- `A Second Border Already Drawn`.

Mechanical effects:

- upgrades templates.
- increases reserve pool size or weekly draw quality slightly, within a capped maximum.
- improves occupation-to-recruitment conversion.
- unlocks higher target confidence.
- raises overextension if too many wars continue.

## Evolution III branch

Unlocks when All Borders at Once is active.

Focus directions:

- `Every Border At Once`.
- `Three War Offices`.
- `Storms On All Fronts`.
- `No Target Is First`.
- `All Roads Are Front Roads`.

Mechanical effects:

- enables simultaneous declarations on all valid neighbors.
- increases reserve-spawned unit quality while the finite pool lasts.
- adds temporary multi-front supply support.
- raises overextension sharply.
- unlocks strongest anti-Fury response for neighbors.

## World-end branch

Unlocked by no-neighbor branch, major-Fury status, high chaos, and world-end eligibility.

Focus directions:

- `The Last Neighbor Has Fallen`.
- `Carry The Orders Overseas`.
- `Continental Ignitions`.
- `Main Fury Pact`.
- `The World In Fury`.
- `No Neutral Map`.

Mechanical effects:

- sets terminal world-end branch through event effect.
- seeds Fury actors in other continents.
- creates or strengthens main Fury faction.
- unlocks terminal targeting rules after warning.
- activates world-threat source.

The world-end branch should not be reachable from a short first war. It requires real Fury success.

## Focus filters

Suggested focus filter taxonomy:

| Filter | Focus families |
| --- | --- |
| Fury Command | opening trunk, internal branch, War Directorate |
| Fury Army | Army of the March, templates, finite reserve support |
| Fury Expansion | target selection, war declarations, no-neighbor path |
| Fury Occupation | compliance, integration, coring, garrisons |
| Fury Pact | cooperation branch |
| Fury Rivalry | hostile branch |
| Fury Evolution | Evolution I and III content |
| Fury World-End | terminal branch |

## Idea lifecycle

| Idea | Start or unlock | Starting role | Mitigation or upgrade | Failure path | Final forms |
| --- | --- | --- | --- | --- | --- |
| National Fury | start | makes tiny country dangerous | Hardened Fury, Continental Fury | collapses after defeat | removed or upgraded |
| Improvised Command | start if weak candidate | better early units and small reserve but poor planning | War Directorate or Officer Tables | command failure events | removed or converted |
| Fury Overextension | gained after conquest | shows strain | Compliance Administration, Rail and Registry | internal stall or collapse | controlled occupation or collapse |
| Compliance Drive | occupation branch | absorbs captured states | Core by Administration | resistance if harsh route | regional cores |
| Fury Pact Command | cooperation branch | shared Fury coordination | Pact Command focuses | pact dispute | world-end pact command |
| Rival Fury Doctrine | hostile branch | anti-Fury competition | Last Fury Standing | self-destruction | absorbed rivalry power |
| World Fury | world-end | terminal identity | none during terminal state | terminal defeat aftermath | removed after defeat |

## AI focus behavior

Baseline Fury AI should prioritize:

1. opening trunk.
2. first war support.
3. Army of the March if it lacks divisions and still has reserve potential or capped refill focuses available.
4. Expansion branch if it is winning.
5. Occupation branch if overextension is high.
6. Cooperation branch if another Fury exists and type is pact.
7. Rivalry branch if type is hostile.
8. no-neighbor branch if no valid targets exist.
9. world-end branch only when eligible.

AI should avoid:

- world-end branch before eligibility.
- all-neighbor focuses before Evolution III.
- pact focuses in hostile type.
- rivalry focuses in pact type unless pact cohesion collapsed.
- coring focuses when it controls no occupied territory.
- unit-spam or reserve-refill focuses when manpower, equipment, and capped reserve allowance are exhausted.

## Localisation tone

Focus text should be bureaucratic, cold, and direct. It should not sound like ordinary nationalist expansion.

Good tone:

- offices.
- registers.
- depots.
- maps.
- border counts.
- marching orders.
- census work.
- corridors.
- staff tables.
- administrative seizure.

Avoid generic lines about destiny, glory, ancient borders, or ideology unless a specific selected country receives custom future integration. Fury is a dynamic behavior, so the shared tree should stay broadly applicable.
