# Decision and Mission Prompt for Event 011 Secret Alliance

Use `hoi4-decisions-missions` and route follow-up audit to `chaosx_decision_mission_auditor`.

Implement the Counter-Conspiracy Dossier category and optional Dossier Board scripted GUI from the spec.

Required decision families:

- investigations
- protection and hardening
- diplomacy and fracture
- border watch missions
- exposure actions
- pact crisis actions
- wartime fracture actions

Non-negotiables:

- decisions should represent concrete national action
- do not make a political power store
- use varied costs: XP, equipment, trains, trucks, support equipment, civilian burden, stability, war support, relations, intel exposure, unit placement, route control, and timed objectives
- missions must have success, failure, partial-success where useful, and cleanup
- border actions must require real neighboring members or suspects
- AI must have equivalents and safe target validation
- hidden member data must not leak through tooltips or raw triggers
- obsolete decisions must hide or clean up after reveal, war, settlement, annexation, or pact collapse

Use `matrices/011_secret_alliance_decision_map.md` as the main decision map.
