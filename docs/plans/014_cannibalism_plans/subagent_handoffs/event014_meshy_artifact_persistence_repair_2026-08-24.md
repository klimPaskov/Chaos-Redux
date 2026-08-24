# Event 014 Meshy artifact persistence repair handoff

## Scope

This tranche repairs the repository-owned locked Meshy MCP compatibility wrapper only.
No Event 014 model package, gameplay file, source asset, paid task, or preserved task ID was changed.

## Root causes and repair

The official `meshy_download_model` implementation persisted ordinary `model_urls` outputs but returned signed URL inventories for rigging and animation `result` objects, ignoring `save_to` for those task families.
The compatibility patch now selects and persists the exact requested official-return artifact for generation, rigging, and animation tasks, including `processed_24fps`, and returns a receipt containing the original task ID, contained local path, byte size, and SHA-256 checksum.
Signed source URLs and query credentials are omitted from successful responses and sanitized from download failures; failures are fail-closed without a manual-download fallback.
All explicit and auto-managed destinations must resolve inside the repository, including their nearest existing real-path ancestor.

The task tool imports `getTaskWithAutoInference` from `services/meshy-client.js`.
The locked patch now verifies and, for the known compatible baseline, repairs that named export before starting Node, then verifies the final import/export contract without weakening preferred-endpoint-first inference.
Exact hashes for the patched task tool, task schema, and client service are locked under Meshy compatibility revision `meshy-7-v5`.

## Owned files

- `.tools/3d_pipeline/wrappers/run_meshy_mcp.ps1`
- `.tools/3d_pipeline/wrappers/patch_meshy_mcp.mjs`
- `.tools/3d_pipeline/tests/test_meshy_wrapper_artifact_compatibility.py`
- Meshy-only fields in `.tools/3d_pipeline/config/dependencies.lock.json`
- This handoff

## Focused evidence

- `python .tools/3d_pipeline/tests/test_meshy_wrapper_artifact_compatibility.py`: 2/2 passed.
  The test imports and parses the actual patched task module, checks the advertised `processed_24fps` schema selector, invokes the registered MCP handlers against local signed-URL fixtures, persists generation GLB, rig FBX, and animation processed-24fps FBX artifacts, verifies task IDs and SHA-256 receipts, proves signed URLs are absent, rejects an out-of-repository destination, exercises preferred-first status inference, removes the client-service export in an isolated copy, and proves two patch passes restore it idempotently with all three JavaScript files parseable.
- `python .tools/3d_pipeline/tests/test_meshy_wrapper_lifecycle.py`: 4/4 passed.
  This includes two consecutive schema probes, concurrent disjoint exact-PID ownership, terminated-parent cleanup, and full-verifier receipt ownership with zero owned survivors.
- Two consecutive `python .tools/3d_pipeline/verify_environment.py --probe-meshy` runs reported zero `meshy_mcp*` findings.
  Both runs retained one unrelated adapter hash finding caused by a concurrent adapter tranche; no Meshy wrapper finding or owned-process survivor remained.

## Restart and recovery use

Clients must close any pre-repair Meshy MCP process and start a fresh process through `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd` so compatibility revision `meshy-7-v5` is loaded.
Do not kill or reuse another route owner's live server.
Before polling or downloading an already-paid Event 014 task, run `python .tools/3d_pipeline/verify_environment.py --probe-meshy` and require zero `meshy_mcp*` findings, then call `meshy_get_task_status` and `meshy_download_model` through the locked MCP only.
For a processed animation FBX, pass the preserved animation task ID with `task_type: "animation"`, `format: "fbx"`, `artifact: "processed_24fps"`, and a repository-contained absolute `save_to` path.
No conversion or generation task is needed to archive an artifact already present in the official task result.

## Simplifications, omissions, and blockers

No fallback or simplification was introduced.
This tranche intentionally made no paid provider call and did not poll or alter preserved Event 014 task IDs.
