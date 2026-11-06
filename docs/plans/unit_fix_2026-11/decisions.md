# Custom unit model repair, November 2026: decisions

## Scripted repair of existing units (user decision, 2026-11-06)

Disposition: `accepted and queued`. The basis is a user decision of 2026-11-06, relayed by the coordinating session. Implementation is in progress on branch `cr-3d-unit-fixes`.

The 3D skill forbade any repository script or adapter operation from generating bones, skin weights or keyframes. Repairing the shipped units needs scripted Blender operations, so the user decided on a hybrid rule:

- **Scripts may repair geometry.** This covers cutting fused body parts, filling holes, and fixing winding, normals and one-sided faces.
- **Scripts may correct existing weights.** This covers moving cloth, tails and wings off the nearest limb, smoothing, and limiting influences.
- **Scripts may correct grounding.** This covers ground contact on existing actions.
- **New rigs and actions stay live.** New creature rigs and new actions are authored live in Blender through the Blender MCP. Template rigs and procedural gaits are not used for Chaos Redux units.
- **Review gates every unit.** A unit is accepted only after it has been rendered and a fresh-context reviewer, given only the renders and the quality bar, finds no defect.
- **Free work comes first.** Free live re-authoring comes before any paid provider action or new generation. A paid step needs user approval, and only after the unit still fails review.

The narrowed policy is in `.claude/skills/chaos-redux-3d-model-pipeline/SKILL.md` under `Skeleton, skinning, and action policy`.
