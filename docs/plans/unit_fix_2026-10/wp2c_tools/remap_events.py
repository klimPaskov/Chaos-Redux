"""python remap_events.py <entity.asset> <state:role_map.json fmap file> [--apply] -> rewrite event times of states whose role has a retime map. Prints before/after."""
import sys, json, re
from pathlib import Path
asset = Path(sys.argv[1]); fm = json.load(open(sys.argv[2])); apply = '--apply' in sys.argv
roles_map = {k: {int(a): float(b) for a, b in v.items()} for k, v in fm.items()}
def newframe(role, f_old):
    m = roles_map[role]; ks = sorted(m)
    if f_old <= ks[0]: return m[ks[0]]
    if f_old >= ks[-1]: return m[ks[-1]]
    for a, b in zip(ks, ks[1:]):
        if a <= f_old <= b: return m[a] + (m[b] - m[a]) * (f_old - a) / (b - a)
t = open(asset, encoding='utf-8', newline='').read(); lines = t.split('\n'); out = []; cur = None; changes = []
for ln in lines:
    mm = re.search(r'animation = "(\w+)"', ln)
    if mm: cur = mm.group(1)
    ev = re.search(r'event = \{ time = ([0-9.]+)', ln)
    if ev and cur in roles_map:
        told = float(ev.group(1)); fnew = newframe(cur, told * 30 + 1); tnew = round((fnew - 1) / 30.0, 4)
        ln2 = ln.replace(f'time = {ev.group(1)}', f'time = {tnew:.4f}', 1); changes.append((cur, told, tnew)); ln = ln2
    out.append(ln)
for c in changes: print(c)
if apply:
    with open(asset, 'w', encoding='utf-8', newline='') as fh: fh.write(chr(10).join(out))
