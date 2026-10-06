# Shared GFX tool audit

Status: implemented test coverage; audit notes delivered to the parent for integration and follow-up.

Date: 2026-10-06.

Scope: read-only audit of `.tools/gfx/gfx.py`; this handoff does not patch that tool.

The task-specific asset conversion contract is in `.agents/skills/chaos-redux-event-assets/SKILL.md`, section `DDS conversion` (lines 820–841). It requires the existing `write_bgra_dds` layout, the 128-byte legacy header, the pixel format at byte 76, exact payload length, intended alpha, and pixel-level validation.

Added `.tools/gfx/test_gfx.py` with eighteen tests for canonical DDS header and pixel round-trip, truncated payload and shifted pixel-format rejection, alpha erosion and chroma RGB replacement, vivid green opaque-core preservation with boundary despill, explicit spill-mask handling of selected versus adjacent legitimate green, wrong-sized spill-mask rejection, partial-alpha core RGB preservation, empty/opaque input rejection, frame-local repair, alpha statistics, size and explicit margin checks, refusal to overwrite an input even with `--force`, JSON report path safety against input/list/planned-output/spill-mask collisions, mixed per-row manifest frame counts, a simulated competing writer during output installation, and installed vanilla division counter baselines.

Validation: `python .tools/gfx/test_gfx.py -v` passes all 18 tests on the current parent-edited tool. The installed references were `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` (152x42, two 76x42 frames) and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` (60x12, two 30x12 frames). Both exact reference files pass `counter_check` against themselves. Mixed manifests correctly audit a one-frame image and a two-frame strip in the same invocation. JSON output collisions with selected input, list file, planned PNG output, and explicit spill mask are refused. The simulated concurrent no-force output creator retains its bytes and causes this run to fail cleanly without leaving a scratch file. A vivid green patch deep inside the opaque silhouette keeps its RGB and alpha; an opaque green pixel on the outer boundary is erased and receives interior RGB. An explicit one-pixel internal mask recolours only the selected spill pixel, leaves adjacent legitimate green unchanged, and produces the same alpha channel as the default erosion. Wrong-shaped masks fail closed.

The reference normal-frame subject-alpha means are 162.254 for the large vanilla infantry counter and 164.212 for the small map counter. Applying a literal `<200` ghost threshold in counter mode would classify the stock references as ghosted. The standalone alpha audit can retain the requested literal threshold; counter QA needs comparison to the supplied exact vanilla reference, as now implemented.

The parent fixed JSON collision checks and switched defringe PNG output to a round-trip-checked temporary file. Non-force installation now uses an exclusive hard link, which protects an output created by a competing worker after the early existence check; the race simulation passes. The updated defringe behavior preserves RGB in surviving core pixels with alpha 240–254, but one-pixel minimum-filter erosion may reduce those pixels' alpha when a neighbor is less opaque; the test confirms this distinction. Explicit spill masks give a reviewed way to select known opaque internal key-colour spill without globally recolouring vivid green artwork. Mask geometry must match the processed frame exactly. The README's core-colour claim is supported for RGB, but should not be read as a promise that every semitransparent core pixel's alpha byte is unchanged by erosion. The counter alternate-frame heuristic compares pale/black structure and coherent-field density, area and aspect to the reference; it cannot establish a complete border or the correct glyph semantics.

The current profile defaults are focus 2px, decision 2px, and category 3px. The explicit test verifies a caller-supplied 3px decision margin. If the accepted repair requirement intended 3px as the default for all three surfaces, the profile table still needs that decision reflected in code and docs.

No vanilla strip required extraction or modification, and no game process was launched.

The independent audit covers 18 tests.
Parent follow-up coverage adds counter-CLI two-frame defaults, stock large/small margin acceptance and rejection of white/black speckles without a coherent NATO field, for 20 passing tests in the final suite.
The small counter profile uses a zero top/bottom margin consistent with the inspected stock field.
