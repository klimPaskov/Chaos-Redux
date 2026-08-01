# Event 016 send-away rejector reaction gap audit

Date: 2026-08-01

Mode: read-only completion audit. No gameplay, localisation, asset, workbook, or catalog files were changed.

## Outcome

The highest-impact bounded content gap is the missing follow-up report for the player country that sends Doctor Warren Kruger away at the opening.

This is a current source gap, not a stale handoff finding. The accepted specification requires the rejecting country to receive a temporary memory flag and a later news or intelligence reaction in `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_1_core.md:164`. Current runtime creates the memory but never consumes it.

## Current evidence

- `events/016_brilliant_scientist.txt:118-132` exposes the human-only send-away option and calls `brilliant_scientist_forward_opening_to_selected_recipient`.
- `common/scripted_effects/016_brilliant_scientist_effects.txt:2690-2724` forwards the opening, marks the rejector with `brilliant_scientist_kruger_redirected`, and sets the timed `brilliant_scientist_rejection_memory` flag.
- `common/script_constants/016_brilliant_scientist_constants.txt:175` gives that memory a 365-day duration.
- A current-source search finds no read, trigger, event, decision, report, or localisation consumer for `brilliant_scientist_rejection_memory`. Its only occurrences are the assignment at `016_brilliant_scientist_effects.txt:2708-2713`.
- The accepting recipient already receives `chaosx.nr16.3`; its localisation names the rejector through `[brilliant_scientist_send_away_rejector.GetNameDef]` in `localisation/english/016_brilliant_scientist_l_english.yml:24-28`. The event chain therefore already carries the exact two actors needed for the missing reverse reaction.
- `chaosx.nr16.12`, `.13`, and `.14` are present in the current event sources. Exact-ID search finds no `chaosx.nr16.15`, so `.15` is presently available for this bounded report.

## Recommended patch

Implement one ordinary, triggered-only rejection follow-up report as `chaosx.nr16.15`.

1. Add the event to `events/016_brilliant_scientist.txt` because it closes the opening referral chain.
2. Schedule it from `brilliant_scientist_appoint_kruger_from_opening` only when the accepting country has `brilliant_scientist_received_initial_referral`, the regular `brilliant_scientist_send_away_rejector` target still exists, and the rejector still has `brilliant_scientist_rejection_memory`.
3. Fire it at `event_target:brilliant_scientist_send_away_rejector` after a short named script-constant delay. Regular event targets explicitly carry through delayed events fired in the same chain, matching the existing referral structure.
4. Use the existing appointment or Directorate dossier report sprite. No new art, route, evolution, reward, project stage, event-log row, or 3D consumer is needed.
5. Give the report public and secret description branches by reading the accepted recipient's current appointment posture. The text should tell the rejecting player what became of the scientist they redirected.
6. Keep the response bounded to acknowledgement and a one-time receipt such as `brilliant_scientist_rejection_reaction_seen`. Do not create a new reclaim, sabotage, or foreign-operation route without a separate design decision.
7. Add the final title, descriptions, option, and any receipt tooltip to `localisation/english/016_brilliant_scientist_l_english.yml`, then update `docs/events/016_brilliant_scientist/overview.md` to record the completed send-away consequence.

## Why this gap is the priority

The send-away branch is the only player-exclusive opening choice, and the accepted design already reserves runtime state for its later consequence. Closing it produces visible campaign memory with a small event-and-localisation patch. It does not overlap the implemented `.12`, `.13`, or `.14` reports and does not require a new route or any excluded asset, model, or live-validation tranche.

## Validation risks

- Verify the regular rejector and recipient event targets survive from `.2` through `.3` into the delayed `.15` report. The offline event-target reference states that regular targets carry through events fired within the chain, including delayed event examples.
- Schedule only after the recipient appointment transaction commits. If `.3` somehow fails to recruit Kruger, the rejector must not receive a false success report.
- Keep the report once-only even if the appointment helper is re-entered. Validate the pending or seen receipt before scheduling and on event trigger.
- Use the initial referral recipient target in text rather than the mutable global current-host target, so a later transfer cannot rewrite who first accepted the referral.
- Confirm `.15` remains collision-free immediately before implementation and run focused event-chain inspection after the patch.

## Accepted-plan disposition and exclusions

The accepted `.12` impossible-lecture, `.13` project-incident, `.14` cross-domain review, KRG focus/AI continuations, and hazardous-mission pressure plan are implemented in current source and are not reopened here. Models, art production, user-owned live validation, quantitative balance, and broader optional flavour are excluded from this tranche.
