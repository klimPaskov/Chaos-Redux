# Event 033 Acid Rain, Part 10, assets, animation, and achievements

## Asset direction

The visual language should fit Hearts of Iron IV and Chaos Redux:

- 1930s and 1940s civil defense
- corroded steel, stained stone, damaged rail, contaminated reservoirs
- gray, yellow-brown, muted green, and rust-red weather palette
- heavy clouds and visible rain without neon science-fiction effects
- period masks, protective capes, shelters, pumps, trains, and field hospitals
- readable silhouettes at small icon sizes

Generated art is appropriate for event scenes, decision icons, state icons, map overlays, and achievements. Historical photographs can guide composition and equipment but should not be copied into generated final art without a license and source review.

## Event and report art

| Asset | Size | Suggested file direction | Use |
| --- | --- | --- | --- |
| Formation super-event | 457 by 328 | `gfx/event_pictures/super_events/033_acid_rain.dds` | Mandatory formation super-event |
| National arrival report | 210 by 176 | `gfx/event_pictures/033_acid_rain_arrival.dds` | First national exposure |
| Shelter response report | 210 by 176 | `gfx/event_pictures/033_acid_rain_shelter.dds` | Preparation success |
| Severe-cell report | 210 by 176 | `gfx/event_pictures/033_acid_rain_severe.dds` | Forecast or impact |
| Corroded transport report | 210 by 176 | `gfx/event_pictures/033_acid_rain_transport.dds` | Damage and recovery |
| Dissipation report | 210 by 176 | `gfx/event_pictures/033_acid_rain_dissipation.dds` | Event end |
| Global formation news | 397 by 153 grayscale | `gfx/event_pictures/news/033_acid_rain_news.dds` | Optional news surface |
| Global-layer news | 397 by 153 grayscale | `gfx/event_pictures/news/033_acid_rain_global_news.dds` | Evolution III milestone |

One report image can serve several closely related reports when the composition remains accurate. Do not create near-duplicate files without a clear presentation need.

## Decision icons

All decision icons are 32 by 32.

| ID direction | Image concept |
| --- | --- |
| Acid Rain category | Corrosive cloud above a shielded city |
| Shelter network | Sealed shelter door under rain |
| Protected water and food | Covered reservoir and sealed ration tin |
| Medical and protective capacity | Period respirator and medical cross |
| Transport resilience | Covered locomotive wheel and rail |
| Shelter protocols | Civil-defense siren and shelter arrow |
| Emergency water and food | Water drum under protective canopy |
| Medical surge | Field hospital under corrosive rain |
| Reroute transport | Branching rail arrows |
| Evacuate severe zone | Truck convoy leaving storm cloud |
| Restore transport | Rail wrench and repaired bridge |
| Decontaminate soil and water | Pump, barrel, and clean water symbol |
| Repair exposed industry | Factory and protective sheet |
| Demobilize emergency apparatus | Folded respirator and closed ledger |

Icons need a strong outer silhouette and no small text.

## State and idea icons

All use 64 by 64 source art before game conversion.

- standard regional acid rain
- strong acid rain
- severe storm cell
- global acid layer
- global superstorm
- aftermath tier 1
- aftermath tier 2
- aftermath tier 3
- national preparedness status if the interface requires an idea icon
- medical fatigue or emergency mobilization if a country modifier needs one

Aftermath tiers should share one visual family with increasing corrosion and contaminated runoff.

## Scripted-GUI assets

Required map package:

- neutral world map base
- seven exact region overlays
- visited-region overlay
- warning-region hatch
- ordinary active-region veil
- global-layer veil
- front marker frames
- severe-cell pulse frames
- warning pulse frames
- superstorm marker frames
- front-card background
- coverage-bar frame and fill
- preparedness badge and four component pips
- static fallback icons for every animation

Use separate masks where changing opacity or triggered visibility is enough. Use animation frames only where the image itself changes.

## Frame package

Suggested naming:

- `acid_rain_front_00.dds` through `acid_rain_front_11.dds`
- `acid_rain_warning_00.dds` through `acid_rain_warning_07.dds`
- `acid_rain_severe_00.dds` through `acid_rain_severe_07.dds`
- `acid_rain_global_00.dds` through `acid_rain_global_11.dds`

Final frame count must match sprite registration. Use zero-padded numbering and one manifest row per sequence.

Animation rates require in-game visual review. The ordinary front should move slowly, while the severe warning can pulse faster without strobing.

## GFX registration

Use one dedicated `interface/033_acid_rain.gfx` file where possible. Register:

- event images
- news images
- super-event image
- decision icons
- state and idea icons
- GUI map layers
- frame animations
- achievement icons

Every sprite ID must have one texture path and one owner. The asset manifest must flag any intentional reuse.

## Asset validation

For every DDS file record:

- source PNG path
- output DDS path
- expected dimensions
- actual dimensions
- alpha requirement
- compression mode
- mipmap rule
- sprite ID
- source or generation record
- visual inspection status

Reject blank, transparent, stretched, mislabeled, or wrong-size textures before implementation completion.

## Achievements

Event 33 requires difficult action-based achievements. The names below are identifier directions and writing prompts, not final localization.

### `acid_rain_033_before_the_first_drop`

- Goal: reach 100 Preparedness before the first controlled state receives an opening exposure shock.
- Eligibility: at least one controlled frozen eligible state at formation.
- Disqualifier: any opening shock before Preparedness reaches 100.
- Tracking: four component tier completion dates, first national shock date.
- Visibility: visible.
- Difficulty: high.
- Icon: fully shielded city beneath first falling droplets.

### `acid_rain_033_shelters_held`

- Goal: survive one severe cell affecting at least three controlled states with cumulative cell deaths below 0.05 percent of their combined population at forecast time.
- Eligibility: severe cell must resolve at least two exposure pulses.
- Disqualifier: evacuation or protection receipt missing from every target state.
- Tracking: severe episode population baseline, deaths, shelter protocol, evacuation.
- Visibility: visible.
- Difficulty: high.
- Icon: shelter door resisting red rain.

### `acid_rain_033_three_evacuations`

- Goal: complete valid evacuations in three separate severe forecast states and keep each state below its accepted severe casualty threshold.
- Eligibility: three distinct state IDs.
- Disqualifier: action completes after first severe pulse.
- Tracking: forecast ID, completion date, state deaths.
- Visibility: visible.
- Difficulty: high.
- Icon: three trucks beneath warning arrows.

### `acid_rain_033_railways_still_run`

- Goal: endure 120 cumulative national exposure days, complete at least three transport reroutes, and never let every rail route to the capital remain broken at a scheduled check.
- Eligibility: capital and at least five eligible controlled states.
- Disqualifier: capital supply isolation receipt.
- Tracking: national exposure-day accumulator, reroute completions, capital route checks.
- Visibility: visible.
- Difficulty: very high.
- Icon: locomotive crossing a corroded bridge.

### `acid_rain_033_under_one_sky`

- Goal: during Global Acid Rain, maintain at least 75 Preparedness for sixty consecutive days and keep the capital below aftermath tier 3.
- Eligibility: global layer occurs.
- Disqualifier: Preparedness below 75 on a scheduled daily or three-day check, capital reaches tier 3.
- Tracking: consecutive-day counter and capital aftermath maximum.
- Visibility: visible only after Evolution III begins.
- Difficulty: very high.
- Icon: globe under a shielded cloud layer.

### `acid_rain_033_after_the_clouds`

- Goal: clear every owned core-state Acid Rain aftermath within 180 days of global dissipation.
- Eligibility: at least three owned core states had aftermath.
- Disqualifier: any qualifying state remains unresolved at deadline.
- Tracking: frozen state list at dissipation, deadline, completion receipts.
- Visibility: visible.
- Difficulty: high.
- Icon: clean river and repaired factory beneath clearing clouds.

### `acid_rain_033_five_states_few_dead`

- Goal: finish acute exposure with at least five distinct controlled states touched and national Event 33 deaths below 0.10 percent of starting Event 33 national population.
- Eligibility: five distinct states and positive starting population baseline.
- Disqualifier: administrative early termination.
- Tracking: starting population, touched state count, actual deaths.
- Visibility: hidden until completion.
- Difficulty: very high.
- Icon: five state markers around a small casualty ledger.

### `acid_rain_033_small_state_civil_defense`

- Goal: as a country starting Event 33 with fewer than ten civilian factories, reach 60 Preparedness, survive first exposure, and finish with no tier-3 aftermath state.
- Eligibility: starting factory count fixed at formation and at least one eligible state.
- Disqualifier: receiving a direct country transfer intended only for debug or scenario setup.
- Tracking: starting factory band, peak Preparedness, aftermath maximum.
- Visibility: visible.
- Difficulty: high.
- Icon: small workshop shielding a town.

### `acid_rain_033_two_regions_ready`

- Goal: complete at least one valid urgent action before arrival in each of two different warned regions containing controlled states.
- Eligibility: country controls eligible states in two regions during separate warnings.
- Disqualifier: action starts after the front arrives.
- Tracking: region IDs, warning visit IDs, action completion dates.
- Visibility: visible.
- Difficulty: high for colonial or transregional countries.
- Icon: two continents joined by supply arrows under clouds.

### `acid_rain_033_no_severe_ruins`

- Goal: resolve every tier-3 Acid Rain aftermath state created under the country's responsibility before any remains at tier 3 for 180 days.
- Eligibility: at least one tier-3 state.
- Disqualifier: any qualifying state's tier-3 age reaches 180 days.
- Tracking: state entry date and downgrade receipt.
- Visibility: hidden until first tier-3 state.
- Difficulty: very high.
- Icon: corroded city restored before a marked deadline.

## Achievement integrity

- Every achievement uses stored event facts, not current modifiers alone.
- Tag switching follows the shared achievement ownership contract.
- Debug triggers and forced test bypasses set a disqualifier.
- Save and reload preserve baselines, deadlines, and disqualifiers.
- Cluster firing remains eligible unless an achievement explicitly requires independent firing.
- An achievement fires once and registers through the accepted achievement framework.
- Icon source and final 64 by 64 DDS are recorded in the asset manifest.

## Achievement interface

Event Details should list all Event 33 achievements with locked, available, completed, and disqualified status. Hidden achievements remain hidden until their reveal condition. Tooltips explain measurable requirements without exposing hidden random seeds.
