# Implementation sequence and acceptance evidence

This package specifies the proposed behavior of Event 069.
It does not contain a gameplay implementation, final assets, a proven country tag, or executed HOI4 validation.
The source-reading and tool-access gaps in `research/source_review.md` must be resolved before the implementation is described as fully source-grounded or complete.

The latest repository instructions take precedence over a stale copy in this package.
Compare the working checkout with the pinned source snapshot recorded in the research notes and re-read changed instructions and affected files.
Do not treat the existence of this specification as proof that every proposed expansion has already been approved or implemented.
Record the explicit user concept, adopted design additions, implementation evidence, and unresolved changes separately.

## Tranche 1: Complete the source and capability review

Read every required core wiki page and applicable skill in full, including the portions not completed in this planning run.
Read the installed vanilla and relevant mod references required by those instructions.
Inspect the current event, its localisation, news, registration, shared helpers, country registry, scenario framework, and the named connected event packages.

Resolve the following capability questions before committing to their implementation: safe limited peace in the actual war graph, theater-limited access and occupation, state or site material allocations, real unit and equipment transfers, scoped ritual effects, country activation and player transfer, safe focus integration, and enforceable treaty payments.
A label or variable that describes an effect is not proof that the game performs it.

Produce a source and capability record with exact paths, current revisions, supported operations, constraints, and remaining blockers.
A failed MCP route must be recorded as a failed route, not replaced by a claim that manual source review is equivalent.

## Tranche 2: Replace the legacy opening and establish the crisis registry

Retain the entry namespace and classification while replacing the hardcoded CHI targeting and legacy civil-war/manpower effects.
Implement target preparation, the reviewed Chinese theater, actor roles, initial centers, the two public values, and the once-only opening transaction.
Use a bounded event-owned scheduler and safe coordinator succession.

At this stage, the event must be able to open, offer coherent Chinese stances, record actual foreign interests, and close a contained crisis without creating a country or declaring a war.
Prove that a failed target search does not consume the source firing.
Do not hide unfinished paths behind false success messages.

## Tranche 3: Build local operations and shared humanitarian integration

Implement the local network states, recruitment and equipment allocations, protection, route disruption, disarmament, and the relevant mission families.
Bind deaths, famine, migration, contamination, and relief to their actual shared owners.

Validate finite stock transfers, manpower ownership, partial evacuation, repair conservation, and one objective per site.
Verify the action cost budget, actual affordability, payment once, cancellation, and AI access.
The normal decision surface must respect the value, action, and mission budgets.

## Tranche 4: Implement foreign commitments and settlements

Build the interest-based response logic, ultimatums, coalition agreement, mandates, contribution records, operations, and withdrawal.
Use real war and access behavior where the capability review proved it.
A political coalition record must not overwrite engine factions or unrelated wars.

Implement the settlement term ledger, capacity-limited reparations, temporary occupation, protection, inspections where supported, and bounded revision or default.
Test mixed outcomes in which one objective ends while another war continues.

## Tranche 5: Activate the country and implement the focus routes

Lock a collision-checked carrier and the reviewed founding map package.
Implement origin-aware activation, actual asset transfers, human-country classification, institutions, research, laws, military setup, and optional player handover.
Preserve meaningful existing-country trees and use the dedicated Boxer tree only on its authorized owner.

Implement B01 through B09, the three political routes, their decisions and missions, the three-slot idea lifecycle, and route-specific AI.
Resolve character identity and portrait ownership before recruiting a named person.
Run the country-package and focus audits against the actual files and graph.

## Tranche 6: Add evolutions and the continuing political game

Implement all three evolutions with enable checks, dynamic timing, valid actors, and complete log records.
Separate baseline stages from evolution state.
Implement the ordinary and anomalous school outcomes, their local consumers, preparation, cooldowns, and failure conditions.

Implement the Chinese pact, safe ceasefire paths where supported, territorial agreements, joint objectives, and the postwar political dispute.
Confirm that disabling an evolution cannot strand baseline progression, delete a country, or leave an infinite active effect.

## Tranche 7: Complete presentation, scenarios, and achievements

Produce the accepted art requirements through the required source or ImageGen route and process them with the current skill-local tools.
Expand focus and other family-level requirements into complete consumer-level manifests before claiming asset coverage.
Use the named portrait, icon, generated-art, source-research, and super-event research roles where the actual runtime supports them.

Complete all super-event image, text, quote, audio, settings, slot, and attribution wiring.
Implement the four scenario types and intensity controls in the shared window.
Implement A01 through A12 only after their actual historical receipts and gameplay conditions exist.

Write final English localisation with context-aware actors, places, obligations, and action results.
Keep working labels and implementation notes out of the player-facing files.

## Tranche 8: Matched audits and closure

Run the event, focus, decision, country, localisation, probability, asset, and completion reviews through their actual supported routes.
The improvement-loop planner should examine the implemented playable loop once a meaningful tranche exists.
It should propose concrete corrections, and the parent should resolve that handoff before requesting another broad expansion pass.

Use the main agent for shared framework wiring and final integration.
Give each worker an explicit file scope, inputs, exclusions, and expected evidence.
Do not let several workers edit the same shared event-log, settings, or registry files without a coordinated ownership plan.
Honor the user's worktree and merge policy and do not remove or merge unrelated work.

Update the authoritative event catalog workbook only when the implementation facts justify its new status.
Run the normal export script after a successful workbook update.
Do not edit exported catalog CSV files directly or mark the event reworked merely because a spec package exists.

Promote durable provenance and completion evidence before cleaning the temporary event asset workspace.
Preserve the separate portrait source archive and all required incomplete-work evidence.
A missing required asset, unverified engine behavior, failed audit, or unimplemented adopted route remains a blocker.

## Expected file ownership

| Surface | Ownership direction |
| --- | --- |
| `events/069_boxer_rebellion.txt` | Parent-owned event chain, stable entry namespace |
| Event-owned decisions, ideas, modifiers, triggers, effects, constants, AI, and on-actions | Separate `069_boxer_rebellion` files under the correct engine folders where supported |
| Shared random selection and log systems | Parent-owned integration in the established shared files |
| Shared scenario and settings surfaces | Parent-owned framework integration, no event worker scope expansion |
| Country carrier, history, characters, and focus tree | Country and focus workers within explicitly granted files, parent reviews activation and shared registration |
| Runtime art | Event-scoped category folders, with root-only flag and achievement exceptions |
| Final audio | Event-scoped sound folder, registered through the existing sound and volume-wrapper framework |
| Final player docs | `docs/events/069_boxer_rebellion/` and the appropriate shared system pages |
| Working plans and audit handoffs | `docs/plans/069_boxer_rebellion_plans/` |
| Source design | `docs/specs/069_boxer_rebellion_specs/` |

The table describes intended ownership and placement.
It does not certify that every proposed destination file already exists.
Inspect existing naming and ownership before creating a new file.

## Acceptance matrix

The following outcomes are required evidence targets, not passed tests.

| Test | Fixture or action | Required result |
| --- | --- | --- |
| T01 | Natural opening in unified China | Correct theater and actual government, with several valid centers and one source record |
| T02 | Natural opening in fragmented China | Separate government stances and no CHI-only assumption |
| T03 | Opening under foreign occupation | Correct owner, controller, local claimant, and foreign interest roles |
| T04 | Stable China with no credible foreign grievance | No fabricated mission, possession, or automatic eight-power coalition |
| T05 | Invalid target search | No half-initialized crisis or consumed fire-once state |
| T06 | Initial support choice | No free arms, fixed fascist split, or five-million-manpower removal |
| T07 | Repeated policy reversal | Commitment period and material ownership remain valid |
| T08 | Empty equipment or manpower | Recruitment cannot create a formation for free |
| T09 | Intercepted donation | One debit and one actual delivery, capture, or loss result |
| T10 | Seized depot and later recapture | Finite stock is conserved and cannot be collected twice |
| T11 | Partial evacuation | Evacuated, remaining, displaced, and killed groups are not duplicated |
| T12 | Railway damage and repair | Only recorded damage is restored and no free extra level appears |
| T13 | Several missions at one site | Shared objective identity prevents duplicate populations and rewards |
| T14 | Three active missions | No invisible fourth deadline |
| T15 | Foreign power without a route | Military expedition is invalid even at maximum Pressure |
| T16 | Hostile foreign factions | No automatic faction merge, common command, or unrelated peace |
| T17 | Intervention layered onto a world war | Event settlement does not terminate the wider war |
| T18 | Limited rescue completed | Withdrawal is available and no new privilege is imposed automatically |
| T19 | Coalition mandate expanded | Every affected member can accept, refuse, or leave |
| T20 | Country activation | Valid capital and land precede dependent setup, with no duplicated armies or stockpiles |
| T21 | Existing meaningful country tree | It is preserved unless a separately authorized transformation applies |
| T22 | Tag or character collision | Activation or recruitment blocks before destructive changes |
| T23 | Three political routes | Distinct institutions, decisions, failures, AI, and late payoffs exist |
| T24 | National-spirit lifecycle | No more than three Event 069 spirits at once, including settlement effects |
| T25 | Each evolution disabled before opening | Baseline progression and its viable alternatives remain complete |
| T26 | Evolution disabled during an operation | No permanent stray effect or deletion of legitimate institutions |
| T27 | Ritual effect | Correct scope, duration, cooldown, supply requirement, and no unauthorized stacking |
| T28 | Chemical or biological exposure | Normal shared protection and consequence rules still apply |
| T29 | Unified-China Evolution III | National institutions coordinate without fake rival-country creation |
| T30 | Postwar Chinese dispute | Actual agreement and territory drive the dispute, not an automatic universal civil war |
| T31 | Treaty payment and capacity loss | Bounded bill, one receipt, real recipient behavior, and usable moratorium or default |
| T32 | Temporary occupation expires | Correct territory and access cleanup without unrelated transfers |
| T33 | Extinct actor or coordinator | Safe succession or closure, no stale payment or target |
| T34 | All sixteen scenario profiles | Correct confirmation, structural gates, finite grants, and cleared launch bypass |
| T35 | Scenario relaunched during a crisis | No duplicate carrier, founding grant, deadline reset, or cleared obligation |
| T36 | Achievement exploit fixtures | No credit from manual setup, fake members, fabricated privileges, or repeated receipts |
| T37 | Event log and details | Accurate actor, stage, evolution, outcome, and toggle state on every relevant view |
| T38 | Normal and crowded presentation | Value, action, mission, tooltip, and native-size art requirements hold |
| T39 | Super-event playback | Correct unique image, quote, final licensed track, audio ID, and settings-aware volume |
| T40 | Cleanup and unrelated terminal condition | No new incompatible incident, leaked allocation, deleted surviving country, or stale scheduled restart |

## Completion report

Report the actual implementation revision, changed files, adopted routes, evidence produced, unresolved findings, and every omitted, renamed, merged, simplified, substituted, or deferred requirement.
Distinguish source inspection, MCP source analysis, rendered visual review, and real game execution.
They are different kinds of evidence.

Do not claim that a named subagent ran because its work was manually imitated.
Do not describe this package's expected results as test results.
The current planning run did not execute any named project subagent or HOI4 MCP tool.
The user owns live game validation under the repository's workflow, and this package does not ask them to run an unperformed agent test in place of the required source and MCP work.
