# Event 007 Fury Decisions and Missions Specification

## Decision category

Working category id:

- `fury_campaign_category`

Visibility:

- visible to Fury AI countries
- may be hidden from players unless the player is observing through event details or debug views
- should not appear for player countries because players cannot become Fury

Header values:

- Current Fury target
- Fury momentum
- Occupation strain
- Integration capacity
- Fury coordination if Evolution II or III is active

The category should not show every possible target state or neighbor at once. Use phases, active caps, and route locks.

## Core decision families

### Prepare the Next Border War

Owner:

- Fury country

Availability:

- not already preparing a declaration
- not in no-neighbor state
- has at least one valid weaker AI land neighbor
- not locked by high occupation strain

Costs:

- command power or army XP only as part of the cost
- equipment and supply burden should matter
- delay grows with occupation strain and low supply

Effect:

- selects next target
- starts short hidden mission or timed flag
- declares war when timer completes

AI:

- aggressive when momentum is high
- cautious if occupation strain is high, equipment is low, or target has strong guarantees

### Seize Border Depots

Owner:

- Fury country

Availability:

- active war with target
- border states controlled or contested

Costs:

- army XP
- infantry equipment
- support equipment
- possible stability or war support cost if repeated

Effect:

- temporary supply support
- small chance of captured equipment
- increases occupation strain if used too often

### Captured Depot Mobilization

Owner:

- Fury country after a victory

Availability:

- captured capital or major supply area from target
- not recently used for same defeated neighbor

Costs:

- captured equipment logic where feasible
- manpower
- army XP

Effect:

- creates route-specific units based on captured territory
- not a generic free-division button

Templates:

- Depot Guards
- Border Shock Detachments
- March Battalions

### Install Provisional Administration

Owner:

- Fury country

Availability:

- controls recently captured states
- has enough equipment and manpower for garrisons

Costs:

- support equipment
- infantry equipment
- manpower
- temporary civilian factory burden or consumer goods pressure if the script supports it

Effect:

- raises compliance in selected captured state or state group
- lowers resistance risk
- raises integration capacity
- slows next declaration slightly unless route modifiers offset it

### Proclaim Frontier Core

Owner:

- Fury country

Availability:

- controls state
- compliance threshold reached
- resistance below threshold
- not a player-owned or protected state
- no invalid peace or transfer state

Costs:

- political power only as legal proclamation part
- support equipment
- manpower
- stability or war support depending on route
- time through mission or cooldown

Effect:

- adds core or staged core depending on balance
- reduces occupation strain
- increases expansion threat

### Coordinate the Next War

Unlock:

- Evolution II
- at least two Fury countries exist
- Fury Pact or working coordination link exists

Costs:

- Fury coordination
- equipment or army XP
- faction cohesion if implemented

Effect:

- partner Fury countries delay or sync declarations
- shared reserve chance
- target deconfliction

### Emergency War Tables

Unlock:

- General Staff route or Evolution III

Costs:

- stability
- war support
- command power
- equipment

Effect:

- shortens declaration delay
- improves weekly units
- increases occupation strain and resistance risk

### Convene the March Council

Unlock:

- March Administration route or no-neighbor branch

Costs:

- political power
- support equipment
- temporary industry burden

Effect:

- improves integration capacity
- reduces occupation strain
- unlocks broader coring projects

### Open the Continental Mandate

Unlock:

- no-neighbor branch
- high chaos
- Fury is large enough
- world-end conditions possible

Costs:

- high political and military burden
- stability and war support risk
- integration capacity requirement

Effect:

- begins world-end preparation, not immediate world-end on click unless all terminal conditions are already true

## Missions

### Hold the First Capital

Type:

- timed objective

Trigger:

- Fury captures the first target capital

Objective:

- hold the target capital and keep a connected supply route for a defined period

Success:

- stronger first victory aftermath
- more compliance
- more momentum

Failure:

- lower momentum
- delayed next target
- higher occupation strain

### Guard the Captured Border

Type:

- timed objective or auto-completing objective

Objective:

- keep supplied divisions in the border states that connect Fury to its new land

Success:

- lower resistance
- unlocks integration decision

Failure:

- resistance rises
- next declaration delayed

### Keep the March Supplied

Type:

- repeatable mission family with active cap

Objective:

- protect rail link from capital to conquered capital or border region

Success:

- improves weekly unit quality and supply

Failure:

- unit pulse weakens and occupation strain rises

## Cleanup

Clean up decisions and missions when:

- Fury country capitulates
- Fury flag is removed
- target no longer exists
- target is no longer a valid scope
- Fury has no valid neighbors and the mission is expansion-only
- world-end starts and replaces local decision logic

## Exploit checks

The implementation must prevent:

- repeatable free unit farming
- coring without compliance or state control
- player gaining Fury assets by tag switching or subject abuse
- Fury countries declaring on players through scripted target selection
- decisions remaining visible after Fury ends
- duplicate active missions for the same target state
- shared reserve loops between Fury countries
