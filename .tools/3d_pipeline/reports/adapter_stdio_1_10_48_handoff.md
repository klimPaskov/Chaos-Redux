# Adapter 1.10.48 stdio response lifecycle

Disposition: implemented and validated; parent owns release review and commit.

The exact repository wrapper intermittently lost its tools/list result when the caller sent all three JSON-RPC messages through communicate() and closed stdin immediately.
The unchanged 1.10.47 route reproduced this once in six fresh attempts, with exit 0 and ListToolsRequest on stderr.
An independent response-drained probe succeeded six times, and a local asynchronous fixture deterministically reproduces the old EOF cancellation.
This is an observed transport race; successful individual legacy calls do not establish that every call is reliable.

The transport selects only the exact command below after resolving its repository wrapper path.
It waits for successful initialize id 1 before sending notifications/initialized and the request, concurrently drains stdout and stderr, and sends stdin EOF only after matching response id 2 arrives.
A single deadline covers exchange and server shutdown.
EOF, initialization errors, request errors, wrong response ids and timeouts fail closed; Windows job ownership, descendant cleanup and survivor checks remain in force.
There is no request retry or mutation replay in this exchange.
Every other command, including provider routes, uses its unchanged existing communicate exchange.

```python
root = Path(repository_path).resolve()
command = ['cmd.exe', '/d', '/c', 'call', str(root / '.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd')]
call_stdio(command, list_tools=True, cwd=root, timeout_seconds=60)
BlenderAdapterClient(root).health('mutant_zombies')
```

The config and dependency lock identify 1.10.48 and lock 19 source files, adding lib/mcp_stdio.py.
All 17 prior non-config source hashes, all 51 operation names, the server wrapper and every 1.10.47 repair implementation remain unchanged.
The transport file has an explicit LF Git attribute and every locked source has equal raw and Git-clean bytes.

Validation: 41 tests passed: 11 transport subprocess regressions, 19 release/recovery regressions and 11 explicit batch contract regressions.
Transport cases cover delayed responses, deterministic legacy EOF cancellation, early EOF, initialize and request errors, response-id mismatch, timeout with owned child-process cleanup, heavy stderr, exact command scope, one mutation request and unchanged other-route behavior.
Final live validation used six fresh tools/list calls, three fresh health calls and one harmless inspect_scene through BlenderAdapterClient; all ten responses arrived before stdin EOF, with no surviving owned processes.
Each discovery returned all 51 operations.
The native inspection request was 567690f961b74c0b8e2b86a5ca61310c.
The Mutant checkpoint SHA remained 138DE96AC6F0957321768ECB00805091EE7E113F176A91DD46FC0A4B3F5720A8 before and after inspection.
No model checkpoint was saved, no provider was called and verify_environment reported findings=[].
The live receipt embeds exact source/config/lock/wrapper hashes, lifecycle records, health results and the native inspection result.

No simplifications were made.
This release proves the bounded transport behavior and preserves repair sources; it does not claim new model quality or in-game validation.
No files were staged or committed by this worker.
The 3D pipeline skill guided the adapter route and source-immutability discipline; no skill was modified.

Exact release-owned commit paths:

```
.gitattributes
.tools/3d_pipeline/lib/mcp_stdio.py
.tools/3d_pipeline/config/blender_hoi4_adapter.json
.tools/3d_pipeline/config/dependencies.lock.json
.tools/3d_pipeline/reports/environment_report.json
.tools/3d_pipeline/tests/test_blender_stdio_response.py
.tools/3d_pipeline/tests/blender_stdio_response_probe.py
.tools/3d_pipeline/tests/blender_stdio_live_regression.py
.tools/3d_pipeline/reports/adapter_stdio_1_10_47_reproduction.json
.tools/3d_pipeline/reports/adapter_stdio_1_10_47_response_probe.json
.tools/3d_pipeline/reports/adapter_stdio_1_10_48_live.json
.tools/3d_pipeline/reports/adapter_stdio_1_10_48_unit_tests.json
.tools/3d_pipeline/reports/adapter_stdio_1_10_48_handoff.md
.tools/3d_pipeline/reports/adapter_stdio_1_10_48_release.json
```

Exclude these pre-existing or concurrently owned dirty pipeline paths:

```
.tools/3d_pipeline/adapter/pyproject.toml
.tools/3d_pipeline/adapter/uv.lock
.tools/3d_pipeline/config/asset_profiles.json
.tools/3d_pipeline/config/pilot_jobs.json
.tools/3d_pipeline/init_pilot_jobs.py
.tools/3d_pipeline/lib/paths.py
.tools/3d_pipeline/manual_recovery/recover_existing_units.py
.tools/3d_pipeline/reports/adapter_1_10_3_scale_persistence_handoff.md
.tools/3d_pipeline/run_pilot.py
.tools/3d_pipeline/tests/blender_action_phase_patch_integration.py
.tools/3d_pipeline/tests/blender_dual_source_base_regression.py
.tools/3d_pipeline/tests/blender_excluded_contact_grounding_integration.py
.tools/3d_pipeline/tests/blender_prepare_scale_persistence_integration.py
.tools/3d_pipeline/tests/blender_saved_normalization_realfile_regression.py
.tools/3d_pipeline/tests/blender_scale_aware_retarget_integration.py
.tools/3d_pipeline/tests/blender_weight_only_sanitize_integration.py
.tools/3d_pipeline/tests/test_meshy_wrapper_lifecycle.py
.tools/3d_pipeline/tests/test_prepare_scale_persistence.py
.tools/3d_pipeline/tests/test_scale_aware_retarget.py
.tools/3d_pipeline/tests/test_weight_only_sanitize_contract.py
.tools/3d_pipeline/verify_environment.py
.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd
.tools/3d_pipeline/wrappers/run_meshy_mcp.ps1
.tools/3d_pipeline/adapter/mesh_winding_seam.py
.tools/3d_pipeline/adapter/pdx_skin_membership.py
.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json
.tools/3d_pipeline/tests/test_fitted_humanoid_repair.py
.tools/3d_pipeline/tests/test_mesh_winding_seam.py
```

All unrelated model, runtime, gameplay and documentation changes outside this explicit list are also excluded.
Native read-only request/result logs written by the adapter are not required commit inputs because the release live receipt embeds the reviewed results.
