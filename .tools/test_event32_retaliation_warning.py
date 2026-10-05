"""Source-contract tests for Event 032 retaliation warnings.

Pins the shared response route (the Accept decision, the warning event
option, and the Delegated or Automatic posture use one effect and one gate)
and the per-warning outcome flags: opening and resolving a warning clear
them, and each route records its outcome only after the warning resolves,
so every new warning can be delayed once and answered by its posture.
This is source evidence, not an engine simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
SCENARIO = source('common/scripted_effects/032_missiles_scenario_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
EVENTS = parse((ROOT / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig'))
LOCALISATION = (ROOT / 'localisation/english/032_missiles_decisions_l_english.yml').read_text(encoding='utf-8-sig')
OUTCOME_FLAGS = {
    'missiles_warning_delayed', 'missiles_warning_false_or_conflicting',
    'missiles_warning_expired_without_launch', 'missiles_retaliation_response_accepted',
}
GATE = ('missiles_retaliation_response_can_be_accepted', 'yes')
CLEAR = ('missiles_clear_warning_outcome_flags', 'yes')
RESOLVE = ('missiles_resolve_warning_queue_receipt', 'yes')


def nodes(body):
    return list(descendants(body))


def event_options(event_id):
    body = next(body for key, body in EVENTS if key == 'country_event' and dict(body).get('id') == event_id)
    return {dict(v)['name']: dict(v) for k, v in body if k == 'option'}


def impact_block():
    """The impact-country body of the warning queue: the warning-opening path."""
    queue = EFFECTS['missiles_queue_warning_for_impact_country']
    return next(v for k, v in dict(queue)['if'] if k == 'var:missiles_operation_impact_country')


def outcome_follows_resolution(body, flag):
    """The flag is set after the resolution call in the same flat effect list."""
    for _, inner in descendants(body):
        if isinstance(inner, list) and RESOLVE in inner and ('set_country_flag', flag) in inner:
            return inner.index(RESOLVE) < inner.index(('set_country_flag', flag))
    return False


class SharedResponseRoute(unittest.TestCase):
    def test_decision_and_event_option_share_effect_and_gate(self):
        decision = dict(DECISIONS['missiles_accept_retaliation_response'])
        self.assertIn(('missiles_accept_retaliation_response', 'yes'), nodes(decision['complete_effect']))
        self.assertNotIn(('missiles_commit_operation', 'yes'), nodes(decision['complete_effect']))
        tooltip = dict(decision['available'])['custom_trigger_tooltip']
        self.assertIn(GATE, tooltip)
        self.assertIn(('tooltip', 'missiles_accept_retaliation_requirements_tt'), tooltip)
        self.assertIn('missiles_accept_retaliation_requirements_tt:', LOCALISATION)
        self.assertIn(('NOT', [('has_country_flag', 'missiles_retaliation_response_accepted')]), decision['visible'])
        accept = event_options('chaosx.nr32.80')['chaosx.nr32.80.d']
        self.assertEqual(accept['trigger'], [GATE])
        self.assertIn(('missiles_accept_retaliation_response', 'yes'), nodes(accept['hidden_effect']))
        effect_limit = dict(dict(EFFECTS['missiles_accept_retaliation_response'])['if'])['limit']
        self.assertEqual(effect_limit, [GATE])

    def test_gate_holds_every_cap_site_and_reserve_requirement(self):
        gate = nodes(TRIGGERS['missiles_retaliation_response_can_be_accepted'])
        for required in (('missiles_warning_is_actionable', 'yes'), ('missiles_retaliation_launch_slot_available', 'yes'),
                         ('missiles_country_can_prepare_operation', 'yes'),
                         ('NOT', [('has_country_flag', 'missiles_retaliation_response_accepted')])):
            self.assertIn(required, gate)
        self.assertIn(('any_controlled_state', [('missiles_site_can_launch', 'yes')]), gate)
        checks = {dict(v)['var']: dict(v)['value'] for k, v in gate if k == 'check_variable'}
        self.assertEqual(checks['missiles_operational_reserve'], 'constant:missiles_reserve.retaliation_reserve_cap')
        self.assertEqual(checks['missiles_warning_generation'], 'constant:missiles_chain_limits.maximum_generation')
        self.assertEqual(checks['missiles_root_incident_count'], 'constant:missiles_chain_limits.maximum_incidents')
        self.assertEqual(checks['missiles_root_participant_count'], 'constant:missiles_chain_limits.maximum_countries')


class PerWarningState(unittest.TestCase):
    def test_outcome_flags_are_cleared_by_opening_resolving_and_cleanup(self):
        cleared = {v for k, v in EFFECTS['missiles_clear_warning_outcome_flags'] if k == 'clr_country_flag'}
        self.assertEqual(cleared, OUTCOME_FLAGS)
        self.assertNotIn('missiles_false_warning_history', cleared)
        opening = impact_block()
        self.assertLess(opening.index(CLEAR), opening.index(('set_country_flag', 'missiles_warning_active')))
        self.assertIn(CLEAR, nodes(EFFECTS['missiles_resolve_warning_queue_receipt']))
        self.assertIn(CLEAR, nodes(SCENARIO['missiles_scenario_seed_retaliation_warning']))
        self.assertIn(CLEAR, nodes(EFFECTS['missiles_cleanup_removed_country']))

    def test_each_route_records_its_outcome_after_resolution(self):
        self.assertTrue(outcome_follows_resolution(EFFECTS['missiles_accept_retaliation_response'],
                                                   'missiles_retaliation_response_accepted'))
        self.assertTrue(outcome_follows_resolution(EFFECTS['missiles_process_scheduled_warning_response'],
                                                   'missiles_warning_expired_without_launch'))
        self.assertTrue(outcome_follows_resolution(EFFECTS['missiles_complete_warning_verification'],
                                                   'missiles_warning_false_or_conflicting'))

    def test_delay_decision_is_once_per_warning(self):
        decision = dict(DECISIONS['missiles_delay_retaliation'])
        self.assertEqual(decision['fire_only_once'], 'no')
        self.assertIn(('NOT', [('has_country_flag', 'missiles_warning_delayed')]), decision['visible'])
        delay = event_options('chaosx.nr32.80')['chaosx.nr32.80.b']
        self.assertIn(('NOT', [('has_country_flag', 'missiles_warning_delayed')]), delay['trigger'])


class RefusedResponse(unittest.TestCase):
    def test_refused_order_restores_target_and_clears_lineage(self):
        route = dict(EFFECTS['missiles_accept_retaliation_response'])['if']
        keys = [key for key, _ in route]
        # The target choice is saved before the attacker overwrites it.
        self.assertLess(keys.index('missiles_save_target_choice_for_retaliation'), keys.index('set_variable'))
        self.assertLess(keys.index('missiles_save_target_choice_for_retaliation'), keys.index('missiles_prepare_operation'))
        self.assertEqual(route[-1], ('missiles_clear_saved_retaliation_target_choice', 'yes'))
        refused = dict(route)['else']
        refused_nodes = nodes(refused)
        for pending in ('missiles_pending_parent_incident_id', 'missiles_pending_root_incident_id',
                        'missiles_pending_root_country', 'missiles_pending_retaliation_generation'):
            self.assertIn(('clear_variable', pending), refused)
        for operation in ('missiles_operation_type', 'missiles_operation_strike_profile', 'missiles_operation_payload'):
            self.assertIn(('clear_variable', operation), refused_nodes)
        self.assertIn(('missiles_restore_target_choice_after_retaliation', 'yes'), refused)
        # No outcome is recorded and the warning is not resolved by a refusal.
        self.assertFalse(any(key == 'set_country_flag' and child in OUTCOME_FLAGS for key, child in refused_nodes))
        self.assertNotIn(RESOLVE, refused_nodes)
        self.assertNotIn(('country_event', [('id', 'chaosx.nr32.83'), ('days', 'missiles_operation_preparation_days')]), refused_nodes)

    def test_restore_returns_the_saved_choice_or_clears_it(self):
        restore = EFFECTS['missiles_restore_target_choice_after_retaliation']
        saved = dict(restore)['if']
        self.assertEqual(dict(saved)['limit'], [('has_variable', 'missiles_retaliation_saved_target')])
        self.assertIn(('set_variable', [('missiles_selected_target', 'missiles_retaliation_saved_target')]), saved)
        self.assertIn(('set_country_flag', 'missiles_target_selected'), saved)
        self.assertIn(('missiles_clear_target', 'yes'), dict(restore)['else'])
        save = nodes(EFFECTS['missiles_save_target_choice_for_retaliation'])
        self.assertIn(('set_variable', [('missiles_retaliation_saved_target', 'missiles_selected_target')]), save)


if __name__ == '__main__':
    unittest.main()
