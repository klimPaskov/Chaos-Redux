# Reward arbitration matrix

## Winner reward state

| Event 016 ownership | Event 036 state | Event 025 result |
| --- | --- | --- |
| At least one valid base family missing | No prior Event 036 reward | Random valid missing base operational technology |
| At least one valid base family missing | Prior Event 036 reward with no exact overlap | Random valid missing base operational technology |
| At least one valid base family missing | Prior Event 036 reward overlaps one field | Exclude exact duplicate when another valid base exists, otherwise compatible upgrade |
| All base families owned, compatible upgrades missing | Any | Random valid upgrade |
| Full external base and upgrade pool owned | Any | Alien Systems Integration |

## Event order

| First incident | Second incident | Overlap | Second reward rule |
| --- | --- | --- | --- |
| Event 025 | Event 036 | None | Ordinary Event 036 reward |
| Event 025 | Event 036 | Alien arms, propulsion, or aircraft field | Upgrade aircraft package or grant higher module or production tier |
| Event 036 | Event 025 | None | Ordinary Event 025 random valid reward |
| Event 036 | Event 025 | Exact field overlap | Different valid base family, compatible upgrade, or Integration capstone |
| Event 025 in Country A | Event 036 in Country B | Global repeated recovery only | Both country rewards remain valid |

## Main reward versus fragments

| Outcome | Base custom technology | Upgrade | Integration capstone | Research bonus | Fragment idea |
| --- | ---: | ---: | ---: | ---: | ---: |
| Main winner, missing base | Yes | No unless helper resolves dependency | No | Supporting only | Optional |
| Main winner, bases full | No | Yes | No | Supporting only | Optional |
| Main winner, full pool | No | No | Yes | Included in capstone | Optional |
| Losing survey tier | No | No | No | Small | No |
| Losing minor fragment tier | No | No | No | Medium | Temporary |
| Losing major fragment tier | No by default | Conditional matching upgrade | No | Large | Staged temporary |

## Broad field mapping

The live Event 016 registry decides exact keys. Scripted localisation should map the selected result into one broad public field.

| Internal family group | Public Event 025 field direction |
| --- | --- |
| Propulsion or alien arms | Flight control, propulsion, or weapons |
| Computation or robotics | Computation and autonomous machinery |
| Materials | Exotic structural materials |
| Teleportation | Spatial manipulation |
| Temporal | Temporal instrumentation |
| Cloning, paleogenetics, xenobiology, or biological | Biological synthesis |
| Full-pool capstone | Integrated alien systems |

## Transfer behavior

| Asset | Transfers with physical custody | Transfers automatically with researched knowledge |
| --- | ---: | ---: |
| Main physical core | Yes | No |
| Fragment category | Yes | No |
| Event 025 winner history | No | No |
| Base custom technology | No | Already researched by original owner |
| Upgrade | No | Already researched by original owner |
| Dependence pressure | Future physical pressure moves, existing institutional effects remain | No automatic full reset |
| Artifact decisions | Yes, after valid transfer | No |

## Failure states

| Failure | Required response |
| --- | --- |
| Base random pool empty | Try compatible upgrade pool |
| Upgrade pool empty | Apply Integration capstone |
| Capstone already owned | Apply documented Integration reinforcement result, never silent no-op |
| Event 036 key unavailable | Resolve Event 025 independently and preserve ledger hook |
| Winner invalid during reward chain | Cancel winner proof and rerun valid same-day finalist comparison, otherwise close without main reward |
| Reward helper returns invalid selector | Fail closed, log implementation error, do not substitute ordinary vanilla tech |
