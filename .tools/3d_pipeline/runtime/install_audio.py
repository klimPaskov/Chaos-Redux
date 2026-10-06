"""CAS-promote only measured, passing, licensed existing-recording candidates.

This applies mastering delivery only. Duplicate-source, take-count, state-loop
and semantic-role findings remain separate sound-package acceptance gates.
"""
import argparse
import json
from pathlib import Path
import shutil
import tempfile

from inventory import REPO
from pdx_reader import sha256


def install(batches, provenance, output, execute=False):
    approved = {row['source']: row for row in provenance['entries'] if row.get('eligible')}
    selected = {}
    for batch in batches:
        for row in batch['results']:
            if row.get('status') == 'staged':
                source = row.get('source_relative_path')
                if source in approved:
                    selected[source] = row
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    record = {'schema': 1, 'execute': execute, 'scope': 'mastering_only', 'selected_count': len(selected),
              'files': [], 'provenance_entries': approved,
              'package_acceptance': 'Source sharing, distinct takes, state logic and role suitability remain in their package reports.'}
    sound_root = (REPO / 'sound').resolve()
    # Validate the entire owned transaction before touching any runtime path.
    for relative, row in sorted(selected.items()):
        target = (REPO / relative).resolve()
        target.relative_to(sound_root)
        candidate = Path(row['destination_path']).resolve()
        candidate.relative_to(REPO / 'docs/plans/unit_fix_2026-10')
        if sha256(target) != row['source_sha256'] or sha256(candidate) != row['output_sha256']:
            raise ValueError('Audio source/staged bytes changed: ' + relative)
        if not all(value for key, value in row['checks'].items() if isinstance(value, bool)):
            raise ValueError('Audio candidate has a failed measurement check: ' + relative)
    for index, (relative, row) in enumerate(sorted(selected.items())):
        target = (REPO / relative).resolve()
        candidate = Path(row['destination_path']).resolve()
        entry = {'path': relative, 'before_sha256': row['source_sha256'], 'after_sha256': row['output_sha256'],
                 'role': row['role'], 'before': row['before'], 'after': row['after'],
                 'processing': row['processing'], 'provenance': approved[relative],
                 'candidate': candidate.relative_to(REPO).as_posix()}
        if execute:
            original = output / 'originals' / ('a{:03d}.wav'.format(index))
            if original.exists():
                raise FileExistsError('Audio install archive exists; this transaction is not replayed.')
            original.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, original)
            if sha256(original) != row['source_sha256'] or sha256(target) != row['source_sha256']:
                raise ValueError('Audio preimage changed immediately before replacement')
            with tempfile.NamedTemporaryFile(dir=target.parent, suffix='.wav', delete=False) as temp:
                temporary = Path(temp.name)
            try:
                shutil.copy2(candidate, temporary)
                if sha256(temporary) != row['output_sha256']:
                    raise ValueError('Audio candidate copy differs')
                temporary.replace(target)
            finally:
                if temporary.exists():
                    temporary.unlink()
            if sha256(target) != row['output_sha256']:
                raise ValueError('Installed audio differs')
            entry['archive'] = original.relative_to(REPO).as_posix()
        record['files'].append(entry)
        (output / 'manifest.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    return record


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--batch', type=Path, action='append', required=True)
    cli.add_argument('--provenance', type=Path, required=True)
    cli.add_argument('--output', type=Path, required=True)
    cli.add_argument('--execute', action='store_true')
    args = cli.parse_args()
    document = install([json.loads(path.read_text(encoding='utf-8-sig')) for path in args.batch],
                        json.loads(args.provenance.read_text(encoding='utf-8-sig')), args.output, args.execute)
    print(json.dumps({'selected': document['selected_count'], 'installed': len(document['files']) if args.execute else 0,
                      'scope': document['scope']}))
