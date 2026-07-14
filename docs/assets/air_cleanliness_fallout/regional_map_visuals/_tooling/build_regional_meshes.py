#!/usr/bin/env python3
"""Export Fallout-owned Air Winter PDX meshes with bound normal materials.

Run through Blender 5.1 in background mode. The installed open-source PDX mesh
exporter writes the engine binary and a text-form proof copy for inspection.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import shutil
import sys
from pathlib import Path

import bpy
from mathutils import Matrix, Vector


REPO_ROOT = Path(__file__).resolve().parents[5]
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOT = REPO_ROOT / "gfx/models/air_cleanliness_winter/regional"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
PROOF_ROOT = PACKAGE_ROOT / "mesh_exports"
PREVIEW_ROOT = PACKAGE_ROOT / "previews"
BLEND_ROOT = PACKAGE_ROOT / "source_blend"
ADDON_ROOT = Path.home() / "AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default"

if str(ADDON_ROOT) not in sys.path:
    sys.path.insert(0, str(ADDON_ROOT))

from io_pdx_mesh.pdx_blender.blender_import_export import export_meshfile  # noqa: E402


REGIONS = [
    "boreal_continental",
    "temperate_maritime",
    "mediterranean",
    "desert_arid_plateau",
    "tropical_coast_monsoon",
    "equatorial_rainforest",
    "mountain_highland",
    "island_oceanic",
    "polar_subpolar",
]

PARTICLE_FAMILIES = ["snow_frost", "cold_rain_mist", "ash_dirty_snow", "thaw_flood"]
EXPORT_RECORDS: list[dict[str, object]] = []


def clear_scene() -> None:
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def create_mesh_object(
    name: str,
    vertices: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    uvs: list[tuple[float, float]],
    face_uvs: list[tuple[int, ...]],
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for polygon, uv_indices in zip(mesh.polygons, face_uvs):
        for loop_index, uv_index in zip(polygon.loop_indices, uv_indices):
            uv_layer.data[loop_index].uv = uvs[uv_index]
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    return obj


def disc_geometry(name: str, radius: float, seed: int, rim: float) -> bpy.types.Object:
    rng = random.Random(seed)
    segments = 32
    ring_radii = (0.0, radius * 0.34, radius * 0.68, radius)
    vertices: list[tuple[float, float, float]] = [(0.0, 0.0, rim * 1.6)]
    uvs: list[tuple[float, float]] = [(0.5, 0.5)]
    ring_indices: list[list[int]] = []
    for ring_index, base_radius in enumerate(ring_radii[1:], start=1):
        indices: list[int] = []
        for segment in range(segments):
            angle = math.tau * segment / segments
            edge_noise = 1.0 + rng.uniform(-0.055, 0.055) * ring_index
            local_radius = base_radius * edge_noise
            x = math.cos(angle) * local_radius
            y = math.sin(angle) * local_radius
            wave = math.sin(angle * 3.0 + seed * 0.17) * rim * (0.34 if ring_index < 3 else 0.12)
            z = max(0.015, rim * (1.45 - ring_index * 0.34) + wave)
            vertices.append((x, y, z))
            uvs.append((0.5 + x / (radius * 2.15), 0.5 + y / (radius * 2.15)))
            indices.append(len(vertices) - 1)
        ring_indices.append(indices)

    faces: list[tuple[int, ...]] = []
    face_uvs: list[tuple[int, ...]] = []
    first = ring_indices[0]
    for segment in range(segments):
        nxt = (segment + 1) % segments
        faces.append((0, first[segment], first[nxt]))
        face_uvs.append((0, first[segment], first[nxt]))
    for inner, outer in zip(ring_indices, ring_indices[1:]):
        for segment in range(segments):
            nxt = (segment + 1) % segments
            faces.append((inner[segment], outer[segment], outer[nxt], inner[nxt]))
            face_uvs.append((inner[segment], outer[segment], outer[nxt], inner[nxt]))
    return create_mesh_object(name, vertices, faces, uvs, face_uvs)


def layered_cards(name: str, half_size: float, seed: int, horizontal: bool) -> bpy.types.Object:
    rng = random.Random(seed)
    base_vertices = [
        (-half_size, -half_size, 0.0),
        (half_size, -half_size, 0.0),
        (half_size, half_size, 0.0),
        (-half_size, half_size, 0.0),
    ]
    vertices: list[tuple[float, float, float]] = []
    faces: list[tuple[int, ...]] = []
    uvs: list[tuple[float, float]] = []
    face_uvs: list[tuple[int, ...]] = []
    uv_quad = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]

    tilts = (0.0, 14.0, -17.0) if horizontal else (46.0, 61.0, 76.0)
    for layer, tilt_degrees in enumerate(tilts):
        angle = math.radians(layer * 57.0 + rng.uniform(-6.0, 6.0))
        tilt = math.radians(tilt_degrees)
        matrix = Matrix.Translation(Vector((0.0, 0.0, 0.10 + layer * 0.10)))
        matrix @= Matrix.Rotation(angle, 4, "Z")
        matrix @= Matrix.Rotation(tilt, 4, "X")
        start_vertex = len(vertices)
        start_uv = len(uvs)
        for vertex in base_vertices:
            transformed = matrix @ Vector(vertex)
            vertices.append(tuple(transformed))
        uvs.extend(uv_quad)
        faces.append(tuple(start_vertex + index for index in range(4)))
        face_uvs.append(tuple(start_uv + index for index in range(4)))
    return create_mesh_object(name, vertices, faces, uvs, face_uvs)


def image_node(nodes: bpy.types.Nodes, path: Path, colorspace: str) -> bpy.types.Node:
    node = nodes.new("ShaderNodeTexImage")
    node.image = bpy.data.images.load(str(path), check_existing=True)
    try:
        node.image.colorspace_settings.name = colorspace
    except TypeError:
        pass
    return node


def material_for(name: str, shader: str, diff: str, spec: str, normal: str) -> bpy.types.Material:
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True
    material["shader"] = shader
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    diff_node = image_node(nodes, MODEL_ROOT / diff, "sRGB")
    spec_node = image_node(nodes, MODEL_ROOT / spec, "Non-Color")
    normal_node = image_node(nodes, MODEL_ROOT / normal, "Non-Color")
    normal_map = nodes.new("ShaderNodeNormalMap")
    normal_map.inputs["Strength"].default_value = 0.72
    bsdf.inputs["Roughness"].default_value = 0.76
    links.new(diff_node.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(spec_node.outputs["Color"], bsdf.inputs["Roughness"])
    links.new(normal_node.outputs["Color"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], bsdf.inputs["Normal"])
    if shader == "PdxMeshAlphaBlend":
        links.new(diff_node.outputs["Alpha"], bsdf.inputs["Alpha"])
        if hasattr(material, "surface_render_method"):
            material.surface_render_method = "DITHERED"
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])
    return material


def export_one(
    name: str,
    obj: bpy.types.Object,
    shader: str,
    diff: str,
    spec: str,
    normal: str,
) -> None:
    material = material_for(f"{name}_material", shader, diff, spec, normal)
    obj.data.materials.append(material)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    output = MODEL_ROOT / f"{name}.mesh"
    export_meshfile(str(output), exp_mesh=True, exp_skel=False, exp_locs=False, plain_txt=True)
    proof_source = output.with_suffix(".txt")
    proof_target = PROOF_ROOT / f"{name}.mesh.txt"
    proof_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(proof_source), str(proof_target))
    EXPORT_RECORDS.append(
        {
            "name": name,
            "shader": shader,
            "mesh": output.relative_to(REPO_ROOT).as_posix(),
            "diffuse": diff,
            "specular": spec,
            "normal": normal,
            "vertices": len(obj.data.vertices),
            "polygons": len(obj.data.polygons),
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        }
    )


def export_all() -> None:
    PROOF_ROOT.mkdir(parents=True, exist_ok=True)
    MODEL_ROOT.mkdir(parents=True, exist_ok=True)

    for region_index, region in enumerate(REGIONS):
        for phase in range(1, 7):
            clear_scene()
            name = f"air_winter_{region}_phase_{phase}"
            obj = disc_geometry(name, 9.6, region_index * 17 + phase, 0.18 + phase * 0.018)
            export_one(
                name,
                obj,
                "PdxMeshAdvanced",
                f"{name}_diff.dds",
                f"air_winter_{region}_spec.dds",
                f"air_winter_{region}_n.dds",
            )

        for family_index, family in enumerate(("dead_vegetation", "frozen_water", "thaw_flood")):
            clear_scene()
            name = f"air_winter_{region}_{family}"
            if family == "dead_vegetation":
                obj = layered_cards(name, 5.8, region_index * 41 + 3, horizontal=True)
            else:
                rim = 0.26 if family == "frozen_water" else 0.12
                obj = disc_geometry(name, 7.4, region_index * 29 + family_index, rim)
            export_one(
                name,
                obj,
                "PdxMeshAlphaBlend",
                f"{name}_diff.dds",
                f"{name}_spec.dds",
                f"{name}_n.dds",
            )

    for family_index, family in enumerate(PARTICLE_FAMILIES):
        clear_scene()
        name = f"air_winter_static_{family}"
        obj = layered_cards(name, 4.3, 170 + family_index, horizontal=False)
        export_one(
            name,
            obj,
            "PdxMeshAlphaBlend",
            f"{name}_diff.dds",
            f"{name}_spec.dds",
            f"{name}_n.dds",
        )


def point_camera(camera: bpy.types.Object, target: tuple[float, float, float]) -> None:
    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def proof_sample(
    name: str,
    location: tuple[float, float, float],
    kind: str,
    shader: str,
    diff: str,
    spec: str,
    normal: str,
    seed: int,
) -> None:
    if kind == "cards":
        obj = layered_cards(name, 3.2, seed, horizontal=True)
    elif kind == "static":
        obj = layered_cards(name, 2.6, seed, horizontal=False)
    else:
        obj = disc_geometry(name, 4.2, seed, 0.24 if kind == "ice" else 0.15)
    obj.location = location
    obj.data.materials.append(material_for(f"{name}_preview_material", shader, diff, spec, normal))


def render_proof() -> None:
    clear_scene()
    proof_sample(
        "proof_boreal_phase_4",
        (-9.0, 4.0, 0.0),
        "disc",
        "PdxMeshAdvanced",
        "air_winter_boreal_continental_phase_4_diff.dds",
        "air_winter_boreal_continental_spec.dds",
        "air_winter_boreal_continental_n.dds",
        410,
    )
    proof_sample(
        "proof_temperate_dead",
        (0.0, 4.0, 0.0),
        "cards",
        "PdxMeshAlphaBlend",
        "air_winter_temperate_maritime_dead_vegetation_diff.dds",
        "air_winter_temperate_maritime_dead_vegetation_spec.dds",
        "air_winter_temperate_maritime_dead_vegetation_n.dds",
        411,
    )
    proof_sample(
        "proof_polar_ice",
        (9.0, 4.0, 0.0),
        "ice",
        "PdxMeshAlphaBlend",
        "air_winter_polar_subpolar_frozen_water_diff.dds",
        "air_winter_polar_subpolar_frozen_water_spec.dds",
        "air_winter_polar_subpolar_frozen_water_n.dds",
        412,
    )
    proof_sample(
        "proof_tropical_thaw",
        (-4.5, -5.0, 0.0),
        "disc",
        "PdxMeshAlphaBlend",
        "air_winter_tropical_coast_monsoon_thaw_flood_diff.dds",
        "air_winter_tropical_coast_monsoon_thaw_flood_spec.dds",
        "air_winter_tropical_coast_monsoon_thaw_flood_n.dds",
        413,
    )
    proof_sample(
        "proof_static_ash",
        (5.5, -5.0, 0.0),
        "static",
        "PdxMeshAlphaBlend",
        "air_winter_static_ash_dirty_snow_diff.dds",
        "air_winter_static_ash_dirty_snow_spec.dds",
        "air_winter_static_ash_dirty_snow_n.dds",
        414,
    )

    bpy.ops.object.light_add(type="AREA", location=(0.0, -2.0, 18.0))
    key = bpy.context.object
    key.data.energy = 1700.0
    key.data.shape = "DISK"
    key.data.size = 13.0
    bpy.ops.object.light_add(type="AREA", location=(-12.0, 8.0, 9.0))
    fill = bpy.context.object
    fill.data.energy = 820.0
    fill.data.color = (0.49, 0.64, 0.82)
    fill.data.size = 10.0

    bpy.ops.object.camera_add(location=(0.0, -27.0, 25.0))
    camera = bpy.context.object
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 31.0
    point_camera(camera, (0.0, 0.0, 0.0))
    bpy.context.scene.camera = camera

    world = bpy.context.scene.world or bpy.data.worlds.new("Air Winter Preview World")
    bpy.context.scene.world = world
    world.color = (0.014, 0.019, 0.026)
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1200
    scene.render.resolution_y = 800
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.render.filepath = str(PREVIEW_ROOT / "normal_mapped_entity_material_proof.png")
    scene.view_settings.look = "AgX - Medium High Contrast"
    PREVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    BLEND_ROOT.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_ROOT / "air_winter_regional_mesh_templates.blend"))
    bpy.ops.render.render(write_still=True)


def write_report() -> None:
    expected = len(REGIONS) * 9 + len(PARTICLE_FAMILIES)
    if len(EXPORT_RECORDS) != expected:
        raise RuntimeError(f"Expected {expected} mesh exports, built {len(EXPORT_RECORDS)}")
    shaders: dict[str, int] = {}
    for record in EXPORT_RECORDS:
        shader = str(record["shader"])
        shaders[shader] = shaders.get(shader, 0) + 1
    report = {
        "mesh_count": len(EXPORT_RECORDS),
        "shaders": shaders,
        "records": EXPORT_RECORDS,
    }
    (PACKAGE_ROOT / "mesh_export_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    export_all()
    write_report()
    render_proof()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
