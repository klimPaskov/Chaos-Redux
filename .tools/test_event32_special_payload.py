"""Source-contract tests for Event 032 special-payload orders and reservation.

Players and AI choose the warhead family to integrate, the active payload, and
the standing use policy through costed decisions; a prepared special
operation holds its warhead once from preparation, returns it on abort or
cancellation, and consumes it once at release. This is source evidence, not an
engine simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
EVENTS = {value(body, 'id'): body for key, body in parse((ROOT / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig')) if key == 'country_event'}
ORDERS = {
    'missiles_integrate_special_payload': 'chaosx.nr32.30',
    'missiles_select_special_payload': 'chaosx.nr32.31',
    'missiles_set_special_payload_policy': 'chaosx.nr32.32',
}


def nodes(body):
    return list(descendants(body))


def options(event):
    return {value(body, 'name'): body for key, body in EVENTS[event] if key == 'option'}


class SpecialPayloadContract(unittest.TestCase):
    def test_three_costed_orders_open_their_choice_events(self):
        for name, event in ORDERS.items():
            decision = dict(DECISIONS[name])
            with self.subTest(decision=name):
                self.assertIn(('country_event', [('id', event)]), nodes(decision['complete_effect']))
                self.assertIn(('missiles_special_payload_orders_are_visible', 'yes'), decision['visible'])
                self.assertTrue(any(k == 'add_command_power' for k, _ in nodes(decision['complete_effect'])))
                self.assertIn('days_re_enable', decision)
                self.assertIn('custom_cost_text', decision)
                self.assertIn('ai_will_do', decision)
        self.assertNotIn(('missiles_integrate_special_payload', 'yes'), nodes(value(DECISIONS['missiles_integrate_special_payload'], 'complete_effect')))
        self.assertIn(('missiles_special_warheads_active', 'yes'), TRIGGERS['missiles_special_payload_orders_are_visible'])

    def test_conventional_is_always_selectable_and_integration_sets_policy(self):
        select = options('chaosx.nr32.31')
        self.assertNotIn('trigger', dict(select['chaosx.nr32.31.a']))
        self.assertIn(('missiles_selected_payload', 'constant:missiles_payload.conventional'), nodes(select['chaosx.nr32.31.a']))
        integrate = options('chaosx.nr32.30')
        for letter in 'abcd':
            body = nodes(integrate[f'chaosx.nr32.30.{letter}'])
            self.assertIn(('country_event', [('id', 'chaosx.nr32.32'), ('days', '1')]), body)
        self.assertEqual(value(integrate['chaosx.nr32.30.e'], 'trigger'), [('NOT', [('missiles_country_has_unintegrated_payload_candidate', 'yes')])])
        for letter, body in options('chaosx.nr32.32').items():
            self.assertIn('custom_effect_tooltip', dict(body), letter)

    def test_payload_is_reserved_with_the_missiles_or_the_order_is_refused(self):
        reserve = EFFECTS['missiles_reserve_operation_resources']
        guard = next(body for key, body in reserve if key == 'if' and ('missiles_reserve_operation_payload', 'yes') in body)
        refusal = value(guard, 'if')
        self.assertIn(('missiles_refund_operation_reserve', 'yes'), refusal)
        self.assertIn(('set_variable', [('missiles_operation_resource_result', 'constant:missiles_result.rejected')]), refusal)
        keys = [k for k, _ in reserve]
        self.assertLess(keys.index('if'), len(keys))
        payload = nodes(EFFECTS['missiles_reserve_operation_payload'])
        self.assertIn(('add_nuclear_bombs', 'constant:missiles_resolution.nuclear_payload_units_negative'), payload)
        self.assertIn(('missiles_debit_biological_payload', 'yes'), payload)
        self.assertIn(('missiles_check_chemical_payload_stock', 'yes'), payload)
        self.assertIn(('set_country_flag', 'missiles_operation_payload_escrow_active'), payload)

    def test_held_warhead_returns_once_or_is_consumed_once(self):
        release = EFFECTS['missiles_release_operation_payload']
        guarded = value(release, 'if')
        self.assertEqual(value(guarded, 'limit'), [('has_country_flag', 'missiles_operation_payload_escrow_active')])
        returned = nodes(guarded)
        self.assertIn(('add_nuclear_bombs', 'constant:missiles_resolution.nuclear_payload_units'), returned)
        for bomb in ('anthrax_bomb_1', 'plague_bomb_1', 'tularemia_bomb_1', 'smallpox_bomb_1'):
            self.assertIn(('type', bomb), returned)
        self.assertIn(('clr_country_flag', 'missiles_operation_payload_escrow_active'), release)
        cleanup = value(EFFECTS['missiles_cleanup_operation'], 'if')
        self.assertIn(('missiles_release_operation_payload', 'yes'), cleanup)
        consume = EFFECTS['missiles_consume_special_payload']
        first = next(body for key, body in consume if key == 'if')
        self.assertIn(('has_country_flag', 'missiles_operation_payload_escrow_active'), value(first, 'limit'))
        self.assertIn(('clr_country_flag', 'missiles_operation_payload_escrow_active'), first)
        self.assertIn(('set_country_flag', 'missiles_operation_payload_debit_verified'), first)
        self.assertNotIn('add_nuclear_bombs', [k for k, _ in nodes(first)])

    def test_objective_step_stays_within_six_actions(self):
        shown = [name for name, body in DECISIONS.items() if ('missiles_target_profile_menu_is_open', 'yes') in nodes(dict(body).get('visible', []))]
        family = [name for name in shown if 'family' in name]
        self.assertEqual(len(family), 2)
        self.assertLessEqual(len(family) + 1 + len(ORDERS), 6)
        orders = nodes(TRIGGERS['missiles_special_payload_orders_are_visible'])
        self.assertIn(('NOT', [('has_country_flag', 'missiles_target_profile_tactical_menu')]), orders)
        self.assertIn(('NOT', [('has_country_flag', 'missiles_operation_active')]), orders)


if __name__ == '__main__':
    unittest.main()
