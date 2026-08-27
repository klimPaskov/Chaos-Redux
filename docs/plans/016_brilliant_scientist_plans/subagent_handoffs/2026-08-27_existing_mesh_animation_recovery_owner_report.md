# Event 016 existing-mesh animation recovery owner report — 2026-08-27

## Scope and disposition

This tranche reused the existing Event 016 meshes only. No new base model, ImageGen reference, image-to-3D task, local rig, manual weapon attachment, manual weighting, transform-only motion, or simple semantic animation fallback was created. The user instructed that live in-game validation is out of scope for this pass; structural, provider, Blender, export/reimport, audio, and counter evidence was still reviewed where available.

The package-wide result is **blocked**. No package was promoted as a complete runtime model because every firing or articulated-family consumer must pass the Meshy-authored action, deformation, effect/locator, sourced-audio, counter, export/reimport, and parent-wiring gates together. Existing runtime files were not expanded with blocked models or guessed entity bindings.

## Package crosswalk

| Family | Existing-mesh result | Runtime disposition |
| --- | --- | --- |
| Portal Raider | Meshy actions `104 Side_Shot` and `98 Run_and_Shoot` succeeded after a six-credit recovery spend, but the locked Blender adapter mapped `portal_raider` to a legacy shared root and could not perform the required deformation review. The firearm action therefore remains unaccepted. | No entity, `.mesh`, `.anim`, sound, or template override was wired. Counter and sourced-audio evidence remain preserved for a later accepted package. |
| Clone Infantry | The rifle is fused upright on the back while Meshy attack/support actions animate empty hands. A weaponless recovery would violate the preserve-firearm requirement, so attack, support attack, and training remain blocked. | Existing static entity is not promoted as a complete firearm package; no new template override, muzzle event, or firing sound was added. Generic counter evidence is ready for a later parent-reviewed package. |
| Autonomous Robot | Idle, move, training, and articulated death remain usable candidates, but attack, defend, support attack, and retreat do not prove coherent arm-mounted-gun aim/discharge/recoil/recovery, and no muzzle locator or discharge particle/light binding is certifiable. | Existing entity/GFX files remain unchanged and no complete robot firing consumer was claimed. Sourced audio and bespoke counter evidence remain preserved. |
| Paleogenetic Creature | Existing 30,000-triangle geometry and segmentation pass, but the returned 24-bone humanoid rig cannot articulate the four-arm/two-head anatomy. All required creature actions are blocked. | No runtime entity, model, animation, sound, or counter registration was added. |
| Xenobiological Assault Organism | Existing six-limb geometry is retained, but the returned 24-bone humanoid rig lacks dedicated chains for the elevated claws and has no substantive action lineage. | No runtime entity, model, animation, sound, or counter registration was added. |
| Alien Infantry | The seven V13 Meshy actions remain distinct and the model/material/audio/counter evidence is preserved. The rig has no supported muzzle/effect locator, so positional firing particles/lights and strict sound synchronization remain unresolved. The historical rig is no longer retrievable from Meshy, and no provider-authored training action could be recovered. | Removed the unsupported `training -> idle` and `wounded -> defend` aliases from `gfx/entities/alien_infantry.asset` and `gfx/entities/alien_infantry.gfx`. The landing API remains bound to the seven real actions only; particle/light definitions remain documented but unbound rather than invented at a guessed node. |
| Temporal Guard | Meshy 7 model, eight provider-authored actions, grounded export/reimport, relinked 1024 PDX DDS materials, and sourced audio pass their available checks. Dedicated `support_attack` and `retreat` actions, bespoke counters, complete source/credit provenance, and parent runtime wiring remain absent. | No runtime entity/GFX binding was added and no action was aliased to fill the missing roles. |
| Aryan Clone Infantry | This is intentionally a visual derivative of installed German infantry entities, not a missing custom model package. | Keep the vanilla German entity alias; it does not require a new 3D model. |

## Provider and budget evidence

- The live Meshy balance was 13 credits at the start of recovery and is 7 credits after the two Portal Raider action attempts; no further paid operation is authorized by the remaining balance in this tranche.
- Portal Raider tasks `01a04356-7d07-7d97-be58-87d36e8e33ac` and `01a04357-9629-7dda-8e2d-c548c34233df` were downloaded and checksummed, but neither passed the locked adapter review.
- The Alien training-action probe against rig `01a03dcf-f0ba-7b67-b769-5a2678b03a40` returned `Resource not found` before task creation and consumed no credits.
- No new geometry, remesh, rig, ImageGen, or image-to-3D call was made for Clone, Robot, Paleogenetic, Xenobiological, Temporal, or Alien during this recovery pass.

## Audio and counter disposition

Sourced audio provenance and PCM/container checks were reverified where packages supplied them. No synthesized or unrelated firearm recording was promoted, no impact recording was invented, and no sound was bound to a firing state whose action or locator gate failed. Portal, Clone, Robot, Alien, and Temporal packages retain counter evidence or parent-ready counter handoffs; Paleogenetic and Xenobiological bespoke counter production remains blocked. No generic or copied counter was substituted for a missing bespoke package.

## Parent wiring boundary

The parent-owned runtime boundary is intentionally unchanged for blocked families: no new `gfx/entities`, `gfx/models/units`, `.gfx`, sound-definition, or `override_model` reference was added for Portal, Clone, Robot, Paleogenetic, Xenobiological, or Temporal. Alien keeps its existing `alien_infantry_entity` API template binding, but its unsupported aliases were removed and its unresolved locator/effect state remains explicit. This prevents a model that has not passed its action and effect gates from being silently presented as complete.

## Unblock conditions

Portal and Clone require a provider result whose weapon is retained in the hands through every firing phase and whose locked adapter can inspect the result. Robot and Alien require a certifiable provider/adapter muzzle locator plus synchronized particles, light, and sourced discharge/impact audio. Paleogenetic and Xenobiological require dedicated anatomy-compatible Meshy rigs and actions. Temporal requires dedicated provider `support_attack` and `retreat` actions, approved bespoke counters, complete provenance, and parent-owned runtime synchronization.

No fallback, omission, or simplification was hidden. The Event 016 goal remains blocked until accepted provider packages and their parent runtime wiring are available.
