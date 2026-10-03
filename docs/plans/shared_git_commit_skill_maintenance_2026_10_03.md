# Shared Git Commit Skill Maintenance

Disposition: `implemented` within the parent's bounded maintenance request, including its explicit wait/retry and provably stale lock clarification.
Changed files: [shared-commit skill](../../.agents/skills/chaos-redux-shared-git-commit/SKILL.md) and this generic handoff.
The skill preserves blank-context prefix spaces, rejects hunk `trimEnd()`, separates stderr warnings from patch content, and distinguishes fully owned new-path staged restore from mixed missing-entry `update-index --add --cacheinfo` reconciliation.
Lock recovery requires confirming no Git process, waiting/retrying, and rechecking lock identity and age before considering removal of a provably stale lock; an active actor's lock is protected.
Review evidence: installed Git `2.54.0.windows.1` output from `git update-index -h` confirms `--[no-]add` means “do not ignore new files” and lists `--cacheinfo <mode>,<object>,<path>`; its usage response exits 1.
The official `skill-creator/scripts/quick_validate.py` returned `Skill is valid!`; the scoped diff retains the existing HEAD/index capture and recheck, compare-and-swap guard, and mode/binary preservation without duplicating them.
Used skills: `skill-creator`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`; only the shared-commit skill was updated, with no new skill or routing change required.
No commit, index/ref mutation, lock deletion, cleanup, gameplay, asset, workbook, other-skill, or external-tool edit was performed; no mutation-based Git workflow test was run under this scope.
Blockers, omissions, and simplifications: none for this maintenance handoff; concurrent repository state is not frozen, so the parent retains the skill's required rechecks and owns final review and shared-tree commit.
