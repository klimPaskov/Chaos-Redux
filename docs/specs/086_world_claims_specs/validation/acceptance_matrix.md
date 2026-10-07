# World Claims: acceptance scenarios

Status legend: **engine pending** means not executed in HOI4 or its MCP environment. The included abstract tests exercise only a Python model of selected contracts and do not upgrade any row below to engine-passed.

| ID | Scenario and expected result | Gate | Status |
| --- | --- | --- | --- |
| T01 | Independent minor and major each receive every foreign land-neighbor, with no country privilege | G3 | Engine pending |
| T02 | Country owns a disconnected overseas state; both owned components seed their actual land frontiers | G3 | Engine pending |
| T03 | Country controls but does not own a distant state; it is not a frontier seed | G3 | Engine pending |
| T04 | Island/no-land-neighbor country gets no claims at every profile including V | G3 | Engine pending |
| T05 | Sea adjacency, sea-classified strait, impassable border and corner touch are not silently treated as valid land edges | G3 | Engine pending |
| T06 | Immediate ring exceeds 100 states; every valid target still included | G3 | Engine pending |
| T07 | Optional budget exhausts halfway through a ring; no disconnected later-ring target appears | G3 | Engine pending |
| T08 | Country iteration order and callback order change; logical wave results do not | G3/G6 | Engine pending |
| T09 | Repeated profile I wave without conquest cannot exceed owned depth two | G3 | Engine pending |
| T10 | V grows only one layer from old connected network; fresh targets do not recursively seed it | G3 | Engine pending |
| T11 | Detached historical claim component and unrelated native claims do not seed V extension | G3 | Engine pending |
| T12 | Another event already issued the claim; a valid wave still records independent WC provenance | G1/G3 | Engine pending |
| T13 | Unrelated distant legacy world claim has no WC integration entitlement | G1/G6 | Engine pending |
| T14 | First control at 0, 40, and 90 Compliance applies a max floor, never lowers or adds the ceiling | G1 | Engine pending |
| T15 | Two claimants occupy the same state sequentially; each has isolated legitimate Compliance history | G1 | Engine pending |
| T16 | Loss and recapture do not refill a consumed starting entitlement | G1/G2 | Engine pending |
| T17 | Higher entitlement upgrades once; II→III and IV→V do not duplicate equal ceilings | G1 | Engine pending |
| T18 | Higher stage activates while target uncontrolled; grant waits for claimant control and available context | G1 | Engine pending |
| T19 | Existing native core does not receive occupation grant or duplicate core reward | G1/G2 | Engine pending |
| T20 | New conquest at IV/V does not core immediately despite 100 starting Compliance | G2 | Engine pending |
| T21 | III exact 360/80/60, IV 120/90/30, V 30/95/10 thresholds qualify inclusively | G2 | Engine pending |
| T22 | One day short or a sub-threshold current Compliance fails core eligibility | G2 | Engine pending |
| T23 | Brief control loss between scheduled checks resets continuity, including save/load across loss | G2/G6 | Engine pending |
| T24 | Drop below 95 but above 90 resets only the 95 clock | G2 | Engine pending |
| T25 | Connection credit cannot bypass physical minima or high-Compliance interval | G2 | Engine pending |
| T26 | Core under occupation preserves another owner's legal ownership and other countries' cores | G2 | Engine pending |
| T27 | Stage disable stops future benefit, does not revoke actual claims/cores or reset receipts | G1/G2/G7 | Engine pending |
| T28 | High first opening uses complete enabled profile, lower stage disabled does not block higher stage | G7 | Engine pending |
| T29 | Threshold reached makes Evolution eligible, does not itself award extra claim wave or Chaos | G7 | Engine pending |
| T30 | Candidate follows actual new overseas center, not only original capital or major status | G4 | Engine pending |
| T31 | Adopted envelope and anchors do not shrink when territory is lost | G4 | Engine pending |
| T32 | Exact Q/E and I/Q integer thresholds agree across preview, GUI, decision and AI | G4/G5 | Engine pending |
| T33 | Subject and ally holdings do not count in generic dynamic formation | G4 | Engine pending |
| T34 | Native provider with missing DLC, ideology, focus or valid tag cannot be bypassed | G4 | Engine pending |
| T35 | Native provider cost/effects commit once with compatible WC recognition only once | G4/G6 | Engine pending |
| T36 | Cosmetic name/flag changes preserve all unrelated country content and claimant epoch | G4/G6 | Engine pending |
| T37 | Rival countries keep overlapping ambitions, claims and records independently | G1/G4 | Engine pending |
| T38 | Recreated tag does not inherit old jobs, grants or reward receipts without explicit succession | G6 | Engine pending |
| T39 | Peace, civil war, scripted transfer, annexation, release and native formation refresh relevant records | G6 | Engine pending |
| T40 | Civil project pays frozen price once, affects one state only, succeeds once, fails on lost target/anchor | G1/G6/G8 | Engine pending |
| T41 | Corridor project requires actual two-anchor route and valid native connection at deadline | G2/G8 | Engine pending |
| T42 | Assurance acceptance with either party unaffordable charges neither | G6/G8 | Engine pending |
| T43 | Passive new claim does not breach assurance; actual incompatible pursuit breaches once | G6/G8 | Engine pending |
| T44 | Confidence success/failure replaces one temporary state, never stacks permanent additions | G8 | Engine pending |
| T45 | Identical territory under new name cannot reissue proclamation rewards | G4/G6 | Engine pending |
| T46 | Projects ≤2, assurances ≤2, primary actions ≤6, payment types ≤4, inline costs ≤3 | G5/G8 | Engine pending |
| T47 | Exact-state geometry is active-map-backed, every needed page compiled, dormant unknown entries fail visibly | G5 | Engine pending |
| T48 | State pieces, counts, summary, decision and AI call one live qualification policy | G5 | Engine pending |
| T49 | Every formation/integration category has correct puzzle attachment and generated window | G5 | Engine pending |
| T50 | Long names, non-ASCII text, missing localisation, hover, optional-hidden, empty and ready states render correctly at all supported resolutions | G5 | Engine pending |
| T51 | Native DDS decode equals source PNG, native flag formats/sizes and political variants complete | G5/G8 | Engine pending |
| T52 | Global ambition reveals objective universe without granting it all as claims | G3/G4 | Engine pending |
| T53 | Global proclamation does not satisfy finished-world milestone while a foreign survivor remains | G4/G8 | Engine pending |
| T54 | Chaos wave alternatives/caps and linked reversals are idempotent across load, repeated offers and callbacks | G6/G8 | Engine pending |
| T55 | Ordinary wars/annexations are not double charged through WC | G8 | Engine pending |
| T56 | Eight achievements use committed historical receipts, not current names or guessed migrated history | G6/G8 | Engine pending |
| T57 | Large active country/state network has bounded job work and measured save/runtime footprint, no periodic world GUI scan | G7 | Engine pending |
| T58 | Two-player wave, rival occupation, save/load, delayed acknowledgement and client order remain synchronized | G3/G6/G7 | Engine pending |
| T59 | Installed map renumber/split mismatch blocks or migrates explicitly, never maps old records by guess | G5/G6 | Engine pending |
| T60 | Catalog remains accurate, old Germany-only route unreachable, mandatory external reads and specialist reviews completed before full closure claim | G8 | Engine pending |
