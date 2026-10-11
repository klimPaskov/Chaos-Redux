"""python chain.py <config.json> [start_step]  -- orchestrates fingers build -> per item (targets, hold, post) -> finger keys, via the Blender Lab socket.
config: {job, src, tag, roles, loops, params:{beta,dsh,tt,clear}, items:[{item, main, off?, al, s_min, s_max}]}"""
import sys, json, subprocess, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(sys.argv[1])); start = sys.argv[2] if len(sys.argv) > 2 else 'fingers'
job = cfg['job']; tag = cfg['tag']; roles = cfg.get('roles', ["idle","move","attack","defend","support_attack","retreat","training","death"]); loops = cfg['loops']
P = cfg.get('params', {'beta': 20, 'dsh': 0.12, 'tt': 0.0, 'clear': 0.02})
def run(script, c, limit=3000):
    r = subprocess.run([sys.executable, os.path.join(HERE, 'run.py'), os.path.join(HERE, script), json.dumps(c), str(limit)], capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    if 'ERROR' in out[:400] or r.returncode: print(script, 'FAILED', out[:2500]); sys.exit(1)
    return out
steps = ['fingers'] + [f'item{i}' for i in range(len(cfg['items']))] + ['keys']
cur = cfg['src']; t0 = time.time()
def ck(n): return f"{tag}_{n}.blend"
if steps.index(start) <= 0:
    print('fingers', run('fingers_build.py', {'job': job, 'src': cur, 'out': ck('01_fingers')}, 600)[:300], flush=True)
cur = ck('01_fingers')
for i, it in enumerate(cfg['items']):
    name = it['item'].replace('ITEM_', '')
    hold_out, post_out = ck(f'02_hold_{name}'), ck(f'03_post_{name}')
    tg = f'targets_{tag}_{name}.json'; aux = f'{tag}_{name}_aux.json'
    if steps.index(start) <= i + 1:
        hc = dict(job=job, src=cur, out=hold_out, item=it['item'], main=it['main'], off=it.get('off'), al=it['al'], roles=roles, loops=loops, s_min=it.get('s_min', 0.8), s_max=it.get('s_max', 5.7), aux_out=aux, **{k: P[k] for k in ('beta', 'dsh', 'tt')})
        o = run('unit_stage.py', hc, 600); print(name, 'stage ok', o[:200], round(time.time() - t0), flush=True)
        pc = dict(job=job, src=hold_out, out=post_out, targets=None, aux=aux, item=it['item'], main=it['main'], off=it.get('off'), roles=roles, loops=loops, s_min=it.get('s_min', 0.8), s_max=it.get('s_max', 5.7), floor_mode=it.get('floor_mode'), no_align=it.get('no_align',[]), tilt_rounds=it.get('tilt_rounds',6), tilt_sigma=it.get('tilt_sigma',2.0), **P)
        o = run('scav_post.py', pc, 8000)
        d = json.loads(o) if o.startswith('{') else {}
        for r, v in d.items(): print(' ', name, r, {k: v[k] for k in ('floor_min', 'below', 'over', 'ang_over', 'local_over', 'local_max', 'seam', 'local_seam') if k in v}, flush=True)
    cur = post_out
if steps.index(start) <= len(steps) - 1:
    cfinal = cur
    for i, it in enumerate(cfg['items']):
        name = it['item'].replace('ITEM_', ''); out = ck('04_keyed') if i == len(cfg['items']) - 1 else ck(f'04_keyed_{name}')
        kc = dict(job=job, src=cfinal, aux=f'{tag}_{name}_aux.json', out=out, main=it['main'], off=it.get('off'), roles=roles, **{k: P[k] for k in ('beta', 'dsh', 'tt')})
        o = run('finger_keys.py', kc, 600); cfinal = out
    print('keys ok', cfinal, round(time.time() - t0), flush=True)
