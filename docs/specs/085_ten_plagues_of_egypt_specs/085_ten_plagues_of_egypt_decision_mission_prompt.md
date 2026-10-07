# Event 085 — Decision and Mission Implementation Prompt

Implement and audit the entire decision and mission surface for Ten Plagues of Egypt.
Read every specification part under `docs/specs/085_ten_plagues_of_egypt_specs/`, with particular attention to Parts 2–7, 10–15, and 18.
Follow `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-scripted-gui`, `chaos-redux-subagents`, and the current local vanilla and offline wiki references.

This is an implementation assignment for the mapped design.
The planning package has no completed runtime decisions or specialist approvals.
Do not treat proposed API names, resource mappings, or tuning values as already verified engine behavior.

## Required gameplay

Create one compact event-owned category with Divine Wrath as its only event-specific mechanic value.
Show the current plague, the next known deadline, useful preparation results, and three to five primary actions, with a hard maximum of six.
Allow at most three urgent Event 085 missions.
Shared Famine, Migration, disease, and Natural Disasters actions remain with their owners.

Implement all sixteen families in Part 14, including their physically valid variants:
Harden Our Hearts; safe water; frog clearance; infestation response; food and sanitation; rural continuity; civilian care; military stand-down; storm shelter; storm evacuation; preservation of remaining harvest; essential service under Darkness; normal Passover; emergency local Passover; foreign relief; and reconstruction coordination.

Use real targets, paid or reserved resources, actual work, and completed objective receipts.
An action that merely sets a success flag after its cost is paid does not satisfy the mission.
Each family needs full success, meaningful partial success, failure, impossible-target handling, AI behavior, deadline behavior, and cleanup.

## Costs and capacity

Use the concrete cost and sacrifice model in Part 14.
No action may have more than four distinct spendable cost types, and preferred variants use one to three.
Inline cost localization displays at most three values with the correct texticons.
Requirements such as access or a valid route are displayed separately and cannot conceal a fifth cost.

The planned 250,000-person relief unit and its road, maritime, and rail alternatives are tuning anchors.
Verify the actual stockpile, cargo, reservation, and return contracts before implementation.
Do not combine every transport mode into one purchase.
Do not translate missing food or capacity APIs into Political Power without approval.

Use the existing stockpile-debit helper contracts.
Initialize each temporary removal amount afresh because the helpers negate their input in place.
Holding exactly the displayed amount must be sufficient.
No partial hidden payment occurs on an unavailable action.

Every essential phase has the real local-organization route.
It commits actual working capacity and has a smaller proven footprint without requiring several civilian factories.
The local capacity reservation is an explicit integration contract to prove or implement, not a cosmetic modifier described as performed labor.
Do not kill population, create manpower, or conjure supplies to imitate the commitment.

## Wrath and objectives

Protective completion earns at most one full credit per phase.
Partial-to-full completion grants only the difference.
Effective foreign deliveries earn at most two separate credits per phase.
Additional genuine work remains useful without generating unlimited Wrath rewards.

Harden Our Hearts preserves only the specified portion of Event 085 production interruption.
It does not restore destroyed buildings or remove another owner's penalties.
A failed route and deliberate diversion are different outcomes and receive different conduct consequences.

Use the 10- and 15-day urgent phase objectives, the five-day storm warning, and the special Darkness schedule as explicit short-emergency exceptions to the normal 90–180-day reconstruction scale.
Do not stretch Passover beyond Darkness to match a generic mission-duration default.

Normal Passover takes 48 hours, the verified working response network allows 36, and emergency local work takes 24.
The global final deadline never moves for a country popup.
Full protection applies only to reached people.
Later arrivals require real prepared reception, not a national immunity flag.

## Shared owners

Do not duplicate Famine reserves or food stages, Migration movements or reception missions, Natural Disasters aftermath actions, or disease treatment ledgers.
Use their positive interfaces and actual result receipts.

The firstborn and Passover metadata extension, peaceful disease adapter, composite Hail and Fire contract, local capacity reservation, and exact cargo mapping remain required proofs.
A missing interface is an explicit blocker to be resolved with its owner.
It is not a reason to substitute a smaller flat national system.

Mission responsibilities, remaining dates, physical work, and reservations must reconcile on release, annexation, occupation, invalid target, and save/load.
Close former pointers and slots without generating false completion rewards.
Retain valid shared aftermath when Event 085 ends.

## Specialist review and evidence

Use `chaosx_decision_mission_auditor` for the mapped action and objective audit.
Use `chaosx_ai_probability_auditor` for actual decision weights and related MTTH behavior, beginning with probability inspection and proceeding through named scenarios, sweeps, and comparisons.
Named roles receive self-contained prompts and `fork_turns="none"` in Codex.

An ordinary compact category does not require a new custom GUI.
If the parent proves a separate event-owned Darkness interface layer is necessary, route only that accepted surface to `chaosx_event_ui_worker`.
Keep costs, gameplay, and AI under their actual owners.

Return changed files, identifiers, action/mission coverage, exact cost and requirement mapping, complete result/cleanup contracts, probability evidence, native consumer evidence where supported, and unresolved blockers.
Cover the corresponding Part 15 cases, including exact-cost affordability, last-hour Passover, failed route, donation loops, controller transfers, and owner cleanup.
Do not claim completion from source formatting or a list of decision IDs.
