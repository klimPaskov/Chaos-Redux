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
Existing sample pools, random delays and repetition prevention remain intact.
- `unresolved`: WP3 requests footsteps at -3 dBFS while section 3.5 and the shared mastering gate require -6 dBFS.
Already accepted -6 dBFS samples remain in place; this preserves the actual mastering contract without claiming that the conflicting WP3 target passed.
- `unresolved`: model-specific undead/demonic specular instructions retain low or constant G values while section 3.2 rejects constant G.
Neither material identity nor acceptance thresholds may be inferred from a compression pass; source-derived region masks and an explicit material review remain required.
- `blocked`: no role or missing source is replaced by an unlabeled vocal, a synthetic sound, a programmatically generated rig/action, or a single-sample substitute for a requested multi-take pool.
Failed candidates remain outside runtime and the exact needs are retained in the package report and audio handoff.

Evidence: `docs/plans/unit_fix_2026-10/wp3_evidence/local_references.json` records local source revisions and line spans; `wp3_evidence/before/` and `wp3_evidence/after_entity_timing/` retain current consumers, decoded motion and the 64-state lint comparison.
The shared report requested as `unit_s3_report.md` is absent; `docs/plans/unit_fix_2026-10/pipeline_report.md` is the existing section 3 implementation report read for this task.
