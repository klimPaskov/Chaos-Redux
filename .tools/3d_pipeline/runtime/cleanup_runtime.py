"""Archive and remove only hash-bound, globally unreferenced unit binaries.

Dry-run is the default. Active consumers and embedded mesh references are
re-read before any deletion; shader overrides or clone variants cannot be
mistaken for unused files. Every target stays inside gfx/models/units.
"""
import argparse
import json
from pathlib import Path
import shutil

from inventory import REPO, snapshot
from pdx_reader import sha256


def cleanup(output, execute=False):
    data = snapshot()
    active = {item['path'] for item in data['files']}
    embedded = {str(Path(model['mesh']['path']).parent / name)
                for model in data['models'] if model['mesh'] for name in model['embedded_texture_names']}
    candidates = {item['path']: item for model in data['models'] for item in model['unreferenced_files']
                  if item['path'] not in active and item['path'] not in embedded}
    result = {'schema': 1, 'execute': execute, 'removed': [], 'candidates': list(candidates.values()),
              'policy': 'global active consumers plus embedded binary references, not per-model directory guesses'}
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    root = (REPO / 'gfx/models/units').resolve()
    for relative, item in sorted(candidates.items()):
        target = (REPO / relative).resolve()
        target.relative_to(root)
        if sha256(target) != item['sha256']:
            raise ValueError('Unreferenced target changed before cleanup: ' + relative)
        if execute:
            archive = output / 'originals' / item['sha256'][:12] / target.name
            archive.parent.mkdir(parents=True, exist_ok=True)
            if archive.exists():
                if sha256(archive) != item['sha256']:
                    raise ValueError('Existing cleanup archive differs')
            else:
                shutil.copy2(target, archive)
            if sha256(archive) != item['sha256'] or sha256(target) != item['sha256']:
                raise ValueError('Cleanup source/archive differs')
            target.unlink()
            result['removed'].append({**item, 'archive': archive.relative_to(REPO).as_posix()})
    (output / 'manifest.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--output', type=Path, required=True)
    cli.add_argument('--execute', action='store_true')
    args = cli.parse_args()
    result = cleanup(args.output, args.execute)
    print(json.dumps({'candidates': len(result['candidates']), 'removed': len(result['removed']),
                      'bytes': sum(row['bytes'] for row in result['removed'])}))
