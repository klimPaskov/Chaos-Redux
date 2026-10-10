# 13. Validation and acceptance matrix

The cases below are future implementation acceptance. No HOI4 engine, MCP renderer, probability service or live campaign was run for this planning package. The local package checks and actual specialist design review are recorded separately in Part 15.

## Arrival and selection

| ID | Setup | Required result |
| --- | --- | --- |
| A01 | Chaos 999, 1000 and a supported value strictly greater than 1000 | Only the last can start grace |
| A02 | One-year anniversary minus one hour, exact anniversary and plus one hour | No early eligibility and no immediate forced arrival at eligibility |
| A03 | Chaos falls to 1000 then rises within one ordinary recovery interval | Shared mutation hooks reset the uninterrupted year |
| A04 | Save and reload during grace and after eligibility | Dates and excess age persist exactly |
| A05 | Another major fires after the grace | The Directorate's age priority is not reset |
| A06 | Event disabled, then enabled after a long qualifying period | Selection is blocked while disabled, environmental age remains truthful |
| A07 | Another world end commits during grace, during preflight or just before arrival commit | No Directorate arrival succeeds afterwards |
| A08 | No valid mainland state, state candidate changes, or CXT is occupied | No partial country, success history, resource change, Chaos gain or consumed major |
| A09 | Uniform-state selector across unequal country sizes | Every valid state has equal draw weight |
| A10 | Island with multiple states, strait, Australia, mainland exclave and mixed archipelago state | Verified mainland classification follows Part 02 without a topology shortcut |
| A11 | Occupied capital, one-state previous holder and different owner/controller | Exactly one state transfers, all required enemies are valid, native capital and country settlement remain legal |
| A12 | Natural draw and two manual confirmations overlap | Exactly one episode commits. Rejections do not mutate or refill |
| A13 | Large age and weight, zero or one competitor, changing settings | No overflow or private forced deadline. Standard pool semantics remain intact |

## Carrier and opening power

| ID | Setup | Required result |
| --- | --- | --- |
| C01 | Fresh dormant CXT | No player switch, former-country annex, occupation fixture or foreign campus acquisition |
| C02 | Dormant history already contains project or test receipts in an old save | Only proved test state is migrated, genuine history preserved, unresolved contamination blocks release |
| C03 | All active country and ideology lookup contexts | Chaos Directorate identity everywhere, no test text or debug controls |
| C04 | Sparse inland state with a very large opening army | Army has real equipment, manpower or manufactured bodies, organization and usable supply at public arrival |
| C05 | Developed world, devastated world and disproportionately strong neighbor | Correct scaling term and floors, no dormant-CXT or own-army double counting |
| C06 | Naval facility and fleet requested from inland origin | No illegal placement or extra state, a real path to coast and delivery remains available |
| C07 | Early and late campaign, each intensity | Full arsenal entitlement throughout, quantities and depth scale as specified |
| C08 | Engine entity pressure with very large forces | Any formation compression preserves family coverage and accounted fighting power and is explicitly reported |
| C09 | Capital lost with surviving land | Legal fallback capital, continued war and no repeated opening grant |
| C10 | Human obtains supported control after arrival | Same paid country mechanics, no harness benefits, correct achievement enrollment boundary |
| C11 | Demand exceeds the 90-percent concession, delivered throughput is zero, or the native maximum is insufficient | Part 03's measured demand and throughput preflight controls admission. Legal support may exceed the first tuning band. No army reduction, extra state, unusable hidden reserve or half-functional public arrival |
| C12 | Native industry grows, is bombed to zero, returns, and changes under focus and terminal stages | Frozen absolute allowance is never recalculated from the world. Every real usable factory adds output. One capacity target applies, zero native capacity creates no stockpile or division-by-zero artifact |

## Dynamic arsenal

| ID | Setup | Required result |
| --- | --- | --- |
| U01 | Complete active definition inventory | Every unit, equipment, technology, project, facility, doctrine and relevant system has a disposition and live consumer |
| U02 | New unit family added without any Event 103 edit | Owner registration makes it available, produces valid templates and enters service review |
| U03 | New support, concrete equipment, project, facility or air/naval family | Same generic discovery and explicit operational proof, no guessed global array |
| U04 | Technology database default entry and more than 1000 real entries | Default skipped and the full real suffix processed without truncation |
| U05 | Identity-gated provider such as refined clone forces | Neutral boss authorization preserves exact content without setting original-country provenance |
| U06 | Mutually exclusive industry, doctrine or support definitions | Truthful compatible modes or equivalent owner adaptation, no lost capability or invalid stacked formation |
| U07 | CBRN readiness and legal target with payloads | Actual native or owner operation runs. No fake attack flag and no double payment |
| U08 | Project completion normally produces news, character, achievement or world-end effects | Only authorized gameplay capability outputs enter the boss, with no source-event impersonation |
| U09 | Future package joins an existing boss | Versioned additions arrive once, no baseline army or stockpile refill |
| U10 | Duplicate registration, conflict, missing adapter and removal on a save | Exact conflict or migration result, no silent skip under a universal claim |
| U11 | Existing family models and counters under CXT | Correct actual visuals and equipment consumers. Selection audio limitations remain truthful |
| U12 | No DLC, relevant individual DLC, supported full set | All required conceptual capabilities retain real supported gameplay or remain an explicit release blocker |

## Conquest and accounting

| ID | Setup | Required result |
| --- | --- | --- |
| W01 | New land neighbor, subject, released country and already-hostile country | Correct sovereign war once, no stale or duplicate target |
| W02 | Shared white-peace event targets a Directorate war | Conquest hostility is preserved without disabling unrelated peace |
| W03 | First capture, loss and recapture of a state | Live capacity changes correctly. Permanent reserves and premiums do not repeat |
| W04 | Native annexation and scripted stockpile transfer overlap | Actual concrete equipment credited exactly once and source debited exactly once |
| W05 | Evacuation, interception, partial arrival and lost destination | Population and equipment conservation, real deaths once, only actual delivery credited |
| W06 | Industrial relocation or demolition interrupted halfway | No duplicated factories, free destination capacity or invisible full refund |
| W07 | Controller changes around a review date | State-owned cadence survives, callback count cannot accelerate growth |
| W08 | Every mainland state held but one remote origin island remains | Continental completion stays false and a pre-terminal delivery campaign begins |
| W09 | Ownable impassable administrative state remains | It stays in the denominator. Actual wartime owner defeat, continent control and exact eligible state are verified before supported ownership and control settlement. A separate resisting controller blocks transfer and queue acceptance alone grants no credit |
| W10 | Exactly complete origin continent then one state lost | Live UI and terminal predicate both become incomplete immediately |
| W11 | Queue exceeds a native loop limit | Unvisited records and unresolved receipts survive without duplicated work |

## Endings and manual launch

| ID | Setup | Required result |
| --- | --- | --- |
| E01 | Full continent, Chaos exactly 1000 | No ending |
| E02 | Full continent, above 1000, branch disabled or global ends disabled | No ending, active conquest continues |
| E03 | All gates true | One shared terminal commit, one branch record and one presentation |
| E04 | Territory lost, Chaos falls or another ending wins just before commit | No stale Event 103 terminal latch |
| E05 | Global random scheduler stops | Boss war, production priorities, operations, absorption and cleanup continue |
| E06 | A sovereign is created after terminal | It joins the valid target lifecycle without a daily world scan |
| E07 | Pre-terminal or post-terminal country destruction | Correct distinct outcome. No resurrection and no historical ending reset |
| E08 | Last sovereign capitulates but land remains outside direct control | No false world-conquest claim |
| S01 | The Final Boss at low Chaos and every intensity | One state, one country, no player switch, immediate functional force |
| S02 | Scenario succeeds at low Chaos | Bounded initial Chaos gain, no forced 1001 meter or terminal flag |
| S03 | Scenario after confirmed destruction and complete cleanup, during residual cleanup, while active or committing, and during an incompatible ending | A clean available carrier permits a fresh immutable manual episode after confirmed defeat. All active/provisional collisions, incomplete cleanup and incompatible terminal states reject consistently. Automatic grace and fire-once history remain unchanged |
| S04 | Selector changes, Cancel timeout, stale request or double click | The accepted frozen request alone may commit, Cancel has no consequence |
| S05 | Old callback, shipment, report, refund, grant or outcome arrives after a new manual episode commits | Old episode/generation authority fails against the replacement actor. It cannot mutate or pay the new CXT, replay its opening or alter the new request |
| S06 | R2 or R5 old post-defeat check remains pending during a fresh manual attempt | The frozen old actor, episode, destruction receipt and due date remain distinct. No replacement CXT, new capture, new defeat or new terminal receipt satisfies old proof. Completed achievements and prior finalized provenance survive |
| S07 | Two partial attempts together satisfy a state, operation, family or hold requirement | No achievement unlock from cross-attempt aggregation. Each new valid attempt has fresh enrollment and its own qualifying intensity and snapshots |

## Actions, focus, AI and presentation

| ID | Setup | Required result |
| --- | --- | --- |
| P01 | Each action below, exactly at and above its quoted cost | One inclusive gate, correct texticons, at most four spendable types, no double debit |
| P02 | Partial payment, target loss, timeout and exceptional cancellation | Native timer and stored deadline agree, only supported unused amounts refund |
| P03 | All eight focus families and their anchor groups | Every promised route, action and meaningful payoff implemented, no capability or essential transport lock |
| P04 | Starting, mature, damaged and terminal institutions | At most three simultaneous tree-owned spirits with correct replacement and cleanup |
| P05 | All AI scenarios in Part 08 | Correct ordering, operational use and bounded family service, with evidence class stated |
| P06 | Human boss, bordering defender, distant observer and hotjoin | Correct actor scope, intelligence precision and player-owned selections |
| P07 | Last origin state, complete geography with ending blocked, terminal, later recapture and defeat | Same truthful objective set and phase-aware public text |
| P08 | 1920x1080 at UI scale 1 and all other supported UI configurations | Native controls readable, no overlap, clipping, raw keys or wrong-context information |
| P09 | Every final asset, flag suffix, achievement state and super-event consumer | Actual source, file, registration, live use and visibility coverage, not just a file count |
| P10 | Super-event sound disabled, lowered volume and normal playback | Correct shared playback behavior without changing the terminal result |
| P11 | Repeated spirit refresh, recapture, surge allocation, servicing and terminal amplification affect the same production dimension | Part 03's additive approved improvements and single phase factor reach one target. No duplicated opening allowance, compounding old spirit stages or free future equipment shipment |
| P12 | Campaign or counterattack capture, loss during the 30-day hold, empty formation, changed priority and already-controlled target | Frozen force and supply work is required. Hold reset cannot move the original 120-day deadline, and payment or existing control grants no success |
| P13 | Defense objective in standard and emergency form | Full disclosed 90-day or 30-day work is required with real threat, force and supply coverage. Acceptance starts work, not success, and a broken interval cannot be relabeled complete |

## Achievement proof

Test every Part 11 concept with a qualifying case and a near miss. Required boundaries include personal versus allied capture, natural versus scenario provenance, resistance High/Maximum qualification, boss-player any-intensity qualification, late enrollment, unavailable ordinary country selection, real family use, three distinct operation owners, required biological operation, updated registry sets and debug contamination.

For B1, verify the 150-day and 300-day bounds, upward rounding to five days, disconnected landmasses excluding the mainland, frozen arrival geography and the exact due date. For B3, retain the pre-victory force requirement and 75 percent serviceable force and sustainment checks after the last enemy disappears. Army disbanding cannot reduce its denominator to zero.

For R2 and R5, delayed proof must survive boss cleanup and save/load. For R3, test the first actor-specific qualification, arrival-capital preference, smallest-native-ID fallback, frozen anchor and due date, delayed UI opening and no later reselection. Chaos and ending-setting continuity matter throughout the hold, but a successful reduction in boss territorial share does not invalidate the historical 90-percent crisis entry. Recapture cannot count the same state twice in R4 or any other unique-state target.

## Evidence standard and stop condition

Separate source coverage, parser validity, arithmetic reasoning, reference evidence, inspected graph, rendered layout, probability classification, save observation and live-game observation. Record exact source revision, scenario and limitations for each meaningful result. Resolve a concrete risk before broadening tests.

The code goal is complete only when every accepted required design row has a current implemented consumer, every accepted review finding has a disposition, all output files and identifiers agree, and no missing capability is disguised as a balance decision. Apply the current AGENTS.md completion rules to the evidence matrix. Use the meaningful available checks and relevant local reference/source alternatives after the bounded retry limit, and distinguish unverified engine behavior from missing implementation or a missing specifically requested measurement. Unavailable optional verification alone does not keep otherwise finished work open. User-owned game testing is neither requested nor awaited, and static review is not reported as observed game behavior.
