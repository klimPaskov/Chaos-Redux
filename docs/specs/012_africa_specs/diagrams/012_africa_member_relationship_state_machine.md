# Event 12 Africa member relationship state machine

This state machine defines the intended political lifecycle. It is not a direct script recipe.

```mermaid
stateDiagram-v2
    [*] --> Outside

    Outside --> Protected: guarantee or successful intervention
    Outside --> Associate: accession offer accepted
    Outside --> RivalBloc: strong regional alternative forms
    Outside --> Occupied: conquest without settlement

    Protected --> Associate: defence or development charter
    Protected --> Outside: guarantee expires or is rejected
    Protected --> Resistant: guarantee fails or exploitation rises

    Associate --> Chartered: clauses and obligations ratified
    Associate --> Outside: peaceful withdrawal
    Associate --> Resistant: confidence collapse

    Chartered --> Federal: constitutional accession
    Chartered --> Integrated: negotiated final accession
    Chartered --> Leaving: departure process begins
    Chartered --> Resistant: clauses breached or burden shock

    Federal --> Integrated: final constitutional merger
    Federal --> Leaving: federal withdrawal or secession crisis
    Federal --> Resistant: representation or fiscal settlement fails

    Resistant --> Chartered: concessions and confidence recovery
    Resistant --> Leaving: departure vote or government decision
    Resistant --> RivalBloc: alternative coalition succeeds
    Resistant --> Occupied: war and coercive takeover

    Leaving --> Outside: negotiated exit completed
    Leaving --> Associate: exit renegotiated into looser membership
    Leaving --> RivalBloc: departure coalition forms
    Leaving --> Occupied: departure war lost

    RivalBloc --> Associate: political settlement
    RivalBloc --> Federal: merger treaty after equal-status congress
    RivalBloc --> Outside: bloc dissolves
    RivalBloc --> Occupied: war defeat without negotiated settlement

    Occupied --> Integrated: long compliance, administration, rights, and settlement route
    Occupied --> Federal: autonomy settlement
    Occupied --> Resistant: occupation resistance survives
    Occupied --> Outside: liberation or withdrawal

    Integrated --> Federal: constitutional restoration of autonomy
    Integrated --> Resistant: extreme overextension or identity crisis
    Integrated --> [*]: terminal world identity only
```

## Transition rules

- Positive opinion alone never moves a country into integration.
- Every upward transition needs visible cooperation, confidence, clauses, route compatibility, and manageable Integration Burden.
- Occupation never grants immediate full integration by default.
- A member can move backward when guarantees fail, clauses are broken, representation is denied, or costs exceed benefits.
- Rival blocs can be legitimate African alternatives. Their peaceful merger requires equal-status settlement.
- Terminal cleanup must preserve history and achievement tracking before obsolete relationship variables are cleared.
