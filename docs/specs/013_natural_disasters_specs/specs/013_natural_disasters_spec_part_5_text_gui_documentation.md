# Event 013 Natural Disasters Spec, Part 5, Event Map, Localisation Direction, GUI Detail, and Documentation Handoff

## Event namespace and subevent map

The exact event ids can change during implementation, but the event should keep one clear namespace around `chaosx.nr13.*`. Use this map as a design guide. Do not treat working titles as final localisation.

| Working event id | Working role | Player-facing | Log behavior | Notes |
| --- | --- | --- | --- | --- |
| `chaosx.nr13.1` | Entry and sequence setup | Yes, short season opening if the random event picker fires it directly | Records one Event 013 firing through shared pipeline | Hidden effects initialize sequence and first pulse |
| `chaosx.nr13.2` | Hidden sequence controller tick | No | No Event Log entry | Selects next family, target, and delay |
| `chaosx.nr13.3` | Hidden family application pulse | No | No Event Log entry | Applies state damage and deaths |
| `chaosx.nr13.10` | Baseline delayed disaster report | Yes | No Event Log entry | Names family and affected area after one to two days |
| `chaosx.nr13.11` | Repeat report digest | Yes, when needed | No Event Log entry | Used when a country has multiple local hits |
| `chaosx.nr13.20` | Evolution II global digest | Yes, selective | No Event Log entry | Summarizes major global hits without spam |
| `chaosx.nr13.30` | Delayed tsunami report and response window | Yes, only when warning is gameplay-relevant | No Event Log entry | Opens evacuation decisions before wave arrives |
| `chaosx.nr13.31` | Delayed tsunami impact | No or report after impact if severe | No Event Log entry | Applies tsunami family damage |
| `chaosx.nr13.40` | Aftershock or secondary wave | No by default | No Event Log entry | Can update disaster GUI |
| `chaosx.nr13.50` | Recovery completion or failure report | Yes, only severe or player-relevant | No Event Log entry | Reports aftermath result without listing hidden values |
| `chaosx.nr13.100` | Evolution I milestone | Yes if evolution event uses popup, otherwise logged view | Evolution log only | Unlocks diversified seasons |
| `chaosx.nr13.200` | Evolution II milestone | Yes if implementation chooses a milestone popup | Evolution log only | Unlocks global disaster systems |
| `chaosx.nr13.300` | Evolution III milestone | Yes if implementation chooses a milestone popup | Evolution log only | Unlocks abnormal families |
| `chaosx.nr13.310` | Meteor shower super-event driver | No normal popup | No Event Log entry beyond sequence | Sets super-event visibility and audio id |
| `chaosx.nr13.320` | Global rupture super-event driver | No normal popup | No Event Log entry beyond sequence | Integrates Event 046 concept |
| `chaosx.nr13.330` | Massive eruption super-event driver | No normal popup | No Event Log entry beyond sequence | Uses super-event package |
| `chaosx.nr13.340` | Storm corridor super-event driver | No normal popup | No Event Log entry beyond sequence | Opens or updates GUI |
| `chaosx.nr13.900` | Disaster Barrage launch wrapper | Scenario confirmation or hidden | Scenario record, then Event 013 row | Reads type and intensity |

The implementation should avoid using player-facing report events as the place where damage happens. Damage belongs in hidden effects or immediate hidden blocks. Report options can point the player to recovery actions and can show concise visible consequences, but they should not reapply damage.

## Report and news localisation direction by family

Final text should be concise, concrete, and area-specific. It should not use final text from this table. Use this as direction only.

| Family | Report viewpoint | Visible facts final text should mention | Avoid |
| --- | --- | --- | --- |
| Earthquake | Local survivors, rail crews, city rescue teams | affected state or region, collapsed roads or rail, damaged city districts, aftershock uncertainty | announcing hidden rupture values or generic apocalypse language |
| Flood | Flooded towns, river crossings, relief stations | river or lowland area, blocked roads, displaced people, contaminated water risk | calling it a warning or listing exact modifiers |
| Tropical cyclone | Coastal reports and port authorities | landfall, port damage, inland flooding, evacuation needs | repeating every small affected state in a global season |
| Thunderstorm | Local stations and airfield crews | severe storm, lightning, airfield or road disruption, flash-flood possibility | treating it as trivial flavor |
| Hailstorm | Rural districts and airfield crews | crop damage, shattered roofs, damaged aircraft or livestock where relevant | comedy that dismisses suffering |
| Extreme wind | Transport and shelter reports | roads blocked, buildings damaged, wind path uncertainty | replacing the event with a tornado movie tone |
| Wildfire | Evacuation crews and forest towns | advancing fire, smoke, closed roads, threatened settlements | modern climate-policy essay tone |
| Drought | Local crews, farms, supply columns | dry wells, failing crops, water distribution, fire risk | instant building-destruction wording |
| Sand and dust storm | Frontline and transport reports | low visibility, buried rails, airfields closed, supply disruption | copying old Event 099 text directly |
| Blizzard | Rail and shelter reports | blocked passes, frozen tracks, exposure deaths, troop supply | making it only a winter combat modifier |
| Heat wave | Hospitals, water crews, labor districts | heat exposure, water distribution, strained work, wildfire or drought risk | stacking wording with Event 051 |
| Cold wave | Shelter and rail reports | freezing exposure, fuel need, rail freeze, supply disruption | treating it as the Sun Moves Away event |
| Mass movement | Valley and rail reports | landslide, blocked pass, buried road or rail, isolated settlements | using the same text for wet and dry variants |
| Volcanic eruption | Evacuation and ash reports | ash, slope danger, airfield closure, water damage, lahar or tsunami risk | final title-like super-event phrasing for ordinary eruptions |
| Tsunami | Coast and port reports | wave arrival, port damage, displaced coastal population, water contamination | using it as ordinary flood text |
| Meteor shower | Regional shock reports or super-event | impact sites, fires, damaged rail or towns, skyfall uncertainty | presenting a quote or omen unless researched |
| Global rupture | Super-event or digest | widespread ground damage, broken transport, aftershock and coastal risk | reusing old Event 046 simple global building damage description |
| Massive eruption | Super-event or digest | ash cloud, evacuation, air closure, regional harvest or water pressure | generic end-of-world wording |
| Storm corridor | GUI report and super-event | current corridor, predicted path, uncertainty, action window | making the GUI a cosmetic map only |

## Option tone direction

Most report events need one practical option that acknowledges receipt and points to recovery. Affected human players should also receive a route into the response category. Severe reports can use a second option only when it represents a real policy split, such as immediate evacuation versus protecting industry, or shelters versus keeping a war corridor open.

Option tone should vary by severity.

- Minor report options can be dry, weary, or practical.
- Major reports should be serious and grounded.
- Abnormal disaster options should feel unnerving without telling the player that a hidden end state exists.
- Do not use final cultural references unless researched.

## Event Details direction

The Event Details window should explain Event 013 as a repeatable disaster season system in player terms. It should not list hidden damage tables. It should state that disaster seasons can hit states, regions, countries, coasts, river systems, and moving corridors, that severe local damage and deaths can occur, and that recovery tools can open afterward.

Evolution detail direction:

- Evolution I detail should describe broader and more varied disaster seasons.
- Evolution II detail should describe global disaster systems, chained aftermath, multi-state damage, and selective news.
- Evolution III detail should describe abnormal high-chaos disasters such as meteor showers, global rupture, massive eruptions, delayed tsunamis, and moving storm corridors. Use researched super-event text separately.

Cluster detail direction:

- Natural Disasters cluster details should explain that the cluster can schedule several Event 013 seasons, not that it triggers separate earthquake, flood, or storm event ids.

Scenario detail direction:

- Disaster Barrage scenario details should explain that the scenario uses the same controller, type options, intensity scaling, and recovery systems.

## Scripted GUI detailed design

The disaster map GUI should be useful at Evolution II and required at Evolution III. A normal decision category can carry baseline recovery, but the map helps with many active states, abnormal hazards, and moving corridors.

### Entry points

- Button in Disaster Response and Reconstruction category.
- Optional button in Event Details for active Event 013 season.
- Automatic opening is not required and could annoy players. Use a notification or category highlight instead.

### Header

Header fields:

- active season status
- current highest severity family
- number of active affected states
- current recovery pressure
- delayed death risk band
- next scheduled abnormal pulse when visible

The header should use dynamic scripted localisation and integer formatting for values that are conceptually integers.

### Left panel, active disaster list

The left panel shows active disaster cards. Each card should include:

- family icon
- affected state or region name
- phase, such as emergency, stabilization, reconstruction, or cleared
- danger band
- next follow-up risk if visible
- button to select that disaster card

For global seasons, this panel should page or filter. It must not show a huge wall of every affected state at once.

### Main map panel

The main panel shows a simplified event map or state-card map. It does not need a fully interactive world map if HOI4 GUI constraints make that costly. It can use a list of regional cards with state highlights.

Visible map states:

- affected now
- threatened next
- recovering
- cleared
- abnormal active
- hidden or unknown future path

Moving storm corridor state:

- current path marker
- predicted next path marker
- alternate uncertainty marker if the path can shift
- movement countdown or pulse stage

Delayed tsunami state:

- source event marker
- threatened coast marker
- arrival window band
- evacuation action state

Massive eruption state:

- eruption marker
- ash fall region
- lahar or tsunami threat if present

Meteor shower state:

- impact marker
- expected afterfall or fire risk marker

### Right panel, response actions

The right panel shows actions for the selected card.

Button groups:

- emergency response
- evacuation
- supply or route repair
- public health and shelter
- reconstruction
- request or send aid
- monitor or forecast follow-up hazard

Every gameplay button needs cost, requirement, effect tooltip, scripted effect, scripted trigger, AI equivalent, and cleanup. Decorative buttons can be disabled for AI.

### Animation states

Animated assets should clarify state.

- Storm marker moves or twists because the corridor is active.
- Warning pulse marks threatened next states.
- Eruption marker shows active ash and plume state.
- Meteor marker shows impact or afterfall state.
- Recovery shimmer is optional and should be skipped if it clutters the interface.

Use static fallbacks when animation is disabled, unsupported, or not yet produced.

## Documentation handoff

Implementation should create or update `docs/events/013_natural_disasters.md` after the event is implemented. The doc should include:

1. What Event 013 is.
2. Event map and subevents.
3. Sequence controller flow.
4. Disaster family catalogue.
5. Target selection and hazard profiles.
6. Deaths and building damage integration.
7. Report and news throttling.
8. Recovery decisions and missions.
9. Evolutions.
10. Cluster behavior.
11. Disaster Barrage scenario behavior.
12. Scripted GUI and animated asset hooks.
13. Super-event thresholds and source research status.
14. Event 046 and Event 099 placeholder conversion.
15. Event 051 non-stacking rule.
16. AI behavior.
17. Validation notes and limitations.

Do not leave the doc describing the old Reserved row or old Earth Earthquake logic.
