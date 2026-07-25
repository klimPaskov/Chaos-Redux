# Fallout NZL fragmented-footprint transfer proof

Status: implemented as a dormant B7 allocation pilot on 2026-07-26. This is static source evidence only. Hearts of Iron IV was not launched.

## Contract

The pilot covers the reviewed New Zealand Lifeboat State footprint from the B7 successor follow-up. It can run only after the generation-bound conflict ledger and player reservation ledger are current, while the AI `NZL` tag is still unassigned, and before any successor allocation completion flag exists.

The source trigger requires all five exact states `284`, `1079`, `723`, `1080`, and `1081` to be current inventory rows and current candidate states. Each state must be owned and controlled by its AI owner, each owner must hold exactly one state, and no target state may be player reserved. The five one-state requirement makes the source set distinct and makes landless retirement deterministic after transfer. Samoa state `726` remains excluded by the existing NZL conflict contract.

## Transaction order

1. NZL records one started flag and the current transition generation.
2. Each target state saves its current owner into `global.fallout_nzl_transfer_source_countries`, records a source generation, and then runs the documented `transfer_state_to = ROOT` effect from state scope.
3. The coordinator iterates only the recorded source-country array. A source receives the `retired_landless` conflict result only after it owns no state, receives its cleanup owner and generation, clears allocation pending, and records a durable retired receipt.
4. NZL proves the exact five-state footprint and all source receipts. It records Wellington state `284` as the deterministic capital candidate and exposes a current capital receipt for the existing NZL conversion producer.
5. The established `fallout_nzl_commit_existing_tag_assignment` effect records `converted_existing`, the package layers, the assignment row, and the capital row. No dynamic country is created and no player tag switch occurs.

The transfer effect is idempotent by the started, committed, and error flags. A partial transfer cannot silently retry. If the exact footprint or any source retirement proof fails, the effect records a typed successor-allocation error and leaves the global allocation completion flags unset.

## Engine-sensitive evidence

The installed vanilla effects documentation defines `transfer_state_to` for state scope and accepts a country target. Chaos Redux precedents use both `transfer_state_to = ROOT` and scope-valued transfer targets. This pilot uses the documented state-scope form and does not use a variable-only substitute.

The source and destination checks use `fallout_successor_state_inventory_row_is_current`, `fallout_successor_state_is_candidate`, `is_controlled_by = OWNER`, and the current live conflict ledger. The post-transfer proof uses the generation-bound source array and `fallout_live_tag_conflict_resolution_is_current`. The exact ownership mutation, source-country capital cleanup, save recovery, multiplayer timing, and map rendering remain unobserved because HOI4 was not launched.

## Files

- `common/script_constants/fallout_nzl_lifeboat_constants.txt`
- `common/script_constants/fallout_successor_b7_constants.txt`
- `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt`
- `common/scripted_effects/fallout_nzl_lifeboat_effects.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`
- `common/scripted_effects/fallout_successor_b7_effects.txt`

## Boundary

This is not the general successor allocator. It does not materialize a dynamic tag, resolve a missing tag, assign a player candidate, activate the orientation scheduler, or certify the complete successor matrix. The B7 USA package still uses temporary vanilla icon references while its dedicated Fallout art is blocked. The global allocation and release-floor gates remain unset.
