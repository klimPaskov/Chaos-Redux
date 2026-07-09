# Infantry Spawn AI matrix

## Parent country AI

| Situation | Preferred behavior | Avoid |
| --- | --- | --- |
| Peace, high stability | organize, disband bad fragments, avoid risky requests | chaos authorization and repeated lotteries |
| Peace, low stability | close musters, inspect, prevent generals | empowering generals |
| Defensive war, losing | request front units, sort depots, accept limited risk | banning musters too early |
| Offensive war, winning | organize and standardize | unnecessary risky spawns |
| Capital threatened | capital defense muster and depot guard | distant lotteries |
| Low supply | depot sorting and disband fragments | armor lotteries and golem binding |
| Low manpower | careful zombie training only at extreme chaos and desperation | endless weak infantry requests |
| High command confusion | staff rotation and registration missions | general concessions |
| High officer appetite | arrest, rotate, negotiate only if strong | political seat concessions |
| High chaos leakage | quarantine, exorcise, close ledger | demand impossible units |

## Breakaway AI

| Package | First priority | Expansion logic | Containment weakness |
| --- | --- | --- | --- |
| Barracks State | parent war and depots | nearby parent states and supply hubs | can be negotiated or isolated |
| Ragged horde | food and population centers | close weak states and fragmented attacks | fragmentation and low organization |
| Grey host | connect pale zones | isolated coasts, depots, low-pop states | recovery missions can roll back harm |
| Stone host | hold quarries and forts | slow push toward industry | poor speed and high supply burden |
| Mixed impossible army | registry-defined | registry-defined | registry-defined |

## Foreign AI

| Actor | Reaction |
| --- | --- |
| Neighbor of parent | may exploit if parent is in revolt and relations are bad |
| Ally of parent | can send equipment or volunteers if relations and access allow |
| Faction leader | may demand containment or offer aid |
| Rival major | can support breakaway if ideology and strategic interest align |
| Anti-zombie or anti-chaos systems | should not be hijacked by lesser splinters unless explicitly integrated |

AI implementation should use strategy values, decision weights, route weights, and helper triggers. Flat always-yes weights are not acceptable for dangerous decisions.
