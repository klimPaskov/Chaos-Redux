# Decision and mission implementation prompt for Event 41

Implement the complete temporary decision and mission system for Disease in Divisions from the full Event 41 spec pack.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, the offline HOI4 decision, trigger, effect, scope, modifier, localisation, and data-structure pages, current vanilla decision documentation, and a comparable Chaos Redux crisis category before editing.

Use `common/decisions/041_disease_in_divisions_decisions.txt` and `common/decisions/categories/041_disease_in_divisions_categories.txt` unless a verified engine constraint requires another owner path.

## Presentation contract

Use an ordinary temporary decision category with:

- one static category picture
- one Army Infection Pressure meter or staged bar
- one trend indicator
- one posture status
- one short current-cause summary
- named infected-sector map highlighting
- three to five visible primary actions in the current phase
- no more than one active rotation mission

Do not create a full event-owned mechanic window for this system. Do not expose hidden profile, node, medical-capacity, evacuation-capacity, or spread-score variables as player counters.

## Required action families

Implement the action families exactly as designed in Part 3:

- Rotate the Sickest Formations
- Establish Quarantine Camps
- Expand Field Hospitals
- Sanitize Camps and Supply
- Assign Medical Evacuation Priority
- Repair the Medical Corridor
- Emergency Medical Mobilization
- Isolate the Military District
- Abandon the Contaminated Sector
- Restrict Offensive Operations
- Preserve Ordinary Operations
- Fight Through the Outbreak

Implement the Evolution I actions:

- Inspect Allied Formations
- Separate Coalition Camps
- Exchange Field Medical Reports
- Restrict Military Access

Implement the Evolution II actions:

- Close or Screen Military Ports
- Controlled Demobilization
- Protect Civilian Transport Hubs
- Restrict Allied Access
- Request International Medical Coordination

Use phased visibility. Severe and evolved actions should replace lower-priority actions where necessary. Do not append every action into one list.

## Rotation mission

Create one goal-style timed mission for the selected infected sector.

The mission must:

- name the infected sector and valid rear area or in-place recovery zone
- require affected formations or their safe event proxy to remain out of active combat
- require adequate supply
- require the medical corridor to remain open when one is used
- require the condition to be held for a sustained period
- auto-complete when the requirement is met
- fail only from a concrete operational breakdown
- lower pressure, improve recovery, and grant short reinfection resistance on success
- increase medical overload and delay recovery on failure
- avoid creating deaths directly from mission failure
- block duplicate missions and invalid targets

## Cost contract

Each decision or gameplay-changing posture action may have at most four spendable cost types. Use matching texticons and compact icon-first cost localisation.

Use the varied cost palette from the spec:

- support equipment
- trains
- motorized equipment
- fuel
- convoys for overseas routes
- manpower commitments
- civilian factory capacity
- army experience
- conservative command power where it represents command effort
- stability or war support only for major emergency diversion
- temporary formation, movement, organization, attack, supply, or logistics commitments

Treat state control, route control, unit placement, safe rear access, and faction relationship as requirements, not extra spendable costs.

Political power must not become the default response cost. Do not hide an extra cost in an effect, tooltip, confirmation, or secondary action.

## Dynamic scaling

Scale costs, duration, effect, cooldown, and AI willingness through:

- affected sector size
- pressure
- active sick and convalescent burden
- country industry and army size
- field hospitals and medical technology
- support equipment and transport
- supply and infrastructure
- front threat
- overseas route requirements
- hidden disease profile
- evolution state
- previous actions and failures

Centralize important thresholds and tuning in script constants or the approved owner tuning source.

## AI

Implement the action scoring from Part 6 and the named probability scenarios.

AI must:

- prefer early low-disruption control in a manageable outbreak
- repair a blocked route before paying for ineffective evacuation
- avoid impossible rotation missions
- accept emergency costs at army-crisis pressure
- use Fight Through only for a short urgent military reason
- protect allied and civilian routes when evolutions make them relevant
- stop dangerous postures when their strategic reason ends
- avoid spending unavailable equipment or transport

Any AI weight or probability patch requires a baseline `chaosx_ai_probability_auditor` pass and a post-change `hoi4.probability_compare` pass against the same scenario IDs.

## Tooltips and localisation

Write final player-facing text from the spec direction.

Every action must show:

- what the army is doing
- current cost
- named target where applicable
- visible immediate sacrifice
- broad expected effect
- exact blocked reason

Do not show raw triggers, raw variables, future surprise branches, or hidden profile names. Keep value and control tooltips concise.

## Cleanup and audit

Remove decisions, missions, target flags, selected-sector state, posture commitments, and active category state after resolution, invalidation, annexation, transfer, or event disable handling.

After implementation, spawn `chaosx_decision_mission_auditor` with a complete prompt and `fork_context=false`. Resolve every local patch or plan finding. Run the event completion audit before claiming the event is complete.
