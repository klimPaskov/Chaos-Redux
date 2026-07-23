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
        target_triangles: int = 0,
        excluded_provider_objects: Optional[list[str]] = None,
        vanilla_reference: Optional[Dict[str, Any]] = None,
        texture_source_rels: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_prepare_candidate",
            {
                "job_id": job_id,
                "source_rel": source_rel,
                "asset_kind": asset_kind,
                "target_height_m": target_height_m,
                "runtime_stem": runtime_stem,
                "target_triangles": target_triangles,
                "excluded_provider_objects": excluded_provider_objects or [],
                "vanilla_reference": vanilla_reference or {},
                "texture_source_rels": texture_source_rels or {},
            },
        )

    def process_textures(self, job_id: str, blend_rel: str) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_process_textures",
            {"job_id": job_id, "blend_rel": blend_rel},
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

    def inspect_scene(self, job_id: str, blend_rel: str) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_inspect_scene",
            {"job_id": job_id, "blend_rel": blend_rel},
        )

    def save_checkpoint(self, job_id: str, blend_rel: str, stage: str) -> Dict[str, Any]:
        return self.call(
            "chaosx_blender_hoi4_save_checkpoint",
            {"job_id": job_id, "blend_rel": blend_rel, "stage": stage},
        )
