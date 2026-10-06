# Event 001 report-image repair

## Accepted result

The Event 001 report-image findings are resolved. The current runtime DDS files for the prior 15-scene package match the reviewed package byte-for-byte, and all 15 package records report pixel-exact DDS round trips. The remaining two textures, communist_state_control and communist_insurgency_start, previously shared one Lenin/Stalin slogan poster and now use distinct, text-free fictional period scenes at the existing runtime paths and sprite names.

The parent visually reviewed the 17-card final contact sheet and the two-card before/after sheet and accepted both new scenes on 2026-10-06. The acceptance basis is the user's current authorized graphics scope plus the parent's visual review on that date.

## Requirement crosswalk

| Finding | Prior issue | Resolution and subject review | Evidence |
| --- | --- | --- | --- |
| GFX_report_event_communist_worker_ritual | Reused street march did not depict a worker ritual. | The package scene shows workers around a floor ring of machine oil, chalk, a gear, and bolts; it is distinct from the machinery-press night gathering in dark_worker_rituals. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_dark_worker_rituals | Reused street march did not depict dark rituals. | The package scene shows a night gathering beneath a factory press and remains visibly different from the raised-view floor ring in worker_ritual. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_control_escalates | Pixel-identical to the emergency intervention march. | The package scene makes the timber factory-gate barricade the dominant subject. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_intervention_backfire | Reused the street-march photo. | The package scene shows opposing worker and police lines at an industrial street barricade and communicates a failed intervention without graphic violence. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_war_warning | Reused the street-march photo. | The package scene shows organized workers packing rifles and ammunition, distinct from the hidden cache and barricade scenes. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_uprising | Reused the street-march photo. | The package scene shows an anonymous organized militia assembly from behind in an industrial field. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_unstable_activity | Reused the street-march photo. | The package scene shows a concealed rifle cache beneath warehouse flooring, separate from the visible weapons packing in war_warning. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_surprise_revolt | Reused the street-march photo. | The package scene shows militia movement from a factory-street barricade, distinct from the organized field assembly in uprising. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_state_control | Reused the Lenin/Stalin poster. | Replaced with an interior municipal checkpoint scene: a sentry at a desk controls a guarded entrance while distant civilians wait. | evidence/001/001_communism_spread_before_after.png; evidence/001/001_dds_validation.json |
| GFX_report_event_communist_world_revolution_whispers | Reused the Lenin/Stalin poster. | The package scene shows a quiet machine shop with folded red cloth and a dark corridor, separate from the larger empty hall in foreshadowing. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_world_revolution_foreshadowing | Reused the Lenin/Stalin poster. | The package scene shows an empty factory hall with a plain hanging cloth and its shadow; no person is portrayed. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_emergency_success | Reused intervention_success and had a 209x176 size. | The package scene shows a cleared factory rail platform held by a tired garrison, and its processed canvas is exactly 210x176. | docs/assets/001_communism_spread/report_qa_20261005/manifest.md; evidence/001/001_communism_spread_final.png |
| GFX_report_event_communist_insurgency_start | A historical poster contained readable Russian text and shared the Lenin/Stalin poster. | Replaced with a bridge-led movement scene showing a small worker-militia file crossing toward an industrial city. The bridge silhouette distinguishes it from the field assembly and barricade cards. | evidence/001/001_communism_spread_before_after.png; evidence/001/001_dds_validation.json |

## New asset production and QA

The two new sources were generated with built-in image_gen as fictional staged documentary scenes because the alternate-history event does not require a specific real person, archive object, or verifiable historical action. No real-person likeness was used. Candidate v1 for insurgency_start was rejected after the contact sheet showed too much visual similarity to uprising; its source, processed preview, and DDS remain in the active package, and candidate v2 uses the railway bridge composition.

Both selected source PNGs are 1536x1024 RGB images. The repository report-card processor produced 210x176 RGBA previews with grayscale-to-sepia treatment, subtle tilt, a thin paper edge, soft shadow, and transparent corners. The repository-standard converter produced one-level uncompressed 32-bit BGRA DDS textures, and the decoded runtime DDS pixels match the selected processed PNGs exactly. The per-asset prompt, source and output hashes, original runtime hashes, header checks, corner-alpha checks, and pixel-exact comparisons are recorded in evidence/001/001_prompts.md and evidence/001/001_dds_validation.json.

## Runtime handoff

| Sprite | Runtime DDS | Target .gfx | Status |
| --- | --- | --- | --- |
| GFX_report_event_communist_state_control | gfx/event_pictures/001_communism_spread/communist_state_control.dds | interface/001_communism_spread.gfx | Complete; existing filename and sprite preserved. |
| GFX_report_event_communist_insurgency_start | gfx/event_pictures/001_communism_spread/communist_insurgency_start.dds | interface/001_communism_spread.gfx | Complete; existing filename and sprite preserved. |

The current hashes for the other fifteen package DDS files match the reviewed package hashes in evidence/001/package_runtime_audit.json. Their existing GFX handoff and source lineage remain in docs/assets/001_communism_spread/report_qa_20261005/.

The two selected original generated sources are also retained permanently under `evidence/001/source/`.
There are no omitted findings or substituted asset families in this group.
No gameplay, weights, event text, or popup dispatch was changed.

Orchestrator live check: in a paused 1936 USA session, use the Event 001 chain to display Insurgency Start and State Control, then its worker-ritual, dark-ritual, emergency-success, and world-revolution reports.
Each report should show its own sepia tilted photograph at 210x176, without a Russian slogan strip or repeated march/poster picture.
For a picture-only fixture, the event-detail/report consumer may be used without completing the gameplay chain.

Skills used: event-assets, imagegen, subagents, shared-git-commit.
