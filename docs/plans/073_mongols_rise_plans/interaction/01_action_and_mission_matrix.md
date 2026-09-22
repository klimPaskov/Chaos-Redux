# Action and mission matrix

## Status and shared rules

D and M labels below are planning identifiers, not final runtime IDs or localisation keys. Costs are dynamic functions with starting anchors in the balance file. PP means political power, CP means command power, IE means infantry equipment, and SE means support equipment.

Those four are the maximum spendable decision-cost types. Treaty terms may schedule a transfer through their own disclosed agreement. A decision must not hide an extra immediate manpower, fuel, or artillery debit under that distinction. Deployment of previously funded entitlement has no second personnel cost. Ordinary recruitment remains an ordinary accounted recruitment process.

Target selection and inspection are free controls. Their existence does not add paid decisions. Only the phase-appropriate actions are shown. Normal visible limit is five and the hard maximum is six, with at most three simultaneous missions.

## Actions

| ID | Context and action purpose | Target and prerequisite | Cost or sacrifice | Result and failure rule |
|---|---|---|---|---|
| D01 | Opening campaign selection | Reachable valid objective | No debit | Changes selected preview only |
| D02 | Sovereignty demand | Actual overlord and accepted restoration | PP, risk of rejected independence demand | Opens the overlord's response, no silent faction deletion |
| D03 | Deploy ready muster | Unspent funded entitlement and safe reception | No second troop cost | Consumes one entitlement allocation, invalid site consumes nothing |
| D04 | Prepare campaign | Selected valid objective and available campaign capacity | PP and CP, commitment of a campaign slot | Opens preparation, cannot prepare the same objective twice |
| D05 | Send submission offer | Reachable valid independent or correctly represented target | PP and commitment to offered terms | Target answers, no unapproved payment before acceptance |
| D06 | Commit follow-up opportunity | Recent qualifying victory and valid next objective | CP and consumed victory opportunity | Shorter next preparation, one opportunity cannot serve several campaigns |
| D07 | Choose regional settlement | Legal ownership or valid agreement and complete required set | Real autonomy, extraction, or direct-rule tradeoff | One chosen settlement and one allocated reward |
| D08 | Allocate secured stores | Unspent settlement allocation | Opportunity cost of other settlement rewards | Credits only the awarded allocation, no duplicate generic capture reward |
| D09 | Reorganize reserve support | Actual reserve and allowed templates | IE or SE as applicable, temporary lower readiness | Supports a selected reorganization, no instant casualty replacement |
| D10 | Restore campaign route | Identified broken section with a valid project | PP and SE, time committed to repair | Actual route project, no completion inside enemy-controlled territory |
| D11 | Review tribute | Selected active agreement at a valid review point | PP and changed future rights | Opens terms, does not create a fifth hidden click cost |
| D12 | Address arrears | Actual recorded shortfall | Foregone payment or risk of enforcement | Deferral, revision, or legal rupture, no fictional donor debit |
| D13 | Negotiate khanate obligation | Actual member and feasible contribution | PP and a stated reciprocal commitment | Target agreement, never compulsory human acceptance |
| D14 | Confirm appointment | Eligible real character or supported institution and open office | PP and political commitment | Office changes once, no fabricated historical identity |
| D15 | Mediate dispute | Concrete unresolved rights conflict | PP and a real territorial or contractual concession | Changes the dispute, no generic repeatable loyalty purchase |
| D16 | Convene kurultai | Valid vacancy or serious recognized succession dispute | PP, time and possible concessions | Opens the eligible succession process |
| D17 | Confirm succession settlement | Valid candidate or accepted institutional choice | Honors negotiated concessions | Updates office and obligations without regranting armies |
| D18 | Shorten exposed frontier | Actual overextended commitment and legal withdrawal choice | Territory, abandoned objective and Momentum | Cancels or revises the commitment without fabricated peace |
| D19 | Negotiate successor compact | Viable independent former member and actual center | PP and revised rights | New agreement after mutual response, old initial grants remain spent |
| D20 | Select reunification campaign | Current former-member territory and legal approach | Standard campaign costs and political risk | Uses current ownership, never a universal annexation shortcut |
| D21 | Advance Karakorum project | Valid site and previous stage | PP or SE where appropriate, construction commitment | Advances actual facilities or administration once |
| D22 | Decide permanent capital | Finished project and verified exact map capability | Government relocation and stated political tradeoff | Real supported relocation, blocked if exact site cannot be represented |

## Phase budget examples

Opening shows D01, D03, D04, and D02 only when subject status requires it. Active campaigning shows D04, D05, D06, D07, and a relevant D09 or D10. Imperial government shows the contextually valid subset of D11 through D15 plus the current campaign action. Succession prioritizes D16, D17, a relevant D15, D18, and one urgent military action. Recovery shows D03 only for genuinely unspent entitlement, D10, D19, D20, and the current capital remedy.

These are examples of priority selection, not permission for an extra tab to expose the full action matrix simultaneously.

## Missions

| ID | Objective | Entry and completion | Failure or interruption | Pacing factors |
|---|---|---|---|---|
| M01 | Secure a reception solution | Blocked entitled army, valid safe deployment achieved | Lost site leaves entitlement unspent | Available territory and current war |
| M02 | Resolve sovereignty | Subject demand issued, valid recognition or legal independent state achieved | Refusal opens the actual next diplomatic step | Overlord response and war situation |
| M03 | First campaign objective | Prepared objective, required hold condition met | Loss pauses or fails the same objective record | Distance, strength and terrain |
| M04 | Establish a regional settlement | Objective secured, lawful chosen settlement completed | Peace or ownership changes revalidate it | Size, government and war rights |
| M05 | Recover a severed route | Specific broken link, actual connection restored | Continued loss leaves dependent benefits suspended | Route length, damage and control |
| M06 | Develop Karakorum | Current valid stage, real facilities or institution complete | Site loss pauses the project | Industry, support and transport |
| M07 | Prove a khanate obligation | New valid member, first actual agreed delivery | Inability differs from refusal | Member resources and access |
| M08 | Resolve arrears | Genuine shortfall, valid paid or revised agreement | Repeated refusal can open enforcement | Actual donor condition and agreement |
| M09 | Resolve kurultai | Valid vacancy, recognized succession settlement | Prolonged contest can lead to defiance | Political route, promises and support |
| M10 | Recover imperial authority | Concrete crisis, required cause addressed durably | Escalates only through stated unresolved condition | Crisis severity and actual remedies |
| M11 | Establish continental connection | Reviewed route chain, all required links functioning | A break pauses qualification | Geography and partner agreements |
| M12 | Stabilize a successor compact | Real post-collapse agreement, obligations hold | Break returns parties to current valid relations | Prior conflict and delivery feasibility |
| M13 | Consolidate a recovered center | Viable surviving government, seat and basic commitments secure | Further territorial loss rechecks viability | Remaining resources and current war |

Each mission owns one progress condition. Completion is automatic. The standard tooltip, custom puzzle, AI, and completion path reference the same qualification. A timer expiry never steals third-party territory to force a clean result.
