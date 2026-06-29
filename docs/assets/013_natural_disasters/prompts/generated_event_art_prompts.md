# Event 013 Natural Disasters generated event art prompts

Tool: official `image_gen`

Source mode summary: generated period-documentary disaster scenes were appropriate because Event 13 needs reusable fictional and alternate-history report/news scenes rather than archival photos of one real historical incident.

## Report event image prompts

- `report_event_nd_flood`: 1936-1945 period documentary disaster photograph, flooded rail junction and low town street under muddy water, rescue workers in raincoats and civilian refugees with handcarts, one derailed freight wagon half-submerged, concrete inspectable flood damage, black and white press realism, no readable text, no modern objects, no cinematic grading.
- `report_event_nd_storm`: 1936-1945 period documentary disaster photograph, severe storm aftermath at a damaged airfield and rail yard, bent hangar doors, toppled telegraph poles, emergency crews clearing debris, grounded propeller aircraft partly visible, concrete inspectable storm damage, black and white press realism, no readable text, no modern objects.
- `report_event_nd_earthquake`: 1936-1945 period documentary disaster photograph, earthquake aftermath in a dense town street, masonry facades collapsed, cracked roadway and broken bridge approach, rescue workers with stretchers and engineers inspecting rubble, concrete inspectable damage, black and white realism, no readable text, no modern props.
- `report_event_nd_drought_famine`: 1936-1945 period documentary disaster photograph, drought emergency at a dry canal and village square, cracked soil, empty water barrels, queues for relief water and grain, ox cart and local officials, clear signs of water shortage and crop failure without graphic suffering, black and white realism, no readable text, no modern objects.
- `report_event_nd_wildfire`: 1936-1945 period documentary disaster photograph, wildfire front near a rural rail line and small settlement, firefighters and soldiers cutting a firebreak, smoke wall, burning treeline, villagers evacuating carts, concrete inspectable details, black and white realism, no readable text, no modern gear.
- `report_event_nd_winter`: 1936-1945 period documentary disaster photograph, winter blizzard aftermath on a snowbound rail station and road, stranded locomotive, rescue party with shovels and sleds, civilians wrapped in heavy coats, drifts burying signals and wagons, concrete inspectable details, black and white realism, no readable text.
- `report_event_nd_dust_sandstorm`: 1936-1945 period documentary disaster photograph, dust and sandstorm sweeping over an arid airfield and road convoy, mechanics covering aircraft, trucks half-lost in dust wall, goggles and scarves, concrete inspectable WW2-era equipment, black and white realism, no readable text, no modern objects.
- `report_event_nd_volcano`: 1936-1945 period documentary disaster photograph, volcanic eruption beyond a rail town, ash plume towering over rooftops, ash-covered street and station, workers and police in masks clearing cinders, concrete inspectable volcanic aftermath, black and white realism, no readable text, no modern props.
- `report_event_nd_landslide`: 1936-1945 period documentary disaster photograph, landslide across a mountain rail pass, buried tunnel mouth, smashed wagons and road cut by rockfall, engineers and laborers assessing the slope, concrete inspectable mass movement scene, black and white realism, no readable text.
- `report_event_nd_skyfall`: 1936-1945 period documentary disaster photograph, meteor skyfall aftermath in open countryside near a rail line, fresh crater, shattered telegraph poles, soldiers and civilians staring at smoking impact field, extraordinary but plausible period press composition, black and white realism, no readable text, no fantasy glow.
- `report_event_nd_tsunami`: 1936-1945 period documentary disaster photograph, tsunami aftermath in a harbor district, fishing boats thrown into a street, collapsed quayside, saltwater flooding, rescuers and stunned civilians, concrete coastal damage, black and white realism, no readable text, no modern objects.
- `report_event_nd_moving_corridor`: 1936-1945 period documentary disaster photograph, moving storm corridor crossing plains toward a small industrial town, wall cloud and debris path visible, freight cars overturned, workers and police watching the advancing corridor from a rail embankment, concrete inspectable scene, black and white realism, no readable text.
- `report_event_nd_rupture_wave`: 1936-1945 period documentary disaster photograph, great rupture seismic wave aftermath across a regional valley, multiple bridge spans down, cracked earth crossing road and rail, dust haze, engineers and soldiers surveying a broad damaged corridor, concrete inspectable details, black and white realism, no readable text.
- `report_event_nd_barrage`: 1936-1945 period documentary disaster photograph, disaster barrage scene combining several simultaneous hazards in one region, flooded street in foreground, smoke from wildfire on ridge, broken rail line and emergency vehicles, crowded relief workers and civilians, busy but readable composition, black and white realism, no readable text, no modern objects.

## News event image prompts

- `news_event_nd_regional_floods`: 1936-1945 black and white press photograph, regional floods across a major river basin, relief boats and rail bridge in same frame, crowded embankment and emergency crews, wide horizontal composition suitable for newspaper banner, strong central subject, no readable text, no modern objects.
- `news_event_nd_great_rupture`: 1936-1945 black and white press photograph, great rupture disaster across a city outskirts and river crossing, collapsed bridge spans, long ground crack, smoke and dust, soldiers and engineers in foreground, wide newspaper composition, period realism, no readable text, no modern objects.
- `news_event_nd_meteor_showers`: 1936-1945 black and white press photograph, meteor shower over a night city edge and rail yard, several bright descending streaks, observers, anti-air silhouettes, one distant impact plume, extraordinary but period-authentic newspaper image, wide horizontal composition, no readable text, no fantasy styling.
- `news_event_nd_massive_eruption`: 1936-1945 black and white press photograph, massive volcanic eruption dominating a port town and bay, towering ash plume, ashfall over rooftops, harbor evacuation and grounded ships, wide horizontal newspaper composition, strong contrast, no readable text, no modern objects.
- `news_event_nd_disaster_barrage`: 1936-1945 black and white press photograph, disaster barrage broadcast scene over one hard-hit region, emergency crews and refugees at a damaged rail junction while floodwater, distant wildfire smoke, and storm debris mark multiple simultaneous disasters, wide newspaper banner composition, readable central subject, no readable text, no modern objects.

## Super-event radio image prompts

- `super_event_nd_great_rupture`: 1936-1945 period documentary super-event radio image, catastrophic earthquake rupture through a dense wartime city and rail district, long ground split, collapsed bridge spans, broken rail lines, rescue crews and civilians in period clothing, black and white press realism, strong central composition, no readable text, no modern objects.
- `super_event_nd_massive_eruption`: 1936-1945 period documentary super-event radio image, massive volcanic eruption over a port city and airfield, towering ash column, ashfall across grounded aircraft, trucks, harbor, and evacuees, black and white press realism, strong central composition, no readable text, no modern objects.
- `super_event_nd_skyfall`: 1936-1945 period documentary super-event radio image, meteor shower over a night city, rail yard, and observatory, bright descending streaks, crater field, urban fires, rescue crews and civilians in period clothing, black and white press realism, strong central composition, no readable text, no modern objects.

## Local processing notes

- Report images were processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` to apply the house report-card treatment.
- News images were cover-cropped to `397x153`, converted to black and white, and normalized to stronger press-photo contrast.
- Super-event radio images were cover-cropped to `457x328`, converted to black and white, normalized, and exported as uncompressed DDS.
- DDS export used `convert -define dds:compression=none`.
