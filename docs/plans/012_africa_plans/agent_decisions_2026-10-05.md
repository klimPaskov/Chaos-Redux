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

## Takeover reporting, 2026-10-06

Disposition: `implemented`, with native shipment movement remaining an orchestrator live check.
Acceptance basis: the current user assignment to finish 012, G2 requiring a low popup count within each chain, and G7 requiring feedback for a forced launch that cannot apply.
A three-instalment continuing-support agreement previously sent `.604` after every shipment.
The two intermediate shipments update the mission, material contribution, history and unpaid balance without a report.
The agreement sends one closure report, showing all material paid and what remains owed, and a failed agreement may also send one punishment report.
An empty intermediate shipment keeps its retry gate and mission without repeatedly opening a report.
The transient suppression flag covers every automatic instalment attempt, including a short final fuel shipment, and is cleared before the attempt returns.
The support-summary flag is reset on each capture, empty shipment and report cleanup.
A partially stored fuel shipment cannot count as a complete instalment: the remaining count is rounded up from the real balance.
Its next attempt moves into the future and its deadline gains one interval, matching the accepted full-tank deferral, so Africa's storage shortage cannot create a participant breach.
Manual Africa preflight selects a valid African host as before and reports its most specific rejection through the existing guarded `chaosx_report_forced_event_failure` helper.
The change stays in the event owner and preserves Settings batch aggregation.
The evidence file is `takeover_reporting_evidence_2026-10-06.json` beside this document.

## Takeover autonomy-art decision, 2026-10-06

Disposition: `accepted and queued` until the asset handoff is installed and reviewed.
Acceptance basis: the assigned 012 GFX fix table and G5 covering every visible defect.
The table incorrectly describes the two autonomy sprites as dead.
`common/autonomous_states/012_africa_autonomy.txt` defines both autonomy states, and their live relationship consumers use native implicit autonomy sprite lookup.
They keep their current sprite IDs and receive separate 35x35 autonomy artwork instead of focus textures or deletion.
The unused division-template emblem sprites are a separate family and require their own consumer check.
