# Decision and Mission Implementation Prompt for Event 55

Implement the Event 55 project category and mission families from the complete source specs.

Read `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, the Event 55 specs, and the relevant offline Decision Modding, Triggers, Effects, Localisation, Modifiers, Scopes, and Data Structures pages. Inspect vanilla and existing Chaos Redux precedents.

## Presentation

Use one ordinary Event 55 decision category with a category icon, static category picture, compact status header, targeted project proposals, and normal missions.

Do not introduce a dedicated scripted GUI.

Keep one category state to three to five primary actions and never more than six. Keep active missions between one and three. Hide new authorizations at the project limit. Hide obsolete, invalid, or stale rows.

Expose one persistent public custom value, National Works Capacity. Project progress belongs to mission progress. Route condition uses qualitative status.

## Required decision families

- survey and refresh proposals
- authorize one of the stored geographic proposals
- choose accelerated, standard, or conservative construction method
- domestic right-of-way response
- foreign partner invitation and counteroffer response
- procurement intervention
- cost overrun response
- reduce project scope
- suspend, resume, abandon, and stage-based salvage
- emergency repair
- reroute a severed project
- renegotiate a Dormant international corridor
- transfer host after annexation or partner collapse
- relief-priority conversion when a valid humanitarian request exists
- network-level repair or operating action under Evolution III

## Required mission families

- survey and charter
- partner agreement deadline
- procurement and mobilization
- main construction
- commissioning
- repair
- rerouting
- continuous operation periods used by achievements

A project should show one main active mission at a time. Do not stack survey, procurement, and construction timers for the same project.

## Cost rules

No action may consume more than four spendable cost types.

Use costs that fit the action, including trains, trucks, convoys, support equipment, fuel, political power, command power only for real military administration, stability or war support consequences, and timed civilian construction burden.

Represent steel and other non-stockpiled resources through access requirements, import arrangements, or industrial diversion. Do not invent a resource stockpile debit.

Use the existing stockpile debit helpers where they fit. Confirm every displayed cost has the correct texticon.

## Objective rules

Name actual route states, ports, resources, and partner countries through dynamic localisation.

Use custom trigger tooltips for long requirements. Do not expose raw trigger blocks.

Construction, repair, and rerouting missions must require real route control, access, equipment, or partner conditions. Do not use passive generic stockpile checks as the whole objective.

Auto-complete missions when the player has done the work. Do not require a second completion click.

## AI and weighted logic

Implement AI equivalents for every human action.

Run the probability audit cycle for project start, method choice, partner response, and failure response. Use the named scenarios in the quality matrix. The probability auditor remains read-only. The owner applies changes, then the auditor compares the same scenarios.

## Cleanup

Every project end state must clear its active mission, burden, temporary method state, invitations, stale proposals, partner receipts, route highlights, and invalid targets once.

Test annexation, civil war, state loss, state recovery, partner withdrawal, war, embargo, project completion, reduced completion, abandonment, transfer, and save reload.

## Audit

After implementation, spawn `chaosx_decision_mission_auditor` with a context-complete prompt. Resolve every category clutter, cost, tooltip, AI, objective, cleanup, exploit, and duplicate mission finding before completion.
