# Event005 Parent Tranche: Breakaway Neighbor Wars

## Scope

Urgent playability follow-up for Soviet Collapse breakaway aggression. This tranche does not touch flags, focus layouts, localisation, or assets.

## Changed Files

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `docs/events/005_soviet_collapse.md`

## Implementation

- `soviet_collapse_apply_breakaway_neighbor_conflict_plan` now applies to any Soviet Collapse breakaway country, not only high-chaos, terminal, or tier-3+ contexts.
- Non-allied neighboring breakaways now receive claims, conquer/antagonize AI strategy, and annexation war goals when direct war is not appropriate.
- Terminal collapse, terminal-collapse setup, and standalone triggerable scenario launches now escalate neighboring breakaway conflicts into immediate wars.
- High-chaos successors keep immediate neighbor-war behavior through the same helper.
- The event overview now documents that breakaway setup creates local rivalries, while terminal/triggerable collapse and high-chaos setup can turn them into direct wars.

## Validation

- Brace-balance check passed for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
- `git diff --name-only -- gfx/flags interface/flags` returned no files.

## Remaining Risks

- Broad focus-tree completion is still not proven. Existing audits still cite pathline risks and helper-heavy rewards.
- The selected-breakaway empty intervention panel bug still needs a dynamic targeted-decision audit/fix.
- Evolution detail parity with the spreadsheet is still not proven by this tranche.
