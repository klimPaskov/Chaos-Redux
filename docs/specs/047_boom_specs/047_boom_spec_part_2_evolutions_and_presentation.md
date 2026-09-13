# BOOM evolutions and presentation

## Evolution structure

Event 47 has one evolution track with two stages:

1. Bigger BOOM
2. BOOM BOOM BOOM

The stages change the future incident profile. Activating or recording an evolution does not cause an explosion and does not change Chaos by itself.

Each stage supports two entry paths:

- Pre-fire evolved opening: the Chaos threshold and enabled evolution are already available before Event 47 has fired for the first time.
- Active-history evolution: Event 47 has fired at least once and the evolution becomes active after its normal paced delay.

A pre-fire evolved opening activates and records the eligible stage immediately before the first incident is built. The first incident then uses the evolved rules.

An active-history evolution uses MTTH pacing. Event 47 can fire again before the pending evolution completes. In that case, the incident uses the highest evolution that is already active and enabled.

Evolution toggles remain independent. Bigger BOOM controls strength and the second blast ring. BOOM BOOM BOOM controls the number of epicenters. If the first evolution is disabled while the second remains enabled, the incident can contain several baseline-strength explosions. This keeps disabled content from blocking the event.

## Evolution I: Bigger BOOM

### Availability

- Minimum Chaos: 400
- Evolution stage: 1
- Base active-history MTTH: about 90 days

The active-history delay becomes shorter when:

- Chaos is at least 500
- Event 47 has already fired more than once
- the latest BOOM caused a very high exact death total

The delay must not become instant from repeated checks. It is recorded once when the evolution actually activates.

### Expanded blast geometry

Bigger BOOM adds a second ring.

- Epicenter: the selected primary state
- First ring: every directly adjacent valid land state
- Second ring: every valid land state adjacent to a first-ring state, excluding the epicenter and every first-ring state

The second ring is deduplicated and frozen before effects begin. A state reached through several first-ring paths receives one second-ring entry.

### Evolved mortality

| Zone | Starting mortality band | Dynamic adjustment | Hard maximum |
| --- | ---: | ---: | ---: |
| Epicenter | 75% to 90% | Up to 5 percentage points for very high population and urban concentration | 95% |
| First ring | 20% to 35% | Up to 5 points for urban concentration and up to 5 points of terrain shielding | 40% |
| Second ring | 2% to 6% | Up to 2 points in either direction from density, exposure, and shielding | 8% |

The protected population floor remains 1,000.

### Evolved building damage

| Building family | Epicenter | First ring | Second ring |
| --- | ---: | ---: | ---: |
| Infrastructure, railways, supply nodes and routes | 90% to 100% | 45% to 70% | 8% to 20% |
| Civilian factories, military factories, dockyards, refineries, synthetic plants | 80% to 100% | 35% to 60% | 8% to 20% |
| Airbases and naval bases | 75% to 100% | 40% to 70% | 8% to 20% |
| Anti-air, radar, land forts, coastal forts and other valid strategic buildings | 75% to 100% | 40% to 70% | 8% to 20% |

### Evolved force disruption

| Zone | Strength loss | Organization loss |
| --- | ---: | ---: |
| Epicenter | 60% to 85% | Reset to the minimum supported state |
| First ring | 20% to 40% | 60% to 90% |
| Second ring | 3% to 10% | 15% to 35% |

The effect remains state-local. Military casualty logging still requires exact observed personnel loss.

### Immediate effect on future firings

Once active and enabled, Bigger BOOM changes the next Event 47 firing immediately. It does not revisit an old blast or retroactively damage old targets.

## Evolution II: BOOM BOOM BOOM

### Availability

- Minimum Chaos: 800
- Evolution stage: 2
- Requires Evolution I to have activated at some point in the campaign
- Base active-history MTTH: about 110 days

The active-history delay becomes shorter when:

- Chaos is at least 900
- an evolved Bigger BOOM incident has already occurred
- Event 47 has fired several times without a multi-strike incident

Evolution II can activate before Event 47's first firing when both evolution thresholds and enable states are already satisfied. In that case, the first firing can begin as a multi-strike incident.

### Number of epicenters

| Current Chaos at incident creation | Two epicenters | Three epicenters |
| --- | ---: | ---: |
| 800 to 899 | 75% | 25% |
| 900 and above | 60% | 40% |

The incident uses fewer epicenters when the eligible pool cannot safely support the rolled count.

- Three requested and only two safe targets found: use two.
- Two or three requested and only one valid target found: use one.
- No valid target found: reject the Event 47 firing cleanly before weight, cap, history, and pacing state are committed.

A degraded count is recorded for debugging and testing. Player-facing text can state that fewer locations were confirmed without exposing selector failure.

### Geographic separation ladder

The selector attempts these standards in order:

1. Different continents, no direct adjacency, and no shared first-ring state.
2. Different strategic regions, no direct adjacency, and different owners where possible.
3. Unique nonadjacent states.
4. Any unique eligible states when no safer separation exists.

The second target is compared with the first. The third target is compared with both earlier targets.

Each stage uses bounded retries. The selector does not loop without a fixed stop and does not scan or reroll after damage begins.

The preference for different owners is weaker than the preference for wide physical separation. A large country can receive two distant blasts when it controls large parts of the world and no better candidate exists.

### Multi-blast timing

The first epicenter uses the complete camera and opening presentation.

Later epicenters occur close enough in time that the world treats them as one incident. They receive their own standalone explosion effect and affected-country report. They do not move the camera again.

A short delayed sequence is acceptable when it helps the player register each location. The total incident must remain bounded and should complete within the same day or immediate event chain.

### Strongest-zone overlap rule

All epicenters and rings are frozen before the first damage transaction. Every affected state receives one final intensity based on this priority:

1. Epicenter
2. First ring
3. Second ring

A state touched by several zones receives the strongest zone only. It does not add mortality percentages, building damage shares, or force loss from overlapping blasts.

This rule makes the result independent of epicenter order and prevents duplicate population loss. The incident ledger stores the winning epicenter and final zone for each state.

Two primary epicenters are always unique. An epicenter that lies inside another blast's ring keeps epicenter intensity.

## Camera and visual sequence

The player's first visible information should be the location and physical blast. The main report follows the effect.

The implementation should use the largest safe standalone mushroom-cloud or thermonuclear-style effect available. It must be called without the gameplay nuclear route.

The first blast sequence is:

1. Center the camera on the first epicenter.
2. Give the map enough time to settle on the location.
3. Play the explosion effect.
4. Apply the state transactions.
5. Open the main report.

Later blasts under Evolution II are shown through map effects and reports. They do not seize the player's camera.

In multiplayer, each human client should receive the camera move only through its own presentation scope. A player must not have the camera moved repeatedly by every blast or by every other player's report.

## Report families

The event uses bounded report families selected by the reader's relationship to the incident.

### Direct-hit report

Sent to the owner or controller of an epicenter state when that country uses normal civilian systems. The report should focus on the flash, the immediate absence of communications, destroyed settlements, broken rail and supply links, local force loss, and the lack of any warning or detected attacker.

### Neighboring-country report

Sent to a country that owns or controls a first-ring or second-ring state. The report should focus on the shockwave crossing borders, regional damage, sudden casualty reports, and the inability to identify a launch point.

### Same-continent distant report

Sent to normal countries on the same continent that were not directly affected. The report should focus on an impossible distant concussion, instrument readings, moving air pressure, and public fear.

### Global distant report

Sent to other normal countries. The report can use shattered glass, microphones, animals, harbor movement, atmospheric instruments, or thunder-like reports. It should make the worldwide reach clear without adding a universal modifier.

### Later-blast location notices

Under Evolution II, each later epicenter creates one concise location notice for human players and one affected-country report for the new region. These notices identify the state or region and the scale of damage. They do not claim a common cause beyond the fact that the blasts occurred within one impossible incident.

### Bounded delivery

Each normal country receives no more than one global soundwave report per Event 47 firing. A country directly affected by several blast zones receives one primary incident report plus concise location summaries where needed. Hidden AI acknowledgments can record awareness without opening large numbers of popups.

## Writing direction

The writing should describe concrete physical evidence:

- a flash that fills the horizon
- pressure arriving far beyond the expected range
- damaged rail lines and roads
- communications ending at the same moment
- buildings opened or flattened by the shockwave
- distant microphones and measuring stations recording the event
- animals reacting far from the site
- windows breaking in places that should be too distant
- several far-separated regions reporting the same kind of blast at higher evolution

The cause remains uncertain. The text can show accusations and speculation only as unconfirmed reactions. No follow-up line should settle the matter.

The word nuclear can appear as an uncertain visual comparison from witnesses or officials. The event must not state that a nuclear weapon was used.

Options should be restrained. Direct victims use grief, shock, or a practical acknowledgement. Distant countries use uneasy understatement or official confusion. Comedy, memes, triumph, and playful sarcasm do not fit the casualty scale.

The writing should not center on paperwork, sealed reports, a staff table, or a generic government statement. Physical damage and human observation carry the scene.

## Event History and evolution records

One Event 47 firing creates one Event History row. The row records the date, event ID, incident profile, first epicenter, total epicenter count, exact civilian deaths, exact military deaths when available, and affected-state count.

The visible Event History actor remains empty. Using the first victim as the actor would misrepresent a multi-country disaster, while assigning an attacker would break the event premise.

Each evolution stage records one actorless evolution entry when it activates. The event-detail preview describes the changed incident profile without fake history dates or sequence numbers.

The event details should explain:

- a state can be struck without an attacker
- the blast destroys population and infrastructure
- the soundwave is detected around the world
- Bigger BOOM widens the damage profile
- BOOM BOOM BOOM allows several distant epicenters

Event details should not expose exact mortality rolls, selector retries, hidden ledgers, or a possible cause.

## Visual asset scope

The event needs one generated report image. The image should show a huge mushroom cloud rising over a period-appropriate populated or industrial region from a documentary distance. The scene should avoid visible missiles, aircraft delivering a weapon, national markings, radiation symbols, modern buildings, modern vehicles, readable generated text, or clues that identify an attacker.

The report image is static. The map explosion effect provides motion and scale. A custom animated frame sheet would repeat information without improving player understanding.
