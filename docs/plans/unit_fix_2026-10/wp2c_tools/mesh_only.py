"""python mesh_only.py <job> <family> <blend_rel> <out_rel> <stem> <anim_rel_dir> [roles_csv]
Exports the mesh through the adapter, then proves it by reimporting each listed existing .anim (same skeleton) against the new mesh."""
import sys, json, hashlib
from pathlib import Path
MOD = Path(r"<mod root>")
sys.path.insert(0, str(MOD / '.tools/3d_pipeline/review')); sys.path.insert(0, str(MOD / '.tools/3d_pipeline/adapter')); sys.path.insert(0, str(MOD / '.tools/3d_pipeline/runtime'))
import provider_intake as pi
job, fam, blend, out, stem, adir = sys.argv[1:7]; roles = sys.argv[7].split(',') if len(sys.argv) > 7 else ['death', 'attack']
J = MOD / 'docs/assets' / fam / 'models_3d' / job
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
mesh_rel = f'{out}/{stem}.mesh'
m = pi.adapter('export_mesh', {'job_id': job, 'blend_rel': blend, 'output_rel': mesh_rel})
rep = {'mesh': mesh_rel, 'sha256': sha(J / mesh_rel), 'gate': m.get('delivery_gate', {}).get('status') if isinstance(m.get('delivery_gate'), dict) else None, 'geometry': m.get('geometry'), 'proofs': {}}
print('mesh', rep['sha256'][:12], rep['gate'], flush=True)
for r in roles:
    anim_rel = f'{adir}/{stem}_{r}.anim'
    try:
        p = pi.adapter('reimport_export', {'job_id': job, 'mesh_rel': mesh_rel, 'anim_rel': anim_rel, 'proof_name': f'meshonly_{Path(out).name}_{r}'})
        c = [b['ground_contact_z'] for b in p.get('animation_bounds', [])]
        rep['proofs'][r] = {'anim_sha256': sha(J / anim_rel), 'contact_min_max': [min(c), max(c)] if c else None, 'previews': p.get('previews', [])[:3]}
    except Exception as e:
        rep['proofs'][r] = {'error': str(e)[:300]}
    print(r, rep['proofs'][r].get('contact_min_max') or rep['proofs'][r], flush=True)
(J / out / 'mesh_only_report.json').write_text(json.dumps(rep, indent=1, default=str), encoding='utf-8')
print('REPORT')
