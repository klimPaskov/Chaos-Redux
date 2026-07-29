# Event 014 Documentation Consolidation Reaudit

Date: 2026-07-15

## Scope

This documentation-only reconciliation reviewed the twelve source-spec parts, current matrices, package status and validation pages, canonical Event 014 document, asset authority, accepted improvement addenda, triggerable-scenario documentation, current audit set, and package manifest against the final consolidated runtime. It did not alter gameplay, localisation, GFX, images, audio, flags, or the catalog workbook.

The curation used the current focus, decision/mission, country-package, localisation/asset, spreadsheet, and improvement-loop consolidation reaudit reports as evidence. Older Event 014 reports and handoffs remain historical records; the current authority points to the consolidation reports instead of treating those checkpoints as live package counts.

## Verdict

| Severity | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

No current source specification, matrix, status page, canonical event document, or root asset handoff contradicts the implemented package. No accepted addendum remains only in a plan, and no documentation blocker, fallback, or unresolved simplification remains.

## Reconciled authority

- Event 014 remains Minor Fire-Once and outside every cluster.
- The baseline is separate from exactly three evolutions, with Evolution III and both terminal rows withheld from player-facing presentation until `cannibalism_reveal_complete`.
- Exactly three origins remain: Island Host, Siege Commune, and March Host.
- The focus counts are 68 warlord, 108 unified, and 28 Wendigo, for 204 total.
- Eight origin-agnostic reusable warlord slots remain live.
- The dedicated merge-safe Event 014 script, GUI, and localisation loader surface is consolidated from 93 files to 23. The 23-file count is the practical one-file-per-incompatible-loader-schema boundary. Per-tag country history files, engine-required flag ladders, binaries, and shared global registries remain structurally separate and are not falsely counted as mergeable loaders.
- Exactly one dedicated Event 014 GFX registry remains. Together with `interface/chaosx_pictures.gfx` and `interface/chaosx_super_events.gfx`, three GFX files contain 812 Event 014 texture references to 598 unique existing runtime paths with 598 unique hashes.
- The flag authority records 65 separate built-in ImageGen masters and 195 unique runtime TGA files in the exact normal, medium, and small ladders.
- The warlord authority records 56 unique 156x210 HOI4-style portraits, each with a distinct face, silhouette, prop, and macabre action and no prison-origin presentation.
- The live static bindings use `gfx/leaders/014_cannibalism/hannibal.dds` and `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` directly. Redundant copied static DDS files are absent.
- The ordinary and transformed Hannibal sheets contain 12 and 16 genuine semantic frames, play at 12 FPS, and use `gfx/FX/buttonstate_blendframes.lua`. Across all 14 animation packages, 142 source frames and 142 processed frames satisfy the real-frame contract.
- Four action-led super-event images and four unique documented 44.1 kHz audio cues remain wired to IDs 49, 50, 52, and 53.
- Eighteen achievements, five SCN-010 types, two independent terminal rows, shared world threat, event-log actor mapping, staged Event Details, and exact Chaos-above-1000 terminal gates remain represented consistently.
- Both accepted improvement addenda are promoted and closed. Optional ideas explicitly left unaccepted remain suggestions rather than missing implementation.

## Secrecy and retired-origin review

Current player-facing authority does not expose the public leader identity before the reveal flag. The baseline, Evolution I, Evolution II, decisions, focuses, GUI, Event Details, achievement tracker, scenario descriptions, reports, portraits, terminal rows, and audio presentation remain neutral until their reveal-gated surfaces become eligible.

Current source specifications and asset authority do not present a fourth origin. Historical plan and handoff references are retained only where they document superseded production or removal work. No current authority makes a living Indigenous sacred-authenticity claim or uses a borrowed sacred motif.

## Files reconciled

- `docs/events/014_cannibalism/overview.md`
- `docs/assets/014_cannibalism/manifest.md`
- `docs/assets/014_cannibalism/gfx_handoff.md`
- `docs/specs/014_cannibalism_specs/README.md`
- `docs/specs/014_cannibalism_specs/PACKAGE_MANIFEST.md`
- `docs/specs/014_cannibalism_specs/matrices/asset_inventory_matrix.md`
- `docs/specs/014_cannibalism_specs/prompts/cannibalism_asset_prompt.md`
- `docs/specs/014_cannibalism_specs/quality/package_status.md`
- `docs/specs/014_cannibalism_specs/quality/package_validation.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_7_hannibal_reveal_and_unification.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_10_assets_animation_and_localisation.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md`

The localisation/asset and improvement-loop audit owners separately corrected their older same-day audit prose to 12 FPS and marked the prior final-completion checkpoint superseded. Those historical-audit corrections are part of the current evidence set, not gameplay edits.

## Package-manifest proof

`docs/specs/014_cannibalism_specs/PACKAGE_MANIFEST.md` was regenerated last from the final package bytes. It lists all 43 package files other than itself. A second independent parser verified:

- 43 manifest rows for 43 files;
- zero missing rows;
- zero extra rows;
- exact byte counts;
- exact LF-byte-plus-one line counts; and
- exact SHA-256 hashes for every row.

## Meaningful validation

- Rechecked current authority for stale nine-GFX, 6 FPS, copied-static, 24-file, four-origin, 72-focus, 208-focus, 39-decision, and missing-asset claims; none remains.
- Reconciled the exact canonical portrait paths and the one-dedicated-plus-two-shared GFX boundary.
- Verified the current audit links point to the consolidation reports with P0/P1/P2/P3 all zero.
- Verified the source package distinguishes internal documentation from reveal-gated player presentation.
- Verified the 93-to-23 count is scoped to merge-safe loader files and does not pretend that engine-required history, flag, binary, or shared-registry files can be combined.

## Simplifications, omissions, fallbacks, and blockers

None. No current documentation surface, manifest row, accepted-addendum disposition, asset authority, catalog status, or source-of-truth link remains unresolved.
