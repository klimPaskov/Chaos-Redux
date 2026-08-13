# Scripted-system architecture prompt for Event 016 Brilliant Scientist

Spawn `chaosx_scripted_system_architect` with `fork_context=false`.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`
- `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_resume_packet.md`
- All Event 16 source specs and matrices under `docs/specs/016_brilliant_scientist_specs/`
- Existing Chaos Redux dynamic effects, triggers, constants, event-log helpers, world-threat helpers, special-project helpers, character patterns, and selected-target decision patterns

## Architecture goal

Design and, where narrow and safe, implement reusable Event 16 helpers before the parent duplicates logic across events, decisions, focuses, country setup, GUI, and evolutions.

This is the exact next implementation-preparation step. Freeze contracts first. Preserve exactly seventeen achievements and six mapped super-event roles. Treat R2, R3, R4, R5, and R7 as binding and R1 and R6 as rejected.

Event 016 uses world-end scenario IDs 11 and 12. Its fixed visible super-event IDs are 90 recognition, 91 formation, 92 global threat, 93 Laboratory World, 94 Strategic Singularity, and 95 qualifying defeat. Live Event 015 wiring occupies visible IDs 85 through 89. Event 020 separately declares world-end ID 10 and visible IDs 85 through 87 in its own constants, which is an external overlap with Event 015 rather than an Event 016 reservation constraint. Re-scan before any live shared-registry edit.

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
- Calculate visible Project Capacity.
- Derive broad Government Control status.
- Derive hidden Independent Capacity without exposing its exact value.
- Track Grievance.

Mandate, Dependence, Exposure, and Project Capacity are visible. Only Independent Capacity and Grievance remain hidden causal state.

### Facility and project lifecycle

- Select and validate primary and secondary laboratory states.
- Register facility type and ownership.
- Clean invalid state targets.
- Read project stages.
- Advance, suspend, damage, dismantle, publish, steal, and inherit project stages.
- Calculate project costs, accident pressure, foreign interest, and rebellion contribution.
- Keep paleogenetic and xenobiological stage, facility, production, supply, failure, and countermeasure state separate until an explicit Synthesis convergence.

### Institutional capture

- Evaluate takeover only from permitted sovereign science, extreme Dependence, compromised Control, several warned incidents, several independent captured national domains, and at least one state-wide domain.
- Never grant takeover because territory is invalid, the host is small, or country creation is inconvenient.
- Preserve a distinct `origin_takeover` consolidation state without creating a duplicate portfolio or focus tree.

### Temporal debt and evidence

- Spend synchronization capacity and add temporal debt for every meaningful temporal action.
- Bind each action to a named crisis, project component, leader, or bounded unit package and record per-target use.
- Prevent passive debt decay. Stabilization lowers debt while disabling actions, occupying the facility, and exposing a weakness window.
- Track persistent scars, evidence, authentication, anchor discovery and loss, ledger capture, and linked-action blocking.

### Origin conclusions

- Lock at most one of extraterrestrial provenance, temporal displacement, manufactured continuity, or unresolved origin.
- Gate public proof on independent evidence. Transformation alone cannot set extraterrestrial provenance.

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
- Enforce the mutual commitment lock between Laboratory World and Strategic Singularity, including verified disarmament before Laboratory World consolidation and permanent cancellation after either terminal firing.
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
