"""Build a task-only documentation patch without staging unrelated local prose."""
from pathlib import Path
import difflib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
patches = []
inventory = {}
for name in ('docs/testing/chaosx_test_country.md', 'common/scripted_effects/chaosx_dynamic_effects.md'):
    head = subprocess.check_output(['git', 'show', 'HEAD:' + name], cwd=ROOT).decode('utf-8-sig').replace('\r\n', '\n')
    working = (ROOT / name).read_text(encoding='utf-8-sig')
    if name.startswith('docs/'):
        start = working.index('Core and registered project callers pass an `sp:<project_id>` scope')
        end = working.index('The country adopts the Chaos Warfare grand doctrine', start)
        addition = working[start:end]
        anchor = 'The country adopts the Chaos Warfare grand doctrine'
    else:
        addition = next(line + '\n' for line in working.splitlines() if line.startswith('| `test_country_facilities_and_projects`'))
        anchor = '| `independence_wave_ledger`'
    assert head.count(anchor) == 1
    assert addition not in head
    candidate = head.replace(anchor, addition + anchor, 1)
    patches.extend(difflib.unified_diff(head.splitlines(True), candidate.splitlines(True), fromfile='a/' + name, tofile='b/' + name))
    inventory[name] = {'staged_addition_lines': len(addition.splitlines()), 'unrelated_local_prose_included': False, 'technology_investigation_wording_included': False}
(QA / 'documentation_index.patch').write_bytes(''.join(patches).encode('utf-8'))
(QA / 'documentation_index_scope.json').write_text(json.dumps(inventory, indent=2) + '\n', encoding='utf-8')
print(json.dumps(inventory))
