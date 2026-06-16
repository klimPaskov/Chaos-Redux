# Event 012 Africa — Focus Tree Architecture Sketch

The Mermaid file `012_africa_focus_tree_architecture.mmd` is a route sketch, not a final HOI4 coordinate map. The implementation agent should use it to preserve branch shape, route locks, convergence, hidden/high-chaos paths, and late-game sequence while creating a clean in-game focus layout.

```mermaid
flowchart TD
    A[The Continental Proclamation] --> B[Assemble the Proclamation Congress]
    B --> C[Choose the Shape of Unity]

    C --> F1[Federal Congress Route]
    C --> F2[People's Liberation Front Route]
    C --> F3[Continental General Staff Route]
    C --> F4[Crown Congress and Old Thrones Route]
    C --> F5[Green Covenant High-Chaos Route]

    B --> I[Continental Works Branch]
    B --> M[Continental Army Branch]
    B --> D[Charter League Diplomacy Branch]
    B --> E[Expansion and Integration Branch]
    B --> R[Diaspora Return Branch]

    F1 --> U[The Living Union]
    F2 --> S[Scramble for Africa Crisis]
    F3 --> S
    F4 --> U
    F5 --> U
    I --> U
    M --> S
    D --> U
    E --> U
    R --> U

    U --> UA[Africa Is One]
    UA --> P1[Guard the Continent]
    UA --> P2[Sponsor Other Continental Unifiers]
    UA --> P3[Cross-Continental Union Names]
    P2 --> CU[Dynamic Union Formation]
    CU --> W[The World Is One Terminal Path]

    RSA[RSA Selected and in Allies] --> RSA1[South African Civil War]
    RSA1 --> RSA2[Continental Proclamation Victory]
    RSA2 --> RSA3[Allied Peace with Africa]
    RSA3 --> B
```

## Archive of Old Seats overlay

```mermaid
flowchart TD
    CL[Charter League Established] --> AOS[Open the Archive of Old Seats]
    AOS --> RF[The First Regional Files]
    RF --> RC[Rivers and Crowns]
    RF --> SS[Stone and Stelae]
    RF --> DB[Desert Books]
    RF --> LC[Lake Courts]
    RF --> CO[Coastal Ledgers]
    RF --> Fork{Restoration Policy}
    Fork --> Respect[Respect the Old Seats]
    Fork --> Counterfeit[Documents Before Consent]
    Fork --> Central[Seal Them Under One Archive]
    Respect --> Settlement[Peaceful Settlements]
    Counterfeit --> Forgery[Forgery Exposure Missions]
    Central --> Direct[Central Archive Integration]
    Settlement --> Bestiary{Evolution III Bestiary Clause?}
    Forgery --> Bestiary
    Direct --> Bestiary
    Bestiary -->|Sign| Nonhuman[Nonhuman Observer Seats]
    Bestiary -->|Break| Extraction[Anti-Bestiary Extraction]
    Nonhuman --> Parliament[Parliament of Root and Fang]
    Extraction --> Revolt[Forest/Herds Revolt Risk]
```

## Niche country unlock graph

# Event 012 Africa — Niche Country Unlock Graph

```mermaid
flowchart TD
    A[Proclamation Congress] --> B[Charter League]
    B --> C[Register the Names]
    C --> D[Seat the First Courts]
    D --> E[Archives Before Armies]
    E --> F[Local Guards, Continental Oaths]
    F --> G{The Autonomy Question}
    G --> H[Federal Preservation]
    G --> I[War Office Centralisation]
    G --> J[Crown Seats]
    G --> K[Municipal Congresses]
    G --> L[Green Covenant Consent]
    H --> M[Many Names, One Congress]
    I --> M
    J --> M
    K --> M
    L --> N[The Lands Remember Their Names]
    M --> O[A Congress Larger Than History]
    N --> P[Mythic Memory Routes]
    P --> Q[Nonhuman Forest Pacts]
    P --> R[River / Stone / Pattern / Monsoon Absurd Routes]
    O --> S[Africa Is One]
    Q --> S
    R --> S
```
