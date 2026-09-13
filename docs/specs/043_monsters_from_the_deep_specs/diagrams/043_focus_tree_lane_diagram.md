# Event 043 full-monster focus-tree lane diagram

```mermaid
flowchart LR
    O[Opening survival] --> A1[Apex entry]
    O --> B1[First brood]
    O --> C1[Second coastal objective]

    A1 --> A2[Apex identity upgrade]
    A2 --> A3[Signature power]
    A3 --> A4[Apex capstone]

    B1 --> B2[Second support family]
    B2 --> B3[Lair support]
    B3 --> B4[Brood capstone]

    C1 --> C2[Additional lair]
    C2 --> C3[Landward adaptation]
    C3 --> C4[Continental Hunger or creature corridor]

    A2 --> P0[Route commitment]
    B2 --> P0
    C2 --> P0

    P0 --> P1[Pact route]
    P0 --> S1[Solitary route]

    P1 --> P2[Truce objective]
    P2 --> P3[Compact]
    P3 --> P4[Abyssal faction]
    P4 --> PT[Terminal pact readiness]

    S1 --> S2[Rival apex hunt]
    S2 --> S3[Dominion control]
    S3 --> S4[Solitary capstone]
    S4 --> ST[Apex Dominion readiness]

    O --> F1[Hidden crisis lane]
    F1 --> F2[Hunger crisis response]
    F1 --> F3[Sea Bond crisis response]
    F2 --> F4[Recovery or remnant handoff]
    F3 --> F4

    PT --> T[Hidden Event 043 terminal branch]
    ST --> T
    C4 --> T
```

## Layout rules

- Apex, brood, and range lanes stay visually separate.
- Pact and solitary routes split from one clear commitment.
- Crisis content occupies a compact lower lane.
- Terminal content stays hidden until Evolution II and World Collapse.
- Connector lines remain short and do not cross unrelated lanes.
- Focus Navigation targets each major lane.
