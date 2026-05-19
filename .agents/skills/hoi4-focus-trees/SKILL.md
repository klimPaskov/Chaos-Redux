---
name: hoi4-focus-trees
description: Use when editing Hearts of Iron IV national focus trees, especially Event 005 republic or successor trees, focus prerequisite links, mutually exclusive branches, layout coordinates, or focus-tree validation.
---

# HOI4 Focus Trees

## Required Checks

- Read the offline Paradox wiki National focus modding page and the repo `AGENTS.md` guidance before editing focus files.
- Use vanilla focus files as syntax precedent when changing prerequisite or mutual-exclusion structure.
- Run the Event 005 verifier after focus edits when touching Event 005 focus files:
  `python3 .tools/verify_event005_completion_gate.py --allow-missing-continuation-spec`

## Prerequisite Semantics

HOI4 focus prerequisites are easy to invert:

- `prerequisite = { focus = a focus = b }` means `a OR b`.
- Separate prerequisite blocks mean AND:
  ```
  prerequisite = { focus = a }
  prerequisite = { focus = b }
  ```

For Event 005 republic convergence or crosslink focuses, use separate prerequisite blocks for each required parent. Keep same-block multi-focus prerequisites only when the design intentionally allows alternative parents.

## Layout Rules

- Keep prerequisite parents above their children; otherwise HOI4 can draw broken turn sprites.
- Validate zero crossing prerequisite lines, no isolated focus components, no duplicate coordinates, and comfortable spacing for mutually exclusive choices.
- If an `available = { has_completed_focus = ... }` condition gates a focus, decide whether it should also be a visible prerequisite. Do not add a visible prerequisite if it creates crossing lines; instead move the branch or redesign the gate.
