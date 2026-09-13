"""Read-only Meshy MCP schema probe.

Purpose
-------
Confirm, from the live locked route rather than from prose, whether
``meshy_image_to_3d`` accepts a single reference image or several, and record the
exact live tool surface and image-related image-to-3D arguments.

This script never starts a paid task: it only issues ``tools/list`` and the free
``meshy_check_balance`` call. It reads ``MESHY_API_KEY`` from the process
environment and never writes the key, or a redacted form of it, to disk.

Usage
-----
    python .tools/3d_pipeline/inspect_meshy_live_schema.py [--out <path>]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / ".tools" / "3d_pipeline"))

from lib.mcp_stdio import MCPRouteError, call_stdio  # noqa: E402

WRAPPER = REPO_ROOT / ".tools" / "3d_pipeline" / "wrappers" / "run_meshy_mcp.cmd"
IMAGE_ARGUMENTS = (
    "file_path",
    "image_url",
    "input_task_id",
    "multi_view_thumbnails",
    "pose_mode",
    "texture_image_url",
    "ai_model",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        default=str(
            REPO_ROOT
            / ".tools"
            / "3d_pipeline"
            / "reports"
            / "meshy_live_schema_probe.json"
        ),
    )
    args = parser.parse_args()

    if not os.environ.get("MESHY_API_KEY", "").strip():
        print("MESHY_API_KEY is missing or blank; refusing to start the route.")
        return 2

    command = ["cmd.exe", "/c", str(WRAPPER)]
    receipt: dict[str, object] = {}

    listing = call_stdio(
        command,
        list_tools=True,
        timeout_seconds=300,
        lifecycle_receipt=receipt,
    )
    tools = {tool["name"]: tool for tool in listing.get("tools", [])}

    balance = call_stdio(
        command,
        tool="meshy_check_balance",
        arguments={},
        timeout_seconds=300,
    )

    image_tool = tools.get("meshy_image_to_3d", {})
    schema = image_tool.get("inputSchema", {})
    properties = schema.get("properties", {})

    report = {
        "wrapper": str(WRAPPER.relative_to(REPO_ROOT)).replace("\\", "/"),
        "tool_count": len(tools),
        "tool_names": sorted(tools),
        "image_to_3d_present": "meshy_image_to_3d" in tools,
        "image_to_3d_required": schema.get("required", []),
        "image_to_3d_any_of": schema.get("anyOf", schema.get("oneOf")),
        "image_to_3d_image_arguments": {
            name: properties[name] for name in IMAGE_ARGUMENTS if name in properties
        },
        "image_to_3d_multi_image_arguments": sorted(
            name
            for name in properties
            if "image" in name.lower() and name not in IMAGE_ARGUMENTS
        ),
        "multi_image_tool_present": "meshy_multi_image_to_3d" in tools,
        "balance_probe": balance,
        "cleanup": receipt,
    }

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(
        json.dumps(report, indent=2, sort_keys=True), encoding="utf-8"
    )

    print(f"tools exposed: {report['tool_count']}")
    print(f"image_to_3d present: {report['image_to_3d_present']}")
    print(f"image arguments: {sorted(report['image_to_3d_image_arguments'])}")
    print(f"multi-image tool present: {report['multi_image_tool_present']}")
    print(f"report: {args.out}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except MCPRouteError as error:
        print(f"MCP route error: {error}")
        raise SystemExit(1)
