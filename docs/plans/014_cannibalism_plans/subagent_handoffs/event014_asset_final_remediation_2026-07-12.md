# Event 014 Asset Final Remediation Handoff

Implementation date: 2026-07-13
Finding source: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_asset_final_reaudit_2026-07-12.md`
Mode: asset and asset-documentation remediation only; no gameplay, localisation, GFX registry, or GUI script was edited
Final verdict: **COMPLETION-READY**

## Findings closed

| Original severity | Finding | Remediation | Recheck |
| --- | --- | --- | --- |
| P1 | Eighteen not-eligible achievement variants used brightness reduction and a locally drawn X. | Replaced the treatment with an exact grey-image copy plus the mandated 64x64 RGBA overlay alpha-composited on top; regenerated the package and runtime outputs. | Closed. |
| P2 | Six retired animation experiments claimed 12 absent DDS outputs were complete. | Rewrote the old manifest as a historical source/provenance ledger and pointed to the accepted 14-animation package. | Closed. |
| P2 | Top/generated-art manifests claimed absent or superseded council, leader, old super-event, report, flag-alternative, achievement-package, and registry ownership. | Reconciled current owners and converted the generated-art document to source/processed provenance without absent runtime claims. | Closed. |

Final severity counts: **P0 0 / P1 0 / P2 0 / P3 0**.

## Achievement overlay implementation

Changed `docs/assets/014_cannibalism/achievements_imagegen/process_achievement_icons.py`:

- Declares the mandatory overlay at `.agents/skills/chaos-redux-event-assets/assets/achievements/overlay.png`.
- Refuses execution if the overlay does not exist, is not exactly 64x64, or is not RGBA.
- Copies each 64x64 RGBA grey variant without applying brightness, contrast, recolour, filter, scale, or any locally drawn marks.
- Uses `Image.alpha_composite(grey_copy, overlay)` for the not-eligible state.
- Verifies each produced not-eligible image byte-for-byte against a fresh exact alpha composite before writing outputs.

The old brightness pass and all `ImageDraw.line` / `ImageDraw.ellipse` X construction were removed.

The existing processor was rerun successfully and reported `Processed and validated 18 achievement masters and 54 runtime variants`. It rebuilt:

- 18 `docs/assets/014_cannibalism/achievements_imagegen/processed_png/014_cannibalism_*_not_eligible.png` files.
- 18 `docs/assets/014_cannibalism/achievements_imagegen/dds/014_cannibalism_*_not_eligible.dds` files.
- 18 live `gfx/achievements/014_cannibalism_*_not_eligible.dds` files.
- `docs/assets/014_cannibalism/achievements_imagegen/contact_sheets/achievement_final_variants_contact_sheet.png`.
- `docs/assets/014_cannibalism/achievements_imagegen/contact_sheets/achievement_dds_decoded_contact_sheet.png`.
- `docs/assets/014_cannibalism/achievements_imagegen/validation/achievement_icon_validation.tsv`.

The processor also refreshed its 18 chroma-cleaned alpha intermediates while reproducing byte-identical completed and grey final states. `docs/assets/014_cannibalism/achievements_imagegen/manifest.md` now states the exact overlay contract and processor assertions.

## Manifest reconciliation

Changed `docs/assets/014_cannibalism/animations_imagegen/manifest.md`:

- Preserves the six early 8-frame experiments and their source/processed/review evidence as historical provenance.
- Explicitly states that they have no live DDS or sprite ownership.
- Points to `docs/assets/014_cannibalism/gui_animation_portraits/manifest.md` and its live handoff as the accepted 14-animation source of truth.

Changed `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md`:

- Preserves the source and processed concept ledger.
- Removes all final runtime DDS/TGA and sprite claims from this historical package.
- Records the current report/news, kinetic super-event, flag, regional portrait, and animated portrait package owners.
- Explicitly identifies rejected or superseded report, council, leader, Last Table flag, and old super-event alternatives as non-runtime provenance.

Changed `docs/assets/014_cannibalism/manifest.md`:

- Uses `docs/assets/014_cannibalism/achievements_imagegen/manifest.md` as the achievement owner.
- Uses `docs/assets/014_cannibalism/gui_animation_portraits/manifest.md` as the live animation owner and labels the earlier six-package manifest historical.
- Names the four existing ordinary/transformed Hannibal sheet/fallback DDS paths instead of the absent council portrait.
- Uses `interface/014_cannibalism_achievements.gfx` as the achievement registry.

## Recheck evidence

### Runtime GFX closure

The same nine Event 014-related GFX files were rescanned after regeneration:

- References: 816
- Unique runtime texture paths: 598
- Missing paths: 0
- Unique SHA-256 hashes: 598
- Duplicate hash groups: 0

### Achievement triplets

- Overlay: exists, RGBA, 64x64.
- Grey inputs tested: 18.
- Exact alpha-composite mismatches: 0.
- Runtime triplets: 54 = 18 completed + 18 grey + 18 not-eligible.
- Unique runtime hashes: 54.
- Package DDS count: 54.
- Package/live DDS hash mismatches: 0.
- The regenerated final-variant contact sheet was inspected; all 18 not-eligible icons show the mandated common overlay over the unchanged grey state.

### Accepted animation contract

- Packages: 14.
- Source frames: 142.
- Processed frames: 142.
- Source/processed count mismatches: 0.
- Packages with duplicate source-frame hashes: 0.
- Packages with duplicate processed-frame hashes: 0.
- Missing GIF/contact evidence: 0.
- Missing sheet/static PNG pairs: 0.
- Missing live sheet/static DDS pairs: 0.
- Packages absent from `docs/assets/014_cannibalism/gui_animation_portraits/validation/gfx_handoff.tsv`: 0.
- Handoff rows: 40 total, including 12 non-portrait animation pairs and both portrait pairs alongside the static GUI entries.

### Manifest closure

A targeted scan of the reconciled manifests found:

- Retired absent-animation DDS claims: 0.
- Absent council/leader/old-super-event DDS claims: 0.
- Stale `interface/chaosx_achievements.gfx` ownership claims: 0.
- Stale superseded achievement-package ownership claims: 0.
- `Status: complete`, `Static DDS:`, or `Sheet DDS:` live-output claims in the retired animation manifest: 0.
- Final-game-file or `gfx/*.dds` / `gfx/*.tga` ownership claims in the historical generated-art ledger: 0.

## Changed-file scope

- Processor and package documentation:
  - `docs/assets/014_cannibalism/achievements_imagegen/process_achievement_icons.py`
  - `docs/assets/014_cannibalism/achievements_imagegen/manifest.md`
- Regenerated achievement package evidence and outputs:
  - 18 alpha intermediates under `docs/assets/014_cannibalism/achievements_imagegen/alpha_png/`
  - 18 not-eligible PNG files under `docs/assets/014_cannibalism/achievements_imagegen/processed_png/`
  - 18 not-eligible package DDS files under `docs/assets/014_cannibalism/achievements_imagegen/dds/`
  - 18 not-eligible runtime DDS files under `gfx/achievements/`
  - two achievement contact sheets and `validation/achievement_icon_validation.tsv`
- Reconciled manifests:
  - `docs/assets/014_cannibalism/animations_imagegen/manifest.md`
  - `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md`
  - `docs/assets/014_cannibalism/manifest.md`
- Audit/handoff documentation:
  - `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_asset_final_reaudit_2026-07-12.md`
  - `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_asset_final_remediation_2026-07-12.md`

## Simplifications, omissions, and remaining blockers

None. No fallback treatment was used, no requested asset was omitted, and no P0-P3 finding remains in the remediated Event 014 asset/audio/animation scope.
