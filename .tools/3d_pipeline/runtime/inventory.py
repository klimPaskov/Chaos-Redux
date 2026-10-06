"""Resolve installed custom unit consumers and capture immutable batch inputs.

Sources are active .gfx/.asset files and decoded .mesh material names, never a
stale handoff. Reports are read-only; missing definitions remain visible.
"""
import argparse
import json
from pathlib import Path
import sys

from clausewitz import parse, walk
from pdx_reader import read, sha256

PIPELINE = Path(__file__).resolve().parents[1]
REPO = PIPELINE.parents[1]
VANILLA = Path(json.loads((PIPELINE / 'config/blender_hoi4_adapter.json').read_text())['vanilla_root'])


def definitions(folder, suffixes):
    rows = []
    for path in sorted(folder.rglob('*')):
        if path.suffix not in suffixes:
            continue
        try:
            tree = parse(path.read_text(encoding='utf-8-sig'))
        except (UnicodeError, ValueError) as exc:
            rows.append({'path': str(path), 'parse_error': str(exc)})
            continue
        rows.append({'path': path, 'tree': tree, 'sha256': sha256(path)})
    return rows


def file_record(path):
    return {'path': path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else str(path),
            'sha256': sha256(path), 'bytes': path.stat().st_size}


def resolve(value, owner=None):
    for candidate in [REPO / value, (owner.parent / value) if owner else REPO / value, VANILLA / value]:
        if candidate.is_file():
            return candidate.resolve()
    return None


def index_assets():
    meshes, animations, entities, sounds, effects, errors = {}, {}, {}, {}, {}, []
    for folder, suffixes in [(VANILLA / 'sound', {'.asset'}),
                             (REPO / 'gfx/entities', {'.gfx', '.asset'}),
                             (REPO / 'gfx/models/units', {'.asset', '.gfx'}),
                             (REPO / 'sound', {'.asset'})]:
        for source in definitions(folder, suffixes):
            if 'parse_error' in source:
                errors.append(source)
                continue
            for node in walk(source['tree']):
                kind = node.key
                name = node.scalar('name')
                if not name:
                    continue
                target = {'pdxmesh': meshes, 'animation': animations, 'entity': entities,
                          'sound': sounds, 'soundeffect': effects}.get(kind)
                if target is not None:
                    target[name] = {'node': node, 'path': source['path'], 'sha256': source['sha256']}
    return meshes, animations, entities, sounds, effects, errors


def action_files(mesh, animations):
    result = {}
    for node in mesh['node'].children('animation'):
        role, name = node.scalar('id'), node.scalar('type')
        if name in animations:
            definition = animations[name]
            value = definition['node'].scalar('file')
            path = resolve(value, definition['path']) if value else None
            result[role] = {'definition': name, 'file': file_record(path) if path else None,
                            'declared_file': value}
        else:
            result[role] = {'definition': name, 'file': None, 'error': 'missing_animation_definition'}
    return result


def snapshot():
    meshes, animations, entities, sounds, effects, errors = index_assets()
    records = []
    all_files = {}
    for name, definition in sorted(meshes.items()):
        value = definition['node'].scalar('file', '')
        if not value.startswith('gfx/models/units/'):
            continue
        path = resolve(value, definition['path'])
        record = {'pdxmesh': name, 'registration': file_record(definition['path']),
                  'declared_mesh': value, 'mesh': file_record(path) if path else None,
                  'actions': action_files(definition, animations), 'textures': [], 'entities': []}
        for entity_name, entity in sorted(entities.items()):
            if entity['node'].scalar('pdxmesh') == name:
                record['entities'].append({'name': entity_name, 'path': entity['path'].relative_to(REPO).as_posix(),
                                           'scale': entity['node'].scalar('scale', '1')})
        if path:
            tree, evidence = read(path)
            record['parser'] = evidence
            record['decoded_materials'] = []
            for obj in tree.find('object') or []:
                for stream in obj.findall('mesh'):
                    material = stream.find('material')
                    if material is not None:
                        record['decoded_materials'].append({'object': obj.tag, 'material': material.attrib})
            texture_values = {node.value for node in walk(definition['node'])
                              if node.key in {'texture_diffuse', 'texture_normal', 'texture_specular'} and isinstance(node.value, str)}
            record['embedded_texture_names'] = sorted({str(v) for material in record['decoded_materials']
                                                       for key in ('diff', 'n', 'spec')
                                                       for v in material['material'].get(key, []) if v})
            for tex in sorted(texture_values):
                target = resolve(tex, path)
                record['textures'].append({'declared': tex, 'file': file_record(target) if target else None})
            referenced = {path.resolve()}
            referenced.update(resolve(t['file']['path']) for t in record['textures'] if t['file'])
            referenced.update(resolve(a['file']['path']) for a in record['actions'].values() if a['file'])
            record['unreferenced_files'] = [file_record(p) for p in sorted(path.parent.iterdir())
                                             if p.suffix.lower() in {'.dds', '.mesh', '.anim'} and p.resolve() not in referenced]
        for group in ([record.get('mesh')], [t['file'] for t in record['textures']],
                      [a['file'] for a in record['actions'].values()]):
            for item in group:
                if item:
                    all_files[item['path']] = item
        records.append(record)
    # Only source files consumed by custom-unit effects are eligible for a batch.
    for record in records:
        cue_names = set()
        for row in record['entities']:
            entity = effective_entity(row['name'], entities)
            cue_names.update(n.value for n in walk(entity) if n.key == 'soundeffect' and isinstance(n.value, str))
        record['sound_cues'] = []
        for cue in sorted(cue_names):
            effect = effects.get(cue)
            sample_rows = []
            if effect:
                for node in walk(effect['node']):
                    if node.key != 'sound' or not isinstance(node.value, str):
                        continue
                    source = sounds.get(node.value)
                    value = source['node'].scalar('file') if source else None
                    target = resolve(value, source['path']) if value else None
                    item = file_record(target) if target else None
                    sample_rows.append({'name': node.value, 'declared': value, 'file': item})
                    if item:
                        all_files[item['path']] = item
            record['sound_cues'].append({'name': cue, 'loop': effect['node'].scalar('loop', 'no') if effect else None,
                                          'samples': sample_rows})
        record['additional_sound_files'] = []
        dirs = {resolve(s['file']['path']).parent for c in record['sound_cues'] for s in c['samples']
                if s['file'] and s['file']['path'].startswith('sound/')}
        for directory in sorted(dirs):
            for sound_path in sorted(directory.glob('*.wav')):
                extra = file_record(sound_path)
                record['additional_sound_files'].append(extra)
                all_files[extra['path']] = extra
    globally_referenced = set(all_files)
    for record in records:
        record['unreferenced_files'] = [item for item in record.get('unreferenced_files', [])
                                         if item['path'] not in globally_referenced]
        if record.get('mesh'):
            folder = resolve(record['mesh']['path']).parent
            record['auto_loaded_asset_files'] = [file_record(path) for path in sorted(folder.glob('*.asset'))]
            record['auxiliary_files'] = [file_record(path) for path in sorted(folder.iterdir())
                                         if path.is_file() and path.suffix not in {'.mesh', '.anim', '.dds', '.asset'}]
    return {'schema': 1, 'source': 'installed runtime files', 'models': records,
            'files': list(all_files.values()), 'parse_errors': errors}


def effective_entity(name, entities, chain=()):
    """Resolve clone inheritance, retaining repeated state alternatives."""
    from clausewitz import Node
    if name in chain or name not in entities:
        raise ValueError('Missing or recursive entity clone: ' + name)
    node = entities[name]['node']
    clone = node.scalar('clone')
    if not clone:
        return node
    base = effective_entity(clone, entities, chain + (name,))
    replaced = {n.scalar('name') for n in node.children('state')}
    own_keys = {n.key for n in node.children() if n.key != 'state'}
    inherited = [n for n in base.children() if
                 (n.key == 'state' and n.scalar('name') not in replaced) or
                 (n.key != 'state' and n.key not in own_keys)]
    return Node('entity', inherited + node.children(), node.line)


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--output', type=Path, required=True)
    args = cli.parse_args()
    data = snapshot()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'registrations': len(data['models']), 'files': len(data['files']),
                      'parse_errors': len(data['parse_errors']), 'output': str(args.output)}))
