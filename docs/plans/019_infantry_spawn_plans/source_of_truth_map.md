# Event 019 Documentation Source-of-Truth Map

Date reconciled: 2026-08-09  
Scope: current documentation reconciliation after the provider-522 and expanded
unit-coverage tranches. The 2026-07-18 regional full-flag and whole-event audit
remain historical evidence for their bounded surfaces; they do not close the
current provider-extension validation boundary. This map records the current
provider inventory, exact equipment contracts, owner gates, support-only CBRN
boundary, MCP limitations, and plan dispositions.

## Authority order

1. Accepted design remains under `docs/specs/019_infantry_spawn_specs/`.
   `README.md` routes the current state, and the review files
   `review/blockers_and_uncertainty.md` and `review/spec_completion_audit.md`
   carry the live gates and planning-only qualification.
2. Player-facing feature status is summarized by
   `docs/events/019_infantry_spawn/overview.md` and
   `docs/events/019_infantry_spawn/systems/triggerable_scenario.md`, which is the
   SCN-013 implementation-facing documentation. The old
   `docs/systems/triggerable_scenarios.md` path is not present in the current tree
   and must not be used as a source reference.
3. Historical asset references name
   `docs/assets/019_infantry_spawn/manifest.md` and
   `docs/assets/019_infantry_spawn/gfx_handoff.md`, but the
   `docs/assets/019_infantry_spawn/` directory is absent in the current tree.
   Static package evidence and legacy 3D roots therefore remain unresolved
   cross-references rather than a durable current asset authority.
4. Working plans and subagent handoffs under
   `docs/plans/019_infantry_spawn_plans/` are evidence with an explicit
   disposition. Historical files remain available, but supersession notices
   identify when they must not be used as current instructions.
5. The workbook remains the only editable catalog source. Parent
   workbook/catalog reconciliation and export are complete, with Event 19 and
   SCN-013 promoted to `Fully Functional`. CSV exports match the workbook rows
   and remain generated outputs rather than documentation authorities.
6. `docs/specs/019_infantry_spawn_specs/review/decision_only_surface_addendum_2026-08-05.md`
   is the current player-facing UI decision. It supersedes the former scripted-
   GUI implementation handoffs while preserving their production provenance as
   archival evidence; provider coverage and registry status remain owned by the
   Event 19 systems docs below.

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
current for the derivative classifier and registry/scenario contract. The current
static provider census is 18 IDs (`501-514`, `518`, `520-522`), with 12
definitions per provider (registration plus eleven Event 19 callbacks). Event 016
providers `504-510` use their history-derived gates; provider `522` is a separate
Aryan clone adapter gated by `germany_mengele_is_germany_scope`,
`germany_mengele_program_active`, the completed cloning-project and master-race-
claim flags, and `mengele_aryan_clone_refinement_tech`. Providers 504 and 522 use
ten combat battalions with 1,000 manpower, 90 infantry equipment, and 1 clone
equipment per battalion, with a 1,000 manpower, 180 infantry equipment, and 2
clone equipment sustainment contract. Provider 521 records only the combat
`chaos_battalion`; CBRN support-only bodies and `chemical_agent_payload` remain
parent-owned. Provider 513 is structurally covered and package-gated until Event
012 sets `africa_strange_formation_package_ready`; static package evidence
includes all eight combat/support unit definitions, eight meshes/entities,
packaged DDS maps, and 49 sound files. The current worktree includes the owner
manifest and setter in `common/scripted_effects/012_africa_strange_force_manifest_effects.txt`,
but that file and its startup call are untracked in this audit and require parent
integration and validation before provider 513 can be promoted from package-
gated evidence. The provider-side `event19_get_management_cost_display` callback
writes the presentation profile into the shared Muster Board cache without
debiting resources; profiles `0-18` identify provider cost text and profile `99`
identifies ledger-backed zero-debit adapters whose tooltip must state that
obligations are tracked by the Event 19 manifest. No second registry file,
family-list edit, or gameplay documentation change is implied by the provider
route.

The selected-family spawn verifier is now manifest-aware. It accepts a committed provider obligation tail of zero, two, seven, or sixteen rows, derives expected manpower liability and equipment debt from the committed manifest totals, and proves sequential obligation UIDs, generation/lot/unit ownership, issued versus outstanding amounts, zero payment/salvage state, outstanding status, profile-appropriate debt, and aligned tail counts before commit. Provider 518's cave package intentionally contributes zero obligation rows because both manifest needs are zero.

The narrow Event 19 MCP inspect is `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. Its current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b8ab34f7c29cf4c369c71654d72a847a85d4a8dc63434cb53ac7597e9e3a617/397c297d86f363f52ab7944e7a9643f05a96d2be00743315a2a57306f95d7b23/event-lint-08357425bddf.json`. The matching bounded Event 19 render request (`overview`, `chaosx.nr19.1`, max depth 2 and 240 nodes) timed out after 180 seconds and produced no artifact. The installed probability adapter cannot expose normalized odds for the dynamic provider pool (`poolComplete=false` and zero discovered candidates in the retained probability evidence). These limitations are recorded as evidence rather than promoted to a completion claim.

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

## Historical 2026-07-18 closure status

- Parent workbook/catalog reconciliation and export are complete.
- Parent package inventory reconciliation is complete. The current
  `review/package_contents.md` verifies all 33 files with no missing, extra, or
  mismatched rows and records the 4,342-character goal prompt.
- The mandatory final whole-event completion audit is PASS with P0/P1/P2 = 0.

The 2026-07-18 audit recorded Event 019 and SCN-013 as `Fully Functional` for
that historical tranche. The approved engine-constrained exact-transfer and
controlled-combat-trial contracts, regional asset gate, workbook/catalog
reconciliation, package inventory, and final audit were resolved for their
bounded surfaces. That status does not include the later provider-522 or expanded
unit-coverage extension, and no current whole-event completion claim is made here.
No fallback or unapproved substitute is recorded here.
