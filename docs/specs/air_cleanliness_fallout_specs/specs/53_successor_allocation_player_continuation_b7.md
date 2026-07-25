# Fallout successor allocation and player continuation B7

## Purpose

This tranche proves a bounded transition slice after state grading and physical collapse. It preserves one North American human continuity case in place, applies a country-specific Fallout package, records its frozen capital, and exposes one deterministic fragmentation candidate without inventing a tag.

## Continuity case

The continuity case is the United States under the federal continuity memory. It is eligible only when the USA is the snapshotted human country, its continuation branch is `surviving_tag`, its frozen primary target is the USA, and the reserved primary capital remains hostable and owned and controlled by the USA.

The package writes current-generation country, focus, archetype, regional, government, and country-memory receipts. It loads `fallout_usa_federal_continuity_focus_tree`, adds the federal continuity idea, and records an explicit current-generation human-control receipt while USA remains human controlled. The focus layer has shelter, supply, guard, bilateral, radio, and reconstruction routes with authored USA-specific text.

Focus costs use centralized engine weeks of `5`, `10`, and `15`, which provide 35-day, 70-day, and 105-day pacing bands.

The assignment row uses the reserved capital as both origin and capital. The row writes the player-reserved conflict resolution, source country, output country, cleanup owner, generation, assignment count, and state receipt. Existing ownership is retained. No tag switch occurs in this case.

## Fragmentation case

For a snapshotted human source that requires a successor choice, the probe scans the frozen `game:all_possible_countries` inventory after the live conflict ledger exists. It rejects live tags, special-package ownership, already committed assignments, dynamic materialization receipts, and releasable-release receipts. It then chooses the lowest country id and the lowest id state from the frozen candidate-state array.

The probe exposes a named country and state to the player-continuation ledger. It does not release, create, transfer, or rename anything. It records an explicit blocked status when either pool is empty. There is no generic successor fallback.

The next package-aware candidate is NZL, the New Zealand Lifeboat State. Its loader requires the exact states 284, 1079, 723, 1080, and 1081, excludes state 726, permits capital 284 or 1079, and requires current-generation assignment identity plus Samoa and Aotearoa conflict-disposition receipts. B7 now supplies one guarded existing-tag producer. It can resolve `converted_existing`, commit one exact capital and origin row, record both dispositions, and call the existing package loader only when an AI NZL tag already owns and controls the exact footprint. It does not create a missing tag or transfer a fragmented footprint. The general allocator and missing-tag path remain blocked.

## Coordinator and idempotence

`fallout_successor_b7_run_vertical_slice` is the only B7 entry point. It is dormant and is not called by an on action, decision, ordinary event, scheduler activation flag, or public scenario. It first repairs the player reservation and conflict inventory prerequisites, begins the existing successor transaction once, applies the USA receipt, assigns the continuity row, probes fragmentation sources, and then attempts the fail-closed NZL existing-tag path. A current generation marker makes repeated calls no-ops.

B7 never writes `fallout_successor_assignment_ledger_built`, `fallout_successor_allocation_complete`, `fallout_player_continuation_commit_complete`, or `fallout_transition_complete`. The full successor matrix therefore remains blocked until every surviving landholder has a current country, focus, archetype, regional, memory, government, capital, ownership, controller, diplomacy, AI, and cleanup receipt.

## Engine-sensitive surfaces

The static implementation mirrors the documented `fallout_begin_successor_allocation_transaction` contract, `for_each_scope_loop` array iteration, `set_state_flag`, scope-valued variables, `load_focus_tree`, and capital-scoped building effects. The exact transition caller, host authority, save recovery, multiplayer timing, state-owner mutation, and human-control receipt remain unproven because the game is not launched.

## Assets and localisation

The pilot uses vanilla focus and idea icon sprites as a temporary reviewed pilot surface. Dedicated USA Fallout focus and idea art is still required before this package can satisfy the final asset contract. The required sprite names and target paths are recorded in `docs/assets/fallout_successor_b7_usa/manifest.md`. The localisation is concrete, region-aware, and government-aware. No zombie-owned path, id, sprite, audio, or asset is reused.

The final icon handoff must place seven focus sprites under `gfx/interface/goals/fallout_successor_b7_usa/` and register them in `interface/fallout_successor_b7_usa.gfx` as `GFX_goal_fallout_usa_federal_continuity_ledger`, `GFX_goal_fallout_usa_shelter_registry`, `GFX_goal_fallout_usa_supply_corridors`, `GFX_goal_fallout_usa_guard_compacts`, `GFX_goal_fallout_usa_bilateral_reconstruction`, `GFX_goal_fallout_usa_continental_radio_net`, and `GFX_goal_fallout_usa_federal_reconstruction`. The idea package needs four dedicated `GFX_idea_fallout_usa_*` sprites in the same GFX handoff. The current pilot intentionally records this asset gap instead of presenting vanilla sprites as final Fallout art.

## Follow-up

The next tranche must add a general allocator materializer for a missing or fragmented reviewed successor, prove exact state transfer and player candidate assignment, and record tag-conflict cleanup for every changed owner. The existing-tag NZL path is intentionally narrower. The global allocator must remain fail-closed until that path and the remaining successor matrix are complete.
