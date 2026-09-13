# Project Lifecycle Diagram

```mermaid
flowchart TD
    A[Stable geographic proposal] --> B[Authorization and method choice]
    B --> C[Survey and charter]
    C --> D{Route remains viable}
    D -->|Yes| E[Right of way and partner agreement]
    D -->|Redesign| C2[Revised alignment]
    C2 --> C
    D -->|Cancel| X[Early cancellation and high salvage]
    E --> F{Required partners resolved}
    F -->|Accepted| G[Procurement and mobilization]
    F -->|Counteroffer| E2[Host accepts or redesigns terms]
    E2 --> E
    F -->|Refused| E3[Reroute reduce scope or cancel]
    E3 --> C
    G --> H[Main construction mission]
    H --> I{Milestone condition}
    I -->|On course| J[Commissioning]
    I -->|Delay or overrun| H2[Add burden extend schedule or reduce scope]
    H2 --> H
    I -->|Critical failure| H3[Suspended works]
    H3 -->|Resume| H
    H3 -->|Reroute| C
    H3 -->|Abandon| Y[Stage based salvage and stranded works]
    J --> K{Physical and legal operation proven}
    K -->|Full| L[Operational project]
    K -->|Weak| M[Strained opening]
    K -->|Reduced| N[Reduced completion]
    M --> O[Maintenance or correction mission]
    O --> L
    L --> P{Later disruption}
    N --> P
    P -->|None| L
    P -->|Equipment shortage| Q[Strained]
    P -->|Segment loss| R[Partially disrupted]
    P -->|Critical loss| S[Severed]
    P -->|Agreement failure| T[Dormant]
    Q --> U[Maintenance]
    R --> V[Repair or reroute]
    S --> V
    T --> W[Renegotiation or transfer]
    U --> L
    V --> L
    W --> L
```

## Reading note

The diagram shows one project object moving through several states. Rerouting, repair, and renegotiation preserve the project identity. They do not create duplicate completed projects.
