# Event 006 current-authority stale-heading cleanup

Date: 2026-08-14.

## Scope

This documentation-only cleanup removes current-sounding labels from dated Event 006 authority sections after the IW-045 adapter-only dispatch update.

## Changed files

- `docs/events/006_independence_wave/overview.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

## Changes

- The overview's dated continuation now points to the current `32/29/161/40` authority at the top instead of the superseded `31/28/162/39` wording.
- The 2026-08-09 headings in the source map and resume packet are explicitly labeled historical snapshots superseded by the post-IW-045 block above.
- The dated portrait-shelf heading in the source map and the 2026-08-10 package-manifest heading now identify their older shelf/count and promotion wording as historical rather than current authority.
- No historical arithmetic or dated evidence was deleted.

## Validation

Targeted searches confirm the old 2026-08-09 headings are historical and the overview continuation uses `32/29/161/40`. `git diff --check` reports no substantive whitespace errors on the three touched documents.

No gameplay, localisation, asset, workbook, central attestation, allocator, or Join files were changed. Event 006 remains **HOLD / PARTIAL**; this cleanup does not promote any package or claim live runtime, save/load, or quantitative balance evidence.
