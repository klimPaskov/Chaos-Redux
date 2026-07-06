# Decision and mission implementation prompt for Event 014 Cannibalism

Use this prompt with the HOI4 decisions and missions workflow.

Read:

- specs/014_cannibalism_spec_part_2_evolutions_decisions.md
- matrices/014_cannibalism_decision_matrix.md
- matrices/014_cannibalism_ai_strategy_matrix.md
- hoi4-decisions-missions skill
- chaos-redux-events skill

Implement the Event 014 decision category, missions, scripted localisation, AI behavior, cleanup, and tooltips.

Requirements:

- open the category only for active outbreak, exposure, aftermath, nearby cannibal country pressure, or valid scenario state
- show a curated set of decisions based on phase and posture
- use dynamic values for hunger, discipline, cult pressure, fear, spread, containment, island silence, hidden-leader resonance, unification readiness, and Wendigo fusion readiness
- use concrete costs such as equipment, trains, convoys, fuel, army XP, command power, manpower, stability, war support, state control, supplied divisions, naval access, and time pressure
- do not make the category a political power store
- add custom trigger tooltips for map and resource requirements
- missions should require action, such as holding named rail routes, placing supplied divisions, inspecting islands, or evacuating garrisons
- every mission needs success, failure, partial success where appropriate, AI behavior, and cleanup
- exploit path decisions must be route-locked and dangerous
- decisions must clean up when the country contains the outbreak, is annexed, loses the target state, changes route, or the world-end scenario begins

After implementation, run or request the decision-mission auditor and record a handoff under docs/plans/014_cannibalism_plans/subagent_handoffs.

Decision strength note: cannibal country, hidden-leader unification, and Wendigo fusion decisions should not use tiny or conservative outcomes. They should alter units, state control, death pressure, hunting grounds, absorbed armies, Wendigo unit access, or terminal threat state in visible ways.
