"""Create serialized, hash-bound Blender checkpoints from installed meshes.

The verified adapter performs native import. These checkpoints establish
geometry/skeleton provenance; .gfx overrides, material review, skin deformation
and live consumer acceptance remain separate evidence. No runtime bytes change.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import sys

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
from blender_client import BlenderAdapterClient
from inventory import REPO, resolve
from pdx_reader import sha256


def archive(source, destination, expected):
    if sha256(source) != expected:
        raise ValueError('Runtime file changed after inventory: ' + str(source))
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if sha256(destination) != expected:
            raise ValueError('Existing immutable snapshot differs: ' + str(destination))
        return
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)
    if sha256(destination) != expected:
        raise RuntimeError('Archived runtime bytes differ')


def run(inventory, crosswalk, output):
    client = BlenderAdapterClient(REPO)
    models = {row['model']: row for row in crosswalk['models']}
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    document = {'schema': 1, 'proof_scope': 'native Blender geometry/skeleton import, no visual material acceptance', 'models': []}
    proofs = {}
    for model in inventory['models']:
        info = models[model['pdxmesh']]
        job_id = info['adapter_job_slug']
        config = json.loads((PIPELINE / 'config/blender_hoi4_adapter.json').read_text())
        job = Path(config.get('job_overrides', {}).get(job_id, str(Path(config['job_root']) / job_id)))
        item = model['mesh']
        row = {'pdxmesh': model['pdxmesh'], 'runtime_mesh': item, 'job_id': job_id}
        if item['sha256'] in proofs:
            row.update(proofs[item['sha256']])
            row['shared_geometry_proof'] = True
            document['models'].append(row)
            continue
        try:
            directory = job / 'validation' / 'i' / item['sha256'][:8]
            mesh = directory / Path(item['path']).name
            archive(resolve(item['path']), mesh, item['sha256'])
            texture_records = []
            for texture in model['textures']:
                target = texture.get('file')
                if target:
                    destination = directory / Path(target['path']).name
                    archive(resolve(target['path']), destination, target['sha256'])
                    texture_records.append({'path': destination.relative_to(job).as_posix(), 'sha256': target['sha256']})
            proof_name = 'installed_' + item['sha256'][:16]
            receipt = job / 'validation' / ('reimport_' + proof_name + '.json')
            if receipt.exists():
                result = json.loads(receipt.read_text(encoding='utf-8'))
                if result.get('mesh_sha256', '').casefold() != item['sha256'].casefold() or not (job / result['proof_blend']).is_file():
                    raise ValueError('Existing reimport receipt does not prove this runtime mesh')
            else:
                result = client.reimport_export(job_id, mesh.relative_to(job).as_posix(), proof_name=proof_name,
                                                stage_default_textures=False, preview_views=[],
                                                expected_mesh_sha256=item['sha256'])
            proof = job / result['proof_blend']
            facts = {'status': 'reimported_geometry', 'receipt': receipt.relative_to(REPO).as_posix(),
                     'proof_checkpoint': proof.relative_to(REPO).as_posix(), 'proof_sha256': sha256(proof),
                     'armatures': result.get('armatures'), 'meshes': result.get('meshes'),
                     'snapshotted_textures': texture_records, 'visual_material_acceptance': False}
            row.update(facts)
            proofs[item['sha256']] = facts
        except Exception as exc:
            row.update({'status': 'blocked', 'blocker': str(exc)})
        document['models'].append(row)
        output.write_text(json.dumps(document, indent=2) + '\n', encoding='utf-8')
        print(model['pdxmesh'], row['status'], row.get('blocker', '')[:250], flush=True)
    output.write_text(json.dumps(document, indent=2) + '\n', encoding='utf-8')
    return document


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--inventory', type=Path, required=True)
    cli.add_argument('--crosswalk', type=Path, required=True)
    cli.add_argument('--output', type=Path, required=True)
    args = cli.parse_args()
    run(json.loads(args.inventory.read_text()), json.loads(args.crosswalk.read_text()), args.output)
