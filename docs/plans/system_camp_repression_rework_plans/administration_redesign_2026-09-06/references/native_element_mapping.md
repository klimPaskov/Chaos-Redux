# Camp administration reference-to-native element mapping

This map reflects the current native source in `interface/camp_repression_ledger.gui` after the parent’s accepted edits. `Existing` IDs below are present in the source; `Proposed` controls are design suggestions only and are not implemented. The reference image is a visual guide, so where it separates values that the native source groups together, the difference is called out explicitly.

## Shared frame and navigation

| Reference region | Text or action | Native element | Status |
|---|---|---|---|
| Window header | Camp Administration | `camp_admin_title` | Existing |
| Close action | close button | `camp_gui_close_window` | Existing |
| Administration tab | click target | `camp_admin_tab_administration` | Existing |
| Administration tab | text label | `camp_admin_tab_label_administration` | Existing |
| Administration tab | selected-state marker | `camp_admin_mark_administration` | Existing |
| Locations tab | click target | `camp_admin_tab_locations` | Existing |
| Locations tab | text label | `camp_admin_tab_label_locations` | Existing |
| Locations tab | selected-state marker | `camp_admin_mark_locations` | Existing |
| Records tab | click target | `camp_admin_tab_records` | Existing |
| Records tab | text label | `camp_admin_tab_label_records` | Existing |
| Records tab | selected-state marker | `camp_admin_mark_records` | Existing |

## Administration

| Reference region | Label element | Value or action element | Notes |
|---|---|---|---|
| Economic contribution card | `camp_admin_contribution_label` | `camp_admin_contribution_value` | Separate label/value controls exist. |
| People in custody card | `camp_admin_detainees_label` | `camp_admin_detainees_value` | Separate label/value controls exist. |
| Assigned workforce card | `camp_admin_workforce_label` | `camp_admin_workforce_value` | Separate label/value controls exist. |
| Deaths this month card | `camp_admin_deaths_label` | `camp_admin_deaths_value` | Separate label/value controls exist. |
| Economic priority selector | `camp_admin_priority_label` | `camp_admin_choose_priority` | The selector button displays the current priority. |
| Repression mandate selector | `camp_admin_mandate_label` | `camp_admin_choose_mandate` | The selector button displays the current mandate. |
| Spending ceiling selector | `camp_admin_budget_label` | `camp_admin_choose_budget` | The selector button displays the current spending ceiling. |
| Economic development card title | `camp_admin_economy_label` | — | Existing label control. |
| Economic development status | — | `camp_admin_economy_summary` | Existing control; text key is `camp_admin_economy_status`. |
| Economic development location | — | `camp_admin_economy_place` | Existing separate value control. |
| Economic development progress | — | `camp_admin_economy_progress` | Existing separate value control. |
| Institutional program card title | `camp_admin_institution_label` | — | Existing label control. |
| Institutional program status | — | `camp_admin_institution_summary` | Existing control; text key is `camp_admin_institution_status`. |
| Institutional program location | — | `camp_admin_institution_place` | Existing separate value control. |
| Institutional program progress | — | `camp_admin_institution_progress` | Existing separate value control. |
| Authorize administration action | button label is its text | `camp_admin_country_action_one` | Active only while the shared authority and resource predicate passes. |
| Authorization unavailable state | button label is its text | `camp_admin_country_action_one_locked` | Separate neutral native control with a contextual reason and the existing monthly quote in its tooltip; no click effect. |
| Close and release action | button label is its text | `camp_admin_country_action_two` | Active only while the shared review or reform predicate passes. |
| Release unavailable state | button label is its text | `camp_admin_country_action_two_locked` | Separate neutral native control with a contextual reason; generic reform quotes its current full Political Power cost. |

The Administration reference shows a pre-authorization state with 0% output, 200 thousand in custody, 0 assigned workers, 1.24 thousand deaths this month, and no authorized project or institutional program. The successful MCP Administration baseline is a separate legacy-network scenario with 20% output, 200 thousand in custody, 130 thousand assigned workers, and a Brandenburg contract at 62% completion; the reference premise is that these inherited records coexist with an action to authorize a separate new paid authority.

## Locations

| Reference region | Label element | Value or action element | Status and notes |
|---|---|---|---|
| Locations panel | — | `camp_admin_locations_panel` | Existing panel. |
| Location filter | visible text is the button label | `camp_admin_filter_button` | Existing control. |
| Location roster | — | `camp_admin_location_list_scroll`, `camp_admin_location_list` | Existing scroll and grid/list controls. |
| Selected roster row | — | `camp_admin_location_selected`, `camp_admin_location_selected_marker` | The selected-only noninteractive background and gold marker sit within the row; `camp_admin_location_select` remains the click target. |
| Selected site heading | — | `camp_admin_selected_name` | Existing control; the image selects Brandenburg. |
| Primary role | `camp_admin_selected_role_label` | `camp_admin_selected_role` | Existing label/value pair. |
| Industrial contribution | `camp_admin_selected_contribution_label` | `camp_admin_selected_contribution` | Existing label/value pair. |
| People in custody | `camp_admin_selected_custody_label` | `camp_admin_selected_custody_value` | Existing label/value pair. |
| Assigned workforce | `camp_admin_selected_workers_label` | `camp_admin_selected_workers_value` | Existing label/value pair. |
| Site support | `camp_admin_selected_support_label` | `camp_admin_selected_support_value` | Existing label/value pair. |
| Deaths this month | `camp_admin_selected_deaths_label` | `camp_admin_selected_deaths_value` | Existing label/value pair. |
| Deaths recorded here | `camp_admin_selected_total_deaths_label` | `camp_admin_selected_total_deaths_value` | Existing separate cumulative pair. |
| Capacity | `camp_admin_selected_capacity_label` | `camp_admin_selected_capacity_value` | Existing label/value pair. The corrected Locations v3 reference and current-source fixture show 18 thousand for the selected site. |
| Site condition/status | — | `camp_admin_selected_condition_status` | Existing value element. The v4 `GetCampAdminSelectedConditions` branch names unreconciled positive custody before ordinary supply status. |
| Pause or resume work | button label is its text | `camp_admin_site_work`, `camp_admin_site_work_locked`, `camp_admin_site_work_locked_empty`, `camp_admin_site_work_locked_purpose`, `camp_admin_site_work_locked_mandate` | Mutually exclusive native controls share the rectangle. The active action requires living labor or penal custody and a coercive mandate; each locked control has a separate blocked-reason tooltip and no click effect. The reference shows active `Pause Work`. |
| Change purpose | button label is its text | `camp_admin_site_role`, `camp_admin_site_role_locked` | Two mutually exclusive native controls share the rectangle. The locked control names absent operating-site authority in its own tooltip and has no click effect. The reference shows active `Change Purpose`. |
| Release survivors | button label is its text | `camp_admin_site_release`, `camp_admin_site_release_locked`, `camp_admin_site_release_locked_site`, `camp_admin_site_release_locked_empty`, `camp_admin_site_release_locked_records` | Mutually exclusive native controls share the rectangle. The locked variants explain absent release authority, absent operating-site authority, zero living custody, or unreconciled living rows in separate tooltips and have no click effect. The v4 records-state reference shows a neutral `Release Locked` face; v2 and v3 show active Release Survivors only with valid rows. |
| Dismantle site | button label is its text | `camp_admin_site_dismantle`, `camp_admin_site_dismantle_locked_site`, `camp_admin_site_dismantle_locked_route`, `camp_admin_site_dismantle_locked_progress`, `camp_admin_site_dismantle_locked_custody`, `camp_admin_site_dismantle_locked_resources` | The `camp_admin_locations_resource_locked_reference_v3.png` displays `Closure Locked` for an insufficient current quote while custody rows remain reconciled. Five neutral native controls explain the first blocking condition; only the separate active control has a click effect. The v2 active action can also be valid with living custody because an accepted dismantlement start releases those survivors. |

The synthetic selected-site values are 14,800 in custody, 9,620 assigned workers, 100% support, 1.24 equivalent factories, 74 deaths this month, and 345 cumulative deaths. The final image shows no map thumbnail. Its roster omits East Prussia from the visible viewport because the generated spelling was incorrect; native list content remains controlled by the GUI data.
The v3 reference arranges the four contextual controls in one row. The native usable rectangles are x=18, 150, 282 and 414, y=340, each 120×38 within the selected-site panel; active and locked variants share their own rectangle, and adjacent click faces have 12-pixel gaps. The [three-scale MCP resource fixture](../mcp/locations_resource_locked_actions_2026-09-27.md) is the intended native comparison; the earlier custody-only fixture is rejected.

## Records

| Reference region | Label element | Value element | Status and notes |
|---|---|---|---|
| Records panel | — | `camp_admin_records_panel` | Existing panel. |
| Human consequences heading | — | `camp_admin_records_heading` | Existing heading. |
| Cause column heading | — | `camp_admin_records_cause_heading` | Existing heading. |
| Month column heading | — | `camp_admin_records_month_heading` | Existing heading. |
| Cumulative column heading | — | `camp_admin_records_total_heading` | Existing heading. |
| Custody cause row | `camp_admin_records_custody_label` | `camp_admin_records_custody_month`, `camp_admin_records_custody_total` | Existing label/month/total controls. |
| Labor cause row | `camp_admin_records_labor_label` | `camp_admin_records_labor_month`, `camp_admin_records_labor_total` | Existing label/month/total controls. |
| Site-violence cause row | `camp_admin_records_violence_label` | `camp_admin_records_violence_month`, `camp_admin_records_violence_total` | Native label/month/total controls; the label has a separate `camp_admin_records_violence_tt` tooltip showing killing-center arrival losses as a nonadditive subset. |
| Institutional cause row | `camp_admin_records_institutional_label` | `camp_admin_records_institutional_month`, `camp_admin_records_institutional_total` | Existing label/month/total controls. |
| Occupation violence row | `camp_admin_records_wider_label` | `camp_admin_records_wider_month`, `camp_admin_records_wider_total` | Existing label/month/total controls; the value is measured campaign violence. |
| All-causes total row | `camp_admin_records_all_label` | `camp_admin_records_all_month`, `camp_admin_records_all_total` | Existing label/month/total controls. |
| Original authority | `camp_admin_records_authority_label` | `camp_admin_records_authority_value` | Existing label/value controls. |
| Record retention/status | `camp_admin_records_retention` | text is the element value | Existing control. |
| Institutional history heading | — | `camp_admin_history_heading` | Existing heading. |
| History list | — | `camp_admin_history_list_scroll`, `camp_admin_history_list` | Existing scroll and grid/list controls. |
| History row container | — | `camp_admin_history_row` | Existing repeated row. |
| History entry kind/text | — | `camp_admin_history_row_title` | Existing row value control. |
| History date | — | `camp_admin_history_row_date` | Existing separate row value control. |
| History location | — | `camp_admin_history_row_place` | Existing separate row value control. |
| Empty-history state | — | `camp_admin_history_empty` | Existing control. |

The current records layout exposes country-level cause rows, not a per-site origin breakdown. The final reference follows that limit and must not be described as showing a native state-by-state or location-by-location loss registry.

The source variable families for monthly rows are `camp_admin_month_custody_deaths_k`, `camp_admin_month_labor_deaths_k`, `camp_admin_month_violence_deaths_k`, `camp_admin_month_institutional_deaths_k`, and `camp_occ_month_deaths_k`. Cumulative totals use `camp_admin_total_custody_deaths_k`, `camp_admin_total_labor_deaths_k`, `camp_admin_total_violence_deaths_k`, `camp_admin_total_institutional_deaths_k`, and `camp_occ_total_deaths_k`.

The synthetic history entries use supported kinds `authority`, `budget`, and `economic_project`. Death values belong in the cause table, not in a `Deaths recorded` history event.

## Maintenance shortage

| Reference region | Label element | Value or action element | Status |
|---|---|---|---|
| Crisis panel | — | `camp_admin_crisis_panel` | Existing embedded panel; the reference is not a separate modal. |
| Shortage heading | — | `camp_admin_crisis_heading` | Existing heading. |
| Country support ratio | `camp_admin_crisis_support_label` | `camp_admin_crisis_support_value` | Existing separate label/value controls. |
| Deferred development | `camp_admin_crisis_development_label` | `camp_admin_crisis_development_value` | Existing separate label/value controls. |
| Shortage explanation | — | `camp_admin_crisis_description` | Existing explanatory value control. |
| Review Spending action | button label is its text | `camp_admin_crisis_budget` | Existing action. |
| Defer New Projects action | button label is its text | `camp_admin_crisis_pause`, `camp_admin_crisis_pause_locked` | Mutually exclusive native controls share the action rectangle. The active order retains its existing guarded effect; the already-paused state says `Projects Deferred`, has a direct blocked-reason tooltip and no click effect. |

The shortage view uses the current support ratio, deferred-development state, and two native actions. No per-site material-origin breakdown, stock amount, reserve duration, affected-site count, named works list, or modal is implied.

## Purpose picker locked state

The [scoped locked-state reference](killing_role_locked_reference_2026-09-26.md) maps the bottom-right role option to the active `camp_admin_option_role_killing` button and six mutually exclusive native locked variants. The active option uses the exact role-availability trigger and click effect; every locked option shares its rectangle, displays `Killing Center Unavailable` with a reason-specific requirements/cost tooltip, and has no click effect. No scripted-localisation expansion remains in that tooltip.
