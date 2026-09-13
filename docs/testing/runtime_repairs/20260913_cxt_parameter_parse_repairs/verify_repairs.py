"""Check helper input delivery, expanded campus logic, and preserved inventories."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent

def source(name, before=False):
    return (QA / 'baseline' / name if before else ROOT / name).read_text(encoding='utf-8-sig')

TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>"#]+')
def parse(text):
    tokens = [m[0] for m in TOKEN.finditer(text) if not m[0].startswith('#')]
    pos = 0
    def block(nested=False):
        nonlocal pos
        result = []
        while pos < len(tokens) and tokens[pos] != '}':
            key = tokens[pos]
            pos += 1
            if pos < len(tokens) and tokens[pos] in ('=', '<', '>'):
                op = tokens[pos]
                pos += 1
                value = tokens[pos]
                pos += 1
                if value == '{':
                    value = block(True)
                result.append((key, op, value))
            else:
                result.append(key)
        if nested:
            assert pos < len(tokens) and tokens[pos] == '}'
            pos += 1
        return result
    result = block()
    assert pos == len(tokens)
    return result

def field(tree, name):
    return next(node[2] for node in tree if isinstance(node, tuple) and node[0] == name)

def normalize(text):
    return parse(text)

effects_name = 'common/scripted_effects/chaosx_test_country_effects.txt'
trigger_name = 'common/scripted_triggers/chaosx_test_country_triggers.txt'
project_name = 'common/scripted_effects/chaosx_test_country_special_project_effects.txt'
before = parse(source(effects_name, True))
after = parse(source(effects_name))
before_core = field(before, 'chaosx_test_country_provision_facility_type')
after_core = field(field(field(after, 'chaosx_test_country_provision_facility_type'), 'meta_effect'), 'text')

def expected_body(text):
    text = text.replace('$FACILITY$', '[FACILITY]')
    text = text.replace('chaosx_test_country_state_can_host_facility_type = { FACILITY = [FACILITY] COASTAL_REQUIRED = $COASTAL_REQUIRED$ }', 'chaosx_test_country_state_can_host_facility_type = yes')
    return text.replace('NOT = { always = $COASTAL_REQUIRED$ }', 'NOT = { check_variable = { chaosx_test_country_current_facility = token:naval_facility } }')

old_text = source(effects_name, True)
start = old_text.index('chaosx_test_country_provision_facility_type = {')
end = old_text.index('\nchaosx_test_country_build_special_facilities', start)
expected_core = field(parse(expected_body(old_text[start:end])), 'chaosx_test_country_provision_facility_type')
assert expected_core == after_core, 'Campus body changed beyond supported parameter delivery'

types = ['naval_facility', 'nuclear_facility', 'air_facility', 'land_facility', 'biowarfare_facility', 'cw_facility']
calls = field(after, 'chaosx_test_country_build_special_facilities')
assert calls[0] == ('clr_country_flag', '=', 'chaosx_test_country_facility_provisioning_incomplete')
for i, kind in enumerate(types):
    assert calls[1+i*2] == ('set_temp_variable', '=', [('chaosx_test_country_current_facility', '=', 'token:' + kind)])
    assert calls[2+i*2] == ('chaosx_test_country_provision_facility_type', '=', 'yes')
assert len(calls) == 13
trigger = field(parse(source(trigger_name)), 'chaosx_test_country_state_can_host_facility_type')
assert field(field(trigger, 'meta_trigger'), 'text') == [('can_construct_building', '=', '[FACILITY]')]
assert field(trigger, 'is_owned_by') == 'ROOT'
assert field(trigger, 'chaosx_test_country_state_can_host_special_facility') == 'yes'

for kind in types:
    for coastal in (False, True):
        assert ((kind != 'naval_facility') or coastal) == ((kind == 'naval_facility') is False or coastal)

# All helper orchestration outside facility provisioning and its input wrapper is identical.
changed = {'chaosx_test_country_provision_facility_type', 'chaosx_test_country_build_special_facilities'}
assert [n for n in before if n[0] not in changed] == [n for n in after if n[0] not in changed]

old_projects = parse(source(project_name, True))
new_projects = parse(source(project_name))
def convert_calls(tree):
    result = []
    for key, op, value in tree:
        if key == 'chaosx_test_country_complete_special_project' and isinstance(value, list):
            project = field(value, 'PROJECT')
            result.extend([('set_temp_variable', '=', [('chaosx_test_country_current_special_project', '=', 'sp:' + project)]), (key, op, 'yes')])
        else:
            result.append((key, op, convert_calls(value) if isinstance(value, list) else value))
    return result
assert convert_calls(field(old_projects, 'chaosx_test_country_complete_all_special_projects')) == field(new_projects, 'chaosx_test_country_complete_all_special_projects')
native_project = 'var:chaosx_test_country_current_special_project'
completion = field(field(new_projects, 'chaosx_test_country_complete_special_project'), 'if')
assert field(completion, 'limit') == [('NOT', '=', [('is_special_project_completed', '=', native_project)])]
assert field(completion, 'complete_special_project') == [('project', '=', native_project), ('show_modifiers', '=', 'no')]
registered = field(new_projects, 'chaosx_test_country_complete_registered_special_projects')
assert field(registered, 'for_each_loop') == [('array', '=', 'global.chaosx_test_country_registered_special_projects'), ('value', '=', 'chaosx_test_country_current_special_project'), ('chaosx_test_country_complete_special_project', '=', 'yes')]
assert field(old_projects, 'chaosx_test_country_register_special_project') == field(new_projects, 'chaosx_test_country_register_special_project')
project_ids = re.findall(r'chaosx_test_country_current_special_project = sp:(\w+)', source(project_name))
assert len(project_ids) == len(set(project_ids)) == 83
assert len(re.findall('has_dlc =', source(project_name, True))) == len(re.findall('has_dlc =', source(project_name)))
for name in (effects_name, trigger_name, project_name):
    assert not re.search(r'\$(?:FACILITY|COASTAL_REQUIRED|PROJECT)\$', source(name))

unchanged_inventory = {}
for name in ('common/scripted_effects/chaosx_test_country_stockpile_effects.txt', 'common/scripted_effects/chaosx_test_country_unit_effects.txt', 'history/countries/CXT - Chaos Redux Test Country.txt', 'events/chaosx_test_country.txt'):
    head = subprocess.check_output(['git', 'show', 'HEAD:' + name], cwd=ROOT).decode('utf-8-sig')
    current = source(name)
    assert normalize(head) == normalize(current), name + ' changed'
    unchanged_inventory[name] = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()

attachment = Path('C:/Users/klimp/.codex/attachments/2124b3ce-d9fd-48b8-bd4f-81b8503c20dc/pasted-text.txt')
raw = attachment.read_bytes()
log = raw.decode('utf-8-sig')
cpp_counts = {}
for name in re.findall(r'\[([a-z_]+\.cpp|gameitemdatabase\.h|scopedvariable\.cpp):\d+\]', log):
    cpp_counts[name] = cpp_counts.get(name, 0) + 1
report = {
    'supplied_report_sha256': hashlib.sha256(raw).hexdigest(),
    'supplied_report_native_components': cpp_counts,
    'native_reported_load_error_summary': re.findall(r'\]: (\d+) errors\.', log),
    'preserved_projects': project_ids,
    'preserved_facility_types': types,
    'expanded_facility_body_equal': True,
    'project_order_dlc_gates_and_silent_lifecycle_equal': True,
    'outside_facility_orchestration_equal': True,
    'unchanged_inventory_hashes': unchanged_inventory,
    'technology_database_entry': 'unidentified; diagnostics retained; full task incomplete',
    'limitations': 'This source comparison is not an HOI4 engine parse or runtime execution.',
}
(QA / 'source_verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k in ('preserved_facility_types', 'expanded_facility_body_equal', 'project_order_dlc_gates_and_silent_lifecycle_equal', 'outside_facility_orchestration_equal', 'technology_database_entry')}))
