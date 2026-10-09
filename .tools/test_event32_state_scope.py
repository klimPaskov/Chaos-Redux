"""Regression for the live SCN-015 invalid-scope and target-cleanup defects.

Checks typed STATE arrays and known STATE APIs while preserving COUNTRY-only
existence checks after ROOT/CONTROLLER transitions. This is source evidence,
not an engine or duplicate-object-ID simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


OPERATIONS = source('common/scripted_effects/032_missiles_operations_effects.txt')
SURVEY = source('common/scripted_effects/032_missiles_survey_effects.txt')
SURVEY_TRIGGERS = source('common/scripted_triggers/032_missiles_survey_triggers.txt')
CORE = source('common/scripted_effects/032_missiles_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
SITE_TRIGGERS = source('common/scripted_triggers/032_missiles_triggers.txt')
SCENARIO = source('common/scripted_effects/032_missiles_scenario_effects.txt')
STATE_ARRAYS = {'missiles_launch_site_states', 'missiles_operation_sites'}
STATE_POINTERS = {'var:missiles_requested_launch_site', 'var:missiles_operation_launch_site', 'var:missiles_operation_impact_state'}


def invalid_state_checks(nodes, scope='country', path=(), previous_scope='country'):
    findings = []
    for key, body in nodes:
        current = (*path, key)
        if key in ('exists', 'has_country_flag') and scope == 'state':
            findings.append(current)
        if not isinstance(body, list):
            continue
        child_scope = scope
        child_previous_scope = previous_scope
        if key.upper() in ('ROOT', 'CONTROLLER', 'OWNER') or key == 'event_target:missiles_disaster_controller':
            child_scope = 'country'
            child_previous_scope = scope
        elif key.upper() == 'PREV':
            child_scope = previous_scope
            child_previous_scope = scope
        elif key in STATE_POINTERS or key in ('every_owned_state', 'every_controlled_state', 'every_neighbor_state', 'capital_scope'):
            child_scope = 'state'
            child_previous_scope = scope
        elif key in ('for_each_scope_loop', 'any_of_scopes') and dict(body).get('array') in STATE_ARRAYS:
            child_scope = 'state'
            child_previous_scope = scope
        findings.extend(invalid_state_checks(body, child_scope, current, child_previous_scope))
    return findings


class MissileStateScopeContract(unittest.TestCase):
    def test_state_arrays_and_launch_pointers_do_not_use_country_triggers(self):
        for effects in (CORE, OPERATIONS, SURVEY):
            for name, body in effects.items():
                if not isinstance(body, list):
                    continue
                with self.subTest(helper=name):
                    self.assertEqual(invalid_state_checks(body), [])
        for name in ('missiles_operation_sites_remain_valid', 'missiles_operation_projected_site_allocations_fit'):
            self.assertEqual(invalid_state_checks(TRIGGERS[name]), [])
            witness = value(TRIGGERS[name], 'any_of_scopes')
            self.assertEqual(witness, [('array', 'missiles_operation_sites'), ('is_controlled_by', 'ROOT')])

    def test_state_apis_keep_country_checks_inside_country_scopes(self):
        for collection, names in (
            (OPERATIONS, ('missiles_recover_rogue_site', 'missiles_natural_disaster_damage_site', 'missiles_apply_natural_disaster_site_damage', 'missiles_register_conventional_military_losses')),
            (TRIGGERS, ('missiles_site_can_receive_project', 'missiles_site_can_receive_firing_recovery', 'missiles_site_is_secure')),
            (SITE_TRIGGERS, ('missiles_target_state_is_valid',)),
        ):
            for name in names:
                with self.subTest(helper=name):
                    self.assertEqual(invalid_state_checks(collection[name], 'state'), [])
        controller = value(SITE_TRIGGERS['missiles_target_state_is_valid'], 'CONTROLLER')
        self.assertIn(('exists', 'yes'), controller)

    def test_site_projects_validate_from_as_a_state(self):
        for helper, predicate, pointer in (
            ('missiles_begin_survey', 'missiles_state_is_valid_survey_target', 'missiles_survey_site_state'),
            ('missiles_begin_secondary_site', 'missiles_state_is_valid_secondary_site', 'missiles_secondary_site_state'),
        ):
            if helper == 'missiles_begin_survey':
                self.assertEqual(OPERATIONS[helper], [('missiles_start_paid_survey', 'yes')])
                selected = SURVEY_TRIGGERS['missiles_survey_selected_project_can_start']
                self.assertEqual(value(selected, 'FROM'), [(predicate, 'yes')])
                guarded = value(SURVEY['missiles_start_paid_survey'], 'if')
                self.assertIn(('missiles_survey_selected_project_can_start', 'yes'), value(guarded, 'limit'))
                self.assertIn(('set_variable', [(pointer, 'FROM')]), guarded)
                continue
            guarded = value(OPERATIONS[helper], 'if')
            self.assertEqual(value(value(guarded, 'limit'), 'FROM'), [(predicate, 'yes')])
            self.assertEqual(value(guarded, 'set_variable'), [(pointer, 'FROM')])

    def test_war_anchor_cleanup_is_guarded_at_both_transaction_boundaries(self):
        for helper in ('missiles_scenario_freeze_candidate_arrays', 'missiles_scenario_finish_transaction'):
            body = SCENARIO[helper]
            clears = [(key, child) for key, child in body if key == 'clear_global_event_target']
            self.assertFalse(any(child == 'missiles_scenario_war_anchor' for _, child in clears))
            guarded = [child for key, child in body if key == 'if' and ('clear_global_event_target', 'missiles_scenario_war_anchor') in child]
            self.assertEqual(len(guarded), 1)
            self.assertEqual(value(guarded[0], 'limit'), [('has_event_target', 'missiles_scenario_war_anchor')])
            self.assertEqual(sum(key == 'clear_global_event_target' and child == 'missiles_scenario_war_anchor' for key, child in descendants(body)), 1)

    def test_scenario_technology_activation_is_missing_only_and_stage_gated(self):
        initializer = OPERATIONS['missiles_initialize_scenario_package']
        expected = {
            'experimental_rockets': 'experimental', 'rocket_engines': 'guided',
            'improved_rocket_engines': 'advanced', 'advanced_rocket_engines': 'strategic',
        }
        grants = [child for key, child in initializer if key == 'if' and 'set_technology' in dict(child)]
        self.assertEqual(len(grants), len(expected))
        for grant in grants:
            technology = value(grant, 'set_technology')
            self.assertEqual(value(technology, 'popup'), 'no')
            token = next(key for key, _ in technology if key != 'popup')
            self.assertEqual(value(technology, token), '1')
            limit = value(grant, 'limit')
            self.assertEqual(value(limit, 'NOT'), [('has_tech', token)])
            self.assertEqual(dict(value(limit, 'check_variable')), {
                'var': 'missiles_program_stage', 'value': f'constant:missiles_stage.{expected[token]}',
                'compare': 'greater_than_or_equals',
            })

    def test_temporary_id_markers_bracket_native_calls_without_replacing_them(self):
        initializer = OPERATIONS['missiles_initialize_scenario_package']
        for key, grant in initializer:
            if key == 'if' and 'set_technology' in dict(grant):
                order = [name for name, _ in grant]
                self.assertEqual(order, ['limit', 'log', 'set_technology', 'log'])
        registration = value(CORE['missiles_register_site'], 'if')
        construction = next(body for key, body in registration if key == 'else')
        self.assertEqual([key for key, _ in construction], ['if', 'add_building_construction', 'if'])
        for key, marker in construction:
            if key == 'if':
                self.assertEqual(value(value(marker, 'limit'), 'ROOT'), [('has_country_flag', 'missiles_scenario_country_bypass_active')])


DISASTERS = source('common/scripted_effects/013_natural_disasters_effects.txt')
EVENT_FILE = parse((ROOT / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig'))
# Helpers whose effects depend on ROOT being the programme country.
PROGRAMME_HELPERS = {
    'missiles_recalculate_network', 'missiles_rebalance_site_custody', 'missiles_allocate_incident_id',
    'missiles_settle_lost_site_allocation', 'missiles_remove_reserve', 'missiles_set_program_phases',
    'chaosx_032_achievement_record_site_damage', 'chaosx_032_achievement_prepare_long_reach_snapshot',
}


class NaturalDisasterBridge(unittest.TestCase):
    def test_event13_building_damage_helper_ends_with_one_guarded_call(self):
        helper = DISASTERS['natural_disaster_apply_family_building_damage']
        self.assertEqual(helper[-1], ('if', [('limit', [('missiles_state_has_registered_site', 'yes')]), ('missiles_natural_disaster_damage_site', 'yes')]))
        calls = [name for name, body in DISASTERS.items() if isinstance(body, list) and ('missiles_natural_disaster_damage_site', 'yes') in list(descendants(body))]
        self.assertEqual(calls, ['natural_disaster_apply_family_building_damage'])

    def test_adapter_only_queues_the_site_on_its_controller(self):
        adapter = OPERATIONS['missiles_natural_disaster_damage_site']
        body = list(descendants(adapter))
        self.assertFalse(PROGRAMME_HELPERS & {key for key, _ in body})
        self.assertNotIn('ROOT', {key for key, _ in body})
        controller = value(value(adapter, 'if'), 'controller')
        self.assertIn(('country_event', [('id', 'chaosx.nr32.9')]), controller)
        self.assertIn(('add_to_array', [('array', 'missiles_disaster_pending_sites'), ('value', 'PREV')]), list(descendants(controller)))
        # Severity comes from Event 013's unscoped temporary through check_variable only.
        severity_checks = [child for key, child in body if key == 'check_variable' and isinstance(child, list) and child and child[0][0] == 'natural_disaster_current_severity']
        self.assertEqual(len(severity_checks), 4)
        for helper in ('missiles_natural_disaster_damage_site', 'missiles_apply_natural_disaster_site_damage'):
            self.assertNotIn(('has_variable', 'natural_disaster_current_severity'), list(descendants(OPERATIONS[helper])))

    def test_receiver_applies_queued_sites_with_the_controller_as_root(self):
        events = {value(body, 'id'): body for key, body in EVENT_FILE if key == 'country_event'}
        receiver = events['chaosx.nr32.9']
        self.assertEqual(value(receiver, 'hidden'), 'yes')
        self.assertEqual(value(receiver, 'immediate'), [('missiles_process_natural_disaster_receipts', 'yes')])
        process = OPERATIONS['missiles_process_natural_disaster_receipts']
        self.assertEqual(process, [
            ('for_each_scope_loop', [('array', 'missiles_disaster_pending_sites'), ('missiles_apply_natural_disaster_site_damage', 'yes')]),
            ('clear_array', 'missiles_disaster_pending_sites'),
        ])
        apply = OPERATIONS['missiles_apply_natural_disaster_site_damage']
        guarded = value(apply, 'if')
        self.assertIn(('is_controlled_by', 'ROOT'), value(guarded, 'limit'))
        self.assertIn(('has_variable', 'missiles_disaster_pending_severity'), value(guarded, 'limit'))
        nodes = list(descendants(apply))
        self.assertEqual(sum(1 for node in nodes if node == ('missiles_scuttle_site_from_current_controller', 'yes')), 1)
        self.assertEqual(sum(1 for node in nodes if node == ('missiles_settle_lost_site_allocation', 'yes')), 1)
        self.assertFalse(any('evolution' in key for key, _ in nodes))
        self.assertFalse(any(key.startswith('event_target:') for key, _ in nodes))
        # Programme helpers run only inside ROOT blocks, bound to the controller.
        def outside_root(body):
            for key, child in body:
                if key == 'ROOT':
                    continue
                yield key
                if isinstance(child, list):
                    yield from outside_root(child)
        self.assertFalse(PROGRAMME_HELPERS & set(outside_root(apply)))
        self.assertEqual(apply[-3:], [
            ('clear_variable', 'missiles_disaster_pending_severity'),
            ('clear_variable', 'missiles_disaster_reserve_loss'),
            ('clear_variable', 'missiles_disaster_reserve_settlement_result'),
        ])


FORMER = 'missiles_capture_former_controller'
ON_ACTIONS = dict(parse((ROOT / 'common/on_actions/032_missiles_on_actions.txt').read_text(encoding='utf-8-sig')))


def tokens(body):
    for key, child in body:
        yield key
        if isinstance(child, list):
            yield from tokens(child)
        elif child is not None:
            yield child


class SiteCaptureFormerController(unittest.TestCase):
    """The capture handler runs in STATE scope, where FROM can be the state."""

    def test_handler_reads_only_the_bound_former_controller(self):
        handler = OPERATIONS['missiles_handle_site_control_changed']
        self.assertFalse([token for token in tokens(handler) if 'FROM' in token])
        limit = value(value(handler, 'if'), 'limit')
        self.assertIn(('has_event_target', FORMER), limit)
        self.assertIn((f'event_target:{FORMER}', [('exists', 'yes'), ('NOT', [('tag', 'ROOT')])]), limit)
        # exists is evaluated only inside country scopes.
        def state_exists(body, scope):
            for key, child in body:
                if key == 'exists' and scope == 'state':
                    yield key
                if isinstance(child, list):
                    inner = 'country' if key in ('ROOT', f'event_target:{FORMER}') else scope
                    yield from state_exists(child, inner)
        self.assertEqual(list(state_exists(handler, 'state')), [])
        writes = [child for key, child in descendants(handler) if key == 'set_variable']
        self.assertIn([('missiles_last_incident_actor_id', f'event_target:{FORMER}.id')], writes)
        self.assertIn([('missiles_site_former_controller_id', f'event_target:{FORMER}.id')], writes)

    def test_state_control_callback_binds_its_own_from_before_entering_the_state(self):
        guarded = value(value(ON_ACTIONS['on_actions'], 'on_state_control_changed'), 'effect')
        body = value(guarded, 'if')
        keys = [key for key, _ in body]
        self.assertLess(keys.index('FROM'), keys.index('FROM.FROM'))
        self.assertEqual(value(body, 'FROM'), [('save_event_target_as', FORMER)])
        self.assertEqual(value(body, 'FROM.FROM'), [('missiles_handle_site_control_changed', 'yes')])

    def test_release_pass_binds_each_site_stored_controller(self):
        loop = value(OPERATIONS['missiles_reconcile_released_country_sites'], 'every_controlled_state')
        self.assertIn(('has_variable', 'missiles_site_current_controller'), value(loop, 'limit'))
        keys = [key for key, _ in loop]
        self.assertLess(keys.index('var:missiles_site_current_controller'), keys.index('missiles_handle_site_control_changed'))
        self.assertEqual(value(loop, 'var:missiles_site_current_controller'), [('save_event_target_as', FORMER)])

    def test_every_controller_id_write_keeps_the_stored_controller_in_step(self):
        for effects in (CORE, OPERATIONS):
            for name, body in effects.items():
                if not isinstance(body, list):
                    continue
                flat = list(descendants(body))
                ids = [child for key, child in flat if key == 'set_variable' and isinstance(child, list) and child[0][0] == 'missiles_site_controller_id']
                if not ids:
                    continue
                stored = [child for key, child in flat if key == 'set_variable' and isinstance(child, list) and child[0][0] == 'missiles_site_current_controller']
                cleared = [child for key, child in flat if key == 'clear_variable' and child == 'missiles_site_current_controller']
                with self.subTest(helper=name):
                    self.assertEqual(len(ids), len(stored) + len(cleared))


if __name__ == '__main__':
    unittest.main()
