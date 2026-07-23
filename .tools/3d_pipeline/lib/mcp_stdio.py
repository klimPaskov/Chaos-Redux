"""Small, strict JSON-RPC client for the repository's pinned MCP routes."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Sequence


class MCPRouteError(RuntimeError):
    """Raised when an MCP process cannot initialize or complete a call."""


def _json_lines(output: str) -> Iterable[Dict[str, Any]]:
    decoder = json.JSONDecoder()
    cursor = 0
    while cursor < len(output):
        start = output.find("{", cursor)
        if start < 0:
            return
        try:
            value, consumed = decoder.raw_decode(output[start:])
        except json.JSONDecodeError:
            cursor = start + 1
            continue
        cursor = start + consumed
        if isinstance(value, dict) and value.get("jsonrpc") == "2.0":
            yield value


def call_stdio(
    command: Sequence[str],
    *,
    tool: Optional[str] = None,
    arguments: Optional[Dict[str, Any]] = None,
    timeout_seconds: int = 1800,
    cwd: Optional[Path] = None,
    env: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Initialize an MCP server, call one tool, and close the stdio session.

    The client accepts only JSON-RPC output from stdout. Human-readable logs
    belong on stderr and are retained in the returned diagnostic when present.
    """

    messages = [
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "chaos-redux-3d-pipeline", "version": "1.0.0"},
            },
        },
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
    ]
    if tool is not None:
        messages.append(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": tool, "arguments": arguments or {}},
            }
        )

    process_env = os.environ.copy()
    if env:
        process_env.update(env)
    request = "\n".join(json.dumps(message, separators=(",", ":")) for message in messages) + "\n"

    try:
        completed = subprocess.run(
            list(command),
            input=request,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(cwd) if cwd else None,
            env=process_env,
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise MCPRouteError(f"MCP route timed out after {timeout_seconds}s: {command}") from exc
    except OSError as exc:
        raise MCPRouteError(f"Unable to start MCP route: {command}") from exc

    responses = list(_json_lines(completed.stdout))
    response = next((item for item in reversed(responses) if item.get("id") == 2), None)
    if response is None and tool is None:
        response = next((item for item in reversed(responses) if item.get("id") == 1), None)
    if response is None:
        diagnostics = (completed.stderr or "").strip()[-4000:]
        requested = f" for tool {tool!r}" if tool else ""
        raise MCPRouteError(
            f"MCP route returned no JSON-RPC response{requested} (exit={completed.returncode}). {diagnostics}"
        )
    if "error" in response:
        raise MCPRouteError(json.dumps(response["error"], sort_keys=True))
    if completed.returncode != 0:
        raise MCPRouteError(
            f"MCP route exited with {completed.returncode}: {(completed.stderr or '').strip()[-4000:]}"
        )
    stderr_text = completed.stderr or ""
    if stderr_text.strip():
        response["_route_stderr"] = stderr_text.strip()[-4000:]
    return response.get("result", response)
