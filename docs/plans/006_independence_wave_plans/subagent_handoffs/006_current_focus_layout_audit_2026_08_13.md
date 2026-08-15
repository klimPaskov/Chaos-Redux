# Event 006 focus layout audit, 2026-08-13

## Scope and disposition

Audited `common/national_focus/006_independence_wave_focus.txt` after the recent visible-prerequisite additions. No gameplay, focus, localisation, icon, or AI source was patched in this pass. The worktree contains concurrent Event 006 edits, so the audit records the smallest safe source disposition for the parent to apply and review without rewriting the wider authored layout.

The opening baseline and recommendation below are retained for traceability. The parent-applied follow-up at the end of this handoff supersedes the initial read-only disposition and records the six accepted redundant-edge removals plus the post-change MCP receipts.

## Required MCP evidence

- `hoi4.focus_inspect`: workspace `mod_chaos_redux_ea3b2d67c2c0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe77bc7ac92c91137da646dc1ffe27b17ad6f261c302a6a4cb431f58a5925b1a/20f1ee505e8382487dfff4288370b9905553d9365c92c30610920f217b10c43a/focus-inspect.3945ca8028624ed5.json`.
- `hoi4.focus_render`: layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`; HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bafadaf3584b61902208ede0723c6463e5b168dd8e52a8faabe6a8bd118f925c/d0d62d7a4172e32ba6c1f87baf8f73b10dae9f1a12b6f80d88018829c50deff1/independence_wave_focus_tree.focus.html`; SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80e261b095ad407628f8fe37b72886556bdee1b5488a472c92bc874660308e5e/16c0835bc38200294ae89c2e76a3df6fb62b317e18f6d4f9c999581f2f2d874a/independence_wave_focus_tree.focus.svg`.
- Engine graph: 184 focuses, 218 connectors, 32 connector crossings, 7 focus-node intersections, bounds `x=1..121`, `y=0..19`, and 14 blocking layout diagnostics. The inline inventory truncation is informational only.

## Route coverage and source semantics

| Route surface | Visible parent added in current diff | Existing gate in `available`/`allow_branch` | Layout disposition |
| --- | --- | --- | --- |
| Internal power struggle | `complete_founding_settlement -> map_internal_power_centers` | `has_completed_focus = independence_wave_complete_founding_settlement` plus `can_open_independence_wave_internal_power_struggle` | Redundant visible edge. It is 17 columns long. Remove the visible prerequisite or move the entire optional lane, do not alter the gate. |
| Economy | `inventory_the_state -> establish_emergency_revenue` | `has_completed_focus = independence_wave_inventory_the_state` | Redundant visible edge. It is 12 columns long and crosses the oath-to-provinces connector. Remove the visible prerequisite. |
| IW-010 municipal commission | `complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` | `has_completed_focus = independence_wave_complete_founding_settlement` plus AJX route flags | Redundant remote edge from `x=20` to `x=92`; it participates in the transport/host/recognition crossings. Remove the visible prerequisite. |
| Former-host policy | `complete_founding_settlement -> define_former_host_policy` | Same completed-focus check in `available` | Semantically redundant, but this is a central branch root. Removing the edge is safe for gating but should be paired with a deliberate branch-anchor/layout review. |
| Regional ambition | `complete_founding_settlement -> survey_regional_ambition` | Same completed-focus check in `available` | Redundant edge. It runs through `establish_customs_service` and `preserve_independent_command`, and crosses the military archetype edge. Remove the visible prerequisite. |
| Recognition network | `complete_founding_settlement -> recognize_fellow_new_states` | Same completed-focus check in `available` | Redundant edge. It participates in the transport/recall crossings. Remove the visible prerequisite. |
| Military archetype choices | `form_border_guard -> adopt_military_archetype_program`; `adopt_military_archetype_program -> reclamation_doctrine/standardize_with_league` | Each child repeats the corresponding `has_completed_focus` in `available` | The new visible edges create the reported detour and long 9/11-column connectors. Remove only if the parent accepts tooltip-only gating for these choice spurs. |
| Distant package roots | `prepare_capital_administration ->` SCO/WLS/AJX/BRI/AFX/AGX/RHI/BAY/ARX/ASX roots | Package-specific `allow_branch`/`available` checks | These are remote cross-lane edges from `x=20` to `x=64..120`. They are not all surfaced in the bounded diagnostic list, but they are the likely source of additional crossings in the 32-crossing total. Keep only if a later lane redesign provides local anchors. |

The visible prerequisites are not required for gameplay when the same completed-focus condition already exists in `available`. HOI4 evaluates prerequisite blocks as visible route lines and `available` as the selectable gate. Removing a redundant visible edge therefore preserves eligibility while removing the problematic connector. Package/route checks must remain untouched.

## Exact MCP layout findings tied to recent edges

- `complete_founding_settlement -> map_internal_power_centers`: `FOCUS_LAYOUT_LONG_CONNECTOR`, 17 columns.
- `inventory_the_state -> establish_emergency_revenue`: `FOCUS_LAYOUT_LONG_CONNECTOR`, 12 columns, and crossing with `bind_the_first_oath -> integrate_provinces_and_councils`.
- The newly visible `complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses the transport branch and the former-host/recognition lines.
- The newly visible `complete_founding_settlement -> independence_wave_survey_regional_ambition` intersects `establish_customs_service` and `preserve_independent_command`, then crosses the military archetype edge.
- `secure_food_and_fuel -> build_regional_transport_authority` is an authored vertical detour (`y=3 -> y=5`) and is not a new prerequisite from the current diff. Do not remove it as part of the prerequisite cleanup without a separate layout decision.
- `activate_package_economic_program -> create_independent_treasury` is an authored horizontal detour and likewise is not caused by the current visible-prerequisite diff.

## Recommended smallest safe source fix

Remove the redundant visible `prerequisite` lines for these five focus ids, leaving their existing `available` checks unchanged:

1. `independence_wave_map_internal_power_centers` at source line 275.
2. `independence_wave_establish_emergency_revenue` at source line 341.
3. `independence_wave_ajx_appoint_neutral_commission_focus` at source line 1352.
4. `independence_wave_survey_regional_ambition` at source line 1612.
5. `independence_wave_recognize_fellow_new_states` at source line 1691.

This is the narrowest safe fix because each line duplicates an existing completed-focus gate and each one is directly implicated in a long connector, connector crossing, or connector-through-node diagnostic. Do not remove the package root edges, former-host edge, or military choice edges in the same patch unless the parent accepts a second layout pass. No focus localisation or icon change is needed.

## Required follow-up validation

After applying the five-line removal, rerun `hoi4.focus_inspect` and `hoi4.focus_render` against the same tree and compare the crossing/long-connector diagnostics. The current pass did not apply the source patch, so post-change MCP evidence is intentionally pending. Parent review must also check that the package-specific `allow_branch` and `available` gates still hide and unlock each branch as intended.

## Audit gaps and remaining risks

- The tree still has authored long/detour connectors unrelated to the recent visible-prerequisite additions, especially the transport, treasury, and military-archetype lanes.
- The baseline full graph reported 32 crossings and 7 focus-node intersections, while the MCP inline diagnostics exposed only the first bounded subset. The six-edge follow-up inspect/render is now recorded at the end of this handoff; remaining remote package-root and authored-lane warnings are intentionally preserved.
- No AI weight was changed, so no probability audit was required for this pass.
- No localisation, icon, reward, or route content was changed. Existing focus strings and sprites remain outside this layout-only audit.

## Follow-up cleanup: establish foreign office

The parent reported five remaining crossing diagnostics, all involving `independence_wave_name_provisional_authority -> independence_wave_establish_foreign_office`. Source inspection confirmed that the visible prerequisite duplicated the focus's existing `available = { has_completed_focus = independence_wave_name_provisional_authority can_use_independence_wave_full_focus_framework = yes }` gate. Removing the visible line therefore preserves gameplay eligibility and route locking while removing only the redundant connector.

Applied one narrow source edit in `common/national_focus/006_independence_wave_focus.txt`: removed `prerequisite = { focus = independence_wave_name_provisional_authority }` from `independence_wave_establish_foreign_office` (formerly source line 779). No localisation or icon changes were needed.

Post-change MCP evidence:

- `hoi4.focus_inspect` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bc477482377591fcb7cf87416e8bf5be05bea3d6dd3205ac8da5e391b7e3359/f8c507ff4d293782a3df9b154e857dd04f521a63a8d70f9aaefac9fa4ac4e92f/focus-inspect.04e7b0637905ea52.json`.
- `hoi4.focus_render` artifacts: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48e8d477b9af14b92e64b9cffb0c271baf53fdbb9f4950a27319839330c597fe/60c98c61ac7b86a2e3f8c34ff5fb48b61604cb49a0c38691a2198194eb1b8ff1/independence_wave_focus_tree.focus.html`; SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a863376835eac016bfec20473661facd97a573ba37867f0364e16f5aa596011b/4c5b3dae2ae282511e5ff201db2fa2f4df976cad5156d9d498e9eec5a8954151/independence_wave_focus_tree.focus.svg`.
- Graph metrics improved from 213 connectors / 13 crossings / 0 node intersections / 19 long connectors to 212 connectors / 8 crossings / 0 node intersections / 18 long connectors. The five establish-foreign-office crossing diagnostics disappeared.
- Remaining layout warnings are authored edges such as the 30-column `complete_founding_settlement -> define_former_host_policy` connector and the transport, military, treasury, and recognition-lane crossings. The MCP validation summary still reports 14 blocking focus diagnostics because those unrelated warnings remain; this single-edge cleanup did not introduce a new blocker.

## Parent-applied follow-up

## Follow-up cleanup: military choice prerequisites

Audited the two visible military-choice prerequisites against the current 212-connector, 8-crossing, 0-intersection, 18-long-connector graph. Both were redundant and layout-safe to remove:

- `independence_wave_adopt_reclamation_doctrine` had `prerequisite = { focus = independence_wave_adopt_military_archetype_program }`, while `available` already required `has_completed_focus = independence_wave_adopt_military_archetype_program`, `can_use_independence_wave_full_focus_framework = yes`, and `has_country_flag = independence_wave_host_reclamation_route_available`. Its mutual exclusion with `independence_wave_adopt_border_defense` remains unchanged.
- `independence_wave_standardize_with_league` had the same visible prerequisite, while `available` already required `has_completed_focus = independence_wave_adopt_military_archetype_program` and `can_participate_in_independence_wave_network_focuses = yes`. Its mutual exclusion with `independence_wave_preserve_independent_command` remains unchanged.

Removed both redundant visible lines from `common/national_focus/006_independence_wave_focus.txt`; no localisation, icon, effect, AI, or mutual-exclusion changes were made. Because the `available` blocks retain the parent completion checks and route gates, focus eligibility and branch locking are preserved. The two long connectors were direct visual artifacts of the removed edges, not required gameplay links.

Post-change MCP evidence:

- `hoi4.focus_inspect` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96d026e4a91f9f9c3ca218e6414d0931d96ac3d739914cf52e39aee84cc24963/e4fef5641f32dcb19a09007a49231ffcb0594245e6853f7a291d8caea71b304e/focus-inspect.cfa1bc8fc6726142.json`.
- `hoi4.focus_render` artifacts: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f1bfd34e1bbabf9f6bb1a15942dab395965d0b026920f41ff32c4b132917827/d6cec3508ed3b2fe88d39a7fe4e5661de55d96d76df0dc12097929ce1e37b166/independence_wave_focus_tree.focus.html`; SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a51acbc0d703a8c6bf4a02def762ab718bc36b99b53bac183499ec8edb2f2c3a/e8489d66abc65e950240323e6a28047d3ad1f5842559f85349a338e60dd925bb/independence_wave_focus_tree.focus.svg`.
- Graph metrics improved from 212 connectors / 8 crossings / 0 node intersections / 18 long connectors to 210 connectors / 8 crossings / 0 node intersections / 16 long connectors. The two military-choice long-connector diagnostics disappeared; the crossing count was unchanged because neither edge participated in a crossing.
- Remaining warnings are unrelated authored geometry, including the 13-column `adopt_military_archetype_program -> preserve_independent_command` edge, former-host/transport/recognition crossings, and other branch detours. MCP still reports 14 blocking diagnostics for those remaining warnings; this cleanup introduced no new diagnostic.

The parent applied the five-line recommendation for `independence_wave_map_internal_power_centers`, `independence_wave_establish_emergency_revenue`, `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_survey_regional_ambition`, and `independence_wave_recognize_fellow_new_states`, retaining each existing `available` gate. A subsequent focused pass also removed the redundant visible prerequisite from `independence_wave_establish_foreign_office`, retaining its `available` gate. The final `hoi4.focus_inspect`/`hoi4.focus_render` pass reports 184 focuses, 212 connectors, 8 crossings, 0 node intersections, 18 long connectors, and 14 blocking diagnostics. Current inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bc477482377591fcb7cf87416e8bf5be05bea3d6dd3205ac8da5e391b7e3359/f8c507ff4d293782a3df9b154e857dd04f521a63a8d70f9aaefac9fa4ac4e92f/focus-inspect.04e7b0637905ea52.json`; current render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a863376835eac016bfec20473661facd97a573ba37867f0364e16f5aa596011b/4c5b3dae2ae282511e5ff201db2fa2f4df976cad5156d9d498e9eec5a8954151/independence_wave_focus_tree.focus.svg`. The cleanup removed the targeted crossing cluster without changing eligibility, but the tree remains HOLD for the remaining authored crossings, long connectors, and blocking diagnostics.

## Current follow-up after IW-044

The parent then removed four redundant visible prerequisite lines whose completed-focus conditions remain in `available`: `independence_wave_integrate_militia_commands`, `independence_wave_prepare_first_assembly`, `independence_wave_define_former_host_policy`, and `independence_wave_sponsor_further_ruptures`. The `independence_wave_preserve_independent_command` prerequisite was restored after its removal produced an isolated focus, so its branch remains visibly connected.

The current `hoi4.focus_inspect` revision `041d42b297734fcde47f1b1794c33ce33cd5539acb370978ddae0a341b41014b` reports 184 focuses, 206 connectors, zero crossings, zero node intersections, and 12 long connectors. The remaining 14 blocking diagnostics are three unrelated vanilla continuous-focus icon references plus authored transport, treasury, military-archetype, former-host, formable, and distant package-root geometry warnings.

The current `hoi4.focus_render` produced HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c29dfe6b234078818639cb0ccb4b9d5bf390573ea8855d634a794d53747cdaf6/959f638fb45e39a0d98b58a3b938718cff4fb7ae057b120b87b0e8251535f90c/independence_wave_focus_tree.focus.html` and SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c51a07eee7fcbe60e40231211902e20aa68aff6e2313b7484db6ee1705a5bf19/fb37f0693f97d8a192c53cf83d0026008436686e1659b4f526ef95db6375bc24/independence_wave_focus_tree.focus.svg` at unchanged layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.

Eligibility, route locks, rewards, localisation, icons, AI, and package hooks were unchanged; this is a visual-edge cleanup only. The shared focus surface remains HOLD until the authored remaining geometry is deliberately redesigned.

## Current military-choice verification

The current worktree source already contains no visible `prerequisite` line on either `independence_wave_adopt_reclamation_doctrine` or `independence_wave_standardize_with_league`, so this audit applied no additional source patch. Their exact gates remain:

- `independence_wave_adopt_reclamation_doctrine`: `available` requires `has_completed_focus = independence_wave_adopt_military_archetype_program`, `can_use_independence_wave_full_focus_framework = yes`, and `has_country_flag = independence_wave_host_reclamation_route_available`; mutual exclusion with `independence_wave_adopt_border_defense` remains.
- `independence_wave_standardize_with_league`: `available` requires `has_completed_focus = independence_wave_adopt_military_archetype_program` and `can_participate_in_independence_wave_network_focuses = yes`; mutual exclusion with `independence_wave_preserve_independent_command` remains.

This makes removal of the two visible edges semantically safe: parent completion, route/framework checks, and choice exclusions are still enforced by `available` and `mutually_exclusive`. The fresh inspect receipt is 184 focuses, 212 connectors, 8 crossings, 0 node intersections, 18 long connectors, and 14 blocking diagnostics, with no reclamation/standardization connector diagnostics. The paired render returned the existing source-linked HTML/SVG artifact set; its cached JSON reflects the earlier 210-connector cleanup. Because the current source and cached MCP artifacts disagree on connector count while both omit the two military diagnostics, no further edit is warranted. Remaining warnings are unrelated authored connectors, especially `adopt_military_archetype_program -> preserve_independent_command` and former-host/transport/recognition lanes.

## Current authority correction after the IW-044 follow-up

The immediately preceding military-choice verification is a dated cache note. The authoritative current source/MCP pair is the `041d42b297734fcde47f1b1794c33ce33cd5539acb370978ddae0a341b41014b` follow-up above: 184 focuses, 206 connectors, zero crossings, zero node intersections, and 12 long connectors. The four additional redundant-edge removals are source-applied and eligibility-preserving; no military-choice edge was removed in that follow-up.
# Focus layout cleanup decision (2026-08-13)

An attempted economy-lane coordinate alignment was rejected after the post-change MCP inspection introduced one connector crossing between the treasury and military-choice lanes. The coordinate edit was reverted; the current source therefore preserves the prior zero-crossing/zero-node-intersection layout and its existing authored warnings. No focus eligibility, prerequisite, localisation, icon, or AI semantics were changed.

The final post-revert `hoi4.focus_inspect` is revision `381140acd320a1be19bab9d19285c85165412d71eba85e04be4c9f3027179eb1`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a2683548930c07d7818181c7e4e32d72e46c8531235859a4736c061b8613531/b051fd3e67e8778cc2a4454b64b810c2f6d3804654721ac0f62710aad08e5cae/focus-inspect.381140acd320a1be.json`; it reports 184 focuses, 206 connectors, zero crossings, zero node intersections, and 12 long connectors. The paired final render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c51a07eee7fcbe60e40231211902e20aa68aff6e2313b7484db6ee1705a5bf19/2aa5202bfd73cb0e6c633c8b489c83a7a2542eeb6a0df10e6206899a5ae29531/independence_wave_focus_tree.focus.svg`. The temporary trial revisions `26e1aca269bc0a1b` and `1ea8f41613239aea` are rejected evidence and are not current source authority.
