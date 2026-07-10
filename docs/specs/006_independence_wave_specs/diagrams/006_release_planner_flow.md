# Release planner flow

This diagram is a design guide. It is not final script.

```mermaid
flowchart TD
    A[Read chaos band and required count] --> B[Build ready candidate pool]
    B --> C[Remove living tags and invalid origins]
    C --> D[Identify hosts and reserve protected states]
    D --> E[Remove candidates with invalid anchors]
    E --> F[Score novelty, region, host diversity, readiness, and wave memory]
    F --> G[Select unique candidate anchors]
    G --> H[Assign compact or extended territory]
    H --> I{Any overlap or host deletion risk?}
    I -- Yes --> J[Trim optional states]
    J --> K{Candidate still valid?}
    K -- No --> L[Replace candidate from ranked reserve]
    K -- Yes --> M[Recheck all hosts]
    L --> H
    M --> I
    I -- No --> N[Lock synchronized plan]
    N --> O[Release all countries]
    O --> P[Apply Event 6 origin and package]
    P --> Q[Create government, values, ideas, forces, focus content, and AI]
    Q --> R[Create host relations and network records]
    R --> S[Fire country openings, host crises, and wave summary]
```

## Priority order when a conflict appears

1. Preserve every host.
2. Preserve each selected candidate's unique anchor.
3. Trim ambition territory.
4. Trim extended territory.
5. Trim compact territory to the anchor.
6. Replace the candidate.
7. Accept a documented shortfall only when no replacement exists.
