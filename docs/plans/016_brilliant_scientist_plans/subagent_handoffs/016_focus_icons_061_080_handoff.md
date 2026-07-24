# Event 016 focus icon tranche 061-080 handoff

Date: 2026-07-24

## Scope and ownership

Produced the 20 exact Kruger State national-focus icon rows 061-080. This handoff owns source PNGs, alpha PNGs, processed 94x86 previews, runtime DDS files, decoded DDS previews, provenance, validation, contact sheets, and asset documentation only. No `.gfx`, focus, localisation, gameplay, GUI, event, spreadsheet, or unrelated file was edited.

## Completed rows

| Row | Focus ID | Runtime DDS |
|---:|---|---|
| 061 | `KRG_designate_breeding_reserves` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_designate_breeding_reserves.dds` |
| 062 | `KRG_train_handlers_and_veterinarians` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_train_handlers_and_veterinarians.dds` |
| 063 | `KRG_build_the_transport_pens` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_build_the_transport_pens.dds` |
| 064 | `KRG_drill_for_the_great_escape` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_drill_for_the_great_escape.dds` |
| 065 | `KRG_the_dinosaur_host` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_the_dinosaur_host.dds` |
| 066 | `KRG_open_the_designed_organism_dossier` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_open_the_designed_organism_dossier.dds` |
| 067 | `KRG_build_the_vat_complexes` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_build_the_vat_complexes.dds` |
| 068 | `KRG_lock_the_control_channel` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_lock_the_control_channel.dds` |
| 069 | `KRG_seal_the_containment_cells` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_seal_the_containment_cells.dds` |
| 070 | `KRG_red_team_the_autonomous_nest` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_red_team_the_autonomous_nest.dds` |
| 071 | `KRG_the_engineered_legion` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_the_engineered_legion.dds` |
| 072 | `KRG_recover_the_transit_logs` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_recover_the_transit_logs.dds` |
| 073 | `KRG_harden_the_terminal_rings` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_harden_the_terminal_rings.dds` |
| 074 | `KRG_link_the_depot_network` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_link_the_depot_network.dds` |
| 075 | `KRG_close_the_transit_breach` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_close_the_transit_breach.dds` |
| 076 | `KRG_the_strategic_transit_corps` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_the_strategic_transit_corps.dds` |
| 077 | `KRG_authenticate_the_temporal_ledger` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_authenticate_the_temporal_ledger.dds` |
| 078 | `KRG_fortify_the_anchor` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_fortify_the_anchor.dds` |
| 079 | `KRG_found_the_synchronization_bureau` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_found_the_synchronization_bureau.dds` |
| 080 | `KRG_issue_bounded_future_warnings` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_issue_bounded_future_warnings.dds` |

For every row, the exact filename stem is shared across `source_png/focus_icons/*_source.png`, `alpha_png/focus_icons/*_alpha.png`, `processed_png/focus_icons/*.png`, decoded DDS previews, and the runtime DDS path above.

## Generation and processing evidence

- Built-in `$imagegen` was used once per row with distinct focus-specific prompts from `docs/assets/016_brilliant_scientist/prompts/kruger_state_focus_icon_prompts.md`.
- Prompt and source-output lineage is recorded in `docs/assets/016_brilliant_scientist/package_records/focus_icon_generation_061_080_provenance.json`.
- Chroma-key removal used the official `remove_chroma_key.py` helper with `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`.
- Each alpha master was cropped to its non-zero alpha bounds and fitted with LANCZOS inside a centered `92x86` content box on an exact `94x86` RGBA canvas. One near-transparent green fringe pixel in row 078 was removed during final alpha cleanup before DDS conversion.
- Final DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` at `94x86`.

## Validation and review

- Row-level evidence with source, processed, processed-RGBA, and DDS SHA-256 hashes is in `docs/assets/016_brilliant_scientist/validation/focus_icon_validation_061_080.tsv` and appended to `focus_icon_validation_partial.tsv`.
- All 20 processed PNGs and decoded DDS files are exactly `94x86` RGBA, with corner alpha `0/0/0/0`, alpha range `0..255`, zero visible green-key pixels, and pixel-identical PNG/DDS decode.
- Runtime decode PNGs are retained under `docs/assets/016_brilliant_scientist/dds_decoded_png/focus_icons/`.
- Contact sheets: `focus_icon_sources_061_080_contact_sheet.png`, `focus_icon_processed_061_080_contact_sheet.png`, and `focus_icon_dds_decoded_061_080_contact_sheet.png`.
- Distinctness audit found all 20 processed pixel payloads unique; the closest pair still differs by mean absolute RGBA distance `26.80`.
- Visual review note: all 20 compositions are distinct, centered, high-contrast, painterly HOI4-style emblems with route-specific subjects (paleogenetic reserves/handlers/transport/escape, engineered organisms and containment, portal transit, and temporal ledgers/anchors/synchronization). The enlarged processed sheet shows clean silhouettes and no opaque background.
- Read-only consumer audit found all 20 exact normal sprite names and all 20 `_shine` sprite names in `interface/016_brilliant_scientist_kruger_state_focus.gfx`, and all 20 exact focus IDs in the loaded `common/national_focus` sources; no missing consumer was found.

## Manifest and handoff updates

- `docs/assets/016_brilliant_scientist/kruger_state_focus_icon_manifest.md` marks rows 061-080 `complete`, records the tranche evidence paths, and includes row-level hash/dimension entries.
- `docs/assets/016_brilliant_scientist/gfx_handoff.md` includes the 061-080 runtime folder, sprite naming contract, evidence paths, and no-wiring boundary.

## Remaining risks

- Native in-game rendering was not claimed and remains part of final acceptance.
- Rows 081-100 are complete and have a separate accepted handoff; they were not edited by this tranche.

## Parent disposition

Accepted on 2026-07-24 after direct visual review of the source, processed, and decoded-DDS contact sheets. All twenty subjects are distinct and route-specific, silhouettes remain legible at the runtime size, transparency is clean, and the processed and decoded-DDS sheets are visually identical. The existing exact normal and shine sprite registrations and exact focus consumers were also confirmed by the tranche audit. Native in-game rendering remains part of the final focus-tree validation rather than this asset-only acceptance.
