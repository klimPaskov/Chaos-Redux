"""Exercise actual catalogue trigger source against the independent MCP membership oracle.

Native GetID is an explicit numeric-state input; opaque id deliberately differs.
The evaluator supports only the commands present in this geometry query and fails
on any persistent mutation or unsupported opcode. Helper-local scratch expires.
"""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import importlib.util
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def parse(text):
    text = '\n'.join(line.split('#', 1)[0] for line in text.splitlines())
    tokens = re.findall(r'"[^"\n]*"|[{}=<>]|[^\s{}=<>]+', text)
    pos = 0
    def block(close=False):
        nonlocal pos
        out = []
        while pos < len(tokens):
            if tokens[pos] == '}':
                assert close
                pos += 1
                return out
            key, op = tokens[pos:pos+2]
            assert op in ['=', '<', '>'], (key, op)
            pos += 2
            if tokens[pos] == '{':
                pos += 1
                value = block(True)
            else:
                value = tokens[pos]
                pos += 1
            out.append((key, op, value))
        assert not close
        return out
    return block()


sources = {}
definitions = {}
for name in ['016_transit_state_province_catalog_triggers.txt', '016_transit_state_province_catalog_data.txt']:
    p = ROOT/'common/scripted_triggers'/name
    sources[p.relative_to(ROOT).as_posix()] = p.read_bytes()
    for key, op, body in parse(p.read_text(encoding='utf-8')):
        assert op == '=' and isinstance(body, list) and key not in definitions
        definitions[key] = body
constants_path = ROOT/'common/script_constants/016_transit_catalog_constants.txt'
sources[constants_path.relative_to(ROOT).as_posix()] = constants_path.read_bytes()
constants = {}
for category, _, body in parse(constants_path.read_text(encoding='utf-8')):
    for key, _, value in body:
        if key != 'schema':
            constants['constant:'+category+'.'+key] = Decimal(value)


class VM:
    def __init__(self, state_id):
        self.state_id = Decimal(str(state_id))
        self.vars = {}
        self.arrays = {}
        self.calls = 0
        self.depth = 0
        self.max_depth = 0
        self.scope = 'state'
    def value(self, text):
        if text.endswith('^num'):
            return Decimal(len(self.arrays.get(text[:-4], [])))
        if text == 'id':
            return -self.state_id  # Explicit opaque-id distinction.
        if text in constants:
            return constants[text]
        try:
            return Decimal(text)
        except Exception:
            return self.vars.get(text, Decimal(0))
    def call(self, name):
        assert name in definitions, name
        old_vars, old_arrays = set(self.vars), set(self.arrays)
        self.calls += 1
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)
        result = self.eval(definitions[name])
        self.depth -= 1
        for key in set(self.vars)-old_vars:
            del self.vars[key]
        for key in set(self.arrays)-old_arrays:
            del self.arrays[key]
        return result
    def eval(self, nodes):
        i = 0
        while i < len(nodes):
            key, op, body = nodes[i]
            i += 1
            if key == 'if':
                limit = next(v for k, _, v in body if k == 'limit')
                yes = self.eval(limit)
                other = None
                if i < len(nodes) and nodes[i][0] == 'else':
                    other = nodes[i][2]
                    i += 1
                if yes:
                    self.eval([n for n in body if n[0] != 'limit'])
                elif other is not None:
                    self.eval(other)
            elif key == 'set_temp_variable':
                assert len(body) == 1
                name, _, value = body[0]
                self.vars[name] = self.value(value)
            elif key == 'clear_temp_array':
                self.arrays[body] = []
            elif key == 'add_to_temp_array':
                values = {k:v for k,_,v in body}
                self.arrays.setdefault(values['array'], []).append(int(self.value(values['value'])))
            elif key == 'meta_trigger':
                values = {k:v for k,_,v in body}
                assert self.scope == 'state', 'Native GetID input requires STATE scope'
                assert values['STATE_ID'] == '"[This.GetID]"'
                def substitute(items):
                    return [(k,o,substitute(v) if isinstance(v,list) else v.replace('[STATE_ID]',str(self.state_id))) for k,o,v in items]
                if not self.eval(substitute(values['text'])):
                    return False
            elif key == 'check_variable':
                values = {k:(o,v) for k,o,v in body}
                if 'var' in values:
                    a = self.value(values['var'][1]); b = self.value(values['value'][1]); cmp = values.get('compare',('=', 'equals'))[1]
                    result = {'equals':a==b,'greater_than_or_equals':a>=b,'less_than_or_equals':a<=b}[cmp]
                else:
                    assert len(body) == 1
                    var, cmp, value = body[0];a,b=self.value(var),self.value(value)
                    result = {'<':a<b,'>':a>b,'=':a==b}[cmp]
                if not result:
                    return False
            elif key == 'always':
                if body != 'yes':
                    return False
            elif key in definitions:
                assert body == 'yes'
                if not self.call(key):
                    return False
            else:
                raise AssertionError('Unsupported or persistent command: '+key)
        return True


data = json.loads((ROOT/'docs/testing/event016_transit_catalog_20261008/state_membership.json').read_text(encoding='utf-8'))
entry = 'brilliant_scientist_transit_load_state_province_catalog'
cases = 0
maximum_depth = 0
for row in data['states']:
    v = VM(row['id'])
    v.vars.update(transit_catalog_state_id=Decimal(99999), transit_catalog_loaded=Decimal(1))
    v.arrays['transit_state_province_ids'] = [99999]
    assert v.call(entry)
    assert v.vars['transit_catalog_state_id'] == row['id']
    assert v.vars['transit_catalog_loaded'] == 1
    assert v.arrays['transit_state_province_ids'] == row['provinceIds'], row['id']
    maximum_depth = max(maximum_depth, v.max_depth)
    cases += 1
for state_id in [0,-1,'0.5','1.5','1081.5',1082,99999]:
    v = VM(state_id)
    v.vars.update(transit_catalog_state_id=Decimal(64), transit_catalog_loaded=Decimal(1))
    v.arrays['transit_state_province_ids'] = [6521]
    assert v.call(entry)
    assert v.vars['transit_catalog_loaded'] == 0 and v.arrays['transit_state_province_ids'] == []
    cases += 1
v = VM(64)
assert v.call(entry)
assert not v.vars and not v.arrays  # Bare caller cannot rely on helper-created outputs.
cases += 1

# Reusing one caller must clear every previous membership/status correctly.
v = VM(64)
v.vars.update(transit_catalog_state_id=Decimal(0), transit_catalog_loaded=Decimal(0))
v.arrays['transit_state_province_ids'] = []
v.vars['unrelated_scalar'] = Decimal(17)
v.arrays['unrelated_array'] = [42]
oracle = {r['id']:r['provinceIds'] for r in data['states']}
for sid in [64,65,1082,64,'1.5',1081]:
    v.state_id = Decimal(str(sid))
    v.call(entry)
    expected = oracle.get(v.state_id, [])
    assert v.arrays['transit_state_province_ids'] == expected
    assert v.vars['transit_catalog_loaded'] == bool(expected)
    assert v.vars['unrelated_scalar'] == 17 and v.arrays['unrelated_array'] == [42]
    cases += 1

# Only caller-created outputs survive; no omitted result is implicitly reliable.
for omitted in ['transit_catalog_state_id','transit_catalog_loaded','transit_state_province_ids']:
    v = VM(64)
    for name in ['transit_catalog_state_id','transit_catalog_loaded']:
        if name != omitted:
            v.vars[name] = Decimal(0)
    if omitted != 'transit_state_province_ids':
        v.arrays['transit_state_province_ids'] = []
    v.call(entry)
    assert omitted not in v.vars and omitted not in v.arrays
    if omitted != 'transit_state_province_ids':
        assert v.arrays['transit_state_province_ids'] == oracle[64]
    cases += 1

cxt_path = ROOT/'common/scripted_effects/016_transit_catalog_cxt_effects.txt'
sources[cxt_path.relative_to(ROOT).as_posix()] = cxt_path.read_bytes()
for key, _, body in parse(cxt_path.read_text(encoding='utf-8')):
    definitions[key] = body


class CxtVM(VM):
    def __init__(self, capital=64, tag='CXT', exists=True, initialized=True):
        super().__init__(capital if capital is not None else 0)
        self.capital = capital
        self.scope = 'country'
        self.tag = tag
        self.exists = exists
        self.regular = {'untouched_regular': Decimal(17)}
        self.flags = {'untouched_flag'}
        if initialized:
            self.flags.add('chaosx_test_country_initialized')
    def eval(self, nodes):
        i = 0
        while i < len(nodes):
            key, op, value = nodes[i]
            i += 1
            if key == 'tag':
                if self.tag != value: return False
            elif key == 'exists':
                if self.exists != (value == 'yes'): return False
            elif key == 'has_country_flag':
                if value not in self.flags: return False
            elif key == 'set_variable':
                assert self.scope == 'country' and len(value) == 1
                name, _, amount = value[0]
                assert name.startswith('chaosx_cxt_event016_transit_catalog_')
                self.regular[name] = self.value(amount)
            elif key in ['set_country_flag','clr_country_flag']:
                assert self.scope == 'country' and value == 'chaosx_cxt_event016_transit_catalog_loaded'
                if key == 'set_country_flag': self.flags.add(value)
                else: self.flags.discard(value)
            elif key == 'capital_scope':
                if self.capital is None:
                    continue  # Explicit modeled absent-native-scope behavior.
                previous = self.scope
                self.scope = 'state'
                self.state_id = Decimal(self.capital)
                self.eval(value)
                self.scope = previous
            else:
                group = [(key,op,value)]
                if key == 'if' and i < len(nodes) and nodes[i][0] == 'else':
                    group.append(nodes[i]);i += 1
                if not super().eval(group): return False
        return True


probe = 'chaosx_cxt_event016_probe_transit_state_catalog'
for sid in [64,1082]:
    v = CxtVM(capital=sid)
    v.flags.add('chaosx_cxt_event016_transit_catalog_loaded')
    v.call(probe)
    assert v.scope == 'country' and v.regular['untouched_regular'] == 17 and 'untouched_flag' in v.flags
    assert v.regular['chaosx_cxt_event016_transit_catalog_state_id'] == sid
    assert v.regular['chaosx_cxt_event016_transit_catalog_province_count'] == len(oracle.get(sid, []))
    assert ('chaosx_cxt_event016_transit_catalog_loaded' in v.flags) == (sid in oracle)
    cases += 1
v = CxtVM(capital=None)
v.flags.add('chaosx_cxt_event016_transit_catalog_loaded')
v.call(probe)
assert v.regular['chaosx_cxt_event016_transit_catalog_state_id'] == 0
assert v.regular['chaosx_cxt_event016_transit_catalog_province_count'] == 0
assert 'chaosx_cxt_event016_transit_catalog_loaded' not in v.flags and v.scope == 'country'
cases += 1
for kwargs in [{'tag':'GER'},{'exists':False},{'initialized':False}]:
    v = CxtVM(**kwargs);before = (dict(v.regular),set(v.flags));v.call(probe)
    assert (v.regular,v.flags) == before
    cases += 1

spec = importlib.util.spec_from_file_location('catalog_builder', ROOT/'.tools/build_event016_transit_state_catalog.py')
builder = importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
for mutate in ['duplicate_state','duplicate_province','empty_membership','fractional_state','boolean_state','fractional_province','boolean_province']:
    bad = json.loads(json.dumps(data))
    if mutate == 'duplicate_state': bad['states'].append(bad['states'][0])
    elif mutate == 'duplicate_province': bad['states'][1]['provinceIds'].append(bad['states'][0]['provinceIds'][0])
    elif mutate == 'empty_membership': bad['states'][0]['provinceIds'] = []
    elif mutate == 'fractional_state': bad['states'][0]['id'] = 1.5
    elif mutate == 'boolean_state': bad['states'][0]['id'] = True
    elif mutate == 'fractional_province': bad['states'][0]['provinceIds'][0] = 1.5
    else: bad['states'][0]['provinceIds'][0] = True
    try: builder.validate(bad)
    except AssertionError: pass
    else: raise AssertionError('Invalid generator input accepted: '+mutate)
    cases += 1
with tempfile.TemporaryDirectory(prefix='transit-catalog-refusal-') as directory:
    p = Path(directory)/'artifact.json';p.write_bytes(b'{}')
    try: builder.extract(p,'0'*64)
    except AssertionError: pass
    else: raise AssertionError('Wrong artifact hash accepted')
    assert p.read_bytes() == b'{}'
    cases += 1
    artifact = {'revision':'test-revision','sourceHashes':{'test:state':'1'*64},
                'catalog':{'states':[{'id':1,'provinceIds':[1],'sourcePath':'test:state','sourceLine':1}]},
                'validation':{'passed':True,'checks':[{'id':k,'passed':True} for k in
                    ['map-files-and-definitions','map-bitmap-geometry','map-state-region-membership','map-networks-adjacencies']]}}
    original_input = builder.INPUT
    builder.INPUT = Path(directory)/'preserved.json'
    builder.INPUT.write_bytes(b'{"preserve":"old"}')
    try:
        raw = json.dumps(artifact).encode('utf-8');p.write_bytes(raw)
        try: builder.extract(p,hashlib.sha256(raw).hexdigest())
        except AssertionError: pass
        else: raise AssertionError('Different preserved input silently overwritten')
        assert builder.INPUT.read_bytes() == b'{"preserve":"old"}'
        cases += 1
        artifact['validation']['checks'][2]['passed'] = False
        raw = json.dumps(artifact).encode('utf-8');p.write_bytes(raw)
        try: builder.extract(p,hashlib.sha256(raw).hexdigest())
        except AssertionError: pass
        else: raise AssertionError('Failed membership check accepted')
        assert builder.INPUT.read_bytes() == b'{"preserve":"old"}'
        cases += 1
    finally:
        builder.INPUT = original_input
print(json.dumps({'passed':cases,'knownStateCases':len(data['states']),'unknownIdCases':7,
                  'bareCallerNegativeControl':True,'maximumHelperDepth':maximum_depth,
                  'sequentialQueries':6,'partialInitializationCases':3,'cxtExecutionCases':6,'generatorRefusals':10,
                  'sourceHashes':{p:hashlib.sha256(b).hexdigest() for p,b in sources.items()},
                  'boundary':['actual parsed dispatcher/data/constant source','GetID is explicit native state-ID input',
                              'conservative nested temporary lifetime','membership oracle is retained MCP data',
                              'no native scope/GetID/loop-performance or supply/network proof']},indent=2))
