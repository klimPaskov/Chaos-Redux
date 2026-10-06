# Shared GFX tool audit

Status: implemented test coverage; audit notes delivered to the parent for integration and follow-up.

Date: 2026-10-06.

Scope: read-only audit of `.tools/gfx/gfx.py`; this handoff does not patch that tool.

The task-specific asset conversion contract is in `.agents/skills/chaos-redux-event-assets/SKILL.md`, section `DDS conversion` (lines 820–841). It requires the existing `write_bgra_dds` layout, the 128-byte legacy header, the pixel format at byte 76, exact payload length, intended alpha, and pixel-level validation.

Added `.tools/gfx/test_gfx.py` with thirteen tests for canonical DDS header and pixel round-trip, truncated payload and shifted pixel-format rejection, alpha erosion and chroma RGB replacement, empty/opaque input rejection, frame-local repair, alpha statistics, size and explicit margin checks, refusal to overwrite an input even with `--force`, JSON report path safety against input/list/planned-output collisions, mixed per-row manifest frame counts, a simulated competing writer during output installation, and installed vanilla division counter baselines.

Validation: `python .tools/gfx/test_gfx.py -v` passes all 13 tests on the current parent-edited tool. The installed references were `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` (152x42, two 76x42 frames) and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` (60x12, two 30x12 frames). Both exact reference files pass `counter_check` against themselves. Mixed manifests correctly audit a one-frame image and a two-frame strip in the same invocation. JSON output collisions with selected input, list file, and planned PNG output are refused. The simulated concurrent no-force output creator retains its bytes and causes this run to fail cleanly without leaving a scratch file.

The reference normal-frame subject-alpha means are 162.254 for the large vanilla infantry counter and 164.212 for the small map counter. Applying a literal `<200` ghost threshold in counter mode would classify the stock references as ghosted. The standalone alpha audit can retain the requested literal threshold; counter QA needs comparison to the supplied exact vanilla reference, as now implemented.

The parent fixed JSON collision checks and switched defringe PNG output to a round-trip-checked temporary file. Non-force installation now uses an exclusive hard link, which protects an output created by a competing worker after the early existence check; the new race simulation passes. The counter alternate-frame heuristic only counts a minimum number of white and black opaque pixels and cannot establish that they form a pale NATO field with a coherent black glyph.

The current profile defaults are focus 2px, decision 2px, and category 3px. The explicit test verifies a caller-supplied 3px decision margin. If the accepted repair requirement intended 3px as the default for all three surfaces, the profile table still needs that decision reflected in code and docs.

No vanilla strip required extraction or modification, and no game process was launched.
