# Decision and Mission Implementation Prompt for Event 018 Resources Found

Implement the complete Event 018 decision and mission systems from the source specs and `matrices/decision_mission_matrix.md`. Follow `AGENTS.md`, `chaos-redux-events`, and `chaos-redux-decisions-missions`. Use the scripted-system architect for repeated field, target, capacity, cost, and cleanup logic. Run the decision and mission auditor before completion.

All working labels are design handles, not final localisation. Write final player-facing text during implementation.

## Required decision surfaces

Implement five coordinated surfaces.

### 1. Resource field management category

Owner-facing category for discovery, appraisal, development, extraction, labor, safety, security, trade posture, suspension, and closure.

Attach a compact scripted GUI header that shows:

- selected field state
- Event 018 resource composition
- Developed Yield
- Excavation Depth
- Workforce Safety
- Foreign Pressure
- Subsurface Disturbance after reveal
- Breach Pressure in Evolution III
- posture
- contracts or commission status
- current closure or suspension state

Use a selected-field cycle for human players. AI must evaluate all fields without selecting them.

The category must use phases and replacement actions. Do not show every development, diplomacy, crisis, and closure decision at once.

### 2. Foreign contract and pressure actions

Implement targeted behavior for interested countries and the field owner.

Required families:

- invite bids
- request purchase agreement
- offer development assistance
- seek exclusive rights
- guarantee or protect access
- reserve domestic output
- balance buyers
- renegotiate concession
- nationalize
- settle compensation
- counter survey teams
- expose sabotage
- break smuggling routes

Only high-interest countries should receive active decisions. Use a compact target-management or event-offer pattern rather than one visible row per country worldwide.

Contracts must store partner, term, access, current status, and interruption reason. They must react to occupation, route loss, war, suspension, closure, partner death, and state transfer.

### 3. Border crisis and commission category

Implement the staged dispute only when a valid claimant exists.

Required stages:

- competing surveys
- road or customs confrontation
- armed patrol incident
- timed frontier mission
- limited border war where appropriate
- victory, transfer, stalemate, and settlement
- commission proposal
- demilitarization and inspection
- violation and compliance restoration
- commission dissolution

Timed missions must use named states, supplied divisions, route control, troop limits, or other active objectives. Do not use passive manpower or stability checks as the main mission.

Reuse existing border-conflict infrastructure if valid. Event 018 still owns field-value gates, claimant validity, state transfer, ledger persistence, contracts, and settlement.

### 4. Evolution III containment and closure category

Required actions:

- reinforce perimeter
- hunt surface packs
- clear urban district
- secure transport corridor
- evacuate field settlements
- evacuate state center
- request foreign hard-attack aid
- seal one access network
- partial closure
- full sealing
- last emergency seal

Hunts require supplied hard-attack capable forces and real equipment commitments. Evacuation uses trains, trucks, routes, time, and receiving capacity. Full sealing requires suspended extraction, state control, engineering, evacuation or secured civilians, surface containment, and total sacrifice of Event 018 resource additions.

Success and failure effects must be distinct. Full-seal success permanently blocks Evolution IV and removes only Event 018 resources. Partial closure must never set the prevention flag.

### 5. Cave-country and anti-cave categories

Cave-country actions:

- mark a high-resource target
- activate a captured resource anchor
- accelerate a critical anchor
- guard a feeding chamber
- choose next spawn template
- replace destroyed protected origin brood
- consolidate Unfed Broods
- build bounded tunnel links
- use doctrine-specific assault actions
- convert captured industry
- track continent progress
- prepare cross-continent rupture after terminal prerequisites

Ordinary-country anti-cave actions:

- emergency anti-armor contracts
- request or send hard-attack aid
- deny a resource state before loss
- liberate an activating anchor within the activation window
- clear a mature anchor
- share hard-attack intelligence
- open evacuation corridors
- restore liberated resources and infrastructure

## Dynamic values and costs

Centralize thresholds, gains, losses, durations, cooldowns, AI weights, and scaling values. Use actual field and country conditions.

Factors include:

- resource amount and types
- field yield, depth, safety, pressure, disturbance, breach
- country industry, manpower, equipment, fuel, trains, and supply
- war state
- stability and war support
- state infrastructure and control
- contract influence
- claimant strength
- chaos and evolution stage
- active field count
- cave capacity and active divisions

Major actions cannot default to political power or command power only. Use civilian factory burden, equipment, manpower exposure, trains, trucks, fuel, supplied divisions, state control, local safety, contract commitments, and time.

Show nonstandard costs with icon-first scripted localisation and custom tooltips. If a button has many requirements, show a short met or not-met summary and place the full list in a tooltip.

## Mission quality

Every timed mission must ask the player or AI to do something active.

Good Event 018 objectives include:

- hold the field and rail corridor
- maintain supplied divisions in named border states
- keep troop levels below commission limits
- recapture a resource state before anchor activation
- secure evacuation routes
- hold a city district during a hunt
- keep the origin state supplied
- control all eligible continent states for the verification period

Use varied durations. Ordinary projects can use 90 to 180 days, major construction and closure longer, emergency missions shorter only when the crisis demands it.

Implement partial success where appropriate. A corridor can remain open while one settlement is lost. A hunt can destroy a pack but lose the transport line. A border mission can secure the field but fail the diplomatic objective.

## Selected-target and clutter rules

- Show one selected field to the human owner.
- Use target shortlists for foreign contracts.
- Use named dispute states for border missions.
- Use one marked resource target for the cave country at a time.
- Hide obsolete development actions after suspension or closure.
- Replace basic decisions with stronger later versions.
- Cancel missions when owner, state, target, route, war, field, cave country, or world-end status becomes invalid.
- Do not leave closed fields, dead partners, lost states, completed anchors, or defeated cave targets visible.

## AI requirements

Implement the full intent in `matrices/ai_strategy_matrix.md`.

AI must:

- choose field posture from need, strength, ideology, and risk
- invest where the field is valuable and defensible
- fund safety and closure when appropriate
- exploit dangerously only under real pressure or extreme route preferences
- offer contracts only when route and need are valid
- avoid border war when much weaker or blocked by commission
- request and send Evolution III aid
- prioritize hard attack and anchor denial against cave units
- target resource-rich states as the cave country
- protect origin and mature anchors
- respond to over-capacity weakness
- complete continent objectives

Human-only scripted GUI buttons need AI-equivalent decision or effect paths.

## Cleanup requirements

Clean:

- selected field
- state field records
- partner targets
- bidder lists
- contract flags and timers
- commission guarantors
- claimant references
- active missions
- disturbance and breach targets
- closure flags
- cave origin references
- anchor activation progress
- capacity contributions
- spawn queue state
- excess-division state
- continent-progress arrays
- world-end candidates

Use global event targets only where persistence requires them and clear them explicitly.

## Localisation requirements

Every category, decision, mission, button, cost, blocked state, success, failure, and tooltip needs final localisation. Use dynamic state, country, resource, value, timer, and cost references. Keep integer values without unwanted decimals.

Do not expose raw triggers. Do not reveal hidden cave formulas in ordinary field text. Do not use achievement language outside the achievement UI.

## Required audit handoff

After implementation, run `chaosx_decision_mission_auditor` with `fork_context=false`. The handoff must report:

- categories and decisions implemented
- mission owners, targets, durations, success, failure, and duplicate risk
- costs and dynamic scaling
- AI validity
- cleanup
- exploit checks
- localisation keys
- meaningful validation scenarios
- simplifications or blockers

## Completion standard

The decision layer is complete only when it creates active field management, material tradeoffs, targeted diplomacy, staged border conflict, meaningful containment and evacuation, full closure, cave resource deployment, anti-cave counterplay, AI parity, readable dynamic values, lifecycle cleanup, and no passive store-like clutter. Every mapped action must be implemented, explicitly merged with a reason, or reported as missing.
