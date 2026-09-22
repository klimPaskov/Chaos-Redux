# Superseded drafts — do not restore

This subtree holds working drafts from the adapter recovery work that preceded the current pipeline.

Status: `superseded`.

The drafts contain complete pre-removal copies of the adapter, including `blender_worker.py` and the MCP server with the rig, skin-weight and keyframe authoring operations that were deleted from the pipeline: the declarative humanoid and creature rig builders, the fitted-humanoid repair route, the skin and batch-skin repairs, the action phase patcher, the locomotion authoring operation, the clip import and retime operations, and the manual recovery script.

Nothing in this subtree may be copied back into `.tools/3d_pipeline`, and no draft publish script or validation script here may be run. Their file lists and test lists are stale: they name test files that were deleted with those operations, and running them would recreate code the pipeline is not allowed to carry.

The current rules live in `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`: no repository Python script and no adapter operation may generate bones, skin weights or keyframes from a declarative spec, a template or a formula; provider results are ingested as authored assets; everything else is authored live in Blender; and manual work takes no shortcuts.

The current adapter surface is the 32 operations recorded in `.tools/3d_pipeline/config/blender_hoi4_adapter.json` and `.tools/3d_pipeline/config/dependencies.lock.json`.

These drafts are retained only as a record of how the current adapter was reached.
