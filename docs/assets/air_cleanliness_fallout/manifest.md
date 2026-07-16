# Air Cleanliness and Fallout Asset Manifest

Status: active implementation manifest. Only reviewed assets with final wiring are listed as complete.

## Ownership

All assets in this package use Air Cleanliness or Fallout-owned filenames and paths. Zombie event images, sprites, audio, filenames, and directories are not source material for this package.

## Completed Air Winter UI assets

| Asset | Source PNG | Processed PNG | Final DDS | Sprite | Size | Source mode |
| --- | --- | --- | --- | --- | --- | --- |
| Air Winter mapmode selected | `source_png/mapmode/air_winter_state_map_mode_selected.png` | `processed_png/mapmode/air_winter_state_map_mode_selected.png` | `gfx/interface/mapmode/custom/air_winter_state_map_mode_selected.dds` | `GFX_mapmode_buttons_selected_small_air_winter_state_map_mode` | 20x18 | Hand-authored geometric UI art |
| Air Winter mapmode deselected | `source_png/mapmode/air_winter_state_map_mode_deselected.png` | `processed_png/mapmode/air_winter_state_map_mode_deselected.png` | `gfx/interface/mapmode/custom/air_winter_state_map_mode_deselected.dds` | `GFX_mapmode_buttons_deselected_small_air_winter_state_map_mode` | 20x18 | Hand-authored geometric UI art |
| Winter Exposure mapmode selected | `source_png/mapmode/air_winter_exposure_map_mode_selected.png` | `processed_png/mapmode/air_winter_exposure_map_mode_selected.png` | `gfx/interface/mapmode/custom/air_winter_exposure_map_mode_selected.dds` | `GFX_mapmode_buttons_selected_small_air_winter_exposure_map_mode` | 20x18 | Hand-authored geometric UI art |
| Winter Exposure mapmode deselected | `source_png/mapmode/air_winter_exposure_map_mode_deselected.png` | `processed_png/mapmode/air_winter_exposure_map_mode_deselected.png` | `gfx/interface/mapmode/custom/air_winter_exposure_map_mode_deselected.dds` | `GFX_mapmode_buttons_deselected_small_air_winter_exposure_map_mode` | 20x18 | Hand-authored geometric UI art |
| Winter Survival mapmode selected | `source_png/mapmode/air_winter_survival_map_mode_selected.png` | `processed_png/mapmode/air_winter_survival_map_mode_selected.png` | `gfx/interface/mapmode/custom/air_winter_survival_map_mode_selected.dds` | `GFX_mapmode_buttons_selected_small_air_winter_survival_map_mode` | 20x18 | Hand-authored geometric UI art |
| Winter Survival mapmode deselected | `source_png/mapmode/air_winter_survival_map_mode_deselected.png` | `processed_png/mapmode/air_winter_survival_map_mode_deselected.png` | `gfx/interface/mapmode/custom/air_winter_survival_map_mode_deselected.dds` | `GFX_mapmode_buttons_deselected_small_air_winter_survival_map_mode` | 20x18 | Hand-authored geometric UI art |

The selected and deselected sprites use the existing Chaos Redux small-mapmode dimensions and 32-bit RGBA DDS format. The phase view uses a snowflake and dim-sky disc. The exposure view uses a sealed filter shield surrounded by cold air and falling ash. The survival view uses a shelter, seedling, and water line. These shapes distinguish the three state views from the radiation and Deaths mapmodes. The six native-size review sprites are recorded together in `processed_png/mapmode/air_winter_mapmode_contact_sheet.png`.

## Technical proof material

`gfx/entities/air_cleanliness_winter_proof.asset` references the vanilla `snow_small_particle` only as retired technical proof material. Its monthly creation call has been removed. Global visual migration and reset retain a literal destroy for the former state-64 entity id.

`gfx/interface/air_cleanliness_winter/proof/air_winter_cold_grade_proof.dds` is a hand-authored translucent RGBA test texture consumed by `air_winter_normal_map_grade_proof_gui`. Its source and processed PNGs live under `source_png/gui/` and `processed_png/gui/`. It is proof material only. The map-layer parent, interface ordering, click-through behavior, supported resolutions, and removal behavior must pass review before a final atmospheric-grade family is created.

## Regional ordinary-map climate package

The dedicated regional package is recorded in `regional_map_visuals/manifest.md` and `regional_map_visuals/handoff.md`. It contains 181 final DDS files, 85 custom PDX meshes, 54 class-and-phase ground plates, 27 regional prop sets, nine particle severities built from 16 separately authored source frames, eight atmospheric grade plates, and four static accessibility alternatives.

The synchronized gameplay route creates five deterministic slots per state from the existing monthly state pass. It retains separate primary and secondary particle channels, so snow or cold rain can coexist with ash. The hydrology slot displays frozen water or class-specific recovery thaw, never both. Tropical, equatorial, desert, and oceanic classes retain their own rain, ash, frost, ground, and runoff identities rather than receiving universal snow.

The full-screen grade and static accessibility setting remain unwired. Runtime placement, draw order, particle playback, save reconstruction, multiplayer behavior, and world-scale performance have not been observed because HOI4 was not launched.

## Air Winter report-event image package

These seven report-event images are fictional period-documentary scenes generated with the built-in `$imagegen` workflow. Generation was selected because the Air Winter progression is fictional, while a geographically varied documentary anthology communicates the world-scale climate collapse better than reusing one archive photograph. No real person, named historical incident, or archival collection is represented.

All source PNGs are distinct 1536x1024 renders. Every processed PNG and final DDS is 210x176. The repository report-event processor applies grayscale conversion, sepia tone, grain, a four-degree card tilt, transparent edge space, and a soft shadow. Runtime DDS files are uncompressed one-image-level 32-bit BGRA with full 8-bit alpha.

| Asset | Related events | Regional visual identity | Source mode | Source PNG | Processed PNG | Final DDS | Sprite | Target `.gfx` | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Air Winter phase 1 | `chaosx.fallout.1` through `chaosx.fallout.5` | Norwegian coastal village under dim first-stage cold | Built-in `$imagegen`, fictional period documentary | `source_png/report_events/report_event_air_winter_phase_1_source.png` | `processed_png/report_events/report_event_air_winter_phase_1.png` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_1.dds` | `GFX_report_event_air_winter_phase_1` | `interface/air_cleanliness_winter.gfx` | `registered` |
| Air Winter phase 2 | `chaosx.fallout.10` through `chaosx.fallout.18` | Bengal delta crop shock under impossible cold rain | Built-in `$imagegen`, fictional period documentary | `source_png/report_events/report_event_air_winter_phase_2_source.png` | `processed_png/report_events/report_event_air_winter_phase_2.png` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_2.dds` | `GFX_report_event_air_winter_phase_2` | `interface/air_cleanliness_winter.gfx` | `registered` |
| Air Winter phase 3 | `chaosx.fallout.20` through `chaosx.fallout.29`, plus `chaosx.fallout.36` and `chaosx.fallout.37` | Canadian prairie freight line locked by hard freeze | Built-in `$imagegen`, fictional period documentary | `source_png/report_events/report_event_air_winter_phase_3_source.png` | `processed_png/report_events/report_event_air_winter_phase_3.png` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_3.dds` | `GFX_report_event_air_winter_phase_3` | `interface/air_cleanliness_winter.gfx` | `registered` |
| Air Winter phase 4 | `chaosx.fallout.30` through `chaosx.fallout.35` | Greek black harvest and dead olive country | Built-in `$imagegen`, fictional period documentary | `source_png/report_events/report_event_air_winter_phase_4_source.png` | `processed_png/report_events/report_event_air_winter_phase_4.png` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_4.dds` | `GFX_report_event_air_winter_phase_4` | `interface/air_cleanliness_winter.gfx` | `registered` |
| Air Winter phase 5 | `chaosx.fallout.40`, `chaosx.fallout.41`, `chaosx.fallout.42`, `chaosx.fallout.44`, `chaosx.fallout.45`, `chaosx.fallout.60`, `chaosx.fallout.61`, `chaosx.fallout.201`, and `chaosx.fallout.202` | Lower Yangtze river town with ash-flecked frozen water | Built-in `$imagegen`, fictional period documentary | `source_png/report_events/report_event_air_winter_phase_5_source.png` | `processed_png/report_events/report_event_air_winter_phase_5.png` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_5.dds` | `GFX_report_event_air_winter_phase_5` | `interface/air_cleanliness_winter.gfx` | `registered` |
| Air Winter phase 6 | `chaosx.fallout.43` and `chaosx.fallout.46` | Terminally dim Central Asian oasis settlement | Built-in `$imagegen`, fictional period documentary | `source_png/report_events/report_event_air_winter_phase_6_source.png` | `processed_png/report_events/report_event_air_winter_phase_6.png` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_6.dds` | `GFX_report_event_air_winter_phase_6` | `interface/air_cleanliness_winter.gfx` | `registered` |
| Air Winter recovery | `chaosx.fallout.50` and `chaosx.fallout.51` | Andean thaw, restored meltwater, and recovering soil | Built-in `$imagegen`, fictional period documentary | `source_png/report_events/report_event_air_winter_recovery_source.png` | `processed_png/report_events/report_event_air_winter_recovery.png` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_recovery.dds` | `GFX_report_event_air_winter_recovery` | `interface/air_cleanliness_winter.gfx` | `registered` |

The final DDS decode contact sheet is `contact_sheets/air_winter_report_events_final_contact_sheet.png`.

The Phase 3 furnace opening and result reuse this dedicated registered report asset. The heavy-industry tranche creates no new report image, sprite, audio, source PNG, processed PNG, DDS, or runtime path.

### Image generation prompts

#### Air Winter phase 1

```text
Use case: historical-scene
Asset type: fictional Hearts of Iron IV report-event source photograph
Primary request: a remote Norwegian coastal village in the early 1940s struck by an unnatural early cold during a dim midday
Scene/backdrop: timber houses, a small fishing jetty, dark calm sea, thin new ice around pilings, frost whitening nets and roofs, low cloud and a muted sun behind dense atmospheric haze
Subject: two period-dressed fishing families examining frost-stiffened nets while the harbor and village recede into the dim cold
Style/medium: photorealistic period documentary photograph made with 1936 to 1945 photographic technology, authentic 35mm black-and-white field photography, natural grain, modest dynamic range
Composition/framing: landscape 3:2 mid-wide view, clear central human activity, layered regional setting, important subjects kept away from extreme edges for a later 4:3 cover crop, no decorative border
Lighting/mood: weak midday light, uneasy first-stage cold, subtle rime rather than a full blizzard
Constraints: fictional people only, period-accurate clothing and architecture, physically plausible weather, no readable text, no signage, no watermark, no colorized treatment, no modern objects, no UI, no map, no split panel, no collage, no frame, no card treatment, no supernatural creatures
```

#### Air Winter phase 2

```text
Use case: historical-scene
Asset type: fictional Hearts of Iron IV report-event source photograph
Primary request: crop shock in a Bengal delta farming village during an impossible cold rain in the early 1940s
Scene/backdrop: waterlogged rice paddies, flattened pale stalks, flooded earthen paths, thatched farm buildings beneath low rain clouds
Subject: several period-dressed farming families standing knee-deep at the edge of a ruined paddy, examining frost-burned rice while cold rain falls
Style/medium: photorealistic period documentary photograph made with 1936 to 1945 photographic technology, authentic black-and-white press photography, natural grain, modest dynamic range
Composition/framing: landscape 3:2 mid-wide view, ruined crop and people both clearly readable, important subjects kept away from extreme edges for a later 4:3 cover crop, no decorative border
Lighting/mood: overcast cold rain, shock and disbelief, wet textures, visibly tropical region subjected to unseasonable cold
Constraints: fictional people only, period-accurate rural clothing and architecture, respectful documentary realism, no readable text, no signage, no watermark, no modern objects, no UI, no map, no split panel, no collage, no frame, no card treatment, no supernatural creatures
```

#### Air Winter phase 3

```text
Use case: historical-scene
Asset type: fictional Hearts of Iron IV report-event source photograph
Primary request: a Canadian prairie freight train immobilized by a severe hard freeze in the early 1940s
Scene/backdrop: open prairie rail line, a small wooden signal hut, telegraph poles, freight cars and a steam locomotive half buried in wind-packed snow and glaze ice
Subject: period railway workers using bars and shovels to break thick ice from a frozen track switch and locomotive running gear
Style/medium: photorealistic period documentary photograph made with 1936 to 1945 photographic technology, authentic black-and-white field photography, natural grain, modest dynamic range
Composition/framing: landscape 3:2 low mid-wide view, frozen switch and locomotive form the central story, strong rail perspective, important subjects kept away from extreme edges for a later 4:3 cover crop, no decorative border
Lighting/mood: hard white cold, blowing snow, mechanical paralysis, severe but physically plausible winter conditions
Constraints: fictional workers only, accurate early 1940s locomotive and work clothing, no readable locomotive numbers, no readable text, no signage, no watermark, no modern objects, no UI, no map, no split panel, no collage, no frame, no card treatment, no supernatural creatures
```

#### Air Winter phase 4

```text
Use case: historical-scene
Asset type: fictional Hearts of Iron IV report-event source photograph
Primary request: the black harvest in a Greek agricultural valley during an unnatural ash winter in the early 1940s
Scene/backdrop: blackened wheat stubble, collapsed dark sheaves, leafless olive trees, low stone farm walls, distant whitewashed hillside village under a soot-heavy sky
Subject: period-dressed farmers beside a wooden donkey cart, holding crumbling black grain and dead olive branches while surveying the failed harvest
Style/medium: photorealistic period documentary photograph made with 1936 to 1945 photographic technology, authentic black-and-white rural press photography, natural grain, modest dynamic range
Composition/framing: landscape 3:2 mid-wide view, ruined vegetation dominates the foreground while people anchor the scene, important subjects kept away from extreme edges for a later 4:3 cover crop, no decorative border
Lighting/mood: dull ash-filtered daylight, severe agricultural loss, dry black residue rather than ordinary snowfall
Constraints: fictional people only, period-accurate Mediterranean clothing and farm tools, no fire, no readable text, no signage, no watermark, no modern objects, no UI, no map, no split panel, no collage, no frame, no card treatment, no supernatural creatures
```

#### Air Winter phase 5

```text
Use case: historical-scene
Asset type: fictional Hearts of Iron IV report-event source photograph
Primary request: ash winter and frozen water at a lower Yangtze river town in the early 1940s
Scene/backdrop: wooden river boats and small cargo junks locked into thick dark-flecked ice, ash-covered tiled roofs, bare waterside trees, a river landing beneath a low soot sky
Subject: period-dressed boat workers and residents crossing the frozen landing with poles and buckets while fine ash settles across the ice
Style/medium: photorealistic period documentary photograph made with 1936 to 1945 photographic technology, authentic black-and-white press photography, natural grain, modest dynamic range
Composition/framing: landscape 3:2 mid-wide riverfront view, frozen boats and black-flecked water dominate the scene, people provide scale, important subjects kept away from extreme edges for a later 4:3 cover crop, no decorative border
Lighting/mood: weak ash-filtered daylight, deep cold, immobilized waterborne life, severe fifth-stage winter
Constraints: fictional people only, period-accurate clothing, boats and architecture, ash must read as dirty particulate rather than ordinary snow, no readable text, no signage, no watermark, no modern objects, no UI, no map, no split panel, no collage, no frame, no card treatment, no supernatural creatures
```

#### Air Winter phase 6

```text
Use case: historical-scene
Asset type: fictional Hearts of Iron IV report-event source photograph
Primary request: a terminally dim Central Asian oasis settlement under an extreme air winter in the early 1940s
Scene/backdrop: adobe homes and a nearly empty market lane, deep dirty snow against walls, a frozen communal well, bare poplars, shutters closed beneath a noon sky as dark as dusk
Subject: a small group of heavily bundled residents clustered around the frozen well while the rest of the settlement appears silent and abandoned
Style/medium: photorealistic period documentary photograph made with 1936 to 1945 photographic technology, authentic black-and-white field photography, natural grain, modest dynamic range
Composition/framing: landscape 3:2 mid-wide street view, the frozen well and surviving residents form the central focus, empty buildings convey terminal settlement failure, important subjects kept away from extreme edges for a later 4:3 cover crop, no decorative border
Lighting/mood: oppressive dim noon, near-total atmospheric darkening, exhausted human endurance, terminal sixth-stage cold without graphic suffering
Constraints: fictional people only, period-accurate clothing and architecture, no electric neon, no readable text, no signage, no watermark, no modern objects, no UI, no map, no split panel, no collage, no frame, no card treatment, no supernatural creatures
```

#### Air Winter recovery

```text
Use case: historical-scene
Asset type: fictional Hearts of Iron IV report-event source photograph
Primary request: the first recovery thaw in an Andean highland village in the early 1940s
Scene/backdrop: adobe houses and stone terraces, snow retreating into muddy banks, meltwater running through an irrigation channel, low clouds breaking over distant mountains, a few first green shoots
Subject: period-dressed village families clearing slush and debris from the channel while a farmer kneels to inspect wet living soil
Style/medium: photorealistic period documentary photograph made with 1936 to 1945 photographic technology, authentic black-and-white field photography, natural grain, modest dynamic range
Composition/framing: landscape 3:2 mid-wide view, flowing meltwater leads toward the people and recovering terraces, important subjects kept away from extreme edges for a later 4:3 cover crop, no decorative border
Lighting/mood: cautious brighter light after prolonged dimness, muddy thaw, communal repair, restrained hope rather than triumph
Constraints: fictional people only, period-accurate Andean clothing and architecture, recovery must be visible through water and emerging soil, no readable text, no signage, no watermark, no modern objects, no UI, no map, no split panel, no collage, no frame, no card treatment, no supernatural creatures
```

## Air Winter decision icon package

The response category and its eighteen decisions use nineteen separately generated fictional pictograms. Every raw source came from one independent built-in `$imagegen` call with no reference image and no reuse of another generated icon. The complete shared prompt contract, the response-priority standalone prompt, and all asset-specific prompt blocks are preserved in `prompts/air_winter_decision_icons.md`.

The raw 1254x1254 RGB chroma-key sources remain editable evidence under `source_png/decisions/`. Transparent 1254x1254 RGBA masters were made with the canonical imagegen helper `remove_chroma_key.py` using `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`. `_tooling/process_air_winter_decision_icons.py` performs the deterministic trim, centered native-size fit, restrained outline and shadow, approved DirectXTex conversion, DDS decode, and package validation. No conversion fallback was used.

| Asset | Related consumer | Visual identity | Source mode | Prompt | Source PNG | Transparent master | Processed PNG | Final DDS | Sprite | Size | Target `.gfx` | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Air Winter response category | `air_winter_response_category` | Riveted civil-defence shield, eclipsed black sun, snow and ash rim | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#response-category) | `source_png/decisions/decision_air_winter_response_category_source.png` | `source_png/decisions/transparent_master/decision_air_winter_response_category_master.png` | `processed_png/decisions/decision_air_winter_response_category.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_response_category.dds` | `GFX_decision_air_winter_response_category` | 52x40 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Designate response priority | `air_winter_designate_response_priority` | Abstract civil-defence map board with one central state area highlighted and pinned | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#response-priority) | `source_png/decisions/decision_air_winter_response_priority_source.png` | `source_png/decisions/transparent_master/decision_air_winter_response_priority_master.png` | `processed_png/decisions/decision_air_winter_response_priority.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_response_priority.dds` | `GFX_decision_air_winter_response_priority` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Designate reception state | `air_winter_designate_reception_state` | Open concrete shelter, warm doorway, bedding and supplies | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#reception-state) | `source_png/decisions/decision_air_winter_reception_source.png` | `source_png/decisions/transparent_master/decision_air_winter_reception_master.png` | `processed_png/decisions/decision_air_winter_reception.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_reception.dds` | `GFX_decision_air_winter_reception` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Distribute respirator kits | `air_winter_distribute_respirator_kits` | Civilian cloth respirator, charcoal filters and replacement strap | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#respirator-kits) | `source_png/decisions/decision_air_winter_respirators_source.png` | `source_png/decisions/transparent_master/decision_air_winter_respirators_master.png` | `processed_png/decisions/decision_air_winter_respirators.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_respirators.dds` | `GFX_decision_air_winter_respirators` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Convert respiratory clinics | `air_winter_convert_respiratory_clinics` | Period oxygen cylinders, hose, mask and enamel medical cross | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#respiratory-clinics) | `source_png/decisions/decision_air_winter_clinics_source.png` | `source_png/decisions/transparent_master/decision_air_winter_clinics_master.png` | `processed_png/decisions/decision_air_winter_clinics.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_clinics.dds` | `GFX_decision_air_winter_clinics` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Station roof samplers | `air_winter_station_roof_samplers` | Tripod ash funnel, specimen jar and wind vane | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#roof-samplers) | `source_png/decisions/decision_air_winter_samplers_source.png` | `source_png/decisions/transparent_master/decision_air_winter_samplers_master.png` | `processed_png/decisions/decision_air_winter_samplers.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_samplers.dds` | `GFX_decision_air_winter_samplers` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Protect crop trials | `air_winter_protect_crop_trials` | Living seedling protected by a frosted glass cloche | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#crop-trials) | `source_png/decisions/decision_air_winter_crop_trials_source.png` | `source_png/decisions/transparent_master/decision_air_winter_crop_trials_master.png` | `processed_png/decisions/decision_air_winter_crop_trials.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_crop_trials.dds` | `GFX_decision_air_winter_crop_trials` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Clear ash routes | `air_winter_clear_ash_routes` | Road-plough blade displacing a ridge of black ash | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#ash-route-clearance) | `source_png/decisions/decision_air_winter_ash_clearance_source.png` | `source_png/decisions/transparent_master/decision_air_winter_ash_clearance_master.png` | `processed_png/decisions/decision_air_winter_ash_clearance.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_ash_clearance.dds` | `GFX_decision_air_winter_ash_clearance` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Protect rail corridors | `air_winter_protect_rail_corridors` | Rails and driving wheel beneath a riveted protective arch | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#rail-corridors) | `source_png/decisions/decision_air_winter_rail_corridors_source.png` | `source_png/decisions/transparent_master/decision_air_winter_rail_corridors_master.png` | `processed_png/decisions/decision_air_winter_rail_corridors.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_rail_corridors.dds` | `GFX_decision_air_winter_rail_corridors` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Close exposed airfields | `air_winter_close_exposed_airfields` | Propeller behind crossed barriers, chain and padlock | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#airfield-closure) | `source_png/decisions/decision_air_winter_airfield_closure_source.png` | `source_png/decisions/transparent_master/decision_air_winter_airfield_closure_master.png` | `processed_png/decisions/decision_air_winter_airfield_closure.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_airfield_closure.dds` | `GFX_decision_air_winter_airfield_closure` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Prepare evacuation ledger | `air_winter_prepare_evacuation_ledger` | Blank ruled ledger, pencil and luggage tag | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#evacuation-ledger) | `source_png/decisions/decision_air_winter_evacuation_ledger_source.png` | `source_png/decisions/transparent_master/decision_air_winter_evacuation_ledger_master.png` | `processed_png/decisions/decision_air_winter_evacuation_ledger.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_evacuation_ledger.dds` | `GFX_decision_air_winter_evacuation_ledger` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Enact emergency shelter law | `air_winter_enact_emergency_shelter_law` | Gavel striking a reinforced shelter emblem | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#emergency-shelter-law) | `source_png/decisions/decision_air_winter_shelter_law_source.png` | `source_png/decisions/transparent_master/decision_air_winter_shelter_law_master.png` | `processed_png/decisions/decision_air_winter_shelter_law.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_shelter_law.dds` | `GFX_decision_air_winter_shelter_law` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Convert greenhouse refuge | `air_winter_convert_greenhouse_refuge` | Frosted greenhouse with warm doorway and living plant | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#greenhouse-refuge) | `source_png/decisions/decision_air_winter_greenhouse_refuge_source.png` | `source_png/decisions/transparent_master/decision_air_winter_greenhouse_refuge_master.png` | `processed_png/decisions/decision_air_winter_greenhouse_refuge.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_greenhouse_refuge.dds` | `GFX_decision_air_winter_greenhouse_refuge` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Controlled evacuation | `air_winter_controlled_evacuation` | Period bus with open door and orderly civilian queue | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#controlled-evacuation) | `source_png/decisions/decision_air_winter_controlled_evacuation_source.png` | `source_png/decisions/transparent_master/decision_air_winter_controlled_evacuation_master.png` | `processed_png/decisions/decision_air_winter_controlled_evacuation.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_controlled_evacuation.dds` | `GFX_decision_air_winter_controlled_evacuation` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| State medical triage | `air_winter_state_medical_triage` | Three blank colour-tab triage tags, bandage and medical cross | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#medical-triage) | `source_png/decisions/decision_air_winter_medical_triage_source.png` | `source_png/decisions/transparent_master/decision_air_winter_medical_triage_master.png` | `processed_png/decisions/decision_air_winter_medical_triage.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_medical_triage.dds` | `GFX_decision_air_winter_medical_triage` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Hold abandonment vote | `air_winter_hold_abandonment_vote` | Ballot box, blank ballot and cracked-house emblem | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#abandonment-vote) | `source_png/decisions/decision_air_winter_abandonment_vote_source.png` | `source_png/decisions/transparent_master/decision_air_winter_abandonment_vote_master.png` | `processed_png/decisions/decision_air_winter_abandonment_vote.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_abandonment_vote.dds` | `GFX_decision_air_winter_abandonment_vote` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Seal bunker doors | `air_winter_seal_bunker_doors` | Closed circular vault door with engaged locking bars | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#bunker-seal) | `source_png/decisions/decision_air_winter_bunker_seal_source.png` | `source_png/decisions/transparent_master/decision_air_winter_bunker_seal_master.png` | `processed_png/decisions/decision_air_winter_bunker_seal.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_bunker_seal.dds` | `GFX_decision_air_winter_bunker_seal` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Final evacuation | `air_winter_final_evacuation` | Loaded period cargo truck departing frozen ruins | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#final-evacuation) | `source_png/decisions/decision_air_winter_final_evacuation_source.png` | `source_png/decisions/transparent_master/decision_air_winter_final_evacuation_master.png` | `processed_png/decisions/decision_air_winter_final_evacuation.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_final_evacuation.dds` | `GFX_decision_air_winter_final_evacuation` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |
| Decontamination gamble | `air_winter_decontamination_gamble` | Brass pump sprayer and brush crossing dirty-to-clean plate | Built-in `$imagegen`, independent fictional pictogram | [Prompt](prompts/air_winter_decision_icons.md#decontamination-gamble) | `source_png/decisions/decision_air_winter_decontamination_source.png` | `source_png/decisions/transparent_master/decision_air_winter_decontamination_master.png` | `processed_png/decisions/decision_air_winter_decontamination.png` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_decontamination.dds` | `GFX_decision_air_winter_decontamination` | 32x32 | `interface/air_cleanliness_winter.gfx` | `wired` |

The review artifact is decoded from the final runtime DDS files, not assembled from source PNGs: `contact_sheets/air_winter_decision_icons_dds_decoded_contact_sheet.png`. It presents each asset enlarged for inspection beside its native 52x40 or 32x32 decode.

Package validation confirmed the exact nineteen expected sprite payloads, one image level per uncompressed 32-bit BGRA DDS, pixel-identical DDS decodes and processed PNGs, transparent corners, visible alpha, centered native-size silhouettes, absence of chroma-key residue, and unique SHA-256 content at the raw source, transparent-master, processed-PNG, and DDS stages. The approved converter was `texconv-may2026.exe` with SHA-256 `dcfdec10244e02cf5037fba089c55fb7e1326b1c8181742d77d15fa5cb5eef06`. The decoded contact sheet SHA-256 is `162b5d6771c2cb02dff191595dba18d302301d0fec0482311d6fea1133bef146`. No zombie asset, filename, directory, sprite ID, or visual motif was used.
