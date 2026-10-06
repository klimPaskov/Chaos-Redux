"""Deliver one already-authored packed map through the common BC/mip gates."""
import argparse
import json
from pathlib import Path
import sys
import uuid

from PIL import Image
PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
from textures.delivery import prepare_batch, convert_batch, install_batch


def deliver(repo, job, source, target, mask, role):
    from textures.atlas import load_occupancy_mask
    if not mask.is_file():
        raise ValueError('Runtime map delivery requires its actual UV occupancy mask.')
    with Image.open(source) as image:
        size = image.size
    with Image.open(mask) as image:
        occupancy = load_occupancy_mask(image)
    unique = 'map_' + uuid.uuid4().hex[:12]
    directory = job / 'validation/texture_delivery' / unique
    directory.mkdir(parents=True)
    if occupancy.size != size:
        occupancy = occupancy.resize(size, Image.Resampling.NEAREST)
    normalized_mask = directory / 'mask.png'
    occupancy.save(normalized_mask)
    request = {'batch_id': unique, 'items': [{'id': 'map', 'role': role,
        'source_rel': source.relative_to(repo).as_posix(), 'target_rel': target.relative_to(repo).as_posix(),
        'occupancy_mask_rel': normalized_mask.relative_to(repo).as_posix(), 'size': min(512, size[0]),
        'conversion_scope': 'packed_normal_cleanup' if role == 'normal' else 'compression_only', 'dilation_px': 12}]}
    request_file = directory / 'request.json'
    request_file.write_text(json.dumps(request, indent=2) + '\n', encoding='utf-8')
    manifest = directory / 'manifest.json'
    prepare_batch(repo, request_file, directory / 'stage', manifest)
    result = convert_batch(repo, manifest, execute=True)
    if not result['install']['install_eligible']:
        raise RuntimeError('Map delivery refused quality; inspect ' + str(manifest))
    result = install_batch(repo, manifest, execute=True)
    return {'manifest': manifest.relative_to(job).as_posix(), 'state': result['state']}


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'job', 'source', 'target', 'mask'):
        cli.add_argument('--' + name, type=Path, required=True)
    cli.add_argument('--role', choices=('diffuse', 'normal', 'specular'), required=True)
    args = cli.parse_args()
    print(json.dumps(deliver(args.repo.resolve(), args.job.resolve(), args.source.resolve(), args.target.resolve(), args.mask.resolve(), args.role)))
