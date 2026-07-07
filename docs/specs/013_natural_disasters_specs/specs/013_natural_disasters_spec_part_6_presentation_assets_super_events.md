# Event 013 Natural Disasters, Part 6, presentation, assets, super-events, and achievements

## Presentation principles

Natural Disasters should use concrete places and physical consequences. The player should not read generic reports from a global institution. A report should sound like people in a named place are dealing with collapsed bridges, flooded rail yards, ash-darkened airfields, dry wells, broken quays, burning forests, shattered factories, or silent coast roads.

Final localisation must be written during implementation. This spec does not provide final copy.

## Report event direction

Every affected country should receive a delayed report after a serious impact.

A report should include:

- affected state, region, coast, or country
- specific disaster family
- visible damage type
- human consequence direction
- active recovery category or aftermath card
- chain risk if the country can influence it

Report remarks should be family-specific. They should never be a bland acknowledgment with a state name swap.

## News event direction

News events are global or broad attention surfaces. They should identify the family and place clearly.

Use news for:

- first meaningful family appearance
- major player country hit
- capital, port, or dense state hit
- large deaths or building loss
- strange chaining
- cross-border effects
- abnormal Evolution III disasters
- super-event adjacent disasters

Do not show news for every small disaster in Evolution II. This prevents spam and keeps major news meaningful.

## Super-event set

Event 013 should have super-events for abnormal milestone moments. Each requires separate super-event research for title direction, description direction, quote, cultural remark, image, and audio. This spec provides roles and research gates only.

| Working super-event id | Role | Trigger direction | Image direction | Audio direction |
| --- | --- | --- | --- | --- |
| `se_013_abnormal_disaster_age` | First abnormal era reveal | First Evolution III abnormal family opens or first abnormal chain begins | Generated high-chaos natural world scene with several disaster motifs, not a map table | Ominous music with rising scale, researched and licensed |
| `se_013_earth_rupture` | Whole-earth rupture wave | First massive rupture wave crosses multiple regions | Generated period documentary scene of cracked rail, broken city, and distant coast movement | Heavy, unstable orchestral or choral mood |
| `se_013_skyfall` | Meteor shower or impact crisis | First major meteor shower or impact cluster | Generated night sky and impact field, readable at super-event size | Percussive, cosmic, or liturgical dread mood, real track only |
| `se_013_mantle_opened` | Massive eruption crisis | Massive volcanic crisis devastates a region | Generated eruption, ash, darkened airfields, and evacuation scene | Slow catastrophic music, not pure ambience |
| `se_013_moving_storm_corridor` | Moving storm or tornado corridor | First abnormal moving storm path is visible on GUI map | Generated storm wall and rail corridor scene | Urgent stormlike orchestral or march-adjacent track |
| `se_013_delayed_tsunami_chain` | Delayed ocean chain | Tsunami chain follows rupture, volcano, or ocean impact | Generated emptied harbor and wave approach without modern elements | Dread and silence followed by movement, real licensed music |

Super-event text and audio are blockers until researched through the super-event workflow. Do not invent quotes, lyrics, slogans, or final titles in the spec or implementation prompt.

## Visual asset families

| Asset type | Needed assets |
| --- | --- |
| Report images | Family-specific report images for earthquake, flood, cyclone, wildfire, blizzard, heat, drought, dust, volcano, tsunami, meteor, and regional aftermath. Generated period-documentary scenes are appropriate unless a sourced period photograph is selected for a specific ordinary disaster. |
| News images | Black-and-white news images for first major family news and abnormal disaster news. Generated news images are acceptable for fictional or impossible disasters. |
| Super-event images | Generated super-event images for abnormal disaster roles. |
| Decision category icon | Natural disaster aftermath category icon. |
| Decision icons | Rescue, evacuation, rail repair, port closure, medical corridor, food relief, firebreak, ash cleanup, winter fuel, water trains, observatory watch, reconstruction. |
| Idea or modifier icons | Damaged transport, refugee pressure, ashfall, famine risk, disease risk, blocked ports, scorched state, frozen supply, cracked ground, crater aftermath. |
| Scripted GUI assets | Dynamic map panel, active path markers, next-hit warnings, selected state cards, progress meters, family emblems, warning frames. |
| Animated assets | Moving storm path, tsunami wavefront, meteor marker blink, ash plume drift, rupture pulse, recovery warning border. |
| Static fallbacks | Required for every animated sprite. |
| Achievement icons | One completed 64x64 icon direction per achievement, plus grey and not-eligible variants when implemented. |

Asset work should follow the event asset workflow and inspect relevant reference folders before generation or sourcing.

## Animation plan

Animation should clarify state. It should not be ornamental noise.

| Animated asset | Use | State logic | Direction |
| --- | --- | --- | --- |
| Storm corridor path | Abnormal moving storm GUI | Shows next path segment and current active segment | Frame-sheet path pulse with static fallback. |
| Tsunami wavefront | Delayed tsunami chain GUI | Shows coast risk and wave approach | Slow wave marker sweep across route, not a GIF asset. |
| Meteor impact marker | Meteor shower GUI | Shows impact cluster and next possible strike area | Brief blink or falling marker frames with static fallback. |
| Ash plume drift | Massive eruption GUI | Shows ash spread and affected airfields | Soft frame-by-frame plume state, not simple opacity filter. |
| Rupture pulse | Whole-earth rupture GUI | Shows seismic wave region and aftershock risk | Ground-line pulse frames with family marker. |
| Recovery warning border | Aftermath card | Card is near failure or chain risk threshold | Warning frame loop with static fallback. |

Every final animation requires source frames, processed frames, horizontal sheet, DDS, static fallback, preview GIF for review only, manifest entry, and GFX handoff.

## Achievement design

Achievement titles below are working labels, not final localisation.

| Working id | Route or challenge | Unlock direction | Disqualifier direction | Icon direction |
| --- | --- | --- | --- | --- |
| `013_after_the_sirens` | Recovery mastery | Recover from a severe disaster season as the affected country with no unresolved aftermath card remaining. | Recovery failure or abandoned aftermath. | Shelter light under storm cloud. |
| `013_no_second_wave` | Tsunami prevention | Stop a delayed tsunami chain from becoming a second major death spike after an offshore quake, volcanic collapse, or ocean impact. | Wave follow-up hits populated coast. | Coast marker and broken wave. |
| `013_every_bridge_counts` | Transport recovery | Clear all transport aftermath missions after a regional flood, cyclone, earthquake, or blizzard without losing the capital supply route. | Capital supply route fails. | Rail bridge under repair. |
| `013_ashes_without_famine` | Volcanic recovery | Survive major ashfall and prevent famine chain in every affected state. | Any ash famine chain matures. | Mask, ash, and grain sack. |
| `013_no_global_announcer` | Anti-institutional framing joke direction | Experience several distinct family reports without any global institutional framing. Tracking should verify family variety, not text. | None beyond route failure. | Torn report card and storm symbol. |
| `013_under_the_falling_sky` | Meteor survival | During a meteor shower, keep the selected country capital, primary supply hub, and airfield network functional until the chain ends. | Capital state hit without recovery or airfield network fails. | Meteor over searchlight. |
| `013_shake_the_world_back` | Whole-earth rupture recovery | After a rupture wave, close regional recovery cards across several affected regions before the delayed tsunami or aftershock chain matures. | Any major follow-up chain matures. | Cracked globe with repair brace. |
| `013_disaster_barrage_maximum` | Manual scenario challenge | Launch Maximum Disaster Barrage and survive the season as the selected country with at least one capital route, one port or rail corridor, and the aftermath recovery category fully closed later. | Terminal country collapse or unresolved aftermath at check date. | Multiple disaster symbols around a shield. |
| `013_not_one_more_camp` | Refugee protection | Accept or manage refugee pressure from a severe disaster and prevent disaster refugee deaths from crossing the severe threshold. | Border camp failure or disease chain in camp. | Tent, medical cross, and rail line. |
| `013_catalogue_of_ruin` | Full-family campaign | Over a campaign, see and recover from every normal family group at least once. | None, rare long-campaign achievement. | Archive card with disaster emblems. |

The achievement set should reward difficult response, prevention, and rare abnormal survival. It should not unlock just because Event 013 fired.
