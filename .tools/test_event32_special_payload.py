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
RECEIPT_ADAPTER = source('common/scripted_effects/032_missiles_payload_receipt_effects.txt')
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
    def test_country_removal_does_not_inherit_an_outer_loop_break(self):
        body = RECEIPT_ADAPTER['missiles_settle_chemical_payloads_on_removal']
        iteration = value(body, 'for_each_scope_loop')
        owned_break = value(iteration, 'break')
        self.assertNotEqual(owned_break, 'break')
        initializer = ('set_temp_variable', [(owned_break, 'constant:cbrn_math.zero')])
        self.assertIn(initializer, body[:body.index(('for_each_scope_loop', iteration))])

    def test_failed_commit_settles_receipts_and_retains_a_chemical_reason(self):
        final_refusal = [body for key, body in EFFECTS['missiles_commit_operation'] if key == 'else_if'][-1]
        calls = [key for key, _ in final_refusal]
        self.assertLess(calls.index('missiles_record_preparation_failure'), calls.index('missiles_abort_operation'))
        self.assertLess(calls.index('missiles_abort_operation'), calls.index('missiles_cleanup_operation'))
        reason = next(body for key, body in EFFECTS['missiles_record_preparation_failure']
                      if isinstance(body, list) and ('missiles_operation_has_paid_chemical_receipt', 'yes') in nodes(body))
        self.assertIn(('set_variable', [('missiles_last_preparation_failure', 'constant:missiles_preparation_failure.chemical_agent')]), reason)

    def test_biological_debit_proof_survives_return_to_each_consuming_caller(self):
        for name in ('missiles_reserve_operation_payload', 'missiles_consume_special_payload'):
            branch = next(body for key, body in EFFECTS[name]
                          if isinstance(body, list) and ('missiles_debit_biological_payload', 'yes') in body)
            debit_index = branch.index(('missiles_debit_biological_payload', 'yes'))
            self.assertIn(('set_temp_variable', [('missiles_biological_payload_debit_proof', 'constant:bio_lifecycle_proof.missing')]), branch[:debit_index])
            accepted = next(body for key, body in branch[debit_index + 1:] if key == 'if')
            self.assertIn(('check_variable', [('var', 'missiles_biological_payload_debit_proof'), ('value', 'constant:bio_lifecycle_proof.supplied'), ('compare', 'equals')]), value(accepted, 'limit'))

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
        self.assertIn(('missiles_reserve_chemical_payload_receipt', 'yes'), payload)
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



class ChemicalLaunchCheck(unittest.TestCase):
    def test_chemical_agent_is_proven_again_before_commitment(self):
        commit = EFFECTS['missiles_commit_operation']
        keys = [key for key, _ in commit]
        self.assertEqual(commit[0], ('set_temp_variable', [('missiles_commit_payload_ready', 'constant:missiles_program_value.one')]))
        check = commit[1][1]
        self.assertEqual(commit[1][0], 'if')
        self.assertIn(('check_variable', [('var', 'missiles_operation_payload'), ('value', 'constant:missiles_payload.chemical'), ('compare', 'equals')]), value(check, 'limit'))
        self.assertIn(('missiles_check_chemical_receipt_for_commit', 'yes'), check)
        # A failed check takes the invalidated path with an exact refund and no launch.
        refused = commit[2][1]
        self.assertEqual(commit[2][0], 'if')
        self.assertIn(('check_variable', [('var', 'missiles_commit_payload_ready'), ('value', 'constant:missiles_program_value.zero'), ('compare', 'equals')]), value(refused, 'limit'))
        refused_keys = [key for key, _ in refused]
        self.assertLess(refused_keys.index('missiles_abort_operation'), refused_keys.index('missiles_cleanup_operation'))
        self.assertIn(('set_variable', [('missiles_last_preparation_failure', 'constant:missiles_preparation_failure.chemical_agent')]), refused)
        self.assertIn(('set_country_flag', 'missiles_preparation_failure_unread'), refused)
        self.assertNotIn(('missiles_resolve_operation', 'yes'), nodes(refused))
        self.assertNotIn(('set_country_flag', 'missiles_operation_committed'), nodes(refused))
        # Only the chemical check can clear the ready marker, so other payloads commit as before.
        self.assertEqual(keys[3], 'else_if')
        launch = commit[3][1]
        self.assertEqual(value(launch, 'limit'), [('missiles_operation_can_be_committed', 'yes')])
        self.assertIn(('missiles_resolve_operation', 'yes'), launch)
        setters = [child for key, child in nodes(commit) if key == 'set_temp_variable' and child[0][0] == 'missiles_commit_payload_ready']
        self.assertEqual(len(setters), 2)

    def test_chemical_failure_reason_is_localised(self):
        constants = (ROOT / 'common/script_constants/032_missiles_constants.txt').read_text(encoding='utf-8')
        block = constants.split('missiles_preparation_failure = {', 1)[1].split('missiles_preparation_cost', 1)[0]
        self.assertIn('chemical_agent = 11', block)
        scripted = (ROOT / 'common/scripted_localisation/032_missiles_localisation.txt').read_text(encoding='utf-8')
        self.assertIn('localization_key = missiles_preparation_failure_chemical_agent', scripted)
        loc = (ROOT / 'localisation/english/032_missiles_decisions_l_english.yml').read_bytes()
        self.assertTrue(loc.startswith(bytes([0xEF, 0xBB, 0xBF])))
        keys = [line.split(':', 1)[0] for line in loc.decode('utf-8-sig').splitlines()]
        self.assertIn('missiles_preparation_failure_chemical_agent', keys)


if __name__ == '__main__':
    unittest.main()
