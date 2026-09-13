# Event 53 Validation Scenarios

These scenarios are implementation acceptance tests. They do not replace the mandatory MCP event and probability passes.

## A. Parent firing and targeting

| ID | Setup | Action | Expected result |
| --- | --- | --- | --- |
| `MM-V-A01` | One valid player country | Allow or manually trigger Event 53 through normal rules | Country receives first appearance, Event 53 records one Fire-Once firing |
| `MM-V-A02` | Four valid player countries | Trigger Event 53 repeatedly from fresh identical checkpoints | Only one player receives each first appearance, target selection uses equal ballots |
| `MM-V-A03` | Human special Chaos actor and human ordinary country | Trigger Event 53 | Ordinary country is the only valid target |
| `MM-V-A04` | Human nonhuman country and human ordinary country | Trigger Event 53 | Nonhuman country is excluded |
| `MM-V-A05` | Human country owns no state | Inspect event availability | Event is unavailable when no other valid player exists |
| `MM-V-A06` | Event 53 already fired | Advance normal random-event system | Parent entry cannot fire again |
| `MM-V-A07` | Event 53 active | Inspect Event History after several visits | One Event 53 History row remains |

## B. Target persistence and control

| ID | Setup | Action | Expected result |
| --- | --- | --- | --- |
| `MM-V-B01` | Active target | Change ideology | Chain remains attached |
| `MM-V-B02` | Active target | Apply cosmetic tag | Chain remains attached |
| `MM-V-B03` | Active target | Move capital | Chain remains attached |
| `MM-V-B04` | Active target | Change subject or faction status | Chain remains attached |
| `MM-V-B05` | Active target | Human switches to another country | Visits pause on original country and do not retarget |
| `MM-V-B06` | Paused target | Human takes control of original country | One pending visit resumes, no backlog appears |
| `MM-V-B07` | Active target | Country is annexed | Chain ends and does not select another player |
| `MM-V-B08` | Active target | Proven legal-successor adapter runs | Full chain state moves atomically to successor |
| `MM-V-B09` | Active target | Unproven breakaway captures capital | Chain remains on original country or ends if original dies, no inferred transfer |
| `MM-V-B10` | Active target | Country becomes actual nonhuman actor | Chain closes through incompatible-target cleanup |
| `MM-V-B11` | Active ordinary target survives an unrelated terminal transition | Set `world_end` through its owning terminal system and advance to the next visit | Event 53 follow-up remains scheduled, incompatible packages are excluded, and one valid package can still resolve |

## C. Scheduling

| ID | Setup | Action | Expected result |
| --- | --- | --- | --- |
| `MM-V-C01` | Complete first payment | Inspect scheduled state | Exactly one future visit is pending |
| `MM-V-C02` | Complete first refusal | Inspect scheduled state after adapter receipt | Exactly one future visit is pending |
| `MM-V-C03` | Visit already present | Fire scheduler again through debug path | No second popup opens |
| `MM-V-C04` | Consequence resolving | Fire scheduler | Scheduler waits or performs one bounded retry without creating another visit |
| `MM-V-C05` | Several consecutive refusals | Compare intervals | Intervals shorten within constants and remain above 45 days |
| `MM-V-C06` | Several refusals then payment | Schedule next visit | Consecutive-refusal pressure clears |
| `MM-V-C07` | Target becomes AI before visit | Reach due date | Visit enters pause and does not resolve |
| `MM-V-C08` | Save with scheduled visit | Reload and advance | One visit fires at the preserved schedule |

## D. Demand selection and locking

| ID | Setup | Action | Expected result |
| --- | --- | --- | --- |
| `MM-V-D01` | Baseline behavior | Open visit | Political Power is demanded |
| `MM-V-D02` | Evolution I major with all systems | Open many test visits from clean checkpoints | Every valid type can be selected with equal ballot evidence |
| `MM-V-D03` | Evolution I landlocked minor | Open visit | Navy and convoy demands are excluded when invalid |
| `MM-V-D04` | Valid equipment system with empty stockpile | Select equipment demand | Demand remains valid, pay option is disabled |
| `MM-V-D05` | Visit popup open | Change stockpile or Political Power | Locked demand type and amount do not reroll |
| `MM-V-D06` | Several prior payments | Compare amount with first visit | Future amount is larger within cap |
| `MM-V-D07` | Command Power demand | Force maximum progression | Locked amount never exceeds 60 |
| `MM-V-D08` | Stability near protected floor | Lock Stability demand | Pay option disables when full payment would cross floor |
| `MM-V-D09` | Temporary industrial demand | Pay | Timed burden applies, factories are not permanently deleted |
| `MM-V-D10` | Industrial burden expires | Advance to end | Burden clears once |

## E. Payment transaction

| ID | Setup | Action | Expected result |
| --- | --- | --- | --- |
| `MM-V-E01` | Affordable locked demand | Pay | Exact displayed amount is removed once, no consequence rolls |
| `MM-V-E02` | Unaffordable locked demand | Inspect option | Payment is disabled with exact blocked reason |
| `MM-V-E03` | Affordable at popup, unaffordable before effect | Attempt pay | Engine-safe refresh or inability-to-pay refusal occurs, no partial debit |
| `MM-V-E04` | Save on payment popup | Pay, save, reload | Debit does not repeat |
| `MM-V-E05` | Payment completed | Inspect counters | Visits and payments increment, refusal streak clears |
| `MM-V-E06` | Payment completed | Inspect Chaos | Payment itself adds no Chaos |

## F. Refusal and equal selector

| ID | Setup | Action | Expected result |
| --- | --- | --- | --- |
| `MM-V-F01` | Several valid packages | Refuse | One package is selected and applied |
| `MM-V-F02` | Previous package remains valid | Refuse on next visit | Previous package can be selected again |
| `MM-V-F03` | Ten valid packages | Inspect normalized pool | Each package has one-tenth probability |
| `MM-V-F04` | Four valid packages | Inspect normalized pool | Each package has one-quarter probability |
| `MM-V-F05` | Package invalid | Build pool | Package is absent, remaining entries renormalize equally |
| `MM-V-F06` | Natural Disasters has many valid families | Build pool | Natural Disaster appears once |
| `MM-V-F07` | Independence Wave has many candidates | Build pool | Selected independence package appears once |
| `MM-V-F08` | Assassination has many candidates | Build pool | Assassination appears once |
| `MM-V-F09` | Compound package valid | Refuse and select it | Whole compound executes from one ballot |
| `MM-V-F10` | First selected adapter rejects before mutation | Resolve refusal | One uniform redraw occurs from fresh pool without rejected entry |
| `MM-V-F11` | Second selected adapter rejects | Resolve refusal | Government paralysis applies once and error receipt records |
| `MM-V-F12` | Save during resolving state | Reload | Selected package or completed receipt resumes without duplicate consequence |

## G. Source-event isolation

For every borrowed event adapter, run the same before-and-after ledger test.

| ID | Source | Expected untouched state |
| --- | --- | --- |
| `MM-V-G01` | Event 006 Independence Wave | Fired count, random weight, cluster pacing, ordinary History, evolutions, opening presentation, terminal routes |
| `MM-V-G02` | Event 013 Natural Disasters | Fired count, repeatable cap, random timer, cluster record, ordinary History, evolutions |
| `MM-V-G03` | Event 021 Random Civil War | Fired count, weight, ordinary History, evolutions and opening presentation |
| `MM-V-G04` | Event 050 Great Embargo | Fired count, weight, ordinary History, evolutions and opening presentation |
| `MM-V-G05` | Event 052 Intel Leaked | Fired count, weight, ordinary History, evolutions and opening presentation |
| `MM-V-G06` | Disease or plague source event | Event firing, special-country unlocks, evolution, super-event, and terminal route |
| `MM-V-G07` | Any disabled source event | Matching borrowed package is absent unless a separately named adapter toggle exists and is enabled |

Every owner operational ledger needed for real consequences may change with Event 53 origin recorded.

## H. Owner adapters

| ID | Adapter | Expected result |
| --- | --- | --- |
| `MM-V-H01` | Natural disaster | Owner resolves target, damage, deaths, aftermath, and cleanup |
| `MM-V-H02` | Independence Wave | Released country has viable territory, forces, equipment, manpower, leader, flag, focus content, claims, and conflict state |
| `MM-V-H03` | Famine | Real Food Security incident begins and owns mortality and relief |
| `MM-V-H04` | Migration | Real cohort transfer or trapped-population state occurs with exact population accounting |
| `MM-V-H05` | Disease | Real outbreak spreads and cleans up through disease owner |
| `MM-V-H06` | Intel Leaked | Foreign recipients gain correct exposure, source Event 52 remains unfired |
| `MM-V-H07` | Great Embargo | Valid coalition applies real pressure and cleans up, source Event 50 remains unfired |
| `MM-V-H08` | Civil war | Legal government proof returns and Event 53 marker remains unique |
| `MM-V-H09` | External war | Actors are reachable and conflict relations remain valid |
| `MM-V-H10` | Military fracture | Units, equipment, commands, and depots do not duplicate |
| `MM-V-H11` | Assassination | One safe eligible character is removed and protected roles remain valid |
| `MM-V-H12` | Occupation revolt | Valid occupied territory and local actor package are used |

## I. Evolutions

| ID | Setup | Expected result |
| --- | --- | --- |
| `MM-V-I01` | Event first fires below 400 | Baseline behavior only |
| `MM-V-I02` | Event first fires at 400+ with Evolution I enabled | First visit can use broader demands and entries |
| `MM-V-I03` | Event first fires at 800+ with I and II enabled | Enabled milestones record in order, first visit uses Evolution II behavior |
| `MM-V-I04` | Event first fires at 1000+ with all enabled | First visit uses Evolution III behavior |
| `MM-V-I05` | Active chain crosses 400 | Evolution I activates through paced target-local event |
| `MM-V-I06` | Evolution I disabled | No I log or I recorded flag appears |
| `MM-V-I07` | Evolution I disabled, Evolution II enabled | Evolution II activates its own entries and full demand family, Evolution I entries and log remain absent |
| `MM-V-I08` | Evolution milestone activates | Chaos value does not change from activation itself |
| `MM-V-I09` | Several visits after evolution | Parent fired count and History remain one |

## J. Nationwide nuclear annihilation

| ID | Setup | Expected result |
| --- | --- | --- |
| `MM-V-J01` | Small target with several states | Every unique owned or controlled valid state processes once |
| `MM-V-J02` | State both owned and controlled | State is not struck twice |
| `MM-V-J03` | Large empire | Bounded batches cover every valid state and produce final receipts |
| `MM-V-J04` | Existing terminal wasteland state | State is skipped with explicit reason |
| `MM-V-J05` | Populated target | Exact civilian population loss enters Deaths once |
| `MM-V-J06` | Military units in struck states | Military losses use the established path without duplicate casualty estimates |
| `MM-V-J07` | Strike completes | Fallout and Air Cleanliness use real state contributions |
| `MM-V-J08` | No attacker exists | No country receives nuclear Condemnation or blame |
| `MM-V-J09` | Air Cleanliness crosses Fallout threshold | Air system may submit normal request, Event 53 does not directly set world end |
| `MM-V-J10` | Source nuclear event or terminal route inspected | It remains unfired and unprogressed by direct Event 53 bookkeeping |

## K. Compound safety

| ID | Package | Expected result |
| --- | --- | --- |
| `MM-V-K01` | Independence and armed war | All releases reserve before mutation and wars use correct actors |
| `MM-V-K02` | Civil war and intelligence exposure | Exposure resolves against post-split legal government |
| `MM-V-K03` | Disease and food collapse | Population deaths are recorded once by owning systems |
| `MM-V-K04` | Embargo and stockpile destruction | Coalition commits and one locked reserve debits once |
| `MM-V-K05` | Mutiny and external war | War safety uses post-mutiny force state |
| `MM-V-K06` | State collapse sequence | Civil fracture, leak, and embargo share one projected target proof |
| `MM-V-K07` | Pestilence, hunger, and flight | Disease, famine, and migration ledgers remain separate and exchange valid proof |
| `MM-V-K08` | War on every front | Mutiny, several wars, and stockpile loss complete under one receipt |

## L. Presentation, logs, and assets

| ID | Check | Expected result |
| --- | --- | --- |
| `MM-V-L01` | Initial popup | Secure location, ordinary man, exact demand, clear choices |
| `MM-V-L02` | Recurring popup | Location can vary while identity remains consistent |
| `MM-V-L03` | Pay option tooltip | Exact cost and blocked reason display correctly |
| `MM-V-L04` | Refusal transition | Does not reveal package before selection |
| `MM-V-L05` | Borrowed consequence report | No duplicate source opening or super-event |
| `MM-V-L06` | Event Details | Premise and status show without registry or formula leak |
| `MM-V-L07` | Evolution rows | Correct event, actor, stage, tier, date, and enabled state |
| `MM-V-L08` | Five event pictures | Correct scene, period fit, same man, no supernatural explanation |
| `MM-V-L09` | Event list | Reworked Event 53 is enabled by default only after completion policy is met |
| `MM-V-L10` | Catalog row | Final workbook mirrors implemented in-game wording and corrected premise |

## M. Cleanup and migration

| ID | Setup | Expected result |
| --- | --- | --- |
| `MM-V-M01` | Duplicate target markers introduced in test setup | Reconciliation retains authoritative target and clears stale marker |
| `MM-V-M02` | Pointer missing, one valid marker exists | Pointer recovers |
| `MM-V-M03` | Two plausible targets, no proof | Chain ends and logs an error without guessing |
| `MM-V-M04` | Locked demand outside present state | Stale demand clears |
| `MM-V-M05` | Completed owner receipt with resolving flag | Reconciliation closes transaction and schedules one visit |
| `MM-V-M06` | Removed package ID in old save | Stale selection clears and current pool rebuilds |

## Completion evidence

A scenario passes only with the relevant source, MCP artifact, ledger values, and visible result when applicable. A compile or syntax pass alone does not prove gameplay acceptance.
