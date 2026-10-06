"""Deliver provider PBR maps as masked PDX BC1/BC3 mipmapped DDS.

Require source-adjacent material_classes.json with explicit classes and UV
occupancy; retain originals, default to 512, and never enlarge source maps.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import uuid
from PIL import Image

PIPE = Path(__file__).resolve().parents[1]
MOD = PIPE.parents[1]
sys.path.insert(0, str(PIPE))
from pack_pdx_material import pack_pdx_specular_channels, pack_pdx_normal_map
from textures.delivery import prepare_batch, convert_batch, install_batch


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--textures', type=Path, required=True)
    cli.add_argument('--out-dir', type=Path, required=True)
    cli.add_argument('--stem', required=True)
    cli.add_argument('--profile', default='humanoid_unit')
    cli.add_argument('--gamma', type=float)
    cli.add_argument('--size', type=int, choices=(128, 256, 512, 1024), default=512)
    cli.add_argument('--size-justification')
    args = cli.parse_args()
    source, out = args.textures.resolve(), args.out_dir.resolve()
    source.relative_to(MOD)
    out.relative_to(MOD)
    if args.size == 1024 and not args.size_justification:
        raise ValueError('1024 delivery requires an atlas justification')
    profiles = json.loads((PIPE / 'config/asset_profiles.json').read_text(encoding='utf-8'))['profiles']
    gamma = args.gamma if args.gamma is not None else float(profiles[args.profile].get('runtime_diffuse_gamma', 1))
    classes = json.loads((source / 'material_classes.json').read_text(encoding='utf-8-sig'))
    mask = source / classes['occupancy']
    out.mkdir(parents=True, exist_ok=True)
    work = out / ('source_' + uuid.uuid4().hex[:10])
    work.mkdir()
    with Image.open(source / 'base_color.png') as image:
        rgba = image.convert('RGBA')
        lut = [round(255 * (value / 255) ** gamma) for value in range(256)]
        r, g, b, a = rgba.split()
        diffuse = Image.merge('RGBA', (r.point(lut), g.point(lut), b.point(lut), a))
        diffuse_path = work / 'diffuse.png'
        diffuse.save(diffuse_path)
    specular_path = work / 'specular.png'
    specular = pack_pdx_specular_channels(MOD, (source / 'metallic.png').relative_to(MOD).as_posix(),
        (source / 'roughness.png').relative_to(MOD).as_posix(), specular_path.relative_to(MOD).as_posix())
    normal = pack_pdx_normal_map(MOD, (source / 'normal.png').relative_to(MOD).as_posix())
    normal_path = MOD / normal['output']['path']
    request = {'batch_id': 'pbr_' + uuid.uuid4().hex[:10], 'items': []}
    for role, path in [('diffuse', diffuse_path), ('specular', specular_path), ('normal', normal_path)]:
        with Image.open(path) as image:
            size = min(args.size, image.width, image.height)
        request['items'].append({'id': role, 'source_rel': path.relative_to(MOD).as_posix(),
            'target_rel': (out / (args.stem + '_' + role + '.dds')).relative_to(MOD).as_posix(),
            'occupancy_mask_rel': mask.relative_to(MOD).as_posix(), 'role': role, 'size': size,
            'size_justification': args.size_justification, 'dilation_px': 12,
            'conversion_scope': 'packed_normal_cleanup' if role == 'normal' else 'compression_only'})
    request_path, manifest = work / 'request.json', work / 'delivery.json'
    request_path.write_text(json.dumps(request, indent=2) + '\n', encoding='utf-8')
    prepare_batch(MOD, request_path, work / 'stage', manifest)
    converted = convert_batch(MOD, manifest, execute=True)
    if not converted['install']['install_eligible']:
        raise RuntimeError('Provider map delivery refused quality; inspect ' + str(manifest))
    result = install_batch(MOD, manifest, execute=True)
    record = {'delivery_manifest': manifest.relative_to(MOD).as_posix(), 'profile': args.profile,
              'diffuse_gamma': gamma, 'size_requested': args.size, 'specular_recipe': specular,
              'normal_recipe': normal, 'state': result['state'],
              'sources': {name: hashlib.sha256((source / name).read_bytes()).hexdigest()
                          for name in ('base_color.png', 'roughness.png', 'metallic.png', 'normal.png')}}
    (out / (args.stem + '_textures_manifest.json')).write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'state': result['state'], 'manifest': str(manifest)}))


if __name__ == '__main__':
    main()
