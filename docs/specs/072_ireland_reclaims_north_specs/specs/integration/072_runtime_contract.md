# Runtime integration contracts

## The settlement proof is first

The normal supported fixture is Ireland attacking Britain for Northern Ireland while Britain can remain at war with another country and lead a faction.
The required result is Irish ownership and control of the North, the end of Event 072 hostilities, and unchanged unrelated hostilities and territory.
The existing event's white_peace call is not sufficient evidence.
The inspected Event 009 triggers exclude faction members, so its implementation cannot be assumed to solve this fixture either.

Before the large tree is implemented, inspect the installed effect documentation and relevant vanilla precedents, then prototype a settlement adapter against the defined relation matrix.
Do not assume that the engine exposes an arbitrary unique war handle that can be removed without consequences.
Do not promise a fully atomic effect transaction if the script engine does not provide one.
Record the actual supported operations, their ordering, their reach into faction members, and the resulting war graph.

Reject a proposed solution that disbands Britain's faction, ends its unrelated wars, transfers unrelated states, forces a peace conference over a much larger conflict, or replaces the opening with an unrequested border-war minigame.
Reject a solution that merely excludes ordinary faction-leading Britain and claims the main event is complete.
The required baseline remains a real war with the stated limited objective.
If an exotic owner/controller or merged-war case cannot be supported safely, fail that candidate before commitment and document the precise boundary.
If the mandatory British fixture cannot be proven, the settlement implementation remains blocked.
The design is not silently weakened.

## Logical lifecycle

| State | Entry condition | Allowed progress | Exit |
| --- | --- | --- | --- |
| Dormant | Event unconsumed | Candidate evaluation | Selected or unchanged |
| Selected | Valid actors and snapshot prepared | Final eligibility, supported settlement and grant preparation | Committed or unconsumed cancellation |
| Active | Force and legal declaration committed once | Northern mission, preparations, possible extension, timed Evolution increment | Securing, settling, or failure |
| Securing | Complete Irish northern control | Five-day continuous hold | Active on loss or settling on completed hold |
| Settling | Objective proof and live relation recheck | Adapter execution and postcondition checks | Success or explicit unresolved resolution |
| Success | Northern owner/control and limited peace postconditions hold | Tree load once, national campaign | Permanent success, with later ordinary territorial setbacks |
| Failure | Definitive unsuccessful outcome | Cleanup and ordinary subsequent play | Permanent failure |

Use one state authority and one permanent outcome authority.
An event callback cannot infer success from present northern control alone after failure.
A branch flag cannot substitute for the permanent successful provenance.
Save/load preserves the lifecycle, target identities, grant ledger, objective timer, offer commitments, source guards, and once-only presentation guards.

## Actor and target ownership

Use explicitly recorded Ireland, northern owner, northern controller, primary opponent, and the relevant settlement participants.
Do not depend on a fragile FROM chain several events after the initial dispatch.
Keep persistent gameplay targets out of scripted GUI contexts that cannot support them.
The GUI uses the approved state-entry and country context with live helpers.

Every temporary field has an owner and a cleanup transition.
War targeting belongs to the active attempt.
Opening-grant entitlement belongs to the committed campaign instance.
Foreign offers belong to the specific contract and counterpart.
Factory reservations belong to the active project.
Custom Chaos guards and permanent success/failure belong to campaign history.
Cleanup removes only fields owned by this event and never clears a shared protection owned by another system.

## Idempotent effects

The opening grant has a cumulative delivered ledger.
The tree load, northern transfer acknowledgment, formation identity, achievement award, and each major news or super-event have separate once-only guards.
An effect that already committed must be safe when a delayed callback arrives again.
A callback carrying an old instance or target is rejected.

Offer payment uses a frozen accepted quote and final revalidation.
The same action's eligibility, tooltip, AI helper, and payment read the same quoted values.
An exact-cost stockpile passes affordability.
No reward is executed between a failed affordability check and a later successful callback without a new explicit commit.

An implementation should prefer simple ordering that minimizes compensating actions.
Where compensation is required, record actual performed effects and compensate only those.
Do not subtract an entire intended package after only half its effects succeeded.
A local Python model of these states can test design invariants, but it cannot prove the HOI4 engine behavior.

## Focus and identity loading

The installed focus-loading effect must be checked for active focus progress, historical completions, continuous focuses, AI selection, and save compatibility.
Choose the tested transition policy described in the architecture file.
Preserve actual existing country content not intentionally superseded by the new tree.
The new tree's eligibility requires the permanent success marker.
Every alternate country identity and cosmetic route uses that same condition.

Country names, flag variants, focus ownership, event-detail text, and achievements must agree after government changes.
An empire route is compatible with more than one constitutional form.
Do not invent a ruler or use a monarchy-only title for a government that remains a republic.
The federal bloc preserves individual country tags and focus trees.

## Technology and equipment

Read installed definitions for every granted technology, unit, support company, doctrine bonus, aircraft role, and ship family.
Use the provided technology inspection, rendering, and comparison tools before and after changing grants, prerequisites, research bonuses, or doctrine interactions.
No new technology graph is required solely for Gaelic flavor.
The package primarily grants verified existing capabilities and coherent research opportunities.

Where a DLC provides designers, licenses, markets, intelligence, or another optional interface, provide equivalent baseline behavior with supported generic equipment and actions.
Do not leave the opening force without a producible equipment family because a DLC is missing.
Do not grant designers, characters, or unlocks from a DLC that is absent.
The exact compatibility matrix belongs in the implementation evidence.

## Performance and bounded work

Only active Ireland and the finite related participants enter the event-owned lifecycle evaluation.
The continuous northern hold may require a bounded active-country daily check.
It must stop immediately after success, failure, or invalidation.
All project, treaty, and territorial work uses finite recorded sets and relevant callbacks or supported mission completion.
No new whole-world daily, weekly, or monthly iterator is authorized.

The formable GUI uses live bounded qualification and must not cache stale owners or readiness.
No runtime-created state texture, arbitrary new GUI node, or generated map geometry is promised.
The finite consumer superset is expanded only through a reviewed build.
