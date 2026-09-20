"""Render five phases and four views of each actual exported PDX zombie action."""

import bpy
import hashlib
import json
from mathutils import Vector
from pathlib import Path


JOB = Path(__file__).resolve().parents[2]
BASE = JOB / "provider" / "user_selected_exact_20260920"
OUTPUT = BASE / "final_reimport_review"
OUTPUT.mkdir(parents=True, exist_ok=True)
MATERIAL_BLEND = BASE / "blender" / "checkpoints" / "46b_exact_reference_pdx_material.blend"
VIEWS = {
    "front": Vector((0, -13, 1)),
    "left": Vector((-13, 0, 1)),
    "back": Vector((0, 13, 1)),
    "three_quarter": Vector((8, -11, 1)),
}


def point_at(obj, target):
    obj.rotation_euler = (target - obj.location).to_track_quat("-Z", "Y").to_euler()


def bounds(obj):
    evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
    mesh = evaluated.to_mesh()
    points = [evaluated.matrix_world @ vertex.co for vertex in mesh.vertices]
    evaluated.to_mesh_clear()
    return (
        Vector(tuple(min(point[axis] for point in points) for axis in range(3))),
        Vector(tuple(max(point[axis] for point in points) for axis in range(3))),
    )


report = {"material_blend": str(MATERIAL_BLEND), "roles": {}}
for role in ("idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"):
    proof = JOB / "blender" / "checkpoints" / f"reimport_exact_selected_{role}.blend"
    bpy.ops.wm.open_mainfile(filepath=str(proof))
    scene = bpy.context.scene
    model = next(obj for obj in scene.objects if obj.type == "MESH")
    rig = next(obj for obj in scene.objects if obj.type == "ARMATURE")
    action = rig.animation_data.action
    if action is None:
        raise ValueError(f"No imported animation for {role}")
    with bpy.data.libraries.load(str(MATERIAL_BLEND), link=False) as (_, destination):
        destination.materials = ["ZombieExactPdxMaterial"]
    material = destination.materials[0]
    if material is None:
        raise ValueError("Exact-reference PDX material did not load")
    texture_hashes = {}
    for node in material.node_tree.nodes:
        if node.type != "TEX_IMAGE" or node.image is None:
            continue
        filename = Path(bpy.path.abspath(node.image.filepath)).name
        path = BASE / "textures" / "dds" / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        node.image.filepath = str(path)
        node.image.reload()
        texture_hashes[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
    if len(texture_hashes) != 3:
        raise ValueError(f"Expected three exact-reference DDS maps: {texture_hashes}")
    for slot in model.material_slots:
        slot.material = material
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.world.color = (0.12, 0.12, 0.12)
    for position, energy, size in (((4, -6, 10), 1800, 7), ((-5, 4, 7), 1400, 7)):
        bpy.ops.object.light_add(type="AREA", location=position)
        lamp = bpy.context.object
        lamp.data.energy = energy
        lamp.data.shape = "DISK"
        lamp.data.size = size
        point_at(lamp, Vector((0, 0, 3.3)))
    bpy.ops.object.camera_add()
    camera = bpy.context.object
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 11.8
    scene.camera = camera
    first, last = action.frame_range
    record = {
        "proof": str(proof.relative_to(JOB)).replace("\\", "/"),
        "triangles": len(model.data.polygons),
        "bones": len(rig.data.bones),
        "frame_range": [first, last],
        "textures_sha256": texture_hashes,
        "frames": [],
    }
    role_dir = OUTPUT / role
    role_dir.mkdir(parents=True, exist_ok=True)
    for fraction in (0.0, 0.25, 0.5, 0.75, 1.0):
        frame = first + (last - first) * fraction
        scene.frame_set(int(frame), subframe=frame % 1)
        minimum, maximum = bounds(model)
        center = (minimum + maximum) / 2
        for name, offset in VIEWS.items():
            camera.location = center + offset
            point_at(camera, center)
            path = role_dir / f"{int(fraction * 100):03d}_{name}.png"
            scene.render.filepath = str(path)
            bpy.ops.render.render(write_still=True)
            record["frames"].append(str(path.relative_to(JOB)).replace("\\", "/"))
    report["roles"][role] = record
    print("RENDERED", role, len(record["frames"]), flush=True)
(BASE / "blender" / "reports" / "exact_reference_actual_byte_visual_review.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
