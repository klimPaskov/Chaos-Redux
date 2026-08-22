# Event 006 focus layout follow-up — 2026-08-22

## Scope and disposition

This pass audited the shared Event 006 national focus tree in `common/national_focus/006_independence_wave_focus.txt` only.

No source file was changed because none of the seven authored layout warnings has a safe one-node position fix that preserves the surrounding route geometry.

The requested plural source path `common/national_focus/006_independence_wave_focuses.txt` does not exist; the active tree source is `common/national_focus/006_independence_wave_focus.txt` and its tree id is `independence_wave_focus_tree`.

## MCP evidence

The current `hoi4.focus_inspect` national-tree run completed with `FOCUS_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Inspect revision: `32020588a8bc725215e70d4e3b97c6ca2d256940aff8b22dbc1dd7e8745064f7`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13fc65d5d5f35e72b1143d8376c1a0458a77aa9dfcb162d050065724933e43fb/33431ae6350a261de5d32c51381132d1a98409b77a940dc4cb9124d5756adb75/focus-inspect.32020588a8bc7252.json`.

The inspect result reports 184 focuses, 195 connectors, zero connector crossings, zero node intersections, three long connectors, and seven Event 006 layout warnings.

The current `hoi4.focus_render` national-tree run completed with `FOCUS_RENDERED` in the same workspace.

Render artifacts: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/835762d5ddb7f3b3838e7d31d4ebcf270388f3576becc1c4f1b5ae37519d200d/6b890182aca7a29f565e5dfd7b75d20412521191e2d71c7980c4ba04edd2dce3/independence_wave_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/770fea0f41e71e39a8a53a400985146a3c20860e3c08996ce27a956cff475d9b/08d7753b9dafdc3d5534c985f399aec6c97b8ba13c883e6b8022487ebef79301/independence_wave_focus_tree.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db966a432fdc7d3426531a7cbe523012f719342cb3de024be564f19fd42f2128/fac84e3ada996e382130080bc30d4048ec69345bdd9fb972769b42bc65a58e45/independence_wave_focus_tree.focus.json`.

Because no source edit was applied, there is no distinct post-change MCP revision; the inspect and render artifacts above are the final evidence for the unchanged source.

The fourteen continuous-focus icon/localisation diagnostics mentioned in the source-of-truth map remain out of scope; the current inspect surfaced one representative generic continuous-focus localisation warning, `continuous_restrict_freedom_desc`, under `game:common/continuous_focus/generic.txt`.

## Seven Event 006 diagnostics

| # | Diagnostic and source location | Current geometry | Safe narrow action | Disposition |
|---|---|---|---|---|
| 1 | `FOCUS_LAYOUT_LINEAR_DETOUR` at lines 411–428: `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` | x 32 to x 32, y 3 to y 5, with expected vertical span 1 | Moving only `build_regional_transport_authority` to y 4 would make its existing child `independence_wave_establish_customs_service` at y 6 the next two-row detour; moving the whole economy tail would be a broader lane edit. | Leave unchanged. |
| 2 | `FOCUS_LAYOUT_LINEAR_DETOUR` at lines 468–487: `independence_wave_activate_package_economic_program` -> `independence_wave_create_independent_treasury` | x 32 to x 28, y 7 to y 8, horizontal span 4 | Moving the treasury to x 32 would place it beside the military choice cohort at row 8, including x 31 and x 33 nodes, and would alter its separate capstone alignment to `independence_wave_secure_durable_sovereignty`. | Leave unchanged. |
| 3 | `FOCUS_LAYOUT_LINEAR_DETOUR` at lines 580–597: `independence_wave_form_border_guard` -> `independence_wave_adopt_military_archetype_program` | x 38 to x 36, y 5 to y 7, horizontal span 2 and vertical span 2 | Moving the archetype to y 6 would leave its eight direct military-policy children at y 8 with a new two-row gap; moving that cohort would be a route-wide military-lane edit. | Leave unchanged. |
| 4 | `FOCUS_LAYOUT_LONG_CONNECTOR` at lines 758–776: `independence_wave_adopt_military_archetype_program` -> `independence_wave_standardize_with_league` | x 36 to x 47, y 7 to y 8, horizontal span 11 | The target is one of the military choice cohort's rightmost row-8 outcomes; moving it or its parent would trade this edge for longer or crossing edges to the other seven children. | Leave unchanged. |
| 5 | `FOCUS_LAYOUT_LONG_CONNECTOR` at lines 778–796: `independence_wave_adopt_military_archetype_program` -> `independence_wave_preserve_independent_command` | x 36 to x 49, y 7 to y 8, horizontal span 13 | This is the same intentional military choice-row separation as warning 4 and is not an isolated metadata defect. | Leave unchanged. |
| 6 | `FOCUS_LAYOUT_LONG_CONNECTOR` at lines 1592–1610: `independence_wave_define_former_host_policy` -> `independence_wave_inherit_successor_ledger` | x 50 to x 59, y 4 to y 5, horizontal span 9 | Moving the target toward x 50 would collide with the living-host settlement node `independence_wave_fortify_former_host_frontier` at x 50, y 5; the right shift keeps the collapsed-host branch separate. | Leave unchanged. |
| 7 | `FOCUS_LAYOUT_LINEAR_DETOUR` at lines 1896–1908: `independence_wave_build_postwar_integration_authority` -> `independence_wave_focus_discover_regional_identity` | x 50 to x 52, y 11 to y 12, horizontal span 2 | Moving the discovery node to x 50 would break its aligned continuation to `independence_wave_prepare_union_congress` at x 52, y 13; moving the shared parent would change both prerequisites and the formable lane anchor. | Leave unchanged. |

## Route coverage

| Event 006 route surface | Current evidence | Layout conclusion |
|---|---|---|
| Survival and founding/state construction | Present in the 184-focus shared tree and connected into the generic root. | No route omission identified in this layout-only pass. |
| Economy, infrastructure, and administration | Includes the emergency revenue, food/fuel, transport, customs, package economy, and treasury chain at lines 367–487. | Warning 1 and warning 2 are authored lane geometry, not broken prerequisites. |
| Army, security, and researched military identity | Includes the military-archetype route, the eight policy children, and the exclusive league/independent-command outcomes at lines 493–796. | Warnings 3–5 are the deliberate military cohort spacing. |
| Diplomacy, recognition, and patrons | Present in the connected shared tree around the foreign-office and recognition lane. | No layout-only route loss found. |
| Former-host settlement and regional ambition | Includes living-host settlement branches and the collapsed-host ledger branch at lines 1432–1623. | Warning 6 protects branch separation. |
| Network, league, formable, signature, and high-chaos work | Includes regional congress/integration and formable preparation at lines 1629–1925 plus imported package branches. | Warning 7 protects the formable lane anchor. |

No prerequisite, mutual exclusion, reward, decision, mission, formable, claim, core, war-goal, event, or route hook was changed in this pass.

## Missing or simplified content

No Event 006 route content was removed or simplified.

No missing route, broken prerequisite, or broken mutual-exclusion relationship was found by the current focus inspect.

The only unresolved layout work is the seven intentional/geometry-sensitive warnings listed above.

## Icon coverage

| Surface | Evidence | Result |
|---|---|---|
| Main Event 006 focus icons | Current inspect scans the Event 006 goal assets and resolves all 184 tree nodes. | No Event 006 icon warning. |
| Imported Event 006 package focus icons | The prior Event 006 overlay audit records 121 unique Event 006 icon references with normal and `_shine` assets. | No icon patch justified. |
| Generic continuous-focus palette | Current inspect reports the generic `continuous_restrict_freedom` localisation/asset-family warning under game files. | Unrelated to Event 006; not patched. |

No icon ids or GFX files changed.

## Localisation and reward mismatch list

No Event 006 focus localisation or reward mismatch was identified by this layout pass.

The current MCP warning `continuous_restrict_freedom_desc` belongs to the vanilla generic continuous-focus palette and is explicitly outside the Event 006 scope.

No localisation keys changed.

## AI behavior gaps

All inspected Event 006 focus definitions retain `ai_will_do` blocks in the current source package, and no AI weights were changed.

The mandatory `chaosx_ai_probability_auditor` route was not invoked because this pass made no weighted-logic or AI edit.

## Validation and blockers

The mandatory national-tree `hoi4.focus_inspect` and `hoi4.focus_render` calls both completed successfully and report no blocking diagnostics, zero crossings, and zero node intersections.

Focus-specific lint/validate MCP routes are not exposed in this runtime; the inspect diagnostics are therefore the available lint-equivalent evidence.

No live HOI4 launch was performed.

No commit was created because the source tree was intentionally left unchanged for parent review.

## Parent handoff

Parent review should treat the seven warnings as a queued geometry-design decision rather than as safe one-line fixes.

If a future pass wants to remove them, it should trial each affected lane with the full focus inspect/render comparison and preserve the current zero-crossing and zero-node-intersection baseline; it should not move only one endpoint of warnings 1, 3, or 7.

