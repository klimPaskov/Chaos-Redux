# Event Map and State Machine

## Global state

| State | Meaning | Entry | Exit |
| --- | --- | --- | --- |
| Dormant | Event 14 has not fired | Campaign start | Valid random firing or manual scenario |
| Baseline Active | One or more countries have wartime predation | Entry event or spread | Global victory, Evolution I, territorial fracture |
| Ritual Active | Evolution I has occurred | Dynamic evolution | Global victory, Evolution II |
| Network Active | Evolution II has occurred | Dynamic evolution | Global victory, Evolution III |
| Convergence | Reveal readiness is near | Network thresholds | Readiness broken or Hannibal reveal |
| Unified | Hannibal is revealed | Evolution III | Defeat, ordinary world-end, Wendigo merge |
| Wendigo Merged | Alternate country exists | Valid existing Wendigo at unification | Defeat before lock or Wendigo world-end |
| Terminal Hunt | One scored current enemy is pursued during the countdown | Paid hunt launch | Success, defender break, timeout, route break, invalidation, or terminal lock |
| Ordinary World-End | Terminal ordinary route | Chaos above 1000 and route completion | Terminal campaign state |
| Wendigo World-End | Terminal alternate route | Chaos above 1000 and transformation lock | Terminal campaign state |
| Defeated | No active Event 14 actor remains | Global stabilization | Manual scenario only |

## Country state

| Country state | Visible values | Available play |
| --- | --- | --- |
| Uninfected | None | Aid, screening, border and convoy precautions |
| Suspected | Field Hunger, Command Integrity | Investigation and logistics |
| Active Baseline | Field Hunger, Command Integrity | Full containment, concealment, exploitation |
| Ritual Cell | Adds Cult Cohesion | Infiltration, amnesty, purge, terror doctrine |
| Network Node | Adds Network Reach context | International actions, node targeting, commune prevention |
| Commune Territory | State cards and liberation mission | Blockade, assault, relief, recovery |
| Locally Defeated | Recovery status | Vigilance and external counterwar |
| Reinfected Externally | Source and route shown | New targeted containment |

## State node lifecycle

| Stage | Description | Consumption | Country risk |
| --- | --- | --- | --- |
| Suspected Predation | Evidence incomplete | None or minimal | Cell discovery |
| Compromised Garrison | Unit or prison involved | Low | Mutiny and spread |
| Hunting Ground | Organized disappearances | Low to moderate | Commune formation |
| Feeding State | Cult controls population and supply | High | Warlord release |
| Silent Larder | Severe depopulation and infrastructure collapse | Extreme | Strong warlord state, low future yield |
| Liberated Emergency | Active loss stops | None | Cell remnants |
| Recovery | Burial, records, supply, administration | None | Long trauma |
| Stabilized | Event-owned crisis closed | None | External re-entry only |

## Reveal gate

All hard minima must be met:

- Evolution III enabled
- chaos at Totalen Chaos or higher
- multiple independent network actors
- sufficient Network Reach
- sufficient cumulative population consumption
- viable host with capital and supply
- no global defeat
- no existing world-end

Weighted readiness then considers:

- aligned warlords
- ports and rail hubs
- controlled population
- global Larder
- successful synchronized operations
- resistant warlords
- recent network losses

## Victory checks

### Local

- no active country cells
- no compromised states under that country's control
- no Event 14 commune or warlord occupying its territory
- stabilization mission complete

### Global

- no active country cell
- no active state node
- no commune
- no warlord country
- no unified country
- no pending spread, convergence, or transformation mission

## Public terminal controls

After reveal, Event Details exposes two independent default-enabled rows. Scenario ID `6`, **The World Is the Larder**, gates only the ordinary terminal route. Scenario ID `7`, **No Thaw Will Come**, gates only the Wendigo terminal route. Each preserves its own disabled state and maps to its own terminal flag and super-event. Before reveal, neither row is projected into the visible Event Details list.
