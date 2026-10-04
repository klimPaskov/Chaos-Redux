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

## D6. Doctrine projects and producers for the unused center project types

Disposition: implemented.

Basis: the decision map names "Restore Local Credit and Trade Connection" as the Finance and Trade state project and "End Rescue Dependence or retain bounded arsenal institution" as the Strategic Industry Stabilization action, and spec part 4 lists restored basic transport and supply as a reopening need.
`finance_restoration`, `transport_integration` and `international_reconstruction` had completion branches but no producer, and Prevent a Relapse accepted no Strategic Industry recovery measure.

- Restore Local Credit and Trade Connection: a state-targeted Finance and Trade decision on the selected (AI: any valid) Distressed, Idled or Shuttered center with an open project slot.
  It needs a completed bank audit, pays the existing `finance_trade` family through the shared affordability check and cost quote, and authorizes `finance_restoration`; completion reopens the center as restructured.
- Keep Essential Freight Moving: on completion, the selected center (AI: one valid center) gets `transport_integration` when it is closed and no center project runs; if a project already runs there, it gains `great_depression_center_project_credit.freight_days` of work once per authorization.
  The mission's own cost pays for the work, so no second charge is made.
- Coordinated Public Works and Reconstruction: after its existing contribution, starts `international_reconstruction` on the selected (AI: one valid) closed center, including an abandoned one that was not liquidated, when no center project runs.
- Strategic Industry closers: two mutually exclusive decisions in Stabilization or Recovery.
  End Rescue Dependence (policy-review cost, strong Severity relief) clears the essential orders and adds the existing `fiscal_response` hidden relief.
  Retain a Bounded Arsenal Institution (strategic-rescue cost, standard Severity relief) needs a completed strategic center, keeps the essential orders, and adds `fiscal_arsenal_upkeep` hidden fiscal pressure and `war_arsenal_relief` hidden war relief while at war.
  Both flags count as the durable recovery measure for Prevent a Relapse and are cleared with the other doctrine flags at episode cleanup.
- Icons reuse the doctrine plates through new aliases in `interface/035_great_depression.gfx`, so bespoke art can replace a texture later without code changes.
- Every new decision has a name, description, cost text, tooltips and an explicit `ai_will_do` built from the existing profile triggers: financial stabilizers prefer the finance project and avoid it under blockade or trade failure; fiscal retrenchers and liquidation gamblers prefer ending the rescue, which the AI never does at war; strategic mobilizers and wartime countries prefer keeping the arsenal, which fiscal retrenchers avoid.

Evidence: `.tools/test_event035_center_projects.py` gained `DoctrineProjectProducerTests` (finance restoration gated by the audit and completing as restructured, freight starting transport integration and then crediting once, reconstruction starting only with an open slot, and both closers satisfying the shared closer gate exclusively); all 15 tests pass.

Probability evidence: the doctrine-scenario before/after pass could not run; `hoi4.probability_inspect` with `adapter = decision_ai_will_do` returned `Invalid tool arguments` again with a three-decision candidate pool and a workspace source selector (see D2).
The AI weights were set by source review against the existing doctrine profiles; numeric AI balance remains unverified.
Catalog notes are in `catalog_changes_pending.md`.

## D7. Negative Economy cluster registration and cluster targeting

Disposition: implemented.

- Registration follows `docs/systems/event_system/event_clusters.md`: cluster ID 10, Minor Fire-Once (`event_cluster_type.one_time`), unlock tier 0 (Chaos level 1).
  Event 35 is the required Low primary-trigger row (10001), and Event 50 The Great Embargo is the optional Medium primary-trigger row (10002).
  Event 50 has no identity constant, so its id lives in `event_cluster_negative_economy.great_embargo_event_id`, as Various Anomalies does for Event 47.
  The candidate mapping is derived from `load_event_cluster_members`, so no separate event-to-cluster table was needed.
  Names and the description show in the Event Details cluster line, History, the Clusters tab, the selected-cluster view and the settings cluster browser.
- Targeting: the cluster fires Event 35 on the event-system host, not on a chosen country, so the old cluster branch would have started a depression on the host or silently done nothing when the host was already in one.
  Both entries now use the weighted independent selector, which never offers a country already in Event 35; a cluster pick carries `great_depression_cluster_target_pending` so the start keeps the cluster's consequence pacing lane.
  Basis: spec part 8, "a country already in Event 35 is skipped as an independent cluster target".
- Event 34 collapse, contagion conversion, the Evolution III spread and relapse call the start contract directly and never pass through the event dispatcher, so they cannot roll or replay the cluster.
- Event 50 is a legacy event owned by its own engineer; it keeps picking its own target and is only referenced here as an optional member.

## D5 amendment: history completion is deferred

Disposition: implemented, superseding the immediate fill-in described in D5.

The shared cluster documents treat no-delay `country_event` dispatch as synchronous, which means the dispatcher writes its countryless row only after Event 35's chain returns.
`chaosx.nr35.1` therefore records the newest history sequence as a dispatch floor, and an independent start schedules the hidden `chaosx.nr35.10` one hour later.
That callback fills the newest countryless Event 35 row at or above the floor with the country and its starting Severity, which works whether dispatch is synchronous (the row is one above the floor) or queued (the row is at the floor), and an older stale row below the floor is never touched.
If no such row exists, it records a full row itself.

## D8. Opening news picture

Disposition: implemented (commit `7704873f7`).

`chaosx.news.40` uses `GFX_news_event_great_depression`, the Event 35 news art that `chaosx.news.95` already uses, instead of the generic gathering-protest picture.

## D9. Deferred history row writer and Event Log refresh

Disposition: implemented.

The deferred `chaosx.nr35.10` callback runs an hour after the firing, so its fallback row (written only when the dispatcher left no countryless Event 35 row) uses `record_events_log_system_history_entry` with the repeatable event type instead of the borrowed `global.last_fired_event_id` path.
Rewriting the last fired event an hour late would show Event 35 as the latest firing even when another event fired in between.
After it fills or adds the row, the callback calls `refresh_events_log_system_history_views`, so an open History, Events or Event Details view shows the country and Severity at once instead of after the window is reopened.
The comment on `great_depression_center_transport_target_is_valid` now states what the trigger checks; it never tested for a working plant.

## D10. Decision AI evidence from `hoi4.decision_inspect`

Disposition: implemented as evidence; numeric before/after comparison remains blocked.

`hoi4.probability_inspect` with `adapter = decision_ai_will_do` still returns `Invalid tool arguments`, with and without a candidate pool.
`hoi4.decision_inspect` in `inspect` mode with declared scenarios now works and runs the `decision_ai_will_do` adapter in baseline mode, so the new and changed decisions have scenario evidence.
All scenarios use GER with `closedFlags`, an active coherent episode (Severity 40), every quoted cost variable present and resources above the quote.
The routes report `DECISION_ANALYZED_PARTIAL` because `has_cosmetic_tag`, state iterators (`any_owned_state`, `any_controlled_state`) and partner relationship checks cannot be declared.

| Decision | Scenario (profile, phase, war) | AI score |
| --- | --- | --- |
| End Rescue Dependence | fiscal retrencher, Stabilization, peace | 38 |
| End Rescue Dependence | liquidation gambler, Stabilization, peace | 34 |
| End Rescue Dependence | strategic mobilizer, Stabilization, peace | 24 |
| End Rescue Dependence | state coordinator, Stabilization, peace | 24 |
| End Rescue Dependence | strategic mobilizer, Stabilization, war | 0 |
| Retain a Bounded Arsenal Institution | strategic mobilizer, Stabilization, war | 44 |
| Retain a Bounded Arsenal Institution | strategic mobilizer, Stabilization, peace | 36 |
| Retain a Bounded Arsenal Institution | state coordinator, Stabilization, peace | 32 |
| Retain a Bounded Arsenal Institution | liquidation gambler, Stabilization, peace | 22 |
| Retain a Bounded Arsenal Institution | fiscal retrencher, Stabilization, peace | 0 |
| Restore Local Credit and Trade Connection (Idled center, 4 factories) | financial stabilizer, Depression, peace | 42 |
| Restore Local Credit and Trade Connection | state coordinator, Depression, peace | 38 |
| Restore Local Credit and Trade Connection | fiscal retrencher, Depression, peace | 28 |
| Restore Local Credit and Trade Connection | financial stabilizer, Depression, war | 0 |

End Rescue Dependence resolved as eligible in every scenario, with the actor gate, phase gate and quoted cost all true.
The two closers rank as D6 intended: retrenchers and liquidation gamblers lean to ending the rescue, mobilizers and coordinators to keeping the arsenal, and war blocks ending it while raising the arsenal.
Eligibility for the arsenal closer and the finance project stays unresolved only because their state checks cannot be declared.

For Exploit Supply Gap, the partner target trigger now runs in partner-country scope: with FRA declared as a partner in its own active episode, `great_depression_active_crisis_is_coherent` resolves true on FRA, while the relationship and the meta-trigger cooldown stay unresolved and the score depends on undeclarable partner valuation.
The pre-fix trigger had no before run, because a compare needs the whole 95 KB trigger file inline; it could never pass, because every condition in it was a state trigger evaluated on a country.

Artifacts (workspace `mod_chaos_redux_ea3b2d67c2c0`): `decision-6148bb24c870ec1a7a58906a.json` (End Rescue Dependence), `decision-4a2def22c09ceceff5ab5739.json` (arsenal), `decision-0af142fc1b38432cd46b634c.json` (finance restoration), `decision-8bff4d692d2dd3640dd90f2f.json` (Exploit Supply Gap).

## D11. Round 1 review fixes

Disposition: implemented.

- Ending the rescue closes Guarantee Essential Orders for the episode.
  End Rescue Dependence clears `great_depression_essential_orders_guaranteed`, which was the only thing hiding Guarantee Essential Orders, so the country could buy the essential orders back while keeping the closer's fiscal relief and its Prevent a Relapse credit.
  `great_depression_should_show_guarantee_essential_orders` now also requires `NOT = { has_country_flag = great_depression_rescue_dependence_ended }`, and its requirement text says so.
  Basis: D6 makes the two closers the end of the Rescue Strategic Industry route, and the decision text says the guarantee is withdrawn.
  The episode reset already clears the flag, so the next episode offers the decision again.
  Evidence: `hoi4.decision_inspect` in `inspect` mode (`decision-77075c3cb630f84ba2728b3f.json`) resolves the decision as not visible with the flag set; without it, visibility stays unresolved only on the undeclared `exists` check. No AI weight changed.
- A random or cluster firing no longer writes the last fired event from Event 35.
  `great_depression_record_history` set `global.last_fired_event_id` to Event 35 on every call, including the deferred random and cluster path where the dispatcher already owns that value.
  It now sets it only in the direct-start branch that writes its own row through `record_events_log_history_entry`, which reads it; this matches D9.

## D12. Event-pool availability and second review fixes

Disposition: implemented.

- Event-pool availability hook.
  The random pool and the Negative Economy cluster could draw Event 35 while no country was a valid independent target; the firing then started nothing and left a countryless history row that no callback could complete.
  `great_depression_has_any_independent_target` (Event 35 triggers) is true while any major or player country passes `great_depression_is_valid_independent_target`.
  The shared `evaluate_event_pool_candidate_unavailability` gained one `else_if` that sets the new reason `event_system_event_unavailability_reason.great_depression_target = 51` when it is false, following the Fury and Doctrine Research hooks.
  The same evaluator feeds the random pool, cluster member availability and the Events tab, so the cluster skips the row and both tabs show `chaosx.events_log.events.na_reason.great_depression_target` (Event 35 localisation file); the two reason lists in `chaosx_scripted_localisation_events_log.txt` each gained one row.
  Basis: spec part 1, "No valid target": with no valid country, Event 35 contributes no live candidate to automatic selection and the event list shows it as unavailable; full spec scenario `TGT-08` expects "Event is unavailable and no call is queued".
  The settings force-fire path bypasses the pool by design and still reaches `chaosx.nr35.1`, which then selects nothing; that debug path is left unchanged.
- Partner target order.
  `great_depression_distressed_asset_target_is_valid` and `great_depression_supply_gap_target_is_valid` check `great_depression_active_crisis_is_coherent` first.
  Every country is tested as a target and most are not in a depression, so they now fail on one flag before the relationship scan and the meta-trigger cooldown; the rule set is unchanged.
- Player text.
  The three partner target texts say "we must not have acted on them recently" instead of "outside the bilateral cooldown", matching the cooldown tooltip.
  The freight and reconstruction center tooltips name the center stages the targets accept instead of calling the center "closed", which a Distressed center is not.

## Commit index

| Decision | Commit |
| --- | --- |
| D1 super-event slot 105 | `0efa5b56c` |
| D2 partner target rules | `0b18abb41` |
| D3 incident state picker | `1bc0522df` |
| D4 inherited-liability adoption | `c398021a9` |
| D5 Event Log wiring | `a5a01b54e` |
| D6 doctrine projects and producers | `97d28a7a4` |
| D7 and the D5 amendment, Negative Economy cluster and deferred history completion | `0c0d4f8d7` |
| D8 opening news picture | `7704873f7` |
| D9 deferred history writer and D10 decision AI evidence | `f6849915e` |
| D11 round 1 review fixes | the commit "Close Guarantee Essential Orders after the rescue ends in Event 35" |
| D12 event-pool availability and second review fixes | the commit "Keep Event 35 out of the event pool while no country can fall into a depression" |

## Remaining limits

- needs_live_game: super-event 105 display, the single history row on a random and on a cluster firing, the Event Details evolution toggles, the cluster appearing and firing, and the new decisions' tooltips and map targeting.
- `hoi4.probability_inspect` and `hoi4.probability_compare` still reject the decision adapter, so no numeric before/after comparison exists for D2, D3 or D6; D10 records the scenario baseline that `hoi4.decision_inspect` could produce.
- needs_live_game: Event 35 shows as unavailable with the new reason in the Events and cluster tabs while every major and player country is in a depression, a boom or its aftermath (D12).
- A settings force-fire of Event 35 with no valid target still selects nothing; the force path bypasses the pool by design (D12).

## D13. National recovery report (round 2, item 1)

Disposition: implemented.

- Basis: the accepted recovery-depth addendum, row `events/035_great_depression.txt` of "Exact implementation surfaces" (freeze summary, receipts, legacy, cleanup, then report or news), and spec part 10 "Recovery text direction".
- `chaosx.nr35.11` is queued by `great_depression_queue_recovery_report` as the last step of `great_depression_try_complete_recovery`, one day later, after cleanup. It reads only the frozen `great_depression_last_completed_*` summary.
- The report counts come from each center's final flags at freeze time, not from the running `great_depression_centers_*_count` counters. Agent decision: the counters do not describe final status. The reopened counter counts every reopening, the restructured counter counts positive resolutions, and the liquidated counter only moves when a deep-severity liquidation removed a factory, while `great_depression_abandon_selected_center` sets the liquidated flag without writing the stage ledger. Flags are the one consistent final record, so the freeze classifies each matching-episode center as reopened, restructured, liquidated, or abandoned (abandoned, hollowed, or scarred) and stores the result in `great_depression_last_completed_center_outcome_entries`, which the durable state outcomes reuse.
- The freeze also records `great_depression_last_completed_episode_doctrine` and `great_depression_last_completed_doctrine_switch_count`. The report names the institution the final doctrine leaves and its weakness from the frozen doctrine, because `great_depression_doctrine` stays live until the next episode resets it.
- The report has no gameplay effect. The option shows the recovery ideas the country holds, and its AI weight is the new constant `great_depression_event_option_weight.recovery_report`.
- The counts are shown without the number of centers struck, because transferred centers count as resolved but have no final outcome of their own, and a total would not add up.

## D14. Real requirement text for the evolution and partner actions (round 2, item 2)

Disposition: implemented.

- The 21 `great_depression_can_*` keys that showed the generic sentence about crisis state, resources and target now name what their trigger bodies check, with no trigger change.
- Financial Contagion actions read "Requires an open national response slot and active Financial Contagion."; Break the Occupations and Nationalize or Socialize Occupied Industry name Social Collapse; Coordinate International Rescue names Social Collapse and The Second Great Depression spreading worldwide.
- Prioritize Domestic Recovery, Restrict Capital Outflows and Support Contagion Source name the open response slot and either active Financial Contagion or an open foreign exposure without a national depression, which is the exposed-economy branch of their trigger.
- Select Depression Center names the active depression and a controlled, unliquidated center with people and industry. `great_depression_center_selection_lock` is never set anywhere, so the text does not mention it.
- Use Foreign Partner names the slot and the recent-support cooldown without a day count, because the 30-day duration is a file-scoped `@` constant that the text would otherwise duplicate.
- Resource affordability stays with the existing cost tooltips.

## D15. Evolution reports, exposed-partner report and first-spread news (round 2, item 3)

Disposition: implemented.

- Basis: spec part 5 "Event and news presentation" and spec part 10 "Financial Contagion text direction" (origin report, exposed-country report), and the lead's decisions 3 and 4 for this round.
- `chaosx.nr35.12` (Financial Contagion) and `chaosx.nr35.13` (Social Collapse) are queued only from the mid-crisis activation branches of `great_depression_try_evolution_activation`, once per episode through `great_depression_contagion_report_episode_id` and `great_depression_social_report_episode_id`. An episode that opens with an evolution active keeps its opening report. Those branches require the evolution to be enabled, so a disabled evolution queues nothing.
- The contagion report freezes the partner count and the partner at the highest exposure stage when it is queued, because the report fires a day later.
- Agent decision: the Social Collapse report needs the movement family, which was chosen only when the extreme incident ladder opened. The activation branch now runs the existing deterministic, idempotent `great_depression_select_social_actor` first, so the report and the later ladder name the same movement. The selector snapshots conditions at activation instead of at the ladder start. No incident weight, list member or AI weight changed; only the timing of the existing selection moved. The numeric probability route for incident pools was not rerun; the decision-adapter blocker recorded in D10 still stands for decisions.
- Agent decision: the exposed-partner report `chaosx.nr35.14` uses a short per-partner queue (`great_depression_exposure_report_origins` and `_relationships`, capped at `great_depression_event.contagion_source_cap`) instead of one variable, so two sources reaching one partner in the same week each get a correct report. The once-per-source-episode guard is the targeted variable `great_depression_exposure_report_from_@PREV`, which holds the source episode id and is bounded at one variable per source tag. The hook is the first add to the source's `great_depression_contagion_material_targets`, as decision 4 says.
- Agent decision: the first-spread news `chaosx.nr35.15` is sent from the converted country's own opening report option in place of `chaosx.news.40`, so `FROM` is the newly struck country, as with `chaosx.news.40`. The source records the episode in `great_depression_first_spread_news_episode_id`; a deepened crisis never counts as a first spread, and later conversions from the same episode keep `chaosx.news.40`. Only full new depressions count, which is what "first full secondary depression" means.
- New option weights: `great_depression_event_option_weight.contagion_report`, `social_collapse_report`, `exposure_report` and `world_news`.
- needs_live_game: the four new popups' scripted names (`[?great_depression_contagion_report_partner.GetName]`, `[?great_depression_exposure_report_origin.GetName]`, `[?FROM.great_depression_first_spread_origin.GetName]`) follow the variable-scope pattern already used across the mod, and their display is not verified in game.
