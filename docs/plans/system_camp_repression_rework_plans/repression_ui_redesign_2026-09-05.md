# Repression interface redesign

The interface uses a dark HOI4 administration window with five navigation entries: Situation, Territories, Sites, Policy, and Accountability.
The paper ledger, horizontal tab strip, repeated dossier cards, and detached action bar are absent from the active GUI.

## Acceptance and disposition

The user explicitly requested a complete repression UI redesign, removal of the ledger presentation, and active MCP GUI previews.
The parent accepted the native 960×600 sidebar and adjacent location-order layout within that authorization; the user did not separately approve pixel geometry.
The presentation design is promoted into the accepted Part 6 spec on that basis.
The implementation disposition is `implemented`, supported by the four runtime files below, the interaction and text audits, and the final production MCP evidence.
This disposition retains the tooling and data limits stated below and does not assert in-game validation.

## Implementation

- `interface/camp_repression_ledger.gui`: 960×600 movable window, native panels and buttons, a 500×104 category header, two scrolling location lists, selected-location orders, country directives, and accountability rows.
- `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`: presentation visibility, selected-row highlights, and two indexed dynamic-list selectors replacing twelve fixed selectors.
- `localisation/english/camp_repression_ui_l_english.yml`: concise page copy, empty states, contextual guidance, and compact resource costs.
- `common/scripted_localisation/camp_repression_ui_scripted_localisation.txt`: selected-location text and independently evaluated resource-cost colors.

The legacy window and action identifiers remain compatibility bindings.
They do not select or display the former ledger artwork.
The existing bounded arrays still hold up to 24 locations; each viewport displays six rows.
Selecting a row uses its array index in country scope and runs the existing selected-state validator.
Entering either location page clears the previous target after the existing display rebuild, preventing a territory selection from becoming a stale site order target.
An empty location list hides the detail card, while a nonempty list without a selected target supplies one selection instruction.

Situation emphasizes civilian-loss pressure, administrative strain, and surviving evidence.
Labor contribution and resistance remain available through focused tooltips.
Territories and Sites put context orders beside the selected location.
Policy contains four country directives and the existing guard and quota controls.
Accountability separates exposure and evidence, recorded deaths, and closure pressure.

## Preserved behavior and resource display

The source comparison in `ui_review_2026-09-05/action-preservation.json` checks 35 existing non-selector click handlers and availability gates against the captured baseline.
Thirty-three are unchanged after whitespace normalization; the two location-navigation handlers only add the selected-target reset described above.
No gameplay effect, payment, AI weight, timing, country route, or recurring hook was changed by this task.

Each displayed resource evaluates its own affordability.
Insufficient resources use red amounts; satisfied resources retain their normal color even when an unrelated condition disables the action.
Labor projects display the immediate payment while their tooltip explains the larger retained-reserve requirement.
Expansion command power and infantry equipment are eligibility requirements rather than debits in the existing expansion consumer.
All debited resource types remain visible, with at most four cost entries per action.
Selected-location costs group complete amount-and-icon pairs into two lines where needed.
Restricted-method costs use the existing abstract payload texticon; their existing detailed tooltips retain the equipment identity.

## MCP review evidence

The parent used the production HOI4 MCP inspect, render, and rewrite routes during the redesign.
Baseline inspection and initial replacement previews used the full Chaos Redux workspace.
Repeated full-workspace calls later exceeded the MCP client's 180-second timeout.
Final visual review therefore uses a bounded source snapshot with the production `hoi4-agent-tools` 3.0.7 MCP stdio server and the installed vanilla assets.
This review snapshot is not installed as mod content.

The snapshot contains copies of the runtime GUI, scripted GUI, and localisation files.
`ui_review_2026-09-05/runtime-source-hashes.json` records the exact runtime bytes used for final review.
`ui_review_2026-09-05/final-source-comparison.json` links those reviewed bytes to the committed source after trailing-whitespace cleanup and verifies that all four runtime files are otherwise identical.
`ui_review_2026-09-05/scenario-fixtures.json` records the explicit presentation inputs, chosen localisation branches, location names, selected states, disabled controls, resource shortages, and scroll position.
These fixtures exercise presentation; they do not claim to execute gameplay triggers.
The separate interaction and localisation audits cover those source contracts.

The production rewrite route produced before, proposed, and visual-difference images.
Its transaction writer failed post-validation on unresolved native sprite references in its general index and restored the review snapshot.
The proposed GUI scene itself resolved the native sprites through the GUI renderer.
The runtime source changes were applied through normal file editing and checked with subsequent read-only MCP renders and inspection.
The failed writer transaction is retained as a tooling limitation, not represented as a successful MCP write.

Final artifacts and tool outcomes are indexed by `ui_review_2026-09-05/mcp-evidence.json`.
The visual cases cover all five pages, no active sites, a long selected name with unavailable orders, the last six entries of a 24-location list, and the category header.
The resolution comparison uses 1920×1080 and 1280×720 scenarios.
All nine render cases returned `GUI_RENDERED`; the exact final source inspection returned `GUI_INSPECTED`, with no blockers.
The parent visually reviewed the rendered pages, selected and empty states, long-name wrapping, cost icons, last six list entries, and category header.
The retained diagnostics are not a zero-warning claim.
They include intentionally left-aligned navigation labels, panel/label/selection-overlay intersections, hidden-page elements and rows outside the scroll viewport, native tiled-sprite declaration dimensions, and the blank close button's font-metric lookup.
The reviewed click-region image shows separate navigation, row-selection, and order targets within their visible controls.
The offline renderer does not execute native button shaders or fully model `click_to_front`; those remain fidelity limits of this evidence.

Issues corrected during preview include the selection pane appearing on the wrong page, orphan decorative bindings, missing snapshot dependencies, redundant empty-state copy, long-name spacing, and cost icon token boundaries.
Colored icon entries terminate the icon name with whitespace before the color reset so the reset cannot become part of the icon identifier.

## Assets and documentation

The runtime references installed `GFX_tiled_window_2b_border`, `GFX_tiled_window_small`, `GFX_tiled_window_small_selectable`, `GFX_button_148x34`, `GFX_button_238x38`, and `GFX_closebutton` sprites.
Existing resource texticons remain wired through their existing GFX definitions.
No replacement panel art or copied vanilla textures are installed by this task.
The old ledger asset definitions remain unused compatibility assets; the active window has no references to them.

Part 4, Part 6, the GUI prompt, and the documentation handoff identify the current presentation contract.
Dated reports describing the former ledger remain historical evidence.
The localisation and interaction handoffs record their bounded review findings and resolutions.
The interaction audit's stale-target finding is resolved by the two navigation resets and the preserved action-gate comparison.
The labor reserve distinction is explained in the detailed requirement flow and the focused cost tooltip.
The inherited array bound remains a disclosed limit rather than being promoted to an unlimited-list claim.

## Simplifications, omissions, and limits

No requested gameplay or UI feature was replaced with placeholder content.
There are no design simplifications relative to the requested interface redesign.
The existing 24-entry data bound remains unchanged.
This inherited bound can exclude later valid locations from the GUI array; this task exposes all entries supplied to the UI and does not redesign that data builder.
MCP previews are offline GUI evidence; this task does not claim a live game session.
The MCP transaction-writer limitation is recorded above.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and `chaos-redux-event-assets`.
No skills were created or modified by this task.
