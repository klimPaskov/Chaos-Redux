"""Rasterize active runtime UV triangles into texture occupancy masks.

PDX stores flipped V (top-left image coordinates). No pixel colour threshold is
used to classify artwork. The .gfx stream binding decides each map's islands.
"""
import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw
from inventory import REPO, index_assets, resolve
from pdx_reader import read, sha256


def masks(model, output, size=1024, mesh_index=None):
    meshes = mesh_index if mesh_index is not None else index_assets()[0]
    output = output.resolve()
    definition = meshes[model['pdxmesh']]
    path = resolve(model['mesh']['path'])
    tree, _ = read(path)
    settings = {(n.scalar('name'), int(n.scalar('index', '0'))): n for n in definition['node'].children('meshsettings')}
    atlases, issues = {}, []
    for obj in tree.find('object'):
        for index, stream in enumerate(obj.findall('mesh')):
            setting = settings.get((obj.tag, index))
            if setting is None:
                issues.append({'object': obj.tag, 'stream': index, 'rule': 'unbound_stream'})
                continue
            uv, tri = stream.get('u0'), stream.get('tri')
            if not uv or not tri:
                issues.append({'object': obj.tag, 'stream': index, 'rule': 'missing_uv'})
                continue
            if any(not -1 <= value <= 2 for value in uv):
                issues.append({'object': obj.tag, 'stream': index, 'rule': 'uv_wrap_requires_explicit_review'})
                continue
            names = [setting.scalar(key) for key in ('texture_diffuse', 'texture_specular', 'texture_normal')]
            points = [(uv[i] * (size - 1), uv[i + 1] * (size - 1)) for i in range(0, len(uv), 2)]
            for name in set(names) - {None}:
                image = atlases.setdefault(name, Image.new('L', (size, size), 0))
                draw = ImageDraw.Draw(image)
                for i in range(0, len(tri), 3):
                    vertices = [points[v] for v in tri[i:i + 3]]
                    # PDX model samplers wrap. Rasterize exact neighbouring tile
                    # copies for triangles crossing a UV seam, including tiny
                    # negative provider UVs, rather than clipping away islands.
                    uv_tri = [(x / (size - 1), y / (size - 1)) for x, y in vertices]
                    for dx in range(-math.floor(max(x for x, y in uv_tri)), 1 - math.floor(min(x for x, y in uv_tri))):
                        for dy in range(-math.floor(max(y for x, y in uv_tri)), 1 - math.floor(min(y for x, y in uv_tri))):
                            draw.polygon([(x + dx * (size - 1), y + dy * (size - 1)) for x, y in vertices], fill=255)
    output.mkdir(parents=True, exist_ok=True)
    result = []
    for name, image in atlases.items():
        target = output / (model['pdxmesh'] + '_' + Path(name).stem + '_occupancy.png')
        image.save(target)
        hist = image.histogram()
        result.append({'texture': name, 'mask': target.relative_to(REPO).as_posix(),
                       'sha256': sha256(target), 'mesh_sha256': model['mesh']['sha256'],
                       'registration_sha256': model['registration']['sha256'],
                       'coverage': hist[255] / (size * size), 'size': size})
    return {'pdxmesh': model['pdxmesh'], 'masks': result, 'issues': issues,
            'policy': 'rasterized actual PDX UVs; no colour-based island inference'}


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--inventory', type=Path, required=True)
    cli.add_argument('--output', type=Path, required=True)
    cli.add_argument('--size', type=int, default=1024)
    args = cli.parse_args()
    data = json.loads(args.inventory.read_text())
    meshes = index_assets()[0]
    rows = [masks(model, args.output, args.size, meshes) for model in data['models']]
    manifest = args.output / 'manifest.json'
    manifest.write_text(json.dumps(rows, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'models': len(rows), 'masks': sum(len(row['masks']) for row in rows),
                      'issues': sum(len(row['issues']) for row in rows), 'manifest': str(manifest)}))
