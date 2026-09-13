# Global Heat Wave Intensity

## Purpose

Global Heat Wave Intensity is the one worldwide public value. It expresses the strength of the active heat system before local conditions are applied.

The value is not a temperature in degrees. It is a normalized crisis index from 0 to 100. This avoids pretending that one global temperature can describe every state and lets the system combine heat duration, nighttime retention, humidity, drought footprint, and atmospheric persistence.

## Public bands

Working presentation labels:

| Intensity | Working band | Player meaning |
| --- | --- | --- |
| 0 | Inactive | No active episode |
| 1 to 19 | Oppressive | Early disruption, vulnerable states begin to suffer |
| 20 to 39 | Severe | Broad civilian and military penalties become material |
| 40 to 59 | Extreme | Hotspots require active protection and failures can cascade |
| 60 to 79 | Lethal | Evolution I mortality becomes likely in exposed states |
| 80 to 100 | Scorched | Evolution III near-uninhabitable conditions become possible |

The final labels can change during localisation work. The ranges and meaning should remain stable unless balance evidence supports a revised threshold table.

## Visible presentation

The category header and event details should show:

- current value or rounded band
- current band name
- trend: rising, steady, easing, or surging
- last meaningful global change
- next threshold and its broad consequence
- current episode phase

The player should not see hidden momentum, volatility, surge reserve, or duration budget as separate counters.

## Initial intensity

Suggested opening range: 18 to 46.

The opening roll should use weighted world factors:

- current Chaos tier within a limited contribution
- global drought and wildfire-risk footprint, if a supported shared fact exists
- number of severely damaged or undersupplied populated states
- current season distribution across inhabited land, with both hemispheres represented
- active Air Winter or other atmospheric conditions that materially alter heat, only if the owning system publishes a compatible fact
- prior permanent desertification footprint
- Evolution stage
- configured event intensity setting, if the shared event framework provides one

Chaos should not dominate the opening formula. A Calm World Heat Wave still needs to be a real event, while a high-Chaos episode can be more volatile and persistent.

## Momentum and volatility

Two hidden values govern short-term movement.

### Momentum

Momentum determines whether the next lifecycle pulse tends to raise or lower intensity. It is affected by the current phase, recent changes, mitigation aggregate, drought footprint, and remaining surge reserve.

### Volatility

Volatility determines the size of fluctuations. It is rolled once at setup within a profile band and can increase at higher evolution stages.

The system should produce recognizable episode shapes:

- fast rise, short peak, steady decline
- slow build, long plateau
- early surge, lull, stronger resurgence
- several regional surges beneath a moderate global value
- high opening intensity followed by a difficult but continuous recovery

It should avoid noisy daily oscillation that changes the map faster than the player can react.

## Update cadence

A lifecycle pulse every three to seven days is preferred over daily whole-world calculation. The exact cadence should follow live repository patterns and performance evidence.

A pulse can:

1. update global momentum
2. change intensity within the phase's permitted range
3. select a bounded state cohort for Heat Stress refresh
4. process incident and mission checks
5. rebuild hotspot summaries when a threshold or ranking changes
6. check phase transitions

A major surge event can force an immediate global change and queue a bounded state refresh rather than processing every state in one frame.

## Global mitigation aggregate

Countries can influence the global duration and peak only through a capped aggregate. This represents shared trade adaptation, changed work schedules, reserve releases, emergency imports, and broad transport adjustments.

The aggregate should count meaningful completed measures, weighted by exposed population and economic size, but it must have diminishing returns. A large country protecting its population can matter more than a tiny country, but no one country should end the event for everyone.

Global mitigation can:

- slightly reduce positive momentum
- reduce the chance of a second or third surge
- lower the maximum intensity reachable during a resurgence
- bring forward terminal decline after a long plateau

It cannot:

- directly set intensity to zero
- erase current local Heat Stress
- remove permanent damage
- suppress Evolution III when the world state still supports it

## Regional amplification

Global intensity applies everywhere, but some lifecycle pulses can add temporary regional amplification. This represents a continental heat dome, stagnant air mass, or synchronized dry conditions.

Regional amplification should:

- select a broad connected or climate-consistent region
- last 10 to 35 days
- raise local Heat Stress without creating a second public global value
- appear through map shading, regional report events, and state tooltips
- have its own generation and cleanup proof

At Evolution II and III, more than one regional amplification may exist at once, but the cap should remain small. This prevents the event from becoming a list of regional mini-meters.

## Surge rules

A surge is a discrete episode development with a clear start and end.

Suggested surge cap:

| Evolution | Maximum major surges per episode |
| --- | --- |
| Baseline | 2 |
| Evolution I | 3 |
| Evolution II | 4 |
| Evolution III | 5 |

A surge should require:

- enough remaining duration budget
- enough surge reserve
- a minimum gap since the prior surge
- no active terminal decline lock
- valid world exposure

Surge strength should scale with:

- current intensity gap below the episode ceiling
- drought and dry-region footprint
- recent global mitigation failure
- Evolution stage
- number of high-stress states

The event should not announce the exact surge chance.

## Lull rules

A lull should reduce intensity enough to change some state bands and decisions. Suggested global drop: 8 to 22 points over several pulses.

A lull can end through:

- resumed positive momentum
- a regional amplification spreading
- elapsed lull duration
- a failed aggregate mitigation threshold
- a new evolution activation

The player should receive factual signs of easing, such as reopened shifts or cooler nights in some regions. The text should not state that the lull is false or that another surge is guaranteed.

## Hard bounds and safety

- Clamp intensity to 0 through 100.
- Do not allow a normal pulse to cross more than two public bands at once.
- Prevent negative values after recovery.
- Prevent a new surge after terminal decline is locked.
- Prevent more than one global intensity mutation per lifecycle transaction.
- Persist the post-change value before queuing state updates.
- Record a compact history of major threshold crossings for Event Details and debug use.

## Tuning table

Suggested starting constants for implementation review:

| Parameter | Starting value or band |
| --- | --- |
| Opening intensity | 18 to 46 |
| Ordinary pulse change | -4 to +5 |
| Surge pulse change | +6 to +14 |
| Lull sequence total | -8 to -22 |
| Minimum surge gap | 28 days |
| Baseline active duration floor | 75 days |
| Evolution III hard active ceiling | 540 days |
| Terminal decline lock | After duration budget exhaustion and no surge reserve |
| Global mitigation influence | Cap at roughly 20 percent of momentum calculation |

These values are planning anchors. The implementation must use script constants and probability evidence, not copy them as scattered magic numbers.
