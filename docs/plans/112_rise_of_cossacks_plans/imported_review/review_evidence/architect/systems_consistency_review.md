# Event 112 systems consistency review

## Scope and evidence boundary

The architect reviewed gameplay chapters 01 through 11 and 13 for opening viability, finite resource accounting, political progression, cross-document consistency, typed defaults, native dependencies, and lifecycle cleanup.
This is a design review.
It does not establish live gameplay, installed geometry, verified native syntax, a completed probability comparison, or a passing MCP suite.

Canonical mechanics are in parts 03 and 07.
The earlier system_proposal.md and its generation scripts are working history and must not overwrite the later canonical text.
The concise current handoff is planning_work/architect/integration_contract.md.
No gameplay script, source skill, workbook, CSV, or final asset was modified by this architect task.

## Reading coverage

All large reads used complete bounded outputs.
A later broad search output was truncated, so it served only as navigation and the relevant clauses were reread separately.
It was never counted as a complete document read.

| Chapter | Complete semantic reading | Subsequent changes inspected |
|---|---|---|
| 01 Core | Entire 18139-character baseline | Current local allowance, core, remaining-country viability, and production-route clauses |
| 02 Hosts and geography | Entire 25633-character baseline | Current production-viability cross-reference |
| 03 Founding and shared systems | Entire authored chapter and every owned edit | All accepted escrow, readiness, weighting, founding, recovery, production, unit, and raid changes |
| 04 Charters and regional paths | Entire 94998-character baseline in four ranges | Exact current readiness, compact, civilian movement, extension, P07, and P09 clauses, without claiming a second full read of unrelated later edits |
| 05 Great projects | Entire original body, followed by the current GP08 section and ending | Complete 11788-character unified delta from the saved 52083-character review snapshot |
| 06 Military and economy | Entire frozen 25767-character snapshot | Complete 4624-character delta covering provisional templates, raid exclusions, and postwar cost precedence |
| 07 Evolution and lifecycle | Entire authored body and full later 37155-character snapshot | All owned dispatch and dependency changes, including the parent-authored Chaos Impact Table |
| 08 Decisions and missions | Entire 23516-character baseline | Current first 75 lines and exact A01, A27, founding-settlement, and shared-delay clauses |
| 09 Countries and characters | Entire frozen 21689-character snapshot | No later change was present at the checked snapshot |
| 10 Focus architecture | Entire frozen 16462-character snapshot | No later delta was present at comparison |
| 11 AI and scenarios | Entire frozen 19611-character snapshot | Complete 1649-character closure-scenario delta |
| 13 Integration and acceptance | Entire frozen 14429-character snapshot | No later delta was present at comparison |

Frozen review copies and their hashes are in review_snapshots/manifest.json.
Final owned-file hashes are separate because the canonical chapters continued to receive accepted corrections during review.
This is revision-level evidence, not a claim that the architect independently reread every byte of every other owner's final edit.
The full supplied-source gate and the nine pinned repository reads remain in their separate source and evidence ledgers.

## Findings and dispositions

| ID | Concrete finding | Accepted correction and reviewed owner | Status |
|---|---|---|---|
| R01 | Paying an arms supplier before delivery and then refunding the buyer could duplicate PP | Part 03 holds actual buyer payment in escrow, credits only cumulative observed delivery, refunds only unearned undelivered escrow, and requires separate physical and financial reversal after completion | Closed at specification level |
| R02 | Event 112-only free manpower becomes unobservable after native pools mix | Parts 03 and 04 use actual current country free manpower divided by current fielded land manpower plus that same free manpower, at least 0.20, with later native units included | Closed |
| R03 | Mixed occupied claimants could receive human and crisis-load factors more than once | Part 03 uses one combined candidate factor, a state-weighted country mean, and a conditional state draw that applies it once | Closed |
| R04 | First charter required a civilian settlement whose normal action required a prior charter | Part 03 A01 supplies a finite pre-charter founding settlement, with root cross-references in parts 04, 08, 10, and 11 | Closed |
| R05 | A late installment lost 2 C and 1 J while settling its dispute gained 6 C and 2 J | Part 03 restores only that receipt's actual still-unrecovered loss, with prior positive credits reconciled and no renegotiation reset | Closed |
| R06 | A zero-MIL state with no free slot could remain industrially blocked forever | Part 03 requires repairable MIL, a genuine free slot, or an actually available verified native CIV-to-MIL path before founding, with matching root references | Closed at design level, installed binding pending |
| R07 | Two nominal owned states did not prove another viable controlled state would remain | Part 03 preserves another owned, controlled, usable state wherever the transaction could otherwise remove an affected authority's last viable territory | Closed |
| R08 | Required exact formation defection had no outcome in the evolution pool | Part 07 now has five weights 32, 28, 20, 10, and 10, with a distinct one-unit exact transfer and matching part 03 receipt contract | Closed at design level, native preservation pending |
| R09 | A zero free-manpower reading could incorrectly remove an actual field-formation opportunity | The separate exact formation candidate uses the real unique unit and its physical route independently of the volunteer pool | Closed |
| R10 | Military chapter put capture in R01 and implied a breach alone made partners raidable | Corrected part 06 delta matches part 03 infrastructure-only R01 and measured R02, with allies, own subjects, protected partners, and truces still excluded | Closed |
| R11 | The raid wording left the peacetime exception implicit | Part 03 explicitly requires actual war for R01 and reserves the separately warned dispute exception for R02 | Closed |
| R12 | UI action count alternated between five and six, while extension prices and durations differed | Current parts 04 and 08 use five ordinary primary actions plus one emergency or status row, one A27 extension for 20 PP and up to 60 days, or one alternative free route-loss suspension using the same guard | Closed |
| R13 | P07, P09, and generic H12 could depend on delayed rewards or dispute farming to cross J60 | Current regional clauses and GP08 use honest reachable 60 baselines with substantive work retained, while higher national gates use finite project endorsement | Regional correction closed, final endorsement launch wording owned by root |
| R14 | GP01 demanded at least 10 J loss for the same shared breach priced at minus 10 C and minus 8 J | Current part 05 delta uses one shared breach receipt and no additive regional punishment | Closed |
| R15 | Shared first-peace and repair defaults could charge the same original promise twice | Current part 05 and part 06 precedence give the original complete P or GP contract ownership, with A20/A21 and A19 defaults only when no specific complete owner exists | Closed |
| R16 | M02 and M05 required a trained formation before unlocking its template | Current part 06 exposes provisional native templates at funded start after real technology gates, without free units or equipment, then awards trained capability only on completion | Closed |
| R17 | Player-optional civilian movement and unverified exact defection could be treated as optional implementation | Parts 03, 07, and 13 retain those selected features as required complete-package content while blocking their unsupported activation | Explicit required-incomplete implementation gate |
| R18 | The immediate transaction did not repeat the already accepted single founding-core rule explicitly | Part 03 now applies that one core before accrual reconciliation, preserves foreign cores and claims, and gives it a boundary case | Closed |

## Exact founding repair

C means Host Cohesion and J means Settlement Legitimacy.
The immediate free compact credits C plus 5 and J plus 2 once.
One actual shared quote on a 35 PP base funds the civilian program.
The opening 40 PP covers the unmodified price, but a larger quote can require ordinary native accrual.
An unpaid setup makes no debit attempt and starts no funded clock.
Unexpected partial native payment uses the existing fault-receipt contract.

The stages can complete no earlier than paid days 30, 60, and 90.
Their maximum C credits are 5, 5, and zero.
Their maximum J credits are 8, 8, and 7.
Founding recovery stops at C60 and J50.
The first council is inside the first stage rather than an additional award, and any previously paid council portion reduces that stage's remaining allocation.
Unused stage credit expires rather than being banked for later losses.

The conservative lower clamps C35 and J25 therefore progress through compact 40/27, first stage 45/35, second stage 50/43, and final stage 50/50.
The actual coupled minimum C40 and J25 finishes at 55/50.
No conquest, passive recovery, raid, external sponsor, extra council, or deliberately unpaid dispute is needed.
The first viable C50/J50 charter can start after the day-90 civilian settlement and meet a 30-day hold at day120.
The assembly window starts when that assembly is actually chosen.
A delayed quote or a more demanding charter moves that actual date later, without replaying the founding mission or any grant.
The settlement remains available after the founding mission expires.

Cases F52 through F61 cover affordability, prior council credit, exact lower clamps, higher existing meters, interruption, restoration, later charter choice, and the late-payment exploit.
F62 through F67 add industry, conversion, source viability, empty free-manpower with a real unit, initial core accrual, and the R01 peacetime exclusion.

## Finite unit and country accounting

The exact-formation outcome selects one real unit.
Its identity, actual strength, equipment models and quantities, experience, composition, commander ownership, location, and incompatible commitments are checked before transfer.
An approved reconstruction adapter must faithfully preserve those values and the original unit lineage.
Renaming or restoring a country cannot create a new eligible copy.
Missing strength and equipment remain missing.
No local allowance, replacement reserve, or full veteran unit is created to compensate for losses.

The country registry still allows at most four simultaneously independent Event 112-created hosts, including the principal, and twelve active registered participants in total.
At most four exile or custody actors fit inside that same twelve.
Living preexisting DHC and KHC partners do not consume new-created-host capacity and are never overwritten.
Dormant admission still needs grounded identity remediation and shared 005/006/112 arbitration.
No dead carrier is recycled while its identity, exile, person, or physical receipt remains live.

Civilian transfers keep one measured physical owner.
Charters, cores, military recruitment, and flags do not move population.
Actual civilian origin debit equals destination credit plus measured route deaths, with symmetric state and country reception ledgers.
The selected P04, P11, P12, P14, and GP08 civilian routes remain required implementation despite player choice.

## Arithmetic actually checked

The seven earlier opening examples and 42 rational invariant checks remain in arithmetic_verification.json.
The proposed raid examples were checked as arithmetic without claiming installed interpolation or live outcomes.
Three further founding settlement traces were evaluated with exact rational arithmetic during this review.
They cover conservative 35/25, actual minimum 40/25, and Case C at C575/12 and J75/2.
Case C reaches 60/50 after its second funded stage and completes the final civilian obligation without another meter increase.

The five answer weights total 100.
Only volunteers and compact normalize to 2/3 and 1/3.
Only exact formation and compact normalize to 1/2 and 1/2, including when source free manpower is zero.
These are specification calculations rather than final game probabilities.

## Final cross-owner clarification

The new project endorsement table fills a bounded gap from its stated ordinary baseline to a higher national formation gate after the project's real work.
The architect requested an explicit global sentence allowing the final constitutional mission to start at that table's minimum baseline once its other start conditions pass.
The higher destination remains the final formation check.
Without that precedence, old branch wording could still be read as requiring the destination before the mission that earns it begins.
The root owns this final wording and disposition.

## Remaining implementation work

The active installed map, complete mod-stack identity scan, country activation, actual fielded-manpower reading, native recipes, automatic accrual, unit creation, troop retreat, occupied-state wars, source-specific equipment debit, native factory conversion, exact formation transfer, and raid lifecycle still need inspected bindings and actual scenarios.
The newer exact-population and universal-cost contracts must be reconciled with their older pinned implementations.
Those source findings remain contract mismatches or qualified inferences, not live-game bug proofs.

The reviewed presentation keeps two public meters, three permanent focus-created spirit slots, and custom visuals for native cavalry and infantry.
Plastun remains an infantry template and visual identity rather than a new combat archetype.
Ordinary arms prices and material opening grants remain governed by the same facts for player and AI countries.
Supported player-crisis pressure belongs only in the stated opportunity and adverse-response contexts.

No further gameplay contradiction identified by this architect remains open in the owned chapters after the accepted corrections.
Other owners retain responsibility for their final edits and the endorsement launch clarification.
The planning package may complete its design review while these explicit future engine and production gates remain open.
