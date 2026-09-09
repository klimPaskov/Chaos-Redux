"""Bounded motion contract tests; no provider submissions."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / ".tools/3d_pipeline"))
from meshy_client import MeshyClient


class MotionTests(unittest.TestCase):
    def test_uncertain_submission_is_journaled_before_transport(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict("os.environ", {"MESHY_API_KEY": "test-only"}):
            client = MeshyClient(ROOT, Path(folder))
            def uncertain(*args, **kwargs):
                journals = list(Path(folder).glob("provider/submissions/*.json"))
                self.assertEqual(1, len(journals))
                self.assertEqual("submission_started", json.loads(journals[0].read_text())["state"])
                raise TimeoutError("simulated uncertain response")
            with patch("meshy_client.call_stdio", side_effect=uncertain) as transport:
                with self.assertRaises(TimeoutError):
                    client.text_to_motion(prompt="collapse", mode="prime", duration=3)
                self.assertEqual(1, transport.call_count)
            journal = next(Path(folder).glob("provider/submissions/*.json"))
            self.assertEqual("uncertain", json.loads(journal.read_text())["state"])

    def test_invalid_motion_and_animation_inputs_never_call_transport(self):
        with patch.dict("os.environ", {"MESHY_API_KEY": "test-only"}), patch("meshy_client.call_stdio") as transport:
            client = MeshyClient(ROOT)
            for duration in (1, 3.1, 11):
                with self.assertRaises(ValueError):
                    client.text_to_motion(prompt="collapse", mode="prime", duration=duration)
            for arguments in ({}, {"action_id": 1, "motion_task_id": "motion"}):
                with self.assertRaises(ValueError):
                    client.animate(rig_task_id="rig", estimate_credits=3, **arguments)
            transport.assert_not_called()

    def test_runtime_motion_routes_and_no_paid_retry(self):
        runtime = ROOT / ".tmp/meshy_mcp_compat_v4_0_4_0_sdk_1_29_0/node_modules/@meshy-ai/meshy-mcp-server/dist"
        script = r'''
import assert from "node:assert/strict";
import { pathToFileURL } from "node:url";
const root = process.argv[1];
const tools = {}, calls = [];
const server = { registerTool(name, definition, handler) { tools[name] = { definition, handler }; } };
const client = { async post(endpoint, body) { calls.push({ endpoint, body }); return { result: "motion-id" }; },
 async get(endpoint, params) { calls.push({ endpoint, params }); return { id: "motion-id", status: "SUCCEEDED", consumed_credits: 10, result: { motion_url: "SECRET", motion_format: "fbx" } }; } };
const { registerMotionTools } = await import(pathToFileURL(root + "/tools/motion-compat.js"));
registerMotionTools(server, client);
assert.equal(Object.keys(tools).length, 5);
const input = { prompt: "collapse", mode: "prime", duration: 3 };
assert.equal((await tools.meshy_text_to_motion.handler(input)).structuredContent.task_id, "motion-id");
assert.deepEqual(calls[0], { endpoint: "/openapi/v1/text-to-motion", body: input });
assert.ok(!JSON.stringify(await tools.meshy_get_motion_status.handler({ task_id: "motion-id" })).includes("SECRET"));
await tools.meshy_list_motion_tasks.handler({ page_num: 2, page_size: 20 });
assert.equal(calls.at(-1).params.page_num, 2);
const { MeshyClient } = await import(pathToFileURL(root + "/services/meshy-client.js"));
const actual = new MeshyClient("test-only");
let attempts = 0;
actual.client.request = async () => { attempts++; const error = new Error("timeout"); error.code = "ECONNRESET"; throw error; };
await assert.rejects(actual.post("/openapi/v1/text-to-motion", input));
assert.equal(attempts, 1);
const { registerPostProcessingTools } = await import(pathToFileURL(root + "/tools/postprocessing.js"));
registerPostProcessingTools(server, client);
const previous = calls.length;
assert.ok((await tools.meshy_animate.handler({ rig_task_id: "rig", action_id: 1, motion_task_id: "motion" })).isError);
assert.equal(calls.length, previous);
await tools.meshy_animate.handler({ rig_task_id: "rig", motion_task_id: "motion", response_format: "json" });
assert.deepEqual(calls.at(-1).body, { rig_task_id: "rig", motion_task_id: "motion" });
console.log("motion endpoint contracts passed");
'''
        result = subprocess.run(["node", "--input-type=module", "-e", script, str(runtime)], capture_output=True, text=True, timeout=30)
        self.assertEqual(0, result.returncode, result.stderr)


if __name__ == "__main__":
    unittest.main()
