"""Resolve hash-bound delivery policy and measure an existing Blender action.

This module never authors keys, weights, or bones. Policy overrides are explicit
job-local evidence, while root identity comes from the actual native skeleton.
"""
import hashlib
import json
import re
from pathlib import Path

ROLES = ('support_attack', 'training', 'retreat', 'defend', 'attack', 'death', 'move', 'idle')
CONTACT_TOLERANCE = .05
STATIONARY_TOLERANCE = .03
MEASUREMENT_UNCERTAINTY = .0001
SOLE_BAND = .025
FOOT_REGION_DOMINANT_WEIGHT = .5


def unit_delivery_job(job, asset_kind=None):
    if asset_kind is not None:
        if asset_kind not in {'static', 'static_prop', 'humanoid', 'humanoid_unit', 'creature', 'nonhumanoid_creature', 'building', 'static_building'}:
            raise ValueError('Unknown explicitly supplied asset kind.')
        return asset_kind in {'humanoid', 'humanoid_unit', 'creature', 'nonhumanoid_creature'}
    path = Path(job) / 'job.yaml'
    if not path.is_file():
        raise ValueError('Delivery gate needs the existing job profile.')
    text = path.read_text(encoding='utf-8')
    try:
        profile = json.loads(text).get('profile', '')
    except ValueError:
        match = re.search(r'^profile:\s*["\']?([a-z_]+)', text, re.M)
        profile = match.group(1) if match else ''
    if not profile:
        raise ValueError('Delivery gate cannot determine the declared job profile.')
    return profile not in {'building', 'static_building', 'equipment', 'static_prop'}


def action_policy(job, action_name, source_sha256):
    path = Path(job) / 'validation' / 'animation_delivery_policy.json'
    role = next((r for r in ROLES if action_name.casefold().endswith('_' + r) or action_name.casefold() == r), None)
    policy = {'role': role, 'looped': role != 'death', 'root_policy': 'in_place_xy_preserve_z',
              'strike_windows': [], 'humanoid': None, 'source': 'conservative role defaults',
              'source_sha256': source_sha256}
    if path.exists():
        document = json.loads(path.read_text(encoding='utf-8'))
        row = document.get('actions', {}).get(action_name)
        if row:
            if row.get('source_sha256', '').casefold() != source_sha256.casefold():
                raise ValueError('Animation delivery policy is bound to a different source checkpoint.')
            if not isinstance(row.get('looped'), bool) or row.get('role') not in ROLES:
                raise ValueError('Explicit animation policy requires role and looped boolean.')
            for key in ('role', 'looped', 'strike_windows', 'humanoid'):
                if key in row:
                    policy[key] = row[key]
            policy['source'] = str(path)
            policy['policy_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    if policy['role'] is None:
        raise ValueError('An action with a custom name requires a hash-bound animation_delivery_policy.json role.')
    return policy


def existing_foot_world_samples(rig, bpy, start, end):
    """Return actual native ankle positions, explicitly insufficient sole proof."""
    names = {side: next((bone.name for bone in rig.pose.bones
                         if side in bone.name.casefold() and 'foot' in bone.name.casefold()), None)
             for side in ('left', 'right')}
    if any(name is None for name in names.values()):
        return {'status': 'unmeasured', 'reason': 'No exact left/right foot bones; anatomy mapping required.'}
    old_frame, old_subframe = bpy.context.scene.frame_current, bpy.context.scene.frame_subframe
    samples = []
    try:
        for frame in range(start, end + 1):
            bpy.context.scene.frame_set(frame)
            bpy.context.view_layer.update()
            samples.append({'frame': frame, 'bones': {side: {'bone': name,
                'world_position': list((rig.matrix_world @ rig.pose.bones[name].matrix).translation)}
                for side, name in names.items()}})
    finally:
        bpy.context.scene.frame_set(old_frame, subframe=old_subframe)
        bpy.context.view_layer.update()
    return {'status': 'ankle_positions_measured', 'samples': samples,
            'axes': 'Blender world Z up', 'limitation': 'Ankle positions do not prove sole contact or planting; provide reviewed foot-world contact measurements.'}


def native_skeleton_tree(rig):
    """Describe actual existing bone parent indices and inverse rest matrices."""
    from xml.etree.ElementTree import Element, SubElement
    from io_pdx_mesh.pdx_blender.blender_import_export import swap_coord_space
    tree = Element('File')
    skeleton = SubElement(tree, 'skeleton')
    bones = list(rig.data.bones)
    indices = {bone.name: index for index, bone in enumerate(bones)}
    for bone in bones:
        inverse = swap_coord_space(rig.matrix_world @ bone.matrix_local).inverted()
        attributes = {'ix': [indices[bone.name]], 'tx': [float(inverse[row][column]) for column in range(4) for row in range(3)]}
        if bone.parent is not None:
            attributes['pa'] = [indices[bone.parent.name]]
        SubElement(skeleton, bone.name, attributes)
    return tree


def measured_sole_contacts(rig, objects, bpy, start, end):
    """Measure actual evaluated sole geometry from existing foot/toe weights.

No ankle proxy and no generated contact curve is accepted. A missing or weak
foot region remains unmeasured. Armature-only meshes retain vertex identity.
"""
    regions = {'left': [], 'right': []}
    for obj in objects:
        if any(modifier.type != 'ARMATURE' for modifier in obj.modifiers):
            return None
        for side in regions:
            groups = {group.index for group in obj.vertex_groups if side in group.name.casefold()
                      and any(token in group.name.casefold() for token in ('foot', 'toe'))}
            vertices = [vertex.index for vertex in obj.data.vertices
                        if sum(group.weight for group in vertex.groups if group.group in groups) > FOOT_REGION_DOMINANT_WEIGHT]
            if vertices:
                regions[side].append((obj, vertices))
    if any(not rows for rows in regions.values()):
        return None
    ground = min((obj.matrix_world @ vertex.co).z for obj in objects for vertex in obj.data.vertices)
    old_frame, old_subframe = bpy.context.scene.frame_current, bpy.context.scene.frame_subframe
    feet = {side: {'bone': side + ' existing foot/toe weighted sole geometry', 'world_positions': []} for side in regions}
    try:
        for frame in range(start, end + 1):
            bpy.context.scene.frame_set(frame)
            bpy.context.view_layer.update()
            graph = bpy.context.evaluated_depsgraph_get()
            evaluated = {}
            try:
                for obj in objects:
                    native = obj.evaluated_get(graph)
                    mesh = native.to_mesh()
                    if len(mesh.vertices) != len(obj.data.vertices):
                        return None
                    evaluated[obj] = (native, mesh)
                for side, rows in regions.items():
                    points = [evaluated[obj][0].matrix_world @ evaluated[obj][1].vertices[index].co
                              for obj, indices in rows for index in indices]
                    bottom = min(point.z for point in points)
                    sole = [point for point in points if point.z <= bottom + SOLE_BAND]
                    feet[side]['world_positions'].append([sum(point.x for point in sole) / len(sole),
                                                          sum(point.y for point in sole) / len(sole), bottom])
            finally:
                for native, mesh in evaluated.values():
                    native.to_mesh_clear()
    finally:
        bpy.context.scene.frame_set(old_frame, subframe=old_subframe)
        bpy.context.view_layer.update()
    return {'feet': feet, 'ground_plane': {'normal': [0, 0, 1], 'offset': ground},
            'contact_tolerance': CONTACT_TOLERANCE, 'stationary_tolerance': STATIONARY_TOLERANCE,
            'measurement_uncertainty': MEASUREMENT_UNCERTAINTY, 'min_contact_frames': 2}
