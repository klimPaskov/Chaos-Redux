"""Audit decoded installed model bytes once for all active unit consumers.

Output is measurement evidence, never fabricated repair or runtime acceptance.
Logical model, state, and source hashes travel together in every action report.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE / 'adapter'))
from animation_delivery_checks import inspect_animation_delivery
from geometry_delivery_checks import inspect_pdx_mesh_tree
from inventory import REPO, effective_entity, index_assets, resolve
from pdx_reader import read, sha256


def audit(inventory, output):
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    entities = index_assets()[2]
    mesh_cache, reports, motion, counts = {}, [], {}, Counter()
    for model in inventory['models']:
        mesh_item = model.get('mesh')
        row = {'pdxmesh': model['pdxmesh'], 'mesh': mesh_item, 'actions': {}, 'issues': []}
        if not mesh_item:
            row['issues'].append('missing mesh')
            reports.append(row)
            continue
        path = resolve(mesh_item['path'])
        if sha256(path) != mesh_item['sha256']:
            row['issues'].append('source changed after inventory; rebuild inventory before acceptance')
            reports.append(row)
            continue
        if mesh_item['sha256'] not in mesh_cache:
            tree, parser = read(path)
            geometry = inspect_pdx_mesh_tree(tree, provider_intake=True, manifold_required=True)
            skeletons = [node for node in tree.iter() if node.tag == 'skeleton']
            roots = {bone.tag for skeleton in skeletons for bone in skeleton if not bone.get('pa')}
            bone_names = {bone.tag for skeleton in skeletons for bone in skeleton}
            mesh_cache[mesh_item['sha256']] = (geometry, roots, bone_names, parser, tree)
        geometry, roots, bone_names, parser, skeleton_tree = mesh_cache[mesh_item['sha256']]
        row['geometry'] = geometry
        row['parser'] = parser
        row['root_bones'] = sorted(roots)
        row['bone_count'] = len(bone_names)
        row['scale'] = [entity['scale'] for entity in model['entities']]
        counts['geometry_' + geometry['status']] += 1
        states = [state for entity in model['entities'] for state in effective_entity(entity['name'], entities).children('state')]
        for role, action in model['actions'].items():
            item = action.get('file')
            if not item:
                row['actions'][role] = {'status': 'blocked', 'reason': 'missing active action'}
                continue
            path = resolve(item['path'])
            if sha256(path) != item['sha256']:
                row['actions'][role] = {'status': 'blocked', 'reason': 'action changed after inventory'}
                continue
            selected = [state for state in states if state.scalar('animation') == role]
            looping = any(state.scalar('looping') == 'yes' or state.scalar('next_state') == state.scalar('name') for state in selected)
            tree, _ = read(path)
            humanoid = {'LeftFoot', 'RightFoot'}.issubset(bone_names)
            report = inspect_animation_delivery(tree, skeleton_tree=skeleton_tree, action_name=action['definition'], role=role,
                                                  looped=looping, root_bone=next(iter(roots)) if len(roots) == 1 else None,
                                                  humanoid=humanoid)
            report['file'] = item
            report['root_identity_evidence'] = 'decoded installed mesh skeleton parent indices'
            row['actions'][role] = report
            motion[item['sha256']] = report
            counts['animation_' + report['status']] += 1
        reports.append(row)
        target = output / (model['pdxmesh'] + '.json')
        target.write_text(json.dumps(row, indent=2) + '\n', encoding='utf-8')
        print(model['pdxmesh'], geometry['status'], len(row['actions']), flush=True)
    (output / 'motion_reports.json').write_text(json.dumps(motion, indent=2) + '\n', encoding='utf-8')
    result = {'schema': 1, 'models': reports, 'counts': dict(counts), 'model_count': len(reports),
              'unique_meshes': len(mesh_cache), 'limitations': ['No live consumer or sole-contact proof; motion peaks are proxies.']}
    (output / 'summary.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--inventory', type=Path, required=True)
    cli.add_argument('--output', type=Path, required=True)
    args = cli.parse_args()
    result = audit(json.loads(args.inventory.read_text(encoding='utf-8')), args.output)
    print(json.dumps({'models': result['model_count'], 'counts': result['counts'], 'output': str(args.output)}))
