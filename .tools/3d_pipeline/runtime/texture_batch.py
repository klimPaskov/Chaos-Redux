"""Plan one safe global texture delivery from installed UV and input hashes."""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys

from PIL import Image, ImageChops
from inventory import REPO, resolve, index_assets, walk
from pdx_reader import sha256
PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
from textures.delivery import prepare_batch, convert_batch, install_batch


def prepare(inventory, uv_rows, output, batch_id):
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    records = defaultdict(list)
    definitions = index_assets()[0]
    masks_by_model = {row['pdxmesh']: {item['texture']: item for item in row['masks']} for row in uv_rows}
    for model in inventory['models']:
        if sha256(REPO / model['registration']['path']) != model['registration']['sha256']:
            raise ValueError('Active registration changed after inventory')
        roles = {node.value: node.key.removeprefix('texture_') for node in walk(definitions[model['pdxmesh']]['node'])
                 if node.key in {'texture_diffuse', 'texture_specular', 'texture_normal'}}
        for texture in model['textures']:
            item = texture.get('file')
            if not item:
                continue
            mask = masks_by_model[model['pdxmesh']].get(texture['declared'])
            if not mask:
                raise ValueError('Missing exact active UV mask: ' + str(texture))
            if mask['mesh_sha256'] != model['mesh']['sha256'] or mask['registration_sha256'] != model['registration']['sha256']:
                raise ValueError('UV mask is bound to stale geometry/registration')
            if sha256(REPO / mask['mask']) != mask['sha256']:
                raise ValueError('UV occupancy mask changed')
            records[item['path']].append({'model': model['pdxmesh'], 'file': item, 'mask': mask,
                                          'role': roles[texture['declared']]})
    request = {'batch_id': batch_id, 'items': []}
    crosswalk = []
    for index, (path, consumers) in enumerate(sorted(records.items())):
        source = resolve(path)
        with Image.open(source) as image:
            size = image.size
        if size[0] != size[1]:
            raise ValueError('Non-square runtime model atlas')
        merged = Image.new('L', size, 0)
        for consumer in consumers:
            with Image.open(REPO / consumer['mask']['mask']) as mask:
                merged = ImageChops.lighter(merged, mask.resize(size, Image.Resampling.NEAREST))
        mask_path = output / 'masks' / ('m{:03d}.png'.format(index))
        mask_path.parent.mkdir(parents=True, exist_ok=True)
        merged.save(mask_path)
        roles = {row['role'] for row in consumers}
        if len(roles) != 1:
            raise ValueError('Texture is consumed with conflicting roles: ' + path)
        role = roles.pop()
        request['items'].append({'id': 't{:03d}'.format(index), 'source_rel': path, 'target_rel': path,
                                  'role': role, 'occupancy_mask_rel': mask_path.relative_to(REPO).as_posix(),
                                  'size': min(512, size[0]), 'dilation_px': 12,
                                  'expected_target_sha256': consumers[0]['file']['sha256'],
                                  'conversion_scope': 'packed_normal_cleanup' if role == 'normal' else 'compression_only'})
        crosswalk.append({'id': request['items'][-1]['id'], 'target': path,
                          'models': sorted(set(row['model'] for row in consumers))})
    request_path = output / 'request.json'
    request_path.write_text(json.dumps(request, indent=2) + '\n', encoding='utf-8')
    (output / 'crosswalk.json').write_text(json.dumps(crosswalk, indent=2) + '\n', encoding='utf-8')
    return prepare_batch(REPO, request_path, output / 'stage', output / 'manifest.json')


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('command', choices=['prepare', 'convert', 'install'])
    cli.add_argument('--inventory', type=Path)
    cli.add_argument('--uv-masks', type=Path)
    cli.add_argument('--output', type=Path, required=True)
    cli.add_argument('--batch-id', default='shared_unit_delivery_20261006')
    cli.add_argument('--execute', action='store_true')
    args = cli.parse_args()
    if args.command == 'prepare':
        result = prepare(json.loads(args.inventory.read_text()), json.loads(args.uv_masks.read_text()), args.output, args.batch_id)
    elif args.command == 'convert':
        result = convert_batch(REPO, args.output / 'manifest.json', execute=args.execute)
    else:
        result = install_batch(REPO, args.output / 'manifest.json', execute=args.execute)
    print(json.dumps({'state': result.get('state'), 'items': len(result.get('items', [])),
                      'conversion': result.get('conversion'), 'install_status': result.get('install', {}).get('status')}))
