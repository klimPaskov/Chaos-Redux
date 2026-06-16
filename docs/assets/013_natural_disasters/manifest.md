# Event 013 Natural Disasters Event Art Manifest

Package scope: generated report event images, generated news event images, decision icons, state-modifier idea icons, achievement icons, and super-event art for Event `013` `natural_disasters`.

Reference inspection completed:
- `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_asset_prompt.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_1.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_evolutions_and_variants.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_natural_disasters_event_log_catalog_and_localisation_map.md`
- `.agents/skills/chaos-redux-event-assets/assets/report_event_images/*`
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images/*`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/*`

DDS conversion note:
- `python3 .tools/convert_to_dds.py` failed on this repo checkout because its ffmpeg conversion path raised a `struct.pack` error while writing DDS headers.
- Final DDS files were produced with `convert -define dds:compression=none`, then verified with `file`.

Prompt log:
- `docs/assets/013_natural_disasters/prompts/generated_event_art_prompts.md`

## Report event images

All report assets:
- Asset type: report event image
- Intended in-game use: Event 013 warning, baseline, impact, recovery, and family-specific report cards
- Source mode: generated
- Era-fit note: prompted as fictional 1936-1945 documentary press scenes with period clothing, vehicles, and architecture; no readable text; no modern props
- Process workflow: generated source PNG, local report-card treatment with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`, final DDS
- Target size: `210x176`
- `.gfx` file: `interface/013_natural_disasters.gfx`
- Asset status: `handed_off`

- `report_event_natural_disaster_baseline`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_baseline_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_baseline.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_baseline.dds`
  - Sprite name: `GFX_report_event_natural_disaster_baseline`
  - Related use: baseline local-disaster report surface
- `report_event_natural_disaster_warning`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_warning_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_warning.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_warning.dds`
  - Sprite name: `GFX_report_event_natural_disaster_warning`
  - Related use: warning report surface
- `report_event_natural_disaster_impact`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_impact_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_impact.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_impact.dds`
  - Sprite name: `GFX_report_event_natural_disaster_impact`
  - Related use: peak-impact report surface
- `report_event_natural_disaster_recovery`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_recovery_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_recovery.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_recovery.dds`
  - Sprite name: `GFX_report_event_natural_disaster_recovery`
  - Related use: rebuilding and recovery report surface
- `report_event_natural_disaster_earthquake`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_earthquake_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_earthquake.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_earthquake.dds`
  - Sprite name: `GFX_report_event_natural_disaster_earthquake`
  - Related use: earthquake family report
- `report_event_natural_disaster_flood`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_flood_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_flood.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_flood.dds`
  - Sprite name: `GFX_report_event_natural_disaster_flood`
  - Related use: flood family report
- `report_event_natural_disaster_storm`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_storm_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_storm.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_storm.dds`
  - Sprite name: `GFX_report_event_natural_disaster_storm`
  - Related use: storm family report
- `report_event_natural_disaster_drought`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_drought_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_drought.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_drought.dds`
  - Sprite name: `GFX_report_event_natural_disaster_drought`
  - Related use: drought family report
- `report_event_natural_disaster_wildfire`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_wildfire_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_wildfire.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_wildfire.dds`
  - Sprite name: `GFX_report_event_natural_disaster_wildfire`
  - Related use: wildfire family report
- `report_event_natural_disaster_landslide`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_landslide_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_landslide.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_landslide.dds`
  - Sprite name: `GFX_report_event_natural_disaster_landslide`
  - Related use: landslide family report
- `report_event_natural_disaster_volcano`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_volcano_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_volcano.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_volcano.dds`
  - Sprite name: `GFX_report_event_natural_disaster_volcano`
  - Related use: volcano family report
- `report_event_natural_disaster_tsunami`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_tsunami_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_tsunami.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_tsunami.dds`
  - Sprite name: `GFX_report_event_natural_disaster_tsunami`
  - Related use: tsunami family report
- `report_event_natural_disaster_meteor`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/report_event_images/report_event_natural_disaster_meteor_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/report_event_images/report_event_natural_disaster_meteor.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_meteor.dds`
  - Sprite name: `GFX_report_event_natural_disaster_meteor`
  - Related use: meteor family report

## News event images

All news assets:
- Asset type: news event image
- Intended in-game use: Event 013 regional or evolved incident broadcast surfaces
- Source mode: generated
- Era-fit note: prompted as fictional 1936-1945 press scenes and processed to black-and-white wide news format
- Target size: `397x153`
- `.gfx` file: `interface/013_natural_disasters.gfx`
- Asset status: `handed_off`

- `news_event_regional_disaster_system`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_images/news_event_regional_disaster_system_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_images/news_event_regional_disaster_system.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/news_event_regional_disaster_system.dds`
  - Sprite name: `GFX_news_event_regional_disaster_system`
  - Related use: regional footprint incident broadcast
- `news_event_disaster_chains`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_images/news_event_disaster_chains_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_images/news_event_disaster_chains.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/news_event_disaster_chains.dds`
  - Sprite name: `GFX_news_event_disaster_chains`
  - Related use: chained aftermath broadcast
- `news_event_abnormal_disaster_age`
  - Source PNG: `docs/assets/013_natural_disasters/source_png/news_event_images/news_event_abnormal_disaster_age_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/news_event_images/news_event_abnormal_disaster_age.png`
  - Final DDS: `gfx/event_pictures/013_natural_disasters/news_event_abnormal_disaster_age.dds`
  - Sprite name: `GFX_news_event_abnormal_disaster_age`
  - Related use: abnormal earthquake-wave or meteor-era broadcast

## Super-event art

- `super_event_natural_disasters_abnormal_disaster_age`
  - Asset type: super-event image
  - Intended in-game use: Evolution IV `Abnormal Disaster Age` super-event
  - Source mode: generated
  - Source PNG: `docs/assets/013_natural_disasters/source_png/super_event_images/super_event_natural_disasters_abnormal_disaster_age_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/processed_png/super_event_images/super_event_natural_disasters_abnormal_disaster_age.png`
  - Final DDS: `gfx/super_events/super_event_natural_disasters_abnormal_disaster_age.dds`
  - Target size: `457x328`
  - Sprite name: `GFX_super_event_natural_disasters_abnormal_disaster_age`
  - `.gfx` file: `interface/chaosx_super_events.gfx`
  - Related use: Evolution IV abnormal disaster-age recognition moment
  - Notes: strong central composition with cracked earth, ash column, storm wall, meteor fragments, and ruined rail or harbor silhouettes; designed to read in the HOI4 super-event frame
  - Asset status: `wired`

## Review files

- `docs/assets/013_natural_disasters/contact_sheets/report_event_sources_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/report_event_processed_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/news_event_sources_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/news_event_processed_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/super_event_sources_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/super_event_processed_contact.png`

## Decision icons

Decision icon sources and processed PNGs live under:

- `docs/assets/013_natural_disasters/source_png/decision_*_source.png`
- `docs/assets/013_natural_disasters/processed_png/decisions/`

Final DDS files live under `gfx/interface/decisions/natural_disasters/` and are registered in `interface/013_natural_disasters.gfx`.

Registered decision sprites:

- `GFX_decision_category_disaster_response_office`
- `GFX_decision_preposition_relief_trains`
- `GFX_decision_evacuate_industrial_districts`
- `GFX_decision_reinforce_flood_barriers`
- `GFX_decision_close_vulnerable_ports`
- `GFX_decision_dispatch_emergency_engineers`
- `GFX_decision_send_medical_columns`
- `GFX_decision_emergency_railway_repair`
- `GFX_decision_firebreak_mobilisation`
- `GFX_decision_shoreline_rescue`
- `GFX_decision_ash_clearance_crews`
- `GFX_decision_survey_crater_belt`
- `GFX_decision_joint_river_commission`

## State-modifier idea icons

Idea icon sources and processed PNGs live under:

- `docs/assets/013_natural_disasters/processed_png/ideas/`

Final DDS files live under `gfx/interface/ideas/natural_disasters/` and are registered in `interface/013_natural_disasters.gfx`.

Registered idea sprites:

- `GFX_idea_recent_earthquake_damage`
- `GFX_idea_flooded_transport_belt`
- `GFX_idea_crop_failure_pressure`
- `GFX_idea_storm_wreckage`
- `GFX_idea_burned_districts`
- `GFX_idea_unstable_mountain_passes`
- `GFX_idea_volcanic_ashfall`
- `GFX_idea_tsunami_scoured_coast`
- `GFX_idea_meteor_scars`
- `GFX_idea_disaster_recovery_pressure`

## Achievement icons

Achievement icon sources, processed PNGs, contact sheet, and final DDS handoff are recorded in:

- `docs/assets/013_natural_disasters/achievement_icons/manifest.md`
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/20260616T154424Z_achievement_icons_local_handoff.md`

Final DDS files live under `gfx/achievements/` and are registered in `interface/chaosx_achievements.gfx`.
