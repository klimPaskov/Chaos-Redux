"""Build the GUI preview scenarios for the 2026-10-04 Repression and Camps render pass.

Values are already formatted to the precision the localisation shows, because the
preview substitutes raw values. Each scenario is a source fixture, not a save.
Run from this folder: python build_scenarios.py
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

PANELS = [
    'camp_admin_administration_panel', 'camp_admin_locations_panel', 'camp_admin_records_panel',
    'camp_admin_picker_priority', 'camp_admin_picker_budget', 'camp_admin_picker_mandate',
    'camp_admin_picker_role', 'camp_admin_picker_filter',
]

BASE_VALUES = {
    'This.GetName': 'Germany',
    'GetCampAdminContribution': '12.5% extraction',
    'GetCampAdminPriority': 'Resource Extraction',
    'GetCampAdminMandate': 'Intensified Coercion',
    'GetCampAdminBudget': 'Controlled Development',
    'GetCampAdminEconomyStatus': 'Resource Extraction',
    'GetCampAdminEconomyPlace': 'Generalgouvernement Distrikt Krakau',
    'GetCampAdminEconomyProgress': 'Work completed: 62%',
    'GetCampAdminInstitutionStatus': 'Institutional review',
    'GetCampAdminInstitutionPlace': 'Ostpreussen-Westpreussen Regierungsbezirk',
    'GetCampAdminInstitutionProgress': 'Funded progress: 40%',
    'GetCampAdminCountryAction1Name': 'Place allocation under SS authority',
    'GetCampAdminCountryAction2Name': 'Close camps and release survivors',
    'GetCampSelectedStateName': 'Ostpreussen-Westpreussen Regierungsbezirk',
    'GetCampAdminSelectedRole': 'Forced-labor institution',
    'GetCampAdminSelectedContributionValue': '1.24 equivalent factories',
    'GetCampAdminSelectedConditions': 'Survivor records are incomplete. Release, transfer and work orders are paused here.',
    'GetCampAdminSiteWorkLabel': 'Pause Work',
    'GetCampAdminFilter': 'All Locations',
    'camp_admin_total_detainees_k': 1186.4,
    'camp_admin_total_workforce_k': 742.9,
    'camp_admin_gui_month_deaths_k': 312.6,
    'camp_admin_gui_site_detainees_k': 148.2,
    'camp_admin_gui_site_workforce_k': 96.7,
    'camp_admin_gui_site_support_pct': 100,
    'camp_admin_gui_site_month_deaths_k': 4.213,
    'camp_admin_gui_site_total_deaths_k': 61.875,
    'camp_admin_gui_site_capacity_k': 180.0,
    'camp_admin_gui_country_support_pct': 64,
    'camp_admin_month_custody_deaths_k': 2.104,
    'camp_admin_total_custody_deaths_k': 120.512,
    'camp_admin_month_labor_deaths_k': 8.817,
    'camp_admin_total_labor_deaths_k': 412.25,
    'camp_admin_month_violence_deaths_k': 1.006,
    'camp_admin_total_violence_deaths_k': 230.75,
    'camp_admin_month_institutional_deaths_k': 0.033,
    'camp_admin_total_institutional_deaths_k': 6.66,
    'camp_occ_month_deaths_k': 300.64,
    'camp_occ_total_deaths_k': 4812.345,
    'camp_admin_gui_total_deaths_k': 5582.517,
}

LOCATION_ROWS = [
    ('Ostpreussen-Westpreussen Regierungsbezirk', 'Forced-labor institution', True),
    ('Upper Silesia', 'Killing center', False),
    ('Generalgouvernement Distrikt Krakau', 'Penal-labor institution', False),
    ('Saxony', 'Detention and internment', False),
    ('Lower Silesia', 'Forced-labor institution', False),
    ('Pomerania', 'Detention and internment', False),
    ('Brandenburg', 'Forced-labor institution', False),
    ('Lublin', 'Killing center', False),
]

HISTORY_ROWS = [
    ('Closed; survivors released with incomplete records', '4/1945', 'Ostpreussen-Westpreussen Regierungsbezirk'),
    ('Survivors escaped to Sweden', '10/1943', 'Zealand'),
    ('Survivors escaped to Sweden', '10/1943', 'Jutland'),
    ('Economic project completed', '8/1943', 'Generalgouvernement Distrikt Krakau'),
    ('Spending ceiling changed', '2/1943', 'Germany'),
    ('Material shortage recorded', '11/1942', 'Upper Silesia'),
    ('Institutional program completed', '6/1942', 'Brandenburg'),
]


def scenario(sid, description, view, resolution=(1280, 720), ui_scale=1, date='1943.11.1', shortage=False,
             empty_locations=False, empty_history=False, picker=None):
    visibility = {name: False for name in PANELS}
    visibility.update({
        'repression_ledger_window': True,
        'camp_admin_mark_administration': view == 'administration',
        'camp_admin_mark_locations': view == 'locations',
        'camp_admin_mark_records': view == 'records',
    })
    if picker:
        visibility['camp_admin_picker_' + picker] = True
    else:
        visibility['camp_admin_%s_panel' % view] = True
    visibility.update({
        'camp_admin_economy_panel': not shortage,
        'camp_admin_institution_panel': not shortage,
        'camp_admin_crisis_panel': shortage and view == 'administration' and not picker,
        'camp_admin_crisis_pause': True,
        'camp_admin_crisis_pause_locked': False,
        'camp_admin_country_action_one': not shortage,
        'camp_admin_country_action_one_locked': False,
        'camp_admin_country_action_two': False,
        'camp_admin_country_action_two_locked': not shortage,
        'camp_admin_location_empty': empty_locations,
        'camp_admin_selected_panel': not empty_locations,
        # The preview applies a window-level value to every list row, so the per-row
        # selection marker is set on the row itself and cleared here.
        'camp_admin_location_selected': False,
        'camp_admin_history_empty': empty_history,
        'camp_admin_site_work': False,
        'camp_admin_site_work_locked': False,
        'camp_admin_site_work_locked_empty': False,
        'camp_admin_site_work_locked_purpose': False,
        'camp_admin_site_work_locked_mandate': True,
        'camp_admin_site_role': True,
        'camp_admin_site_role_locked': False,
        'camp_admin_site_release': False,
        'camp_admin_site_release_locked': False,
        'camp_admin_site_release_locked_site': False,
        'camp_admin_site_release_locked_empty': False,
        'camp_admin_site_release_locked_records': True,
        'camp_admin_site_dismantle': False,
        'camp_admin_site_dismantle_locked_site': False,
        'camp_admin_site_dismantle_locked_route': False,
        'camp_admin_site_dismantle_locked_progress': False,
        'camp_admin_site_dismantle_locked_custody': True,
        'camp_admin_site_dismantle_locked_resources': False,
        'camp_admin_option_role_killing': False,
        'camp_admin_option_role_killing_locked': True,
        'camp_admin_option_role_killing_site_locked': False,
        'camp_admin_option_role_killing_existing_locked': False,
        'camp_admin_option_role_killing_level_locked': False,
        'camp_admin_option_role_killing_funds_locked': False,
        'camp_admin_option_role_killing_other_locked': False,
    })
    values = copy.deepcopy(BASE_VALUES)
    locations = [] if empty_locations else [
        {'This.GetName': name, 'GetCampAdminRowRole': role, 'camp_admin_location_selected.visible': selected}
        for name, role, selected in LOCATION_ROWS
    ]
    history = [] if empty_history else [
        {'GetCampAdminHistoryKind': kind, 'GetCampAdminHistoryPlace': place,
         'camp_admin_history_months^camp_admin_history_index': int(date_text.split('/')[0]),
         'camp_admin_history_years^camp_admin_history_index': int(date_text.split('/')[1])}
        for kind, date_text, place in HISTORY_ROWS
    ]
    return {
        'id': sid,
        'description': description + ' Source fixture, not a save.',
        'country': {'tag': 'GER'},
        'date': date,
        'resolution': {'width': resolution[0], 'height': resolution[1]},
        'uiScale': ui_scale,
        'state': 'normal',
        'language': 'l_english',
        'animationTimeSeconds': 0,
        'values': values,
        'visibility': visibility,
        'lists': {'camp_admin_location_list': locations, 'camp_admin_history_list': history},
        'elementStates': {},
    }


SCENARIOS = [
    scenario('admin_ger_1943_11_01_full', 'GER 1943-11-01 Administration: four-digit custody, long project places, available and blocked national actions.', 'administration'),
    scenario('admin_ger_1943_11_01_shortage', 'GER 1943-11-01 Administration during a maintenance shortage.', 'administration', shortage=True),
    scenario('locations_ger_1943_11_01_records_incomplete', 'GER 1943-11-01 Locations: eight rows (scroll), long names, selected host with incomplete survivor records.', 'locations'),
    scenario('locations_ger_1943_11_01_empty', 'GER 1943-11-01 Locations with no matching location.', 'locations', empty_locations=True),
    scenario('records_ger_1945_05_01_full', 'GER 1945-05-01 Records: large totals, records-incomplete closure, escapes to Sweden, seven history entries (scroll).', 'records', date='1945.5.1'),
    scenario('records_ger_1943_11_01_empty', 'GER 1943-11-01 Records with no history entries.', 'records', empty_history=True),
    scenario('picker_role_ger_1943_11_01', 'GER 1943-11-01 purpose picker with the killing-center option locked by mandate.', 'locations', picker='role'),
]

if __name__ == '__main__':
    for s in SCENARIOS:
        (HERE / (s['id'] + '.json')).write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding='utf-8')
        print(s['id'])
