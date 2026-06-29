
# Event 013 evolutions, cluster behavior, and manual scenario

This file expands the evolution, cluster, and scenario handling for Event 13 Natural Disasters. All stage labels are working labels and are not final localisation.

## Evolution logging principles

Evolution records should be rare and meaningful. Normal disaster sequence stages are baseline progression, not evolutions. An ordinary flood report, impact report, and recovery mission should not each log an evolution. The evolution log records when Event 13 gains a new behavior class.

The implementation should set the shared evolution context before recording an evolution entry, and disabled evolutions must not set the same recorded flags that later content reads. If an evolution has no actor, the shared logger should handle the no-actor state instead of leaking stale event targets.

## Evolution stage table

| Evolution | Working label | Unlock direction | Active-event entry | Pre-fire evolved opening | Event details direction |
| --- | --- | --- | --- | --- | --- |
| I | Varied Local Disasters | Gathering Storm, plus prior disaster memory or high chaos opening. | New family weights and warning decisions become available for active recovery categories. | First Event 13 sequence can use the expanded catalogue immediately. | Describe the wider family catalogue and local warnings. |
| II | Regional Disaster Systems | Rising Chaos or Chaos Tier, plus prior disaster sequence or direct high chaos opening. | Active aftermath ledgers can chain into regional follow-ups and foreign relief. | First Event 13 sequence can start as a regional system with neighboring states. | Describe regional damage, recovery tasks, supply penalties, and aftermath chains. |
| III | Abnormal Disaster Age | Totalen Chaos or World Collapse, plus severe disaster memory or manual high intensity. | Active regional systems can schedule abnormal follow-ups only when family logic supports it. | First Event 13 sequence can start with one abnormal family if high-chaos weighting selects it. | Describe meteor showers, massive seismic, volcanic, tsunami, and storm corridor variants, with no world-end branch. |

## Baseline sequence details

Baseline should select one anchor state and zero to two follow-up states. The follow-ups can be the same family, a related family, or a recovery report. The event should prefer meaningful targets, but should not always target majors.

### Baseline sequence patterns

| Pattern | Frequency direction | Sequence |
| --- | --- | --- |
| Single local impact | Uncommon | Warning or no warning, then one impact and one recovery marker. |
| Paired impact | Common | Anchor disaster, then delayed related report in the same country or neighbor. |
| Local disaster week | Common at higher baseline chaos | Two or three related reports across 5 to 10 days. |
| Quiet aftermath | Occasional | The only follow-up is a recovery mission or refugee pressure, not another impact. |

## Evolution I sequence details

Evolution I adds family variety and more incidents, but it should not create large regional damage by default.

### Evolution I patterns

| Pattern | Sequence |
| --- | --- |
| Split reports | Two or three different countries receive small local disasters. |
| Same-family cluster | Several floods, storms, heat events, or blizzards appear in a loosely connected climate zone. |
| Rare local volcano | One volcanic warning and one ash or lahar follow-up, with small regional footprint. |
| Dust and airfield week | Sandstorm and dust events disrupt airbases, supply, and rail in desert regions. |

## Evolution II sequence details

Evolution II should feel like regional disaster management. It can use larger sequences, but the news throttle becomes strict.

### Evolution II patterns

| Pattern | Sequence |
| --- | --- |
| Regional flood system | Anchor flood, two to four neighboring states, rail and supply recovery, refugee pressure. |
| Cyclone landfall | Coastal impact, port closure, inland flood follow-up, neighboring relief. |
| Drought belt | Several warm or dry states receive water stress, then famine or wildfire risk if not addressed. |
| Seismic basin | Earthquake in one state, aftershocks nearby, possible delayed coastal wave. |
| Volcanic ash region | Anchor eruption, ashfall in neighbor states, airfield and rail cleanup. |

## Evolution III sequence details

Evolution III should reserve abnormal disasters for high-chaos moments. It is allowed to be spectacular and damaging, but still recoverable.

### Evolution III patterns

| Pattern | Sequence |
| --- | --- |
| Meteor shower track | Several impact states appear over a short period. Some receive crater aftermath. |
| Massive earthquake-wave | One regional seismic wave damages many neighboring states, then aftershock or tsunami follow-up. |
| Volcanic regional crisis | Huge eruption, ashfall, airfield closures, possible lahar, possible delayed coastal wave. |
| Moving storm corridor | Forecast path appears, one or two updates happen, then state-by-state impact occurs. |
| Compound abnormal week | One abnormal disaster anchors a set of ordinary follow-ups, such as meteor fire starts or ash crop failure. |

## Event 46 placeholder integration

Event 46 should be converted into an inactive unknown placeholder. Its event details should direct seismic content back to Event 13 without listing mechanical effects. It should not be selectable as an active random disaster event.

Implementation should remove or disable independent Earth Earthquake gameplay while preserving catalog history. If an old triggerable scenario or debug hook points to Event 46, it should be updated to call Event 13's geological crisis scenario type instead.

## Sandstorm placeholder integration

A separate Sandstorm event should become a placeholder or a wrapper that triggers Event 13 with the sandstorm family. It should not keep separate damage rules, separate evolutions, or separate logs. The report can still call the family a sandstorm, but the owning event is Event 13.

## Natural Disasters cluster design

The cluster is a repeatable disaster season. It does not include unrelated disaster-like event IDs at this stage. It contains Event 13 member slots with different tier gates and severity displays.

### Member slot model

| Slot | Min chaos tier direction | Participation | Expected sequence |
| --- | --- | --- | --- |
| Local report A | Calm World | Required when cluster fires. | Baseline local sequence. |
| Local report B | Calm World | Optional high chance. | Baseline local sequence with different target if possible. |
| Local report C | Gathering Storm | Optional medium chance. | Baseline or Evolution I sequence. |
| Varied family slot | Gathering Storm | Optional medium to high chance. | Evolution I sequence. |
| Regional system slot | Rising Chaos or Chaos Tier | Optional medium chance, high chance at Totalen Chaos. | Evolution II sequence. |
| Abnormal slot | Totalen Chaos or World Collapse | Optional low chance, higher in manual or maximum chaos. | Evolution III sequence. |

The cluster details UI should show skipped member slots clearly. Skip reasons should include no valid state, family not unlocked, evolution disabled, same-day spacing blocked, or member roll failed.

### Same-day spacing

Disasters should not feel like everything fires on the same date. The cluster wrapper should queue member Event 13 sequences with a start delay. Baseline member slots can begin 5 to 10 days apart in calm worlds. Higher chaos shortens that to 2 to 6 days. Maximum scenario intensity can go down to 1 to 3 days.

Within each member sequence, subevents use their own internal delay model. The cluster delay and sequence delay must not accidentally collapse into same-day spam.

### Cluster history

A cluster history row can record that a Natural Disasters season was launched, with fired and skipped member count. Event 13 history rows still record each member sequence that truly fired. Subdisaster popups inside a sequence do not create extra random event history rows.

## Manual scenario, Disaster Barrage

The manual scenario should be direct and controllable. It is a scenario, not a normal random event roll.

### Scenario launch rules

- It should launch from the triggerable scenario UI.
- It should ignore chaos tier and prior evolution prerequisites.
- It should remain forceable from the manual scenario UI. Do not block it on chaos tier, prior evolution state, active world-end state, an existing Event 13 sequence, or a valid-state precheck. The launch helper should clear any active Event 13 sequence context before queuing the manual barrage so scenario flags do not leak into later automatic events.
- Delayed manual controllers should carry a launch token or equivalent guard so a later force launch makes older delayed manual deliveries self-cancel. Automatic delayed controllers scheduled before the force launch should also be discarded through active-sequence and short flush guards rather than allowed to resume after the manual season ends.
- It should set a tightly scoped scenario launch flag so evolved families can be used without permanently unlocking them for normal automatic selection.
- It should clear scenario bypass variables after setup.

### Scenario type behavior

| Type | Low | Medium | High | Maximum |
| --- | --- | --- | --- | --- |
| Random Barrage | Local varied reports. | Wider local and regional reports. | Chained severe reports. | Full short-period disaster season. |
| Geological Crisis | Earthquake and mass movement focus. | Adds volcano and tsunami. | Adds severe regional quake. | Massive quake-wave, volcano, tsunami, and meteor if allowed by type weighting. |
| Weather Crisis | Flood, storm, blizzard, heat, cold. | Adds cyclone, drought, wildfire. | Adds regional storm and drought chains. | Moving storm corridor and broad compound weather crisis. |
| Skyfall Crisis | Small meteor-like anomalies if allowed. | Meteor shower and airburst pressure. | Severe meteor impacts and crater recovery. | Meteor shower, airburst field, skyfire, and multiple crater aftermaths. |
| Full Catalogue | Small mixed sequence. | Mixed regional sequence. | Mixed regional and abnormal sequence. | Near full catalogue, with strict news throttle and recovery overload. |

### Scenario detail direction

Scenario detail text should tell the player that the barrage begins immediately, that warnings and impacts arrive over time, that intensity controls incident count and abnormal access, and that no world-end branch begins. It should not expose exact hidden weights.

## Evolution and scenario validation checklist

- Each evolution has one log entry when it becomes available.
- Baseline stages are not logged as evolutions.
- Active-event evolution upgrades active recovery or follow-up behavior without rewriting past impacts.
- Pre-fire evolved opening works when the first Event 13 fire happens at high chaos.
- Cluster member slots can fire Event 13 repeatedly with delays.
- Cluster member slots do not fire multiple Event 13 sequences on the same date unless the manual maximum scenario explicitly compresses timing.
- Manual scenario launches without ordinary chaos prerequisites.
- Manual scenario launches over any active Event 13 sequence, then stale normal and stale manual delayed controllers self-cancel instead of mutating the replacement sequence.
- Manual scenario intensity changes incident count, delay, and abnormal access.
- Manual scenario does not set world-end flags.
- Event 46 and Sandstorm placeholders do not keep active independent disaster logic.
