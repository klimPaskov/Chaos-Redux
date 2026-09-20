import math
import os
import sys

import bpy
from mathutils import Vector

GLB_PATH = os.path.abspath(sys.argv[-1])
OUT_DIR = os.path.dirname(GLB_PATH)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB_PATH)

for obj in bpy.context.scene.objects:
    if obj.type == "MESH" and obj.name.lower() != "char1":
        obj.hide_render = True
        obj.hide_viewport = True
    if obj.type == "ARMATURE":
        obj.hide_render = True

character = bpy.data.objects.get("char1")
if character is None:
    raise RuntimeError("Meshy rig import did not create char1")

scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 512
scene.render.resolution_y = 512
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.film_transparent = False
scene.world = bpy.data.worlds.new("MeshyRigReviewWorld")
scene.world.color = (0.035, 0.04, 0.035)

def look_at(camera, target):
    camera.rotation_euler = (Vector(target) - camera.location).to_track_quat("-Z", "Y").to_euler()

def add_area(name, location, energy, size, color):
    data = bpy.data.lights.new(name=name, type="AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    data.color = color
    obj = bpy.data.objects.new(name, data)
    scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, (0.0, 0.0, 0.9))
    return obj

plane_data = bpy.data.meshes.new("MeshyRigReviewGround")
plane_data.from_pydata([(-4,-4,0),(4,-4,0),(4,4,0),(-4,4,0)], [], [(0,1,2,3)])
plane_data.update()
plane = bpy.data.objects.new("MeshyRigReviewGround", plane_data)
scene.collection.objects.link(plane)
mat = bpy.data.materials.new("MeshyRigReviewGroundMaterial")
mat.diffuse_color = (0.12, 0.14, 0.12, 1.0)
mat.use_nodes = True
mat.node_tree.nodes.get("Principled BSDF").inputs["Base Color"].default_value = (0.12,0.14,0.12,1.0)
mat.node_tree.nodes.get("Principled BSDF").inputs["Roughness"].default_value = 0.82
plane.data.materials.append(mat)

add_area("Key", (3.5, -4.0, 5.0), 850.0, 4.0, (0.86, 0.95, 0.84))
add_area("Fill", (-3.0, -1.0, 2.5), 420.0, 3.0, (0.48, 0.56, 0.48))
add_area("Rim", (0.0, 3.5, 4.0), 600.0, 3.0, (0.42, 0.50, 0.44))

camera_data = bpy.data.cameras.new("MeshyRigReviewCamera")
camera = bpy.data.objects.new("MeshyRigReviewCamera", camera_data)
scene.collection.objects.link(camera)
scene.camera = camera
camera_data.lens = 58

target = (0.0, 0.0, 0.9)
views = {
    "front": (0.0, -5.8, 1.8),
    "left": (-5.8, 0.0, 1.8),
    "three_quarter": (4.7, -4.7, 2.0),
}
is_walking = "walking" in os.path.basename(GLB_PATH).lower()
prefix = "w" if is_walking else "s"
view_tokens = {"front": "fr", "left": "l", "three_quarter": "q"}
frames = [1, 13, 25] if is_walking else [0]
for frame in frames:
    scene.frame_set(frame)
    for view, location in views.items():
        camera.location = location
        look_at(camera, target)
        suffix = f"_{frame:03d}" if is_walking else ""
        scene.render.filepath = os.path.join(OUT_DIR, f"{prefix}{suffix}_{view_tokens[view]}.png")
        bpy.ops.render.render(write_still=True)

scene.render.filepath = os.path.join(OUT_DIR, "meshy_rig_once_review.blend")
bpy.ops.wm.save_as_mainfile(filepath=scene.render.filepath)
print("Rendered Meshy rig review to", OUT_DIR)
