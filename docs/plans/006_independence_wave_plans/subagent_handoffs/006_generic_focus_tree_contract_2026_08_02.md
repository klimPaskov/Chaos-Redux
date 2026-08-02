# Event 006 generic focus-tree contract

Date: 2026-08-02

## User decision

The current Event 006 scope uses one generic Independence Wave focus tree for every country released by Event 006. Bespoke country focus trees and live/in-game testing are out of scope for this pass. This later decision supersedes the earlier planning wording that described a different full tree assembled for each country.

## Implementation

- `common/national_focus/006_independence_wave_focus.txt` is the single generic tree, `independence_wave_focus_tree`.
- The tree contains the shared survival, government, economy, military, diplomacy/host, regional expansion, network/league, formable, and high-chaos lanes. Regional and researched package modules are gated shared-focus nodes inside this tree; no Event 006 package loads a second country tree.
- `common/scripted_effects/006_independence_wave_focus_effects.txt` publishes `independence_wave_generic_focus_tree_assigned` for full assignments and `independence_wave_generic_focus_overlay_assigned` for reviewed carrier overlays. Cleanup clears both flags with the other generation-scoped focus state.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt` exposes `has_independence_wave_generic_focus_contract`. Full assignments must still own `independence_wave_focus_tree`; additive assignments must still prove a registered owning carrier.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` applies the shared final validation barrier. A package adapter that reports success without the full tree or a reviewed additive carrier is converted to failure before release commit.
- The implementation-facing explanation and lane matrix are in `docs/events/006_independence_wave/systems/generic_focus_tree.md`.

## Validation boundary

The allocator audit still passes the approved 6/8/10/14/20 ladder, World Collapse 20, crisis gates, anchor-first planner, and Event 005-first joint ordering. The current HOI4 focus inspection remains byte-limited (`SCAN_BYTE_LIMIT`), so no live or in-game claim is made. The focus-tree auditor is the required follow-up for branch geometry, icon/localisation coverage, and the new assignment barrier.

## Remaining scope

This contract does not admit unresearched country packages, add new portraits or advisor icons, or waive the existing source/asset/formable/super-event blockers. Those remain governed by the current v97 whole-event authority. Bespoke package focus modules remain dormant or gated compatibility surfaces for later work; no new bespoke tree is added here.
