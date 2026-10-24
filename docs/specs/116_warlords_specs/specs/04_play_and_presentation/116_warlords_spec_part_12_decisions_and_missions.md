# Part 12: Decisions, missions, and material costs

Decisions let the player commit resources, propose agreements, choose a political course, and direct attention to a real objective. Missions resolve that objective from current facts. Paying for a plan does not prove that it succeeded.

All action and mission labels below are structural working labels for implementation. Player wording, tooltips, and option text remain direction-only.

## Decision families and cost principles

| Family | Starting cost and commitment examples | Scaling factors | Main constraint |
| --- | --- | --- | --- |
| Command appointments | 35 to 60 political power or 20 to 40 command power, with an actual eligible appointment | Breadth of authority, institutional strength, current crisis | Pure administrative appointment can use PP/CP alone, but it grants no troops, supplies, or conquered territory |
| Depot and route security | About 35 PP, one civilian-factory equivalent reserved for 90 to 120 days, and real security capacity in the target area | Area, transport damage, hostile pressure, distance | The assigned force and required route must actually remain available |
| Military administration | About 45 PP, two civilian-factory equivalents for 90 to 150 days, and an identified support or transport plan | Army size, disorder, shortages, existing institutions | Capacity is committed to a real service, not a fictional payroll currency |
| Training and reorganization | Native manpower, actual equipment, training time, and a bounded staff fee where needed | Template, current experience, equipment mix, founder/staff ability | Native unit costs are paid in full, with no duplicate event-funded training cohort |
| Material aid | Exact cargo, a real route and transport, optionally a modest PP negotiation fee | Shipment size, available variants, route risk, contract terms | Sender loss equals receipt plus actual transit loss |
| Political settlements | Roughly 50 to 100 PP plus explicit autonomy, command, access, or territorial concessions | Conflict scale, bargaining position, promises, legitimacy | Every party is real and every concession changes an actual relationship |
| Integration and reconstruction | About 50 PP, one to three factory equivalents for 120 to 180 days, and actual controlled sites or accounted cohorts | Damage, force size, regional acceptance, current access | Completed work changes the relevant surviving capacity, not a historic maximum |
| Major military campaigns | Real armies, supply, strategic access, production and opportunity cost, with at most 60 CP per special staff action | Theater size, enemies, geography, logistics | Victory is fought through ordinary warfare |

These are starting price anchors. Each action has at most four spendable resource types. Do not turn an ordinary action into a checklist of unrelated currencies. Command-power charges never exceed 60. Resource requirements can be meaningful nonconsumed commitments, such as a real division guarding a route, but they must remain assigned and verifiable.

Track committed capacity across active objectives. One formation, commander, transport allotment, or industrial reservation cannot fully satisfy two incompatible missions or defend a disconnected external front at the same time. A second request must use spare capacity, declare a proved partial allocation where meaningful, or visibly displace the first assignment. Moving a cohort out of range removes its previous contribution. Compatible objectives at the same place can share a genuinely sufficient service only through a documented capacity rule, never two full claims on the same scarce capacity. AI uses the same commitments and may cancel obsolete work.

Use the universal cost framework for eligible quoted fees and charges. Quote again at confirmation and at a delayed installment. The displayed quote, actual debit, and receipt must agree. A quote is not a lock. Preserve native reserve floors and inclusive affordability. Physical troop and cargo requirements are separate from a discounted price and cannot be reduced while delivering the original full physical quantity.

Factory reservation is a logical requirement until a supported owner adapter is verified. If the engine cannot reserve the intended capacity honestly, implementation must provide an explicitly accepted equivalent economic action with the same strategic cost. It must not use an invisible factory-count change that permanently destroys or duplicates factories.

## Parent actions

| ID | Action and eligible target | Actual outcome sought | Failure, cleanup, and restraint |
| --- | --- | --- | --- |
| P01 | Secure a named depot or route in the remaining country | Sustain control and security capacity for the associated mission | Losing the site stops progress, unused reservations can be released, forces remain real units |
| P02 | Restore administration for a disrupted real command | Complete the support plan and remove its identified coordination problem | No credit for undelivered supplies or an army that no longer exists |
| P03 | Reassign a threatened general to a lawful available role | Remove the relevant independent authority through a verified appointment | Reject protected, unreachable, or owner-locked actors, do not pick a replacement silently |
| P04 | Negotiate with a warned command | Fulfill a bounded material or regional settlement before defection | Refusal remains possible, broken terms resume the actual pressure |
| P05 | Attempt lawful detention of the actual conspirator | Secure custody through a credible local security advantage | A failed attempt may aid a viable escape, never creates a country without a viable region |
| P06 | Organize a recovery offensive on a specific front | Prepare logistics and staffing for an ordinary military campaign | No automatic state transfer, failed or abandoned plans release only unspent reservations |
| P07 | Offer reintegration or partition to actual parties | Reach and perform a valid military and political settlement | Refused, stale, or legally unsupported peace operations do not charge a success outcome |
| P08 | Reintegrate veterans or reconstruct a recovered district | Account for surviving cohorts and repair actual productive or civil capacity | No double manpower return, no casualty refund, lost territory removes the dependent benefit |

## Warlord and foreign actions

| ID | Action and eligible target | Actual outcome sought | Failure, cleanup, and restraint |
| --- | --- | --- | --- |
| W01 | Organize the actual founding reserve | Assign existing loyal formations and sustain their training/supply | Template naming alone is insufficient, no free experience or equipment refill |
| W02 | Establish an affordable recruitment program | Train ordinary formations from real manpower and equipment | Missing stocks or population block the program before a free unit is created |
| W03 | Repair an arsenal or transport link | Complete work at a specific controlled site | Damage, occupation, or resource loss can delay the project, progress follows actual work |
| W04 | Request a material contract from a real potential patron | Secure a declared supply agreement and delivered support | AI may refuse, route failure stays pending or cancels according to the contract |
| W05 | Offer a regional civil compact | Establish actual administration and mobilization terms | Exclusive personal-rule benefits transform, violated terms create real political pressure |
| W06 | Reform staff and succession | Appoint lawful officers or institutions and establish continuity | A dead or removed person cannot complete the appointment, current country persists |
| W07 | Prepare a civilian transition | Fulfill institutional and military handover requirements | An autonomous personal army blocks completion, failure does not refresh opening grants |
| W08 | Negotiate with, subordinate, or campaign against a rival | Obtain a real treaty, submission, or military outcome | No automatic absorption from a demand, allies remain independently commanded |
| F01 | Recognize a government or offer mediation | Change a diplomatic relationship or convene actual parties | Recognition grants no forces or obedience, mediation cannot sign for absent countries |
| F02 | Deliver equipment or provide native volunteers | Transfer owned cargo or create a lawful native service relationship | Exact custody and native return rules remain, duplicate delivery receipts are rejected |
| F03 | Intervene against a parent or warlord | Enter a real war with native diplomatic consequences | No scripted victory, no free universal military access |
| F04 | Support an independence or restoration effort | Supply an existing command or a viable owner-approved claimant | Cannot create a full army, government, or population from an independence flag alone |

## Unification and terminal actions

| ID | Action and eligible target | Actual outcome sought | Failure, cleanup, and restraint |
| --- | --- | --- | --- |
| G01 | Prepare a campaign against an actual origin rival | Establish a real front and demand backed by military operations | Requires the canonical 067 actor in lawful command, no substitute leader |
| G02 | Negotiate genuine military submission after a campaign | Bind existing and future armies, policy, and access through a verified relationship | Nominal subjecthood or an independently commanded army fails |
| G03 | Integrate a defeated rival's surviving capacity | Incorporate real officers, forces, industry, and routes | Duplicate lineage rewards and repaired historical armies are forbidden |
| G04 | Establish Supreme War State after domestic consolidation | Change the existing host's political identity and command constitution | Recheck every current rival, no annexation or world-end launch in this action |
| G05 | Establish a theater command and supply program | Sustain an actual military anchor with forces, production, and routes | An isolated flag or port does not complete the program |
| G06 | Examine international readiness | Obtain current authoritative proof for Part 9 | This is a bounded assessment, unknowns fail, it does not fill missing requirements |
| G07 | Reconstitute a damaged military union | Recover real control and complete the required consolidation again | No second formation reward or historical-victory substitute |
| O01 | Coordinate the defense of a real threatened theater | Agree access, supplies, and ordinary joint war activity | No automatic alliance or transfer of independent defenders' armies |
| O02 | Free a genuinely subordinated country or support a surviving rival | Break an actual command relationship through military or owner-approved political success | Credit occurs only when independence is real and command changes |

These rows describe required gameplay actions. Implementation may combine tightly related rows in one targeted decision with explicit variants. It must not merge materially different routes into one opaque button or remove the human choice that distinguishes them.

## Missions and completion evidence

| Mission | Entry and ordinary duration anchor | Automatic completion proof | Invalidation and consequence |
| --- | --- | --- | --- |
| M01: secure the remaining command base | P01, about 90 to 120 days | Named sites controlled and supplied with required security for the sustained interval | Site or route loss resets the affected proof, completed paid work remains |
| M02: contain a warned defection | Active continuation warning, normally 120 days and never below 90 | Actual grievance resolved, authority lawfully removed, or a performed settlement acknowledged | On expiry, only a still-viable actual command can defect |
| M03: sustain the new state | New warlord, about 120 days | Working capital, supplied founding force, replacement route, and functional government held through the interval | Defeat or collapse resolves through actual survivors, no survival army grant |
| M04: fulfill an aid contract | Actual agreement, normally 90 to 180 days by route and cargo | Delivered accepted quantities and performed recipient obligations | Partial delivery remains partial, losses and cancellation follow exact receipts |
| M05: integrate a surviving command | Real surrender, about 120 to 180 days | Actual existing/future military authority, lawful appointments or disarmament, and supply proved | Freedom, refusal, or broken command invalidates membership and current proof |
| M06: consolidate domestic unification | All current origin rivals controlled, 180 days | All required current relationships and viable root sustained | A freed or new actual rival restarts the uninterrupted proof requirement |
| M07: establish a theater anchor | Actual controlled target area, about 120 to 180 days | Working command center, hinterland, forces, replacement access, and routes | Lost or unknown critical control removes the anchor's credit |
| M08: transfer government to civilians | Chosen political route, about 180 days | Performed institutional settlement and real end to independent personal military rule | A remaining autonomous political army blocks completion |
| M09: consolidate international dominance | Part 9 military requirements first met, 180 days | Continuous current effective global command and sustainable capacity | Material loss invalidates readiness, global toggles and Chaos rechecked at commit |
| M10: reconstruct a postwar district | Real damaged territory or accounted cohort, about 180 days | Declared repair or settlement work completed at the actual target | Ownership or population changes require fresh target proof, no fabricated completion |

Missions complete from their objective facts. A separate claim-reward click is unnecessary unless it makes a real subsequent choice. Do not punish a player who fulfilled the objective before the last day but did not click an extra button. Do not award completion if the qualifying actor or site has changed to something else with the same UI row position.

An easier ordinary mission should not use an extremely short deadline. Special urgent military situations may create warnings whose real event timing is shorter, but they cannot replace the normal prevention window without a documented justified route and clear counterplay.

## Interface behavior

Show each category only to actors with relevant work. Parent rows point to threatened regions and actual generals. Warlord rows point to its own administration and resources. Patron rows identify actual recipients. Generalissimo rows distinguish unresolved rivals, genuine subordinates, historical victories, and current world-end readiness.

Use one selected factual context per action and freeze it on confirmation. A country row, mutable list index, or last-opened target is not durable transaction identity. The tooltip explains the real requirement that is missing. The main cost line uses at most three values and four words, with detailed receipts and secondary constraints in the normal tooltip or detail panel.

Show Command Cohesion consistently when relevant, with a single color identity and the main current causes. Do not add loyalty, order strength, global dominance, patron favor, or reconstruction currencies. Required region and country lists are facts, not a second meter. Event Details provide context and identity rather than reproducing the event's effects.

## AI execution and cancellation

AI willingness uses current affordability, the probability of performing the objective, military danger, political route, and diplomatic interests. Starting an action reserves its target and resources so the AI cannot queue mutually impossible commitments. A failed prerequisite removes the action from consideration instead of repeatedly attempting it every day.

Refund only actual paid components that remain refundable after the proved reversal or cancellation. Spent equipment, completed work, transit losses, and executed political concessions do not reappear. Keep partial-debit and partial-refund evidence until settled. Same-key retries return the same result. Save/load, nested owner calls, and simultaneous human requests must not change the target or replay the benefit.
