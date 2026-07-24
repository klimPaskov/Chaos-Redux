# Event 016 focus icon tranche 041-060 handoff

Date: 2026-07-24

## Scope and ownership

Produced the 20 exact Kruger State national-focus icon rows 041-060. This handoff owns source PNGs, alpha PNGs, processed 94x86 previews, runtime DDS files, provenance, validation, contact sheets, and asset documentation only. No `.gfx`, focus, localisation, gameplay, GUI, event, spreadsheet, or unrelated file was edited.

## Completed rows

| Row | Focus ID | Runtime DDS |
|---:|---|---|
| 041 | `KRG_restore_the_ordinary_chain_of_command` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_restore_the_ordinary_chain_of_command.dds` |
| 042 | `KRG_recall_the_defector_officers` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_recall_the_defector_officers.dds` |
| 043 | `KRG_laboratory_engineer_battalions` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_laboratory_engineer_battalions.dds` |
| 044 | `KRG_found_the_counterintelligence_bureau` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_found_the_counterintelligence_bureau.dds` |
| 045 | `KRG_shield_the_laboratory_airspace` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_shield_the_laboratory_airspace.dds` |
| 046 | `KRG_a_general_staff_for_the_state` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_a_general_staff_for_the_state.dds` |
| 047 | `KRG_a_council_of_project_commanders` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_a_council_of_project_commanders.dds` |
| 048 | `KRG_audit_the_growth_halls` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_audit_the_growth_halls.dds` |
| 049 | `KRG_secure_the_nutrient_chain` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_secure_the_nutrient_chain.dds` |
| 050 | `KRG_write_the_identity_register` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_write_the_identity_register.dds` |
| 051 | `KRG_field_the_clone_cadres` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_field_the_clone_cadres.dds` |
| 052 | `KRG_stabilize_replication_drift` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_stabilize_replication_drift.dds` |
| 053 | `KRG_the_replicated_host` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_the_replicated_host.dds` |
| 054 | `KRG_wake_the_assembly_lines` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_wake_the_assembly_lines.dds` |
| 055 | `KRG_secure_the_machine_power_backbone` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_secure_the_machine_power_backbone.dds` |
| 056 | `KRG_standardize_frame_repair` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_standardize_frame_repair.dds` |
| 057 | `KRG_write_the_machine_command_protocol` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_write_the_machine_command_protocol.dds` |
| 058 | `KRG_air_gap_the_rogue_nodes` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_air_gap_the_rogue_nodes.dds` |
| 059 | `KRG_an_army_of_machines` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_an_army_of_machines.dds` |
| 060 | `KRG_open_the_restoration_ledger` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_open_the_restoration_ledger.dds` |

For every row, the exact filename stem is shared across `source_png/focus_icons/*_source.png`, `alpha_png/focus_icons/*_alpha.png`, `processed_png/focus_icons/*.png`, and the runtime DDS path above.

## Generation and processing evidence

- Built-in `$imagegen` was used once per row with distinct focus-specific prompts from `docs/assets/016_brilliant_scientist/prompts/kruger_state_focus_icon_prompts.md`.
- Prompt and source-output lineage is recorded in `docs/assets/016_brilliant_scientist/package_records/focus_icon_generation_041_060_provenance.json`.
- Chroma-key removal used the official `remove_chroma_key.py` helper with `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`.
- Each alpha master was cropped to its non-zero alpha bounds and fitted with LANCZOS inside a centered `92x86` content box on an exact `94x86` RGBA canvas.
- Final DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` at `94x86`.

## Validation and review

- Row-level evidence with source, processed, processed-RGBA, and DDS SHA-256 hashes is in `docs/assets/016_brilliant_scientist/validation/focus_icon_validation_041_060.tsv` and appended to `focus_icon_validation_partial.tsv`.
- All 20 processed PNGs and decoded DDS files are exactly `94x86` RGBA, with corner alpha `0/0/0/0`, alpha range `0..255`, zero visible green-key pixels, and pixel-identical PNG/DDS decode.
- Runtime decode PNGs are retained under `docs/assets/016_brilliant_scientist/dds_decoded_png/focus_icons/`.
- Contact sheets: `focus_icon_sources_041_060_contact_sheet.png`, `focus_icon_processed_041_060_contact_sheet.png`, and `focus_icon_dds_decoded_041_060_contact_sheet.png`.
- Read-only consumer audit found all 20 exact normal sprite names and all 20 `_shine` sprite names in `interface/016_brilliant_scientist_kruger_state_focus.gfx`, and all 20 exact focus IDs in the loaded `common/national_focus` sources; no missing consumer was found.
- Visual review note: all 20 compositions are distinct, centered, high-contrast, painterly HOI4-style emblems with route-specific subjects (conventional command, engineering/counterintelligence/air defense, clone infrastructure and host, robotics power/repair/command, and paleogenetic restoration). The enlarged processed sheet shows clean silhouettes and no opaque background.

## Parent rejection and row 053 revision

- Parent rejected the original `KRG_the_replicated_host` master because the bottom shield and several medical-supply surfaces contained recognizable red-cross medical emblems.
- A targeted built-in ImageGen edit preserved the host ranks, DNA standard, laurel, neutral supply gear, and overall composition, removed every red-cross/protected mark, and replaced the bottom shield with a fictional gold-and-ivory double-helix-and-cradle clone-host symbol.
- Stable source, alpha, processed PNG, DDS, and DDS-decoded filenames remain unchanged. All three 041-060 contact sheets were rebuilt so row 053 shows the accepted revision.
- Rejected source SHA-256: `048388512bd70ee18cefedd392b69dfbfb12d43593268d562bfc09a2c81b245f` from ImageGen output `exec-a76ba041-ecf5-4222-96a9-7464d094da58.png`.
- Accepted source SHA-256: `cc9d1ffb3b19ba12e07b21552d950195471383128ee7cead52cd2549b83d67c7` from ImageGen edit `exec-b4adabf4-f00d-487f-964c-4747a99fc801.png`.
- Accepted row 053 processed SHA-256: `5ee8b601b834f13ee7a53a6e0d966290938b7c91cbd4661f1582ce0b4b036746`; accepted DDS SHA-256: `0a56ce2b7be73b8cf1ea195f5936d1d37f948fe08e27bd96008158c37ada8e30`.
- The complete revision lineage is recorded in `docs/assets/016_brilliant_scientist/package_records/focus_icon_generation_041_060_provenance.json`; updated row-level hashes are in both validation TSVs.

## Manifest and handoff updates

- `docs/assets/016_brilliant_scientist/kruger_state_focus_icon_manifest.md` marks rows 041-060 `complete`, records the tranche evidence paths, and includes row-level hash/dimension entries.
- `docs/assets/016_brilliant_scientist/gfx_handoff.md` includes the 041-060 runtime folder, sprite naming contract, evidence paths, and no-wiring boundary.

## Remaining risks

- Native in-game rendering was not claimed and remains part of final acceptance.
- Rows 061-100 are complete and have separate accepted handoffs; they were not edited by this tranche.

## Parent review disposition

Accepted on 2026-07-24 after review of the rebuilt source, processed, and DDS-decoded contact sheets. The revised row 053 removes every recognizable red-cross or protected medical emblem and replaces the shield with a fictional double-helix-and-cradle clone-host mark while preserving the intended replicated-host composition. All twenty rows are visually accepted, and the exact normal and `_shine` registrations plus matching focus consumers are accepted from the recorded static audit. Live in-game focus-tree rendering is not claimed here.
