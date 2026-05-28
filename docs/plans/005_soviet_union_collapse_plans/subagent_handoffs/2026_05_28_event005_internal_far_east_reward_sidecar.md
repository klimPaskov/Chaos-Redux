# Event 005 Internal Far East Reward Sidecar

Date: 2026-05-28

## Scope

Bounded focus-quality patch for `common/national_focus/005_soviet_collapse_republics.txt`, limited to the internal republic Far Eastern branch and the focus-tree audit note.

## Changed Files

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Split three internal republic Far Eastern rewards away from repeated generic civilian-industry packets. |
| `docs/events/005_soviet_collapse_focus_tree_audit.md` | Added this cleanup to the focus-quality audit trail. |
| `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_internal_far_east_reward_sidecar.md` | Handoff for the parent agent. |

## Changed Focus IDs

| Focus id | Before | After |
| --- | --- | --- |
| `internal_soviet_collapse_far_eastern_rail_contracts` | Foreign-channel helper plus a generic civilian factory. | Foreign-channel helper plus train stock, depot control, recognition progress, and local rail infrastructure. |
| `internal_soviet_collapse_far_eastern_port_authority` | Foreign/depot helpers plus another generic civilian factory. | Foreign/depot helpers plus naval XP, convoys, and a coastal dockyard. |
| `internal_soviet_collapse_amur_rail_customs_board` | Infrastructure plus a civilian factory, foreign channel, and League preparation. | Train stock, liaison reach, infrastructure, supply node, foreign channel, and League preparation. |

## Route Coverage

| Required route | Implemented branch | Status | Notes |
| --- | --- | --- | --- |
| Internal Far Eastern rail authority | `internal_soviet_collapse_far_eastern_rail_contracts` | Improved | Rail contracts now visibly affect trains, depot control, recognition, and map infrastructure. |
| Internal Far Eastern port authority | `internal_soviet_collapse_far_eastern_port_authority` | Improved | Port authority now has naval/dockyard payoff rather than generic civil industry. |
| Internal Amur customs corridor | `internal_soviet_collapse_amur_rail_customs_board` | Improved | Customs board now reinforces rail-customs logistics through trains, liaison reach, infrastructure, and supply capacity. |

## Icon Coverage

| Focus id | Icon status |
| --- | --- |
| `internal_soviet_collapse_far_eastern_rail_contracts` | Icon assignment unchanged by this patch. |
| `internal_soviet_collapse_far_eastern_port_authority` | Icon assignment unchanged by this patch. |
| `internal_soviet_collapse_amur_rail_customs_board` | Icon assignment unchanged by this patch. |

## Localisation And Rewards

No localisation keys were renamed or added. Existing descriptions still match the new rewards: rail contracts, port authority, and Amur customs now produce rail, port, and customs/logistics outcomes.

No AI blocks, prerequisites, mutual exclusions, layout coordinates, or focus IDs changed.

## AI Behavior Gaps

The three touched focuses keep their prior AI weights. This patch does not add route-specific AI because the existing weights already key off Soviet foreign appetite or branch position, and the reward changes do not alter route eligibility.

## Validation

Run after patch:

- `python3` brace/focus check for `common/national_focus/005_soviet_collapse_republics.txt`: brace depth `0`, premature closes `0`, each changed focus id appears once, parsed `focus = {` count `482`.
- Forbidden comparison-operator scan across the touched focus, audit, and handoff files: no matches.
- `git diff --check`: pass.

## Skipped Validation

No live HOI4 launch or in-game focus completion test was run in this bounded sidecar pass.

## Remaining Risks

This patch fixes one small duplicate-reward cluster only. Broader internal republic layout/readability and remaining shared-helper reward similarity remain tracked in the main focus-tree audit.
