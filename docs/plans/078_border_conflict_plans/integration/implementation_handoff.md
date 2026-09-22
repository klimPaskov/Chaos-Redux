# Implementation handoff

## First milestone: native feasibility

Build an isolated test fixture for one country fighting two neighbors simultaneously and another fixture for two independent fronts between the same pair.
Use actual native border battles with automatic state transfer disabled.
Record installed game version, DLC configuration, endpoint states, countries, troop placement, callback delivery, and final ownership.
The essential proof is that both battles are genuinely active and each terminal result can be attributed to exactly its own declared state pair.

Also prove that a participant in an unrelated normal war can enter and resolve its allocated border battle.
Do not reuse a helper's country-wide prohibition on ordinary war or existing border war.
Diplomatic and ownership compatibility must be tested separately from that design requirement.

If ordinary callback scopes cannot carry enough identity, investigate a supported conflict-specific dispatch mechanism with the native tools and installed references.
Any finite dispatch pool must have an evidenced capacity strategy that covers all legal simultaneous fronts and prevents stale slot reuse.
Do not invent an arbitrary five-conflict limit or claim dynamic callback IDs are supported without proof.
Do not apply a generic country callback to every currently active record and hope it selects the right battle.

## Second milestone: complete territorial lifecycle

Implement one declared target, distinct staging state, valid native start, attacking transfer, defensive retention, draw, cancellation, and exact cleanup.
Both sides' callbacks must converge on one terminal result.
The effect of receiving callbacks twice, in reverse order, after save/load, or after another wave starts must be the same single result.

Track enough stable country, state, wave, root, and battle identity to reject stale results.
The design does not prescribe an undocumented native object or storage API.
The architect must choose supported persistence from the current game and repository references and provide evidence for it.
Country summaries and temporary UI selection are not authoritative combat identity.

A state transferred by another system cannot be adopted as an Event 078 capture.
A direct normal war beginning between the pair cancels the dispute without a scripted territorial award.
A foreign occupation or ownership change affects only the invalidated conflicts.
The rest of the wave continues.

## Third milestone: worldwide allocation and repeat behavior

Implement one synchronized discovery and allocation pass per accepted firing.
Canonicalize unordered pairs, apply the baseline opportunity across the whole candidate set, then allocate evolved extra fronts fairly across represented pairs.
Keep state-target selection distinct from staging-state selection so a state with several adjacent enemy states does not receive extra target tickets accidentally.

Reserve incompatible endpoint footprints across waves and across relevant existing native border-war systems.
Reservation updates must not release another event's ownership of an endpoint.
Avoid a global daily scan of all country pairs.
Repeated firings perform the authorized new map scan, while battle results and bounded local reconciliation maintain active records.

Distinguish admitted roots from currently active roots.
Finishing a battle does not refill the same wave's opening quota.
An old wave cannot spend a new wave's budget or move its records under a new history entry.
Preserve deterministic state across multiplayer peers and save/load.

## Fourth milestone: evolutions and consequences

Implement all three evolution profiles, individual toggles, high-Chaos openings, paced active mutations, and one applied-history record per actual mutation.
A continuation starts only after a valid capture creates a new adjacent target against the original opponent.
It must not select a preexisting neighboring state or branch to a third country.
A chain consumes actual army commitments without unit creation or recovery bonuses.

Implement all mapped event-owned Chaos sources, rolling guards, and containment reduction.
Inspect the shared generic adapters for overlap with fighting, casualties, state transfer, and annexation.
A generic consequence already counted elsewhere must not be counted again through a second representation of the same source.
Keep world-tension handling with its existing owner unless the inspected integration explicitly requires an adapter.

Implement the three achievement histories and their hold periods without keeping an otherwise finished wave alive.
A retained target is a defensive result, not a capture receipt.
A debug-forced result never earns campaign progress.

## Fifth milestone: presentation and assets

Implement the native information category, country notices, world news, ordinary history integration, and direction-only writing briefs.
The information category has no purchase actions or paid combat resolution.
Use the actual native state-target and list capabilities supported by the installed consumer.
The owning presentation workers produce final localization and assets only after reviewing the relevant references.

Public information is limited to useful combat and objective state.
One country-wide active-dispute count is sufficient as the primary event value.
Opponent, target, outcome, applied profile, and chain depth are contextual facts for a selected dispute.
Internal identities, random seeds, reservations, receipt generations, and cooldown ledgers are not additional gameplay currencies or headline meters.

## Repository boundaries

The existing entry point is `chaosx.nr78.1` in `events/078_border_war.txt` at the inspected repository revision.
Retain that external entry identity unless the shared catalog registration is intentionally migrated with all consumers.
Use three-digit `078` for new paths and descriptive identifiers where the repository convention expects them.
The existing numeric namespace spelling is an observed compatibility boundary, not a reason to rename all event IDs mechanically.

The inspected old event includes an ordinary-war option, a global opponent variable, nested border-state loops, and automatic state transfer.
Those behaviors cannot remain reachable through the new rework.
Legacy result IDs must not be repurposed to process new concurrent records without an explicit migration rule.

The parent owns shared registries, timer and weight wiring, cluster integration, shared event log and details, evolution framework, shared achievements, and final status changes.
Specialists receive narrow file ownership.
Asset workers do not silently edit gameplay.
Read-only auditors return evidence and do not patch implementation.

The current authoritative runtime helper names, constants consumer, catalog workbook location, and shared UI hooks must be inspected in the actual repository before editing.
This handoff intentionally does not invent their exact paths from older documentation.

## Catalog and cluster treatment

The supplied event export retains the old player-and-random-neighbor description for Event 78.
The supplied cluster export does not yet show this new Wars membership.
The user's current brief is the design authority for the worldwide rework and Wars/Medium assignment.
Medium denotes member severity in this design.
The shared framework's separate participation-role field, if present, must be resolved through the current workbook and cluster schema.

Update the authoritative workbook through the spreadsheet worker when implementation and final wording are ready.
Keep the event name, Minor Repeatable type, Chaos level 1, all three thresholds, and requested cluster assignment consistent.
Do not edit the export-only CSV snapshots by hand.
Use the current export tool to regenerate them from the workbook.
Do not overwrite unrelated rows or change the status to completed before acceptance.

Each worldwide wave consumes one event firing and the appropriate Wars cluster selection accounting.
Extra roots, terminal callbacks, and momentum continuations do not draw another main event or advance the main repeat countdown.
Individual evolution history remains separate from main firing accounting.

## Migration and interruption policy

Inspect whether an existing save can contain old Event 078 delays or native battles at the moment of update.
An old result callback has no authority over a new battle merely because its country is the same.
Where a legacy conflict's exact identity can be proven, finish or cancel that legacy case through an explicit migration path without granting new achievements or new event-specific Chaos.
Where identity cannot be proven, block unsafe reuse and record the affected save limitation.
Do not cancel every border war in the country as a migration shortcut.

A master setting disabled during a battle prevents new starts but preserves the current battle's declared valid settlement.
A disabled evolution prevents subsequent new behavior associated with that evolution.
Hold objectives remain truthful until they complete or fail under the documented policy.
No delayed callback may recreate an event after its owning wave has closed.

## Completion evidence

Provide source changes, inspected native references, exact game version, static checks, multiplayer and save/load fixtures, result traces, probability reports, native-size asset reviews, and supported-resolution UI evidence.
Run the mandatory improvement-loop and completion specialists after the event is near complete and resolve their findings.
Distinguish source inspection, abstract design checks, native prototype results, and actual campaign tests.
The implementation is complete only when the delivered behavior meets the full specification.
