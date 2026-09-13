"""Verify deferred condemnation requests and complete indexed grant delivery."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
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

def field(tree, key):
    matches = [n[2] for n in tree if isinstance(n, tuple) and n[0] == key]
    assert len(matches) == 1, (key, len(matches))
    return matches[0]

def source(name, before=False):
    path = QA / 'baseline' / name if before else ROOT / name
    return path.read_text(encoding='utf-8-sig')

def head(name):
    return subprocess.check_output(['git', 'show', 'HEAD:' + name], cwd=ROOT).decode('utf-8-sig')

shared = 'common/scripted_effects/condemnation_sanctions_effects.txt'
old = parse(source(shared, True))
new = parse(source(shared))
capital = [('any_owned_state', '=', [('is_capital', '=', 'yes')])]
pairs = [('condemnation_recalculate_participants', 'condemnation_participant_refresh_pending'),
         ('condemnation_start_targeted_pulse', 'condemnation_targeted_pulse_pending')]
for helper, flag in pairs:
    assert field(old, helper) == field(new, helper + '_apply'), helper
    assert field(new, helper) == [
        ('if', '=', [('limit', '=', [('tag', '=', 'CXT'), ('NOT', '=', capital)]),
                     ('set_country_flag', '=', flag)]),
        ('else', '=', [(helper + '_apply', '=', 'yes')])]
flush_body = [('limit', '=', capital)]
for helper, flag in pairs:
    flush_body.append(('if', '=', [('limit', '=', [('has_country_flag', '=', flag)]),
                                  ('clr_country_flag', '=', flag), (helper, '=', 'yes')]))
assert field(new, 'condemnation_flush_deferred_refresh') == [('if', '=', flush_body)]
public_names = {helper for helper, _ in pairs}
added_names = {helper + '_apply' for helper in public_names} | {'condemnation_flush_deferred_refresh'}
assert [n for n in old if n[0] not in public_names] == [n for n in new if n[0] not in public_names | added_names]
assert len({n[0] for n in new}) == len(new)

core = 'common/scripted_effects/chaosx_test_country_effects.txt'
old_core = parse(source(core, True))
new_core = parse(source(core))
hook_names = {'chaosx_test_country_initial_setup', 'chaosx_test_country_sync_registered_content'}
for helper in hook_names:
    assert field(new_core, helper) == [('condemnation_flush_deferred_refresh', '=', 'yes')] + field(old_core, helper)
assert [n for n in old_core if n[0] not in hook_names] == [n for n in new_core if n[0] not in hook_names]
assert field(old_core, 'chaosx_test') == field(new_core, 'chaosx_test')

tech = 'common/scripted_effects/chaosx_test_country_technology_effects.txt'
tree = field(parse(source(tech)), 'chaosx_test_country_complete_all_technologies')
assert tree[:3] == [
    ('set_temp_variable', '=', [('chaosx_test_country_technology_grant_applied', '=', '0')]),
    ('set_temp_variable', '=', [('chaosx_test_country_technology_count', '=', 'global.technology^num')]),
    ('set_temp_variable', '=', [('chaosx_test_country_technology_loop_break', '=', '0')])]
loop = field(tree, 'for_loop_effect')
for key, value in [('start', '0'), ('end', 'chaosx_test_country_technology_count'),
                   ('compare', 'less_than'), ('value', 'chaosx_test_country_current_technology_index'),
                   ('break', 'chaosx_test_country_technology_loop_break')]:
    assert field(loop, key) == value
assert field(loop, 'set_temp_variable') == [('chaosx_test_country_current_technology', '=', 'global.technology^chaosx_test_country_current_technology_index')]
grant = field(loop, 'if')
assert field(grant, 'limit') == [('NOT', '=', [('has_tech', '=', 'var:chaosx_test_country_current_technology')])]
assert field(grant, 'set_technology') == [('var:chaosx_test_country_current_technology', '=', '1'), ('popup', '=', 'no')]
assert field(grant, 'set_temp_variable') == [('chaosx_test_country_technology_grant_applied', '=', '1')]
assert field(tree, 'if') == [('limit', '=', [('check_variable', '=', [('chaosx_test_country_technology_grant_applied', '>', '0')])]), ('mark_technology_tree_layout_dirty', '=', 'yes')]
assert len(loop) == 9 and len(tree) == 6, 'Unexpected filter, early break, or additional consumer'

unchanged = {}
for name in (
    'common/scripted_effects/chaosx_test_country_special_project_effects.txt',
    'common/scripted_effects/chaosx_test_country_stockpile_effects.txt',
    'common/scripted_effects/chaosx_test_country_unit_effects.txt',
    'common/scripted_triggers/chaosx_test_country_triggers.txt',
    'history/countries/CXT - Chaos Redux Test Country.txt',
    'events/chaosx_test_country.txt',
    'common/on_actions/chaosx_test_country_on_actions.txt'):
    assert parse(source(name)) == parse(head(name)), name
    unchanged[name] = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
projects = re.findall(r'chaosx_test_country_current_special_project = sp:(\w+)', source(next(iter(unchanged))))
assert len(projects) == len(set(projects)) == 83

# Model the two queue flags, not the engine's scoring or native technology execution.
def dispatch(is_cxt, capital_valid, pending, applied):
    if is_cxt and not capital_valid:
        return True, applied
    return pending, applied + 1
pending, applied = False, 0
for _ in range(91):
    pending, applied = dispatch(True, False, pending, applied)
assert pending and applied == 0
pending = False  # Cleared before valid-capital public dispatch.
pending, applied = dispatch(True, True, pending, applied)
assert not pending and applied == 1
assert dispatch(False, True, False, 0) == (False, 1)

report = {
    'validation': 'source and dispatch-state model only; no engine execution',
    'original_participant_and_pulse_bodies_preserved': True,
    'all_other_shared_helpers_preserved': True,
    'public_console_and_receiver_preserved': True,
    'queue_cases': ['dormant CXT coalesces 91 requests', 'no-capital flush retains flags', 'valid activation clears then dispatches once', 'ordinary country dispatch is immediate'],
    'activation_and_registered_bus_flush_first': True,
    'technology_contract': 'all in-bounds runtime indexes, native var consumers, silent and idempotent; runtime outcome unverified',
    'core_project_count': len(projects),
    'unchanged_inventory_sources': unchanged,
    'temporary_technology_diagnostics_retained': source(tech).count('\n\tlog = ') + source(tech).count('\n\t\tlog = '),
    'current_source_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in (shared, core, tech)}
}
(QA / 'source_verification.json').write_bytes((json.dumps(report, indent=2) + '\n').encode('utf-8'))
print('Original scoring bodies, console activation, history pre-unlocks, 83 projects, and all inventory sources are preserved.')
print('Deferred request state model and full indexed technology source contract pass; runtime grant result is unverified.')
