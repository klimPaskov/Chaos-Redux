# Asset skill DDS converter path migration handoff

Date: 2026-07-16  
Role: bounded `chaosx_skill_maintainer` path migration

## Outcome

The repository DDS converter was moved, not copied, from:

- `.tools/convert_to_dds.py`

to the owning reusable skill resource path:

- `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`

The move used native PowerShell `Move-Item -LiteralPath` after resolving and asserting both absolute paths inside the Chaos Redux workspace, asserting the destination directory was exactly `.agents/skills/chaos-redux-event-assets/tools/`, and confirming the destination file did not already exist.

## Byte and path proof

- Source before move: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.tools/convert_to_dds.py`
- Destination after move: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`
- Source exists after move: no
- Destination exists after move: yes
- File size: `10086` bytes
- Pre-move SHA-256: `D8AA0BA6A16BA8B6B698CCD6CF599B90E81DB6F6C6132009F07115C728F6B8A0`
- Post-move SHA-256: `D8AA0BA6A16BA8B6B698CCD6CF599B90E81DB6F6C6132009F07115C728F6B8A0`
- Executable content proof: the destination retains the `#!/usr/bin/env python3` shebang and is byte-identical to the source.

## Changed files

### Tool ownership and active guidance

- `.tools/convert_to_dds.py` — removed by the move.
- `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` — move destination.
- `.agents/skills/chaos-redux-event-assets/SKILL.md` — points portrait finishing and the canonical DDS invocation at the bundled tool.
- `.codex/agents/chaosx_asset_source_researcher.toml` — names the bundled converter explicitly.
- `.codex/agents/chaosx_generated_event_art.toml` — names the bundled converter explicitly.
- `.codex/agents/chaosx_icon_artist.toml` — invokes the bundled converter from the mod root.

### Rerunnable asset tooling

- `docs/assets/air_cleanliness_fallout/_tooling/process_air_winter_decision_icons.py`
- `docs/assets/air_cleanliness_fallout/regional_map_visuals/_tooling/process_regional_visuals.py`
- `docs/assets/019_infantry_spawn/_tooling/process_event_019_generated_art.py`
- `docs/assets/006_independence_wave/_tooling/process_independence_wave_icons.py`
- `docs/assets/006_independence_wave/_tooling/build_nwe_registered_civic_portraits.py`
- `docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py`
- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/build_portrait_package.py`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/_tooling/build_validation_evidence.py`
- `docs/assets/014_cannibalism/gui_animation_portraits/process_gui_nonportrait_assets.py`
- `docs/assets/014_cannibalism/achievements_imagegen/process_achievement_icons.py`
- `docs/assets/014_cannibalism/report_news_imagegen/process_report_news_assets.py`
- `docs/assets/014_cannibalism/warlord_focus_icons_imagegen/process_warlord_focus_icons.py`
- `docs/assets/014_cannibalism/remaining_registered_icons_imagegen/process_remaining_registered_icons.py`
- `docs/assets/014_cannibalism/unified_focus_assets/_tooling/process_unified_focus_assets.py`
- `docs/assets/014_cannibalism/warlord_command_assets_imagegen/process_warlord_command_assets.py`
- `docs/assets/014_cannibalism/registered_static_icons_imagegen/process_registered_static_icons.py`
- `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/_tooling/process_rows_01_09.py`
- `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/_tooling/process_rows_25_39.py`
- `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/subsets/rows_10_24/process_rows_10_24.py`
- `docs/assets/015_utopia_manifesto/_tooling/process_final_non_icon_package.py`
- `docs/assets/015_utopia_manifesto/_tooling/process_final_icon_frame_package.py`
- `docs/assets/015_utopia_manifesto/value_calling_icon_repair_2026_07_16/_tooling/process_value_calling_icons.py`
- `docs/assets/015_utopia_manifesto/ledger_case_cards_2026_07_16/tooling/process_case_cards.py`

Only converter path constants or converter-attribution comments changed in the Event 15 tooling files above. No Event 15 runtime asset, manifest, metadata file, or `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` was edited by this migration.

### Current asset documentation

- `docs/assets/fallout_world_end/manifest.md`
- `docs/assets/fallout_world_end/living_world_pilot/manifest.md`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prompts/bio_designate_strategic_raid_staging_state.md`
- `docs/assets/chaos_warfare_system/stage_6_chemical_designers/prompts/cbrn_chemical_munitions_combine.md`
- `docs/assets/chaos_warfare_system/stage_6_chemical_designers/prompts/cbrn_aerosol_air_delivery_bureau.md`
- `docs/assets/chaos_warfare_system/stage_6_chemical_designers/manifest.md`
- `docs/assets/chaos_warfare_system/stage_6_chemical_delivery/manifest.md`
- `docs/assets/chaos_warfare_system/stage_6_cbrn_designers/manifest.md`
- `docs/assets/chaos_warfare_system/stage_2_protective_equipment/manifest.md`
- `docs/assets/air_cleanliness_fallout/regional_map_visuals/manifest.md`
- `docs/assets/016_brilliant_scientist/manifest.md`
- `docs/assets/014_cannibalism/wendigo_focus_icons_imagegen/manifest.md`
- `docs/assets/014_cannibalism/static_event_art_imagegen/super_events_manifest.md`
- `docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/manifest.md`
- `docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/prompts/warlord_prompts.md`
- `docs/assets/014_cannibalism/registered_static_icons_imagegen/manifest.md`
- `docs/assets/006_independence_wave/bri_package_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/live_afx_agx_portrait_regen_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/generated_event_scenes_manifest.md`
- `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/submanifest.md`
- `docs/assets/006_independence_wave/low_countries_form03_progression/manifest.md`
- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/manifest.md`

### Handoff

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/asset_skill_tool_path_migration_2026_07_16.md`

## Reference audit

The audit covered all 11 repository `SKILL.md` files, all 16 `.codex/agents/*.toml` definitions, hidden repository files, asset prompts, Python tooling, manifests, metadata, checksums, and dated handoffs.

Final active-source results:

- stale old-path references in repository skills: `0`
- stale old-path references in custom subagent definitions: `0`
- stale old-path references in rerunnable Python callers: `0`
- unclassified old-path references: `0`

No separate reusable tool map or converter catalog exists outside the event-assets skill, so no additional map required an update.

## Intentionally retained historical references

The final repository scan finds old-path text in 19 files: 18 pre-existing preserved records or excluded surfaces plus this migration handoff, which necessarily names the source path. None is active skill, subagent, reusable-tool, or current-document guidance.

### This migration record

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/asset_skill_tool_path_migration_2026_07_16.md` names the removed source path to document and prove the move.

### Immutable dated handoffs

These record the command/path actually used at the time and were not rewritten:

- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_opening_report_asset_handoff.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_base_portrait_source_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form03_report_asset_handoff_2026_07_15.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/flag_institutional_identity_correction_handoff_2026_07_15.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_icon_correction_handoff.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_warlord_portraits_cbe_cbh_imagegen_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_warlord_portraits_cba_cbd_imagegen_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_idea_icon_repair_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_hoi4_portraits_cbg_cbh_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_hoi4_portraits_cbe_cbf_2026-07-15.md`
- `docs/assets/air_cleanliness_fallout/air_winter_modifier_icon_handoff.md`
- `docs/assets/015_utopia_manifesto/generated_event_art_handoff.md`

### Immutable provenance records

These preserve the path paired with an original build, validation, or checksum record:

- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/sha256_inventory.sha256`
- `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/metadata/report_event_006_form03_charter_convention_metadata.json`
- `docs/assets/006_independence_wave/live_afx_agx_portrait_regen_2026_07_15/validation.json`

### Event 15 surfaces reserved for the other worker

These were left untouched under the parent scope boundary:

- `docs/assets/015_utopia_manifesto/value_calling_icon_repair_2026_07_16/manifest.md`
- `docs/assets/015_utopia_manifesto/prompts/island_variant_icon_generation.md`
- `docs/assets/015_utopia_manifesto/prompts/generated_event_art_prompts.md`

## Validation

- `python -m py_compile` succeeded for the moved converter and all 23 updated Python callers.
- `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --help` exited successfully and displayed the expected required `--input` and `--output` arguments plus optional `--width` and `--height` arguments.
- The official skill-creator `quick_validate.py` reported `Skill is valid!` for `.agents/skills/chaos-redux-event-assets`.
- Python 3.12 `tomllib` parsed all three edited custom asset-agent TOML files successfully.
- Final path/hash proof confirms source absence, destination presence, identical SHA-256, and retained shebang.
- Final full-repository search found zero stale old-path references in skills, custom subagent definitions, or Python callers; the 18 pre-existing retained files and this migration record are classified above.

No gameplay, GFX, localisation, runtime assets, spreadsheets, Event 15 manifests/metadata, or portrait-processor behavior changed. No commit was created.

## Simplifications, omissions, and blockers

None. The requested move and active-reference migration are complete. Historical records were intentionally preserved rather than rewritten.
