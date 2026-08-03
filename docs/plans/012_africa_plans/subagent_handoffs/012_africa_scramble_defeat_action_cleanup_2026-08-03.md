# Event 012 Scramble defeat action cleanup handoff

## Finding

Actions 77-84 were structurally implemented but their category and selectors used only `africa_is_one`, while every action validator required `africa_scramble_response_active`. After a Scramble intervention defeat cleared the active response, the stale Scramble family and quote could leave a dead late-action surface visible or selected.

## Changes

- `common/decisions/categories/012_africa_categories.txt` now requires `africa_scramble_response_active` for the Scramble action category.
- `common/scripted_effects/012_africa_world_order_effects.txt` clears response phase flags, resets the action family to post-unification, clears the selected action and quote, and clears state-selection context when the host records defeat.
- `common/on_actions/012_africa_world_order_on_actions.txt` mirrors the same reset in the fallback intervention-loss callback.
- `docs/events/012_africa/overview.md` records the lifecycle contract and the controlled scope.

## Validation

Focused Event 012 lint was rerun at current head with zero blocking diagnostics; the workspace-wide helper/lifecycle pass remains deferred by the inspector. Touched Clausewitz files have balanced braces and clean diff checks.

## Boundaries

No tags, country definitions, portraits, models, external packages, or world-order gates were added. No new action store was introduced; the existing quote and action-context kernels remain the sole owner.
