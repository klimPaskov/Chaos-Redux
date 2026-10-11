"""python install_model.py <job> <folder> <stem> <out_rel> <tag1,tag2,...>
Requires every role in <out_rel>/wp2b_report.json to have final_gate pass and a reimport proof. Installs each texture batch (repository CAS CLI) and copies mesh + anims with SHA parity."""
import sys, json, hashlib, shutil, subprocess
from pathlib import Path
MOD = Path(r"<mod root>")
job, folder, stem, out, tags = sys.argv[1:6]
J = MOD / 'docs/assets/014_cannibalism/models_3d' / job
rep = json.load(open(J / out / 'wp2b_report.json'))
bad = {r: e['final_gate']['status'] for r, e in rep['roles'].items() if e['final_gate']['status'] != 'pass' or 'error' in e.get('reimport', {})}
if bad or len(rep['roles']) != 8:
    sys.exit(f'refusing install: {bad} roles={len(rep["roles"])}')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
dest = MOD / 'gfx/models/units' / folder
rec = {'files': {}}
for tag in [x for x in tags.split(',') if x]:
    man = (J / 'textures' / f'wp2b_{tag}' / 'manifest.json').relative_to(MOD).as_posix()
    r = subprocess.run([sys.executable, '-B', str(MOD / '.tools/3d_pipeline/textures/cli.py'), 'install', '--root', str(MOD), '--manifest', man, '--execute'], capture_output=True, text=True, cwd=MOD)
    print('texture install', tag, r.returncode, r.stdout[-300:] if r.returncode == 0 else r.stderr[-1500:] + r.stdout[-500:])
    if r.returncode: sys.exit(1)
files = [(J / out / f'{stem}.mesh', dest / f'{stem}.mesh')] + [(J / out / f'{stem}_{role}.anim', dest / f'{stem}_{role}.anim') for role in rep['roles']]
for src, dst in files:
    shutil.copy2(src, dst)
    assert sha(src) == sha(dst), dst
    rec['files'][dst.name] = sha(dst)
for p in sorted(dest.glob('*.dds')): rec['files'][p.name] = sha(p)
(J / out / 'install_record.json').write_text(json.dumps(rec, indent=1))
print('installed', len(rec['files']), 'files to', dest)
