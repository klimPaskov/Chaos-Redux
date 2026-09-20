"""SHA-bound removal of explicitly reviewed isolated duplicate face groups."""

import json
import re
from pathlib import Path


def _safe_mesh_name(value):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]{0,127}", value):
        raise ValueError("Require one exact safe mesh name.")
    return value


def _validate_face_groups(face_groups):
    if not isinstance(face_groups, list) or not 1 <= len(face_groups) <= 32:
        raise ValueError("Require 1-32 explicit duplicate face groups.")
    normalized = []
    seen = set()
    for group in face_groups:
        if (
            not isinstance(group, list)
            or len(group) < 2
            or len(group) > 8
            or any(type(index) is not int or index < 0 for index in group)
            or len(set(group)) != len(group)
        ):
            raise ValueError("Duplicate face groups require 2-8 unique non-negative indices.")
        ordered = tuple(sorted(group))
        if ordered in seen:
            raise ValueError("Duplicate face group repeated.")
        seen.add(ordered)
        normalized.append(list(ordered))
    return normalized


def _protected_fingerprint(h, job, mesh_name):
    """Exclude only the target mesh's geometry and derived object bounds."""

    sections = h["_promotion_fingerprint"](job, [], include_sections=True)["sections"]
    sections["geometry"].pop(mesh_name, None)
    target_object = sections["objects"].get(mesh_name)
    if target_object is not None:
        target_object.pop("dimensions", None)
        target_object.pop("bounds", None)
    return json.dumps(sections, sort_keys=True, separators=(",", ":"))


def remove_explicit_duplicate_faces(req, h):
    """Remove only complete, isolated duplicate face groups and orphaned geometry."""

    bpy = h["bpy"]
    p = req["payload"]
    job = Path(req["job_root"]).resolve()
    source = h["within"](job, p["blend_rel"])
    output = h["within"](job, p["checkpoint_rel"], allow_missing=True)
    expected_source = p.get("expected_source_sha256")
    if (
        not isinstance(expected_source, str)
        or not re.fullmatch(r"[A-Fa-f0-9]{64}", expected_source)
        or h["file_sha256"](source) != expected_source.upper()
    ):
        raise ValueError("Source SHA-256 mismatch.")
    if (
        source.suffix != ".blend"
        or output.suffix != ".blend"
        or output.parent != source.parent
        or output == source
        or output.exists()
    ):
        raise ValueError("Require a new sibling .blend checkpoint.")
    mesh_name = _safe_mesh_name(p.get("mesh_name"))
    face_groups = _validate_face_groups(p.get("face_groups"))
    report_path = job / "blender" / "reports" / (output.stem + ".json")
    if report_path.exists():
        raise FileExistsError("Duplicate-face repair report already exists; choose a new sibling name.")

    bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
    mesh = bpy.context.scene.objects.get(mesh_name)
    if (
        mesh is None
        or mesh.type != "MESH"
        or not mesh.get("chaosx_working")
        or mesh.library
        or mesh.override_library
        or mesh.data.library
        or mesh.data.users != 1
        or mesh.data.shape_keys
        or mesh.get("chaosx_source_protected")
        or mesh.get("chaosx_reference_read_only")
    ):
        raise ValueError("Require one unique local approved working mesh.")

    polygons = mesh.data.polygons
    groups_by_vertices = {}
    for polygon in polygons:
        key = tuple(sorted(int(index) for index in polygon.vertices))
        groups_by_vertices.setdefault(key, []).append(int(polygon.index))
    requested = {index for group in face_groups for index in group}
    remove_indices = set()
    validated_groups = []
    edge_faces = {}
    for polygon in polygons:
        vertices = list(polygon.vertices)
        for a, b in zip(vertices, vertices[1:] + vertices[:1]):
            edge_faces.setdefault(tuple(sorted((int(a), int(b)))), []).append(int(polygon.index))

    for group in face_groups:
        if any(index >= len(polygons) for index in group):
            raise ValueError("Duplicate face index is outside the reviewed source mesh.")
        keys = {tuple(sorted(int(index) for index in polygons[index].vertices)) for index in group}
        if len(keys) != 1:
            raise ValueError("Every reviewed duplicate group must use one exact vertex triplet.")
        key = next(iter(keys))
        observed = sorted(groups_by_vertices.get(key, []))
        if observed != group:
            raise ValueError("Reviewed group is not the complete duplicate face group.")
        if len(key) != 3:
            raise ValueError("Only triangular duplicate face groups are supported.")
        for a, b in zip(key, key[1:] + key[:1]):
            edge = tuple(sorted((a, b)))
            if sorted(edge_faces.get(edge, [])) != group:
                raise ValueError("Duplicate group is not an isolated closed component.")
        remove_indices.update(group)
        validated_groups.append({"face_indices": group, "vertex_indices": list(key)})

    before_protected = _protected_fingerprint(h, job, mesh_name)
    before_geometry = h["geometry_metrics"]()
    import bmesh

    bm = bmesh.new()
    bm.from_mesh(mesh.data)
    bm.faces.ensure_lookup_table()
    bmesh.ops.delete(bm, geom=[bm.faces[index] for index in sorted(remove_indices)], context="FACES_ONLY")
    bm.edges.ensure_lookup_table()
    for edge in list(bm.edges):
        if not edge.link_faces:
            bm.edges.remove(edge)
    for vertex in list(bm.verts):
        if not vertex.link_edges and not vertex.link_faces:
            bm.verts.remove(vertex)
    bm.verts.index_update()
    bm.edges.index_update()
    bm.faces.index_update()
    bm.normal_update()
    bm.to_mesh(mesh.data)
    bm.free()
    mesh.data.update()
    after_geometry = h["geometry_metrics"]()
    if after_geometry["loose_boundary_edges"] or after_geometry["non_manifold_edges"] or after_geometry["degenerate_faces"]:
        raise RuntimeError("Duplicate-face removal left an open, non-manifold, or degenerate working mesh.")
    after_protected = _protected_fingerprint(h, job, mesh_name)
    if after_protected != before_protected:
        raise RuntimeError("Duplicate-face removal changed protected materials, rig, actions, or scene data.")

    h["save_blend"](output)
    bpy.ops.wm.open_mainfile(filepath=str(output), use_scripts=False)
    reopened_geometry = h["geometry_metrics"]()
    if reopened_geometry["loose_boundary_edges"] or reopened_geometry["non_manifold_edges"] or reopened_geometry["degenerate_faces"]:
        raise RuntimeError("Reopened duplicate-face checkpoint is not closed and manifold.")
    if _protected_fingerprint(h, job, mesh_name) != before_protected:
        raise RuntimeError("Reopened duplicate-face checkpoint changed protected data.")
    if h["file_sha256"](source) != expected_source.upper():
        raise RuntimeError("Immutable duplicate-face source changed.")

    report = {
        "operation": "remove_explicit_duplicate_faces",
        "status": "reopened_invariants_passed_requires_visual_export_review",
        "source": p["blend_rel"],
        "source_sha256": expected_source.upper(),
        "checkpoint": p["checkpoint_rel"],
        "checkpoint_sha256": h["file_sha256"](output),
        "mesh": mesh_name,
        "reviewed_groups": validated_groups,
        "removed_face_count": len(remove_indices),
        "geometry_before": before_geometry,
        "geometry_after": reopened_geometry,
        "protected_fingerprint": before_protected,
        "reopened_verified": True,
        "new_provider_call": False,
        "source_immutable": True,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report["report"] = report_path.relative_to(job).as_posix()
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report
