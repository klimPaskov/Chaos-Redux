# International Corridor State Machine

```mermaid
stateDiagram-v2
    [*] --> Proposed
    Proposed --> Negotiating
    Negotiating --> Authorized: all core receipts accepted
    Negotiating --> Revised: counteroffer or route change
    Revised --> Negotiating
    Negotiating --> Cancelled: refusal with no viable route
    Authorized --> Constructing
    Constructing --> Suspended: partner withdrawal or segment loss
    Constructing --> Commissioning: core works complete
    Suspended --> Constructing: contribution and access restored
    Suspended --> Revised: replacement route chosen
    Suspended --> Cancelled: project abandoned
    Commissioning --> Operational: physical and operating proofs pass
    Commissioning --> Strained: partial operating proof
    Commissioning --> Dormant: physical route complete but agreement fails
    Strained --> Operational: correction completed
    Operational --> Strained: equipment or maintenance shortage
    Operational --> PartiallyDisrupted: noncritical segment unavailable
    Operational --> Severed: critical node unavailable
    Operational --> Dormant: agreement suspended
    PartiallyDisrupted --> Operational: segment repaired or bypassed
    Severed --> Operational: critical route repaired
    Dormant --> Operational: agreement renegotiated
    Dormant --> Transferred: new host accepted
    Transferred --> Operational
    Cancelled --> [*]
```

## State rule

Physical infrastructure and the operating agreement are distinct. A corridor can remain physically present while its international benefits are Dormant.
