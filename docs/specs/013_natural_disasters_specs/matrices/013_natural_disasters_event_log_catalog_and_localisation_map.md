# Event 013 — Event Log, Catalog, and Localisation Map

## Event details window text direction

The Event Details text should describe the premise, not modifiers.

Suggested player-facing detail direction:

> Natural disasters strike named places across the world, damaging local industry, transport, homes, and population. Early incidents are local, but rising chaos makes reports more varied, regional, chained, and eventually abnormal. Warnings sometimes give countries a chance to prepare relief trains, evacuate workers, reinforce ports or dams, and shorten the aftermath. Every disaster report names the affected area clearly.

Do not include exact damage numbers in this detail field.

## Evolution detail directions

| Evolution | Detail direction |
| --- | --- |
| Evolution I | Local disasters diversify. Earthquakes, floods, storms, droughts, fires, landslides, and volcanic unrest can arrive in short delayed bursts, with clearer warning reports and modestly stronger local aftermath. |
| Evolution II | Disasters can affect named regions rather than only one state. River basins, coastlines, mountain belts, dry belts, volcanic zones, and industrial corridors can take anchor and secondary damage. |
| Evolution III | First impacts can leave delayed aftermaths: famine pressure, refugees, aftershocks, tsunamis, damaged rail corridors, ashfall, or regional stability pressure. Some variants can span a continent or macro-region through selected footprints. |
| Evolution IV | Abnormal high-chaos disasters become possible: meteor showers, abnormal earthquake waves, massive volcanic eruptions, delayed tsunamis, traveling storm paths, black-rain-like storms, and other intense natural disasters. Event 46 Earth Earthquake is absorbed here as an abnormal earthquake-wave variant. |

## History row detail data

Each fired history row should be able to display:

- disaster family name;
- affected state or region;
- controlling country;
- severity band;
- warning/no warning;
- recovery phase active/inactive;
- chain follow-up count;
- manual scenario source if relevant.

## Cluster detail direction

Cluster name: **Natural Disasters**.  
Cluster detail:

> Natural disasters are repeatable incidents that damage named places, disrupt local industry and population, and can grow from local emergencies into regional chains as chaos rises. The current cluster contains only Event 13; other disaster-like catalog entries remain separate until deliberately added later.

Member row:

- Event ID: 13
- Event name: Natural Disasters
- Role: required/current only member
- Member severity: Low
- Notes: evolved incidents can be stronger inside the event, but membership severity stays Low until the cluster gains additional members.

## Manual scenario catalog direction

Scenario ID working suggestion: `SCN-013` if available.  
Scenario name direction: Global Disaster Barrage — working label, final localisation may differ.  
Details direction:

> Launches a compressed sequence of natural disasters from selected families. Low intensity creates a few local incidents; Maximum intensity can fire nearly the full catalogue, including high-chaos meteor, volcanic, earthquake, storm, flood, drought, wildfire, tsunami, and regional chain variants.

Type options:

- Random Barrage
- Geological Crisis
- Weather Crisis
- Skyfall Crisis
- Full Catalogue

Intensity scaling:

> Low/Medium/High/Maximum controls the number of incidents, regional footprints, chained aftermaths, and whether Evolution IV abnormal variants can appear.

## Event names and subevent naming direction

Use clear names that can be combined with dynamic state/region names.

| Key concept | Naming direction |
| --- | --- |
| Root event | Natural Disasters |
| Baseline impact | Disaster Report: [Area] |
| Warning | Warning from [Area] |
| Earthquake | Earthquake in [Area] |
| Flood | Floods in [Area] |
| Storm | Storm over [Area] |
| Drought | The Dry Belt around [Area] |
| Wildfire | Fires around [Area] |
| Landslide | Mountain Collapse near [Area] |
| Volcano | Ash over [Area] |
| Tsunami | The Sea Reaches [Area] |
| Meteor | Skyfall over [Area] |
| Recovery | Recovery in [Area] |
| Chain | Aftermath in [Area] |

## Regular event option tone map

| Disaster family | Option tone |
| --- | --- |
| Earthquake | engineers, rubble, silence after shaking, official shock |
| Flood | sandbags, broken bridges, evacuation trains, rumours of water rising faster than orders |
| Storm | closed ports, missing ships, winter/mud, weather offices blamed |
| Drought | grain ledgers, empty wells, ration cards, prayers for rain |
| Wildfire | ash, sirens, volunteers, factory smoke blending with forest smoke |
| Landslide | passes buried, tunnel mouths sealed, mountain roads gone |
| Volcano | ash on windows, mountain “speaks,” airfields closed |
| Tsunami | sea withdrawal, sirens, ships inland, coast scoured |
| Meteor | astronomers, sky artillery, crater fields, ministries denying panic |

## Localisation caution

- Do not reveal hidden chain chances in player-facing text.
- Do not list raw state ids.
- Do not show exact mechanical damage values in Event Details.
- Do show the affected area clearly.
- Do show missing requirements for nonstandard response decisions.
- Use scripted localisation for state, region, family, severity, relief capacity, and active warning names.
