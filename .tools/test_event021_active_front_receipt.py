"""Execute the actual active-front receipt validator on bounded fixtures.

This is not an engine simulation. Only the validator and its integer helper
are executed; object ownership and capacities are declared fixture inputs.
Decimal arithmetic models four-decimal script values. Scoped saved values,
temporary scalars, and temporary arrays are separate, and helper return drops
storage that was not initialized by its caller.
"""
from dataclasses import dataclass
from decimal import Decimal
import operator
import unittest

from test_event021_evolution_log import Country, load


ACTIVE = dict(load('common/scripted_effects/021_random_civil_war_active_evolution_effects.txt'))
CONSTANTS = dict(load('common/script_constants/021_random_civil_war_constants.txt'))
PREFIX = 'random_civil_war_active_front_'
INTEGER_COLUMNS = ('ids', 'source_ids', 'generations', 'actor_types', 'archetypes',
                   'goals', 'routes', 'relationships', 'package_ids', 'package_regions',
                   'package_depths', 'package_archetypes', 'statuses', 'force_divisions',
                   'state_offsets', 'state_counts')
READY = 'random_civil_war_active_front_transaction_ready'


@dataclass(eq=False)
class State:
    id: int
    owner: Country
    controller: Country


class ReceiptRuntime:
    def __init__(self):
        self.host = Country(1)
        self.source = Country(2)
        self.temporary = {}
        self.temp_arrays = {}
        self.globals = {'random_civil_war_max_active_fronts': Decimal(20),
                        'random_civil_war_active_front_count': Decimal(2)}
        self.targets = {'random_civil_war_active_review_source': self.source}
        states = [State(i, self.source, self.source) for i in (10, 11, 12)]
        for column in INTEGER_COLUMNS:
            self.host.values[PREFIX + column] = [Decimal(1), Decimal(1)]
        for column, rows in {
            'ids': [10001, 10002], 'source_ids': [9, 9], 'generations': [0, 0],
            'state_offsets': [0, 1], 'state_counts': [1, 2], 'force_divisions': [2, 3],
            'anchors': [states[0], states[2]], 'actor_scopes': [self.source, self.source],
            'sizes': [Decimal('.1250'), Decimal('.1875')],
            'navy_ratios': [Decimal('.0500'), Decimal('.0750')],
            'air_ratios': [Decimal('.1000'), Decimal('.1000')], 'state_entries': states,
        }.items():
            self.host.values[PREFIX + column] = rows

    def value(self, token, actor):
        if token == 'THIS':
            return actor
        if token.startswith('constant:'):
            group, key = token[9:].split('.', 1)
            return Decimal(dict(CONSTANTS[group])[key])
        if '^' in token:
            name, index = token.split('^', 1)
            rows = self.value(name, actor)
            return Decimal(len(rows)) if index == 'num' else rows[int(self.value(index, actor))]
        if token.startswith('global.'):
            return self.globals.get(token[7:], Decimal(0))
        if token in self.temporary:
            return self.temporary[token]
        if token in self.temp_arrays:
            return self.temp_arrays[token]
        if token in actor.values:
            return actor.values[token]
        return Decimal(token)

    def condition(self, nodes, actor):
        comparisons = {'equals': operator.eq, 'less_than': operator.lt,
                       'less_than_or_equals': operator.le, 'greater_than': operator.gt,
                       'greater_than_or_equals': operator.ge}
        for key, data in nodes:
            if key == 'OR':
                result = any(self.condition([node], actor) for node in data)
            elif key == 'NOT':
                result = not any(self.condition([node], actor) for node in data)
            elif key == 'check_variable':
                fields = dict(data)
                result = comparisons[fields['compare']](self.value(fields['var'], actor),
                                                        self.value(fields['value'], actor))
            elif key == 'has_variable':
                result = data[7:] in self.globals if data.startswith('global.') else data in actor.values
            elif key == 'is_in_array':
                fields = dict(data)
                result = self.value(fields['value'], actor) in self.value(fields['array'], actor)
            elif key in ('is_owned_by', 'is_controlled_by'):
                expected = self.targets[data.removeprefix('event_target:')]
                result = (actor.owner if key == 'is_owned_by' else actor.controller) is expected
            else:
                raise AssertionError(f'Unmodelled receipt predicate: {key}')
            if not result:
                return False
        return True

    def call(self, name, actor):
        scalars, arrays = set(self.temporary), set(self.temp_arrays)
        self.run(ACTIVE[name], actor)
        self.temporary = {k: v for k, v in self.temporary.items() if k in scalars}
        self.temp_arrays = {k: v for k, v in self.temp_arrays.items() if k in arrays}

    def run(self, nodes, actor):
        for key, data in nodes:
            if key == 'if':
                if self.condition(dict(data)['limit'], actor):
                    self.run([(k, v) for k, v in data if k != 'limit'], actor)
            elif key in ('set_temp_variable', 'subtract_from_temp_variable', 'add_to_temp_variable'):
                name, token = data[0]
                number = self.value(token, actor)
                if key == 'set_temp_variable':
                    self.temporary[name] = number
                else:
                    self.temporary[name] += number if key == 'add_to_temp_variable' else -number
            elif key == 'modulo_temp_variable':
                fields = dict(data)
                self.temporary[fields['var']] %= self.value(fields['value'], actor)
            elif key == 'clear_temp_array':
                self.temp_arrays[data] = []
            elif key == 'add_to_temp_array':
                fields = dict(data)
                self.temp_arrays[fields['array']].append(self.value(fields['value'], actor))
            elif key in ('for_each_loop', 'for_each_scope_loop'):
                fields = dict(data)
                body = [(k, v) for k, v in data if k not in ('array', 'value', 'index', 'break')]
                for index, row in enumerate(list(self.value(fields['array'], actor))):
                    if key == 'for_each_loop':
                        self.temporary[fields['value']] = row
                        if 'index' in fields:
                            self.temporary[fields['index']] = Decimal(index)
                    self.run(body, row if key == 'for_each_scope_loop' else actor)
                    if self.temporary.get(fields.get('break', 'break'), Decimal(0)):
                        break
            elif key in ('set_country_flag', 'clr_country_flag'):
                (actor.flags.add if key == 'set_country_flag' else actor.flags.discard)(data)
            elif key in ACTIVE:
                self.call(key, actor)
            else:
                raise AssertionError(f'Unmodelled receipt effect: {key}')

    def validate(self):
        self.call('event021_parent_validate_active_front_receipt', self.host)
        return READY in self.host.flags


class ActiveFrontReceiptTests(unittest.TestCase):
    def test_exact_integer_rows_with_fractional_asset_ratios_are_ready(self):
        rt = ReceiptRuntime()
        before = {k: list(v) for k, v in rt.host.values.items()}
        self.assertTrue(rt.validate())
        self.assertEqual(rt.host.values, before)
        self.assertEqual(rt.temporary, {})
        self.assertEqual(rt.temp_arrays, {})

    def test_each_integer_column_rejects_fraction_without_rewriting_it(self):
        for column in INTEGER_COLUMNS:
            for fraction in (Decimal('.0001'), Decimal('.5000')):
                with self.subTest(column=column, fraction=fraction):
                    rt = ReceiptRuntime()
                    rt.host.values[PREFIX + column][0] += fraction
                    before = list(rt.host.values[PREFIX + column])
                    self.assertFalse(rt.validate())
                    self.assertEqual(rt.host.values[PREFIX + column], before)

    def test_balanced_fractional_spans_do_not_pass_exhaustive_coverage(self):
        rt = ReceiptRuntime()
        rt.host.values[PREFIX + 'state_counts'] = [Decimal('1.5000'), Decimal('1.5000')]
        rt.host.values[PREFIX + 'state_offsets'] = [Decimal(0), Decimal('1.5000')]
        self.assertFalse(rt.validate())

    def test_helper_checks_late_fields_without_borrowing_loop_control(self):
        rt = ReceiptRuntime()
        rt.temporary.update(event021_active_receipt_row=Decimal(1),
                            event021_active_receipt_valid=Decimal(1),
                            **{'break': Decimal(1), 'i': Decimal(777)})
        rt.host.values[PREFIX + 'state_counts'][1] = Decimal('2.0001')
        rt.call('event021_parent_validate_active_front_row_integers', rt.host)
        self.assertEqual(rt.temporary['event021_active_receipt_valid'], 0)
        self.assertEqual(rt.temporary['break'], 1)
        self.assertEqual(rt.temporary['i'], 777)
        self.assertEqual(set(rt.temporary), {'event021_active_receipt_row',
                                             'event021_active_receipt_valid', 'break', 'i'})
        self.assertEqual(rt.temp_arrays, {})

    def test_stale_ready_flag_is_removed_on_bad_receipt(self):
        rt = ReceiptRuntime()
        rt.host.flags.add(READY)
        rt.host.values[PREFIX + 'force_divisions'][0] = Decimal('2.5000')
        self.assertFalse(rt.validate())

    def test_original_identity_span_ownership_and_capacity_guards(self):
        cases = {
            'zero id': lambda r: r.host.values[PREFIX + 'ids'].__setitem__(0, 0),
            'duplicate id': lambda r: r.host.values[PREFIX + 'ids'].__setitem__(1, 10001),
            'missing column': lambda r: r.host.values[PREFIX + 'goals'].pop(),
            'duplicate state': lambda r: r.host.values[PREFIX + 'state_entries'].__setitem__(1, r.host.values[PREFIX + 'state_entries'][0]),
            'lost control': lambda r: setattr(r.host.values[PREFIX + 'state_entries'][0], 'controller', r.host),
            'lost ownership': lambda r: setattr(r.host.values[PREFIX + 'state_entries'][0], 'owner', r.host),
            'wrong anchor': lambda r: r.host.values[PREFIX + 'anchors'].__setitem__(1, r.host.values[PREFIX + 'state_entries'][0]),
            'capacity full': lambda r: r.globals.update(random_civil_war_active_front_count=20),
            'span gap': lambda r: r.host.values[PREFIX + 'state_offsets'].__setitem__(1, 2),
            'short coverage': lambda r: r.host.values[PREFIX + 'state_counts'].__setitem__(1, 1),
        }
        for name, change in cases.items():
            with self.subTest(name=name):
                rt = ReceiptRuntime()
                change(rt)
                self.assertFalse(rt.validate())


if __name__ == '__main__':
    unittest.main()
