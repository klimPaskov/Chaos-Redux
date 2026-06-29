
# Event 013 AI strategy matrix

This file gives implementation-ready AI behavior direction. It is not final code.

| AI actor group | When affected directly | When neighbor is affected | When world is in high chaos | Major blockers |
| --- | --- | --- | --- | --- |
| Major power at peace | Repair high-value buildings, ports, supply hubs, capitals, and dense states. Use expensive recovery when stockpiles are healthy. | Send relief to allies, faction members, and important trade partners. | Prepares for regional chains and opens foreign relief if stable. | Do not spend all equipment on low-value states. |
| Major power at war | Prioritize supply hubs, rail, ports, airbases, and capital safety before full shelter work. | Send aid only to faction members or strategic partners if routes are safe. | Can exploit enemy disaster through readiness, but should not gain free war goals. | Avoid recovery choices that cripple active fronts. |
| Minor at peace | Use cheap shelter, rail, and water decisions. Ask for relief early. | Accept refugees if stability and supply are adequate. | Hardens borders if unstable. | Avoid unaffordable high-cost decisions. |
| Minor at war | Protect capital, rail, and supply. Use evacuation first for dense states because percentage losses become much larger absolute deaths there. | Rarely sends aid unless faction duty is strong. | Requests aid from faction leader or neighbor. | Avoid sending scarce trains and trucks away. |
| Island country | Prioritize port closure, cyclone warnings, tsunami evacuation, convoys, and dockyard recovery. | Sends or requests relief by convoy. | Treats coastal danger as strategic survival risk. | Avoid land-only recovery decisions. |
| Landlocked country | Prioritize rail, roads, flood, drought, cold, fire, and mass movement recovery. | Sends relief by rail or trucks if routes exist. | Protects borders from refugee pressure. | Avoid port-specific actions. |
| Faction leader | Coordinates aid for key member states, especially ports and front supply hubs. | Uses faction relief decisions when several members are affected. | Treats regional systems as strategic cohesion tests. | Avoid free member rebuilding. |
| Rival or enemy | Repairs own disasters first. | Can harden border, prepare readiness, or exploit if already at war. | More opportunistic, especially at high chaos. | No disaster-created free declarations unless separately designed. |
| Human player target logic | The player receives clear reports and visible choices. | The player sees neighbor refugee or relief decisions only when relevant. | The player receives abnormal tracker and meaningful news only. | No hidden unavoidable chain if a warning was promised. |

## AI decision scoring factors

AI recovery scoring should consider these values.

- Is the affected state a capital, port, supply hub, major rail junction, or high-population state where a percentage-based loss can become a very large absolute death count.
- Does the country have enough trains, trucks, fuel, convoys, support equipment, manpower, and XP.
- Is the country at war, losing supply, or defending a front.
- Is stability low enough that rationing or refugee acceptance could cause unrest.
- Is the disaster family likely to chain if ignored.
- Is the state already under another disaster aftermath.
- Is the country a faction leader or protected ally.
- Is the action a physical recovery task or only a diplomatic relief task.

AI should never use the scripted GUI. Every GUI action that matters needs a decision or helper equivalent.
