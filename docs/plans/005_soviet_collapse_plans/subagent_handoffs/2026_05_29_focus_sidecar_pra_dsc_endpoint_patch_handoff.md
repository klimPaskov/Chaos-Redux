# Soviet Collapse Focus Sidecar PRA/DSC Endpoint Patch Handoff

Date: 2026-05-29

## Scope

- Active small patch in `common/national_focus/005_soviet_collapse_custom_splinters.txt`.
- No edits to scripted effects, scripted triggers, decisions, localisation, flags, or assets.
- Parent-owned Soviet Collapse release, decision, evolution, and Ukraine layout wiring was not touched.

## Route Coverage Table

| Required route/content area | Implemented branch | Status | Notes |
| --- | --- | --- | --- |
| PRA railway authority identity | `PRA_soviet_collapse_focus_tree`, especially `PRA_the_pale_line_endures` | Improved locally | Peaceful corridor endpoint now grants rail authority, rolling stock, trains, rail/supply construction, and industry filter alignment. |
| PRA aggressive rail conquest | `PRA_rails_over_capitals` | Already covered by earlier patches | Existing focus has annexation filter, rail authority reward, SOV war goal, AI aggression, and assault-column hooks. |
| DSC dead soldiers congress identity | `DSC_soviet_collapse_focus_tree`, especially `DSC_memorial_frontier_state` | Improved locally | Memorial endpoint now grants army XP, command power, manpower, roll-call legitimacy, revenant mobilization, frontier construction, and defensive SOV AI posture. |
| DSC dead-army conquest route | `DSC_congress_of_the_dead_army`, `DSC_armies_that_do_not_demobilize` | Already covered by earlier patches | Existing route has manpower/equipment, neighbor/SOV war goals, AI conquest pressure, and assault-column hooks. |
| Factory/military/naval/rail successor states | CFR/MFR/NRF/PRA/DSC focus files | Audited only in this pass | Existing handoffs show direct reward/AI patches already applied. No additional safe bounded patch found beyond PRA/DSC endpoints. |

## Changed Files

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Strengthened two endpoint focus rewards and search filters. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_sidecar_pra_dsc_endpoint_patch_handoff.md` | This handoff. |

## Changed Focus IDs

| Focus id | Behavior before | Behavior after |
| --- | --- | --- |
| `PRA_the_pale_line_endures` | Completed the Pale Railway endgame and applied legal recognition/League prep only. | Also applies rail authority reward, adds `pra_rail_authority`, `pra_rolling_stock`, train equipment, a core-state supply node/rail buildout, industry search filter, and an AI weight bump when Soviet depot vulnerability is high. |
| `DSC_memorial_frontier_state` | Completed the Dead Soldiers endgame, legal/depot rewards, and small stability only. | Also adds army XP, command power, manpower, roll-call legitimacy, revenant mobilization, controlled-state fort/infrastructure construction, army/manpower filters, and a defensive SOV prepare/antagonize AI posture. |

## Icon Coverage Table

| Focus id | Icon id | Status |
| --- | --- | --- |
| `PRA_the_pale_line_endures` | `GFX_focus_PRA_the_pale_line_endures` | Existing reference, unchanged. |
| `DSC_memorial_frontier_state` | `GFX_focus_DSC_memorial_frontier_state` | Existing reference, unchanged. |

## Localisation and Reward Mismatch List

| Focus id | Status | Notes |
| --- | --- | --- |
| `PRA_the_pale_line_endures` | Improved | Existing text calls it a corridor authority; reward now visibly builds rail/supply authority. No localisation keys changed. |
| `DSC_memorial_frontier_state` | Improved | Existing text says it guards memorial towns and old-front roads; reward now adds manpower, command capacity, fort/infrastructure construction, and defensive AI posture. No localisation keys changed. |

## AI Behavior Gaps

- Improved: `PRA_the_pale_line_endures` is more attractive when Soviet depot vulnerability is high.
- Improved: `DSC_memorial_frontier_state` now grants persistent prepare/antagonize AI strategies against `SOV`, weaker than the conquest endpoint and fitting the memorial-frontier route.
- Remaining: PRA and DSC are still compact crisis trees, not full major-country route families.
- Remaining: Route-level AI strategy cleanup/removal hooks were not added because that would require broader systems outside this subagent scope.

## Missing or Simplified Content

- PRA still needs a broad rail-control mechanic and larger diplomacy/expansion branch if it is meant to stand beside full custom splinter trees.
- DSC still needs full dead-army economic, command, and aftermath depth beyond endpoint strengthening.
- Ukraine layout and scripted release/decision/evolution wiring remain parent-owned and were not changed.
- No localisation text was edited, so descriptions were only checked for the two changed focus IDs.

## High-Priority Fixes Completed

1. Strengthened the non-conquest PRA rail endpoint without adding new systems.
2. Strengthened the non-conquest DSC memorial endpoint without touching decisions or scripted helpers.
3. Aligned search filters with the new endpoint rewards.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed.
- Brace balance on `005_soviet_collapse_custom_splinters.txt`: `open=10931 close=10931 balance=0`.
- Unsupported operator scan: `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt` returned no matches.
- Focus block review confirmed changed rewards are limited to `PRA_the_pale_line_endures` and `DSC_memorial_frontier_state`.

## Skipped Validation

- No in-game load test was run.
- No full mod-wide validator was run because the worktree contains extensive parent/user changes outside this sidecar scope.
- No localisation encoding validation was needed because localisation was not edited.

## Remaining Route Risks

- This is not a full clutter/depth rewrite. It is a bounded local endpoint reward patch.
- The working tree already contained many uncommitted Soviet Collapse focus changes from other agents; this handoff only claims the two endpoint edits above.
- No git commit was made because staging the touched focus file would include unrelated parent/agent changes already present in the same file.
