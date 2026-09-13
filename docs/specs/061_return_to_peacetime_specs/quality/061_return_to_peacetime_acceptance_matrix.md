# Event 061 acceptance matrix

## Status meaning

`Specified` means the source package contains a concrete requirement and implementation direction.

`Pending implementation` means no gameplay, final asset, workbook, probability, or in-game evidence is claimed by this planning package.

Implementation should replace the final column with Pass, Failed, Blocked, or Not applicable and link the exact evidence.

## Matrix

| ID | Requirement | Specification | Required implementation evidence | Planning status | Runtime status |
| --- | --- | --- | --- | --- | --- |
| A01 | Event ID remains 61 | Part 1 | Registration and catalog diff | Specified | Pending implementation |
| A02 | Event name is Return to Peacetime | Part 1 | Localisation and workbook diff | Specified | Pending implementation |
| A03 | Type remains Minor Repeatable | Parts 1 and 7 | Event type helper and workbook | Specified | Pending implementation |
| A04 | Minimum Chaos level remains 1 | Parts 1 and 7 | Registration and workbook | Specified | Pending implementation |
| A05 | Canonical entry remains chaosx.nr61.1 | Parts 1 and 7 | Event source | Specified | Pending implementation |
| A06 | Every valid normal civilian country is processed once | Part 1 | Controlled global firing test | Specified | Pending implementation |
| A07 | One global cycle ID guards each firing | Part 7 | Save-safe variable test | Specified | Pending implementation |
| A08 | One global Event Logs history entry is recorded | Parts 1 and 7 | Event Logs output | Specified | Pending implementation |
| A09 | Every human country receives one national report | Part 1 | Multiplayer test | Specified | Pending implementation |
| A10 | AI countries resolve without popup spam | Part 1 | AI global firing test | Specified | Pending implementation |
| A11 | Shared Minor Repeatable weight and cap rules apply | Parts 1 and 4 | Repeatable state inspection | Specified | Pending implementation |
| A12 | Evolution activation follows shared pacing | Parts 3 and 7 | Evolution-system evidence | Specified | Pending implementation |
| A13 | Evolution activation adds zero Event 61 Chaos | Parts 1 and 3 | Chaos source audit | Specified | Pending implementation |
| B01 | Eligible factories are physical military levels in owned and controlled states | Part 1 | State test matrix | Specified | Pending implementation |
| B02 | Baseline conversion amount equals floor of eligible factories divided by two | Part 1 | Integer boundary tests | Specified | Pending implementation |
| B03 | One eligible military factory remains unchanged | Part 1 | One-factory test | Specified | Pending implementation |
| B04 | Every conversion removes one military factory and adds one civilian factory | Part 1 | Atomic transaction log | Specified | Pending implementation |
| B05 | Every successful conversion increments state ledger by one | Parts 1 and 7 | State variable test | Specified | Pending implementation |
| B06 | Failed conversion records no civilian factory or ledger | Parts 1 and 7 | Forced failure test | Specified | Pending implementation |
| B07 | New civilian construction never creates ledger | Parts 1 and 5 | Construction exploit test | Specified | Pending implementation |
| B08 | Annexation never creates ledger | Parts 1 and 5 | Annexation exploit test | Specified | Pending implementation |
| B09 | Ledger follows state ownership | Parts 1 and 5 | Ownership transfer test | Specified | Pending implementation |
| B10 | Only current valid owner and controller can reopen | Parts 1 and 2 | State target test | Specified | Pending implementation |
| B11 | Reopening consumes one civilian level and one ledger unit | Parts 1 and 2 | Atomic restoration test | Specified | Pending implementation |
| B12 | Destroyed or missing civilian capacity is not recreated free | Parts 1 and 5 | Building destruction test | Specified | Pending implementation |
| B13 | Permanent conversion clears ledger and retains civilians | Parts 1 and 2 | Confirmation and state test | Specified | Pending implementation |
| B14 | Repeat firing appends new ledgered conversions | Part 1 | Two-cycle test | Specified | Pending implementation |
| B15 | Country ledger cache reconciles from authoritative states | Part 7 | Ownership reconciliation log | Specified | Pending implementation |
| C01 | Half of current War Support is removed | Part 1 | Value test at several inputs | Specified | Pending implementation |
| C02 | The same amount is added to Stability | Part 1 | Value test at several inputs | Specified | Pending implementation |
| C03 | Stability ceiling overflow is lost and reported | Part 1 | High-Stability test | Specified | Pending implementation |
| C04 | No overflow reserve meter exists | Part 1 | Variable and UI audit | Specified | Pending implementation |
| C05 | Economy law moves one adjacent step toward Civilian Economy | Part 1 | Law ladder tests | Specified | Pending implementation |
| C06 | Conscription law moves one adjacent step toward Disarmed Nation | Part 1 | Law ladder tests | Specified | Pending implementation |
| C07 | Baseline does not force Peacetime Economy | Part 1 | Law-floor test | Specified | Pending implementation |
| C08 | Baseline does not force No Army | Part 1 | Law-floor test | Specified | Pending implementation |
| C09 | Law change does not add fake manpower | Part 1 | Manpower diff test | Specified | Pending implementation |
| C10 | Deployed manpower returns only through safe disband | Parts 1 and 3 | Unit disband test | Specified | Pending implementation |
| C11 | Highest unresolved economy restore rank is preserved | Parts 1 and 7 | Repeat-cycle law test | Specified | Pending implementation |
| C12 | Highest unresolved conscription restore rank is preserved | Parts 1 and 7 | Repeat-cycle law test | Specified | Pending implementation |
| C13 | External upward law change blocks duplicate restoration | Parts 1, 4, and 5 | Event 82 integration test | Specified | Pending implementation |
| C14 | Unknown incompatible law token fails closed | Parts 1 and 4 | Custom-law compatibility test | Specified | Pending implementation |
| D01 | One staged Industrial Reconversion Shock is used | Part 1 | Idea-state inspection | Specified | Pending implementation |
| D02 | Default lifecycle has three 90-day phases | Part 1 | Timed stage test | Specified | Pending implementation |
| D03 | Severe phase applies major military output penalty | Part 1 | Modifier inspection | Specified | Pending implementation |
| D04 | Repeat firing returns to severe phase | Part 1 | Repeat timing test | Specified | Pending implementation |
| D05 | Remaining duration is capped at 540 days | Parts 1 and 5 | Repeated firing stress test | Specified | Pending implementation |
| D06 | Shock copies never stack | Parts 1 and 5 | Idea stack test | Specified | Pending implementation |
| D07 | High Readiness mitigates only later phases | Part 1 | Readiness timing test | Specified | Pending implementation |
| E01 | One public Readiness value ranges from 0 to 100 | Part 2 | UI and variable inspection | Specified | Pending implementation |
| E02 | Five hidden pillars contribute no more than 20 each | Part 2 | Calculation trace | Specified | Pending implementation |
| E03 | Only qualitative pillar states are shown | Part 2 | UI review | Specified | Pending implementation |
| E04 | Readiness recalculates after every Event 61 action | Part 2 | Action trace | Specified | Pending implementation |
| E05 | Bounded active-country pulse catches external changes | Parts 1 and 7 | Pulse test | Specified | Pending implementation |
| E06 | No permanent whole-world pulse is added | Parts 1 and 5 | On-action audit | Specified | Pending implementation |
| E07 | Meaningful rearmament needs Readiness 50 | Part 2 | Threshold test | Specified | Pending implementation |
| E08 | Meaningful rearmament also needs factory or law proof | Part 2 | Structural proof test | Specified | Pending implementation |
| E09 | Category shows at most five primary actions | Part 2 | UI audit | Specified | Pending implementation |
| E10 | Category shows at most one active mission | Part 2 | Mission overlap test | Specified | Pending implementation |
| E11 | At most three state reopening targets are visible | Part 2 | Large-ledger UI test | Specified | Pending implementation |
| E12 | Category phases hide obsolete actions | Part 2 | Phase progression test | Specified | Pending implementation |
| E13 | Category closes only after all Event 61 state resolves | Parts 1 and 2 | Cleanup test | Specified | Pending implementation |
| F01 | Restart Arms Contracts uses political power and civilian commitment | Part 2 | Decision cost test | Specified | Pending implementation |
| F02 | Arms contracts unlock factory reopening | Part 2 | Progression test | Specified | Pending implementation |
| F03 | State reopening uses current valid target state | Part 2 | Target invalidation test | Specified | Pending implementation |
| F04 | State reopening batch is bounded from one to five | Part 2 | Small and major tests | Specified | Pending implementation |
| F05 | General Staff uses institutional costs and affects later protection | Part 2 | Decision and evolution trace | Specified | Pending implementation |
| F06 | Public defence transfer is inefficient and cooldown-bound | Part 2 | Repeat farming test | Specified | Pending implementation |
| F07 | Economy law restoration stops at Event 61 target | Part 2 | Law ceiling test | Specified | Pending implementation |
| F08 | Conscription restoration stops at Event 61 target | Part 2 | Law ceiling test | Specified | Pending implementation |
| F09 | Emergency Rearmament needs concrete danger | Part 2 | Safe-peace invalidation test | Specified | Pending implementation |
| F10 | Emergency Rearmament is once per cycle | Parts 2 and 5 | Cycle guard test | Specified | Pending implementation |
| F11 | Emergency Rearmament applies real aftermath | Part 2 | Idea and cost inspection | Specified | Pending implementation |
| F12 | Permanent conversion requires irreversible confirmation | Part 2 | Player UI test | Specified | Pending implementation |
| F13 | National Rearmament Program checks 60 Readiness and two actions | Part 2 | Mission success test | Specified | Pending implementation |
| F14 | Failed national program keeps completed structures | Part 2 | Mission failure test | Specified | Pending implementation |
| F15 | Extreme-law recovery starts with Defence Ministry | Part 2 | Recovery progression test | Specified | Pending implementation |
| F16 | Ledger-free country has a costly minimum-arsenal fallback | Part 2 | Zero-ledger extreme-law test | Specified | Pending implementation |
| F17 | Service Registry does not require army experience or manpower | Part 2 | No Army soft-lock test | Specified | Pending implementation |
| F18 | Universal cost framework owns commitments and cleanup | Parts 2 and 7 | Cost framework audit | Specified | Pending implementation |
| G01 | High-Chaos evolved effects are staggered | Part 3 | Timeline test | Specified | Pending implementation |
| G02 | Disabled Evolution I does not block Evolution II | Part 3 | Enable-state test | Specified | Pending implementation |
| G03 | Disabled earlier stages do not block Evolution III | Part 3 | Enable-state test | Specified | Pending implementation |
| G04 | Newly activated evolution reaches active transitions | Part 3 | Mid-cycle activation test | Specified | Pending implementation |
| G05 | Every evolution resolves once per country and cycle | Parts 3 and 7 | Idempotence test | Specified | Pending implementation |
| G06 | Repeat cycles merge matching visible missions | Parts 1 and 3 | Repeat overlap test | Specified | Pending implementation |
| G07 | Merged pressure remains capped | Parts 3 and 5 | Stress test | Specified | Pending implementation |
| H01 | Inventory Liquidation provides a useful response window | Part 3 | Mission timing test | Specified | Pending implementation |
| H02 | Only positive supported conventional stockpile is eligible | Part 3 | Stockpile family test | Specified | Pending implementation |
| H03 | Reserve floors protect active military need | Part 3 | Shortage test | Specified | Pending implementation |
| H04 | Ships, nuclear assets, missiles, projects, and unknown special gear are excluded | Part 3 | Mixed-stockpile test | Specified | Pending implementation |
| H05 | Captured and obsolete variants receive priority when supported | Part 3 | Variant selection test | Specified | Pending implementation |
| H06 | Base share begins near 25 percent of eligible surplus | Part 3 | Controlled surplus test | Specified | Pending implementation |
| H07 | Dynamic share remains within planned normal range | Part 3 | Readiness and war sweep | Specified | Pending implementation |
| H08 | Only relevant protection families appear | Part 3 | Decision pool test | Specified | Pending implementation |
| H09 | No more than three protection decisions appear | Part 3 | Large-stockpile UI test | Specified | Pending implementation |
| H10 | Protected family share falls to a very low band | Part 3 | Protection result test | Specified | Pending implementation |
| H11 | Central Reconstruction has complete base behavior | Part 3 | Disposition test | Specified | Pending implementation |
| H12 | Civilian Auctions has complete DLC-safe base behavior | Part 3 | No-DLC test | Specified | Pending implementation |
| H13 | Reward uses actual removed value | Parts 3 and 7 | Partial debit test | Specified | Pending implementation |
| H14 | Reconstruction Materials is tiered and capped | Parts 3 and 5 | Huge-stockpile test | Specified | Pending implementation |
| H15 | Event 94 forces final surplus recalculation | Parts 3 and 4 | Cross-event timing test | Specified | Pending implementation |
| I01 | Mustering Out provides a useful response window | Part 3 | Mission timing test | Specified | Pending implementation |
| I02 | Unsafe, combat, foreign, transported, and special units are excluded | Part 3 | Mixed-army test | Specified | Pending implementation |
| I03 | Candidate score favors rear, weak, and low-experience units | Part 3 | Selection trace | Specified | Pending implementation |
| I04 | Veterans, fronts, borders, ports, and critical units receive retention priority | Part 3 | Selection trace | Specified | Pending implementation |
| I05 | Secure low-Readiness base share reaches at most 25 percent | Part 3 | Controlled army test | Specified | Pending implementation |
| I06 | Readiness 80 can reduce normal share to zero | Part 3 | Threshold test | Specified | Pending implementation |
| I07 | Defensive war normally reduces involuntary share to zero | Part 3 | Defensive-war test | Specified | Pending implementation |
| I08 | Tiny-army absolute caps apply | Parts 3 and 5 | Army sizes 0 through 7 | Specified | Pending implementation |
| I09 | Cadre decision reduces target and protects quality units | Part 3 | Decision result test | Specified | Pending implementation |
| I10 | Border decision requires a real named threat | Part 3 | Safe-border invalidation test | Specified | Pending implementation |
| I11 | Accelerated demobilization is voluntary and visible | Part 3 | Confirmation test | Specified | Pending implementation |
| I12 | Safe disband returns manpower and equipment | Parts 3 and 7 | Local engine proof and gameplay test | Specified | Pending implementation |
| I13 | Destructive unit deletion is never used | Parts 3 and 7 | Source audit | Specified | Pending implementation |
| I14 | Veteran Reintegration uses actual returned scale | Part 3 | Benefit trace | Specified | Pending implementation |
| I15 | One-battalion template farming is blocked | Parts 3 and 5 | Template spam test | Specified | Pending implementation |
| J01 | Peacetime Economy is below Civilian Economy | Parts 3 and 7 | Law database inspection | Specified | Pending implementation |
| J02 | No Army is below Disarmed Nation | Parts 3 and 7 | Law database inspection | Specified | Pending implementation |
| J03 | Immediate exemption checks 50 Readiness and proof | Part 3 | Prepared-country test | Specified | Pending implementation |
| J04 | Last chance checks 60 Readiness and two action families | Part 3 | Settlement test | Specified | Pending implementation |
| J05 | At least one last-chance action is factory or law based | Part 3 | Action mask test | Specified | Pending implementation |
| J06 | Direct war danger grants bounded deferral | Part 3 | Defensive-war settlement test | Specified | Pending implementation |
| J07 | Postwar review starts after valid deferral | Part 3 | War-end test | Specified | Pending implementation |
| J08 | Irrelevant war cannot defer forever | Parts 3 and 5 | Distant-war exploit test | Specified | Pending implementation |
| J09 | Non-exempt country enters Peacetime Economy | Part 3 | Forced settlement test | Specified | Pending implementation |
| J10 | First economy transition converts one third of remaining eligible factories | Part 3 | Factory count tests | Specified | Pending implementation |
| J11 | First economy transition uses the same state ledger | Part 3 | Ledger trace | Specified | Pending implementation |
| J12 | Non-exempt country enters No Army | Part 3 | Forced settlement test | Specified | Pending implementation |
| J13 | First No Army transition safely demobilizes eligible conventional units | Part 3 | Safe disband test | Specified | Pending implementation |
| J14 | First-entry effects are guarded per cycle | Parts 3 and 5 | Law toggle test | Specified | Pending implementation |
| J15 | Voluntary Permanent Peace has a full confirmation | Part 3 | Player decision test | Specified | Pending implementation |
| J16 | Peace Dividend is bounded and law-linked | Part 3 | Idea lifecycle test | Specified | Pending implementation |
| J17 | Emergency National Defence is threat-gated and costly | Parts 2 and 3 | Extreme-law emergency test | Specified | Pending implementation |
| J18 | Extreme-law exit remains possible without military resources | Parts 2 and 3 | Soft-lock test | Specified | Pending implementation |
| K01 | AI selects Reconstruction Pacifist, Cautious Hedge, or Wartime Rearmament | Part 4 | AI stance trace | Specified | Pending implementation |
| K02 | Direct danger overrides pacifist preference | Part 4 | AI61_PACIFIST_THREAT_OVERRIDE | Specified | Pending implementation |
| K03 | Defensive war rearmament reaches target band | Part 4 | AI61_DEFENSIVE_WAR evidence | Specified | Pending implementation |
| K04 | Secure isolated minor reconstruction reaches target band | Part 4 | AI61_PEACE_ISOLATED evidence | Specified | Pending implementation |
| K05 | Majors and faction leaders preserve a mobilisation skeleton | Part 4 | AI61_INDUSTRIAL_MAJOR evidence | Specified | Pending implementation |
| K06 | Voluntary Permanent Peace is hard-blocked by danger | Part 4 | AI61_PERMANENT_PEACE_RISK evidence | Specified | Pending implementation |
| K07 | Shortage family dominates stockpile protection | Part 4 | AI61_EQUIPMENT_POOR evidence | Specified | Pending implementation |
| K08 | Low-autonomy subject follows overlord unless locally threatened | Part 4 | AI61_SUBJECT_FOLLOWS_OVERLORD evidence | Specified | Pending implementation |
| K09 | AI respects project capacity and affordability | Part 4 | Low-capacity tests | Specified | Pending implementation |
| K10 | All complex weights have probability-tool evidence | Part 4 | Saved probability audit | Specified | Pending implementation |
| K11 | White Peace resolves before Return to Peacetime in cluster | Parts 1 and 4 | Cluster execution test | Specified | Pending implementation |
| K12 | Event 9 skip does not block Event 61 | Parts 1 and 4 | No-war cluster test | Specified | Pending implementation |
| K13 | Peace cluster members are corrected to 9 and 61 | Parts 1 and 4 | Workbook and registry diff | Specified | Pending implementation |
| K14 | Event 59 increases rearmament preference | Part 4 | AI comparison test | Specified | Pending implementation |
| K15 | Event 82 updates Readiness and blocks duplicate law step | Part 4 | Cross-event test | Specified | Pending implementation |
| K16 | Event 94 stockpile timing is safe | Part 4 | Cross-event test | Specified | Pending implementation |
| K17 | Event 131 owner units are excluded | Part 4 | Special unit test | Specified | Pending implementation |
| K18 | Navy is not dismantled | Parts 3 and 4 | Fleet integrity test | Specified | Pending implementation |
| K19 | Aircraft stockpile and air wings follow separate rules | Part 4 | Air handling test | Specified | Pending implementation |
| K20 | Unknown special owners fail closed | Part 4 | Owner contract audit | Specified | Pending implementation |
| L01 | Baseline and evolution text uses final in-world wording | Part 6 | Localisation audit | Specified | Pending implementation |
| L02 | Dynamic country results match actual effects | Part 6 | Value and localisation test | Specified | Pending implementation |
| L03 | At-war, major, minor, and zero-result variants read correctly | Part 6 | Variant screenshots | Specified | Pending implementation |
| L04 | Four distinct report images exist | Part 6 | Asset manifest and in-game review | Specified | Pending implementation |
| L05 | One static category picture exists without fake controls | Part 6 | Asset and UI review | Specified | Pending implementation |
| L06 | Category and decision icons are distinct and wired | Part 6 | Asset manifest and sprite audit | Specified | Pending implementation |
| L07 | Five idea icons are final and wired | Part 6 | Idea sprite audit | Specified | Pending implementation |
| L08 | Two law icons share a coherent family and remain distinct | Part 6 | Law sprite audit | Specified | Pending implementation |
| L09 | Three achievement icons are final and readable | Part 6 | Achievement UI review | Specified | Pending implementation |
| L10 | Every asset uses exact local consumer dimensions | Part 6 | Reference and processing evidence | Specified | Pending implementation |
| L11 | Every asset has source, preview, DDS, path, and sprite handoff | Part 6 | Asset manifest | Specified | Pending implementation |
| L12 | No placeholder, halo, bad crop, raw key, or broken path remains | Part 6 | In-game visual audit | Specified | Pending implementation |
| M01 | The Arsenal Returns has persistent cycle and deadline tracking | Part 6 | Achievement state test | Specified | Pending implementation |
| M02 | The Arsenal Returns blocks external shortcuts | Part 6 | Disqualifier tests | Specified | Pending implementation |
| M03 | Swords Ploughshares Swords uses actual liquidation and recovery | Part 6 | Achievement trace | Specified | Pending implementation |
| M04 | Defensive victory against a major is robustly proven | Part 6 | War-result tests | Specified | Pending implementation |
| M05 | The Arsenal Sleeps uses a continuous five-year timer | Part 6 | Timer save and reload test | Specified | Pending implementation |
| M06 | Chaos below 800 resets sustained progress | Part 6 | Threshold test | Specified | Pending implementation |
| M07 | Faction, subject, emergency, and puppet-shield exploits are blocked | Part 6 | Disqualifier matrix | Specified | Pending implementation |
| M08 | Special-unit classification is explicit | Part 6 | Unit eligibility test | Specified | Pending implementation |
| M09 | All achievements use the single registry | Parts 6 and 7 | Database inspection | Specified | Pending implementation |
| M10 | All achievements have final icons, text, docs, and tests | Part 6 | Completion report | Specified | Pending implementation |
| N01 | Save and reload repeats no baseline transaction | Part 5 | Save test | Specified | Pending implementation |
| N02 | Save and reload repeats no decision completion | Part 5 | Project completion save test | Specified | Pending implementation |
| N03 | Save and reload repeats no evolution resolution | Part 5 | Mission deadline save test | Specified | Pending implementation |
| N04 | Annexation cleans country projects and preserves state ledger | Part 5 | Annexation test | Specified | Pending implementation |
| N05 | Released countries receive state ledger without foreign Readiness | Part 5 | Release test | Specified | Pending implementation |
| N06 | Civil war does not run unsafe generic disband | Part 5 | Civil-war test | Specified | Pending implementation |
| N07 | Performance uses bounded event-time passes | Part 5 | Profiler and source audit | Specified | Pending implementation |
| N08 | Active-country pulse stops after cleanup | Parts 5 and 7 | Cleanup timing test | Specified | Pending implementation |
| N09 | All balance numbers are centralized | Parts 4 and 7 | Constant audit | Specified | Pending implementation |
| N10 | Event docs describe verified behavior | Part 7 | Documentation curator handoff | Specified | Pending implementation |
| N11 | Law docs cover both new laws and exit | Part 7 | Documentation diff | Specified | Pending implementation |
| N12 | Event Logs and Event Details are complete | Parts 6 and 7 | UI and log validation | Specified | Pending implementation |
| N13 | Authoritative workbook is updated | Catalog handoff | Workbook diff | Specified | Pending implementation |
| N14 | CSV exports are regenerated, not hand-edited | Catalog handoff | Exporter output | Specified | Pending implementation |
| N15 | Improvement-loop review is run once near completion | Part 7 | Subagent handoff | Specified | Pending implementation |
| N16 | Decision, localisation, docs, spreadsheet, probability, and completion audits are resolved | Part 7 | Subagent handoff set | Specified | Pending implementation |
| N17 | Completion report lists every simplification, fallback, and blocker | Coding prompt | Final report | Specified | Pending implementation |
| N18 | No completion claim is made with an unverified hard gate | All parts | Completion auditor result | Specified | Pending implementation |

## Requirement count

Total acceptance rows: 195

## Completion rule

Event 61 cannot be called complete while any required row is Failed, Blocked, or unsupported by evidence. A deliberate design change must update the source specification, implementation, documentation, workbook, and this matrix together.
