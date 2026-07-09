# Mengele improvement-loop prompt

Spawn `chaosx_improvement_loop_planner` with `fork_context=false` after the main implementation tranche and before final completion.

Explicit inputs for the planner:

- User goal: finish the Mengele super-event, inspect connected events, test the path, and keep improving until the chain is complete.
- Current source files: `germany_mengele.md`, `genocide_crisis_system.md`, and `genocide_mechanics_spec.md`.
- Package files: `specs/mengele_path_completion_spec.md`, `specs/current_implementation_map.md`, and `specs/mengele_improvement_loop_addendum.md`.
- Current implementation status from the main agent, including files changed and tests run.
- Any existing `docs/plans/*mengele*` addenda and their dispositions.

Planner task:

- Decide whether additional expansion improves play or would add bloat.
- If improvement is needed, write a concrete addendum under the discovered plans folder.
- If the chain is clean enough, write a closure handoff listing only final polish, validation, asset verification, docs, spreadsheet, and audit tasks.
- Do not create a second expansion addendum while an earlier one is unresolved.
- Do not add graphic atrocity content, celebratory framing, or random extra branches.

The main agent must resolve the planner output before claiming completion.
