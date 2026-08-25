# Event 006 shared focus geometry closure tranche

Date: 2026-08-25

## Disposition

**READY FOR PARENT IMPLEMENTATION AS ONE COORDINATES-ONLY CLOSURE TRANCHE.**

This is an implementation handoff for an accepted shared-tree mechanic, not another expansion addendum. The queued IW-050 admission addendum remains evidence-blocked and is not superseded, widened, or repeated here. The completed FORM-03 visibility addendum remains closed.

The tranche has no fallback. It either reaches the coordinate, topology, source-equivalence, and visual acceptance gates below or it is reverted as a whole.

## Design problem

The accepted Event 006 focus architecture requires seven recognizable lane families, short clean connectors, visually clear capstones, and a broad readable shared tree. The latest completion reaudit identified the shared focus geometry as the safest bounded completion surface because it could close five authored layout diagnostics without touching package admission, eligibility, rewards, AI, decisions, events, or maps.

A concurrent parent-owned coordinate trial is visible in the current working copy. Fresh mandatory MCP evidence shows that this trial has already removed the five audited detour and long-connector warnings, reduced the long-connector count to zero, and preserved zero crossings and zero node intersections. It also introduced two new same-row spacing warnings. The remaining work is therefore a precise closure of that trial, not a new route redesign.

## Accepted design and research connections

This geometry pass preserves the institutional sequence already justified by Event 006 research.

- The 1933 Montevideo Convention research packet connects functioning administration, defensible territory, government, and external relations to the event's public statehood pillars. The economy and customs trunk, military and border-security trunk, and recognition lane should consequently read as adjacent but distinct institutions.
- The accepted League of Nations Covenant research supports a visible distinction between defense institutions and neutrality, patronage, and collective-network diplomacy. The remaining military-to-neutrality spacing warning obscures that distinction at normal tree scale.
- The accepted focus architecture assigns economy and administration to Lane 3, army and military identity to Lane 4, and recognition and patrons to Lane 5. The closure keeps those lanes parallel, preserves their mechanical compatibility, and avoids presenting a geometry collision as a false route convergence.
- The provisional treasury, border guard, former-host ledger, and postwar integration concepts remain historical and institutional abstractions already accepted by the spec. This tranche adds no new historical claim, identity, border, leader, flag, portrait, or player-facing wording.

Primary research authority remains `docs/specs/006_independence_wave_specs/research/006_historical_and_institutional_research_notes.md` and `docs/specs/006_independence_wave_specs/research/006_research_bibliography.md`. Permanent design authority remains `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`.

## Fresh MCP baseline

The planner ran `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster` against the current working copy of `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`.

- Inspect status: `FOCUS_INSPECTED`.
- Revision: `2b95fc71cda2a32473e8675a7478543ae3b0f585594939b09fc722a48d5cf707`.
- Layout hash: `68e570b4b447dc4eb884a7c9fe484a80a6ddc02bdfa48f6be73e511700fb5704`.
- Topology: 184 focuses and 195 connectors.
- Geometry: zero crossings, zero node intersections, and zero long connectors.
- Event 006 authored diagnostics: two same-row spacing warnings.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c42b02896c7d1019b55cbbea461c5e607cb89fd71424e5dd9e9a00376036330/4324d431a74735d5d58d404d35247d1abbfbc17299c03a5374dfb69cbd42518a/focus-inspect.2b95fc71cda2a324.json`.
- Render status: `FOCUS_RENDERED`.
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eeff4781d11b59594cfabb336aa15fae477c6c16e6c00996225ede5876fb269d/85932431310269114d63a81acc94fa2e0b6efaaaf94c4ba91c70ac4fa2f222f9/independence_wave_focus_tree.focus.html`.
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9a04cf6f23848fc6083e91f7cf814d237c8a035f44b7a5ae11ccdfa14927fdb/f8e9af7d724dee2be02e3c86d20593e34b91a767db36b2b5bd5394c6199bcadd/independence_wave_focus_tree.focus.svg`.
- Raster status: `RENDER_DIMENSIONS_BLOCKED` because the deterministic PNG would be `21424x2440`, exceeding the fixed `16384` dimension ceiling. Raster evidence is unresolved and must not be claimed. The HTML and SVG remain the available visual-review surfaces.

The vanilla continuous-focus localisation warning for `continuous_restrict_freedom_desc` is outside Event 006 ownership and does not count as an Event 006-authored diagnostic.

## Exact implementation tranche

### FCL-006-A: preserve the successful provisional reflow

Retain the current parent-owned coordinate trial only if the final gates remain green. It is already evidenced to remove the five diagnostics named by the latest completion reaudit:

1. `independence_wave_activate_package_economic_program` to `independence_wave_create_independent_treasury`.
2. `independence_wave_form_border_guard` to `independence_wave_adopt_military_archetype_program`.
3. `independence_wave_adopt_military_archetype_program` to `independence_wave_preserve_independent_command`.
4. `independence_wave_define_former_host_policy` to `independence_wave_inherit_successor_ledger`.
5. `independence_wave_build_postwar_integration_authority` to `independence_wave_focus_discover_regional_identity`.

Do not split these changes into isolated endpoint fixes. The audit already rejected one-node moves because they displaced defects into adjacent children or branch cohorts.

### FCL-006-B: close the economy and radical-sovereignty spacing warning

Move the complete six-focus economy trunk one column right from its provisional `x = 30` alignment to `x = 31`. Preserve every `y` coordinate.

| Focus id | Final x | Final y |
| --- | ---: | ---: |
| `independence_wave_establish_emergency_revenue` | 31 | 2 |
| `independence_wave_secure_food_and_fuel` | 31 | 3 |
| `independence_wave_build_regional_transport_authority` | 31 | 4 |
| `independence_wave_establish_customs_service` | 31 | 5 |
| `independence_wave_activate_package_economic_program` | 31 | 6 |
| `independence_wave_create_independent_treasury` | 31 | 7 |

This creates the required two-column separation from `independence_wave_arm_aligned_movements` at `x = 29`, `y = 5` while keeping the treasury capstone vertically honest and retaining the shortened economy connectors.

### FCL-006-C: close the military and neutrality spacing warning

Move the complete five-focus military trunk one column left from its provisional `x = 42` alignment to `x = 41`. Preserve every `y` coordinate and leave the row-8 military choice cohort unchanged.

| Focus id | Final x | Final y |
| --- | ---: | ---: |
| `independence_wave_integrate_militia_commands` | 41 | 3 |
| `independence_wave_secure_national_depots` | 41 | 4 |
| `independence_wave_recall_and_vet_officers` | 41 | 5 |
| `independence_wave_form_border_guard` | 41 | 6 |
| `independence_wave_adopt_military_archetype_program` | 41 | 7 |

The row-8 child cohort spans `x = 32` through `x = 50` in two-column steps, so `x = 41` is its exact horizontal center. It also creates the required two-column separation from `independence_wave_declare_entrenched_neutrality` at `x = 43`, `y = 5` without moving the diplomacy lane or the former-host settlement lane.

## Explicitly forbidden changes

- No focus ID, prerequisite, mutually exclusive link, `allow_branch`, `available`, `bypass`, completion reward, cost, icon, search filter, localisation key, or AI block may change.
- No connector may be added or removed.
- No `relative_position_id`, offset, synthetic hub, hidden bridge focus, duplicate focus, or other structural substitute may be introduced.
- No event, decision, mission, formable, country package, package attestation, allocator, Join, portrait, flag, map, GUI, sound, spreadsheet, or super-event surface may change.
- No package gate may be weakened to make a route easier to render.
- No unrelated vanilla continuous-focus file may be patched under this tranche.

These restrictions are source-equivalence requirements, not optional scope guidance.

## Dependency order

1. Save the current inspect revision, layout hash, HTML, SVG, and source diff as the provisional before-state receipt.
2. Apply FCL-006-B as one economy-cohort coordinate change.
3. Apply FCL-006-C as one military-cohort coordinate change.
4. Verify a normalized source diff that ignores only the approved `x` and `y` lines. Every other token in `common/national_focus/006_independence_wave_focus.txt` must remain byte-equivalent to the tranche baseline.
5. Run fresh `hoi4.focus_inspect` and `hoi4.focus_render` against `independence_wave_focus_tree`.
6. Review the HTML or SVG at normal zoom. Confirm that the economy, radical-sovereignty, military, diplomacy, former-host, and formable lanes remain distinct at first glance and that no cohort appears to converge merely because it occupies adjacent rows.
7. If any Event 006 authored layout warning, crossing, node intersection, long connector, or first-glance ambiguity remains, reject and revert the whole coordinate tranche. Do not apply an unplanned one-node substitute.
8. Route the accepted result through `chaosx_focus_tree_auditor` for an independent focus-only receipt.
9. Reconcile the accepted final metrics and artifact URIs in the documentation surfaces listed below.
10. Commit the coordinate patch, audit receipt, and documentation reconciliation as one bounded implementation commit.

## Acceptance evidence

The tranche is accepted only when all of the following are true.

- `hoi4.focus_inspect` reports exactly 184 focuses and 195 connectors.
- It reports zero crossings, zero node intersections, zero long connectors, and zero Event 006-authored layout diagnostics.
- The only potentially remaining reported warning is the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference or another explicitly demonstrated non-Event-006 diagnostic.
- The final source diff changes only approved `x` and `y` fields.
- All focus IDs, connectors, route gates, rewards, AI weights, and availability logic remain identical.
- `hoi4.focus_render` succeeds and supplies fresh HTML, SVG, JSON, source-map, and plan artifacts tied to the final revision.
- Normal-zoom HTML or SVG review records `Pass` for the economy, radical-sovereignty, military, diplomacy, former-host, and formable lane boundaries affected by the reflow.
- The independent focus auditor finds no route, icon, localisation, reward, AI, or topology regression caused by the coordinate change.

`hoi4.focus_raster` was attempted and is unavailable for this full tree because of the fixed dimension ceiling. A final raster claim is forbidden unless the tool later succeeds without changing the tree or degrading review scale. The installed package has no Technology Tree Viewer, so no technology or doctrine conclusion is made. This tranche changes no weighted surface, so `hoi4.probability_inspect` and `chaosx_ai_probability_auditor` are not applicable. Any AI or weight change invalidates this scope and requires a separate probability-audit tranche.

## Exact implementation and documentation surfaces

Parent-owned gameplay file:

- `common/national_focus/006_independence_wave_focus.txt`

Post-acceptance documentation reconciliation:

- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md`
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/events/006_independence_wave/overview.md`
- `docs/events/006_independence_wave/systems/generic_focus_tree.md`
- A dated focus-auditor handoff under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.

## Open questions and unresolved authority

There is no open design question inside this tranche. The only unresolved acceptance item is the post-edit MCP and visual receipt.

The overall Event 006 authority remains `HOLD / PARTIAL`. This focus closure does not resolve unattested packages, IW-050 admission evidence, probability fixtures, GUI workspace diagnostics, map evidence, portrait and symbol provenance, super-event rights, or any other blocker recorded by the source-of-truth map and completion reaudit.

## Prior addendum status

`006_event6_improvement_addendum_2026_08_24.md` remains **QUEUED / EVIDENCE-BLOCKED** for IW-050 and is not implemented or promoted by this plan. `006_event6_form03_phase_docket_improvement_addendum_2026_08_24.md` has a closure receipt and does not block this separate shared-focus surface.

## Promotion recommendation

Keep this dated implementation handoff in `docs/plans/006_independence_wave_plans/`. Do not promote its coordinates, revisions, hashes, or artifact URIs into `docs/specs/`. The accepted Part 4 focus architecture already requires the intended broad, readable, lane-separated result. Promote nothing unless a later implementation changes route logic, which this tranche explicitly forbids.

