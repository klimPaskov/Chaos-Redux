# Repression UI interaction audit

Audit snapshot: 2026-09-05. Scope was the live shared repression scripted GUI and its location selectors in `interface/camp_repression_ledger.gui` and `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, compared with `.tmp/repression_ui_20260904/baseline/`. This audit covers interaction preservation, selector scoping, visibility and enabled gates, visible costs, empty and long-list behavior, lifecycle, and cleanup. It does not validate the unchanged repression balance, effects, AI weights, or the whole gameplay system.

## Findings sorted by severity

### Medium: selection can remain valid across the Territories and Sites pages

The live selectors correctly write `camp_gui_pool_states^camp_ui_pool_index` or `camp_gui_active_site_states^camp_ui_site_index` on the country root and then call `camp_rework_validate_selected_state` (`common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, selector effects near lines 59-69). The selection variable is not cleared by the tab click effects, however. After selecting a Territory and opening Sites with at least one Site, the detail card can still present the old selected state because the validator checks the underlying state registries rather than membership in the currently displayed GUI array. The reverse transition has the same stale-context behavior.

The existing action click-enabled gates and route effects still recheck their original state and route conditions, so this does not provide a gameplay or cost bypass. It can present disabled actions, or leave the player looking at a valid state that has no highlighted row on the active page. Clear `camp_selected_state_id` when switching between the two location pages, or require current-page array membership in `camp_ui_selected_location_visible` and each location-action presentation gate. Keep the existing validator and effect gates unchanged.

### Medium: the 24-entry array cap has no overflow or total-count signal

Both dynamic lists use the requested six-row viewport and expose up to 24 entries through `camp_gui_pool_states` and `camp_gui_active_site_states` (`common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, dynamic lists near lines 523-537). The array builders stop appending at `constant:camp_rework_gui_limit.pool_rows` or `active_site_rows`, both currently 24 (`common/scripted_effects/camp_repression_rework_effects.txt` and `common/script_constants/camp_repression_rework_constants.txt`). The scrollbar reaches all entries that made it into the array, and the empty labels and greater-than-six scroll hints are correctly scoped.

If more than 24 valid locations exist, later locations have no selector and are inaccessible through this UI with no indication that the list is truncated. Add a visible total or overflow indicator, or add deterministic paging before treating 24 as a complete interaction surface. This is a UI coverage limitation and does not change the underlying arrays or gameplay actions.

### Low: labor reserve gating can look inconsistent in the collapsed cost row

The visible labor row shows the actual one-time debit of political power, motorized equipment, trains, and support equipment, while its red affordability helpers use the larger reserve-inclusive start requirement. The new tooltip distinguishes “paid now” from “required at the start including retained reserve” (`localisation/english/camp_repression_ui_l_english.yml`, `camp_ui_cost_labor` near line 50), and the underlying gate remains unchanged. A player who can pay the displayed debit but fails the reserve check can therefore see displayed amounts marked unavailable without the reason being visible until hover. A compact `paid now`/`reserve required` cue would make this state self-explanatory while preserving the existing payment logic.

### Low: long names and restricted payload identity depend on hover text

Location names are constrained to the row text width and height in `camp_repression_ledger.gui`; the selector tooltip supplies the full state name. Chemical and biological compact rows show the amount and restricted-payload icon, while their existing detailed tooltips retain payload identity. The production render should confirm that the tooltip is reachable for clipped names and that the compact payload rows are understandable at the target resolution. A visible count or short payload name would improve accessibility if the render shows truncation.

No high-severity interaction or gameplay bypass was found in the current source snapshot.

## Old-to-new selector and action coverage

The former six static pool selectors and six static site selectors are replaced by two indexed dynamic selectors:

- `camp_gui_select_pool_1` through `camp_gui_select_pool_6` are replaced by `camp_ui_pool_list` with `array = camp_gui_pool_states`, `index = camp_ui_pool_index`, `value = camp_ui_pool_state`, `change_scope = yes`, and `entry_container = "camp_ui_pool_row"`.
- `camp_gui_select_site_1` through `camp_gui_select_site_6` are replaced by `camp_ui_site_list` with the corresponding `camp_gui_active_site_states` array and `camp_ui_site_index`.
- `camp_ui_pool_select_click` and `camp_ui_site_select_click` only copy the indexed state into `camp_selected_state_id` and invoke the existing validator. They do not debit resources, start missions, change flags, or dispatch actions.
- The row click gates are always enabled because the row is a selector, and the changed scope plus `ROOT` assignment targets the country root while the indexed array value identifies the selected state.
- The selected-row visibility checks compare `camp_selected_state_id` with the matching array entry, so a selected row highlights only when it is the current entry in that list.

The parent comparison reports 35 existing non-selector operational handlers and enabled gates unchanged against `.tmp/repression_ui_20260904/action-preservation.json`. The old static selector effects and four orphan decoration triggers were removed, but no operational action handler was removed. The selected-location action card retains the existing route handlers for expansion, labor, inspection, dismantlement, evidence destruction, chemical, biological, guards, quotas, and policy directives.

## Decision-category lifecycle notes

The scripted GUI remains a player-only `player_context` window attached to `top_bar` with `ai_enabled = { always = no }`. Root visibility still requires a human eligible for the repression category, the open flag, and the category-visible action. Opening clears tab flags, selects the Situation page, and rebuilds display arrays and values. Closing clears the open and tab flags, selected state, and GUI arrays through the existing close effect.

The five sidebar tab effects clear sibling tab flags, set the selected tab, and rebuild display values. Action effects still route through the existing country-specific dispatch and rebuild display values after state changes. `camp_rework_validate_selected_state` removes an invalid or no-longer-controlled selection and repopulates the display values. The final `camp_ui_selected_location_visible` gate now also requires the active location page's array count to be greater than zero, so an empty Territories or Sites page does not leave a stale detail card visible.

The list builders exclude invalid, dismantled, active-site, and otherwise ineligible locations using the existing source logic before appending entries. The dynamic list definitions are nested under `camp_repression_ledger_scripted_gui`, which is required for the GUI to own and instantiate the lists. No selector path reaches a gameplay effect without the existing selected-state validation.

## Cognitive-load notes

The redesign presents five named views: Situation, Territories, Sites, Policy, and Accountability. Situation and Accountability are informational; Territories and Sites show a six-row viewport with scrolling; Policy shows the existing directive and guard/quota actions. The action card presents at most six location actions on a page, and the policy page remains within the six-action limit. The location rows contain names rather than raw variables or indices, and the selected card supplies the adjacent context and action choices.

Visible values have labels and current helper text for harm, strain, evidence, exposure, recorded deaths, and closure/redress. Harm and strain have tooltips describing consequences and relevant responses. The body text is concise enough for the panel; old detailed requirements remain in action tooltips and blocked summaries rather than being repeated in every row.

The remaining cognitive-load risks are the cross-page stale selection, the silent 24-entry truncation, and the labor reserve distinction described above. The absence of a numeric `shown/total` count makes scrollbar reachability less obvious for both six-plus and capped lists.

## Mission quality notes

This UI change adds no mission type, owner, category, region, requirement, duration, outcome, or cleanup path. The labor action still activates the existing `generic_labor_project_cycle` through the selected-state route, and the selected dismantlement action still uses `camp_gui_selected_dismantlement_mission` with the existing selected-state and active-site requirements, duration, success/failure effects, and cancellation cleanup. Existing active-mission and state-validity gates prevent duplicate activation through the new selectors. Because mission logic was not changed, this audit does not claim fresh balance or outcome validation for those missions.

## Cost and requirement clarity

The 13 visible cost rows cover seven selected-location actions, two general policy actions, and four directive/package slots. The maximum number of distinct consumed cost types remains four per action:

- Activation uses political power, manpower, command power, and support equipment.
- Expansion displays political power, manpower, support equipment, and trains. Command power and infantry equipment remain requirements in the existing gate and are not consumed by the expansion effect.
- Labor consumes political power, motorized equipment, trains, and support equipment immediately, with the existing reserve-inclusive start gate.
- Inspection uses political power; dismantlement uses political power, manpower, and support equipment; evidence destruction uses political power, manpower, command power, and support equipment.
- Chemical and biological actions each use political power plus a restricted payload type; guards use political power, manpower, command power, and infantry equipment; quotas use political power.
- Directive slots and their package variants remain at or below four consumed types, including the slot political-power cost.

Every displayed spendable value in the new English UI localisation has a matching texticon, including political power, manpower, command power, infantry, support, motorized equipment, trains, convoys, fuel, and restricted payload. The resource helper branches resolve the shortage state, and the current scripted-localisation reference check found no unresolved `GetCampUi...` helper or unused helper definition. Existing detailed action tooltips still carry the full requirement and blocked-reason text, including non-consumed expansion prerequisites.

## AI validity and route-lock notes

The new selectors are player interaction only and do not create an AI button or weight. AI decisions, monthly bridges, route weights, and action effects are outside the redesign diff. Each operational button retains its baseline click-enabled predicate, and the route dispatcher retains its original action and selected-state checks. Selecting a state through a dynamic row therefore cannot bypass control, active-site, eligibility, technology, cooldown, equipment, or mission gates. No dead-country or impossible-border target was introduced by the selector change.

No probability audit was required for this bounded review because no weighted logic or AI value changed. This handoff does not claim balance validation of the unchanged AI or repression system.

## Localisation and tooltip gaps

The new navigation, empty-state, selection, status, value, cost, and policy keys are present in `localisation/english/camp_repression_ui_l_english.yml`. The old action labels and detailed tooltips remain in `camp_repression_rework_l_english.yml`. The selector tooltip uses the current row scope and provides the full location name. The compact payload row is intentionally generic and relies on the existing hover tooltip for payload identity.

The only material wording gap found is the labor row's collapsed reserve explanation. The full tooltip covers it, but the row itself does not visibly label which amount is paid immediately versus retained as a start reserve. Verify this in the final production render and consider a short visible label if the distinction is not clear at a glance.

## Cleanup and exploit-risk notes

The selector effects contain no resource or gameplay effects and call the existing validator. Close cleanup clears selection and GUI arrays. Rebuild cleanup removes invalid active sites, reconstructs both arrays, and refreshes display values. Operational clicks still use the existing debits, flags, mission activation, cooldown, and dispatch logic. No free action, repeated-debit loop, mission duplication path, equipment farming path, or cooldown bypass was found in the GUI diff.

## Concrete recommended fixes

1. In `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, clear `camp_selected_state_id` when switching between Territories and Sites, or add current-array membership to the selected-card and location-action presentation gates. Retain the existing effect-level validation and enabled gates.
2. In `common/scripted_effects/camp_repression_rework_effects.txt` and `common/script_constants/camp_repression_rework_constants.txt`, pair the 24-entry cap with a visible total/overflow state or deterministic paging. If the cap is an accepted product constraint, expose that constraint to the player so valid locations are not silently hidden.
3. In `localisation/english/camp_repression_ui_l_english.yml`, add a compact paid-now/reserve-required cue to the labor cost row if production rendering shows the red reserve gate as an unexplained mismatch.
4. In `interface/camp_repression_ledger.gui` and the selector localisation, verify long state names at the production resolution and preserve a reachable full-name tooltip. Verify that the final scroll row remains clickable after an action-triggered array rebuild.

## Validation, evidence, and limits

Source review covered the live GUI, scripted GUI, existing effect and validator call sites, current English localisation, scripted-localisation helper references, constants, and the baseline comparison. The parent-provided action-preservation artifact is `.tmp/repression_ui_20260904/action-preservation.json`, reporting 35 preserved non-selector handlers/gates. The current source has two dynamic indexed selectors, the final empty-page presentation gate, and all current helper localisation references resolved.

The parent owns the mandatory `hoi4.gui_inspect` and `hoi4.gui_render` production evidence for this shared scripted GUI and reports a sparse exact-source render at 1280x720 with the missing texticon and user-text issues corrected. I did not issue a duplicate MCP call under the bounded handoff request, so this document does not independently certify pixel alignment, clipping, asset, or click-region appearance. In-game consumer validation remains parent/user-owned. No source or gameplay files were edited by this audit; only this handoff was written.

Remaining issues are the medium cross-page selection context, the silent 24-entry truncation, and the low-severity labor reserve and long-name accessibility concerns. No other simplification or gameplay change was made by this audit.

## Parent resolution after audit, 2026-09-05

The cross-page target finding is `implemented`: both location-navigation handlers clear `camp_selected_state_id` after the existing display rebuild.
The durable `../ui_review_2026-09-05/action-preservation.json` records 33 unchanged handler/gate bodies and two navigation-only reset additions, with no unexpected action changes.
Final MCP previews show the long location name within the row and detail bounds, complete cost pairs on explicit lines, an empty page without a stale detail card, and entries 19 through 24 reachable by scrolling.
The source tooltip explains the labor reserve distinction, while compact payload icons retain full identity in the existing detailed tooltip.
The existing 24-entry array bound remains unchanged and is disclosed in the final report; no unlimited-location claim is made.
These are parent-reviewed resolutions within the user-authorized UI redesign, not a claim that the read-only auditor made or reaudited the later patch.
The implementation evidence and production MCP tooling limits are recorded in `../repression_ui_redesign_2026-09-05.md`.
