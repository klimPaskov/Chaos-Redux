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

## Temporal guard weapon and paleogenetic tentacle chains (user decision, 2026-11-06)

Disposition: `accepted and queued`. The basis is a user decision of 2026-11-06, relayed by the coordinating session in answer to the two open questions in `reauthor_plans_first_five.md`. Implementation is queued on branch `cr-3d-live-reauthor`, where the units are re-authored live.

- **The temporal guard carries a weapon.** The weapon fits the unit's time-themed lore in Chaos Redux (the Temporal Continuity Guard and its Continuity Field Apparatus). It is modelled live in Blender as a component, attached through a real hand control, and the attack and defend actions are planned around it. This replaces the plan's earlier default of unarmed close combat.
- **The paleogenetic creature gets two new tentacle chains.** All six visible tentacles are rigged. The two new chains and their weights are authored live, and the weights stay off the body.

## Modelled tatter and the review procedure (user decision, 2026-11-06)

Disposition: `accepted and queued`. The basis is a maintainer decision of 2026-11-06, relayed by the coordinating session. Implementation is in progress on branch `cr-3d-author-3`, where the two affected units are re-authored live.

- **Tatter is design.** The see-through tears in the demonic zombies' wing membranes and the ragged, spiky hem of the death ghost hosts' coat are intended looks. Their review requests tell the reviewer so, and the reviewer does not report them. Everything else is still judged: stretching, clipping, floating, weights, ground contact and how each clip reads.
- **Double-sided membranes stay.** The demonic zombies' wing faces are duplicated with reversed winding, so the membranes do not vanish from behind. That repair is kept.
- **The bar stays at zero findings.** A unit is accepted only when a fresh reviewer reports no defect.
- **Rounds are consistent.** Every reviewer gets the same fixed checklist and the same fixed camera angles in each round. Intermediate rounds re-review only the clips that changed. One full fresh review of every clip ends each unit before it is accepted.
