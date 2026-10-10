# Event 037: Mysterious People

## Part 5: Event chain, flavour, and reactions

## Event map

| ID | Role | Audience |
| --- | --- | --- |
| `chaosx.nr37.1` | Hidden entry that runs the world transaction | None |
| `chaosx.nr37.2` | Manifestation report, one per firing | Each human country with newcomers |
| `chaosx.nr37.3` to `chaosx.nr37.5` | Evolution reports, one per activated evolution | Human players |
| `chaosx.nr37.10` to `chaosx.nr37.26` | Flavour pool | One country, one state |
| `chaosx.news.42` | World news for the first manifestation only (rewritten) | Everyone |

There is no popup per state, per pressure tick, or per project.
AI countries resolve the same events silently through `ai_chance`.

## Manifestation report

`chaosx.nr37.2` merges the global and national report into one popup per human country.
It describes the worldwide arrival in a sentence or two, then the country's own share with its newcomers created and its largest hotspot, and it points to the decision category when pressure is Strained or higher.
After the first firing it says whether this wave was larger than the last.

Tone follows the stage: restrained curiosity at baseline, crowding and building at Evolution I, queues and empty shelves at Evolution II, and cities overflowing at Evolution III.

Sample opening line for a baseline firing: "Overnight, [ROOT.GetNameDef] has gained [?mysterious_people_country_created|0] people who say they have always lived here, and their neighbours cannot remember otherwise."

## Flavour selection

After each firing, every country with newcomers rolls once for a flavour event, delayed `20` to `60` days.
The candidate pool is the events whose conditions hold for one of the country's states.
An event that has fired for a country cannot fire for it again until four other flavour events have.
An event with no valid state never fires, and no event is starved while its conditions persist.

Every option has a visible, concrete effect on the values in Parts 2 to 4, or on stability, political power, or opinion.
Option magnitudes are planning anchors in the event's constants.
Each event below lists its trigger, its scene, and its options.

## Flavour pool

### Any stage

**`.10` The Village with Old Foundations.** Rural state with a recent grant and no crisis.
A complete village stands where the county map showed open fields, with weathered foundations and mature orchards.
Options: register the village and connect it to the district (`10` political power, settles `15%` of the state's unsettled newcomers), or leave it to the county (no effect).

**`.11` The School Nobody Opened.** Populated state with an unregistered school among the newcomers.
A teacher arrives with forty pupils and knows every family in the district by name, though the town never built a school there.
Options: keep the school open and pay the teacher (settlement in the state `x 1.25` for `180` days), or close it until the children are registered (no effect, and Open Integration countries lose `1%` stability for `60` days).

**`.12` The Unknown Relative.** State at Absorbing or Strained.
Families across the region are visited by cousins and aunts who remember shared holidays that only one side recalls.
Options: let families take them in (settles `10%` of the state's unsettled newcomers), or ask the police to check every visitor (`+1%` stability for Restricted Registration countries, settlement in the state `x 0.75` for `90` days).

**`.13` The Road Everyone Uses.** State with infrastructure `3` or more and a recent grant.
Drivers use a road to the new settlements as if they had driven it for years, though it appears on no survey.
Options: add it to the national road plan (the next Extend Roads and Water in this state costs half), or close it until surveyed (no effect).

**`.14` The Factory Shift.** State with at least one factory and pressure below Overcrowded.
A full shift walks into a factory and starts work, and the foreman remembers hiring every one of them.
Options: keep the line running (factory output `+3%` for `90` days, settlement in the state `x 0.75` for `90` days while the workers live on the factory floor), or send them home until housing is found (no effect).

**`.15` Graves for Living Families.** State where newcomers are at least `30%` of the population.
The town cemetery holds generations of graves belonging to families who arrived last month, with stones as worn as their neighbours'.
Options: leave the graves in peace (settles `10%` of the state's unsettled newcomers), or exhume and examine them (`-2%` stability for `90` days, no other result).

**`.16` Two Families, One House.** Urban state at Strained or higher.
Two unrelated families hold keys to the same house, each with photographs of their children growing up in its rooms.
Options: split the house and pay for a second one (`15` political power, the next Emergency Housing in this state costs half), or rule for the older family (`-1%` stability for `60` days).

**`.17` The Wedding Guests from Abroad.** Two countries with newcomers whose relations are not hostile.
Families in two distant countries recognize each other in newsreel footage and swear they attended the same wedding before the war.
Options: let the families write and visit (`+15` opinion with the other country), or censor the newsreel (no effect).

### Evolution I and later

**`.18` New Districts by Morning.** Urban hotspot with a grant from the latest firing.
Whole streets of shops and flats fill empty lots on the edge of the city, and the trams stop short of them.
Options: extend the tram lines (`25` political power, the state's settlement `x 1.25` for `180` days), or let the districts fend for themselves (no effect).

**`.19` Work Without Homes.** Industrial hotspot at Strained or higher.
The factories have hired every newcomer who asked, and their families sleep in warehouses and rail yards.
Options: keep production first (factory output `+3%` for `90` days, stability `-1%` for `90` days), or open the warehouses as dormitories (settles `15%` of the state's unsettled newcomers, factory output `-2%` for `60` days).

### Evolution II and later

**`.20` Grain for People Who Were Not Here.** Hotspot at Emergency where the Famine owner records supply strain or worse.
Bakeries run out by mid-morning, and the queues include families nobody in the district remembers.
Options: ration everyone equally (stability `-2%` for `90` days), or feed long-time residents first (Restricted Registration only, stability `+1%` for `90` days, and settlement in the state `x 0.5` for `180` days).
The Famine owner keeps every food value, and this event only names the cause.

**`.21` The Station Never Empties.** Hotspot at Breakdown with an active Migration flight request.
Families crowd the main station faster than trains can carry them away, and many hold tickets dated before they arrived.
Options: run extra trains (`25` political power, the state's Event 037 flight request doubles for `30` days), or close the station (the state sends no flight request for `60` days and its pressure stays).

**`.22` A City Asks for Entry Limits.** Urban hotspot at Emergency.
The mayor asks for power to turn newcomers away at the city limits.
Options: grant the limits (`+2%` stability for `180` days, settlement in the state `x 0.5` for `180` days), fund the city instead (`50` political power, settles `20%` of the state's unsettled newcomers), or refuse (`-2%` stability for `60` days).

### Evolution III

**`.23` The Majority Nobody Remembers Meeting.** State where newcomers exceed half the population.
Most families in the province now belong to households that arrived through the manifestations, and the old residents cannot say when that happened.
Options: hold local elections on the new rolls (settlement in the state `x 1.5` for `180` days, `-1%` stability for `60` days), or suspend the local council (`+1%` stability for `60` days, settlement in the state `x 0.5` for `180` days).

**`.24` A Government Counts Origins.** National pressure at Overcrowded or higher, and the country is not a democracy.
Ministers propose marking every household by whether it arrived through the manifestations.
Options: reject the register (`-3%` stability for `90` days), or adopt it (switches the stance to Restricted Registration at once without the political power cost, `+3%` stability for `90` days, `+5` world tension, and settlement in every state `x 0.75` for `365` days).

**`.25` The Second Capital.** The capital is a hotspot at Emergency or worse.
A complete government quarter has appeared beside the capital, staffed by clerks who insist the ministries have always worked from there.
Options: put the quarter to work (`50` political power, settles `25%` of the capital's unsettled newcomers), or clear it (`-3%` stability for `90` days).

**`.26` The Country That Managed.** Evolution III, newcomers at least `25%` of the country, and national pressure below Strained for `180` days.
Cities, farms, and schools built for the newcomers now run like any others.
Option: one acknowledgement option granting `+5%` stability and the workforce bonus doubled for `365` days, once per country.

## Cross-event callbacks

A flavour event may add one line when a related event has fired, such as an Event 019 soldier recognizing a village or an Event 030 traveller's papers contradicting a family history.
Callbacks change no outcome and never explain the newcomers.

## Writing direction

Write about people, homes, streets, work, and food.
Records, deeds, and archives may appear as supporting detail and are never the centre of a scene.
Follow the event writing rules in `.claude/skills/chaos-redux-events/SKILL.md`, including no staged contrasts between observations and official reactions.
Final localisation uses dynamic country, state, population, and stance context, and the working titles above may change.

## Event-chain acceptance statement

Repeated firings produce varied, state-specific scenes while the origin stays unexplained.
Every option changes something the player can see in the category, and no event replaces population, pressure, Famine, or Migration mechanics with text.
