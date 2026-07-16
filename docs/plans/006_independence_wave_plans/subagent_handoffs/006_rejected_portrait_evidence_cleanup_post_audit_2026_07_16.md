# Event 006 rejected portrait evidence cleanup post-audit

Date: 2026-07-16

Mode: independent read-only final-state audit. This handoff is the only file
created by the audit. No gameplay, interface, localisation, runtime asset,
flag, package evidence, spreadsheet, builder, ledger, manifest, prompt, or
other documentation file was edited.

## Verdict

**PASS.** The exact nineteen-target cleanup is complete and bounded. All
authorized deletion targets are absent, every named protected surface remains,
the accepted package exactly covers the twenty regenerated large portraits and
ten regenerated commander-small portraits, all thirty-two runtime Event 006
portrait DDS files match the accepted runtime ledger, the two protected
historical hashes remain exact, the generated-NWE workflow is genuinely
flag-only, and the withdrawn custom advisor-icon surface remains absent.

No active stale dependency on a deleted portrait-evidence path was found.

The deletion transaction itself is recorded in
`006_rejected_portrait_evidence_cleanup_execution_2026_07_16.md` as exactly
nineteen targets, 331 files, and 155,622,295 bytes. This post-audit independently
validated the resulting path state and dependency boundaries.

## Exact deletion-set audit

Every exact target below returns absent.

### Five rejected portrait-only packages

- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/`
- `docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15/`
- `docs/assets/006_independence_wave/live_afx_agx_portrait_regen_2026_07_15/`
- `docs/assets/006_independence_wave/bri_package_2026_07_15/`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/`

### Ten mixed-tree portrait directories

- `docs/assets/006_independence_wave/source_png/generated_nwe/command_portraits/`
- `docs/assets/006_independence_wave/source_png/generated_nwe/institutional_portraits/`
- `docs/assets/006_independence_wave/source_png/generated_nwe/registered_command_portraits/`
- `docs/assets/006_independence_wave/source_png/generated_nwe/registered_institutional_portraits/`
- `docs/assets/006_independence_wave/processed_png/generated_nwe/command_portraits/`
- `docs/assets/006_independence_wave/processed_png/generated_nwe/command_portraits_small/`
- `docs/assets/006_independence_wave/processed_png/generated_nwe/institutional_portraits/`
- `docs/assets/006_independence_wave/dds_decoded_png/generated_nwe/command_portraits/`
- `docs/assets/006_independence_wave/dds_decoded_png/generated_nwe/command_portraits_small/`
- `docs/assets/006_independence_wave/dds_decoded_png/generated_nwe/institutional_portraits/`

### Four rejected portrait contact sheets

- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_command_portraits_contact_sheet.png`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_institutional_portraits_contact_sheet.png`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_final_dds_decoded_contact_sheet.png`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_officer_small_dds_decoded_contact_sheet.png`

The similarly named
`docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md`
was not part of the nineteen-target transaction. It is retained as a rewritten
flag-only engine handoff and contains no portrait, leader, commander, advisor,
or `gfx/leaders` dependency.

## Protected-surface audit

### NWE flags and unrelated asset packages

All named protected directories exist and are non-empty:

- `source_png/generated_nwe/flags/`: 8 files;
- `processed_png/generated_nwe/flags/`: 12 files;
- `source_png/country_symbols/`: 5 files;
- `source_svg/country_symbols/`: 5 files;
- `afx_unique_assets_2026_07_16/`: 49 files;
- `ajx_asset_completion_2026_07_15/`: 10 files;
- `rhi_bay_unique_assets_2026_07_16/`: 111 files;
- `form01_02_04_flags_2026_07_15/`: 37 files;
- `low_countries_form03_2026_07_15/`: 14 files;
- `low_countries_form03_progression/`: 94 files;
- `mediterranean_danube_flag_sources_2026_07_15/`: 11 files;
- `mediterranean_danube_generated_flags_2026_07_15/`: 27 files;
- `super_events/`: 2 files.

Both protected NWE flag contact sheets and
`006_nwe_historical_flag_comparison.md` exist. All twelve ACX, AFX, AGX, and
AJX runtime flag TGAs exist across the normal, medium, and small ladders.

### Rupprecht, Matthes, and Debeauvais evidence

Nineteen exact protected provenance/review records were checked with zero
missing paths. These include both original historical sources, both processed
portraits, both metadata JSON files, both canonical comparison sheets, both
process-review sheets, the real-portrait visual review, the real-portrait
ImageGen provenance record, the protected NWE GFX handoff, all five named
Debeauvais negative-rights/source records, and the BRI portrait registry.

The related `source_png/portraits/imagegen_edits/` evidence also remains:

- `portrait_bay_rupprecht_of_bavaria_imagegen_candidate_01.png`;
- `portrait_bay_rupprecht_of_bavaria_imagegen_master.png`;
- `portrait_rhi_josef_friedrich_matthes_imagegen_master.png`.

## Runtime and accepted-package coverage

`gfx/leaders/006_independence_wave/` contains exactly thirty-two DDS files:

- 22 large `156x210` portraits;
- 10 commander-small `65x67` portraits.

The accepted runtime ledger contains exactly the same thirty-two paths. Direct
SHA-256 recomputation found zero missing rows, zero extra rows, and zero hash
mismatches. Independent binary-header checks found zero failures across DDS
magic, header size, dimensions, legacy uncompressed BGRA32 pixel format,
masks, texture caps, and exact byte length.

After excluding only the two protected historical portraits, the runtime set
contains exactly twenty regenerated large stems. Their set is identical to the
twenty files in the accepted package's `processed_png/` directory. The ten
runtime commander-small stems are identical to the ten files in
`small_processed_png/`.

Row-level retained evidence is complete:

| Evidence surface | Large | Small | Missing runtime stems |
| --- | ---: | ---: | ---: |
| generation prompts | 20 | not applicable | 0 |
| raw ImageGen masters | 20 | derived from matching commander master | 0 |
| processed PNGs | 20 | 10 | 0 |
| runtime DDS decodes | 20 | 10 | 0 |
| processing metadata | 20 | 10 | 0 |
| individual review sheets | 20 | 10 | 0 |

The raw-master ledger has twenty existing hash-matching rows. The frozen v4.3
input ledger has seventeen existing hash-matching rows. All five required
merged validation/review records named by the accepted manifest are present.

The protected runtime hashes remain exact:

- `portrait_BAY_rupprecht_of_bavaria.dds`:
  `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`;
- `portrait_RHI_josef_friedrich_matthes.dds`:
  `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`.

The six ACX/AEX readiness-pool textures remain included in the thirty-file
replacement coverage and in the thirty-two-row runtime ledger. Their
unregistered admission state was not changed by this cleanup.

## Old-authority reference audit

A broad repository scan covered all five deleted package names, all ten
deleted mixed-tree portrait directory families, and all four deleted contact
sheet names. Fifteen files retain at least one matching string. Every result is
bounded as one of the following:

- ten portrait-era implementation/audit handoffs with prominent
  portrait-specific supersession notices;
- `006_event6_portrait_documentation_promotion_2026_07_16.md`, which records
  those supersession edits;
- `006_nwe_flag_only_asset_workflow_cleanup_2026_07_16.md`, which records the
  pre-delete non-interference snapshot;
- `006_rejected_portrait_evidence_cleanup_plan_2026_07_16.md`, the cleanup
  source record;
- the unrelated Event 015 asset-tool migration handoff, where the paths are
  historical migration evidence; or
- the accepted second-tranche `validation_report.json`, whose single deleted
  contact-sheet path is explicitly labelled a production-time non-mutation
  guard that was later superseded and is not a current package dependency.

The current Event 006 asset manifest, source manifest, GFX handoff, package
documentation, source-of-truth map, resume packet, three asset-research
records, generated-flag manifest, generated-flag prompt record, and flag-only
engine handoff contain zero dependency on any deleted path. Current portrait
authorities point to
`portrait_regeneration_male_hoi4_2026_07_16/`.

**Active stale dependencies: none.**

## Generated-NWE flag-only audit

`_tooling/build_nwe_generated_art.py` is structurally flag-only:

- its source and processed roots are only `generated_nwe/flags/`;
- its runtime root is only `gfx/flags/`;
- its only write surfaces are retained flat masters, processed flag PNGs,
  runtime flag TGAs, two flag contact sheets, and the flag ledger;
- its explicit tag set is ACX, AFX, AGX, and AJX;
- `flags` is the only accepted `--scope` value;
- its inventory is built from an explicit flag path allowlist;
- it has zero `portrait`, `leader`, `commander`, `advisor`, `gfx/leaders`, or
  deleted generated-NWE portrait-tree references;
- it parses successfully as Python source.

`generated_nwe_hashes.sha256` has 47 rows. Every path exists and every hash
matches; there are zero portrait, leader, commander, advisor, or
`gfx/leaders` rows. The generated-flag manifest, prompt record, and retained
engine handoff likewise have zero forbidden non-flag semantic hits.

The corrected builder had already been run after deletion. The final-state
audit confirms that it recreated none of the nineteen deleted targets.

## Advisor-icon withdrawal audit

The custom advisor directory
`gfx/interface/ideas/006_independence_wave/advisors/` remains absent. The
dedicated registry `interface/006_independence_wave_nwe_advisors.gfx` remains
absent.

Active Event 006 script, history, interface, and runtime trees contain zero:

- `GFX_portrait_advisor_*` handles;
- withdrawn advisor runtime-path references;
- references to the deleted advisor registry; or
- custom advisor texture tokens.

The few repository-wide textual matches are either the current specification's
explicit no-custom-advisor rule or historical withdrawal/audit records. No
advisor icon, sprite, or runtime dependency was reintroduced.

## Files changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_rejected_portrait_evidence_cleanup_post_audit_2026_07_16.md`
  created as this audit handoff.

No commit was created.

## Simplifications, omissions, and blockers

No fallback, cleanup simplification, omission, active stale dependency, or
blocker was found.

The builder was not run a second time by this read-only audit because doing so
would rewrite protected flag assets and the ledger. Its just-completed
post-delete run was assessed through the resulting path state, an independent
write-surface/source audit, exact flag-ledger hash verification, and the
absence of all nineteen deleted targets. This scope boundary does not weaken
the PASS result.

## Skills used

- `chaos-redux-event-assets` for deletion/preservation classification,
  runtime portrait coverage, protected hashes, flag-only workflow separation,
  and advisor asset boundaries.
- `chaos-redux-subagents` for bounded audit ownership, handoff structure, and
  parent-review evidence.

No skill was created or updated.
