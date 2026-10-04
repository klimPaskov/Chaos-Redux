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
CORE = source('common/scripted_effects/032_missiles_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
SITE_TRIGGERS = source('common/scripted_triggers/032_missiles_triggers.txt')
SCENARIO = source('common/scripted_effects/032_missiles_scenario_effects.txt')
STATE_ARRAYS = {'missiles_launch_site_states', 'missiles_operation_sites'}
STATE_POINTERS = {'var:missiles_requested_launch_site', 'var:missiles_operation_launch_site', 'var:missiles_operation_impact_state'}


def invalid_state_checks(nodes, scope='country', path=()):
    findings = []
    for key, body in nodes:
        current = (*path, key)
        if key in ('exists', 'has_country_flag') and scope == 'state':
            findings.append(current)
        if not isinstance(body, list):
            continue
        child_scope = scope
        if key.upper() in ('ROOT', 'CONTROLLER', 'OWNER') or key == 'event_target:missiles_disaster_controller':
            child_scope = 'country'
        elif key in STATE_POINTERS or key in ('every_owned_state', 'every_controlled_state', 'every_neighbor_state', 'capital_scope'):
            child_scope = 'state'
        elif key in ('for_each_scope_loop', 'any_of_scopes') and dict(body).get('array') in STATE_ARRAYS:
            child_scope = 'state'
        findings.extend(invalid_state_checks(body, child_scope, current))
    return findings


class MissileStateScopeContract(unittest.TestCase):
    def test_state_arrays_and_launch_pointers_do_not_use_country_triggers(self):
        for effects in (CORE, OPERATIONS):
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
            (OPERATIONS, ('missiles_recover_rogue_site', 'missiles_natural_disaster_damage_site', 'missiles_register_conventional_military_losses')),
            (TRIGGERS, ('missiles_site_can_receive_project', 'missiles_site_can_receive_firing_recovery', 'missiles_site_is_secure')),
            (SITE_TRIGGERS, ('missiles_target_state_is_valid',)),
        ):
            for name in names:
                with self.subTest(helper=name):
                    self.assertEqual(invalid_state_checks(collection[name], 'state'), [])
        controller = value(SITE_TRIGGERS['missiles_target_state_is_valid'], 'CONTROLLER')
        self.assertIn(('exists', 'yes'), controller)

    def test_site_projects_validate_from_as_a_state(self):
        for helper, predicate in (
            ('missiles_begin_survey', 'missiles_state_is_valid_site_target'),
            ('missiles_begin_secondary_site', 'missiles_state_is_valid_secondary_site'),
        ):
            guarded = value(OPERATIONS[helper], 'if')
            self.assertEqual(value(value(guarded, 'limit'), 'FROM'), [(predicate, 'yes')])
            self.assertEqual(value(guarded, 'set_variable'), [('missiles_pending_site_state', 'FROM')])

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


if __name__ == '__main__':
    unittest.main()
