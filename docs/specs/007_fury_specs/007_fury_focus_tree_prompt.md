# Focus Tree Prompt for Event 007 Fury

Implement the Fury shared focus tree or additive runtime branch according to:

- docs/specs/007_fury_specs/007_fury_focus_tree_spec.md
- docs/specs/007_fury_specs/007_fury_spec.md
- AGENTS.md
- hoi4-focus-trees
- chaos-redux-events
- chaos-redux-event-assets

The focus tree must be loaded only for countries marked by Event 007 as Fury. Do not blindly replace existing country trees.

Required route families:

- Opening trunk.
- General Staff Dictate.
- March Administration.
- Military improvisation.
- Captured industry.
- Occupation administration.
- Expansion loop.
- Evolution I branch.
- Evolution II branch.
- Evolution III branch.
- No-neighbor branch.
- World-end branch.

Rules:

- The tree must not be one vertical checklist.
- Rewards must not be repeated flat modifiers or generic equipment dumps.
- Unit rewards must represent institutions, templates, depots, reserves, or route-specific formations.
- Focuses must unlock or modify decisions, missions, target selection, unit templates, ideas, values, cooperation, coring, or world-end behavior.
- Route-specific AI behavior must exist.
- Every focus needs localisation, icon, completion reward, bypass or availability where needed, and AI weights.
- Provide focus filters or search categories where the repo supports them.

Completion report must include a route coverage table and list any merged, simplified, missing, or fallback route.
