# Fallout NZL dynamic materialization proof

## Scope

This proof covers the dormant B7 New Zealand Lifeboat materializer and its rollback surface. It is a bounded successor allocation pilot. It is not a general successor allocator, a player tag switch, a release-floor event tranche, or a completion claim.

## Admission gate

`fallout_successor_b7_nzl_dynamic_materialization_can_commit` admits only a current survivor-allocation transaction with a current conflict ledger. The source country must be a non-player live conflict row with allocation pending, no known event-package ownership, and at least one owned state. The frozen candidate rows for Wellington 284, Auckland 1079, Canterbury 723, Marlborough 1080, and Otago 1081 must all be current candidates. Each state must be owned and controlled by an AI country that owns exactly one state. A live NZL tag or an existing dynamic NZL package output rejects the materializer. The guard does not treat `game:all_possible_countries` membership as a live output.

## Materialization contract

`fallout_successor_b7_materialize_dynamic_nzl` records the current source country, marks the dynamic transaction started, and calls the documented `create_dynamic_country` effect with `original_tag = NZL`, `copy_tag = NZL`, and `reserve_dynamic_country = yes`. The new country receives a Fallout-owned dynamic flag and a generation-bound source receipt. The effect transfers exactly the five reviewed states, records each former owner, and preserves the source state scope for rollback before the source retirement helper clears its ordinary transfer receipt.

The output must own and control the exact five-state package. Each former owner must be landless and carry a current `retired_landless` receipt. The output records Wellington as the capital, `created_dynamic` as the conflict result, the source and cleanup owner, assignment and package generations, maritime-remnant government, Oceania identity, and the New Zealand Lifeboat country-memory id. The output is appended once to the assigned-country array and the capital is appended once to the assigned-capital array. The reviewed Lifeboat package then loads its focus tree, characters, ideas, units, decisions, AI override, and country cosmetic identity through the existing package activation effect.

The source row links to the output through `fallout_live_tag_conflict_output_country`. The output links back through `fallout_successor_conflict_source_country`, uses the same `created_dynamic` result, and names the same cleanup owner and generation. A missing transfer receipt, disposition receipt, assignment row, or package-current receipt sets `fallout_transition_error` and prevents `fallout_b7_vertical_slice_ran` from being written.

## Cleanup contract

`fallout_successor_b7_cleanup_dynamic_nzl` is called by the successor-ledger reset. It finds only a same-generation dynamic NZL output. It retires the package runtime and current leader, returns each recorded state to its former source, restores the source controller, resets each source to allocation pending, clears capital and assignment rows, removes output package and provenance receipts, makes the output landless, and runs `reserve_dynamic_country = no`. The engine documentation exposes dynamic-country creation and reservation release, but it does not expose a destroy-country effect. The output is therefore released for documented recycling rather than claimed destroyed.

## Engine references and blockers

The implementation mirrors `effects_documentation.md` for `create_dynamic_country`, `reserve_dynamic_country`, `transfer_state_to`, and `set_state_controller_to`. Static source review proves the gates, exact state list, generation receipts, source-to-output links, rollback fields, and fail-closed error path. It does not prove dynamic-country membership in `game:all_possible_countries`, absent possible-country scope behavior, persistence of `original_tag`, immediate ownership and controller reads, save recovery, recycling timing, multiplayer country delivery, or player tag continuation. HOI4 was not launched.

The general 99-successor matrix, global allocator finalizer, scheduler activation, and player continuation handoff remain incomplete. This pilot remains outside release-floor credit.
