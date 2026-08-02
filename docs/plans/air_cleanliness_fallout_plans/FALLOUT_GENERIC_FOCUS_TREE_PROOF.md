# Fallout generic focus tree proof

Date: 2026-08-02

The current runtime source is `common/national_focus/fallout_consolidated_focus.txt`. It contains one tree named `fallout_generic_focus_tree` with thirty-two authored focuses. The tree has zero country weight and is loaded only by `fallout_generic_focus_activate` in `common/scripted_effects/fallout_consolidated_effects.txt`.

## Loader and generation proof

The successful map-return branch sets `fallout_active` after `fallout_apply_fracture_contract`. It then iterates `every_country` once and calls the activation helper. The helper gates on `fallout_generic_focus_tree_loaded` and the current `global.fallout_transition_generation`, loads the tree with `keep_completed = no`, calls `mark_focus_tree_layout_dirty`, and initializes the shared values. The call is therefore repeat-safe for the generation and reaches the dynamic countries created by the fracture pass.

## Route coverage

| Layer | Implemented surface |
| --- | --- |
| Opening | Survivor count, ruin survey, capital security |
| Government choice | Civic Compact, Ration Congress, Command Directorate, Shelter Council |
| Recovery | Power grid, rail spine, workshops |
| Military | Survivor Guard, Frontier Columns, Cordon |
| Diplomacy | Radio net, Frontier Pact faction, neighbour invitations |
| Border pressure | Adjacent claims, state-owner ultimatum, border settlement |
| Regions | Nine region-gated lanes using `fallout_region_id` |
| Late order | Survivor federation, heartland reclamation, Year Ten Order |

## Static audit

- Thirty-two focus nodes are present under the generic tree and all ids are unique across `common/national_focus`.
- Every focus has an icon, a cost, an AI weight, and a localisation title and description.
- Every political route is mutually exclusive and converges through `fallout_generic_publish_survival_charter`.
- Every regional lane has an explicit `allow_branch` check against one of the nine Fallout region constants.
- Shared authority, cohesion, frontier pressure, regional influence, memory, and route variables are initialized and clamped by scripted effects.
- The focus, scripted effect, constant, and opinion-modifier files are brace-balanced. No generic source file remains outside the consolidated Fallout loaders.
- Static search finds the generic tree as the only active `load_focus_tree` target in the consolidated Fallout effects. The retained NZL and USA package tree definitions have no active loader.

The focus MCP was attempted against the consolidated focus source, but the installed workspace returned `SCAN_BYTE_LIMIT` before reading a file. This proof records the limitation rather than claiming a render or live focus inspection. No Hearts of Iron IV execution was performed.

## Scope boundary

This tranche intentionally does not add bespoke country trees. Country-memory, archetype, and regional overlays remain future expansion surfaces. The shared tree is the complete universal post-Fallout play surface requested for this goal.
