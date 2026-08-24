"""Synthetic Blender integration proof for material-preserving weight-only cleanup."""

from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path

import bpy


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import blender_worker  # noqa: E402


def reset_scene() -> None:
    bpy.ops.object.mode_set(mode="OBJECT") if bpy.context.object and bpy.context.object.mode != "OBJECT" else None
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for data_collection in (bpy.data.meshes, bpy.data.armatures, bpy.data.materials, bpy.data.images):
        for block in list(data_collection):
            data_collection.remove(block)


def make_material() -> bpy.types.Material:
    material = bpy.data.materials.new("ProviderMaterial")
    material.use_nodes = True
    material["chaosx_pdx_shader"] = "PdxMeshAdvanced"
    nodes = material.node_tree.nodes
    nodes.clear()
    principled = nodes.new("ShaderNodeBsdfPrincipled")
    principled.name = "ProviderPrincipled"
    output = nodes.new("ShaderNodeOutputMaterial")
    output.name = "ProviderOutput"
    texture = nodes.new("ShaderNodeTexImage")
    texture.name = "ProviderDiffuseImage"
    image = bpy.data.images.new("ProviderDiffuse", width=2, height=2, alpha=True)
    image.filepath = "//provider_diffuse.png"
    image.colorspace_settings.name = "sRGB"
    texture.image = image
    material.node_tree.links.new(texture.outputs["Color"], principled.inputs["Base Color"])
    material.node_tree.links.new(principled.outputs["BSDF"], output.inputs["Surface"])
    principled.inputs["Metallic"].default_value = 0.73
    principled.inputs["Alpha"].default_value = 0.41
    emission = principled.inputs.get("Emission Color") or principled.inputs.get("Emission")
    if emission is not None:
        emission.default_value = (0.2, 0.3, 0.4, 1.0)
    emission_strength = principled.inputs.get("Emission Strength")
    if emission_strength is not None:
        emission_strength.default_value = 0.62
    return material


def make_armature() -> bpy.types.Object:
    data = bpy.data.armatures.new("GuardRigData")
    armature = bpy.data.objects.new("GuardRig", data)
    bpy.context.scene.collection.objects.link(armature)
    bpy.context.view_layer.objects.active = armature
    armature.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    parent = None
    for index in range(5):
        bone = data.edit_bones.new(f"Bone{index}")
        bone.head = (0.0, 0.0, float(index))
        bone.tail = (0.0, 0.0, float(index + 1))
        bone.parent = parent
        parent = bone
    bpy.ops.object.mode_set(mode="OBJECT")
    for bone in data.bones:
        bone["pdxIgnoreJoint"] = True
    armature["chaosx_working"] = True
    return armature


def make_body(armature: bpy.types.Object, material: bpy.types.Material) -> bpy.types.Object:
    mesh = bpy.data.meshes.new("GuardBodyMesh")
    mesh.from_pydata(
        [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)],
        [(0, 1), (1, 2), (2, 0)],
        [(0, 1, 2)],
    )
    body = bpy.data.objects.new("GuardBody", mesh)
    bpy.context.scene.collection.objects.link(body)
    body["chaosx_working"] = True
    mesh.materials.append(material)
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for loop, uv in zip(uv_layer.data, ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))):
        loop.uv = uv
    modifier = body.modifiers.new("GuardRig", "ARMATURE")
    modifier.object = armature
    for bone, weight in zip(armature.data.bones, (0.40, 0.30, 0.20, 0.10, 0.05)):
        group = body.vertex_groups.new(name=bone.name)
        group.add([0, 1, 2], weight, "REPLACE")
    return body


def make_weapon(armature: bpy.types.Object, material: bpy.types.Material) -> bpy.types.Object:
    mesh = bpy.data.meshes.new("GuardWeaponMesh")
    mesh.from_pydata(
        [(0.0, 0.0, 0.0), (0.3, 0.0, 0.0), (0.0, 0.1, 0.0)],
        [(0, 1), (1, 2), (2, 0)],
        [(0, 1, 2)],
    )
    weapon = bpy.data.objects.new("GuardWeapon", mesh)
    bpy.context.scene.collection.objects.link(weapon)
    mesh.materials.append(material)
    weapon.location = (0.25, -0.5, 1.75)
    weapon.rotation_euler = (0.1, 0.2, 0.3)
    weapon.parent = armature
    weapon.parent_type = "BONE"
    weapon.parent_bone = "Bone4"
    weapon["chaosx_weapon"] = True
    return weapon


def protected_surface_snapshot() -> dict[str, object]:
    body = bpy.data.objects["GuardBody"]
    weapon = bpy.data.objects["GuardWeapon"]
    armature = bpy.data.objects["GuardRig"]
    material = bpy.data.materials["ProviderMaterial"]
    principled = material.node_tree.nodes["ProviderPrincipled"]
    emission = principled.inputs.get("Emission Color") or principled.inputs.get("Emission")
    emission_strength = principled.inputs.get("Emission Strength")
    return {
        "body_vertices": [tuple(vertex.co) for vertex in body.data.vertices],
        "body_edges": [tuple(edge.vertices) for edge in body.data.edges],
        "body_polygons": [tuple(polygon.vertices) for polygon in body.data.polygons],
        "body_uvs": [tuple(loop.uv) for layer in body.data.uv_layers for loop in layer.data],
        "material_slots": [slot.material.name if slot.material else None for slot in body.material_slots],
        "material_nodes": sorted((node.name, node.bl_idname) for node in material.node_tree.nodes),
        "material_links": sorted(
            (link.from_node.name, link.from_socket.name, link.to_node.name, link.to_socket.name)
            for link in material.node_tree.links
        ),
        "image_reference": (
            material.node_tree.nodes["ProviderDiffuseImage"].image.name,
            material.node_tree.nodes["ProviderDiffuseImage"].image.filepath,
        ),
        "metallic": principled.inputs["Metallic"].default_value,
        "alpha": principled.inputs["Alpha"].default_value,
        "emission": tuple(emission.default_value) if emission is not None else None,
        "emission_strength": emission_strength.default_value if emission_strength is not None else None,
        "skeleton": [
            (
                bone.name,
                bone.parent.name if bone.parent else None,
                tuple(bone.head_local),
                tuple(bone.tail_local),
                bool(bone["pdxIgnoreJoint"]),
            )
            for bone in armature.data.bones
        ],
        "weapon_vertices": [tuple(vertex.co) for vertex in weapon.data.vertices],
        "weapon_matrix_world": tuple(tuple(row) for row in weapon.matrix_world),
        "weapon_parent": weapon.parent.name if weapon.parent else None,
        "weapon_parent_type": weapon.parent_type,
        "weapon_parent_bone": weapon.parent_bone,
    }


def main() -> None:
    reset_scene()
    material = make_material()
    armature = make_armature()
    make_body(armature, material)
    make_weapon(armature, material)
    with tempfile.TemporaryDirectory(prefix="chaosx_weight_only_") as temp_dir:
        job = Path(temp_dir)
        source = job / "source.blend"
        output = job / "output.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(source))
        bpy.ops.wm.open_mainfile(filepath=str(source))
        before = protected_surface_snapshot()
        report = blender_worker.sanitize_runtime_candidate(
            {
                "job_root": str(job),
                "payload": {
                    "blend_rel": "source.blend",
                    "output_blend_rel": "output.blend",
                    "target_height_m": None,
                    "weight_only": True,
                    "max_influences_per_vertex": 2,
                },
            }
        )
        assert output.exists()
        assert report["weight_only"] is True
        assert report["materials"] == {
            "applied": False,
            "policy": "preserve_checkpoint_materials",
            "objects": [],
        }

        bpy.ops.wm.open_mainfile(filepath=str(output))
        after = protected_surface_snapshot()
        assert after == before
        body = bpy.data.objects["GuardBody"]
        for vertex in body.data.vertices:
            weights = [assignment.weight for assignment in vertex.groups if assignment.weight > 0.0]
            assert len(weights) == 2
            assert math.isclose(sum(weights), 1.0, rel_tol=0.0, abs_tol=1e-6)
        assert all(bool(bone["pdxIgnoreJoint"]) for bone in bpy.data.objects["GuardRig"].data.bones)
        preserved_material = bpy.data.materials["ProviderMaterial"]
        assert "ProviderDiffuseImage" in preserved_material.node_tree.nodes
        preserved_principled = preserved_material.node_tree.nodes["ProviderPrincipled"]
        assert math.isclose(preserved_principled.inputs["Metallic"].default_value, 0.73, abs_tol=1e-6)
        assert math.isclose(preserved_principled.inputs["Alpha"].default_value, 0.41, abs_tol=1e-6)
        assert preserved_material.node_tree.nodes["ProviderDiffuseImage"].image.name == "ProviderDiffuse"
        assert bpy.data.objects["GuardWeapon"].parent_bone == "Bone4"
        assert report["max_influences_per_vertex"] == 2
        print(json.dumps({"status": "pass", "protected_surfaces_preserved": True}, sort_keys=True))


if __name__ == "__main__":
    main()
