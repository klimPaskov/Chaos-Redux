# Armed humanoid adapter recovery documentation handoff

Status: reusable workflow guidance updated; no adapter or gameplay files changed.

## Exact changes

- Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` beside the Blender checkpoint, rig, and action guidance. It now requires grouped visual review of explicit loose-component ids, forbids bounds-only selection, preserves the source checkpoint during review, requires visible hand/shoulder alignment before export, documents the 24-bone body plus dedicated `weapon` bone and rigid weapon binding, lists the seven armed action roles, and keeps the recovery operations job-root-bounded with no arbitrary Python, shell, URL, or unrestricted path inputs.
- Updated `.tools/3d_pipeline/README.md` in the humanoid animation section with the exact repository-owned adapter operations and the same review, alignment, rig, action, and input-boundary rules.
- Added no adapter, client, configuration, dependency-lock, gameplay, asset, or `.qoder/**` changes, and made no commit.

## Route verification

- A live `tools/list` probe through `.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd` exposed `chaosx_blender_hoi4_review_humanoid_components` and `chaosx_blender_hoi4_isolate_humanoid_weapon`, along with `chaosx_blender_hoi4_author_humanoid_rig` and `chaosx_blender_hoi4_author_humanoid_actions`.
- A live adapter health probe reported `chaosx_blender_hoi4` version `1.6.0`, Blender `5.1.2`, and loaded `io_pdx_mesh` export functions.
- The ambient preloaded `mcp__blender_hoi4` catalog in this session did not list the two new operation names, so treat that separate route as stale or requiring refresh; the repository-owned wrapper route above is the verified callable surface. Do not claim direct ambient-tool availability until it exposes the same names.
