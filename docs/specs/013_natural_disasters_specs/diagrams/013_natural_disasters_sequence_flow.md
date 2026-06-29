
# Event 013 sequence flow diagram

```text
Event 13 selected or cluster member starts
        |
        v
Build sequence context
        |
        +-- choose evolution stage allowed by chaos, scenario, and enabled-state
        |
        +-- choose incident count and delay rhythm
        |
        +-- choose family set and first anchor state
        |
        v
Record one Event 13 random-event history row
        |
        v
Warning phase if family and preparedness allow it
        |
        +-- player or AI preparation decisions
        |
        v
Impact subevent
        |
        +-- family-specific building damage
        +-- real state population loss
        +-- civilian deaths log
        +-- state modifiers and supply penalties
        |
        v
Create aftermath ledger
        |
        +-- decision category shows relevant actions
        +-- missions start if family needs them
        |
        v
Delayed follow-up scheduler
        |
        +-- no follow-up if recovery succeeds
        +-- family chain if recovery is incomplete
        +-- news only if news gate passes
        |
        v
Recovery complete or aftermath persists
        |
        +-- cleanup modifiers and flags
        +-- close sequence when all ledgers are done
```

Subevents inside the sequence do not create additional random event history rows. Cluster member slots that fire separate Event 13 sequences do create separate Event 13 history rows.
```
