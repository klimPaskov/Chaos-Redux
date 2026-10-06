# Event 012 unit model repair decisions

## WP1 review, 2026-10-06

Acceptance basis: the user's WP1 assignment and `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md`, common rules, WP1, and section 3.
This pass concerns the seven unit models and their sound/entity consumers; it does not change event gameplay or catalog wording.

- Implemented: plague carrier entity scale is `0.75`, as required by its ticket, to reduce the oversized donkey and cargo together without changing their proportions or authored geometry.
Actual installed-byte height and pose/contact review are recorded in the WP1 handoff and completion report; scale alone does not accept its rig, normal map, or actions.
- Implemented: the plague carrier attack state no longer plays the containment deployment hiss.
The deployment state retains that cue; a bray requires a suitable existing recorded source or remains an audio need.
- Implemented: death blood effects for gorilla heavy infantry, pan sappers, riverborn, and oracle recon use a finite burst without `keep_particle`.
The installed `blood_file` is a short emitter, and section 3.7 reserves persistence for continuous effects.
- Implemented: forest giant idle uses a dedicated looping soundeffect with `trigger_once` and one audible instance.
Two non-overlapping source-derived CC0 wood-creak beds form the loop pool; the former one-shot wrapper let the repeating idle state fall silent.
Attack and defend retain their existing one-shot wood sounds; this avoids restarting or looping those individual cues.
- Implemented: four recorded outdoor horse-hoof contacts supply plague carrier movement and retreat, matching the ticket's horse/donkey source allowance and fitting the existing plant-event gaps.
Indoor and stylized/cartoon variants were rejected; no pitch-only duplicate take was counted.
- Implemented: three Pan death takes combine different public-domain goat calls with the clean archived CC0 leonelmail body fall on dirt.
The named BigSoundBank source was unavailable and the existing remaxim/qubodup original was clipped; this source selection retains the exact physical role within the user-authorized archived-source pool.
The relative body timing preserves the old landing beat, and the old landing hoof cue is removed to avoid a second, wrong impact.
- Implemented: three recorded stone-grind takes supply stone cohort recovery and settling.
They do not substitute for the missing rockslide death or stone-and-iron thrust recordings.
- Accepted and queued: plague move frame 21 has a whole-mesh minimum `0.03410357` units above ground at scale `0.75`, exceeding the planted-frame `0.01` tolerance.
Current-hash idle/move reimport receipts establish those bounds; the older per-hoof report is stale for the current move hash, and per-part cargo clearance remains unmeasured.
- Accepted and queued: use the installed shader's normal packing when the plague normal is rebaked.
`standardfuncsgfx.fxh` decodes tangent X from G and tangent Y from negative A; the ticket's X-in-A/Y-in-G wording conflicts with that actual consumer.
No normal map was changed by this pass.
- Blocked: no rig, skin weight, action, attachment-performance, or grounded-motion repair may be synthesized by repository code when an exclusive live Blender authoring session is unavailable.
Initial TCP and direct-read probes failed at `localhost:9877`; a later read-only probe succeeded and verified Blender 5.2.2 build `d13f752e3b9c` and add-on 1.0.3.
The session subsequently loaded the other work package's `mutant_zombies/.../21d_export_batches.blend` checkpoint, while the WP1 background inspection waited on the serialized worker lock.
WP1 must not replace or mutate that other package's session; exclusive availability was requested from the orchestrator.
The exposed client has fewer tools than the lock's full server inventory, but that count alone does not prove an incompatible schema.
- Accepted and queued: all remaining authored WP1 pose, loop, stride, prop/contact, topology, material-mask, and normal-detail repairs remain required.
Queue reason: authoring capability and source evidence must satisfy the pipeline before any replacement is installed.
The item-specific dispositions and numerical findings belong to `docs/plans/unit_fix_2026-10/wp1_africa_report.md` and its linked worker handoffs.
- Blocked audio sources stay at their existing runtime cues when no licensed, semantically suitable archived recording can be verified.
No Internet file was downloaded and no sound was synthesized.

The missing requested `unit_s3_report.md` is a documentation route gap.
The current shared delivery report is `docs/plans/unit_fix_2026-10/pipeline_report.md`, with `geometry_animation_tools_handoff.md`, `texture_tools_handoff.md`, and `audio_tools_handoff.md` as section-specific handoffs.
