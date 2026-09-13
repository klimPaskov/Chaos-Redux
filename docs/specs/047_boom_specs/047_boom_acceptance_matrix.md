# Event 47 BOOM acceptance matrix

| ID | Scenario | Setup | Required result | Failure evidence |
| --- | --- | --- | --- | --- |
| B-01 | Baseline peacetime strike | Eligible ordinary state in a country at peace | One epicenter, one first ring, camera to first state, exact population loss, building damage, local force disruption, reports | War gate, missing damage, or extra target bias |
| B-02 | Baseline wartime strike | Eligible state in an active war | Same target and damage rules as peace | War changes eligibility or protects the state |
| B-03 | Uniform ten-state pool | Ten eligible states across countries of different sizes | Equal first-target probability by state | Country-first or major-country weighting |
| B-04 | Invalid primary exclusions | Add unowned, low-population, unsafe, and actual nonhuman states | Invalid states receive zero primary probability | Any excluded state selected |
| B-05 | Human special country | Human special actor that uses normal civilian systems | State remains eligible | Blanket special-country exclusion |
| B-06 | Isolated island | Eligible state with no valid land neighbor | Full epicenter effect and no invented ring | Selector searches for substitute neighbor or fails |
| B-07 | Cross-border ring | Epicenter adjacent to several countries | Each valid neighbor receives one ring package | Ring limited to target owner |
| B-08 | Duplicate adjacency path | Same state reached through several adjacency paths | One ring entry and one transaction | Duplicate deaths or building damage |
| B-09 | Population conservation | Known pre-population and rolled request | Post-population equals pre-population minus applied amount, subject to floor | Requested value recorded instead of applied value |
| B-10 | Protected floor | Small eligible state near 1,000 population after prior damage | Applied loss stops at 1,000 remaining | Population crosses floor |
| B-11 | Deaths disabled display | Disable Deaths display under supported settings while population loss remains active | Real population still falls and no duplicate log appears | Blast becomes harmless or logs twice |
| B-12 | Building inventory | State contains every supported state building type | Every family is classified and correct levels are damaged | Unclassified family or levels below zero |
| B-13 | Rail and supply | State has rail and supply infrastructure | Accepted zone damage applies to both | Generic modifier used instead |
| B-14 | State-local divisions | Units inside and outside affected states | Only inside units lose strength and organization | Country-wide army damage |
| B-15 | Unit deduplication | Unit target reachable through overlap data | Unit processed once | Repeated strength loss |
| B-16 | Military casualty precision | Engine exposes exact personnel delta | Exact delta enters military Deaths once | Estimate or duplicate entry |
| B-17 | Military casualty unavailable | Engine cannot expose exact personnel delta | Force effect applies with no invented military deaths | Guessed casualty number |
| B-18 | Nuclear stockpile isolation | Record nuclear stockpiles before firing | Values unchanged | Any stockpile debit |
| B-19 | Nuclear history isolation | Record use and responsibility ledgers | No Event 47 entry | BOOM appears as nuclear use |
| B-20 | Fallout isolation | Observe target and global fallout values | No fallout created | Fallout intensity or duration changes |
| B-21 | Condemnation isolation | Observe public condemnation sources | No nuclear or Event 47 condemnation | Condemnation source added |
| B-22 | Air Cleanliness isolation | Observe value and source ledger | No BOOM source and no direct change | Atmospheric source added |
| B-23 | Nuclear achievement isolation | Prepare near-complete nuclear achievement | BOOM does not satisfy strike condition | Achievement progresses |
| B-24 | Soundwave presentation | Normal countries across world | One acknowledgment each and no universal modifier | Popup spam or gameplay penalty |
| E1-01 | Pre-fire Bigger BOOM | Event never fired, Chaos at least 400, evolution enabled | Evolution records before first incident and evolved profile applies | Baseline profile or duplicate evolution log |
| E1-02 | Active-history Bigger BOOM | Prior baseline firing, Chaos at least 400 | MTTH pacing occurs and later firing uses evolved profile after activation | Instant repeated activation or retroactive damage |
| E1-03 | Bigger BOOM disabled | Evolution recorded but currently disabled | Future firing uses baseline strength and no second ring | Disabled content still active |
| E1-04 | Second-ring construction | Branching adjacency graph | Unique second ring excludes epicenter and first ring | Duplicate or wrong-zone states |
| E2-01 | Pre-fire multi-strike | Event never fired, both stages eligible and enabled | First incident can resolve two or three epicenters | Forced baseline opening |
| E2-02 | Chaos 800 count | Complete target pool | 75% two and 25% three in probability evidence | Wrong distribution |
| E2-03 | Chaos 900 count | Complete target pool | 60% two and 40% three | Wrong distribution |
| E2-04 | Three-target shortage | Only two safe targets | Rolled three degrades to two and completes | Repeated target or failure loop |
| E2-05 | One-target shortage | Only one target | Incident resolves one blast with degraded record | Duplicate target or invalid commit |
| E2-06 | No-target rejection | No eligible state | No history, cap, fired count, pacing, death, or damage commit | Empty firing counted |
| E2-07 | Different-continent preference | Valid distant candidates exist | Later target comes from a different continent under tier one | Lower tier chosen while higher tier exists |
| E2-08 | Strategic-region fallback | No different-continent candidate | Different strategic region dominates | Same-region chosen too early |
| E2-09 | Nonadjacent fallback | No higher separation candidate | Unique nonadjacent state selected | Adjacent state chosen too early |
| E2-10 | Final unique fallback | Only close unique states remain | Unique states selected with bounded retries | Same state repeated or infinite retry |
| E2-11 | Third target comparison | Third candidate near first but far from second | Candidate must satisfy comparisons against both earlier states at chosen tier | Pairwise check omitted |
| E2-12 | Overlap strongest zone | Rings overlap several epicenters | One strongest final zone per state | Additive percentages or order dependence |
| E2-13 | Epicenter inside another ring | Primary state also lies in a ring | Epicenter intensity wins | Ring downgrades primary state |
| P-01 | Camera behavior | Three-blast human incident | One camera move to first epicenter | Camera moves for later blasts |
| P-02 | Multiplayer camera | Several human players | Each client receives bounded presentation | Cross-client repeated seizure |
| P-03 | Report cap | Country affected by several zones | One primary report plus bounded summaries | One popup per state or ring |
| P-04 | One history row | Three-blast incident | One Event History row with total count and totals | One row per blast |
| P-05 | One pacing transaction | Three-blast incident | Event system advances once | Timer advances per blast |
| P-06 | Actorless history | Direct victim and several other victims | No attacker or first-victim actor field | Misleading actor shown |
| R-01 | Repeat same state | Prior target restored above eligibility threshold | Later firing can select it again | Permanent immunity remains |
| R-02 | Save and reload evolution | Save after evolution activation | State persists and does not relog | Lost or duplicated evolution |
| R-03 | Save and reload delayed incident | Save during bounded secondary sequence when supported | Generation resumes once or fails closed without duplicate effects | Duplicate blast or stale target |
| R-04 | Cleanup | Complete and rejected incidents | Temporary targets, receipts, and generation data clear | Stale state affects later firing |
| C-01 | Standalone registration | Event enabled outside cluster | Normal Chaos level 1 selection works | Cluster dependency blocks event |
| C-02 | Cluster pending ID | Various Anomalies still lacks stable ID | No guessed cluster wiring | Invented or unstable ID |
| C-03 | Cluster member firing | Stable cluster added later | One member incident, one pacing transaction, ordinary Event 47 state updates | Member bypasses cap or double-paces |
| A-01 | Report image | Final asset wired | Correct period scene, no attacker clue, no modern object, no generated text | Placeholder, unrelated nuke art, or missing sprite |
| L-01 | Cause remains unresolved | Review all event and detail text | No confirmed explanation anywhere | Any text confirms cause or future reveal |
| L-02 | Catalog alignment | Compare workbook and in-game wording | State-based description, two evolutions, Severe role, correct type and level | Stale province wording or Low severity |
