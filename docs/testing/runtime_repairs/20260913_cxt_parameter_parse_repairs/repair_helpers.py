"""Bounded mechanical conversion of the supplied CXT placeholder error sites."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
FILES = [
    'common/scripted_effects/chaosx_test_country_effects.txt',
    'common/scripted_triggers/chaosx_test_country_triggers.txt',
    'common/scripted_effects/chaosx_test_country_special_project_effects.txt',
    'docs/testing/chaosx_test_country.md',
    '.agents/skills/chaos-redux-events/SKILL.md',
]
hashes = {}
for name in FILES:
    raw = (ROOT / name).read_bytes()
    dest = QA / 'baseline' / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    assert not dest.exists(), f'Baseline already exists: {name}'
    dest.write_bytes(raw)
    hashes[name] = hashlib.sha256(raw).hexdigest()
(QA / 'before_hashes.json').write_text(json.dumps(hashes, indent=2) + '\n', encoding='utf-8')

def read(name):
    return (ROOT / name).read_text(encoding='utf-8-sig')

def write(name, text):
    original = (ROOT / name).read_bytes()
    raw = text.replace('\r\n', '\n').encode('utf-8')
    if original.startswith(b'\xef\xbb\xbf'):
        raw = b'\xef\xbb\xbf' + raw
    if b'\r\n' in original:
        raw = raw.replace(b'\n', b'\r\n')
    (ROOT / name).write_bytes(raw)

name = FILES[0]
text = read(name)
start = text.index('chaosx_test_country_provision_facility_type = {')
end = text.index('\nchaosx_test_country_build_special_facilities = {', start)
body = text[start:end]
inner = body[body.index('\n') + 1:body.rfind('\n}')]
inner = inner.replace('$FACILITY$', '[FACILITY]')
inner = inner.replace('chaosx_test_country_state_can_host_facility_type = { FACILITY = [FACILITY] COASTAL_REQUIRED = $COASTAL_REQUIRED$ }', 'chaosx_test_country_state_can_host_facility_type = yes')
inner = inner.replace('NOT = { always = $COASTAL_REQUIRED$ }', 'NOT = { check_variable = { chaosx_test_country_current_facility = token:naval_facility } }')
assert '$' not in inner
replacement = (
    'chaosx_test_country_provision_facility_type = {\n'
    '\tmeta_effect = {\n\t\ttext = {\n'
    + '\n'.join('\t\t' + line if line else '' for line in inner.splitlines())
    + '\n\t\t}\n\t\tFACILITY = "[?chaosx_test_country_current_facility.GetTokenKey]"\n\t}\n}\n'
)
text = text[:start] + replacement + text[end:]
text, count = re.subn(
    r'(?m)^(\t)chaosx_test_country_provision_facility_type = \{ FACILITY = (\w+) COASTAL_REQUIRED = (yes|no) \}$',
    lambda m: f'{m[1]}set_temp_variable = {{ chaosx_test_country_current_facility = token:{m[2]} }}\n{m[1]}chaosx_test_country_provision_facility_type = yes',
    text,
)
assert count == 6
write(name, text)

name = FILES[1]
text = read(name)
start = text.index('# State scope. FACILITY')
text = text[:start] + '''# State scope, ROOT = CXT. Input: temporary building token
# chaosx_test_country_current_facility, assigned before the helper call.
# Native construction legality remains specific to that installed type.
chaosx_test_country_state_can_host_facility_type = {
	is_owned_by = ROOT
	OR = {
		NOT = { check_variable = { chaosx_test_country_current_facility = token:naval_facility } }
		is_coastal = yes
	}
	chaosx_test_country_state_can_host_special_facility = yes
	meta_trigger = {
		text = { can_construct_building = [FACILITY] }
		FACILITY = "[?chaosx_test_country_current_facility.GetTokenKey]"
	}
}
'''
write(name, text)

name = FILES[2]
text = read(name)
text = text.replace('# Country scope. PROJECT is a static installed project id; repeated calls are safe.', '# Country scope. Input: temporary sp: scope in\n# chaosx_test_country_current_special_project; repeated calls are safe.')
text = text.replace('sp:$PROJECT$', 'var:chaosx_test_country_current_special_project')
text, count = re.subn(
    r'(?m)^(\t+)chaosx_test_country_complete_special_project = \{ PROJECT = (\w+) \}$',
    lambda m: f'{m[1]}set_temp_variable = {{ chaosx_test_country_current_special_project = sp:{m[2]} }}\n{m[1]}chaosx_test_country_complete_special_project = yes',
    text,
)
assert count == 83
old = '''		if = {
			limit = { NOT = { is_special_project_completed = var:chaosx_test_country_current_special_project } }
			complete_special_project = { project = var:chaosx_test_country_current_special_project show_modifiers = no }
		}'''
assert old in text
text = text.replace(old, '\t\tchaosx_test_country_complete_special_project = yes')
assert '$PROJECT$' not in text and 'PROJECT =' not in text
write(name, text)
print(json.dumps({'facility_calls_converted': 6, 'project_calls_converted': count, 'baseline_files': len(FILES)}))
