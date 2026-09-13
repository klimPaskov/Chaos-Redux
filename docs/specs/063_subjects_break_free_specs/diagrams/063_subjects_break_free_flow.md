# Event 063 flow diagrams

## Firing transaction

```mermaid
flowchart TD
    A[Event 063 selected] --> B{Any valid subjects?}
    B -->|No| C[Weight displays N/A and firing fails closed]
    B -->|Yes| D[Freeze candidate snapshot]
    D --> E[Choose release count from pool band]
    E --> F[Select subjects without replacement]
    F --> G[Reserve subjects and relations]
    G --> H{All required reservations valid?}
    H -->|Before first release, no| I[Use frozen fallbacks]
    I --> G
    H -->|Yes| J[Release each valid subject in place]
    J --> K[Record shared liberation origin]
    K --> L[Resolve subject posture and overlord policy]
    L --> M{Settlement result}
    M --> N[Negotiated separation]
    M --> O[Recognized unilateral separation]
    M --> P[Contested separation]
    M --> Q[Armed refusal when safe]
    N --> R[Evaluate recognition and network support]
    O --> R
    P --> R
    Q --> S[Build independence war theater]
    S --> R
    R --> T[Evaluate cohort and Pact opportunities]
    T --> U[Publish one global report and direct human notices]
    U --> V[Record event and evolution history]
    V --> W[Clear reservations and temporary context]
```

## Candidate and cohort selection

```mermaid
flowchart LR
    A[Valid subject pool] --> B[Score autonomy, strength, overlord pressure, relations, claims, network support, and cooldown]
    B --> C{Evolution I active?}
    C -->|No| D[Select across different overlords where possible]
    C -->|Yes| E[Choose one eligible cohort host]
    E --> F[Select two to five subjects of that overlord]
    F --> G[Fill remaining slots from global pool]
    D --> H[Freeze alternates]
    G --> H
    H --> I[Reserve entire batch]
```

## Settlement resolution

```mermaid
flowchart TD
    A[Independence already complete] --> B[Subject chooses conciliatory, guarded, or defiant posture]
    A --> C[Former overlord chooses recognition, association, contest, or restoration]
    B --> D[Combine choices with frozen relation facts]
    C --> D
    D --> E{Safe common relationship?}
    E -->|Yes| F[Negotiated separation]
    E -->|No, recognition still accepted| G[Unilateral recognized separation]
    E -->|No recognition, no safe war| H[Contested separation]
    E -->|No recognition and safe war| I{Evolution II and cohort?}
    I -->|No| J[Single baseline independence war, rare]
    I -->|Yes| K[Compound independence war]
    H --> L[Recognition, mediation, ultimatum, or border incident]
    J --> M[War settlement]
    K --> M
```

## Shared origin and ownership

```mermaid
flowchart TD
    A[Owner event completes a valid liberation] --> B[Neutral liberation-origin adapter]
    B --> C[Record first origin if absent]
    B --> D[Record latest liberation event and former overlord]
    B --> E[Set active network state]
    C --> F[Neutral compatibility queries]
    D --> F
    E --> F
    F --> G[Recognition]
    F --> H[Material support]
    F --> I[Pact eligibility]
    F --> J[Intervention evaluation]

    K[Event 006 private release ledger] -. remains owner controlled .-> A
    L[Event 005 successor and League systems] -. remains owner controlled .-> A
    M[Event 063 subject release and settlement] -. remains owner controlled .-> A
```

## Liberation Pact lifecycle

```mermaid
flowchart TD
    A[Evolution III active] --> B{Enough compatible active liberated states?}
    B -->|No| C[Informal network continues]
    B -->|Yes| D[Founder prepares congress]
    D --> E[Freeze invitation pool]
    E --> F[Invite full members, partners, and observers]
    F --> G{Minimum full membership accepted?}
    G -->|No| H[Congress fails and receives cooldown]
    H --> C
    G -->|Yes| I[Create Liberation Pact]
    I --> J[Initialize Liberation Cohesion]
    J --> K[Recognition, aid, mediation, and collective defense]
    K --> L{Member or leadership failure?}
    L -->|No| K
    L -->|Yes| M[Transfer leader, suspend member, mediate, or expel]
    M --> N{At least two members and Cohesion above collapse gate?}
    N -->|Yes| K
    N -->|No after grace period| O[Dissolve formal Pact]
    O --> C
```

## Independence-war support ladder

```mermaid
flowchart LR
    A[Recognition] --> B[Equipment, fuel, convoys, or civilian support]
    B --> C[Advisers or volunteers]
    C --> D[Guarantee]
    D --> E[Direct war entry]
```

A supporter should choose the lowest level that can materially help. Direct war entry requires access, capacity, compatibility, and a free theater slot.
