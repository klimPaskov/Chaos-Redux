"""Build a reviewable existing-recording batch from installed unit consumers.

An exact existing attribution row supplies the source/creator/license link.
The captured runtime preimage hash is labelled as a derivative, not an original
recording hash. Missing attribution is reported and never invented.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import subprocess
import tempfile

from inventory import REPO, index_assets, walk
from pdx_reader import sha256

LICENSE = re.compile(r'CC[ -]*(?:BY(?:[ -]*SA)?|0)|public domain|creativecommons\.org/(?:publicdomain|licenses/by)', re.I)


def build(inventory):
    by_path = {}
    for model in inventory['models']:
        for cue in model['sound_cues']:
            for sample in cue['samples']:
                record = sample.get('file')
                if not record or not record['path'].startswith('sound/'):
                    continue
                row = by_path.setdefault(record['path'], {'file': record, 'units': [], 'cues': []})
                row['units'].append(model['pdxmesh'].removesuffix('_mesh'))
                row['cues'].append({'name': cue['name'], 'loop': cue['loop'] == 'yes'})
    # Include selection and order cues in those exact unit directories.
    sounds, effects = index_assets()[3:5]
    directories = {str(Path(path).parent) for path in by_path}
    for effect_name, effect in effects.items():
        for node in walk(effect['node']):
            if node.key != 'sound' or not isinstance(node.value, str) or node.value not in sounds:
                continue
            value = sounds[node.value]['node'].scalar('file')
            if not value:
                continue
            canonical = value.replace('\\', '/')
            if not canonical.startswith('sound/'):
                canonical = 'sound/' + canonical
            if str(Path(canonical).parent) not in directories or not (REPO / canonical).is_file():
                continue
            if canonical not in by_path:
                related = next(row for path, row in by_path.items() if Path(path).parent == Path(canonical).parent)
                by_path[canonical] = {'file': {'path': canonical, 'sha256': sha256(REPO / canonical)},
                                     'units': list(set(related['units'])), 'cues': []}
            by_path[canonical]['cues'].append({'name': effect_name, 'loop': effect['node'].scalar('loop') == 'yes'})
    basenames = {Path(path).name.casefold() for path in by_path}
    documents = []
    with tempfile.TemporaryDirectory(prefix='chaosx_audio_attribution_') as search_dir:
        pattern_file = Path(search_dir) / 'runtime_names.txt'
        pattern_file.write_text('\n'.join(sorted(basenames)), encoding='utf-8')
        matches = subprocess.run(['rg', '--no-ignore', '-l', '-i', '-F', '-f', str(pattern_file),
                                  '-g', '*.md', '-g', '*.json',
                                  '-g', '!**/unit_fix_2026-10/**',
                                  str(REPO / 'docs'), str(REPO / 'sound')],
                                 capture_output=True, text=True, encoding='utf-8', check=False)
        if matches.returncode not in {0, 1}:
            raise RuntimeError('Attribution rg search failed: ' + matches.stderr)
    for value in matches.stdout.splitlines():
        path = Path(value)
        if 'unit_fix_2026-10' in path.parts:
            continue
        if path.stat().st_size > 2000000:
            continue
        text = path.read_text(encoding='utf-8-sig', errors='replace')
        if not LICENSE.search(text):
            continue
        lowered = text.casefold()
        found = [name for name in basenames if name in lowered]
        if found:
            documents.append((path, text.splitlines(), set(found), len(text)))
    entries, unresolved = [], []
    for path, row in sorted(by_path.items()):
        filename = Path(path).name.casefold()
        candidates = []
        for doc, lines, names, length in documents:
            if filename not in names:
                continue
            for index, line in enumerate(lines):
                if filename in line.casefold():
                    if re.search(r'CC[ -]*BY[ -]*NC', line, re.I):
                        continue
                    nearby_license = LICENSE.search(line) is not None
                    preference = 0 if nearby_license and re.search(r'https?://', line) else 1 if 'attribution' in doc.name.casefold() else 2
                    candidates.append((preference, length, str(doc), index + 1, line))
        if not candidates:
            unresolved.append({'path': path, 'units': sorted(set(row['units'])), 'reason': 'missing exact attributable recording row'})
            continue
        _, _, doc, line_no, source_row = min(candidates)
        name = filename.lower()
        loop = any(cue['loop'] for cue in row['cues']) or any(token in name for token in ('_loop', '_ambient', '_idle', '_breath'))
        step = any(token in name for token in ('footstep', '_step', '_foot_', 'footfall')) or name.endswith(('_move.wav', '_movement.wav'))
        role = 'loop' if loop else 'step' if step else 'shot'
        entries.append({'source': path, 'sha256': row['file']['sha256'],
                        'unit_id': sorted(set(row['units']))[0], 'consumer_units': sorted(set(row['units'])),
                        'soundeffect': row['cues'][0]['name'] if row['cues'] else 'unresolved',
                        'consumer_cues': row['cues'], 'role': role, 'subsonic': False,
                        'attribution': {'manifest_path': Path(doc).relative_to(REPO).as_posix(),
                                        'source_sha256': row['file']['sha256'],
                                        'hash_scope': 'installed licensed derivative preimage, not untouched original recording',
                                        'source_row': source_row, 'source_line': line_no}})
    for index, entry in enumerate(entries):
        entry['output'] = 'a{:03d}.wav'.format(index)
    return {'schema': 1, 'inventory_path': 'docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json',
            'entries': entries, 'unresolved': unresolved, 'family_pools': [],
            'role_policy': 'existing loop or idle/ambient/breath filename -> loop; foot/step/move filename -> step; other unit cue -> shot; parent-reviewed before staging',
            'provenance_limit': 'Existing attribution inherited; no original recording SHA or restored unclipped source is claimed.'}


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--inventory', type=Path, required=True)
    cli.add_argument('--output', type=Path, required=True)
    args = cli.parse_args()
    document = build(json.loads(args.inventory.read_text(encoding='utf-8')))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'entries': len(document['entries']), 'unresolved': len(document['unresolved']), 'output': str(args.output)}))
