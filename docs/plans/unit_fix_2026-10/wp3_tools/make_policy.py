"""python make_policy.py <job> <blend_rel> <prefix> [stagger_move]  -> writes validation/animation_delivery_policy.json bound to the blend SHA."""
import sys, json, hashlib
from pathlib import Path
MOD = Path(r"C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux")
job, blend, prefix = sys.argv[1:4]; stagger = len(sys.argv) > 4 and sys.argv[4] == 'stagger_move'
J = MOD / 'docs/assets/002_zombie_outbreak/models_3d' / job
sha = hashlib.sha256((J / blend).read_bytes()).hexdigest().upper()
acts = {}
for r in ('idle', 'move', 'attack', 'defend', 'support_attack', 'retreat', 'training', 'death'):
    row = {'role': r, 'looped': r != 'death', 'strike_windows': [], 'humanoid': True, 'source_sha256': sha}
    if r == 'move' and stagger: row['humanoid'] = False
    acts[f'{prefix}_{r}'] = row
doc = {'actions': acts, 'note': 'Roles and loop state from the entity states; humanoid=false on move declares a stagger gait whose plants are measured and reported but not forced into a 1.0-1.5 s two-plant stride.' if stagger else 'Roles and loop state from the entity states.'}
(J / 'validation').mkdir(exist_ok=True)
(J / 'validation/animation_delivery_policy.json').write_text(json.dumps(doc, indent=1))
print(sha)
