"""Install only reported small-unit aliases and two compact resource texticons."""
from pathlib import Path
import hashlib
import json
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
VANILLA = Path('C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

inventory = json.loads((QA / 'reported_error_inventory.json').read_text(encoding='utf8'))
names = [re.search(r'texticon: (unit_\w+_icon_small)\|1', row['message']).group(1)
         for row in inventory['messages'] if 'texticon:' in row['message']]
registry = {}
for path in (ROOT / 'interface').glob('*.gfx'):
    source = path.read_text(encoding='utf-8-sig')
    for block in re.findall(r'spriteType\s*=\s*\{[^{}]*\}', source, re.I):
        name = re.search(r'name\s*=\s*"([^"]+)"', block)
        texture = re.search(r'texturefile\s*=\s*"([^"]+)"', block, re.I)
        if name and texture:
            registry[name.group(1)] = (path, texture.group(1))

reference = VANILLA / 'gfx/texticons/unit_infantry_icon_small.dds'
assert Image.open(reference).size == (60, 12)
rows = []
blocks = ['# Reported CXT roster texticons use their existing two-frame unit artwork.', 'spriteTypes = {']
sheet = Image.new('RGBA', (380, len(names) * 20 + 40), (30, 30, 30, 255))
from PIL import ImageDraw
draw = ImageDraw.Draw(sheet)
for index, name in enumerate(names):
    base = name.removesuffix('_icon_small')
    family = base
    if base.startswith('unit_rat_'):
        family = 'unit_black_plague_rat'
    elif base in ('unit_death_weak_ghost_host', 'unit_death_last_shore_ghost_host'):
        family = 'unit_death_ghost'
    definition, texture = registry['GFX_' + family + '_icon_medium_white']
    path = ROOT / texture
    image = Image.open(path).convert('RGBA')
    assert image.size == (60, 12), (name, texture, image.size)
    assert image.getextrema()[3][1] == 255
    blocks.append(f'\tspriteType = {{ name = "GFX_{name}" texturefile = "{texture}" noOfFrames = 2 legacy_lazy_load = no }}')
    rows.append({'name': 'GFX_' + name, 'texture': texture, 'definition': str(definition.relative_to(ROOT)),
                 'sha256': sha(path), 'size': [60, 12], 'frames': 2, 'family': family,
                 'alpha_range': list(image.getextrema()[3]),
                 'operation': 'exact existing unit-family texture alias'})
    draw.text((4, index * 20), name, fill='white')
    sheet.alpha_composite(image, (310, index * 20 + 2))

resources = [
    ('cbrn_instruments_texticon', 'gfx/interface/technologies/stage_2_protective_equipment/equipment/cbrn_instrument_equipment_1.dds', (32, 13)),
    ('medical_capacity_texticon', 'gfx/interface/decisions/biowarfare/countermeasures/decision_bio_expand_medical_capacity.dds', (18, 18)),
]
for index, (name, source, size) in enumerate(resources):
    destination = ROOT / 'gfx/texticons' / (name + '.dds')
    assert not destination.exists(), destination
    image = Image.open(ROOT / source).convert('RGBA').resize(size, Image.Resampling.LANCZOS)
    image.save(destination)
    reopened = Image.open(destination).convert('RGBA')
    assert reopened.tobytes() == image.tobytes()
    blocks.append(f'\tspriteType = {{ name = "GFX_{name}" texturefile = "gfx/texticons/{name}.dds" legacy_lazy_load = no }}')
    rows.append({'name': 'GFX_' + name, 'texture': str(destination.relative_to(ROOT)).replace('\\', '/'),
                 'source': source, 'source_sha256': sha(ROOT / source), 'sha256': sha(destination),
                 'size': list(size), 'frames': 1, 'operation': 'existing matching resource artwork resized with alpha preserved'})
    y = len(names) * 20 + index * 20
    draw.text((4, y), name, fill='white')
    sheet.alpha_composite(reopened, (310, y))
blocks.append('}')
destination = ROOT / 'interface/chaosx_missing_unit_texticons.gfx'
assert not destination.exists()
destination.write_bytes(('\n'.join(blocks) + '\n').encode('utf8'))
sheet.save(QA / 'texticon_native_contact_sheet.png')
(QA / 'texticon_source_checks.json').write_bytes(json.dumps({
    'vanilla_reference': str(reference), 'vanilla_sha256': sha(reference),
    'registry': str(destination.relative_to(ROOT)), 'registry_sha256': sha(destination),
    'reported_unit_count': len(names), 'resource_count': len(resources), 'rows': rows,
    'review': 'native 60x12 unit strips and 32x13/18x18 resources, unscaled contact sheet'
}, indent=2).encode('utf8'))
print(f'Installed {len(names)} exact unit-family aliases and {len(resources)} resource texticons.')
