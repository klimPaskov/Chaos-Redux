# Wider persecution and occupation accounting

Status: implemented bounded accounting module; historical calibration and engine evidence remain incomplete.
Acceptance basis: accepted_implementation.md and the parent acceptance on 2026-09-06 of national/regional aggregate ceilings apportioned by present state population, a one-time historical setup scan, and conservative outside-loss reconciliation followed by distinct finite campaign receipts.
The acceptance permits a documented geographic approximation; it does not establish historically exact state victim counts.

## Accounting contract

All `_k` quantities represent thousands of actual people.
A cohort reserves a finite subset of current state civilians outside `camp_admin_detainees_k`.
The foundation admission helper subtracts `camp_occ_remaining_k` before enrolling custody survivors.
Occupation enrollment excludes existing detainees and the protected population floor.
Neither enrollment nor release changes real population.
Each accepted death makes one call to `apply_exact_state_civilian_population_loss` with logging disabled, measures the before/after `state_population_k` difference, and makes one `chaos_meter_register_deaths` call with `chaos_deaths_apply_state_pop = 0`.
The latter is a projection only; `chaos_deaths_record_state_ledger = 1` also publishes that already measured receipt to the existing territorial ledger, and no legacy camp death wrapper is called.
The shared helper's precomputed `state_civilian_population_loss_applied` value is deliberately not treated as a measured receipt.
Each request is limited to 1,000 thousand people before conversion to people.

The country holds aligned, append-only cohort arrays with monotonic row IDs, root IDs, original states, current hosts, original authorities, profiles, living amounts, deaths, outside removals, releases, movements and statuses.
The state `camp_occ_remaining_k` remains the aggregate live reservation used by custody admission, and each state still has one responsible authority.
Enrollment creates a native row; a one-time bounded adoption creates rows for older state records without changing their totals.
Each row preserves its original state and responsible authority even when its living survivors move.
The state cannot be reseeded after capture, closure, exhaustion or reform.
The transfer helper uses a regular, same-chain destination event target; no global event target is created.
Persistent country arrays carry row identity and provenance.
The state's registry row is never reassigned to a conqueror, even when the former authority ceases to exist.
`camp_occ_transfer_survivors_exact` is a route-gated physical survivor transaction. Its first production caller is the dated Danish rescue in escape mode (`camp_occ_transfer_escape = 1`).
It rejects an absent destination, inactive or wrong-host row, invalid or fractional request, wrong authority, unaligned arrays, inadequate origin headroom, closed host, and failed destination control before touching physical population.
It measures the source debit and destination credit in whole people; any mismatch invokes physical inverse operations before metadata changes.
The destination event target expires with the effect chain and the temporary route inputs are consumed; an inverse mismatch leaves a sticky source rollback-failure flag for diagnosis and blocks another transfer attempt there.
An exact receipt splits the source row, appends a destination row with the original provenance, and updates only living aggregate reservations and movement totals.
Movement never projects a Deaths entry.
The ordinary occupation-to-occupation mode still has no named caller or engine receipt and rollback evidence; the separate dated Łódź occupation-to-custody route uses `camp_occ_transfer_to_custody_exact`.

### Dated Danish rescue

USHMM records that the largely independent Danish government kept Danish Jews out of German deportation until the order of October 1943, when about 7,200 people escaped across the Oresund to Sweden and about 470 were deported to Theresienstadt.
`camp_occ_origin_campaign_deferred` keeps the generic campaign off Danish-origin rows (origin state `is_core_of = DEN`) before 1943-10-01; this is dated policy timing, and the campaign rate is unchanged.
The same deferral keeps a Danish-origin host out of `camp_occ_manual_transfer_source_ready` until that date, so Germany's paid Auschwitz transfer order cannot deport a Danish cohort before the October 1943 order either.
From that date, `camp_occ_try_danish_rescue` runs in the German monthly pass before the campaign: each living Danish-origin row still at a German-controlled Danish home state sends `camp_occ_rescue.danish_escape_share` (0.94 = 7,200 / 7,670) of its living people, in whole people, to Skane (`camp_occ_rescue.refuge_anchor_state` 138) or, if Sweden does not hold Skane, to the Swedish capital.
The move uses `camp_occ_transfer_survivors_exact` in escape mode: one measured source debit and one measured refuge credit, or a full inverse; the arrival row keeps origin, root and German authority and is retired at once as released with no living amount, so the refuge never joins the camp registry and no death is recorded.
Each home state rescues once (`camp_occ_danish_rescue_done`); a cohort first exposed after October 1943 escapes in its first exposed month.
`camp_occ_danish_refuge_available` requires an existing Sweden that is not a German subject or faction member, is not at war with Denmark and is neutral or fighting Germany; otherwise nothing moves and nothing is recorded, and the residual cohort meets the campaign from October 1943.
Records count the escaped people in `camp_occ_total_escaped_k` (Occupation violence tooltip) and add one `escape` history entry per home state.
`docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/danish_rescue_source_tests.py` runs the production monthly pass from July 1941 to April 1945: the pre-change rule reproduces the rejected 2,859-death no-rescue model, while deferral plus rescue leaves 81 deaths with 3,940 escaped from 4,192 allocated people.

### Dated deportation start for Western and Greek origins

The same `camp_occ_origin_campaign_deferred` trigger holds the campaign and the manual order off the origin rows of five more occupied countries until their mass deportations began (USHMM): France before 1942-03-27 (first train to Auschwitz), the Netherlands before 1942-07-15 (first train from Westerbork), Belgium before 1942-08-04 (first train from Mechelen), Norway before 1942-10-26 (arrest of Jewish men by Norwegian police) and Greece before 1943-03-15 (first train from Salonika).
The rule reads the origin state's cores (`is_core_of`), like the Danish rule, which is unchanged; other origins, including Poland, the Soviet Union, the Baltic states, Czechoslovakia and Yugoslavia, are never deferred, and the campaign rate is unchanged.
`occupation/deportation_start_dates_source_tests.py` checks every boundary on the production trigger, runs the production monthly pass for the five changed states of the 13-state dated sensitivity and the manual-transfer source check, and reruns that sensitivity: modeled campaign deaths fall from 707,607 to 682,271 (France 25,347 to 21,166, the Netherlands 79,397 to 65,361, Belgium 13,431 to 9,898, Norway 316 to 244, Greece 8,434 to 4,920).

### Dated partner deportation (Hungary 1944)

USHMM records that about 825,000 Jews lived in wartime Hungary and that about 437,000 were deported, almost all to Auschwitz-Birkenau, between 15 May and 9 July 1944, when Horthy halted the deportations; they began only after Germany took control of the Hungarian government.
`camp_occ_try_partner_deportation` runs in the German monthly pass while `camp_occ_partner_deportation_window_open` holds (after 1944-05-14 and before 1944-07-10).
It needs a German authority with an active radical campaign, an existing Hungary that `camp_occ_partner_under_german_influence` accepts (a German subject, or a fascist government inside Germany's faction, and not at war with Germany) and an operational supported killing role at state 88 (`camp_occ_killing_destination_active`); otherwise nothing is registered, moved or recorded.
`camp_occ_register_partner_state` registers each European Hungarian-held state with an unregistered foreign origin cohort through `camp_occ_register_cohort` with the partner proof `camp_occ_source_partner = 1`: German responsibility, the state as origin and host, and `camp_occ_partner.hungary_deportation_share` (0.53 = 437 / 825) of the living origin ceiling after measured losses since the seed, bounded by the civilians present; the state gets `camp_occ_partner_host`.
The route then moves living people from those rows to state 88 through `camp_occ_transfer_to_custody_exact`, with the same wave bounds as the Lodz route: supported throughput per undamaged extermination level, resident and population-share capacity refreshed before every wave, the live row, source headroom minus one person, and at most `camp_occ_arrival.max_batches_per_month` waves.
`camp_occ_custody_partner_route = 1` lets `camp_occ_state_has_route_authority` accept the partner-held source for that one transaction; every other route still requires `camp_occ_state_has_current_authority`, so partner-held cohorts take no campaign violence and cannot feed generic movement, the Danish rescue or the manual order.
Each committed wave keeps origin, root and German responsibility on the bound custody row and requests arrival-phase violence on that row only (`camp_occ_apply_killing_arrival_loss`); one killing-center transfer history entry names each source state that moved people that month.
The monthly closure loop and the control-change callback keep a partner host open only while `camp_occ_state_has_partner_authority` holds; once the window lapses, Hungary leaves German domination or Germany loses its campaign, the host closes and its remaining order cohort is released at home.
A Hungarian state under direct German control follows the ordinary occupation path instead and is never registered twice.

#### Hungary's answer

Every partner check reads `camp_occ_partner_order_stands` (Hungary under German domination and not `camp_occ_partner_deportations_halted`) instead of the domination check alone.
When the first pass of the window places Hungarian-held cohorts under orders, Hungary (player or AI) receives `camp_occ_partner.1` once (`camp_occ_partner_order_notified`); the June waves of that pass still leave, so the answer governs the remaining transports.
- Let the trains run (`camp_occ_partner_comply_with_order`): nothing changes.
- Tell our officials to delay (`camp_occ_partner_obstruct_deportations`): each later pass multiplies the supported throughput by `camp_occ_partner.obstructed_wave_share` (0.5), and Germany's opinion of Hungary falls (`camp_occ_hungary_obstructed_deportations`, -20).
- Halt the deportations (`camp_occ_partner_halt_deportations`, also the paid decision `camp_occ_hun_halt_deportations` in the vanilla `political_actions` category while trains still run): the halt is permanent, so the next German pass closes every Hungarian host through `camp_occ_close_state` and releases the people still waiting at home with no death recorded, and the order never reopens. Hungary loses `camp_occ_partner_response.halt_stability` and `halt_war_support`, Germany's opinion falls (`camp_occ_hungary_halted_deportations`, -60), a German subject loses `@CAMP_OCC_HUNGARY_HALT_AUTONOMY` autonomy, and Germany receives `camp_occ_partner.2` and one `partner_halt` Records entry, once.
The decision costs the Event 026 sale price of `camp_occ_partner_response.halt_pp` and credits one Political Power purchase.
AI answers come from `camp_occ_partner_ai`: a fascist government complies (shares 0.78 / 0.20 / 0.02 for comply / delay / halt) and never takes the decision; a non-fascist German subject, the Horthy position, halts with 0.57 and weights the decision 10. USHMM: Horthy halted the transports on 7 July 1944.
In the partner suite, a halt after the June pass leaves 150,000 deported and releases 85,849 people at home; a delay holds July to 75,000 and releases 10,849.
If the decision was taken before the event was answered, the event offers only "The trains have already stopped" (`camp_occ_partner.1.e`).
Assets: no new art. The events use the vanilla `GFX_report_event_hungary_parliament` and `GFX_report_event_hungary_refused` (`interface/eventpictures.gfx`), and the decision uses the vanilla `GFX_decision_generic_protection` (`interface/decisions.gfx`). The opinion modifiers live in `common/opinion_modifiers/camp_occ_partner_opinion_modifiers.txt`; text is in `localisation/english/camp_administration_occupation_l_english.yml`.
The generic campaign rate is unchanged.
`docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/partner_deportation_source_tests.py` runs the production monthly pass from May to September 1944: with two supported extermination levels, 235,847 of the 235,849 people placed under orders move to state 88 (150,000 in June, the rest in July) with 153,297 arrival-phase deaths and no campaign death inside Hungary, and a Horthy-government Axis member, a Hungary outside the faction or at war with Germany, a state 88 without a killing role or under Soviet control, and dates outside the window register nothing.

## Public helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
|---|---|---|---|
| `camp_occ_historical_setup` | Country invocation in existing startup chain; no ROOT dependency | Once-only explicit country origin snapshots and GER/JAP controlled-state registration | Existing package startup, integration owner |
| `camp_occ_seed_origin = yes` | Historical country; required temporary origin ceiling | Fixed European owned-state denominator, per-state source ceilings and source-country unassigned residual | Explicit country calls inside setup |
| `camp_occ_track_controlled_state` | Actual state | Adds state to current GER/JAP authority's eligible array and attempts enrollment | Initial controlled-state scan and control-change callback |
| `camp_occ_on_state_control_changed` | Actual changed state | Closes former authority row when appropriate, tracks current eligible controller, preserves ROOT and event targets | Existing `genocide_on_state_control_changed`, integration owner |
| `camp_occ_initialize_country` | Country | Idempotent arrays and zero records; no policy selection | Registration and country callback |
| `camp_occ_try_register_current_state` | State, source snapshot or China-region membership | Builds explicit source contract; no loss | Bounded eligible registry and lifecycle insertion |
| `camp_occ_register_cohort` | State; temporary `camp_occ_source_proven = 1`, `camp_occ_source_requested_k`, `camp_occ_source_membership_k`, `camp_occ_source_authority`, `camp_occ_source_profile`; optional `camp_occ_source_partner = 1` for a partner-held candidate (`camp_occ_partner_deportation_candidate`) under a German authority, which also sets `camp_occ_partner_host` | `camp_occ_admitted_k`; consumes all request inputs on success and rejection, appends actual state to immutable authority's `camp_occ_states` | Enrollment adapter and `camp_occ_register_partner_state` |
| `camp_occ_backfill_cohort_origin` | Registered state; no input | Sets `camp_occ_cohort_origin_state = THIS` only when absent; no population, death, or authority changes | Bounded monthly row, control-change callback, closure |
| `camp_occ_initialize_rows` / `camp_occ_append_row` | Original authority country; append inputs staged from a state | Once-only legacy adoption and aligned country-owned row creation | Registration, monthly adoption and transfer commit |
| `camp_occ_stage_transfer_destination` | Actual destination state | Regular event target for the same effect chain | `camp_occ_try_danish_rescue` (refuge state) |
| `camp_occ_transfer_survivors_exact` | Actual source state; `camp_occ_transfer_route_proven = 1`, exact `camp_occ_transfer_row_id`, integer `camp_occ_transfer_requested_people`, staged destination; optional `camp_occ_transfer_escape = 1` for a refuge outside the authority's control (`camp_occ_rescue_refuge_state_valid`) | `camp_occ_transfer_result` and `camp_occ_transfer_committed_people`; measured physical debit/credit and rollback or exact row split; in escape mode the arrival row is retired as released, `camp_occ_total_escaped_k` grows on source and authority, and the refuge is not registered; consumes the route inputs; no death entry | `camp_occ_try_danish_rescue` (escape mode); no ordinary occupation-to-occupation caller |
| `camp_occ_try_danish_rescue` | GER country inside `camp_occ_monthly_country`, from 1943-10-01; valid refuge | Once per German-controlled Danish home state, moves the escaping share of each living Danish-origin row to Skane or the Swedish capital through the escape-mode receipt and records one `escape` history entry; nothing without a refuge | `camp_occ_monthly_country` |
| `camp_occ_preflight_custody_source` | Actual source state; exact `camp_occ_custody_row_id` and positive whole-person `camp_occ_custody_requested_people` | Read-only validation of aligned original-authority rows, source host, finite row/state/physical headroom; returns `camp_occ_custody_source_valid`, original state/root/authority and precommit snapshots | `camp_occ_transfer_to_custody_exact` only |
| `camp_occ_stage_custody_destination` | Actual destination state | Regular same-chain event target `camp_occ_custody_destination` | `camp_occ_try_lodz_auschwitz_transfer` in state 88 |
| `camp_occ_transfer_to_custody_exact` | Actual source state; one-shot `camp_occ_custody_route_proven = 1`, exact occupation row ID, positive whole-person amount and staged destination; optional one-shot `camp_occ_custody_partner_route = 1` lets a partner host pass `camp_occ_state_has_route_authority` | Exact source debit, destination credit and foundation custody bind; only matching receipts retire source occupation row and aggregate; outputs `camp_occ_custody_result`, `camp_occ_custody_committed_people` and named physical/bind/rollback receipts; consumes route inputs; no destination occupation row or Deaths entry | Dated `camp_occ_try_lodz_auschwitz_transfer`, dated `camp_occ_try_partner_deportation` and selected `camp_occ_try_manual_auschwitz_transfer` |
| `camp_occ_refresh_manual_transfer_source` | GER country; bounded `camp_occ_states` in registration order | Clears a stale selection, checks the current aligned native row and physical source margin, caps its whole-person share by real row and source headroom, and stores the first source that can fill the minimum order | Enrollment, monthly processing, control change, execution start and post-order refresh |
| `camp_occ_try_manual_auschwitz_transfer` | GER country ROOT with a refreshed `camp_occ_manual_source_state_id`; current authority, live native occupation row, supported state-88 killing role and affordability required | Quotes a whole-person request from the exact living row at `manual_auschwitz_living_share`, caps it by refreshed destination capacity/population-share headroom, source physical margin minus one person, live row and country aggregate, stages destination from state 88 and calls `camp_occ_transfer_to_custody_exact`; only a valid receipt can call bound-row arrival violence, while payment belongs to the decision effect | `camp_rework_germany_apply_exact_cohort_transfer` through one national `germany_transfer_prisoners_to_experiment_site` order |
| `camp_occ_apply_killing_arrival_loss` | Original GER country after a valid positive custody transfer, with bound destination row and active killing role | Requests `camp_occ_arrival.violence_request_fraction` of committed whole people, records only actual state-88 death receipts against the exact bound row, and returns `camp_occ_arrival_actual_k`; disabled or clipped requests leave survivors in custody | Dated Łódź and partner waves and paid manual order |
| `camp_occ_rollback_custody_transaction` | Actual source state, same effect chain | Calls `camp_admin_inverse_import_bind` first when a bind exists, then measures destination debit and source credit; an inverse mismatch or failed physical undo sets sticky `camp_occ_custody_rollback_failed` and suppresses retry | Failure path of custody transfer only |
| `camp_occ_apply_population_credit` / `camp_occ_apply_population_debit` | Actual state; temporary whole-person request | Measured actual whole-person receipt, with owner/controller manpower correction on positive credit | Transfer and same-chain rollback only |
| `camp_occ_try_lodz_auschwitz_transfer` | Original GER country within the monthly guard, 1944-08-09 through 1944-09-30; states 87 and 88 under current control, native source row, active campaign and operational supported killing-center destination | Reserves the proved living row once, attempts at most 12 batches per month within supported undamaged throughput and resident/population capacity, calls the exact occupation-to-custody transaction for each positive wave, subtracts only committed people from the pending and throughput budgets, then requests bound-row arrival violence; clears any unmoved remainder at the October cutoff | `camp_occ_monthly_country` |
| `camp_occ_stage_german_origin_request` | State with an assigned foreign origin | Stages `camp_occ_source_requested_k`: origin ceiling less the decline measured since the seed (at least the recorded deaths, at most the ceiling) | `camp_occ_try_register_current_state`, `camp_occ_register_partner_state` |
| `camp_occ_register_partner_state` | Partner-held candidate state; temp `camp_occ_partner_authority` (German authority) | Stages the order share of the origin request and calls `camp_occ_register_cohort` with the partner proof | `camp_occ_try_partner_deportation` |
| `camp_occ_try_partner_deportation` | Original GER country inside `camp_occ_monthly_country`, 1944-05-15 through 1944-07-09; Hungary under German domination; operational supported state-88 killing role | Registers partner-held cohorts once, moves living people in bounded exact waves to state 88, requests bound-row arrival violence and records one killing-center transfer history entry per source state per month | `camp_occ_monthly_country` |
| `camp_occ_monthly_country` | Country | One calendar-month guard using foundation month key, bounded eligible/source rows, dated Łódź route, monthly totals and active consequence | Existing active-country dispatch after foundation callback |
| `camp_occ_record_deaths` | State; temporary `camp_occ_loss_contract = 1`, `camp_occ_requested_k`, `camp_occ_loss_cause = constant:camp_occ_cause.campaign_violence` | `camp_occ_actual_k`, finite cohort debit and identical state/authority cause and cumulative receipt; consumes inputs | Monthly callback |
| `camp_occ_reconcile_external_population` | Registered state | Decreases exposure for observed outside population decline, records exposure removal only | Monthly callback, immediately before own debit, and closure |
| `camp_occ_close_state` / `camp_occ_close_country` | State / original country | Release remaining exposure in place, permanent closure, preserve deaths, original responsibility and registry history | Reform, control loss, annexation and special-country cleanup |
| `camp_occ_country_has_records` | Country trigger | True for nonempty eligible or admitted registries | Existing bounded country retention predicate |

The country arrays are aligned and append-only; indexes are scan positions and row IDs are stable identity.
Two original states can have separate rows at one destination under the same responsible authority.
`camp_occ_eligible_states` retains a bounded lifetime history; `camp_occ_states` contains accepted rows.
An unregistered source has no monthly loss and no authority attribution.
The custody transfer passes the occupation row's immutable original state, original authority and root ID to `camp_admin_preflight_import` and `camp_admin_bind_import` in the destination state.
The bind adds only destination custody membership; the occupation commit retires the same living amount at the source after source debit, destination credit and custody bind all return exact whole-person receipts.
The destination custody row is the later death and release owner, while source occupation history retains its original provenance and moved-out amount.
`camp_occ_custody_source_debit_people`, `camp_occ_custody_destination_credit_people`, `camp_occ_custody_bind_people`, `camp_occ_custody_bound_row_id`, `camp_occ_custody_inverse_people`, `camp_occ_custody_destination_undone_people` and `camp_occ_custody_source_restored_people` are same-chain temporary receipts for route review.
The source helper requires explicit route proof from its caller; its one-shot proof and request tokens are cleared after invocation, and a failed inverse quarantines the source state.
The dated country caller sets `camp_occ_lodz_auschwitz_transfer_recorded` when it proves and reserves one native row, so later months cannot invent a second source budget; each successful wave writes an exact source/destination receipt, while the monthly caller writes one killing-center transfer history entry if any wave succeeded that month.
The persistent `camp_occ_lodz_pending_people` and `camp_occ_lodz_source_row_id` are cleared on country closure or at the October cutoff, with no catch-up transfer.
`camp_occ_arrival.throughput_per_supported_level_k` is paid through the site support ratio already funded by monthly maintenance; it is separate from resident custody capacity and does not create another resource debit.
Arrival deaths are a measured subset of foundation violence totals at the destination, original authority country and aligned origin row; they are never an additional physical debit or a contribution to research progress.
The separate player/AI ordered route uses the same finite source row and exact destination bind but has its own manual share and paid decision contract.
Its decision availability and source-name localisation scan the registered array for a currently valid living row; the execution effect refreshes the oldest-source pointer before the exact transfer and again afterward.
The separate destination gate checks the current site row ledger, developed capacity, population-share space and uncommitted population for at least the minimum whole-person order.
The source gate checks aligned row arrays, live host/origin/authority, row status, a minimum living share, aggregate exposure and the strict physical population margin.
An external state change between UI refresh and effect execution can still reject the physical transaction; that rejection has no payment or false history entry.
It does not set the dated Łódź once-only flag or claim that its transfer represents the August–September 1944 episode.
The decision effect owns the debit and responsibility history only after a positive exact receipt; a rejected or rolled-back movement pays nothing.
The foundation preflight requires an initialized, aligned custody destination in state 88 with an operational supported killing-center role and `extermination_camp > 0`; the optional Mengele experiment marker is not a prerequisite, and a failed preflight changes no population or membership.
On a successful source commit, `camp_admin_import_bind_pending_inverse` is cleared; failure after a bind uses the inverse-first rollback path.
All cause record families have `camp_occ_month_*` and `camp_occ_total_*` projections in state and original country scope.
Violence, deprivation, deaths, exposure removed and survivors released remain distinct; exposure removed is never labeled an authority death.

## Source and tuning plan

`camp_occ_origin_k` stores 21 documented national estimates totaling 9,064,960 people.
These are circa-1933 source ceilings, not expected deaths or a complete 1939 population census.
The Soviet number applies to European territory only.
At startup, each source is apportioned over all of that country's European owned states by their then-current population shares, before later occupation is considered.
The seed marks states originally held by Germany with `camp_occ_home_german_origin`; both German occupation-admission gates exclude those states, leaving domestic German exposure to the separate national custody census. The original flag is stable if cores or owners later change, while foreign-origin states retain the possibility of occupation enrollment only under current control, campaign authority and finite headroom.
The unassigned country residual prevents rounding from allocating beyond the original ceiling.
Only controlled, policy-eligible state shares can be admitted; taking one quarter of an origin cannot concentrate its whole ceiling into that quarter.
An observed population decline between the source snapshot and first enrollment conservatively reduces that state's admissible share.
Population growth never expands the source ceiling.

The primary source is the [USHMM national population article, French edition](https://encyclopedia.ushmm.org/content/fr/article/jewish-population-of-europe-in-1933-population-data-by-country), read on 2026-09-06 after the English page failed to fetch.
It gives Poland 3 million, European USSR 2.525 million and Germany 525,000, alongside the other national estimates used in the constants.
The broader [USHMM European overview](https://encyclopedia.ushmm.org/content/en/gallery/jewish-population-of-europe) places the continental total around 9.5 million.
The difference is unmodeled source coverage, not a reserve that can be redistributed among occupied states.
State geometry, colonies, border changes, migration and national census dates make this an approximation rather than a documented Jewish population map.
The records identify the Holocaust's Jewish victims explicitly; the interface introduces no selectable demographic target.

The China-region adapter uses existing Chinese and Manchurian core geography, current direct Japanese control, and a one-time 90-percent present-civilian exposure share.
That 90-percent share is an accepted model parameter, not a historical census statistic or an estimate of casualties.
It leaves headroom for other civilian commitments and is clamped against actual population and current custody.
The historical comparison concerns combined civilian war and occupation losses, not institutional experimentation totals.
Richard B. Frank's [National WWII Museum interview](https://www.nationalww2museum.org/war/articles/asia-pacific-war-richard-b-frank) describes roughly 4,000 Chinese noncombatant deaths per day across eight years, approximately 11.7 million, within a broader Asian catastrophe.
That estimate includes multiple causes and cannot be assigned wholesale to this module or to one institutional site.
The [NARA Japanese war-crimes collection guide](https://www.archives.gov/iwg/japanese-war-crimes) supplies archival provenance for distinct responsibility records, not a replacement state population distribution or a complete casualty census.

The Holocaust comparison is [USHMM's six million Jewish victims across the wider murder campaign](https://encyclopedia.ushmm.org/content/en/article/the-final-solution).
This includes events beyond concentration-camp custody.
The [USHMM account of the invasion of the Soviet Union](https://encyclopedia.ushmm.org/content/en/article/invasion-of-the-soviet-union-june-1941) supports the June 1941 escalation gate.
It does not imply that persecution began in June 1941 or that earlier victims did not exist.

Deterministic monthly fractions are 0.001 for the China occupation campaign and 0.025 for the German campaign, applied to remaining finite exposure.
They are model tuning values, not historical per-person probabilities, random draws, AI weights, or a death quota.
No reward, output or research bonus depends on the number of deaths.
Chronology and enacted mandate are independent gates: Japan requires a qualifying regime, coercive/radical mandate and 1937-07-07 or later; Germany requires the Nazi authority trigger, radical mandate and 1941-06-22 or later.
No automatic 1945 cutoff rewrites an alternate war outcome; valid continuing authority may persist through 1948 and later, while regime/policy/control loss closes exposure and preserves aftermath records.

## Shared overlap and conservation

The core already charges generic occupation-law mortality in `common/scripted_effects/chaos_meter_effects.txt` when the state is not owned and controlled by its controller and has resistance.
Those deaths and campaign-specific violence are separate transactions against a shrinking population.
Before a campaign transaction, the common physical-host observer compares net decline, positive shared territorial Deaths growth and current combined reservation headroom.
Those observations can overlap and are not added as victim counts.
When exactly one proved row is present, its owner retires the bounded conservative exposure through that exact positive row ID and verifies the resulting outside-removal receipt.
When origins, roots or memberships mix, the host instead retains sticky ambiguity and frozen row/aggregate snapshots.
Observation and retirement make no physical debit or attributed death entry.
After a measured package death and its completed row/shared projection, the common canonical baseline is adjusted to the measured receipt so another family cannot consume it as outside loss.
Generic occupation laws therefore do not suppress the separate campaign transaction.
The deprivation constant is zero and the death adapter rejects the deprivation cause, so it cannot become a second generic occupation debit through a caller.
No all-cause territorial ledger is used to assign responsibility; it can only remove exposure conservatively.

An unlabelled outside signal can conservatively retire up to the entire sole proved exposed row, without declaring that those people died under a camp cause.
Known package deaths and movements are excluded through their completed measured endpoint receipts.
Other territorial losses have no source-labelled cohort distribution and can undercount uniquely reserved exposure through this conservative rule.
The territorial death ledger prevents population growth or inward transfers from hiding recorded deaths between observations.
Unlogged outward movement exactly offset by inward movement is not recoverable from the present public snapshots; no known generic occupation debit has that problem because its public routine writes the territorial death ledger synchronously.
This remains aggregate conservative membership accounting, not individual identity reconstruction.
Mixed-origin observation never calls a physical-loss API, projects Deaths, allocates losses newest-first/proportionally or creates an unknown-origin continuation pool.
The accepted policy pauses origin-specific deaths and both movement/import endpoints until full source-labelled provenance can be restored.
No complete external-loss recovery provider is implemented.
Terminal capture/closure stops the occupation programme while preserving uncertain original rows, original authority and historical cause records without a fabricated release count.
National reform preflights the complete bounded custody/occupation union before policy flags or survivor-derived outcomes advance.
Conservation for each root family is `admitted = living across hosts + own measured deaths + exposure removed + released survivors`.
For an individual row, living transfers count as moved out or moved in, not as deaths.

Every movement retains independent source/destination opening sequences and physical/shared-counter images.
Both endpoints adjust their common baselines only after complete physical and row commit or a complete measured inverse.
A failed inverse persists measured debit/credit/bind/inverse residuals and both endpoint pointers before the regular target expires, quarantines both endpoints and preserves the verified opening baseline.
Separate quarantine observation checkpoints record subsequent territory changes without calling the already-known partial movement another outside loss.
The existing bind-before-physical-undo ordering remains unchanged.
The generic occupation-to-occupation helper still has no named production route consumer, but joined tests execute its production receipt and conservation logic.

## Validation, omissions and next work

The focused `occupation/test_occupation_accounting.py` checks actual receipts, physical/custody floors, partial control, repeated month, interleaved outside/custody/campaign losses, growth masking net population decline, capture and annexation attribution, release without population creation, and million-scale finite scenarios using parsed source constants.
It is an arithmetic model with source assertions, not a Clausewitz interpreter or in-game proof.
The all-covered-origin 48-month unblocked capacity scenario produces approximately 6.376 million deaths and the 100-million China-region, 96-month unblocked scenario approximately 8.242 million incremental deaths.
Neither is a historically calibrated campaign: dates of control, missing origins, custody overlap, competing losses and demographic movements materially alter the result.
Do not describe either result as meeting the six-million historical acceptance requirement.

The narrow `hoi4.event_inspect` returned partial event evidence and `hoi4.map_inspect` returned state 43/88 map evidence; artifact references and limits are recorded in the focused cross-state handoff.
The dated Łódź caller is wired through `camp_occ_monthly_country`, but no engine receipt or rollback proof or dated control scenario establishes that it executes in natural 1944 play.
The separate occupation-to-custody transaction is implemented as package infrastructure and covered by focused source/model scenarios; it has not been accepted by the Clausewitz engine, and the required killing-center role and site support in natural play remain unproven.
No focus, GUI, map data, AI weight or random probability source is edited by this module.
GUI presentation and final parent source/MCP validation remain integration-owned.
No new icons or artwork are required; the records text uses the parent's existing records view and sprite family.
Future work must validate actual campaign chronology against historically occupied geography and add documented source/transfer coverage where supported.
The incomplete historical calibration is a blocker, not a silent substitute for the accepted full-period requirement.

## Origin input contract

Initialize temporary `camp_occ_origin_ceiling_input_k` with the explicit `constant:camp_occ_origin_k.<origin>` before `camp_occ_seed_origin = yes`.
The country helper copies that required input into `camp_occ_origin_initial_ceiling_k` inside its existing once-only guard.
All 21 origin calls retain their exact constant keys, owned-European-state denominator, immutable origin attribution and residual accounting.
No default ceiling, target, population movement or cleanup is introduced.
