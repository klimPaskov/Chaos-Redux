# Conditional Subagent Prompt: Event 021 Focus-Tree Auditor

Use this prompt only when Event 021 implementation changes focus files, focus-tree loading, focus availability, route locks, or Event 006 focus assignment.

Spawn `chaosx_focus_tree_auditor` with `fork_context=false`.

Read:

- repository `AGENTS.md`
- `chaos-redux-focus-trees`
- full Event 021 source-spec folder
- affected focus files
- Event 006 focus-tree contracts
- ordinary claimant and Event 006 origin rules

Use mandatory `hoi4.focus_inspect` and `hoi4.focus_render` evidence.

Audit:

- ordinary claimants preserve meaningful existing trees
- no generic Event 021 tree replaces an existing country tree
- Event 006 actors load their package tree only when Event 021 created the package
- completed one-time rewards cannot be collected by both sides
- dead-leader and missing-state routes are blocked
- route validity follows ideology, origin, state, and package conditions
- search filters remain accurate
- Focus Navigation remains valid
- layout is unchanged unless a real focus change requires it
- no focus inlay window is introduced
- no new full route family is invented
- AI cannot choose impossible routes
- settlement and winner transitions leave a playable tree

Patch only small, safe focus-loading, prerequisite, bypass, filter, AI, icon, localisation, or reward-duplication issues.

Write:

`docs/plans/021_random_civil_war_plans/subagent_handoffs/focus_tree_auditor_handoff.md`
