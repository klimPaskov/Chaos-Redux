"""Re-encode and verify one reviewed local repair without rerunning a batch."""
import argparse
import copy
import json
from pathlib import Path
import sys

from inventory import REPO
from pdx_reader import sha256
PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
from textures.delivery import prepare_batch, convert_batch


def accept(path, proof_path):
    manifest = json.loads(path.read_text(encoding='utf-8'))
    proof = json.loads(proof_path.read_text(encoding='utf-8'))
    already_reviewed = manifest.get('reviewed_repair', {}).get('item') == 't062'
    if not already_reviewed and sha256(path) != proof['parent_manifest_sha256_before']:
        raise ValueError('Parent manifest changed after repair review')
    item = next(row for row in manifest['items'] if row['id'] == 't062')
    if item['source_sha256'] != proof['source_sha256'] or sha256(REPO / proof['repair_dds_rel']) != proof['repair_dds_sha256']:
        raise ValueError('Repair source or output differs from reviewed bytes')
    directory = path.parent / 'verified_t062'
    if already_reviewed:
        converted = item['converted']
        if converted['stage_dds_sha256'] != proof['repair_dds_sha256'] or sha256(REPO / converted['stage_dds_rel']) != proof['repair_dds_sha256']:
            raise ValueError('Previously reviewed repair changed')
        for key in ('stage_dds_rel', 'prepared_png_rel', 'qa_report_rel', 'source_archive_rel'):
            item[key] = converted[key]
        path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
        return {'state': manifest['state'], 'items': len(manifest['items']), 'repair_manifest_paths_reconciled': True}
    directory.mkdir()
    request = {'batch_id': manifest['batch_id'] + '_verified_t062', 'items': [{key: item[key] for key in
        ('id', 'source_rel', 'target_rel', 'role', 'occupancy_mask_rel', 'dilation_px', 'conversion_scope', 'alpha_used', 'expected_target_sha256')}]}
    request['items'][0]['size'] = item['output_size']
    request_path = directory / 'request.json'
    request_path.write_text(json.dumps(request, indent=2) + '\n', encoding='utf-8')
    repaired_manifest_path = directory / 'manifest.json'
    prepare_batch(REPO, request_path, directory / 'stage', repaired_manifest_path)
    repaired = convert_batch(REPO, repaired_manifest_path, execute=True)
    if not repaired['install']['install_eligible']:
        raise RuntimeError('Recomputed repair fails unchanged delivery gates')
    converted = repaired['items'][0]['converted']
    if converted['stage_dds_sha256'] != proof['repair_dds_sha256']:
        raise RuntimeError('Independent repair encoding differs from reviewed artifact')
    before = copy.deepcopy(item['converted'])
    item['converted'] = converted
    for key in ('stage_dds_rel', 'prepared_png_rel', 'qa_report_rel', 'source_archive_rel'):
        item[key] = converted[key]
    item['status'] = 'converted'
    if not all(row['converted']['qa']['install_eligible'] for row in manifest['items']):
        raise RuntimeError('Another batch item remains ineligible')
    manifest['state'] = 'staged'
    manifest['conversion'].update(status='passed', failures=[], native_encoder_version='mixed 1.1.0 + t062 mip7 1.2.0')
    manifest['install'].update(status='ready', install_eligible=True)
    manifest['reviewed_repair'] = {'item': 't062', 'proof': proof_path.relative_to(REPO).as_posix(),
                                   'before': before, 'after': converted,
                                   'basis': 'source-only endpoint search; independent same-byte encode; unchanged QA thresholds'}
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    return {'state': manifest['state'], 'items': len(manifest['items']), 'repair_independently_verified': True}


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--manifest', type=Path, required=True)
    cli.add_argument('--proof', type=Path, required=True)
    args = cli.parse_args()
    print(json.dumps(accept(args.manifest.resolve(), args.proof.resolve())))
