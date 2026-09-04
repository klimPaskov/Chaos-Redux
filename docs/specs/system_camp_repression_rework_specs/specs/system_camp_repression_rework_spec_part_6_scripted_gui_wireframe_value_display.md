# System Camp Repression Rework Spec, Part 6: Scripted GUI Redesign Wireframe and Exact Value Display Plan

Working feature id: `system_camp_repression_rework`

All GUI labels in this file are player-facing design labels or compatibility implementation ids, not final localisation. Final GUI text must be written in localisation files after implementation choices are known. This part defines the current sparse presentation, the values and actions exposed by it, the native interface surfaces reused, and the visibility and cleanup rules.

## Current presentation contract, 2026-09-04

The accepted presentation is a full replacement of the former paper-ledger composition. `repression_ledger_window` remains the compatibility window id, but its player-facing surface is a 960x600 dark vanilla HOI4 framed window using native tiled panels and buttons. The title is `Repression and Camps`, and the left navigation labels are Situation, Territories, Sites, Policy, and Accountability. The previous 900x560 ledger wireframe, old tab labels, parchment treatment, detached action bar, and visible card or table requirements are superseded in this source only and remain historical evidence in older plan reports. The current parent implementation and final report are tracked at `docs/plans/system_camp_repression_rework_plans/repression_ui_redesign_2026-09-05.md`. Gameplay, effects, costs, AI paths, arrays, and retained window, panel, navigation-mark, and action identifiers remain unchanged unless parent implementation evidence says otherwise. The user explicitly requested a complete UI redesign, removal of the ledger appearance, and active MCP previews. The parent accepted this native 960x600 sidebar and adjacent order layout within that authorization; the user did not separately approve pixel geometry. The design disposition is `promoted into an accepted spec` on this parent acceptance basis. The implementation disposition is `implemented`, with current runtime files, final MCP read-preview evidence, and the transaction-writer limitation recorded in the linked final report; this does not claim in-game validation.

## Presentation principle

The average player should not manage this system unless their country has active sites, inherited reform work, discovery pressure, or a country-specific crisis. The GUI should feel like an administrative command surface for a state system that already exists. It should not appear as a gamey optimization board for maximizing deaths.

Use two presentation layers:

1. A decision category header for the ordinary player-facing surface.
2. A player-opened scripted GUI window called `repression_ledger_window` for players who expand, reform, or investigate the network.

The decision category header remains required as a compact entry surface and fallback. The redesigned scripted GUI is the required full-window implementation target, and the header does not replace it. The header shows only the title, active institution, and current phase; Situation, location, Policy, and Accountability values appear in the window or existing tooltips through scripted localisation.

## Visibility gates

### Decision category visibility

The category should be visible only when one of these conditions is true:

- country has at least one active camp, labor, gulag, experiment, radicalized, or contaminated evidence site.
- country has dormant country-specific infrastructure and a meaningful survey, activation, or reform decision.
- country has discovery, tribunal, reform, redress, or dismantlement pressure.
- country is eligible for a country-specific route such as U.K. Raj, U.S. wartime security, Vichy North Africa, Italy Libya, Belgium Congo, Germany Auschwitz, Japan Pingfang, or Soviet gulag pressure.
- country has an active mission from this system.
- country has selected the show-managed-network toggle.

The category should hide when all active sites are closed, all missions are complete, no dormant or inherited route remains, and no discovery or reform memory requires action.

### Scripted GUI visibility

`repression_ledger_window` should be visible only from a decision-category button or scripted GUI toggle. It should not open automatically on monthly processing.

Open button conditions:

- human player controls the country.
- category is visible.
- country has at least one displayed value or action.
- no modal discovery or tribunal event is currently pending for the same country.

Close and cleanup:

- close when tag changes.
- close when country is annexed.
- clear selected state when the state is no longer controlled, no longer active, or no longer valid.
- clear the selected Policy context when its route becomes invalid.
- rebuild values on monthly pulse, decision click, state control change, discovery, dismantlement, and regime change.

AI should not need GUI clicks. Every GUI button must call a scripted effect that also has a decision or AI path.

## Main window wireframe

Compatibility window id: `repression_ledger_window`.

Target size: 960x600 pixels at the authored UI scale. The window should remain centered, movable where the existing interface pattern permits it, and readable at the parent-selected minimum-resolution scenarios.

The window uses a dark vanilla HOI4 frame, native tiled panel sprites, native button sprites, and the existing interface font family. It must not use parchment textures, paper-ledger decoration, copied game textures, custom replacement panel art, or a detached global action bar. Context actions belong inside the selected-location or Policy content pane, and the title bar owns only window chrome such as close.

### Layout sketch

```text
+--------------------------------------------------------------------------------+
| Repression and Camps       [Institution] [Current phase]             [X]     |
+----------------------+---------------------------------------------------------+
| SITUATION             | Situation                                               |
| TERRITORIES           | Three compact consequence panels                       |
| SITES                 |                                                         |
| POLICY                |                                                         |
| ACCOUNTABILITY        |                                                         |
|                      |                                                         |
+----------------------+---------------------------------------------------------+
```

The window header contains only the player-facing title, the active institution, and the current phase, with close control kept in the title bar.

The interface should use compact numbers, dark framed groups, and bounded rows. It should avoid long paragraph text inside the window. Detailed context belongs in the existing selected-state tooltip, tooltips, events, docs, and decision descriptions.

Territories and Sites use the same two-pane detail composition so the player can select a location without leaving the navigation context.

```text
+----------------------+---------------------------------------------------------+
| Location list        | Selected location                                      |
| Two-line name        | Selected name and site type                            |
| Two-line name        | Neutral review instruction                             |
| Two-line name        | [1] [2] [3] [4] [5] [6] context slots with cost rows  |
+----------------------+---------------------------------------------------------+
```

The left navigation rail is distinct from the location list. The location list appears only inside Territories or Sites and is never replaced by an unbounded world-state list. List rows contain names only; status, owner, pressure, and other details remain in the selected-state tooltip or the selected-location review context.

## Navigation labels and compatibility mapping

The new labels describe the player-facing information architecture. Compatibility is limited to the existing window, panel, navigation-mark, and action identifiers that the parent verifies in the runtime source. Removed `*_card` element ids are not retained, and raw legacy arrays remain internal unless explicitly named as the two bounded location arrays below.

| Player-facing navigation | Retained compatibility surfaces | Functional obligations carried forward |
| --- | --- | --- |
| Situation | Existing Situation panels and parent-verified navigation marks | Three compact consequence panels for civilian-loss pressure, administrative strain, and surviving evidence, with a warning state and tooltip detail |
| Territories | Existing Territories panel, navigation marks, `camp_gui_pool_states`, and action ids | Bounded location-name list and selected-location review pane |
| Sites | Existing Sites panel, navigation marks, `camp_gui_active_site_states`, and action ids | Bounded location-name list and selected-location review pane |
| Policy | Existing Policy panel, navigation marks, and action ids | Current institution, current course, four directive panels, and guard or quota controls |
| Accountability | Existing Accountability panel, navigation marks, and action ids | Three rows: exposure/evidence, recorded deaths, and closure/reform pressure |

No removed `*_card` element id is a current compatibility obligation. The parent may use native tiled groups for the three Situation panels, four Policy directive panels, and Accountability rows without restoring the former card ids.

## Required navigation surfaces

### Situation surface

Purpose: show the current national consequences of the network at a glance.

Use three compact summary panels and no state list on Situation.

| Summary panel | Displayed values | Tooltip breakdown |
| --- | --- | --- |
| Civilian-loss pressure | Current population-loss pressure and the recorded consequence summary | Current civilian-loss pressure, the resistance band, and inspection or closure guidance remain in the tooltip |
| Administrative strain | Current strain or warning band | Current strain, labor contribution, and guards or quotas guidance remain in the tooltip; no extra scalar burden row is required |
| Surviving evidence | Evidence or exposure state with a warning when discovery pressure is high | Records, failed concealment, inspections, redress, and dismantlement remain in the tooltip |

Situation does not render bounded state summaries. Location names and all state or site detail belong to Territories or Sites.

### Territories surface

Purpose: show the bounded territories where the administration can establish or extend detention without exposing protected-class target logic.

The left pane uses a scrollable dynamic list over the bounded `camp_gui_pool_states` array. The list may contain up to 24 entries while showing six viewport rows, with a visible selected-row highlight and an explicit empty state. Each row is a two-line location-name label with no status columns or values. When the list is empty, the right detail pane is hidden; when the list is nonempty but no row is selected, it shows a neutral selection instruction; when a row is selected, it shows the selected location name and applicable site type plus six context button slots with paired cost rows. The interface has no visible table or ledger columns.

The existing selected-state tooltip remains the detailed source for territory context and available actions. Do not promote its legacy details into list columns or additional visible panels.

Pool type display bands remain available in the existing selected-state tooltip only:

- Occupied non-core.
- Colonial or subject-administered.
- Non-core integrated.
- Country periphery.
- Strategic security zone.
- Political-opposition route marker.
- Core fallback.

Core fallback remains a tooltip warning when applicable. The tooltip should explain that output is lower and domestic damage is higher.

### Sites surface

Purpose: manage existing active states.

The left pane uses a scrollable dynamic list over the bounded `camp_gui_active_site_states` array. The list may contain up to 24 entries while showing six viewport rows, with a visible selected-row highlight and an explicit empty state. Each row is a two-line location-name label with no status columns or values. When the list is empty, the right detail pane is hidden; when the list is nonempty but no row is selected, it shows a neutral selection instruction; when a row is selected, it shows the selected location name and site type plus six context button slots with paired cost rows. The interface has no visible table or ledger columns.

The existing selected-state tooltip remains the detailed source for site context and the state-targeted action. The right pane does not duplicate its legacy details as status columns.

Registration validation should happen before display. Invalid active entries should show an emergency cleanup action for the player only if the state is relevant. Otherwise, script should silently unregister stale inactive entries.

### Policy surface

Purpose: show the active institution and current course, then expose four existing directive panels plus guard and quota controls without changing gameplay effects, costs, cooldowns, or AI paths.

Only the active institution and current course are shown in the Policy header. Four directive panels provide the existing route-specific actions, and guard or quota actions remain inline in the same pane with their normal cost rows. Country-specific mechanics continue through their existing decisions, effects, AI paths, and tooltips rather than becoming extra scalar display rows.

### Accountability surface

Purpose: summarize exposure, evidence, recorded deaths, closure, and reform pressure.

Use three compact status rows.
Location closure orders are on Sites, and country reform directives are on Policy.

| Status row | Display |
| --- | --- |
| Exposure and evidence | discovery state and surviving evidence band |
| Recorded deaths | civilian deaths total attributed to this system and responsibility guidance |
| Closure and reform pressure | current reform route and reform pressure |

Accountability is the only place that presents exposure or closure warnings as a dedicated status surface. Existing selected-state tooltips retain detailed responsibility, retreat, and action context without adding visible card ids or extra rows.

## Exact value display plan

All displayed values should be rebuilt through a single country-scoped refresh effect before the category header or GUI reads them.

Recommended effect id: `camp_rework_rebuild_display_values`.

Recommended display variables should be country-scoped unless marked global or state-scoped.

### Core display variables

| Display surface | Source value | Display rule |
| --- | --- | --- |
| Civilian-loss pressure | `display_camp_population_loss_pressure` | Primary Situation panel; show as a consequence summary and keep exact Deaths accounting in the Chaos Meter Deaths tab. |
| Administrative strain | Existing current-course strain and warning values | Support Situation panel; show the warning state while labor and resistance context remain in tooltips. |
| Surviving evidence | `display_camp_evidence_risk` and existing exposure state | Support Situation panel and Accountability exposure row; show a warning when discovery pressure rises. |
| Recorded deaths | Existing recorded Deaths total | Accountability recorded-deaths row; do not expose it as an optimization or efficiency value. |
| Closure and reform pressure | `display_camp_reform_pressure` and existing closure state | Accountability closure or reform row; related orders and costs are on Sites or Policy. |

### Country-specific display variables

Country-specific values remain owned by their existing decisions, effects, AI paths, and localisation. The current UI exposes the active institution, current course, four directive panels, and their action or tooltip context without adding extra scalar display rows.

### Bands and color identity

Use consistent bands across the three Situation panels, Accountability rows, and their tooltips.

| Band id | Numeric interpretation | Color direction | Use |
| --- | ---: | --- | --- |
| `camp_band_none` | 0 | neutral grey | no active pressure |
| `camp_band_low` | 1 to low threshold | muted green or pale neutral | manageable pressure |
| `camp_band_medium` | medium threshold | yellow | visible burden |
| `camp_band_high` | high threshold | orange | strong warning |
| `camp_band_severe` | severe threshold | red | crisis or discovery danger |
| `camp_band_critical` | critical threshold | dark red or flashing warning state if GUI supports it | large-network breakdown or tribunal danger |

Suggested color identity:

- civilian-loss pressure: red.
- administrative strain and warnings: orange.
- surviving evidence and exposure: purple or red when severe.
- closure and reform pressure: green.
- labor, resistance, guard, and rail context: tooltip-only colors that do not create additional visible rows.

### Display text and scripted localisation ids

Scripted localisation should return compact labels, not final prose.

Recommended ids:

| Scripted localisation id | Purpose |
| --- | --- |
| `GetCampNetworkPhaseName` | Displays dormant, active, expanded, radicalized, contaminated evidence, reform, discovery, or dismantled phase. |
| `GetCampPoolTypeName` | Displays state-pool type for the selected state. |
| `GetCampSiteTypeName` | Displays current site type. |
| `GetCampEvidenceBandName` | Displays evidence risk band. |
| `GetCampOverstretchBandName` | Displays overextension band. |
| `GetCampPopulationLossPressureName` | Displays consequence band for monthly population damage. |
| `GetCampReformRouteName` | Displays current reform route. |
| `GetCampCountryPanelName` | Displays the active country-specific panel label. |
| `GetCampBlockedCostSummary` | Displays compact met or not met cost summary. |
| `GetCampSelectedStateActionSummary` | Displays the selected state's available actions. |

Do not put final event-style prose inside scripted localisation. Use it to produce compact labels and dynamic numbers.

## Button plan

Every gameplay action button must retain its matching decision or AI path.
The selected-location pane reserves six context button slots with paired cost rows, including location closure orders, while country directives remain on Policy.
Navigation and location selectors only change presentation state.
There is no detached global action bar.

| Button id | Scope | Calls | Visible when | Cost display |
| --- | --- | --- | --- | --- |
| `camp_ui_pool_select`, `camp_ui_site_select` | dynamic state row, country assignment through ROOT | Assign the indexed state id and call `camp_rework_validate_selected_state` | Row supplied by the corresponding bounded array | none |
| `camp_gui_expand_selected_pool` | country with selected state | country-specific or generic expand effect | Selected state eligible, route active | icon-led cost summary |
| `camp_gui_start_labor_project` | country with selected state | country-specific labor project effect | Selected state supports construction, resource, or logistics output | transport and factory burden |
| `camp_gui_allocate_guards` | country with selected state or national | guard allocation effect | Overstretch or unrest pressure | manpower and equipment |
| `camp_gui_reduce_quotas` | country | reduce quota effect | Expanded labor network active | output loss and pressure reduction |
| `camp_gui_inspect_selected_site` | country with selected state | inspection effect | Reform route or discovery risk | political and factory burden |
| `camp_gui_dismantle_selected_site` | country with selected state | dismantlement effect | Active or discovered site, valid reform route | support equipment, factory burden, time |
| `camp_gui_destroy_evidence` | country with selected state | evidence destruction effect | Enemy proximity, undiscovered evidence, authoritarian route | command, equipment, stability, risk warning |
| `camp_gui_country_specific_primary` | country | route-specific effect | Country panel has primary action | dynamic cost summary |
| `camp_gui_close_window` | player context | GUI close effect | title bar visible | none |

Button availability tooltips must explain missing state pool, missing equipment, missing transport, reform freeze, discovered evidence, route lock, or core fallback penalties. The existing selected-state tooltip remains the detailed explanation for the selected location.

## Decision category header display

The category header is the compact entry surface for the full GUI.

Required header structure:

```text
Repression and Camps
[GetCampCountryPanelName]
[GetCampNetworkPhaseName]
```

The header contains only the title, active institution, and current phase. The open action is a separate category or title-bar control, and the Situation panels carry consequence values after the player opens the window.

## State selection and target-management pattern

Use a selected-state pattern to prevent decision spam.

Recommended storage:

- country variable `camp_selected_state_id` for current selected state id.
- state flag `camp_selected_by_current_country` only if needed for decision visibility.
- optional event target `camp_selected_state` only inside a short effect chain, never as a scripted-GUI data source.
- no global event target unless implementation proves it needs persistence, and if used it must be cleaned.

Flow:

1. Player clicks state selector or GUI row.
2. Script stores selected state id.
3. Category or GUI rebuilds the selected-location details pane.
4. Only actions for that selected state become visible.
5. When state becomes invalid, selected state clears.

Territories and Sites navigation resets the selected state after a display-list rebuild; a subsequent row click establishes the current selection again.

AI does not use selected-state UI. AI evaluates all valid states through hidden decisions, scripted effects, or weighted target loops.

## Visual and asset boundary

The current GUI uses native HOI4 frame, tiled panel, and button surfaces with parent-verified window, panel, navigation-mark, and action identifiers. Native selection highlighting and text warning states are sufficient for the current sparse layout.

This spec does not require custom replacement panel, card, background, copied-texture, status-sprite, or animation art. Existing decision-category or action icons follow their own consumers, while GUI asset decisions and `.gfx` or `.gui` wiring remain parent-owned and are tracked with the final report at `docs/plans/system_camp_repression_rework_plans/repression_ui_redesign_2026-09-05.md`.

## Data rebuild order

Use this order whenever the category header or GUI is refreshed:

1. Clean invalid active site registrations.
2. Recalculate the active institution and current course.
3. Recalculate civilian-loss pressure, administrative strain, surviving evidence, recorded deaths, and closure or reform pressure.
4. Recalculate selected-state validity.
5. Rebuild the bounded Territories and Sites location-name lists for visible rows.
6. Rebuild the six selected-location context slots and their cost rows.
7. Rebuild scripted localisation display values.

Do not run this as a separate whole-world daily loop. Tie it to existing monthly pulse, state-control changes, decision clicks, opening the GUI, and relevant country or state events.

## GUI arrays

Recommended arrays for visible lists:

| Array | Scope | Contents |
| --- | --- | --- |
| `camp_gui_pool_states` | country | state ids for the Territories dynamic location list, bounded to 24 entries with six viewport rows |
| `camp_gui_active_site_states` | country | active site state ids for the Sites dynamic location list, bounded to 24 entries with six viewport rows |

Keep both arrays bounded at 24 entries, show six viewport rows, provide an explicit empty state, and render names only in list rows. Other shared subsystem arrays remain internal and feed selected-state tooltips, scripted effects, or cost resolution rather than visible list columns.

## Internal values

Raw evidence, burden, death-calculation, AI-weight, responsibility-pointer, script-constant, and random-roll values remain internal implementation data. They are not current UI obligations and must not become visible rows, columns, cards, or debug surfaces in the player window.

## Acceptance criteria for UI

- Category header contains only the `Repression and Camps` title, active institution, and current phase while the custom GUI is closed.
- The custom GUI opens only on player action.
- Average player with no active route sees no category clutter.
- Values are visible as consequences and recognizable conditions, not implementation telemetry or optimization curves.
- The 960x600 window uses a dark vanilla HOI4 frame with native tiled panels and buttons.
- The left navigation labels are Situation, Territories, Sites, Policy, and Accountability.
- Situation contains three compact panels: civilian-loss pressure as the primary consequence, administrative strain as supporting context, and surviving evidence with its warning state; the harm tooltip contains current civilian-loss pressure, the resistance band, and inspection or closure guidance, and the strain tooltip contains current strain, labor contribution, and guards or quotas guidance.
- Situation does not render bounded state summaries.
- Territories and Sites each use a scrollable dynamic location-name list over the existing bounded arrays on the left, up to 24 entries with six viewport rows, selected-row highlight, and explicit empty state; an empty list hides the right detail pane, and a nonempty unselected list shows a neutral selection instruction.
- Territories and Sites show the selected name and site type plus six context button slots with paired cost rows on the right, with detailed context remaining in the selected-state tooltip.
- Territories and Sites do not expose visible status or table or ledger columns.
- Policy shows the active institution, current course, four existing directive panels, and guard or quota actions with their existing costs and AI or decision equivalents.
- Accountability shows three rows for exposure/evidence, recorded deaths, and closure/reform pressure.
- No parchment cards, copied game textures, custom replacement panel art, or detached global action bar appear in the redesigned window.
- Ordinary text remains inside its fixed box at long-text and minimum-resolution review states.
- State list is bounded and does not show every world state.
- Buttons have AI equivalents or decision equivalents.
- Tooltips explain missing costs and blocked conditions.
- Exposure, recorded deaths, closure, and reform routes are readable.
- No recurring minor flavor popup is created by monthly processing.
- GUI cleans selected state and invalid arrays after state-control change, dismantlement, or annexation.
- Existing window, panel, navigation-mark, and action identifiers remain available for compatibility even when player-facing labels use the new navigation names; removed `*_card` element ids are not retained.
