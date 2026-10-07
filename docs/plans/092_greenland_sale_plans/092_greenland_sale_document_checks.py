#!/usr/bin/env python3
"""Check delivered documents and source-byte integrity, not HOI4 correctness.

Run in either the delivered sibling-folder layout or after placing the folders
under docs/specs and docs/plans. No external packages or network calls are used.
Reading-range checks verify the recorded coverage structure, not human/model
comprehension. Hashes are identity evidence and do not replace full-text reading.
"""
from pathlib import Path
import hashlib
import io
import json
import re
import sys
import zipfile

P = Path(__file__).resolve().parent
S = P.parent / '092_greenland_sale_specs'
if not S.is_dir():
    S = P.parent.parent / 'specs' / '092_greenland_sale_specs'
if not S.is_dir():
    raise SystemExit('Cannot locate the accompanying 092_greenland_sale_specs folder.')

records = []

def check(name, condition, detail):
    records.append({'check': name, 'status': 'PASS' if condition else 'FAIL', 'detail': detail})


def sha(data):
    return hashlib.sha256(data).hexdigest()

parts = sorted(S.glob('*_spec_part_*.md'))
check('13 complete numbered parts', len(parts) == 13 and
      [int(re.search(r'part_(\d+)', p.name).group(1)) for p in parts] == list(range(1,14)),
      'Checks the presence and numbering of all 13 main specification files.')
check('Substantive part bodies', all(len(p.read_text(encoding='utf-8').split()) >= 600 for p in parts),
      'Each part contains at least 600 whitespace-separated words. This is a size check, not a quality proof.')
needed_prompts = ['asset', 'achievement', 'decision_mission', 'coding', 'goal']
check('All five production prompts', all((S/f'092_greenland_sale_{x}_prompt.md').is_file() for x in needed_prompts),
      ', '.join(needed_prompts))
goal_len = len((S/'092_greenland_sale_goal_prompt.md').read_text(encoding='utf-8'))
check('Goal prompt character limit', 3500 <= goal_len <= 4000,
      f'{goal_len} Unicode characters, including final newline.')
check('Two folder indexes', (S/'092_greenland_sale_spec_index.md').is_file() and
      (P/'092_greenland_sale_plans_index.md').is_file(), 'Both event-folder indexes exist.')

mds = list(S.glob('*.md')) + list(P.glob('*.md'))
broken = []
output_name = '092_greenland_sale_document_check_results.json'
for p in mds:
    text = p.read_text(encoding='utf-8')
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if link.startswith(('https:', 'http:', '#', 'mailto:')):
            continue
        target = (p.parent / link.split('#')[0]).resolve()
        # This exact result file is emitted after all checks finish.
        if not target.exists() and target != P/output_name:
            broken.append(f'{p.name}: {link}')
check('Internal Markdown file links', not broken, broken or 'All relative file targets resolve.')
check('Authored Markdown prose style', all('—' not in p.read_text(encoding='utf-8') and
      ';' not in p.read_text(encoding='utf-8') for p in mds),
      'No em dash or semicolon characters in the authored Markdown files.')
check('No unfinished part markers', not any(re.search(r'(?mi)^\s*(TODO|TBD|PLACEHOLDER)\b',
      p.read_text(encoding='utf-8')) for p in parts),
      'No leading TODO/TBD/PLACEHOLDER markers in the main parts. Open validation gates remain explicit elsewhere.')

ledger = json.loads((P/'092_greenland_sale_supplied_source_read_ledger.json').read_text(encoding='utf-8'))
ranges = json.loads((P/'092_greenland_sale_supplied_source_read_ranges.json').read_text(encoding='utf-8'))
archive = P/'092_greenland_sale_supplied_sources_original.zip'
check('Original archive byte identity', sha(archive.read_bytes()) == ledger['archive_sha256'],
      ledger['archive_sha256'])
source_bytes = {}
with zipfile.ZipFile(archive) as z:
    archive_crc = z.testzip()
    for name in z.namelist():
        if name.endswith('/'):
            continue
        if name == 'subagents.zip':
            with zipfile.ZipFile(io.BytesIO(z.read(name))) as nested:
                nested_crc = nested.testzip()
                for n in nested.namelist():
                    if not n.endswith('/'):
                        source_bytes['subagents/' + n] = nested.read(n)
        else:
            source_bytes[name] = z.read(name)
check('Original and nested ZIP integrity', archive_crc is None and nested_crc is None,
      'CRC checks pass for both preserved archive containers.')
file_rows = ledger['files']
check('46 source identities', len(source_bytes) == len(file_rows) == 46 and
      set(source_bytes) == {f['path'] for f in file_rows} and
      all(sha(source_bytes[f['path']]) == f['sha256'] for f in file_rows),
      'All recorded source-file hashes match the preserved archive, including all nested role TOMLs.')
coverage_ok = True
for f in file_rows:
    expected = 1
    for start, end in f['read_line_ranges']:
        if start != expected or end < start:
            coverage_ok = False
        expected = end + 1
    if expected != f['lines'] + 1:
        coverage_ok = False
check('Recorded full line coverage', coverage_ok,
      'Every recorded file range is contiguous from line 1 to its recorded final line. This does not substitute for reading.')
check('109 unique full-text chunk records', len(ranges) == len({r['chunk'] for r in ranges}) == 109 and
      sum(r['characters'] for r in ranges) == ledger['total_characters_in_read_chunks'] == 1265078,
      '109 unique chunk identities, totaling 1,265,078 recorded characters.')
role_names = {f['path'].split('/')[-1].removesuffix('.toml') for f in file_rows if f['path'].endswith('.toml') and f['path'].startswith('subagents/')}
roles_text = (P/'092_greenland_sale_role_handoffs.md').read_text(encoding='utf-8')
check('All 20 supplied roles accounted for', len(role_names) == 20 and all(f'`{r}`' in roles_text for r in role_names),
      'Definitions read and applicability recorded, with no claim of actual subagent execution.')
abstract = json.loads((P/'092_greenland_sale_design_check_results.json').read_text(encoding='utf-8'))
check('Recorded abstract test result', abstract['cases_run'] == abstract['passed'] == 32 and
      abstract['failures'] == abstract['errors'] == 0, '32 abstract cases passed. Native validation remains unperformed.')
matrix = (P/'092_greenland_sale_validation_matrix.md').read_text(encoding='utf-8')
native_rows = re.findall(r'^\| N\d+ .*$', matrix, re.M)
check('Native test status is explicit', len(native_rows) == 54 and all('| Not run |' in row for row in native_rows),
      '54 native fixtures remain Not run, rather than inheriting the abstract results.')

payload = {
    'scope': 'Document integrity and recorded evidence checks only. Not source-comprehension, subagent, engine or production validation.',
    'checks_run': len(records),
    'passed': sum(r['status'] == 'PASS' for r in records),
    'failed': sum(r['status'] == 'FAIL' for r in records),
    'main_specification_words': sum(len(p.read_text(encoding='utf-8').split()) for p in parts),
    'goal_prompt_characters': goal_len,
    'checks': records,
}
(P/output_name).write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
print(json.dumps(payload, indent=2))
sys.exit(1 if payload['failed'] else 0)
