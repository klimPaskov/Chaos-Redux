"""Extract unscaled native rows from returned production MCP artifacts."""
from pathlib import Path
import base64
import hashlib
import io
import json
import re
from PIL import Image, ImageDraw

QA = Path(__file__).resolve().parent
CACHE = Path('C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts')

def artifact(result, name):
    item = next(x for x in result['artifacts'] if x['name'] == name)
    raw = (CACHE / item['sha256'][:2] / item['sha256'] / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    return raw

cases = {}
receipts = []
for index in range(4):
    result = json.loads((QA / f'decision_cost_verified_group_{index}.json').read_text(encoding='utf8'))
    assert result['code'] == 'GUI_RENDERED'
    metadata = json.loads(artifact(result, 'decision_item-scenario-matrix.json'))
    svg = artifact(result, 'decision_item-scenario-matrix.svg').decode('utf8')
    images = re.findall(r'data:image/png;base64,([^\"]+)', svg)
    assert len(images) == len(metadata['scenarios'])
    assert base64.b64decode(images[0]) == artifact(result, 'decision_item-full.png')
    for entry, payload in zip(metadata['scenarios'], images):
        scenario = entry['scenario']
        assert not entry['fidelity']['missing'], (scenario['id'], entry['fidelity']['missing'])
        assert not entry['fidelity']['unresolved'], (scenario['id'], entry['fidelity']['unresolved'])
        raw = base64.b64decode(payload)
        image = Image.open(io.BytesIO(raw)).convert('RGBA')
        assert image.size == (1920, 1080)
        cases[scenario['id']] = (scenario, image.crop((0, 0, 512, 41)))
        receipts.append({'id': scenario['id'], 'group': index, 'source_revision': entry['sourceRevision'],
                         'native_png_sha256': hashlib.sha256(raw).hexdigest(), 'crop': [0, 0, 512, 41],
                         'resized': False, 'missing': 0, 'unresolved': 0})

for suffix, name in [('', 'decision_cost_native_custom_after.png'), ('_NATIVE_BUDGET', 'decision_cost_native_budget_after.png')]:
    selected = {key: value for key, value in cases.items() if key.endswith('_NATIVE_BUDGET') == bool(suffix)}
    ready = [(key, value) for key, value in selected.items() if key.endswith('_READY' + suffix)]
    canvas = Image.new('RGBA', (1024, len(ready) * 61 + 20), (24, 24, 24, 255))
    draw = ImageDraw.Draw(canvas)
    draw.text((4, 2), 'Ready', fill='white')
    draw.text((516, 2), 'Blocked', fill='white')
    for index, (key, (scenario, row)) in enumerate(ready):
        blocked = key.removesuffix('_READY' + suffix) + '_BLOCKED' + suffix
        y = 20 + index * 61
        draw.text((4, y), scenario['localisation'][''], fill='white')
        canvas.alpha_composite(row, (0, y + 20))
        canvas.alpha_composite(selected[blocked][1], (512, y + 20))
    canvas.save(QA / name)
(QA / 'decision_native_pixel_receipts.json').write_bytes(json.dumps({
    'scenario_count': len(receipts), 'custom_count': 28, 'native_budget_count': 24,
    'native_budget_limit': 'Width fixture only; engine concatenation order is not documented.',
    'cases': receipts
}, indent=2).encode('utf8'))
print(f'Extracted {len(receipts)} native rows with no missing or unresolved texticons.')
