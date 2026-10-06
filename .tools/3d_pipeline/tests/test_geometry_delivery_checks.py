"""Read-only positional topology and PDX stream grouping tests."""
from __future__ import annotations

import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import geometry_delivery_checks as geometry  # noqa: E402


class GeometryDelivery(unittest.TestCase):
    def test_nonmanifold_island_returns_boundary_duplicate_and_winding_evidence(self):
        positions = [(0., 0., 0.), (1., 0., 0.), (0., 1., 0.), (0., -1., 0.), (0., 0., 1.)]
        triangles = [(0, 1, 2), (1, 0, 3), (0, 1, 4)]
        result = geometry.inspect_geometry_delivery(positions, triangles)
        topology = result["topology_by_tolerance"][-1]
        self.assertEqual(result["status"], "review_required")
        self.assertEqual(topology["nonmanifold_edge_count"], 1)
        self.assertEqual(topology["nonmanifold_face_count"], 3)
        self.assertEqual(topology["components"][0]["nonmanifold_edge_count"], 1)
        self.assertFalse(topology["weld_applied"])
        self.assertEqual(result["winding_report"]["non_manifold_edge_count"], 1)

    def test_positional_tolerance_measures_hypothetical_weld_without_mutation(self):
        positions = [(0., 0., 0.), (1., 0., 0.), (0., 1., 0.),
                     (0.0004, 0., 0.), (1., 0., 0.), (0., 0., 1.)]
        triangles = [(0, 1, 2), (3, 4, 5)]
        original = list(positions)
        result = geometry.inspect_geometry_delivery(positions, triangles)
        rows = result["topology_by_tolerance"]
        self.assertEqual([row["tolerance_units"] for row in rows], [0.0005, 0.001, 0.002])
        self.assertEqual(rows[0]["hypothetical_vertex_merge_count"], 2)
        self.assertEqual(rows[0]["weld_applied"], False)
        self.assertEqual(positions, original)

    def test_duplicate_faces_and_split_normals_are_diagnostic(self):
        positions = [(0., 0., 0.), (1., 0., 0.), (0., 1., 0.), (0., 0., 0.)]
        triangles = [(0, 1, 2), (3, 1, 2)]
        normals = [(0., 0., 1.), (0., 0., 1.), (0., 0., 1.), (0., 0., -1.)]
        result = geometry.inspect_geometry_delivery(positions, triangles, normals=normals)
        row = result["topology_by_tolerance"][0]
        self.assertEqual(row["duplicate_face_count"], 1)
        self.assertEqual(row["duplicate_face_orientation_counts"]["same"], 1)
        self.assertEqual(row["split_normals"]["positional_vertex_groups_with_split_normals"], 1)
        self.assertEqual(result["winding_report"]["status"], "blocked")

    def test_provider_intake_boundary_ceiling_reports_failure_without_dropping_evidence(self):
        positions = []
        triangles = []
        for index in range(67):
            offset = index * 2.0
            base = len(positions)
            positions.extend([(offset, 0., 0.), (offset + 1., 0., 0.), (offset, 1., 0.)])
            triangles.append((base, base + 1, base + 2))
        result = geometry.inspect_geometry_delivery(positions, triangles)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["provider_intake_boundary_gate"]["status"], "blocked")
        self.assertEqual(result["topology_by_tolerance"][-1]["boundary_edge_count"], 201)
        self.assertEqual(len(result["topology_by_tolerance"][-1]["components"]), 67)

    def test_pdx_material_streams_are_combined_by_logical_object(self):
        tetra_positions = [(0., 0., 0.), (1., 0., 0.), (0., 1., 0.), (0., 0., 1.)]
        tetra_faces = [(0, 2, 1), (0, 1, 3), (0, 3, 2), (1, 2, 3)]
        root = ET.Element("File")
        object_root = ET.SubElement(root, "object")
        model = ET.SubElement(object_root, "Model")
        for faces in (tetra_faces[:2], tetra_faces[2:]):
            mesh = ET.SubElement(model, "mesh")
            mesh.set("p", repr([value for point in tetra_positions for value in point]))
            mesh.set("n", repr([value for _ in tetra_positions for value in (0., 0., 1.)]))
            mesh.set("tri", repr([value for face in faces for value in face]))
        result = geometry.inspect_pdx_mesh_tree(root, manifold_required=True)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["mesh_node_count"], 1)
        logical = result["meshes"][0]
        self.assertEqual(logical["logical_object_name"], "Model")
        self.assertEqual(logical["stream_count"], 2)
        self.assertEqual([row["triangle_count"] for row in logical["per_stream_capacities"]], [2, 2])
        self.assertEqual(logical["topology_by_tolerance"][0]["boundary_edge_count"], 0)
        self.assertFalse(any(row["topology_checked_as_separate_surface"] for row in logical["per_stream_capacities"]))


if __name__ == "__main__":
    unittest.main()
