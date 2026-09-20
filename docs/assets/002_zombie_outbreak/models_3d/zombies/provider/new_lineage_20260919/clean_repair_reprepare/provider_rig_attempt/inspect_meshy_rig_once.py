import json
import math
import os
import sys

import bpy

GLB_PATH = os.path.abspath(sys.argv[-1])
stem = os.path.splitext(os.path.basename(GLB_PATH))[0]
REPORT_PATH = os.path.join(os.path.dirname(GLB_PATH), f"{stem}_inspection.json")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB_PATH)

meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
armatures = [o for o in bpy.context.scene.objects if o.type == "ARMATURE"]
actions = []
for action in bpy.data.actions:
    fcurves = list(action.fcurves) if hasattr(action, "fcurves") else []
    actions.append({
        "name": action.name,
        "frame_start": float(action.frame_range[0]),
        "frame_end": float(action.frame_range[1]),
        "fcurves": len(fcurves),
        "keyframes": sum(len(fc.keyframe_points) for fc in fcurves),
    })

def mesh_metrics(obj):
    mesh = obj.data
    edge_use = {}
    degenerate = 0
    for poly in mesh.polygons:
        verts = list(poly.vertices)
        if len(set(verts)) < 3 or poly.area <= 1.0e-12:
            degenerate += 1
        for i, a in enumerate(verts):
            b = verts[(i + 1) % len(verts)]
            key = tuple(sorted((a, b)))
            edge_use[key] = edge_use.get(key, 0) + 1
    boundary = sum(1 for n in edge_use.values() if n == 1)
    nonmanifold = sum(1 for n in edge_use.values() if n > 2)
    weld_edge_use = {}
    for poly in mesh.polygons:
        verts = list(poly.vertices)
        points = [tuple(round(float(c), 5) for c in mesh.vertices[idx].co) for idx in verts]
        for i, point_a in enumerate(points):
            point_b = points[(i + 1) % len(points)]
            key = tuple(sorted((point_a, point_b)))
            weld_edge_use[key] = weld_edge_use.get(key, 0) + 1
    weld_boundary = sum(1 for n in weld_edge_use.values() if n == 1)
    weld_nonmanifold = sum(1 for n in weld_edge_use.values() if n > 2)
    groups = {g.name for g in obj.vertex_groups}
    arm_group_names = set()
    if armatures:
        arm_group_names = {b.name for b in armatures[0].data.bones}
    zero_weights = 0
    over_four = 0
    sums = []
    for v in mesh.vertices:
        weights = [g.weight for g in v.groups if g.group < len(obj.vertex_groups)]
        weights = [w for i, w in enumerate(weights) if w > 0.0]
        if not weights:
            zero_weights += 1
        if len(weights) > 4:
            over_four += 1
        if weights:
            sums.append(sum(weights))
    return {
        "object": obj.name,
        "vertices": len(mesh.vertices),
        "polygons": len(mesh.polygons),
        "triangles": sum(len(p.vertices) - 2 for p in mesh.polygons),
        "boundary_edges_raw": boundary,
        "non_manifold_edges_raw": nonmanifold,
        "position_welded_boundary_edges_1e-5": weld_boundary,
        "position_welded_non_manifold_edges_1e-5": weld_nonmanifold,
        "degenerate_faces": degenerate,
        "materials": [material.name if material else None for material in mesh.materials],
        "vertex_groups": len(groups),
        "armature_vertex_groups": len(groups.intersection(arm_group_names)),
        "zero_weight_vertices": zero_weights,
        "vertices_over_four_influences": over_four,
        "weight_sum_min": min(sums) if sums else None,
        "weight_sum_max": max(sums) if sums else None,
        "dimensions": [float(x) for x in obj.dimensions],
    }

report = {
    "source": GLB_PATH,
    "imported_meshes": [mesh_metrics(o) for o in meshes],
    "armatures": [
        {"name": o.name, "bones": len(o.data.bones), "bone_names": [b.name for b in o.data.bones]}
        for o in armatures
    ],
    "actions": actions,
    "objects": [{"name": o.name, "type": o.type} for o in bpy.context.scene.objects],
}
with open(REPORT_PATH, "w", encoding="utf-8") as handle:
    json.dump(report, handle, indent=2)
print(json.dumps(report, indent=2))
