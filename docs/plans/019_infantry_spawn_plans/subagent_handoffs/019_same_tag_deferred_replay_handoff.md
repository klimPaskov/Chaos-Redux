# Event 19 Same-Tag Deferred Replay Handoff

> Current extension note (2026-07-15): the later Evolution II prototype
> maintenance mission adds a tenth mission route and raises the live contract to
> 53 routes. Counts below describe the original independently audited 52-route
> tranche; the added route is mapped in the parent audit packet and remains
> inside the pending specialist/final audit scope.

## Scope and outcome

Implemented transaction-safe replay for all 52 requested Event 19 mutation paths owned by this tranche:

- 9 activated-mission timeout effects;
- 39 incident report options across `chaosx.nr19.300` through `.312`;
- 2 Evolution III prefire report options on `chaosx.nr19.2`;
- 2 claimant-demand report options on `chaosx.nr19.201`.

Every routed path executes its original gameplay effect immediately only when `infantry_spawn_scenario_transaction_is_idle = yes`. While locked, the path records only its exact deferred selection and stable identity. No deferred replay substitutes another row, state, claimant, demand, or choice when proof fails.

## Files changed

- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
- `common/script_constants/019_infantry_spawn_constants.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_ledger_triggers.txt`
- `common/decisions/019_infantry_spawn_decisions.txt`
- `events/019_infantry_spawn.txt`
- this handoff

No commit was created.

## Public replay contract

- `infantry_spawn_resume_deferred_management_completions`: mission-only replay entry point for all nine mission records.
- `infantry_spawn_resume_deferred_incident_choice`: replays the one pending incident selection after exact lot-UID proof and any resource recheck.
- `infantry_spawn_resume_deferred_prefire_opening_choice`: replays the stored draw or decline only while the original opening remains pending.
- `infantry_spawn_resume_deferred_claimant_demand_choice`: resolves the stored claimant UID, proves the stored demand, rechecks acceptance affordability, and executes the stored response.
- `infantry_spawn_resume_deferred_event19_actions`: aggregate entry point, ordered prefire, claimant, incident, then mission completions.

The aggregate is not called from `infantry_spawn_run_country_management_pulse`. Current shared-workspace integration calls it from `infantry_spawn_scenario_finish_same_tag_transaction` after transaction flags clear and the stable view rebuilds, and from the idle branch of `infantry_spawn_run_country_pulse` before subsequent pulse mutation. The scenario finish performs a second view rebuild after replay.

`infantry_spawn_run_country_management_pulse` itself now requires the transaction-idle trigger. `infantry_spawn_settle_selected_lot_exact_obligations` is an idle-only public wrapper around `infantry_spawn_settle_selected_lot_exact_obligations_unlocked`, preventing initial refresh or any public caller from debiting obligations during a lock.

## Mission timeout coverage

| Mission | Timeout wrapper | Deferred identity/proof |
|---|---|---|
| Formation roll call | `infantry_spawn_defer_or_complete_selected_lot_audit` | immutable audit lot UID plus original running flag; original completion owns live-row and terminal-state handling |
| Standardization cycle | `infantry_spawn_defer_or_complete_selected_lot_standardization` | immutable standardization lot UID plus original running flag; original completion owns live-row and terminal-state handling |
| Supervised demobilization | `infantry_spawn_defer_or_complete_supervised_demobilization` | immutable demobilization lot UID plus original running flag; original completion owns live-row and terminal-state handling |
| Training cycle | `infantry_spawn_defer_or_complete_selected_lot_training` | immutable training lot UID plus original running flag; original completion owns live-row and terminal-state handling |
| Muster districts | `infantry_spawn_defer_or_complete_muster_districts` | dedicated pending flag plus original running flag |
| Integration staff search | `infantry_spawn_defer_or_complete_integration_staff_search` | dedicated pending flag plus original running flag |
| Specialist preservation | `infantry_spawn_defer_or_complete_specialist_preservation` | immutable specialist lot UID plus original running flag; original completion owns live-row and terminal-state handling |
| Rail corridor | `infantry_spawn_defer_or_complete_rail_corridor_mission` | exact stored state plus original running flag |
| Request cooldown | `infantry_spawn_defer_or_finish_request_cooldown` | dedicated pending flag only, as required |

Each record is independent; the mission-only resume effect uses separate calls rather than an exclusive branch, so simultaneous expirations all remain replayable. Replay restores the immutable UID or state to the original target and calls the original completion whenever the original running context still exists. That original completion owns semantic drift, failure, and unconditional cleanup. Structurally malformed records instead enter the shared replay/ledger invariant quarantine, clear only their exact original and deferred context, and never substitute another row.

## Incident choice enum and call-site proof

The current bounded implementation uses the following named values from `infantry_spawn_deferred_incident_choice` in `common/script_constants/019_infantry_spawn_constants.txt` at the event options, affordability checks, and central dispatcher. No raw route IDs remain at those call sites.

| ID | Event option | Constant key | Original effect | Replay resource proof |
|---:|---|---|---|---|
| 1 | `chaosx.nr19.300.a` | `barracks_local_authority` | `infantry_spawn_incident_barracks_local_authority` | none |
| 2 | `chaosx.nr19.300.b` | `barracks_regular_army` | `infantry_spawn_incident_barracks_regular_army` | none |
| 3 | `chaosx.nr19.300.c` | `barracks_provisional_committee` | `infantry_spawn_incident_barracks_provisional_committee` | none |
| 4 | `chaosx.nr19.301.a` | `ammunition_divert_production` | `infantry_spawn_incident_ammunition_divert_production` | infantry equipment |
| 5 | `chaosx.nr19.301.b` | `ammunition_cannibalize` | `infantry_spawn_incident_ammunition_cannibalize` | none |
| 6 | `chaosx.nr19.301.c` | `ammunition_delay` | `infantry_spawn_incident_ammunition_delay` | none |
| 7 | `chaosx.nr19.302.a` | `motor_pool_territorial` | `infantry_spawn_incident_motor_pool_territorial` | none |
| 8 | `chaosx.nr19.302.b` | `motor_pool_rebuild` | `infantry_spawn_incident_motor_pool_rebuild` | motorized equipment |
| 9 | `chaosx.nr19.302.c` | `motor_pool_accept_burden` | `infantry_spawn_incident_motor_pool_accept_burden` | none |
| 10 | `chaosx.nr19.303.a` | `village_territorial_service` | `infantry_spawn_incident_village_territorial_service` | none |
| 11 | `chaosx.nr19.303.b` | `village_enforce_transfer` | `infantry_spawn_incident_village_enforce_transfer` | none |
| 12 | `chaosx.nr19.303.c` | `village_supply_bargain` | `infantry_spawn_incident_village_supply_bargain` | support equipment |
| 13 | `chaosx.nr19.304.a` | `officers_regularize` | `infantry_spawn_incident_officers_regularize` | none |
| 14 | `chaosx.nr19.304.b` | `officers_disperse` | `infantry_spawn_incident_officers_disperse` | none |
| 15 | `chaosx.nr19.304.c` | `officers_preserve_cadre` | `infantry_spawn_incident_officers_preserve_cadre` | none |
| 16 | `chaosx.nr19.305.a` | `staff_merge` | `infantry_spawn_incident_staff_merge` | none |
| 17 | `chaosx.nr19.305.b` | `staff_favor_regular` | `infantry_spawn_incident_staff_favor_regular` | none |
| 18 | `chaosx.nr19.305.c` | `staff_reserve_command` | `infantry_spawn_incident_staff_reserve_command` | none |
| 19 | `chaosx.nr19.306.a` | `depot_absorb` | `infantry_spawn_incident_depot_absorb` | none |
| 20 | `chaosx.nr19.306.b` | `depot_preserve` | `infantry_spawn_incident_depot_preserve` | none |
| 21 | `chaosx.nr19.306.c` | `depot_strip` | `infantry_spawn_incident_depot_strip` | none |
| 22 | `chaosx.nr19.307.a` | `colors_recognize` | `infantry_spawn_incident_colors_recognize` | none |
| 23 | `chaosx.nr19.307.b` | `colors_refuse` | `infantry_spawn_incident_colors_refuse` | none |
| 24 | `chaosx.nr19.307.c` | `colors_territorial` | `infantry_spawn_incident_colors_territorial` | none |
| 25 | `chaosx.nr19.308.a` | `tanks_engineers` | `infantry_spawn_incident_tanks_engineers` | support equipment and army experience |
| 26 | `chaosx.nr19.308.b` | `tanks_one_offensive` | `infantry_spawn_incident_tanks_one_offensive` | none |
| 27 | `chaosx.nr19.308.c` | `tanks_dismantle` | `infantry_spawn_incident_tanks_dismantle` | none |
| 28 | `chaosx.nr19.309.a` | `rotorcraft_maintain` | `infantry_spawn_incident_rotorcraft_maintain` | support and motorized equipment |
| 29 | `chaosx.nr19.309.b` | `rotorcraft_ceremonial` | `infantry_spawn_incident_rotorcraft_ceremonial` | none |
| 30 | `chaosx.nr19.309.c` | `rotorcraft_field` | `infantry_spawn_incident_rotorcraft_field` | none |
| 31 | `chaosx.nr19.310.a` | `radios_standardize` | `infantry_spawn_incident_radios_standardize` | support equipment |
| 32 | `chaosx.nr19.310.b` | `radios_accept_penalty` | `infantry_spawn_incident_radios_accept_penalty` | none |
| 33 | `chaosx.nr19.310.c` | `radios_split_command` | `infantry_spawn_incident_radios_split_command` | none |
| 34 | `chaosx.nr19.311.a` | `cavalry_keep_horses` | `infantry_spawn_incident_cavalry_keep_horses` | none |
| 35 | `chaosx.nr19.311.b` | `cavalry_force_trucks` | `infantry_spawn_incident_cavalry_force_trucks` | motorized equipment |
| 36 | `chaosx.nr19.311.c` | `cavalry_mixed_doctrine` | `infantry_spawn_incident_cavalry_mixed_doctrine` | none |
| 37 | `chaosx.nr19.312.a` | `armored_cars_recon` | `infantry_spawn_incident_armored_cars_recon` | none |
| 38 | `chaosx.nr19.312.b` | `armored_cars_retrain` | `infantry_spawn_incident_armored_cars_retrain` | army experience |
| 39 | `chaosx.nr19.312.c` | `armored_cars_preserve` | `infantry_spawn_incident_armored_cars_preserve` | none |

Incident dispatch now records `infantry_spawn_incident_lot_uid` before opening the report. The option copies that immutable UID rather than deriving identity from a potentially stale row index. Replay additionally proves that the original pending incident UID still matches, resolves the current row by UID, proves the live ordinary-lot state, and only then calls the original effect. Costly choices recheck the same resource combinations used by their option triggers. The deferred record clears only after an enumerated original effect ran and cleared `infantry_spawn_incident_pending`.

## Prefire and claimant option mapping

The prefire and claimant popup routes likewise use the named `infantry_spawn_deferred_prefire_choice` and `infantry_spawn_deferred_claimant_choice` constants:

| Surface | ID | Event option | Suggested key | Original effect |
|---|---:|---|---|---|
| Prefire | 1 | `chaosx.nr19.2.b` | `draw` | `infantry_spawn_execute_prefire_evolution_iii_initial_draw` |
| Prefire | 2 | `chaosx.nr19.2.c` | `decline` | `infantry_spawn_decline_prefire_evolution_iii_initial_draw` |
| Claimant | 1 | `chaosx.nr19.201.a` | `accept` | `infantry_spawn_accept_selected_claimant_demand` |
| Claimant | 2 | `chaosx.nr19.201.b` | `refuse` | `infantry_spawn_refuse_selected_claimant_demand` |

The claimant record stores the exact claimant UID and demand value. Replay resolves that UID with `infantry_spawn_find_claimant_row`, proves the same bounded demand on the resolved row, temporarily selects that row for the existing response triggers/effects, and restores the stable-view selection afterward. Acceptance calls the existing exact affordability trigger at replay time. A temporarily unaffordable exact acceptance remains pending; a structurally invalid record is quarantined without executing another response. The only post-accept retry is the intentional `another_formation` route whose original demand remains pending.

## Validation evidence

- All 9 mission `timeout_effect` blocks call deferred wrappers; none directly call the original completion effects.
- Event parsing found exactly 39 incident request IDs, 2 prefire request IDs, and 2 claimant request IDs.
- Incident call-site enumeration is contiguous and unique from `.300.a = 1` through `.312.c = 39`; the central dispatcher has exactly 39 matching branches.
- No direct incident, prefire, or claimant original mutation effect remains in the owned event file.
- Structurally orphaned mission, incident, prefire, and claimant records fail closed through one shared invariant/quarantine path; temporary affordability failures remain retryable.
- The shared deferred-action trigger exactly covers all 12 authoritative pending flags and is the single compaction gate.
- Braces balance in all three gameplay files after the edits.
- The aggregate replay effect is not called inside the management pulse, and no recurring on-action was added.

## Integration status and remaining constraint

Named route constants, both aggregate callers, structural quarantine, and the shared 12-flag compaction gate are integrated. There is no exact country-level Event 19 teardown effect in the owned management file. No deferred-record cleanup was attached to lot/family cleanup paths; any future country teardown must call the exact deferred-context cleanup from its actual owner rather than guessing at a broader hook.

Lifetime-ledger compaction blocks while any valid deferred action is pending. Quarantine raises the ledger invariant, clears the malformed action so it cannot gate forever, and fail-closes compaction without self-rescheduling.

No fallback or substitute replay was implemented.
