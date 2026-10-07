"""Execute bounded custody/refund source against concrete reserve ledgers.

The model covers variables, flags, arrays, scopes and arithmetic. Presentation,
native missions and conventional-payload cleanup have no modeled ledger effects.
It does not establish engine timing or special-payload behavior.
"""
from copy import deepcopy
from decimal import Decimal, InvalidOperation
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


CORE = source('common/scripted_effects/032_missiles_effects.txt')
OPS = source('common/scripted_effects/032_missiles_operations_effects.txt')
TRIGGERS = {**source('common/scripted_triggers/032_missiles_triggers.txt'),
            **source('common/scripted_triggers/032_missiles_operations_triggers.txt')}
CONSTANTS = source('common/script_constants/032_missiles_constants.txt')
EFFECTS = {**CORE, **OPS}


def scope(**variables):
    return {'vars': variables, 'flags': set(), 'arrays': {}}


class Ledger:
    def __init__(self, free=12, escrow=4, capacities=(10, 10), allocations=(4, 0)):
        self.owner = scope(missiles_operational_reserve=free, missiles_reserved_reserve=escrow,
                           missiles_active_operation_id=7, missiles_operation_missile_cost=escrow,
                           missiles_operation_state=2)
        self.foreign = scope(missiles_operational_reserve=90)
        self.root = self.owner
        self.sites = [scope(missiles_site_capacity=c, missiles_site_operation_allocation=a,
                            missiles_site_operation_id=7, missiles_site_reserve=0)
                      for c, a in zip(capacities, allocations)]
        for site in self.sites:
            site['controller'] = self.owner
        self.owner['arrays'] = {'missiles_launch_site_states': self.sites[:], 'missiles_operation_sites': self.sites[:]}
        self.owner['flags'] = {'missiles_operation_active', 'missiles_operation_reserve_receipt_active'}
        self.targets = {'missiles_lost_allocation_site': self.sites[0]}
        self.temp = {'missiles_allocation_loss_mode': 1}
        self.refreshes = 0

    def selected(self, key, stack):
        if key == 'ROOT':
            return self.root
        if key == 'PREV':
            return stack[-2]
        if key.startswith('event_target:'):
            return self.targets[key.split(':', 1)[1]]
        return None

    def number(self, token, stack):
        if token.startswith('constant:'):
            group, field = token[9:].split('.', 1)
            return Decimal(value(CONSTANTS[group], field))
        if '.' in token:
            prefix, field = token.split('.', 1)
            selected = self.selected(prefix, stack)
            return selected['vars'].get(field, 0) if selected is not None else 0
        if token in self.temp:
            return self.temp[token]
        if token.endswith('^num'):
            return len(stack[-1]['arrays'].get(token[:-4], []))
        try:
            return Decimal(token)
        except InvalidOperation:
            return stack[-1]['vars'].get(token, 0)

    def condition(self, nodes, stack):
        return all(self.term(k, v, stack) for k, v in nodes)

    def term(self, key, body, stack):
        obj = stack[-1]
        selected = self.selected(key, stack)
        if selected is not None:
            return self.condition(body, [*stack, selected])
        if key in ('AND', 'limit'):
            return self.condition(body, stack)
        if key == 'NOT':
            return not any(self.term(k, v, stack) for k, v in body)
        if key == 'OR':
            return any(self.term(k, v, stack) for k, v in body)
        if key == 'has_variable':
            return body in obj['vars']
        if key in ('has_country_flag', 'has_state_flag'):
            return body in obj['flags']
        if key == 'has_event_target':
            return body in self.targets
        if key == 'is_controlled_by':
            return obj.get('controller') is self.selected(body, stack)
        if key == 'scope_exists':
            return True
        if key == 'impassable':
            return body == 'no'
        if key == 'is_in_array':
            return self.number(value(body, 'value'), stack) in obj['arrays'].get(value(body, 'array'), [])
        if key == 'check_variable':
            fields = dict(body)
            a, b = self.number(fields['var'], stack), self.number(fields['value'], stack)
            return {'equals': a == b, 'greater_than': a > b, 'less_than': a < b,
                    'greater_than_or_equals': a >= b, 'less_than_or_equals': a <= b}[fields['compare']]
        if key in TRIGGERS:
            return self.condition(TRIGGERS[key], stack)
        raise AssertionError(('unmodeled trigger', key))

    def run(self, name):
        self.execute(EFFECTS[name], [self.owner])

    def execute(self, nodes, stack):
        branch_taken = False
        for key, body in nodes:
            obj = stack[-1]
            selected = self.selected(key, stack)
            if selected is not None:
                self.execute(body, [*stack, selected])
            elif key in ('if', 'else_if', 'else'):
                allowed = key == 'if' or not branch_taken
                if key == 'if':
                    branch_taken = False
                if allowed and (key == 'else' or self.condition(value(body, 'limit'), stack)):
                    self.execute([(k, v) for k, v in body if k != 'limit'], stack)
                    branch_taken = True
            elif key == 'for_each_scope_loop':
                for member in obj['arrays'][value(body, 'array')][:]:
                    self.execute([(k, v) for k, v in body if k != 'array'], [*stack, member])
            elif key == 'every_controlled_state':
                for member in self.sites:
                    child_stack = [*stack, member]
                    if member['controller'] is obj and self.condition(value(body, 'limit'), child_stack):
                        self.execute([(k, v) for k, v in body if k != 'limit'], child_stack)
            elif key in ('set_variable', 'set_temp_variable', 'add_to_variable', 'subtract_from_variable', 'subtract_from_temp_variable'):
                field, token = body[0]
                target = self.temp if 'temp' in key else obj['vars']
                amount = self.number(token, stack)
                target[field] = amount if key.startswith('set_') else target.get(field, 0) + (-amount if key.startswith('subtract_') else amount)
            elif key == 'clamp_temp_variable':
                fields = dict(body)
                result = self.temp[fields['var']]
                if 'max' in fields:
                    result = min(result, self.number(fields['max'], stack))
                if 'min' in fields:
                    result = max(result, self.number(fields['min'], stack))
                self.temp[fields['var']] = result
            elif key == 'clear_variable':
                obj['vars'].pop(body, None)
            elif key == 'clear_array':
                obj['arrays'][body] = []
            elif key == 'add_to_array':
                obj['arrays'].setdefault(value(body, 'array'), []).append(self.number(value(body, 'value'), stack))
            elif key == 'set_country_flag':
                obj['flags'].add(body)
            elif key == 'clr_country_flag':
                obj['flags'].discard(body)
            elif key == 'missiles_set_program_phases':
                self.refreshes += 1
            elif key in ('remove_mission', 'missiles_release_operation_payload', 'missiles_back_to_target_profiles', 'missiles_recalculate_network'):
                pass
            elif key in EFFECTS:
                self.execute(EFFECTS[key], stack)
            else:
                raise AssertionError(('unmodeled effect', key))


class ReserveCustody(unittest.TestCase):
    def test_network_totals_follow_the_defender_with_a_foreign_root(self):
        ledger = Ledger(capacities=(4, 8))
        ledger.root = ledger.foreign
        for index, site in enumerate(ledger.sites):
            site['flags'].add('missiles_site_active')
            site['vars']['missiles_site_strategic_region'] = index + 1
        foreign = deepcopy(ledger.foreign)
        ledger.run('missiles_recalculate_network')
        self.assertEqual(ledger.owner['vars']['missiles_active_site_count'], 2)
        self.assertEqual(ledger.owner['vars']['missiles_total_site_capacity'], 12)
        self.assertEqual(ledger.owner['vars']['missiles_active_site_region_count'], 2)
        self.assertEqual(ledger.foreign, foreign)

    def test_sealed_recapture_debits_only_the_proven_former_held_ledger(self):
        capture = value(OPS['missiles_handle_site_control_changed'], 'if')
        former = value(capture, 'event_target:missiles_capture_former_controller')
        for held, site_stock, transferred in ((8, 8, 8), (3, 8, 3), (8, 3, 3), (0, 8, 0)):
            ledger = Ledger()
            ledger.owner['vars']['missiles_captured_reserve_held'] = held
            ledger.sites[0]['vars']['missiles_site_captured_reserve'] = site_stock
            ledger.temp['missiles_captured_reserve_amount'] = 0
            ledger.temp['missiles_recaptured_reserve_amount'] = 0
            ledger.execute(former, [ledger.sites[0], ledger.owner])
            self.assertEqual(ledger.owner['vars']['missiles_captured_reserve_held'], held - transferred)
            self.assertEqual(ledger.temp['missiles_recaptured_reserve_amount'], transferred)
            self.assertEqual(ledger.owner['vars']['missiles_operational_reserve'], 12)

    def test_incoming_damage_reads_its_state_receipt_without_a_country_shadow(self):
        ledger = Ledger()
        ledger.owner['flags'].add('missiles_program_initialized')
        ledger.targets['missiles_incoming_damage_state'] = ledger.sites[0]
        receipt = value(OPS['missiles_record_incoming_operation_site_damage'], 'if')
        self.assertTrue(ledger.condition(value(receipt, 'limit'), [ledger.owner]))
        field = 'missiles_incoming_damage_actor_id'
        ledger.sites[0]['vars'][field] = 77
        ledger.owner['vars'][field] = 999
        copy_actor = next(body for key, body in receipt if key == 'set_variable' and body[0][0] == 'missiles_last_incident_actor_id')
        ledger.execute([('set_variable', copy_actor)], [ledger.owner])
        self.assertEqual(ledger.owner['vars']['missiles_last_incident_actor_id'], 77)

    def test_free_and_escrow_never_fill_the_same_physical_slot(self):
        for free in range(21):
            for reserved in range(11):
                ledger = Ledger(free=free, escrow=reserved, allocations=(reserved, 0))
                ledger.run('missiles_rebalance_site_custody')
                stocks = [site['vars']['missiles_site_reserve'] for site in ledger.sites]
                self.assertEqual(sum(stocks) + ledger.owner['vars']['missiles_unallocated_reserve'], free)
                self.assertLessEqual(stocks[0] + reserved, 10)
                self.assertLessEqual(stocks[1], 10)

    def test_foreign_root_and_stale_foreign_registry_entry_do_not_mutate_foreign_stock(self):
        ledger = Ledger()
        ledger.root = ledger.foreign
        ledger.sites[1]['controller'] = ledger.foreign
        ledger.sites[1]['vars']['missiles_site_reserve'] = 8
        foreign = deepcopy(ledger.foreign)
        ledger.run('missiles_rebalance_site_custody')
        self.assertEqual(ledger.sites[0]['vars']['missiles_site_reserve'], 6)
        self.assertEqual(ledger.sites[1]['vars']['missiles_site_reserve'], 8)
        self.assertEqual(ledger.owner['vars']['missiles_unallocated_reserve'], 6)
        self.assertEqual(ledger.foreign, foreign)

    def test_lost_allocation_does_not_redistribute_the_free_site_snapshot(self):
        ledger = Ledger()
        ledger.run('missiles_rebalance_site_custody')
        original = [s['vars']['missiles_site_reserve'] for s in ledger.sites]
        ledger.root = ledger.foreign
        ledger.run('missiles_settle_lost_site_allocation')
        self.assertEqual(ledger.owner['vars']['missiles_operational_reserve'], 12)
        self.assertEqual([s['vars']['missiles_site_reserve'] for s in ledger.sites], original)
        self.assertEqual(ledger.refreshes, 0)
        self.assertNotIn('missiles_site_settlement_in_progress', ledger.owner['flags'])
        # The caller destroys precisely the free missiles physically at the site.
        ledger.owner['vars']['missiles_operational_reserve'] -= original[0]
        ledger.owner['arrays']['missiles_launch_site_states'].remove(ledger.sites[0])
        ledger.run('missiles_rebalance_site_custody')
        self.assertEqual(ledger.owner['vars']['missiles_operational_reserve'], 6)
        self.assertEqual(ledger.sites[1]['vars']['missiles_site_reserve'], 6)
        ledger.run('missiles_settle_lost_site_allocation')
        self.assertEqual(ledger.owner['vars']['missiles_operational_reserve'], 6)

    def test_refund_mode_and_ordinary_abort_return_the_full_reservation_once(self):
        for loss_mode in (False, True):
            ledger = Ledger()
            ledger.run('missiles_rebalance_site_custody')
            if loss_mode:
                ledger.temp['missiles_allocation_loss_mode'] = 0
                ledger.run('missiles_settle_lost_site_allocation')
            else:
                ledger.run('missiles_abort_operation')
                ledger.run('missiles_cleanup_operation')
            self.assertEqual(ledger.owner['vars']['missiles_operational_reserve'], 16)
            self.assertEqual(ledger.owner['vars']['missiles_reserved_reserve'], 0)
            ledger.run('missiles_abort_operation')
            ledger.run('missiles_cleanup_operation')
            self.assertEqual(ledger.owner['vars']['missiles_operational_reserve'], 16)


if __name__ == '__main__':
    unittest.main()
