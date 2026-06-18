# Event 012 High-Chaos Hidden Route Parent Handoff

## Scope

Parent-owned patch for the Event 012 main Africa focus tree high-chaos Bestiary route visibility.

## Subagent status

- Spawned `chaosx_focus_tree_auditor` with `fork_context=false`.
- Agent id: `019edb72-37f4-75c0-aa21-3ac6389fe7d8`.
- The subagent stalled during the audit window and was closed before it edited files. The parent completed and reviewed the patch.

## Files changed

- `common/national_focus/012_africa_focus.txt`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_high_chaos_hidden_route_parent_handoff.md`

## Gameplay behavior

Before this patch, the high-chaos Bestiary branch was always visible in the main Africa focus tree even though the design intent and audit follow-up called for a hidden route revealed by the Archive gate.

After this patch, `AFR_high_chaos_door` sets `africa_high_chaos_branch_revealed` and calls `mark_focus_tree_layout_dirty`. The downstream Bestiary focuses use `allow_branch = { has_country_flag = africa_high_chaos_branch_revealed }`, so the lane is hidden until the gate focus completes.

Affected focus ids:

- `AFR_high_chaos_door`
- `AFR_forest_parliament`
- `AFR_archive_bestiary_clause`
- `AFR_no_seats_for_caricature`
- `AFR_first_nonhuman_envoys`
- `AFR_habitat_trust_board`
- `AFR_omen_reliability_office`
- `AFR_treaty_of_teeth_and_roots`
- `AFR_court_of_thunder_and_tides`
- `AFR_spider_at_the_signature_table`
- `AFR_world_root_mandate`

## Validation

The final parent validation checked the reveal flag call sites, vanilla support for `mark_focus_tree_layout_dirty` as a country-scoped effect, and the touched focus tree syntax around the edited branch.

## Remaining risks

This closes the narrow visible-hidden mismatch for the Bestiary focus lane only. It does not claim full Event 012 focus-tree completion or close the broader audit findings around country-package depth, historical dossier mission depth, Continental Congress GUI depth, targeted scenario validation, or super-event/audio source blockers.
