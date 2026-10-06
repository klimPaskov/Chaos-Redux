"""Read-only PDX mesh topology evidence for delivery and repair review.

Positional tolerances describe hypothetical weld topology only. This module
never changes vertex positions, faces, normals, or the source PDX tree.
"""
from __future__ import annotations

import ast
import math
from collections import defaultdict, deque


DEFAULT_POSITIONAL_TOLERANCES = (0.0005, 0.001, 0.002)
PROVIDER_INTAKE_BOUNDARY_CEILING = 200


def _sequence(value, label):
    if isinstance(value, (list, tuple)):
        return list(value)
    if isinstance(value, str):
        try:
            parsed = ast.literal_eval(value)
        except (ValueError, SyntaxError) as exc:
            raise ValueError(f"{label} is not a decoded PDX array.") from exc
        if isinstance(parsed, (list, tuple)):
            return list(parsed)
    raise ValueError(f"{label} is not a decoded PDX array.")


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must contain finite numeric values.")
    return float(value)


def _vectors(values, width, label):
    flat = _sequence(values, label)
    if len(flat) % width:
        raise ValueError(f"{label} length must be divisible by {width}.")
    return [tuple(_number(value, label) for value in flat[index:index + width])
            for index in range(0, len(flat), width)]


def _triangles(values, vertex_count):
    flat = _sequence(values, "mesh.tri")
    if len(flat) % 3:
        raise ValueError("mesh.tri length must be divisible by three.")
    result = []
    for index in range(0, len(flat), 3):
        row = flat[index:index + 3]
        if any(type(value) is not int or value < 0 or value >= vertex_count for value in row):
            raise ValueError("mesh.tri contains an invalid vertex index.")
        result.append(tuple(row))
    return result


class _UnionFind:
    def __init__(self, count):
        self.parent = list(range(count))
        self.rank = [0] * count

    def find(self, value):
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left, right):
        left, right = self.find(left), self.find(right)
        if left == right:
            return
        if self.rank[left] < self.rank[right]:
            left, right = right, left
        self.parent[right] = left
        if self.rank[left] == self.rank[right]:
            self.rank[left] += 1


def _neighbor_cells(cell):
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                yield cell[0] + x, cell[1] + y, cell[2] + z


def _positional_clusters(positions, tolerance):
    if tolerance == 0:
        exact = {}
        aliases = []
        for index, point in enumerate(positions):
            exact.setdefault(point, index)
            aliases.append(exact[point])
        return aliases
    union = _UnionFind(len(positions))
    cells, exact_first = defaultdict(list), {}
    tolerance_sq = tolerance * tolerance
    for index, point in enumerate(positions):
        exact_previous = exact_first.get(point)
        if exact_previous is not None:
            union.union(index, exact_previous)
            continue
        exact_first[point] = index
        cell = tuple(math.floor(value / tolerance) for value in point)
        for neighbor in _neighbor_cells(cell):
            for other in cells.get(neighbor, ()):
                if sum((point[axis] - positions[other][axis]) ** 2 for axis in range(3)) <= tolerance_sq:
                    union.union(index, other)
        cells[cell].append(index)
    roots = [union.find(index) for index in range(len(positions))]
    first_index_by_root = {}
    for index, root in enumerate(roots):
        first_index_by_root.setdefault(root, index)
    stable_ids = {root: ordinal for ordinal, root in enumerate(sorted(first_index_by_root, key=first_index_by_root.__getitem__))}
    return [stable_ids[root] for root in roots]


def _unit_normal(normal):
    length = math.sqrt(sum(value * value for value in normal))
    if length <= 1e-12:
        return None
    return tuple(value / length for value in normal)


def _normal_split_report(positions, aliases, normals, angular_tolerance_degrees):
    if normals is None:
        return {"status": "unavailable", "reason": "PDX mesh has no decoded normal buffer"}
    if len(normals) != len(positions):
        return {"status": "unavailable", "reason": "normal and position vertex counts differ",
                "position_vertices": len(positions), "normal_vectors": len(normals)}
    groups = defaultdict(list)
    for index, alias in enumerate(aliases):
        normalized = _unit_normal(normals[index])
        if normalized is not None:
            groups[alias].append((index, normalized))
    split_groups = []
    for alias, rows in groups.items():
        directions = []
        for index, normal in rows:
            if not any(math.degrees(math.acos(max(-1.0, min(1.0, sum(a * b for a, b in zip(normal, old)))))) <= angular_tolerance_degrees for old in directions):
                directions.append(normal)
        if len(directions) > 1:
            split_groups.append({"positional_vertex": alias, "vertex_indices": [row[0] for row in rows],
                                 "distinct_normal_directions": len(directions), "normal_angular_tolerance_degrees": angular_tolerance_degrees})
    return {"status": "reported", "positional_vertex_groups_with_split_normals": len(split_groups),
            "split_normal_vertex_index_count": sum(len(row["vertex_indices"]) for row in split_groups),
            "groups": split_groups[:64], "groups_truncated": len(split_groups) > 64,
            "normal_angular_tolerance_degrees": angular_tolerance_degrees,
            "policy": "count distinct normal directions among vertices joined only by the positional diagnostic tolerance; no normal changes"}


def _topology_at_tolerance(positions, triangles, tolerance, normals, normal_tolerance):
    aliases = _positional_clusters(positions, tolerance)
    cluster_positions = {}
    members = defaultdict(list)
    for index, alias in enumerate(aliases):
        members[alias].append(index)
        cluster_positions.setdefault(alias, positions[index])

    edges = defaultdict(list)
    face_ids = []
    face_keys = {}
    degenerate_faces = []
    duplicate_faces = []
    duplicate_orientations = {"same": 0, "opposed": 0, "other": 0}
    for face_index, tri in enumerate(triangles):
        face = tuple(aliases[index] for index in tri)
        if len(set(face)) != 3:
            degenerate_faces.append(face_index)
        else:
            a, b, c = (cluster_positions[value] for value in face)
            cross = ((b[1] - a[1]) * (c[2] - a[2]) - (b[2] - a[2]) * (c[1] - a[1]),
                     (b[2] - a[2]) * (c[0] - a[0]) - (b[0] - a[0]) * (c[2] - a[2]),
                     (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))
            if math.sqrt(sum(value * value for value in cross)) <= 2e-14:
                degenerate_faces.append(face_index)
        canonical_key = tuple(sorted(face))
        if canonical_key in face_keys:
            first_index, first_face = face_keys[canonical_key]
            duplicate_faces.append(face_index)
            forward = any(face == tuple(first_face[index:] + first_face[:index]) for index in range(3))
            reverse = tuple(reversed(face))
            backward = any(reverse == tuple(first_face[index:] + first_face[:index]) for index in range(3))
            duplicate_orientations["same" if forward else "opposed" if backward else "other"] += 1
        else:
            face_keys[canonical_key] = (face_index, face)
        face_ids.append(face)
        for left, right in zip(face, face[1:] + face[:1]):
            if left != right:
                edges[tuple(sorted((left, right)))].append((face_index, left, right))

    boundary = {key: rows for key, rows in edges.items() if len(rows) == 1}
    manifold = {key: rows for key, rows in edges.items() if len(rows) == 2}
    nonmanifold = {key: rows for key, rows in edges.items() if len(rows) > 2}
    same_direction = sum(rows[0][1:] == rows[1][1:] for rows in manifold.values())
    opposed_direction = len(manifold) - same_direction

    adjacency = [[] for _ in triangles]
    for rows in edges.values():
        if len(rows) > 1:
            anchor = rows[0][0]
            for row in rows[1:]:
                adjacency[anchor].append(row[0])
                adjacency[row[0]].append(anchor)
    seen, components = set(), []
    nonmanifold_faces = {row[0] for rows in nonmanifold.values() for row in rows}
    boundary_faces = {row[0] for rows in boundary.values() for row in rows}
    face_to_component = {}
    for seed in range(len(triangles)):
        if seed in seen:
            continue
        queue, group = deque([seed]), []
        seen.add(seed)
        while queue:
            current = queue.popleft()
            group.append(current)
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        component_id = len(components)
        for face_index in group:
            face_to_component[face_index] = component_id
        used = sorted({vertex for index in group for vertex in face_ids[index]})
        components.append({"component": component_id, "triangle_count": len(group),
                           "triangle_index_preview": group[:32], "boundary_edge_count": 0,
                           "nonmanifold_edge_count": 0, "nonmanifold_edge_examples": [],
                           "ambiguous_for_orientation_repair": False})

    for edge, rows in boundary.items():
        components[face_to_component[rows[0][0]]]["boundary_edge_count"] += 1
    for edge, rows in nonmanifold.items():
        component = components[face_to_component[rows[0][0]]]
        component["nonmanifold_edge_count"] += 1
        component["ambiguous_for_orientation_repair"] = True
        if len(component["nonmanifold_edge_examples"]) < 16:
            component["nonmanifold_edge_examples"].append({"positional_vertices": list(edge), "incident_face_count": len(rows)})

    edge_examples = [{"positional_vertices": list(edge), "incident_face_count": len(rows),
                      "incident_face_indices": [row[0] for row in rows[:16]], "face_indices_truncated": len(rows) > 16}
                     for edge, rows in list(nonmanifold.items())[:64]]
    merged_count = len(positions) - len(members)
    return {"tolerance_units": tolerance, "source_position_count": len(positions),
            "hypothetical_positional_vertex_count": len(members), "hypothetical_vertex_merge_count": merged_count,
            "weld_applied": False, "face_count": len(triangles), "edge_count": len(edges),
            "boundary_edge_count": len(boundary), "manifold_edge_count": len(manifold),
            "nonmanifold_edge_count": len(nonmanifold), "nonmanifold_edge_examples": edge_examples,
            "nonmanifold_edge_examples_truncated": len(nonmanifold) > len(edge_examples),
            "nonmanifold_face_count": len(nonmanifold_faces), "boundary_face_count": len(boundary_faces),
            "degenerate_face_count": len(set(degenerate_faces)), "degenerate_face_indices": sorted(set(degenerate_faces))[:64],
            "duplicate_face_count": len(duplicate_faces), "duplicate_face_indices": duplicate_faces[:64],
            "duplicate_face_indices_truncated": len(duplicate_faces) > 64,
            "duplicate_face_orientation_counts": duplicate_orientations,
            "same_direction_manifold_edges": same_direction, "opposed_direction_manifold_edges": opposed_direction,
            "components": components,
            "split_normals": _normal_split_report(positions, aliases, normals, normal_tolerance),
            "policy": "read-only transitive positional adjacency; no vertex/face/normal edit"}


def inspect_geometry_delivery(positions, triangles, *, normals=None,
                              positional_tolerances=DEFAULT_POSITIONAL_TOLERANCES,
                              normal_angular_tolerance_degrees=1.0, provider_intake=True,
                              manifold_required=False):
    """Return topology diagnostics at 0.0005-0.002-unit hypothetical weld radii."""
    if not isinstance(positions, (list, tuple)) or not 1 <= len(positions) <= 1_000_000:
        raise ValueError("Geometry inspection requires 1-1,000,000 source positions.")
    normalized_positions = []
    for point in positions:
        if not isinstance(point, (list, tuple)) or len(point) != 3:
            raise ValueError("Geometry positions must be numeric triples.")
        normalized_positions.append(tuple(_number(value, "position") for value in point))
    if not isinstance(triangles, (list, tuple)) or not 1 <= len(triangles) <= 200_000:
        raise ValueError("Geometry inspection requires 1-200,000 indexed triangles.")
    normalized_triangles = []
    for face in triangles:
        if not isinstance(face, (list, tuple)) or len(face) != 3 or any(type(index) is not int or index < 0 or index >= len(normalized_positions) for index in face):
            raise ValueError("Geometry faces must be indexed triangles.")
        normalized_triangles.append(tuple(face))
    normalized_normals = None
    if normals is not None:
        if not isinstance(normals, (list, tuple)):
            raise ValueError("Normals must be a sequence of numeric triples.")
        normalized_normals = []
        for normal in normals:
            if not isinstance(normal, (list, tuple)) or len(normal) != 3:
                raise ValueError("Normals must be numeric triples.")
            normalized_normals.append(tuple(_number(value, "normal") for value in normal))
    if type(provider_intake) is not bool or type(manifold_required) is not bool:
        raise ValueError("provider_intake and manifold_required must be boolean values.")
    normal_angular_tolerance_degrees = _number(normal_angular_tolerance_degrees, "normal_angular_tolerance_degrees")
    if not 0 <= normal_angular_tolerance_degrees <= 180:
        raise ValueError("normal angular tolerance must be between 0 and 180 degrees.")
    tolerances = tuple(_number(value, "positional_tolerance") for value in positional_tolerances)
    if not tolerances or any(not 0.0005 <= value <= 0.002 for value in tolerances) or tuple(sorted(set(tolerances))) != tolerances:
        raise ValueError("Positional tolerances must be unique, ascending values from 0.0005 through 0.002 units.")

    topology = [_topology_at_tolerance(normalized_positions, normalized_triangles, tolerance,
                                       normalized_normals, normal_angular_tolerance_degrees)
                for tolerance in tolerances]
    measured_boundary_max = max(row["boundary_edge_count"] for row in topology)
    intake_pass = measured_boundary_max < PROVIDER_INTAKE_BOUNDARY_CEILING
    winding = _winding_report(normalized_positions, normalized_triangles)
    clean_topology = all(row["boundary_edge_count"] == 0 and row["nonmanifold_edge_count"] == 0 and
                         row["degenerate_face_count"] == 0 and row["duplicate_face_count"] == 0 for row in topology)
    clean_winding = winding.get("status") == "pass" and not winding.get("flip_face_indices")
    clean = clean_topology and clean_winding
    if manifold_required:
        status = "pass" if clean else "blocked"
    elif provider_intake and not intake_pass:
        status = "blocked"
    else:
        status = "pass" if clean else "review_required"
    return {"status": status, "read_only": True, "source_geometry_mutated": False,
            "provider_intake_boundary_ceiling_exclusive": PROVIDER_INTAKE_BOUNDARY_CEILING,
            "provider_intake_boundary_gate": {"status": "pass" if intake_pass else "blocked",
                "evaluated_tolerance_units": "all_requested_tolerances",
                "boundary_edge_count_by_tolerance": [{"tolerance_units": row["tolerance_units"], "boundary_edge_count": row["boundary_edge_count"]} for row in topology],
                "worst_boundary_edge_count": measured_boundary_max},
            "manifold_export_gate": {"status": "pass" if clean else "blocked" if manifold_required else "not_accepted",
                "reason": "manifold, duplicate-free, nondegenerate and already outward-oriented topology required before export",
                "winding_status": winding.get("status"), "planned_flip_count": len(winding.get("flip_face_indices", ()))},
            "positional_weld_tolerances_units": list(tolerances), "topology_by_tolerance": topology,
            "winding_report": winding,
            "limitations": ["split-normal groups are positional diagnostics, not an automatic smoothing prescription",
                            "nonmanifold topology is reported in full and remains ambiguous for orientation repair"]}


def _winding_report(positions, triangles):
    try:
        from .mesh_winding_repair import plan_consistent_outward_winding
    except ImportError:
        from mesh_winding_repair import plan_consistent_outward_winding
    try:
        return plan_consistent_outward_winding(positions, triangles, adjacency_mode="exact_positions")
    except ValueError as exc:
        return {"status": "blocked", "error": str(exc), "policy": "winding planner rejected ambiguous duplicate/degenerate input"}


def _mesh_nodes(tree):
    if getattr(tree, "tag", None) != "File":
        raise ValueError("Mesh inspection requires an io_pdx_mesh File tree.")
    return [node for node in tree.iter() if node.tag == "mesh"]


def inspect_pdx_mesh_tree(tree, *, positional_tolerances=DEFAULT_POSITIONAL_TOLERANCES,
                          provider_intake=True, manifold_required=False):
    """Inspect logical PDX mesh objects, combining their material streams.

    PDX mesh nodes below one named object are material/vertex-buffer streams
    over the same object surface. They are combined with offset indices for
    topology and winding; per-stream capacities remain separate evidence.
    """
    object_roots = [node for node in tree if node.tag == "object"]
    if not object_roots:
        raise ValueError("Decoded PDX tree contains no object block.")
    results, stream_counter = [], 0
    for object_root_index, object_root in enumerate(object_roots):
        logical_groups = []
        for child in object_root:
            nodes = [child] if child.tag == "mesh" else [node for node in child.iter() if node.tag == "mesh"]
            if nodes:
                logical_groups.append((child.tag, child, nodes))
        for object_name, owner, streams in logical_groups:
            combined_positions, combined_normals, combined_triangles = [], [], []
            stream_rows = []
            normals_complete = True
            for node in streams:
                positions = _vectors(node.get("p"), 3, f"{object_name}.stream[{stream_counter}].p")
                triangles = _triangles(node.get("tri"), len(positions))
                offset = len(combined_positions)
                combined_positions.extend(positions)
                combined_triangles.extend(tuple(index + offset for index in face) for face in triangles)
                raw_normals = _vectors(node.get("n"), 3, f"{object_name}.stream[{stream_counter}].n") if node.get("n") is not None else None
                if raw_normals is None:
                    normals_complete = False
                else:
                    combined_normals.extend(raw_normals)
                stream_rows.append({"stream_index": stream_counter, "source_object_node": object_name,
                                    "vertex_count": len(positions), "triangle_count": len(triangles),
                                    "index_count": len(triangles) * 3,
                                    "maximum_index": max((index for face in triangles for index in face), default=None),
                                    "indices_in_declared_vertex_range": True,
                                    "topology_checked_as_separate_surface": False})
                stream_counter += 1
            normals = combined_normals if normals_complete and len(combined_normals) == len(combined_positions) else None
            row = inspect_geometry_delivery(combined_positions, combined_triangles, normals=normals,
                                            positional_tolerances=positional_tolerances,
                                            provider_intake=provider_intake,
                                            manifold_required=manifold_required)
            row["object_root_index"] = object_root_index
            row["logical_object_name"] = object_name
            row["stream_count"] = len(streams)
            row["per_stream_capacities"] = stream_rows
            row["position_buffer_sha256_basis"] = "combined decoded PDX p attribute values in stream order; parent binds source file SHA-256"
            results.append(row)
    if not results:
        raise ValueError("Decoded PDX tree contains no mesh streams under object nodes.")
    statuses = {row["status"] for row in results}
    status = "blocked" if "blocked" in statuses else "review_required" if "review_required" in statuses else "pass"
    return {"status": status, "read_only": True, "source_geometry_mutated": False,
            "mesh_node_count": len(results), "meshes": results}
