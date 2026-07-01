# Natural Disasters AI and Tuning Matrix

## AI response priorities

| Situation | AI urgency | Preferred action | Avoid |
| --- | --- | --- | --- |
| Capital hit | Extreme | Emergency rescue, supply repair, stability protection | Waiting for slow reconstruction only |
| Major port hit for island or naval country | Extreme | Reopen port, import supplies, request aid | Spending on inland repairs first |
| Supply hub or rail hub hit during war | Very high | Clear rail, restore hub, protect troops | Ignoring supply collapse |
| High population state hit | Very high | Shelters, rescue, medical response | Only repairing factories |
| Factory-heavy state hit | High | Emergency repair and reconstruction | Empty public-order decisions |
| Drought across several core states | High | Food imports, water, wildfire prevention | Letting famine pressure stack |
| Wildfire near industry | High | Firebreaks and evacuation | Rebuilding before fire containment |
| Minor hail or storm in rural area | Low to medium | Low-cost rural relief | Spending scarce equipment while at war |
| Predicted tsunami or storm corridor path | Extreme | Evacuate predicted states and reinforce routes | Treating prediction as normal aftermath |

## Tuning principles

- Strong disasters should not be balanced by tiny numeric penalties. They should change state usability.
- Weak countries should have cheaper emergency actions but slower reconstruction.
- Major powers should pay more and recover faster if they allocate resources.
- At war, supply repair and evacuation should outrank long-term industry projects.
- AI should not take a decision if the target state, country, route, port, rail hub, or evolution is invalid.
- AI should not repeatedly spend resources on the same low-value state while a capital or supply hub is still damaged.
- Recovery costs scale with affected population, damaged building count, country industry, war state, and severity.
- Disaster deaths scale with affected population, infrastructure, response score, family severity, and delayed aftermath.

## News thresholds

| Context | News threshold |
| --- | --- |
| Baseline player country hit | Report after one to two days |
| Baseline non-player minor hit | Report only if high severity or nearby major relevance |
| Evolution I | Report first few meaningful hits, then use digests |
| Evolution II | Severe, capital, player, major-country, or high-death hits only |
| Evolution III abnormal | Super-event if threshold crossed, otherwise severe digest |
| Disaster Barrage maximum | Super-event or digest for abnormal set, not all pulses |

## Suggested route for constants

Use script constants for:

- sequence pulse ranges
- delay bands
- damage multipliers
- family weights
- state cooldown days
- news digest cooldowns
- delayed death tick duration
- recovery mission duration bands
- AI priority thresholds
- manual scenario intensity scales
- GUI danger thresholds
