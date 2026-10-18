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


EFFECTS = {**source('common/scripted_effects/032_missiles_operations_effects.txt'),
           **source('common/scripted_effects/032_missiles_survey_effects.txt')}
TRIGGERS = {**source('common/scripted_triggers/032_missiles_operations_triggers.txt'),
            **source('common/scripted_triggers/032_missiles_survey_triggers.txt'),
            **source('common/scripted_triggers/032_missiles_recovery_triggers.txt')}
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
            begin = project['begin']
            if begin == 'missiles_begin_survey':
                self.assertEqual(EFFECTS[begin], [('missiles_start_paid_survey', 'yes')])
                begin = 'missiles_start_paid_survey'
            nodes = list(descendants(EFFECTS[begin]))
            with self.subTest(mission=mission):
                self.assertIn(('set_country_flag', flag), nodes)
                writes = [dict(body) for key, body in nodes if key in ('set_variable', 'add_to_variable') and isinstance(body, list)]
                self.assertIn({variable: 'global.date'}, writes)
                self.assertIn({variable: 'chaosx_date_offset'}, writes)
                temps = [dict(body) for key, body in nodes if key == 'set_temp_variable']
                if begin == 'missiles_start_paid_survey':
                    self.assertIn({'missiles_survey_paid_duration_days': 'constant:missiles_evolution_timing.survey_mission_days'}, writes)
                    self.assertIn({'chaosx_date_days': 'missiles_survey_paid_duration_days'}, temps)
                else:
                    self.assertIn({'chaosx_date_days': f"constant:missiles_evolution_timing.{project['timing']}"}, temps)
                keys = [key for key, _ in nodes]
                self.assertLess(keys.index('chaosx_convert_days_to_date_offset'),
                                nodes.index(('add_to_variable', [(variable, 'chaosx_date_offset')])))

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
                if mission == 'missiles_site_recovery_mission':
                    self.assertIn((project['cancel'], 'yes'), complete)
                    complete += cancel
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

    def test_recovery_is_goal_style_with_one_shared_owned_garrison_path(self):
        available = list(descendants(value(MISSIONS['missiles_site_recovery_mission'], 'available')))
        self.assertIn(('missiles_selected_rogue_site_has_loyal_garrison', 'yes'), available)
        self.assertIn(('missiles_recovery_receipt_is_current', 'yes'), available)
        garrison = list(descendants(TRIGGERS['missiles_selected_rogue_site_has_loyal_garrison']))
        self.assertNotIn(('is_ai', 'yes'), available + garrison)
        stationed = dict(next(body for key, body in garrison if key == 'divisions_in_state'))
        self.assertEqual(stationed['state'], 'var:missiles_rogue_site_state')
        self.assertEqual(stationed['size'], '[DIVISION_FLOOR]')
        current = list(descendants(TRIGGERS['missiles_recovery_receipt_is_current']))
        self.assertIn(('missiles_recovery_target_is_valid', 'yes'), current)
        self.assertIn(('missiles_recovery_goal_is_satisfied', 'yes'),
                      list(descendants(EFFECTS['missiles_complete_site_recovery'])))

    def test_suspended_sites_cannot_launch_and_restoration_stays_reachable(self):
        site_triggers = source('common/scripted_triggers/032_missiles_triggers.txt')
        # The suspension flag is internal state, so the launch gate hides it from tooltips.
        self.assertIn(('NOT', [('hidden_trigger', [('has_state_flag', 'missiles_site_suspended')])]), site_triggers['missiles_site_can_launch'])
        visible = list(descendants(value(DECISIONS['missiles_restore_retaliation_network'], 'visible')))
        self.assertIn(('missiles_maintenance_actions_are_visible', 'yes'), visible)
        self.assertNotIn(('has_country_flag', 'missiles_program_phase_retaliation'), visible)
        self.assertIn(('has_country_flag', 'missiles_program_phase_maintenance'), list(descendants(TRIGGERS['missiles_maintenance_actions_are_visible'])))

    def test_projects_use_separate_state_pointers(self):
        pointers = {
            'missiles_begin_survey': 'missiles_survey_site_state',
            'missiles_begin_secondary_site': 'missiles_secondary_site_state',
            'missiles_begin_site_recovery': 'missiles_recovery_site_state',
        }
        for effect, pointer in pointers.items():
            if effect == 'missiles_begin_survey':
                effect = 'missiles_start_paid_survey'
            writes = [dict(body) for key, body in descendants(EFFECTS[effect]) if key == 'set_variable']
            self.assertTrue(any(pointer in write for write in writes), effect)
        self.assertNotIn('missiles_pending_site_state', str(EFFECTS))

    def test_a_suspended_site_stays_registered_and_keeps_its_repair_project(self):
        site_triggers = source('common/scripted_triggers/032_missiles_triggers.txt')
        registered = list(descendants(site_triggers['missiles_state_has_registered_site']))
        self.assertIn(('has_state_flag', 'missiles_site_suspended'), registered)
        # Damage to another site never rewrites or clears a running repair project.
        incoming = EFFECTS['missiles_record_incoming_operation_site_damage']
        guarded = [body for key, body in descendants(incoming)
                   if key == 'if' and ('limit', [('NOT', [('has_active_mission', 'missiles_site_repair_mission')])]) in body]
        self.assertEqual(len(guarded), 2)
        guarded_writes = [entry for body in guarded for entry in body]
        self.assertIn(('clr_country_flag', 'missiles_site_repair_active'), guarded_writes)
        self.assertIn(('set_country_flag', 'missiles_site_repair_active'), guarded_writes)
        self.assertIn(('set_variable', [('missiles_site_repair_due_date', 'global.date')]), guarded_writes)
        survey_gate = list(descendants(TRIGGERS['missiles_country_can_start_survey']))
        self.assertIn(('has_active_mission', 'missiles_site_repair_mission'), survey_gate)

    def test_a_transferred_site_is_released_for_its_new_controller(self):
        released = ('clr_state_flag', 'missiles_site_suspended')
        for helper, expected in (('missiles_finalize_civil_war_split_child', 1), ('missiles_finalize_planned_inheritance', 1),
                                 ('missiles_cleanup_removed_country', 2)):
            with self.subTest(helper=helper):
                body = list(descendants(EFFECTS[helper]))
                self.assertEqual(sum(1 for node in body if node == released), expected)
                # The transferred site stays compromised and isolated until repaired.
                self.assertIn(('set_state_flag', 'missiles_site_isolated'), body)
                self.assertIn(('set_state_flag', 'missiles_site_compromised'), body)
        # The parent keeps its own sites and their running repair programme.
        self.assertNotIn(released, list(descendants(EFFECTS['missiles_finalize_civil_war_split_parent'])))
        suspend = TRIGGERS['missiles_site_can_be_suspended']
        self.assertIn(('NOT', [('has_state_flag', 'missiles_site_suspended')]), suspend)
        self.assertIn(('has_state_flag', 'missiles_site_isolated'), value(suspend, 'OR'))

    def test_a_former_owner_programme_ends_without_touching_the_lost_state(self):
        repair = MISSIONS['missiles_site_repair_mission']
        recovery = MISSIONS['missiles_site_recovery_mission']
        self.assertIn(('NOT', [('missiles_repair_target_is_valid', 'yes')]), value(value(repair, 'cancel_trigger'), 'OR'))
        self.assertIn(('NOT', [('missiles_recovery_target_is_valid', 'yes')]), value(value(recovery, 'cancel_trigger'), 'OR'))
        self.assertIn(('is_controlled_by', 'ROOT'), value(TRIGGERS['missiles_repair_target_is_valid'], 'var:missiles_repair_site_state'))
        self.assertIn(('is_controlled_by', 'ROOT'), value(TRIGGERS['missiles_recovery_target_is_valid'], 'var:missiles_recovery_site_state'))
        cancel = EFFECTS['missiles_cancel_site_repair_project']
        release = value(cancel, 'if')
        self.assertIn(('var:missiles_repair_site_state', [('is_controlled_by', 'ROOT')]), value(release, 'limit'))
        for cleared in (('clr_country_flag', 'missiles_site_repair_active'), ('clear_variable', 'missiles_site_repair_due_date'),
                        ('clear_variable', 'missiles_repair_site_state')):
            self.assertIn(cleared, cancel)
        recovery_cancel = EFFECTS['missiles_cancel_site_recovery_project']
        self.assertEqual(recovery_cancel, [
            ('clear_variable', 'missiles_site_recovery_actor_id'),
            ('clear_variable', 'missiles_site_recovery_context_id'),
            ('clear_variable', 'missiles_site_recovery_site_id'),
            ('clr_country_flag', 'missiles_site_recovery_active'),
            ('clear_variable', 'missiles_site_recovery_due_date'),
            ('clear_variable', 'missiles_recovery_site_state'),
        ])


if __name__ == '__main__':
    unittest.main()
