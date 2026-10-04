"""Source-contract tests for Event 032 site and command project missions.

Each non-preparation mission must have a reachable success path: the decision
that activates it first calls a begin effect that sets the in-progress flag and
a converted due date, the due date is shorter than the native timeout, the
mission completes on that date through a dedicated completion effect, and
cancel/timeout paths clear only their own project. This is source evidence,
not an engine simulation.
"""
from pathlib import Path
from decimal import Decimal
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
CONSTANTS = source('common/script_constants/032_missiles_constants.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
MISSION_FILE = source('common/decisions/032_missiles_missions.txt')
MISSIONS = dict(MISSION_FILE['missiles_program_management_category'])
EVENTS = parse((ROOT / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig'))

PROJECTS = {
    'missiles_launch_state_survey_mission': dict(
        decisions=('missiles_survey_launch_state',), begin='missiles_begin_survey', due='missiles_survey_is_due',
        timing='survey_mission_days', complete='missiles_complete_survey', cancel='missiles_cancel_site_survey'),
    'missiles_secondary_site_construction_mission': dict(
        decisions=('missiles_establish_secondary_launch_site',), begin='missiles_begin_secondary_site',
        due='missiles_secondary_site_is_due', timing='secondary_site_mission_days',
        complete='missiles_establish_secondary_site', cancel='missiles_cancel_secondary_site_project'),
    'missiles_site_repair_mission': dict(
        decisions=('missiles_suspend_damaged_site',), begin='missiles_suspend_damaged_site',
        due='missiles_site_repair_is_due', timing='repair_mission_days',
        complete='missiles_complete_site_repair', cancel='missiles_cancel_site_repair_project'),
    'missiles_site_recovery_mission': dict(
        decisions=('missiles_send_loyal_forces',), begin='missiles_begin_site_recovery',
        due='missiles_site_recovery_is_due', timing='site_recovery_mission_days',
        complete='missiles_complete_site_recovery', cancel='missiles_cancel_site_recovery_project'),
    'missiles_warning_verification_mission': dict(
        decisions=('missiles_verify_warning',), begin='missiles_verify_warning',
        due='missiles_warning_verification_is_due', timing='warning_response_days',
        complete='missiles_complete_warning_verification', cancel='missiles_cancel_warning_verification'),
    'missiles_retaliation_network_restoration_mission': dict(
        decisions=('missiles_sever_retaliation_network', 'missiles_restore_retaliation_network'),
        begin='missiles_begin_network_restoration', due='missiles_network_restoration_is_due',
        timing='network_restore_days', complete='missiles_restore_retaliation_network',
        cancel='missiles_cancel_network_restoration'),
}


def number(token):
    if token.startswith('@'):
        token = MISSION_FILE[token]
    if token.startswith('constant:'):
        group, field = token[9:].split('.', 1)
        token = value(CONSTANTS[group], field)
    return Decimal(token)


def due_contract(trigger):
    body = TRIGGERS[trigger]
    flag = value(body, 'has_country_flag')
    variable = value(body, 'has_variable')
    date = dict(value(body, 'check_variable'))
    return flag, variable, date


class ProjectMissionContract(unittest.TestCase):
    def test_due_triggers_compare_the_current_date_with_a_stored_due_date(self):
        for mission, project in PROJECTS.items():
            flag, variable, date = due_contract(project['due'])
            with self.subTest(mission=mission):
                self.assertEqual(date, {'var': 'global.date', 'value': variable, 'compare': 'greater_than_or_equals'})
                self.assertIn((project['due'], 'yes'), list(descendants(value(MISSIONS[mission], 'available'))))

    def test_begin_effects_produce_the_flag_and_a_converted_due_date(self):
        for mission, project in PROJECTS.items():
            flag, variable, _ = due_contract(project['due'])
            nodes = list(descendants(EFFECTS[project['begin']]))
            with self.subTest(mission=mission):
                self.assertIn(('set_country_flag', flag), nodes)
                writes = [dict(body) for key, body in nodes if key in ('set_variable', 'add_to_variable') and isinstance(body, list)]
                self.assertIn({variable: 'global.date'}, writes)
                self.assertIn({variable: 'chaosx_date_offset'}, writes)
                temps = [dict(body) for key, body in nodes if key == 'set_temp_variable']
                self.assertIn({'chaosx_date_days': f"constant:missiles_evolution_timing.{project['timing']}"}, temps)
                keys = [key for key, _ in nodes]
                self.assertLess(keys.index('chaosx_convert_days_to_date_offset'), [k for k, b in nodes].index('add_to_variable'))

    def test_every_due_date_falls_before_the_native_timeout(self):
        for mission, project in PROJECTS.items():
            timeout = number(value(MISSIONS[mission], 'days_mission_timeout'))
            due = number(f"constant:missiles_evolution_timing.{project['timing']}")
            with self.subTest(mission=mission):
                self.assertLess(due, timeout)

    def test_activating_decisions_call_the_begin_effect_before_the_mission(self):
        for mission, project in PROJECTS.items():
            for decision in project['decisions']:
                nodes = list(descendants(value(DECISIONS[decision], 'complete_effect')))
                keys = [key for key, _ in nodes]
                with self.subTest(mission=mission, decision=decision):
                    self.assertIn((project['begin'], 'yes'), nodes)
                    self.assertIn(('activate_mission', mission), nodes)
                    self.assertLess(keys.index(project['begin']), nodes.index(('activate_mission', mission)))

    def test_warning_event_verifies_before_activating_the_mission(self):
        events = dict((value(body, 'id'), body) for key, body in EVENTS if key == 'country_event')
        option = next(body for key, body in events['chaosx.nr32.80'] if key == 'option' and value(body, 'name') == 'chaosx.nr32.80.a')
        nodes = list(descendants(option))
        keys = [key for key, _ in nodes]
        self.assertLess(keys.index('missiles_verify_warning'), nodes.index(('activate_mission', 'missiles_warning_verification_mission')))

    def test_completion_and_cancellation_are_owned_by_the_project(self):
        for mission, project in PROJECTS.items():
            flag, variable, _ = due_contract(project['due'])
            body = MISSIONS[mission]
            with self.subTest(mission=mission):
                self.assertIn((project['complete'], 'yes'), list(descendants(value(body, 'complete_effect'))))
                for outcome in ('cancel_effect', 'timeout_effect'):
                    self.assertIn((project['cancel'], 'yes'), list(descendants(value(body, outcome))))
                cancel = list(descendants(EFFECTS[project['cancel']]))
                self.assertIn(('clear_variable', variable), cancel)
                self.assertIn(('clr_country_flag', flag), cancel)
                complete = list(descendants(EFFECTS[project['complete']]))
                self.assertIn(('clr_country_flag', flag), complete)

    def test_projects_survive_program_phase_changes(self):
        for mission in PROJECTS:
            cancel = list(descendants(value(MISSIONS[mission], 'cancel_trigger')))
            with self.subTest(mission=mission):
                self.assertFalse(any(isinstance(v, str) and v.startswith('missiles_program_phase_') for _, v in cancel))

    def test_site_projects_complete_by_registering_or_restoring_their_own_state(self):
        self.assertIn(('missiles_register_site', 'yes'), list(descendants(value(EFFECTS['missiles_complete_survey'], 'if'))))
        self.assertIn(('missiles_register_site', 'yes'), list(descendants(value(EFFECTS['missiles_establish_secondary_site'], 'if'))))
        self.assertIn(('set_country_flag', 'missiles_secondary_site_established'), EFFECTS['missiles_establish_secondary_site'][0][1])
        repair = list(descendants(EFFECTS['missiles_finish_site_repair']))
        self.assertIn(('set_state_flag', 'missiles_site_active'), repair)
        self.assertIn(('clr_state_flag', 'missiles_site_suspended'), repair)
        release = list(descendants(EFFECTS['missiles_cancel_site_repair_project']))
        self.assertIn(('missiles_release_suspended_site', 'yes'), release)
        recovery = list(descendants(EFFECTS['missiles_complete_site_recovery']))
        self.assertIn(('missiles_recover_rogue_site', 'yes'), recovery)
        self.assertIn(('set_country_flag', 'missiles_site_recovery_complete'), recovery)
        self.assertIn(('missiles_close_rogue_incident', 'yes'), recovery)

    def test_recovery_is_goal_style_with_real_divisions_or_the_ai_path(self):
        available = list(descendants(value(MISSIONS['missiles_site_recovery_mission'], 'available')))
        stationed = dict(next(body for key, body in available if key == 'divisions_in_state'))
        self.assertEqual(stationed['state'], 'var:missiles_recovery_site_state')
        self.assertEqual(stationed['size'], '@m32_mission_recovery_division_floor')
        self.assertIn(('is_ai', 'yes'), available)
        self.assertIn(('missiles_recovery_target_is_valid', 'yes'), available)

    def test_suspended_sites_cannot_launch_and_restoration_stays_reachable(self):
        site_triggers = source('common/scripted_triggers/032_missiles_triggers.txt')
        self.assertIn(('NOT', [('has_state_flag', 'missiles_site_suspended')]), site_triggers['missiles_site_can_launch'])
        visible = list(descendants(value(DECISIONS['missiles_restore_retaliation_network'], 'visible')))
        self.assertIn(('has_country_flag', 'missiles_program_phase_maintenance'), visible)
        self.assertNotIn(('has_country_flag', 'missiles_program_phase_retaliation'), visible)

    def test_projects_use_separate_state_pointers(self):
        pointers = {
            'missiles_begin_survey': 'missiles_survey_site_state',
            'missiles_begin_secondary_site': 'missiles_secondary_site_state',
            'missiles_begin_site_recovery': 'missiles_recovery_site_state',
        }
        for effect, pointer in pointers.items():
            writes = [dict(body) for key, body in descendants(EFFECTS[effect]) if key == 'set_variable']
            self.assertTrue(any(pointer in write for write in writes), effect)
        self.assertNotIn('missiles_pending_site_state', str(EFFECTS))


if __name__ == '__main__':
    unittest.main()
