"""Execute the production inheritance path with conservative helper temp lifetime.

Native flags, country/state ownership, variables and clamps are modelled.
The current Cohesion-row registry predicate is a declared fixture input; map
rewrite, engine date scheduling and native effects are outside these cases.
"""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('fallout_clausewitz', ROOT / '.tools/3d_pipeline/runtime/clausewitz.py')
module = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = module
spec.loader.exec_module(module)
parse = module.parse


def definition(source, name):
    text = re.search(r'^' + re.escape(name) + r' = \{[\s\S]*?^\}', source, re.M).group()
    return parse(text).children()[0]


constants = {}
for filename in ('fallout_consolidated_constants.txt', 'fallout_winter_recovery_memory_constants.txt'):
    text = (ROOT / 'common/script_constants' / filename).read_text(encoding='utf-8-sig')
    groups = ('fallout_winter_recovery_memory',) if filename.startswith('fallout_winter') else (
        'fallout_air_winter_memory', 'fallout_survival_resource', 'fallout_survival_numeric', 'fallout_runtime')
    for group in groups:
        category = definition(text, group)
        for key in category.children():
            if key.key != 'schema' and not isinstance(key.value, list):
                try:
                    constants['constant:' + category.key + '.' + key.key] = float(key.value)
                except ValueError:
                    pass

main = (ROOT / 'common/scripted_effects/fallout_consolidated_effects.txt').read_text(encoding='utf-8-sig')
functions = {name: definition(main, name) for name in (
    'fallout_air_winter_apply_survivor_memory', 'fallout_air_winter_clear_survivor_memory_flags',
    'fallout_survival_apply_cohesion_delta', 'fallout_orientation_apply_cohesion_loss',
    'fallout_orientation_clamp_resources')}
functions.update({n.key: n for n in parse((ROOT / 'common/scripted_effects/fallout_winter_recovery_memory_effects.txt').read_text()).children()})


class World:
    def __init__(self, states=(), value=50, generation=1):
        self.country = {'flags': set(), 'vars': {
            **{'fallout_survival_current_entries^' + str(i): value for i in range(1, 10)},
            'fallout_survival_current_entries^num': 10,
            'fallout_survival_cohesion_current': value}, 'states': list(states)}
        self.temps = {}
        self.generation = generation

    def number(self, value, scope):
        if value == 'global.fallout_transition_generation':
            return self.generation
        if value in constants:
            return constants[value]
        try:
            return float(value)
        except ValueError:
            return self.temps.get(value, scope['vars'].get(value, 0))

    def conditions(self, nodes, scope):
        answers = []
        for node in nodes:
            key = node.key
            if key == 'OR':
                answers.append(any(self.conditions([n], scope) for n in node.children()))
            elif key == 'AND':
                answers.append(self.conditions(node.children(), scope))
            elif key == 'NOT':
                answers.append(not self.conditions(node.children(), scope))
            elif key == 'any_owned_state':
                answers.append(any(self.conditions(node.children(), state) for state in self.country['states']))
            elif key in ('has_state_flag', 'has_country_flag'):
                answers.append(node.value in scope['flags'])
            elif key == 'has_variable':
                answers.append(node.value in scope['vars'] or node.value in self.temps)
            elif key == 'is_controlled_by':
                assert node.value == 'PREV'
                answers.append(scope.get('controlled', True))
            elif key == 'check_variable':
                var = node.scalar('var')
                compare = node.scalar('compare', 'equals')
                if var is None and node.children()[0].key == '':
                    var, operator, value = [n.value for n in node.children()]
                    compare = {'>': 'greater_than', '<': 'less_than'}[operator]
                elif var is None:
                    item = node.children()[0]
                    var, value = item.key, item.value
                else:
                    value = node.scalar('value')
                left, right = self.number(var, scope), self.number(value, scope)
                answers.append({'equals': left == right, 'greater_than': left > right,
                                'less_than': left < right,
                                'greater_than_or_equals': left >= right,
                                'less_than_or_equals': left <= right}[compare])
            elif key == 'fallout_survival_country_cohesion_row_is_current':
                answers.append(True)  # Explicit current-row fixture; not native proof.
            else:
                raise AssertionError('Unmodelled trigger: ' + key)
        return all(answers)

    def execute(self, nodes, scope=None):
        scope = scope or self.country
        branch_taken = False
        for node in nodes:
            key = node.key
            if key in ('if', 'else_if', 'else'):
                if key == 'if':
                    branch_taken = False
                gate = next(iter(node.children('limit')), None)
                if not branch_taken and (gate is None or self.conditions(gate.children(), scope)):
                    branch_taken = True
                    self.execute([n for n in node.children() if n.key != 'limit'], scope)
            elif key in ('set_country_flag', 'clr_country_flag'):
                (scope['flags'].add if key == 'set_country_flag' else scope['flags'].discard)(node.value)
            elif key in ('set_variable', 'add_to_variable', 'subtract_from_variable', 'set_temp_variable', 'add_to_temp_variable', 'subtract_from_temp_variable', 'multiply_temp_variable'):
                item = node.children()[0]
                target = self.temps if 'temp' in key else scope['vars']
                value = self.number(item.value, scope)
                if key.startswith('set_'):
                    target[item.key] = value
                elif key in ('add_to_variable', 'add_to_temp_variable'):
                    target[item.key] = target.get(item.key, 0) + value
                elif key in ('subtract_from_variable', 'subtract_from_temp_variable'):
                    target[item.key] = target.get(item.key, 0) - value
                else:
                    target[item.key] = target.get(item.key, 0) * value
            elif key == 'clamp_variable':
                var = node.scalar('var')
                scope['vars'][var] = min(self.number(node.scalar('max'), scope), max(self.number(node.scalar('min'), scope), scope['vars'].get(var, 0)))
            elif key == 'clear_variable':
                scope['vars'].pop(node.value, None)
            elif key == 'add_political_power':
                scope['vars']['political_power'] = scope['vars'].get('political_power', 0) + self.number(node.value, scope)
            elif key in functions:
                retained = set(self.temps)
                self.execute(functions[key].children(), scope)
                self.temps = {k: v for k, v in self.temps.items() if k in retained}
            else:
                raise AssertionError('Unmodelled effect: ' + key)

    def apply(self):
        retained = set(self.temps)
        self.execute(functions['fallout_air_winter_apply_survivor_memory'].children())
        self.temps = {k: v for k, v in self.temps.items() if k in retained}


def state(*flags, controlled=True):
    return {'flags': set(flags), 'vars': {}, 'controlled': controlled}


cases = 0
for memory, field, expected in (
    ('phase_1_success', 'fallout_survival_cohesion_current', 52),
    ('phase_1_failure', 'fallout_survival_cohesion_current', 48),
    ('tunnel_school_protection', 'fallout_survival_current_entries^8', 54),
    ('tunnel_civic_failure', 'fallout_survival_cohesion_current', 47),
    ('rail_clearance_succeeded', 'fallout_survival_current_entries^4', 53),
    ('rail_clearance_failed', 'fallout_survival_current_entries^4', 47),
    ('dam_full_head_held', 'fallout_survival_current_entries^6', 54),
    ('dam_full_head_failed', 'fallout_survival_current_entries^2', 48),
    ('refinery_military_output_held', 'fallout_survival_current_entries^5', 54),
    ('refinery_district_heat_result', 'fallout_survival_current_entries^5', 48),
    ('refinery_shutdown_result', 'fallout_survival_current_entries^4', 52),
    ('refinery_military_output_failed', 'fallout_survival_current_entries^5', 47),
    ('reactor_plant_council_succeeded', 'fallout_survival_current_entries^6', 55),
    ('reactor_scram_succeeded', 'fallout_survival_current_entries^4', 53),
    ('reactor_scram_failed', 'fallout_survival_current_entries^7', 48),
    ('furnace_full_shifts_held', 'fallout_survival_current_entries^5', 47),
    ('furnace_shutdown_complete', 'fallout_survival_current_entries^4', 52),
    ('furnace_full_shifts_failed', 'fallout_survival_current_entries^4', 46),
):
    w = World([state('air_winter_memory_' + memory)])
    w.apply()
    assert w.country['vars'][field] == expected, memory
    before = dict(w.country['vars'])
    w.apply()
    assert w.country['vars'] == before, 'Repeated orientation changed ' + memory
    assert not w.temps, 'Helper-created temporary escaped its caller'
    cases += 1

w = World([state('air_winter_memory_furnace_full_shifts_held')] * 10)
w.apply()
assert w.country['vars']['fallout_survival_current_entries^4'] == 55
cases += 1
w = World([state('air_winter_memory_reactor_plant_council_succeeded', controlled=False)])
w.apply()
assert w.country['vars']['fallout_survival_current_entries^6'] == 50
cases += 1
w = World([state('air_winter_memory_phase_1_success'), state('air_winter_memory_phase_1_failure')])
w.apply()
assert w.country['vars']['fallout_survival_cohesion_current'] == 50
cases += 1
for initial in (0, 99, 100):
    w = World([state('air_winter_memory_phase_1_success'), state('air_winter_memory_phase_1_failure')], value=initial)
    w.apply()
    assert w.country['vars']['fallout_survival_cohesion_current'] == initial
    cases += 1
w = World([state('air_winter_memory_refinery_military_output_held'), state('air_winter_memory_refinery_district_heat_result')])
w.apply()
assert w.country['vars']['fallout_survival_current_entries^5'] == 52
assert w.country['vars']['fallout_survival_current_entries^6'] == 53
cases += 1
for value, memory, field, expected in (
    (0, 'reactor_scram_failed', 'fallout_survival_current_entries^7', 0),
    (100, 'furnace_full_shifts_held', 'fallout_survival_current_entries^4', 100),
    (0, 'phase_1_failure', 'fallout_survival_cohesion_current', 0),
    (100, 'phase_1_success', 'fallout_survival_cohesion_current', 100),
):
    w = World([state('air_winter_memory_' + memory)], value=value)
    w.apply()
    assert w.country['vars'][field] == expected
    cases += 1
w = World([state('air_winter_memory_seed_vaults_flourished', 'air_winter_memory_furnace_full_shifts_held')])
w.apply()
assert w.country['vars']['fallout_survival_current_entries^1'] == 56
assert w.country['vars']['fallout_survival_current_entries^4'] == 55
cases += 1
print(f'{cases} production-source cases passed; native engine execution remains untested.')
