# Kruger State country and focus implementation prompt

Apply the binding institutional-capture, split project-family, temporal-debt, origin-conclusion, and terminal-commitment contracts from `016_source_of_truth_map.md`.

Read:

- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_5_kruger_state_country_package.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_6_kruger_state_focus_tree.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_country_package_matrix.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_focus_tree_architecture.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_ai_behavior_matrix.md`
- `docs/specs/016_brilliant_scientist_specs/acceptance/016_acceptance_criteria.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `AGENTS.md`

## Country package

Create the Kruger State only from a peaceful charter, violent laboratory rebellion, partial enclave, multi-site split, or valid host takeover.

`KRG` is a working tag. Check conflicts before registration.

Implement:

- Valid capital and territory derived from actual facility history.
- Peaceful and violent origin flags.
- Narrow core rules and staged integration.
- Direct public country names and route cosmetic identities.
- Parties, ideology, leaders, advisors, and commanders.
- Doctor Warren Kruger and route continuity variants.
- Base and route flags.
- Starting ideas with lifecycle.
- Economy, technology, production, supply, equipment, manpower, and resources.
- Conventional guard and project-derived starting forces.
- Clone, robot, dinosaur, monster, portal, temporal, exotic, and biological systems only when inherited.
- Former-host diplomacy and war.
- Foreign recognition, patronage, containment, and submission.
- Special-chaos and actual-nonhuman classification at the correct route state.
- Full AI and cleanup.

Do not release an empty or invalid tag. Do not transfer third-party controlled states. Do not destroy a small host through a peaceful charter. When a clean split is impossible, evaluate defection, confinement, non-country crisis, charter, or enclave on their own conditions. Takeover remains available only when the full institutional-capture contract was independently satisfied; it is never a fallback.

## Focus tree

Create a coherent 85 to 115 focus tree using the path architecture, not a generated reward ladder.

Required branches:

- Opening survival and formation-type handling.
- Government and human status.
- Human technocracy.
- Replicated sovereignty when cloning is valid.
- Machine ascendancy when robotics is valid.
- Temporal Continuum when time research, debt, anchor, authentication, and stabilization state support it.
- Separate paleogenetic and xenobiological openers, facilities, production, units, failures, counters, and capstones, converging only through Synthesis.
- Synthesis when several portfolios are valid.
- Laboratory economy.
- Conventional security.
- Project military branches.
- Diplomacy and intelligence.
- Expansion and postwar integration.
- Evolution IV world conquest.
- Strategic Singularity and Laboratory World as mutually exclusive commitments with verified transition locks.
- Crisis and failure branches.

Political choices must change economy, military, diplomacy, leaders, flags, laws, and integration. Project branches stay hidden or unavailable without inherited stages. Rewards should unlock decisions, missions, units, advisors, buildings, technology, facilities, claims, war goals, diplomacy, and identity. Tiny modifiers and new-idea filler are unacceptable.

Create final focus names, descriptions, coordinates, prerequisites, mutual exclusions, bypasses, filters, icons, rewards, and AI weights from the design direction. Keep player-facing text free of hidden spoilers.

## Audits

After implementation:

- Spawn `chaosx_country_package_auditor` with `fork_context=false`.
- Spawn `chaosx_focus_tree_auditor` with `fork_context=false`.

They may patch small local defects. Broad redesign becomes a plan. Each writes a handoff under `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/`.

The completion report must include a route coverage table, country-package checklist, starting-force derivation, project-branch validity proof, asset coverage, and task-specific balance observations.
