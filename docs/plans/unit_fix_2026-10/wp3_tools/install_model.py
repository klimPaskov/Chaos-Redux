"""python install_model.py <job> <folder> <stem> <out_rel> <tex_tag> [--no-tex]
Requires every role in <out_rel>/wp3_report.json to have final_gate pass. Installs textures (repository CAS CLI) and copies mesh + anims with SHA parity.
"""
import sys, json, hashlib, shutil, subprocess
from pathlib import Path
MOD = Path(r"C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux")
job, folder, stem, out, tag = sys.argv[1:6]
J = MOD / 'docs/assets/002_zombie_outbreak/models_3d' / job
rep = json.load(open(J / out / 'wp3_report.json'))
bad = {r: e['final_gate']['status'] for r, e in rep['roles'].items() if e['final_gate']['status'] != 'pass' or 'error' in e.get('reimport', {})}
if bad or len(rep['roles']) != 8:
    sys.exit(f'refusing install: {bad} roles={len(rep["roles"])}')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
dest = MOD / 'gfx/models/units' / folder
rec = {'files': {}}
if '--no-tex' not in sys.argv:
    man = (J / 'textures' / f'wp3_{tag}' / 'manifest.json').relative_to(MOD).as_posix()
    r = subprocess.run([sys.executable, '-B', str(MOD / '.tools/3d_pipeline/textures/cli.py'), 'install', '--root', str(MOD), '--manifest', man, '--execute'], capture_output=True, text=True, cwd=MOD)
    print('texture install', r.returncode, r.stdout[-400:] if r.returncode == 0 else r.stderr[-1500:] + r.stdout[-500:])
    if r.returncode: sys.exit(1)
files = [(J / out / f'{stem}.mesh', dest / f'{stem}.mesh')] + [(J / out / f'{stem}_{role}.anim', dest / f'{stem}_{role}.anim') for role in rep['roles']]
for src, dst in files:
    shutil.copy2(src, dst)
    assert sha(src) == sha(dst), dst
    rec['files'][dst.name] = sha(dst)
for k in ('diffuse', 'normal', 'specular'):
    p = dest / f'{stem}_{k}.dds'; rec['files'][p.name] = sha(p)
(J / out / 'install_record.json').write_text(json.dumps(rec, indent=1))
print('installed', len(rec['files']), 'files to', dest)
