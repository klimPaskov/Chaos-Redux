# Event 006 focus layout repair handoff

Status: blocked; no coordinate patch was retained. The requested current MCP revision could not be inspected because the focus MCP transport returned `Transport closed` for both `hoi4.focus_inspect` and `hoi4.focus_render`.

## Scope and source state

The bounded task was a coordinate-only repair for `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt`, requested against revision prefix `5b4efbd9...`.

The source file remains unchanged by this pass. Its current SHA-256 is `DF0CD14EEBFB3450174D5BB2C64D305D9C9FB5E955B5FC5784B8BB7FE7B8B95E`. No focus IDs, prerequisites, mutual exclusions, rewards, icons, localisation keys, AI weights, shared-focus imports, or route semantics were edited.

## Route coverage table

| Route family | Existing coverage | This pass |
| --- | --- | --- |
| Survival and state construction | Present through the opening administration, oath, integration, and founding-settlement focuses | Unchanged; opening and founding geometry remains coupled. |
| Package-gated government settlements | Present through the existing constitutional, emergency-command, protected-future, AJX, and inherited-border branches | Unchanged; no package route was moved or removed. |
| Economy, infrastructure, and administration | Present through `independence_wave_establish_emergency_revenue`, `independence_wave_secure_food_and_fuel`, and `independence_wave_build_regional_transport_authority` | Unchanged; the economy lane is one affected coordinate group. |
| Army, security, and military identity | Present through `independence_wave_integrate_militia_commands`, the depot/recall spine, and the professional-defense branch | Unchanged; depot and professional-defense geometry remain coupled to the founding fan. |
| Diplomacy, recognition, and patrons | Present through the former-host, recognition, league, and patron lanes | Unchanged; fan endpoints were not moved. |
| Independence network, formable, signature, and high-chaos work | Present in the existing late tree and shared imports | Unchanged and outside this local repair. |

## Diagnostics before and after

The last authoritative post-revert baseline (the source state still present locally) reported `passed: false` with 14 blocking focus diagnostics: one `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` and thirteen `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` diagnostics.

| Baseline metric | Value |
| --- | ---: |
| Connector crossings | 49 |
| Node intersections | 18 |
| Long connectors | 27 |
| Too-close same-row pairs | 6 |
| Bounds | x=1..101, y=0..19 |
| Layout hash | `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1` |

No patch was applied, so there is no post-patch metric set. A fresh inspect/render for the requested `5b4efbd9...` revision is `N/A` until the MCP transport is available; the failed calls returned `Transport closed` before producing an artifact.

## Blocking clusters and smallest safe change

| Priority | Cluster and source references | Why a one-node move is unsafe | Smallest parent-owned change |
| --- | --- | --- | --- |
| 1 | Opening handoff: `independence_wave_inventory_the_state` (`:104-108`) and `independence_wave_bind_the_first_oath` (`:123-127`) feed `independence_wave_integrate_provinces_and_councils` (`:181-186`) and `independence_wave_establish_emergency_revenue` (`:285-289`). | The parent order at x=20/24 is inverted against the child order at x=24/32. Moving only oath, integration, or revenue changes the next economy, military, and founding prerequisite lanes. | Reflow both parent columns and both child columns as one two-tier ordering, then recheck the downstream food/transport and capstone fans. |
| 2 | Founding fan: `independence_wave_complete_founding_settlement` (`:201-207`) to `independence_wave_ajx_appoint_neutral_commission_focus` (`:1219-1224`), `independence_wave_define_former_host_policy` (`:1279-1283`), and `independence_wave_recognize_fellow_new_states` (`:1534-1538`) crosses `independence_wave_secure_food_and_fuel` (`:304-308`) -> `independence_wave_build_regional_transport_authority` (`:324-328`). | The x=20 founding fan must pass around the vertical economy lane at x=32; moving only a fan endpoint or only the economy child simply transfers crossings to other capstone prerequisites. | Move the capstone fan and the food/transport lane together while keeping government columns x=3..28 and package columns x>=67 clear. |
| 3 | Depot spine: the same `independence_wave_complete_founding_settlement` fan crosses `independence_wave_secure_national_depots` (`:426-430`) -> `independence_wave_recall_and_vet_officers` (`:447-451`), whose parent is `independence_wave_integrate_militia_commands` (`:406-410`). | The depot lane shares the founding fan's y=3/y=4 tier and is also anchored to the oath branch; an isolated shift creates new prerequisite crossings. | Reflow militia/integration, depot, and recall with the founding fan as one coupled group. |
| 4 | Professional-defense merge: `independence_wave_adopt_military_archetype_program` (`:488-492`), all five mutually exclusive pairs (`:532-663`), and `independence_wave_found_professional_defense_institution` (`:507-515`). | The five choice pairs are interleaved across y=7..11 and all merge at y=12. Moving only the final node or one option creates another crossing. | Treat y=6..12 as one monotone branch layout, preserving every pair and the downstream sovereignty handoff. |

The smallest safe change is therefore a constrained four-group authored reflow, not a single coordinate edit. Keep focus IDs, prerequisite semantics, mutual exclusions, rewards, AI, and filters byte-for-byte equivalent while changing only the affected `x`/`y` fields.

## Candidate trial evidence

The prior coupled trial moved only the professional-defense coordinates and preserved all non-coordinate script. It still reported 14 blockers and worsened global metrics to 51 connector crossings, 20 node intersections, and 31 long connectors. Earlier two-anchor opening trials also failed to close the blocker set and introduced new capstone prerequisite crossings; all candidates were reverted. This evidence is why no speculative coordinate patch is retained here.

## Missing or simplified content

- No route, focus, reward, decision, mission, idea, advisor, leader, flag, claim, core, war goal, event, or formable content was omitted from the source.
- The unresolved item is layout geometry only: the restored baseline still has the 14 blocking crossings above.
- The requested current revision was not semantically re-audited because MCP inspection/rendering terminated before returning diagnostics.

## Icon coverage table

| Affected surface | Existing icon coverage | Result |
| --- | --- | --- |
| Opening, economy, and administration | `GFX_goal_independence_wave_infrastructure_authority`, `GFX_goal_independence_wave_founding_administration` | No missing or repeated icon was introduced; IDs unchanged. |
| Army, depot, and professional core | `GFX_goal_independence_wave_army_integration`, `GFX_goal_independence_wave_military_emergency`, `GFX_goal_independence_wave_constitutional_state` | No missing or repeated icon was introduced; IDs unchanged. |
| Founding fan endpoints | `GFX_goal_independence_wave_ajx_neutral_commission`, `GFX_goal_independence_wave_former_host_settlement`, `GFX_goal_independence_wave_league_congress` | No missing icon was introduced; endpoints remain in their existing package lanes. |
| Patron and reclamation choices | `GFX_goal_independence_wave_patron_client`, `GFX_goal_independence_wave_high_chaos_sovereignty` | No missing icon was introduced; IDs unchanged. |

## Localisation and reward mismatch list

No localisation keys or completion rewards changed, so this pass introduced no name/description/reward mismatch. Full current-revision localisation and reward validation remains deferred with the unavailable MCP revision; the source references above retain their existing keys and effects.

## AI behavior gaps

No AI weights, route-aware modifiers, `allow_branch`, or focus filters changed. The affected focuses retain their existing AI blocks in the source. A current-revision AI recheck is deferred until MCP transport recovers; no new AI gap is attributable to this pass.

## Validation performed and skipped

Meaningful local checks were exact coordinate/source inspection for every affected focus ID, a worktree comparison confirming no focus-file diff, and the recorded SHA-256 for the unchanged source.

`hoi4.focus_inspect` and `hoi4.focus_render` were attempted for `common/national_focus/006_independence_wave_focus.txt` / `independence_wave_focus_tree` with the requested workspace and revision context, but both returned `Transport closed`; therefore no fresh artifact or after-metrics can be claimed. `hoi4.focus_rewrite` was skipped because a compact rewrite would exceed this bounded scope. In-game validation was not run because live consumer testing belongs to the parent/user.

## Parent handoff and remaining risks

The parent should first restore MCP access, inspect the requested revision, and then solve the four coupled groups in priority order: opening handoff, founding/economy fan, depot spine, and professional-defense merge. Rerun inspect and render after each coherent tranche; reject any candidate that increases the global crossing, node-intersection, or long-connector metrics even if a local warning improves.

Remaining risks are the 14 unresolved baseline geometry diagnostics, long connectors from `independence_wave_complete_founding_settlement` -> `independence_wave_map_internal_power_centers`, `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue`, and `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_militia_commands`, plus the two non-blocking through-node warnings retained in the prior geometry handoff.

No gameplay files were changed. The next parent-owned implementation should be recorded under this handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_focus_layout_repair_2026-07-29.md`.
