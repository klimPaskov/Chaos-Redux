"""Convert extracted native checkpoint textures through the shared BC gates.

UV occupancy comes from existing Blender mesh loops. Packed map conventions
are preserved where provider handedness or material masks are unresolved.
"""
import argparse
import json
import math
from pathlib import Path
import sys
import uuid

from PIL import Image, ImageDraw
PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
from textures.delivery import prepare_batch, convert_batch, install_batch


def run(repo, job, extraction, roles):
    config = json.loads((PIPELINE / 'config/texture_delivery.json').read_text())
    batch = 'checkpoint_' + uuid.uuid4().hex[:12]
    directory = job / 'validation' / 'texture_delivery' / batch
    directory.mkdir(parents=True)
    request = {'batch_id': batch, 'items': []}
    images = {}
    for index, record in enumerate(extraction['textures']):
        name = record['image']
        source = job / record['processed_png']
        role = roles.get(name)
        if not role and len(record.get('connected_texture_roles', [])) == 1:
            role = record['connected_texture_roles'][0]
        if not role:
            stem = source.stem.casefold()
            role = next((role for role in ('diffuse', 'specular', 'normal') if role in stem), None)
        if role not in {'diffuse', 'specular', 'normal'}:
            raise ValueError('Unknown packed texture role; supply texture_roles for ' + name)
        with Image.open(source) as image:
            width, height = image.size
        if width != height:
            raise ValueError('Model texture atlas must be square')
        uv_record = json.loads((job / record['uv_triangles_rel']).read_text())
        mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(mask)
        for triangle in uv_record['triangles']:
            if any(not -1 <= value <= 2 for point in triangle for value in point):
                raise ValueError('UV wrapping beyond adjacent tiles requires reviewed atlas repair')
            for dx in range(-math.floor(max(p[0] for p in triangle)), 1 - math.floor(min(p[0] for p in triangle))):
                for dy in range(-math.floor(max(p[1] for p in triangle)), 1 - math.floor(min(p[1] for p in triangle))):
                    draw.polygon([((p[0] + dx) * (width - 1), (p[1] + dy) * (height - 1)) for p in triangle], fill=255)
        occupancy = directory / ('m{:03d}.png'.format(index))
        mask.save(occupancy)
        target = job / 'textures/dds' / (source.stem + '.dds')
        request['items'].append({'id': 't{:03d}'.format(index), 'source_rel': source.relative_to(repo).as_posix(),
                                  'target_rel': target.relative_to(repo).as_posix(), 'role': role,
                                  'occupancy_mask_rel': occupancy.relative_to(repo).as_posix(),
                                  'size': min(width, config['default_dimension']), 'dilation_px': config['dilation_pixels'],
                                  'conversion_scope': 'packed_normal_cleanup' if role == 'normal' else 'compression_only'})
        images[name] = target.relative_to(job).as_posix()
    request_path = directory / 'request.json'
    request_path.write_text(json.dumps(request, indent=2) + '\n', encoding='utf-8')
    manifest = directory / 'manifest.json'
    prepare_batch(repo, request_path, directory / 'stage', manifest)
    converted = convert_batch(repo, manifest, execute=True)
    if not converted['install']['install_eligible']:
        raise RuntimeError('Checkpoint texture delivery failed; inspect ' + str(manifest))
    installed = install_batch(repo, manifest, execute=True)
    return {'dds_map': images, 'manifest': manifest.relative_to(job).as_posix(), 'state': installed['state'],
            'backend': 'native BC1/BC3, full mip chain; semantic map failures remain reported'}


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--repo', type=Path, required=True)
    cli.add_argument('--job', type=Path, required=True)
    cli.add_argument('--extraction', type=Path, required=True)
    cli.add_argument('--roles', type=Path)
    cli.add_argument('--output', type=Path, required=True)
    args = cli.parse_args()
    report = run(args.repo.resolve(), args.job.resolve(), json.loads(args.extraction.read_text()),
                 json.loads(args.roles.read_text()) if args.roles else {})
    args.output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'state': report['state'], 'manifest': report['manifest']}))
