# Stage 6: Run the required improvement and completion reviews

Event: **074, Japan Lands in USA**.
Spec root: `docs/specs/074_japan_lands_in_usa_specs/`.
Working plans: `docs/plans/074_japan_lands_in_usa_plans/`.
Primary implementation contract: `docs/specs/074_japan_lands_in_usa_specs/prompts/074_japan_lands_in_usa_coding_prompt.md`.
Read that contract and the referenced design parts before starting this stage.
This card is a pending instruction, not evidence that the stage has run.

## Stage task

Before claiming the goal is near complete, spawn chaosx_improvement_loop_planner with fork_turns="none" and the exact context from the specialist task card.
Give it the implemented files, all spec paths, evidence, constraints and unresolved questions.
Resolve its accepted addendum or closure handoff across the real implementation and all affected specs, prompts, tests, assets and docs.
Then obtain chaosx_event_completion_auditor review and resolve every acceptance finding.
Do not manufacture an expansion when the coherent mechanic is already complete.
Run all applicable acceptance cases and clearly distinguish static passes from runtime evidence.
Report changed files, actual outputs, scope limits, findings and unresolved gates honestly.
Do not claim completion until the implemented files satisfy the full specification and required evidence.

## Stage handoff

Record exact changed files, source consumers read, completed acceptance cases, unexecuted tests, remaining blockers and specialist findings under the working plans path.
Use the current AGENTS.md and relevant skills, and preserve all nonnegotiables in the coding prompt.
Do not drop unmet requirements to make a stage appear complete.
This is the final planned stage. Do not produce a temporary continuation prompt inside the source package.
