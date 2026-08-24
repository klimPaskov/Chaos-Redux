# Required-action manifest

All eight roles are blocked at the shared provider-rig gate. No `.anim` file exists and no semantic alias, static pose, procedural action, or Blender-authored replacement motion was used.

| Role | FPS | Loop | Root policy | Required substantive evidence | Status |
|---|---:|---|---|---|---|
| idle | 24 | yes | in place | horse breathing/weight shift and mounted rider settling | blocked |
| move / gallop | 24 | yes | in-place canter | four-beat hoof contacts and coherent rider follow-through | blocked |
| attack / sling | 24 | no | in place | wind-up, aim, discharge, recoil, recovery | blocked |
| defend | 24 | yes | in place | horse brace and rider guarded response | blocked |
| support attack | 24 | no | in place | distinct mounted support throw cycle | blocked |
| retreat | 24 | yes | in-place retreat gait | distinct retreat motion, not a renamed move cycle | blocked |
| training | 24 | yes | in place | controlled sling drill and horse response | blocked |
| death | 24 | no | contact-corrected collapse | articulated horse+rider impact, collapse, and settling | blocked |

Meshy 7 generation task `01a03404-f74d-7d5b-876d-5f426afe11f6` and remesh task `01a03418-57e3-7399-bf55-2d769bedabee` succeeded. The rig recovery failed with HTTP 422 pose-estimation failure, so there is no valid `rig_task_id` accepted by `meshy_animate`.

The v9 live audit confirmed this is a provider capability blocker, not merely a bad retry. Meshy's official [Rigging API](https://docs.meshy.ai/en/api/rigging) says programmatic rigging is for standard humanoid bipeds and is unsuitable for nonhumanoid assets. Its official [Animation API](https://docs.meshy.ai/en/api/animation) requires the ID of a successfully completed Meshy rig task. A separated rider can satisfy only the humanoid half; the living horse has no Meshy quadruped rig/action source. No further paid call was made because it could not supply compliant mounted motion.
