# Event 012 Africa host-overlay and country-package selection flow

This diagram shows how the event creates country specificity without assigning a separate full tree to every African start.

```mermaid
flowchart TD
    A[Select valid country with African capital] --> B[Identify capital region and host identity]
    B --> C{Full host dossier available}

    C -->|Yes| D[Load country-specific host overlay]
    C -->|No| E[Load compact host signature]

    D --> F[Set starting problem]
    E --> F
    F --> G[Select first proof mission and corridor type]
    G --> H[Apply route biases and early rival pressures]
    H --> I[Open shared continental tree]

    I --> J{First proof result}
    J -->|Success| K[League mandate strengthened]
    J -->|Partial success| L[League opens with oversight or autonomy clause]
    J -->|Failure| M[Recovery mission or regional coalition route]

    K --> N[Regional congresses and candidate polities]
    L --> N
    M --> N

    N --> O{Candidate needs full country package}
    O -->|No| P[Cultural body, autonomous region, association, or compact tag]
    O -->|Yes| Q{Promotion conditions met}

    Q -->|No| P
    Q -->|Yes| R[Activate priority member package]

    R --> S[Starting problem and idea lifecycle]
    R --> T[Country focus modules]
    R --> U[Distinct decision family]
    R --> V[Starting forces and reinforcement]
    R --> W[League, refusal, and rival behaviour]

    P --> X[May qualify for later promotion]
    X --> Q

    S --> Y[Post-settlement play]
    T --> Y
    U --> Y
    V --> Y
    W --> Y

    Y --> Z[Host and member legacies survive unification]
```

## Selection rules

A full host dossier is used when the country has a distinct opening problem that changes the first mission, constitutional risks, diplomatic behaviour, military geography, and post-unification legacy.

A compact signature is used when the country needs identity but does not justify a parallel large overlay. It changes one host problem, one first proof, one regional hook, one support-branch mutation, and AI preferences.

A priority member package is promoted only when it has:

- a viable compact territory or stable autonomy
- local support or a functioning political institution
- an economic or strategic role
- a distinct relationship problem with the League
- a safe force and access plan
- content that does not duplicate a neighbouring package

A candidate remains a cultural body, autonomous region, associated council, or compact tag when a full country would create an inaccessible enclave, unsafe territorial transfer, or duplicate system.
