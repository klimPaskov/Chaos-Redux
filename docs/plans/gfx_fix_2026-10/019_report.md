# Event 019 graphics repair

The two zombie focus badges retain their original artwork and canvases, with fully opaque interiors and antialiasing confined to the surviving outlines.
The detached fragment outside A Realm of Base Dead is removed.
The prototype-cannibalization decision icon retains its scrap-pile silhouette without the isolated translucent base speckles.

| Sprite | Runtime DDS | Result |
| --- | --- | --- |
| GFX_goal_infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks | gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks.dds | Solid badge interior; main silhouette preserved. |
| GFX_goal_infantry_spawn_derivative_zombie_a_realm_of_base_dead | gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_zombie_a_realm_of_base_dead.dds | Solid badge; detached nineteen-pixel source fragment removed. |
| GFX_decision_infantry_spawn_prototype_cannibalization | gfx/interface/decisions/019_infantry_spawn/prototype_cannibalization.dds | Solid scrap pile with cleaned base. |

The base and shine focus sprites share the same repaired textures.
No sprite, focus, decision, reward, or AI identifier changed.
The original 100x88 focus canvases and 33x32 decision canvas remain consistent with their inspected consumers.

Parent native/4x review and the independent `alpha_review` worker accepted all three outputs on 2026-10-06 within the user-assigned graphics scope.
The independent row hashes, source/runtime bounds, masks, native-size comparisons and strict DDS round-trip proof are in `alpha_independent_review.md` and `evidence/alpha/`.
No assigned art repair was omitted or substituted.

Orchestrator live check: use a fresh paused 1936 session with an independent Event 019 zombie derivative country and its derivative focus tree.
Open the zombie branch and inspect Scavenge the Abandoned Barracks and A Realm of Base Dead at normal and close zoom, including their highlighted states.
Expected: solid interiors, intact wreaths and no detached fleck outside the latter badge.
For the decision icon, use a country with an Event 019 prototype and open its Prototype Cannibalization decision; the scrap pile should have a clean, solid base.

Skills used: event-assets, subagents, shared-git-commit; focus-tree guidance was consulted for the consumer audit.
