# Focus tree lane map

This diagram shows branch relationships. The implementation agent owns final coordinates and exact focus count.

```mermaid
flowchart TB
    A[Release opening] --> B[Secure capital and provisional authority]
    B --> C[Founding state trunk]

    C --> G1[Constitutional republic]
    C --> G2[Popular councils]
    C --> G3[Traditional restoration]
    C --> G4[Emergency military rule]
    C --> G5[Patron client]
    C --> G6[Radical sovereignty, hidden]

    C --> E[Economy, infrastructure, and administration]
    C --> M[Army, security, and military identity]
    C --> D[Diplomacy, recognition, and patrons]

    G1 --> H[Former-host settlement and borders]
    G2 --> H
    G3 --> H
    G4 --> H
    G5 --> H
    G6 --> H

    E --> H
    M --> H
    D --> H

    D --> N[Independence network]
    H --> X[Regional ambition]
    N --> L[League congress and charter]
    X --> F[Formable discovery and integration]
    L --> F

    G6 --> R[Revisionist league and hidden formables]
    L --> R

    F --> Z[Late state identity and regional order]
    R --> Z
```

## Layout intent

- The survival trunk stays central.
- Government routes fan outward and remain visually distinct.
- Economy, military, and diplomacy support several governments.
- Former-host content and regional ambition occupy one side.
- Network, league, and formables occupy the opposite side.
- Hidden high-chaos content appears only after reveal conditions.
- Regional and country modules attach near the lane they modify.
