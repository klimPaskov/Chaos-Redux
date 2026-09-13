# Candidate Generation Flow

```mermaid
flowchart TD
    A[Bounded generation moment] --> B[Validate host country]
    B --> C{Ordinary civilian country with usable territory}
    C -->|No| Z[Reject host]
    C -->|Yes| D[Build meaningful node pool]
    D --> E[Build connected route and facility pool]
    E --> F[Apply hard project family validity]
    F --> G[Exclude hostile impossible duplicate and locked candidates]
    G --> H[Score valid candidates]
    H --> I[National integration role]
    H --> J[Economic extraction or trade role]
    H --> K[Geography specific opportunity role]
    I --> L[Diversity selection]
    J --> L
    K --> L
    L --> M[Store three stable proposals]
    M --> N[Display actual states partners purpose duration and risk]
    N --> O{Proposal state changes}
    O -->|Accepted| P[Convert to active project]
    O -->|Still valid| Q[Keep stable]
    O -->|Invalid| R[Automatic bounded replacement]
    O -->|Paid survey after cooldown| S[Replace full set]
    R --> D
    S --> D
```

## Hard and soft gates

Hard validity determines whether a project can exist. Soft scoring determines whether a valid project is attractive. A low score can reduce selection. It can never make an invalid fixed link or foreign route appear.
