# Event 002 unit-model repair decisions

## WP3 execution on 2026-10-06

Acceptance basis: the user assigned every WP3 ticket in `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md`, authorized weak-design repairs, prohibited paid Meshy tasks and new audio downloads, and reserved live-game capture for the orchestrator.
These decisions apply to model presentation and source-derived sound delivery; gameplay and event choices are outside this work package.

- `implemented`: blood on each of the eight death states uses the installed vanilla burst emitter without `keep_particle`.
The installed emitter lasts 0.1 seconds; retaining it as a continuous effect is inappropriate for a single hit.
- `implemented`: undead attack grunt plays at 2.45 seconds and necrotic death impact at 3.30 seconds, as the respective WP3 tickets request.
Decoded necrotic death bytes put the hips at 4.10 source units at the superseded 1.30-second cue and 1.646 at 3.30 seconds.
Joint height does not prove deformed body contact, so final synchronization acceptance remains with stationary footage.
- `implemented`: shared zombie idle volume is 0.42, shared movement volume is 0.50, and parasitic feeding volume is 0.55, within the ticketed targets.
Shared idle retains its pool and random delay; all existing pools retain repetition prevention.
- `implemented`: movement takes 03–06 isolate complete recorded footsteps with bounded release fades rather than overlap adjacent contact events.
Takes 01–02 already fit the shortest interval; the six original-source identities and distinct takes are preserved.
Movement delay randomization is removed so an authored plant is not displaced by up to 80 milliseconds.
Playback-rate variation remains; the longest 0.17-second file lasts about 0.193 seconds at the slowest allowed rate, below the shortest 0.20-second contact gap.
- `implemented`: demonic scream and attack effects each use three variants, with the two extra screams and lower attack voice derived from the same already classified CC0 recordings.
Pitch variants are expressly allowed by the ticket; the source counts remain one scream recording and two attack recordings and are reported separately from variant counts.
The dedicated low-growl loop candidates fail the recorded-edge gate and stay outside runtime.
- `implemented`: undead support_attack starts the existing 2.369-second feeding recording once, at 1.50 seconds.
Its nominal playback spans both hands-to-mouth movements and ends at 3.869 seconds, near the 4.00-second grunt.
Removing the second start at 3.1333 seconds prevents two copies of the same feeding recording from overlapping on one unit while retaining the complete sourced cue.
The recovery grunt starts at 4.0333 seconds, one frame later, so the retained slowest feeding playback rate (0.94×) can finish near 4.020 seconds without touching the grunt.
- `implemented`: the mutant mesh removes four isolated spur triangles at the neck, shoulder and left toes, with their loose edge and orphan vertex records.
The accepted repair leaves every retained UV corner, weight, material and normal intact and preserves the exact 24-bone rest hierarchy, so it does not require replacing the other registered actions.
The installed positional topology has zero boundary, non-manifold, duplicate, degenerate or same-direction edges at all three required tolerances.
- `implemented`: the mutant idle uses a manually authored six-second breathing stance, head sweep/sniff and wrist flex on its existing rig.
This removes the large height jump at the cycle boundary while retaining visible creature motion; the filmed motion target remains unresolved.
- `implemented`: the mutant diffuse uses its immutable provider detail with an occupied median of 86.740, within the requested 80–95 interval, instead of the bright 156.610 preimage.
Its normal uses a source-detail 1.15× tangent-strength adjustment with unit-vector normalization after the untouched repack failed the normal gate.
The parent reviewed the exact two-map set on front and quarter surface previews before installation; the skin/jaw specular requirement remains open.
- `implemented`: the demonic current-mesh diffuse receives source-island dilation before a calibrated ten-percent skin/head darkening, and its normal is repacked from immutable provider detail.
The parent approved matching front and quarter rest-pose previews and installed only those two maps.
The grade remains tied to the original preimage and current UV/weight masks, so a later rig or UV change requires rebinding and re-QA rather than applying another darkening pass to the published texture.
The unchanged specular and all animated deformation requirements remain open.
- `implemented`: mutant attack uses two lower-register, formant-shifted derivatives of its already classified attack recordings.
The original contact onset and duration are retained, so the voice events keep their measured times.
- `implemented`: mutant movement and retreat use an own two-take footstep pool with a source-only bass/EQ treatment.
An EQ-only route preserves the accepted short onsets and 40 ms releases; longer raw-source and latency-shifted candidates were rejected for state timing.
The ±12% sound-rate variation changes sample duration without changing the animation plant gap, leaving 0.073518 seconds at the closest current plants.
- `unresolved`: WP3 requests footsteps at -3 dBFS while section 3.5 and the shared mastering gate require -6 dBFS.
Already accepted -6 dBFS samples remain in place; this preserves the actual mastering contract without claiming that the conflicting WP3 target passed.
- `unresolved`: model-specific undead/demonic specular instructions retain low or constant G values while section 3.2 rejects constant G.
Neither material identity nor acceptance thresholds may be inferred from a compression pass; source-derived region masks and an explicit material review remain required.
- `blocked`: no role or missing source is replaced by an unlabeled vocal, a synthetic sound, a programmatically generated rig/action, or a single-sample substitute for a requested multi-take pool.
Failed candidates remain outside runtime and the exact needs are retained in the package report and audio handoff.

Evidence: `docs/plans/unit_fix_2026-10/wp3_evidence/local_references.json` records local source revisions and line spans; `wp3_evidence/before/` and `wp3_evidence/after_entity_timing/` retain current consumers, decoded motion and the 64-state lint comparison.
The shared report requested as `unit_s3_report.md` is absent; `docs/plans/unit_fix_2026-10/pipeline_report.md` is the existing section 3 implementation report read for this task.

## Paced idle and defend voices

Disposition: implemented within the user-authorized WP3 sound-state repair; audible cadence and state-exit cleanup remain orchestrator checks.
Ten repeating idle/defend states previously triggered a one-shot voice once and then went silent.
Four dedicated ambient aliases retain their exact existing moan, rattle and gurgle families, gain, pitch variation and audible limits, with 4-8-second randomized pauses, loop playback and a short exit fade.
Existing attack, pain, selection and other timed one-shot effects keep their behavior; the legacy shared idle identifier remains available to the WP5 owner until its separate package removes that dependency.
This prevents silence without turning impact/grab cues into repeating loops or producing a continuous short-voice chatter.
No WAV, mesh or action bytes change, no recording or take is added, and the incomplete source/take requirements remain listed.
The 64-state source comparison clears all ten one-shot/silent-state findings and changes 39 findings to 29, retaining the 11 motion-offset, 15 contact-proof and three duration findings.
Evidence: `docs/plans/unit_fix_2026-10/wp3_evidence/idle_ambient_fix_20261006/parent_comparison.json`.
