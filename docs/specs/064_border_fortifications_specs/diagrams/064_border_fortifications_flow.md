# Event 064 Flow Diagram

All labels below are design handles. The diagram shows behavior, not exact script syntax.

```mermaid
flowchart TD
    A[Event 064 selected] --> B{Automatic context}
    B -->|Yes| C[Build eligible cluster memberships]
    B -->|No| D[Use standalone manual or debug context]
    C --> E{One cluster chosen and roll succeeds}
    E -->|Yes| F[Save exact cluster incident]
    E -->|No| G[Save standalone natural context]
    D --> H[Create unique global wave token]
    F --> H
    G --> H
    H --> I[Snapshot valid countries and current map]
    I --> J[Process one country]
    J --> K[Find current foreign land frontier]
    K --> L[Deduplicate direct frontier provinces]
    L --> M[Apply baseline one-level wave under cap]
    M --> N{Defense in Depth enabled and matured}
    N -->|Yes| O[Select anchors and bounded depth positions]
    N -->|No| P{Fortress States enabled and matured}
    O --> P
    P -->|Yes| Q[Select bounded Fortress States and role packages]
    P -->|No| R{Fortress World enabled and matured}
    Q --> R
    R -->|Yes| S[Select capital and bounded internal redoubts]
    R -->|No| T[Finalize country result]
    S --> T
    T --> U{More snapshotted countries}
    U -->|Yes| J
    U -->|No| V[Finalize global footprint and materialization]
    V --> W[Apply mapped Chaos with guards]
    W --> X[Record one Event 064 history row]
    X --> Y[Record concrete evolution rows]
    Y --> Z[Send local reports to human countries]
    Z --> AA[Resolve AI postures]
    AA --> AB[Open bounded response windows]
    AB --> AC[Clear world candidates and wave context]
    AC --> AD{Country chooses or has posture}
    AD -->|Integrate| AE[Reinforce Priority Sector]
    AD -->|Logistics| AF[Connect New Line]
    AD -->|Breach| AG[Conduct Breach Exercises]
    AD -->|No valid active posture| AH[Close without category]
    AE --> AI{Evolution II or III actions valid}
    AF --> AI
    AG --> AI
    AI -->|Evolution II| AJ[Harden Air or Coastal Flank]
    AI -->|Evolution III| AK[Prepare National Redoubt]
    AI -->|No extra action| AL[Response window continues]
    AJ --> AL
    AK --> AL
    AL --> AM{Project completes or fails}
    AM --> AN[Apply result once and clean target state]
    AN --> AO{Response window or project still active}
    AO -->|Yes| AL
    AO -->|No| AP[Remove posture and hide category]
    AP --> AQ[Physical buildings remain on map]
    AQ --> AR[Later border change does not trigger a world scan]
    AR --> AS[Later Event 064 wave builds a new snapshot]
```

## Evolution package view

```mermaid
flowchart LR
    A[Baseline direct frontier] --> B[One land-fort level under ordinary cap]
    B --> C{Defense in Depth}
    C -->|Active| D[One bounded anchor bonus]
    C -->|Active| E[One-level depth positions]
    D --> F{Fortress States}
    E --> F
    F -->|Active| G[Selected state sectors]
    F -->|Active| H[Role-based AA radar logistics and coast]
    G --> I{Fortress World}
    H --> I
    I -->|Active| J[Capital redoubt]
    I -->|Active| K[Bounded VP supply industry port and site redoubts]
```

## Province overlap view

```mermaid
flowchart TD
    A[Province candidate] --> B{Direct foreign land frontier}
    B -->|No| C{Valid depth or internal role}
    B -->|Yes| D[Baseline grant under ordinary cap]
    D --> E{Strategic anchor selected}
    E -->|Yes| F[Resolve one evolved bonus under anchor cap]
    E -->|No| G{Selected Fortress State sector}
    G -->|Yes| F
    G -->|No| H[No second land-fort grant]
    C -->|Depth| I[One depth grant under depth cap]
    C -->|Internal redoubt| J[One redoubt grant under redoubt cap]
    C -->|No| K[No land-fort change]
    F --> L[Maximum two automatic Event 064 fort levels this wave]
    H --> M[Maximum one automatic Event 064 fort level this wave]
    I --> M
    J --> M
```

## Cluster arbitration view

```mermaid
flowchart TD
    A[Automatic Event 064 selection] --> B[Check Sudden Abundance membership]
    A --> C[Check Military Preparation membership]
    B --> D[Eligible membership set]
    C --> D
    D --> E{Any eligible membership}
    E -->|No| F[Standalone Event 064]
    E -->|Yes| G[Choose at most one membership]
    G --> H{Chosen cluster roll succeeds}
    H -->|No| F
    H -->|Yes| I[Run chosen cluster incident]
    I --> J[Prepare Event 064 member context]
    J --> K[Execute one global Event 064 wave]
    K --> L[One member result and one event history row]
```
