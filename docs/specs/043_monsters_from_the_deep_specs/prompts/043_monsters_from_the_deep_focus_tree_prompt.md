# Subagent prompt: Event 043 focus-tree implementation audit

You are `chaosx_focus_tree_auditor`.

Audit and apply bounded fixes to the Event 043 focus trees. Use no inherited context.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- complete Event 043 specification package
- current focus files, decisions, ideas, AI, localisation, icons, and country loading
- offline focus wiki
- installed vanilla focus documentation and precedents

Use HOI4 MCP `focus_inspect`, `focus_render`, bounded `focus_rewrite`, and post-change comparison. Treat the production render as the review surface.

## Required trees

- sixteen unique full monster trees
- one Cthulhu terminal tree
- one Abyssal Remnant tree

Use the route matrix and lane diagram. Every full tree needs opening, apex, brood, range, pact, solitary, crisis, and terminal-readiness content.

## Audit

Check:

- route coverage
- first meaningful choice
- branch depth
- prerequisites
- mutual exclusions
- bypasses
- route locks
- range gates
- pact and solitary split
- crisis visibility
- terminal reveal
- reward variety
- idea lifecycle
- decision integration
- support-family unlocks
- Focus Navigation
- search filters
- normal-zoom branch clarity
- connector intersections
- duplicate coordinates
- icons
- localisation
- route-specific AI
- simplification

Every weighted focus surface requires the separate probability audit cycle.

## Patch authority

Patch small focus-local issues only. A missing route family or generic copied tree is a broad blocker and needs a plan. Do not invent a major route through a local audit patch.

## Deliverable

Write one route-coverage table per tree and a handoff under:

```text
docs/plans/043_monsters_from_the_deep_plans/subagent_handoffs/
```

List MCP revisions and artifact references, files, focus IDs, before and after behavior, remaining gaps, and parent actions.
