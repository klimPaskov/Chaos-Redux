# Event 019 Focus Tree Layout Fix

## Scope

This pass changes authored focus coordinates in `common/national_focus/019_infantry_spawn_derivative_focus.txt` and synchronizes the source-bound planning metadata in `common/national_focus/019_infantry_spawn_derivative_focus.focus-plan.json`.

Focus identifiers, prerequisites, mutual exclusions, branch visibility, availability, rewards, AI weights, icons, costs, and localisation references remain unchanged.

## Layout changes

The hidden zombie and ghost derivative branches now fan outward immediately below `infantry_spawn_derivative_name_the_future_host`.

Each derivative root, its three mutually exclusive specializations, and its capstone occupy a compact branch-local stack instead of projecting long connector lines through the main focus tree.

The planning sidecar records the same preferred coordinates and the current source hash.

## Validation evidence

The HOI4 focus inspector resolves 45 focuses and 54 prerequisite connectors, matching the pre-change tree.

The final layout has zero connector crossings, zero connector-through-node intersections, and zero long connectors.

The inspector applies the source-hash-bound planning sidecar without stale-metadata diagnostics.

A semantic comparison with all authored `x` and `y` lines removed matches the pre-change source exactly.

No gameplay simplification or fallback was used.
