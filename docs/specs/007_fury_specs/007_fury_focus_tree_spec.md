# Event 007 Fury Focus Tree Specification

## Tree model

Fury uses a shared runtime focus tree or an additive Fury branch assigned only to AI countries that the event has actually marked as Fury. Existing countries with meaningful trees should not receive a blind replacement unless they were selected and flagged by Event 007. The implementation should choose the safest existing Chaos Redux pattern.

Working tree id:

- `fury_shared_focus_tree`

Working route flag:

- `fury_country`

## Tree purpose

The tree is not a full normal national identity. Fury is a fixed-purpose war actor. It still needs meaningful choices inside that purpose so the AI can behave differently across campaigns.

Main identity:

- a small state has built an emergency war machine around rapid border campaigns

Starting problems:

- small industry
- thin officer corps
- occupation strain after victory
- weak supply if it grows too quickly
- diplomatic isolation
- limited manpower base

## Architecture map

```text
Opening trunk
  The Border Stirs
  No Warning Orders
  Fury Impetus

Fork family
  General Staff Dictate
    Faster declarations
    stronger weekly combat units
    worse occupation strain
    harsher integration
  March Administration
    slower declarations
    stronger compliance and coring
    better supply and stability
    weaker immediate tempo

Support lanes
  Military improvisation lane
  Captured industry lane
  Border logistics lane
  Occupation administration lane

Expansion lane
  First Neighbor
  Second Border
  Capital Roads
  Next Weak Link
  Continental Claims

Evolution branches
  Evolution I: Veteran Marches
  Evolution II: Joint Campaign Office
  Evolution III: All Fronts Open

No-neighbor branch
  No Frontier Left
  Continental Guard
  Integrate the Marches

World-end branch
  War Without Borders
  Export the Spark
  The Fury Pact Commands
```

## Focus filters and search categories

Use existing focus filter tags where possible.

| Focus group | Filter direction |
| --- | --- |
| military and unit growth | army, war support |
| captured industry and logistics | industry, construction, supply |
| occupation and coring | stability, annexation, political |
| expansion and war goals | war support, annexation |
| Fury cooperation | diplomacy, faction, army |
| world-end branch | special or hidden if the repo supports it |

## Opening trunk

### The Border Stirs

Role:

- gives the selected Fury country its first clear identity
- unlocks the Fury decision category
- gives small readiness and planning support

Avoid:

- large factory dumps
- generic political power

### No Warning Orders

Role:

- prepares the first scripted declaration
- improves initial attack speed and division organization
- raises diplomatic suspicion

### Fury Impetus

Role:

- upgrades or confirms the core Fury idea
- enables the weekly reinforcement pulse
- opens the route fork

## Political and command fork

### General Staff Dictate

Narrative role:

- the army takes control of the state as a marching command office

Mechanical role:

- faster target selection after each victory
- stronger weekly unit packages
- better attack bonuses against weaker neighbors
- higher occupation strain
- worse resistance and slower coring

Compatible branches:

- military improvisation
- captured industry
- all evolution branches

Failure state:

- if occupation strain becomes too high, the country slows down and may lose compliance or garrison control

AI preference:

- high chaos
- low stability
- many weak neighbors
- successful first war

### March Administration

Narrative role:

- the Fury country builds an administration to make conquest stick

Mechanical role:

- slower declarations
- better compliance gain
- cheaper coring decisions
- lower resistance
- stronger logistics and captured factories

Compatible branches:

- occupation administration
- captured industry
- cooperation routes

Failure state:

- if it delays too long, nearby countries can prepare or join factions

AI preference:

- more captured territory
- high resistance
- low manpower
- no immediate weak neighbor

## Military improvisation lane

Focus groups:

- Border Shock Detachments
- Depot Guards
- March Battalions
- Officer Tables
- Convert the Militia

Reward style:

- unlocks templates
- improves unit quality
- adds commanders or high command where feasible
- changes weekly reinforcement mix
- consumes army XP or equipment through decisions rather than only giving free divisions

## Captured industry lane

Focus groups:

- Inventory the Captured Workshops
- Move the Rails Forward
- Convert Border Factories
- Field Repair Trains
- War Stores Office

Reward style:

- factories in owned core or controlled captured states only when justified
- supply hubs, railways, infrastructure, repair bonuses, production lines
- temporary consumer goods burden if overused

Geographic grounding:

- map work should target the capital, captured neighbor capitals, border states, and connected rail corridors

## Occupation administration lane

Focus groups:

- Provisional Administrators
- Local Registries
- Garrison Bargains
- Frontier Courts
- Core the First March

Reward style:

- unlocks coring decisions
- improves compliance and lowers resistance
- converts `Fury Impetus` into a more stable state package
- may reduce weekly reinforcement tempo as a tradeoff

## Expansion lane

Focus groups:

- First Neighbor
- Second Border
- The Next Weak Link
- Demand the Roads
- Continental Claims

Reward style:

- unlocks or improves target-selection decisions
- changes declaration delay
- adds claims where needed
- unlocks postwar settlement and integration decisions
- interacts with diplomacy and nearby-country alertness

Do not make this branch a linear claim ladder. Each focus should change the expansion loop or postwar handling.

## Evolution I branch, Veteran Marches

Unlock:

- Evolution I active for Event 007

Role:

- gives better starting units and more organized campaign tempo

Anchor focus groups:

- Lessons from the First March
- Standardize the Columns
- Veterans at the Border

Effects:

- better unit templates
- slightly larger weekly pulse
- lower early organization penalties
- new decision to convert weak militia into regular border units

## Evolution II branch, Joint Campaign Office

Unlock:

- Evolution II active and at least one other Fury country exists

Role:

- Fury countries can cooperate without becoming a single state

Anchor focus groups:

- Joint Campaign Office
- Shared War Tables
- Reserve Exchanges
- Fury Pact Liaison

Effects:

- creates or joins Fury Pact if valid
- unlocks shared reserves
- increases Fury coordination value
- prevents Fury countries from wasting declarations against each other under ordinary conditions
- gives faction cohesion goals

Failure:

- if one partner falls, coordination falls and shared reserve decisions become weaker or hidden

## Evolution III branch, All Fronts Open

Unlock:

- Evolution III active

Role:

- Fury becomes chaotic, stronger, and less cautious

Anchor focus groups:

- All Fronts Open
- Simultaneous Orders
- No Reserve Left Behind
- The Border Everywhere

Effects:

- declares on all valid weaker AI neighbors at once
- increases weekly force strength
- raises occupation strain sharply
- opens emergency all-front unit templates
- increases chance of no-neighbor or world-end branch if successful

Failure:

- overextension can halt declarations and weaken unit quality

## No-neighbor branch

Unlock:

- Fury country has no valid weaker AI land neighbors
- Fury has not capitulated

Role:

- lets the country consolidate rather than making impossible wars

Anchor focus groups:

- No Frontier Left
- Guard the Continent
- Integrate the Marches
- A State Made by War

Effects:

- improves coring and compliance
- unlocks defensive border missions
- reduces weekly reinforcement
- opens world-end preparation only under high chaos and size thresholds

## World-end branch

Unlock:

- world-end conditions from the core spec

Role:

- turns Fury from local campaign event into multi-continent terminal scenario

Anchor focus groups:

- War Without Borders
- Export the Spark
- Orders Across the Sea
- The Fury Pact Commands

Effects:

- starts cross-continent Fury ignition
- creates or strengthens main Fury faction
- changes decisions from local expansion to global ignition and coordination
- triggers world-end super-event

## Focus reward audit rules

The implementation should reject filler focuses. A focus is valid if it does at least one meaningful thing:

- unlocks or changes a decision family
- changes Fury values
- changes unit templates or weekly unit mix
- changes target selection
- changes compliance, coring, or resistance handling
- changes faction or cooperation behavior
- changes no-neighbor or world-end eligibility
- creates map or production changes tied to real states

## Route coverage table required after implementation

| Required route | Implemented branch | Status | Notes |
| --- | --- | --- | --- |
| Opening trunk |  |  |  |
| General Staff fork |  |  |  |
| March Administration fork |  |  |  |
| Military improvisation |  |  |  |
| Captured industry |  |  |  |
| Occupation administration |  |  |  |
| Expansion loop |  |  |  |
| Evolution I |  |  |  |
| Evolution II |  |  |  |
| Evolution III |  |  |  |
| No-neighbor branch |  |  |  |
| World-end branch |  |  |  |
