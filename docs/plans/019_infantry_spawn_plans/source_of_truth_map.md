# Event 019 Documentation Source-of-Truth Map

Date reconciled: 2026-07-18  
Scope: documentation reconciliation after the regional full-flag production
tranche. This map records current evidence and dispositions. The final
completion audit is PASS with P0/P1/P2 = 0, and Event 019 and SCN-013 are
`Fully Functional`.

## Authority order

1. Accepted design remains under `docs/specs/019_infantry_spawn_specs/`.
   `README.md` routes the current state, and the review files
   `review/blockers_and_uncertainty.md` and `review/spec_completion_audit.md`
   carry the live gates and planning-only qualification.
2. Player-facing feature status is summarized by
   `docs/events/019_infantry_spawn/overview.md` and
   `docs/systems/triggerable_scenarios.md`.
   `docs/events/019_infantry_spawn/systems/triggerable_scenario.md` is the SCN-013
   implementation-facing documentation.
3. Asset status is owned by
   `docs/assets/019_infantry_spawn/manifest.md` and
   `docs/assets/019_infantry_spawn/gfx_handoff.md`, with machine evidence in
   the 7/18 validation and checksum records named below.
4. Working plans and subagent handoffs under
   `docs/plans/019_infantry_spawn_plans/` are evidence with an explicit
   disposition. Historical files remain available, but supersession notices
   identify when they must not be used as current instructions.
5. The workbook remains the only editable catalog source. Parent
   workbook/catalog reconciliation and export are complete, with Event 19 and
   SCN-013 promoted to `Fully Functional`. CSV exports match the workbook rows
   and remain generated outputs rather than documentation authorities.

## Current regional flag chain

The sole current source/runtime chain is:

1. **91 raw sources:** unmodified built-in ImageGen full-flag raws under
   `docs/assets/019_infantry_spawn/source_png/flags/regional_full_flag_raw/`.
   The claimant/zombie tranche has 35 rows, ghost has 28, and golem has 28.
   The seven GHOST_BASE prompt records were recovered exactly in their existing
   ghost-owned prompt/provenance files. Those protected files were not edited.
2. **91 spot masters:** deterministic 820x520 RGB masters under
   `docs/assets/019_infantry_spawn/processed_png/flags/regional_spot_colour_masters/`.
3. **273 native PNGs:** normal, medium, and small outputs under
   `docs/assets/019_infantry_spawn/processed_png/flags/`, at 82x52, 41x26, and
   10x7 respectively.
4. **273 runtime TGAs:** bottom-left-origin files under
   `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

The processor and exact evidence are:

- processor: `docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py`
- processor SHA-256: `d87e879184d5a28a52736b80af4bc0ce70abd9744de47210b1f6a7c3db15ece6`
- validation: `docs/assets/019_infantry_spawn/regional_flag_validation_2026_07_18.json`
- checksums: `docs/assets/019_infantry_spawn/regional_flag_checksums_2026_07_18.sha256`
- recorded runtime: Python 3.9.12, Pillow 11.1.0, NumPy 2.0.2
- validator status: `candidate_requires_independent_visual_review`

The validation record reports 91 identity rows, 7 region rows, 91 tag rows,
273 runtime TGA rows, and passing visual/runtime review rows. The independent
remediation re-audit handoff
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`
is PASS and clears the regional asset gate for parent-owned package promotion.
The machine JSON retains its immutable literal
`candidate_requires_independent_visual_review` processor-state value, which is
superseded for approval by the separate PASS handoff and was not edited.

## Prompt and provenance disposition

The 7/18 claimant/zombie, ghost, and golem raw prompt/provenance records are
the current production evidence. The ghost prompt and provenance records are
ghost-owned and were deliberately left unchanged. The 7/16 motif prompt and
generation-provenance files are retained only as historical superseded records.

## Runtime and registry documentation

The one Event 019 registry code file remains
`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.
`common/scripted_triggers/chaosx_dynamic_triggers.md` was inspected and remains
current for the derivative classifier and registry/scenario contract. No second
registry file, family-list edit, or gameplay documentation change is implied by
the regional asset route.

## Superseded or archival material

The following are historical evidence and must not be treated as the current
source/runtime chain:

- `docs/assets/019_infantry_spawn/source_png/flags/regional_variants/`
- `docs/assets/019_infantry_spawn/regional_flag_validation_2026_07_16.json`
- `docs/assets/019_infantry_spawn/regional_flag_checksums_2026_07_16.sha256`
- 7/16 motif/composite notes, prompts, provenance, validation, and contact
  sheets, including the files with explicit supersession banners
- `subagent_handoffs/019_regional_flag_assets_handoff_2026_07_16.md`
- `subagent_handoffs/019_regional_flag_flat_source_blocker_options_2026_07_17.md`
- `subagent_handoffs/019_regional_flag_flatness_rescue_2026_07_16.md`

The three 7/18 raw-tranche handoffs remain valid as tranche evidence, but their
raw-only boundary is historical after the common postprocess. Their banners
route readers to this map and the independent validation record. The separate
remediation re-audit PASS handoff is the approval authority for the current
regional candidate.

## Final closure status

- Parent workbook/catalog reconciliation and export are complete.
- Parent package inventory reconciliation is complete. The current
  `review/package_contents.md` verifies all 33 files with no missing, extra, or
  mismatched rows and records the 4,342-character goal prompt.
- The mandatory final whole-event completion audit is PASS with P0/P1/P2 = 0.

Event 019 and SCN-013 are `Fully Functional`. The approved engine-constrained exact-transfer and
controlled-combat-trial contracts, regional asset gate, workbook/catalog
reconciliation, package inventory, and final audit are resolved. No closure gate
remains. No fallback or unapproved substitute is recorded here.
