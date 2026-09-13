# Event 067 State Machine

```mermaid
flowchart TD
    A[Event 067 available] --> B{Valid major or player country exists}
    B -->|No| A
    B -->|Yes| C[Select one host]
    C --> D[Create canonical Generalissimo]
    D --> E[Loyal commander phase]
    E --> F{Evolution I enabled and Chaos at least 200}
    F -->|No| E
    F -->|Yes after paced entry| G[Supreme Command crisis]
    G --> H{Government action}
    H -->|Contain influence| G
    H -->|Successful permanent removal| R[Resolved by removal]
    H -->|Failed arrest capture or assassination| V[Immediate military revolt]
    H -->|Influence and Chaos remain high| I{Evolution II enabled and Chaos at least 400}
    I -->|No| G
    I -->|Yes after paced entry| J[State Within the State]
    J --> K{Government action}
    K -->|Build counterweights| J
    K -->|Grant demands| J
    K -->|Successful permanent removal| R
    K -->|Failed arrest capture or assassination| V
    K -->|High influence and Chaos| L{Evolution III enabled and Chaos at least 600}
    L -->|No| J
    L -->|Yes after paced entry| M[Final ultimatum]
    M -->|Submit| N[Peaceful military government]
    M -->|Refuse| V
    M -->|Final removal succeeds| R
    M -->|Final removal fails| V
    V --> O[Create host-derived junta country]
    O --> P[Generalissimo becomes ruler and commander]
    P --> Q{Civil war outcome}
    Q -->|Government wins| S[Government reform aftermath]
    Q -->|Junta wins| T[Reunified Generalissimo state]
    N --> U[Generalissimo focus tree]
    T --> U
    R --> W{World-end readiness}
    S --> W
    U --> X{Chaos at least 1000 and public branch enabled}
    X -->|No| U
    X -->|Yes| Y[The Generalissimos' World]
    W -->|Removed Generalissimo blocks normal readiness| Z[World-end branch unavailable]
```

## State ownership notes

- Loyal commander, Supreme Command, and State Within the State belong to the original host country.
- The manual scenario may enter Supreme Command, State Within the State, Final Ultimatum, or Immediate Military Revolt through a scenario-only setup flag.
- Generalissimo Influence exists only before peaceful submission or civil war resolution.
- Command Cohesion replaces Influence after a Generalissimo government is established.
- Successful permanent removal clears normal world-end readiness.
- The public world-end branch requires the original Generalissimo to remain active, ruling, or represented by an undefeated junta legacy state.
