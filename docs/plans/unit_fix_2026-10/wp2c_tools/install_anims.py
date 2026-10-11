"""python install_anims.py <job> <family> <export_rel> <export_stem> <dest_dir> <dest_stem>: copy the eight gate-passing .anim files (report must pass) into the runtime folder with SHA parity."""
import sys, json, shutil, hashlib
from pathlib import Path
job, fam, out, es, dest, ds = sys.argv[1:7]
J = Path('docs/assets') / fam / 'models_3d' / job; D = Path(dest)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
rep = json.load(open(J / out / 'wp2b_report.json'))
bad = {r: e['final_gate']['status'] for r, e in rep['roles'].items() if e['final_gate']['status'] != 'pass' or 'error' in e.get('reimport', {})}
if bad or len(rep['roles']) != 8: sys.exit(f'refusing: {bad} roles={len(rep["roles"])}')
rec = {}
for r in rep['roles']:
    s = J / out / f'{es}_{r}.anim'; d = D / f'{ds}_{r}.anim'; shutil.copy2(s, d); assert sha(s) == sha(d); rec[d.name] = sha(d)
(J / out / 'install_record.json').write_text(json.dumps(rec, indent=1)); print('installed', len(rec))
