"""Read-only WP3 installed-byte and entity evidence using section 3 parsers."""
import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(REPO / '.tools/3d_pipeline/runtime'), str(REPO / '.tools/3d_pipeline/adapter')]
from inventory import snapshot, resolve
from pdx_reader import read, sha256
from animation_delivery_checks import decode_animation_tree
from entity_lint import audit

SLUGS = ['zombies', 'infected_zombies', 'rabid_zombies', 'parasitic_zombies',
         'mutant_zombies', 'undead_zombies', 'necrotic_zombies', 'demonic_zombies']

phase = sys.argv[1]
out = Path(__file__).parent / phase
out.mkdir(parents=True, exist_ok=True)
data = snapshot()
data['models'] = [m for m in data['models'] if m['pdxmesh'] in {'chaosx_' + s + '_mesh' for s in SLUGS}]
if len(data['models']) != 8:
    raise ValueError('Expected eight WP3 model consumers')
def referenced_paths(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str):
            yield value['path']
        for child in value.values():
            yield from referenced_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from referenced_paths(child)

owned_references = set(referenced_paths(data['models']))
data['files'] = [row for row in data['files'] if row['path'] in owned_references]
(out / 'inventory.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
motions = {}
for model in data['models']:
    old = REPO / 'docs/plans/unit_fix_2026-10/pipeline_evidence/installed_before' / (model['pdxmesh'] + '.json')
    prior = json.loads(old.read_text(encoding='utf-8'))
    for role, action in model['actions'].items():
        known = prior['actions'].get(role, {})
        if known.get('file', {}).get('sha256') == action.get('file', {}).get('sha256'):
            motions[action['file']['sha256']] = known
result = audit(data, motions)
(out / 'entity_lint.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
samples = []
for slug, role in [('necrotic_zombies', 'death'), ('undead_zombies', 'attack')]:
    path = REPO / 'gfx/models/units' / ('chaosx_' + slug) / ('chaosx_' + slug + '_' + role + '.anim')
    tree, parser = read(path)
    decoded = decode_animation_tree(tree)
    frames = []
    for i, frame in enumerate(decoded['frames']):
        frames.append({'frame': i + 1, 'time_s': i / decoded['fps'],
                       'hips_height_pdx_y': frame['Hips']['t'][1],
                       'left_hand_q': frame['LeftHand']['q'], 'right_hand_q': frame['RightHand']['q']})
    samples.append({'path': str(path.relative_to(REPO)), 'sha256': sha256(path), 'parser': parser,
                    'fps': decoded['fps'], 'frame_count': decoded['frame_count'], 'frames': frames,
                    'limitation': 'Joint samples establish motion, not deformed surface contact.'})
(out / 'timing_samples.json').write_text(json.dumps(samples, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'models': len(data['models']), 'states': result['coverage']['states'], 'rules': result['rules']}))
