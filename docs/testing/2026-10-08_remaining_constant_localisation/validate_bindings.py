"""Bounded source contract for the twelve repaired numeric localisation bindings."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = Path(__file__).resolve().parent
groups = json.loads((EVIDENCE / 'bindings.json').read_text(encoding='utf-8'))
constants = {}
for path in (ROOT / 'common/script_constants').glob('*.txt'):
    stack = []
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        line = line.split('#', 1)[0]
        for match in re.finditer(r'(\w+)\s*=\s*\{|\}|(\w+)\s*=\s*(-?\d+(?:\.\d+)?)', line):
            if match[1]:
                stack.append(match[1])
            elif match[2]:
                if len(stack) == 1:
                    constants[stack[0] + '.' + match[2]] = float(match[3])
            elif stack:
                stack.pop()
scripts = '\n'.join(p.read_text(encoding='utf-8-sig') for p in (ROOT / 'common/scripted_localisation').glob('*.txt'))
loc = '\n'.join(p.read_text(encoding='utf-8-sig') for p in (ROOT / 'localisation/english').glob('*.yml'))
results = []
for group in groups:
    text = (ROOT / group['localisation']).read_text(encoding='utf-8-sig')
    baseline = (EVIDENCE / 'before' / Path(group['localisation'])).read_text(encoding='utf-8-sig')
    expected = baseline
    for binding in group['bindings']:
        token = '[?constant:' + binding['constant'] + '|' + binding['format'] + ']'
        expected = expected.replace(token, '[' + binding['getter'] + ']')
    current_values = dict(re.findall(r'^(\w+): (.*)$', text, re.M))
    for key, value in re.findall(r'^(\w+): (.*)$', expected, re.M):
        assert current_values[key].rstrip('\r') == value.rstrip('\r'), key
    assert (ROOT / group['localisation']).read_bytes().startswith(bytes.fromhex('efbbbf'))
    script = (ROOT / group['scripted_localisation']).read_text(encoding='utf-8-sig')
    assert '[?constant:' not in text
    for binding in group['bindings']:
        name, var, key = (binding[k] for k in ('getter', 'variable', 'key'))
        assert len(re.findall(r'name\s*=\s*' + name + r'\b', scripts)) == 1
        assert len(re.findall(r'^' + key + ':', loc, re.M)) == 1
        body = re.search(r'defined_text\s*=\s*\{\s*name\s*=\s*' + name + r'\b(.*?)\n\}', script, re.S)[1]
        assignment = re.search(r'set_temp_variable\s*=\s*\{\s*(\w+)\s*=\s*constant:([\w.]+)\s*\}', body)
        assert assignment.groups() == (var, binding['constant'])
        assert 'localization_key = ' + key in body and 'always = yes' in body
        assert key + ': "[?' + var + '|' + binding['format'] + ']"' in text
        value = constants[assignment[2]]
        rendered = str(round(value * 100)) + '%' if binding['format'] == '%0' else str(round(value))
        results.append(dict(**binding, value=value, rendered=rendered))
    keys = re.findall(r'^(\w+):', text, re.M)
    assert len(keys) == len(set(keys))
assert len({r['variable'] for r in results}) == 12
# Negative mutations prove the two primary regression guards reject bad input.
def raw_guard(text):
    assert '[?constant:' not in text
def key_guard(text, key):
    assert len(re.findall(r'^' + key + ':', text, re.M)) == 1
for guard, args in [(raw_guard, ('bad: "[?constant:x.y|0]"',)), (key_guard, ('l_english:\n', results[0]['key']))]:
    try:
        guard(*args)
    except AssertionError:
        pass
    else:
        raise AssertionError('Negative regression guard failed')
(EVIDENCE / 'validation.json').write_text(json.dumps(dict(bindings=results, raw_token_guard=True, missing_key_guard=True, distinct_variables=12, scope='Production source binding contract, not native engine execution'), indent=2), encoding='utf-8')
print('12 production bindings resolve; raw-token and missing-key negative guards reject regressions.')
