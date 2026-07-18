# Event 19 Derivative Country Route Map

This is the live implementation map for
`common/national_focus/019_infantry_spawn_derivative_focus.txt`. The tree has
45 focus nodes: 30 shared nodes and five family nodes for each of zombie,
ghost, and golem derivatives. A single derivative sees the 30 shared nodes plus
its five family nodes, for a 35-focus adapted route. Coordinates,
prerequisites, mutual exclusions, AI weights, icons, and completion effects are
implemented in that source file.

```text
                               SURVIVE THE SEPARATION
                                         |
                  +----------------------+----------------------+
                  |                      |                      |
          Secure Headquarters     Gather Formations      First Sustainment
                  |                      |                      |
                  +----------------------+----------------------+
                                         |
                               CHOOSE THE HIERARCHY
                +------------------------+------------------------+
                |                        |                        |
       CLAIMANT SOVEREIGNTY       COLLECTIVE HOST          SPECIES COMMAND
                |                        |                        |
      Personal Guard and Staff   District Councils        Family Logic Route
                |                        |                        |
      Command Estates            Shared Supply Rules      Pure Family Method
                |                        |                        |
                +-----------+------------+------------+-----------+
                            |                         |
                     SUSTAIN THE HOST          FORMATION METHOD
              +-------------+-------------+    +--------+---------+
              |             |             |    |        |         |
           Depots          Rail       Family Sites  Concentrated Scattered Auxiliaries
              |             |             |    Host      Bands       Route
              +-------------+-------------+    +--------+---------+
                            |                         |
                   SURVIVE THE FORMER PARENT WAR
                            |
            +---------------+----------------+
            |                                |
     Break Reconquest                  Seize Old Districts
            |                                |
            +---------------+----------------+
                            |
                    REGIONAL HOST AMBITION
              +-------------+-------------+
              |                           |
       Bounded Expansion          Conquered Integration
              |                           |
              +-------------+-------------+
                            |
                 FAMILY TRANSFORMATION LANE
         +------------------+------------------+
         |                  |                  |
      Zombie Module      Ghost Module       Golem Module
         |                  |                  |
  Command or Growth   Anchor or Procession  Pattern or Quarry
         +------------------+------------------+
                            |
                    REGIONAL PREDATOR CAPSTONE
```

## Opening survival groups

### Secure Headquarters

- protect the capital or claimant headquarters
- establish initial command
- avoid immediate collapse

### Gather Formations

- find and organize scattered event lots
- decide which ordinary auxiliaries remain
- create the first reinforcement decision

### First Sustainment

- zombie population and containment
- ghost manifestation anchor
- golem material and repair capacity

## Hierarchy mutual exclusions

The three hierarchy routes are mutually exclusive after a clear commitment point.

Support lanes remain compatible with every hierarchy route.

### Claimant Sovereignty

Visible payoff:

- claimant becomes permanent leader
- personal guard and district governors
- strongest concentrated command

Tradeoff:

- succession and leader-dependence risk

### Collective Host

Visible payoff:

- council or network leader identity
- district representation and resilient recruitment

Tradeoff:

- slower concentration and cohesion management

Live policy actions:

- Rotate the District Commands for stability, garrisoning, and restraint
- Centralize the Common Muster for war support and concentrated operations

### Species Command

Visible payoff:

- strongest family-specific mechanics
- final species identity and flag

Tradeoff:

- weakest normal diplomacy and administration

Live policy actions:

- Ratify the District Compacts for stability and bounded coexistence
- Proclaim the Family's Primacy for war support and family-led predation

## Sustainment lane interactions

- Claimant route turns depots and sustainment sites into command estates.
- Collective route shares local capacity and reduces single-point failure.
- Species route creates the most specialized family economy.

## Military method interactions

### Concentrated Host

- fewer stronger formations
- high command and supply concentration

### Scattered Bands

- more territorial coverage
- lower individual strength

### Captured Auxiliaries

- ordinary regional support units
- improved administration or combined arms
- loyalty and identity risk

Family availability can narrow these choices.

## Former-parent war gate

The expansion lane should not fully open until the derivative has either:

- secured survival against the former parent
- forced a negotiated ceasefire
- reduced the former parent to a non-threatening state
- outlived a defined opening crisis period

This prevents the AI from abandoning the revolt war for unrelated expansion.
Resolving that gate replaces the route-specific former-parent idea with *The
Outward Muster*, preserving the fourth live idea track while the host builds
the districts, victories, and sustainment needed for the capstone. *Regional
Predator* then replaces the bridge instead of stacking with it.

## Family transformation modules

### Zombie

- fragmented command mitigation
- controlled base-zombie recruitment versus uncontrolled proliferation
- claimant discipline, host coordination, or instinct hierarchy
- route lock: Species Realm numbers the devouring bands, Collective Host teaches the base dead to muster, and Claimant Sovereignty keeps the hunger in column

### Ghost

- stable anchors versus wandering procession
- controlled slow haunting versus predatory decline
- claimant binding, chorus organization, or autonomous manifestation
- route lock: Species Realm calls a second procession, Collective Host binds the procession to place, and Claimant Sovereignty thins the hunger for life

### Golem

- centralized master pattern versus distributed binding
- a few heavy constructs versus broader weaker hosts
- human technicians versus species-pure workshops
- route lock: Species Realm reconstructs the binding marks, Collective Host turns workshops into foundries, and Claimant Sovereignty shares the living pattern

## Capstone meaning

The Regional Predator capstone marks a derivative country that has become a sustainable regional threat. It can unlock stronger claims, reinforcement, a final identity, and an achievement route. It does not unlock a world-end mechanic or parent-event endgame.

The live availability gate requires hierarchy consolidation, completed family
transformation, sustainable reinforcement, resolved former-state pressure, at
least one integrated family district or, for a claimant breakaway using the
adapted shared route, one established sustainment district, the centralized
controlled-state threshold, and the centralized recorded-war-victory threshold. Local submission demands
use a warning mission and a bounded annexation war goal; they do not bypass
those route gates or resolve the former parent automatically.
