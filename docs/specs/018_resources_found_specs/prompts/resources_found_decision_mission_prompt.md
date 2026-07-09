# Decision and Mission Prompt for Event 018 Resources Found

Use `hoi4-decisions-missions`, `chaos-redux-events`, and the Event 018 spec files. After implementation, run `chaosx_decision_mission_auditor` and resolve its findings.

## Required category

Create a resource field decision category or scripted GUI-backed category for the owning country of the active field. It must show the selected state and the current visible values.

Visible values:

- field richness
- extraction pressure
- survey confidence
- worker safety
- foreign interest
- local dependence
- public panic after public danger
- vague below pressure or dangerous-depth status after sickness

## Required decision families

Implement staged families from the decision map:

- survey and confirmation
- extraction and infrastructure
- trade and concessions
- nationalization and concession balancing
- security and smuggling response
- safety and worker relief
- medical survey camps
- demilitarized field pressure
- border crisis and possible border war
- evacuation and city shelter
- cave hunts
- closure and emergency shaft collapse
- anti-Cave Host resource denial
- aftermath reclamation

## Cost rules

Do not default to political power or command power. Use concrete costs and requirements such as civilian factory time, construction capacity, infantry equipment, support equipment, artillery, anti-tank, trains, convoys, fuel, manpower, divisions in the state, state infrastructure, rail access, relations, stability, war support, local dependence, survey confidence, and worker safety.

Command power costs must stay conservative.

## Mission rules

Create timed missions for actual objectives:

- securing survey zones with divisions
- building extraction routes
- balancing concessions
- protecting lower works
- evacuating settlements
- sealing before breach
- starving Cave Host by denying resource states
- reclaiming and sealing origin state

Missions need success, failure, partial success where useful, cleanup, AI logic, and dynamic localisation for state names and costs.

## AI rules

AI must understand resource need, war state, stability, industry, country strength, ideology, foreign relations, field richness, public danger, and Cave Host risk. AI must be able to use equivalents for any important scripted GUI button.

## Cleanup

Handle owner change, state transfer, site closure, Cave Host emergence, Cave Host defeat, invalid target countries, invalid state, disabled evolution, and world-end state. Do not leave stale decisions or missions visible.
