from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import re

root = Path.cwd()
run = root / 'docs/testing/live_qa/20260913_main_menu_startup'
module = Path('C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh/pdx_data.py')
spec = importlib.util.spec_from_file_location('verified_pdx_data', module)
pdx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pdx)

def blocks(text, name):
    for match in re.finditer(r'\b' + name + r'\s*=\s*\{', text):
        start = match.end()
        depth = 1
        index = start
        quoted = False
        while depth:
            char = text[index]
            if char == '"':
                quoted = not quoted
            if not quoted:
                depth += (char == '{') - (char == '}')
            index += 1
        yield text[start:index - 1]

def field(text, key):
    match = re.search(r'\b' + key + r'\s*=\s*(?:"([^"]*)"|([^\s{}]+))', text)
    assert match, (key, text[:200])
    return match.group(1) if match.group(1) is not None else match.group(2)

overrides = {}
for gfx in list((root / 'gfx').rglob('*.gfx')) + list((root / 'interface').rglob('*.gfx')):
    for block in blocks(gfx.read_text(encoding='utf-8-sig'), 'pdxmesh'):
        file_name = field(block, 'file')
        settings = {}
        for setting in blocks(block, 'meshsettings'):
            key = (field(setting, 'name'), int(field(setting, 'index')))
            value = {attr: field(setting, token) for attr, token in [('diff', 'texture_diffuse'), ('n', 'texture_normal'), ('spec', 'texture_specular')]}
            assert key not in settings or settings[key] == value
            settings[key] = value
        if file_name in overrides:
            assert overrides[file_name] == settings
        overrides[file_name] = settings

def structure(node):
    return (node.tag, node.attrib, [structure(child) for child in node])

planned = []
for mesh in (root / 'gfx/models/units').rglob('*.mesh'):
    raw = mesh.read_bytes()
    if b'texture_0.dds' not in raw:
        continue
    relative = mesh.relative_to(root).as_posix()
    if relative not in overrides:
        continue
    source = pdx.read_meshfile(str(mesh))
    revised = copy.deepcopy(source)
    substitutions = []
    for shape in revised.find('object'):
        for index, stream in enumerate(shape.findall('mesh')):
            material = stream.find('material')
            for attr, generic in [('diff', 'texture_0.dds'), ('n', 'texture_normal.dds'), ('spec', 'texture_specular.dds')]:
                old = material.attrib.get(attr)
                if old != [generic]:
                    continue
                settings = overrides[relative]
                key = (shape.tag, index)
                if key in settings:
                    replacement = settings[key][attr]
                else:
                    choices = {value[attr] for value in settings.values()}
                    assert len(choices) == 1, (relative, key, choices)
                    replacement = choices.pop()
                assert (mesh.parent / replacement).is_file(), (relative, replacement)
                material.attrib[attr] = [replacement]
                substitutions.append({'object': shape.tag, 'index': index, 'field': attr, 'before': generic, 'after': replacement})
    assert substitutions, relative
    planned.append((mesh, raw, source, revised, substitutions))

receipts = []
for mesh, raw, source, revised, substitutions in planned:
    relative = mesh.relative_to(root).as_posix()
    backup = run / 'baseline/models_embedded' / relative
    backup.parent.mkdir(parents=True, exist_ok=True)
    assert not backup.exists(), backup
    backup.write_bytes(raw)
    pdx.write_meshfile(str(mesh), revised)
    reopened = pdx.read_meshfile(str(mesh))
    assert structure(reopened) == structure(revised), relative
    for change in substitutions:
        stream = reopened.find('object').find(change['object']).findall('mesh')[change['index']]
        stream.find('material').attrib[change['field']] = [change['before']]
    assert structure(reopened) == structure(source), relative
    receipts.append({'mesh': relative, 'before_sha256': hashlib.sha256(raw).hexdigest(), 'after_sha256': hashlib.sha256(mesh.read_bytes()).hexdigest(), 'substitutions': substitutions, 'all_other_parsed_fields_identical': True})

(run / 'model_evidence/embedded_texture_repair_receipt.json').write_text(json.dumps(receipts, indent=2) + '\n')
print(json.dumps({'meshes': len(receipts), 'exact_texture_substitutions': sum(len(r['substitutions']) for r in receipts), 'all_other_parsed_fields_identical': True}))
