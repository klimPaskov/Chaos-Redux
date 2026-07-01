# Event 013 Natural Disasters Spec, Part 3, Evolutions, Cluster, Scenario, GUI, and Super-Events

## Baseline stage

The baseline stage is the ordinary Natural Disasters event. It can hit a state, small area, country, region, coast, river system, or neighboring state group depending on family. It usually creates one to three disaster pulses with five to ten days between them.

The player-facing behavior should be concrete. The affected area should be named. The family should be clear. The consequences should be felt through building damage, population loss, local modifiers, and recovery decisions.

Baseline should use a curated family pool. It should include earthquakes, floods, severe storms, hailstorms, wildfires, drought, blizzards, heat or cold waves when appropriate, sandstorms in valid regions, and mass movement. Tropical cyclones, tsunamis, and volcanic eruptions can appear when target logic supports them, but they should be rarer than ordinary storms and floods.

Baseline report policy is generous. A country hit by a disaster gets a delayed report one to two days after the pulse when the hit is meaningful. A season with multiple pulses can create multiple reports, but the implementation should avoid repeating nearly identical report events in the same country.

## Evolution I, diversified disaster seasons

Evolution I makes disasters more varied and makes several regions suffer within the same season. It does not make every effect massively stronger. The main change is breadth, variety, and pacing.

Design goals:

- More family types are eligible in the same season.
- Three to six disaster pulses are common.
- Delays shorten to three to seven days.
- Multi-region targeting becomes common.
- Same-family repetition receives lower weight unless the family is a chained follow-up.
- The event can hit several countries, several regions in one country, or neighboring countries.
- Damage increases slightly, mainly through secondary states and longer aftermath.

New behavior:

- Family combos become common. Examples include cyclone to flood to landslide, drought to wildfire to dust storm, earthquake to aftershock to tsunami, storm to hail to flash flood.
- Recovery decisions can refer to the season, not only one state.
- AI countries with several active disaster states should prioritize capital, supply hub, port, and population centers first.

Evolution I log direction:

- The evolution log should present this as a change in disaster pattern and spread, not as a normal stage.
- It should not tell the player exact hidden weights.

## Evolution II, global disaster systems and aftermath chains

Evolution II makes Natural Disasters a global pressure system. Disasters happen across the world in a single Event 013 season, but news is throttled. The player should see that the world is being hit in many places through the map, reports, death log, recovery decisions, and selective news.

Design goals:

- Seven to fourteen disaster pulses can happen in a season.
- Targeting is global and can affect many countries.
- Multiple neighboring states take damage for larger families.
- Delays are one to four days.
- News only fires for meaningful hits.
- Chained aftermath becomes a major part of gameplay.
- Disaster recovery becomes a dedicated mechanic, not one cleanup button.

Evolution II family behavior:

- Earthquakes can damage an epicenter and adjacent states.
- Floods can run downstream and affect several river states.
- Tropical cyclones can draw a landfall and inland path.
- Volcanic eruptions can spread ash to neighbors.
- Tsunamis can move along several coastal states.
- Drought can create multi-state famine pressure.
- Heat and cold waves can cover whole regions, but they still avoid stacking with separate active heat or cold global events.

Aftermath chains:

- Famine pressure can follow drought, flood, hail, ash, heat, and cyclone damage.
- Refugee pressure can follow high deaths, heavy building damage, port destruction, wildfire, flood, tsunami, or eruption.
- Damaged infrastructure can reduce local supply, delay recovery, and increase follow-up disaster deaths.
- Local stability and war support can fall when repeated disasters hit the same country.
- Occupied territories can become harder to control if disaster recovery is ignored, but this should not become a resistance exploit.

Decision category behavior:

- The Disaster Response and Reconstruction category should appear to countries with active aftermath.
- The category should show an overview of active disasters, highest-risk states, delayed deaths risk, and current recovery phase.
- It should keep clutter under control. Show top priority decisions first and hide obsolete actions.
- The category should include emergency response, stabilization missions, and reconstruction.

News throttling:

- Severe global seasons should not spam. A global digest can name the worst affected regions or family types.
- Player-country hits, major-country capital hits, high-death disasters, and abnormal chains can still get reports.
- A report should not fire for every small disaster in every country.

## Evolution III, abnormal high-chaos disasters

Evolution III shifts the event from normal natural disasters into abnormal high-chaos disasters. This does not create a terminal branch. It creates severe, strange, region-breaking, and world-affecting disaster families that can receive super-event treatment.

Evolution III should unlock at high chaos and should be rare enough to feel special. It can occur as an active-event evolution for future Event 013 seasons and as a pre-fire evolved opening where the first Natural Disasters event in a high-chaos world starts with abnormal access.

### Meteor shower abnormal family

Meteor showers should strike several states over a short period. Each impact can create building damage, fire, crater aftermath, population loss, and possible tsunami if coastal or ocean logic is supported.

Super-event threshold:

- A super-event should trigger when multiple impact states are selected, when one impact hits a capital or major population center, or when a maximum-intensity Disaster Barrage launches skyfall behavior.
- Title, quote, button remark, and audio are research gates. The spec does not provide final wording.

Gameplay:

- The player can respond with evacuation, fire suppression, impact-site security, and repair corridors.
- Scientific exploitation is optional future content, not required for this rework.

### Global rupture family, integrated Earth Earthquake

The Earth Earthquake event concept is folded into Evolution III as the global rupture family. Event 046 should become a placeholder after implementation. The new logic must not reuse its old content.

Global rupture should damage many states across the world, but it should still have structure. It should not blindly apply the same tiny damage to every state. Instead, it should select major rupture bands, epicenter clusters, coastal tsunami risk zones, aftershock zones, and supply breakpoints.

Core behavior:

- Several rupture regions are selected.
- Each region gets an epicenter state, adjacent damage, and lesser regional supply shock.
- Coastal epicenters can schedule delayed tsunamis.
- Aftershocks happen over several days.
- Global supply and construction disruption can appear as a temporary world or country modifier if supported.

Super-event threshold:

- The first global rupture should receive super-event treatment.
- The super-event should mark the abnormality of the event and the worldwide nature of the damage.
- Research required for title, quote, button remark, image, and audio.

### Massive volcanic eruption family

Massive eruptions should devastate a selected volcanic region, spread ash over neighboring states, close air operations, damage buildings, and create delayed fallout-like ash pressure. This is not nuclear fallout and should not use condemnation.

Core behavior:

- Select a volcanic region or island arc.
- Epicenter state receives severe damage and deaths.
- Neighboring states receive ash fall, supply penalties, air disruption, crop pressure, and delayed deaths.
- Coastal or island eruptions can trigger tsunami follow-ups.
- Large ash clouds can lower regional production and food output for months.

Super-event threshold:

- A massive eruption with regional ash cloud, high death forecast, or tsunami follow-up deserves super-event treatment.

### Moving storm corridor and world tornadoes

The user specifically wants massive tornadoes or storm systems that move around the world and destroy everything on their path. This needs scripted GUI support and animation.

The storm corridor should be a state-driven moving hazard.

Player-facing UI:

- A disaster map window or category-attached scripted GUI shows current corridor position, predicted next regions, uncertainty, affected states, danger level, and response actions.
- The map updates as the corridor moves.
- The player sees at least current path, likely next path, and threatened states.
- A warning pulse or animated storm marker should show active movement.
- Static fallback sprites are required.

Gameplay:

- Each movement step damages the current state group.
- The next state group is selected from weighted neighbors, regional path logic, and chaos intensity.
- Player decisions can reduce damage in predicted states, evacuate population, reinforce bridges, ground aircraft, or move supply reserves.
- A storm can shift unexpectedly when pressure is high or response is poor.
- AI countries use equivalent scripted decisions and do not depend on human-only GUI buttons.

Animations:

- Animated storm marker for active path.
- Animated warning border for threatened states or map panel.
- Animated progress line or pulse for next movement if the GUI can support it.
- Static fallbacks for every animated element.
- Use real planned animation frames, not a script-made glow pulse from one still image.

### Delayed tsunami aftermath from abnormal disasters

Evolution III should make delayed tsunamis more important. Global rupture, massive volcanic eruption, submarine landslide, or meteor impact can schedule tsunami waves after a delay. This delay is useful because it gives the player a response window.

Behavior:

- The source disaster saves coastal targets and expected arrival windows.
- A report or GUI entry can show coastal evacuation risk without exposing every hidden roll.
- Evacuation decisions reduce deaths and maybe lower port damage.
- The wave arrives after a scheduled delay and applies tsunami family damage.

## Disaster Response and Reconstruction decision category

This category is mandatory for the rework. It is the main player response layer.

Category purpose:

- Show active disaster aftermath.
- Let the player reduce deaths, repair infrastructure, and stop chained aftermath.
- Make disasters feel recoverable but costly.
- Avoid flat political power purchases.

Recommended decision families:

- Emergency rescue operations.
- Evacuate threatened area.
- Clear rail and road corridors.
- Reopen ports and airfields.
- Restore supply hubs.
- Establish field hospitals and shelters.
- Import food and water.
- Stabilize slopes and levees.
- Firebreak and fire suppression.
- Ash and dust clearing.
- Rebuild local industry.
- Request or provide foreign disaster aid.
- Monitor follow-up hazard.

Mission families:

- Hold and supply affected states for a duration.
- Keep a port or rail hub open during recovery.
- Place supplied divisions or support units in named states.
- Maintain stability above a threshold while recovery is active.
- Complete evacuation before a delayed tsunami or storm corridor movement.
- Repair a named supply route before famine or refugee pressure worsens.

Clutter control:

- Human players should see only active relevant decisions.
- If many states are affected, show top priority states or use a selected-target category pattern.
- AI can see all decisions or use hidden AI-only decisions.

## Disaster map scripted GUI

A custom GUI becomes required at Evolution III because the moving storm corridor and massive disaster maps need readable state. The same GUI can also improve Evolution II global seasons.

Window content:

- Active sequence id and severity tier.
- Current active family or abnormal family.
- Affected states or state groups.
- Predicted next target for moving hazards.
- Recovery pressure summary.
- Death risk summary.
- Buttons to focus the map, show disaster list, open recovery category, and toggle digest detail.

Visual states:

- Normal season.
- Global season.
- Abnormal active disaster.
- Moving corridor active.
- Recovery-only phase.
- Cleared phase.

Animation plan:

- Animated storm marker for moving corridor.
- Animated eruption marker for massive eruption locations.
- Animated meteor impact marker for active shower states.
- Warning pulse for threatened next states.
- Progress shimmer for recovery completion can be static if animation would clutter the UI.

AI equivalent:

- Every button that changes gameplay must have an AI equivalent effect or decision.
- Decorative map controls do not need AI.

## Super-event package directions

Evolution III larger disasters should get super-event treatment. Super-events are not for every disaster. They mark abnormal thresholds.

Required super-event candidates:

1. Meteor shower major threshold.
2. Global rupture first occurrence.
3. Massive volcanic eruption major threshold.
4. Moving world storm corridor first public threshold.

Optional super-event candidates:

- A severe combined Disaster Barrage maximum launch.
- A delayed tsunami chain after global rupture when coastal death risk is extreme.

For each super-event, the super-event researcher must produce real quote candidates, exact attribution, cultural remark candidates, licensed audio, and final source documentation. The spec only provides direction. The final implementation must not turn working labels into final localisation.

## Event cluster behavior

Natural Disasters has a special cluster role because one event identity can fire multiple times in a cluster. Instead of treating Event 013 as one cluster member only, the cluster can contain several entries that all call Event 013 with different sequence profiles.

Cluster design:

- Base cluster roll chance should be high compared with ordinary low-severity clusters.
- At low chaos, the cluster can contain several baseline Event 013 members. A suggested structure is three baseline member entries with low severity.
- At higher chaos, Evolution I and Evolution II member profiles unlock.
- Evolution III abnormal one-off families should not be repeated casually inside ordinary cluster loops.
- Global one-off style families such as global rupture, massive eruption, and major heat-wave analogues should have strong cooldowns and special availability.

Cluster pacing:

- Cluster members should not all fire on the same day.
- A cluster launch should schedule the member Event 013 seasons over several days or weeks.
- Each Event 013 member that actually fires produces one Event 013 Event Log entry under the normal cluster contract. The disasters inside each member still do not create separate Event Log entries.

Cluster details:

- The cluster detail window should explain that Natural Disasters members represent disaster seasons, not isolated single disasters.
- Member severity should rise with evolution tier.
- Member skip reasons should include no valid targets, active disaster season cap, abnormal cooldown, and disabled evolution.

Catalog alignment:

- The uploaded cluster CSV has Natural Disasters and Natural Disasters 2 rows with missing cluster ids. Implementation should assign stable ids and update the workbook through the spreadsheet worker after in-game wording exists.

## Disaster Barrage manual scenario

The scenario catalog already contains Disaster Barrage as SCN-007. The rework should keep that scenario and route it through the same sequence controller.

Scenario purpose:

- Manual sandbox and challenge setup.
- Direct testing for Event 013 families, evolutions, recovery decisions, death logging, and news throttling.
- Does not depend on normal chaos, normal evolution prerequisites, date gates, or prior Event 013 firing.

Scenario type options:

- Random Barrage uses the full eligible pool.
- Geological Crisis favors earthquakes, global rupture, landslides, volcanic eruptions, tsunamis, and meteor families.
- Weather Crisis favors floods, tropical cyclones, severe storms, hail, extreme winds, drought, heat, cold, wildfire, blizzards, and dust.
- Skyfall Crisis favors meteor showers and skyfall behavior.
- Full Catalogue keeps everything open, including abnormal families at high intensity.

Intensity stops:

- Low creates a varied local season.
- Medium creates regional disaster systems.
- High opens severe chained behavior and some abnormal access.
- Maximum can combine meteor showers, rupture waves, massive eruption pressure, delayed tsunami, and storm corridor movement in one season.

Scenario boundaries:

- It launches Event 013 directly.
- It bypasses automatic prerequisites only for the scenario setup.
- It uses normal family helpers, damage helpers, recovery helpers, death logging, and news throttling.
- It must not copy separate disaster logic.
- It must not create a terminal event branch.

## Catalog update direction

After implementation, the catalog workbook should be updated by the spreadsheet worker using final in-game wording.

Event 013 should no longer show `Reserved`. Evolution III should own the meteor shower and intense natural disaster language currently sitting in the uploaded Evo IV field. Event 046 and Event 099 should be marked as placeholder or unknown after their logic is moved or retired.

The catalog details should describe the situation and premise, not mechanical values. It should say that disaster seasons strike states, regions, or countries, that affected areas suffer building damage and population loss, and that recovery decisions can open afterward. It should not list exact modifiers.
