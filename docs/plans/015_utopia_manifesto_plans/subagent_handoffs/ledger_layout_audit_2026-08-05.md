# Event 015 Commonwealth Ledger layout and decision-category audit

## Scope and result

Audited the Event 015 Commonwealth Ledger scripted-GUI surface, its nine decision categories, linked ledger effects, and the relevant English localisation.

Patched one concrete UI defect: long live accounting strings were placed in fixed `118x58`, `306x204`, and `268x204` text boxes, so routine long bands and the detailed contribution/calling breakdowns clipped.

The compact visible summary now fits the surface and retains every live number in a hover tooltip.

No decision reward, cost, duration, mission, route gate, or AI score was changed.

## Changed files and identifiers

| File | Changed identifiers | Before | After |
| --- | --- | --- | --- |
| `interface/015_utopia_manifesto_ledger.gui` | `utopia_ledger_need_value`, `utopia_ledger_plenty_value`, `utopia_ledger_concord_value`, `utopia_ledger_assignment_value`, `utopia_ledger_overview_right`, `utopia_ledger_callings_left`, `utopia_ledger_callings_right` | Detailed, variable-length content relied on fixed-size visible boxes. | Each affected text box has a matching `pdx_tooltip`; the existing GUI layout and scripted actions are unchanged. |
| `localisation/english/015_utopia_manifesto_l_english.yml` | `utopia_manifesto_ledger_gui_need[_tt]`, `plenty[_tt]`, `concord[_tt]`, `assignment[_tt]`, `overview_right[_tt]`, `callings_left[_tt]`, `callings_right[_tt]` | Top values showed label, value, band, and delta in 58 pixels; two panels showed thousands of characters of contribution data. | Top values show their label and current number; compact panels show the current method/summary; the original current band, delta, and accounting details are available on hover. |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `on_puppet`, `on_release_as_puppet`, `on_release_as_free`, `on_subject_free`, `on_subject_autonomy_level_change`, `on_subject_annexed` | Subject-derived Need and Concord values could remain stale until Recount or another unrelated Event 015 callback. | Each bounded subject lifecycle callback refreshes the accepted ROOT and accepted FROM countries without a recurring scan. |

The four top-value tooltips describe their own current contribution sources, while the two Calling indicators tooltips retain the full U/P/S/D/T records.

## GUI wiring, geometry, and category lifecycle

The decision category `utopia_manifesto_ledger_category` correctly loads `utopia_manifesto_ledger_container` through `utopia_manifesto_ledger_scripted_gui` with `context_type = decision_category`.

The ledger has five actionable GUI buttons, all with a matching scripted GUI effect and click gate: `Recount` calls `utopia_manifesto_refresh_ledger` plus the three proof refreshes, and the four tabs set `utopia_manifesto_ledger_tab` to an existing script constant.

There are no fake action buttons, orphaned effects, or decorative elements over a control in this surface.

The background asset is an exact `700x500` panel, matching the clipping container.

| Ledger region | Bounds inside the `700x500` surface | Audit result |
| --- | --- | --- |
| Header | `0,0` through `700,96` | Header art, title, subtitle, identity marks, and formation state are contained. |
| Status strip | `0,96` through `700,154` | Four value slots use `118x58` boxes; the patch removes their variable band/delta overflow. |
| Tab rail | `31..646,156..190` | Four `123x34` buttons have 41-pixel gaps and matching tab effects. |
| Active panel | `24,202` through `676,424` | Exactly one tab panel is visible; the long overview and Calling detail text was the concrete clipping defect fixed here. |
| Footer | `0,430` through `700,486` | Warning art/text and `Recount` do not exceed the panel bounds. |

The default/missing tab state selects Overview, and `utopia_manifesto_clear_ledger_runtime` clears both `utopia_manifesto_ledger_visible` and `utopia_manifesto_ledger_tab`; stale panel state is therefore cleaned when the ledger ends.

The category priority ordering is deliberate and correct: Ledger `1100`, District `1099`, Island `1098`, Necessary Ground `1097`, Stewardship `1096`, League `1095`, Defense `1094`, Governance `1093`, and Formation `1092`.

## Issue list, sorted by severity

### Resolved — lifecycle changes refresh the Ledger for both humans and AI

`Recount` remains an explicit idempotent presentation action, but it is no longer the only path that can refresh subject-derived values.

`common/on_actions/015_utopia_manifesto_on_actions.txt` now refreshes the accepted ROOT and accepted FROM countries on `on_puppet`, `on_release_as_puppet`, `on_release_as_free`, `on_subject_free`, `on_subject_autonomy_level_change`, and `on_subject_annexed`.

These are bounded engine callbacks for the exact countries whose subject status changed. War, peace, capitulation, annexation, peace-conference, and state-control callbacks already refresh the relevant accepted countries. No daily, weekly, monthly, or world scan was added.

The GUI remains intentionally human-only (`is_ai = no`, `ai_enabled = no`); AI ledger consumers receive the same event-scoped refreshes without a fake GUI action.

### Medium — selected tabs lack a persistent selected treatment

The selected tab changes panel visibility but the four tab buttons all use the same normal static button sprite and do not expose a selected overlay/frame.

This is a readability gap, not a broken action.

It requires a small visual-state/art decision rather than a safe audit-only source tweak, so it remains unpatched.

### Resolved — variable ledger data clipped in fixed text boxes

The visible top values and Overview/Callings detail blocks could not reliably fit their fixed dimensions, particularly with `Commonwealth in Plenty`, full accounting variables, and three Calling records.

The visible text has been reduced to readable current summaries and all removed detail is preserved in localised hover tooltips.

### Low — offline GUI fidelity has unrelated repository limitations

The post-patch inspector reports `585` modelled, `2` approximated, `41` ignored, `1` missing, and `12` unresolved nodes.

Its source graph also has global diagnostics and overlap findings from unrelated scripted GUI files.

The bounded inline diagnostics contain no Event 015 ledger reference error, but the linked MCP artifacts should be used if a project-wide GUI repair is undertaken.

## Decision and mission quality notes

| Property | Audit note |
| --- | --- |
| Owner | The current country; the GUI is player-only while the category/decisions retain their normal country scope. |
| Category and region | The Ledger category is national; state-targeted projects use their own controlled/core-state requirements. |
| Requirements | Foundation and route flags, ledger/public-state flags, controlled territory, campaign status, material stores, and existing proof helpers gate the relevant actions. |
| Costs | Ledger actions use custom cost/availability helpers and varied political, equipment, transport/train, manpower, and project requirements rather than a flat passive political-power store. Tab buttons have no cost because they are presentation-only; Recount is an idempotent recalculation rather than a reward. |
| Duration and outcomes | The Ledger category contains 27 decisions and 11 missions. Mission durations use the Event 015 variable/helper pattern, with completion and cleanup effects in the linked decision/effect files. No duplicate mission identity was observed in this bounded category audit. |
| Failure and cleanup | The runtime-clear helper removes ledger visibility and tab state; mission/project cleanup remains owned by the existing Event 015 helpers. No click-to-reward, equipment-farming, war-goal, core, or cooldown bypass was found in the GUI surface. |
| AI and route locks | GUI tab actions need no AI equivalent because they only select a panel. Event-scoped lifecycle callbacks refresh AI ledger consumers without a fake GUI action. Category priority and route locks are consistent with the shared Event 015 flow. |

## Localisation and tooltip notes

All twelve `pdx_tooltip` keys referenced by the ledger GUI resolve in the Event 015 English localisation file.

The localisation remains UTF-8 with BOM.

The patch removes no player-facing information: dynamic band, delta, contributions, Calling methods, and all U/P/S/D/T values remain localised in hover text.

## MCP artifact evidence

Post-patch inspection and rendering used workspace `mod_chaos_redux_ea3b2d67c2c0`, source revision `caf9e1026358776d45afc2924e327db0e1f69fdeb6ec0500eab0bc115ffeea4b`.

- Inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62091e30121f14cdf181a1b56a74234fd7927576ed24b0f0f9e0ad49ab2d2f1f/3d96bb45ff3a0637e35227533b883059fa464ada0c8478030faeb56154aabe5f/gui-inspect.caf9e1026358776d.json`.
- State matrix: `utopia_manifesto_ledger_container-state-matrix.png`, SHA-256 `947ee2687b6f79cfc444d4031600d5d5ab920c08ab84f0a49c4ad8e0aafd1552`.
- Resolution scale: `utopia_manifesto_ledger_container-resolution-scale.png`, SHA-256 `f13819a980abb3d066938cbb54f21fe0a0d412ed2157ae403493c107d7b014d8`.
- Click regions: `utopia_manifesto_ledger_container-click-regions.png`, SHA-256 `24fee08fe3f8563ae548e8f851c8e32a18c834a38b87de2862327177c8437e23`.
- Fidelity: `utopia_manifesto_ledger_container-fidelity.json`, SHA-256 `bc399d994f1262fdc105d2a4d375c86f6e7f1bf524af83216dbb626bd280fb13`.

The render matrix covered `normal`, `hover`, `selected`, `warning`, `long-text`, and `missing-localisation` at `1280x720` and `1920x1080`, both at UI scale `1`.

The generic offline scenario produced `stateCount = 6`, `resolutionCount = 2`, and no pixel difference between its generic states.

This confirms the render requests and geometry traversal, but it does not simulate a live Event 015 country with active variables, warning flags, or a selected-tab sprite state.

## Validation and limits

Validated the targeted source diff, all GUI tooltip-to-localisation references, and the localisation BOM.

Inspected the post-patch GUI graph and rendered the requested state/resolution matrix.

Skipped live game validation and dynamic campaign-state rendering: the user owns live consumer validation, and the MCP default scenario has no active Event 015 ledger variables.

No new fallback, mechanic, asset, mission, or broad event chain was introduced.

## Recommended parent follow-up

1. Decide whether the four tabs need a selected-state frame/overlay and, if accepted, source/register the needed state treatment before a narrow GUI patch.
