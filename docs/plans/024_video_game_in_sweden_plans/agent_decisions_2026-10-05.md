# Event 024 decisions carried into the 6 October finishing pass

Acceptance basis: the user assigns the complete 024 workstream and its inherited changes to this pass, authorizes repairs to weak design under G6, requires G1 through G8, and explicitly reserves live play for the orchestrator.
The 4 October decision log remains historical implementation evidence.
This file records decisions made under the user's requested filename during the 6 October pass.

## D27. Manual firing refusals use the shared requester report

Disposition: implemented in `video_game_in_sweden_prepare_random_event_fire`.
A refused manual request selects `no_country` when no living Swedish country exists, `unavailable` for a living but ineligible Sweden, `already_active` for a running cabinet, or `unavailable` after the fire-once opening has been spent.
The existing Settings requester target and per-request guard deliver one report, including a request made by a foreign player, and suppress the dispatcher's subsequent generic report.
Natural selection stays quiet and a running cabinet retains its host and achievements.
The new runtime case tests all three reasons and repeated calls within one request.
No shared Settings source is edited.

## D28. Foreign replies produce one Swedish summary

Disposition: implemented in the owned event and effects files.
The old queue could show the same report for each reply and bypass its cap for human partners.
Each responding country retains its own single policy choice, while Sweden receives one summary after the third answer or at programme closure if fewer replies arrived.
The summary copies the five outcome counts before dispatch so a late answer cannot alter an open report.
The summary's queued and pending flags are set before scheduling, and its shown guard is set when it opens.
The report states the received choices in plain text and adds no reward.
The queued latch is a country flag, and the obsolete numeric report counter and configurable repeat cap are removed.
Outcome counts remain actual counts from zero through three, while publication is boolean.
Existing foreign rewards, costs, and the three-recipient limit retain their values.
The runtime cases cover repeated summary requests, stable counts, and an empty round.

## D29. Expired foreign offers cannot grant rewards

Disposition: implemented in all five foreign resolvers.
Each answer checks its still-pending offer, the current Swedish host, the answering country's existence and capitulation, and peace with Sweden before granting consequences or counting a reply.
This closes the gap where an already-open foreign popup could grant Swedish benefits after closure, war, or partner release.
Invalid answers clear only their own pending state and use the existing identity-guarded pointer cleanup.
The previous R4-8 policy allowing released partners to apply their late outcome is superseded by this decision because an expired offer should not grant a second or stale benefit.
The runtime case tests every resolver after release, host loss, and war, with a different newer partner retained.

## D30. The lifetime fixture states its actual dependency boundary

Disposition: implemented in `tests/lifetime/actual_source_lifetime_audit.py`.
The failing ticket assertion treated an archived 024 caller with today's shared helper, trigger, and tuning as a complete historical baseline.
The shared helper's handling of caller-owned load storage changed, so the observed middle value is two tickets rather than four.
The test retains the zero-ticket uninitialized-output check and verifies the fully initialized archived caller against the current caller's two-ticket result.
Its middle case is explicitly an observation under current dependencies, not a historical probability comparison.
The runner accepts `--output` so this pass preserves the previous tracked report and writes separate current evidence.
All six lifetime cases pass without a gameplay or tuning change.

## D31. Incident families remain seen for the whole cabinet

Disposition: implemented in `video_game_in_sweden_roll_incident`.
The previous reset recycled all seen families whenever the currently valid pool was exhausted, so a peaceful baseline could repeat the same counterplan and bootleg prose indefinitely.
The reset call and its unused helper are removed under the explicit G2 instruction and the core specification's rule that rare incidents must not repeat endlessly.
Each of the twelve distinct families retains its existing eligibility, cost, severity, and relative weight when it is first available.
Later phases can open additional unseen families, while an exhausted pool stays quiet.
The pre-edit effects source is preserved with its SHA-256 in `20261006_probability` for the auditor's same-scenario comparison.
Probability-tool discovery succeeded, while the weighted helper inspection was still pending after more than two minutes when the authorized source repair proceeded.
No numerical probability acceptance is inferred from this source review.
The Evolution III opening pool also excludes each already-seen family and checks that the remaining total weight is positive before drawing.
If all four opening families have already appeared, the transition adds no duplicate report.
This is an explicit G2 design change to the earlier guaranteed opening incident, rather than an unreported omission.
The runtime case covers exhaustion of all four opening families.

## D32. Conclusions and audit reports describe what happened

Disposition: implemented in both owned English localisation files after the independent wording audit.
The ordinary conclusion describes retained training and civilian clubs, the officer conclusion describes retiring league rankings, and the commercial aftermath describes municipal games.
The audit reports name missing troops, stores, and independent reviews instead of a field package or recorded loss.
Requirement text explains that an interruption can limit the result even after recovery.
Acknowledgements describe outcomes, and the final-review title describes a decision about the cabinet.
Foreign-licence text describes one summary and the current government's answer, preserving the displayed trade-opinion benefit, term, and civilian-office cost.
Event Details, evolution titles, and catalog detail fields are unchanged.

## D33. Cancelling a follow-up clears its running state

Disposition: implemented by the decision auditor's local cancellation callback and the parent's programme-close cleanup.
The timed follow-up could be cancelled when its host was lost without calling its normal completion effect, leaving its running marker set.
Both paths clear that marker without granting the follow-up reward.
Simple resource payment checks remain visible under the earlier accepted tooltip rule.

## D34. Mission starts reserve the cabinet before native activation

Disposition: implemented in `video_game_in_sweden_no_active_mission` after the independent decision audit.
The old guard checked only native active missions, while each start effect sets its country flag before native activation registers the mission.
The offline Decision modding reference at lines 465 through 479 documents daily activation checks.
The guard checks all four immediate active flags as well as all four native missions, preventing a second same-day action from replacing the first mission after charging both costs.
The idle state stays available, and normal completion and cancellation clear the same active flags.
The pre-edit trigger file and hash are preserved in `20261006_probability` for scenario comparison.
The runtime case checks every reserved flag with all native mission predicates false, then checks the idle state again.
No cost, reward, weight, or duration value is retuned.

## D35. One private predicate owns foreign-offer validity

Disposition: implemented after the bounded scripted-system review.
The five identical guards are extracted into `video_game_in_sweden_can_answer_foreign_offer` in the owned trigger file.
It reads country flags, existence, capitulation, the saved current host, and war status and returns a boolean without side effects.
All five resolver limits call it, and the same valid, repeated, released, closed-host, and wartime reply cases pass against the shared predicate.
The host identity check retains both scope entries: the predicate enters Sweden from the responder, then the current-host trigger enters the saved host from Sweden and compares it with that Swedish PREV.
The frozen `715b572e` effects snapshot remains the exact final weighted-pool source for the incident comparison.
This later extraction changes no weighted-pool code or eligibility and is verified separately by source equivalence and the runtime cases.

## D36. A mission result remains authoritative until it is answered

Disposition: implemented after source review confirmed the delayed-report race.
The no-active-mission predicate also excludes all four pending mission-report flags.
A player therefore cannot start an audit that clears `dual_track_failed` before the queued dual-track report opens, or replace proof and result state before the previous report is acknowledged.
Its single requirement tooltip names both running missions and unanswered result reports.
The source case covers each pending flag with native missions absent.

## D37. Primary and narrow audit reports state their own evidence

Disposition: implemented in the owned event, scripted localisation, and English localisation files.
The narrow reassessment has its own report title and full, partial, and failed descriptions.
Partial and failed narrow tooltips no longer promise another copy of the one-time narrow action.
The primary full description also accommodates the accepted active-front alternative instead of claiming every report came from all three Swedish regions.
The four pending-report guards preserve these result and proof flags through delayed delivery and acknowledgement.
There is no additional event, route, price, reward, or asset.
An independent decision review rejected a suspected Trust-surge leak because the three direct recovery decisions already end the surge and record reassessment before starting their path.
The existing early choices are retained and no duplicate review decision is added.

## Validation limits

The source model executes bounded declared predicates and records scheduled events.
It does not prove native delivery, save persistence, decision presentation, modifier expiry, or achievements.
Current MCP findings, probability coverage, graphics review, inherited-document dispositions, commits, and exact live checks are recorded in `takeover_status_2026-10-06.md`.
