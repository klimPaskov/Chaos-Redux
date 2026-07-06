# Decision and mission prompt for 011 Secret Alliance

Use `hoi4-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`. After implementation, spawn `chaosx_decision_mission_auditor` with `fork_context=false` and explicit context for Event 11.

Source specs:

- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_1_core.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_2_mechanics_and_decisions.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_decision_map.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_values_and_tuning.md`

## Implementation goals

Build an event-owned decision category for the Secret Alliance dossier. The category appears in Evolution II or earlier if the player reaches a strong Evidence state. It should not show every target at once. Use phases, suspect selection, ring visibility, and active mission caps.

Implement decision families for:

- investigations
- counter-sabotage
- diplomatic pressure
- neutral inquiry
- border watch
- controlled border incidents
- public accusation
- public confrontation and revealed-war pressure

## Cost model

Use concrete costs and requirements:

- infantry equipment
- support equipment
- trains
- convoys
- fuel
- army XP, navy XP, and air XP where relevant
- manpower commitments
- civilian factory burden
- stability or war support risk
- actual unit placement for border missions
- diplomatic relations and concessions for negotiations

Political power can support diplomatic actions, but it must not become the main cost of the system.

## Mission expectations

Timed missions should require real objectives. Use named states or named dynamic regions where possible. Include success, failure, and partial success. Avoid passive stockpile missions and avoid a second click after an objective is fulfilled.

Key missions:

- Protect the line of communication
- Guard the conference shadow
- Keep the border quiet
- Secure the officer corps

## Tooltip and localisation expectations

Use concise icon-first costs. Use custom trigger tooltips for dynamic requirements. Do not expose raw trigger blocks. If requirements are numerous, show a short requirements summary and put the full list in a tooltip.

## Cleanup

After public reveal, remove or hide hidden-phase decisions, cancel obsolete missions, clear invalid target flags, and convert the category to public confrontation and war pressure behavior.

## Audit requirements

The decision auditor should report:

- issue list by severity
- cost and requirement clarity
- active mission cap behavior
- duplicate mission risk
- AI validity
- cleanup behavior
- exploit risk
- localisation gaps
- remaining design gaps
