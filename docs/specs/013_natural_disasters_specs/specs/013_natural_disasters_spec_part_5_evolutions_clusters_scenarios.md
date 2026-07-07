# Event 013 Natural Disasters, Part 5, evolutions, clusters, and manual scenario

## Baseline flow

Baseline Natural Disasters is a local disaster season. It starts with a few selected families and gives the player clear place-specific reports. The baseline should already be consequential. It can damage industry, break transport, kill enough population to matter, and open aftermath recovery.

Baseline should teach the system:

- disasters are delayed, not same-day spam
- warnings can appear before impact
- named places matter
- affected countries receive reports
- serious damage opens recovery work
- small disaster seasons record one Event 013 log row

## Evolution I, varied local disasters

Evolution I widens the disaster pool and increases sequence activity. It does not make every disaster dramatically stronger. It makes the world feel more active and varied.

Design changes:

- expand pool into storms, droughts, dust, wildfire, mass movement, blizzards, rare volcanic signals, heat, and cold
- increase sequence size modestly
- allow small neighboring spillover for some families
- keep news for meaningful disasters, first family appearances, and player-impacting hits
- preserve the same reusable system and aftermath model
- add first family-specific achievement hooks for recovery mastery

Active-event evolution should adjust currently available family pools and future season rolls. Pre-fire evolved opening should allow Event 013 to start with the wider pool if it has not fired yet.

## Evolution II, regional disaster systems

Evolution II turns local disasters into regional systems. It should be much deadlier and more destructive when target vulnerability is high.

Design changes:

- disaster impacts can hit an anchor state and neighboring valid states
- all baseline families can appear with stronger impact
- tsunami, ashfall, lahar, regional flood, serious cyclone, regional wildfire, and drought-to-famine behavior become more common
- chain ledgers become central
- recovery categories become more complex
- serious impacts can create refugee, famine, disease, supply, and political shock chains
- small weak disasters stop generating global news
- meaningful, large, strange, cascading, or player-relevant disasters still get news

Deaths must scale harder in this evolution. Dense states, poor infrastructure, damaged supply, existing devastation, weak stability, weak recovery, ongoing war, and unresolved aftermath should create large death spikes and delayed death pressure.

Active-event evolution should upgrade open aftermath cards and allow new chain risks for unresolved serious disasters. Pre-fire evolved opening can start with regional systems immediately.

## Evolution III, abnormal disaster age

Evolution III opens high-chaos abnormal disasters. It is not a world-end branch. It is a severe non-terminal catastrophe era.

Abnormal families include:

- meteor shower and meteor impact
- whole-earth rupture wave, using the old Earth Earthquake concept without old logic
- massive volcanic crisis
- delayed tsunami chain after global rupture, volcanic collapse, or ocean impact
- moving storm or tornado corridor
- massive wildfire storm after heat and drought
- abnormal blizzard or cold collapse chain
- skyfire hail linked to meteor showers

Evolution III should use super-event treatment for the first abnormal era reveal and for major rare abnormal disasters. It should also use the scripted GUI dynamic map for moving or path-based systems.

Evolution III deaths and destruction must be much higher than earlier stages. These disasters can devastate regions, destroy large amounts of industry and infrastructure, and cause very large population losses when the family fits.

## Evolution log design

Do not log ordinary disaster hits as evolutions. Evolution log entries are for the three mutation stages.

| Evolution | Log meaning direction |
| --- | --- |
| Evolution I | The disaster catalogue has widened and ordinary local disasters now arrive in more varied forms. |
| Evolution II | Disasters have become regional systems with chained aftermaths and stronger recovery pressure. |
| Evolution III | Abnormal high-chaos disaster families can appear, including meteor, rupture, volcanic, tsunami, and moving storm chains. |

The final implementation can name these in localisation. This spec gives direction only.

## Cluster behavior

The Natural Disasters cluster should contain Event 013 only at this stage. Do not add flood, sandstorm, heat wave, Earth Earthquake, or volcano entries as separate cluster members.

The cluster should make Event 013 fire repeatedly or in stronger internal seasons rather than treating many old events as separate members.

Suggested cluster behavior:

| Chaos state | Cluster member behavior |
| --- | --- |
| Early chaos | Several baseline Event 013 entries are possible, each low severity. |
| Evolution I available | Cluster can schedule more varied local seasons. |
| Evolution II available | Cluster can schedule regional systems and stronger aftermath. |
| Evolution III available | Cluster can schedule one abnormal chain, but global one-off families must not repeat carelessly. |

The cluster firing should still respect the one-log-row rule for each Event 013 sequence. If a cluster causes multiple Event 013 seasons, each season creates its own Event 013 log row because each is a real Event 013 firing.

## Disaster Barrage scenario

Disaster Barrage is the manual scenario for Event 013. It should launch Event 013 directly from the selected country or scenario context. It bypasses ordinary chaos and evolution prerequisites only for the manual launch.

### Scenario type options

| Type option | Family pool direction |
| --- | --- |
| Random Barrage | Full eligible pool, weighted for variety. |
| Geological Crisis | Earthquake, rupture, dry mass movement, wet mass movement, volcanic, tsunami, meteor when intensity allows. |
| Weather Crisis | Flood, cyclone, extreme wind, tornado, thunderstorm, hail, wildfire, drought, heat, cold, blizzard, dust. |
| Skyfall Crisis | Meteor, meteor shower, skyfire hail, ocean impact, abnormal ash if chained. |
| Full Catalogue | Broad pool with minimal family restrictions and strong news throttling. |

### Intensity options

| Intensity | Direction |
| --- | --- |
| Low | A varied local season with normal warnings, reports, and recovery. |
| Medium | Regional systems become likely and sequence size increases. |
| High | Severe chained behavior opens, with stronger deaths and more recovery pressure. |
| Maximum | Abnormal access opens, with meteor showers, rupture waves, massive eruption pressure, delayed tsunami, and moving storm corridor possible in one season. |

Disaster Barrage should never create a terminal world-end branch. It can be campaign-shaping and devastating, but it must not set global terminal state.

## Handling outdated related events

| Event | Required handling |
| --- | --- |
| Event 046 Earth Earthquake | Inactive unknown placeholder. Remove independent gameplay. The whole-world rupture wave lives in Event 013 Evolution III. |
| Event 099 Sandstorm | Placeholder or one-line bridge into Event 013 sandstorm family. No separate dust logic. |
| Event 051 Heat Wave | Keep as separate event unless later accepted. Event 013 heat family must block stacking. |
| Event 043 Massive Flood | Do not absorb by default. Event 013 has flood family, but separate Event 043 needs its own later decision. |
| Event 120 Massive Volcano Eruption | Event 013 Evolution III can express massive eruption crisis. Separate Event 120 stays unimplemented unless later accepted. |
