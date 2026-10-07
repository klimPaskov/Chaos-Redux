# Occupation revolt: lifecycle, invariants and acceptance

## A persistent national episode

Separate a national occupation episode from an active Event 095 incident.
The occupation episode owns the authentic homeland profile, the original cache issue, surviving history and anti-farming record.
An incident owns the current selection, preparation, armed opening, operations, evolving capabilities and settlement.
Several defeated incidents can belong to the same occupation episode.
A new incident does not reset the episode's previously spent resources or one-shot rewards.

Each incident has a stable identifier and a generation number.
Every delayed operation points to that identifier and the exact claimant and target it was created for.
A reusable list position is not an identity.
A country or state reference that has become invalid cannot be silently replaced with whichever country or state now occupies a previous selection slot.

## The state transitions

Selection can lead to prepared opening, dormant preparation or no valid firing.
Preparation can lead to armed opening, negotiated closure, dispersal, overtaken-by-restoration closure or failure.
Armed opening can lead to sustained restoration, a settlement or military defeat.
Sustained restoration can continue through ordinary warfare, open additional prepared regions, achieve a full or partial settlement, or lose its territorial base.
Settlement can lead to recovery and normal national play, or to a specifically recorded breach while the relevant obligations remain active.
Defeat can preserve a dormant survivor record and later permit a newly qualified incident.

Every transition records what actually happened before presenting a completed outcome.
An event report, mission expiry or evolution unlock cannot create a second copy of the opening transaction.
A failed preflight does not spend the event's outcome rewards, create a news item or masquerade as a successful revolt.
The shared event selector and log must be integrated so a real claimant can be prepared before the root's actor-dependent entry is recorded.

## Local organization and opening gates

Local organization is an internal 0–100 assessment with four display bands.
Values below 25 are unsupported, 25–49 are organizing, 50–74 are prepared, and 75–100 are ready to join.
Initial organization uses the actual network evidence described in Parts 02 and 03.
The starting band is documented per candidate source and cannot be inferred from national population alone.
Readiness is national coordination and is distinct from these hidden local organization values.

A seed for a primary displaced claimant must reach local organization 50 and be capable of funding at least one approved useful baseline formation with actual manpower and enough compatible equipment for its supported initial deployment standard.
A dormant movement normally requires Readiness 50, local organization 50 in its seed and a settled provisional command before opening.
The deployment standard must be verified against installed unit definitions and cannot be reduced to a token unusable formation to force eligibility.
The entire locally funded opening may consist of a single formation for a genuinely small country.
This is a feasibility minimum, not a universal army size.

A voluntary additional-state breakaway normally requires local organization 75, national Cohesion at least 25 and the supply and local-control conditions in Part 06.
Combat can still liberate a state whose underground organization is lower.
The event must not prevent ordinary conquest because a custom preparation score is insufficient.
An additional disconnected center also needs the Evolution II capability or an already established supported national military presence.

Strong occupation control means that supplied hostile field forces or functioning local security can decisively contest the proposed opening.
Weak control means that the actual local military and administrative commitment cannot reliably contain the prepared movement.
Collapse means a real loss of command or administrative ability, not merely a low abstract score.
Implementation must use a verified comparable measure of local forces, supply and garrison fulfillment, with compliance and current resistance as supporting evidence.
An unavailable field or unknown local-force measure cannot be substituted with zero control.
The exact engine adapter for this assessment is an open verification task, while the gameplay distinction and required facts are fixed here.

## Transaction invariants

A resource reservation, debit and delivery have different meanings.
Only a confirmed debit reduces the resource owner.
Only a confirmed arrival increases the recipient's usable material.
A refunded amount cannot exceed what was actually paid and remained eligible for refund.
Captured, destroyed, delivered and returned shipment amounts reconcile to the actual departure.
A source helper that merely requests a debit or mutates a temporary variable does not prove the amount paid.

Unit creation or transfer must conserve the real manpower and equipment assigned to it.
A returning formation is not both retained abroad and newly spawned at home.
A defection removes the source's actual eligible capacity and creates or transfers only the corresponding recipient capacity through a supported mechanism.
A formation's ordinary losses cannot be healed by reopening its original receipt.
A cache, donor shipment and captured inventory remain distinct sources.

State ownership, state control, civilian population, military manpower and custody are separate domains.
A change in one is not an automatic receipt for changing another.
Civilian transfers use the existing exact movement owner.
Civilian deaths use the actual mortality owner and do not debit people twice.
A restored country's recruitable pool is not a generic relocation of the occupier's civilian population.

## One-shot rewards and repeat history

Use durable receipts for opening caches, first state liberations, government settlements, formation integration, focus payoffs, mission rewards and achievements.
A one-shot reward belongs to the meaningful national episode or real operation that earned it.
Tag recreation, save/load, a focus reload, a changed capital, a new controller or a different UI path does not make that reward available again.

A national government can legitimately lose its homeland again later.
A new occupation episode requires a real restored interval followed by a new qualifying displacement.
For anti-farming purposes, treat an independent restored interval shorter than 180 days as part of the existing episode unless a separately verified major external conquest supplies a genuine new-displacement record.
Use observable owner receipts for farming exclusions rather than trying to infer player intent.
A claimant released by the acting player country or its subject and then reannexed diplomatically, reacquired without a genuine independent hostile war, or cycled through the same controlled political arrangement during the 180-day interval does not receive a fresh grant episode or achievement progress from that transition.
Debug-created transitions are also excluded.
A genuinely independent later conquest uses its actual war and sovereignty receipts, not a claim about whether the player meant to exploit the system.
The military situation can still produce a revolt without awarding exploit-prone progression rewards.

## Recovery completion

An incident can finish when its military outcome is settled and all event-owned active obligations are either fulfilled, explicitly abandoned with their real consequences, or transferred to a supported ordinary national system.
It does not need to remain active forever because a country retains a political claim.
Clear the emergency category, obsolete mission rows, temporary local coordination burdens and unused reservations.
Preserve the country's actual army, government, diplomatic commitments and completed development.

A country with no viable territory and no surviving active organization closes the armed incident.
An exile or underground history record can remain without occupying a permanent crisis slot.
A later material change re-enters selection through normal repeat eligibility rather than keeping invisible active missions running indefinitely.

## Performance and multiplayer

Only active incidents and their tracked home regions receive recurring work.
Selection can inspect the relevant candidate registry when the global event framework requests a candidate.
Local ownership changes, operation completion and meaningful military changes invalidate the affected cached assessment.
Do not add a daily worldwide scan for every possible claimant.
The chosen bounded active-check cadence must reuse the existing project scheduler or obtain explicit approval before adding a new one.

Human target selection is local to the acting country and operation.
It must not overwrite another human's choice or an AI target.
AI evaluates its own eligible targets.
Simultaneous support offers, state transfers and evolution callbacks revalidate their reservations and generation records before committing.
A country's later owner, ideology or controller cannot inherit authority to spend an earlier actor's resources merely through a stale reference.

## Essential acceptance scenarios

A government in exile can return through a limited home base without receiving divisions in every overseas possession.
A living overseas remnant can launch a homeland revolt without creating a second national tag.
An annexed historical country can return with valid identity and a complete playable package.
A dormant claimant prepares before opening and never pays from nonexistent national resources.
No valid claimant produces no invented country or fake successful log.

A homeland divided between occupiers can open against one party at baseline without accidental war against all others.
Evolution II can later coordinate several viable components while preserving one national resource budget.
Evolution III can transfer a genuine eligible local asset without touching unrelated occupation armies.
Evolution IV can prepare several national movements from real success without recursive uncontrolled spawns.
All four capabilities work on active incidents as well as new openings where their conditions apply.

A weak revolt can lose and leave only real survivors.
A later attempt can use those survivors without repeating the first cache or resurrecting dead leaders.
A country can achieve a viable partial restoration and continue normal play.
A major occupier can negotiate a bounded settlement without ending unrelated wars.
Disabled evolutions, absent optional DLC, save/load and multiplayer targeting preserve the baseline restoration promise.

## What remains unproven in this package

This document defines required behavior and proposed tuning.
It is not engine code and does not establish that a particular uninspected native effect supports every transition.
Country activation, exact unit transfer, local-force assessment, war isolation, optional focus integration, native payment semantics and shared hook ownership require implementation evidence.
The supplied source files were fully read, but several transitive installed references were not supplied or read.
No isolated subagent, HOI4 MCP inspection, live playtest, final art production or runtime implementation is claimed.
The accompanying reading report, verification matrix and specialist assignment files preserve those distinctions.
