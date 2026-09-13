# Balkan War Escalation map

| Stage | Numeric range | Required proof | Main new actions | Exit route |
| --- | --- | --- | --- | --- |
| Balkan Conflict | `0-24` | Opening linked wars | principal claim, corridor mission, arms request, local arbitration | decisive victory or early armistice |
| The Balkans Are on Fire | `25-44` | wider regional participation or several real fronts | neutral intervention, secondary claim, regional mobilization | regional conference or military settlement |
| European Crisis | `45-64` | material outside commitments | containment coalition, sanctions, volunteers, guarantees, faction pressure | coordinated withdrawal or imposed armistice |
| The Powder Keg Explodes | `65-84` | opposing majors or major-led factions in direct war | direct-intervention management, reduced regional settlement controls | wider European peace or further spread |
| Another World War | `85-100` | global-war proof | regional actions close except essential claim and survival state | normal world-war systems own continuation |

## Irreversible floors

```text
Outside major enters directly
    -> escalation cannot fall below European Crisis

Opposing majors or major-led factions fight directly
    -> escalation cannot fall below The Powder Keg Explodes

Another World War proof met
    -> stage locks and Event 045 hands off
```

## Anti-farming structure

```text
Aid clicks -> hidden cumulative sponsor-to-camp support -> bounded support tiers -> escalation only on tier crossing

Guarantee -> one proof record -> escalation once when enforced

Faction entry -> one entrant record -> escalation once

Armistice -> one generation -> one violation record per country
```
