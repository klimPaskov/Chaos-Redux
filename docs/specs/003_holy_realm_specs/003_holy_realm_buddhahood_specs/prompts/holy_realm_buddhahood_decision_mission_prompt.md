# Decision and Mission Prompt: Holy Realm Buddhahood

Use `hoi4-decisions-missions` with the Holy Realm specs.

Implement the decision and mission systems from:

- `specs/holy_realm_buddhahood_decisions_missions.md`.
- `specs/holy_realm_buddhahood_mechanics_and_gui.md`.
- `matrices/holy_realm_buddhahood_ai_matrix.md`.

Core requirements:

- Teaching missions must require real action, costs, route access, named targets, or timed objectives.
- Meditation must gate Buddha powers through a three-minute channel if the engine supports it, or the accepted concentration sequence fallback if not.
- Buddha powers must require Buddhahood and Meditation Charge.
- Anti-chaos buffs must only apply against valid chaos countries.
- Final Silence decisions must require Buddhahood and must not become terminal unless chaos is over 1000 and no world-end exists.
- AI must have equivalent paths for all meaningful GUI actions.
- Decision categories must use visibility, cooldowns, cleanup, and clutter control.
- Costs should use equipment, convoys, trains, manpower, stability, supply, objectives, and route access where fitting, not only political power or command power.

Create clear localisation, icon-first cost text, custom trigger tooltips, dynamic scripted localisation for values, and cleanup effects for stale targets.
