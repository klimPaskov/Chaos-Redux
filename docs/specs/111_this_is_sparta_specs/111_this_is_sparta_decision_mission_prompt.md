# Event 111 decision and mission implementation prompt

Implement the complete ordinary and Age of Heroes decision and mission package for Event 111, `This is SPARTA!!!`. Work from the accepted specification package in `docs/specs/111_this_is_sparta_specs/`. Treat all semantic keys below as authoring consumers that must receive an explicit crosswalk to final collision-audited script IDs. They are not permission to invent shared registry identifiers.

## Required reading and task boundary

Complete the Project Source reading gate under the current project protocol before implementation or redesign. Read the current AGENTS and mechanics, the full event, decision/mission, focus, country, asset and GUI guidance, applicable shared-system references and the accepted eight design parts. Resolve source-version conflicts through the recorded precedence. An inventory, hash, excerpt or search result does not substitute for full required-source reading.

The principal design owners are:

- [Part 1: Core](111_this_is_sparta_spec_part_1_core.md), for event identity, initial values, common milestones, persistence and Chaos accounting.
- [Part 2: Country and military](111_this_is_sparta_spec_part_2_country_and_military.md), for finite personnel, renewable modern recruitment, technology, equipment and institutional stages.
- [Part 3: Focus routes](111_this_is_sparta_spec_part_3_focus_routes.md), for commitment, exact geographic roles, sovereignty rules and final charters.
- [Part 4: Decisions and settlements](111_this_is_sparta_spec_part_4_decisions_and_settlements.md), for ordinary action records, costs, missions and transactional semantics.
- [Part 5: Age of Heroes](111_this_is_sparta_spec_part_5_age_of_heroes.md), for MY01–MY14, EX01–EX03, unique actors, force caps, service conflicts and Strain.
- [Part 6: Connections and achievements](111_this_is_sparta_spec_part_6_connections_and_achievements.md), for actual outside actors and achievement consumers.
- [Part 7: Presentation and assets](111_this_is_sparta_spec_part_7_presentation_and_assets.md), for the exact panel, category rules and all visual consumers.
- [Part 8: Implementation and AI](111_this_is_sparta_spec_part_8_implementation_and_ai.md), for state ownership, provider contracts, callbacks, AI and proof requirements.

Implement the accepted behavior. Do not replace the five campaigns with generic claim decisions, invent a fourth public value, add a sixth conquest route or resolve a missing native capability by silently changing its meaning. Bring a concrete unsupported operation and a reviewed supported alternative to the owning implementation task. Keep the accepted gameplay usable with the evolution disabled and without paid DLC.

## 1. Establish dependencies and operation ownership

The country must already have the audited `SPARTA_TAG` identity, an actual build-time Laconia state split, valid supply and capital, event creation provenance and the required custom military packages. An unavailable dependency blocks the affected action with a truthful reason. This task must not create a second country, transfer all the Peloponnese or award a replacement founding host.

The founding contemporary local brigades are ordinary native infantry, not custom modern cadres. Preserve the accepted 1/2/3/4 local brigades at 3,000-person ceilings and 2/3/5/6 returned brigades at 2,000 people. No local brigade receives returned-origin credit.

Use current 111 and migrated legacy 116 as one incident. Route, institution, geography, unit cohort, hero and manifestation records have one authoritative owner each. A selection cursor is never proof of payment, ownership, service, membership or completion. Reuse the shared owner interfaces from Part 8 and preserve its parent-owned versus provider-supported military dispositions.

Create the event-owned decisions, missions, scoped response events, scripted effects and triggers, required cost adapters, localisation directions, asset-consumer manifest and tests or scenarios appropriate to the installed project. Shared registration remains with its owning system. The CXT daily hook performs registration only. It must not gain recurring repair, supply or manifestation effects.

## 2. Ordinary actions: complete coverage

Implement every family below, including contextual variants needed by the accepted routes. Each operation has a real target, disclosed material costs, a deadline where relevant, distinct success and failure, legal cancellation and a complete receipt. Part 4 remains the authoritative detailed tuning table.

| Consumer | Required behavior | Anchor cost or important constraint |
|---|---|---|
| `111_action_emergency_supply` | Repair or organize one actual home logistics bottleneck and observe the stated objective | 25 PP and one civilian factory for 35 days. First completed home program grants 5 Civic Settlement. |
| `111_action_civic_compact` | Deliver selected administrative and citizenship obligations, mature institutions and legitimate civic restoration | 50 PP and one civilian factory for 90 days. Founding compact grants 10 Civic Settlement, ratification 15 and the mature post-charter variant 10, each once. |
| `111_action_agoge_intake` | Train contemporary adults through actual manpower and equipment consumption | Basic cohort is 500 adults, 500 rifles, 25 support equipment and 25 PP. Advanced tiers are 1,000 and 2,000 people with proportional materials. |
| `111_action_convert_returnees` | Convert a selected surviving ancient cohort once, conserving actual people and equipment | 25 PP, 20 CP, matching modern rifles and support equipment. Existing surviving manpower is reused rather than charged again. |
| `111_action_industrial_project` | Complete one actual workshop, arsenal, transport, port, airfield or institutional project | 50 PP, real industrial commitment and at most the specifically justified material type. No abstract factory-point currency. |
| `111_action_armament_contract` | Obtain a real supplier's equipment with consent, debit, compensation and delivery | 25 PP plus industrial terms. Early batch anchor 500 basic rifles, bounded by actual stock and route conditions. |
| `111_action_select_objective` | Select and display one eligible current target | Free selection, no automatic claims, rewards or route commitment. |
| `111_action_diplomatic_offer` | Propose exact league, union, client, access, coastal-charter or limited-settlement terms | Normally 25 PP preparation cost. Remaining terms and all affected human consent are explicit. |
| `111_action_campaign_preparation` | Complete real staging, transport, depot, passage or exercise objectives | 50 PP, 30 CP, one logistics-equipment type and one industrial commitment. Only the disclosed target set receives its mandate. |
| `111_action_postwar_settlement` | Establish one valid regional administration or basin service, including a contextual charter-repair variant | 50 PP, one civilian factory for 90 days and any one justified supply-equipment type. First regional civic gains are capped and deduplicated. |
| `111_action_regional_integration` | Deliver accepted rights and native administration or recruitment benefits | 100 PP and one civilian factory for 180 days. Core scope is Laconia and eligible Greek-homeland states only. |
| `111_action_proclaim_route` | Verify and commit the selected route's enduring charter | 100 PP, all required administered geography, current civic/military gates and the required 90-day persistence. |

Keep the three spirit slots as polity, military institution and state capacity. A decision that changes a spirit replaces its current stage. A timed country modifier cannot become a hidden fourth spirit. Use genuine state, unit, character, equipment or institutional consumers for their accepted specific effects.

### Renewable cadre quota and finite attribution

Implement Part 4's exact quota. `O` is actual Spartan-owned deployed ordinary-native land manpower, excluding returned-host and modern-cadre personnel, mythical bodies and liaison staff, foreign-owned expeditionaries, garrisons, queues and the unassigned pool. The academy tier `p` is 0.10, 0.20 or 0.25, and `Q = max(2000, floor(p*O/(1-p)))`. Let `M` be actual cadre manpower, `E` certified surviving original-returnee attribution in those cadres and `P` all committed contemporary intake or replacement not yet in `M`. Every proposed recruitment or refill must leave `M - E + P <= Q`.

Contemporary recruits and replacements always count against the renewable quota. Original conversion and proven reorganization move existing attribution once, without increasing the founding allowance. Gross casualty evidence reduces `E`. Where mixed casualties cannot identify people, consume original attribution first using `E_i_after = max(0, E_i_before - L_i)`, capped by actual remaining strength, with each gross loss receipt consumed once. Replenishment never raises `E_i`, and net strength polling cannot prove conservation when loss and refill may cancel.

Prove native support for every automatic reinforcement route and safe gross-loss/admission accounting, or a supported method to prevent automatic refill and admit only through conserved quota-checked transactions. No invented casualty-identity or reinforcement API is accepted. Missing safe support blocks enablement of the affected consumer. If `Q` falls below existing non-exempt cadre strength, keep living troops, freeze further admission/refill and reconcile unused pending reservations through actual receipts. Never delete formations to satisfy the equation or refill an inherited excess with contemporary people outside quota.

The adaptation and civic source register must distinguish first founding work, constitutional ratification, mature compact, first civic intake, curriculum tiers, first conversion, support services, exercises and regional settlements. The early firearms familiarization outcome grants 5 Military Adaptation below 25 with a safe site, actual liaison instructors and 100 real rifles. Together with the 10-point liaison stage, it closes the weak opening's path from 10 to 25.

The mature compact grants 10 Civic Settlement once after a valid route charter and 180 days of fulfilled duties. The existing regional pool is capped at 25 and includes the five optional Greek civic-service districts in Part 4, deduplicated against already credited district sources. Listed ordinary sources can reach 95 Civic Settlement from weak/normal and 90 from severe/late. The Western Campaign's four required administration groups alone support 90 or 85 respectively after the mature compact. Preserve the source records and the earned civic ceiling. Paid repair of a real recorded breach can restore only documented lost points up to that ceiling. New legitimate institutional credits raise the ceiling despite an older unresolved loss. Repeatable emergency recovery cannot generate a new high score. A changed template, released country, replacement port or renamed partner cannot create another first-completion source.

## 3. Ordinary missions: complete coverage

| Mission consumer | Objective and default deadline | Required failure distinction |
|---|---|---|
| `111_mission_home_supply` | Actual home intervention plus its observation condition, 90 days | Failed provisioning versus authority lost at the selected site. |
| `111_mission_civic_settlement` | Fulfil the promised institutional and citizenship terms, 120 days | Broken promise, negotiated revision or country loss. |
| `111_mission_agoge_training` | Complete a funded adult cohort, 180 days | Partial real graduates, unused resources and unearned full-stage reward. |
| `111_mission_returnee_conversion` | Complete the local 35-day training of surviving selected people, 90-day deadline | Destruction, stale unit, unsafe site or voluntary cancellation, with no invented survivors. |
| `111_mission_industrial_delivery` | Real construction or delivery, 180 days or 365 for major works | Sunk work, actual delivered material and remaining reservations are separate. |
| `111_mission_campaign_preparation` | Staging and supply objective, 180 days or 270 for distant operations | Failed operation versus loss of legal access. Old incompatible preparation cannot survive a revision. |
| `111_mission_regional_settlement` | Administration or basin service and final observation, 180 or 270 days | Valid reconstruction can remain without granting a full region receipt. |
| `111_mission_charter_repair` | Restore one specified broken contribution, 180 days | Unresolved loss leaves its benefits suspended and permits only declared alternatives. |

Success checks precede timeout on the same tick, and completed objectives resolve without another paid click. Setup must have succeeded before any outcome can pay. Native timeout and helper display use one authoritative due date. `days_remove` or its current native equivalent is an effect lifetime, not an assumed mission deadline. Extensions update every deadline consumer once.

## 4. Mythic actions MY01–MY14

Use the exact roster: Castor and Polydeuces as separate manifested mythic characters, earthborn Spartoi, unique Talos and short-range Stymphalian birds. There is no additional sea-creature family or unnamed replacement hero. The first material proof is fixed to the Dioscuri, following the Laconian investigation and actual service.

| Consumer | Required operation | Anchor cost, duration and conservation |
|---|---|---|
| `MY01` | Investigate the Laconian manifestation | 35 PP, 25 support equipment, 35 days with damaged-supply extension up to 60. Lost control pauses up to 30 days, then cancels consumed and unused work correctly. Retry delay 90 days. |
| `MY02` | Accept or renew one heroic service | 20 PP, 15 CP, 120-day term. Revalidate the selected actual character and assignment conflicts before debit. |
| `MY03` | Secure custody at a real foreign site | 40 PP and 90-day negotiation window. No fabricated treaty, automatic consent or automatic war after refusal. |
| `MY04` | Prepare the Theban manifestation area | 75 PP, 100 support equipment, one civilian factory for 120 days. Produces a supplied custody site and permission for the first company. |
| `MY05` | Raise or replenish an allowed earthborn company | 35 PP, 20 CP, 50 support equipment, 60 days. Exact being and human-support receipt, live cap and access recheck. |
| `MY06` | Restore the Cretan guardian | 100 PP, 200 support equipment, two civilian factories for 180 days. One unique body, same identity through repair or loss. |
| `MY07` | Recover or legally relocate Talos | 50 PP, 30 CP, 100 support equipment, 90 to 180 days. Safe withdrawal and valid paid transport, no teleportation or duplicate destination entity. |
| `MY08` | Establish the controlled Arcadian flock | 75 PP, 40 CP, 150 support equipment, 150 days. Legal native air-wing size and the approved small total combat effect. |
| `MY09` | Use one bounded mythic overdrive | 30 CP and the separate +8 Strain consequence, 30-day effect. Shared cooldown 90 days or 120 while stressed. Supported scoped consumer only. |
| `MY10` | Stand down a service | No cost. Immediate safe withdrawal or verified native completion delay during combat. No destroyed ordinary army and no erased unique identity. |
| `MY11` | Restore a warned custody obligation | 40 PP, 75 support equipment, one civilian factory for 90 days. Resolve that actual breach, up to 15 Strain reduction, 120-day cooldown. |
| `MY12` | Settle an actual rupture | 60 PP, 30 CP, 100 support equipment, 180 to 240 days. Stricter rebinding, permanent release or a recorded lost capability. |
| `MY13` | Permanently release military manifestations | 75 PP and a 180-day aftercare receipt after safe release. Preserve ordinary country, technology, route and human institutions. |
| `MY14` | Establish one final mythic constitution | 100 PP, 60 CP and 180-day institutional settlement. Recheck completed ordinary route, the actual twins, stable custody, values and the branch's Chaos condition. |

Activation requires Chaos at least 600, enabled evolution, independent non-capitulated Sparta owning and controlling Laconia, Civic Settlement at least 30, Military Adaptation at least 35 and no incompatible prior activation or seal. Activation itself gives zero Chaos. A high-Chaos opening uses the same later investigation after its ordinary founding and institutional gates, with no duplicate package.

Apply Part 5's actual duration scaling, recovery margins, cooldown changes and cost modifiers through a final quote. Where that scaling applies, strong valid preparation can reduce an undertaking to 75% of its anchor and poor valid conditions can extend it to 150%. Preserve explicit exceptions, including MY01's investigation limits and EX03's fixed 180-day durability episode. Invalid conditions disable the action. Do not display a rounded duration or equipment amount that differs from execution.

Before the final constitution, only one twin supplies active field-command or national training service at a time. Tournament, rescue, recovery, command, training and sovereign office consume the actual character's availability. Assignment cooldown is 30 days, 21 under mature service and 45 after rupture. Term expiry safely removes only that service. It cannot create a fresh hero.

Sacred dyarchy makes Castor the single visible leader representing joint kingship and removes his free field-command role. Polydeuces has his real second sovereign and senior-office consumer, with explicit release from incompatible duties before command or tournament participation. Mortal custodianship and a mortal divine mandate preserve the mortal institutional leader. Their caps and ongoing costs follow Part 5, and none creates a sixth route.

Interim military caps are four Spartoi companies, one Talos and one bird wing, further limited by actual sites and liaison capacity. Mortal custodianship lowers Spartoi to three companies. The coercive mandate can reach six companies and two wings only after its additional institutions and supplied site exist. These are single event-wide allowances, never fresh allowances for each recipient. The owner ledger counts active consumers, pending paid reservations and surviving equipment held for redeployment or recovery across all authorized owners. A verified transfer moves the same count and receipt. Constitutional cap reduction requires safe release of excess before completion, including stored survivors.

General Event 019 foreign draws are ineligible for mythic families. Any deliberately authored derivative must retain its Event 111 origin, real recipient custody or registered-site access, trained human support, actual paid manifestation and the same global count. Missing provenance or safe transfer/cleanup support rejects that consumer. Talos remains globally unique. Impossible combatants cannot be disbanded into ordinary human manpower. Human liaison staff use real population and exact conservation.

### Warning episodes and actual mitigation

Entering Strain 75 to 89 with a real exposed service starts one named-site episode due exactly 90 days later. Preserve its site, material cause, original date and outcome receipt through value changes, ownership changes, reload and assignment toggles. An inactive family in lawful supplied custody is not exposed. A dangerous unresolved binding remains exposed even if its nominal service was switched off.

MY11 displays its actual scaled completion date alongside that original warning deadline. Its paid project never extends the warning. If the repair will finish late, state that clearly and identify feasible MY10 withdrawal. MY10 neutralizes exposure only after actual safe service termination and lawful supplied custody or valid permanent release. A request during combat does not stop the clock. Repair must fulfil the named obligation and reduce Strain below 75 to neutralize exposure.

A neutralized episode becomes dormant with its original history. The service cannot resume until the material breach is repaired or lawfully released, every related entity has a valid disposition and Strain remains below 50 for 30 continuous days. Toggling cannot reset that recovery. At the original due date, unresolved exposure sets Strain to at least 90 and causes one actual targeted rupture before any Chaos award. Direct Strain of 90 or more resolves the same real-exposure rule immediately. Without an exposed entity, block resumption and allow safe recovery, with no invented damage or award.

## 5. Outside containment EX01–EX03

| Consumer | Eligible acting country and operation | Cost and duration |
|---|---|---|
| `EX01` | Actual controller of an exposed site, hostile to its current coercive use, secures it and denies replacement | 40 PP, 50 support equipment, 120 days. |
| `EX02` | Actual war participant controlling the relevant site while that Spartan power is defeated or withdrawn, dismantles its binding | 60 PP, 100 support equipment, 180 days. Exact permanent service closure and survivor/entity disposition. |
| `EX03` | Actual peace participant or recognized custodian after defeat of Sparta with a prior `C111_TRANSREGIONAL` or `C111_ROUTE_ORDER` receipt and actual `C111_DIVINE_SOVEREIGNTY` or `C111_COERCIVE_MANDATE` use | 75 PP and one civilian factory for the fixed 180-day durability episode. The settlement must actually remove the qualifying mythic sovereignty or coercive institution. |

Authority belongs to the real actor at commitment and throughout its operation. Outside actions do not seize an ally's land, override human consent, transfer a free creature or reset a shared worldwide threat aggregate. A target changing owner or controller has an explicit pause, continuation or cancellation result from its receipt.

EX03, `C111_MAJOR_CONTAINMENT`, ACH20 and the conditional international-defeat presentation consume the same fixed 180-day durability episode. It starts only when authenticated removal of the qualifying power, accepted settlement authority and the paid EX03 commitment coexist. The industrial reservation supports that same period. Technical project scaling cannot shorten it, and no second automatic 180-day wait follows it. A material breach invalidates the episode, with exact payment and site treatment. A later valid attempt cannot reuse a failed period as successful time.

The shared episode uses Part 6's qualifying-opponent and actual-removal predicate. ACH20 additionally requires the claimant's real hostile-war participation for at least 90 days and contribution of control of Laconia or a registered manifestation site to the settlement. Sacred-sovereignty eligibility does not assert that every sacred government exercised coercion. Credit follows the authenticated acting country and contribution, never a copied victory flag. The containment Chaos band is -15 after a completed route or -10 otherwise, paying only the remaining difference if local dissolution already reduced Chaos.

## 6. Shared mission slots and independent timers

Enforce three concurrent player-accepted Event 111 work undertakings per acting country across all its event categories. Sparta's ordinary and mythic projects share one budget. At most two are territorial/industrial and at most one is intake/conversion. An outsider has its own equivalent budget, so Sparta cannot prevent EX01–EX03 by filling its queue.

Classify MY01, MY03 and MY14 as general undertakings. Classify MY04, MY06, MY07, MY11 and MY12 as territorial/industrial. Classify MY05 and MY08 as intake/conversion alongside the ordinary Agoge. EX01–EX03 count as territorial/industrial for their actual actor while material work is underway. In particular, EX03's paid 180-day industrial reservation occupies one territorial/industrial work slot while material work remains. Its shared durability record adds no second slot.

MY02's service term, MY09's effect duration and cooldown, MY10's safe-removal wait and MY13's completed release aftercare have separate durable due-date receipts. They are not extra ongoing paid projects. The same applies to pure 90-day regional, partner and final-charter holding-period records, 180-day sealing or containment durability records and achievement observations. A timer's independence does not exempt its associated paid material work from the undertaking budget. Unavoidable Strain warnings remain visible independent conditions of the registered custody state until a paid repair is selected. MY10 stays freely available with every project slot occupied. Starting MY12 may require pausing or canceling an existing undertaking with exact consumed-resource and completed-work treatment. A full queue must never prevent mitigation or enemy containment. This rule cannot conceal a fourth active construction or manifestation undertaking.

## 7. Geographic truth and postwar operation

Use one versioned region registry and one authoritative eligibility evaluator for action, focus, puzzle, map tooltip, charter and achievement. The six principal final predicates are `111_set_hegemony_final`, `111_set_alexander_final`, `111_set_thermopylae_south_final`, `111_set_thermopylae_north_final`, `111_set_west_final` and `111_set_colonies_final`. The optional `111_set_alexander_eastern_extension` is separate from principal Alexander completion.

Resolve every role against the installed state map after the mandatory Laconia split. Preserve complete connected alternative corridors. The colonial route requires nine selected anchors across five basins, with exact alternative rules and no double-counted state. Its commonwealth model requires direct holdings in three different basins including the Aegean, with real qualifying coastal partners for remaining contributions.

Generic faction membership, docking rights or military access do not prove ownership, control, a regional client or a commonwealth charter. A current partner must own and control its required contribution and meet the accepted terms. Its loss invalidates live map qualification. An expired lease or broken strait-access condition cannot remain green.

Complete the relevant regional administrations before final proclamation. Territories and treaty contributions must remain valid for the prescribed 90 days after settlement. Record historical completion once, suspend live dependent benefits after loss, and restore only the effects whose actual conditions recover. Do not grant another Chaos milestone, achievement or formable merely for reconquest or scene playback.

Core eligibility is closed. This package permits its Laconian founding core and eligible Greek-homeland cores after the explicit civic integration conditions. Extra-Greek territory uses ordinary administration, occupation, legal recruitment and real clients. Do not invent an extra-Greek core list.

## 8. Cost, receipt and UI requirements

Use the shared universal-cost framework and its supported owner adapters. A quote is not a payment or reservation. Revalidate it before a single committed debit. All resource comparisons are inclusive and exact. Preserve fractional quotes where modifiers create them. Implement base, blocked and tooltip cost surfaces from the same component, with at most three inline values and at most four spendable types overall. Command power never exceeds 60. Strain is a disclosed consequence, not an invented spendable currency.

Every receipt contains actor, target, authority, route, set revision, selected unit or site, original and final quote, actual component debits, reservations, objective and native due dates, setup success, outcome and refund state. Keep tombstones or equivalent consumed markers so callbacks and reload cannot pay twice. Return only unused surviving components to their exact owner, and acknowledge owner-adapter completion once. Delivered goods, destroyed troops and sunk construction do not become refundable deposits.

Use the four ordinary categories from Part 4 and the approved mythic category consumers from Part 7. Keep roughly six primary visible actions per category, contextual targeting and the shared mission budget. Display only Civic Settlement, Military Adaptation and active Mythic Strain. The campaign category contains one compact exact-shape puzzle and no static category picture beside it. Ordinary categories can use their permitted simple pictures.

State pieces, counters, icons and tooltips use their actual consumers. Render the active route with lost territory, a valid partner, a broken treaty, missing nonterritorial gates and ready proclamation. Required state geometry comes from the installed map, not generated artwork. Build the asset manifest from every instantiated decision and mission, not just the twelve parent family names.

## 9. AI, audit and completion evidence

Use route-aware willingness and target scores. Prioritize home supply, rifles, civic viability, renewable recruitment and finishing feasible paid work. Evaluate all legal AI targets even when the human UI shows a selected subset. Respect actual seller needs, treaty refusal, force balance, access and industrial commitments. Scores are not probabilities. Report percentages only from a complete named pool evaluated through the actual probability tooling.

Run the applicable reference, syntax, cost, decision/mission, scope, GUI, probability and runtime checks supported by the installed project. Record exact tool calls, covered scenarios, artifacts and remaining engine limitations. Where a required MCP or game environment is unavailable, report that boundary and leave its acceptance gate pending. Do not claim that a generated test, source inspection or focused helper trace proves native execution.

The bounded decision/mission auditor checks costs, real objectives, target sets, timing, outcomes, clutter, route interactions and cleanup. The probability auditor remains read-only and checks complete choice pools. Focus and country auditors keep their local boundaries. Asset and localisation workers own their respective final consumers. None may silently replace the accepted architecture to make a test easier.

Verify at least these concrete cases:

- Exactly affordable and one-unit-short resources, fractional quote changes, duplicate confirmation and repeated refunds.
- Safe cancellation, timeout, same-tick success, extended deadline, actor loss, target disappearance and owner/controller change.
- A nearly destroyed returned formation, an already converted cohort, captured or disbanded ancient equipment, and lawful modern replacements.
- A real seller with insufficient stock, blocked delivery, changed treaty and no-DLC contract fallback.
- Each principal route's full and incomplete geography, both Thermopylae corridors, both colonial sovereignty models and the optional eastern extension.
- Three occupied project slots, shared human/myth intake cap and an outsider undertaking while Sparta's queue is full.
- Both twins assigned, a tournament conflict, Castor as sovereign, Talos relocation or capture, illegal wing size and a family-cap breach.
- Disabled evolution, eligible high-Chaos birth followed by later activation callbacks, permanent seal, warning, rupture, recovery and external containment.
- Historical completion retained after loss, live benefits suspended, independent holding timers and no repeated milestone payout.

Deliver a complete consumer and operation crosswalk, changed files, meaningful validation evidence, known blocked native operations and any narrowly necessary unresolved decision. A successful bounded implementation means every accepted ordinary and mythic action has a real player-visible consequence and a conserved state transition. It does not by itself authorize a catalog promotion or prove that unrelated event systems are complete.
