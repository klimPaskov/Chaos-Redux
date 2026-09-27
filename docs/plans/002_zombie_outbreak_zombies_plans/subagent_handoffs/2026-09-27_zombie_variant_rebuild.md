# Zombie variant rebuild: demonic, infected, mutant, necrotic, parasitic, rabid, undead (2026-09-27)

Disposition: `implemented` — all seven variant models, actions, textures, entities, and voices are installed; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework on 2026-09-27 and instructed that generated models match the zombie type portraits, using renders of the current models as secondary inspiration (for example the demonic wings).

## Triage findings (shipped models)

Free triage with `.tools/3d_pipeline/review/review_cli.py triage` showed every variant unusable:

- only four actions each; `defend`, `support_attack`, `retreat`, and `training` were aliased to other actions;
- six variants shared one broken 24-bone rig: idle and move tilted the whole body backward with knees folding back, attacks crossed the legs, deaths splayed like a spider;
- the demonic mesh was 296 loose pieces that separated in attack and death;
- seam tears and flat grey texturing; no provider task ids were recorded, so the bodies could not be re-rigged.

## References

Each reference combines the type portrait `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_<type>.dds` (identity, face) with a lit render of the legacy model (silhouette, outfit, wings, growths), in `<job>/refs/original/meshy_input*.png` beside `refs/legacy_model/`.
Rabid and parasitic references were refused by the image model when the realistic female portrait was attached; both were produced from text descriptions of the portrait, and parasitic took a second edit pass to make the parasite dominant.

## Provider route and credits

Meshy 7 body, one rig, six presets, and two prime text-to-motion actions per variant, with unit-specific prompts and presets chosen so no two variants move alike.
Two preset choices were replaced after review because they cannot loop as their role: necrotic's seated "Dozing Elderly" idle (replaced by Long Breathe and Look Around) and parasitic's falling "Sliding Stumble" move and prone "Crawl Backward" retreat (replaced by Monster Walk and Injured Walk Backward).
Every task and its cost is in `docs/plans/system_unit_model_rework_plans/credit_ledger.json`; per-model spend averages about 83 credits against the 70-credit route A ceiling because both custom actions use the prime text-to-motion mode.

## Demonic wings

Meshy's humanoid rig fitted the elbows inside the wings, so the wing membranes followed the arms and wrapped over the head in the death.
In the live Lab session the wings were given their own spine-rooted two-bone chains (`WingL/R_Arm`, `WingL/R_Finger`) placed from the wing geometry; the 13,170 wing vertices were isolated by position, welded on a temporary duplicate, weighted with Blender heat weighting to the wing bones only, and mapped back by exact position.
Wing motion is authored per action as spread and forward-sweep angles carried through the spine pose: breathing in idle, pulses in move, a forward shield wrap in defend and retreat, flares in attack, support attack, and training, and a flat splay in death.
The arm chain keeps Meshy's rest pose so the provider arm motion stays valid.

## Export and runtime

Every variant was grounded with `lab_finalize` (4 mm contact on every frame), partitioned into four `char1.001` streams, exported, and reimport-proven for all eight roles with `export_package.py`, then installed hash-identical into `gfx/models/units/chaosx_<type>_zombies/` and registered with `wire_unit.py`.
Entities `gfx/entities/chaosx_<type>_zombies.asset` define eight distinct states; event times come from the phase review (`review_cli.py actions --humanoid`).
Voices come from `sound/chaosx_zombie_variant_sounds.asset` (one voice family per variant); see `docs/systems/3d_model_pipeline/chaosx_zombie_unit_sound_design.md`.

## Remaining limits

- No listening tool can confirm loudness balance in game.
- Grounding flattened the demonic leap and the mutant knockdown flip into grounded motions.
- Counter art for the variants was already unique and was not changed; the new bodies differ from the old models the counters were drawn from, so a counter refresh may be wanted.
