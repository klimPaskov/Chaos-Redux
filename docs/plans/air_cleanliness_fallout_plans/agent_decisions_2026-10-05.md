# Fallout finishing decisions

Recorded on 2026-10-06 under the user's explicit authority to finish the Fallout workstream and correct weak design under G1–G8.
These are parent decisions within that scope, not approvals inferred from old status labels.
Implemented dispositions below establish source behavior only; the required MCP and live checks remain separately identified.

## F1. Manual launch follows the selected intensity

Disposition: implemented in source.
The shared `trigger_fallout_scenario` wrapper passed Maximum regardless of the slider, although the owned bootstrap already read the selected value.
Its single owned assignment reads `triggerable_scenarios_intensity`; the exact strike set remains unchanged.
The owned entry effect sends local report `chaosx.fallout.905` when no valid admission is possible, and event 900 delegates rejection to that effect instead of suppressing a forced entry with its own trigger.
Reason: the setting must govern the aftermath and a rejected forced order must explain that no weapons were launched.

## F2. Ash-week choices share one closing report

Disposition: implemented in source; native delivery remains unobserved.
Human acknowledgments 64, 68, 72, 76, and 80 are hidden; their existing immediate resolvers, delays, receipts, and history remain intact.
The authenticated apply-once branch saves each component's result before clearing its transient inputs.
The player receives five choice reports and event 82, for six visible popups rather than eleven.
The closure names the appointed office and reports each actual success, partial result, failure, or incomplete course.
The 108 cell and twelve pilot settlement narratives remain reachable when all five orders succeeded; a contested settlement uses neutral context and the actual individual outcomes.
Reason: remove acknowledgment spam without discarding local identity or describing failed orders as successful.

## F3. Winter recovery follows inherited sites

Disposition: implemented in source; thirty bounded production-source cases pass.
The first survival account also consumes regional relief, tunnel-school, rail, dam, refinery, reactor, and furnace outcomes from owned and controlled states.
Twenty-five existing state-memory inputs are recognized, including orderly refinery shutdown.
Each distinct outcome contributes once nationally; holding ten matching states does not multiply it.
Different sites' successes and failures both contribute, and Cohesion receives their net change before one clamp.
All magnitudes are in `fallout_winter_recovery_memory`; event 82 names the applied causes.
This carries stores, fittings, shelter capacity, and surviving skills, and does not recreate buildings destroyed by Fallout.
Reason: preserve the consequences of winter choices without awarding unlimited stores or concealing another site's losses.
The original A20 country-history families retain their existing source contract; broader refugee identity, focus, and migration-allocation consumers remain outside this patch.

## F4. Eligible candidates may have nonpositive scores

Disposition: implemented in source; thirteen production-condition cases pass; probability comparison blocked.
The first eligible row establishes the score baseline even at zero or a negative value.
The existing score, priority, candidate-id, target-id, and partner-index tie order remains intact.
Ordinary reservation, saved-receipt validation, and numerical-row validation accept that score too.
A saved row with no selected candidate still requires score zero.
Reason: fatigue is a ranking input, not an implicit second eligibility test that can reject every otherwise valid story.
No score formula, factor, cooldown, or candidate eligibility predicate was changed.
The auditor's same-scenario MCP comparisons returned `Transport closed`; source-condition tests are not probability evidence.

## F5. Reconstruction delegates have one exact counterpart

Disposition: implemented in source; native callback checks remain required.
A country may participate in one proposal, either as sender or recipient, at a time.
The originating effect carries a regular proposer target into event 22; replies match that target, the stored counterpart, and the current generation.
Refusal keeps the incoming reservation until the sender closes its project.
Cleanup clears only the matching counterpart, and annexation/capitulation closes the exact lost-country pair without a world iterator.
The surviving sender recovers its Recognition deposit once, with a separate lost-government result; stale answers receive a plain local closing notice.
The pair refusal flag receives a literal 365-day duration through `meta_effect`, derived from the existing constant.
Reason: prevent overwritten delegates, wrong-sender answers, orphan reservations, mixed simultaneous results, and ineffective cooldowns.

## F6. Relief needs a majority and deliverable supplies

Disposition: implemented in source; exact native payment and delivery remain live checks.
Caller and recipient retain their automatic yes votes.
Passage requires more than half of the current live members and at least two yes votes.
A three-member treaty can therefore pass with its caller and recipient; two yes votes in a four-member treaty cannot.
Availability requires a prospective peaceful donor with the existing 30-support-equipment pledge; resolution repeats that check among yes voters and retains the four-donor cap.
An unfunded session grants no aid or success memory and imposes no rejection penalty or 180-day recipient lock.
Its caller recovers the saved native 25-PP quote once and may retry after fourteen days.
Invalid cancellation uses the same consumed quote and retry window; funded success and political rejection retain their 120/180-day pacing.
F15 replaces native billing with a charge after admission; a stale start makes no debit.
Reason: a successful relief report must represent actual supplies, and resupply must not lock a failed caller out for four months.
The four saved-quote tests execute the production refund body and demonstrate that repeated invocation cannot credit twice.

## F7. An unaffordable inspection response closes its visit

Disposition: implemented in source.
Event 8 ends the paired inspection instead of reopening event 6 indefinitely.
Its owned prose explains the missing equipment and makes no finding against the inspected member.
The inspector's already dispatched travel equipment remains spent, as in the existing visit contract; response equipment is not charged.
Reason: avoid repeating the same report when supplies changed between display and selection.

## F8. Treaty actions follow size and urgency

Disposition: implemented in source; decision-panel visual acceptance remains open.
Small treaties expose the one-donor filter convoy; treaties with the existing four-member sampling quorum expose pooled decontamination.
Sampling is offered when its global work/active/cooldown window is free; seed exchange occupies that policy slot while the grid works or rests, and remains available to smaller treaties.
Phase 4 recipients receive relief votes; Phase 5/6 recipients receive evacuation corridors.
Existing paid projects remain visible through their active receipts and are not cancelled by these presentation gates.
This reduces callable primary families to six per recipient and stage without deleting any family or adding another category.
It does not introduce a target picker or a global cap on project timers; native targeted clones and final panel fit require visual review.
Reason: show the next useful response instead of a flat catalogue of overlapping projects.

## F9. Cost rows show the existing commitments

Disposition: implemented for Cleaning Day, filter convoy, and verification in source; Recognition glyph wiring follows the graphics handoff.
The three legacy projects use native custom-cost rows and per-component ready/blocked selectors for their existing support equipment, convoys, and assigned factories.
Their entry guards and cost selectors share inclusive affordability components, and their original debits remain unchanged.
Outcome tooltips omit duplicate payment amounts and describe the work and cancellation consequences.
Reason: a zero native PP price must not hide substantial equipment and factory commitments.

## F10. Reset restores the default climate presentation

Disposition: implemented in source; GUI render blocked.
`reset_miscellaneous_to_defaults` clears only the owned `air_winter_static_climate_map` flag in one surgical shared-file edit.
The existing monthly visual lifecycle applies the changed weather setting; phase ground and gameplay cues remain as defined by A22.
Reason: Reset All Settings must reset this visual preference too.

## F13. Fallout prose names the actual people, work and consequences

Disposition: source prose cleanup; full visual wrapping remains unobserved.
Literal implementation and bookkeeping language is rewritten in the owned localisation while internal identifiers and dynamic tokens remain stable.
Descriptions name food, medical work, cargo, census papers, routes and public choices directly; short acknowledgments refer to the event instead of asking players to close a bookkeeping object.
Reason: enforce G3 across the full owned text surface, including phrases the previous takeover retained as diegetic bookkeeping.
This changes display wording, not resource amounts, selectors, flags, dates or event effects.
The complete before/after key list and token/value invariance are recorded in the final prose handoff.

## F15. Relief refunds represent an actual charge, and results get time to circulate

Disposition: implemented in source; native fee and timing checks remain required.
The relief vote shows its existing 25-PP price as a native custom-cost row, checks affordability, and charges it once only after successful admission.
The stored refund quote is the amount actually debited by that owned effect; stale admission makes no debit or refund.
Reason: the native Easy Decisions mode bypasses the old engine cost, so recording a nominal native quote could create PP on cancellation.
After a valid vote closes, the secretariat waits fourteen days before admitting any next vote, using one schema-owned constant and a literal timed global flag.
Reason: normal 21-day sessions already outlast the default thirteen-day result report, but Easy Decisions shortens native sessions to one day; the circulation gap protects the existing global result fields and keeps reports sparse.
Existing caller and recipient cooldowns, strict-majority rules, donor payments, payload magnitudes and all AI factors remain unchanged.
The production-source cases cover real charge/refund cycles, repeated calls, and the 24/25/75 PP boundary.

## F16. Relief requirements describe the implemented vote

Disposition: implemented player text, native wrapping remains a live check.
The effect tooltip names a majority of all live members instead of merely more yes than no ballots, so abstentions have their actual effect.
The same government counts once when the caller also receives relief.
The compact explanation states conditional support-equipment payments, the four delivery effects, neutral unfunded refunds, political rejection, and the existing cooldowns without a misleading negative-loss phrase.
Reason: the published-diff review found the old majority wording beside the corrected effect, which could mislead a player choosing abstention.
No vote weight, eligibility, debit, payload or duration changes in this text correction.

## Retained limits

F11, recorded under the same G6 authority: the ordinary named fictional NZL radio coordinator is presented as the grounded institutional Radio Service Board, retaining its internal tokens, trait, role, and gameplay.
The portrait creator found that the generic generated face does not pass the current source-mode gate.
Authentic period radio-staff material supplies an attributed institutional source placeholder; it must not identify an unnamed archive subject as Ruth Calder.
The original generated image is retained as superseded evidence, and a styled final remains explicitly user-owned.

The requested catalogue change remains queued for the catalogue owner; no workbook or exported CSV was edited.
No game or desktop window was opened.
The parent GUI render and event/probability compare routes returned `Transport closed`, while other read-only routes returned partial or stalled results.
The source fixes above do not establish blackout exclusivity, multiplayer host identity, native railway collapse, map placement, queue delivery, or ten-year campaign behavior.
The unfinished country-memory library and character-content targets recorded by the takeover remain explicit content gaps rather than completion claims.
