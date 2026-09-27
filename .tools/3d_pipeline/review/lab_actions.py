"""Live Blender Lab helpers for reviewing and correcting skeletal actions.

Import inside a Blender Lab ``execute_blender_code`` call:

    import sys; sys.path.insert(0, r"<mod>/.tools/3d_pipeline/review"); import lab_actions as la

These helpers only carry out an edit the agent has decided on after visual review; none of
them invents motion. Keys written by ``pose_bone_directions`` are exactly the target bone
directions the agent authored; ``ground_action`` offsets the root by the measured floor error.

- ``bind_action(rig, action)``: assign an action and its first slot (Blender 5 slotted actions).
- ``fix_slot_identifiers(rig, prefix)``: rename action slots so they bind to ``rig``; a slot
  identifier that differs from ``OB<rig name>`` silently exports an unanimated ``.anim``.
- ``floor_scan(rig, meshes, action)``: per-frame lowest vertex height.
- ``ground_action(rig, meshes, source, new_name, target=0.004)``: copy ``source`` and key the root
  bone location on every frame so the lowest vertex sits at ``target`` (removes provider float,
  hops, and floor sinking). Review the result; a deliberate jump would be flattened.
- ``pose_bone_directions(rig, action, frame, directions)``: key bones so each points along an
  authored armature-space direction, parent first, keeping quaternion continuity.
- ``copy_action(name, new_name)``: fake-user copy for non-destructive iteration.
- ``clear_nla_and_drivers()``: run before saving an export checkpoint; partition refuses NLA/driver scenes.
"""
import bpy
import mathutils
from mathutils import Matrix, Quaternion, Vector


def bind_action(rig, action):
    rig.animation_data_create()
    rig.animation_data.action = action
    if action.slots:
        rig.animation_data.action_slot = action.slots[0]


def fcurves(action):
    return action.layers[0].strips[0].channelbag(action.slots[0]).fcurves


def fix_slot_identifiers(rig, prefix=""):
    changed = []
    for act in bpy.data.actions:
        if act.name.startswith(prefix) and act.slots and act.slots[0].identifier != "OB" + rig.name:
            act.slots[0].name_display = rig.name
            changed.append(act.name)
    return changed


def clear_nla_and_drivers():
    """Remove NLA tracks and drivers left by action swaps; the adapter's partition and
    promotion steps refuse "driver/NLA proof scenes". Returns the objects cleaned."""
    cleaned = []
    for obj in bpy.data.objects:
        ad = obj.animation_data
        if ad and (ad.nla_tracks or ad.drivers):
            for track in list(ad.nla_tracks):
                ad.nla_tracks.remove(track)
            for drv in list(ad.drivers):
                ad.drivers.remove(drv)
            cleaned.append(obj.name)
    return cleaned


def copy_action(name, new_name):
    old = bpy.data.actions.get(new_name)
    if old:
        bpy.data.actions.remove(old)
    act = bpy.data.actions[name].copy()
    act.name = new_name
    act.use_fake_user = True
    return act


def _lowest(meshes):
    dg = bpy.context.evaluated_depsgraph_get()
    return min(min((o.evaluated_get(dg).matrix_world @ v.co).z for v in o.evaluated_get(dg).data.vertices) for o in meshes)


def floor_scan(rig, meshes, action):
    bind_action(rig, action)
    f0, f1 = map(int, action.frame_range)
    out = []
    for f in range(f0, f1 + 1):
        bpy.context.scene.frame_set(f)
        out.append((f, _lowest(meshes)))
    return out


def ground_action(rig, meshes, source, new_name, target=0.004, root="Hips"):
    act = copy_action(source, new_name)
    bind_action(rig, act)
    scale = rig.matrix_world.to_scale().z
    pb = rig.pose.bones[root]
    f0, f1 = map(int, act.frame_range)
    offsets, base = {}, {}
    for f in range(f0, f1 + 1):
        bpy.context.scene.frame_set(f)
        offsets[f] = target - _lowest(meshes)
        # Capture the ungrounded pose first: when the bone has sparse keys (a vehicle or creature
        # root), a key inserted at frame f changes the interpolated pose at f + 1, and adding the
        # offset to that would stack every earlier offset.
        base[f] = pb.matrix.copy()
    for f, dz in offsets.items():
        bpy.context.scene.frame_set(f)
        m = base[f].copy()
        m.translation.z += dz / scale
        pb.matrix = m
        bpy.context.view_layer.update()
        pb.keyframe_insert("location", frame=f)
    after = [z for _, z in floor_scan(rig, meshes, act)]
    return {"action": new_name, "offset_range": [min(offsets.values()), max(offsets.values())], "after_min_max": [min(after), max(after)]}


def ground_all(rig, meshes, prefix, roles, target=0.004, root="Hips"):
    """Ground every <prefix>_<role> action, keep the ungrounded provider copy as
    provider_<prefix>_<role>_ungrounded, then repair slots and clear NLA tracks so the
    checkpoint is ready for partitioning. Returns per-role offset ranges."""
    out = {}
    for role in roles:
        name = f"{prefix}_{role}"
        out[role] = ground_action(rig, meshes, name, name + "_grounded", target, root)
        bpy.data.actions[name].name = f"provider_{name}_ungrounded"
        bpy.data.actions[name + "_grounded"].name = name
    out["slots_fixed"] = fix_slot_identifiers(rig, prefix)
    out["nla_cleared"] = clear_nla_and_drivers()
    # Provider FBX imports can leave zero-user packed images; Blender drops them on save, which the
    # partition step reports as "changed image content or image datablock identities".
    # Remove every image that no material node uses (a first orphan's ".001" twin survives a
    # users==0 sweep), keeping viewer images.
    for mat in [m for m in bpy.data.materials if m.users == 0]:
        bpy.data.materials.remove(mat)   # FBX imports leave orphan materials that keep their images "used"
    used = set()
    for mat in bpy.data.materials:
        if mat.node_tree:
            used |= {n.image.name for n in mat.node_tree.nodes if n.type == "TEX_IMAGE" and n.image}
    orphans = [im.name for im in bpy.data.images if im.source != "VIEWER" and im.name not in used]
    for name in orphans:
        bpy.data.images.remove(bpy.data.images[name])
    out["orphan_images_removed"] = orphans
    bind_action(rig, bpy.data.actions[f"{prefix}_{roles[0]}"])
    return out


def _prev_quat(action, bone, frame):
    fcs = fcurves(action)
    comps = []
    for i in range(4):
        fc = next((c for c in fcs if c.data_path == f'pose.bones["{bone}"].rotation_quaternion' and c.array_index == i), None)
        if fc is None:
            return None
        comps.append(fc.evaluate(frame - 1))
    return Quaternion(comps)


def pose_bone_directions(rig, action, frame, directions):
    """directions: ordered {bone_name: (x, y, z)} in armature space, parents before children."""
    bind_action(rig, action)
    bpy.context.scene.frame_set(frame)
    errors = {}
    for bone, target in directions.items():
        pb = rig.pose.bones[bone]
        goal = Vector(target).normalized()
        cur = (pb.tail - pb.head).normalized()
        q = cur.rotation_difference(goal)
        head = pb.head.copy()
        pb.matrix = Matrix.Translation(head) @ q.to_matrix().to_4x4() @ Matrix.Translation(-head) @ pb.matrix
        bpy.context.view_layer.update()
        prev = _prev_quat(action, bone, frame)
        if prev is not None and pb.rotation_quaternion.dot(prev) < 0:
            pb.rotation_quaternion.negate()
        pb.keyframe_insert("rotation_quaternion", frame=frame)
        errors[bone] = round(((pb.tail - pb.head).normalized()).angle(goal) * 57.2958, 3)
    return errors
