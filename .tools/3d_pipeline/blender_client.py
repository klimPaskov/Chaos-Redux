"""Client for the repository-owned allowlisted Blender MCP adapter."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

from lib.mcp_stdio import MCPRouteError, call_stdio
from meshy_client import require_meshy_key


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
        require_meshy_key()
        self.repo_root = repo_root.resolve()
        self.wrapper = self.repo_root / ".tools" / "3d_pipeline" / "wrappers" / "run_blender_hoi4_adapter.cmd"
        if not self.wrapper.exists():
            raise FileNotFoundError(self.wrapper)

    def call(self, tool: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        command = ["cmd.exe", "/d", "/c", "call", str(self.wrapper)]
        result: Optional[Dict[str, Any]] = None
        for attempt in range(3):
            try:
                result = call_stdio(
                    command,
                    tool=tool,
                    arguments=arguments,
                    timeout_seconds=1800,
                    cwd=self.repo_root,
                )
                break
            except MCPRouteError:
                if attempt == 2:
                    raise
        if result is None:
            raise RuntimeError(f"Blender adapter returned no result for {tool}.")
        if result.get("isError"):
            raise RuntimeError(str(_structured(result)))
        value = _structured(result)
        if "error" in value:
            raise RuntimeError(str(value))
        return value

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
        geometry_source_rel: Optional[str] = None,
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
                "geometry_source_rel": geometry_source_rel or "",
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

    def export_mesh(self, job_id: str, blend_rel: str, output_rel: str) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_export_mesh",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "output_rel": output_rel,
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

    def author_locomotion_action(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        action_name: str = "Armature|Move|baselayer_WORKING",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_author_locomotion_action",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "action_name": action_name,
            },
        )

    def import_animation_action(
        self,
        job_id: str,
        blend_rel: str,
        source_rel: str,
        checkpoint_rel: str,
        action_name: str,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_import_animation_action",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "source_rel": source_rel,
                "checkpoint_rel": checkpoint_rel,
                "action_name": action_name,
            },
        )

    def segment_creature_components(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        region_mode: str = "loose",
        rider_z_min_fraction: float = 0.72,
        rider_z_max_fraction: float = 1.0,
        rider_x_center_fraction: float = 0.5,
        rider_x_half_fraction: float = 0.38,
        rider_y_center_fraction: float = 0.5,
        rider_y_half_fraction: float = 0.42,
        rider_object_name: str = "elephant_rider_region",
        body_object_name: str = "elephant_body_region",
        component_prefix: str = "elephant_component",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_segment_creature_components",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "region_mode": region_mode,
                "rider_z_min_fraction": rider_z_min_fraction,
                "rider_z_max_fraction": rider_z_max_fraction,
                "rider_x_center_fraction": rider_x_center_fraction,
                "rider_x_half_fraction": rider_x_half_fraction,
                "rider_y_center_fraction": rider_y_center_fraction,
                "rider_y_half_fraction": rider_y_half_fraction,
                "rider_object_name": rider_object_name,
                "body_object_name": body_object_name,
                "component_prefix": component_prefix,
            },
        )

    def calibrate_creature_scale(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        rider_component_names: list[str],
        target_rider_runtime_height_m: float,
        runtime_entity_scale: float = 0.8,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_calibrate_creature_scale",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "rider_component_names": rider_component_names,
                "target_rider_runtime_height_m": target_rider_runtime_height_m,
                "runtime_entity_scale": runtime_entity_scale,
            },
        )

    def author_creature_rig(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        rider_component_names: Optional[list[str]] = None,
        weight_mode: str = "semantic",
        rig_name: str = "",
        creature_rig_family: str = "elephant",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_author_creature_rig",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "rider_component_names": rider_component_names or [],
                "weight_mode": weight_mode,
                "rig_name": rig_name,
                "creature_rig_family": creature_rig_family,
            },
        )

    def author_creature_action(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        action_role: str,
        action_name: str,
        creature_rig_family: str = "elephant",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_author_creature_action",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "action_role": action_role,
                "action_name": action_name,
                "creature_rig_family": creature_rig_family,
            },
        )

    def correct_action_grounding(
        self,
        job_id: str,
        blend_rel: str,
        checkpoint_rel: str,
        action_name: str,
        root_bone: str = "Hips",
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_correct_action_grounding",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "checkpoint_rel": checkpoint_rel,
                "action_name": action_name,
                "root_bone": root_bone,
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
        preview_frame: int = -1,
        preview_view_names: Optional[list[str]] = None,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_inspect_scene",
            {
                "job_id": job_id,
                "blend_rel": blend_rel,
                "render_previews": render_previews,
                "runtime_stem": runtime_stem,
                "action_name": action_name,
                "preview_frame": preview_frame,
                "preview_view_names": preview_view_names or [],
            },
        )

    def save_checkpoint(self, job_id: str, blend_rel: str, stage: str) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_save_checkpoint",
            {"job_id": job_id, "blend_rel": blend_rel, "stage": stage},
        )
