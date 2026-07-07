# Event 013 Natural Disasters, Part 4, aftermath decisions and UI

## Aftermath category purpose

The aftermath category is the player management surface for active disaster recovery. It should appear reliably for affected countries after a serious impact. It should not be a hidden cleanup menu.

The category should show current active disaster cards. Each card should name the family, affected state or regional set, severity direction, damage type, recovery needs, chain risk, and cleanup state. The player should understand what must be done now and what may happen if recovery fails.

## Opening and notification behavior

A serious impact should do three things for the affected country.

1. Deliver a delayed report event 1 to 2 days after impact.
2. Show or refresh the decision category notification.
3. Activate the relevant aftermath card and first recovery decisions.

This must happen even if the disaster came from the reusable system, an external event call, the Disaster Barrage scenario, or an abnormal Evolution III chain. The notification path should not depend on Event 013 being the random event source.

## Category state groups

The category can be separated into these groups.

| Group | Purpose |
| --- | --- |
| Active disasters | Cards for each current impact or regional system. |
| Immediate rescue | Short urgent actions that lower delayed deaths and chain risk. |
| Transport recovery | Rail, infrastructure, ports, supply hubs, and airfields. |
| Population relief | shelter, food, medicine, evacuation, refugees, and sanitation. |
| Family-specific work | flood barriers, firebreaks, ash cleanup, winter fuel, water trains, crater security, volcanic valley evacuation. |
| Reconstruction | Longer building repair and recovery missions. |
| Foreign relief | Aid intake, aid corridors, convoy support, and diplomatic help. |
| Aftermath closure | Final cleanup once recovery thresholds are met. |

## Decision design standards

Disaster decisions should use resources that match the action. Political power can appear when the action is administrative, but it must not be the default cost.

| Decision family | Cost palette | Result direction |
| --- | --- | --- |
| Search and rescue | manpower, support equipment, trucks, fuel, command power | lowers delayed deaths and rescue failure risk. |
| Rail clearance | trains, support equipment, civilian capacity, army XP for engineers | restores rail and supply, reduces famine and supply collapse. |
| Port closure | navy XP, fuel, convoys, dockyard disruption | lowers cyclone, tsunami, ash, and storm surge losses. |
| Evacuation | trains, convoys, trucks, fuel, manpower, stability | lowers direct deaths but creates refugee pressure and temporary economic disruption. |
| Medical corridor | support equipment, manpower, trucks, convoys | lowers disease and exposure chains. |
| Food corridor | trains, convoys, civilian capacity, stability | lowers famine and refugee death chains. |
| Firebreaks | fuel, trucks, manpower, local support | lowers wildfire spread and industry loss. |
| Ash cleanup | support equipment, manpower, air mission disruption | restores airfields and lowers respiratory and famine chains. |
| Winter fuel line | fuel, trains, trucks, support equipment | lowers cold deaths and factory disruption. |
| Water trains | trains, fuel, support equipment, civilian capacity | lowers drought, heat, and dust death chains. |
| Observatory watch | air XP, radar or airfield presence, command attention | improves warning odds and lowers volcanic, meteor, or tsunami surprise. |

## Timed missions

Timed missions should ask the player to do real work, not passively wait.

| Mission | Objective direction | Suitable families | Success | Failure |
| --- | --- | --- | --- | --- |
| Hold relief railheads | Keep supply and rail access in named affected states | flood, quake, blizzard, cyclone | lowers transport aftermath and delayed deaths | supply collapse chain and larger repair cost |
| Keep the port open or closed as ordered | Maintain naval access or prevent port use during danger | cyclone, tsunami, ash | lowers coastal disruption | port damage and refugee pressure worsen |
| Guard evacuation corridors | Keep supplied divisions or garrisons near named states | flood, wildfire, volcano, meteor | lowers refugee death and unrest | refugee pressure and local instability grow |
| Clear the valley roads | Control and repair mountain or river states | landslide, lahar, flood | reopens supply, blocks disease chain | blocked transport and population loss continue |
| Maintain water distribution | Use trains, fuel, and infrastructure in heat or drought states | heat, drought, dust | lowers delayed heat and famine deaths | famine, unrest, and wildfire risk grow |
| Secure damaged airfields | Hold and repair airbases | hail, cyclone, ash, meteor | restores air operations and warning capacity | air disruption persists and follow-up warnings degrade |
| Inspect unstable structures | Spend engineers and time in earthquake zones | earthquake, rupture | lowers aftershock deaths | aftershock chain becomes harsher |

Missions need varied duration. Urgent follow-up windows can be short when a tsunami or aftershock is imminent. Recovery missions should usually last long enough for player and AI action.

## Partial success

Some recovery should allow partial success. For example, a country can clear rail but fail shelter work, or evacuate the coast while losing port capacity. Partial success keeps the aftermath category from feeling binary.

Partial success can:

- lower one chain risk while raising another
- save population while increasing economic disruption
- preserve ports while losing airfield readiness
- stop disease while leaving refugee pressure
- restore supply but leave industry damaged

Tooltips should explain visible consequences without revealing hidden formulas.

## Foreign relief and cross-border consequences

Foreign relief should matter when the disaster is severe. It should not be free.

Relief options can include:

- equipment convoy
- medical volunteers
- rail engineers
- refugee intake
- port access
- food shipments
- fuel shipments
- airlift support
- construction crews

Costs and risks should include convoys, trains, fuel, support equipment, relations, stability, war support, intelligence exposure, faction cohesion, or temporary consumer burden. Aid can improve relations and lower deaths, but it can create dependency, foreign influence, or political backlash when overused.

## Refugee pressure

Serious disasters should sometimes create refugee pressure in neighboring states or countries. This is especially important after floods, volcanic eruptions, tsunamis, wildfires, droughts, and abnormal disasters.

Refugee pressure can:

- raise local supply strain
- reduce stability or war support
- increase disease chain risk
- create border-camp hardening decisions
- open aid decisions for neighbors
- create minor diplomatic friction
- feed the Deaths system if camps fail

The player should be able to mitigate refugee deaths through shelters, transport, food, and medical support.

## Scripted GUI for abnormal systems

Evolution III moving disasters need a scripted GUI dynamic map. The GUI should show active abnormal corridors and the next likely regions.

The GUI should support:

- storm corridor path cards
- tornado path markers
- tsunami wave path markers
- meteor impact clusters
- volcanic ash and lahar zones
- rupture wave regions
- next-hit prediction windows
- warning success or warning failure status
- affected states already hit
- recovery cards tied to each path segment

The GUI should use animations when they clarify state. Examples include a moving storm path pulse, a tsunami wavefront sweep, meteor blink markers, ash plume drift, and warning border flash for the next hit. Every animated sprite must have a static fallback and a proper frame-sheet handoff.

## Normal aftermath UI should stay readable

Not every local hailstorm needs a custom GUI. Small and medium hits can use the decision category cards. The full map GUI is for abnormal, moving, regional, or scenario-scale systems where the player needs to see where the disaster is going.
