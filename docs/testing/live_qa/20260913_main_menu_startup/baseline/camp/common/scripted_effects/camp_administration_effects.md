# Camp administration public contract

Status: implemented foundation; parent owns integration and complete-feature acceptance.
Acceptance: `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/accepted_implementation.md` and parent assignment.

## Data and controls

All population quantities end in `_k` and mean thousands of actual people, with 0.001 representing one person.
Detainees remain included in their current state's real civilian population.
Admission, release and closure never add or subtract population.
Only `camp_admin_record_deaths` invokes the shared physical death API.
State admission through `camp_admin_admit_detainees` is explicit: the caller supplies temporary `camp_admin_admission_requested_k` and `camp_admin_admission_source_k`, proving people already present in this state and not already detained, plus `camp_admin_admission_proven = 1`.
The helper clamps against source membership, free physical capacity, the state civilian floor, and a population share ceiling; it returns `camp_admin_admission_accepted_k` and consumes the proof.
There is no automatic intake from a pressure score or from the entire state population.
Site initialization creates an empty cohort and copies the existing registered responsible authority once into `camp_admin_responsible_country`.
That immutable evidence pointer and cumulative records survive capture and closure.

Country controls: `camp_admin_priority` industry=1, works=2, extraction=3; `camp_admin_mandate` custody=1, coercive=2, radical=3; `camp_admin_budget` maintenance=1, development=2, priority=3.
Defaults: industry, custody, maintenance.
Radical mandate requires `camp_admin_can_use_radical_mandate`, which combines the existing generic route and the major-country owner's distinct `camp_admin_country_can_radicalize`, rejects democratic government and forbids reform.
Site role `camp_admin_role` is custody=1, labor=2, penal=3, killing=4.
Only labor or penal roles plus an explicit coercive/radical national mandate produce forced-work output.
Violence mortality requires both killing-center role and a currently permitted radical mandate.
`camp_admin_site_suspended` suppresses productive allocations without ending custody, maintenance or its mortality obligations.
State cohort: `camp_admin_detainees_k`; capacity `camp_admin_capacity_k`; supported fraction `camp_admin_support_ratio`; allocations `camp_admin_industry_k`, `camp_admin_works_k`, `camp_admin_extraction_k` are mutually exclusive portions of surviving workforce.
Country display totals use `camp_admin_total_detainees_k`, `camp_admin_total_workforce_k`, `camp_admin_month_deaths_k`, `camp_admin_total_deaths_k`, and `camp_admin_industrial_factor`.
Cause enum: custody=1, labor=2, violence=3, institutional=4.
Each cause has state and responsible-country `camp_admin_month_<cause>_deaths_k` and `camp_admin_total_<cause>_deaths_k`.

## Public helpers and parent insertion points

`camp_admin_initialize_country = yes`: country; idempotent defaults and migration marker; call from eligible-country initializer.
`camp_admin_initialize_site = yes`: registered state; empty cohort initialization and immutable responsibility; call after `camp_rework_register_active_site` binds `genocide_responsible_country`.
`camp_admin_monthly_country = yes`: country; bounded iteration of `camp_active_site_states`, maintenance before development, cause outcomes, refresh and one calendar-month guard.
Parent must replace the legacy state percent-death pulse, not run both paths.
`camp_admin_record_deaths = yes`: state; temporary `camp_admin_death_requested_k`, `camp_admin_death_cause`, `camp_admin_death_contract = 1`; output `camp_admin_death_actual_k`; finite cohort and physical floor bounded.
`camp_admin_release_survivors = yes`: state; releases all surviving detainees in place, records release totals, clears allocations, preserves physical population; returns temporary `camp_admin_release_actual_k`.
`camp_admin_release_detainees = yes`: state; bounded release of temporary `camp_admin_release_requested_k`, returns actual surviving amount and consumes the request; the full release helper delegates here.
`camp_admin_close_site = yes`: state; release, remove modifiers, cancel support and active project references, preserve responsibility and cumulative records; call before current pointers and registry membership are erased.
`camp_admin_begin_reform = yes`: country; freeze admissions, release survivors, use paid civilian workforce replacement through the economy slot.
`camp_admin_reform_site = yes`: state; same-authority voluntary closure preserves a surviving-worker conversion target in `camp_admin_civilian_states`, without requiring national reform.
`camp_admin_reopen_site = yes`: state; only the same retained authority with valid control can reopen an empty location; neither cohorts nor historical records reset.
`camp_admin_refresh_country_economy = yes`: country; rebuild country output from live bounded site contributions.
`camp_admin_site_is_operational = yes`: state trigger; registration, current responsible controller, nonclosed state and current eligible authority.
`camp_admin_site_authority_is_valid = yes` permits direct control or a currently subordinate controller only when the owning historical kit explicitly set `camp_admin_subject_authority` for this institution.
No generic overlord-to-subject access exists.

## Population receipts and lifecycle

Capacity is 25,000 per physical camp building, a 5,000 fallback for an explicitly registered institutional marker, and 25,000 per completed paid development level, bounded by actual civilian headroom.
Intake also cannot exceed 20 percent of local civilian population minus existing detainees, the documented local source membership, or noncommitted headroom after `camp_occ_remaining_k` is reserved.
Capacity does not manufacture an intake source; country owners consume their declared source allowance by `camp_admin_admission_accepted_k` only.
The initial migration marker is `camp_admin_migration_v1`; it does not seed detainees from pressure, infer historical deaths or reset country-owner admissions.
If outside population loss makes an existing cohort larger than the remaining host population, the difference enters `camp_admin_external_attrition_k` without another physical debit or invented cause.

The existing exact civilian loss helper computes an accepted amount before its engine primitive runs.
To provide a measured receipt, `camp_admin_record_deaths` invokes `apply_exact_state_civilian_population_loss` with logging off, measures `state_population_k` before and after, then invokes `chaos_meter_register_deaths` with `chaos_deaths_apply_state_pop = 0` once for that actual loss.
The legacy `camp_rework_record_latest_state_deaths` remains an accounting projection only and runs once after the actual receipt.
The actual amount reduces the finite cohort and updates cause-separated site and original-authority month/cumulative records.
The largest individual API request is 1,000,000 people, with a 1,000-person protected host-state floor.
The Deaths-disabled setting suppresses the entire foundation mortality transaction.
`camp_admin_records_month` and `camp_admin_last_month` use actual calendar year/month, derived through current-year meta date comparisons; repeated callbacks on another day of the same month cannot pay or kill again.

Closing releases living people in place, removes state output, refreshes original-authority national output immediately and cancels matching project pointers.
It does not erase `camp_admin_responsible_country`, cumulative cause records, external attrition, admission or release history.
Different-authority reopening and locations already reserved for civilian conversion are deliberately rejected; a later distinct institution requires an explicit new authority-phase ledger instead of overwriting historical blame or counting the state in both workforce registries.
National reform and selected voluntary reform preserve surviving-worker replacement targets; four funded work programs convert 25 percent each into sustainable civilian work, with duration determined by each surviving civilian group and the required conversion work.
These people already remain civilians in the same state, so conversion adds no population and restores no deaths.
Infrastructure constructed by a completed works project remains after closure and reform.
The bounded `camp_admin_civilian_states` array must retain its country in the existing camp processor after the legacy active array retires.
Parent terminal-country cleanup must close these retained states and remove current economic modifiers before removing the country from processing.

## Economy, payment and tuning

`camp_admin_refresh_state_economy` derives mutually exclusive allocations from surviving supported workers, a 65 percent workforce share, the selected national priority and a clamped `camp_admin_site_output_scale` defaulting to one.
Industrial participation uses undamaged military factories and 10,000 allocated workers per factory equivalent; developed sites reach 40 percent equivalent output, aggregated over the responsible country's military-factory denominator and capped at 25 percent.
Construction uses up to 20,000 workers and a 40 percent developed maximum only while that state is the current live works project, through the vanilla-supported `state_production_speed_infrastructure_factor` for the project's actual building type.
Extraction uses existing local resource opportunity, 1,000 workers per resource unit and a 40 percent developed maximum.
There is no permanent construction bonus merely for having civilian factories or unfinished infrastructure.
Development level starts at zero with a 25 percent productive-development fraction; three completed upgrades reach the full fraction.

`camp_admin_prepare_project_quote` is read-only country-scope quotation: temporary `camp_admin_quote_support = 40` and `camp_admin_quote_pp = 0` for an ordinary monthly development installment.
`camp_admin_try_pay_project` accepts those explicit temporary quotes, checks both current physical stock/reserves and country remaining ceilings, pays only a complete positive quote, returns `camp_admin_payment_accepted`, and zeroes both quotes so they cannot be replayed.
Political-power quotes are supported for exceptional country-owner institutional administration; ordinary foundation maintenance and development consume no PP.
The shared support-equipment debit helper remains unmodified.
All active obligations are quoted first at 0.5 support equipment per thousand people per month.
The maintenance ceiling equals those existing obligations; development/priority budgets add 150/350 support-equipment units of optional development allowance.
Actual equipment after a 100-unit reserve determines funded support; all sites receive the same supported fraction before any project can spend.
The PP reserve is 20 and the remaining PP allowance is 5/15/35 for maintenance/development/priority tiers.
Any maintenance shortage blocks economic development progress that month.
Changing the budget tier does not make an existing million-person network impossible to maintain merely because a fixed small ceiling was exceeded.

Country project fields are `camp_admin_economy_state_id`, `camp_admin_economy_project_type` (priority enum 1–3; civilian conversion=4), `camp_admin_economy_progress` in completed work units, `camp_admin_economy_target` in required work units, and `camp_admin_economy_work_rate` in potential work units per funded monthly installment.
The GUI ratio is progress divided by target only when target is positive.
One economy slot and one institution slot are independent, while both draw from `camp_admin_budget_support_remaining` and `camp_admin_budget_pp_remaining` after maintenance.
Economic projects require enough supplied work, continuing control/support and a nonsuspended location.
`camp_admin_prepare_economy_work_target` freezes project size once per committed slot; ordinary refresh cannot shrink the target or discard partial work.
Industry, works and extraction targets start at two work units, add 0.01 units per thousand supported-capacity places and the real physical footprint: 0.20 per participating military factory, one per target infrastructure level, or 0.05 per existing resource unit respectively.
The result is multiplied by `1 + 0.50 * development_level`, so a later development stage requires more work.
A civilian conversion target starts at two work units and adds 0.04 per thousand people in the next finite quarter of its released-worker cohort.
All coefficients and the positive minimum target live in `camp_administration_constants.txt`.
Each paid installment contributes matching surviving assigned workers divided by 10,000, capped at four work units; supported allocations already include the funded support fraction.
Civilian conversion uses only the next unconverted finite group, bounded by remaining host population and funded support.
Zero workers or rejected material payment yield no progress and spend no development resources; reduced workers yield fractional work that persists through later interruptions.
The one-time `camp_admin_project_work_v2` migration preserves the completed fraction of an already committed legacy month-based slot against its historical three-month denominator, then freezes its work target.
New projects begin with zero work, and cancellation clears the work target, work rate and migration flag alongside the slot.
Insufficient support or payment pauses progress without spending; the parent lifecycle closes a lost target.
Completed works add one infrastructure level when below the vanilla maximum; industry/extraction upgrades improve supported capacity and contribution instead of creating free factories or resource deposits.
Completion publishes `camp_admin_economy_completed_this_month`, `camp_admin_economy_completed_state_id` and `camp_admin_economy_completed_type` for the parent history consumer.
`camp_admin_development_paused` defers new economy starts, including new civilian conversion installments, while an already committed project continues to meet its obligations.
The institutional owner must apply the same flag to its auto-start predicate.

Example admission from an owner-documented local cohort:

```txt
set_temp_variable = { camp_admin_admission_requested_k = 10 }
set_temp_variable = { camp_admin_admission_source_k = local_host_source_remaining_k }
set_temp_variable = { camp_admin_admission_proven = 1 }
camp_admin_admit_detainees = yes
subtract_from_variable = { local_host_source_remaining_k = camp_admin_admission_accepted_k }
```

This helper never authorizes an unknown source cohort; the caller's historical intake contract must identify the local membership and persist consumed headroom across closure/reopening.

## Institutional slot and award boundary

Independent flags: `camp_admin_economy_slot_active` and `camp_admin_institution_slot_active`.
Institution worker owns `camp_admin_institution_state_id`, `camp_admin_institution_progress`, program-specific requirements, authorization and suspension.
`camp_admin_try_claim_research_award = yes` is country scoped.
Inputs: temporary `camp_admin_research_requested_bonus` (fraction), plus `camp_admin_research_contract = 1`.
Requires occupied institutional slot, temporary proof `camp_admin_research_program_valid = 1`, and annual count below two.
Outputs: temporary `camp_admin_research_award_accepted` (0/1), `camp_admin_research_award_bonus` (0.5–1.0).
Success increments `camp_admin_research_awards_this_year` once and clears the slot flag; failure returns zero and preserves progress.
Country module applies `add_tech_bonus` only after accepted=1, with fixed stable program bonus name, `uses = 1`, and the returned bonus.
Country module must prevent repeated same-program awards and cancel/suspend support on regime or target loss.
Common helper does not create a research slot or choose research category.
Annual rollover uses actual `global.year`; there are at most two accepted awards across all programs per calendar year.

## Validation boundary

No new global hook, shared accounting change, AI weight or protected-group selector is part of this foundation.
Population, maintenance, allocation, project, reform, capture and annual-cap scenarios are evaluated against parsed source helpers.
MCP evidence and precise engine limitations are recorded in the focused handoff.
No new icons are required by these helpers; the parent owns existing/new GUI and modifier localisation.
Future extension: a supported construction-queue query could permit the construction allocation to support an engine-queued relevant building outside the named automatic project; no such undocumented query is invented here.
