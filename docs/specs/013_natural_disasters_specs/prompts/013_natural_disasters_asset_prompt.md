# Asset Prompt — Event 013 Natural Disasters

Use `chaos-redux-event-assets` and, where animation is requested, `chaos-redux-frame-animation`. Use the correct narrow asset subagent for each item: `chaosx_icon_artist` for icons and small animated icon sprites, `chaosx_generated_event_art` for fictional/alternate/high-chaos event art and UI panels, and `chaosx_asset_source_researcher` for archival/source-based disaster images if a real historical source is chosen.

## Reference folders to inspect first

- Ideas/national spirits: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`
- Decision icons and category icons: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`
- Report event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- News event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- Super-event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- Achievement icons: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`

## Source-mode rules

- Generated art is preferred for fictional, symbolic, high-chaos, meteor-shower, abnormal earthquake-wave, massive volcano, and disaster-ledger UI art.
- Sourced/archival images may be used for grounded report/news images if the source, date, license, and era fit are clear.
- Do not use generated art for real historical photos or real people.
- Report images must use the report-card processing workflow and final 210x176 size.
- News images must be black-and-white and final 397x153 size.
- Super-event images are 457x328.
- Decision icons are 32x32, idea/national spirit icons 64x64, achievement icons 64x64.

## Required icon family

### Decision category icon

- **Asset:** `decision_category_disaster_response_office`
- **Type:** decision category icon
- **Size:** follow existing category pattern after inspection
- **Visual direction:** emergency command desk with cracked map, telephone, warning stamp, and engineer tools; no readable text.
- **Sprite suggestion:** `GFX_decision_category_disaster_response_office`

### Decision icons

| Asset | Size | Direction |
| --- | --- | --- |
| `decision_preposition_relief_trains` | 32x32 | small train/rail relief symbol with crate/medical cross-like shape, no text |
| `decision_evacuate_industrial_districts` | 32x32 | factory silhouette with arrows moving workers away |
| `decision_reinforce_flood_barriers` | 32x32 | sandbags/pump/water line |
| `decision_close_vulnerable_ports` | 32x32 | port anchor/closed harbour gate, no lettering |
| `decision_dispatch_emergency_engineers` | 32x32 | wrench, helmet, broken beam |
| `decision_send_medical_columns` | 32x32 | field tent/ambulance-style symbol, period appropriate |
| `decision_emergency_railway_repair` | 32x32 | broken track being bridged |
| `decision_firebreak_mobilisation` | 32x32 | firebreak line and shovel/helmet |
| `decision_ash_clearance_crews` | 32x32 | ash cloud over shovel/airfield marker |
| `decision_shoreline_rescue` | 32x32 | lifeboat/rope/wave |
| `decision_survey_crater_belt` | 32x32 | crater with survey flags, no text |
| `decision_joint_river_commission` | 32x32 | river bridge with two hands/tools, diplomatic relief tone |

### Idea and state modifier icons

| Asset | Size | Direction |
| --- | --- | --- |
| `idea_recent_earthquake_damage` | 64x64 | cracked factory and fault line |
| `idea_flooded_transport_belt` | 64x64 | submerged rails/bridge |
| `idea_crop_failure_pressure` | 64x64 | dry field, empty grain sack |
| `idea_storm_wreckage` | 64x64 | shattered port/airfield in storm wind |
| `idea_burned_districts` | 64x64 | burned street/factory silhouette |
| `idea_unstable_mountain_passes` | 64x64 | blocked mountain road and fallen rocks |
| `idea_volcanic_ashfall` | 64x64 | ash cloud over buildings/fields |
| `idea_tsunami_scoured_coast` | 64x64 | broken harbour and receding wave |
| `idea_meteor_scars` | 64x64 | crater field and burning fragments |
| `idea_disaster_recovery_pressure` | 64x64 | ledger, stretcher, and construction crane motif |

## Report event image package

Create one grounded/generated documentary-style report image per family. Final 210x176 with report-card treatment.

| Asset | Direction | Source mode |
| --- | --- | --- |
| `report_event_natural_disaster_earthquake` | collapsed factory district, rescue workers, 1930s/40s documentary feel | generated or sourced |
| `report_event_natural_disaster_flood` | flooded railway/industrial street | generated or sourced |
| `report_event_natural_disaster_storm` | damaged harbour after cyclone/blizzard/storm | generated or sourced |
| `report_event_natural_disaster_drought` | cracked fields, ration queue/grain office | generated or sourced |
| `report_event_natural_disaster_wildfire` | smoke over factory/forest edge | generated |
| `report_event_natural_disaster_landslide` | mountain rail line buried by rocks | generated |
| `report_event_natural_disaster_volcano` | ashfall on town/airfield | generated |
| `report_event_natural_disaster_tsunami` | damaged coast/boats inland, no modern props | generated |
| `report_event_natural_disaster_meteor` | cratered district under smoky sky, period documentary | generated |

## News images

Use news images only for regional/evolved incidents that deserve wider broadcast.

| Asset | Size | Direction |
| --- | --- | --- |
| `news_event_regional_disaster_system` | 397x153 B/W | several railway/port/city reports represented as a period press panorama, no text |
| `news_event_disaster_chains` | 397x153 B/W | refugees and damaged infrastructure after flood/earthquake chain |
| `news_event_abnormal_disaster_age` | 397x153 B/W | skyfall/ash/earthquake reports as global press scene, no readable headlines |

## Super-event image direction

One generated super-event image if the Evolution IV super-event is implemented:

- **Asset:** `super_event_natural_disasters_abnormal_disaster_age`
- **Size:** 457x328
- **Source mode:** generated
- **Direction:** strong central composition: several disaster forces visible without becoming a collage — cracked earth, ash column, storm wall, burning meteor fragments, ruined rail/port silhouettes; 1936–1945 documentary/painted super-event style; no readable text; ominous but not world-ending.
- **Sprite suggestion:** `GFX_super_event_natural_disasters_abnormal_disaster_age`

## Scripted GUI / animated assets

If the Disaster Ledger GUI is implemented, create:

| Asset | Type | Size | State logic |
| --- | --- | --- | --- |
| `disaster_ledger_panel` | UI panel | implementation-defined | static background for active disaster list |
| `disaster_warning_pulse` | animated warning icon | 32x32 or GUI pattern | appears when warning phase is active |
| `disaster_selected_state_glow` | animated card overlay | GUI card size | selected affected state/region |
| `disaster_chain_warning_frame` | animated warning frame | GUI card size | follow-up chain is near |
| `disaster_meteor_skyfall_marker` | animated marker | 32x32 or state-card size | Evolution IV meteor/crater active |
| `disaster_volcanic_ash_marker` | animated marker | 32x32 or state-card size | volcanic ash/eruption active |

Animation requirements:

- real source frames for every animated state;
- static fallback DDS for every animated sprite;
- horizontal frame sheet DDS;
- GIF preview for review only;
- manifest entries with frame count, frame timing, target size, and state logic;
- `gfx_handoff.md` with sprite names and suggested `.gfx` target.

## Achievement icons

Create completed 64x64 icons for every achievement in `013_natural_disasters_achievement_prompt.md`. Grey and not-eligible variants should follow the project achievement workflow.

Priority motifs:

- relief train in flood water;
- cracked factory repaired by engineers;
- meteor crater with a surviving capital silhouette;
- volcano ash cleared from an airfield;
- drought grain sacks and railway map;
- warning siren/bell over a coast;
- tornado/storm path with intact rail line;
- global disaster ledger stamp with no readable text.

## Manifest and handoff

Write or update:

- `docs/assets/013_natural_disasters/manifest.md`
- `docs/assets/013_natural_disasters/gfx_handoff.md`

For every asset, record source mode, prompt or source URL, source file, processed PNG, final DDS, target size, sprite name, intended in-game use, and status.
