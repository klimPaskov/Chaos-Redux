# Cave-Country Focus Architecture

This is a path-level design guide. All labels are working labels, not final localisation. The implementation agent owns exact focus count, coordinates, and connector layout while preserving the route logic.

## High-level lane map

```text
                                      [The First Breach]
                                              |
                              [Secure the Origin Chamber]
                                              |
                              [Organize the First War-Broods]
                                              |
                                  [Read the Surface Veins]
                                              |
                 +----------------------------+----------------------------+
                 |                            |                            |
          BROOD HIERARCHY              RESOURCE ECONOMY             SURFACE WAR
                 |                            |                            |
      +----------+----------+        [Survey Surface Seams]     [Learn the Open Sky]
      |          |          |                 |                            |
 [One Maw] [Many Chambers] [Hoard]   [Activate Resource Anchors]   +-------+-------+
      |          |          |                 |                    |       |       |
      |          |          |         [Build Brood Queues]      [Stone] [Burrow] [Scree]
      |          |          |                 |                    |       |       |
      |          |          |         [Consume Industry]          |       |       |
      |          |          |                 |                    |       |       |
      +----------+----------+---------[Link the Chambers]----------+-------+-------+
                                              |
                                       ADAPTATION LANE
                                              |
                 +----------------------------+----------------------------+
                 |                            |                            |
        [Study Broken Weapons]       [Grow or Lighten Plates]     [Surface Senses]
                 |                            |                            |
                 +----------------------------+----------------------------+
                                              |
                                  [Choose the Final Adaptation]
                                              |
                                  CONTINENTAL EXPANSION LANE
                                              |
                                  [Mark the Richest Route]
                                              |
                                     [Break the First Ring]
                                              |
                                [Consume an Industrial Belt]
                                              |
                                      [Seal the Coast]
                                              |
                               [Break Continental Coalitions]
                                              |
                                  [Consume the Last Resistance]
                                              |
                                      [Continent Consumed]
                                              |
                                  WORLD-END TRANSFORMATION
                                              |
                             [Deepen the Continental Heart]
                                              |
                              [Listen Beneath Distant Shores]
                                              |
                               [Choose the First Rupture]
                                              |
                                  [The World Opens Below]
```

The hierarchy and surface-war choices are real route locks. Resource economy, adaptation, and continental expansion remain shared. Route-specific subbranches should feed into shared late play rather than ending in isolated stat nodes.

## Opening trunk

| Focus group | Position in tree | Main purpose | Mechanical unlock | Route connection |
| --- | --- | --- | --- | --- |
| The First Breach | Root | Apply origin package and identify Event 018 history | Resource-capacity interface, cave decisions, threat registration | All lanes |
| Secure the Origin Chamber | Early trunk | Stabilize capital supply and exits | Origin state modifier, supply, defensive project | Hierarchy and resource lanes |
| Organize the First War-Broods | Early trunk | Set commanders and base template | Base commander set, queue explanation, anchor guard concept | Doctrine lane |
| Read the Surface Veins | Trunk splitter | Identify rich neighboring targets | Resource target scoring, marked-state decision | Resource and expansion lanes |

The opening trunk should be short enough that the cave country can act immediately, but deep enough to teach its special rules before route locks.

## Hierarchy lane

### Split point

The hierarchy split should appear after the first origin and capacity focuses. The player chooses one of three incompatible command systems.

### One Maw route

```text
[One Maw]
    |
[Central Resonance]
    |
[Count Every Vein]----[Directed War-Broods]
    |                         |
[Origin Above All]------------+
    |
[The Singular Hunger]
```

| Group | Mechanical role | Decision or idea effect | Tradeoff |
| --- | --- | --- | --- |
| One Maw | Route lock and leader centralization | Replaces command idea, updates leader trait or portrait state | Higher origin dependence |
| Central Resonance | Planning and coordination | Concentration decision, organization near command range | Remote anchors weaker |
| Count Every Vein | Capacity efficiency | Better queue reliability and fractional progress handling | Strong central accounting cost |
| Directed War-Broods | Front control | Target priority and reserve control | Less regional autonomy |
| Origin Above All | Capital defense | Strong origin recovery, protected allocation repair | Origin loss penalties worsen |
| The Singular Hunger | Route capstone | Decisive concentrated offensive and central brood identity | No secondary capital route |

### Many Chambers route

```text
[Many Chambers]
       |
[Local Brood Memory]----[Chamber Autonomy]
       |                         |
[Distributed Command]-----------+
       |
[A Second Deep Capital]
       |
[The Host Without a Head]
```

| Group | Mechanical role | Decision or idea effect | Tradeoff |
| --- | --- | --- | --- |
| Many Chambers | Route lock and distributed identity | Replaces command idea | Lower global planning |
| Local Brood Memory | Anchor resilience | Partial activation retention and local recovery | Less central efficiency |
| Chamber Autonomy | Regional queues | Faster distant spawning and anchor decisions | Harder template standardization |
| Distributed Command | Multi-front control | More commanders and simultaneous offensive handling | Weaker concentrated breakthrough |
| A Second Deep Capital | Origin-loss resilience | Difficult secondary capital designation | Requires rich mature anchor |
| The Host Without a Head | Route capstone | Reduced decapitation risk and strong distributed recovery | No singular leader offensive |

### Hoard the Veins route

```text
[Hoard the Veins]
        |
[Mineral Tithe]----[Guard the Feeding Chambers]
        |                         |
[Refuse Barren Ground]------------+
        |
[Preserve Every Plate]
        |
[Vaults Beneath the Continent]
```

| Group | Mechanical role | Decision or idea effect | Tradeoff |
| --- | --- | --- | --- |
| Hoard the Veins | Route lock and rich-anchor identity | Resource-state priorities and defensive command | Slow poor-land expansion |
| Mineral Tithe | Convert resources and factories | Stronger benefits per anchor | Slower raw division growth |
| Guard the Feeding Chambers | Anchor defense | Reserve capacity for guard broods | Fewer offensive formations |
| Refuse Barren Ground | Target discipline | Bonuses toward rich states, penalties in poor regions | Route inflexibility |
| Preserve Every Plate | Unit survival | Better recovery and lower strength loss | Slower replacements |
| Vaults Beneath the Continent | Route capstone | Mature rich-anchor network and consumption progress | Weak broad-front pursuit |

## Resource economy lane

```text
[Survey Surface Seams]
          |
[Activate Resource Anchors]
          |
+---------+----------------+
|                          |
[Build Brood Queues]  [Fortify the Feeding State]
|                          |
+-----------[Consume Captured Industry]----------+
                         |
                 [Link the Chambers]
                         |
              [The Continental Network]
```

| Focus group | Main unlock | Map or mechanic effect | Route variation |
| --- | --- | --- | --- |
| Survey Surface Seams | Pre-conquest capacity preview | Highlights rich targets and improves AI scoring | Hoard route gets stronger target discipline |
| Activate Resource Anchors | Basic 30-day anchor mission | Enables captured-state capacity | Many Chambers gets distant activation support |
| Build Brood Queues | Visible automatic spawn system | Queue preferences and replacement logic | One Maw gets central priority, Many Chambers regional queues |
| Fortify the Feeding State | Anchor guard decisions | Local defense and recovery | Hoard route gains strongest state defense |
| Consume Captured Industry | Factory conversion choices | Anchor construction, adaptation, or immediate brood progress | Doctrine determines military conversion benefit |
| Link the Chambers | Local tunnel link projects | Movement and supply between nearby anchors | Burrow War gains stronger links |
| The Continental Network | Shared economic capstone | Mature anchor network and world-end preparation access | Hierarchy route changes network behavior |

The one-per-ten capacity formula and ten-per-state cap do not change. This lane improves activation, queue, defense, and logistics.

## Surface-war doctrine lane

### Shared opening

```text
[Learn the Open Sky]
        |
[Read the Enemy Line]
        |
+-------+-------+-------+
|               |       |
STONE         BURROW  SCREE
```

The shared opening provides reconnaissance and basic surface command without removing slow movement.

### Stone Phalanx route

```text
[Stone Phalanx]
      |
[Interlocking Carapaces]
      |
[Deliberate Front Advance]----[Resist the Great Guns]
      |                                |
[Crush the Fortified Line]-------------+
      |
[The Moving Mountain]
```

Key rewards:

- heavy brood template
- deliberate assault decision
- stronger defense and breakthrough
- better recovery in prepared fronts
- extreme slowness and predictable attack windows

### Burrow War route

```text
[Burrow War]
      |
[Listen Beneath the Roads]
      |
[Hidden Approach Chambers]----[Undermine the Rail Junction]
      |                                  |
[Urban Cellar Networks]------------------+
      |
[The Front Has a Floor]
```

Key rewards:

- infiltration brood template
- prepared adjacent-state burrow action
- supply disruption
- terrain and urban combat
- lower open-field armor concentration

### Scree Tide route

```text
[Scree Tide]
      |
[Split the Great Broods]
      |
[Lighter Plates]----[Follow the Retreat]
      |                      |
[Swarm the Crossings]--------+
      |
[The Hills Begin to Move]
```

Key rewards:

- lighter raiding brood template
- higher formation count from the same capacity through template structure, not capacity-ratio change
- faster movement and pursuit
- lower armor and higher vulnerability to ordinary firepower

## Adaptation lane

```text
[Study Broken Weapons]
          |
+---------+---------------------------+
|                                     |
[Grow Denser Plates]           [Open the Joints]
|                                     |
+-------------[Surface Senses]--------+
                         |
               [Harden Against the Sky]
                         |
              [Choose the Final Adaptation]
```

### Adaptation choices

The final adaptation should choose one strong package. Suggested options:

- dense armor, stronger against piercing but slower
- lighter motion, faster but less armored
- urban and mountain infiltration
- stronger anchor regeneration
- air-attack resilience

Only one final package should be fully available. This prevents the cave country from erasing every counter.

### Enemy-linked prerequisites

The tree should require actual experience where appropriate:

- hard-attack adaptation after fighting piercing enemies
- air resilience after suffering meaningful air attack
- urban adaptation after controlling or fighting in major cities
- mountain adaptation after a mountain campaign

## Continental expansion lane

```text
[Mark the Richest Route]
          |
[Break the First Ring]
          |
+---------+----------------+
|                          |
[Consume an Industrial Belt] [Take the Continental Capitals]
|                          |
+-------------[Seal the Coast]-------------+
                         |
             [Break Continental Coalitions]
                         |
               [Consume the Last Resistance]
                         |
                 [Continent Consumed]
```

| Focus group | Public objective | Gameplay unlock |
| --- | --- | --- |
| Mark the Richest Route | Select first strategic resource corridor | Marked target and AI offensive plan |
| Break the First Ring | Defeat or bypass first neighboring ring | Expanded anchor range and commander reward |
| Consume an Industrial Belt | Control a generated industrial-resource region | Strong factory conversion and local anchor project |
| Take the Continental Capitals | Capture key surviving capitals | Coalition disruption and progress |
| Seal the Coast | Secure coast and ports against containment | Coastal defense and supply resilience, no navy |
| Break Continental Coalitions | Defeat coordinated defenders | Multi-enemy strategy and shared-command disruption |
| Consume the Last Resistance | Complete final state missions | Final verification preparation |
| Continent Consumed | Map condition milestone | Opens world-end lane when chaos gate also met |

The generated region and capital objectives must be valid for the origin continent. They should not assume Europe or one historical map.

## World-end lane

```text
[Deepen the Continental Heart]
              |
[Listen Beneath Distant Shores]
              |
[Choose the First Rupture]
              |
[The World Opens Below]
```

| Focus group | Reveal rule | Effect direction |
| --- | --- | --- |
| Deepen the Continental Heart | Near full continent control | Strong origin-continent network and terminal preparation |
| Listen Beneath Distant Shores | Continent consumed, world end not active | Identifies valid high-resource states elsewhere |
| Choose the First Rupture | Chaos above 1000 and valid candidates | Influences foothold weighting without free arbitrary target |
| The World Opens Below | Full terminal prerequisites | Calls world-end effect and super-event |

The final focus cannot bypass the shared world-end checks.

## Branch interaction rules

- Hierarchy changes how anchor and queue focuses work.
- Doctrine changes template unlocks and warfare decisions.
- Resource economy supports every route and is required for sustained expansion.
- Adaptation reacts to enemies and preserves a choice of weakness mitigation.
- Continental progress requires actual state control, not focus completion alone.
- World-end preparation remains hidden until the campaign state justifies it.
- Industry and resource effects are map-based or mechanic-based, not generic factory gifts.
- No hierarchy or doctrine route should end after one or two focuses.
- Every side branch returns to a mechanic, a decision family, a template, or a late route.

## Suggested focus-duration rhythm

- emergency emergence focuses: shorter duration
- route commitments and system activations: normal duration
- major anchor, tunnel, and adaptation projects: longer duration
- continent and world-end preparation: long duration with map prerequisites

Exact days belong to implementation and should vary by purpose. The tree should not use one identical duration for every focus.

## Route coverage proof required after implementation

| Required route | Implemented branch | Status | Notes |
| --- | --- | --- | --- |
| Emergence and origin stabilization |  |  |  |
| One Maw central hierarchy |  |  |  |
| Many Chambers distributed hierarchy |  |  |  |
| Hoard the Veins resource hierarchy |  |  |  |
| Resource anchor network |  |  |  |
| Stone Phalanx doctrine |  |  |  |
| Burrow War doctrine |  |  |  |
| Scree Tide doctrine |  |  |  |
| Enemy adaptation |  |  |  |
| Continental expansion |  |  |  |
| World-end transformation |  |  |  |
