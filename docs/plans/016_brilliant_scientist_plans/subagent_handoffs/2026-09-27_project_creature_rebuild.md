# Paleogenetic creature and xenobiological assault organism rebuild (2026-09-27)

Disposition: `implemented` — both creature models, eight standard actions each, extra-appendage rigs, textures, mesh registrations, and timed entities are installed; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework on 2026-09-27 and asked that every remaining model be finished thoroughly, using renders of the current models as references.

## Why they were replaced

A triage with the fixed review tool showed both shipped creatures nearly static: the xenobiological organism's move, crawl, leap, and retreat held one upright pose, and the paleogenetic creature barely moved outside its death.
Both also carried non-standard states (`crawl`, `leap`, `wounded`, `stalk`, `charge`, `roar`) that the engine never enters, and neither had any sound.

## Route

References in `docs/assets/chaos_redux_3d_model_pilots/models_3d/<job>/refs/original/meshy_input_v3.png` keep the legacy designs (a four-armed beaked insectoid; a screaming host fused to a one-eyed growth with six tentacles), posed so every limb is separated for rigging.
Each unit: Meshy 7 body, one rig, six presets, and two prime text-to-motion actions; the xeno organism's first training preset (Jump and Slam Back Down) flipped the creature upside down in a loop and was replaced by Crouch Look Around (preset 258).
Credits are in `docs/plans/system_unit_model_rework_plans/credit_ledger.json`.

## Extra appendages

Meshy's humanoid rig drove the xeno organism's lower arm pair and one tentacle per side of the paleogenetic creature; the rest were weighted to the hips or smeared across the spine.
`lab_limbs.py` gave the xeno organism's scythe arms (`UpperArmL/R_1-3`) and four tentacles of the paleogenetic creature (`TentFrontL/R_1-4`, `TentOuterL/R_1-4`) their own heat-weighted chains on joints measured with its survey (components after cutting the torso core away).
The tentacle roots are feathered into the provider weights so they do not tear.
Every role is keyed by authored angles (scythes held ready, stabbing on the attack beats, folding into a guard; tentacles writhing, trailing, lashing twice, reaching and wrapping, flailing in the death), with the right side half a cycle off the left on looping roles; the measured floor pass re-keyed the paleogenetic creature's death so the splayed tentacles rest on the ground.

## Runtime

`gfx/models/units/xenobiological_assault_organism/` and `gfx/models/units/paleogenetic_creature/` hold the new meshes (four streams each), eight `.anim` files, and maps; the entities keep `xenobiological_assault_organism_entity` and `paleogenetic_creature_entity` as clones for the sprites.
All eight actions are grounded and reimport-proven.

## Remaining limits

- Neither creature has dedicated sourced audio: the xeno organism uses the Black Plague rat's licensed chitters, bites, and screeches, and the paleogenetic creature uses licensed zombie roars, gurgles, grabs, and footsteps. Dedicated insect and flesh-creature sounds need a sourcing pass, which downloads files and needs the user's approval.
- The paleogenetic creature's outer tentacle shares its shoulder with the provider-rigged middle tentacle; the seam is feathered, not modelled apart.
- Counter art was not changed.
