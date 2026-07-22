# Real-person leader finish trials — 2026-07-22

This workspace tests the leader-only deterministic processor at
`.agents/skills/chaos-redux-event-assets/tools/leader_portrait_finish.py`.
It does not replace or modify the frozen advisor processor.

Every candidate in this folder:

- starts from the retained attributed archival master;
- uses one explicit crop and a fixed `156x210` Lanczos fit;
- derives the face and subject only from source pixels;
- records every semantic mask, colour ramp, smoothing control, brush-field
  control, and identity threshold in its JSON configuration and metadata;
- has status `candidate_requires_visual_approval`;
- is not approved for DDS conversion or runtime wiring.

The review sheets show the archival crop, candidate, protected Chaos Redux
targets, and canonical skill-local vanilla leaders at native size and at 4x
nearest-neighbour scale. The mask sheets expose the manual subject, face, and
palette-region boundaries used in each run.

## Outcome

Rejected. The deterministic treatment preserves facial structure and adds a
muted period palette, but it does not escape the appearance of colourized
archival photography. The Harpe trial also has visible semantic-mask seams at
the face, cap, neck, and collar. Neither candidate is suitable for DDS
conversion or runtime wiring.

The adjacent processor is experimental evidence only. It is not a production
workflow, must not be referenced from `SKILL.md`, and should be omitted from a
final production merge unless the repository intentionally retains failed
experiments. The configs, metadata, review sheets, and blocker handoff are the
durable evidence of the tested deterministic ceiling.

This rejection authorizes no DDS conversion, runtime wiring, or skill/workflow
recommendation.
