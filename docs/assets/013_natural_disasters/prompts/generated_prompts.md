# Event 013 Natural Disasters Generated Prompt Log

## Decision Icons

Decision icons were generated as individual `image_gen` assets, then chroma-keyed or alpha-cleaned for `32x32` decision DDS output. They are not resized focus icons.

- `decision_nd_evacuate_shelter_source`: shelter sign, evacuation arrows, field bedding, compact HOI4 decision icon, no text.
- `decision_nd_rescue_columns_source`: rescue trucks and stretcher column, compact HOI4 decision icon, no text.
- `decision_nd_field_hospitals_source`: medical tent, stretcher, lamp, compact HOI4 decision icon, no text.
- `decision_nd_repair_rail_source`: damaged rail, wrench, bridge timber, compact HOI4 decision icon, no text.
- `decision_nd_restore_supply_source`: crates, depot marker, supply truck, compact HOI4 decision icon, no text.
- `decision_nd_clear_debris_source`: shovel, rubble, broken masonry, compact HOI4 decision icon, no text.
- `decision_nd_rebuild_ports_source`: pier crane, mooring post, repair planks, compact HOI4 decision icon, no text.
- `decision_nd_firefighting_source`: firebreak tools, hose, smoke glow, compact HOI4 decision icon, no text.
- `decision_nd_water_rationing_source`: water tins, ration token, hand pump, compact HOI4 decision icon, no text.
- `decision_nd_heat_shelters_source`: shaded shelter, water station, heat shimmer, compact HOI4 decision icon, no text.
- `decision_nd_winter_convoys_source`: snow convoy, fuel drum, rail lantern, compact HOI4 decision icon, no text.
- `decision_nd_dust_masks_source`: respirator masks, dust goggles, covered crate, compact HOI4 decision icon, no text.
- `decision_nd_seismology_teams_source`: seismograph drum, cracked ground marker, field case, compact HOI4 decision icon, no text.
- `decision_nd_lava_diversion_source`: lava trench, sandbags, engineer tools, compact HOI4 decision icon, no text.
- `decision_nd_meteor_crater_cordon_source`: crater cordon, warning stakes, observer kit, compact HOI4 decision icon, no text.
- `decision_nd_international_relief_source`: relief crates, rail stamp, convoy papers, compact HOI4 decision icon, no text.
- `decision_nd_barrage_launch_controls_source`: control levers, disaster-map markers, warning lamp, compact HOI4 decision icon, no text.

## Decision Category Icons

Decision category icons were generated through `image_gen` as family-specific disaster emblems on chroma-key backgrounds. The current processed icons remove chroma green and use non-square `53x40` canvases for category button art. They are separate from category pictures.

## Decision Category Pictures

Decision category pictures use existing generated Event 13 report-image sources. The processed outputs are report-card-style `114x101` category pictures, wired through `picture = GFX_decision_cat_picture_nd_*` in the decision category definitions.

## Achievement Sheets

### `nd_achievement_sheet_a_source`
- Prepared capital, no deaths sequence, tame the barrage, firebreak master.
- Direction: painted HOI4 achievement art with integrated bronze laurel frame, `2x2` grid.

### `nd_achievement_sheet_b_source`
- Aftershock control, skyfall survivor, global relief, no world end.
- Direction: painted HOI4 achievement art with integrated bronze laurel frame, `2x2` grid.

## Animation Sheets

### `natural_disaster_warning_pulse_source_sheet`
- Eight-frame `4x2` warning pulse sequence.
- Direction: shield, warning lamp, and hazard sign moving from dim rest to peak alert and back.

### `natural_disaster_storm_corridor_track_source_sheet`
- Eight-frame `4x2` storm corridor sequence.
- Direction: moving storm spiral crossing a forecast route on a map plaque.

### `natural_disaster_skyfall_alarm_source_sheet`
- Eight-frame `4x2` skyfall alarm sequence.
- Direction: shelter arch, alarm beacon, and advancing meteor streaks.

### `natural_disaster_tsunami_countdown_source_sheet`
- Eight-frame `4x2` tsunami countdown sequence.
- Direction: wave band advancing toward a coastal beacon and high-ground marker.

### `natural_disaster_eruption_ashfall_source_sheet`
- Eight-frame `4x2` eruption ashfall sequence.
- Direction: volcanic plume and ash spread rising to peak and easing back into loop.
