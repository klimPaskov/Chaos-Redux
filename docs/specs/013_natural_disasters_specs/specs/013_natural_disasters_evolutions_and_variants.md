# Event 013 — Natural Disasters: Evolutions, Variant Catalogue, and Chaining

## Evolution philosophy

Natural Disasters uses evolutions as mutation tracks, not ordinary stage labels. A baseline disaster is not an evolution. A flood causing a recovery mission is not an evolution. An evolution means the event has learned a new pattern: more disaster families, wider affected areas, chained aftermaths, and finally abnormal high-chaos disasters.

Each evolution can enter in two ways:

- **Active-event evolution:** if Event 13 has already fired, the next eligible disaster cycle can use the unlocked behavior immediately. Existing active aftermaths may receive new follow-up risk, such as famine after drought or tsunami after earthquake.
- **Pre-fire evolved opening:** if Event 13 has not fired yet when the world is already chaotic, the first Natural Disasters firing can start with the evolved package instead of beginning as a single calm-world local incident.

The event should have four evolutions from the user brief. There is no need for Evolution V unless later accepted design adds a fifth stage.

## Baseline — Local Disaster Report

**Core identity:** one disaster strikes one clearly named state, small area, country, or local region.  
**Severity:** low to moderate.  
**Player feeling:** a serious local emergency, not a global apocalypse.  
**Main result:** local industry and population damage plus an optional recovery path.

### Baseline eligible families

Baseline should start with a limited pool so early campaigns do not feel like every possible disaster is already active:

- earthquake;
- flood;
- storm or blizzard;
- drought/crop failure;
- landslide/avalanche;
- limited wildfire;
- rare volcanic unrest only in curated volcanic regions.

Meteor shower, global earthquake wave, traveling tornado chains, massive volcanic winter-like ash, and continent-wide variants are locked behind later evolutions.

### Baseline warning examples

- river gauge reports rising water near a named basin;
- storm offices warn coastal states;
- seismographs report unusual tremors but no exact prediction;
- drought observers warn that granaries are not matching public reports;
- volcanic observatories warn of ash and evacuation zones.

### Baseline aftermath examples

- factory district cracked: local building repair pressure;
- rail embankments flooded: supply and rail recovery mission;
- harvest failure: relief train/convoy decisions;
- wildfire perimeter: evacuate workers or lose more population;
- volcanic ash: clear airfields and protect water supplies.

## Evolution I — The Weather Office No Longer Sleeps

**Short catalogue label:** Varied Local Disasters.  
**Unlock theme:** disasters become more varied while staying local.  
**Minimum chaos direction:** early chaos tier, but the exact trigger should consider prior disaster count, recent weather/geologic memory, and active instability.

Evolution I expands the local catalogue and allows small bursts: selected few disasters can fire at once, slightly delayed from each other. The effects are only slightly stronger than baseline; the danger comes from overlap and variety.

### New behavior

- The event can queue a **local disaster burst** of two to four incidents.
- Incidents are delayed by a few days or weeks rather than firing all on the same tick.
- The burst tries to avoid hitting the same exact state unless it is a chain family such as earthquake aftershock or flood following storm.
- The burst can mix disaster families: storm + flood, drought + wildfire, earthquake + landslide, volcanic unrest + ashfall.
- Warning events become more common and more specific.
- The Events detail window should describe that disaster reports no longer arrive as isolated accidents.

### Evolution I family additions

- storm surge and port storm;
- wildfire after drought;
- dam strain and local dam failure;
- avalanche and mountain-pass collapse;
- crop blight/famine pressure as drought aftermath;
- ashfall from volcanic unrest.

### Evolution I active-event path

If any state currently has a disaster aftermath modifier, Evolution I unlocks follow-up chances tied to that aftermath. Examples:

- `flooded_transport_belt` can produce a disease/water-safety relief mission;
- `crop_failure_pressure` can produce a refugee movement report;
- `recent_earthquake_damage` can produce aftershocks;
- `volcanic_ashfall` can produce airfield closure.

These should be event-driven follow-ups from disaster impact or recovery expiration, not a new daily world scan.

### Evolution I pre-fire opening

If Event 13 first fires after Evolution I is unlocked, the first incident should be a small burst rather than one isolated disaster. This opening demonstrates the evolution immediately.

### Suggested event families inside Evolution I

| Burst archetype | Incidents | Notes |
| --- | --- | --- |
| Broken River Week | storm warning, flood, bridge/rail failure | Names a basin or lowland region. |
| Dry Wind Season | drought, wildfire, relief train mission | Uses slow-burn aftermath. |
| Mountain Collapse | earthquake, landslide, pass closure | Good for mountainous states. |
| Ash and Rain | volcanic unrest, ashfall, flood/landslide | Only in volcanic regions. |
| Winter Severance | blizzard, rail closure, supply mission | Good in cold regions. |

## Evolution II — Regional Disaster Systems

**Short catalogue label:** Regional Disaster Systems.  
**Unlock theme:** disasters can affect a wider region instead of one state or country.  
**Minimum chaos direction:** Rising Chaos or equivalent disaster memory.  
**Player feeling:** the disaster is no longer a local bulletin; it is a recurring world condition.

Evolution II allows almost all baseline disasters to hit and makes them stronger. The key change is regional scope and layered effects: neighboring states take building damage, larger population loss, temporary supply penalties, and local recovery modifiers.

### New behavior

- The event can choose a **regional footprint**: one anchor state plus neighboring states, coastal chain, river basin, mountain belt, or administrative region.
- The anchor state receives the strongest hit. Secondary states receive lighter damage and shorter modifiers.
- Regional incidents can cross borders if the physical disaster supports it. Border-crossing should be clearly named and logged.
- Recovery becomes regional: one country may need to help several states, or multiple countries may receive smaller response decisions.
- Disaster memory should increase future weighting for follow-up families while the aftermath is active.

### Regional footprint types

| Footprint | Disaster families | Player-facing name style |
| --- | --- | --- |
| River basin | flood, dam failure, storm rain | “The [river/basin/local region] flood” |
| Coastal belt | cyclone, tsunami, storm surge | “The [coast/sea] surge” |
| Mountain belt | earthquake, avalanche, landslide | “The [mountain/pass] collapse” |
| Dry belt | drought, heat, wildfire | “The [plain/steppe] dry season” |
| Volcanic zone | eruption, ashfall, lahar | “The [volcanic region] ashfall” |
| Industrial corridor | earthquake, firestorm, flood | “The [city/rail/factory belt] disaster” |

### Regional aftermath

- temporary supply penalties on affected states;
- regional recovery modifiers that can be reduced by missions;
- displaced population pressure on the controller or nearby countries;
- larger death tracking than baseline;
- small chaos increase when multiple countries are hit;
- reduced local stability or war support in the affected country when relief fails.

### Evolution II active-event path

Existing aftermath can widen if ignored:

- an ignored flood can become regional water crisis;
- an ignored drought can become famine pressure;
- earthquake-damaged rail can isolate neighboring states;
- ashfall can close several airbases;
- storm-damaged ports can create convoy disruption.

### Evolution II pre-fire opening

If first firing starts at Evolution II, choose one regional footprint and queue two to five incident reports over a short period. The first event should name the wider region immediately.

## Evolution III — Chained Aftermaths and Continent Pressure

**Short catalogue label:** Disaster Chains.  
**Unlock theme:** disasters begin chaining or leaving aftermath.  
**Minimum chaos direction:** Chaos Tier or a high disaster-memory threshold.  
**Player feeling:** the event is becoming a condition of the world rather than a random local hit.

Evolution III introduces chained aftermaths: famine, refugee pressure, damaged infrastructure, reduced local stability/war support, and continent/region-wide variants.

### New behavior

- Disasters can have **primary impact** and **secondary aftermath** separated by days or weeks.
- Regional chains can produce continental pressure without hitting every state.
- Affected countries receive decisions to help neighbors, close borders, accept refugees, rebuild rail corridors, or exploit rival disasters.
- Relief failure matters more: not every failure is catastrophic, but ignored evolved disasters should leave political and population consequences.
- The event can generate several reports under one logged disaster chain, but the event log should distinguish the original disaster and the follow-up.

### Chain families

| Primary disaster | Possible chained aftermath | Gameplay role |
| --- | --- | --- |
| Earthquake | aftershocks, landslide, tsunami, refugee pressure | acute damage and follow-up risk |
| Flood | disease/water pressure, bridge collapse, crop failure | supply and population pressure |
| Storm surge | port closure, convoy disruption, refugee pressure | naval/logistics disruption |
| Drought | famine, wildfire, migration, stability loss | slow crisis and relief management |
| Volcanic eruption | ashfall, lahar, crop failure, aviation disruption | regional environment pressure |
| Wildfire | smoke, displaced workers, industry shutdown | factory and population disruption |
| Meteor fragment | fires, panic, tsunami if offshore | high-chaos bridge to Evolution IV |

### Continent and macro-region variants

Evolution III can create continent/region-wide disaster variants, but they should still be implemented as a sequence of selected footprints rather than one blanket modifier across every state. Examples:

- **Pacific Rim Tremor Chain:** several coastal/mountain states around the Pacific receive earthquakes, ashfall, or tsunami warnings.
- **Monsoon Failure Belt:** selected South/East/Southeast Asian or African agriculture states suffer drought and crop pressure.
- **Atlantic Storm Year:** several coastal storm events hit different countries.
- **Steppe Fire Season:** drought followed by wildfire across selected steppe states.
- **Northern Ice Break:** blizzards, avalanches, and rail shutdowns in high-latitude states.

These variants should name the macro-region and still list affected areas clearly.

### Evolution III active-event path

Existing baseline and Evolution I/II aftermaths can receive delayed chain events. The chain should respect a maximum active chain count so the event does not overload the player with every possible follow-up at once.

### Evolution III pre-fire opening

If Natural Disasters first fires at Evolution III, open with one regional disaster and one delayed aftermath already scheduled. The player should understand that the first report is not the whole incident.

## Evolution IV — Abnormal Disaster Age

**Short catalogue label:** Abnormal Disaster Age.  
**Unlock theme:** meteor showers and more intense natural disasters.  
**Minimum chaos direction:** Totalen Chaos or World Collapse tier, with disaster memory and manual scenario support.  
**Player feeling:** the world is still not ending, but natural systems now behave as if they have joined Chaos Redux.

Evolution IV escalates from normal disasters into abnormal high-chaos disasters. It is dramatic enough to deserve super-event consideration, but it must not become a world-end scenario.

### New behavior

- Meteor showers can hit several states.
- Stronger earthquakes damage many buildings across a region or several regions.
- Severe storms, sandstorms, ash storms, acid-rain-like high-chaos storms, or wildfire smoke can linger as state modifiers.
- Massive volcanic activity can devastate selected volcanic regions and create ashfall/crop effects in neighboring states.
- Earthquake aftermath can produce delayed tsunamis.
- Traveling tornado or storm paths can move through a sequence of states, damaging each one in turn.
- The absorbed Event 46 Earth Earthquake concept becomes a rare abnormal earthquake wave variant.

### Required absorption of Event 46

Event 46 “Earth Earthquake” should be reduced to an unknown placeholder. Its old global slight-building-damage concept is reimplemented here as **abnormal earthquake wave**:

- It should not damage every building in every state silently.
- It should choose several regions or state groups, name them, and apply scaled damage.
- It can have aftershocks and tsunami follow-ups.
- It should be logged under Event 13 and Evolution IV.
- It should be available from maximum manual scenario intensity.

### Evolution IV abnormal variants

| Variant | Scope | Effects direction | Notes |
| --- | --- | --- | --- |
| Meteor Shower | several states, possibly several countries | building damage, population loss, fires, crater modifier | Should not duplicate Event 28 large asteroid plot. |
| Abnormal Earthquake Wave | several regions | buildings, infrastructure, supply, casualties, tsunami chance | Absorbs Event 46. |
| Massive Volcanic Eruption | volcanic region plus downwind ash states | devastation, ashfall, airbase disruption, crop pressure | Strong super-event candidate. |
| Traveling Tornado Chain | path of adjacent states | light/medium damage in each state, heavy in one anchor | Good for high-chaos spectacle. |
| Black Rain / Acid-Rain-Like Storm | several industrial/contaminated states | temporary supply, production, population, air-cleanliness pressure | Must be a high-chaos natural/abnormal weather effect, not chemical weapon condemnation. |
| Hyperstorm Coastline | coastal belt | ports, naval bases, dockyards, convoys, population | Can be tied to storm surge maps and warnings. |
| Ash Winter Season | macro-region | crop failure, air disruption, supply penalties | Not a world-end nuclear winter. |
| Earthquake-Tsunami Delay | earthquake first, coastal follow-up later | coastal destruction after warning | Player can mitigate if warned. |

### Evolution IV active-event path

Existing regional disaster chains can mutate into abnormal variants if chaos is high enough. Example paths:

- repeated earthquakes unlock abnormal earthquake wave chance;
- volcanic unrest unlocks massive eruption;
- meteor warning reports unlock meteor shower;
- drought/wildfire chains unlock black rain or smoke season;
- coastal storm season unlocks hyperstorm coastline.

### Evolution IV pre-fire opening

If Event 13 first fires while Evolution IV is already available, do not waste the first firing on a single small flood. Start with a high-chaos disaster burst: one major abnormal incident plus several smaller local or regional incidents in a compressed window.

### Super-event role direction

Evolution IV can fire a super-event for the first abnormal disaster burst or first massive volcanic/meteor/earthquake wave. The super-event role is **global recognition that natural disaster reports have become a recurring high-chaos world condition**. The super-event must use research gates for final title, quote, button remark, and audio. It is not a world-end super-event.

### Manual scenario maximum variant

Maximum manual scenario intensity should be allowed to fire several Evolution IV variants in sequence. This is the custom manual triggerable scenario requested by the user: it fires all or almost all disaster families in a short period. The sequence should have cooldown cleanup and should avoid corrupting ordinary random-event pacing afterward.

## Variant implementation matrix

| Disaster family | Baseline | Evolution I | Evolution II | Evolution III | Evolution IV |
| --- | --- | --- | --- | --- | --- |
| Earthquake | one state | aftershock/landslide burst | regional fault belt | tsunami/refugee chain | abnormal earthquake wave |
| Flood | one state/basin | storm-flood burst | river basin | disease/crop/refugee chain | continent-scale flood season in selected basins |
| Storm | one coastal/plain state | storm + flood/surge | coastline or winter front | port closure and refugee chain | hyperstorm/traveling storm path |
| Drought | one agricultural state | drought + wildfire | dry belt | famine/refugee chain | ash/dust/water-collapse season |
| Wildfire | limited | after drought | regional fire season | smoke and displacement | firestorm under meteor/black rain variants |
| Landslide | local | aftershock/avalanche | mountain belt | pass isolation | massive mountain collapse after abnormal quake |
| Volcano | rare unrest | ashfall | volcanic region | lahar/crop chain | massive eruption/ash winter season |
| Tsunami | rare follow-up | earthquake chain | coastline chain | refugee/port closure chain | delayed mega-tsunami after abnormal quake/meteor |
| Meteor | not normal | rare warning only | rare fragment | fragment chain | meteor shower and crater fields |

## Evolution log wording directions

The evolution log should use player-facing names that describe the pattern, not mechanical stage numbers. Suggested names are design labels, not required final localisation:

1. **Varied Local Disasters** — local disasters diversify and can arrive in small delayed bursts.
2. **Regional Disaster Systems** — disasters can cover named regions, basins, coastlines, or mountain belts.
3. **Disaster Chains** — first impacts can leave famine, refugee, tsunami, infrastructure, or stability aftermaths.
4. **Abnormal Disaster Age** — meteor showers, massive eruptions, abnormal earthquake waves, and high-chaos storm paths become possible.

Each evolution detail should explain what the player sees. It should avoid listing exact modifiers.

## Repetition and pacing limits

Natural Disasters can become intense, but it should not become a spam machine. Use these design controls:

- maximum active disaster aftermaths per country before new disasters prefer other targets;
- family cooldown per state and per region;
- burst queue cap by evolution stage;
- recovery decision active cap;
- warning cap so the player is not buried in alerts;
- manual scenario flag that safely permits temporary burst intensity without permanently loosening automatic caps;
- high-chaos exception only for Evolution IV.

## Balance intent by evolution

| Stage | Player impact | Balance guardrail |
| --- | --- | --- |
| Baseline | one noticeable local hit | not campaign-ending, recovery optional |
| Evolution I | multiple local hits | damage only slightly stronger; danger is overlap |
| Evolution II | regional footprint | anchor/secondary scaling prevents full-region deletion |
| Evolution III | chained aftermath | caps on active chains; recoveries prevent runaway |
| Evolution IV | abnormal spectacle | rare, high-chaos, named, super-event-worthy, not terminal |
