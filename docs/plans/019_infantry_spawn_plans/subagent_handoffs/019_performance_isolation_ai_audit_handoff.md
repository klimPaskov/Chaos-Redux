# Event 019 performance, isolation, and AI audit handoff

> **Superseded findings notice (2026-07-15):** The two P1 findings below are
> preserved as the original audit record, not as current defects. Lifetime-ledger
> work was replaced by bounded, cursor-driven compaction and independently
> re-audited clean at P0/P1; see
> `019_lifetime_ledger_compaction_handoff.md`. The SCN-013 snapshot race was
> closed by the shared `infantry_spawn_scenario_transaction_is_idle` gate,
> deferred exact-action replay, wrapper rechecks, decision and claimant gates,
> pulse suspension, scripted-GUI mutation locks, and transaction-owned resume.
> The current consolidated verdict is recorded in
> `019_parent_implementation_audit_packet_2026_07_15.md`.

## Audit status

This was a read-only static source audit. No gameplay, localisation, asset, workbook, registry, or existing documentation file was changed. This handoff is the only file created by the audit.

Event 019 management and claimant military integration were being edited concurrently. The observations below identify functions and contracts rather than treating transient line movement or standardization work in progress as final. No finding depends on a transient standardization tuning line.

No runtime profiler was used. In this report, **measured design tradeoff** means that the cadence, iteration scope, and configured cap were measured directly from script. It does not mean wall-clock performance was profiled.

## Reference basis

The audit followed `AGENTS.md`, `chaos-redux-events`, and `chaos-redux-subagents`.

The offline wiki pages consulted were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, Division modding, Unit modding, and Country creation.

The official game references consulted included:

- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- `documentation/script_concept_documentation.md`
- `common/on_actions/_documentation.md`
- `common/script_constants/documentation.md`
- `common/scripted_guis/_documentation.md`
- `events/LaR_espionage_operations.txt`, especially the exact-ID removal pattern around lines 186 through 209

## Executive result

| Severity | Classification | Result |
|---|---|---|
| P1 | Defect | The seven-day country pulse repeatedly scans append-only lifetime ledgers. Several paths are nested. Cost grows with all Event 019 history rather than current unresolved work. |
| P1 | Defect | SCN-013 same-tag and dynamic rollback transactions do not lock the ordinary pulse, player actions, AI actions, timed mission completions, open incident choices, or scripted GUI mutations. A retry can truncate or restore over legitimate post-snapshot work. |
| None | Measured design tradeoff | There is no nested recurring whole-world scan and no unbounded daily ledger scan. The recurring world sample is globally date-gated. The daily continuity pulse is country-only and ledger-free. |
| None | Isolation proof | Direct scenario actors and Event 019 derivatives are excluded from ordinary Event 019 evolution/history writers. No Event 2, Event 5, or Event 10 progression writer, super-event, death meter, or `world_end` writer is called or set by Event 019 derivative packages. |
| None | AI parity proof | Player decisions, scripted GUI actions, and AI management normally converge on shared gates and effects. The transaction lock omission affects both player and AI paths. The claimant refusal decision is the clearest direct availability hole. |

## Recurring entry points and measured cadence

| Entry point | Cadence and scope | Work reached | Classification |
|---|---|---|---|
| `chaosx.nr19.900` in `events/019_infantry_spawn.txt` lines 566 through 571 | Seven days from `constant:infantry_spawn_event.audit_pulse_days`, currently `7` in `common/script_constants/019_infantry_spawn_constants.txt:31`. One active country per scheduled event. | `infantry_spawn_run_country_pulse` in `common/scripted_effects/019_infantry_spawn_pulse_effects.txt:9`. Validation, live-unit reconciliation, management closeout, pressure, claimants, anomalous-family AI, evolution due check, and rescheduling. | Defect only because its ledger work grows with lifetime history. The active-country scheduler itself is a measured design tradeoff. |
| `chaosx.nr19.901` in `events/019_infantry_spawn.txt` lines 578 through 583 | One day from `constant:infantry_spawn_achievement_threshold.continuity_pulse_days`, currently `1` in `common/script_constants/019_infantry_spawn_achievement_constants.txt:38`. Only countries with an active rail proof, claimant-survival proof, or scenario-origin proof reschedule it. | `infantry_spawn_run_achievement_continuity_pulse` and `infantry_spawn_achievement_country_pulse` in `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:824-927`. | Measured design tradeoff. Country-only and ledger-free. It must not be globally paused by the SCN-013 transaction lock because rail, leadership, capitulation, and world-end continuity are time-sensitive. Scenario-origin tracking is registered only after scenario setup succeeds at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2821-2828`. |
| `chaosx.nr19.954` in `events/019_infantry_spawn_scenario.txt:89-93` | Seven days while a provisional dynamic actor still has units. Actor-country scope. No maximum attempt count. | `infantry_spawn_scenario_retry_pending_rollback_cleanup` in `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2228-2258`. Deletes the actor army, proves emptiness, removes actor cores from owned states, and annexes only after the empty-army proof. | Measured safety tradeoff. Each call is actor-bounded. Lifetime is unbounded because exact cleanup is preferred to abandoning a provisional actor. The missing ordinary-work lock is a separate P1 defect. |
| `chaosx.nr19.955` in `events/019_infantry_spawn_scenario.txt:99-103` | Seven days while same-tag cleanup is pending. Country scope. No maximum attempt count. | `infantry_spawn_scenario_retry_same_tag_rollback` and `infantry_spawn_scenario_attempt_same_tag_rollback` in `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2122-2169`. | Measured safety tradeoff per call. The stale-snapshot race is a P1 defect. |
| Event 019 achievement on-actions | One-shot `on_capitulation` and `on_annex` only in `common/on_actions/019_infantry_spawn_achievement_on_actions.txt:13-39`. | Achievement continuity and exact defeated-actor proof. The only Event 019 `any_country` is the launch-roster hostile-survivor proof in `common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:185-209`. | Measured design tradeoff. It is not daily, weekly, or monthly. |
| Event 019 derivative on-actions | One-shot `on_capitulation` and `on_annex` only in `common/on_actions/019_infantry_spawn_derivative_on_actions.txt:9-39`. | Derivative victory, defeat, and final cleanup. | Measured design tradeoff. |
| Global manifestation | One call per Event 019 firing. | `infantry_spawn_fire_manifestation` has one `every_country` at `common/scripted_effects/019_infantry_spawn_core_effects.txt:472-505`. | Measured design tradeoff. It is not a recurring on-action. |
| Global evolution sample | Called by active country pulses but guarded by one global due date. | `infantry_spawn_maybe_advance_global_evolution` in `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:605-632` advances the date before sampling. `infantry_spawn_refresh_global_evolution_context` has one `every_country` at lines 82 through 132. MTTH is clamped to 21 through 180 days and a failed threshold check retries after 30 days in `common/script_constants/019_infantry_spawn_constants.txt:87-96`. | Measured design tradeoff. Simultaneous country pulses cannot each perform a world sample. |
| Evolution activation | One time per stage. | `every_country` in `infantry_spawn_activate_evolution_i` through `infantry_spawn_activate_evolution_iv` at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:525`, `542`, `559`, and `576`. | Measured design tradeoff. |
| SCN-013 launch | One pass per scenario launch. | `infantry_spawn_scenario_launch_unregistered` has one host-selection `every_country` and one bypass-cleanup `every_country` at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2793` and `2806`. | Measured design tradeoff. No recurring world scan follows it. |

## Loop-bound audit

### Country and world loops

No nested recurring whole-world loop was found. The only recurring route that can reach `every_country` is the globally due-date-gated evolution sample. The guard moves `global.infantry_spawn_next_evolution_check_date` before the sample, so several participant pulses on one date do not duplicate it.

The SCN-013 hostile-survivor `any_country` is reached only from capitulation or annex achievement handling. It is not a periodic monitor.

### State loops

- `infantry_spawn_scenario_build_coherent_revolt_region` uses `every_owned_state` at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:278`. It is a launch-time host operation.
- `infantry_spawn_scenario_transfer_selected_region_to_actor` uses `every_owned_state` at line 1513. It is a one-shot transfer over the chosen host.
- Dynamic rollback and retry use `every_owned_state` at lines 2199 and 2238. They are actor-country operations on the seven-day cleanup retry.
- Scenario host and split triggers use `any_owned_state` in `common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:108` and `213`.

No state loop is nested under a recurring `every_country` after setup. The dynamic rollback state loop is repeatable but bounded to the provisional actor's owned states.

### Division loops

- `infantry_spawn_reconcile_live_unit_ledger` uses one `every_country_division` at `common/scripted_effects/019_infantry_spawn_ledger_effects.txt:125-197`. This runs every seven days for an active ordinary country and is part of the P1 lifetime-ledger finding.
- Standardization preflight, conversion, and rollback use country-division loops in `common/scripted_effects/019_infantry_spawn_management_effects.txt` under `infantry_spawn_preflight_standardization_conversion`, `infantry_spawn_convert_preflighted_lot_to_canonical_template`, and `infantry_spawn_rollback_preflighted_standardization_conversion`. These are action transactions, not pulse recurrence. They were under concurrent implementation and were not judged for final behavior.
- Exact lot teardown uses country-division loops under `infantry_spawn_preflight_exact_lot_teardown` and `infantry_spawn_execute_exact_lot_teardown`. These are selected-lot action transactions.
- Same-tag rollback absence proof uses `every_country_division` under `infantry_spawn_scenario_prove_same_tag_package_objects_absent` at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:1845`. It runs only during rollback or its retry.

### Array loops

All inspected `while_loop_effect` bodies advance their index, reduce a remaining budget, or stop on a configured cap. No syntactically infinite array loop was found.

The important distinction is that a terminating loop can still be a performance defect when its upper bound is an append-only lifetime ledger. That is the case for the ordinary pulse paths below.

## P1 defect: append-only lifetime ledgers are rescanned every seven days

### Evidence

`infantry_spawn_run_country_pulse` calls the following ordinary route every seven days when the country remains active:

1. `infantry_spawn_validate_all_ledgers`
2. `infantry_spawn_reconcile_live_unit_ledger`
3. `infantry_spawn_run_country_management_pulse`
4. family cleanup and pressure recalculation
5. claimant pulse
6. anomalous-family AI
7. evolution due check

The dominant lifetime-history paths are:

- `infantry_spawn_reconcile_live_unit_ledger` in `common/scripted_effects/019_infantry_spawn_ledger_effects.txt:125-197` snapshots every current country division, scans every lifetime unit row, performs live-snapshot membership checks, resolves missing units to lots, and then scans every lifetime lot row.
- `infantry_spawn_close_resolved_generations` in `common/scripted_effects/019_infantry_spawn_management_effects.txt:3149-3237` scans all lifetime lots for paid unaccounted rows, scans all lifetime generations, scans all lifetime lots again for every open or audited generation, then scans generations again for any remaining open row.
- `infantry_spawn_evolution_one_reevaluate_management` and `infantry_spawn_evolution_two_expand_management` at `common/scripted_effects/019_infantry_spawn_management_effects.txt:3420-3476` each scan all lifetime lots on every pulse after their stage is active.
- AI exact-obligation selection in `infantry_spawn_select_first_affordable_exact_obligation_lot` at `common/scripted_effects/019_infantry_spawn_management_effects.txt:2192` performs up to two lot-ledger scans. Each candidate refresh invokes `infantry_spawn_refresh_selected_lot_exact_obligations` at line 1172, which scans the lifetime unit and obligation ledgers. This is a nested lifetime path.
- `infantry_spawn_muster_board_build_lot_view` at `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:164-180` stops after 40 live rows but may scan the entire old lot prefix before finding them. The configured display cap does not cap source scanning.
- `infantry_spawn_muster_board_calculate_current_family_state` at `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:231-293` scans all unit and lot rows for each displayed family. `infantry_spawn_muster_board_build_family_view` can repeat this for every enabled registry family. This is player-triggered rather than periodic, but its cost grows with lifetime history.
- Generation closeout achievement evaluation at `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:409-576` also scans generation, lot, unit, and obligation identity. It runs when a generation closes, not daily or every pulse after closeout. Compaction must happen after this exact proof.

The ledgers are append-only during ordinary play. Row removal exists for failed transactions and complete derivative teardown, not for resolved ordinary history. Therefore the seven-day cost grows with every repeat manifestation and paid request.

### Why this is P1

The problem is not one expensive world iteration. It is the combination of:

- repeatable Event 019 manifestations and requests
- append-only lot, unit, template, component, obligation, claimant, and auxiliary identity ledgers
- a seven-day active-country pulse
- nested lot-to-obligation and generation-to-lot scans
- GUI family reconstruction over the same lifetime rows

Long campaigns accumulate work that can no longer affect gameplay but remains in every operational scan.

## Required safe compaction contract

This is an implementation contract, not a fallback. UIDs remain immutable and globally monotonic.

### Scheduling and hard bounds

Add subsystem script constants for every threshold and work budget. A safe initial policy is:

- Start maintenance when any core child ledger has at least `256` rows, or when at least `64` terminal child rows have been certified compactable.
- Perform the threshold check from `^num` values or maintained counters. Do not run a full lifetime pre-scan merely to decide whether to compact.
- Do not run compaction from `.901` or any daily on-action.
- Run maintenance at the tail of the ordinary `.900` pulse, after validation, reconciliation, generation closeout, and closed-generation achievement evaluation.
- Require `infantry_spawn_scenario_transaction_is_idle = yes` and no request, standardization, demobilization, template teardown, derivative creation, or incident transaction in progress.
- When no backlog is active, attempt maintenance no more often than every `30` days.
- Once a certified backlog exists, process one bounded chunk per ordinary seven-day pulse until the backlog drops below threshold.
- Inspect at most `256` source rows and remove at most `128` aligned child rows per pass. Process at most `8` certified generations per pass. Stop at the first reached budget.
- Use a persistent round-robin ledger selector and per-ledger cursor so an old ineligible prefix cannot cause every pass to rescan the same rows.
- Candidate indices must be gathered first and removed from highest source index to lowest. Never remove an aligned source row while walking the same source array forward. The LaR exact-ID deletion precedent demonstrates the safe identify-then-remove shape.
- Revalidate all aligned ledgers after every chunk. Rebuild GUI views and resolve selected objects by stable UID, never by the old source index.

The work budget must include candidate discovery as well as deletion. A nominal cap on removed rows is not sufficient if finding each row still scans the full lifetime ledger.

### Exact generation eligibility

A generation can receive a compactable certificate only when all of these conditions are true:

- Generation status is `resolved` or an explicit archived state. It is never `open` or `audited`.
- `infantry_spawn_achievement_evaluate_closed_generation` has completed for that exact generation.
- Every child lot is terminal and has zero live units, zero outstanding debt, and zero outstanding manpower.
- Every child obligation is settled, forfeited, or transferred and has zero outstanding amount and zero outstanding debt value.
- Every child unit is terminal. Allowed terminal states are `transferred_out`, `demobilized`, `destroyed`, or exact-settled `unaccounted`. No unit may be active, claimant-loyal, `transfer_staged`, or unresolved `unaccounted`.
- No engine division carrying a child unit UID remains.
- Every private template is retired or exactly deleted. A shared canonical template is not deleted with the generation.
- No pending exact deletion, standardization rollback, template conversion, or template teardown references a child UID.
- No active claimant references the generation, a lot, or a unit.
- No derivative former-parent, origin-generation, package-owner, claimant, or transfer record references a child UID.
- No scenario snapshot, same-tag transaction, dynamic rollback, cleanup retry, or setup bypass transaction is active.
- No management target or active mission references a child UID. This includes audit, standardization, training, supervised demobilization, specialist preservation, rail proof, exact settlement, paid-request rollback, incidents, and family management.
- No achievement proof still requires an exact child UID.

The certificate should be produced once during closeout while the exact generation is already being inspected. The maintenance pass should not rediscover eligibility by repeating full cross-ledger scans.

### Achievement identities that must survive

The following exact contracts must be consumed or archived before their source rows are removed:

- `infantry_spawn_achievement_pretech_unit_uid_entries` paired with `infantry_spawn_achievement_pretech_gate_entries`, registered in `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:20-47`
- `infantry_spawn_achievement_composition_disqualified_unit_uid_entries`, evaluated around lines 330 through 345
- `infantry_spawn_achievement_integrated_random_lot_uids`
- `infantry_spawn_achievement_supervised_demobilized_lot_uids`
- the closed-generation audit over exact lots, units, and obligations at lines 409 through 576
- `infantry_spawn_achievement_rail_generation_uid` and its target-state and expiry proof at lines 582 through 625
- exact division battle identity, which resolves unit, generation, lot, template, and component rows at lines 933 through 1078

UIDs must never be reused. Where an achievement only needs a distinct historical count after exact closeout, preserve a monotonic archived count plus enough immutable UID tombstone identity to prevent a repeated UID from being counted twice. Do not replace exact proof with a raw increment before the proof has completed.

### Aligned rows eligible for child compaction

Remove every field in an aligned group at the same source index.

1. Selected-state rows: `infantry_spawn_selected_state_generation_uid_entries`, `infantry_spawn_selected_state_scope_entries`, and `infantry_spawn_selected_state_lot_uid_entries`.
2. Lot rows: `infantry_spawn_lot_uid_entries`, generation UID, template UID, family ID, profile, origin state, quality, coherence, start experience, start equipment, start manpower, command owner, status, previous status, unit count, outstanding debt, outstanding manpower, supply, training, equipment state, claimant UID, combat count, support count, mobility mismatch, incident count, claimant susceptibility, and demobilization resistance arrays.
3. Template rows: template UID, lot UID, status, and recruitment mode arrays.
4. Component rows: component template UID, slot kind, unit profile, column, and row arrays.
5. Unit rows: unit UID, delete cohort ID, generation UID, lot UID, template UID, origin state, division scope, spawn province, family ID, start experience, start equipment, start manpower, status, previous status, and claimant UID arrays.
6. Obligation rows: obligation UID, generation UID, lot UID, unit UID, resource profile, issued amount, paid amount, salvageable paid amount, outstanding amount, outstanding debt value, and status arrays.
7. Terminal claimant rows, only after all references are gone: claimant UID, profile, archetype, name variant, influence, demand, demand date, status, headquarters state, loyal-lot count, accepted-demand count, and refused-demand count arrays.
8. Auxiliary membership/history arrays tied to compacted rows: locked template UIDs, spawn-only template UIDs, technology-locked template and unit UIDs, transfer-eligible unit UIDs, pretechnology template and unit UIDs, the achievement pretechnology UID/gate pair, achievement composition-disqualified unit UIDs, integrated-random lot UIDs, and supervised-demobilized lot UIDs.

Generation summary rows should remain in phase one. They are small, they drive the history board, and `infantry_spawn_last_closed_generation_uid` depends on immutable generation identity. Retain the exact generation UID, date, evolution stage, profile, selected-state count, lot count, unit count, terminal status, and any precomputed closeout result bits needed by the history UI.

If historical claimant wording needs exact identity, retain a lightweight claimant archive row with claimant UID, archetype, name variant, and accepted/refused totals. Do not keep its operational lot and obligation graph alive for localisation alone.

### Aggregates that compaction must not change

Retain all existing global evolution/history values, including:

- Event 019 generation and total formation/lot/request counts
- management success and failure totals
- integrated and demobilized lot totals
- claimant crisis, takeover, failed-coup, and revolt totals
- lot incident totals
- current Event 019 evolution flags and next-check date
- Event Log and evolution history rows

Retain all country aggregate state, including active and unaccounted counts, unresolved generation count, debt, manpower liability, request counts, management outcomes, integrated/standardized/demobilized/preserved/incident counts, claimant state, control, congestion, saturation, stage, evolution flags, achievement flags, and `infantry_spawn_last_closed_generation_uid`.

Never decrement, reuse, or rebase `global.infantry_spawn_next_generation_uid`, `global.infantry_spawn_next_lot_uid`, `global.infantry_spawn_next_template_uid`, `global.infantry_spawn_next_unit_uid`, `global.infantry_spawn_next_obligation_uid`, or claimant UID allocation.

## P1 defect: SCN-013 rollback races ordinary country work

### Exact race

`infantry_spawn_scenario_begin_same_tag_transaction` in `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:1540-1674` records pre-transaction country counters, flags, selected indices, and aligned-array lengths.

Rollback then:

- deletes provisional package objects
- resizes aligned arrays back to the saved lengths
- restores saved counters and flags
- retries every seven days if exact absence is not proven

The rollback work is in `infantry_spawn_scenario_attempt_same_tag_rollback` at lines 2122 through 2160, with tail truncation and snapshot restoration in the helpers it invokes around lines 1895 through 2119.

The ordinary Event 019 package can schedule `.900` while the transaction is still provisional. `.900`, `.954`, and `.955` all use a seven-day cadence. Same-day delayed-event order is not a transaction boundary.

At audit time:

- `infantry_spawn_country_can_continue_pulse` in `common/scripted_triggers/019_infantry_spawn_triggers.txt:54-67` did not exclude the transaction or either cleanup-pending flag.
- `infantry_spawn_management_is_available` at lines 191 through 197 did not exclude them.
- `infantry_spawn_muster_board_is_available` in `common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt:10-16` did not exclude them.
- claimant action gates in `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:202-303` did not exclude them.
- family action gates in `common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt:219-271` did not exclude them.
- `infantry_spawn_refuse_claimant_demand` used `available = { always = yes }` in `common/decisions/019_infantry_spawn_claimant_decisions.txt:68-77`.
- timed mission timeout effects bypass normal decision availability.
- open player incident options can resolve after the snapshot.
- the scripted GUI can call effect wrappers directly.

If any of those paths append a legitimate ordinary row after the snapshot, rollback truncates it. If they update a saved counter or flag, rollback restores the stale value. AI claimant or family work can also add provisional references that make exact cleanup take longer.

The snapshot stores selected lot and claimant source indices but not all GUI view arrays. A GUI rebuild during the transaction can leave source indices pointing at provisional rows after tail truncation.

## Required SCN-013 lock and resume contract

### Shared idle trigger

Create one shared country trigger, for example `infantry_spawn_scenario_transaction_is_idle`. It is false while any of these durable flags exists:

- `infantry_spawn_scenario_same_tag_transaction_active`
- `infantry_spawn_scenario_same_tag_cleanup_pending`
- `infantry_spawn_scenario_rollback_cleanup_pending`

`infantry_spawn_scenario_setup_bypass` is broader than a failed transaction and exists during successful setup. Treat it as a transaction lock only when paired with one of the durable transaction or cleanup flags, or replace that ambiguity with one dedicated durable lock set before the first package mutation.

The durable lock is set before any package row, unit, template, claimant, counter, or state mutation. Only exact commit, exact rollback completion, or successful dynamic-actor annex may clear it.

### Normal and continuity pulses

- Hard-gate `infantry_spawn_country_can_continue_pulse` and recheck inside `infantry_spawn_run_country_pulse`.
- A locked `.900` clears `infantry_spawn_audit_pulse_scheduled`, performs no achievement, ledger, management, claimant, family, derivative, evolution, or idea work, and does not reschedule itself.
- Exact same-tag commit or rollback schedules one fresh `.900` after resume validation if the country still satisfies the continuation trigger.
- Do not globally gate `.901`. It has no core-ledger writes and preserves time-sensitive proof. Scenario-origin continuity is not armed until setup succeeds.

### Timed mission completions

All timeout effects in `common/decisions/019_infantry_spawn_decisions.txt:674-779` need a deferred completion path:

- `infantry_spawn_complete_selected_lot_audit`
- `infantry_spawn_complete_selected_lot_standardization`
- `infantry_spawn_complete_supervised_demobilization`
- `infantry_spawn_complete_selected_lot_training`
- `infantry_spawn_complete_muster_districts`
- `infantry_spawn_complete_integration_staff_search`
- `infantry_spawn_complete_specialist_preservation`
- `infantry_spawn_complete_rail_corridor_mission`
- `infantry_spawn_finish_request_cooldown`

If a timeout fires while locked, store the exact completion type and stable target lot/generation UID where applicable. Schedule a lightweight one-day retry that only checks for transaction idle. Replay the completion exactly once after unlock. Never repay a start cost and never silently discard a paid mission.

### Player and AI decisions

Add the idle requirement to:

- `infantry_spawn_management_is_available`
- `infantry_spawn_muster_board_is_available`
- `infantry_spawn_selected_claimant_demand_can_be_paid`
- `infantry_spawn_can_recognize_selected_claimant`
- `infantry_spawn_can_counter_command_selected_claimant`
- `infantry_spawn_can_discredit_selected_claimant`
- `infantry_spawn_can_arrest_selected_claimant`
- a new exact refusal gate replacing `available = { always = yes }`
- `infantry_spawn_can_execute_selected_family_reinforcement`
- `infantry_spawn_can_open_selected_family_cantonment`
- `infantry_spawn_can_appoint_selected_family_liaison`
- `infantry_spawn_can_issue_selected_family_restricted_deployment`
- `infantry_spawn_can_sustain_selected_family`
- `infantry_spawn_can_seal_selected_family_breach`
- `infantry_spawn_can_disperse_selected_anomalous_lot`

Also recheck idle inside the shared mutating wrappers because the scripted GUI calls them without going through decision availability:

- all `infantry_spawn_execute_selected_lot_*_action` wrappers
- all `infantry_spawn_request_*_action` wrappers
- `infantry_spawn_recognize_selected_claimant`
- `infantry_spawn_accept_selected_claimant_demand`
- `infantry_spawn_refuse_selected_claimant_demand`
- `infantry_spawn_counter_command_selected_claimant`
- `infantry_spawn_discredit_selected_claimant`
- `infantry_spawn_arrest_selected_claimant`
- `infantry_spawn_execute_selected_family_train_or_spawn`
- `infantry_spawn_open_selected_family_cantonment`
- `infantry_spawn_appoint_selected_family_liaison`
- `infantry_spawn_issue_selected_family_restricted_deployment`
- `infantry_spawn_sustain_selected_family`
- `infantry_spawn_seal_selected_family_breach`
- `infantry_spawn_disperse_selected_anomalous_lot`

Gate or recheck the recurring AI routes:

- `infantry_spawn_run_country_management_pulse`
- `infantry_spawn_run_claimant_pulse`
- `infantry_spawn_ai_respond_to_selected_claimant_demand`
- `infantry_spawn_run_anomalous_family_ai`

Category-level availability prevents AI decision consideration. Wrapper checks protect alternate callers.

### Scripted GUI mutations

The scripted GUI is `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt`.

While locked, allow close and harmless presentation-only tab or animation toggles. Disable:

- refresh and rebuild at line 24
- lot and family row selection at lines 48 and 49
- claimant cycling at line 50
- all lot action clicks at lines 52 through 58
- all request clicks at lines 60 through 64
- all claimant clicks at lines 66 through 89
- all family clicks at lines 91 through 97

The corresponding enabled triggers are at lines 101 through 182. After commit or rollback, clear all GUI view arrays, resolve selected lot, claimant, and family by stable UID, rebuild the views, and only then re-enable gameplay clicks.

### Already-open lot incidents

Every player option effect with the `infantry_spawn_incident_*` prefix in `events/019_infantry_spawn.txt:208-558` can outlive the snapshot. The affected choice families are barracks, ammunition, motor pool, village, officers, staff, depot, colors, tanks, rotorcraft, radios, cavalry, and armored cars.

If the player chooses an option while locked, persist the exact incident choice enum and incident lot UID. Replay that exact choice once after idle. Do not reroll the incident and do not charge its resource effect twice.

### Unlock order

For same-tag commit or rollback:

1. Finish or restore the exact transaction while the lock remains set.
2. Validate every aligned ledger.
3. Resolve selected lot, claimant, and family from stable UIDs.
4. Clear and rebuild scripted GUI view arrays.
5. Replay each deferred timeout and incident exactly once.
6. Clear the durable lock.
7. Schedule one fresh country pulse if continuation remains valid.

For a failed dynamic actor, successful exact cleanup annexes the provisional actor. There is no actor resume. The former parent resumes only if it separately owns locked Event 019 work.

## SCN-013 idempotency and retry review

### No duplicate launch effects found

- `infantry_spawn_scenario_process_host` sets `infantry_spawn_scenario_host_processed` before setup at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2624-2625`.
- `infantry_spawn_scenario_finalize_actor_setup` is guarded by `NOT = { has_country_flag = infantry_spawn_scenario_actor_setup_complete }`.
- actor roster insertion and hostile-count growth are guarded by actor identity and membership checks in the actor-marking effect.
- regional war candidates require no existing war and a valid `can_declare_war_on` result in `common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:249-260`. Each selected candidate is removed from the temporary array. `maximum_immediate_targets` is `8` in `common/script_constants/019_infantry_spawn_scenario_constants.txt:108`.
- former-parent war declaration checks that the war does not already exist, then proves that it exists after declaration.
- dynamic regional state transfer is one-shot. Rollback removes actor cores and annexes only after the army is proven empty.
- same-tag package setup is not repeated after `infantry_spawn_scenario_actor_setup_complete`.
- setup bypass flags are cleared after package success, identity failure, and the launch-wide final cleanup.

No duplicate war declaration, repeated regional transfer, repeated actor count, or repeated hostile count defect was found.

### Retry classification

The retry counter can grow without a maximum attempt. That is a measured exact-cleanup safety tradeoff, not independently a defect. Each retry is bounded to one actor and its owned states or exact package rows. The P1 defect is that unrelated ordinary work can occur between retries and invalidate the frozen rollback boundary.

No terminal fallback is proposed.

## Ordinary Event 019 evolution/history isolation

`infantry_spawn_contributes_to_ordinary_evolution_history` in `common/scripted_triggers/019_infantry_spawn_triggers.txt:42-52` excludes:

- every Event 019 derivative country
- `infantry_spawn_scenario_actor`
- `infantry_spawn_scenario_dynamic_breakaway`
- `infantry_spawn_scenario_takeover_actor`
- `infantry_spawn_scenario_setup_bypass`

The gate is used by the inspected writers for:

- lot and formation totals in `common/scripted_effects/019_infantry_spawn_ledger_effects.txt:414-415` and `524-525`
- management successes, failures, integrations, and demobilizations in `common/scripted_effects/019_infantry_spawn_management_effects.txt:35-75`
- claimant crisis creation in `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:249-273`
- claimant request totals in `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt:377-385`
- claimant takeover and failed-coup totals in `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:219-252`
- anomalous-family request totals in `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:837-842`
- paid request totals in `common/scripted_effects/019_infantry_spawn_management_effects.txt:4400-4412`
- lot incident totals in `common/scripted_effects/019_infantry_spawn_management_effects.txt:4638-4643`
- the global evolution world sample in `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:92-125`

Scenario identity is set before package generation:

- dynamic actors receive `infantry_spawn_scenario_dynamic_breakaway` inside `create_dynamic_country` at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2560-2564`, before `chaosx.nr19.950`
- same-tag actors receive `infantry_spawn_scenario_takeover_actor` at lines 2614 through 2617, before `chaosx.nr19.950`

Package success proofs explicitly require that the actor does not contribute to ordinary evolution history.

`global.infantry_spawn_total_claimant_revolts` is initialized but no writer was found. It therefore cannot be contaminated by scenario actors.

Event Log follow-up history is intentionally allowed. `infantry_spawn_record_country_followup_history` in `common/scripted_effects/019_infantry_spawn_core_effects.txt:514-523` records a history row while restoring the normal last-fired identity. It does not increment ordinary manifestation or evolution totals.

## Event 2, Event 5, and Event 10 parent isolation

No Event 019 file calls `chaosx.nr2.*`, `chaosx.nr5.*`, or `chaosx.nr10.*`.

No Event 019 derivative package writes parent participant flags, parent stage flags, parent evolution flags, parent super-event flags, parent death-meter values, or the global `world_end` flag. Event 019 reads `world_end` for availability and achievement invalidation only.

`infantry_spawn_derivative_is_parent_isolated` in `common/scripted_triggers/019_infantry_spawn_triggers.txt:584-593` rejects zombie parent identity, Death identity, cave-country identity, coal-golem template identity, original `ZZZ`, and original `DTH`.

The package initialization in `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:326-376` sets only Event 019 derivative identity and clears ordinary Event 019 participant identity.

Provider composition is also isolated:

- zombie provider rows use Event 019 unit-registry templates and zombie battalions. They do not set Event 2 outbreak flags.
- ghost provider rows use Event 019 ghost-host composition. They do not set Event 10 country flags or stage values.
- golem provider rows use coal-golem battalions and equipment. They do not run Event 5 KMB setup, focus, or evolution effects.

Event 2 classification requires original `ZZZ` or its own zombie dynamic-country flags in `common/scripted_triggers/002_zombie_outbreak_triggers.txt:1-6`. Event 10 classification requires `DTH`, original `DTH`, or `death_country` in `common/scripted_triggers/010_death_triggers.txt:12-18`. Event 10 recurring hooks use the same parent identity rather than Event 019 derivative identity.

SCN-013 hosts require `uses_normal_civilian_systems`. `is_actual_nonhuman_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt:131-153` excludes zombie, Death, cave, and Event 019 nonhuman derivative actors. This prevents a scenario dynamic actor from inheriting a parent Event 2, Event 5, or Event 10 nonhuman host.

Event 5 KMB decision and package writers use actual `tag = KMB` or KMB focus flags. Some KMB AI strategy plans use `original_tag = KMB`, so a dynamic country with that origin can be considered by those strategy plans. No Event 5 progression, history, super-event, or count writer was reached from that eligibility alone. This is a non-contaminating AI-strategy inheritance note, not a defect found in the requested parent-history surfaces.

The Event 019 ghost consumption path calls the shared civilian-death pipeline with a death reason. That is required shared casualty accounting. It does not call Event 10 event effects, Event 10 evolution, or Event 10 death-meter writers.

## Player and AI parity

The ordinary lot, request, claimant, and anomalous-family systems normally share their actual mutating effects:

- main decisions use the same `infantry_spawn_can_*` gates used by scripted GUI enabled triggers
- scripted GUI clicks call the same action wrappers used by decisions
- AI exact-obligation settlement uses the same affordability trigger and exact settlement effect as the player
- claimant AI demand response calls the same accept or refuse effects as claimant decisions
- anomalous-family AI tests the same family gates before calling the same family effects
- the scripted GUI has `ai_enabled = { always = no }` at `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:213`

No separate AI effect was found that bypasses player costs or writes a stronger outcome.

The exception is transaction isolation, not balance parity. Both AI and player paths can currently mutate the frozen same-tag snapshot. `infantry_spawn_refuse_claimant_demand` is especially exposed because its decision availability is unconditional. Family gates also omit management and transaction state.

## Findings classified by design tradeoff versus defect

### Defects

1. Seven-day operational work grows with append-only lifetime ledgers and includes nested lifetime scans.
2. SCN-013 snapshots and rollback retries do not isolate ordinary pulses, AI, decisions, mission timeouts, incidents, or scripted GUI actions.

### Measured design tradeoffs

1. Seven-day active-country scheduling is bounded by explicit country continuation state.
2. One-day achievement continuity is country-only, conditionally scheduled, and ledger-free.
3. Evolution has one global sample per due date, with a 21 to 180 day MTTH clamp and 30 day retry.
4. Manifestation and SCN-013 launch use one-shot world passes.
5. Dynamic and same-tag rollback retries are seven-day, actor-country operations with no attempt ceiling so exact cleanup is never abandoned.
6. Event 019 uses one-shot capitulation and annex on-actions, not daily, weekly, or monthly all-country on-actions.

## Files changed

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_performance_isolation_ai_audit_handoff.md`

## Simplifications, omissions, and blockers

No fallback, gameplay simplification, or omitted requested audit surface was used.

Runtime wall-clock profiling was outside this read-only static audit. All performance classifications are based on exact script cadence, scope, configured caps, and call-graph bounds. Concurrent Event 019 management and claimant edits may move line numbers after this handoff. The identifiers and contracts are the authoritative references.
