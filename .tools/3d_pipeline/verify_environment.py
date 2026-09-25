"""Verify the installed 3D dependency routes against the observed lock."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List


PIPELINE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PIPELINE_ROOT.parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.paths import sha256_file, utc_now, write_json  # noqa: E402
from meshy_client import _payload  # noqa: E402
from lib.mcp_stdio import call_stdio  # noqa: E402


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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe-meshy", action="store_true", help="List tools and read Meshy balance")
    parser.add_argument("--probe-blender-lab", action="store_true", help="Check the live Lab bridge and tool list")
    parser.add_argument("--blender-only", action="store_true", help="Skip Meshy runtime checks")
    parser.add_argument("--report", type=Path, default=PIPELINE_ROOT / "reports/environment_report.json")
    args = parser.parse_args()
    if args.blender_only and args.probe_meshy:
        parser.error("--blender-only and --probe-meshy cannot be combined")
    if args.probe_meshy and not os.environ.get("MESHY_API_KEY", "").strip():
        print("MESHY_API_KEY is required only for --probe-meshy. Set it in the environment before probing.")
        return 2
    probe_meshy = args.probe_meshy
    lock_path = PIPELINE_ROOT / "config" / "dependencies.lock.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    findings: List[Dict[str, Any]] = []
    checks: Dict[str, Any] = {}

    def check(name: str, ok: bool, detail: Any) -> None:
        checks[name] = {"ok": ok, "detail": detail}
        if not ok:
            findings.append({"check": name, "detail": detail})

    if not args.blender_only:
        npx = shutil.which("npx.exe") or shutil.which("npx")
        check("npx", bool(npx), npx or "npx.exe not found")
    uv = shutil.which("uv.exe") or shutil.which("uv")
    check("uv", bool(uv), uv or "uv.exe not found")

    meshy_lock = lock["routes"]["meshy_mcp"]
    runtime_slug = meshy_lock["version"].replace(".", "_")
    sdk_lock = meshy_lock["resolved_dependencies"]["modelcontextprotocol_sdk"]
    sdk_slug = sdk_lock["version"].replace(".", "_")
    meshy_runtime = REPO_ROOT / ".tmp" / f"meshy_mcp_native_{runtime_slug}_sdk_{sdk_slug}"
    meshy_manifest = meshy_runtime / "node_modules" / "@meshy-ai" / "meshy-mcp-server" / "package.json"
    sdk_manifest = meshy_runtime / "node_modules" / "@modelcontextprotocol" / "sdk" / "package.json"
    sdk_entries = [sdk_manifest.parent / item for item in sdk_lock["required_entry_points"]]
    def check_meshy_runtime() -> None:
        actual_meshy_version = None
        if meshy_manifest.exists():
            actual_meshy_version = json.loads(meshy_manifest.read_text(encoding="utf-8"))["version"]
        check(
            "meshy_mcp_package_version",
            actual_meshy_version == meshy_lock["version"],
            {"expected": meshy_lock["version"], "actual": actual_meshy_version},
        )
        actual_sdk_version = None
        if sdk_manifest.exists():
            actual_sdk_version = json.loads(sdk_manifest.read_text(encoding="utf-8"))["version"]
        check(
            "meshy_mcp_sdk_version",
            actual_sdk_version == sdk_lock["version"],
            {"expected": sdk_lock["version"], "actual": actual_sdk_version},
        )
        for sdk_entry in sdk_entries:
            relative_entry = sdk_entry.relative_to(sdk_manifest.parent).as_posix()
            check(
                f"meshy_mcp_sdk_entry_point:{relative_entry}",
                sdk_entry.exists(),
                str(sdk_entry),
            )

    if not probe_meshy and not args.blender_only:
        check_meshy_runtime()

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
        expected_version = lock["routes"]["blender"]["version"]
        check("blender_version", f"Blender {expected_version}" in version_text, version_text.splitlines()[:3])
    for name in ("shortcut", "launcher"):
        optional_path = lock["routes"]["blender"].get(name)
        if optional_path:
            check(f"blender_{name}", Path(optional_path).exists(), optional_path)

    blender_project = REPO_ROOT / lock["routes"]["blender_lab_mcp"]["server_project"]
    check("blender_lab_mcp_checkout", (blender_project / "pyproject.toml").exists(), str(blender_project))
    if (blender_project / "pyproject.toml").exists():
        git_root = blender_project.parent
        commit = command_version(["git", "-C", str(git_root), "rev-parse", "HEAD"])
        check(
            "blender_lab_mcp_commit",
            commit == lock["routes"]["blender_lab_mcp"]["commit"],
            {"expected": lock["routes"]["blender_lab_mcp"]["commit"], "actual": commit},
        )
        project_text = (blender_project / "pyproject.toml").read_text(encoding="utf-8")
        server_version = lock["routes"]["blender_lab_mcp"]["verified_server_version"]
        check("blender_lab_mcp_version", f'version = "{server_version}"' in project_text, server_version)

    addon_lock = lock["routes"]["blender_mcp_addon"]
    addon_manifest = Path(addon_lock["installed_manifest"])
    check("blender_mcp_addon_manifest", addon_manifest.exists(), str(addon_manifest))
    if addon_manifest.exists():
        addon_text = addon_manifest.read_text(encoding="utf-8")
        check(
            "blender_mcp_addon_version",
            f'version = "{addon_lock["version"]}"' in addon_text
            and f'id = "{addon_lock["id"]}"' in addon_text,
            str(addon_manifest),
        )
    if args.probe_blender_lab:
        port = int(addon_lock["socket_port"])
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=3):
                pass
            check("blender_lab_bridge", True, f"127.0.0.1:{port}")
            os.environ["BLENDER_MCP_PORT"] = str(port)
            lab_wrapper = REPO_ROOT / lock["routes"]["blender_lab_mcp"]["wrapper"]
            lab_listed = call_stdio(
                ["cmd.exe", "/d", "/c", "call", str(lab_wrapper)],
                list_tools=True, timeout_seconds=180, cwd=REPO_ROOT,
            )
            lab_tools = {item.get("name") for item in lab_listed.get("tools", [])}
            check("blender_lab_tools", "execute_blender_code" in lab_tools,
                  {"tool_count": len(lab_tools), "authoring_tool": "execute_blender_code"})
        except Exception as exc:
            check("blender_lab_bridge", False, str(exc))

    io_lock = lock["routes"]["io_pdx_mesh"]
    io_archive = REPO_ROOT / ".tools" / "3d_pipeline" / "vendor" / "io_pdx_mesh" / io_lock["asset"]
    check("io_pdx_mesh_archive", io_archive.exists(), str(io_archive))
    if io_archive.exists():
        digest = sha256_file(io_archive)
        check(
            "io_pdx_mesh_archive_sha256",
            digest == io_lock["sha256"],
            {"expected": io_lock["sha256"], "actual": digest},
        )
    compat_archive = REPO_ROOT / io_lock["compat_archive"]
    compat_hash = sha256_file(compat_archive) if compat_archive.exists() else None
    check("io_pdx_mesh_compat_archive_sha256", compat_hash == io_lock["compat_archive_sha256"],
          {"expected": io_lock["compat_archive_sha256"], "actual": compat_hash})

    io_manifest = Path(io_lock["installed_manifest"])
    check("io_pdx_mesh_installed", io_manifest.exists(), str(io_manifest))
    if io_manifest.exists():
        io_text = io_manifest.read_text(encoding="utf-8")
        check(
            "io_pdx_mesh_version",
            f'id = "{io_lock["installed_extension_id"]}"' in io_text
            and f'version = "{io_lock["version"]}"' in io_text,
            str(io_manifest),
        )
        for relative, expected in io_lock.get("installed_patch_files_sha256", {}).items():
            installed_file = io_manifest.parent / relative
            actual = sha256_file(installed_file) if installed_file.exists() else None
            check(f"io_pdx_mesh_patch:{relative}", actual == expected,
                  {"expected": expected, "actual": actual})

    meshy_report: Dict[str, Any] = {}
    if probe_meshy:
        try:
            wrapper = REPO_ROOT / meshy_lock["wrapper"]
            command = ["cmd.exe", "/d", "/c", "call", str(wrapper)]
            schema_lifecycle: Dict[str, Any] = {}
            listed = call_stdio(
                command,
                list_tools=True,
                timeout_seconds=300,
                cwd=REPO_ROOT,
                lifecycle_receipt=schema_lifecycle,
            )
            check_meshy_runtime()
            live_tools = {item.get("name"): item for item in listed.get("tools", [])}
            required_tools = set(meshy_lock["verified_tools"])
            missing_tools = sorted(required_tools - set(live_tools))
            image_schema = live_tools.get("meshy_image_to_3d", {}).get("inputSchema", {})
            schema_text = json.dumps(image_schema, sort_keys=True)
            check(
                "meshy_mcp_tools_list",
                not missing_tools,
                {"required": sorted(required_tools), "missing": missing_tools},
            )
            check(
                "meshy_mcp_meshy_7_schema",
                '"meshy-7"' in schema_text,
                {"tool": "meshy_image_to_3d", "model": "meshy-7"},
            )
            balance_lifecycle: Dict[str, Any] = {}
            result = call_stdio(
                command,
                tool="meshy_check_balance",
                arguments={},
                timeout_seconds=300,
                cwd=REPO_ROOT,
                lifecycle_receipt=balance_lifecycle,
            )
            meshy_report = {
                "route": "verified",
                "server_version": meshy_lock["version"],
                "tools": sorted(live_tools),
                "image_model": "meshy-7",
                "public_result": _payload(result),
            }
            check("meshy_mcp_balance_probe", True, meshy_report["public_result"])
            lifecycle_receipts = {
                "tools_list": schema_lifecycle,
                "balance": balance_lifecycle,
            }
            leaked_processes = {
                probe: receipt.get("surviving_process_ids", [])
                for probe, receipt in lifecycle_receipts.items()
                if receipt.get("surviving_process_ids")
            }
            check(
                "meshy_mcp_process_cleanup",
                not leaked_processes,
                {
                    "survivors": leaked_processes,
                    "receipts": lifecycle_receipts,
                },
            )
        except Exception as exc:
            check("meshy_mcp_balance_probe", False, str(exc))
            meshy_report = {"route": "failed", "error": str(exc)}
    else:
        meshy_report = {"route": "not_probed", "hint": "run with --probe-meshy"}

    report = {
        "timestamp": utc_now(),
        "hard_gate": "failed" if findings else "passed",
        "repository_root": str(REPO_ROOT),
        "lock": lock,
        "checks": checks,
        "findings": findings,
        "meshy": meshy_report,
    }
    report_path = args.report
    write_json(report_path, report)
    print(json.dumps({"report": str(report_path), "findings": findings}, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
