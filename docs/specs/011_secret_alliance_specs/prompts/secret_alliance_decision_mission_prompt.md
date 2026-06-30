# Decision and Mission Prompt: Event 011 Secret Alliance

Use `hoi4-decisions-missions` and the decision map in `matrices/011_secret_alliance_decision_map.md`.

Build the Counter Pact Operations category so decisions represent real actions. Avoid a political power store. Use dynamic costs based on target size, industry, agency capacity, war state, supply, border geography, equipment, faction state, suspicion, evidence, preparedness, and pact pressure.

Required decision families:

1. Investigation: courier routes, cipher traffic, safehouse raids, procurement tracing, interrogation chains.
2. Internal security: rail offices, industrial districts, officer protection, port and cable hardening.
3. Diplomacy and split operations: private demarche, off-ramp guarantees, neutral conference, partial dossier, defector protection.
4. Military readiness: contingency plans, border watch, capital command lines, reserve depots, allied observers.
5. Neighbor confrontation: border search, frontier closure, border war, inspectors.
6. Public confrontation: demand dissolution, publish dossier, preemptive strike, emergency alliance consultation.

Timed missions should use named states or clear dynamic named regions. Goal-style missions should auto-complete when the player has done the work. Mission failure must change pact readiness, hostility, evidence, preparedness, or member commitment. Add AI equivalents and cleanup for invalid targets, reveal, annexation, peace, and member defection.
