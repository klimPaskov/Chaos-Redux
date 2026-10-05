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

## D16. Recovery legacy costs, later-episode effects, safeguard and hollow flag (round 2, item 4)

Disposition: implemented.

- Basis: spec part 4 "Recovery legacy budget", "Strong reforms and future resistance" and "Repeated failures", and the lead's decisions 6 and 7.
- Each legacy idea keeps its benefit and gains one countervailing modifier: Public Works `consumer_goods_factor` 0.02 (upkeep), Strategic Industry `production_speed_industrial_complex_factor` -0.08 (civilian sector passed over), Finance and Trade `min_export` 0.05 (foreign claims), Austerity `stability_factor` -0.03 (thin relief), Direct State Planning `line_change_production_efficiency_factor` -0.10 (lower flexibility), Market-Clear `production_factory_start_efficiency_factor` -0.05 (skilled workers lost).
- Agent decision: the hidden components are summed into one clamped net pressure, so a flat -1 relief on one component and a flat +1 weakness on another would cancel. `great_depression_apply_recovery_legacy_pressure` therefore applies the relief always and the weakness only under the condition the spec names for it (deep crisis upkeep, peacetime rescue dependence, foreign exposure, unemployment shock, administrative burden after the emergency, regional unemployment), and Market-Clear's relief needs stable conditions. A legacy makes a later episode easier on its own ground and harder when its weakness is exposed, and no route grants immunity.
- `great_depression_post_recovery` is added when an episode closes with the recovery watch running and removed when the watch expires or when any new episode commits, which covers relapse. Agent decision: the safeguard follows the watch, so a country that could not join the capped watch registry (32 rows) gets no safeguard instead of an unbounded one.
- `great_depression_resolve_recovery_outcome` sets `great_depression_recovery_hollow` for a Hollow result and clears it for Strong or Uneven, which makes the contagion-vulnerability trigger and the worldwide-pressure score live without changing them.
- AI: no `ai_will_do`, `ai_chance` or random-list weight changed. The legacy offsets change hidden Severity pressure in later episodes, which is not a weighted surface.

## D17. Lasting district outcomes after recovery (round 2, item 5)

Disposition: implemented.

- Basis: accepted addendum B3 ("One country legacy and at most two state outcomes"), spec part 4 "Cleanup after recovery" step 4, and the lead's decision 5.
- `great_depression_apply_durable_state_outcomes` runs in the recovery transaction after the freeze and reads only the frozen center arrays, including the final outcome array added in D13.
- Agent decision on scoring: a structural project scores by type through the new `great_depression_state_outcome` constants (lasting capacity 6, international reconstruction 5, public works and transport integration 4, strategic rescue and finance restoration 3, asset reorganization and trusteeship 2). The short treatments (reopened capacity, protection) score zero, because addendum A separates them from structural projects. A scar scores each frozen Event 35 factory level lost plus one for an abandoned or liquidated center, and only a center that did not end reopened or restructured can be scarred, which is what "unrepaired" means here.
- Agent decision on ownership: only centers the recovering country still owns are eligible, so a transferred district never receives an outcome from an episode its new owner did not run.
- B3's rule that a second distinct project may keep a positive outcome when no scar is due is implemented. One state never gets both, and a later episode's outcome replaces the earlier one on the same state.
- The modifiers `great_depression_state_recovered_district` and `great_depression_state_scarred_district` reuse `GFX_modifier_035_great_depression_center_reopened` and `_hollowed`; no new art.
- The recovery report names the districts, so the outcome is visible at the moment it is granted.
- needs_live_game: the state modifier display on the map and state view.

## D18. Emergency Government spirit and Social Collapse political aftermath (round 2, item 6)

Disposition: implemented.

- Basis: spec part 6 "Coup design" (an emergency national spirit with a lifecycle) and "Resolution and aftermath" (one coherent aftermath that persists and affects future episodes).
- `great_depression_emergency_government` is added by a successful coup, an emergency dictatorship and Form an Emergency Government, and removed by mandate success, failure or cancellation, Remove Emergency Controls, recovery, and a rolled-back opening.
- Agent decision: Remove Emergency Controls now also clears `great_depression_social_emergency_mandate_active`. It already cleared `great_depression_emergency_government_formed`, which the mandate objective requires, so the mandate could no longer succeed; ending it at the same time keeps the spirit and the flag consistent and does not change any outcome the player could reach.
- Agent decision on aftermath priority: Emergency Rule, Planning Settlement, Corporate Rescue Order, Regional Autonomy, Labor Scar, Social Compact. The outcome that reshaped the state comes first, and repression outranks a negotiated compact, because a compact signed after troops broke the strikes does not erase that memory. Only an episode with Social Collapse active at recovery chooses one; a new aftermath replaces the old, and an episode that earned none keeps it.
- Later-episode effect: the `aftermath_*` keys of `great_depression_hidden_component` shift hidden social stress (Corporate Rescue Order and Labor Scar +1, the others -1).
- Agent decision on art: the seven spirits use Event 35 sprite names that alias installed vanilla national-spirit textures (`idea_ARG_military_government`, `idea_SWE_saltsjobaden_agreement`, `idea_HUN_state_protection_authority_idea`, `idea_generic_nationalization`, `idea_CZE_industrialists_veto`, `idea_AFG_economic_regionalism`, `FRA_factory_strikes`). Each texture was confirmed present in the base game install. Bespoke Event 35 art remains an asset follow-up and only needs the texture paths changed.
- AI: no event option, decision or random-list weight changed.
- needs_live_game: spirit icons and tooltips in the national-spirit panel.

## D19. World news for the global episode (round 2, item 7)

Disposition: implemented for the three milestones in the acceptance; two spec milestones remain queued.

- Basis: spec part 7 "News and reports" and spec part 10 "Recovery text direction" (end of the worldwide depression), and the lead's decision 3 (Event 35-owned news ids in the `chaosx.nr35` namespace).
- `great_depression_queue_global_news` guards each news with its own global episode-id receipt (`global.great_depression_reconstruction_news_episode_id`, `_retirement_news_episode_id`, `_supplier_news_episode_id`), so the reconstruction news is not replayed when `great_depression_reset_global_recovery_proof` moves the stage back to recovery and it later returns.
- The disabled check uses `has_disabled_current_evolution` with the Second Great Depression evolution identity, not the tier check, because the episode can outlive the Chaos tier that opened it.
- Agent decision: the origin is copied into `global.great_depression_news_origin` from the global activation-source event target when the news is queued, because retirement clears that event target in the same pulse; the text names the origin only when that variable exists.
- Agent decision on art: all three use `GFX_news_event_great_depression`. The registered recovery and boom-collapse pictures are 210x176 report images and would not fill the 397x153 news frame; dedicated news art for these milestones is an asset follow-up.
- Accepted and queued: spec part 7 also lists news for the failure of a major recovery conference and the formation of a major clearing or protectionist bloc. Neither has a single transition point in the current source that marks "failure" or "major" formation, so they need a design pass before news can hang on them; the lead's acceptance for this round did not include them.

## D20. Receipt-based country scars at recovery (round 2, item 8)

Disposition: implemented.

- Basis: spec part 4 "Recovery scars" (a real source receipt and a mitigation path for each scar) and "Recovery legacy budget".
- Agent decision on receipts: `great_depression_emergency_credit_requested`, `great_depression_external_supervision_accepted`, `great_depression_foreign_support_active` and `great_depression_capital_outflows_restricted` are never reset between episodes, so they cannot prove a use in the closing episode. The actions now also write per-family episode receipts (`great_depression_scar_debt_episode_id`, `_foreign_episode_id`, `_controls_episode_id`), and only a receipt matching the closing episode counts.
- Agent decision on Labor Bitterness: the same security-force and broken-occupation flags already earn the Labor Scar political aftermath (D18). Labor Bitterness is earned only when that aftermath was not chosen, for example when an emergency government that settled outranked it, so one cause never yields two penalties.
- Agent decision on priority: Debt Overhang, Foreign Credit Dependence, Emergency Controls, Labor Bitterness, Policy Fatigue; the first match is earned. Policy Fatigue needs `great_depression_country_scar.policy_fatigue_switches` = 2 doctrine switches in one episode.
- Removal paths: a later strong recovery under the matching doctrine (or with the controls removed, a Social Compact aftermath, or no doctrine switch) clears an older scar, and a newly earned scar replaces it. Each scar carries one bounded modifier.
- Art: the five spirits alias installed vanilla textures (`idea_AST_liberty_loans`, `idea_generic_foreign_capital`, `idea_can_wartime_prices_and_trade_board`, `idea_ICE_general_strike`, `idea_NOR_optimistic_cabinet_ns`), each confirmed present in the base install.
- AI: no weight changed.

## Round 2 commit index

| Decision | Item | Commit |
| --- | --- | --- |
| D13 national recovery report | 1 | `51e9c1532` |
| D14 real requirement text | 2 | `b2cb3c478` |
| D15 evolution reports, exposed-partner report, first-spread news | 3 | `26512b905` |
| D16 legacy costs, later-episode effects, safeguard, hollow flag | 4 | `d24652e14` |
| D17 lasting district outcomes | 5 | `91822b390` |
| D18 Emergency Government spirit and political aftermath | 6 | `95a90f663` |
| D19 global episode news | 7 | `546f86a0e` |
| D20 receipt-based country scars | 8 | `d7424e315` |

## Round 2 remaining limits

- needs_live_game: display of the eight new popups and their scripted names, the new spirit icons and tooltips, the district modifiers on the map, and the recovery report's option tooltip.
- Accepted and queued: news for the failure of a major recovery conference and for the formation of a major clearing or protectionist bloc (D19).
- Asset follow-up: bespoke Event 35 art for the twelve aliased spirits and dedicated news art for the reconstruction, end and supplier-collapse news.
- The numeric AI probability comparison remains blocked by the decision adapter (D10); no weight changed in round 2.

## Lead decisions for round 2, attempt 2

Disposition: recorded as the acceptance basis for D21 onward. The lead took these under the user's grant of full design authority.

- L1. Round 2 attempt 1 (D13 to D20, `51e9c1532` to `eaa9ab8f8`) counts as done; the one defect found (`great_depression_occupied_industry_socialized` never cleared) belongs to the flag-leak item.
- L2. The six trap actions keep their identities, stop raising the actor's Severity, give a bounded current-episode benefit read by `great_depression_rebuild_hidden_components`, and move the cost to the partner or the world. Withdraw from International Commitments stops charging the reconstruction quote and visibly gives up the country's global contribution.
- L3. The Global Recovery Conference becomes a convened conference that other countries join, with success and failure outcomes, one guarded Chaos change and one world news on failure.
- L4. Clearing and protectionist blocs become global member sets with real effects and formation news.
- L5. Effect tooltips cover the whole decision surface; the Severity amount comes from the same constant the effect uses.
- L6. Flag lifecycle: a country's own action and condition flags clear at episode start, abort and recovery cleanup after the recovery outcomes have read them; partner and global flags end with the relationship or at global retirement; achievement receipts count within one episode.
- L7. Art: the twelve vanilla-texture spirits need bespoke Event 35 art; the D6 decisions keep their shared doctrine plates; the global news may keep the Event 35 news picture.
- L8. Excluded: Event 34 supplier choices, the hidden-row paid paths closed in D4, the settings force-fire path, workbook and CSV edits, documentation-only churn.

## D21. Market exits and supply-gap purchases (round 2 attempt 2, item 2)

Disposition: implemented.

- Basis: L2; spec part 5 "Abandon the Distressed Market", "Exposure pressure", and "Foreign aid and exploitation balance".
- Agent decision on the actor benefit: each action opens a current-episode relief window (due day plus episode id) read by `great_depression_rebuild_hidden_components`. Abandon is the strongest (credit -2 and trade -2 for 84 days), Withdraw the smallest (trade -1 for 56 days), Exploit gives industrial relief (-2 for 70 days). A later use refreshes the window rather than stacking it. The actor's Severity no longer moves, and an action with no Severity change keeps the measured trend.
- Agent decision on "stops that partner pair from passing pressure on": Abandon adds the partner to the actor's bounded `great_depression_severed_partner_countries`, and `great_depression_process_contagion_network` no longer applies the actor's weekly exposure to that partner. The cut link carries the one shock below and nothing after it.
- Agent decision on the partner cost: Abandon gives a partner in its own depression +4 Severity; an exposed partner's existing link rises one stage through `great_depression_raise_partner_exposure_link` and `great_depression_apply_exposure`, so the ordinary conversion rules apply; an untouched partner opens a new link at Dependent. The partner gains `great_depression_market_abandoned` (-30, decay 2) towards the actor, which is the diplomatic cost. Withdraw gives +2 to a partner in its own depression, opens a new link only at Pressured, and adds no opinion. Exploit gives +3 to the partner (always in its own depression by the target rule) and `great_depression_supply_gap_exploited` (-20, decay 2); while the actor's Social Collapse is active, its relief window also adds +1 hidden social stress.
- The never-read partner flags `great_depression_distressed_market_abandoned`, `_withdrawn` and `great_depression_supply_gap_exploited` are gone. Contagion rows still record abandonment through the temporary `great_depression_partner_outcome_hostile`.
- Cleanup: `great_depression_clear_market_exit_state` runs in `great_depression_reset_episode_policy_state` and `great_depression_clear_dynamic_state`, which covers episode start, abort, invalid retirement and recovery.
- Tooltips: each decision sets temporary values from the same constants and shows one custom tooltip naming the actor's relief, its duration and the partner's cost. The Severity line itself comes from `great_depression_apply_public_action_delta` (D23).
- AI: abandonment gains +8 when the partner is at Systemic Breakdown or worse (`great_depression_ai_partner_is_near_paralysis`) and is blocked for a faction member, ally, overlord or subject (`great_depression_ai_partner_is_close_ally`); Withdraw is now the retrencher's preferred quiet exit and is preferred for close allies; Exploit is blocked for close allies and when the actor's social strain is extreme.
- Evidence: `hoi4.decision_inspect` inspect mode, scenario `abandon_gambler_partner_near_paralysis` (GER liquidation gambler at Severity 75, HUN partner in its own crisis at Severity 90): base 10, +14 profile, +8 urgent, +8 near paralysis, score 40 before the close-ally factor, which stays unresolved because faction and alliance relations cannot be declared. Artifacts `decision-747f5175db1908b66a088471.json`, `probability-befa994aa735f70f3642704e.json`.
- Route blocker: `hoi4.probability_compare` was not run because the decision adapter of `hoi4.probability_inspect` still returns `INTERNAL_ERROR` (lead MCP note, 2026-10-05).

## D22. Competitive devaluation and withdrawal from international commitments (round 2 attempt 2, item 3)

Disposition: implemented.

- Basis: L2; spec part 7 "Competitive Devaluation or Currency Break" ("can help locally while raising pressure on partners") and the decision's own text ("a smaller role in global recovery").
- Devaluation: costs the market-clearing quote, is available once per country per global episode (`great_depression_devaluation_global_episode_id`, `great_depression_devaluation_is_unused`), gives standard relief (-3) at once and a trade-relief window (-2 for 84 days). Agent decision on the partner set: up to six partners, first the actor's contagion exposure targets, then registered worldwide-pressure countries with a proved relationship, receive a partner pressure window for 84 days: +2 worldwide exposure score (it can lift them into the severe contraction tier) and +1 hidden trade stress if they are in a national depression. Agent decision on the recovery term: each devaluation adds 20 days to the international-reconstruction proof, at most 60 days in total for one global episode (`global.great_depression_global_recovery_drag_days`, reset with the global ledgers). The text describes cheaper exports and lost partner sales and never names an exchange rate.
- Withdrawal: costs the policy-review quote (political power and stability), which `great_depression_can_pay_policy_review` and `great_depression_cost_policy_review` already pair. `great_depression_remove_global_contribution` removes the country's row and recorded industrial weight from the global ledger, its receipts and its contribution flags, including the Recovery of Nations candidate. `great_depression_commitments_withdrawn_global_episode_id` closes every global contribution decision through `great_depression_global_commitments_are_open`, which also guards `great_depression_increment_global_contribution`. The civilian commitment is released, Severity falls by 2 at once, and a fiscal-relief window (-2 for 84 days) follows.
- AI: devaluation is blocked during the Recovery and International Reconstruction stages, so the AI does not lengthen a proof that is already running; withdrawal keeps its retrencher and gambler weights and its recovery-stage block.
- Evidence (`hoi4.decision_inspect` inspect mode): devaluation, GER financial stabilizer at Severity 72 in Coordination, eligible, score 26 plus 8 if affordable (has_equipment cannot be declared); fiscal retrencher at Severity 60, eligible, 12 plus 8; the same stabilizer in the Recovery stage scores 0; a country that already devalued in the current global episode is not eligible. Withdrawal, ITA liquidation gambler in Coordination, eligible, 24 plus 8; already withdrawn, not eligible. Artifacts `decision-66fc598805568413265da5ff.json`, `probability-cef5c8bf8626bba8a5b5f4e9.json`, `decision-97cf94e2ef3d94186c0fabb1.json`, `probability-b7c81957c4a3dd8e201fb409.json`.

## D23. Severity line in every action tooltip (round 2 attempt 2, part of item 5)

Disposition: implemented for the shared Severity path; the per-decision consequence lines are tracked under item 5.

- Basis: L5; paradox_wiki Data structures (variable and flag effects have no tooltip); vanilla `common/national_focus/france.txt` (FRA_force_the_issue) shows a temporary variable set in an effect block feeding the tooltip of the next effect.
- `great_depression_apply_public_action_delta` shows `great_depression_severity_change_tt` ("Depression Severity: [?great_depression_action_delta|=-0]") whenever the change is not zero, from the same temporary value it adds, and wraps band, phase, spirit and modifier upkeep in `hidden_effect`.
- `great_depression_commit_country_action` and `great_depression_commit_external_action` hide the cost payment (already shown by the custom cost text) and the action receipt.

## D24. Episode flag lifecycle (round 2 attempt 2, item 6)

Disposition: implemented.

- Basis: L6; spec part 1 repeatability and acceptance tests I-01 and I-02.
- Own action and condition flags (`great_depression_clearing_agreement_active`, `_boom_supply_contract_active`, `_foreign_support_active`, `_supplier_contract_active`, `_emergency_credit_requested`, `_trade_failure`, `_supplier_contract_collapsed`, `_event34_supplier_pressure`, `_contagion_containment_action_receipt`, `_occupied_industry_socialized`) clear in `great_depression_clear_episode_action_flags`, called at episode start and from `great_depression_clear_dynamic_state`. In the recovery transaction that call comes after `great_depression_resolve_recovery_outcome`, `great_depression_apply_political_aftermath` (D18) and `great_depression_apply_country_scar` (D20), so the outcomes still read them.
- Agent decision on Event 34 timing: the collapse handoff and `great_depression_apply_supplier_collapse` set their flags after the opening reset, so a collapsing boom keeps its supplier pressure for the episode it opens.
- Agent decision on the partner-held flag: `great_depression_import_contract_shifted` lives on the partner that lost the contract, so it becomes a timed flag for `great_depression_market_exit.import_shift_pressure_days` (84), passed through a temporary variable, and it also clears in that partner's own episode cleanup.
- Containment Line: `great_depression_record_containment_action` writes the flag and `great_depression_containment_action_episode_id`; the achievement requires the id to match the current episode.
- `.tools/test_event035_center_projects.py` (15 tests) and `.tools/test_event035_inherited_hooks.py` (8 tests) pass.

## D25. A convened Global Recovery Conference (round 2 attempt 2, item 4)

Disposition: implemented; closes the D19 queued news for a failed recovery conference.

- Basis: L3; spec part 7 "Global Recovery Conference", "News and reports" and "Chaos impact".
- Convening: a country in its own depression, during Fragmented Recovery or International Reconstruction, in Stabilization or Recovery or with a falling Severity trend; one conference per global episode. Convening pays the reconstruction quote and no longer grants -8 Severity at once.
- Agent decision on the joining surface: countries in their own depression, countries with an open contagion exposure, Event 34 boom suppliers, and countries that contributed to the worldwide recovery in this global episode. The ordinary supplier surface ends at Fragmented Recovery, so earlier contributors stand in for it; the decision category opens for them while a conference sits, and the convener refreshes their cost quote. Joining pays the reconstruction quote outside the national and exposure slots; a country that withdrew from its international commitments cannot join.
- Agent decision on resolution: the daily global pulse resolves the conference on its due day (60 days). This replaces a hidden event because the pulse already runs daily, needs no extra event id, and still resolves when the convener has lost its crisis or ceased to exist.
- Agent decision on thresholds: at least 4 participants, 2 majors and 100 industrial weight (the global contribution weight: civilian factories twice, military factories and dockyards once, at most 100 per country), counted only for participants that still have a viable economy at resolution.
- Success: during Fragmented Recovery it starts a stopped proof or moves a running proof 30 days forward; during International Reconstruction it brings retirement 30 days closer. The proof still needs every ordinary condition. Participants in a depression lose 6 Severity; others gain `great_depression_recovery_conference_dividend` (+5% factory output growth, -2% consumer goods) for 120 days.
- Failure: during Fragmented Recovery the proof stops and the world returns to the Worldwide Depression stage, with one guarded +2 Chaos receipt per global episode, the "failed conference deepens the stage" case of spec part 7; during International Reconstruction the retirement wait restarts and no Chaos is added. The world news `chaosx.nr35.19` is sent once per global episode, names the convener, uses `GFX_news_event_great_depression`, and is skipped while the evolution is switched off.
- Cleanup: an open conference closes without an outcome when its global episode ends or retires or the evolution is switched off; the global ledger reset clears the receipts.
- AI: convening keeps its relief-coalition, stabilizer and recovery-stage weights, gains +10 for majors, and is blocked for liquidation gamblers; joining starts at 6, adds 16 for a country in its own depression, 10 for majors, 8 each for relief coalitions and financial stabilizers, 6 for earlier contributors, and is blocked for liquidation gamblers and outside the conference stages.
- Evidence (`hoi4.decision_inspect` inspect mode): convening, ENG relief coalition major in Stabilization during Fragmented Recovery: every non-cost gate true, score 42 plus 8 if affordable (convoy stock cannot be declared); the same country after a conference this global episode, during the Worldwide Depression stage, or in Depression with a rising trend is not eligible. Joining, FRA financial stabilizer major in its own depression with a conference open: score 40; ITA liquidation gambler: 0; eligibility stays unresolved only on convoy stock and the participant count. Artifacts `decision-6b6708b982294055572d7b79.json`, `probability-51c4ac9170b103f6d7979ec7.json`, `decision-3317150253e93138eeef928e.json`.
- needs_live_game: the failure news, the dividend modifier display, and a full conference cycle in a running worldwide episode.

## D26. Effect tooltips on every decision and mission (round 2 attempt 2, item 5)

Disposition: implemented.

- Basis: L5; paradox_wiki `Data structures - Hearts of Iron 4 Wiki.md` lines 119 and 526 (flags and variable effects have no tooltip; `custom_effect_tooltip` tells the player); vanilla `common/national_focus/france.txt` FRA_force_the_issue (a temporary variable set in the effect block feeds the following tooltip); spec part 10 "Severity and category text direction" (explain what changes Severity and what happens on success or failure, without a long hidden contributor ledger).
- All 124 effect blocks of the 79 decisions and 15 missions carry a `custom_effect_tooltip`; a source scan of `common/decisions/035_great_depression_decisions.txt` finds none missing, and all 86 new keys resolve once in `localisation/english/035_great_depression_l_english.yml`.
- Agent decision on the wording: lasting hidden pressure is shown per Severity update as "up to N lower/higher" with its duration, the same phrasing the D21 market-exit tooltips use, rather than as category scores. Numbers come from `great_depression_prepare_action_tooltip_values`, which reads the same constants as the effects.
- Agent decision on partner and boom tooltips: `great_depression_commit_partner_action` now commits outside its event-target block so the actor's Severity line appears in the tooltip; the Event 34 boom contract states its Severity relief in text because acceptance is decided by the Event 34 adapter at runtime.
- needs_live_game: the rendered tooltip layout, and whether the engine prints `country_event` or modifier lines that the source review could not predict.

## D27. Policy trade-offs that had no benefit (round 2 attempt 2, found while writing item 5)

Disposition: implemented.

- Basis: spec part 3 "Retrench the Relief Administration" (frees civilian capacity, supports the final proof, causes relapse used too early), "Ration Strategic Inputs" (protects selected output, raises pressure elsewhere), "Withdraw Emergency Support" (reduces fiscal pressure, increases short-term closure risk); the decision descriptions; CLAUDE.md section 5 (no shallow actions).
- Each of the three only raised Severity by 2 and set a flag that nothing read. Agent decision: each now leaves a lasting trade-off for the rest of the episode in `great_depression_rebuild_hidden_components` (constants `retrenchment_fiscal_relief`, `early_retrenchment_social`, `rationing_industrial_relief`, `rationing_trade_pressure`, `support_withdrawal_fiscal_relief`, `support_withdrawal_demand_pressure`). Retrenchment releases the paid civilian commitment and changes Severity by -2 in Stabilization or Recovery and +2 earlier, when it also sets `great_depression_relief_retrenched_early`, cleared at the episode reset. The existing AI weights already favor retrenchment in Stabilization and block it under high social strain, so they were kept.
- Agent decision on whiplash: `great_depression_event.policy_whiplash_days` (42) existed but whiplash never ended before the episode did; it is now a timed flag and a timed dynamic modifier, matching the "short-term whiplash" of the decision text.
- Agent decision on liquidation: a deliberately liquidated center (`great_depression_center_liquidated`) counted both the abandoned and the hollowed demand weight, so Abandon Depression Center and Auction or Reorganize Failed Assets cost +4 Severity and left more lasting pressure than the shuttered center they replaced. A liquidated center now adds only `demand_liquidated_center` (1), which gives the Let the Market Clear write-off its spec purpose of protecting the rest of the economy; centers lost to sustained failure keep the full weight.
- Defect fixes: Maximum-Severity Emergency's -6 relief was overwritten by the ordinary -4 mission relief inside `great_depression_mission_complete`; it now passes `great_depression_mission_relief_override`. Failed center projects incremented an unread `great_depression_center_project_failure_count`, so the National Employment Guarantee and the incident weights always saw zero failures; they now increment the per-episode `great_depression_project_failure_count`.
- AI evidence: no weight changed; `hoi4.probability_compare` stays blocked by the decision-adapter `INTERNAL_ERROR` recorded in the lead MCP note.

## D28. Clearing and protectionist blocs (round 2 attempt 2, item 7)

Disposition: implemented; closes the D19 queued news for bloc formation.

- Basis: L4; spec part 7 "Regional Clearing Agreement" (lowers exposure, can form a bloc, clear exit conditions), "Protectionist Bloc" (protects members from some external pressure while weakening global recovery, relations and nonmember trade), "News and reports" (formation of a major clearing or protectionist bloc), "End of global episode" (preserve blocs with a post-crisis purpose).
- Membership: two bounded global arrays (cap 12). Actor and partner both join; the clearing-bloc incident adds the crisis country and its incident partner. The never-read flags `great_depression_regional_clearing_partner` and the partner-only `great_depression_protectionist_bloc_member` path are gone; the member flags now mirror the arrays.
- Agent decision on clearing membership lifecycle: a 365-day term, renewed by joining again, ended early when a new national episode starts in the member or when it no longer exists. It survives global retirement and recovery because the payments arrangement keeps a post-crisis purpose. Relief applies only inside the member's own depression, so it never reaches a later episode.
- Agent decision on the protectionist effects: the actor's +2 Severity is gone. Shield: -2 worldwide exposure score for pressure countries and 0.15 instead of 0.35 global pressure on each Severity update for members in their own depression. Costs: `great_depression_protectionist_bloc_membership` (trade opinion -20%, which stands for lost relations and nonmember trade, plus consumer goods +2%) and 10 extra proof days per member, at most 40. Relations are represented through trade opinion rather than opinion modifiers on every nonmember, which would need a world scan.
- Agent decision on exclusivity: the blocs are not mutually exclusive, because one is a payments arrangement and the other a tariff wall; the spec's "no conflicting exclusive agreement" is met by the per-bloc room and new-member requirements.
- Formation news: `chaosx.nr35.20` and `chaosx.nr35.21`, once per bloc type per global episode, at three living members with a major, through `great_depression_queue_global_news`, which skips them while The Second Great Depression is switched off; they use `GFX_news_event_great_depression` (L7).
- AI: both clearing decisions add +12 for a close-ally partner and score 0 when both countries are already members; Protectionist Bloc adds +12 for a close ally and scores 0 during Fragmented Recovery and International Reconstruction.
- Evidence (`hoi4.decision_inspect` inspect mode): Protectionist Bloc, GER fiscal retrencher in Coordination: target root true, score unresolved only on the faction, subject and neighbour relations the scenario cannot bind (by source: base 10, +16 retrencher, +8 stable partner, +12 close ally); the same country during Fragmented Recovery scores 0; with GER and ITA already members the new availability gate `great_depression_protectionist_bloc_can_take_member` is false. Establish a Clearing Bloc, FRA financial stabilizer with BEL: both already members scores 0; a new pair is unresolved only on the same relation triggers. Artifacts `decision-0b146c20d7abf515ea7b4034.json`, `decision-265eeb2276821c7d474a2228.json`, `decision-61afbbd988ae9c7a33a70f35.json`.
- Route blocker: `hoi4.probability_compare` stays blocked by the decision-adapter `INTERNAL_ERROR` (lead MCP note).
- needs_live_game: the formation news in a running worldwide episode, the member modifiers in the country view, and the lighter contraction tier on a protectionist pressure country.
