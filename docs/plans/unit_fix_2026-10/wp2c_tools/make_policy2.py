"""python make_policy2.py <job> <family> <blend_rel> <prefix> <looped_csv> [windows_json] [nonhumanoid_csv]"""
import sys, json, hashlib
from pathlib import Path
MOD = Path(r"<mod root>")
job, fam, blend, prefix, looped = sys.argv[1:6]; looped = set(looped.split(','))
windows = json.loads(sys.argv[6]) if len(sys.argv) > 6 else {}
nonhum = set(sys.argv[7].split(',')) if len(sys.argv) > 7 and sys.argv[7] else set()
J = MOD / 'docs/assets' / fam / 'models_3d' / job
sha = hashlib.sha256((J / blend).read_bytes()).hexdigest().upper()
acts = {f'{prefix}_{r}': {'role': r, 'looped': r in looped, 'strike_windows': windows.get(r, []), 'humanoid': r not in nonhum, 'source_sha256': sha} for r in ('idle','move','attack','defend','support_attack','retreat','training','death')}
(J / 'validation').mkdir(exist_ok=True)
(J / 'validation/animation_delivery_policy.json').write_text(json.dumps({'actions': acts}, indent=1))
print(sha)
