# Scripted-system architecture prompt for Event 016 Brilliant Scientist

Spawn `chaosx_scripted_system_architect` with `fork_context=false`.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- All Event 16 source specs and matrices under `docs/specs/016_brilliant_scientist_specs/`
- Existing Chaos Redux dynamic effects, triggers, constants, event-log helpers, world-threat helpers, special-project helpers, character patterns, and selected-target decision patterns

## Architecture goal

Design and, where narrow and safe, implement reusable Event 16 helpers before the parent duplicates logic across events, decisions, focuses, country setup, GUI, and evolutions.

## Required helper families

### Character and ownership

- Recruit or transfer Doctor Warren Kruger.
- Synchronize advisor, scientist, portrait stage, host, recipient, and breakaway state.
- Remove old-host access without duplicating the character.
- Resolve clone, machine, temporal, injury, confinement, death, and sovereign continuity.

### Host values

- Calculate and change Scientific Mandate.
- Calculate and change Institutional Dependence.
- Calculate and change Security Exposure.
- Calculate project capacity.
- Derive broad Government Control status.
- Derive hidden Independent Capacity without exposing its exact value.
- Track Grievance.

### Facility and project lifecycle

- Select and validate primary and secondary laboratory states.
- Register facility type and ownership.
- Clean invalid state targets.
- Read project stages.
- Advance, suspend, damage, dismantle, publish, steal, and inherit project stages.
- Calculate project costs, accident pressure, foreign interest, and rebellion contribution.

### Evolution and logging

- Prepare active and pre-fire evolution context.
- Set actor safely.
- Respect disabled evolutions before setting recorded or unlock flags.
- Record all four evolution stages through shared event-log helpers.

### Foreign targets

- Build valid interest pools.
- Select and clear human target state.
- Validate invitation, theft, sabotage, extraction, assassination, joint laboratory, and protection actions.
- Clean dead and invalid actors.

### Country formation

- Score and assemble valid laboratory territory.
- Protect host viability.
- Derive starting forces from project history.
- Apply peaceful, violent, enclave, multi-site, or takeover origin.
- Register special-chaos and route-specific nonhuman classification.

### World threat and terminal logic

- Refresh a Kruger-specific source inside the shared world-threat framework.
- Calculate singularity component and arming state.
- On valid terminal firing, calculate the chaos deficit to above 1000, add it through a documented source, then call the existing world-end pipeline.
- Clean all Event 16 missions, targets, and active categories after world end.

## Constants and tuning

Create a documented tuning plan for:

- Value thresholds and status bands.
- Project capacity and stage costs.
- Evolution MTTH factors.
- Foreign-interest thresholds and AI weights.
- Facility scores and territory bands.
- Starting-force scaling.
- Force-production caps.
- Accident severity.
- Singularity research and construction duration.
- Surrender threshold and terminal activation.

Use script constants where supported and file-scoped literals or meta logic only where required. Avoid scattered magic numbers.

## Handoff

Return:

- Helper map with exact names, scopes, inputs, outputs, side effects, and call sites.
- Constants table.
- Event-target and cleanup plan.
- Migration plan from repeated logic.
- Unsupported engine surfaces and risks.
- Files changed if narrow helpers were implemented.
- Documentation added.
- Task-specific validation.

Write the handoff under `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/`. Do not redesign the event. Large system changes remain plans for the parent.
