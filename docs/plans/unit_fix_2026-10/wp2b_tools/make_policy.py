"""python make_policy.py <job> <blend_rel> <prefix> <looped_csv> [windows_json] -> validation/animation_delivery_policy.json bound to the blend SHA."""
import sys, json, hashlib
from pathlib import Path
MOD = Path(r"<mod root>")
job, blend, prefix, looped = sys.argv[1:5]; looped = set(looped.split(','))
windows = json.loads(sys.argv[5]) if len(sys.argv) > 5 else {}
nonhum = set(sys.argv[6].split(',')) if len(sys.argv) > 6 else set()
J = MOD / 'docs/assets/014_cannibalism/models_3d' / job
sha = hashlib.sha256((J / blend).read_bytes()).hexdigest().upper()
acts = {}
for r in ('idle', 'move', 'attack', 'defend', 'support_attack', 'retreat', 'training', 'death'):
    acts[f'{prefix}_{r}'] = {'role': r, 'looped': r in looped, 'strike_windows': windows.get(r, []), 'humanoid': r not in nonhum, 'source_sha256': sha}
doc = {'actions': acts, 'note': 'Roles and loop state from the entity states; strike windows are explicit per measured strike or kick.'}
(J / 'validation').mkdir(exist_ok=True)
(J / 'validation/animation_delivery_policy.json').write_text(json.dumps(doc, indent=1))
print(sha)
