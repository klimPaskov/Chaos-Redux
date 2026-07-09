# Event 018 Resources Found Cave Host Focus Route Diagram

All labels are working labels only. They are not final localisation.

## Lane sketch

```text
row 00                       [Origin nest anchor]
row 01                       [Bodies from the seam]
row 02              [First surface war]     [Hunger remembers]
row 03       [The slow host]  [Lower roads]  [Brood forms]
row 04  Hunger opens    Stone opens    Tunnel opens    Brood method opens          Surface smell
row 05  ore scent       bullets         mine rail       resource wombs              first city fear
row 06  resource fork   armor fork      tunnel fork     method lock                 emptying streets
row 07  old memory      pressure        seam links      swarm or elder split         fear fork
row 08  calculation     cracks          logistics       route development           public hunts
row 09  tenfold rule    siege body      deep road       route payoff                city maw
row 10  hunger capstone stone capstone  tunnel capstone route payoff                terror capstone
row 11                       [Roots of the continent]
row 12                  [Resource knots] [Beneath every border]
row 13              [Against denial lines] [The continent opens]
row 14                       [Stored origin hunger]
row 15                  [Mountain chains] [World below ready]
row 16                       [Maw warning state]
row 17                       [Continental maw capstone]
```

## Mermaid route map

```mermaid
flowchart TB
    A[origin nest anchor] --> B[bodies from the seam]
    B --> C[first surface war]
    B --> D[hunger remembers]
    C --> E[the slow host]
    C --> F[the lower roads]
    D --> F
    D --> G[brood forms]
    C --> H[surface smell]

    D --> H1[scent of ore]
    H1 --> H2[taste of the old field]
    H2 --> H3[rich ground calling]
    H2 --> H4[empty ground disdain]
    H3 --> H5[old resource memory]
    H4 --> H6[rival seams]
    H5 --> H7[hungry calculation]
    H6 --> H7
    H7 --> H8[tenfold rule]
    H8 --> H9[mouth of the vein]

    E --> S1[hardened bodies]
    S1 --> S2[bullets on stone]
    S2 --> S3[deep plates]
    S2 --> S4[mineral wounds close]
    S3 --> S5[pressure carapace]
    S4 --> S6[shells find cracks]
    S5 --> S7[slow siege body]
    S6 --> S7
    S7 --> S8[stone hide capstone]

    F --> T1[lower road sense]
    T1 --> T2[mine rail ghosts]
    T2 --> T3[under the forts]
    T2 --> T4[burrowed reserves]
    T3 --> T5[seam listening]
    T4 --> T6[resource gateways]
    T5 --> T7[closed earth logistics]
    T6 --> T7
    T7 --> T8[deep road capstone]

    G --> B1[brood ordering]
    B1 --> B2[resource wombs]
    B2 --> B3[claim the deep hierarchy]
    B3 --> BS1[many small shapes]
    B3 --> BE1[older bodies]
    BS1 --> BS2[fast awakening]
    BS2 --> BS3[front swarm]
    BS3 --> BS4[broken armor bargain]
    BS4 --> BS5[swarm capstone]
    BE1 --> BE2[long waking]
    BE2 --> BE3[cracking fortified ground]
    BE3 --> BE4[fewer deeper names]
    BE4 --> BE5[elder capstone]

    H --> F1[first city fear]
    F1 --> F2[emptying streets]
    F2 --> F3[night roads]
    F2 --> F4[names in shelters]
    F3 --> F5[failed hunts]
    F4 --> F6[fear crosses borders]
    F5 --> F7[city maw]
    F6 --> F7
    F7 --> F8[surface terror capstone]

    H9 --> M1[roots of the continent]
    T8 --> M1
    M1 --> M2[resource knots]
    M1 --> M3[beneath every border]
    M2 --> M4[against denial lines]
    M3 --> M5[the continent opens]
    M4 --> M6[stored origin hunger]
    M5 --> M6
    M6 --> M7[across mountain chains]
    M6 --> M8[world below ready]
    M7 --> M9[maw warning state]
    M8 --> M9
    F8 --> M9
    M9 --> M10[continental maw capstone]
```

## Route lock notes

- Swarm and elder routes must be mutually exclusive.
- Hunger, stone hide, tunnel, surface terror, and continental maw are compatible paths.
- Continental maw needs a territory and chaos gate even when focus prerequisites are met.
- Surface terror should require public Host violence, not only an early focus click.
- Existing branch completion should change decision categories and AI behaviour where possible.

## Final layout warning

The diagram is a design map. It should not force final in-game coordinates if the actual focus file becomes ugly. The final tree should use readable lanes, comfortable spacing, and no duplicate coordinates. The route coverage table in Part 7 is the acceptance target.
