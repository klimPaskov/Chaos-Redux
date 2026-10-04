"""Source-contract tests for Event 032 captured-site resolution.

A captured site must be resolvable through exactly one of four state-targeted
decisions, each resolution must clear the unresolved marker once no captured
state remains, and held captured missiles must move or be destroyed exactly
once. This is source evidence, not an engine simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
CORE = source('common/scripted_effects/032_missiles_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
EVENTS = parse((ROOT / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig'))
RESOLUTIONS = ('guard', 'study', 'integrate', 'scuttle')


def nodes(body):
    return list(descendants(body))


class CapturedSiteResolution(unittest.TestCase):
    def test_four_mutually_exclusive_state_decisions_use_one_focus_state(self):
        for route in RESOLUTIONS:
            name = f'missiles_{route}_captured_site'
            decision = dict(DECISIONS[name])
            with self.subTest(decision=name):
                self.assertEqual(decision['state_target'], 'yes')
                self.assertEqual(decision['target_array'], 'missiles_captured_site_focus')
                visible = nodes(decision['visible'])
                self.assertIn(('has_country_flag', 'missiles_program_phase_incident'), visible)
                self.assertIn(('has_country_flag', 'missiles_captured_site_unresolved'), visible)
                self.assertIn(('missiles_site_awaits_capture_resolution', 'yes'), visible)
                self.assertIn(('is_controlled_by', 'ROOT'), visible)
                self.assertIn((name, 'yes'), nodes(decision['complete_effect']))
                self.assertIn('custom_cost_text', decision)
                self.assertIn('ai_will_do', decision)
                effect = value(EFFECTS[name], 'if')
                self.assertIn(('missiles_site_awaits_capture_resolution', 'yes'), value(effect, 'limit'))

    def test_every_resolution_leaves_the_awaiting_state(self):
        trigger = TRIGGERS['missiles_site_awaits_capture_resolution']
        self.assertIn(('NOT', [('has_state_flag', 'missiles_site_capture_resolved')]), trigger)
        for route in ('guard', 'study'):
            body = nodes(EFFECTS[f'missiles_{route}_captured_site'])
            self.assertIn(('set_state_flag', 'missiles_site_capture_resolved'), body)
            self.assertIn(('missiles_finish_captured_site_resolution', 'yes'), body)
        integrate = nodes(EFFECTS['missiles_integrate_captured_site'])
        self.assertIn(('clr_state_flag', 'missiles_site_captured'), integrate)
        self.assertIn(('missiles_finish_captured_site_resolution', 'yes'), integrate)
        self.assertIn(('missiles_scuttle_site', 'yes'), nodes(EFFECTS['missiles_scuttle_captured_site']))
        scuttle = nodes(EFFECTS['missiles_scuttle_site'])
        self.assertIn(('set_state_flag', 'missiles_site_scuttled'), scuttle)
        self.assertIn(('missiles_finish_captured_site_resolution', 'yes'), scuttle)

    def test_finish_clears_the_marker_and_closes_only_the_capture_incident(self):
        finish = EFFECTS['missiles_finish_captured_site_resolution']
        guarded = value(finish, 'if')
        self.assertEqual(value(guarded, 'limit'), [('NOT', [('missiles_country_has_unresolved_captured_site', 'yes')])])
        self.assertIn(('clr_country_flag', 'missiles_captured_site_unresolved'), guarded)
        closure = value(guarded, 'if')
        self.assertIn(('check_variable', [('var', 'missiles_current_incident_type'), ('value', 'constant:missiles_incident_type.site_capture'), ('compare', 'equals')]), value(closure, 'limit'))
        self.assertIn(('missiles_close_current_incident', 'yes'), closure)
        self.assertIn(('missiles_select_next_captured_site', 'yes'), finish)

    def test_held_reserve_moves_or_is_destroyed_exactly_once(self):
        transfer = value(value(EFFECTS['missiles_integrate_captured_site'], 'if'), 'if')
        root = value(transfer, 'ROOT')
        self.assertIn(('add_to_variable', [('missiles_operational_reserve', 'PREV.missiles_site_captured_reserve')]), root)
        self.assertIn(('subtract_from_variable', [('missiles_captured_reserve_held', 'PREV.missiles_site_captured_reserve')]), root)
        self.assertIn(('set_variable', [('missiles_site_captured_reserve', 'constant:missiles_program_value.zero')]), transfer)
        scuttle = value(EFFECTS['missiles_scuttle_site'], 'if')
        self.assertIn(('set_variable', [('missiles_site_captured_reserve', 'constant:missiles_program_value.zero')]), scuttle)
        self.assertTrue(any(k == 'subtract_from_variable' and dict(v).get('missiles_captured_reserve_held') == 'PREV.missiles_site_captured_reserve' for k, v in nodes(scuttle)))

    def test_incident_phase_shows_at_most_six_primary_actions(self):
        incident = []
        for name, body in DECISIONS.items():
            visible = nodes(dict(body).get('visible', []))
            if ('has_country_flag', 'missiles_program_phase_incident') not in visible:
                continue
            if ('NOT', [('has_country_flag', 'missiles_captured_site_unresolved')]) in visible or ('NOT', [('has_country_flag', 'missiles_captured_site_unresolved')]) in list(dict(body)['visible']):
                continue
            incident.append(name)
        # Four resolutions for the one focus state; every other incident action steps aside.
        self.assertLessEqual(len(incident), 6, incident)
        for route in RESOLUTIONS:
            self.assertIn(f'missiles_{route}_captured_site', incident)

    def test_former_and_new_controllers_refresh_with_their_own_root(self):
        handler = nodes(EFFECTS['missiles_handle_site_control_changed'])
        self.assertIn(('country_event', [('id', 'chaosx.nr32.7')]), handler)
        self.assertIn(('missiles_select_next_captured_site', 'yes'), handler)
        events = {value(body, 'id'): body for key, body in EVENTS if key == 'country_event'}
        self.assertIn(('immediate', [('missiles_refresh_program_from_receiver', 'yes')]), events['chaosx.nr32.7'])
        receiver = nodes(EFFECTS['missiles_refresh_program_from_receiver'])
        self.assertIn(('missiles_finish_captured_site_resolution', 'yes'), receiver)

    def test_focus_selection_breaks_after_the_first_awaiting_state(self):
        select = EFFECTS['missiles_select_next_captured_site']
        self.assertIn(('clear_array', 'missiles_captured_site_focus'), select)
        loop = value(select, 'for_each_scope_loop')
        self.assertEqual(value(loop, 'array'), 'missiles_launch_site_states')
        self.assertEqual(value(loop, 'break'), 'missiles_captured_focus_break')

    def test_network_totals_skip_unresolved_captured_sites(self):
        recalc = CORE['missiles_recalculate_network']
        scan = value(recalc, 'every_controlled_state')
        self.assertIn(('NOT', [('has_state_flag', 'missiles_site_captured')]), value(scan, 'limit'))


if __name__ == '__main__':
    unittest.main()
