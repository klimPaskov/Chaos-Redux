# Release planner flow

This diagram is a design guide. It is not final script.

```mermaid
flowchart TD
    A[Read chaos band and required count] --> B[Build ready candidate pool]
    B --> C[Remove living tags and invalid origins]
    C --> D[Score novelty, region, host diversity, readiness, and wave memory]
    D --> E[Try one tag, host, protected host state, and unique anchor]
    E --> F{Anchor row valid?}
    F -- No --> G[Rollback provisional tail and reroll]
    G --> E
    F -- Yes --> H[Freeze country and anchor row]
    H --> I{Exact country count reached?}
    I -- No --> E
    I -- Yes --> J[Run compact pass across every frozen country]
    J --> K[Trim optional collisions and host-survival risks]
    K --> L[Run extended pass across every frozen country]
    L --> M[Trim optional collisions and host-survival risks]
    M --> N{Aligned rows, exact count, unique anchors, and host survival valid?}
    N -- No --> O[Abort structurally invalid plan before ownership mutation]
    N -- Yes --> P[Lock synchronized plan]
    P --> Q[Release all countries]
    Q --> R[Transfer and verify every frozen state]
    R --> S[Apply Event 6 origin and package]
    S --> T[Create government, values, ideas, forces, focus content, and AI]
    T --> U[Create host relations and network records]
    U --> V[Fire country openings, host crises, and wave summary]
```

## Priority order when a conflict appears

1. Preserve every host.
2. Preserve each selected candidate's unique anchor.
3. Keep ambition territory outside the automatic release footprint; preserve it as later claims, negotiations, missions, or formable requirements.
4. Trim extended territory.
5. Trim compact territory to the anchor.
6. During anchor selection only, replace an invalid candidate and continue until the exact count is reached or the incident aborts before mutation.

The ambition step is not a fourth release tier. Part 1's package contract is authoritative: automatic and scenario allocation reserves anchor, compact, and extended states only, while ambition territory remains playable post-release content.
