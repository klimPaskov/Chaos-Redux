# System Camp Repression Rework Spec, Part 6: Scripted GUI Wireframe and Exact Value Display Plan

Working feature id: `system_camp_repression_rework`

All GUI labels in this file are working labels and implementation ids, not final localisation. Final GUI text must be written in localisation files after implementation choices are known. This part defines what the player sees, how values are calculated for display, which buttons exist, which sprites are needed, and how the GUI stays hidden for ordinary players.

## Live implementation reconciliation, 2026-07-11

The optional/deferred wording below records the original implementation plan. The full `repression_ledger_window` is live with Overview, State Pools, Active Sites, Country System, and Discovery & Reform tabs. The header displays `[ROOT.GetName]: [GetCampCountryPanelName]` plus phase and discovery state; all 32 Ledger country action slots use their native decision cooldown gates. All 24 ImageGen-derived static sprites have live consumers, including scripted visibility for evidence and reform seals. The maintained static presentation is not a fallback or simple-shape substitute. Only authored frame animation remains optional and queued.

## Presentation principle

The average player should not manage this system unless their country has active sites, inherited reform work, discovery pressure, or a country-specific crisis. The GUI should feel like a ledger and command surface for a state system that already exists. It should not appear as a gamey optimization board for maximizing deaths.

Use two presentation layers:

1. A decision category header for the ordinary player-facing surface.
2. An optional scripted GUI window called `repression_ledger_window` for players who expand, reform, or investigate the network.

The decision category header is required. The scripted GUI is recommended when implementation capacity allows it. If the custom GUI is deferred, all values listed here still need to appear through decision-category scripted localisation and targeted tooltips.

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
- clear selected country-specific tab when route becomes invalid.
- rebuild values on monthly pulse, decision click, state control change, discovery, dismantlement, and regime change.

AI should not need GUI clicks. Every GUI button must call a scripted effect that also has a decision or AI path.

## Main window wireframe

Recommended window id: `repression_ledger_window`.

Recommended size target: close to the existing Chaos Redux movable window scale if available. The window should fit the standard HOI4 interface without hiding the decision list entirely.

### Layout sketch

```text
+--------------------------------------------------------------------------------+
| Header: country name, current phase, close button                               |
|--------------------------------------------------------------------------------|
| Summary strip                                                                   |
| Reach | Active sites | Labor output | Population loss pressure | Evidence risk  |
| Stability drag | Resistance pressure | Guard burden | Rail burden | Reform       |
|--------------------------------------------------------------------------------|
| Left column: tabs and state pools          | Right panel: selected tab content   |
|                                            |                                      |
| [Overview]                                 | Overview cards                       |
| [State Pools]                              | Active site list or pool list         |
| [Active Sites]                             | Selected state card                   |
| [Country System]                           | Country-specific values               |
| [Discovery and Reform]                     | Discovery, tribunal, reform actions   |
|--------------------------------------------------------------------------------|
| Bottom action bar: expand, allocate guards, reduce quotas, dismantle, inspect   |
+--------------------------------------------------------------------------------+
```

The interface should use compact numbers and icon-led tooltips. It should avoid long paragraph text inside the window. Detailed context belongs in tooltips, events, docs, and decision descriptions.

## Required tabs

### Overview tab

Purpose: show the current national state of the network.

Cards:

| Card id | Displayed values | Tooltip breakdown |
| --- | --- | --- |
| `repression_ledger_reach_card` | Network reach, active site count, phase | Sites by type, country-specific routes, dormant markers excluded |
| `repression_ledger_output_card` | Labor output, construction pressure, resource pressure | Output by selected allocation, state pool, overextension penalty |
| `repression_ledger_damage_card` | Monthly population loss pressure, stability drag, resistance pressure | Deaths-tab reason, state modifiers, radicalized or contaminated evidence flags |
| `repression_ledger_burden_card` | Guard burden, rail burden, convoy burden, supply strain | Manpower, infantry equipment, support equipment, trains, trucks, convoys |
| `repression_ledger_evidence_card` | Evidence risk band, discovery status, tribunal severity band | Evidence from sites, destroyed evidence, failed cover-up, liberated evidence |
| `repression_ledger_reform_card` | Reform pressure, dismantlement progress, active review missions | Court review, postwar inquiry, colonial inspection, local administration route |

### State Pools tab

Purpose: tell the player where actions will draw from without exposing protected-class target logic.

Columns:

| Column | Source |
| --- | --- |
| State | `[THIS.GetName]` in state scope |
| Pool type | scripted localisation from pool trigger match |
| Controller | state controller |
| Owner receiving population loss | state owner or configured local owner |
| Responsible country | stored `genocide_responsible_country` or proposed ROOT before activation |
| Eligibility | valid, blocked by core fallback, blocked by no route, blocked by discovery, blocked by reform freeze |
| Expected burden | low, medium, high, severe based on state and route |
| Available actions | expand, labor project, guard allocation, dismantle, inspect |

Pool type display bands:

- Occupied non-core.
- Colonial or subject-administered.
- Non-core integrated.
- Country periphery.
- Strategic security zone.
- Political-opposition route marker.
- Core fallback.

Core fallback should display a severe warning band. The tooltip should explain that output is lower and domestic damage is higher.

### Active Sites tab

Purpose: manage existing active states.

Columns:

| Column | Source |
| --- | --- |
| State | state name |
| Site type | concentration, forced labor, radicalized, gulag, experiment-linked, contaminated evidence, destroyed evidence |
| Registration | active, dormant, destroyed, discovered, invalid |
| Monthly population loss pressure | projected band and Deaths reason |
| Labor output | current state contribution |
| Resistance pressure | local pressure band |
| Evidence state | hidden, exposed, destroyed, failed cover-up, liberated |
| Enemy proximity | safe, threatened, contested, enemy controlled |
| Action | state-targeted button or selected state details |

Registration validation should happen before display. Invalid active entries should show an emergency cleanup action for the player only if the state is relevant. Otherwise, script should silently unregister stale inactive entries.

### Country System tab

Purpose: show country-specific mechanics only when they exist.

Country panels:

| Country package | Values shown | Buttons |
| --- | --- | --- |
| Germany | Mengele autonomy band, permission level band, Auschwitz status, experiment-linked site count | military review, transfer prisoners, close Auschwitz program, dismantle Auschwitz complex |
| Japan | Ishii influence, Kwantung autonomy, Pingfang facility level, outbreak accident risk band, occupied China evidence depth | army review, shut down experiments, evacuate records, containment office |
| Soviet Union | gulag reach, NKVD authority, paranoia band, famine pressure, Union Crisis suppression relief cap | reduce paranoia, famine relief, purge administrators, dismantle overextended camps |
| U.K. | imperial detention reach, Raj burden, dominion control pressure, Indian autonomy resistance | reform administration, release prisoners, postwar Raj review |
| U.S. | wartime security reach, civil-liberties damage, court challenge pressure, redress pressure | court review, terminate authority, redress commission |
| France or Vichy | camp legacy, Vichy collaboration reach, North Africa labor burden, refugee pressure | inspect legacy, open review, dismantle North Africa network |
| Italy | colonial repression reach, desert camp burden, Libyan resistance pressure, colonial logistics output | close desert camps, compensation route, transport guard |
| Belgium | Congo extraction pressure, concession labor burden, colonial resource output, accountability pressure | inspection, concession reform, local administration recognition |
| Generic users | network reach, labor output, overextension, reform pressure | expand, guard, dismantle, evidence action |

Only one country panel should display at a time. Generic panel should be used only when no country-specific panel applies or when a country uses the generic route in addition to a small inherited package.

### Discovery and Reform tab

Purpose: explain consequences and cleanup.

Cards:

| Card id | Display |
| --- | --- |
| `repression_discovery_status_card` | undiscovered, partial evidence, discovered, severe discovery, tribunal preparation |
| `repression_condemnation_card` | responsible country condemnation band and latest change if visible |
| `repression_deaths_card` | civilian Deaths total attributed to this system and latest monthly change band |
| `repression_reform_route_card` | available reform route, current mission, remaining duration, blocked costs |
| `repression_retreat_risk_card` | enemy proximity and evidence destruction availability |

Discovery and reform tab should be the only place that mentions tribunal severity bands. Ordinary expansion decisions can warn about future evidence risk, but they should not read like legal paperwork.

## Exact value display plan

All displayed values should be rebuilt through a single country-scoped refresh effect before the category header or GUI reads them.

Recommended effect id: `camp_rework_rebuild_display_values`.

Recommended display variables should be country-scoped unless marked global or state-scoped.

### Core display variables

| Display variable | Source calculation | Display format | Display rule |
| --- | --- | --- | --- |
| `display_camp_network_reach` | count of active registered sites plus weighted active buildings | integer | show `0` only when category is already visible for reform or dormant route |
| `display_camp_active_site_count` | active registered sites with valid current condition | integer | exclude dormant markers |
| `display_camp_concentration_sites` | site type count | integer | show in tooltip |
| `display_camp_radicalized_sites` | site type count | integer | show in tooltip with severe warning band |
| `display_camp_gulag_sites` | site type count | integer | show for Soviet and generic gulag routes |
| `display_camp_experiment_sites` | experiment-linked site count | integer | show only for Germany, Japan, or other explicit experiment route |
| `display_camp_contaminated_evidence_sites` | contaminated evidence site count | integer | show only after route unlock or discovery risk |
| `display_camp_labor_output` | state local labor output, allocation multipliers, overextension penalty | band and numeric percent | show as construction or extraction pressure, not as killing efficiency |
| `display_camp_coercive_control` | site reach, guard allocation, local resistance context | band and numeric percent | show as short-term control pressure |
| `display_camp_population_loss_pressure` | monthly state death pressure sum before application | band plus approximate count range if deaths system exposes it | show as consequence pressure, never as resource efficiency |
| `display_camp_stability_drag` | national stability damage from active ideas and values | signed percent | show negative when active |
| `display_camp_resistance_pressure` | country and state resistance pressure | band | show local breakdown in state tooltip |
| `display_camp_guard_burden` | manpower and equipment burden | icon summary plus tooltip | show missing burden in red |
| `display_camp_rail_burden` | train, truck, convoy, and supply burden | icon summary plus tooltip | show severe when transport shortage exists |
| `display_camp_evidence_risk` | evidence level, visibility, enemy proximity, destroyed or failed cover-up state | band | show as risk band, exact hidden values in debug only |
| `display_camp_foreign_visibility` | foreign observer pressure and discovered evidence | band | show only after active expansion or discovery |
| `display_camp_tribunal_severity` | condemnation, evidence, deaths, repeat discoveries | band | show in Discovery and Reform tab only |
| `display_camp_reform_pressure` | reform route, regime change, democratic pressure, court review, colonial review | band | show when reform actions exist |
| `display_camp_overstretch` | reach, guard shortage, rail shortage, stability drag, resistance pressure | band and numeric score | show warning above high threshold |

### Country-specific display variables

| Variable | Country package | Display rule |
| --- | --- | --- |
| `display_mengele_autonomy_band` | Germany | Use banded display, exact variable can stay hidden unless debug mode is active |
| `display_mengele_permission_band` | Germany | Show rejected, restricted, full, bypass, or closed as a banded status |
| `display_auschwitz_site_status` | Germany | Show dormant, labor, radicalized, experiment-linked, facility-linked, discovered, dismantled |
| `display_ishii_influence_band` | Japan | Show only when Ishii route is visible |
| `display_kwantung_autonomy_band` | Japan | Show only when occupied China or Manchuria pool exists |
| `display_pingfang_facility_level` | Japan | Show facility level or inactive state, not final prose |
| `display_outbreak_accident_risk_band` | Japan | Show risk band tied to research pressure and containment, not operational details |
| `display_gulag_reach` | Soviet Union | Show as gulag reach or dormant background depending on phase |
| `display_paranoia_band` | Soviet Union | Read existing paranoia system where possible |
| `display_famine_pressure_band` | Soviet Union | Show only once famine pressure is possible or active |
| `display_union_crisis_repression_relief_band` | Soviet Union | Show cap and warning if relief no longer works |
| `display_raj_labor_burden_band` | U.K. | Show Raj burden when Raj or India pool is active |
| `display_indian_autonomy_resistance_band` | U.K. | Show in U.K. panel when it is affected |
| `display_civil_liberties_damage_band` | U.S. | Show always while U.S. authority is active or redress pressure remains |
| `display_court_challenge_pressure_band` | U.S. | Show if court review can start or has started |
| `display_vichy_collaboration_reach_band` | France or Vichy | Show only for Vichy or authoritarian route |
| `display_north_africa_labor_burden_band` | France or Vichy | Show when North Africa route active |
| `display_desert_camp_burden_band` | Italy | Show in Italy panel when Libya or East Africa route active |
| `display_congo_extraction_pressure_band` | Belgium | Show when Congo route active |
| `display_congo_accountability_pressure_band` | Belgium | Show after inspection, discovery, or decolonization pressure |

### Bands and color identity

Use consistent bands across the category and GUI.

| Band id | Numeric interpretation | Color direction | Use |
| --- | ---: | --- | --- |
| `camp_band_none` | 0 | neutral grey | no active pressure |
| `camp_band_low` | 1 to low threshold | muted green or pale neutral | manageable pressure |
| `camp_band_medium` | medium threshold | yellow | visible burden |
| `camp_band_high` | high threshold | orange | strong warning |
| `camp_band_severe` | severe threshold | red | crisis or discovery danger |
| `camp_band_critical` | critical threshold | dark red or flashing warning state if GUI supports it | large-network breakdown or tribunal danger |

Suggested color identity:

- labor output: muted construction yellow.
- coercive control: blue grey.
- population loss pressure: red.
- stability drag: orange.
- resistance pressure: dark red.
- evidence risk: purple.
- reform pressure: green.
- guard and rail burden: equipment icon colors.
- country-specific danger values: use the same color as their consequence, not a new color for every country.

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

Every clickable GUI button must call a scripted effect with matching decision or AI path.

| Button id | Scope | Calls | Visible when | Cost display |
| --- | --- | --- | --- | --- |
| `camp_gui_select_state` | state | `camp_rework_select_state_for_display` | State row is valid | none |
| `camp_gui_expand_selected_pool` | country with selected state | country-specific or generic expand effect | Selected state eligible, route active | icon-led cost summary |
| `camp_gui_start_labor_project` | country with selected state | country-specific labor project effect | Selected state supports construction, resource, or logistics output | transport and factory burden |
| `camp_gui_allocate_guards` | country with selected state or national | guard allocation effect | Overstretch or unrest pressure | manpower and equipment |
| `camp_gui_reduce_quotas` | country | reduce quota effect | Expanded labor network active | output loss and pressure reduction |
| `camp_gui_inspect_selected_site` | country with selected state | inspection effect | Reform route or discovery risk | political and factory burden |
| `camp_gui_dismantle_selected_site` | country with selected state | dismantlement effect | Active or discovered site, valid reform route | support equipment, factory burden, time |
| `camp_gui_destroy_evidence` | country with selected state | evidence destruction effect | Enemy proximity, undiscovered evidence, authoritarian route | command, equipment, stability, risk warning |
| `camp_gui_country_specific_primary` | country | route-specific effect | Country panel has primary action | dynamic cost summary |
| `camp_gui_close_window` | player context | GUI close effect | window open | none |

Button availability tooltips must explain missing state pool, missing equipment, missing transport, reform freeze, discovered evidence, route lock, or core fallback penalties.

## Decision category header display

The category header must remain useful even without custom GUI.

Required header structure:

```text
Current phase: [GetCampNetworkPhaseName]
Network reach: [?display_camp_network_reach]
Active sites: [?display_camp_active_site_count]
Labor output: [GetCampLaborOutputDisplay]
Population loss pressure: [GetCampPopulationLossPressureName]
Stability drag: [GetCampStabilityDragDisplay]
Resistance pressure: [GetCampResistancePressureName]
Evidence risk: [GetCampEvidenceBandName]
Guard and transport burden: [GetCampBurdenSummary]
Reform pressure: [GetCampReformPressureName]
```

For countries with no active network but with reform or dormant route, replace output and damage lines with dormant or reform summaries. Do not show zero-heavy debug lines to ordinary players.

## State selection and target-management pattern

Use a selected-state pattern to prevent decision spam.

Recommended storage:

- country variable `camp_selected_state_id` for current selected state id.
- state flag `camp_selected_by_current_country` only if needed for decision visibility.
- optional event target `camp_selected_state` only inside a short effect chain.
- no global event target unless implementation proves it needs persistence, and if used it must be cleaned.

Flow:

1. Player clicks state selector or GUI row.
2. Script stores selected state id.
3. Category or GUI rebuilds selected-state card.
4. Only actions for that selected state become visible.
5. When state becomes invalid, selected state clears.

AI does not use selected-state UI. AI evaluates all valid states through hidden decisions, scripted effects, or weighted target loops.

## Warning and animation states

Animated assets are optional but recommended for the ledger because state changes matter. If animation is implemented, follow the frame-animation skill. The final game asset must be a frame sheet with static fallback, not a GIF.

Recommended visual states:

| Sprite id | Static fallback | Animated state | Use |
| --- | --- | --- | --- |
| `GFX_repression_ledger_warning_frame` | `GFX_repression_ledger_warning_frame_static` | pulsing border when overextension is high | Overview and Discovery tabs |
| `GFX_repression_ledger_evidence_seal` | `GFX_repression_ledger_evidence_seal_static` | slow seal movement when evidence is discovered | Discovery card |
| `GFX_repression_ledger_reform_seal` | `GFX_repression_ledger_reform_seal_static` | soft glow when reform route is available | Reform card |
| `GFX_repression_ledger_selected_state_frame` | `GFX_repression_ledger_selected_state_frame_static` | subtle highlight when a selected state has valid action | Selected state card |
| `GFX_repression_ledger_critical_frame` | `GFX_repression_ledger_critical_frame_static` | severe danger pulse when critical breakdown or enemy proximity exists | Bottom action bar |

Static presentation is acceptable for the first implementation if the GUI still displays all values and buttons clearly. Do not request animation if the custom GUI is not being implemented.

## Asset id plan for GUI

| Asset id | Type | Size direction | Use |
| --- | --- | --- | --- |
| `GFX_decision_category_repression_ledger` | decision category icon | follow existing decision category pattern | category entry |
| `GFX_decision_open_repression_ledger` | decision icon | 32x32 | open GUI button |
| `GFX_repression_ledger_window_bg` | UI panel | match existing Chaos Redux window scale | main GUI background |
| `GFX_repression_ledger_tab_overview` | UI icon | compact tab icon | overview tab |
| `GFX_repression_ledger_tab_state_pools` | UI icon | compact tab icon | state pool tab |
| `GFX_repression_ledger_tab_sites` | UI icon | compact tab icon | active sites tab |
| `GFX_repression_ledger_tab_country` | UI icon | compact tab icon | country panel tab |
| `GFX_repression_ledger_tab_discovery` | UI icon | compact tab icon | discovery and reform tab |
| `GFX_repression_ledger_population_pressure` | UI icon | 24x24 or existing pattern | population loss pressure card |
| `GFX_repression_ledger_labor_output` | UI icon | 24x24 or existing pattern | labor output card |
| `GFX_repression_ledger_evidence_risk` | UI icon | 24x24 or existing pattern | evidence risk card |
| `GFX_repression_ledger_reform_pressure` | UI icon | 24x24 or existing pattern | reform pressure card |
| `GFX_repression_ledger_guard_burden` | UI icon | 24x24 or existing pattern | guard burden card |
| `GFX_repression_ledger_rail_burden` | UI icon | 24x24 or existing pattern | rail burden card |

Do not generate final assets until the implementation agent confirms exact GUI dimensions and target `.gfx` or `.gui` files.

## Data rebuild order

Use this order whenever the category header or GUI is refreshed:

1. Clean invalid active site registrations.
2. Recalculate site counts by type.
3. Recalculate country-specific values.
4. Recalculate state pool availability counts.
5. Recalculate national output, burden, damage, evidence, and reform values.
6. Recalculate selected-state validity.
7. Rebuild GUI arrays for visible rows.
8. Rebuild scripted localisation display values.

Do not run this as a separate whole-world daily loop. Tie it to existing monthly pulse, state-control changes, decision clicks, opening the GUI, and relevant country or state events.

## GUI arrays

Recommended arrays for visible lists:

| Array | Scope | Contents |
| --- | --- | --- |
| `camp_gui_pool_state_ids` | country | state ids for eligible pools |
| `camp_gui_pool_type_ids` | country | numeric pool type for each row |
| `camp_gui_pool_eligibility_ids` | country | valid or blocked state |
| `camp_gui_active_site_state_ids` | country | active site state ids |
| `camp_gui_active_site_type_ids` | country | site type by row |
| `camp_gui_active_site_evidence_ids` | country | evidence state by row |
| `camp_gui_active_site_pressure_ids` | country | pressure band by row |
| `camp_gui_active_site_action_ids` | country | primary action id by row |
| `camp_gui_country_value_ids` | country | country-specific panel rows |
| `camp_gui_country_value_band_ids` | country | band for each country-specific row |

Keep arrays bounded. Do not push every world state. Rebuild only states in active site array or country-specific eligible pool arrays.

## Debug-only values

The implementation may need debug displays while testing, but they must not remain in ordinary player UI.

Debug-only values:

- raw evidence score.
- raw hidden atrocity score.
- raw monthly death calculation before clamping.
- raw AI weights.
- raw responsible-country pointer id.
- raw script constant values.
- raw random rolls for discovery or cover-up.

If debug UI is added, gate it behind existing debug setting or a development-only flag and document removal before completion.

## Acceptance criteria for UI

- Category header shows current values without requiring the custom GUI.
- Custom GUI, if implemented, opens only on player action.
- Average player with no active route sees no category clutter.
- Values are visible as consequence and management pressure, not as optimization curves.
- State list is bounded and does not show every world state.
- Buttons have AI equivalents or decision equivalents.
- Tooltips explain missing costs and blocked conditions.
- Discovery and reform routes are readable.
- No recurring minor flavor popup is created by monthly processing.
- GUI cleans selected state and invalid arrays after state-control change, dismantlement, or annexation.
