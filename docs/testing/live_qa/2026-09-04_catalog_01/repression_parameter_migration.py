"""Bounded, guarded migration for the accepted repression parameter repair."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
BACKUP = QA / 'pre_patch_repression_parameters'
EVIDENCE = QA / 'repression_parameter_evidence'
FILES = {
    'common/decisions/camp_repression_generic_decisions.txt': 12,
    'common/scripted_effects/camp_repression_action_dispatcher_effects.txt': 14,
    'common/scripted_effects/camp_repression_rework_effects.txt': 12,
    'common/scripted_effects/camp_repression_site_cost_effects.txt': 5,
    'common/scripted_triggers/camp_repression_site_cost_triggers.txt': 5,
    'common/scripted_guis/camp_repression_ledger_scripted_gui.txt': 6,
    'common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt': 6,
    'common/scripted_localisation/camp_repression_site_cost_scripted_localisation.txt': 54,
}
DOC = 'common/scripted_effects/camp_repression_site_cost_effects.md'
PROTECTED = ['common/script_constants/camp_repression_site_cost_constants.txt', 'interface/camp_repression_ledger.gui']
CALL = re.compile(r'(?P<helper>camp_rework_prepare_site_cost_quote|camp_rework_(?:can_pay|pay)_site_\w+)\s*=\s*\{\s*STATE\s*=\s*(?P<state>[^}\s]+)\s*\}')
TOKEN = re.compile(r'"(?:\\.|[^"\\])*"|[^\s={}<>]+|[={}<>]')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8')

def tokens(text):
    return TOKEN.findall(re.sub(r'#[^\r\n]*', '', text))

def migrate(text, path):
    rows = []
    output = []
    for n, line in enumerate(text.splitlines(keepends=True), 1):
        matches = list(CALL.finditer(line))
        assert len(matches) < 2, (path, n)
        if not matches:
            output.append(line)
            continue
        m = matches[0]
        helper, state = m['helper'], m['state']
        row = dict(line=n, helper=helper, state=state, original=m.group())
        if state == '$STATE$':
            changed = line[:m.start()] + helper + ' = yes' + line[m.end():]
            row['input'] = 'inherited'
        else:
            value = {'FROM': 'FROM.id', 'var:camp_selected_state_id': 'camp_selected_state_id', 'var:camp_rework_action_state_id': 'camp_rework_action_state_id'}[state]
            init = 'set_temp_variable = { camp_site_cost_state_id = ' + value + ' }'
            row['input'] = value
            if path.endswith('camp_repression_ledger_scripted_localisation.txt'):
                old = 'NOT = { ' + m.group() + ' }'
                assert old in line, (path, n)
                changed = line.replace(old, init + ' NOT = { ' + helper + ' = yes }', 1)
                row['negative'] = True
            else:
                prefix = line[:m.start()]
                sep = ('\r\n' if '\r\n' in line else '\n') + prefix if not prefix.strip() else ' '
                changed = prefix + init + sep + helper + ' = yes' + line[m.end():]
            row['initializer'] = init
        row['before_line'] = line
        row['after_line'] = changed
        rows.append(row)
        output.append(changed)
    new = ''.join(output)
    if path.endswith('camp_repression_site_cost_triggers.txt'):
        assert new.count('$STATE$') == 1
        new = new.replace('$STATE$', 'var:camp_site_cost_state_id')
        new = new.replace('# Country scope; STATE is an explicit state scope (FROM or var:camp_selected_state_id).', '# Country scope. Required input: unscoped temporary camp_site_cost_state_id.')
    if path.endswith('camp_repression_site_cost_effects.txt'):
        new = new.replace('# STATE is the explicit state used by the matching quote and gate; never inferred.', '# Required input: unscoped temporary camp_site_cost_state_id, matching the quote and gate.')
    assert len(rows) == FILES[path], (path, len(rows))
    restored = new.replace('var:camp_site_cost_state_id = {', '$STATE$ = {')
    for row in rows:
        assert row['after_line'] in restored, (path, row['line'])
        restored = restored.replace(row['after_line'], row['before_line'], 1)
    assert tokens(restored) == tokens(text), 'Unexpected semantic change: ' + path
    return new, rows

def migrate_doc(text):
    text = text.replace('`camp_rework_prepare_site_cost_quote = { STATE = <state scope> }`', '`camp_rework_prepare_site_cost_quote = yes`')
    text = text.replace('The GUI passes `STATE = var:camp_selected_state_id`, decisions pass `STATE = FROM`, and execution passes the validated selected/action state.', 'Every external caller immediately initializes the required unscoped temporary `camp_site_cost_state_id` before the boolean helper call.\nThe GUI copies `camp_selected_state_id`, targeted decisions and their localisation copy `FROM.id`, and dispatcher execution copies `camp_rework_action_state_id`.\nOnly the quote calculator enters `var:camp_site_cost_state_id` to read building levels.\nAffordability and payment retain the original country scope as payer.\nNested helper calls forward the initialized temporary without replacing it, and payment callers initialize it again after the execution guard.\nThere is no default target, persistent input cache, or global event target.\nFor a negated affordability predicate, initialize the input outside `NOT` so the condition retains its meaning.')
    text = text.replace('camp_rework_prepare_site_cost_quote = { STATE = var:camp_selected_state_id }', 'set_temp_variable = { camp_site_cost_state_id = camp_selected_state_id }\ncamp_rework_prepare_site_cost_quote = yes')
    text = text.replace('take the same `STATE` parameter in country scope.', 'use boolean `= yes` calls in country scope and consume the required `camp_site_cost_state_id` temporary input.')
    text = text.replace('They take `STATE`, initialize retained temporary outputs, recompute the same quote, negate separate scratch amounts, and debit each quoted resource once.', 'They consume `camp_site_cost_state_id`, initialize retained temporary outputs, recompute the same quote, negate separate scratch amounts, and debit each quoted resource once.')
    assert 'STATE =' not in text and 'take `STATE`' not in text
    return text

if __name__ == '__main__':
    if sys.argv[1] == 'prepare':
        assert not BACKUP.exists(), 'Refuse to overwrite earlier backup'
        BACKUP.mkdir(parents=True)
        EVIDENCE.mkdir(exist_ok=True)
        manifest = {'files': [], 'protected': [], 'calls': {}}
        # Read the complete live transaction before creating any candidate.
        originals = {p: (ROOT / p).read_bytes() for p in [*FILES, DOC, *PROTECTED]}
        for path, data in originals.items():
            target = BACKUP / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            assert target.read_bytes() == data
            if path in PROTECTED:
                manifest['protected'].append({'path': path, 'sha256': sha(data)})
                continue
            text = data.decode('utf-8')
            if path in FILES:
                candidate, rows = migrate(text, path)
                manifest['calls'][path] = rows
            else:
                candidate = migrate_doc(text)
            encoded = candidate.encode('utf-8')
            dest = EVIDENCE / 'candidates' / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(encoded)
            manifest['files'].append({'path': path, 'before_sha256': sha(data), 'candidate_sha256': sha(encoded)})
        assert sum(map(len, manifest['calls'].values())) == 114
        dump(EVIDENCE / 'migration_manifest.json', manifest)
        print('Prepared and backed up 9 files, 114 calls. Gameplay source unchanged.')
    elif sys.argv[1] == 'apply':
        manifest = json.loads((EVIDENCE / 'migration_manifest.json').read_text())
        for item in manifest['files']:
            assert sha((ROOT / item['path']).read_bytes()) == item['before_sha256'], 'Concurrent edit: ' + item['path']
        written = []
        try:
            for item in manifest['files']:
                path = item['path']
                data = (EVIDENCE / 'candidates' / path).read_bytes()
                assert sha(data) == item['candidate_sha256']
                assert sha((ROOT / path).read_bytes()) == item['before_sha256'], 'Concurrent edit: ' + path
                (ROOT / path).write_bytes(data)
                written.append(item)
                assert sha((ROOT / path).read_bytes()) == item['candidate_sha256']
            dump(EVIDENCE / 'application.json', {'status': 'applied', 'files': written, 'recovery': 'Not needed. Verified byte backups retained.'})
        except Exception:
            restored = []
            for item in written:
                path = item['path']
                if sha((ROOT / path).read_bytes()) == item['candidate_sha256']:
                    (ROOT / path).write_bytes((BACKUP / path).read_bytes())
                    restored.append(path)
            dump(EVIDENCE / 'application.json', {'status': 'failed', 'safely_restored': restored})
            raise
        print('Applied 9 guarded file writes. All candidate hashes verified.')
