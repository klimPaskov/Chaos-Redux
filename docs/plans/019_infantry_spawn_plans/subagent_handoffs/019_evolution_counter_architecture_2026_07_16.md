# Event 019 evolution counter architecture

Date: 2026-07-16  
Role: `chaosx_scripted_system_architect`  
Scope: architecture only. No gameplay file was edited by this handoff.

## Decision

Replace the due-date `every_country` sample with persistent, country-local membership receipts and global counters. Keep two distinct populations:

1. The ordinary world population supplies `world_country_count`, `world_war_country_count`, and the war-share ratio.
2. Event 019 participants supply participant spread, low control, severe congestion, active claimant, and anomalous preservation counts.

These populations must not be merged. The removed scan counted every existing ordinary country in the war-share numerator and denominator, including countries that had never participated in Event 019. Setting both world counters from the participant count changes the evolution score.

## Exact state contract

### Global counters

| Persistent variable | Meaning |
| --- | --- |
| `global.infantry_spawn_evolution_world_country_count` | Existing countries eligible for ordinary Event 019 evolution history |
| `global.infantry_spawn_evolution_world_war_country_count` | Eligible world countries currently at war |
| `global.infantry_spawn_evolution_participant_count` | Eligible countries with `infantry_spawn_participant` |
| `global.infantry_spawn_evolution_low_control_count` | Eligible participants satisfying `infantry_spawn_control_is_low` |
| `global.infantry_spawn_evolution_severe_congestion_count` | Eligible participants satisfying `infantry_spawn_congestion_is_severe` |
| `global.infantry_spawn_evolution_claimant_crisis_count` | Eligible participants satisfying `infantry_spawn_has_active_claimant` |
| `global.infantry_spawn_evolution_anomalous_preservation_count` | Eligible participants with an active registry and at least one anomalous division |
| `global.infantry_spawn_evolution_counter_epoch` | Version of the current receipt set |

Use flags for boolean state:

- `infantry_spawn_evolution_counters_ready`
- `infantry_spawn_evolution_counter_rebuild_in_progress`
- `infantry_spawn_evolution_counter_invariant_failure`

### Country receipts

| Country flag | Counter owned by the receipt |
| --- | --- |
| `infantry_spawn_evolution_world_country_contributor` | `global.infantry_spawn_evolution_world_country_count` |
| `infantry_spawn_evolution_world_war_contributor` | `global.infantry_spawn_evolution_world_war_country_count` |
| `infantry_spawn_evolution_participant_contributor` | `global.infantry_spawn_evolution_participant_count` |
| `infantry_spawn_evolution_low_control_contributor` | `global.infantry_spawn_evolution_low_control_count` |
| `infantry_spawn_evolution_severe_congestion_contributor` | `global.infantry_spawn_evolution_severe_congestion_count` |
| `infantry_spawn_evolution_claimant_crisis_contributor` | `global.infantry_spawn_evolution_claimant_crisis_count` |
| `infantry_spawn_evolution_anomalous_preservation_contributor` | `global.infantry_spawn_evolution_anomalous_preservation_count` |

Store `infantry_spawn_evolution_counter_epoch_seen` as a normal country variable. If it differs from the global epoch during an authorized rebuild, clear stale receipt flags without subtracting from the newly reset counters, copy the global epoch, then derive current membership.

### Stable eligibility trigger

Add `infantry_spawn_is_ordinary_evolution_counter_country` in `common/scripted_triggers/019_infantry_spawn_triggers.txt`:

```text
infantry_spawn_is_ordinary_evolution_counter_country = {
	exists = yes
	NOT = { is_infantry_spawn_derivative_country = yes }
	NOT = {
		OR = {
			has_country_flag = infantry_spawn_scenario_actor
			has_country_flag = infantry_spawn_scenario_dynamic_breakaway
			has_country_flag = infantry_spawn_scenario_takeover_actor
			has_country_flag = infantry_spawn_scenario_setup_bypass
		}
	}
}
```

Do not put `infantry_spawn_scenario_transaction_is_idle` in this persistent membership trigger. It is a transient global transaction gate. Keep that gate on the pulse and due-check caller, as it is now. A scenario transaction must pause scoring, not remove every ordinary country from persistent counters.

Desired memberships are:

- world country: stable eligibility trigger
- world war: world-country receipt and `has_war = yes`
- participant: world-country receipt and `has_country_flag = infantry_spawn_participant`
- low control: participant receipt and `infantry_spawn_control_is_low = yes`
- severe congestion: participant receipt and `infantry_spawn_congestion_is_severe = yes`
- claimant crisis: participant receipt and `infantry_spawn_has_active_claimant = yes`
- anomalous preservation: participant receipt, `infantry_spawn_anomalous_registry_active`, and `infantry_spawn_anomalous_division_count > 0`

This reproduces the removed scan exactly. In particular, the old scan did not require `infantry_spawn_country_is_active` before counting a participant.

## Required helper effects

Implement these in `common/scripted_effects/019_infantry_spawn_evolution_effects.txt`:

- `infantry_spawn_initialize_evolution_counter_state`
- `infantry_spawn_begin_evolution_counter_rebuild`
- `infantry_spawn_sync_country_evolution_counter_epoch`
- `infantry_spawn_reconcile_world_evolution_memberships`
- `infantry_spawn_reconcile_participant_evolution_memberships`
- `infantry_spawn_reconcile_all_evolution_memberships`
- `infantry_spawn_unregister_participant_evolution_memberships`
- `infantry_spawn_unregister_world_evolution_memberships`
- `infantry_spawn_unregister_all_evolution_memberships`
- `infantry_spawn_validate_evolution_counter_state`
- `infantry_spawn_mark_evolution_counter_invariant_failure`
- `infantry_spawn_load_evolution_counter_context`

`infantry_spawn_load_evolution_counter_context` replaces the body of `infantry_spawn_refresh_global_evolution_context`. It only copies the seven persistent counters into the existing temporary score inputs, then computes:

```text
infantry_spawn_world_war_share =
	global.infantry_spawn_evolution_world_war_country_count
	/ global.infantry_spawn_evolution_world_country_count
```

Keep the existing temporary names and all four score helpers unchanged. This preserves the current multi-signal weights, thresholds, MTTH schedule, and one-record activation pipeline.

## Initialization and repair

### Fresh initialization

Use the already requested global manifestation pass in `infantry_spawn_fire_manifestation`. Do not add another recurring or standalone world pass.

1. After `infantry_spawn_event_has_fired` is set and before its existing `every_country`, call `infantry_spawn_begin_evolution_counter_rebuild` when counters are not ready or an invariant failure exists.
2. Remove the outer `limit` from the existing manifestation `every_country`.
3. At the top of that loop, call `infantry_spawn_reconcile_world_evolution_memberships` for every existing country.
4. Put the existing generation work in an inner `if` limited by `infantry_spawn_country_can_receive_generation`.
5. Country initialization and pressure recalculation register participant signals inside that same country scope.
6. After the loop, validate the counters. Set `infantry_spawn_evolution_counters_ready` only if validation succeeds, then clear the rebuild flag and invariant-failure flag.

The manifestation remains one world iteration. It performs its requested generation work and seeds the counter registry in the same pass.

### Repair

On any invariant failure, evolution advancement fails closed. Leave the due date on the normal retry schedule, clear `infantry_spawn_evolution_counters_ready`, and do not record or activate an evolution.

The next Event 019 manifestation may rebuild counters inside its already authorized world pass. It increments the epoch, resets the seven counters, reconciles each country once, validates, and marks the registry ready. Do not launch a repair `every_country` from a seven-day pulse.

## Country-local update call sites

| File and effect | Required call |
| --- | --- |
| `019_infantry_spawn_ledger_effects.txt`, `infantry_spawn_initialize_country_system` | Reconcile participant memberships after all opening variables are initialized |
| `019_infantry_spawn_core_effects.txt`, `infantry_spawn_recalculate_country_pressure` | Reconcile participant memberships after `infantry_spawn_apply_staged_ideas`, because that helper finishes the congestion and control clamps |
| `019_infantry_spawn_claimant_identity_effects.txt`, `infantry_spawn_append_current_claimant_row` | Reconcile participant memberships after the claimant-active receipt is set |
| `019_infantry_spawn_claimant_crisis_effects.txt`, `infantry_spawn_refresh_claimant_presence_flags` | Reconcile participant memberships after claimant flags are rebuilt |
| `019_infantry_spawn_pulse_effects.txt`, `infantry_spawn_run_country_pulse` | Reconcile all memberships immediately before `infantry_spawn_maybe_advance_global_evolution` as an idempotent backstop |
| `019_infantry_spawn_management_effects.txt`, `infantry_spawn_finalize_annexed_ordinary_country_cleanup` | Unregister participant memberships before participant and runtime flags are cleared |
| `019_infantry_spawn_derivative_package_effects.txt`, `infantry_spawn_setup_derivative_identity_common` | Unregister all memberships after derivative identity is set and before participant state is cleared |
| `019_infantry_spawn_derivative_package_effects.txt`, `infantry_spawn_derivative_process_global_manifestation` | Unregister all memberships before clearing `infantry_spawn_participant` |
| `019_infantry_spawn_scenario_effects.txt`, `infantry_spawn_scenario_mark_actor` | Reconcile all memberships after actor flags are set, which removes the actor from both populations |
| `019_infantry_spawn_scenario_effects.txt`, `infantry_spawn_scenario_apply_actor_bypass_for_type` | Reconcile all memberships after the bypass flags are finalized |
| `019_infantry_spawn_scenario_effects.txt`, `infantry_spawn_scenario_restore_same_tag_country_state` | Reconcile all memberships after the full snapshot is restored |
| `019_infantry_spawn_scenario_effects.txt`, failed actor and rollback finalizers | Reconcile all memberships after final identity flags are cleared or restored |

Do not rely only on the seven-day pulse for low control, congestion, claimant, or anomalous changes. The pulse is a repair backstop. Canonical local mutators keep the counters current before another country's due pulse can score them.

## Event-driven country lifecycle hooks

Extend `common/on_actions/019_infantry_spawn_derivative_on_actions.txt`. These hooks are country-local and event-driven. They are not daily, weekly, monthly, or whole-world recurring work.

- `on_war`: call `THIS = { infantry_spawn_reconcile_world_evolution_memberships = yes }`.
- `on_peace`: call the same helper in `THIS`.
- `on_release_as_free`: call `ROOT = { infantry_spawn_reconcile_all_evolution_memberships = yes }`.
- `on_release_as_puppet`: call the same helper in `ROOT`.
- `on_government_change`: call the same helper in `ROOT`. This idempotently registers both sides created by `start_civil_war`, for which the offline wiki documents government-change firing on both sides.
- `on_annex`: before any derivative bypass or cleanup branch, call `FROM = { infantry_spawn_unregister_all_evolution_memberships = yes }`, then reconcile `ROOT`.
- `on_subject_annexed`: unregister `ROOT`. Receipt guards make a duplicate notification harmless if `on_annex` also fires.

All hooks should first require `has_global_flag = infantry_spawn_event_has_fired` and `has_global_flag = infantry_spawn_evolution_counters_ready`, except annex cleanup, which should still attempt receipt removal while a failure is being quarantined.

## Idempotency, ordering, and failure rules

HOI4 effect execution is sequential, but several country pulses may run on the same date. Preserve these rules:

1. Set a country receipt immediately before incrementing its counter.
2. Decrement only when the corresponding receipt exists.
3. Clear a receipt only after a successful decrement.
4. If a receipt exists but its counter is missing or below one, set `infantry_spawn_evolution_counter_invariant_failure`, clear readiness, leave the receipt as evidence, and return cleanup failure. Do not silently skip subtraction and clear the receipt.
5. Do not clamp counters to hide an underflow.
6. The all-memberships unregister helper removes participant-derived receipts before the participant receipt, then removes the war receipt before the world-country receipt.
7. The all-memberships reconcile helper adds the world-country receipt before any dependent receipt and removes dependent receipts before world-country removal.
8. Keep the existing due-date lease. The first due pulse moves `global.infantry_spawn_next_evolution_check_date` before scoring. Later same-day pulses see the new date and cannot duplicate an evolution record.
9. `infantry_spawn_maybe_advance_global_evolution` must require ready counters, no rebuild, no invariant failure, and `infantry_spawn_scenario_transaction_is_idle = yes` before loading score context.

Minimum validation invariants:

- every counter exists while readiness is set
- every counter is zero or greater
- world war count is no greater than world country count
- participant count is no greater than world country count
- low-control, severe-congestion, claimant-crisis, and anomalous-preservation counts are each no greater than participant count

For participant annex cleanup, propagate an unregister success temporary into the existing exact cleanup finalizer. Do not set `infantry_spawn_country_cleanup_complete` if a participant receipt could not be removed. The existing annex retry queue is the correct owner for retrying that exact country scope. For a nonparticipant annex underflow, fail global evolution closed and rebuild on the next manifestation pass.

## Current replacement hazards to reject

- Do not assign `infantry_spawn_world_country_count` from `global.infantry_spawn_evolution_participant_count`.
- Do not treat a participant-only war count as the old world war count.
- Do not describe seven-day pulse lag as exact maintenance when local decision or crisis helpers can update the receipt immediately.
- Do not clear contributor receipts after an underflow guard merely skipped subtraction.
- Do not run a repair `every_country` from `infantry_spawn_maybe_advance_global_evolution`.

## Validation scenarios

1. With 100 eligible ordinary countries, 20 at war, 10 participants, and 4 participant countries at war, war share must be `0.20`, not `0.40`.
2. Calling reconciliation twice without state changes must leave every counter unchanged.
3. Crossing the low-control threshold must change only the low-control counter by one.
4. Resolving the final claimant must change only the claimant-crisis counter by one.
5. Ordinary Event 019 closeout while the country still exists must remove participant receipts but leave world-country and world-war receipts intact.
6. Converting an ordinary participant into a derivative must remove all seven applicable receipts once.
7. Annexing a nonparticipant country at war must reduce world-country and world-war counts once.
8. Marking a same-tag scenario actor must remove its world and participant receipts. Exact rollback must restore the memberships once.
9. A forced counter-underflow setup must clear readiness and must not activate or log an evolution.
10. Two participant pulses on the due date must produce at most one evolution activation and one log record.

## Validation searches

Run from the mod root after implementation:

```powershell
rg -n -U "infantry_spawn_refresh_global_evolution_context\s*=\s*\{[\s\S]{0,2500}every_country" common/scripted_effects/019_infantry_spawn_evolution_effects.txt
rg -n "world_country_count = global\.infantry_spawn_evolution_participant_count|world_war_country_count = global\.infantry_spawn_evolution_participant" common
rg -n "infantry_spawn_evolution_(world_country|world_war|participant|low_control|severe_congestion|claimant_crisis|anomalous_preservation)_contributor" common events
rg -n "on_war|on_peace|on_annex|on_subject_annexed|on_release_as_free|on_release_as_puppet|on_government_change" common/on_actions/019_infantry_spawn_derivative_on_actions.txt
rg -n "infantry_spawn_(reconcile|unregister)_(world|participant|all)_evolution_memberships" common/scripted_effects common/on_actions
rg -n "every_country" common/scripted_effects/019_infantry_spawn_evolution_effects.txt common/scripted_effects/019_infantry_spawn_pulse_effects.txt
```

Expected result: the first two searches return no matches. Receipt mutations should be confined to the counter helpers. Any remaining `every_country` in the evolution file should be a one-time evolution activation migration, not due-date sampling or repair.

## References consulted

- Required offline wiki core pages, especially Data structures, Effects, Triggers, Scopes, On actions, and Event modding
- Vanilla `documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`
- Vanilla `common/on_actions/_documentation.md` and `common/script_constants/documentation.md`
- Vanilla on-action precedents for `on_war`, `on_peace`, release, and annex scopes
- Event 019 Part 7 performance contract and the evolution entry and cleanup matrix
- Current Event 019 evolution, pulse, core, claimant, scenario, derivative, pressure, and cleanup helpers

## Simplifications and blockers

No gameplay simplification is proposed. A standalone one-time migration scan is deliberately excluded. Fresh counter initialization and any repair reuse the existing Event 019 manifestation world pass. If support for a save that has already fired Event 019 but will never receive another manifestation is required, that needs an explicit user decision because exact reconstruction would require an additional one-time whole-world pass.
