# Event 013 Natural Disasters research notes

All source references are research support for design direction, not final localisation.

## Hazard classification basis

EM-DAT classifies natural hazards into geophysical, hydrological, meteorological, climatological, biological, and extra terrestrial groups. Event 13 uses that structure as a design scaffold, while player facing text should describe the visible disaster instead of academic labels.

Source: https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/

## Severity basis

Our World in Data notes that recent global disaster deaths are often much lower than historic peaks, but single extreme events can still kill tens or hundreds of thousands, and the 20th century had years with more than a million disaster deaths. This supports an Event 13 model where ordinary baseline disasters are usually modest, while severe dense state chains and failed aftermaths can cause huge casualties.

Source: https://ourworldindata.org/natural-disasters

## Million scale historical inspiration

The 1931 China floods have widely varying estimates, with systematic estimates in the hundreds of thousands and some official or historical claims around two million or more when starvation and disease are included. This supports flood aftermath chains where the first impact is not the whole death count.

Sources:

- https://disasterhistory.org/central-china-flood-1931
- https://journals.ametsoc.org/view/journals/clim/36/18/JCLI-D-22-0771.1.xml

USGS lists the 1556 Shensi or Shaanxi earthquake as the worst earthquake death toll in history, with 830,000 deaths. This supports severe earthquake and Great Rupture Wave paths that can produce massive casualties in dense vulnerable regions.

Source: https://earthquake.usgs.gov/learn/today/index.php?day=23&month=1

## Family mechanics support

NOAA and NWS hurricane guidance identifies storm surge, heavy rainfall, high winds, rip currents, and tornadoes as major hurricane hazards. Event 13 tropical cyclones therefore need port, dockyard, airfield, flood, surge, and evacuation mechanics rather than generic storm damage.

Source: https://www.nhc.noaa.gov/prepare/hazards.php

NOAA severe thunderstorm material identifies straight line winds, tornadoes, and hail as distinct hazards with different damage patterns. Event 13 treats thunderstorm, hail, extreme wind, and moving storm corridor as related but separate playbooks.

Source: https://www.nssl.noaa.gov/education/svrwx101/thunderstorms/

USGS hazard material treats earthquakes, volcanic eruptions, landslides, and tsunamis as connected coastal and geologic hazards. Event 13 uses that relationship for earthquake to tsunami chains, volcanic tsunami, lahar, and mass movement aftermaths.

Source: https://www.usgs.gov/special-topics/subduction-zone-science/science/tsunamis

NASA describes Tunguska as an asteroid airburst over Siberia that produced a fireball, large explosion, forest fires, and trees blown down for miles. Event 13 uses this as inspiration for meteor shower airburst, fire ignition, shock damage, and crater or dust aftermath, while keeping it separate from Event 28 Asteroid Incoming.

Source: https://www.nasa.gov/history/115-years-ago-the-tunguska-asteroid-impact-event/

NOAA climate impact material links drought to food production and health, and flooding to disease, deaths, ecosystem damage, and infrastructure damage. Event 13 therefore treats drought and flood aftermaths as long pressure chains, not only immediate building damage.

Source: https://www.noaa.gov/education/resource-collections/climate/climate-change-impacts

## Design conclusion

The disaster system should not use fixed deaths. It should combine family specific dynamic loss rates with the current population of each affected state. It should let warning, evacuation, rescue, supply, rail, fuel, ports, and foreign relief change the final rate. It should allow million scale outcomes when dense regions receive severe direct impacts or when aftermath is not contained.
