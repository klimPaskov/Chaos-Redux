#!/usr/bin/env python3
"""Validate the planning artifact only. This does not run HOI4 or specialist audits."""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path

PREFIX = '095_occupation_revolt_'
ROOT = Path(__file__).resolve().parent


def read_json(name: str):
    return json.loads((ROOT / (PREFIX + name + '.json')).read_text(encoding='utf-8'))


def main() -> int:
    checks: list[dict[str, object]] = []

    def check(name: str, success: bool, detail: str) -> None:
        checks.append({'check': name, 'status': 'PASS' if success else 'FAIL', 'detail': detail})

    parts = sorted(ROOT.glob(PREFIX + 'spec_part_*.md'))
    numbers = [int(re.search(r'part_(\d+)', p.name).group(1)) for p in parts]
    check('Fourteen consecutive specification parts', numbers == list(range(1, 15)), str(numbers))
    names = ['asset', 'achievement', 'decision_mission', 'super_event', 'coding', 'goal']
    check('Six required prompts', all((ROOT / f'{PREFIX}{n}_prompt.md').is_file() for n in names), ', '.join(names))
    goal = (ROOT / (PREFIX + 'goal_prompt.md')).read_text(encoding='utf-8')
    check('Goal character limit', 3500 <= len(goal) <= 4000, f'{len(goal)} characters, including heading and trailing newline')

    requirements = read_json('requirement_coverage')
    check('36 original gameplay coverage rows', len(requirements) == 36 and len({r['id'] for r in requirements}) == 36, str(len(requirements)))
    missing = [p for row in requirements for p in row['specification_files'] if not (ROOT / p).is_file()]
    check('Coverage references resolve', not missing, json.dumps(missing))
    check('No implementation claim in coverage', all(r['implementation_status'] == 'NOT_IMPLEMENTED' for r in requirements), 'Design coverage remains separate')
    cases = read_json('validation_scenarios')
    check('97 planned unique scenarios', len(cases) == 97 and len({r['id'] for r in cases}) == 97, str(len(cases)))
    check('Runtime tests remain NOT_RUN', all(r['runtime_status'] == 'NOT_RUN' for r in cases), 'No engine or live-test execution claimed')
    roles = read_json('specialist_execution_status')
    check('20 unique role assignments', len(roles) == 20 and len({r['role'] for r in roles}) == 20, str(len(roles)))
    check('Assignments exist and are unexecuted', all((ROOT / r['assignment']).is_file() and r['status'] == 'NOT_EXECUTED' and r['actual_run_id'] is None for r in roles), 'Prepared prompts are not runs')
    assets = read_json('asset_coverage_matrix')
    check('49 distinct asset-family rows', len(assets) == 49 and len({r['id'] for r in assets}) == 49, str(len(assets)))
    check('Six achievement triplet families', sum(r['family'] == 'Achievement triplet' for r in assets) == 6, '18 required final icons, none produced')

    inventory = read_json('source_inventory')
    archive = ROOT / 'source_snapshot' / 'all-project-sources(20261005-165144).zip'
    raw = archive.read_bytes()
    expected = '0f13352a0bbf4c657fcb82ac6ec549a1ac208f2624b23489c25dc9bd85105d3e'
    check('Original archive unchanged', hashlib.sha256(raw).hexdigest() == expected, expected)
    source_bytes: dict[str, bytes] = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as outer:
        for entry in outer.infolist():
            if entry.is_dir():
                continue
            data = outer.read(entry)
            if entry.filename == 'subagents.zip':
                with zipfile.ZipFile(io.BytesIO(data)) as inner:
                    for nested in inner.infolist():
                        if not nested.is_dir():
                            source_bytes['subagents/' + Path(nested.filename).name] = inner.read(nested)
            else:
                source_bytes[entry.filename] = data
    check('46 supplied source entries', len(inventory) == len(source_bytes) == 46, f'{len(inventory)} inventory / {len(source_bytes)} archive')
    source_errors = []
    for row in inventory:
        data = source_bytes.get(row['path'])
        if data is None or len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
            source_errors.append(row['path'])
    check('Every source byte count and hash matches', not source_errors, json.dumps(source_errors))
    check('Recorded source total', sum(r['lines'] for r in inventory) == 15017 and sum(r['bytes'] for r in inventory) == 1337172, '15,017 recorded physical lines / 1,337,172 bytes')
    source_agents = {Path(p).stem for p in source_bytes if p.startswith('subagents/')}
    check('Assignments match supplied roles exactly', source_agents == {r['role'] for r in roles}, ', '.join(sorted(source_agents)))
    supplied_skills = [p for p in source_bytes if p.startswith('chaos-redux-') and p.endswith('.md')]
    check('17 supplied skills', len(supplied_skills) == 17, str(len(supplied_skills)))

    broken: list[str] = []
    for path in ROOT.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^\s]+?)(?:\s+"[^"]*")?\)', text):
            if ref.startswith(('https:', 'http:', 'mailto:', '#')):
                continue
            target = ref.split('#')[0]
            if target and not (path.parent / target).is_file():
                broken.append(str(path.relative_to(ROOT)) + ': ' + ref)
    check('All local Markdown links resolve', not broken, json.dumps(broken))
    prohibited = [str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in {'.dds', '.tga', '.ttf', '.otf', '.xlsx', '.csv', '.wav'}]
    check('No loose runtime, font or catalog files', not prohibited, json.dumps(prohibited))
    manifest_file = ROOT / (PREFIX + 'package_manifest.json')
    if manifest_file.exists():
        manifest = json.loads(manifest_file.read_text(encoding='utf-8'))
        mismatch = []
        for entry in manifest['files']:
            path = ROOT / entry['path']
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
                mismatch.append(entry['path'])
        listed = {r['path'] for r in manifest['files']}
        actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p != manifest_file}
        check('Manifest hashes and membership match', not mismatch and listed == actual, json.dumps(mismatch))
    else:
        check('Manifest exists', False, 'Final packaging must create the manifest')

    result = {'artifact_validation_only': True, 'checks': checks, 'passed': all(r['status'] == 'PASS' for r in checks), 'runtime_validation': 'NOT_RUN', 'isolated_agents_executed': 0}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        print(f'Package validation could not finish: {exc}', file=sys.stderr)
        sys.exit(2)
