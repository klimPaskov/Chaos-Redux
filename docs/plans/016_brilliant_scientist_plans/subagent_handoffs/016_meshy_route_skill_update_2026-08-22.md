# Meshy MCP runtime recovery documentation handoff

Status: documentation updated; the parent resolved and verified the live process-cleanup gate after this documentation pass.

## Exact changes

- Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` in the existing Meshy compatibility-wrapper guidance. It now requires exact version, package integrity, and git-head locks for the official Meshy server and transitive `@modelcontextprotocol/sdk`; both SDK server entry points; a versioned compatibility runtime; an interprocess install/patch mutex; two consecutive and one concurrent `tools/list` probe pair exposing Meshy 7; a live balance probe; zero exact-route provider processes before paid work; and Windows kill-on-close Job Object or equivalent process-tree ownership for stdio calls.
- Updated `.tools/3d_pipeline/README.md` under `Lock and route gate` with the same generic runtime-recovery gates and the exact repository wrapper path.
- No gameplay, tools code, `.qoder/**`, or provider-paid operation was changed or run.

## Verification evidence

- The locked route is `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, integrity `sha512-py2xFIrrBcU4SW7ked90/qjRqa6bheVn0fNLEW8Lnki3BCJTFaVvWN0W6a9mJYr26+M9y0WezGsTCKalzWrGtg==`.
- Its transitive `@modelcontextprotocol/sdk` is `1.29.0`, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32`, integrity `sha512-zo37mZA9hJWpULgkRpowewez1y6ML5GsXJPY8FI0tBBCd77HEvza4jDqRKOXgHNn867PVGCyTdzqpz0izu5ZjQ==`.
- The versioned runtime `.tmp/meshy_mcp_compat_v4_0_4_0_sdk_1_29_0/` contains both `dist/esm/server/index.js` and `dist/esm/server/streamableHttp.js`.
- Two consecutive and one concurrent pair of `tools/list` calls through `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd` returned the live Meshy tool surface, and each `meshy_image_to_3d` declaration exposed `meshy-7`.
- The live `meshy_check_balance` probe returned `626` credits. The route tool names observed through the active MCP surface include `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.

## Parent resolution

The documentation worker correctly stopped when it observed 18 matching wrapper/provider processes in the shared workspace. The parent then identified every process as an orphaned exact-path instance of this repository's Meshy wrapper or provider entry point, stopped only those exact processes, and confirmed a zero count.

The parent added Windows kill-on-close Job Object ownership to `.tools/3d_pipeline/lib/mcp_stdio.py`, extended `.tools/3d_pipeline/verify_environment.py` to validate both locked SDK entry points and exact-route cleanup, and reran `python -B .tools/3d_pipeline/verify_environment.py --probe-meshy`. The regenerated report at `.tools/3d_pipeline/reports/environment_report.json`, timestamp `2026-08-22T11:16:30Z`, records no findings, a successful Meshy 7 schema probe, balance 626, and `meshy_mcp_process_cleanup = true` with an empty exact-route process list. The route-health blocker is resolved for the authorized recovery attempt.
