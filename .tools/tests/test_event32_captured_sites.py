"""Source-contract tests for Event 032 captured-site resolution.

A captured site must be resolvable through exactly one of four state-targeted
decisions, each resolution must clear the unresolved marker once no captured
state remains, and held captured missiles must move or be destroyed exactly
once. This is source evidence, not an engine simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[2]


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


def captured_reserve_block(body):
    """The top-level if that settles a captured site's held reserve."""
    return next(child for key, child in body if key == 'if' and ('has_variable', 'missiles_site_captured_reserve') in value(child, 'limit'))


def guarded_blocks(body, needle):
    """Every if block (at any depth) whose direct children contain needle."""
    return [child for key, child in descendants(body) if key == 'if' and isinstance(child, list) and needle in child]


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
        scuttle = captured_reserve_block(EFFECTS['missiles_scuttle_site'])
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


SITE_TRIGGERS = source('common/scripted_triggers/032_missiles_triggers.txt')
LOCALISATION = (ROOT / 'localisation/english/032_missiles_decisions_l_english.yml').read_bytes()
CLOSE_ROGUE = ('missiles_close_rogue_incident', 'yes')


class RogueSiteResolution(unittest.TestCase):
    def test_rogue_decisions_target_only_the_rogue_site_from_the_registry(self):
        for name in ('missiles_isolate_rogue_site', 'missiles_scuttle_rogue_site'):
            decision = dict(DECISIONS[name])
            with self.subTest(decision=name):
                self.assertEqual(decision['state_target'], 'yes')
                self.assertEqual(decision['target_array'], 'missiles_launch_site_states')
                self.assertEqual(decision['target_trigger'], [('FROM', [('missiles_site_is_rogue_incident_site', 'yes')])])
                self.assertIn(('FROM', [('missiles_site_is_rogue_incident_site', 'yes')]), decision['visible'])
                tooltip = value(decision['available'], 'custom_trigger_tooltip')
                self.assertEqual(value(tooltip, 'tooltip'), 'missiles_rogue_site_target_tt')
        retaliation = dict(DECISIONS['missiles_isolate_retaliation_site'])
        self.assertEqual(retaliation['state_target'], 'yes')
        self.assertEqual(retaliation['target_array'], 'missiles_launch_site_states')
        self.assertEqual(value(value(retaliation['available'], 'custom_trigger_tooltip'), 'tooltip'), 'missiles_retaliation_site_target_tt')

    def test_rogue_site_trigger_matches_the_recorded_crisis_site(self):
        trigger = TRIGGERS['missiles_site_is_rogue_incident_site']
        self.assertIn(('has_state_flag', 'missiles_site_rogue'), trigger)
        self.assertIn(('is_controlled_by', 'ROOT'), trigger)
        self.assertIn(('check_variable', [('var', 'THIS.id'), ('value', 'ROOT.missiles_rogue_site_id'), ('compare', 'equals')]), trigger)

    def test_isolating_or_scuttling_another_site_leaves_the_crisis_open(self):
        for helper, marker in (('missiles_isolate_site', 'missiles_isolation_closes_rogue'), ('missiles_scuttle_site', 'missiles_scuttle_closes_rogue')):
            body = EFFECTS[helper]
            with self.subTest(helper=helper):
                # The marker starts at zero and only the rogue crisis site sets it to one.
                self.assertEqual(body[0], ('set_temp_variable', [(marker, 'constant:missiles_program_value.zero')]))
                setters = [child for key, child in descendants(body) if key == 'if' and ('set_temp_variable', [(marker, 'constant:missiles_program_value.one')]) in child]
                self.assertEqual(len(setters), 1)
                self.assertEqual(value(setters[0], 'limit'), [('missiles_site_is_rogue_incident_site', 'yes')])
                # Every rogue closure in the helper is gated on that marker.
                closers = guarded_blocks(body, CLOSE_ROGUE)
                self.assertEqual(len(closers), 1)
                self.assertEqual(value(closers[0], 'limit'), [('check_variable', [('var', marker), ('value', 'constant:missiles_program_value.one'), ('compare', 'equals')])])
                self.assertEqual(sum(1 for node in descendants(body) if node == CLOSE_ROGUE), 1)
        # A site destroyed by a strike or disaster closes only its controller's rogue crisis.
        adapter = EFFECTS['missiles_scuttle_site_from_current_controller']
        requests = guarded_blocks(adapter, ('set_country_flag', 'missiles_refresh_close_rogue_requested'))
        self.assertEqual(len(requests), 1)
        self.assertIn(('check_variable', [('var', 'missiles_rogue_site_id'), ('value', 'PREV.id'), ('compare', 'equals')]), value(requests[0], 'limit'))

    def test_rogue_paths_never_repoint_the_general_incident_site(self):
        for helper in ('missiles_select_rogue_incident_site', 'missiles_open_rogue_incident', 'missiles_execute_rogue_launch',
                       'missiles_resolve_rogue_incident_timeout', 'missiles_close_rogue_incident', 'missiles_select_rogue_custody_payload'):
            body = nodes(EFFECTS[helper])
            with self.subTest(helper=helper):
                self.assertFalse(any(key in ('set_variable', 'clear_variable') and (child == 'missiles_incident_site' or (isinstance(child, list) and dict(child).get('missiles_incident_site'))) for key, child in body))
                self.assertFalse(any(key == 'var:missiles_incident_site' for key, _ in body))
        self.assertNotIn('missiles_point_incident_at_rogue_site', EFFECTS)
        for name in ('missiles_rogue_incident_site_has_reserve', 'missiles_rogue_incident_site_has_payload'):
            self.assertEqual(SITE_TRIGGERS[name][0], ('has_variable', 'missiles_rogue_site_state'))
        # The rogue closure ends the general incident only when the rogue incident is the current one.
        close = value(EFFECTS['missiles_close_rogue_incident'], 'if')
        closers = guarded_blocks(close, ('clr_country_flag', 'missiles_incident_active'))
        self.assertEqual(len(closers), 1)
        self.assertEqual(value(closers[0], 'limit'), [('check_variable', [('var', 'missiles_rogue_incident_is_current'), ('value', 'constant:missiles_program_value.one'), ('compare', 'equals')])])

    def test_isolated_site_returns_to_service_through_repair_with_one_refund(self):
        suspend = TRIGGERS['missiles_site_can_be_suspended']
        self.assertIn(('has_state_flag', 'missiles_site_isolated'), value(suspend, 'OR'))
        self.assertIn(('has_state_flag', 'missiles_site_isolated'), value(SITE_TRIGGERS['missiles_site_can_repair'], 'OR'))
        finish = EFFECTS['missiles_finish_site_repair']
        for node in (('clr_state_flag', 'missiles_site_isolated'), ('clr_state_flag', 'missiles_site_suspended'), ('set_state_flag', 'missiles_site_active')):
            self.assertIn(node, finish)
        hardened = next(child for key, child in CORE['missiles_refresh_site_flags'] if key == 'if' and ('set_state_flag', 'missiles_site_hardened') in child)
        self.assertIn(('NOT', [('has_state_flag', 'missiles_site_isolated')]), value(hardened, 'limit'))
        isolate = EFFECTS['missiles_isolate_site']
        keys = [key for key, _ in isolate]
        self.assertLess(keys.index('ROOT'), keys.index('set_state_flag'))
        self.assertIn(('set_temp_variable', [('missiles_allocation_loss_mode', 'constant:missiles_program_value.zero')]), isolate)
        self.assertEqual(sum(1 for node in descendants(isolate) if node == ('missiles_settle_lost_site_allocation', 'yes')), 1)
        for helper in ('missiles_suspend_damaged_site', 'missiles_finish_site_repair', 'missiles_complete_site_repair', 'missiles_release_suspended_site'):
            self.assertNotIn(('missiles_settle_lost_site_allocation', 'yes'), nodes(EFFECTS[helper]), helper)
        # A programme whose only site is isolated has no working site and falls
        # back to establishment, where the suspension is still offered.
        offered = value(TRIGGERS['missiles_site_suspension_is_offered'], 'OR')
        self.assertIn(('AND', [('has_country_flag', 'missiles_program_phase_establishment'),
                               ('NOT', [('has_country_flag', 'missiles_program_capture_shell')])]), offered)

    def test_ai_isolates_only_a_compromised_retaliation_site(self):
        weight = dict(DECISIONS['missiles_isolate_retaliation_site'])['ai_will_do']
        self.assertIn(('modifier', [('factor', '0'), ('FROM', [('NOT', [('has_state_flag', 'missiles_site_compromised')])])]), weight)

    def test_removed_country_releases_its_open_rogue_crisis_count(self):
        cleanup = EFFECTS['missiles_cleanup_removed_country']
        release = next(child for key, child in cleanup if key == 'if' and ('subtract_from_variable', [('global.missiles_rogue_active_incidents', 'constant:missiles_program_value.one')]) in child)
        self.assertIn(('has_country_flag', 'missiles_rogue_active_counted'), value(release, 'limit'))
        keys = [node for node in cleanup]
        self.assertLess(keys.index(('if', release)), keys.index(('clr_country_flag', 'missiles_rogue_active_counted')))
        for name in ('missiles_rogue_site_state', 'missiles_rogue_site_id'):
            self.assertIn(('clear_variable', name), cleanup)

    def test_rogue_target_tooltips_are_localised(self):
        self.assertTrue(LOCALISATION.startswith(b'\xef\xbb\xbf'))
        text = LOCALISATION.decode('utf-8-sig')
        for key in ('missiles_rogue_site_target_tt', 'missiles_retaliation_site_target_tt'):
            self.assertIn(f'\n{key}: "', text)


if __name__ == '__main__':
    unittest.main()
