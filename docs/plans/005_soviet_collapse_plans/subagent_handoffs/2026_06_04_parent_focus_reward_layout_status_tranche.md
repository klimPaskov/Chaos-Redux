# Event005 Soviet Collapse Focus Reward/Layout Status Tranche

Date: 2026-06-04

## Scope

This tranche addressed the current blocker preventing a completion claim: Soviet Collapse focus rewards still contained repeated high-chaos helper payloads and several visible focus-choice rows remained pathline-prone.

No flag files, `.tga` files, flag sprites, flag `.gfx` files, or visual flag assets were edited.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_062603_event005_focus_reward_high_chaos_payload_patch_handoff.md`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_parent_focus_reward_layout_status_tranche.md`

## Implemented Changes

- Accepted Curie's helper-level patch that gates the shared high-chaos focus payload behind persistent country flags:
	- `soviet_collapse_high_chaos_focus_payload_granted`
	- `soviet_collapse_high_chaos_focus_identity_payload_granted`
- Kept high-chaos countries dangerous while preventing repeated focus completions from granting the same broad assault/claims/neighbor-war package over and over.
- Trimmed duplicate helper calls from `PRA_the_pale_line_endures`; the endgame effect already carries the railway authority and corridor-network payload.
- Recentered the generic breakaway route-choice row so the foreign liaison focus no longer sits down inside another route.
- Recentered the Baltic legal/league/foreign/military route-choice row around its route parent.
- Tightened the CFR governance and strategy choice rows so mutually exclusive choices are compact and less likely to draw long overlapping pathlines across the tree.

## Validation

- Brace balance checked on touched Event005 script/focus files: all final depths were `0`, with no negative depth.
- `git diff --check` on touched files: clean.
- Unsupported operator scan for `<=` and `>=` on touched files: no matches.
- Flag-file diff scan: no output.

## Remaining Incomplete Work

- This is not a full Event005 completion claim. The remaining blocker is content breadth: the focus trees still need another full visual/layout audit and deeper reward pass across all republic and chaos-country trees.
- The current changes reduce repeated shared payloads and obvious pathline-prone rows, but they do not prove every tree is visually clean in-game.
- No commit was created because the worktree contains broad unrelated pre-existing Event005 and Event006 changes.
