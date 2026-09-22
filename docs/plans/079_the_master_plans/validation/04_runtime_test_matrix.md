# Event 79 runtime acceptance matrix

All tests in this file are required or proposed runtime evidence. They have not been run in HOI4 in this session. The separate Python reference model tests only selected authored arithmetic and state invariants.

## Core and participant cases

| Test | Setup | Required result |
| --- | --- | --- |
| T01 | Independent AI minor, two majors, one player minor | One target and separate scores for all three sponsors |
| T02 | Target has industry larger than the initiating player | Target remains eligible |
| T03 | Target already a subject | It cannot be selected |
| T04 | Target already has an active race | A second root cannot duplicate that target |
| T05 | Player minor changes controller and returns | Same participant entry, no second seed |
| T06 | New major appears during an active contest | Registers once with a current snapshot |
| T07 | Registered major loses major status | Existing participant remains |
| T08 | Target joins or already belongs to a faction | Race remains valid, legal takeover is proved |
| T09 | Target leads a minor faction | Legal takeover does not delete or accidentally dissolve unrelated members |
| T10 | Target fights a third party | Valid aid and takeover preserve unrelated war state |
| T11 | Sponsor directly wars with target | Political takeover action is suspended, not secretly successful |
| T12 | Sponsor is a player-controlled subject | Required direct puppet result is proved or explicitly blocked |
| T13 | Target is the sponsor's existing overlord or ancestor | Hierarchy-cycle limitation is detected before an invalid victory |

## Arithmetic and political cases

| Test | Setup | Required result |
| --- | --- | --- |
| T14 | All positive seed evidence qualifies | Family caps apply, total no greater than 45 |
| T15 | Strong hostility and no positive evidence | Score never below zero |
| T16 | Two sponsors share an ideology | Popularity can benefit both, Influence remains separate |
| T17 | Popularity crosses 25 or 50 during a completion | Documented before-gain ordering applies |
| T18 | Same family completed repeatedly within 60 days | 100%, 75%, then 50% saturation |
| T19 | Upgrade subtype or rejoin after withdrawal | Family saturation is not reset |
| T20 | Start before regime change, finish after | Saved pledge and valid current recipient are respected |
| T21 | Protected national leadership owner rejects direct writes | Ordinary routes stay available, unsupported leadership action is blocked |
| T22 | Target's politics are overwritten by native puppeting | Intended current political state is restored without undoing legitimate transitions |
| T23 | Sponsor score reaches exactly 100 | Immediate real puppet, no extra button |
| T24 | Sponsor score remains 99.75 | No premature takeover |

## Rivalry, payment, and material cases

| Test | Setup | Required result |
| --- | --- | --- |
| T25 | Interfere against zero Influence | No paid operation and no attacker reward |
| T26 | Several sponsors attack the same victim | Shared rolling loss budget caps actual total loss |
| T27 | Another operation consumes the budget before completion | Actual remaining loss and proportional political refund agree |
| T28 | Coalition initiator disappears | Oldest still-valid funded member can finish one operation, not duplicate it |
| T29 | Discount starts or ends between preview and payment | Requoted display and actual debit agree |
| T30 | Direct equipment donation during a sale | Recipient receives exactly conserved material, no discounted creation |
| T31 | Mixed concrete equipment variants | Affordability, debit, escrow, delivery, and refund conserve each supported type |
| T32 | Invoke refund twice | Second call is a no-op |
| T33 | Donor loses usable factories mid-project | Work pauses and future work does not accrue free |
| T34 | Target state fills its last slot | No over-cap building, explicit relocation or pause |
| T35 | Another sponsor wins during an investment | Future donor capacity released, funded credit preserved, no free output |
| T36 | New overlord funds the remainder | Exactly one contracted output, no post-race Influence |
| T37 | Donor loses race after a shipment arrives | Delivered weapons remain with target |
| T38 | Project pauses for 30 days | Renegotiation or closure becomes available, no indefinite hidden reservation |

## Evolution, concurrency, and persistence

| Test | Setup | Required result |
| --- | --- | --- |
| T39 | Chaos crosses 200 in an active baseline contest | Eligibility begins without instant automatic stage activation |
| T40 | First eligible opening at Chaos 400 | One target at permitted evolved stage, capacity five |
| T41 | First evolution disabled, second enabled | Dependency is respected and shown |
| T42 | Evolution while a campaign is paid and running | Existing quote, duration, target, and output are unchanged |
| T43 | Two multiplayer schedulers fire together at baseline | At most one target reservation succeeds |
| T44 | Five active Great Game targets, sixth firing | No sixth target or false repeat consumption |
| T45 | Same sponsor acts in two targets while selected view changes | Each completion affects its saved target only |
| T46 | Two rivals reach threshold in one simulation tick | First authoritative valid commit wins once |
| T47 | Race A closes while Race B has investments and shipments | B remains unchanged |
| T48 | Reuse target slot after closure | Old-generation callbacks cannot mutate the new race |
| T49 | Save before payment, after payment, after delivery, and after victory | No duplicated debit, delivery, refund, winner, or log |
| T50 | Target becomes human, annexed, or externally puppeted | Correct invalidation, no fake winner, reconciled commitments |

## Interface, integration, and campaign tests

| Test | Setup | Required result |
| --- | --- | --- |
| T51 | Baseline and Great Game at four specified resolutions | No clipping, overlap, inaccessible actions, or misleading bar text |
| T52 | Long country names and no rival | Correct wrapping/tooltip and empty-rival state |
| T53 | Two human clients select different targets | UI selection remains isolated, authoritative data consistent |
| T54 | Normal takeover with shared Chaos logging | One world-change award, no Event 79 duplicate |
| T55 | Cluster export and runtime registry | Diplomacy membership and Medium severity align, no direct CSV edit |
| T56 | Achievement with inactive majors in roster | No false meaningful-competition qualification |
| T57 | CXT forced race | Runtime behavior can be tested, achievements remain ineligible |
| T58 | Supported no-DLC configuration | Full playable baseline and actual puppet ending |
| T59 | Normal AI campaign across multiple random targets | Report duration, spending, winners, invalidations, and unfinished races, not only successful examples |
| T60 | Baseline race with maximum legal sustained rivalry | It can finish through funded positive play without hidden AI mercy |
| T61 | Legacy save with global target and no receipts | Explicit migration disposition, no invented refunds or deleted real guarantees |
| T62 | Unexpected puppet postcondition failure | Commit failure is visible in diagnostics, no awards, no repeated delivered action |

## Evidence receipt

For every executed runtime test, record game version, DLC configuration, mod revision, setup method, country identities, initial values, commands or actions, relevant logs, expected result, actual result, and pass/fail/blocked state. A screenshot proves its visible frame only. A code inspection does not prove the game executed it.

Normal campaign tests should include an unassisted player-sized minor and at least two active major rivals. Report the complete sample, including stalled and invalidated races. Do not claim a percentage from a handpicked successful run.
