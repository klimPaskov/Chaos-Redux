"""Bounded source regressions for the unpublished Event 021 ledger repair.

Checks helper output lifetime and the final native-mutation guard. This does
not simulate countries, force transfer, rollback restoration, or the engine.
"""
import unittest

from test_event021_evolution_log import PARENT, Runtime, load


LEDGER = dict(load('common/scripted_effects/021_random_civil_war_front_ledger_effects.txt'))


def descendants(nodes):
    for key, data in nodes:
        yield key, data
        if isinstance(data, list):
            yield from descendants(data)


class RowRuntime(Runtime):
    def run(self, nodes, actor):
        for key, data in nodes:
            if key == 'add_to_temp_variable':
                name, token = data[0]
                self.temporary[name] += self.value(token, actor)
            elif key == 'round_temp_variable':
                self.temporary[data] = round(self.temporary[data])
            elif key == 'event021_parent_validate_front_ledger_row_span':
                self.call(LEDGER[key], actor)
            else:
                super().run([(key, data)], actor)

    def condition(self, nodes, actor):
        for key, data in nodes:
            if key == 'OR':
                if not any(self.condition([node], actor) for node in data):
                    return False
            elif key == 'AND':
                if not self.condition(data, actor):
                    return False
            elif key == 'check_variable' and dict(data)['compare'] in ('less_than', 'less_than_or_equals', 'greater_than_or_equals'):
                values = dict(data)
                left, right = self.value(values['var'], actor), self.value(values['value'], actor)
                comparison = {'less_than': lambda: left < right, 'less_than_or_equals': lambda: left <= right,
                              'greater_than_or_equals': lambda: left >= right}[values['compare']]
                if not comparison():
                    return False
            elif not super().condition([(key, data)], actor):
                return False
        return True


class LedgerContractTests(unittest.TestCase):
    def test_contiguous_row_counts_survive_helper_return(self):
        members = LEDGER['event021_parent_validate_front_ledger_members']
        row_loop = next(data for key, data in members if key == 'for_each_loop')
        call = ('event021_parent_validate_front_ledger_row_span', 'yes')
        at = row_loop.index(call)
        self.assertEqual(row_loop[at - 1], ('set_temp_variable', [('event021_ledger_count', 'constant:random_civil_war_value.zero')]))
        rt = RowRuntime()
        rt.temporary.update(event021_ledger_expected_offset=0, event021_planned_front_plan_valid=1,
                            event021_ledger_member_break=0)
        rt.globals.update(random_civil_war_planned_front_state_counts=[1, 2],
                          random_civil_war_planned_front_state_offsets=[0, 1],
                          random_civil_war_planned_front_state_entries=[10, 11, 12],
                          random_civil_war_planned_front_anchor_entries=[10, 12])
        for row in range(2):
            rt.temporary['event021_ledger_row_index'] = row
            rt.run(row_loop[at - 1:at + 2], rt.sender)
            self.assertEqual(rt.temporary['event021_ledger_count'], (1, 2)[row])
            self.assertEqual(rt.temporary['event021_planned_front_plan_valid'], 1)
        self.assertEqual(rt.temporary['event021_ledger_expected_offset'], 3)

    def test_final_receipt_guards_all_native_branches_and_missile_preflight(self):
        starter = PARENT['event021_parent_start_secondary_civil_war']
        outer = next(data for key, data in starter if key == 'if')
        receipt = ('event021_parent_validate_secondary_transfer_receipt', 'yes')
        at = outer.index(receipt)
        self.assertEqual(outer[at - 1], ('set_temp_variable', [('event021_secondary_transfer_valid', 'constant:random_civil_war_value.zero')]))
        guard = outer[at + 1]
        self.assertEqual(guard[0], 'if')
        body = guard[1]
        self.assertEqual(dict(body)['limit'], [('check_variable', [
            ('var', 'event021_secondary_transfer_valid'), ('value', 'constant:random_civil_war_value.one'), ('compare', 'equals')])])
        guarded = list(descendants(body))
        self.assertEqual(sum(key == 'start_civil_war' for key, _ in guarded), 4)
        self.assertIn(('missiles_preflight_country_split', 'yes'), guarded)
        self.assertEqual(sum(key == 'start_civil_war' for key, _ in descendants(starter)), 4)
        self.assertEqual(outer[at + 2], ('else', [('event021_parent_reject_secondary_transfer', 'yes')]))
        rt = Runtime()
        for value, expected in ((0, False), (1, True)):
            rt.temporary['event021_secondary_transfer_valid'] = value
            self.assertEqual(rt.condition(dict(body)['limit'], rt.sender), expected)

    def test_both_rejection_paths_share_existing_cleanup(self):
        starter = PARENT['event021_parent_start_secondary_civil_war']
        calls = [node for node in descendants(starter) if node == ('event021_parent_reject_secondary_transfer', 'yes')]
        self.assertEqual(len(calls), 2)
        rejection = PARENT['event021_parent_reject_secondary_transfer']
        self.assertIn(('event021_parent_clear_pending_force_transaction', 'yes'), rejection)
        self.assertIn(('clr_global_flag', 'random_civil_war_secondary_front_pending'), rejection)
        self.assertIn(('clear_global_event_target', 'random_civil_war_secondary_source_country'), rejection)
        self.assertIn(('clear_variable', 'global.random_civil_war_pending_secondary_front_id'), rejection)


if __name__ == '__main__':
    unittest.main()
