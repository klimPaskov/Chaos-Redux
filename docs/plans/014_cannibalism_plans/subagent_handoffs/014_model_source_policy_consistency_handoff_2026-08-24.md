# 014 model source policy consistency handoff

Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` to make the source-first model-reference policy internally consistent.

The skill now requires actual Internet-sourced modern designed artwork, excludes archival and historical material, permits copyrighted artwork only as `reference_only_user_authorized` with explicit user authorization and no `NoAI` restriction, and requires native ImageGen faithful edits that preserve the selected subject rather than redesigning it.

The bounded `chaosx_3d_model_pipeline` contract now carries the same faithful-edit rules and requires exactly one cleaned `refs/original/meshy_input.png`; from-scratch generation is permitted only after documented eligible-source search failure and explicit parent/user approval.

No gameplay, asset, runtime, or provider files were changed, and no commit was created. Parent review and commit ownership remain with `/root`.

The earlier `chaosx_3d_model_pipeline_skill_update_2026-08-22.md` handoff contains superseded source wording; this handoff records the current policy correction.
