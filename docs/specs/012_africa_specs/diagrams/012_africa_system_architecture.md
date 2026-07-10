# Event 12 Africa system architecture

This diagram is a design guide, not final HOI4 GUI geometry or script structure.

```mermaid
flowchart TD
    A[Event 12 selects valid African-capital host] --> B[Host legitimacy and regional overlay]
    B --> C[Protection-first opening]
    C --> D[Charter League formation]
    D --> E[Member relationships]
    D --> F[Regional congresses]
    D --> G[Corridor and development network]
    D --> H[Common reserve and intervention]
    D --> I[Diaspora trust and return]

    E --> J{Constitutional route}
    J --> J1[Charter Federalism]
    J --> J2[Continental Republic]
    J --> J3[Council of Crowns]
    J --> J4[People's Union]
    J --> J5[Military Continentalism]
    J --> J6[Continental Confederation]
    J --> J7[High-chaos Covenant]

    F --> K[Claim-overlap settlements]
    F --> L[Restored polity packages]
    G --> M[Resource sovereignty]
    G --> N[Food security]
    G --> O[Rail, river, road, port, and air links]
    H --> P[Protection wars]
    H --> Q[Colonial intervention response]
    I --> R[Voluntary travel]
    I --> S[Citizenship and representation]
    I --> T[Skills, capital, and local projects]

    E --> U[Member confidence crises]
    U --> U1[Concessions and recovery]
    U --> U2[Peaceful departure]
    U --> U3[Rival African bloc]
    U --> U4[War]

    K --> V[Regional readiness]
    L --> V
    M --> V
    N --> V
    O --> V
    P --> V
    R --> V

    V --> W[Africa is one threshold]
    W --> X[Scramble response crisis]
    X --> X1[Recognition and negotiated withdrawal]
    X --> X2[Sanctions and containment]
    X --> X3[Expeditionary coalition]
    X --> X4[African defensive war]

    B --> Y[Evolution system]
    Y --> Y1[Evolution I, continental consolidation]
    Y1 --> Y2[Evolution II, stronger integration and strange formations]
    Y2 --> Y3[Evolution III, high-chaos actors and world-order content]
    Y3 --> Z[Post-unification Evolution IV escalation layer]

    Z --> AA[Other continent unifiers]
    AA --> AB[Alliance, sponsorship, rivalry, federation, or union]
    AB --> AC[Continental wars]
    AC --> AD[Last eligible continent-scale power]
    AD --> AE[The World terminal identity]
```

## Reading notes

- Protection, member agency, development, military preparation, diaspora return, and restoration operate in parallel.
- Constitutional routes change integration policy and political identity without closing the support branches by default.
- Rival blocs and member departure are normal political outcomes, not script failures.
- High-chaos content enters after the grounded continental system is already established.
- Scramble response is a global reaction to successful unification.
- The World is a rare terminal identity after every continent-scale rival is resolved.
