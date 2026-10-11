"""python wire2.py <spec.json>
spec: {"unit":..., "body_node":"Mesh_0.001","body_streams":4,"items":[{"node":..,"index":0,"stem":..}],
       "events":{state:[times]}  (rewrites existing event times in order),
       "events_full":{state:[[time,"a"|"i"],...]} (replaces the weapon attack/impact events of the state)}
Rewrites the unit's meshsettings blocks in gfx/entities/014_cannibalism_units.gfx and the event times of the listed states in the entity of gfx/entities/014_cannibalism_units.asset."""
import re, sys, json
from pathlib import Path
MOD = Path(r"<mod root>")
NL = chr(10)
TAB = chr(9)
spec = json.load(open(sys.argv[1]))
u = spec['unit']
g = MOD / 'gfx/entities/014_cannibalism_units.gfx'
t = open(g, encoding='utf-8', newline='').read()
i = t.index(f'name = "{u}_mesh"')
nxt = t.find(TAB + 'pdxmesh = {', i + 10)
j = nxt if nxt >= 0 else t.rindex(chr(10) + '}')  # keep the file's closing brace (the last mesh block would otherwise swallow it)
blk = t[i:j]
k = blk.index(TAB * 2 + 'meshsettings = {')
head = blk[:k]


def ms(name, index, stem):
    lines = [TAB * 2 + 'meshsettings = {', TAB * 3 + f'name = "{name}"', TAB * 3 + f'index = {index}',
             TAB * 3 + f'texture_diffuse = "{stem}_diffuse.dds"', TAB * 3 + f'texture_specular = "{stem}_specular.dds"',
             TAB * 3 + f'texture_normal = "{stem}_normal.dds"', TAB * 3 + 'shader = "PdxMeshAdvanced"', TAB * 2 + '}']
    return NL.join(lines) + NL


body = ''.join(ms(spec['body_node'], n, u) + NL for n in range(spec['body_streams']))
items = ''.join(ms(it['node'], it.get('index', 0), it['stem']) + NL for it in spec.get('items', []))
new = head + (body + items).rstrip(NL) + NL + TAB + '}' + NL + NL
t = t[:i] + new + t[j:]
open(g, 'w', encoding='utf-8', newline=NL).write(t)

a = MOD / 'gfx/entities/014_cannibalism_units.asset'
at = open(a, encoding='utf-8', newline='').read()
e0 = at.index(f'name = "{u}_entity"')
e1 = at.index(NL + 'entity = {', e0 + 10)
eb = at[e0:e1]


def state_bounds(eb, state):
    s0 = eb.index(f'name = "{state}"')
    n1 = eb.find(TAB + 'state = {', s0)
    s1 = n1 if n1 >= 0 else eb.index(TAB + 'scale', s0)
    return s0, s1


for state, times in spec.get('events', {}).items():
    s0, s1 = state_bounds(eb, state)
    sb = eb[s0:s1]
    it = iter(times)

    def rep(m):
        try:
            return f'event = {{ time = {next(it):.4f} '
        except StopIteration:
            return m.group(0)
    sb2 = re.sub(r'event = \{ time = [0-9.]+ ', rep, sb)
    eb = eb[:s0] + sb2 + eb[s1:]

for state, rows in spec.get('events_full', {}).items():
    s0, s1 = state_bounds(eb, state)
    sb = eb[s0:s1]
    lines = sb.split(NL)
    keep = [l for l in lines if 'weapon_attack_sfx' not in l and 'weapon_impact_sfx' not in l]
    idx = max(n for n, l in enumerate(keep) if 'next_state' in l or 'looping' in l)
    newl = []
    for tm, kind in rows:
        which = 'attack' if kind == 'a' else 'impact'
        newl.append(TAB * 2 + f'event = {{ time = {tm:.4f} sound = {{ soundeffect = "{u}_weapon_{which}_sfx" }} }}')
    keep[idx + 1:idx + 1] = newl
    eb = eb[:s0] + NL.join(keep) + eb[s1:]

at = at[:e0] + eb + at[e1:]
open(a, 'w', encoding='utf-8', newline=NL).write(at)
print('wired', u)
