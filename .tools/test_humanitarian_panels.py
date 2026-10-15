"""Production-source regression for humanitarian panel presentation.

Usage: python .tools/test_humanitarian_panels.py
Inputs: committed panel source, owner predicates, date conversion and localisation.
Outputs: .tmp/national_policy_panels/panel_helpers_test_results.json.
Asserts read-only gameplay state, bounded collection, selection, exact work progress
and open-flag, list and selection behavior for close, cross-open and invalidation.
The optional foreach cap is a stress assumption, not an observed HOI4 engine limit.
The action-status presentation seam is recorded. GUI rendering and live gameplay are excluded.
"""
from pathlib import Path
import importlib.util, sys, json, copy, re, hashlib
from decimal import Decimal
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / '.tmp' / 'national_policy_panels'
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('panel_parser', ROOT / '.tools/test_event035_center_projects.py')
P = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = P
spec.loader.exec_module(P)
Scope = P.Scope
Node = P.Node

def read_named(path, name):
    s = (ROOT / path).read_text(encoding='utf-8-sig')
    m = re.search('(?m)^' + re.escape(name) + '\\s*=\\s*\\{', s)
    assert m, name
    ts = P.lex(P.uncomment(s[m.end():]))
    (rows, end) = P.parse_nodes(ts, 0, name)
    return P.Definition(name, ROOT / path, 1, rows)

class Runtime(P.Event35Runtime):
    EXTERNAL_FIXTURES = {'famine_gui_refresh_selected_action_status', 'migration_gui_refresh_selected_action_status'}

    def __init__(self, states=(), foreach_cap=None):
        saved = (P.EFFECT_FILES, P.TRIGGER_FILES)
        P.EFFECT_FILES = ('common/scripted_effects/humanitarian_panel_effects.txt',)
        P.TRIGGER_FILES = ('common/scripted_triggers/humanitarian_panel_triggers.txt',)
        try:
            super().__init__()
        finally:
            (P.EFFECT_FILES, P.TRIGGER_FILES) = saved
        self.foreach_cap = foreach_cap
        self.foreach_reads = []
        self.states = list(states)
        self.effect_defs['chaosx_convert_date_offset_to_days'] = read_named('common/scripted_effects/chaosx_dynamic_effects.txt', 'chaosx_convert_date_offset_to_days')
        self.globals['date'] = 0
        for (path, name) in [('common/scripted_triggers/migration_report_triggers.txt', 'migration_state_has_header_trapped_people'), ('common/scripted_triggers/migration_report_triggers.txt', 'migration_state_has_header_sheltered_or_fleeing_people'), ('common/scripted_triggers/migration_core_triggers.txt', 'migration_reception_capacity_is_valid'), ('common/scripted_triggers/humanitarian_validation_triggers.txt', 'humanitarian_country_is_valid')]:
            self.trigger_defs[name] = read_named(path, name)

    def _read_constants(self):
        result = {}
        for file in ('humanitarian_panel_constants.txt', 'famine_core_constants.txt', 'migration_core_constants.txt', 'humanitarian_runtime_constants.txt', 'civilian_transfer_constants.txt', 'chaosx_date_units_constants.txt', 'humanitarian_gui_action_constants.txt'):
            for (group, d) in P.read_definitions('common/script_constants/' + file).items():
                for n in d.body:
                    if isinstance(n.value, str) and P.NUMBER.fullmatch(n.value):
                        result['constant:' + group + '.' + n.key] = float(n.value)
        return result

    def _value(self, t):
        if t == 'id':
            return getattr(self.current, 'id', 0)
        v = super()._value(t)
        if isinstance(v, str) and t.startswith(('famine_', 'migration_', 'humanitarian_')):
            return self._variable(t)
        return Decimal(str(v)) if isinstance(v, (int, float)) and (not isinstance(v, bool)) else v

    def _variable(self, t):
        if t == 'id':
            return getattr(self.current, 'id', 0)
        v = super()._variable(t)
        return Decimal(str(v)) if isinstance(v, (int, float)) and (not isinstance(v, bool)) else v

    def _write_path(self, path, value, clear=False):
        (c, rest, glob) = self._path_container(path)
        assert not glob and c.kind == 'country' and rest.startswith(('famine_panel_', 'migration_panel_', 'national_policy_panel_')), ('Gameplay write', path)
        super()._write_path(path, value, clear)

    def _condition(self, n, scope):
        if n.key == 'scope_exists':
            return isinstance(scope, Scope)
        if n.key == 'migration_pending_reception_issue_is_valid':
            return scope.values.get('fixture_pending_offer', False)
        if n.key == 'check_variable' and len(n.value) == 1:
            a = n.value[0]
            return self._compare(self._variable(a.key), a.op, self._value(a.value))
        if n.key.startswith('var:') and (not isinstance(self._value(n.key), Scope)):
            return False
        return super()._condition(n, scope)

    def _effects(self, nodes, scope):
        chunk = []
        for n in nodes:
            if n.key in ('every_owned_state', 'every_controlled_state', 'for_each_loop', 'for_each_scope_loop', 'clamp_variable', 'divide_temp_variable'):
                if chunk:
                    super()._effects(chunk, scope)
                    chunk = []
                if n.key in ('for_each_loop', 'for_each_scope_loop'):
                    array = P.first(n.value, 'array')
                    values = list(self._array_values(array))
                    if self.foreach_cap is not None:
                        values = values[:self.foreach_cap]
                    self.foreach_reads.append((array, len(values)))
                    for (index, value) in enumerate(values):
                        if n.key == 'for_each_scope_loop':
                            self.scope_stack.append(value)
                            try:
                                self._effects([x for x in n.value if x.key not in ('array', 'break')], value)
                            finally:
                                self.scope_stack.pop()
                        else:
                            self._set_temp(P.first(n.value, 'value', 'v'), value)
                            self._set_temp(P.first(n.value, 'index', 'i'), index)
                            self._effects([x for x in n.value if x.key not in ('array', 'value', 'index', 'break')], scope)
                    continue
                if n.key == 'clamp_variable':
                    name = P.first(n.value, 'var')
                    self._write_path(name, max(self._value(P.first(n.value, 'min', str(-10000000000.0))), min(self._variable(name), self._value(P.first(n.value, 'max', str(10000000000.0))))))
                    continue
                if n.key == 'divide_temp_variable':
                    node = n.value[0]
                    self._set_temp(node.key, self._variable(node.key) / self._value(node.value))
                    continue
                candidates = [s for s in self.states if (s.owner if n.key == 'every_owned_state' else s.controller) is scope]
                for s in candidates:
                    self.scope_stack.append(s)
                    try:
                        if self._conditions(P.first(n.value, 'limit', []), s):
                            self._effects([x for x in n.value if x.key != 'limit'], s)
                    finally:
                        self.scope_stack.pop()
            elif n.key == 'divide_variable' and len(n.value) == 1:
                a = n.value[0]
                chunk.append(Node(n.key, n.op, [Node('var', '=', a.key, n.line), Node('value', '=', a.value, n.line)], n.line))
            else:
                chunk.append(n)
        if chunk:
            super()._effects(chunk, scope)

    def _native_effect(self, key, value, scope, line):
        if key == 'clamp_temp_variable':
            name = P.first(value, 'var')
            self._set_temp(name, max(self._value(P.first(value, 'min', str(-10000000000.0))), min(self._variable(name), self._value(P.first(value, 'max', str(10000000000.0))))))
            return
        return super()._native_effect(key, value, scope, line)

def country(tag='FRA'):
    return Scope('country', tag, resources={'political_power': 300, 'fuel': 1000, 'manpower': 2000})

def state(i, owner, controller=None, flags=(), **values):
    return Scope('state', i, values=values, flags=set(flags), owner=owner, controller=controller or owner, population_k=100)

def gameplay(r, c):

    def values(s):
        return {k: (v.kind, v.id) if isinstance(v, Scope) else v for (k, v) in s.values.items() if '_panel_' not in k}
    return (values(c), {f for f in c.flags if '_panel_' not in f}, dict(c.resources), [(s.id, values(s), s.flags.copy(), dict(s.resources), s.population_k, s.owner.id, s.controller.id) for s in r.states], {k: [(v.kind, v.id) if isinstance(v, Scope) else v for v in vals] for (k, vals) in r.global_arrays.items()})

def run_unchanged(r, c, name):
    before = gameplay(r, c)
    r.run_effect(name, c)
    assert before == gameplay(r, c), name
    assert not r.native_calls
checks = []
c = country()
r = Runtime()
run_unchanged(r, c, 'famine_panel_open_window')
assert 'famine_panel_open' in c.flags and (not c.arrays['famine_panel_states']) and ('famine_panel_selected_state' not in c.values) and ('famine_panel_food_assessed' not in c.flags) and ('famine_panel_reserves_assessed' not in c.flags)
c.values.update({'migration_panel_view': 2, 'migration_panel_group': 3})
run_unchanged(r, c, 'migration_panel_open_window')
assert 'migration_panel_open' in c.flags and 'famine_panel_open' not in c.flags and (c.values['migration_panel_view'] == 2) and (c.values['migration_panel_group'] == 3) and ('migration_panel_capacity_assessed' not in c.flags)
before = copy.copy(c.values)
run_unchanged(r, c, 'migration_panel_close_window')
assert c.values == before and 'migration_panel_open' not in c.flags
checks.append('Quiet open/refresh/close changes only UI, preserves unassessed states and mutually exclusive windows, retains supplied view/group')

# Native per-tick windows follow open flags and actual list/selection invalidation.
def panel_presentation(actor):
    return (dict(actor.values), set(actor.flags), {key: list(values) for key, values in actor.arrays.items()})

for system, other in [('famine', 'migration'), ('migration', 'famine')]:
    actor = country('CAN')
    runtime = Runtime()
    run_unchanged(runtime, actor, system + '_panel_open_window')
    before_values, before_flags, before_arrays = panel_presentation(actor)
    run_unchanged(runtime, actor, system + '_panel_close_window')
    expected_values = dict(before_values)
    assert panel_presentation(actor) == (expected_values, before_flags - {system + '_panel_open'}, before_arrays)
    run_unchanged(runtime, actor, other + '_panel_open_window')
    before_values, before_flags, before_arrays = panel_presentation(actor)
    run_unchanged(runtime, actor, system + '_panel_open_window')
    expected_values = dict(before_values)
    expected_flags = (before_flags - {other + '_panel_open'}) | {system + '_panel_open'}
    assert panel_presentation(actor) == (expected_values, expected_flags, before_arrays)

for entry in ['famine_panel_open_window', 'migration_panel_open_window', 'famine_panel_close_window', 'migration_panel_close_window', 'famine_panel_refresh', 'migration_panel_refresh']:
    actor = country('AST')
    actor.ai = True
    selected = state(500, actor)
    runtime = Runtime([selected])
    actor.flags.update({'famine_panel_open', 'migration_panel_open', 'famine_panel_food_assessed'})
    actor.values.update({'famine_panel_selected_state': selected, 'migration_panel_selected_state': selected, 'famine_panel_state_count': 1, 'migration_panel_state_count': 1, 'famine_panel_view': 2, 'migration_panel_group': 3})
    actor.arrays.update({key: [selected] for key in ['famine_panel_states', 'migration_panel_states', 'famine_panel_candidates', 'migration_panel_candidates']})
    before_values, before_flags, before_arrays = panel_presentation(actor)
    run_unchanged(runtime, actor, entry)
    expected_values = {key: value for key, value in before_values.items() if key not in {'famine_panel_selected_state', 'migration_panel_selected_state'}}
    expected_values.update({'famine_panel_state_count': 0, 'migration_panel_state_count': 0})
    expected_arrays = {key: [] for key in before_arrays}
    expected_flags = before_flags - {'famine_panel_open', 'migration_panel_open'}
    assert panel_presentation(actor) == (expected_values, expected_flags, expected_arrays), entry
checks.append('Own-close and cross-open flags update immediately, and all six invalid entry paths clear lists and selections without extra presentation or gameplay mutation')

a = country()
b = country('GER')
s1 = state(1, a, flags=['famine_food_security_active', 'famine_food_reserve_initialized'], famine_food_stage=1, famine_food_reserve_amount=200, famine_food_reserve_daily_need=10, famine_component_production=40)
s2 = state(2, a, flags=['famine_food_security_active', 'famine_food_reserve_initialized', 'famine_relief_access_active'], famine_food_stage=4, famine_food_reserve_amount=100, famine_food_reserve_daily_need=10, famine_component_transport=70)
s3 = state(3, b)
s4 = state(4, a, flags=['famine_mission_route_subject'])
spoof = state(9, a)
r = Runtime([s1, s2, s3, s4, spoof])
r.global_arrays['famine_active_states'] = [s1, s3, s2, s1]
a.arrays['famine_action_states'] = [s2]
a.values['famine_panel_selected_state'] = spoof
r.temp_frames[0]['break'] = 1
r.temp_frames[0]['humanitarian_panel_list_break'] = 1
run_unchanged(r, a, 'famine_panel_open_window')
assert [s.id for s in a.arrays['famine_panel_states']] == [2, 1, 4]
assert a.values['famine_panel_selected_state'] is s2
assert a.values['famine_panel_food_stage'] == 4 and a.values['famine_panel_priority_cause'] == 2 and (a.values['famine_panel_reserve_days'] == 15) and (a.values['famine_panel_selected_reserve_days'] == 10) and (a.values['famine_panel_food_stage_frame'] == 6)
checks.append('Bounded actor-state filtering, deduplication, worst-food ordering, pending/mission retention, spoof rejection, aggregate/selected copies and inherited break reset')
band_actor = country('ENG')
bands = [state(100 + stage, band_actor, flags=['famine_food_security_active'], famine_food_stage=stage) for stage in (1, 4, 0, 3, 2)]
band_runtime = Runtime(bands)
band_runtime.global_arrays['famine_active_states'] = bands
run_unchanged(band_runtime, band_actor, 'famine_panel_open_window')
assert [s.id for s in band_actor.arrays['famine_panel_states']] == [104, 103, 102, 101, 100]
band_actor.arrays.update({'famine_action_ids': [11], 'famine_action_types': [7], 'famine_action_states': [bands[1]], 'famine_action_starts': [0], 'famine_action_dates': [0.0048]})
band_runtime.globals['date'] = 0.0024
run_unchanged(band_runtime, band_actor, 'famine_panel_refresh')
assert band_actor.values['famine_panel_work_uid'] == 11 and band_actor.values['famine_panel_work_frame'] == 6 and (band_actor.values['famine_panel_work_remaining_days'] == 10)
s2.owner = s2.controller = b
run_unchanged(r, a, 'famine_panel_refresh')
assert a.values['famine_panel_selected_state'] is s1 and s2 not in a.arrays['famine_panel_states']
r.global_arrays['famine_active_states'] = []
a.arrays['famine_action_states'] = []
s4.flags.clear()
s1.flags.clear()
s1.values.clear()
run_unchanged(r, a, 'famine_panel_refresh')
assert 'famine_panel_selected_state' not in a.values
checks.append('Captured or retired targets cannot retain selection and empty lists clear the pointer')
a = country()
b = country('GER')
flee = state(11, a, migration_state_flight_population=600)
trapped = state(12, a, migration_state_trapped_population=200, migration_state_flight_population=50)
prep = state(13, b, controller=a, flags=['migration_evacuation_prepared'])
foreign = state(14, b, migration_state_trapped_population=999)
r = Runtime([flee, trapped, prep, foreign])
r.global_arrays['migration_active_states'] = [flee, foreign, trapped]
run_unchanged(r, a, 'migration_panel_open_window')
assert [s.id for s in a.arrays['migration_panel_states']] == [12, 11, 13] and a.values['migration_panel_trapped'] == 200 and (a.values['migration_panel_fleeing'] == 650)
assert a.values['migration_panel_selected_trapped'] == 200 and a.values['migration_panel_displacement_frame'] == 3 and ('migration_panel_capacity_assessed' not in a.flags)
a.values.update({'migration_reception_capacity_schema_version': r.constants['constant:migration_capacity.schema_version'], 'migration_reception_capacity_valid': 1, 'migration_reception_capacity_dirty': 0, 'migration_reception_capacity_revision': 1, 'migration_reception_capacity': 500, 'migration_reception_load': 500, 'migration_reception_candidate_count': 1, 'migration_reception_safe_candidate_count': 1, 'migration_reception_invalid_candidate_count': 0})
run_unchanged(r, a, 'migration_panel_refresh')
assert 'migration_panel_capacity_assessed' in a.flags and a.values['migration_panel_capacity_frame'] == 3
a.values['migration_reception_capacity_dirty'] = 1
run_unchanged(r, a, 'migration_panel_refresh')
assert 'migration_panel_capacity_assessed' not in a.flags and a.values['migration_panel_capacity_frame'] == 1
checks.append('Trapped-first migration states, controlled prepared state retention, separate un-summed counters and valid-versus-stale capacity proof')
a.arrays.update({'migration_action_ids': [1, 2, 3], 'migration_action_types': [1, 11, 2], 'migration_action_states': [trapped, trapped, flee], 'migration_action_starts': [0, 0.0024, 0], 'migration_action_dates': [0.0096, 0.0072, 0.0036]})
r.globals['date'] = 0.0048
run_unchanged(r, a, 'migration_panel_refresh')
assert a.values['migration_panel_work_uid'] == 2 and a.values['migration_panel_work_frame'] == 6 and (a.values['migration_panel_work_remaining_days'] == 10)
r.globals['date'] = 0.0084
run_unchanged(r, a, 'migration_panel_refresh')
assert a.values['migration_panel_work_frame'] == 11 and a.values['migration_panel_work_remaining_days'] == 0
a.arrays['migration_action_starts'].pop()
run_unchanged(r, a, 'migration_panel_refresh')
assert 'migration_panel_has_active_work' not in a.flags and a.values['migration_panel_work_frame'] == 1
checks.append('Exact selected-state earliest-due progress from saved start/date metadata, midpoint6/end11, due work remains observational, missing alignment does not invent a clock')
a.ai = True
a.flags.update({'famine_panel_open', 'migration_panel_open'})
a.values['famine_panel_selected_state'] = flee
run_unchanged(r, a, 'migration_panel_refresh')
assert not a.flags & {'famine_panel_open', 'migration_panel_open'} and 'famine_panel_selected_state' not in a.values and ('migration_panel_selected_state' not in a.values)
checks.append('Effect-time eligibility loss closes both panels and removes selected pointers')
late_actor = country('POL')
other_actor = country('GER')
prefix = [state(i, other_actor, flags=['famine_food_security_active', 'migration_displacement_active'], famine_food_stage=1, migration_state_flight_population=1) for i in range(1, 1200)]
late_owned = state(1200, late_actor, flags=['famine_food_security_active'], famine_food_stage=4, migration_state_trapped_population=500)
late_controlled = state(1201, other_actor, controller=late_actor, flags=['famine_food_security_active'], famine_food_stage=2, migration_state_flight_population=100)
unknown_owned = state(1202, late_actor, famine_food_stage=0, migration_state_flight_population=0, migration_state_trapped_population=0, migration_state_reception_load=0)
registry = prefix + [late_owned, late_controlled]
stress = Runtime(registry + [unknown_owned], foreach_cap=1000)
stress.global_arrays.update({'famine_active_states': list(registry), 'migration_active_states': list(registry)})
run_unchanged(stress, late_actor, 'famine_panel_open_window')
assert [s.id for s in late_actor.arrays['famine_panel_states']] == [1200, 1201]
run_unchanged(stress, late_actor, 'migration_panel_open_window')
assert [s.id for s in late_actor.arrays['migration_panel_states']] == [1200, 1201]
assert not any((name.startswith('global.') for (name, count) in stress.foreach_reads))
assert unknown_owned not in late_actor.arrays['famine_panel_states'] and unknown_owned not in late_actor.arrays['migration_panel_states']
assert 'famine_food_security_active' not in unknown_owned.flags and 'famine_food_reserve_initialized' not in unknown_owned.flags and ('migration_displacement_active' not in unknown_owned.flags)
checks.append('1201-row registry suffix survives a hypothetical foreach1000 cap through native owned/controlled collection, preserves priority and excludes zero-filled unassessed ownership without initialization')
# Read-only obligations and pending actor rows remain visible without a global scan.
obligation_actor = country('USA')
workforce_state = state(1301, obligation_actor, migration_industrial_workforce_delta=-500)
corridor_state = state(1302, obligation_actor, flags=['humanitarian_corridor_contract_active'])
pending_state = state(1303, obligation_actor)
obligation_runtime = Runtime([workforce_state, corridor_state, pending_state])
obligation_actor.arrays['migration_action_states'] = [pending_state]
run_unchanged(obligation_runtime, obligation_actor, 'migration_panel_open_window')
assert {s.id for s in obligation_actor.arrays['migration_panel_states']} == {1301, 1302, 1303}
checks.append('Published signed workforce, corridor work and exact pending actor membership remain visible without state registration')
raw = (ROOT / 'common/scripted_localisation/humanitarian_panel_localisation.txt').read_text()
tokens = P.lex(P.uncomment(raw))
(defs, end) = P.parse_nodes(tokens, 0, 'panel loc')
getters = {P.first(n.value, 'name'): n.value for n in defs}
assert len(getters) == len(defs)
required = ['GetMigrationPanel' + n for n in ('Displacement', 'Capacity', 'ReceptionLaw', 'DepartureLaw', 'Situation', 'StateTitle', 'StateSummary', 'StateDetails')] + ['GetFaminePanel' + n for n in ('FoodStage', 'ReserveSummary', 'ReliefAccess', 'Situation', 'StateTitle', 'StateSummary', 'StateDetails')]
assert all((n in getters for n in required + ['GetFaminePanelActiveWork', 'GetMigrationPanelActiveWork']))
keys = set()
for file in [p.name for p in (ROOT / 'localisation/english').glob('*.yml')]:
    keys |= set(re.findall('(?m)^([^# \\n:]+):', (ROOT / 'localisation/english' / file).read_text(encoding='utf-8-sig')))
for d in getters.values():
    for n in d:
        if n.key == 'text':
            assert P.first(n.value, 'localization_key') in keys
checks.append('All 17 requested getters including active work, auxiliary selectors and referenced localisation keys resolve')
result = {'source_sha256': {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in (ROOT / 'common/scripted_effects/humanitarian_panel_effects.txt', ROOT / 'common/scripted_triggers/humanitarian_panel_triggers.txt', ROOT / 'common/scripted_localisation/humanitarian_panel_localisation.txt', ROOT / 'common/script_constants/humanitarian_panel_constants.txt')}, 'checks': checks, 'limitations': ["Action-status refresh calls recorded as the owner's presentation-only seam", 'No GUI rendering or native variable-to-state localisation execution', 'No game run or simulation assessment']}
(ROOT / '.tmp/national_policy_panels/panel_helpers_test_results.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
