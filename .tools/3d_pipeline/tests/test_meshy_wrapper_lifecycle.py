"""Windows lifecycle regression tests for the exact locked Meshy MCP wrapper."""

from __future__ import annotations

import json
import os
import queue
import subprocess
import threading
import time
import unittest
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
WRAPPER_CMD = REPO_ROOT / ".tools" / "3d_pipeline" / "wrappers" / "run_meshy_mcp.cmd"
WRAPPER_PS1 = REPO_ROOT / ".tools" / "3d_pipeline" / "wrappers" / "run_meshy_mcp.ps1"
LOCK_PATH = REPO_ROOT / ".tools" / "3d_pipeline" / "config" / "dependencies.lock.json"


def _meshy_entry() -> Path:
	lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
	route = lock["routes"]["meshy_mcp"]
	runtime = REPO_ROOT / ".tmp" / (
		f"meshy_mcp_compat_v4_{route['version'].replace('.', '_')}_"
		f"sdk_{route['resolved_dependencies']['modelcontextprotocol_sdk']['version'].replace('.', '_')}"
	)
	return runtime / "node_modules" / "@meshy-ai" / "meshy-mcp-server" / "dist" / "index.js"


MESHY_ENTRY = _meshy_entry()


def _windows_processes() -> dict[int, dict[str, Any]]:
	"""Return one non-secret CIM snapshot keyed by PID."""

	script = r"""
$items = @(Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId, Name, CommandLine)
ConvertTo-Json -InputObject @($items) -Compress
"""
	completed = subprocess.run(
		["powershell.exe", "-NoProfile", "-Command", script],
		text=True,
		encoding="utf-8",
		errors="replace",
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		timeout=30,
		check=True,
		creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
	)
	decoded = json.loads(completed.stdout or "[]")
	if isinstance(decoded, dict):
		decoded = [decoded]
	return {int(item["ProcessId"]): item for item in decoded}


def _descendants(root_pid: int, snapshot: dict[int, dict[str, Any]]) -> set[int]:
	owned = {root_pid}
	changed = True
	while changed:
		changed = False
		for pid, item in snapshot.items():
			if pid not in owned and int(item.get("ParentProcessId", -1)) in owned:
				owned.add(pid)
				changed = True
	return owned


def _wait_absent(pids: set[int], timeout: float = 15.0) -> set[int]:
	deadline = time.monotonic() + timeout
	remaining = set(pids)
	while remaining and time.monotonic() < deadline:
		remaining &= set(_windows_processes())
		if remaining:
			time.sleep(0.1)
	return remaining


@dataclass
class Probe:
	process: subprocess.Popen[str]
	stdout_queue: queue.Queue[str] = field(default_factory=queue.Queue)
	stderr: list[str] = field(default_factory=list)
	owned_pids: set[int] = field(default_factory=set)

	@classmethod
	def launch(cls) -> "Probe":
		process = subprocess.Popen(
			["cmd.exe", "/d", "/c", "call", str(WRAPPER_CMD)],
			cwd=REPO_ROOT,
			env=os.environ.copy(),
			text=True,
			encoding="utf-8",
			errors="replace",
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			bufsize=1,
			creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
		)
		probe = cls(process)
		threading.Thread(target=probe._read_stdout, daemon=True).start()
		threading.Thread(target=probe._read_stderr, daemon=True).start()
		return probe

	def _read_stdout(self) -> None:
		assert self.process.stdout is not None
		for line in self.process.stdout:
			self.stdout_queue.put(line)

	def _read_stderr(self) -> None:
		assert self.process.stderr is not None
		self.stderr.extend(self.process.stderr)

	def request_schema(self) -> dict[str, Any]:
		assert self.process.stdin is not None
		messages = [
			{
				"jsonrpc": "2.0",
				"id": 1,
				"method": "initialize",
				"params": {
					"protocolVersion": "2024-11-05",
					"capabilities": {},
					"clientInfo": {"name": "meshy-lifecycle-test", "version": "1.0"},
				},
			},
			{"jsonrpc": "2.0", "method": "notifications/initialized"},
			{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
		]
		for message in messages:
			self.process.stdin.write(json.dumps(message, separators=(",", ":")) + "\n")
		self.process.stdin.flush()

		deadline = time.monotonic() + 45
		while time.monotonic() < deadline:
			try:
				message = json.loads(self.stdout_queue.get(timeout=0.25))
			except queue.Empty:
				if self.process.poll() is not None:
					break
				continue
			if message.get("id") == 2:
				return message
		raise AssertionError(
			f"Meshy schema response did not arrive (exit={self.process.poll()}): "
			+ "".join(self.stderr)[-2000:]
		)

	def capture_owned_tree(self) -> set[int]:
		snapshot = _windows_processes()
		self.owned_pids = _descendants(self.process.pid, snapshot)
		owned_items = [snapshot[pid] for pid in self.owned_pids if pid in snapshot]
		wrapper_nodes = [
			item
			for item in owned_items
			if item.get("Name", "").casefold() == "powershell.exe"
			and str(WRAPPER_PS1.resolve()).casefold() in (item.get("CommandLine") or "").casefold()
		]
		node_nodes = [
			item
			for item in owned_items
			if item.get("Name", "").casefold() == "node.exe"
			and str(MESHY_ENTRY.resolve()).casefold() in (item.get("CommandLine") or "").casefold()
		]
		if len(wrapper_nodes) != 1 or len(node_nodes) != 1:
			raise AssertionError(
			f"Expected one exact PowerShell wrapper and one exact Node child; got {owned_items!r}"
		)
		return self.owned_pids

	def close_stdin_and_wait(self) -> int:
		assert self.process.stdin is not None
		self.process.stdin.close()
		return self.process.wait(timeout=15)

	def kill_parent_and_wait(self) -> None:
		self.process.kill()
		self.process.wait(timeout=10)

	def emergency_cleanup(self) -> None:
		if self.process.poll() is None:
			self.process.kill()
			try:
				self.process.wait(timeout=5)
			except subprocess.TimeoutExpired:
				pass
		for stream in (self.process.stdin, self.process.stdout, self.process.stderr):
			if stream is not None and not stream.closed:
				stream.close()


@unittest.skipUnless(os.name == "nt", "The Meshy wrapper lifecycle contract is Windows-specific.")
class MeshyWrapperLifecycleTests(unittest.TestCase):
	def _assert_schema(self, response: dict[str, Any]) -> None:
		self.assertNotIn("error", response)
		tools = response.get("result", {}).get("tools", [])
		image_tool = next(item for item in tools if item.get("name") == "meshy_image_to_3d")
		self.assertIn("meshy-7", json.dumps(image_tool.get("inputSchema", {}), sort_keys=True))

	def test_two_consecutive_schema_probes_exit_their_exact_process_trees(self) -> None:
		for _ in range(2):
			probe = Probe.launch()
			try:
				self._assert_schema(probe.request_schema())
				owned = probe.capture_owned_tree()
				self.assertEqual(0, probe.close_stdin_and_wait())
				self.assertEqual(set(), _wait_absent(owned))
			finally:
				probe.emergency_cleanup()

	def test_concurrent_schema_probes_keep_pid_ownership_disjoint_and_exit(self) -> None:
		probes = [Probe.launch(), Probe.launch()]
		try:
			responses: list[dict[str, Any] | None] = [None, None]
			failures: list[BaseException] = []

			def request(index: int) -> None:
				try:
					responses[index] = probes[index].request_schema()
				except BaseException as exc:  # Preserve worker-thread assertion details.
					failures.append(exc)

			threads = [threading.Thread(target=request, args=(index,)) for index in range(2)]
			for thread in threads:
				thread.start()
			for thread in threads:
				thread.join(timeout=50)
			if failures:
				raise failures[0]
			for response in responses:
				assert response is not None
				self._assert_schema(response)

			owned = [probe.capture_owned_tree() for probe in probes]
			self.assertEqual(set(), owned[0] & owned[1])
			for probe in probes:
				assert probe.process.stdin is not None
				probe.process.stdin.close()
			for probe in probes:
				self.assertEqual(0, probe.process.wait(timeout=15))
			for pid_set in owned:
				self.assertEqual(set(), _wait_absent(pid_set))
		finally:
			for probe in probes:
				probe.emergency_cleanup()

	def test_terminated_cmd_parent_releases_wrapper_owned_node_tree(self) -> None:
		probe = Probe.launch()
		try:
			self._assert_schema(probe.request_schema())
			owned = probe.capture_owned_tree()
			probe.kill_parent_and_wait()
			self.assertEqual(set(), _wait_absent(owned))
		finally:
			probe.emergency_cleanup()


if __name__ == "__main__":
	unittest.main()
