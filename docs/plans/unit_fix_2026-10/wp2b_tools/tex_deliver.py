"""python tex_deliver.py <job> <folder> <stem> <fin_dir> [execute_install]
Copies graded maps into the job, writes provenance + request, runs the repository texture CLI (prepare, convert --execute).
Install is a separate explicit step (cli install --execute) run with the mesh/anim install."""
import sys, json, hashlib, shutil, subprocess
from pathlib import Path
MOD = Path(r"<mod root>")
job, folder, stem, fin, tag = sys.argv[1:6]
fin = Path(fin); J = MOD / 'docs/assets/014_cannibalism/models_3d' / job
out = J / 'textures' / f'wp2b_{tag}'; out.mkdir(parents=True, exist_ok=True)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rel(p): return Path(p).resolve().relative_to(MOD).as_posix()
files = {'diffuse': 'diffuse.png', 'normal': 'normal.png', 'specular': 'specular.png', 'occupancy': 'occupancy.png'}
for k, v in files.items(): shutil.copy2(fin / v, out / f'{stem}_{k}.png')
for m in fin.glob('class_*.png'): shutil.copy2(m, out / m.name)
masks = {m.stem.replace('class_', ''): {'path_rel': rel(out / m.name), 'sha256': sha(out / m.name)} for m in out.glob('class_*.png')}
prov_n = {'kind': 'pdx_packed_normal_evidence', 'source': {'path_rel': rel(out / f'{stem}_normal.png'), 'sha256': sha(out / f'{stem}_normal.png')}, 'detail_synthesized': False}
prov_s = {'kind': 'pdx_material_mask_evidence', 'source': {'path_rel': rel(out / f'{stem}_specular.png'), 'sha256': sha(out / f'{stem}_specular.png')}, 'material_masks': masks, 'detail_synthesized': False}
(out / 'normal_provenance.json').write_text(json.dumps(prov_n, indent=1)); (out / 'specular_provenance.json').write_text(json.dumps(prov_s, indent=1))
items = []
for role in ('diffuse', 'normal', 'specular'):
    target = MOD / 'gfx/models/units' / folder / f'{stem}_{role}.dds'
    it = {'id': f'{stem}_{role}', 'role': role, 'source_rel': rel(out / f'{stem}_{role}.png'), 'target_rel': rel(target),
          'occupancy_mask_rel': rel(out / f'{stem}_occupancy.png'), 'conversion_scope': 'compression_only',
          'size': int(__import__('os').environ.get('TEX_SIZE','512')), 'dilation_px': 12, 'alpha_used': role != 'diffuse' and 'auto' or False}
    if role == 'diffuse': it['alpha_used'] = False
    else: it.pop('alpha_used')
    if target.exists(): it['expected_target_sha256'] = sha(target).lower()
    if role == 'normal': it['provenance_rel'] = rel(out / 'normal_provenance.json')
    if role == 'specular': it['provenance_rel'] = rel(out / 'specular_provenance.json')
    items.append(it)
req = {'batch_id': f'wp2b_{job}_textures_{tag}', 'items': items}
(out / 'request.json').write_text(json.dumps(req, indent=1))
cli = [sys.executable, '-B', str(MOD / '.tools/3d_pipeline/textures/cli.py')]
stage = rel(J / 'textures' / f'wp2b_{tag}_staging'); man = rel(out / 'manifest.json')
for cmd in (['prepare', '--root', str(MOD), '--request', rel(out / 'request.json'), '--staging-root', stage, '--manifest', man],
            ['convert', '--root', str(MOD), '--manifest', man, '--execute']):
    r = subprocess.run(cli + cmd, capture_output=True, text=True, cwd=MOD)
    print(cmd[0], r.returncode, (r.stdout[-1500:] if r.returncode == 0 else r.stderr[-2500:] + r.stdout[-800:]))
    if r.returncode: sys.exit(1)
