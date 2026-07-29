# Event 12 Focus Loader Preservation Patch

## Scope

This patch hardens Event 12 focus-tree replacement without changing the authored continental routes, regional overlays, constitutional branches, or reviewed world-package gates.

## Gameplay changes

- `africa_load_continental_focus_tree` remains the canonical continental loader and preserves completed-focus history when replacing an approved tree.
- `africa_focus_route_ensure_continental_tree_loaded` delegates to the canonical loader instead of maintaining a second copy of its one-shot, flag, and layout-refresh contract.
- The six reviewed external-continent package loaders preserve completed-focus history when their implementation-readiness gates eventually open.
- Host, priority-package, and world-package replacement restrictions remain unchanged. A meaningful existing national tree is not replaced unless its package carries the appropriate explicit approval.

## Changed files and identifiers

- `common/scripted_effects/012_africa_effects.txt`
  - `africa_load_continental_focus_tree`
- `common/scripted_effects/012_africa_focus_route_effects.txt`
  - `africa_focus_route_ensure_continental_tree_loaded`
- `common/scripted_effects/012_africa_world_order_effects.txt`
  - `africa_world_install_current_package`
- `docs/events/012_africa/overview.md`
- `docs/events/012_africa/charter_autonomy_and_focus_ai.md`
- `docs/events/012_africa/world_order.md`

## Validation evidence

- All eight Event 12 `load_focus_tree` call sites preserve completed-focus history.
- The continental route compatibility helper has no independent tree-replacement implementation.
- `africa_continental_focus_tree` remains inspectable with 276 active focuses and its existing icon and localisation references.
- The existing layout inspection reports 570 blocking diagnostics and 1,028 intersections because mutually exclusive regional and constitutional overlays deliberately reuse coordinates. This patch does not treat that structural explanation as runtime acceptance evidence and does not flatten the authored overlays.

## Remaining risks

- Runtime overlay visibility and focus-layout interaction still require live consumer acceptance by the user.
- The six external-continent trees remain dormant until their unique packages and implementation-readiness reviews are complete.
- No model-dependent focus, unit, or entity consumer was enabled.
