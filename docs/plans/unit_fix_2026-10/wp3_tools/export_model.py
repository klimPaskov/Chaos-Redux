"""Export mesh + eight actions through the adapter, repair exporter-level quaternion signs, re-gate the final bytes, prove by reimport.
python export_model.py <job> <blend_rel> <stem> <prefix> <out_rel> [--roles r1,r2] [--skip-mesh]
Report: <job>/<out_rel>/wp3_report.json
"""
import sys, json, hashlib, subprocess, traceback
from pathlib import Path
MOD = Path(r"C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux")
sys.path.insert(0, str(MOD / '.tools/3d_pipeline/review')); sys.path.insert(0, str(MOD / '.tools/3d_pipeline/adapter')); sys.path.insert(0, str(MOD / '.tools/3d_pipeline/runtime'))
import provider_intake as pi
import anim_signs
import pdx_reader
from animation_delivery_checks import inspect_animation_delivery

job, blend, stem, prefix, out = sys.argv[1:6]
roles = ['idle', 'move', 'attack', 'defend', 'support_attack', 'retreat', 'training', 'death']
for a in sys.argv[6:]:
    if a.startswith('--roles='): roles = a.split('=', 1)[1].split(',')
skip_mesh = '--skip-mesh' in sys.argv
PT = next((a.split('=',1)[1] for a in sys.argv if a.startswith('--proof-tag=')), '')
J = pi.job_root(job)
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
policy = json.load(open(J / 'validation/animation_delivery_policy.json'))['actions']
report = {'blend': blend, 'blend_sha256': digest(J / blend), 'roles': {}}
mesh_rel = f'{out}/{stem}.mesh'
if not skip_mesh:
    mesh = pi.adapter('export_mesh', {'job_id': job, 'blend_rel': blend, 'output_rel': mesh_rel})
    report['mesh'] = {'rel': mesh_rel, 'sha256': digest(J / mesh_rel), 'streams': mesh.get('mesh_streams'), 'geometry': mesh.get('geometry'), 'delivery_gate': mesh.get('delivery_gate')}
    print('mesh', report['mesh']['sha256'][:12], flush=True)
else:
    report['mesh'] = {'rel': mesh_rel, 'sha256': digest(J / mesh_rel)}
mesh_tree, _ = pdx_reader.read(J / mesh_rel)
skel = [n for n in mesh_tree.iter() if n.tag == 'skeleton'][0]
for role in roles:
    action = f'{prefix}_{role}'
    anim_rel = f'{out}/{stem}_{role}.anim'
    entry = {'action': action, 'anim_rel': anim_rel}
    try:
        if '--regate' in sys.argv: raise KeyError('regate')
        exp = pi.adapter('export_animation', {'job_id': job, 'blend_rel': blend, 'action_name': action, 'output_rel': anim_rel})
        entry['adapter_gate'] = 'pass'
    except KeyError:
        entry['adapter_gate'] = 'reused'; exp = {}
    except RuntimeError as e:
        entry['adapter_gate'] = 'refused'
        entry['adapter_error'] = str(e)[:300]
        exp = {}
    ap = J / anim_rel
    delivery_path = ap.with_suffix('.delivery.json')
    if not ap.exists():
        entry['status'] = 'no_anim'; report['roles'][role] = entry; print(role, 'NO ANIM'); continue
    fixed = anim_signs.fix(ap)  # rotation-preserving sign normalisation, original kept as .signs_orig
    entry['sign_fix'] = {k: fixed[k] for k in ('negative_dots_before', 'samples_negated', 'negative_dots_after', 'sha256_in', 'sha256_out')}
    tree, _ = pdx_reader.read(ap)
    pol = policy[action]
    try:
        rep = inspect_animation_delivery(tree, skeleton_tree=skel, action_name=action, role=role, looped=pol['looped'],
                                         root_bone='Hips', humanoid=pol['humanoid'], strike_windows=pol.get('strike_windows', []))
    except Exception as ex:
        rep = {'status': 'error', 'error': str(ex)}
    adapter_delivery = json.load(open(delivery_path))['delivery'] if delivery_path.exists() else {}
    adapter_foot = (adapter_delivery.get('foot_contacts') or {}).get('status')
    sub = {k: rep.get(k, {}).get('status') for k in ('quaternion_sign_continuity', 'single_frame_limits', 'loop_seam', 'root_motion', 'world_motion')}
    ok = all(v in ('pass', 'not_applicable') for v in sub.values()) and adapter_foot in ('pass', 'unmeasured', 'measured', None)
    entry['final_gate'] = {'status': 'pass' if ok else 'blocked', 'sub': sub, 'adapter_foot_contacts': adapter_foot}
    entry['frames'] = [rep.get('frame_start'), rep.get('frame_end')]
    entry['violations'] = [(v['kind'], v['frame'], v['bone'], round(v.get('translation_step', 0), 3), round(v.get('angular_deg', 0), 1)) for v in rep.get('single_frame_limits', {}).get('violations', [])[:8]]
    entry['sha256'] = digest(ap)
    try:
        proof = pi.adapter('reimport_export', {'job_id': job, 'mesh_rel': mesh_rel, 'anim_rel': anim_rel, 'proof_name': f'{Path(out).name}_{role}{PT}'})
        contact = [b['ground_contact_z'] for b in proof.get('animation_bounds', [])]
        entry['reimport'] = {'contact_min_max': [min(contact), max(contact)] if contact else None, 'proof_blend': proof.get('proof_blend'), 'previews': proof.get('previews', [])[:3]}
    except RuntimeError as e:
        entry['reimport'] = {'error': str(e)[:300]}
    report['roles'][role] = entry
    print(role, entry['final_gate']['status'], sub if not ok else '', entry['violations'][:3], entry['reimport'].get('contact_min_max'), flush=True)
(J / out / 'wp3_report.json').write_text(json.dumps(report, indent=1, default=str), encoding='utf-8')
print('REPORT', J / out / 'wp3_report.json')
