# Event 015 Utopia Manifesto planning package

This package contains the source specification and implementation handoff for Event 015 `utopia_manifesto`.

The event replaces the old World Tension Subsides Event 15. It targets eligible minors and player minors, excludes majors and strong industrial powers, makes AI always accept, and gives human players an accept or refuse choice.

## Important v2 design correction

The focus tree is now specified as a deeper uneven tree. Main branches should not be implemented as five-focus lanes. The tree should build through opening institutions, domestic pillars, doctrine routes, military and diplomacy branches, late enforcement, puppet utopias, and an Ultimate Utopia convergence branch where the mature branches connect into route-colored final outcomes.

The late tree now includes external goals to export, enforce, or renounce Utopia abroad. It also includes puppet utopia subject forms such as Charter Commonwealths, Surveyor Protectorates, Necessary Wards, Daughter Commonwealths, and hidden No-Place Precincts. These subjects need visible mechanics, local values, decisions, failure states, and final fates.

## Important v3 workflow correction

The compact goal prompt now makes `chaosx_improvement_loop_planner` mandatory when the implementation goal is nearing completion. The loop must run after a meaningful implementation tranche and before the final completion audit. Its output must have a recorded disposition before completion is claimed.


## Important v4 workflow correction

The package now includes `prompts/utopia_manifesto_subagent_routing_prompt.md`. The compact goal prompt, coding prompt, and acceptance criteria point to this routing handoff. The near-completion `chaosx_improvement_loop_planner` pass must receive explicit context with `fork_context=false`, must run before the final completion audit, and must have a recorded disposition before any completion claim. If the loop subagent cannot be spawned because the tool is unavailable, that is a blocker.

## Structure

- `specs/` contains the event source design parts.
- `matrices/` contains implementation-facing design matrices.
- `prompts/` contains prompts for the implementation agent and subagents, including the subagent routing handoff.
- `research/` contains research notes and the source reading log.

## Main files

Read `specs/015_utopia_manifesto_spec_part_2_focus_tree.md` for the expanded focus tree. Read `specs/015_utopia_manifesto_spec_part_6_late_enforcement_and_puppet_utopias.md` for late enforcement and subject mechanics.

Use `prompts/utopia_manifesto_goal_prompt.md` for the compact `/goal` prompt. It is under 4000 characters.
