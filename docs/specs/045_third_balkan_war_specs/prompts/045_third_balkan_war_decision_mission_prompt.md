# Decision and mission implementation handoff for Event 045

Implement the Event 045 decision system from the accepted specifications and diagrams. Read `chaos-redux-decisions-missions` before editing and use `chaosx_decision_mission_auditor` after the parent implementation pass.

## Presentation choice

Use one ordinary Event 045 decision category with a static category picture and a compact dynamic header. Do not build a dedicated scripted GUI. The header shows:

- Balkan War Escalation as the only persistent custom value
- current named stage
- latest material cause of movement
- next threshold and any missing proof
- the current country's role

Keep the category phase-aware. A country should normally see three to five primary actions, never more than six, and one to three active missions. Use the selected-target pattern for country lists so the category does not display one action row for every Balkan participant or sponsor.

## Required action families

### Regional belligerents

- activate one valid regional claim or settlement goal
- secure a named military corridor
- request or reject foreign support
- press for an armistice when military conditions justify it
- contest an allied occupation that conflicts with the country's registered interests

### Neutral Balkan governments

- declare guarded neutrality
- mobilize around a newly relevant registered interest
- mediate a bilateral frontier issue
- join a camp only through a real claim, threat, guarantee, ideological, or strategic connection
- prepare defenses around a named frontier, port, railway, or capital route

### Outside containment powers

- coordinate mediation
- suspend arms or volunteers
- pressure a guarantor or faction leader to limit commitments
- sponsor an armistice conference
- enforce sanctions or diplomatic pressure against the party widening the war

### Outside exploitative powers

- send equipment through a viable route
- send volunteers or a military mission
- recognize one registered claim
- issue a guarantee
- invite a participant into a faction through normal validity rules
- prepare direct intervention only when access, forces, readiness, and escalation justify it

## Required mission families

- hold the capital rail line
- secure an Aegean or Adriatic corridor
- observe and hold an armistice line
- restrain an ally from occupying a disputed registered region
- secure or deny the Straits approaches when Turkey and the theater make that objective relevant

Missions must name their states or named regions and require real action. They should use varied durations, normally 90 to 180 days, based on travel, construction, and combat difficulty. Success, partial success, and failure need distinct effects.

## Costs and effects

Use no more than four spendable cost types for one action. Match costs to the act through equipment, fuel, convoys, trains, command power, XP, stability, war support, civilian factory burden, or tied military capacity. Political power may support diplomatic actions but must not become the default payment.

Every action must change a relationship, mission, claim, settlement term, map objective, support tier, or escalation state. Do not add a tray of small modifier purchases. All costs need matching texticons and clear blocked tooltips.

## AI and probability evidence

Every AI-usable action needs equivalent scripted logic. Before changing weights, route the surface through `chaosx_ai_probability_auditor` and the named scenarios in `quality/045_third_balkan_war_probability_scenarios.md`. After the owner applies the chosen balance, run `hoi4.probability_compare` on the same scenarios.

## Cleanup

Remove obsolete actions after camp destruction, target invalidation, settlement, role change, wider-war handoff, or event cleanup. Clear selected targets, temporary flags, active missions, costs, and stale decision activations. Do not use a whole-world daily scan.

The handoff must list every category, decision, mission, helper, localisation key, cost type, AI surface, cleanup hook, audit result, and unresolved risk. No unapproved fallback is permitted.
