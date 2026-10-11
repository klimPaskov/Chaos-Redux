"""python chain_run.py <config.json>
Runs, in the Lab on LABPORT: [holdpass] -> post_hold -> finish_floor -> seal, chaining checkpoints, and prints compact results.
config: {job, prefix, src (wp2b_03_items.blend), steps:[...], hold:{...holdpass CFG without job/src/out/prefix}, items:[{item,main,off?,axis_local,shaft?}], loops:[...], roles:[...]}"""
import sys, json, os
sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import lab
BASE = r"<mod root>/.tmp/wp2b/"
cfg = json.load(open(sys.argv[1]))
def run(script, c):
    code = "import json\nCFG=json.loads(%r)\n" % json.dumps(c) + open(BASE + script, encoding='utf-8').read()
    r = lab.run(code)
    if r.get('status') != 'ok': print('ERROR', script, str(r.get('message'))[:1500]); sys.exit(1)
    return r.get('result')
cur = cfg['src']; n = 4
roles = cfg.get('roles', ["idle","move","attack","defend","support_attack","retreat","training","death"])
for step in cfg['steps']:
    out = f"wp2b_{n:02d}_{step}.blend"
    if step == 'hold':
        c = dict(cfg['hold']); c.update(job=cfg['job'], prefix=cfg['prefix'], src=cur, out=out)
        res = run('holdpass.py', c)
    elif step == 'post':
        c = dict(job=cfg['job'], prefix=cfg['prefix'], src=cur, out=out, items=cfg['items'], roles=roles, trim=cfg.get('trim', {}))
        res = run('post_hold.py', c)
    elif step in ('floor', 'floor0'):
        res = {}
        c0 = cur
        for k, it in enumerate(cfg['items']):
            o = out if k == len(cfg['items']) - 1 else f"wp2b_{n:02d}_{step}_{k}.blend"
            c = dict(job=cfg['job'], prefix=cfg['prefix'], src=cur, out=o, roles=roles, item='ITEM_' + it['item'], main=it['main'], upper_off=cfg.get('upper_off', 'LeftArm'), fore_off=cfg.get('fore_off', 'LeftForeArm'),
                     axis_local=it['axis_local'], rounds=(0 if step == 'floor0' else cfg.get('rounds', 8)), hold_tol=cfg.get('hold_tol', 0.3), s_min=cfg.get('s_min', 1.0), s_max=cfg.get('s_max', 5.0), floor_clear=(cfg.get('floor_clear_final', 0.0) if step == 'floor0' else 0.02))
            if it.get('off'): c['off'] = it['off']
            res[it['item']] = run('finish_floor.py', c); cur = o
        out = cur
    elif step == 'refresh':
        it = cfg['items'][0]
        c = dict(job=cfg['job'], prefix=cfg['prefix'], src=cur, out=out, roles=roles, main=it['main'], off=it['off'], upper_off=cfg.get('upper_off', 'LeftArm'), fore_off=cfg.get('fore_off', 'LeftForeArm'),
                 axis_local=it['axis_local'], s_min=cfg.get('s_min', 1.0), s_max=cfg.get('s_max', 5.0))
        res = run('refresh.py', c)
    elif step == 'seal':
        c = dict(job=cfg['job'], prefix=cfg['prefix'], src=cur, out=out, roles=cfg['loops'], ground_roles=roles)
        res = run('seal.py', c)
    print('##', step, '->', out); print(json.dumps(res)[:2600]); cur = out; n += 1
print('FINAL', cur)
