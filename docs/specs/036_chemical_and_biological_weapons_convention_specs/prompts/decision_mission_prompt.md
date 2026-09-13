# Decision and mission implementation prompt

Implement the complete Event 036 decision and mission system from `09_decisions_missions_costs_and_visibility.md` and the treaty, posture, evolution, and project specs.

Before editing, read:

- `AGENTS.md`
- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- the offline decision, trigger, effect, localisation, scope, modifier, and data-structure wiki pages
- current vanilla decision documentation and precedents
- existing Chaos Redux selected-target, dynamic-cost, CBRN, inspection, and project decision patterns

Use one phased ordinary decision category with a static category picture and compact status header.

Do not create a separate scripted GUI unless normal decisions are proven unable to present the accepted public state and a later accepted plan authorizes the change.

## Public state

Show only:

- National Posture
- Convention Standing
- Current Agenda or active project progress

Keep hidden voting weights, source multipliers, candidate arrays, internal project points, and AI calculations out of player-facing text.

## Phase rules

Implement posture management, conference influence, treaty implementation, and project contribution as state-based replacement phases.

Expose three to five primary actions in a normal phase and never more than six.

Keep one to three active missions.

Hide obsolete and invalid decisions immediately.

Use selected-target or bounded target pools for country-targeted diplomacy.

AI must see valid targets without depending on the human target selector.

## Costs

Use no more than four spendable cost types on one action.

Use political power for public diplomacy, civilian factories for industrial and facility commitments, support equipment for protection and inspections, convoys and trains for international movement, fuel for transport-intensive work, manpower for staff and security, experience for doctrine, and temporary research burden for scientific commitments.

Keep command power conservative.

Scale costs from documented factors and centralize tuning.

Use icon-first cost localisation and concise blocked tooltips.

## Missions

Implement the full mission catalog with dynamic durations inside the specified bands.

Success and failure must have distinct logic.

Contribution missions apply costs and progress once.

Withdrawal cannot erase prior obligations.

Inspection success reveals only valid evidence.

Guarantee missions require a valid victim action record.

Doctrine integration requires real capability and readiness.

## AI and probability

Route every decision AI weight and target score through the baseline audit, owner patch, and `hoi4.probability_compare` cycle with `chaosx_ai_probability_auditor`.

Use the named scenarios in `matrices/ai_probability_scenarios.md`.

Hard invalidity gates must remain zero regardless of positive strategy factors.

## Audit and handoff

After implementation, run `chaosx_decision_mission_auditor` with a complete context-free prompt.

The audit must cover visibility, mission capacity, costs, tooltips, target cleanup, AI validity, balance, duplicate actions, posture cycling, contribution duplication, withdrawal exploits, evidence duplication, and save persistence.

Apply bounded fixes, write the required subagent handoff, and rerun meaningful scenarios.

Do not present the category as complete while it is cluttered, passive, exploitable, or missing AI-equivalent behavior.
