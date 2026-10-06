> Current parent status: all 47 runtime DDS files were independently reviewed, installed and pixel-verified on 2026-10-06. The worker staging statements below are historical handoff evidence. Final MCP rendering returned Transport closed; live acceptance is pending.

# AOX focus icon handoff

Status: the parent reviewed all 47 native-size DDS sheets and approved the staged art for root-owned guarded runtime promotion.

## Existing registration

The existing registry is interface/005_soviet_collapse_focus_icons.gfx. It already defines 47 base aliases named GFX_focus_AOX_<suffix> and 47 shine aliases named GFX_focus_AOX_<suffix>_shine. Both aliases for each focus point to the same runtime texture path, gfx/interface/goals/005_soviet_collapse/focus_005_aox_<suffix>.dds. Keep those existing sprite names and paths when promoting this package.

The exact focus-id, localized title, base sprite, shine sprite, staged DDS, runtime DDS and source-to-output hashes are in staged_to_runtime_crosswalk.csv. The full runtime source details and reward blocks are in notes/aox_source_inventory.json.

## Staged assets

Each selected 94x86 PNG is in processed_png/focus_005_aox_<suffix>.png. Each converted DDS is staged under staged_runtime/gfx/interface/goals/005_soviet_collapse/focus_005_aox_<suffix>.dds. The matching source PNG, exact prompt and candidate history remain in source_png/, prompts/aox_imagegen_prompts.json and notes/candidate_lineage.json.

The staged files are ready for copy to their matching runtime paths. This worker did not change runtime DDS files or interface/005_soviet_collapse_focus_icons.gfx.

## Review and conversion evidence

Before and after native-size checker/dark sheets, enlarged previews, source-to-PNG-to-DDS comparisons and decoded DDS roundtrip sheets are in contact_sheets/. The strict verification report is notes/dds_roundtrip_report.json; all 47 staged files pass header, dimensions, alpha, exact-file-length and pixel-equality checks.

Parent review accepted all 47 native DDS sheets and selected the arc-free AOX_extreme_path revision. Its PNG, DDS, roundtrip sheets and strict proof were refreshed after that focused edit. Candidate-specific revisions and the edge-color correction are recorded in notes/candidate_lineage.json and notes/processing_metadata.json. Runtime promotion and the tree commit remain root-owned.

## Plan-name reconciliation

Five suffixes in the older review row do not match the live focus ids and existing registry: icebound_supply maps to icebound_supply_ledger; petrograd_signal maps to petrograd_signal_watch; red_fleet_signal maps to red_fleet_signal_posts; sailor_worker_deputies maps to sailor_worker_defense_council; sailors_assembly maps to sailors_assembly_registers. The crosswalk uses the existing live suffixes and paths.

The review row proposes 100x88 icons. The current AOX DDS consumer is 94x86, and the parent task specified 94x86, so the staged files use the exact current texture size.
