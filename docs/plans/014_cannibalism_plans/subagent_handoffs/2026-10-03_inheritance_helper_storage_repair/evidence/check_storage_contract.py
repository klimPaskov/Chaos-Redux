"""One-off actual-source storage probe, not an engine or complete transaction emulator.
Reuse the current audit's lexical block reader without running its inventory.
Only direct snapshot assignments and documented conservative return cleanup execute.
Control-flow and native side-effect preservation checks remain source evidence.
"""
from pathlib import Path
from functools import lru_cache
import ast
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'common/scripted_effects/014_cannibalism_effects.txt'
PRIOR = OUT / '014_cannibalism_effects.before.txt'
audit = ROOT / 'docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_final_current_completion_audit/evidence/audit_inventory.py'
node = next(n for n in ast.parse(audit.read_text(encoding='utf-8-sig')).body if isinstance(n, ast.FunctionDef) and n.name == 'blocks')
exec(compile(ast.Module(body=[node], type_ignores=[]), str(audit), 'exec'))
before = PRIOR.read_text(encoding='utf-8-sig')
after = SOURCE.read_text(encoding='utf-8-sig')
meta = json.loads((OUT / 'storage_boundaries.json').read_text())
results = []

@lru_cache(maxsize=4)
def definitions(text):
    return {b['key']: b for b in blocks(text) if b['depth'] == 0}

def get(text, name):
    b = definitions(text)[name]
    return text[b['start']:b['end']]

def assignments(text):
    return re.findall(r'set_temp_variable\s*=\s*\{\s*(\w+)\s*=\s*([^\s{}]+)\s*\}', text)

def prefix(text, name):
    body = get(text, name)
    first = next((b['start'] for b in blocks(body) if b['depth'] == 1 and b['key'] not in ['set_temp_variable']), len(body))
    return dict(assignments(body[:first]))

def check(name, passed, details):
    results.append(dict(name=name, passed=bool(passed), details=details))
    assert passed, (name, details)

def returned(storage, writes):
    # Newly created names belong to the callee. Preserve only caller-owned names.
    keys = set(storage)
    changed = dict(storage)
    changed.update(writes)
    return {k: v for k, v in changed.items() if k in keys}

def project_compare(body, left_token, values):
    block = next(b for b in blocks(body) if b['key'] == 'check_variable' and 'var = ' + left_token in body[b['start']:b['end']])
    fields = dict(re.findall(r'(var|value|compare)\s*=\s*([^\s{}]+)', body[block['start']:block['end']]))
    left, right = values[fields['var']], values[fields['value']]
    assert fields['compare'] in ['equals', 'greater_than_or_equals']
    return left == right if fields['compare'] == 'equals' else left >= right

# Verify all original bytes, including mixed line endings, survive as equal lines.
old_lines = PRIOR.read_bytes().splitlines(keepends=True)
new_lines = SOURCE.read_bytes().splitlines(keepends=True)
ops = list(difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False).get_opcodes())
check('insertion_only_exact_byte_preservation', all(op[0] in ['equal', 'insert'] for op in ops), 'Every original line retains its exact bytes. Provider 523, all tuning, guards and effects are preserved.')
(OUT / 'source_lifetime.patch').write_bytes(''.join(difflib.unified_diff(PRIOR.read_bytes().decode('utf-8-sig').splitlines(keepends=True), SOURCE.read_bytes().decode('utf-8-sig').splitlines(keepends=True), fromfile='common/scripted_effects/014_cannibalism_effects.txt (before)', tofile='common/scripted_effects/014_cannibalism_effects.txt (after)')).encode('utf-8'))
for boundary in meta['boundaries']:
    actual = prefix(after, boundary['caller'])
    check('frame_entry_' + boundary['caller'], all(actual.get(n) == v for n, v in boundary['defaults'].items()), boundary['outputs'])

inherit = meta['inheritanceOutputs']
capture = get(after, 'cannibalism_capture_current_warlord_inheritance')
donor = {rhs: (i + 1) * 11 for i, (lhs, rhs) in enumerate(assignments(capture)) if lhs in inherit and rhs != '0' and rhs != '1'}
flag_sets = re.findall(r'has_country_flag = (\w+)\s*\}\s*set_temp_variable = \{ (\w+) = 1', capture)
snap = {lhs: donor.get(rhs, int(rhs) if rhs.isdigit() else 0) for lhs, rhs in assignments(capture) if lhs in inherit and rhs != '1'}
callers = ['cannibalism_create_unified_country_from_selected_host', 'cannibalism_absorb_current_warlord_into_unified_host', 'cannibalism_create_wendigo_unification_from_selected_hosts']
for caller in callers:
    for flag, output in flag_sets:
        expected = dict(snap, **{output: 1})
        retained = returned({n: 0 for n in prefix(after, caller)}, expected)
        check(caller + '_' + flag + '_capture_return', all(retained[n] == expected[n] for n in inherit), expected)
    lost = returned({n: 0 for n in prefix(before, caller)}, snap)
    check(caller + '_negative_control', any(n not in lost for n in inherit), 'Pre-repair source fails caller ownership under conservative cleanup.')

# Snapshot carries across country changes without assigning scoped temp tokens.
for apply in ['cannibalism_apply_inherited_host_identity_to_cbl', 'cannibalism_apply_absorbed_warlord_inheritance_to_unified_host']:
    check(apply + '_preserved', get(before, apply) == get(after, apply), 'Current route consumers and rewards unchanged.')
for caller in callers:
    ledger = meta['playerLedgerOutputs']
    ledger_capture = get(after, 'cannibalism_achievement_capture_current_player_ledger')
    source_counters = list(dict.fromkeys(v for n, v in assignments(ledger_capture) if n in ledger and not v.isdigit()))
    donor_counters = {v: (i + 1) * 17 for i, v in enumerate(source_counters)}
    # Projection fixture: human donor, every referenced achievement flag set,
    # and every referenced donor counter present. All conditional writes execute.
    writes = {n: int(v) if v.isdigit() else donor_counters[v] for n, v in assignments(ledger_capture) if n in ledger}
    retained = returned({n: 0 for n in prefix(after, caller)}, writes)
    check(caller + '_player_ledger_return', all(retained[n] == writes[n] for n in ledger), {'fixture': 'human donor with all referenced flags/counters present', 'sourceDefinedWrites': writes})

# Exercise both nested result boundaries using actual success/default assignments.
for outcome in ['0', '1']:
    for caller in ['cannibalism_absorb_current_warlord_into_unified_host', 'cannibalism_absorb_primary_warlord_donor_into_wendigo']:
        storage = {n: 0 for n in prefix(after, caller)}
        migration = get(after, 'cannibalism_migrate_runtime_references_to_unified_country')
        spread = get(after, 'cannibalism_migrate_spread_entries_between_countries')
        spread_values = [v for n, v in assignments(spread) if n == 'cannibalism_spread_migration_result']
        runtime_values = [v for n, v in assignments(migration) if n == 'cannibalism_runtime_migration_result']
        check('migration_assignment_' + caller + '_' + outcome, outcome in spread_values and outcome in runtime_values, 'Uses source-defined failure/success assignments. Queue validation is not emulated.')
        inner = dict(storage)
        inner.update({n: 0 for n in prefix(after, 'cannibalism_migrate_runtime_references_to_unified_country')})
        inner = returned(inner, {'cannibalism_spread_migration_result': int(outcome)})
        outer = returned(storage, {'cannibalism_runtime_migration_result': inner['cannibalism_spread_migration_result']})
        check('migration_return_' + caller + '_' + outcome, outer['cannibalism_runtime_migration_result'] == int(outcome), 'Nested failure and success retain their separate values after scope/helper return.')

wendigo = get(after, callers[2])
human = min((b for b in blocks(wendigo) if b['key'] == 'if' and 'cannibalism_inherited_larder = 0' in wendigo[b['start']:b['end']]), key=lambda b: b['end'] - b['start'])
human_body = wendigo[human['start']:human['end']]
check('both_human_preservation', all(x in human_body for x in ['cannibalism_primary_warlord_donor_was_human > 0', 'cannibalism_wendigo_merge_host_was_human > 0', 'cannibalism_primary_warlord_donor_can_be_absorbed = 0']), 'The exact both-human branch still clears inherited Larder and disables donor absorption after capture.')
storage = returned({n: 0 for n in prefix(after, callers[2])}, snap)
for n, v in assignments(human_body):
    storage[n] = int(v)
check('both_human_larder_return_projection', storage['cannibalism_inherited_larder'] == 0 and all(storage[n] == snap[n] for n in inherit if n != 'cannibalism_inherited_larder'), 'Only captured Larder is overridden. Local donor storage is untouched by these temp assignments.')

# Retain source guards, not claims that native annex/population/equipment executed.
triggers = (ROOT / 'common/scripted_triggers/014_cannibalism_triggers.txt').read_text(encoding='utf-8-sig')
gate = get(triggers, 'cannibalism_selected_unification_host_is_valid')
check('selected_host_generation_gate', all(x in gate for x in ['var = cannibalism_actor_generation', 'value = global.cannibalism_unification_host_generation', 'compare = equals']), 'Equal generation requirement rejects mismatched selected hosts in the source predicate. No runtime scenario was executed.')
for expected in [9, 10]:
    matched = project_compare(gate, 'cannibalism_actor_generation', {'cannibalism_actor_generation': 9, 'global.cannibalism_unification_host_generation': expected})
    check('selected_host_generation_projection_' + str(expected), matched == (expected == 9), 'Source equality accepts the matching generation and rejects the stale generation. Other eligibility conditions are not projected.')
for name in ['cannibalism_consume_current_state', 'cannibalism_set_consumption_parameters_from_context', 'cannibalism_prepare_current_warlord_slot_for_unification', 'cannibalism_absorb_primary_warlord_donor_into_wendigo']:
    for op in ['apply_exact_state_civilian_population_loss', 'add_equipment_to_stockpile', 'create_unit', 'annex_country']:
        check(name + '_' + op + '_count', get(before, name).count(op) == get(after, name).count(op), 'No extra native transfer or population call introduced.')
consume = get(after, 'cannibalism_consume_current_state')
check('duplicate_population_guard_preserved', all(x in consume for x in ['var = cannibalism_last_consumption_request_id', 'value = cannibalism_consumption_request_id', 'compare = greater_than_or_equals', 'constant:cannibalism_consumption_result.duplicate_request']), 'Duplicate-request branch and exact-loss output preallocation remain unchanged.')
for requested in [26, 27, 28]:
    duplicate = project_compare(consume, 'cannibalism_last_consumption_request_id', {'cannibalism_last_consumption_request_id': 27, 'cannibalism_consumption_request_id': requested})
    check('population_request_projection_' + str(requested), duplicate == (requested <= 27), 'Source request guard rejects replay and older IDs. Native population loss and callbacks are not executed.')
constants = (ROOT / 'common/script_constants/014_cannibalism_constants.txt').read_text(encoding='utf-8-sig')
applied = int(re.search(r'\bapplied\s*=\s*(\d+)', get(constants, 'cannibalism_consumption_result')).group(1))
anchor = returned({n: 0 for n in prefix(after, 'cannibalism_register_current_wendigo_anchor')}, {'cannibalism_consumption_result': applied, 'cannibalism_population_loss_applied': 17000})
check('anchor_population_return', anchor['cannibalism_consumption_result'] == applied and anchor['cannibalism_population_loss_applied'] == 17000, 'Nonzero population result survives the helper return using the source-defined applied result. Native loss/accounting not emulated.')
check('events_unmodified', not any(n in (ROOT / 'events/014_cannibalism.txt').read_text(encoding='utf-8-sig') for n in ['cannibalism_absorption_result', 'cannibalism_runtime_migration_result', 'cannibalism_wendigo_unification_result']), 'No owned caller return output is consumed in Event014 event definitions.')
report = dict(kind='actual-source bounded storage projection and preservation checks', engineEvidence=False, sourceSHA256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(), beforeSHA256=hashlib.sha256(PRIOR.read_bytes()).hexdigest(), parserReused=str(audit), checks=results, unsupported=['Complete event/helper/native execution', 'Entire spread validation and migration scenarios', 'Annex callbacks, technology union, population/deaths ledger, equipment transfer, focus selection and live multiplayer'], knownLimit='The destination-validity trigger has no actor/global generation equality check. Its predicate is preserved, and source-only storage repair does not prove rejection of every stale destination.')
(OUT / 'source_contract_checks.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(str(len(results)) + ' bounded actual-source checks passed. No engine or full transaction acceptance claimed.')
