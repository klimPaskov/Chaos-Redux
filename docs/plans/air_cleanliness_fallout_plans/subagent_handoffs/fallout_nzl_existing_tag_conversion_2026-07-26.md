# Fallout NZL existing-tag conversion handoff

Date: 2026-07-26

## Scope

This tranche adds a B7-only existing-tag successor path for the New Zealand Lifeboat State. It does not create a tag, transfer a state, switch a player, set the global allocation completion flag, enable the Fallout scheduler, or add a public caller.

## Changed files

- `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt`
- `common/scripted_effects/fallout_nzl_lifeboat_effects.txt`
- `common/scripted_effects/fallout_successor_b7_effects.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_SUCCESSOR_PLAYER_CONTINUATION_B7_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md`
- `docs/plans/air_cleanliness_fallout_plans/source_of_truth_map.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/53_successor_allocation_player_continuation_b7.md`

## Static contract

`fallout_nzl_existing_tag_conversion_can_commit` requires an AI NZL tag with no known live event-package ownership, a current preallocation inventory and conflict ledger, a pending live conflict row, no prior conversion or assignment receipt, exact ownership and control of states 284, 1079, 723, 1080, and 1081, no player-reserved owned state, exclusion of state 726, one valid Wellington or Auckland capital row, and current Samoa and Aotearoa disposition inputs.

The producer first records both typed conflict dispositions. It then writes one `converted_existing` conflict result, one cleanup owner, one current-generation assignment row, one exact capital row, the five package receipts, and the NZL region, memory, and maritime-remnant government identity. Duplicate country and capital array entries are rejected before append. The existing NZL package activation effect is called only after `fallout_nzl_existing_tag_conversion_is_current` passes.

The allocation reset clears the NZL disposition receipts through the dedicated helper. The B7 vertical slice remains the only caller and remains dormant.

## Validation and blockers

Targeted script brace counts are balanced for all three gameplay files. No unsupported `<=` or `>=` operators were introduced. The producer, caller, and trigger names each have one definition. Static proof does not establish native tag creation, state transfer, player control, save reconstruction, multiplayer ordering, alternate AI-plan retirement, or a live transition caller. No HOI4 run was performed.
