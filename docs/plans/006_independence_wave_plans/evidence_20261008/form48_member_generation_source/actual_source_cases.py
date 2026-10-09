"""Bounded R4 receipts using the existing R1 parser/evaluator, not a native VM.
Run from mod root. Writes only adjacent case_receipt.json.
Native scope/variable/array/relation/idea/decision primitives are supplied.
"""
from pathlib import Path
from copy import deepcopy
import ast
import hashlib
import json
import difflib

ROOT = Path.cwd()
OUT = Path(__file__).parent
PRIOR = ROOT / 'docs/plans/006_independence_wave_plans/evidence_20261008/d34_dynamic_target_source/actual_source_cases.py'
# Reuse only parser functions and VM class. Do not execute R1 cases or outputs.
tree = ast.parse(PRIOR.read_text(encoding='utf-8-sig'))
nodes = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom)) or isinstance(n, ast.FunctionDef) and n.name in ['parse', 'extract', 'vals'] or isinstance(n, ast.ClassDef) and n.name == 'VM']
env = {'ROOT': ROOT, 'TR': {}, 'FX': {}, 'CONSTANTS': {}}
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(PRIOR), 'exec'), env)
extract, vals = env['extract'], env['vals']
source_bytes = {}

def read(path):
    raw = (ROOT / path).read_bytes()
    assert path not in source_bytes or source_bytes[path] == raw, 'source changed during read'
    source_bytes[path] = raw
    return raw.decode('utf-8-sig')

EP = 'common/scripted_effects/006_independence_wave_form48_effects.txt'
TP = 'common/scripted_triggers/006_independence_wave_form48_triggers.txt'
AP = 'common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt'
CP = 'common/script_constants/006_independence_wave_constants_registry.txt'
fx_names = ['independence_wave_form48_install_autonomous_member', 'independence_wave_form48_remove_event6_autonomous_relations', 'independence_wave_form48_clear_autonomous_member_state', 'independence_wave_form48_clear_member_cycle_responses', 'independence_wave_form48_remove_compact_ideas', 'independence_wave_form48_cleanup_frozen_autonomous_members', 'independence_wave_form48_rollback_identity']
env['FX'].update({n: extract(read(EP), n) for n in fx_names})
env['TR']['has_independence_wave_form48_current_autonomous_binding'] = extract(read(TP), 'has_independence_wave_form48_current_autonomous_binding')
env['TR']['independence_wave_formable_member_arrays_are_aligned'] = extract(read(AP), 'independence_wave_formable_member_arrays_are_aligned')
for category in ['independence_wave_formable_family', 'independence_wave_formable_tuning', 'independence_wave_formable_consent']:
    for k, op, v in extract(read(CP), category):
        if isinstance(v, str):
            try:
                env['CONSTANTS']['constant:' + category + '.' + k] = int(v)
            except ValueError:
                pass

G = 'independence_wave_generation_id'
MG = 'independence_wave_form48_autonomous_member_generation'
CG = 'independence_wave_form48_autonomous_carrier_generation'
PTR = 'independence_wave_form48_autonomous_carrier'
MF = 'independence_wave_form48_autonomous_family'
CF = 'independence_wave_formable_family'
MEMBER = 'independence_wave_form48_autonomous_member'
BOUND = 'independence_wave_form48_all_autonomous_members_bound'
DEPARTED = 'independence_wave_form48_member_departed'
ACTIVE = 'independence_wave_formable_active'
COUNTRIES = 'independence_wave_formable_member_country_entries'
GENERATIONS = 'independence_wave_formable_member_generation_entries'
ANCHORS = 'independence_wave_formable_member_anchor_entries'
CONSENTS = 'independence_wave_formable_member_consent_entries'
FAMILY = env['CONSTANTS']['constant:independence_wave_formable_family.pacific_regional_federation']
INSTALL, REMOVE, CLEAR, WALK, ROLLBACK = [
    'independence_wave_form48_' + suffix for suffix in
    ['install_autonomous_member', 'remove_event6_autonomous_relations', 'clear_autonomous_member_state', 'cleanup_frozen_autonomous_members', 'rollback_identity']]
BIND = 'has_independence_wave_form48_current_autonomous_binding'
DIRECTIONS = [
    ('independence_wave_form48_member_granted_access_to_carrier', [902, 901, 'military_access']),
    ('independence_wave_form48_member_guaranteed_carrier', [902, 901, 'guarantee']),
    ('independence_wave_form48_carrier_granted_access_to_member', [901, 902, 'military_access']),
    ('independence_wave_form48_carrier_guaranteed_member', [901, 902, 'guarantee'])]
RESPONSES = [v for k, op, v in env['FX']['independence_wave_form48_clear_member_cycle_responses'] if k == 'clr_country_flag']
DECISIONS = [v for k, op, v in env['FX']['independence_wave_form48_clear_member_cycle_responses'] if k == 'remove_decision']
IDEAS = [v for k, op, v in env['FX']['independence_wave_form48_remove_compact_ideas'] if k == 'remove_ideas']

class R4VM(env['VM']):
    def __init__(self, world, current=902, root=903):
        super().__init__(world, current, root)
        self.trace = []

    def location(self, token):
        identity, offset = self.stack[-1], 1
        if token.startswith('ROOT.'):
            identity, token = self.root, token[5:]
        else:
            while token.startswith('PREV.'):
                offset += 1
                identity, token = self.stack[-offset], token[5:]
        return identity, token

    def array(self, token):
        identity, name = self.location(token)
        return self.world['countries'].get(identity, {}).get('arrays', {}).get(name, [])

    def value(self, token):
        if token == 'PREV.PREV':
            return self.stack[-3]
        if token in env['CONSTANTS'] or token in ['THIS', 'ROOT', 'PREV'] or token.startswith('event_target:'):
            return super().value(token)
        if '^' in token:
            name, idx = token.split('^', 1)
            array = self.array(name)
            if idx == 'num':
                return len(array)
            index = int(self.value(idx))  # index is deliberately unscoped
            return array[index] if 0 <= index < len(array) else 0
        if token.startswith(('ROOT.', 'PREV.')):
            identity, name = self.location(token)
            return self.world['countries'].get(identity, {}).get('vars', {}).get(name, 0)
        return super().value(token)

    def test(self, body):
        for node in body:
            key, op, value = node
            if key in ['gives_military_access_to', 'has_guaranteed']:
                kind = 'military_access' if key == 'gives_military_access_to' else 'guarantee'
                result = [self.stack[-1], self.value(value), kind] in self.world['relations']
            elif key == 'has_cosmetic_tag':
                result = self.obj().get('cosmetic') == value
            else:
                result = super().test([node])
            if not result:
                return False
        return True

    def effects(self, body):
        for node in body:
            key, op, value = node
            identity = self.stack[-1]
            if key in ['set_country_flag', 'clr_country_flag']:
                flags = self.obj()['flags']
                if key == 'set_country_flag' and value not in flags:
                    flags.append(value)
                if key == 'clr_country_flag' and value in flags:
                    flags.remove(value)
                self.trace.append([key, identity, value])
            elif key == 'clear_variable':
                self.obj()['vars'].pop(value, None)
                self.trace.append([key, identity, value])
            elif key in ['remove_ideas', 'remove_decision']:
                store = self.obj()['ideas' if key == 'remove_ideas' else 'decisions']
                if value in store:
                    store.remove(value)
                self.trace.append([key, identity, value])
            elif key in ['give_military_access', 'give_guarantee', 'diplomatic_relation']:
                if key == 'diplomatic_relation':
                    fields = {k: v for k, op, v in value}
                    relation = [identity, self.value(fields['country']), fields['relation']]
                    add = fields['active'] == 'yes'
                else:
                    relation = [identity, self.value(value), 'military_access' if key == 'give_military_access' else 'guarantee']
                    add = True
                if add and relation not in self.world['relations']:
                    self.world['relations'].append(relation)
                if not add and relation in self.world['relations']:
                    self.world['relations'].remove(relation)
                self.trace.append([key, relation, add])
            elif key == 'ROOT' or key.startswith('event_target:'):
                self.scope(self.value(key), value, effect=True)
            elif key == 'drop_cosmetic_tag':
                self.obj()['cosmetic'] = None
                self.trace.append([key, identity])
            elif key == 'clr_global_flag':
                if value in self.world['global_flags']:
                    self.world['global_flags'].remove(value)
                self.trace.append([key, value])
            else:
                before = len(self.writes)
                super().effects([node])
                if key == 'set_variable':
                    self.trace.extend([['set_variable', *write] for write in self.writes[before:]])

def fixture(installed=True):
    def obj(generation):
        return {'exists': True, 'original': 'fixture', 'dynamic': True, 'vars': {G: generation}, 'flags': [], 'ideas': [], 'decisions': [], 'arrays': {}, 'cosmetic': None}
    carrier, member, other = obj(100), obj(101), obj(999)
    carrier['vars'][CF] = FAMILY
    carrier['flags'] = [ACTIVE, BOUND, 'independence_wave_form48_federal_carrier', 'independence_wave_form48_postformation_initialized']
    carrier['cosmetic'] = 'PFX'
    carrier['arrays'] = {COUNTRIES: [901, 902], GENERATIONS: [100, 101], ANCHORS: [378, 629], CONSENTS: [1, 1]}
    member['flags'] = list(RESPONSES) + ['independence_wave_form48_autonomous_invitation_authorized']
    member['ideas'], member['decisions'] = list(IDEAS) + ['unrelated_idea'], list(DECISIONS) + ['unrelated_decision']
    world = {'countries': {901: carrier, 902: member, 903: other}, 'states': {}, 'vars': {}, 'arrays': {}, 'global_flags': ['independence_wave_form48_pfx_identity_in_use'], 'relations': [[902, 903, 'guarantee']]}
    if installed:
        member['flags'] += [MEMBER] + [flag for flag, relation in DIRECTIONS]
        member['vars'].update({MG: 101, CG: 100, PTR: 901, MF: FAMILY})
        world['relations'] += [deepcopy(relation) for flag, relation in DIRECTIONS]
    return world

cases = []
def run(name, helper=REMOVE, modify=None, check=None, current=902, root=903):
    world = fixture()
    if modify:
        modify(world)
    before = deepcopy(world)
    vm = R4VM(world, current, root)
    vm.call(helper, effect=True)
    assert not vm.temp, 'private helper temporary escaped'
    if check:
        check(world, before, vm)
    cases.append({'case': name, 'helper': helper, 'current': current, 'root': root, 'input': before, 'output': deepcopy(world), 'trace': deepcopy(vm.trace), 'result': 'assertions passed'})
    return world, vm

def cleaned(world, before, vm):
    assert all(relation not in world['relations'] for flag, relation in DIRECTIONS)
    assert [902, 903, 'guarantee'] in world['relations'], 'unrelated relation removed'
    assert DEPARTED in world['countries'][901]['flags'] and BOUND not in world['countries'][901]['flags']
    assert all(k not in world['countries'][902]['vars'] for k in [MG, CG, PTR])
    assert len([t for t in vm.trace if t[0] == 'diplomatic_relation']) == 4

run('valid_member101_carrier100_owned_four_directions_departed', check=cleaned)
def no_relation_remove(world, before, vm):
    assert world['relations'] == before['relations']
    assert not any(t[0] == 'diplomatic_relation' for t in vm.trace)
    assert world['countries'][901] == before['countries'][901]
    # Existing direct cleanup still retires stale binding receipts.
    assert all(k not in world['countries'][902]['vars'] for k in [MG, CG, PTR])
for name, mutate in [
    ('stale_member_generation', lambda w: w['countries'][902]['vars'].__setitem__(G, 102)),
    ('stale_carrier_generation', lambda w: w['countries'][901]['vars'].__setitem__(G, 99)),
    ('missing_own_receipt', lambda w: w['countries'][902]['vars'].pop(MG)),
    ('equal_number_stale_own_receipt', lambda w: w['countries'][902]['vars'].__setitem__(G, 100)),
    ('missing_carrier_object', lambda w: w['countries'][901].__setitem__('exists', False))]:
    run(name + '_no_native_relation_remove', modify=mutate, check=no_relation_remove)

def intact(world, before, vm):
    assert world == before, 'walker touched rejected incarnation'
    assert not vm.trace, 'walker invoked destructive primitive'
for name, mutate in [
    ('stale_frozen_member_row_new_incarnation', lambda w: w['countries'][902]['vars'].update({G: 102, MG: 102})),
    ('current_row_but_stale_binding', lambda w: (w['countries'][902]['vars'].__setitem__(G, 102), w['countries'][901]['arrays'][GENERATIONS].__setitem__(1, 102))),
    ('walker_missing_own_receipt', lambda w: w['countries'][902]['vars'].pop(MG)),
    ('walker_stale_carrier_generation', lambda w: w['countries'][901]['vars'].__setitem__(G, 99)),
    ('copied_foreign_carrier_ledger', lambda w: (w['countries'][903].update(deepcopy(w['countries'][901])), w['countries'][903]['vars'].__setitem__(G, 100))),
    ('unaligned_member_arrays', lambda w: w['countries'][901]['arrays'][GENERATIONS].pop())]:
    run(name, helper=WALK, modify=mutate, current=903 if name == 'copied_foreign_carrier_ledger' else 901, root=903, check=intact)

def fully_cleaned(world, before, vm):
    cleaned(world, before, vm)
    member = world['countries'][902]
    assert not any(flag in member['flags'] for flag in RESPONSES + [MEMBER])
    assert member['ideas'] == ['unrelated_idea'] and member['decisions'] == ['unrelated_decision']
    assert MF not in member['vars']
run('valid_walker_ROOT_is_third_country', helper=WALK, current=901, root=903, check=fully_cleaned)
world, vm = run('valid_walker_before_duplicate', helper=WALK, current=901, root=903, check=fully_cleaned)
before, start = deepcopy(world), len(vm.trace)
vm.call(WALK, effect=True)
assert world == before and len(vm.trace) == start
cases.append({'case': 'duplicate_walker_cleanup_idempotent', 'helper': WALK, 'input': before, 'output': deepcopy(world), 'trace': vm.trace[start:], 'result': 'assertions passed'})
world, vm = run('valid_direct_before_duplicate', check=cleaned)
before, start = deepcopy(world), len(vm.trace)
vm.call(REMOVE, effect=True)
assert world == before and not any(t[0] == 'diplomatic_relation' for t in vm.trace[start:])
cases.append({'case': 'duplicate_direct_cleanup_idempotent_world', 'helper': REMOVE, 'input': before, 'output': deepcopy(world), 'trace': vm.trace[start:], 'result': 'assertions passed'})

world = fixture(False)
before = deepcopy(world)
vm = R4VM(world, 902, 901)
vm.call(INSTALL, effect=True)
assert world['countries'][902]['vars'][MG] == 101 and world['countries'][902]['vars'][CG] == 100
stamp = next(i for i, t in enumerate(vm.trace) if t[:3] == ['set_variable', 902, MG])
grants = [i for i, t in enumerate(vm.trace) if t[0] in ['give_military_access', 'give_guarantee']]
assert len(grants) == 4 and stamp < min(grants)
cases.append({'case': 'installer_captures_member_before_all_grants', 'helper': INSTALL, 'input': before, 'output': deepcopy(world), 'trace': deepcopy(vm.trace), 'result': 'assertions passed'})

def remove_owned_flags(world):
    flags = world['countries'][902]['flags']
    flags[:] = [f for f in flags if f not in [flag for flag, relation in DIRECTIONS]]
def unowned_preserved(world, before, vm):
    assert world['relations'] == before['relations']
    assert not any(t[0] == 'diplomatic_relation' for t in vm.trace)
run('preexisting_four_unowned_relations_preserved', modify=remove_owned_flags, check=unowned_preserved)
for selected_flag, selected_relation in DIRECTIONS:
    def modify(world, flag=selected_flag):
        remove_owned_flags(world)
        world['countries'][902]['flags'].append(flag)
    def check(world, before, vm, relation=selected_relation):
        assert relation not in world['relations']
        assert world['relations'] == [r for r in before['relations'] if r != relation]
        assert len([t for t in vm.trace if t[0] == 'diplomatic_relation']) == 1
    run('only_owned_direction_' + selected_flag, modify=modify, check=check)

world = fixture(False)
world['relations'] += [deepcopy(r) for f, r in DIRECTIONS]
vm = R4VM(world, 902, 901)
before = deepcopy(world)
vm.call(INSTALL, effect=True)
assert not any(f in world['countries'][902]['flags'] for f, r in DIRECTIONS)
assert not any(t[0] in ['give_military_access', 'give_guarantee'] for t in vm.trace)
vm.call(REMOVE, effect=True)
assert world['relations'] == before['relations']
cases.append({'case': 'install_then_cleanup_preexisting_relations_unowned', 'input': before, 'output': deepcopy(world), 'trace': deepcopy(vm.trace), 'result': 'assertions passed'})

def preformation(world):
    world['countries'][901]['flags'].remove('independence_wave_form48_postformation_initialized')
def rolled_back(world, before, vm):
    # Rollback clears the carrier's departed flag after member cleanup.
    assert all(r not in world['relations'] for f, r in DIRECTIONS)
    member, carrier = world['countries'][902], world['countries'][901]
    assert not any(f in member['flags'] for f in RESPONSES + [MEMBER])
    assert member['ideas'] == ['unrelated_idea'] and member['decisions'] == ['unrelated_decision']
    assert all(k not in member['vars'] for k in [MG, CG, PTR, MF])
    assert carrier['cosmetic'] is None and DEPARTED not in carrier['flags']
    assert any(t[:3] == ['set_country_flag', 901, DEPARTED] for t in vm.trace)
    assert [902, 903, 'guarantee'] in world['relations']
run('rollback_before_postformation_initialization', helper=ROLLBACK, modify=preformation, current=901, root=903, check=rolled_back)

# Preserve exact narrow source differences against the parent's frozen R4 source.
baseline = ROOT / 'docs/plans/006_independence_wave_plans/evidence_20261008/form48_generation_cleanup_probability/source_snapshots'
diffs, baseline_hashes = {}, {}
for path in [EP, TP]:
    raw = (baseline / path).read_bytes()
    baseline_hashes[path] = hashlib.sha256(raw).hexdigest()
    diffs[path] = ''.join(difflib.unified_diff(raw.decode('utf-8-sig').splitlines(True), source_bytes[path].decode('utf-8-sig').splitlines(True), fromfile='frozen/' + path, tofile=path))
assert all((ROOT / p).read_bytes() == raw for p, raw in source_bytes.items()), 'source changed during run'
receipt = {'model': 'actual-source subset; supplied native primitives; no native VM/probability/admission proof', 'reused_framework': str(PRIOR), 'framework_sha256': hashlib.sha256(PRIOR.read_bytes()).hexdigest(), 'source_hashes': {p: hashlib.sha256(raw).hexdigest() for p, raw in source_bytes.items()}, 'baseline_hashes': baseline_hashes, 'source_diffs': diffs, 'cases': cases, 'case_count': len(cases), 'all_assertions_passed': True}
(OUT / 'case_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'cases': len(cases), 'all_assertions_passed': True, 'receipt': str(OUT / 'case_receipt.json')}, indent=2))
