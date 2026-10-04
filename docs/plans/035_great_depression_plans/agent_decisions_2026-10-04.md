# Event 35 Agent Decisions, 2026-10-04

These decisions were taken by the implementing agent under the user's grant of full design authority for the Event 35 takeover.
Each entry records the rule, its basis in the accepted spec package, and its disposition.
Implementation evidence is linked by commit; it proves what exists and does not by itself establish design approval beyond this grant.

## D1. Super-event slot 105 in the shared lists

Disposition: implemented (commit `0efa5b56c`).

Event 35 raises `super_event_visible` slot 105 when the depression becomes worldwide (`great_depression_event.worldwide_super_event_slot`).
Each of the five shared lists (`GetSuperEventImage`, `GetSuperEventTitle`, `GetSuperEventQuote`, `GetSuperEventRemark`, `GetSuperEventDesc`) gained one 105 row that points at `GFX_super_event_105_second_great_depression` and the existing `chaosx_super_event.105.t/.q/.a/.d` keys.
No other shared row changed.
The in-game display remains `needs_live_game`.

## D2. Partner target rules for Acquire Distressed Assets and Exploit Supply Gap

Disposition: implemented.

Both decisions target countries, so their target triggers run in partner-country scope with ROOT as the acting country.

- Acquire Distressed Assets: the partner passes `great_depression_has_proved_partner_relationship` and `great_depression_partner_pair_cooldown_is_open`, is in its own active Event 35 crisis (`great_depression_active_crisis_is_coherent`), and owns and controls a center registered to its current episode that is Shuttered or Abandoned and not liquidated (`great_depression_partner_has_failed_center`).
  Basis: spec part 5 maps this action to "purchase failed assets", so the seller must actually hold a failed asset.
- Exploit Supply Gap: the partner passes the same relationship and cooldown checks and is in its own active Event 35 crisis.
  Basis: the review left the partner rule undecided; the narrowest rule consistent with part 5's exploitation balance is that only an economy in depression has a supply gap to exploit.

Neither trigger uses a state-only condition in country scope any more.
The tooltips for both scripted triggers describe the partner condition, and the new `great_depression_partner_has_failed_center_tt` names the failed-center requirement.
The AI weight bodies did not change; only the set of legal targets did.

Probability evidence: the required before/after `hoi4.probability_inspect`/`hoi4.probability_compare` pass could not run.
`hoi4.probability_inspect` with `adapter = decision_ai_will_do` returned `Invalid tool arguments` with a candidate pool and with no source, and `INTERNAL_ERROR` (zero artifacts) with `source.path = common/decisions/035_great_depression_decisions.txt`.
`hoi4.decision_inspect` in `inspect` mode for `great_depression_acquire_distressed_assets` returned `Invalid tool arguments`.
The route failure is recorded as a blocker for numeric AI evidence; target legality was reviewed from source.

## D3. Incident state picker keeps the registered center

Disposition: implemented.

`great_depression_incident_select_state` first saves a valid registered center, then falls back to a random owned and controlled state only when no center target was saved (`NOT = { has_variable = great_depression_incident_state_target }`).
Before this, the fallback read `great_depression_incident_target_valid`, which is set only after both branches, so it always ran and replaced the chosen center.
Basis: spec part 4 requires an incident to name the exact center state and its current treatment.
A country without a valid center still receives a valid owned state.

Incident weights, factors and gates did not change.
The K-09 audit (`subagent_handoffs/k09_incident_pool_audit_2026-09-05.md`) declared its center-specific gates as "usable centers" true or false, which is the behavior the picker now delivers, so the audited distribution is restored rather than changed.
The K-09 manifest was never saved in the repository, and the probability routes failed in this session (see D2), so no new compare artifact exists; this is recorded as a route blocker, not as fresh numeric evidence.

## D4. Adopt the inherited-liability tranche with the national inheritance pressure kept

Disposition: implemented.

The stopped thread's inherited-liability consumer (`common/scripted_effects/035_great_depression_inherited_liability_effects.txt` and `.md`, hooks in the main, decision and region effects, `.tools/test_event035_inherited_hooks.py`, the `.tools/test_event035_center_projects.py` changes, `audit_inputs/liability_hooks_2026_10_03/` and its handoff) is adopted as finished work.
As written, it deleted the flat `credit_boom_inheritance` and `industrial_inherited_region` terms from `great_depression_rebuild_hidden_components`.
Its row consumer adds credit only for supplied regional project, protection or fragility facts, and Event 34 never supplies them (`industrial_boom_region_project_profile` and the related fields have no producer), so every real Event 34 to Event 35 handoff would have lost about 2 net hidden stress per pulse.

Rule taken:

- The boom credit hangover is a national fact: the flat `credit_boom_inheritance` term is restored for every `great_depression_event34_inherited` country, and the row credit output adds to it only for rows with supplied facts.
- The flat `industrial_inherited_region` term applies while no current inherited row carries a supplied project profile, project stage, protection or fragility value (`great_depression_inherited_project_fact_count` is zero).
  Once one does, the exact row industrial output replaces the flat term; the two are never both added.
- Live control and damage, which Event 34 does supply, do not count as project facts, so a damaged or disconnected real row keeps the flat term instead of adding a second industrial unit.
- Row demand output (hidden-row stage pressure and supplied exhaustion) is added as before; it has no flat counterpart.
- The main -5 to 5 clamp is unchanged.

Evidence: both test files pass, and the new `test_real_event34_row_keeps_baseline_hidden_pressure` shows an intact and a damaged real Event 34 row keep all seven hidden components and the net value of the frozen pre-tranche source.

Closed as blocked on Event 34, not queued for Event 35: hidden-row paid paths, corridor restoration, breakup and scar, secured-value salvage, and multi-region inherited priority.
Event 34 is a legacy event with no per-region project or corridor system, and the spec forbids inventing that history (spec part 8; inherited consumer audit, section B).

## D5. Event Log wiring and the single history row

Disposition: implemented.

- Details: `GetEventsLogEventDetailDescription` shows `chaosx.events_log.window.event_details.great_depression`, whose wording matches the catalog Details column.
  When the window is opened from a History row that names a country, it shows `chaosx.events_log.window.event_details.great_depression.history`, which adds that country and the Depression Severity stored as the row payload.
- Evolutions: type, title, body and per-stage summary rows for evolution type 35 use `constant:great_depression_evolution_log.*` in the Evolutions, History and Event Details lists.
  Stage and tier labels come from the shared numeric lists, so no Event 35 rows are needed there.
- Toggles: the Event Details producer adds three preview rows (stages 1 to 3, tiers 2 to 4), so the existing `events_log_disabled_evolution_35_35_1..3` toggles that `is_current_evolution_enabled` already reads can be reached.
- Single row: following the lead decision, the duplicate is fixed in Event 35's own file instead of a pre-fire branch in the shared dispatcher.
  When the call comes from the independent Event 35 path (random pool or cluster dispatch), `great_depression_record_history` fills in the newest row if it is an Event 35 row from today with no country, writing the country and Severity into index 0.
  Otherwise it appends its own row, so inherited, conversion and relapse starts, and a second country on the same day, keep separate rows.
  The cluster path is included because it uses the same dispatcher and leaves the same countryless row.
- `docs/events/035_great_depression.md` no longer claims Event Log surfaces that did not exist.

needs_live_game: the fill-in relies on the dispatcher recording its row before the queued `chaosx.nr35.1`/`chaosx.nr35.9` events run, which is how the prefire actor bindings of other events already behave; if a live firing still shows two rows, the order is different and the dispatcher would need the pre-fire branch after all.
