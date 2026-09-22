"""Client for the repository-owned allowlisted Blender MCP adapter."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Literal, Optional

from lib.mcp_stdio import MCPRouteError, call_stdio


def _structured(result: Dict[str, Any]) -> Dict[str, Any]:
    structured = result.get("structuredContent", {})
    if isinstance(structured, dict):
        if isinstance(structured.get("result"), dict):
            return structured["result"]
        if structured:
            return structured
    for block in result.get("content", []):
        if isinstance(block, dict) and block.get("type") == "text":
            text = block.get("text", "")
            try:
                value = json.loads(text)
            except (TypeError, json.JSONDecodeError):
                continue
            if isinstance(value, dict):
                return value
    return result


class BlenderAdapterClient:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()
        self.wrapper = self.repo_root / ".tools" / "3d_pipeline" / "wrappers" / "run_blender_hoi4_adapter.cmd"
        if not self.wrapper.exists():
            raise FileNotFoundError(self.wrapper)

    def call(self, tool: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        command = ["cmd.exe", "/d", "/c", "call", str(self.wrapper)]
        result: Optional[Dict[str, Any]] = None
        read_only_tools = {"chaosx_blender_hoi4_health", "chaosx_blender_hoi4_inspect_scene", "chaosx_blender_hoi4_inspect_mesh_landmarks", "chaosx_blender_hoi4_inspect_mesh_winding", "chaosx_blender_hoi4_review_humanoid_components"}
        attempt_limit = 3 if tool in read_only_tools else 1
        for attempt in range(attempt_limit):
            try:
                result = call_stdio(
                    command,
                    tool=tool,
                    arguments=arguments,
                    timeout_seconds=1800,
                    cwd=self.repo_root,
                )
                break
            except MCPRouteError as exc:
                if attempt == attempt_limit - 1:
                    if tool not in read_only_tools:
                        receipts = self._matching_mutation_receipts(tool, arguments)
                        raise MCPRouteError(f"Mutation response uncertain; no automatic retry for {tool}. Inspect saved checkpoint/report before any new call. Matching adapter request evidence: {receipts}. Transport: {exc}") from exc
                    raise
        if result is None:
            raise RuntimeError(f"Blender adapter returned no result for {tool}.")
        if result.get("isError"):
            raise RuntimeError(str(_structured(result)))
        value = _structured(result)
        if "error" in value:
            raise RuntimeError(str(value))
        return value

    def _matching_mutation_receipts(self, tool: str, arguments: Dict[str, Any]) -> list[dict[str, Any]]:
        """Read bounded matching request headers after uncertain transport; never replay."""
        config_path = self.repo_root / ".tools/3d_pipeline/config/blender_hoi4_adapter.json"
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
            job_id = arguments.get("job_id", "")
            job = Path(config.get("job_overrides", {}).get(job_id, str(Path(config["job_root"]) / job_id))).resolve()
            directory = job / "logs/adapter"
            candidates = sorted((p for p in directory.glob("*.json") if not p.name.endswith(".result.json")), key=lambda p:p.stat().st_mtime, reverse=True)[:16]
            result = []
            expected = {k:v for k,v in arguments.items() if k != "job_id"}
            for path in candidates:
                if path.stat().st_size > 16_000_000:
                    continue
                request = json.loads(path.read_text(encoding="utf-8"))
                payload = request.get("payload", {})
                if request.get("operation") == tool.removeprefix("chaosx_blender_hoi4_") and all(payload.get(k) == v for k,v in expected.items()):
                    result.append({"request_id":request.get("request_id",path.stem),"request_rel":path.relative_to(job).as_posix(),"worker_result_exists":path.with_suffix(".result.json").exists()})
            return result
        except (OSError, ValueError, KeyError, TypeError):
            return []

    def health(self, job_id: str) -> Dict[str, Any]:
        return self.call("chaosx_blender_hoi4_health", {"job_id": job_id})

    def prepare_candidate(
        self,
        job_id: str,
        *,
        source_rel: str,
        asset_kind: str,
        target_height_m: float,
        runtime_stem: str,
        runtime_entity_scale: float = 1.0,
        target_triangles: int = 0,
        excluded_provider_objects: Optional[list[str]] = None,
        vanilla_reference: Optional[Dict[str, Any]] = None,
        texture_source_rels: Optional[Dict[str, str]] = None,
        preserve_geometry_topology: bool = False,
        repair_before_reduction: bool = False,
        topology_weld_distance: float = 1e-5,
        max_runtime_footprint_m: Optional[float] = None,
        runtime_footprint_policy: str = "reject",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_prepare_candidate",
            {
                "job_id": job_id,
                "source_rel": source_rel,
                "asset_kind": asset_kind,
                "target_height_m": target_height_m,
                "runtime_entity_scale": runtime_entity_scale,
                "runtime_stem": runtime_stem,
                "target_triangles": target_triangles,
                "excluded_provider_objects": excluded_provider_objects or [],
                "vanilla_reference": vanilla_reference or {},
                "texture_source_rels": texture_source_rels or {},
                "preserve_geometry_topology": preserve_geometry_topology,
                "repair_before_reduction": repair_before_reduction,
                "topology_weld_distance": topology_weld_distance,
                "max_runtime_footprint_m": max_runtime_footprint_m,
                "runtime_footprint_policy": runtime_footprint_policy,
            },
        )

    def process_textures(
        self,
        job_id: str,
        blend_rel: str,
        *,
        rewrite_to_dds: bool = False,
        dds_map: Optional[Dict[str, str]] = None,
        rename_images: bool = False,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_process_textures",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "rewrite_to_dds": rewrite_to_dds,
                "dds_map": dds_map or {},
                "rename_images": rename_images,
            },
        )

    def promote_accepted_reimport(
        self,
        job_id: str,
        blend_rel: str,
        expected_source_sha256: str,
        validation_rel: str,
        expected_validation_sha256: str,
        checkpoint_rel: str,
        target_armature_name: str,
        target_mesh_names: list[str],
        mesh_rel: str,
        expected_mesh_sha256: str,
        anim_rel: str,
        expected_anim_sha256: str,
    ) -> Dict[str, Any]:
        return self.call("chaosx_blender_hoi4_promote_accepted_reimport", {
            "job_id": job_id, "blend_rel": blend_rel, "expected_source_sha256": expected_source_sha256,
            "validation_rel": validation_rel, "expected_validation_sha256": expected_validation_sha256,
            "checkpoint_rel": checkpoint_rel, "target_armature_name": target_armature_name,
            "target_mesh_names": list(target_mesh_names), "mesh_rel": mesh_rel,
            "expected_mesh_sha256": expected_mesh_sha256, "anim_rel": anim_rel,
            "expected_anim_sha256": expected_anim_sha256,
        })

    def author_locator(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        target_armature_name: str,
        parent_bone: str,
        locator_name: str,
        bone_local_position: tuple[float, float, float],
        bone_local_rotation_xyzw: tuple[float, float, float, float],
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_author_locator",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "target_armature_name": target_armature_name,
                "parent_bone": parent_bone,
                "locator_name": locator_name,
                "bone_local_position": list(bone_local_position),
                "bone_local_rotation_xyzw": list(bone_local_rotation_xyzw),
            },
        )

    def export_mesh(self, job_id: str, blend_rel: str, output_rel: str, split_verts: bool = False) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_export_mesh",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "output_rel": output_rel,
                "split_verts": split_verts,
            },
        )

    def export_animation(
        self,
        job_id: str,
        blend_rel: str,
        action_name: str,
        output_rel: str,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_export_animation",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "action_name": action_name,
                "output_rel": output_rel,
            },
        )


    def bake_static_mesh_transforms(
        self,
        job_id: str,
        blend_rel: str,
        output_blend_rel: str,
        *,
        asset_kind: str,
        bounds_tolerance: float = 1e-5,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_bake_static_mesh_transforms",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "output_blend_rel": output_blend_rel,
                "asset_kind": asset_kind,
                "bounds_tolerance": bounds_tolerance,
            },
        )

    def partition_skeletal_mesh_export_batches(
        self, *, job_id: str, blend_rel: str, expected_source_sha256: str,
        checkpoint_rel: str, target_armature_name: str, target_mesh_names: list[str],
        max_export_vertices_per_batch: int = 24000,
    ) -> Dict[str, Any]:
        return self.call("chaosx_blender_hoi4_partition_skeletal_mesh_export_batches", {
            "job_id": job_id, "blend_rel": blend_rel,
            "expected_source_sha256": expected_source_sha256, "checkpoint_rel": checkpoint_rel,
            "target_armature_name": target_armature_name, "target_mesh_names": target_mesh_names,
            "max_export_vertices_per_batch": max_export_vertices_per_batch,
        })

    def partition_static_mesh_export_batches(
        self,
        job_id: str,
        blend_rel: str,
        output_blend_rel: str,
        *,
        asset_kind: str,
        max_export_vertices_per_batch: int = 60000,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_partition_static_mesh_export_batches",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "output_blend_rel": output_blend_rel,
                "asset_kind": asset_kind,
                "max_export_vertices_per_batch": max_export_vertices_per_batch,
            },
        )


    def prepare_export_coordinate_checkpoint(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        action_name: str,
        target_armature_name: str,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_prepare_export_coordinate_checkpoint",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "action_name": action_name,
                "target_armature_name": target_armature_name,
            },
        )

    def sanitize_runtime_candidate(
        self,
        job_id: str,
        blend_rel: str,
        output_blend_rel: str = "blender/checkpoints/07_runtime_candidate_sanitized.blend",
        target_height_m: Optional[float] = None,
        weight_only: bool = False,
        max_influences_per_vertex: int = 4,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_sanitize_runtime_candidate",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "output_blend_rel": output_blend_rel,
                "target_height_m": target_height_m,
                "weight_only": weight_only,
                "max_influences_per_vertex": max_influences_per_vertex,
            },
        )

    def reimport_export(
        self,
        job_id: str,
        mesh_rel: str,
        anim_rel: str = "",
        proof_name: str = "",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_reimport_export",
            {
                "job_id": job_id,
                "mesh_rel": mesh_rel,
                "anim_rel": anim_rel,
                "proof_name": proof_name,
            },
        )

    def inspect_scene(
        self,
        job_id: str,
        blend_rel: str,
        render_previews: bool = False,
        runtime_stem: str = "",
        action_name: str = "",
        target_armature_name: str = "",
        preview_frame: int = -1,
        preview_view_names: Optional[list[str]] = None,
        mesh_region: Optional[Dict[str, Any]] = None,
        include_action_channels: bool = False,
        expected_source_sha256: str = "",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_inspect_scene",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "render_previews": render_previews,
                "runtime_stem": runtime_stem,
                "action_name": action_name,
                "target_armature_name": target_armature_name,
                "preview_frame": preview_frame,
                "preview_view_names": preview_view_names or [],
                **({"mesh_region": mesh_region} if mesh_region is not None else {}),
                **({"include_action_channels": True, "expected_source_sha256": expected_source_sha256} if include_action_channels else {}),
            },
        )

    def review_humanoid_components(
        self,
        job_id: str,
        blend_rel: str,
        expected_source_sha256: str,
        mesh_name: str,
        render_group: bool = True,
        component_ids: Optional[list[str]] = None,
        component_offset: int = 0,
        component_limit: int = 16,
        preview_view_names: Optional[list[str]] = None,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_review_humanoid_components",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "expected_source_sha256": expected_source_sha256,
                "mesh_name": mesh_name,
                "render_group": render_group,
                "component_ids": component_ids or [],
                "component_offset": component_offset,
                "component_limit": component_limit,
                "preview_view_names": preview_view_names or [],
            },
        )

    def save_checkpoint(self, job_id: str, blend_rel: str, stage: str) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_save_checkpoint",
            {"job_id": job_id, "blend_rel": blend_rel, "stage": stage},
        )

    def import_animation_action(
        self,
        job_id: str,
        blend_rel: str,
        source_rel: str,
        provenance_rel: str,
        checkpoint_rel: str,
        source_action_name: str,
        target_armature_name: str,
        target_action_name: str,
        source_kind: Literal["meshy_animate", "professional_source"],
        source_reference_id: str,
        source_sha256: str,
        bone_chains: Optional[Dict[str, list[str]]] = None,
        promote_audited_target: bool = False,
        source_armature_name: str = "",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_import_animation_action",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "source_rel": source_rel,
                "provenance_rel": provenance_rel,
                "checkpoint_rel": checkpoint_rel,
                "source_action_name": source_action_name,
                "source_armature_name": source_armature_name,
                "target_armature_name": target_armature_name,
                "target_action_name": target_action_name,
                "source_kind": source_kind,
                "source_reference_id": source_reference_id,
                "source_sha256": source_sha256,
                "bone_chains": bone_chains or {},
                "promote_audited_target": promote_audited_target,
            },
        )

    def import_bvh_animation_action(
        self,
        job_id: str,
        blend_rel: str,
        source_rel: str,
        provenance_rel: str,
        checkpoint_rel: str,
        source_action_name: str,
        target_armature_name: str,
        target_action_name: str,
        semantic_role: str,
        source_reference_id: str,
        source_sha256: str,
        source_fps: float,
        target_fps: float,
        bone_chains: Dict[str, list[str]],
        root_motion_policy: Literal["in_place_xy_preserve_z"],
        global_scale: float = 1.0,
        axis_forward: Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "-Z",
        axis_up: Literal["X", "Y", "Z", "-X", "-Y", "-Z"] = "Y",
        promote_audited_target: bool = False,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_import_bvh_animation_action",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "source_rel": source_rel,
                "provenance_rel": provenance_rel,
                "checkpoint_rel": checkpoint_rel,
                "source_action_name": source_action_name,
                "target_armature_name": target_armature_name,
                "target_action_name": target_action_name,
                "semantic_role": semantic_role,
                "source_reference_id": source_reference_id,
                "source_sha256": source_sha256,
                "source_fps": source_fps,
                "target_fps": target_fps,
                "bone_chains": bone_chains,
                "root_motion_policy": root_motion_policy,
                "global_scale": global_scale,
                "axis_forward": axis_forward,
                "axis_up": axis_up,
                "promote_audited_target": promote_audited_target,
            },
        )

    def retime_animation_action(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        action_name: str,
        target_armature_name: str,
        source_fps: float,
        target_fps: float,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_retime_animation_action",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "action_name": action_name,
                "target_armature_name": target_armature_name,
                "source_fps": source_fps,
                "target_fps": target_fps,
            },
        )
