# Event 012 Africa host-overlay and country-package selection flow

This diagram shows how the event creates country specificity without assigning a separate full tree to every African start.

```mermaid
flowchart TD
    A[Select any existing country whose current capital is in Africa] --> B[Identify capital region and host identity]
    B --> C{Named host dossier available}

    C -->|Full mapping| D[Load country-specific host overlay]
    C -->|Compact mapping| E[Load compact host signature]
    C -->|No mapping| AA[Load capital-only compact package]

    D --> F[Set starting problem]
    E --> F
    AA --> F
    F --> G[Select first proof mission and corridor type]
    G --> H[Apply route biases and early rival pressures]
    H --> AB{Host has a generic focus tree}
    AB -->|Yes| I[Open shared continental tree]
    AB -->|No| AC[Preserve meaningful tree and add Event 12 systems]
    AC --> J

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

The host pool is geographic and exhaustive: every existing country whose current capital is in Africa is eligible. Named dossiers, focus trees, contacts, political status, capital control, and country classification change content or weighting only. Event 12 has no valid host only when the map contains no country with an African capital.

A full host dossier is used when the country has a distinct opening problem that changes the first mission, constitutional risks, diplomatic behaviour, military geography, and post-unification legacy.

A compact signature is used when the country needs identity but does not justify a parallel large overlay. It changes one host problem, one first proof, one regional hook, one support-branch mutation, and AI preferences.

An African-capital country outside the named matrix receives the neutral capital-only compact package and a continent-wide contact pool. It never impersonates a named country dossier. A meaningful existing focus tree is preserved; only the generic focus tree is replaced by the continental tree.

A priority member package is promoted only when it has:

- a viable compact territory or stable autonomy
- local support or a functioning political institution
- an economic or strategic role
- a distinct relationship problem with the League
- a safe force and access plan
- content that does not duplicate a neighbouring package

A candidate remains a cultural body, autonomous region, associated council, or compact tag when a full country would create an inaccessible enclave, unsafe territorial transfer, or duplicate system.
