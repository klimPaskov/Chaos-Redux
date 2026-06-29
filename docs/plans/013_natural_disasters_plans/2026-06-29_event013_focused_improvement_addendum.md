# Event 013 Natural Disasters focused improvement addendum

This addendum responds to the latest Event 013 completion audit gaps. It is a plan only. It does not replace the source spec package under `docs/specs/013_natural_disasters_specs/`, and it does not claim implementation completion.

Expansion is still useful. The current implementation has the main frame in place, including family ids, family categories, dynamic death profiles, family damage profiles, scenario launch, cluster launch, report and news art, achievement shells, and registered animated sprites. The remaining gap is not more catalogue size. The gap is that the runtime still chooses and resolves too much through broad random pools, generic warning flow, generic objectives, and one generic news event.

The main agent should treat this as a focused implementation tranche. Do not add a world-end branch, focus tree, country package, formable, super-event, or new unrelated disaster event. Natural Disasters should become deeper through target choice, warning variance, family chains, family objectives, visible forecast state, tracked achievements, and throttled family news.

## Research basis

Use these sources as design anchors, not as final player-facing text.

- USGS earthquake hazard material supports scoring seismic states by likely shaking exposure, built environment, bridges, utilities, and landslide potential. This supports high-value target scoring, aftershock inspections, bridge integrity, and dense-state loss scaling. Source: <https://www.usgs.gov/programs/earthquake-hazards/science/earthquake-hazards-101-basics>
- U.S. Tsunami Warning Centers support delayed coastal warning behavior after seismic or volcanic triggers. This supports a separate tsunami countdown state, not instant tsunami impact every time. Source: <https://www.tsunami.gov/>
- NOAA tornado alert guidance separates watch and warning behavior. This supports moving storm corridors with forecast confidence, shelter readiness, and a short impact path instead of a static storm popup. Source: <https://www.weather.gov/safety/tornado-ww>
- USGS volcano hazard material supports ashfall, lahars, weakened volcanic slopes, and valley or river route damage. This supports volcanic ash belts, lahar valley aftermath, airfield closure, water contamination, and possible delayed coastal wave when the anchor is coastal. Sources: <https://www.usgs.gov/programs/VHP>, <https://www.usgs.gov/programs/VHP/lahars-move-rapidly-down-valleys-rivers-concrete>, <https://www.usgs.gov/programs/VHP/landslides-are-common-tall-steep-and-weak-volcanic-cones>
- USGS drought, flood, and hydrologic hazard material supports long aftermaths where water, food, watersheds, and infrastructure are the main danger. This supports delayed famine, contaminated wells, post-fire water problems, and relief corridor objectives. Sources: <https://www.usgs.gov/programs/ecosystems-land-change-science-program/science/science-topics/drought-and-floods>, <https://www.usgs.gov/centers/washington-water-science-center/science/hydrologic-hazards>

## Priorities for this pass

### P0 blocker items before claiming Event 013 complete

These should be implemented in the next main-agent patch if Event 013 is meant to close after this pass.

1. Replace plain target random selection with a scored target pool or curated hazard groups.
2. Make warning availability vary by family and country capacity, with a no-warning path that can go straight to impact.
3. Add family-specific objective packets to every currently opened big-disaster category, using at least one family-specific mission or objective effect per category family group.
4. Give Evolution II and III real chain controllers for regional systems and abnormal families, with meteor clusters, delayed tsunami, massive rupture wave, massive eruption, and moving storm corridor behavior.
5. Put at least one registered animated sprite onto a gameplay or scripted GUI surface, with static fallback and no gameplay button hidden inside the visual.
6. Replace achievement auto-flags with richer tracked predicates.
7. Split the current generic Natural Disasters news into family or state specific news routing with global and family cooldowns.

If any of the seven items above are skipped, report Event 013 as incomplete. Do not call the skipped item polish.

### Quick items that should fit this pass

These reuse existing constants, categories, sprites, and helper shape.

- Use the existing `natural_disasters_target_score` constants as the first target scoring table.
- Add a small `decision_category` scripted GUI strip for active Event 013 categories rather than a full new recovery window.
- Add family-specific mission success and failure helper branches under the existing `natural_disasters_recovery_mission_success` and `natural_disasters_recovery_mission_failure` flow.
- Add state and country predicate variables for achievements at the same call sites that already set the simple achievement flags.
- Add 4 to 6 news events that reuse existing news sprites instead of requesting new art.

### Items that can stay queued after this pass

These are useful later, but they should not block the focused audit fix.

- A full forecast ledger with selectable state cards.
- More abnormal news images beyond the sprites already registered.
- Foreign relief diplomacy between countries.
- Occupied-state or collaboration-government disaster flavor.
- Curated world hazard state lists for every basin and volcano belt, if the scoring helper is implemented now.

## Target scoring and hazard groups

Current gap: `natural_disasters_select_target_state_for_current_family` chooses a family-specific random owned controlled state. The family triggers are better than a pure random state, but they still do not score the best hazard target. The event can hit a valid but low-value state while ignoring a capital, port, rail hub, dense state, active front, or unresolved aftermath.

### Implementation surface

Patch surfaces:

- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `events/013_natural_disasters.txt` only if scheduling needs to read the selected warning result
- `docs/events/013_natural_disasters.md` after implementation

The constants file already contains `natural_disasters_target_score`. Extend it instead of creating a second tuning group.

### Helper design

Add these helpers.

| Helper | Scope | Purpose |
| --- | --- | --- |
| `natural_disasters_clear_target_pool_marks` | Country | Clears temporary candidate flags and candidate score variables from owned states. |
| `natural_disasters_score_state_for_current_family` | State | Writes `natural_disaster_target_score` from base score, family match, population, buildings, ports, capital, supply, front strain, recent impact penalty, and active aftermath. |
| `natural_disasters_mark_scored_target_tier` | State | Converts the numeric score into flags such as `natural_disaster_target_tier_top`, `natural_disaster_target_tier_high`, and `natural_disaster_target_tier_valid`. |
| `natural_disasters_prepare_target_pool_for_current_family` | Country | Loops owned controlled states, scores valid candidates, and records whether at least one candidate exists. |
| `natural_disasters_select_scored_target_state_for_current_family` | Country | Selects top tier first, then high tier, then valid tier. Only if no tier exists may it return no target and let the sequence schedule another family. |

The helper may still use `random_owned_controlled_state`, but only inside a prefiltered tier. That gives variation without falling back to blind family randomness.

### Score factors

Use a readable score formula.

| Score source | Families affected | Direction |
| --- | --- | --- |
| `base` | All | Every candidate starts above zero. |
| Population divided by a constant | All deadly families | Dense states rise without hardcoded country lists. |
| Capital | All severe families | Capitals become important targets when valid, but not guaranteed. |
| Ports, dockyards, naval bases, island state | Cyclone, tsunami, flood, volcanic coastal wave | Coastal and naval infrastructure rises. |
| Rail, supply hub, low infrastructure | Flood, winter, landslide, rupture, corridor storm | Transport-sensitive states rise. |
| Mountain, hills, fault, volcanic candidate | Earthquake, rupture, landslide, volcano | Geological states rise. |
| Forest, drought, heat aftermath | Wildfire | Fire-prone states rise. |
| Desert, arid, drought aftermath | Dust, heat, drought | Arid states rise. |
| Airbase and radar | Dust, ashfall, severe storm, hail, meteor | Air disruption states rise. |
| Existing aftermath | Evolution II and III chains | Can deliberately revisit a stressed region. |
| Recent same-state impact | All unless chain requires same basin | Strong penalty, not a total block for chained disasters. |
| Scenario maximum | Abnormal families | Raises high-value target selection during Disaster Barrage. |

### Curated groups

Curated state flags are optional for this pass if scoring is implemented. If the main agent has time, add only the highest-value group seeds first.

Recommended first seeded flags:

- `natural_disaster_volcanic_candidate` for Japan, Indonesia, Italy, Iceland, Alaska, the Andes, Central America, the Philippines, New Zealand, and East Africa where state ids are already easy to verify.
- `natural_disaster_fault_candidate` for Japan, California, the Andes, Anatolia, Iran, the Himalayas, China, the Balkans, Italy, and New Zealand.
- `natural_disaster_cyclone_basin_candidate` for Caribbean, Gulf of Mexico, Bay of Bengal, South China Sea, western Pacific, Madagascar and Mozambique Channel, and northern Australia coastal states.
- `natural_disaster_tsunami_basin_candidate` for Pacific and Indian Ocean coasts, with Mediterranean and Caribbean as lower weight.

If curated flags are not seeded, the scoring helper must still work through terrain, coastal status, population, buildings, and existing aftermath. Do not block the patch on perfect global hazard geography.

## Warning availability by family and capacity

Current gap: every selected incident opens `chaosx.nr13.11`, calls `natural_disasters_open_warning_window`, and schedules impact. This makes sudden earthquakes, meteor impacts, and landslides feel as forecastable as cyclones and droughts.

### Implementation surface

Patch surfaces:

- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `events/013_natural_disasters.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `localisation/english/013_natural_disasters_l_english.yml`

Do not write final warning text in this addendum. Implementation should provide text direction only in docs before localisation work.

### Helper design

Add these helpers.

| Helper | Scope | Purpose |
| --- | --- | --- |
| `natural_disasters_prepare_warning_score_for_current_target` | State | Writes `natural_disaster_warning_score` from family base, evolution, severity, country capacity, buildings, stability, war state, prior preparedness, and active aftermath. |
| `natural_disasters_roll_warning_for_current_target` | State | Rolls a 1 to 100 variable and sets `natural_disaster_warning_available` or `natural_disaster_warning_missed`. |
| `natural_disasters_schedule_warning_or_impact` | Country | If the current target has warning available, fire `.11`. If not, fire `.21` after `natural_disasters_warning.missed_warning_days`. |
| `natural_disasters_apply_missed_warning_penalty` | State | Sets preparedness multiplier to `none`, opens the category only after impact, and adds a small aftermath multiplier for sudden families. |

Replace the `.10` direct state warning call with this flow.

### Family warning bands

Add constants in `natural_disasters_warning` or a new child table under it.

| Band | Families | Base direction |
| --- | --- | --- |
| Long warning | Drought, heat, winter, cyclone, massive eruption unrest | High base chance. |
| Short warning | Flood, wildfire, volcano, dust, severe storm, tsunami after known trigger | Medium base chance. |
| Unreliable warning | Landslide, earthquake, rupture, meteor, skyfall, corridor storm first tick | Low base chance. |
| Guaranteed warning only from chain | Delayed tsunami after a recorded quake, volcanic coastal wave, later corridor movement | Warning exists because a previous impact created the clue. |

### Capacity modifiers

Use country and state factors.

- Raise warning score if the country has high stability, no war, high infrastructure in the target state, radar or airbase for storm families, ports for coastal families, and prior Event 013 preparedness actions.
- Lower warning score if the country is at war, the target is occupied or low infrastructure, the sequence is Evolution III, the same country already has active aftermaths, or scenario maximum intensity is active.
- Never make warning score remove all danger. Preparedness changes loss rate and available actions, not impact existence.

### Player-facing effects

Warning available:

- `.11` appears.
- Family category opens immediately.
- Warning decisions are visible.
- The animated warning or family specific sprite can appear in the scripted GUI strip.

Warning missed:

- `.11` is skipped.
- `.21` appears after a short delay.
- Category opens after impact.
- Recovery actions are available, but warning actions are not.
- Achievements that require preparation do not progress.

## Family objective packets

Current gap: most categories have one warning action, one recovery action, and one mission routed through generic recovery helpers. The audit asks for family-specific objective mechanics. The main agent should implement objective packets rather than invent one-off bespoke code for every single decision.

### Shared objective model

Add a light objective data model on affected states and owner countries.

| Variable or flag | Scope | Use |
| --- | --- | --- |
| `natural_disaster_objective_family_id` | Country | Current family objective being resolved. |
| `natural_disaster_objective_type_id` | Country | Routes helper effects and scripted localisation. |
| `natural_disaster_objective_target_count` | Country | Number of states or tasks needed. |
| `natural_disaster_objective_progress` | Country | Progress from decisions, missions, or state cleanup. |
| `natural_disaster_objective_failure_pressure` | Country | Increases delayed deaths or follow-up chance on timeout. |
| `natural_disaster_objective_state` | State flag | Marks states that count for the objective. |
| `natural_disaster_objective_completed` | Country flag | Lets achievements and cleanup read success. |
| `natural_disaster_objective_failed` | Country flag | Lets failure packages avoid duplicate penalties. |

Add constants:

- `natural_disasters_objective_type.rail_belt`
- `natural_disasters_objective_type.port_reopen`
- `natural_disasters_objective_type.shelter_belt`
- `natural_disasters_objective_type.aftershock_inspection`
- `natural_disasters_objective_type.ash_clearance`
- `natural_disasters_objective_type.firebreak`
- `natural_disasters_objective_type.water_and_food`
- `natural_disasters_objective_type.airfield_clearance`
- `natural_disasters_objective_type.pass_rescue`
- `natural_disasters_objective_type.crater_cordon`
- `natural_disasters_objective_type.corridor_forecast`

### Helper design

Add these helpers.

| Helper | Scope | Purpose |
| --- | --- | --- |
| `natural_disasters_start_family_objective_packet` | Country | Reads target family and starts the matching objective type. |
| `natural_disasters_mark_objective_states` | Country | Marks affected states or selected neighbor states for objective tracking. |
| `natural_disasters_apply_family_objective_success` | Country | Routes success to family-specific recovery, achievement predicates, and cleanup. |
| `natural_disasters_apply_family_objective_failure` | Country | Routes failure to delayed deaths, state modifier extension, spread, or follow-up family pressure. |
| `natural_disasters_add_objective_progress_from_decision` | Country | Adds progress and checks completion. |
| `natural_disasters_cleanup_family_objective_packet` | Country | Clears flags, variables, and invalid objective marks. |

Existing decisions can call these helpers through their `complete_effect` and mission `timeout_effect`. Do not create a new wall of duplicate code inside each decision.

### Objective packet table

Use this as the implementation map. Each category needs at least one packet in this pass.

| Family category | First objective packet | Success | Failure |
| --- | --- | --- | --- |
| Flood Relief Authority | `rail_belt` plus contaminated water cleanup | Clears floodwater pressure and reduces delayed deaths. | Adds contaminated water deaths and can hit one neighboring lowland state. |
| Cyclone Emergency Command | `port_reopen` or island relief | Reopens port relief and lowers refugee pressure. | Keeps port closed and starts island food pressure if coastal or island. |
| Severe Storm Office | `airfield_clearance` or shelter belt | Removes airfield and radar disruption. | Flash flood or shelter pressure if flood-capable. |
| Hail Damage Board | harvest and airfield packet | Prevents famine linkage and shortens airfield damage. | Adds crop shock flag and can feed famine displacement. |
| Wind Damage Control | rail signal and shelter packet | Restores supply movement and limits industrial damage. | Extends production penalty and can start fire if heat or drought aftermath exists. |
| Storm Corridor Command | `corridor_forecast` | Raises forecast confidence, marks next path, and lowers next tick severity. | Next tick has missed-warning behavior and stronger refugee pressure. |
| Seismic Emergency Authority | `aftershock_inspection` | Clears aftershock watch and reduces bridge collapse. | Aftershock follow-up hits anchor or neighbor at lower severity. |
| Great Rupture Command | regional bridge and dam packet | Reduces secondary rupture wave and tsunami chance. | Another neighbor state is hit by reduced severity rupture or coastal wave if coastal. |
| Tsunami Coastal Command | `shelter_belt` plus port reopen | Clears coastal aftermath and lowers deaths. | Port remains closed and displaced population rises. |
| Volcanic Crisis Office | `ash_clearance` and water safety | Clears ashfall, reopens airfields, and lowers lahar chance. | Lahar or ashfall strikes one valley, river, or adjacent state. |
| Massive Eruption Command | regional ash and food corridor | Clears regional airfield closures and food transport pressure. | Ashfall extension, crop failure pressure, and possible coastal wave if anchor is coastal. |
| Firefront Command | `firebreak` | Stops spread and unlocks firebreak achievement predicates. | Fire spreads to neighbor or repeats on same state with lower warning. |
| Drought Famine Office | `water_and_food` | Reduces famine displacement and stabilizes supply. | Opens or strengthens Famine Displacement Commission. |
| Heat Emergency Office | shelter and water packet | Reduces delayed deaths and prevents wildfire link. | Adds wildfire risk and hospital overload pressure. |
| Winter Emergency Directorate | fuel and rail switch packet | Clears exposure pressure and rail penalties. | Exposure deaths and frozen rail extension. |
| Dust Emergency Office | `airfield_clearance` and well protection | Clears airfield closure and water contamination. | Dust aftermath extends and air operations stay disrupted. |
| Landslide Rescue Office | `pass_rescue` | Clears pass closure and trapped valley pressure. | Rescue teams trapped, supply penalty extends, neighbor valley risk rises. |
| Slope Collapse Response | mine and tunnel packet | Clears rail or mine collapse pressure. | Industrial or resource damage extends. |
| Skyfall Emergency Bureau | `crater_cordon` | Clears crater aftermath and limits fire starts. | Meteor dust, fire, or rail crater follow-up. |
| Meteor Storm Command | national shelter and crater network | Counts impact clusters, clears all crater states, and gates skyfall achievement. | Additional crater or fire impact, capped by active incident count. |
| Famine Displacement Commission | food column and shelter registry | Clears displacement and delayed deaths. | Disease or refugee pressure extends. |

### Decision and mission shape

For each category, keep the first pass lean.

- One warning action if the family can warn.
- One family-specific recovery action.
- One family-specific objective mission.
- One optional emergency action only for Evolution II or III categories.

Do not add every action from the old spec in this pass. The pass should deepen the category enough to stop being generic, then leave extra variants queued.

## Evolution II and III chain controllers

Current gap: Evolution II and III change incident count and family pool, but regional and abnormal behavior mostly uses generic neighbor impacts. The event needs family chains that remember why a later impact happened.

### Shared chain model

Add country variables:

- `natural_disasters_active_chain_family`
- `natural_disasters_active_chain_type`
- `natural_disasters_chain_stage`
- `natural_disasters_chain_remaining`
- `natural_disasters_chain_warning_quality`
- `natural_disasters_chain_anchor_state_score`

Add state flags:

- `natural_disaster_chain_anchor`
- `natural_disaster_chain_forecast_state`
- `natural_disaster_chain_impacted_state`
- `natural_disaster_chain_secondary_state`

Use regular state flags and country variables for delayed scheduling. Do not use persistent global event targets except for news, because global event targets require explicit cleanup and are easy to leak.

### Evolution II regional systems

Implement these first.

| Chain | Trigger | Behavior |
| --- | --- | --- |
| Regional flood system | Flood in Evolution II or higher | Anchor plus 1 to 3 neighbor states. Objective is rail belt and contaminated water. News only if death or state count threshold passes. |
| Cyclone landfall | Cyclone in Evolution II or higher | Coast impact, inland flood or port aftermath follow-up, island relief if island or high naval base. |
| Drought belt | Drought, heat, or dust in Evolution II or higher | Several arid or low infrastructure states gain water pressure. Failure opens famine displacement. |
| Seismic basin | Earthquake in Evolution II or higher | Anchor impact, aftershock watch, one neighbor aftershock. Coastal anchor can schedule delayed tsunami. |
| Volcanic ash region | Volcano in Evolution II or higher | Anchor eruption, one or two neighbor ashfall states, airfield and water objective. |

### Evolution III abnormal systems

Implement these without a world-end branch.

| Chain | Required behavior |
| --- | --- |
| Meteor cluster | The first skyfall impact marks a cluster anchor. The next 2 to 4 incident slots prefer dense, rail, airbase, or industrial states in the same country or neighboring states. Each impact increments `natural_disasters_meteor_cluster_impacts`. Meteor Storm Command opens only when the cluster has at least 3 planned or recorded impacts, or maximum scenario intensity is active. |
| Delayed tsunami | Earthquake, rupture, volcano, massive eruption, or meteor impact can set `natural_disasters_pending_tsunami_chain` when coastal or adjacent to coastal candidate states. The chain schedules a short warning window, then a tsunami impact against the highest scored coastal state in the owner or neighbor pool. Use `GFX_natural_disaster_tsunami_countdown_animated` in the GUI strip while pending. |
| Massive rupture wave | Rupture hits anchor, then one to three neighbor states at same or one lower severity. It should mark a bridge or dam objective and a possible coastal wave, but it must not create a world-end state. |
| Massive eruption | Massive eruption hits a volcanic anchor, applies ashfall to nearby states, can open famine displacement if recovery fails, and can schedule delayed tsunami only if coastal conditions exist. Use `GFX_natural_disaster_eruption_ashfall_animated` in the GUI strip while ashfall objective is active. |
| Moving storm corridor | Corridor storm creates a forecast state, a current path state, and up to 3 movement ticks. Each tick marks the next state before impact when warning exists. The player objective is to raise forecast confidence and shelter readiness before the next tick. Use `GFX_natural_disaster_storm_corridor_track_animated`. |

### Event schedule

Add small hidden event ids inside `events/013_natural_disasters.txt`, keeping one logged random event row.

Suggested working ids:

- `chaosx.nr13.40` chain continuation scheduler.
- `chaosx.nr13.41` delayed tsunami warning.
- `chaosx.nr13.42` delayed tsunami impact.
- `chaosx.nr13.43` storm corridor update.
- `chaosx.nr13.44` meteor cluster follow-up.
- `chaosx.nr13.45` ashfall or lahar follow-up.

These are hidden or report-style subordinate events. They must not call random event history recording. They should reuse sequence variables and cleanup.

## Animated gameplay surface

Current gap: Event 013 registers animated sprites but no gameplay or UI surface uses them.

### Recommended minimal surface

Build a read-only `decision_category` scripted GUI strip for Event 013 categories.

Patch surfaces:

- `interface/013_natural_disasters.gui` or the existing `interface/chaosx_decisions.gui`
- `common/scripted_guis/013_natural_disasters_scripted_gui.txt` or the existing `common/scripted_guis/chaosx_scripted_guis.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `interface/013_natural_disasters.gfx` only if sprite names need aliases
- `localisation/english/013_natural_disasters_l_english.yml`

Use the repo precedent from `holy_realm_mandala_category_scripted_gui`, `zzz_cure_progress_scripted_gui`, and `death_black_atlas_container`.

### GUI content

Working container id:

- `natural_disasters_category_status_strip_container`

Working scripted GUI id:

- `natural_disasters_category_status_strip_scripted_gui`

Context:

- `context_type = decision_category`
- `ai_enabled = { always = no }`
- visible for human players while any Event 013 category active

Elements:

| Element | Purpose |
| --- | --- |
| `natural_disasters_status_animation` | Shows the active animated family sprite, with static fallback when no active animation is needed. |
| `natural_disasters_status_header` | Working label direction only. Should name the active family or chain state through scripted localisation. |
| `natural_disasters_status_body` | Shows target state, warning quality, active aftermath count, and current objective in short dynamic text. |

Sprite routing:

| State | Animated sprite | Static fallback |
| --- | --- | --- |
| Generic warning available | `GFX_natural_disaster_warning_pulse_animated` | `GFX_natural_disaster_warning_pulse_static` |
| Delayed tsunami pending | `GFX_natural_disaster_tsunami_countdown_animated` | `GFX_natural_disaster_tsunami_countdown_static` |
| Moving storm corridor active | `GFX_natural_disaster_storm_corridor_track_animated` | `GFX_natural_disaster_storm_corridor_track_static` |
| Volcanic ash or massive eruption active | `GFX_natural_disaster_eruption_ashfall_animated` | `GFX_natural_disaster_eruption_ashfall_static` |
| Skyfall or meteor cluster active | `GFX_natural_disaster_skyfall_alarm_animated` | `GFX_natural_disaster_skyfall_alarm_static` |

The strip should not add clickable gameplay buttons in this pass. It exists to make warning, corridor, tsunami, ashfall, and skyfall state visible. Existing decisions and missions remain the gameplay layer.

If this surface cannot be wired cleanly, report it as a blocker rather than claiming the animations are used.

## Achievement predicate upgrade

Current gap: achievements mostly read a single flag set by broad events or generic mission success. They should track the hard path that the tooltip claims.

### Implementation surface

Patch surfaces:

- `common/achievements/chaos_redux_achievements.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/events/013_natural_disasters.md`

### Predicate plan

Do not remove the visible achievement ids. Replace simple unlock points with predicate variables and final unlock helpers.

| Achievement | Required tracked predicates |
| --- | --- |
| `achievement_nd_prepared_capital` | Target was capital, warning was available, at least two preparation actions taken before impact, final capital loss rate below threshold, and capital aftermath cleared. |
| `achievement_nd_no_deaths_sequence` | Sequence had at least two incidents, country was directly hit, sequence registered zero Natural Disasters deaths, no aftermath mission failed, and no missed warning occurred in the sequence. |
| `achievement_nd_tame_the_barrage` | Maximum Disaster Barrage launched, at least the maximum-intensity incident floor fired or safely skipped for no valid target, all Event 013 aftermaths cleared, and no world-end flag active. |
| `achievement_nd_firebreak_master` | Serious or stronger wildfire impact occurred, Firefront Command objective succeeded, no wildfire spread flag was set, and active fire aftermath cleared. |
| `achievement_nd_aftershock_control` | Earthquake or rupture at severe or stronger level occurred, aftershock objective succeeded, aftershock watch cleared, and no delayed tsunami from that chain struck the country. |
| `achievement_nd_skyfall_survivor` | Skyfall or meteor cluster produced at least three impacts or one extreme capital-adjacent impact, crater objective succeeded, all crater aftermath cleared, and the country retained control of its capital. |
| `achievement_nd_global_relief` | Relief corridor actions succeeded across at least three distinct family groups or three separate Event 013 sequences, and at least one severe or regional aftermath was cleared through relief rather than only shelters. |
| `achievement_nd_no_world_end` | Maximum barrage or Evolution III abnormal sequence completed, no world-end flag active, at least one abnormal family resolved, and all Event 013 ledgers cleaned. |

### Helper plan

Add a central helper:

- `natural_disasters_refresh_achievement_predicates`

Call it from:

- warning action success
- impact dispatch
- objective success
- objective failure
- sequence finish
- category cleanup
- maximum barrage cleanup watch

Keep per-achievement predicate variables named clearly, for example:

- `nd_ach_prepared_capital_actions`
- `nd_ach_sequence_registered_deaths`
- `nd_ach_sequence_missed_warnings`
- `nd_ach_meteor_cluster_impacts`
- `nd_ach_relief_family_count`

The final achievement `happened` blocks may still check final country flags if the helper sets them only after all predicates pass. Do not set those final flags in generic mission success.

## News routing

Current gap: `chaosx.news.84` is one generic major news event with one picture. The title has family dynamic text, but the description and image do not vary enough. News also needs family and state-specific throttling.

### Implementation surface

Patch surfaces:

- `events/_chaosx_news.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `localisation/english/013_natural_disasters_l_english.yml`
- `docs/events/013_natural_disasters.md`

### News event split

Do not rely on a dynamic picture unless the implementation agent verifies that the news event picture field supports it in the current pattern. The safe route is separate news ids with fixed pictures.

Suggested ids:

| Working event | Families | Picture |
| --- | --- | --- |
| `chaosx.news.84` | Generic severe sequence fallback | `GFX_news_event_generic_natural_disaster` |
| `chaosx.news.85` | Regional floods, cyclone flood, drought displacement if no better image | `GFX_news_event_nd_regional_floods` |
| `chaosx.news.86` | Rupture, earthquake regional system, delayed tsunami if no tsunami image exists | `GFX_news_event_nd_great_rupture` |
| `chaosx.news.87` | Massive eruption and volcanic ash region | `GFX_news_event_nd_massive_eruption` |
| `chaosx.news.88` | Meteor shower, skyfall, airburst field | `GFX_news_event_nd_meteor_showers` |
| `chaosx.news.89` | Moving storm corridor or tsunami if using existing generic art is acceptable | Use generic or the closest existing disaster news art. Do not request new art in this pass unless the parent expands asset scope. |

### Throttle rules

Add these flags.

- `natural_disasters_recent_news_report` as global all-family cooldown.
- `natural_disasters_recent_news_geological`
- `natural_disasters_recent_news_hydrologic`
- `natural_disasters_recent_news_volcanic`
- `natural_disasters_recent_news_skyfall`
- `natural_disasters_recent_news_corridor`

News eligibility should require at least one of:

- sequence estimated deaths above a threshold
- severe or extreme impact on a capital
- Evolution II regional system with at least 3 affected states
- Evolution III abnormal family
- manual high or maximum barrage
- port, supply hub, or major airbase destroyed in a key state

Store:

- `natural_disasters_last_news_family_id`
- `natural_disasters_last_news_severity_id`
- `natural_disasters_last_news_affected_states`
- `natural_disasters_last_news_estimated_deaths`

Use the existing `natural_disaster_news_state` global event target, but keep its cleanup in every news event option. If a news event cannot find a valid target, do not fire.

### Text direction

Localisation should be family and state specific, but implementation should not draft sensational all-purpose prose. The direction is:

- Flood and cyclone news should focus on rails, ports, shelters, wells, and displacement.
- Rupture and earthquake news should focus on bridges, hospitals, districts, aftershocks, and coastal watch where relevant.
- Tsunami news should focus on coastal evacuation, harbor works, islands, and delayed wave timing.
- Volcano news should focus on ash, airfields, water, lahar valleys, and food transport.
- Meteor news should focus on cratered rail, fire starts, shelters, and confused skywatch reports.
- Corridor news should focus on the path, forecast misses, shelter belts, and rail junctions.

Do not mention achievements, implementation changes, exact hidden score values, or world-end denial.

## AI behavior

The AI should use the same family objective system, not a human-only GUI.

Decision and mission weights should consider:

- target is capital or core
- severity id
- sequence evolution stage
- active aftermath count
- current war state
- target has port, supply hub, rail, airbase, or major industry
- country has enough equipment, trains, trucks, fuel, convoys, or manpower
- whether warning was available
- whether objective failure can create spread

Hard AI limits:

- AI should not attempt `corridor_disruption` style emergency actions if fuel and air XP are below gates.
- AI should prioritize tsunami evacuation over ordinary recovery when delayed tsunami is pending.
- AI should prioritize aftershock inspection before generic relief in Seismic Emergency Authority.
- AI should not spend itself into negative stability or war support for low severity hail, dust, or wind categories.
- AI should use relief corridors more aggressively when at war and the affected state has supply hub, rail, port, or capital status.

## Implementation order

1. Implement target scoring and warning variance first. These change the entire sequence quality and should be reviewed before family objectives.
2. Add the shared objective data model and wire objective packets to existing category decisions and missions.
3. Add Evolution II and III chain controllers, starting with delayed tsunami, meteor cluster, rupture wave, massive eruption, and storm corridor.
4. Add the read-only decision category scripted GUI strip and route the registered animated sprites.
5. Upgrade achievement predicate helpers and keep final achievement ids stable.
6. Split news routing and cooldowns.
7. Update docs and, after implementation facts exist, the spreadsheet through the proper spreadsheet worker.

## Acceptance criteria

The implementation can be accepted when all of these are true.

- No Event 013 incident uses plain random target selection without a scored or curated target tier.
- Warnings can be available, missed, or chain-guaranteed, and family/capacity factors drive that outcome.
- Every active big-disaster category has at least one family-specific objective packet with distinct success and failure behavior.
- Evolution II produces regional systems beyond one generic neighbor impact.
- Evolution III has recoverable abnormal chains for meteor clusters, delayed tsunami, rupture wave, massive eruption, and moving storm corridor.
- At least one registered Event 013 animated sprite appears on an Event 013 scripted GUI or decision-category surface, and it has a static fallback.
- Achievements are gated by tracked predicates, not only broad generic mission success or sequence cleanup flags.
- News events choose family-appropriate art and text direction, and both global and family cooldowns prevent spam.
- No world-end flag, world-end super-event, or terminal branch is added.
- No gameplay fallback is used silently. Any skipped packet, merged chain, missing GUI surface, or omitted news family is reported as incomplete or queued with a reason.

## Promotion guidance

If accepted, fold this addendum into these source spec files after implementation decisions are final.

- Target scoring and warning variance belong in `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec.md`.
- Objective packets belong in `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_big_disaster_decision_categories.md`.
- Evolution II and III chains belong in `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_evolutions_cluster_scenario.md`.
- GUI and animated sprite usage belongs in `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_recovery_gui_spec.md`.
- Achievement predicates should update `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_achievement_prompt.md` or a promoted achievement section.

Until the main agent either implements, promotes, queues, or rejects this addendum, do not run another improvement-loop pass for Event 013.
