# 020 Black Plague decision and mission prompt

Use `hoi4-decisions-missions`, `chaos-redux-events`, and the existing shared disease and biowarfare system. The Black Death must use dynamic shared disease decisions, not a duplicate Black Plague category.

All labels are working labels only. Final decision and mission text belongs to implementation and localisation.

## Required decision-board structure

The shared disease board should change by country and state status.

| State or country situation | Visible action direction |
| --- | --- |
| no nearby infection | preparedness, surveillance, medical stockpiles, early warning, port readiness |
| bordering infection | border controls, troop-route restriction, local medical buildup, refugee corridor management |
| port or overseas threat | port inspection, convoy checks, naval movement screening, island health patrols |
| infected owned state | quarantine, lockdown, field hospitals, treatment surge, army cordon, vector control |
| contained state | maintain cordon, monitor relapse, staged reopening, treatment continuation |
| recovering or cured state | cleanup crews, recovery support, relapse watch, optional prevention |
| weaponized exposure | emergency containment, evidence handling, accident response, diplomatic risk control |
| rat-held border | cordon, evacuation, fortification, nest assault preparation, retaken-state cleanup |

Do not show every possible decision at once. Use phases, target selection, state lists, status filters, cooldowns, and cleanup so the board feels like a crisis board rather than a debug menu.

## Required decision families

Prepared and clean-state family:

- surveillance network
- emergency stockpiles
- local health inspections
- port readiness
- early warning in high-risk states
- prevention law or public health mobilization where existing systems support it

Threatened-state family:

- border controls
- port inspections
- troop-route restrictions
- refugee corridor management
- local medical buildup
- supplies to threatened states
- public order support if panic affects state capacity

Infected-state family:

- emergency quarantine
- lockdown or movement restriction
- field hospital expansion
- treatment surge
- army cordon
- vector and sanitation work
- cleanup crews after severity falls
- severe-state triage where the player accepts economic and stability costs to lower death ticks

Contained and recovery family:

- maintain containment
- monitor relapse
- staged reopening
- recovery support
- local reconstruction
- remove or downgrade disease state modifiers after enough progress

Cure and countermeasure family:

- national cure effort
- sample-sharing through safe gameplay abstraction
- field treatment deployment
- medical production funding
- international research support
- countermeasure project hooks for bio-capable countries

Weaponization and exposure family:

- defensive study
- special-project study route
- safety program
- weaponization project hooks
- accident response
- domestic exposure containment
- condemnation and retaliation response
- deployment handling through existing biowarfare delivery systems

Anti-rat family:

- rat border cordon
- evacuation from threatened border states
- emergency fortification
- nest assault preparation
- retake rat-held state operation
- protect cleanup crews after retaking
- destroy warren remnants
- maintain anti-rat buffer while plague residue is still active

International family where implementation supports it:

- medical aid
- research sharing
- containment coalition support
- port inspection coordination
- emergency border compact
- anti-rat coalition support after public King reveal

## Cost rules

Political power and command power may appear only when they fit the action. They must not be the default cost model.

Use costs and requirements such as:

- support equipment
- trucks
- trains
- convoys
- infantry equipment
- artillery or motorized equipment for cordons when appropriate
- manpower for medical, police, or cordon staffing
- stability
- war support
- civilian factory burden
- supply throughput
- fuel for large troop or evacuation operations
- army XP for military cordons or anti-rat doctrine actions
- air or navy XP only when port or air delivery systems justify it
- local control, compliance, or resistance conditions
- divisions present in named states
- ports, rail, or supply hub control
- medical capacity or cure progress
- intelligence exposure for foreign study or weaponization work
- condemnation for bioweapon actions
- diplomatic relations or access for international support
- time pressure through missions

Costs should scale with state population, number of target states, disease severity, war state, industry, and evolution state where practical.

## Mission rules

Use missions when the player must hold, guard, secure, retake, or sustain something. Missions should have meaningful success and failure.

Required mission pools:

- hold a border cordon for a threatened state group
- keep supplied divisions in threatened or infected border states
- keep ports inspected during overseas exposure
- sustain quarantine until severity drops
- protect field hospitals during severe outbreak
- maintain cure work while infection remains active
- retake rat-held states
- hold retaken states long enough for cleanup crews to work
- destroy warren remnants after rat defeat
- prevent rat entry into core states
- maintain anti-rat buffer before attacking a King-held front

Success should lower spread risk, disease load, death pressure, rat pressure, relapse chance, or warren strength. Failure should raise spread risk, trigger state severity growth, open new infection routes, damage stability or supply, or strengthen rat growth where relevant.

Partial success is useful for retaken plague states, port inspection, evacuation, and field hospital missions.

## Target and cleanup rules

Every state-targeted decision or mission must clean up stale state flags, country variables, active mission entries, and target lists when:

- the state changes owner
- the state changes controller
- infection status changes
- containment succeeds
- cleanup finishes
- rat country takes the state
- rat country is defeated
- King forms and transfers state logic
- world-end scenario fires
- disease system is disabled if the shared system supports toggles

Do not leave missions active for cured states, dead countries, annexed tags, invalid ports, or states no longer adjacent to a threat.

## UI and tooltip rules

Every dynamic state decision needs readable requirement text. Avoid raw state id lists. Use state names, target country names, named regions, or dynamic summaries.

Costs should be icon-first. Long requirements should use a compact status line with a detailed tooltip. Missing requirements should be clear without exposing raw triggers.

The board should show:

- selected state status
- disease load or severity
- containment level
- cure effect
- spread risk direction
- death pressure direction
- rat or warren pressure after public reveal
- available response families
- why key actions are blocked

Hidden rat and King mechanics must not appear in early disease-board text before the public reveal conditions.

## AI rules

AI decisions must account for:

- infected state count
- threatened state count
- population at risk
- severity and death pressure
- war state
- stability and war support
- industry and supply capacity
- equipment and manpower
- ports and borders
- current cure progress
- disease protections
- faction membership
- ideology and risk tolerance
- biowarfare capability
- condemnation
- rat borders
- King threat level

AI should not weaponize or underreact through flat chance. Dangerous choices should require desperation, extreme ideology, strong biowarfare capability, high chaos, or strategic pressure.

Rat AI and King AI should use separate logic. They should not use the human disease board as if they were normal countries.

## Audit request

After implementation or major changes, spawn `chaosx_decision_mission_auditor` with `fork_context=false`. Ask it to inspect the shared disease board, state target lists, costs, mission quality, AI behavior, cleanup, duplicate missions, tooltip clarity, and exploit risk.
