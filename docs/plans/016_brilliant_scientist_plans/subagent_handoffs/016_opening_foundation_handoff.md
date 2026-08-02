# Event 016 opening and Kruger identity handoff

> Historical enablement note (2026-08-01): the default-disabled instruction later in this handoff belonged to the opening tranche's pre-core acceptance boundary. Use `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` for current enablement and deferred-content status. This handoff remains evidence for the opening identity contract and does not claim whole-event completion.

## Scope

This tranche replaces the placeholder opening with the minor fire-once Doctor Warren Kruger incident. It implements the fixed character identity, weighted valid-host dispatch, public and secret appointments, one-time player referral, the exact research reward, and event-log actor correction. It does not claim completion of the Directorate, project portfolio, evolutions, foreign operations, containment, Kruger State, focus tree, terminal paths, achievements, or later visual stages.

## Gameplay files

- `common/characters/016_brilliant_scientist_characters.txt`
  - Defines the one fixed token `KRG_warren_kruger`.
  - Uses the registered Stage-0 leader/scientist and advisor portraits.
  - Prevents capture from creating an unintended ownership state.
- `common/country_leader/016_brilliant_scientist_traits.txt`
  - Defines `brilliant_scientist_research_director`.
  - Its `research_speed_factor = constant:brilliant_scientist_identity.advisor_research_speed_factor` resolves to exactly `1.0`.
- `common/scientist_traits/016_brilliant_scientist_traits.txt`
  - Defines `brilliant_scientist_polymath` with extreme project, breakthrough, research, experience, and facility-supply modifiers.
- `common/script_constants/016_brilliant_scientist_constants.txt`
  - Adds `brilliant_scientist_opening_ai` and `brilliant_scientist_opening_duration` tuning.
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
  - Extends automatic availability with a global duplicate-character refusal.
  - Uses the shared final-chaos threshold inclusively for Laboratory World eligibility.
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
  - Adds `brilliant_scientist_appoint_kruger_from_opening`.
  - Adds `brilliant_scientist_forward_opening_to_selected_recipient`.
  - Adds `brilliant_scientist_finalize_pending_prefire_opening`.
  - Includes biowarfare and chemical-warfare facilities in host and referral weights.
  - Makes the active Kruger advisor role non-dismissable.
- `events/016_brilliant_scientist.txt`
  - Keeps `chaosx.nr16.1` as the hidden dispatcher entry.
  - Uses `chaosx.nr16.2` for the first host and `chaosx.nr16.3` for a referred recipient.
  - Gives AI nonzero public and secret weights and no referral route.
- `common/scripted_effects/chaosx_settings_effects.txt`
  - Resolves and dispatches the preserved Event 16 host and evolved-opening context.
- `common/scripted_effects/chaosx_logic_effects.txt`
  - Uses the Event 16 constants and availability trigger in the fire-once pool.
- `common/scripted_effects/chaosx_events_log_effects.txt`
  - Binds the prefire actor, records the opening sequence, and rebinds the row to the final accepting host after a referral.
- `events/_chaosx_news.txt`
  - Removes the old opening `chaosx.news.18`; the minor incident does not create a global headline.
- `common/ideas/016_brilliant_scientist_ideas.txt`
  - Removes the obsolete anonymous `+50%` country idea.

## Appointment transaction

Both visible appointment routes call the same guarded transaction. It refuses an already resolved event, any existing Kruger character, and an active character transaction. On success it recruits `KRG_warren_kruger` once, records nationality and personal state, initializes the selected public or secret Directorate posture, adds one theorist advisor role, and adds one scientist role at level five in nuclear, naval, aeronautics, land warfare, biowarfare, and chemical warfare.

The advisor occupies the engine-supported theorist slot and cannot be fired. The advisor trait is the sole opening `+100%` national research-speed anchor, preventing dismissal/recruitment reward loops. Later movement must use `brilliant_scientist_transfer_kruger_atomically`, whose gate rejects an active-project scientist and whose transaction removes roles before changing nationality and restoring roles in the recipient.

## Referral and chronology

The human-only referral route selects a weighted valid recipient before the option is shown, validates it again before mutation, marks the first host as a permanent rejector, carries the prefire evolution stage and tier, and fires the recipient appointment without recruiting or transferring a character in the rejecting country. The recipient cannot refer Kruger again.

The event history may be written before a human chooses or after an AI resolves. `brilliant_scientist_prefire_opening_pending`, `global.brilliant_scientist_pending_history_sequence`, and the final-host rebind helpers make both orderings converge on one history row whose actor is the final accepting host. Evolved-opening chronology is recorded only after an appointment exists.

## Localisation and presentation

- `localisation/english/016_brilliant_scientist_l_english.yml` names the character, advisor, scientist trait, options, and exact effects without asserting an alien origin.
- `localisation/english/chaosx_ideas_l_english.yml` removes the obsolete anonymous idea text.
- `docs/events/016_brilliant_scientist/overview.md` records the implemented opening and the remaining package work.
- The existing Stage-0 leader/scientist and advisor DDS files remain the native character portraits.
- The opening report-event DDS, sprite registration, and `chaosx.nr16.2`/`.3` picture swap are completed with the dedicated opening-report asset handoff before this tranche is committed.

## Review evidence

- The fixed token has one character definition and one opening recruit path.
- Both public and secret options use the same role transaction and exact `1.0` research-speed constant.
- Six distinct special-project specializations are assigned at level five.
- The old `+50%` idea and opening news event have no remaining references.
- The appointment and referral paths are guarded against duplicate character ownership and repeat resolution.
- The shared Event Chain Viewer was attempted, but its artifact store reported `ARTIFACT_STORAGE_LIMIT`; direct source review remains authoritative for this tranche.

## Remaining integration

- Keep Event 16 default-disabled until the complete package and mapped audits are accepted.
- Wire evolved opening content, four active-chain evolutions, Event Details text, later portrait stages, and severe animations in their own reviewed tranches.
- Finish all Directorate, project, foreign-operation, containment, Kruger State, focus-tree, super-event, achievement, aftermath, world-end, documentation, and workbook surfaces before enablement.

No fallback or deliberate simplification is used in this opening tranche. The listed remaining work is outside this tranche and prevents any whole-event completion claim.
