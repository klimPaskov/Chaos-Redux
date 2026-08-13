# Mandatory improvement-loop prompt for Event 016 Brilliant Scientist

> Superseded 2026-07-14. The planner ran and produced `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_improvement_loop_addendum.md`. Its R1 through R7 recommendations received a complete parent disposition in `016_source_of_truth_map.md`. Do not rerun this prompt until the promoted material is implemented or a new implementation finding creates a distinct depth gap.

Spawn `chaosx_improvement_loop_planner` with `fork_context=false`.

## Exact current state

The full source-spec draft is under `docs/specs/016_brilliant_scientist_specs/`. Ten spec parts, eight matrices, research notes, acceptance criteria, balance review, asset and implementation prompts, and a parent anti-bloat review are complete.

No prior Event 16 improvement addendum exists in the supplied source set. Check the live repo under `docs/plans/016_brilliant_scientist_plans/` before writing anything. Do not stack a new addendum on an unresolved one.

## Required reading

- `AGENTS.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Every file under `docs/specs/016_brilliant_scientist_specs/`
- Current Event 16 implementation and any existing Event 16 plans or handoffs

## User constraints to preserve

- Event ID 16, minor fire-once.
- Fixed name Doctor Warren Kruger.
- Accepted appointment gives a deliberate `+100%` research-speed anchor.
- AI always accepts.
- Player can send him to another country.
- He is one visible scientist identity across all special-project fields with extreme bonuses.
- Base portrait derives from `portrait_generic_biowarfare_europe_male_01`.
- Portrait and advisor or scientist art evolve, severe states animate with real per-frame source art.
- Four evolutions only.
- Project families include teleportation, cloning, time, robots, dinosaurs, monsters, biological weapons, alien arms, and a final stronger-than-thermonuclear device.
- Project history determines rebellion territory and army.
- Kruger State receives a large focus tree and Evolution IV world-conquest branch.
- The final device can trigger Fallout from any starting chaos tier only by raising chaos above the existing world-end threshold before terminal firing.
- Event remains outside clusters.
- Planning text remains direction-only, with super-event text and audio research-gated.

## Review questions

Inspect for:

- Shallow or duplicate project families.
- Missing host choices, failure states, or safe resolutions.
- Missing active or pre-fire evolution behavior.
- Weak AI, invalid route handling, or human-only GUI actions.
- Focus branches without real payoffs or postwar play.
- Country-package gaps in territory, economy, army, politics, diplomacy, or classification.
- Project forces without production and supply constraints.
- Missing visual states, static fallbacks, or asset families.
- Missing super-event thresholds or aftermath.
- Achievement redundancy.
- Hidden fallbacks or simplifications.
- Scope bloat that should be cut.

Pay special attention to:

- Whether the international-recognition super-event justifies its cost.
- Whether host takeover is a useful rare route or unnecessary duplication.
- Whether paleogenetics and xenobiological monsters are distinct enough.
- Whether the temporal branch has sufficient counterplay.
- Whether the alien-origin route should have one truth or several possible explanations.
- Whether 17 working achievements should be kept, merged, or reduced.
- Whether the singularity and Laboratory World endings feel different enough.

## Output

Return either:

1. A concrete addendum under `docs/plans/016_brilliant_scientist_plans/` with exact design changes, affected spec files, research basis, AI, assets, and acceptance criteria.

2. A closure handoff explaining why further expansion would add bloat, listing only final small design cleanup and audit work.

State whether any plan should remain in `docs/plans` or be promoted into exact files under `docs/specs/016_brilliant_scientist_specs/`.

Do not edit gameplay files. Do not claim implementation completion. The parent must disposition every recommendation before the design can be process-closed.
