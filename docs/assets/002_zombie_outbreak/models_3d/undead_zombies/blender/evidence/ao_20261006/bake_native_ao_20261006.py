"""Bake and re-open a native Cycles AO map from the exact undead rest mesh.

The original checkpoint is read-only. The bake uses a temporary duplicate with
the original Armature modifier in REST position, one render-visible mesh, and a
temporary image-target material. The duplicate, temporary material and copied
world are removed before saving the evidence-only rest-pose checkpoint.
"""

import bpy
import hashlib
import json
import math
import os
from pathlib import Path
import struct


REPO = Path("C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux")
MODEL = REPO / "docs/assets/002_zombie_outbreak/models_3d/undead_zombies"
REGIONS = MODEL / "blender/evidence/regions"
AO_DIR = MODEL / "blender/evidence/ao_20261006"
SOURCE = MODEL / "blender/checkpoints/06_exported.blend"
RUNTIME_MESH = MODEL / "export/v2/chaosx_undead_zombies.mesh"
OCCUPANCY = REGIONS / "runtime_occupancy_512.png"
AO_IMAGE_PATH = AO_DIR / "undead_zombies_ao_512.png"
CHECKPOINT = MODEL / "blender/checkpoints/07_ao_baked_restpose_20261006.blend"
RECEIPT = AO_DIR / "ao_bake_receipt_20261006.json"
SCRIPT = AO_DIR / "bake_native_ao_20261006.py"
EXPECTED_SOURCE_SHA = "c7439c1af44891d480082fa85efee73f848f0a8a086bbc05e9e0676878f269bf"
EXPECTED_RUNTIME_SHA = "de3f5f66b6d724221200a883941ebcda649d880a07780f71d1820c7a2c301052"
EXPECTED_OCCUPANCY_SHA = "a8e66b00f776819691ff8b2a78f6611e005b8ec9d9d5e994fe2f5b9b480f59dc"
EXPECTED_UV_SHA = "ffc52fc345baf26d8aff6f89f2f3907bf7f7a0063b47e829715ace401c564401"
EXPECTED_COUNTS = (40875, 64933, 30474, 91422)
AO_IMAGE_NAME = "undead_zombies_ao_20261006"
TARGET_NAME = "AO_Bake_Target_rest_20261006"
TEMP_MATERIAL_NAME = "AO_Bake_Image_Target_TEMP_20261006"


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def json_write_new(path, data):
    temp = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    with open(temp, "x", encoding="utf-8", newline="\n") as stream:
        json.dump(data, stream, sort_keys=True, indent=2, ensure_ascii=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    with open(temp, "r", encoding="utf-8") as stream:
        if json.load(stream) != data:
            raise RuntimeError("validated sibling receipt did not round-trip")
    os.replace(temp, path)


def mesh_signature(mesh):
    coords = hashlib.sha256()
    edges = hashlib.sha256()
    loops = hashlib.sha256()
    uv = hashlib.sha256()
    polys = hashlib.sha256()
    layer = mesh.uv_layers.get("UVMap")
    if layer is None:
        raise RuntimeError("UVMap missing")
    for vertex in mesh.vertices:
        coords.update(struct.pack("<3f", float(vertex.co.x), float(vertex.co.y), float(vertex.co.z)))
    for edge in mesh.edges:
        edges.update(struct.pack("<2I", int(edge.vertices[0]), int(edge.vertices[1])))
    for i, loop in enumerate(mesh.loops):
        loops.update(struct.pack("<2I", int(loop.vertex_index), int(loop.edge_index)))
        value = layer.data[i].uv
        uv.update(struct.pack("<2f", float(value.x), float(value.y)))
    for poly in mesh.polygons:
        polys.update(struct.pack("<4I", int(poly.loop_start), int(poly.loop_total), int(poly.material_index), int(poly.use_smooth)))
    return {
        "counts": [len(mesh.vertices), len(mesh.edges), len(mesh.polygons), len(mesh.loops)],
        "vertex_coordinate_sha256": coords.hexdigest(),
        "edge_index_sha256": edges.hexdigest(),
        "loop_vertex_edge_sha256": loops.hexdigest(),
        "uv_loop_float32_xy_sha256": uv.hexdigest(),
        "polygon_layout_sha256": polys.hexdigest(),
    }


def weight_signature(obj):
    h = hashlib.sha256()
    for group in obj.vertex_groups:
        encoded = group.name.encode("utf-8")
        h.update(struct.pack("<I", len(encoded)))
        h.update(encoded)
    for vertex in obj.data.vertices:
        for assignment in sorted(vertex.groups, key=lambda item: item.group):
            h.update(struct.pack("<II f", int(vertex.index), int(assignment.group), float(assignment.weight)))
    return h.hexdigest()


def rig_signature(armature):
    h = hashlib.sha256()
    bones = []
    for bone in armature.data.bones:
        parent = bone.parent.name if bone.parent else None
        matrix = [float(value) for row in bone.matrix_local for value in row]
        bones.append({"name": bone.name, "parent": parent, "matrix_local": matrix, "deform": bool(bone.use_deform)})
        h.update(bone.name.encode("utf-8") + b"\0")
        h.update((parent or "").encode("utf-8") + b"\0")
        h.update(struct.pack("<16f?", *matrix, bool(bone.use_deform)))
    return h.hexdigest(), bones


def action_inventory(armature):
    result = []
    for action in sorted(bpy.data.actions, key=lambda item: item.name):
        fcurves = getattr(action, "fcurves", None)
        result.append({
            "name": action.name,
            "frame_range": [float(value) for value in action.frame_range],
            "fcurve_count": len(fcurves) if fcurves is not None else None,
            "layer_count": len(getattr(action, "layers", [])),
            "slot_count": len(getattr(action, "slots", [])),
            "slots": [{"identifier": getattr(slot, "identifier", None), "display_name": getattr(slot, "display_name", None)} for slot in getattr(action, "slots", [])],
        })
    animation = armature.animation_data
    nla = []
    if animation:
        for track in animation.nla_tracks:
            nla.append({"track": track.name, "strips": [{"name": strip.name, "action": strip.action.name if strip.action else None, "action_slot_identifier": getattr(getattr(strip, "action_slot", None), "identifier", None)} for strip in track.strips]})
    return {"actions": result, "active_action": animation.action.name if animation and animation.action else None, "nla_tracks": nla}


def evaluated_world_signature(obj):
    depsgraph = bpy.context.evaluated_depsgraph_get()
    evaluated = obj.evaluated_get(depsgraph)
    mesh = evaluated.to_mesh(preserve_all_data_layers=True, depsgraph=depsgraph)
    try:
        h = hashlib.sha256()
        points = []
        for vertex in mesh.vertices:
            value = evaluated.matrix_world @ vertex.co
            point = (float(value.x), float(value.y), float(value.z))
            points.append(point)
            h.update(struct.pack("<3f", *point))
        bounds = [[min(point[i] for point in points), max(point[i] for point in points)] for i in range(3)]
        return {"counts": [len(mesh.vertices), len(mesh.edges), len(mesh.polygons), len(mesh.loops)], "world_coordinate_sha256": h.hexdigest(), "bounds_xyz": bounds}
    finally:
        evaluated.to_mesh_clear()


def scalar_stats(values):
    if not values:
        raise RuntimeError("no occupied AO texels were found")
    ordered = sorted(values)
    def percentile(p):
        return ordered[int((len(ordered) - 1) * p)]
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return {
        "count": len(values),
        "min": min(values),
        "p05": percentile(0.05),
        "p50": percentile(0.50),
        "mean": mean,
        "p95": percentile(0.95),
        "max": max(values),
        "stddev_population": math.sqrt(variance),
        "unique_8bit_levels": len({round(value * 255.0) for value in values}),
    }


def main():
    for path in (SOURCE, RUNTIME_MESH, OCCUPANCY):
        if not path.is_file():
            raise RuntimeError("required source file is missing: " + str(path))
    for path in (AO_IMAGE_PATH, CHECKPOINT, RECEIPT):
        if path.exists():
            raise RuntimeError("refusing to overwrite prior AO output: " + str(path))
    if sha_file(SOURCE) != EXPECTED_SOURCE_SHA:
        raise RuntimeError("source checkpoint hash mismatch")
    if sha_file(RUNTIME_MESH) != EXPECTED_RUNTIME_SHA:
        raise RuntimeError("runtime mesh hash mismatch")
    if sha_file(OCCUPANCY) != EXPECTED_OCCUPANCY_SHA:
        raise RuntimeError("runtime occupancy hash mismatch")

    bpy.ops.wm.open_mainfile(filepath=str(SOURCE))
    scene = bpy.context.scene
    source_obj = bpy.data.objects.get("char1.001")
    armature = bpy.data.objects.get("Armature.001")
    if source_obj is None or armature is None:
        raise RuntimeError("source mesh or armature missing")
    if tuple((len(source_obj.data.vertices), len(source_obj.data.edges), len(source_obj.data.polygons), len(source_obj.data.loops))) != EXPECTED_COUNTS:
        raise RuntimeError("source mesh counts changed")
    source_mesh_signature = mesh_signature(source_obj.data)
    if source_mesh_signature["uv_loop_float32_xy_sha256"] != EXPECTED_UV_SHA:
        raise RuntimeError("source UV loop hash mismatch")
    source_weight_sha = weight_signature(source_obj)
    source_rig_sha, source_bones = rig_signature(armature)
    source_actions = action_inventory(armature)
    original_frame = scene.frame_current
    original_pose_position = armature.data.pose_position
    original_world = scene.world
    original_engine = scene.render.engine
    original_samples = scene.cycles.samples
    original_device = scene.cycles.device
    original_denoising = scene.cycles.use_denoising
    original_seed = scene.cycles.seed
    original_animated_seed = scene.cycles.use_animated_seed
    original_bake_type = scene.cycles.bake_type
    original_world_ao_factor = original_world.light_settings.ao_factor
    original_world_ao_distance = original_world.light_settings.distance
    original_bake = {
        "target": scene.render.bake.target,
        "margin": scene.render.bake.margin,
        "margin_type": scene.render.bake.margin_type,
        "use_clear": scene.render.bake.use_clear,
        "use_selected_to_active": scene.render.bake.use_selected_to_active,
        "use_cage": scene.render.bake.use_cage,
        "max_ray_distance": scene.render.bake.max_ray_distance,
    }
    original_visibility = {obj.name: {"hide_render": obj.hide_render, "hide_viewport": obj.hide_viewport} for obj in scene.objects}
    original_selected = [obj.name for obj in scene.objects if obj.select_get()]
    original_active = bpy.context.view_layer.objects.active.name if bpy.context.view_layer.objects.active else None
    original_materials = [slot.material for slot in source_obj.material_slots]
    original_material_names = [material.name if material else None for material in original_materials]

    world_lengths = []
    for edge in source_obj.data.edges:
        first = source_obj.matrix_world @ source_obj.data.vertices[edge.vertices[0]].co
        second = source_obj.matrix_world @ source_obj.data.vertices[edge.vertices[1]].co
        world_lengths.append((first - second).length)
    world_lengths.sort()
    p90_world_edge = float(world_lengths[int((len(world_lengths) - 1) * 0.90)])
    if not math.isfinite(p90_world_edge) or p90_world_edge <= 0.0:
        raise RuntimeError("measured AO distance is invalid")

    if bpy.data.images.get(AO_IMAGE_NAME) or bpy.data.objects.get(TARGET_NAME) or any(bpy.data.materials.get(TEMP_MATERIAL_NAME + "_" + str(index)) for index in range(len(source_obj.material_slots))):
        raise RuntimeError("AO evidence datablock name already exists in source")

    ao_image = bpy.data.images.new(AO_IMAGE_NAME, width=512, height=512, alpha=True, float_buffer=False)
    ao_image.colorspace_settings.name = "Non-Color"
    ao_image.use_fake_user = True

    target = source_obj.copy()
    target.data = source_obj.data.copy()
    target.name = TARGET_NAME
    target.data.name = TARGET_NAME + "_Mesh"
    target.animation_data_clear()
    for collection in source_obj.users_collection:
        collection.objects.link(target)
    target.matrix_world = source_obj.matrix_world.copy()
    target.hide_render = False
    target.hide_viewport = False
    if target.data.uv_layers.active is None or target.data.uv_layers.active.name != "UVMap":
        target.data.uv_layers.active = target.data.uv_layers.get("UVMap")
    target_mesh_signature = mesh_signature(target.data)
    if target_mesh_signature != source_mesh_signature:
        raise RuntimeError("isolated AO target mesh differs from source geometry/UV/topology")

    temp_materials = []
    for index in range(len(target.data.materials)):
        temp_material = bpy.data.materials.new(TEMP_MATERIAL_NAME + "_" + str(index))
        temp_material.use_nodes = True
        nodes = temp_material.node_tree.nodes
        nodes.clear()
        image_node = nodes.new("ShaderNodeTexImage")
        image_node.name = "AO_Bake_Target_Image"
        image_node.image = ao_image
        image_node.select = True
        nodes.active = image_node
        temp_materials.append(temp_material)
        target.data.materials[index] = temp_material
    if len(target.data.materials) != len(original_materials):
        raise RuntimeError("temporary target did not preserve material slot count")

    # A true rig rest evaluation yields the calibrated source height while the
    # stored source action and its keys remain untouched.
    armature.data.pose_position = "REST"
    scene.frame_set(original_frame)
    bpy.context.view_layer.update()
    source_rest_signature = evaluated_world_signature(source_obj)
    target_rest_signature = evaluated_world_signature(target)
    if source_rest_signature != target_rest_signature:
        raise RuntimeError("isolated bake target does not evaluate to the same rest geometry")
    if target_rest_signature["counts"] != list(EXPECTED_COUNTS):
        raise RuntimeError("rest evaluation changed source topology")
    rest_world_height = target_rest_signature["bounds_xyz"][2][1] - target_rest_signature["bounds_xyz"][2][0]

    bake_world = original_world.copy()
    bake_world.name = "AO_Bake_World_TEMP_20261006"
    scene.world = bake_world
    bake_world.light_settings.ao_factor = 1.0
    bake_world.light_settings.distance = p90_world_edge
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 128
    scene.cycles.use_denoising = False
    scene.cycles.seed = 0
    scene.cycles.use_animated_seed = False
    bake_type_items = [item.identifier for item in scene.cycles.bl_rna.properties["bake_type"].enum_items]
    if "AO" not in bake_type_items:
        raise RuntimeError("Cycles scene bake_type does not expose native AO")
    scene.cycles.bake_type = "AO"
    scene.render.bake.target = "IMAGE_TEXTURES"
    scene.render.bake.margin = 0
    scene.render.bake.margin_type = "EXTEND"
    scene.render.bake.use_clear = True
    scene.render.bake.use_selected_to_active = False
    scene.render.bake.use_cage = False
    scene.render.bake.max_ray_distance = 0.0

    visibility_during_bake = {}
    for scene_obj in scene.objects:
        visibility_during_bake[scene_obj.name] = {"hide_render": scene_obj.hide_render, "is_mesh": scene_obj.type == "MESH"}
        scene_obj.hide_render = True
    target.hide_render = False
    visibility_during_bake[target.name] = {"hide_render": target.hide_render, "is_mesh": True}
    bpy.ops.object.select_all(action="DESELECT")
    target.select_set(True)
    bpy.context.view_layer.objects.active = target
    bpy.context.view_layer.update()
    if not bpy.ops.object.bake.poll():
        raise RuntimeError("native object bake operator poll failed")
    bake_result = bpy.ops.object.bake(type="AO", target="IMAGE_TEXTURES", uv_layer="UVMap", margin=0, margin_type="EXTEND", use_clear=True, use_selected_to_active=False, use_cage=False, max_ray_distance=0.0)
    if "FINISHED" not in bake_result:
        raise RuntimeError("native AO bake did not finish")

    ao_image.filepath_raw = str(AO_IMAGE_PATH)
    ao_image.file_format = "PNG"
    ao_image.save()
    if not AO_IMAGE_PATH.is_file() or ao_image.size[:] != (512, 512):
        raise RuntimeError("AO PNG was not saved at 512x512")
    image_sha = sha_file(AO_IMAGE_PATH)
    ao_image.pack()
    if ao_image.packed_file is None:
        raise RuntimeError("AO image failed to pack into the checkpoint")

    # Restore shared source materials and render settings; retain REST pose in
    # this evidence-only checkpoint, leaving the immutable source file untouched.
    for index, material in enumerate(original_materials):
        target.data.materials[index] = material
    for name, state in original_visibility.items():
        scene_obj = scene.objects.get(name)
        if scene_obj is not None:
            scene_obj.hide_render = state["hide_render"]
            scene_obj.hide_viewport = state["hide_viewport"]
    bpy.data.objects.remove(target, do_unlink=True)
    if target.data.users == 0:
        bpy.data.meshes.remove(target.data)
    for temp_material in temp_materials:
        if temp_material.users == 0:
            bpy.data.materials.remove(temp_material)
    scene.world = original_world
    if bake_world.users == 0:
        bpy.data.worlds.remove(bake_world)
    scene.render.engine = original_engine
    scene.cycles.samples = original_samples
    scene.cycles.device = original_device
    scene.cycles.use_denoising = original_denoising
    scene.cycles.seed = original_seed
    scene.cycles.use_animated_seed = original_animated_seed
    scene.cycles.bake_type = original_bake_type
    original_world.light_settings.ao_factor = original_world_ao_factor
    original_world.light_settings.distance = original_world_ao_distance
    for key, value in original_bake.items():
        setattr(scene.render.bake, key, value)
    for scene_obj in scene.objects:
        scene_obj.select_set(scene_obj.name in original_selected)
    bpy.context.view_layer.objects.active = scene.objects.get(original_active) if original_active else None
    if bpy.context.view_layer.objects.active is None:
        bpy.context.view_layer.objects.active = source_obj
    source_obj.select_set(True)
    source_obj.hide_render = original_visibility[source_obj.name]["hide_render"]
    source_obj.hide_viewport = original_visibility[source_obj.name]["hide_viewport"]
    armature.data.pose_position = "REST"
    scene.frame_set(original_frame)
    bpy.context.view_layer.update()
    if [slot.material.name if slot.material else None for slot in source_obj.material_slots] != original_material_names:
        raise RuntimeError("source material slots changed during temporary bake")
    if mesh_signature(source_obj.data) != source_mesh_signature or weight_signature(source_obj) != source_weight_sha:
        raise RuntimeError("source mesh/UV/weights changed during AO authoring")
    if rig_signature(armature)[0] != source_rig_sha or action_inventory(armature) != source_actions:
        raise RuntimeError("source rig/action data changed during AO authoring")
    if scene.world is not original_world or scene.render.engine != original_engine:
        raise RuntimeError("source scene world/render engine was not restored")

    save_result = bpy.ops.wm.save_as_mainfile(filepath=str(CHECKPOINT), check_existing=False)
    if "FINISHED" not in save_result or not CHECKPOINT.is_file():
        raise RuntimeError("source-preserving AO checkpoint save failed")
    checkpoint_sha = sha_file(CHECKPOINT)

    # Independently reopen the saved evidence checkpoint before accepting the bake.
    bpy.ops.wm.open_mainfile(filepath=str(CHECKPOINT))
    reopened_obj = bpy.data.objects.get("char1.001")
    reopened_arm = bpy.data.objects.get("Armature.001")
    reopened_image = bpy.data.images.get(AO_IMAGE_NAME)
    if reopened_obj is None or reopened_arm is None or reopened_image is None:
        raise RuntimeError("reopened AO checkpoint is missing source object, armature, or packed AO image")
    reopened_mesh_signature = mesh_signature(reopened_obj.data)
    reopened_weight_sha = weight_signature(reopened_obj)
    reopened_rig_sha, _ = rig_signature(reopened_arm)
    reopened_actions = action_inventory(reopened_arm)
    reopened_world_signature = evaluated_world_signature(reopened_obj)
    if reopened_mesh_signature != source_mesh_signature or reopened_weight_sha != source_weight_sha:
        raise RuntimeError("reopened source mesh/UV/weights differ from immutable source")
    if reopened_rig_sha != source_rig_sha or reopened_actions != source_actions:
        raise RuntimeError("reopened rig/actions differ from immutable source")
    if reopened_arm.data.pose_position != "REST" or reopened_world_signature != source_rest_signature:
        raise RuntimeError("reopened checkpoint is not the measured source rest pose")
    if reopened_image.size[:] != (512, 512) or reopened_image.packed_file is None:
        raise RuntimeError("reopened AO image is not a packed 512x512 image")
    if reopened_image.colorspace_settings.name != "Non-Color":
        raise RuntimeError("reopened AO image is not marked Non-Color")
    if any(node.type == "TEX_IMAGE" and node.image == reopened_image for mat in bpy.data.materials if mat.use_nodes and mat.node_tree for node in mat.node_tree.nodes):
        raise RuntimeError("AO evidence image is unexpectedly bound to a material")
    if bpy.data.objects.get(TARGET_NAME) or any(bpy.data.materials.get(TEMP_MATERIAL_NAME + "_" + str(index)) for index in range(len(original_materials))):
        raise RuntimeError("temporary bake target/material persisted in evidence checkpoint")
    if sha_file(CHECKPOINT) != checkpoint_sha or sha_file(AO_IMAGE_PATH) != image_sha:
        raise RuntimeError("checkpoint or AO image checksum changed after reopen")

    occupancy_image = bpy.data.images.load(str(OCCUPANCY), check_existing=False)
    if occupancy_image.size[:] != (512, 512):
        raise RuntimeError("occupancy mask is not 512x512")
    occupancy_channels = occupancy_image.channels
    occupancy_pixels = occupancy_image.pixels[:]
    ao_channels = reopened_image.channels
    ao_pixels = reopened_image.pixels[:]
    if len(ao_pixels) != 512 * 512 * ao_channels or len(occupancy_pixels) != 512 * 512 * occupancy_channels:
        raise RuntimeError("image pixel buffer dimensions mismatch")
    occupied_indices = []
    for index in range(512 * 512):
        if occupancy_pixels[index * occupancy_channels] >= 0.5:
            occupied_indices.append(index)
    occupied_values = [float(ao_pixels[index * ao_channels]) for index in occupied_indices]
    occupied_index_set = set(occupied_indices)
    empty_values = [float(ao_pixels[index * ao_channels]) for index in range(512 * 512) if index not in occupied_index_set]
    rgb_max_delta = max(abs(float(ao_pixels[index * ao_channels + channel]) - float(ao_pixels[index * ao_channels])) for index in occupied_indices for channel in (1, 2))
    occupancy_image_hash = sha_file(OCCUPANCY)
    occupancy_count = len(occupied_indices)
    if occupancy_count == 0:
        raise RuntimeError("occupancy mask selected no texels")
    ao_data = {
        "path": "blender/evidence/ao_20261006/undead_zombies_ao_512.png",
        "sha256": image_sha,
        "dimensions": [512, 512],
        "format": "PNG 8-bit RGB/RGBA as saved by Blender; values are linear data, not display-regraded",
        "colorspace": reopened_image.colorspace_settings.name,
        "bake_pass": "Cycles native AO bake (bpy.ops.object.bake(type='AO'))",
        "packed_in_checkpoint": True,
        "material_binding": "unbound evidence image; no runtime material changed",
        "linear_occupied_texel_stats": scalar_stats(occupied_values),
        "linear_empty_texel_stats": scalar_stats(empty_values),
        "max_rgb_channel_delta_on_occupied": rgb_max_delta,
    }
    receipt = {
        "schema_version": 1,
        "status": "native_ao_baked_and_checkpoint_reopened_parent_review_required",
        "scope": "native geometry-derived AO only; semantic head masks remain draft and were not edited",
        "source": {
            "checkpoint_path": "blender/checkpoints/06_exported.blend",
            "checkpoint_sha256": EXPECTED_SOURCE_SHA,
            "runtime_mesh_path": "export/v2/chaosx_undead_zombies.mesh",
            "runtime_mesh_sha256": EXPECTED_RUNTIME_SHA,
            "source_uv_layer": "UVMap",
            "source_uv_sha256": EXPECTED_UV_SHA,
            "calibrated_rest_world_height": rest_world_height,
            "rest_geometry_world_coordinate_sha256": source_rest_signature["world_coordinate_sha256"],
            "source_mesh_signature": source_mesh_signature,
        },
        "lineage": {
            "protected_provider_glb_sha256": "acd462a4a6d3adc16788c82a1169e790e6e33518d21c6ce190fb44cad7575101",
            "provider_base_color_sha256": "a1cd159979ebfd5904f44a66df73d67f55aba21bfcc6fca1c3b4824d69d40717",
            "source_normal_sha256": "51443810c3fc5bf3073bc64e00c4b7df6019149a44aa0e1b4a26bdcd96eba785",
            "source_ao_map": "none; bake derives occlusion from geometry",
        },
        "bake": {
            "engine": "CYCLES",
            "device": "CPU",
            "operator": "bpy.ops.object.bake",
            "type": "AO",
            "target": "IMAGE_TEXTURES",
            "image_resolution": [512, 512],
            "image_colorspace": "Non-Color",
            "cycles_samples": 128,
            "cycles_denoising": False,
            "cycles_seed": 0,
            "ao_factor": 1.0,
            "ao_distance_world_units": p90_world_edge,
            "ao_distance_recipe": "90th percentile length of source-mesh edges transformed by the source object world matrix, measured from rest-pose source geometry",
            "edge_sample_count": len(world_lengths),
            "world_edge_p50": float(world_lengths[int((len(world_lengths) - 1) * 0.50)]),
            "world_edge_p90": p90_world_edge,
            "world_edge_p99": float(world_lengths[int((len(world_lengths) - 1) * 0.99)]),
            "margin_pixels": 0,
            "margin_type": "EXTEND (no margin applied because margin is 0)",
            "use_clear": True,
            "use_selected_to_active": False,
            "use_cage": False,
            "max_ray_distance": 0.0,
            "uv_layer": "UVMap",
            "target_visibility": {
                "only_render_visible_mesh_during_bake": TARGET_NAME,
                "target_object_render_visible": True,
                "source_and_other_scene_objects_render_hidden_during_bake": [name for name, state in visibility_during_bake.items() if name != TARGET_NAME and state["hide_render"]],
                "target_mesh_geometry_only": True,
                "original_rig_modifier_retained_on_temporary_target": True,
                "armature_pose_position_during_bake": "REST",
            },
            "temporary_target_source_mesh_signature": target_mesh_signature,
            "temporary_target_rest_world_geometry": target_rest_signature,
        },
        "occupancy": {
            "path": "blender/evidence/regions/runtime_occupancy_512.png",
            "sha256": occupancy_image_hash,
            "dimensions": [512, 512],
            "white_means_occupied": True,
            "occupied_texels": occupancy_count,
            "empty_texels": 512 * 512 - occupancy_count,
            "occupied_fraction": occupancy_count / float(512 * 512),
            "statistics_selection": "AO scalar samples at occupancy pixels >= 0.5; empty samples are reported separately",
        },
        "output": ao_data,
        "checkpoint": {
            "path": "blender/checkpoints/07_ao_baked_restpose_20261006.blend",
            "sha256": checkpoint_sha,
            "save_reopen_proof": True,
            "reopened_source_object": reopened_obj.name,
            "reopened_armature_pose_position": reopened_arm.data.pose_position,
            "reopened_rest_geometry": reopened_world_signature,
            "reopened_mesh_signature": reopened_mesh_signature,
            "reopened_weight_sha256": reopened_weight_sha,
            "reopened_rig_signature_sha256": reopened_rig_sha,
            "reopened_action_inventory": reopened_actions,
            "ao_image_exists_packed_and_unbound": True,
            "source_geometry_uv_weights_rig_actions_unchanged": True,
            "evidence_checkpoint_pose_property": "Armature.001.pose_position=REST; source actions/keys retained unchanged",
        },
        "blender_authoring_recipe_path": "blender/evidence/ao_20261006/bake_native_ao_20261006.py",
        "blender_authoring_recipe_sha256": sha_file(SCRIPT),
        "approval": "native AO bake and evidence checkpoint ready for parent review; no runtime installation or material binding",
        "runtime_installed": False,
    }
    if sha_file(CHECKPOINT) != checkpoint_sha:
        raise RuntimeError("checkpoint checksum changed before receipt write")
    json_write_new(RECEIPT, receipt)
    bpy.data.images.remove(occupancy_image, do_unlink=True)
    print(json.dumps({"status": receipt["status"], "ao_path": ao_data["path"], "ao_sha256": image_sha, "checkpoint_sha256": checkpoint_sha, "occupancy": {"occupied": occupancy_count, "fraction": occupancy_count / float(512 * 512)}, "ao_linear_occupied": ao_data["linear_occupied_texel_stats"], "distance": p90_world_edge, "receipt": str(RECEIPT.relative_to(MODEL)), "receipt_sha256": sha_file(RECEIPT)}, sort_keys=True))


main()
