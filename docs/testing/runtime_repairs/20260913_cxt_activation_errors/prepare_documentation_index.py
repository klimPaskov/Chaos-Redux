"""Project only the owned technology and queue documentation into the Git index."""
from pathlib import Path
import difflib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
name = 'docs/testing/chaosx_test_country.md'
head = subprocess.check_output(['git', 'show', 'HEAD:' + name], cwd=ROOT).decode('utf-8-sig').replace('\r\n', '\n')
current = (ROOT / name).read_text(encoding='utf-8-sig')
old = "The technology helper enumerates `global.technology` and injects each object's documented `GetTokenKey` into native `has_tech` and `set_technology` fields through `meta_effect`, with `popup = no`."
new = 'The technology helper captures `global.technology^num`, reads every zero-based index below that count explicitly, and passes each database object to native `var:` technology fields with `popup = no`.\nAn empty database produces no technology reads, and the numeric loop has its own initialized break variable.\nTemporary `CXT_TECH_DIAGNOSTIC` output records the count, index, numeric value, and token text; the supplied error report does not include those values, so runtime error elimination remains unverified.'
assert head.count(old) == 1 and current.count(new) == 1
projected = head.replace(old, new, 1)
anchor = 'Core and registered project grants are idempotent and use `chaosx_test_country_silent_unlocks` to suppress completion reports while retaining their gameplay outputs.'
addition = "Project condemnation gains remain in CXT's country record during dormant history setup; participant calculations and pulse scheduling wait until it has an owned capital.\nInitialization and the existing registered-content bus flush the queued requests after activation, so scoring has valid capital and initialized-country scopes without repeating project completion."
assert head.count(anchor) == current.count(anchor) == 1 and current.count(addition) == 1
projected = projected.replace(anchor, anchor + '\n' + addition, 1)
patch = ''.join(difflib.unified_diff(head.splitlines(True), projected.splitlines(True), fromfile='a/' + name, tofile='b/' + name))
(QA / 'documentation_index.patch').write_bytes(patch.encode('utf-8'))
receipt = {'path': name, 'owned_changes': ['runtime indexed technology delivery and explicit unverified result', 'dormant condemnation queue and activation flush'], 'unrelated_working_tree_documentation_preserved': projected != current}
(QA / 'documentation_scope.json').write_bytes((json.dumps(receipt, indent=2) + '\n').encode('utf-8'))
print('Prepared only the two owned documentation changes; other draft content stays outside this commit.')
