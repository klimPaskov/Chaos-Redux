# NZL conflict disposition producer handoff

## Status

This handoff records a bounded implementation tranche for the dormant New Zealand Lifeboat State pilot. It does not authorize NZL activation and it does not change the Fallout release floor.

## Changed files

- `common/script_constants/fallout_nzl_lifeboat_constants.txt` adds the typed `fallout_nzl_conflict_disposition` values `none`, `samoa_state_excluded`, and `aotearoa_overlap_inactive`.
- `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt` adds the phase-bound input gate and the guarded `fallout_nzl_conflict_dispositions_can_record` trigger. It requires the current successor conflict ledger, the exact five-state NZL footprint, an excluded Samoa state 726, a current Samoa row when Samoa is live, and no unresolved Independence Wave holder of Wellington or Canterbury.
- `common/scripted_effects/fallout_nzl_lifeboat_effects.txt` adds `fallout_nzl_record_conflict_dispositions` and the separate `fallout_nzl_clear_conflict_dispositions` reset helper. The producer writes both disposition values and both transition-generation receipts in one guarded block.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md` records the engine contract and dormant caller boundary.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_SUCCESSOR_PLAYER_CONTINUATION_B7_PROOF.md`, `docs/specs/air_cleanliness_fallout_specs/specs/53_successor_allocation_player_continuation_b7.md`, `docs/plans/air_cleanliness_fallout_plans/source_of_truth_map.md`, and `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md` replace the former no-producer statement with the current dormant-producer statement.

## Idempotence and cleanup

The write trigger rejects an already current receipt pair, so an exact retry does not overwrite same-generation dispositions. The separate clear helper is intended for a future allocator reset and is not called by `fallout_nzl_reset_package_runtime`. Package runtime reset therefore cannot erase allocation receipts before activation validation.

## Static review

The producer name has one definition and zero non-documentation callers. The new script blocks have balanced braces and no unsupported `<=` or `>=` operators. The array iteration follows existing `all_of_scopes` repository syntax. Direct `SAM` country scope follows the established Independence Wave precedent. The documentation contains no em dash or semicolon.

## Remaining blockers

- No approved Fallout allocator materializer transfers states 284, 1079, 723, 1080, and 1081 to NZL.
- No live caller authenticates the transfer and invokes `fallout_nzl_record_conflict_dispositions`.
- `fallout_nzl_activate_lifeboat_package` remains defined without a caller.
- Runtime save recovery, host authority, tag collision behavior, AI plan retirement, and multiplayer behavior remain unobserved because HOI4 was not launched.
- The Radio Service Coordinator portrait remains an independent asset blocker.
