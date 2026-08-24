"""Regression coverage for the locked Meshy task/download compatibility patch."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from test_meshy_wrapper_lifecycle import Probe, REPO_ROOT


RUNTIME = REPO_ROOT / ".tmp" / "meshy_mcp_compat_v4_0_4_0_sdk_1_29_0"
TASKS_MODULE = (
	RUNTIME
	/ "node_modules"
	/ "@meshy-ai"
	/ "meshy-mcp-server"
	/ "dist"
	/ "tools"
	/ "tasks.js"
)
PATCH_SCRIPT = REPO_ROOT / ".tools" / "3d_pipeline" / "wrappers" / "patch_meshy_mcp.mjs"


class MeshyArtifactCompatibilityTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		# Exercise the exact wrapper reconstruction path before importing patched JS.
		probe = Probe.launch()
		try:
			response = probe.request_schema()
			if "result" not in response:
				raise AssertionError(f"Meshy tools/list failed: {response}")
			tools = {tool["name"]: tool for tool in response["result"]["tools"]}
			download_schema = tools["meshy_download_model"]["inputSchema"]
			artifact_schema = download_schema["properties"]["artifact"]
			if "processed_24fps" not in artifact_schema.get("enum", []):
				raise AssertionError(f"Meshy artifact selector missing from tools/list: {artifact_schema}")
			if probe.close_stdin_and_wait() != 0:
				raise AssertionError("Meshy wrapper did not close normally after compatibility setup.")
		finally:
			probe.emergency_cleanup()

	def test_generation_rig_animation_persistence_and_status_inference(self) -> None:
		with tempfile.TemporaryDirectory(dir=REPO_ROOT / ".tmp") as output_dir:
			harness = Path(output_dir) / "artifact_harness.mjs"
			harness.write_text(
				"""
import crypto from "node:crypto";
import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [tasksPath, outputRoot] = process.argv.slice(2);
const payloads = {
  "/generation.glb": Buffer.from("generation-artifact"),
  "/rig.fbx": Buffer.from("rig-artifact"),
  "/animation24.fbx": Buffer.from("animation-24fps-artifact")
};
const httpServer = http.createServer((request, response) => {
  const body = payloads[new URL(request.url, "http://127.0.0.1").pathname];
  if (!body) { response.writeHead(404).end(); return; }
  response.writeHead(200, { "content-length": body.length });
  response.end(body);
});
await new Promise(resolve => httpServer.listen(0, "127.0.0.1", resolve));
const port = httpServer.address().port;
const signed = file => `http://127.0.0.1:${port}/${file}?Signature=SECRET&Expires=999999`;

const tasks = {
  generation: { id: "generation", status: "SUCCEEDED", model_urls: { glb: signed("generation.glb") } },
  rig: { id: "rig", status: "SUCCEEDED", result: { rigged_character_fbx_url: signed("rig.fbx") } },
  animation: { id: "animation", status: "SUCCEEDED", result: { processed_animation_fps_fbx_url: signed("animation24.fbx") } },
  inferred: { id: "inferred", status: "SUCCEEDED", progress: 100, model_urls: { glb: signed("generation.glb") } }
};
const endpointFor = { generation: "image-to-3d", rig: "rigging", animation: "animations", inferred: "image-to-3d" };
const calls = [];
const client = {
  async get(route) {
    calls.push(route);
    const id = route.split("/").at(-1);
    if (!tasks[id] || !route.includes(endpointFor[id])) throw new Error("not found");
    return tasks[id];
  }
};
const handlers = {};
const server = { registerTool(name, _definition, handler) { handlers[name] = handler; } };
const { registerTaskTools } = await import(pathToFileURL(tasksPath));
registerTaskTools(server, client);

const cases = [
  ["generation", { task_id: "generation", task_type: "image-to-3d", format: "glb", artifact: "primary", include_textures: false }],
  ["rig", { task_id: "rig", task_type: "rigging", format: "fbx", artifact: "primary", include_textures: false }],
  ["animation24", { task_id: "animation", task_type: "animation", format: "fbx", artifact: "processed_24fps", include_textures: false }]
];
const results = {};
for (const [name, params] of cases) {
  const saveTo = path.join(outputRoot, `${name}.${params.format}`);
  const result = await handlers.meshy_download_model({ ...params, save_to: saveTo });
  if (result.isError) throw new Error(JSON.stringify(result));
  const serialized = JSON.stringify(result);
  if (/Signature=|Expires=|127\.0\.0\.1/.test(serialized)) throw new Error(`signed URL leaked for ${name}`);
  const bytes = fs.readFileSync(saveTo);
  const digest = crypto.createHash("sha256").update(bytes).digest("hex");
  if (result.structuredContent.task_id !== params.task_id || result.structuredContent.sha256 !== digest) {
    throw new Error(`receipt mismatch for ${name}`);
  }
  results[name] = result.structuredContent;
}

const outside = path.join(path.dirname(path.dirname(path.dirname(outputRoot))), "meshy-outside-regression.glb");
const escaped = await handlers.meshy_download_model({
  task_id: "generation", task_type: "image-to-3d", format: "glb", artifact: "primary",
  include_textures: false, save_to: outside
});
if (!escaped.isError || fs.existsSync(outside)) throw new Error("repository containment was not enforced");

const status = await handlers.meshy_get_task_status({
  task_id: "inferred", task_type: "text-to-3d", wait: false, response_format: "markdown"
});
if (status.isError || !JSON.stringify(status).includes("inferred")) throw new Error("status inference failed");
if (!calls.some(route => route.includes("text-to-3d/inferred")) || !calls.some(route => route.includes("image-to-3d/inferred"))) {
  throw new Error("status did not preserve preferred-first auto-inference");
}

httpServer.close();
process.stdout.write(JSON.stringify(results));
""",
				encoding="utf-8",
			)
			completed = subprocess.run(
				["node", str(harness), str(TASKS_MODULE), output_dir],
				cwd=REPO_ROOT,
				text=True,
				encoding="utf-8",
				errors="replace",
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				timeout=30,
				check=False,
			)
			self.assertEqual(0, completed.returncode, completed.stderr)
			receipts = json.loads(completed.stdout)
			self.assertEqual({"generation", "rig", "animation24"}, set(receipts))
			for receipt in receipts.values():
				self.assertEqual(64, len(receipt["sha256"]))
				self.assertGreater(receipt["file_size_bytes"], 0)

	def test_missing_status_inference_export_is_repaired_idempotently(self) -> None:
		package_root = RUNTIME / "node_modules" / "@meshy-ai" / "meshy-mcp-server"
		with tempfile.TemporaryDirectory(dir=REPO_ROOT / ".tmp") as temp_dir:
			copy_root = Path(temp_dir) / "package"
			for relative in (
				Path("dist/tools/tasks.js"),
				Path("dist/schemas/tasks.js"),
				Path("dist/services/meshy-client.js"),
			):
				target = copy_root / relative
				target.parent.mkdir(parents=True, exist_ok=True)
				shutil.copy2(package_root / relative, target)
			client_path = copy_root / "dist" / "services" / "meshy-client.js"
			client_path.write_text(
				client_path.read_text(encoding="utf-8").replace(
					"export async function getTaskWithAutoInference(",
					"async function getTaskWithAutoInference(",
					1,
				),
				encoding="utf-8",
			)
			for _ in range(2):
				completed = subprocess.run(
					["node", str(PATCH_SCRIPT), str(copy_root), str(REPO_ROOT)],
					cwd=REPO_ROOT,
					text=True,
					encoding="utf-8",
					errors="replace",
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE,
					timeout=15,
					check=False,
				)
				self.assertEqual(0, completed.returncode, completed.stderr)
				hashes = json.loads(completed.stdout)
				self.assertIn("dist/services/meshy-client.js", hashes)
			self.assertIn(
				"export async function getTaskWithAutoInference(",
				client_path.read_text(encoding="utf-8"),
			)
			for relative in ("dist/tools/tasks.js", "dist/schemas/tasks.js", "dist/services/meshy-client.js"):
				checked = subprocess.run(
					["node", "--check", str(copy_root / relative)],
					text=True,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE,
					check=False,
				)
				self.assertEqual(0, checked.returncode, checked.stderr)


if __name__ == "__main__":
	unittest.main(verbosity=2)
