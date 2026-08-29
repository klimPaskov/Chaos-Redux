# Event 033 Acid Rain, Part 5, preparedness, decisions, and recovery

## Decision-category purpose

Every existing country receives the Acid Rain category at formation, including countries outside the current front region. The category supports three practical stages:

- advance preparation
- urgent response during warning or exposure
- state recovery after the front leaves

Only actions relevant to the country's current stage appear. The category should not become a long list of inactive buttons.

All project, action, mission, and category names in this part are working labels. Final player-facing wording belongs in implementation and localisation review.

## Preparedness components

Each country has four component tiers from 0 to 4.

| Component | Weight | Main protection |
| --- | --- | --- |
| Shelter network | 30 | Opening mortality, severe-cell survival, civilian exposure |
| Protected water and food | 25 | Sustained mortality, contaminated runoff, aftermath |
| Medical and protective capacity | 25 | Sustained mortality, severe casualties, recovery speed |
| Transport and infrastructure resilience | 20 | Evacuation, rail and supply continuity, building damage |

Preparedness is the sum of each component's completed fraction multiplied by its weight.

Example: Shelter tier 2 contributes `15`, water tier 1 contributes `6.25`, medical tier 3 contributes `18.75`, and transport tier 2 contributes `10`, for total Preparedness `50`.

## Project presentation

Show four repeatable project decisions, one per component. Each button reads the current tier, next tier, duration, exact costs, expected protection direction, and whether the project can finish before a known front arrival.

The project closes at tier 4. It does not create four separate buttons.

## National scale and affordability bands

Project cost should reflect the population and territory being protected without making poor large countries unable to act.

### Geographic scale band

Use owned or controlled frozen eligible states and starting Event 33 civilian population:

| Scale | Direction |
| --- | --- |
| Local | 1 to 5 eligible states and under 10 million population |
| Regional | 6 to 15 eligible states or 10 to 30 million population |
| National | 16 to 40 eligible states or 30 to 80 million population |
| Continental | More than 40 eligible states or more than 80 million population |

Use the higher qualifying scale.

### Industrial capacity band

| Capacity | Available civilian factories direction |
| --- | --- |
| Fragile | Fewer than 5 |
| Limited | 5 to 14 |
| Established | 15 to 39 |
| Great-power | 40 or more |

The final cost band equals the geographic scale band, capped at no more than one band above industrial capacity. This keeps populous weak countries under pressure while preserving a payable route.

### Cost multipliers

| Final band | Multiplier |
| --- | --- |
| A | 0.65 |
| B | 0.85 |
| C | 1.00 |
| D | 1.35 |

Project tier multipliers are `1.00`, `1.25`, `1.55`, and `1.90` for tiers 1 through 4. Equipment values round up to whole items.

## Project 1, shelter network

### Direction

Expand public shelters, seal basements, harden public buildings, distribute shelter instructions, and create protected assembly points.

### Base tier-1 commitment before multipliers

- 21 days
- 1 civilian factory commitment
- 90 support equipment consumed
- 1,000 manpower temporarily reserved

### Tier effects

Each completed tier:

- adds 7.5 Preparedness
- improves ordinary and global opening-shock protection
- improves severe-cell shelter response
- lowers the chance that a weak warning is treated as unprotected

Manpower returns when the project completes or is safely cancelled. Equipment remains consumed.

## Project 2, protected water and food

### Direction

Cover reservoirs, protect wells, stock sealed containers, establish food inspection, and create protected distribution routes.

### Base tier-1 commitment

- 21 days
- 1 civilian factory commitment
- 60 support equipment consumed
- 1 train consumed for land-heavy countries, or 5 convoys for countries whose eligible population is mainly overseas or island-based
- 500 manpower temporarily reserved

The train and convoy routes are mutually exclusive variants. One action never charges both.

### Tier effects

Each completed tier:

- adds 6.25 Preparedness
- reduces sustained mortality after twelve days of exposure
- reduces environmental aftermath from contaminated water and soil
- improves famine, disease, and Humanitarian integration outcomes when those systems qualify

## Project 3, medical and protective capacity

### Direction

Expand burn and respiratory treatment, train emergency staff, distribute protective clothing, maintain filters and masks, and stock decontamination supplies.

### Base tier-1 commitment

- 24 days
- 1 civilian factory commitment
- 120 support equipment consumed
- 1,000 manpower temporarily reserved
- 250 fuel consumed

### Tier effects

Each completed tier:

- adds 6.25 Preparedness
- reduces sustained mortality
- raises the cap on concurrent emergency medical actions
- shortens severe-casualty recovery
- integrates with existing CBRN civilian protection without duplicating its equipment classes

## Project 4, transport and infrastructure resilience

### Direction

Protect rolling stock, create alternate rail plans, move repair material, cover exposed machinery, and prepare evacuation transport.

### Base tier-1 commitment

- 24 days
- 1 civilian factory commitment
- 1 train consumed
- 25 motorized equipment consumed
- 250 fuel consumed

### Tier effects

Each completed tier:

- adds 5 Preparedness
- reduces building-damage pressure
- improves evacuation effectiveness
- lowers acute supply and movement penalties
- improves transport-recovery decisions

## Project duration scaling

Apply the tier duration factors below after the base duration:

| Next tier | Duration factor |
| --- | --- |
| 1 | 1.00 |
| 2 | 1.15 |
| 3 | 1.35 |
| 4 | 1.60 |

Country cost band changes physical costs, not duration. Known front proximity does not make construction finish instantly.

## Concurrent project limits

| Capacity band | Maximum active projects |
| --- | --- |
| Fragile | 1 |
| Limited | 1 |
| Established | 2 |
| Great-power | 3 |

A country at Global Acid Rain can receive one temporary extra slot if it has at least ten available civilian factories after current commitments. The extra slot closes when the global phase ends and does not cancel a valid project already in progress.

## Cancellation and resource ledger

Every project records:

- start date
- expected completion date
- exact paid equipment
- exact temporarily reserved manpower
- civilian factory commitment
- owning country
- component and target tier

Cancellation rules:

- consumed equipment, fuel, trains, convoys, and motorized equipment are not refunded
- temporarily reserved manpower returns once
- civilian factory commitment ends once
- the component tier is granted only on completion
- invalid tag transitions call the shared commitment cleanup before country deletion

A project cannot be started twice for the same component and target tier.

## Urgent response stage

Urgent decisions appear when the country has a warning, active exposure, or a severe forecast. They are temporary measures and do not replace permanent project tiers.

### Activate shelter protocols

- country action, 14 days
- costs political power, support equipment, and a small manpower reserve
- reduces opening and sustained mortality in currently exposed states
- stronger with shelter tier
- one active instance per country

### Secure emergency water and food

- country action, 21 days
- land route uses support equipment and trains
- island or overseas route uses support equipment and convoys
- lowers sustained mortality and aftermath growth
- improves contaminated-water Humanitarian outcomes

### Emergency medical surge

- country action, 14 days
- uses support equipment, manpower reserve, and fuel
- lowers sustained mortality and severe-cell casualty pressure
- creates a post-action medical fatigue cooldown

### Reroute transport and repair crews

- country action, 14 days
- uses trains, motorized equipment, and fuel
- lowers acute supply penalties and building-damage pressure
- cannot run if the country has no valid transport stock

### Evacuate forecast severe zone

- state-targeted action
- available only during a severe-cell or superstorm forecast
- uses manpower reserve, motorized equipment, trains, and fuel, or a documented convoy variant for an island state
- applies a local evacuation receipt before impact
- reduces severe mortality and civilian exposure
- temporarily reduces local production, construction, and supply efficiency
- registers displacement pressure with the shared Humanitarian interface when the evacuation is large enough

The evacuation action protects people in place and through temporary relocation. It does not directly transfer permanent state population unless a verified shared migration API is available and accepted during implementation.

## Urgent action limits

- maximum five primary urgent actions visible
- maximum one active version of each national action
- maximum one evacuation per forecast state
- maximum two simultaneous state evacuations for fragile and limited countries
- maximum four for established countries
- maximum eight for great powers

These are active-operation caps, not lifetime caps.

## Warning and timing rules

A permanent preparation project can continue after a front arrives. Its next tier applies only after completion.

Urgent action behavior:

- an action must finish before the applicable pulse to affect that pulse unless its definition grants partial immediate protection
- severe evacuation gives a partial immediate effect after one full day and its full effect on completion
- the tooltip compares completion date with the known arrival window
- an AI country does not start a long urgent action that cannot affect any remaining forecast or exposure pulse

## Recovery stage

A country with aftermath states receives a compact state list. Selecting a state exposes the relevant recovery actions.

### Restore transport network

Targets infrastructure and railway damage. Uses civilian factory commitment, trains, motorized equipment, and fuel. It reduces transport aftermath and can add bounded repair progress.

### Decontaminate water and soil

Uses civilian factory commitment, support equipment, manpower, and trains or convoys. It lowers environmental aftermath and contaminated-water pressure.

### Repair exposed industry

Uses civilian factory commitment, support equipment, and manpower. It improves civilian and military factory repair and lowers industrial aftermath. It cannot restore more levels than were damaged.

### Demobilize emergency apparatus

Available after no active exposure remains in the country. It returns valid temporary manpower commitments, removes fatigue modifiers, and converts unused emergency preparation into a small recovery-speed benefit. It does not refund consumed equipment.

## Recovery priority

The state list sorts by:

1. aftermath tier
2. current population
3. capital status
4. supply and railway importance
5. damaged factory count
6. first exposure date
7. state ID as deterministic tie-breaker

The AI uses the same priority model with additional affordability checks.

## Category visibility

| Country state | Category behavior |
| --- | --- |
| No warning, no exposure, projects available | Show four permanent projects and map summary |
| Warning active | Show projects plus relevant urgent actions |
| Exposure active | Show urgent actions first, projects below |
| Severe forecast | Pin evacuation and shelter response at top |
| Rain gone, aftermath remains | Show recovery state list and actions |
| No exposure, aftermath, warning, or commitment | Close category after final national report |

The global GUI remains available through the Event Log after national category closure.

## Preparation report

A country receives one successful-preparation report when all conditions hold:

- it has taken meaningful exposure
- its prevented-death estimate crosses the accepted threshold
- Preparedness or an urgent action materially reduced the outcome
- no similar report has fired in the last sixty days

The report explains the relevant preparation component and avoided-loss estimate. It does not claim exact counterfactual certainty.
