# Event 013 accepted static-asset completion prompt and provenance ledger

Production date: 2026-07-10

Tool: official built-in `image_gen`

Source mode: generated. Every scene is fictional, composite, alternate-history, or presentation-specific. No third-party archive image, author, license, or public-domain claim applies.

Reference basis:

- current Event 013 report, news, icon, achievement, animation, and super-event contact sheets
- current Event 013 `457x328` super-event image set
- vanilla HOI4 achievement, decision-category, progress-bar, and interface assets
- existing Chaos Redux dark aged-metal custom GUI panels

The skill-pack reference directories named in `chaos-redux-event-assets` were absent in this checkout. The accepted asset audit explicitly directs this pass to use the current Event 013 library and active Chaos Redux UI as the comparison set; no alternate reference package was invented.

## Shared report prompt contract

Each report source used this full shared contract plus the asset-specific subject below:

> Use case: historical-scene. Asset type: HOI4 report-event source photograph, later cropped and given a report-card treatment. Authentic black-and-white press documentary photograph made with 1936-1945 camera technology, realistic grain and imperfect exposure. Landscape documentary photograph with one clear physical-damage focal point; no tilt, frame, border, or report-card styling in the source. Period-correct clothing, vehicles, architecture, rail equipment, aircraft, and harbor craft as relevant. No readable text, logos, watermark, modern objects, cinematic color grading, collage, map, or UI overlay.

| Asset | Asset-specific generated subject | Built-in result |
| --- | --- | --- |
| `report_event_nd_tropical_cyclone` | Cyclone aftermath at a wartime harbor and coastal airfield: wrecked wooden quays, grounded fishing craft, flooded coastal railway, torn hangar doors, rescue workers, evacuees, and period propeller aircraft. | `exec-712cc944-c018-435f-a498-89448faf0cd8.png` |
| `report_event_nd_heat_wave` | Dense industrial-city heat emergency: period water cart, worker queue, halted factory, crowded shade shelter, medical attendants, high sun, and heat haze; not a drought-only farm scene. | `exec-5362dbd7-ccf1-4b18-9276-336bfd4f4b5d.png` |
| `report_event_nd_extreme_wind` | Exposed rail and airfield corridor: stripped roofs, snapped telegraph poles, derailed freight car, torn hangar canvas, damaged aircraft, and debris crews; no tornado funnels. | `exec-c6d74d29-cfc2-48c3-ab06-b2a3f040b409.png` |
| `report_event_nd_tornado_outbreak` | Narrow plains-town destruction corridor: splintered structures, overturned freight cars, scattered aircraft frames, rescuers, and one distant receding funnel. | `exec-f1ae207c-e335-4138-8d61-114ecfb33287.png` |
| `report_event_nd_hailstorm` | Agricultural-airfield hail damage: shattered greenhouse glass, dented aircraft and truck roofs, ruined crops, slush-covered road, and workers inspecting damage. | `exec-f803ed86-84ed-4bed-84b1-e2de3694811e.png` |
| `report_event_nd_extreme_cold_wave` | Still-air urban cold emergency distinct from blizzard: fuel queue, frozen broken mains, crowded warming shelter, hospital attendants, closed tram, and frost-coated street. | `exec-ce9cc39a-3af4-4f23-8a0f-23642705eb00.png` |
| `report_event_nd_wet_mass_movement` | Rain-soaked mountain valley: mud-choked floor, torn bridge, buried road bends, flooded sidings, period trucks, and rescue crews. | `exec-c3f556f5-ead7-4b55-98c4-ed70f7144ff4.png` |
| `report_event_nd_ashfall` | Downwind airfield and industrial town: ash-loaded roofs, quiet aircraft, fouled engines, ash-covered fields, platform clearing, and protected water stores. | `exec-d4ec78e1-6f31-4f18-89c7-967e238f6a08.png` |
| `report_event_nd_lahar` | Volcanic mudflow in a river valley: thick mud, broken bridge, buried settlement edge, stranded truck, higher-ground rescuers, and visible ash-covered volcano. | `exec-b815f0b3-177d-423e-b312-e118549ec8c0.png` |
| `report_event_nd_storm_surge` | Cyclone-battered low port: seawater through quays, flooded warehouses, broken marsh road, debris over coastal rail, damaged period boats, and pumping crews; not tsunami withdrawal. | `exec-40db92a6-9e1a-4d10-9b81-f0da0fb3cb8b.png` |
| `report_event_nd_meteor_impact` | One destructive impact: one crater and blast ring, burning outskirts, broken rail and telegraph lines, strange fragments, soldiers, engineers, and civilians. | `exec-becc9628-f2b7-4d93-9407-5aa597550ac9.png` |
| `report_event_nd_meteor_shower` | Multi-impact cluster: separated small craters, roof fires, airfield sparks, several fire trails, rail inspection, and shelter damage. | `exec-d5fcf23d-9eb9-4e0a-9f4c-428fbe5e2140.png` |
| `report_event_nd_massive_eruption` | Regional eruption crisis: immense ash column, buried slopes, darkened fields, lahar channels, grounded aircraft, blocked road, food convoy, and evacuees. | `exec-cf311027-9a1f-4116-8b38-a0b19e4fa5d4.png` |

Local processing: cover crop, grayscale, sepia, deterministic fine grain, paper edge, subtle deterministic tilt, transparent canvas margin, and soft shadow at `210x176`.

## Live-reference report completion

The parent integration audit found one additional gameplay-referenced identity after the Part 8 coverage pass:

| Asset | Asset-specific generated subject | Built-in result |
| --- | --- | --- |
| `report_event_nd_regional_aftermath` | Wide regional reconstruction scene after overlapping disasters: damaged railway bridge and road, flooded agricultural plain, ruined small town, relief convoys, emergency workers, distant smoke and storm fronts; no single dominant hazard. | `exec-760bb4d0-8c25-4c33-b8f6-a26627ba6499.png` |

The source was generated as a restrained full-colour mid-century documentary painting, then normalized to the Event 013 sepia report-card treatment at `210x176`. It is a distinct broad recovery identity, not a renamed copy or filename fallback.

## Shared news prompt contract

Each news source used this full shared contract plus the asset-specific subject below:

> Use case: historical-scene. Asset type: HOI4 news-event source photograph for a wide `397x153` black-and-white press crop. Authentic 1936-1945 newspaper photograph, high contrast, realistic grain, very wide horizontal banner composition, strong central subject, edge-safe detail, period-correct vehicles, clothing, architecture, rail, aircraft, and harbor equipment as relevant. No readable text, logos, watermark, modern objects, cinematic color, collage, map, or UI overlay.

| Asset | Asset-specific generated subject | Built-in result |
| --- | --- | --- |
| `news_event_nd_tornado_outbreak` | Long rail/industrial damage corridor, overturned freight cars, torn roofs, rescue columns, two distant funnels, and a broad moving storm wall. | `exec-622b77eb-5be1-446a-b3d0-8fa304bd991b.png` |
| `news_event_nd_ashfall` | Major capital airfield and rail closure: ash-loaded roofs, grounded aircraft, fouled locomotive, platform clearing, protected stores, and distant plume. | `exec-0ede63d4-d6d6-4477-82eb-8546b02616de.png` |
| `news_event_nd_lahar` | Strategic volcanic valley: thick mud channels, collapsed bridge, buried town edge, stranded trucks and trains, rescuers on high ground, and visible volcano. | `exec-4b546b35-41c4-4e5e-9320-30d77262e3f6.png` |
| `news_event_nd_storm_surge` | Major port and coastal railway overwhelmed by storm-driven water, damaged ships, debris, pumps, evacuation columns, and wind-damaged roofs. | `exec-4867b3b3-c9aa-4e6e-8292-abe13242b574.png` |
| `news_event_nd_meteor_impact` | One confirmed major crater at a rail-city edge, broken rail arteries, burned buildings, smoke, fragments, period cordon, soldiers, engineers, and civilians. | `exec-8aecb61e-8342-418d-8a44-77fc30ca41ec.png` |

Local processing: cover crop to `397x153`, grayscale, press contrast, and restrained sharpening.

## Super-event image prompts

### `super_event_nd_abnormal_disaster_age`

> Use case: historical-scene. Asset type: HOI4 super-event source image, final `457x328` radio photograph. One coherent 1936-1945 coastal rail junction and industrial valley: cracked railway and displaced workers in the foreground, an unnaturally emptied harbor or river mouth to one side, an ash-darkened storm horizon, and only a few descending fire trails high above. Authentic black-and-white alternate-history documentary photography, realistic grain, restrained contrast, strong central rail-junction subject, readable depth, ominous and severe but not world-ending. Period clothing, rail equipment, harbor craft, buildings, and trucks. No text, logos, watermark, globe, strategic map, collage, poster panels, modern emergency branding, satellites, radar UI, modern vehicles, superhero framing, or world visibly split apart.

Built-in result: `exec-66c24983-6d75-476e-8f82-0cc6210e9929.png`.

### `super_event_nd_delayed_tsunami_chain`

> Use case: historical-scene. Asset type: HOI4 super-event source image, final `457x328` radio photograph. A 1936-1945 harbor after the sea has withdrawn but before destructive arrival: exposed mud, stranded fishing boats, quay foundations, port and rail workers plus civilians evacuating uphill, abandoned period transport below, and a broad low dark water disturbance approaching on the distant sea. Strong harbor-to-road diagonal, authentic black-and-white documentary photography, realistic grain and high contrast, dreadful silence and urgent organized withdrawal. No text, logos, watermark, giant curling Hollywood wave, tropical imagery, modern sirens, emergency vests, helicopters, container cranes, modern ships, map UI, or post-impact-only framing.

Built-in result: `exec-7dce1e35-2bc1-4409-8456-faeaebc912bc.png`.

### `super_event_nd_storm_corridor` provenance closure

This generated source supersedes the earlier stable-identity image whose exact generation prompt was missing. The accepted identity, sprite, slot, dimensions, and live path remain unchanged.

Exact built-in prompt:

```text
Use case: historical-scene
Asset type: Hearts of Iron IV super-event source photograph, later cropped and normalized to a 457x328 black-and-white radio image
Primary request: the accepted sustained multi-state moving storm and tornado corridor, not one local storm
Scene/backdrop: a broad 1936-1945 North American-style rail and road corridor crossing open plains, several small industrial towns, and distant farm settlements
Subject: a long advancing convective storm wall traveling diagonally along the corridor, with three separated tornado funnels at different distances embedded in the same moving front; a continuous trail of uprooted telegraph poles, damaged station buildings, torn roofs, and derailed period freight cars shows where the corridor has already passed; farther along the route another town is being evacuated
Style/medium: authentic black-and-white 1936-1945 press documentary photograph made with period camera technology, realistic grain, imperfect exposure, natural disaster reportage, not cinematic concept art
Composition/framing: wide elevated landscape view with the rail line and parallel road leading from the damaged foreground through multiple towns toward the advancing storm; the sequence of funnels, damage, relief traffic, and receding route must make sustained geographic motion visible without any drawn arrows or map overlay; strong readable storm wall and rail corridor at final super-event size
Human details: small period rescue crews, railway workers, civilian evacuees, canvas-covered relief trucks, and one period ambulance working along the damaged route
Lighting/mood: severe daylight beneath a dark storm shelf, high documentary contrast, urgent but plausible
Constraints: 1936-1945 clothing, architecture, freight equipment, automobiles, emergency vehicles, telephone poles, and rescue methods; one coherent real scene; no modern objects; no modern emergency branding; no readable text; no signs; no logos; no flags; no watermark; no borders; no title card; no collage; no map; no UI; no supernatural scale; no giant single funnel dominating the whole frame; no postwar vehicles; no colorized-photo look
```

Built-in result: `exec-f951d9ec-e1c4-49e2-bab7-fbdee7797b5a.png`.

Source-mode rationale: the accepted corridor is a fictional, composite Event 013 escalation whose simultaneous sustained route, tornado outbreak, rail damage, multiple towns, and period rescue traffic cannot be represented honestly by claiming one real archival incident. Generated period-documentary art is the correct source mode.

Processing: cover crop to `457x328`, strict grayscale normalization, high-quality resampling, then conversion to 32-bit RGB+A DDS. The scene retains the broad storm shelf, four separated visible funnels, continuous rail/road damage path, multiple settlements, and period response convoy at final size.

Local processing: cover crop, grayscale, contrast normalization, and restrained sharpening at `457x328`.

## Decision icon atlas

Built-in result: `exec-10e167f9-d744-447c-aae2-b9c83b2f1f85.png`.

Prompt contract: exact `4x2` grid, first seven cells filled, eighth green; one centered compact painted HOI4 decision symbol per cell on uniform `#00ff00`; aged bronze, iron, canvas, muted red, dark outline, subtle subject shadow; no circular medallion, focus frame, text, opaque square backdrop, or cross-cell artwork.

Cell order:

1. closed harbor gate and crossed mooring chains, port closure
2. grain sack, ration crate, relief ladle, food relief
3. shovel, axe, short firebreak, contained flame, firebreaks
4. runway, propeller aircraft, broom and shovel, ash cleanup
5. period water tank rail wagon and pipe, water trains
6. brass telescope and compact seismograph, observatory watch
7. brick wall, railway tie, hammer, rolled plan, reconstruction

The atlas was sliced to individual generated source PNGs, chroma-removed through the official helper, centered, and resized to `32x32`.

## Idea and state-modifier icon atlas

Built-in result: `exec-f573dc2d-f4bf-4dd7-a1ab-317233937be9.png`.

Prompt contract: exact `4x2` grid, first seven cells filled, eighth green; one centered compact painted HOI4 national-spirit symbol per cell on uniform `#00ff00`; aged bronze, iron, canvas, ash grey, muted rust and warning red; dark outline and subtle subject shadow; no medallion, focus frame, text, opaque square backdrop, or cross-cell artwork.

Cell order:

1. period respirator, ash plume, ash-dusted wheat, ashfall
2. medical satchel, cracked canteen, fly, thermometer, disease risk
3. anchor, crossed chain, broken quay timber, blocked ports
4. charred trunk, burned sleepers, factory gear, scorched state
5. frost-coated fuel drum, crates, rail lantern, frozen supply
6. fissure splitting railway tie and road slab, cracked ground
7. crater rim, black fragment, cordon stake, bent pole, crater aftermath

The atlas was sliced to individual generated source PNGs, chroma-removed through the official helper, centered, and resized to `64x64`.

## Aftermath category icon

Built-in result: `exec-4edbc7de-f2f7-47af-9305-1b041dcf322e.png`.

Prompt: one compact horizontal aftermath emblem on uniform `#00ff00`: civil-defense shelter arch and rescue lantern, broken railway tie, small wave, cracked-ground shard, restrained smoke, aged bronze and iron, muted red warning accent, dark outline, no institutional seal, globe, office motif, text, medallion, or opaque background. Processed at `53x40`.

## Abnormal GUI static prompts

| Source asset | Prompt direction | Built-in result |
| --- | --- | --- |
| `013_abnormal_disaster_panel` | Wide `760x520` HOI4 dark aged-steel command plate with header, five-card left rail, large empty central map workspace, empty right detail recess, bottom timeline, and legend rail; restrained brass, charcoal canvas, aged paper, ash and water stains; no text or live icons. | `exec-edc8dc73-0b6c-4669-909d-3be94db6b07f.png` |
| `013_abnormal_disaster_panel_damaged` | Image edit preserving the base panel's exact geometry and empty content areas; add bent brass corners, hairline trim cracks, small scorched corner, ash, dried-water marks, torn paper edges, and subtle dents. | `exec-275680d1-3ad9-4d88-97a9-deaf3642f56b.png` |
| `013_disaster_card_frame` | Empty horizontal blackened-steel frame on uniform `#00ff00`, oxidized brass corner clamps, tiny rivets, small ash-stained tab, completely green center, no text or symbols. | `exec-527c6dca-03f4-4692-9231-73b044a485dd.png` |
| marker atlas | Three uniform-green cells: cracked impact pin and crater; three linked chain-risk loops with branching arrow; period relief crate, blanket, ship/rail/handshake badge. | `exec-ac092f53-4534-4792-80fe-4e11788989e7.png` |
| recovery progress atlas | Two isolated horizontal assets on uniform green: hollow riveted blackened-steel/brass frame; separate amber-gold enamel fill with diagonal repair hatching. | `exec-c0f66a12-37eb-4474-a69a-e18f5c503b48.png` |

Transparent GUI sources were processed through the official chroma-removal helper with border sampling, soft matte, and despill.

## Achievement source sheets

Shared prompt contract: exact `3x2` grid; first five cells filled and sixth blank; each filled cell is a complete opaque square HOI4 achievement icon with the same aged bronze laurel frame, dark inner border, painterly 1930s-1940s disaster imagery, strong silhouette, muted colors, and no text.

Sheet A result: `exec-0ad40100-67e6-4146-ab19-5aaef0097316.png`.

1. lit shelter beneath storm and siren, `after_the_sirens`
2. coast marker and wave broken by evacuation barrier, `no_second_wave`
3. railway bridge under repair, `every_bridge_counts`
4. respirator, protected grain, falling ash, `ashes_without_famine`
5. torn blank report, storm symbol, snapped microphone, `no_global_announcer`

Sheet B result: `exec-97962ebd-3061-429f-a7c9-94669b4cfafa.png`.

1. burning meteor over crossed searchlights and intact capital, `under_the_falling_sky`
2. cracked globe held by metal repair brace, `shake_the_world_back`
3. civil-defense shield with wave, flame, lightning, crack, meteor, `disaster_barrage_maximum`
4. refugee tent, medical satchel, railway line, `not_one_more_camp`
5. blank archive file with disaster emblem cards, `catalogue_of_ruin`

Each sheet was sliced to individual source PNGs. Completed icons were resized to `64x64`; grey variants are simple black-and-white conversions.

## Achievement not-eligible overlay provenance

The reference overlay path named by the asset skill was absent in this checkout. This pass did not invent a red tint or redraw the treatment. It recovered the repository's existing overlay mathematically from the eight current Event 013 grey/not-eligible DDS pairs, using their shared alpha-composite relationship.

- recovered overlay: `docs/assets/013_natural_disasters/source_png/achievement_not_eligible_overlay_recovered.png`
- recovery evidence: 939 non-zero-alpha pixels on a `64x64` canvas
- reconstruction error across the eight existing repository pairs: mean `0.07/255` pixel RMSE
- method: solve the shared per-pixel overlay color and alpha across all eight input/output pairs, then composite the recovered overlay over each new grey icon

The ten new not-eligible variants therefore use the existing repository overlay method rather than a substitute visual treatment.
