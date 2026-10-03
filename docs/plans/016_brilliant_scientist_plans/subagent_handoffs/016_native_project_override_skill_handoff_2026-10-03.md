# Native special-project override skill handoff

Disposition: implemented, pending parent review.
Acceptance basis: the parent explicitly requested this bounded reusable rule and this handoff, with no commit.

Changed files:

- `.agents/skills/chaos-redux-events/SKILL.md`: one additive subsection under `### 4. Handle supporting gameplay systems`, immediately before `#### Event-created country setup and audit`.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_project_override_skill_handoff_2026-10-03.md`: this report.

## Exact owned addition

The subsection starts at working-tree line 447.
The exact added hunk is below, followed by one separating blank line before the existing country-setup heading.

```diff
+#### Native special-project output overrides
+
+Do not assume duplicate native project IDs safely replace or partially merge definitions across filenames.
+For approved vanilla project output changes, use a complete replacement at the same relative vanilla file path unless the relevant engine merge behavior is proven.
+Repeating full definitions in a distinct mod filename can duplicate enable-equipment or module list entries.
+
+- Check installed native documentation, current vanilla source, and every existing mod owner of the file and project IDs before editing.
+- Retain original tuning, availability, rewards, and file-scoped constants, including other projects in the replaced file, while adding only approved owned output hooks.
+- Record vanilla source paths and SHA-256 hashes, then remove only the owned hooks from a comparison copy and verify exact remaining content against those sources.
+- Check effective source-ID uniqueness after same-path masking, including other mod files that still declare the IDs.
+
+Source equality establishes preservation only, and must not be described as engine validation.
+
```

## Evidence and limits

Read `AGENTS.md`, `chaos-redux-subagents`, the relevant `chaos-redux-events` integration sections, and the official `skill-creator` guidance.
Directly read user-supplied `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log:2-14`, which reports duplicate equipment and module entries in native special-project files.
The parent supplied the causal context: complete native project definitions with existing IDs were repeated in a distinct mod filename.
The parent is replacing that approach with masking at the original relative vanilla file paths.
The parent also reports that native content equals installed vanilla after removing approved hidden output hooks.
Those parent-reported implementation checks were not independently rerun by this skill maintainer.
Source equality demonstrates content preservation and does not establish engine behavior or post-fix live success.

Verified that removing only this addition restores the exact pre-edit skill content, preserving existing edits and line endings.
The addition contains no event IDs, event-specific paths, live-QA references, or one-off context.
No gameplay, model, image, other skill, index, or commit changes were made by this worker.
No simplifications were made in the requested skill change.
No skill-maintenance blocker remains, while parent implementation and engine acceptance remain outside this scope.

## Shared-tree isolation and parent follow-up

Unrelated unstaged hunks remain in the events skill.
The observed pre-existing hunk is the event-option audit paragraph immediately before `### 1. Classify the event first`, covering reused option identifiers, scenario schemas, `poolComplete`, `unresolved`, and eligibility assumptions.
It was preserved exactly and is not owned by this worker.
The parent must review and isolate only the native special-project subsection above and this handoff, without staging the whole skill file or disturbing other agents' edits.
No AGENTS.md or subagent-routing update is required.
Skills updated: `chaos-redux-events` only.
Skills created: none.
Other skills left unchanged, including `chaos-redux-subagents` and `skill-creator`.
