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

State identity is the state itself, admitted once; one immutable `camp_occ_responsible_country` and `camp_occ_profile_id` are assigned on acceptance.
The state cannot be reseeded after capture, closure, exhaustion or reform.
No regular or global event target is created or overwritten.
Persistent state and country variables carry the evidence pointer and records instead.
The state's registry row is never reassigned to a conqueror, even when the former authority ceases to exist.
This module intentionally has no cross-state cohort movement; any future transfer must use an exact survivor transfer receipt and preserve identity.

## Public helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
|---|---|---|---|
| `camp_occ_historical_setup` | Existing startup chain, no ROOT dependency | Once-only explicit country origin snapshots and GER/JAP controlled-state registration | Existing package startup, integration owner |
| `camp_occ_seed_origin = { ORIGIN = pol }` | Historical country; fixed constant suffix | Fixed European owned-state denominator, per-state source ceilings and source-country unassigned residual | Explicit country calls inside setup |
| `camp_occ_track_controlled_state` | Actual state | Adds state to current GER/JAP authority's eligible array and attempts enrollment | Initial controlled-state scan and control-change callback |
| `camp_occ_on_state_control_changed` | Actual changed state | Closes former authority row when appropriate, tracks current eligible controller, preserves ROOT and event targets | Existing `genocide_on_state_control_changed`, integration owner |
| `camp_occ_initialize_country` | Country | Idempotent arrays and zero records; no policy selection | Registration and country callback |
| `camp_occ_try_register_current_state` | State, source snapshot or China-region membership | Builds explicit source contract; no loss | Bounded eligible registry and lifecycle insertion |
| `camp_occ_register_cohort` | State; temporary `camp_occ_source_proven = 1`, `camp_occ_source_requested_k`, `camp_occ_source_membership_k`, `camp_occ_source_authority`, `camp_occ_source_profile` | `camp_occ_admitted_k`; consumes all request inputs on success and rejection, appends actual state to immutable authority's `camp_occ_states` | Enrollment adapter |
| `camp_occ_monthly_country` | Country | One calendar-month guard using foundation month key, bounded eligible/source rows, monthly totals and active consequence | Existing active-country dispatch after foundation callback |
| `camp_occ_record_deaths` | State; temporary `camp_occ_loss_contract = 1`, `camp_occ_requested_k`, `camp_occ_loss_cause = constant:camp_occ_cause.campaign_violence` | `camp_occ_actual_k`, finite cohort debit and identical state/authority cause and cumulative receipt; consumes inputs | Monthly callback |
| `camp_occ_reconcile_external_population` | Registered state | Decreases exposure for observed outside population decline, records exposure removal only | Monthly callback, immediately before own debit, and closure |
| `camp_occ_close_state` / `camp_occ_close_country` | State / original country | Release remaining exposure in place, permanent closure, preserve deaths, original responsibility and registry history | Reform, control loss, annexation and special-country cleanup |
| `camp_occ_country_has_records` | Country trigger | True for nonempty eligible or admitted registries | Existing bounded country retention predicate |

The arrays hold state references only; metadata and amounts remain on that unique state, so there is no multi-array index alignment to drift.
`camp_occ_eligible_states` retains a bounded lifetime history; `camp_occ_states` contains accepted rows.
An unregistered source has no monthly loss and no authority attribution.
All cause record families have `camp_occ_month_*` and `camp_occ_total_*` projections in state and original country scope.
Violence, deprivation, deaths, exposure removed and survivors released remain distinct; exposure removed is never labeled an authority death.

## Source and tuning plan

`camp_occ_origin_k` stores 21 documented national estimates totaling 9,064,960 people.
These are circa-1933 source ceilings, not expected deaths or a complete 1939 population census.
The Soviet number applies to European territory only.
At startup, each source is apportioned over all of that country's European owned states by their then-current population shares, before later occupation is considered.
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
Before a campaign transaction, the module retires exposure equal to the greatest of net observed population decline, positive growth of the shared state civilian-death ledger converted to thousands, or the shortfall between recorded exposure and current noncustody civilian headroom.
This maximum is capped at remaining exposure; the three measurements are not added, since they can describe the same loss.
It makes no physical debit and creates no attributed death entry.
After the new measured campaign debit and its projection, both observation baselines advance, so its own receipt cannot be consumed as an outside loss next month.
Generic occupation laws therefore do not suppress the separate campaign transaction.
The deprivation constant is zero and the death adapter rejects the deprivation cause, so it cannot become a second generic occupation debit through a caller.
No all-cause territorial ledger is used to assign responsibility; it can only remove exposure conservatively.

Observed outside population decline or recorded outside civilian deaths remove up to the entire remaining exposed cohort before another module-owned loss.
It may include already-accounted camp deaths, migration, combat or other events; its attribution remains unknown.
This is deliberately conservative and can undercount remaining exposure.
The territorial death ledger prevents population growth or inward transfers from hiding recorded deaths between observations.
Unlogged outward movement exactly offset by inward movement is not recoverable from the present public snapshots; no known generic occupation debit has that problem because its public routine writes the territorial death ledger synchronously.
This remains aggregate conservative membership accounting, not individual identity reconstruction.
Unknown removal never calls the physical-loss API and never projects a Deaths entry.
Conservation for each row is `initial = remaining + own measured deaths + exposure removed + released survivors`.

## Validation, omissions and next work

The focused `occupation/test_occupation_accounting.py` checks actual receipts, physical/custody floors, partial control, repeated month, interleaved outside/custody/campaign losses, growth masking net population decline, capture and annexation attribution, release without population creation, and million-scale finite scenarios using parsed source constants.
It is an arithmetic model with source assertions, not a Clausewitz interpreter or in-game proof.
The all-covered-origin 48-month unblocked capacity scenario produces approximately 6.376 million deaths and the 100-million China-region, 96-month unblocked scenario approximately 8.242 million incremental deaths.
Neither is a historically calibrated campaign: dates of control, missing origins, custody overlap, competing losses and demographic movements materially alter the result.
Do not describe either result as meeting the six-million historical acceptance requirement.

The attempted narrow `hoi4.event_inspect` route timed out after 180 seconds before returning evidence.
Map inspection status and final test result are recorded in the focused handoff.
No focus, GUI, map data, AI weight or random probability source is edited by this module.
GUI presentation and final parent source/MCP validation remain integration-owned.
No new icons or artwork are required; the records text uses the parent's existing records view and sprite family.
Future work must validate actual campaign chronology against historically occupied geography and add documented source/transfer coverage where supported.
The incomplete historical calibration is a blocker, not a silent substitute for the accepted full-period requirement.
