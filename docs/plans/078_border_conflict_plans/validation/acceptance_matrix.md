# Acceptance matrix

## Evidence standard

All runtime cases below are pending.
No row represents a passed native test in this planning session.
Record the installed game version, DLC setup, fixture save, exact endpoints, expected result, actual result, and supporting trace or screenshot when executing a case.
Distinguish source checks from live behavior.
An acceptance case passes only when its asserted behavior was actually observed or otherwise established by the appropriate tool.

## Allocation and native compatibility

| Case | Fixture | Required result |
| --- | --- | --- |
| A01 | Two ordinary eligible land neighbors | One baseline battle with one declared stake |
| A02 | A–B is already a normal war | No A–B Event 078 start |
| A03 | A is at war with X and is at peace with neighboring B | A–B remains eligible and can fight |
| A04 | One country with three disjoint neighboring fronts | Genuine simultaneous native battles, no country-level serialization |
| A05 | One pair with several disjoint fronts and evolution I applied | The computed additional roots run simultaneously |
| A06 | Both loop directions enumerate the same pair | One canonical relationship and no duplicate baseline dispute |
| A07 | One target state has several possible staging states | One target ticket, then staging selection |
| A08 | Two pairs compete for an incompatible endpoint | One reservation owner, alternate legal candidate or documented omission |
| A09 | A pair has no valid state despite country adjacency | No false start or illegal inland target |
| A10 | Long front and short front compete | Baseline opportunity precedes the long front's extra roots |
| A11 | F equals 0, 1, 4, 5, 9, 10, or 15 | Allowance follows the documented formula and available capacity |
| A12 | Owner differs from controller | Affected endpoint excluded unless an evidenced native-supported arrangement exists |
| A13 | Same faction, overlord, common overlord, or non-aggression pact | Native compatibility established without invented immunity or forced diplomacy change |
| A14 | Capital and final owned state | Correctly supported settlement and cleanup, or documented native exclusion |
| A15 | Strait, impassable border, demilitarized area, unusual adjacency | Only the proved legal native land connection is admitted |
| A16 | No usable world pair | No native start, outbreak Chaos, false news, or empty live wave |

## Results, chains, and settings

| Case | Fixture | Required result |
| --- | --- | --- |
| R01 | Attacker wins | Only the declared target transfers once |
| R02 | Defender wins | Target retained, staging state not awarded |
| R03 | Native draw or cancellation | No Event 078 territorial award |
| R04 | Both side callbacks arrive | One result, one receipt, one set of consequences |
| R05 | Duplicate and reversed callback order | Same final state without repeated seed or reward |
| R06 | Two simultaneous battles end on the same tick | Each callback resolves its own endpoints and participants |
| R07 | Another event changes target ownership first | No stolen third-party state or false Event 078 capture credit |
| R08 | Direct normal war starts during border battle | Only affected border dispute cancels, normal war remains untouched |
| R09 | Unrelated normal war starts during border battle | Valid dispute continues |
| R10 | Country annexed and tag later reused | Old result has no authority over recreated country |
| R11 | Capture opens a genuinely new neighbor state | Valid seed opportunity and immediate safe native continuation |
| R12 | Candidate already bordered attacker before latest capture | Candidate rejected for momentum |
| R13 | Newly opened candidate belongs to a third country | No change of chain opponent |
| R14 | Seeded chain wins again | No extra random stop roll, next valid target or justified conclusion |
| R15 | Chain loses or draws | Chain ends without reversal or replacement reward |
| R16 | Target already spent in the same wave | No repeat target or territorial ping-pong |
| R17 | Several chains seek one newly opened state | Single reservation owner, no duplicate battle |
| R18 | Next endpoint busy at resolution | No persistent retry queue or invented substitute |
| R19 | Root completes before new active evolution | Completed opportunity does not refill the root budget |
| R20 | Multiple evolution thresholds qualify | Correct immediate opening or one paced active mutation at a time |
| R21 | Every combination of three evolution toggles | Exact behavior from the settings matrix |
| R22 | Chaos falls during an ongoing battle | No rollback of declared stake or prior valid mutation |
| R23 | Evolution or event disabled while active | Current valid result retained, prohibited new starts blocked |

## Repeat, shared systems, and objectives

| Case | Fixture | Required result |
| --- | --- | --- |
| S01 | New wave while same pair remains active | No baseline duplicate and no theft of the old wave's records |
| S02 | Evolved new wave with older active fronts | Occupancy respected without retroactive cancellation |
| S03 | Several local results within one wave | Main timer, repeat weight, and Wars cluster charged once |
| S04 | First confirmed native start | Outbreak grant at most once and only outside its rolling guard |
| S05 | Five pairs involving five countries active together | Broad spread qualifies once |
| S06 | Five pairs sequentially, or fewer than five countries | No false broad-spread grant |
| S07 | Fifth genuine capture in one chain | Sustained advance qualifies once, guards respected |
| S08 | Two waves qualify on the same tick | Shared rolling guards prevent duplicate source grants |
| S09 | Positive source condition met during closed rolling guard | No deferred payout when guard later expires |
| S10 | Qualifying chain stopped and target held 30 days | One budgeted containment reduction if all conditions still hold |
| S11 | Stop by cancellation, toggle, or normal war | No containment reduction |
| S12 | Generic casualty, occupation, or annexation adapter also fires | No double charge for the same represented source |
| S13 | Five-opponent achievement with mixed attack and defense | Correct distinct-opponent count, no-loss rule, closure, and 30-day hold |
| S14 | One chain with at least five captures | All chain gains held for 90 days after chain closure |
| S15 | Five historical lost states recovered in later waves | Exact-state and exact-opponent evidence, then 90-day hold |
| S16 | Debug or stale results attempt objective progress | No campaign achievement credit |
| S17 | Normal transfer recovers a required achievement state | No Event 078 recovery credit |
| S18 | Country or objective fails during hold | Attempt fails or closes according to its documented rule |

## Persistence, migration, scale, and presentation

| Case | Fixture | Required result |
| --- | --- | --- |
| P01 | Save/load during discovery or admitted battle state | No duplicate starts or lost ownership identity |
| P02 | Save/load between result, transfer, and continuation | One atomic logical result and safe recovery |
| P03 | Save/load during 30-day and 90-day holds | Same objective and remaining valid hold period |
| P04 | Multiplayer clients with the same seed and state | Same pair order, target choices, starts, and outcomes |
| P05 | Worldwide high-Chaos wave on a fragmented map | Functional scale without unannounced country caps or global daily rescans |
| P06 | Ordinary project or vanilla border war already active | No endpoint conflict, stolen callback, or foreign cleanup |
| P07 | Old Event 078 delayed event or battle in a migrated save | Explicit safe migration or truthful unsupported-save blocker |
| P08 | Player has many disputes and long country names | Every stake accessible in the native information surface |
| P09 | Multiple results on one game day | Readable grouped reporting without delayed mechanics |
| P10 | Shared log and Event Details | One firing record and narrative-only details with correct subjects |
| P11 | Report, news, category, and achievement assets | Correct native canvas, alpha, frame, identity, and consumer rendering |
| P12 | AI fights multiple borders and an unrelated normal war | Native troop behavior functions without free or teleported armies |
| P13 | Wave closes with holds pending | Wave stays closed for evolution, objective checks remain valid |
| P14 | All planned files and final catalog export | No stale one-neighbor description, normal-war option, or false completed status |

## Stop conditions

A failure of concurrent native support or exact result identity blocks production enablement.
A known case omitted because of missing tools remains pending.
A source-only approximation cannot close a live-engine case.
A narrower fallback requires a new explicit design decision and cannot be labelled the completed Event 078 specified here.
