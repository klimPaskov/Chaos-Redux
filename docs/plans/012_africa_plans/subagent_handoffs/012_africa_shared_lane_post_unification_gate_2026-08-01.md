# Event 012 shared-lane reachability handoff - 2026-08-01

## Scope

The 78-row focus payoff matrix places external-continent sponsorship in the post-unification phase. The first shared-lane focus, `africa_support_sponsor_another_continent`, previously became available after constitutional commitment and a grounded origin, before Africa had completed the `africa_is_one` milestone.

## Patch

- File: `common/national_focus/012_africa_continental_focus_tree.txt`
- Focus: `africa_support_sponsor_another_continent`
- Change: added `has_global_flag = africa_is_one` to the existing `available` block.
- Downstream focuses `africa_support_choose_external_partner` and `africa_support_external_sponsorship_mandate` remain behind this focus prerequisite, so no second gate or new helper is needed.

## Behavior

Before the patch, grounded routes could select the sponsorship lane before the continental settlement. After the patch, all seven grounded route overlays retain their existing route locks and shared-lane effects, while the sponsorship lane becomes reachable only after Africa is one. No tags, models, icons, localisation, or reward effects changed.

## Validation

- Static focus scan found exactly one `africa_is_one` gate in the sponsor focus and no accidental gate in `africa_support_choose_corridor_philosophy`.
- The focus file still has 2,565 opening and 2,565 closing braces; `git diff --check` reports no whitespace error.
- The existing Event 12 focus tree has 107 route-body `africa_focus_ai_route_pressure` call sites and zero remaining flat `ai_will_do = { factor = @africa_ai_normal }` blocks.
- `hoi4_focus_inspect` and `hoi4_focus_render` were attempted before/after the patch; both returned `SCAN_BYTE_LIMIT` for this large tree, so no new artifact or parser diagnostic was available from MCP.

## Remaining limits

The patch does not add live world-order target feasibility or simulation evidence. The existing shared sponsorship effect and downstream target/action checks remain the source of truth once the post-unification lane is entered.

## Acceptance slice

| Surface | Current evidence | Disposition |
| --- | --- | --- |
| Shared opening and regional overlays | Existing Event 012 focus audit records the shared opening, nine regional overlays, host signatures, and post-formation bands in `africa_continental_focus_tree`. | No change in this tranche. |
| Seven constitutional routes | Existing route bands contain the six grounded routes plus the gated Covenant route; the prior route-AI tranche supplies 107 live-state pressure call sites. | No route locks or layout coordinates changed. |
| Shared support lanes | Thirty-six shared-lane focuses exist, and ten payoff anchors call `africa_apply_route_sensitive_support_reward`, which stores the selected constitution and applies axis-specific payoffs. | Sponsorship entry now matches the matrix post-unification phase. |
| Priority member overlay | `africa_priority_member_focus_tree` has eight focuses and sixteen package IDs; Action 102 registration and the existing loader keep package activation bounded. | No package, tag, model, or icon changes. |
| Localisation and icons | The patch adds no player-facing key or asset reference. | Existing keys and icon IDs remain unchanged. |
