"""Verify the hard-gated provider and local 3D dependency routes."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List


if not os.environ.get("MESHY_API_KEY", "").strip():
    print(
        "MESHY_API_KEY is missing or blank. Stop. Run this PowerShell command, "
        "then restart the shell or Codex:\n\n"
        '[Environment]::SetEnvironmentVariable(\n'
        '    "MESHY_API_KEY",\n'
        '    "msy_your_actual_key_here",\n'
        '    "User"\n'
        ")\n"
    )
    raise SystemExit(2)

PIPELINE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PIPELINE_ROOT.parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.paths import file_record, sha256_file, utc_now, write_json  # noqa: E402
from meshy_client import MeshyClient, _payload  # noqa: E402


def command_version(command: List[str]) -> str:
    completed = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=30,
        check=False,
    )
    return completed.stdout.strip()


def main() -> int:
    probe_meshy = "--probe-meshy" in sys.argv[1:]
    lock_path = PIPELINE_ROOT / "config" / "dependencies.lock.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    findings: List[Dict[str, Any]] = []
    checks: Dict[str, Any] = {}

    def check(name: str, ok: bool, detail: Any) -> None:
        checks[name] = {"ok": ok, "detail": detail}
        if not ok:
            findings.append({"check": name, "detail": detail})

    npx = shutil.which("npx.exe") or shutil.which("npx")
    check("npx", bool(npx), npx or "npx.exe not found")
    uv = shutil.which("uv.exe") or shutil.which("uv")
    check("uv", bool(uv), uv or "uv.exe not found")

    adapter_lock = lock["routes"]["blender_hoi4_adapter"]
    adapter_config_path = REPO_ROOT / adapter_lock["config"]
    check("blender_hoi4_adapter_config", adapter_config_path.exists(), str(adapter_config_path))
    if adapter_config_path.exists():
        adapter_config = json.loads(adapter_config_path.read_text(encoding="utf-8"))
        check(
            "blender_hoi4_adapter_version",
            adapter_config.get("adapter_version") == adapter_lock["version"],
            {
                "expected": adapter_lock["version"],
                "actual": adapter_config.get("adapter_version"),
            },
        )
        check(
            "blender_hoi4_adapter_operations",
            adapter_config.get("operations") == adapter_lock["operations"],
            {
                "expected": adapter_lock["operations"],
                "actual": adapter_config.get("operations"),
            },
        )
    for relative_path, expected_hash in adapter_lock.get("source_sha256", {}).items():
        source_path = REPO_ROOT / relative_path
        actual_hash = sha256_file(source_path) if source_path.exists() else None
        check(
            f"blender_hoi4_adapter_sha256:{relative_path}",
            actual_hash == expected_hash,
            {"expected": expected_hash, "actual": actual_hash},
        )

    blender_path = Path(lock["routes"]["blender"]["executable"])
    check("blender_executable", blender_path.exists(), str(blender_path))
    if blender_path.exists():
        version_text = command_version([str(blender_path), "--version"])
        check("blender_version", "Blender 5.1.2" in version_text, version_text.splitlines()[:3])
    blender_shortcut = Path(lock["routes"]["blender"]["shortcut"])
    blender_launcher = Path(lock["routes"]["blender"]["launcher"])
    check("blender_shortcut", blender_shortcut.exists(), str(blender_shortcut))
    check("blender_launcher", blender_launcher.exists(), str(blender_launcher))

    blender_project = REPO_ROOT / lock["routes"]["blender_lab_mcp"]["server_project"]
    check("blender_lab_mcp_checkout", (blender_project / "pyproject.toml").exists(), str(blender_project))
    if blender_project.exists():
        git_root = blender_project.parent
        commit = command_version(["git", "-C", str(git_root), "rev-parse", "HEAD"])
        check(
            "blender_lab_mcp_commit",
            commit == lock["routes"]["blender_lab_mcp"]["commit"],
            {"expected": lock["routes"]["blender_lab_mcp"]["commit"], "actual": commit},
        )

    addon_manifest = Path(
        "C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/"
        "extensions/lab_blender_org/mcp/blender_manifest.toml"
    )
    check("blender_mcp_addon_manifest", addon_manifest.exists(), str(addon_manifest))
    if addon_manifest.exists():
        addon_text = addon_manifest.read_text(encoding="utf-8")
        check(
            "blender_mcp_addon_version",
            'version = "1.0.0"' in addon_text and 'id = "mcp"' in addon_text,
            str(addon_manifest),
        )

    io_archive = REPO_ROOT / "vendor" / "not-present"
    io_archive = REPO_ROOT / ".tools" / "3d_pipeline" / "vendor" / "io_pdx_mesh" / "blender-io_pdx_mesh.zip"
    check("io_pdx_mesh_archive", io_archive.exists(), str(io_archive))
    if io_archive.exists():
        digest = sha256_file(io_archive)
        check(
            "io_pdx_mesh_archive_sha256",
            digest == lock["routes"]["io_pdx_mesh"]["sha256"],
            {"expected": lock["routes"]["io_pdx_mesh"]["sha256"], "actual": digest},
        )

    io_manifest = Path(
        "C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/"
        "extensions/user_default/io_pdx_mesh/blender_manifest.toml"
    )
    check("io_pdx_mesh_installed", io_manifest.exists(), str(io_manifest))
    if io_manifest.exists():
        io_text = io_manifest.read_text(encoding="utf-8")
        check(
            "io_pdx_mesh_version",
            'id = "io_pdx_mesh"' in io_text and 'version = "0.91.0"' in io_text,
            str(io_manifest),
        )

    meshy_report: Dict[str, Any] = {}
    if probe_meshy:
        try:
            result = MeshyClient(REPO_ROOT).check_balance()
            meshy_report = {
                "route": "verified",
                "server_version": os.environ.get("MESHY_MCP_VERSION", "0.4.0"),
                "public_result": _payload(result),
            }
            check("meshy_mcp_balance_probe", True, meshy_report["public_result"])
        except Exception as exc:
            check("meshy_mcp_balance_probe", False, str(exc))
            meshy_report = {"route": "failed", "error": str(exc)}
    else:
        meshy_report = {"route": "not_probed", "hint": "run with --probe-meshy"}

    report = {
        "timestamp": utc_now(),
        "hard_gate": "passed",
        "repository_root": str(REPO_ROOT),
        "lock": lock,
        "checks": checks,
        "findings": findings,
        "meshy": meshy_report,
    }
    report_path = PIPELINE_ROOT / "reports" / "environment_report.json"
    write_json(report_path, report)
    print(json.dumps({"report": str(report_path), "findings": findings}, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
