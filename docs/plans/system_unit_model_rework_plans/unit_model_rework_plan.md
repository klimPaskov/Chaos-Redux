# Chaos Redux Unit Model Rework Plan

Disposition: `accepted and queued` — the user approved the plan and its defaults on 2026-09-27 (“okay, go ahead”): ceilings of 70 (route A), 105 (route B), and 40 (route D) credits, Mummy Stagger first for the zombie walk, zombie-variant routes decided after free triage, and the autonomous robot first, then the base zombie. Models 1 and 2 are `implemented`; the rest remain queued in that order.

Scope from the user (2026-09-27): rebuild the Chaos Redux unit models from scratch one at a time, with Meshy body generation, one Meshy rig attempt and one set of suitable preset actions, Blender completion of any poor rig or action, separately generated equipped items, full HOI4 export and wiring, sourced synchronized sound, a unique counter, and multi-angle reimport QA of every action. The autonomous robot, portal raider, and alien infantry stay as they are, except that the autonomous robot receives shooting particles and deeper sound design. The trailer capture is paused until the models are ready.

Governing workflow: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` (Meshy 7 only, exactly one input image per geometry task, item-free bodies with separately generated items, no repeated paid rig or animation attempts, Blender completion without renewed approval, export and actual-byte reimport proof, parent-owned wiring, user-owned in-game validation).

## Credit basis

Live Meshy balance on 2026-09-27: **3,300 credits**.

| Operation | Credits |
|---|---|
| Image-to-3D, Meshy 7, textured PBR | 30 |
| Remesh (required for sources over 300k triangles) | 5 |
| Rig (humanoid-eligible bipeds only, includes walk and run) | 5 |
| Preset animation, per action | 3 |
| Retexture (keeps geometry, so an existing rig and actions carry over) | 10 |

Route estimates per model, before any recovery attempt:

| Route | Contents | Estimate |
|---|---|---|
| A. Unarmed biped | body 30 + remesh 5 + rig 5 + 6–8 preset actions (18–24) | **58–64** |
| B. Biped with one held item (firearm or melee) | route A + item geometry 30 + item remesh 5 | **93–99** |
| C. Biped with two held items | route B + 35 | **128–134** |
| D. Non-biped creature or quadruped | body 30 + remesh 5; rig and all actions authored in Blender | **35** |
| E. Retexture variant of an accepted body | retexture 10; rig and actions reused on identical geometry | **10** |
| F. Blender-only repair of an existing model | none | **0** |

Geometry recovery (a second body attempt) adds 30–35 when a candidate cannot be repaired in Blender. Rig and animation attempts are never repeated; failures go to Blender.

## Step 0 for every model: free triage

Before any credits, each existing model is imported from its shipped `.mesh`/`.anim` bytes, rendered from front, side, rear, and top in every action, and checked against the installed vanilla infantry calibration (source height 7.35, entity scale 0.8). The triage report lists holes, broken textures, outlines, deformation, missing props, aliased or static actions, missing particles, missing sounds, and counter status. The route (A–F) is fixed from that evidence, not assumed.

## Model inventory and proposed routes

Only lead-battalion units render as 3D map models; support-company sprites (CBRN companies, chemical tank support, Livens projectors, saboteur cell) never render as map models and are out of scope.

| # | Model | Consumers | Current state (observed) | Proposed route | Credits |
|---|---|---|---|---|---|
| 1 | **Autonomous robot** (polish only) | `autonomous_robot` | Implemented 2026-09-27: attack states loop, visible recoil in `attack`, `support_attack`, and `defend`, braced `defend` bursts with muzzle particles, smoke, light, and report, and layered CC0 heave, casing, venting, motor-death, blast, and debris sounds (job evidence `evidence/audio/polish_20260927/README.md`) | F | **0** |
| 2 | **Base zombie** | base `zombies` battalion (`chaosx_zombies_entity`) | Implemented 2026-09-27: training re-authored from boxing into zombie claw-and-feed choreography, attack and training grounded, death arms re-authored, mesh reduced to the 30k project norm, eight actions exported and reimport-proven, CC BY/CC0 voices and impacts wired (handoff `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/2026-09-27_base_zombie_rebuild_runtime.md`) | Blender completion of the existing lineage | **0** |
| 3–9 | Demonic, infected, mutant, necrotic, parasitic, rabid, undead zombies | 7 zombie types plus 3 armored variants | Separate meshes with 4 actions each; quality unreviewed | E where the design is a reskin of the base body, A where the silhouette differs (demonic, mutant, parasitic likely) | 70–450 |
| 10 | Clone infantry (and Aryan clone variant) | `clone_infantry`, `aryan_clone_infantry` | 9 actions; firearm unit | B, variant by E | 103–109 |
| 11 | Chaos assault battalion | `chaos_battalion` | 4 actions; firearm unit | B | 93–99 |
| 12 | Temporal guard | `temporal_guard` | 10 actions; weapon unit | B | 93–99 |
| 13 | Death ghost hosts | 3 ghost host types | 5 actions | A | 58–64 |
| 14 | Black Plague rat (shared) | 6 rat types | 8 actions; quadruped | D | 35 |
| 15 | Oth-Kesh cave brood | 5 brood types | 4 actions; creature | D | 35 |
| 16 | Paleogenetic creature | `paleogenetic_creature` | 11 actions; creature | D | 35 |
| 17 | Xenobiological assault organism | `xenobiological_assault_organism` | 10 actions; creature | D | 35 |
| 18 | Elephants (shared base) | `chaosx_elephant` | **Blocked without vanilla Elephantry DLC:** `sprite = elephantry`, no shipped `chaosx_elephant_entity` fallback. Live CXT QA 2026-10-03 19:15: every elephant division renders a placeholder box; 24 missing-entity errors. Parent commissions a real shared model (`accepted and queued`, orchestrator instruction 2026-10-03); 6 actions, quadruped. [Exact runtime evidence](../../events/012_africa/strange_forces.md#elephant-map-model-blocker). | D | 35 |
| 19–25 | Africa: forest giants, gorilla heavy infantry, oracle recon, pan sappers, riverborn, stone cohorts, plague carriers | 7 units | Meshes with 5 actions each | A, B, or D per anatomy (plague carriers and gorilla likely D) | 245–630 |
| 26 | Africa disaster wardens | `disaster_wardens` | No shipped mesh; axe-bearing | B | 93–99 |
| 27–33 | Cannibal bone guard, feast cohort, feast guard, island reavers, march predation column, scavenger warband, siege eaters | 7 units | Meshes present; melee items likely | B | 650–700 |
| 34–38 | Assassin cadre, master assassin, mechanized assassin, shadow company, silent guard | Event 039 units | Entity binding not resolved by the inventory scan; verify at triage | A or B | 290–500 |
| — | Portal raider, alien infantry | — | Kept as is by user decision | — | 0 |

**Whole-program estimate: roughly 2,200–3,000 credits** against the 3,300 balance, depending on how many zombie and Africa models qualify for the cheaper retexture or creature routes. Recovery attempts would come out of the remaining margin, so the order below front-loads the units that matter most for the trailer.

## First model: autonomous robot polish (0 credits)

1. Render every action from the shipped bytes and confirm the `robot_muzzle_l`/`robot_muzzle_r` locators exist in the exported mesh and sit on the barrels.
2. Decide per state whether the animation visibly fires: `defend` is a combat state in HOI4 and likely needs discharge events; `training` likely stays non-firing. Add discharge timing, muzzle particles, smoke, light, and sound for every firing state, synchronized to the rendered recoil frames.
3. Check the vanilla `mg_muzzle_particle` at the robot's scale; source or tune a heavier particle if it reads too small.
4. Deepen sound design from licensed sources: bullet impacts and ricochets, casing drops, per-action servo and hydraulic layers, footfall variations, hit reactions, and a distinct overheat or spin-down on attack end. Every file keeps its source URL, licence, and transformation record.
5. Verify the `autonomous_robot_select_sfx` binding reaches a real selection consumer; if HOI4 only routes selection by country tag (`<TAG>_infantry_idle`), record the exact constraint instead of claiming it.
6. Export, reimport, render every action, and hand off entity, particle, and sound wiring.

## Second model: base zombie (3–6 credits)

1. Finish the open 90k-triangle remesh topology review; repair holes and outlines in Blender.
2. Ingest the seven hash-verified Meshy clips onto the existing rig and review each for zombie-appropriate motion; rework in Blender where a boxing clip (punch, block, boxing practice) reads as human rather than undead.
3. Replace the rejected walk with one preset action: **Mummy Stagger** (id 113) first, **Limping Walk** (555–558) as the alternative. Up to two attempts: **3–6 credits**. The previously proposed CC0 Quaternius zombie walk remains an alternative that needs your approval.
4. Add **Zombie Scream** (id 386, 3 credits) only if you want it for `support_attack` or selection.
5. Bind textures, export, reimport, render all eight roles from multiple angles, and fix visible defects.
6. Restore the held-out `animation_chaosx_zombies.asset` (moved out of the mod during trailer capture because its `.anim` files did not yet exist) only once the matching `.anim` exports land.
7. Sound: extend the existing `sound/chaosx_zombies_sound.asset` roles with licensed sources for any missing role.

## Decisions needed from you

1. **Credit ceiling per model:** approve a default ceiling of 70 (route A), 105 (route B), and 40 (route D), with any excess brought back to you first.
2. **Zombie variants:** allow the retexture route (10 each) for variants whose silhouette matches the base zombie, or generate every variant from scratch (about 64 each)?
3. **Base zombie walk:** Meshy Mummy Stagger or Limping Walk (3 credits each), or the CC0 Quaternius zombie walk?
4. **Order after the zombie:** proposed next units are the ones the trailer shows most (clone infantry, chaos assault battalion, death ghost hosts, Black Plague rat, Oth-Kesh brood, Africa forces), then the remaining cannibal and assassin units.

## Open items carried from the trailer capture

- HOI4 crashed at 01:35:49 on 2026-09-27 while zoomed into a battle; the exception is an access violation in the renderer (crash dump retained under the trailer `capture_run/crash_0135`). The zoomed stack was a zombie division, so the zombie models are the first suspects and triage will cover them.
- Runtime error: `common/scripted_effects/002_zombie_outbreak_effects.txt:693` calls `add_to_faction` while the countries are at war.
