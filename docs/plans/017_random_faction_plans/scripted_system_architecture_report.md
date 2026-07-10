# Event 017 Random Faction scripted-system architecture report

## Status and authority

This is a read-only architecture handoff. It does not edit or approve the restored Event 017 gameplay draft. The implementation must follow the four source specs under `docs/specs/017_random_faction_specs/specs/`, the AI and decision matrices, and the stricter contracts in this report.

Resolution update on 2026-07-10: the blocker table below records the restored draft observed during the architecture pass. Current disposition lives in `017_random_faction_improvement_addendum.md`. The tuning-ownership blocker is resolved. Event effects use shared script constants directly for fixed delays and temporary-variable bridges for computed delays, timed flags, and timed ideas. Decision re-enable fields use script constants directly, and mission timeout variables are initialized from constants before activation. The only documented file-scoped exceptions are the three `ai_hint_pp_cost` mirrors, whose field rejects dynamic values, and the maritime `random_select_amount`, which has no proven dynamic form. The prohibited regional substitute identifier and behavior are absent.

The closure addendum rejects the proposed generic option scorer, new MTTH table, and larger generic lifecycle framework. Their rows below remain historical architecture proposals, not open completion requirements.

The implementation has these non-negotiable guarantees:

1. Automatic dispatch uses weighted selection across all eligible countries. It does not automatically prefer the country that happens to own the event-system call scope.
2. A selected country receives exactly `min(valid_faction_leader_count, 4)` unique living faction choices. With four or more valid factions, it receives exactly four.
3. Human and AI countries use the same selected country, saved option set, validity rules, scoring inputs, and final join effect. The only difference is whether a human clicks an option or the AI resolver chooses one.
4. The selected minor, chosen faction leader, regional pressure source, and pressure anchor remain attributable after the original event chain ends.
5. Evolution I schedules at most one neighboring response per baseline firing. Evolution III uses a per-cascade, per-region cap and cannot consume a shared world counter.
6. Pressure expiry and invalid-country cleanup are event-driven. No `on_daily`, `on_weekly`, `on_monthly`, or comparable whole-world periodic on-action is permitted.
7. No hardcoded faction names, static faction tag list, alternate target, generic regional substitute, or silent simplification is permitted.

## Restored-draft blockers at architecture review time

The following are acceptance blockers in the gameplay draft observed during this pass.

| Surface | Current evidence | Required replacement |
| --- | --- | --- |
| Automatic target dispatch | `common/scripted_effects/chaosx_settings_effects.txt` unconditionally sets `random_faction_prefer_current_dispatch_target`; `random_faction_prepare_runtime_context` then accepts that country before building the weighted pool. An eligible dispatcher country is therefore always preferred. | Automatic dispatch must always build and draw from the weighted eligible-country pool. `random_faction_prefer_current_dispatch_target` may exist only for an explicit direct/manual call mode and must never be set by normal random-event dispatch. |
| Player/AI option generation | `random_faction_entry_route_current_country` collects options, then both `chaosx.nr17.10` and `.20` collect a second random set in `immediate`. `.20` duplicates four large `ai_chance` blocks. | Collect once in `chaosx.nr17.1`, preserve that set, and route it to `.10` or `.20`. AI scoring belongs in one shared resolver; both paths call the same join effect. |
| Persistent chosen leader | `random_faction_selected_leader` is a regular event target only. The joined minor retains no scope variable identifying the chosen faction leader. | Persist `random_faction_alignment_leader` on the joined minor and store the same leader in the history result. Reconcile it on faction-leader succession. |
| Pressure attribution | `random_faction_apply_pressure_to_current_region_target` adds flags, ideas, and array entries but stores no source country, source leader, anchor, region id, or expiry day on the target. | Every pressured target must store all five pieces of memory before any event/decision is exposed. Decisions must resolve their leader from that memory, not from an arbitrary live faction. |
| Region model | `random_faction_current_region_targets` is owned by the selected country, has no region identity, and the code uses `@random_faction_regional_fallback_targets` plus a same-continent `every_country` scan when no neighbor was found. | Use an explicit region id and a designed maritime-reach branch for isolated/coastal countries. There is no generic substitute target path. |
| Evolution scheduling | `random_faction_apply_regional_pressure` can schedule `.30`, `.60`, and `.70` together, while `random_faction_check_evolution_unlocks` can schedule additional `.50`, `.60`, and `.70` calls. Delays are short file-scoped literals rather than MTTH-owned pacing. | Schedule exactly one highest-active-stage follow-up packet per successful baseline join. Use Event 017 MTTH entries and persistent pending guards. |
| Evolution III isolation | `random_faction_run_evo3_cascade` resets and consumes `global.random_faction_evo3_cascade_count`, loops until the absolute maximum, and has only a country lock. Concurrent regions can collide and no regional-share cap exists. | Allocate a cascade id, store its region and owner in an active-cascade ledger, draw the desired count once, clamp it to pool size and region share, and resolve exactly that many unique candidates. |
| Pressure expiry | Timed flags and ideas expire, but members remain in `global.random_faction_pressure_targets` and related arrays until another Event 017 action happens to call `random_faction_refresh_runtime_arrays`. | Each first pressure application schedules one country-owned expiry worker. The worker reschedules itself when pressure was extended and calls cleanup when the stored expiry day is reached. |
| Faction-leader succession | The current on-actions do not handle `on_assume_faction_leadership`, and `random_faction_refresh_runtime_arrays` simply drops an invalid old leader. | Transfer or rebuild Event 017 leader memory, regional pull, and active target ownership from `FROM` to `ROOT`; update every affected target through compact Event 017 arrays. |
| External faction joins | `common/on_actions/017_random_faction_on_actions.txt` has no guarded join hook. Vanilla also states that `on_join_faction` does not fire for `add_to_faction`. | The Event 017 join effect must directly call cleanup. Guarded `on_join_faction` and `on_offer_join_faction` hooks handle other join routes without scanning the world. |
| Event history | `events_log_set_default_actor_for_current_event` records `random_faction_target_country`, but the history schema has no chosen-leader field. The history row is created before a human chooses. | Add a two-phase Event 017 result binding keyed by the exact history sequence, with a parallel chosen-leader scope entry. Never assume the newest row is still index zero. |
| Event-details evolution catalog | Event 017 scripted localisation exists, but `events_log_rebuild_open_event_details_view` has no Event 017 preview branch. | Add three previews using `random_faction_event.evolution_type` and the three `random_faction_evolution_stage` constants. |
| Tuning ownership [resolved] | The restored draft mirrored values from `chaosx_random_faction_constants.txt` and included the prohibited `random_faction_regional_fallback_targets` identifier. | The live implementation uses shared constants and documented parser bridges. Only `ai_hint_pp_cost` and maritime `random_select_amount` retain file-scoped values. The prohibited identifier and substitute behavior are removed. |

The invalid-option path in the source spec is implemented as canonical revalidation of the same selected country. It is not a second target-selection mode: rebuild the valid faction set, reopen the same human/AI resolver, and cancel without join or pressure if the set is empty.

## Required file ownership

| File | Required responsibility |
| --- | --- |
| `common/script_constants/chaosx_random_faction_constants.txt` | All option caps, target weights, region ids, pressure values, durations, AI coefficients, evolution limits, and cascade-share tuning |
| `common/mtth/017_random_faction_mtth.txt` | Target dispatch weight, faction option AI weight, Evolution I/II delay, Evolution III spacing, resistance weight, and faction-leader reaction delay |
| `common/scripted_triggers/017_random_faction_triggers.txt` | Eligibility, join validity, reach, current pressure-source validity, decision visibility, regional cascade admission, and guarded lifecycle checks |
| `common/scripted_effects/017_random_faction_effects.txt` | Weighted target selection, unique option collection, shared resolution, persistent memory, regional pressure, evolution scheduling, succession, expiry, and cleanup |
| `events/017_join_faction.txt` | `chaosx.nr17.1`, human `.10`, AI `.20`, neighbor `.30`, leader `.40`, evolution dispatchers `.50/.60/.70`, report `.80`, and hidden expiry/cascade workers |
| `common/on_actions/017_random_faction_on_actions.txt` | Narrow, guarded country/faction lifecycle hooks only |
| `common/scripted_effects/chaosx_settings_effects.txt` | Event 017 prefire preparation and post-history sequence binding |
| `common/scripted_effects/chaosx_logic_effects.txt` | Repeatable registration, active-pool availability, and initialization/clearing of Event 017 log arrays |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Actor mapping, chosen-leader history schema, sanitization, view/detail copying, and three evolution previews |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | Event 017 default-enabled entry and evolution enable checks |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Chosen leader/faction display plus the existing evolution/detail mappings |
| `common/scripted_localisation/017_random_faction_scripted_localisation.txt` | Pressure-source, region, and holder-state text only |
| `common/scripted_effects/chaosx_dynamic_effects.txt` and `common/scripted_triggers/chaosx_dynamic_triggers.txt` | Reuse only; no new Event 017-specific public API is needed |

Reuse `uses_normal_civilian_systems`, `is_special_chaos_country`, and `is_actual_nonhuman_country` from `chaosx_dynamic_triggers.txt`. No existing helper in `chaosx_dynamic_effects.txt` collects faction leaders, joins a saved faction, or manages pressure memory, so those helpers remain Event 017-owned.

## Exact helper contract map

| Helper | Execution scope | Inputs | Output and side effects | Call sites |
| --- | --- | --- | --- | --- |
| `random_faction_prepare_candidate_weight` | candidate country | candidate state and centralized weights | unscoped temporary `random_faction_candidate_weight`; no persistent mutation | automatic target pool builder |
| `random_faction_prepare_runtime_context` | event-system dispatcher country | explicit automatic/direct mode | regular `random_faction_target_country`, its one saved option set, and temporary `random_faction_context_ready` | Event 017 prefire only |
| `random_faction_collect_faction_options` | selected country | current eligibility and option cap | `random_faction_option_count` plus one to four regular leader targets | entry, same-country invalid-option revalidation, cascade candidate entry |
| `random_faction_score_current_option` | saved faction leader | regular target country and pressure context | one positive temporary option weight or zero when invalid | AI option resolver for slots 1–4 |
| `random_faction_select_ai_option` | selected AI country | saved option targets and four computed weights | regular `random_faction_selected_leader`; no membership mutation | `chaosx.nr17.20` only |
| `random_faction_resolve_selected_option` | selected country | regular selected leader | validated call into the join effect, same-country revalidation, or clean cancellation | human option effects, AI resolver, neighbor/cascade outcome |
| `random_faction_join_selected_faction` | selected country | regular selected leader | exactly one faction join and all successful-result state | every Event 017 join route |
| `random_faction_set_current_region_id` | aligned/anchor country | capital/continent | temporary region id from the complete vanilla token map | regional target collection and cascade creation |
| `random_faction_collect_regional_pressure_targets` | aligned/anchor country | selected leader and region id | temporary unique land or maritime-reach target pool | pressure application and evolutions |
| `random_faction_apply_regional_pressure` | newly aligned country | selected leader and bounded regional pool | persistent source memory, pressure state, one highest-stage schedule packet | shared join success |
| `random_faction_resolve_live_pressure_leader` | pressured country | stored source country and leader | refreshed stored leader or complete pressure cleanup | every pressure decision/event and lifecycle refresh |
| `random_faction_schedule_neighbor_followup` | newly aligned country | one bounded regional pool and MTTH result | at most one pending Evolution I response | highest active stage I packet |
| `random_faction_run_evo2_pressure` | newly aligned country/one chosen target | reach, war, enemy, and mission caps | at most one automatic Evolution II incident | highest active stage II packet |
| `random_faction_run_evo3_cascade` | cascade owner country | region pool, desired count, region-share cap | one active-cascade ledger row and bounded sequential candidate jobs | highest active stage III packet |
| `random_faction_schedule_pressure_expiry` | pressured country | absolute expiry day | one pending hidden expiry worker | first pressure application and worker reschedule |
| `random_faction_cleanup_country_pressure` | affected country | none | clears Event 017 pressure, missions, selectors, pointers, and active-ledger membership | join, expiry, invalidation, lifecycle hooks |
| `random_faction_reconcile_faction_leader_succession` | new leader ROOT | old leader FROM and active Event 017 arrays | transfers leader memory and regional ownership without a world scan | `on_assume_faction_leadership` and invalid-leader refresh |
| `random_faction_bind_history_sequence` | selected minor | exact current history sequence | pending sequence variable and optional immediate result finalize | post-history Event 017 hook |
| `random_faction_finalize_history_result` | selected minor | pending sequence and chosen leader scope variable | writes the chosen leader at the matching history index exactly once | join success and post-history binding |

Required trigger contracts remain `random_faction_country_base_valid`, `is_random_faction_eligible_country`, `is_random_faction_wartime_candidate`, `is_random_faction_allowed_faction_leader`, `can_random_faction_join_faction`, `is_random_faction_pressure_neighbor`, `random_faction_option_1_valid` through `_4_valid`, `random_faction_has_active_pressure`, and `random_faction_region_can_cascade`. Slot triggers may delegate to one generic leader-versus-target trigger, but every slot must still be gated by the refreshed option count.

## Scope and state contracts

### Chain-local event targets

These remain regular event targets created with `save_event_target_as`:

- `random_faction_target_country`
- `random_faction_option_1_leader`
- `random_faction_option_2_leader`
- `random_faction_option_3_leader`
- `random_faction_option_4_leader`
- `random_faction_selected_leader`

They are valid only for the current selection/resolution chain. Regular event targets carry into events fired by that chain and clear automatically when the chain ends. They cannot be manually cleared. After a same-chain option refresh, every read must therefore be gated by the newly reset `random_faction_option_count`; an old fourth target is inert when the new count is below four.

No Event 017 global event target is required.

### Persistent country scope variables

Normal variables store country-scope ids after the chain ends:

| Holder | Variable | Meaning |
| --- | --- | --- |
| joined minor | `random_faction_alignment_leader` | faction leader chosen by this Event 017 result |
| pressured country | `random_faction_pressure_source_country` | aligned country that caused the pressure |
| pressured country | `random_faction_pressure_source_leader` | live leader responsible for the faction pull |
| pressured country | `random_faction_pressure_anchor_country` | regional anchor used for reach and objectives |
| pressured country | `random_faction_pressure_region_id` | one of the defined Event 017 region ids |
| pressured country | `random_faction_pressure_expiry_day` | absolute `global.num_days` expiry |
| pressured country | `random_faction_pressure_worker_due_day` | due day of the one active expiry worker |
| cascade candidate | `random_faction_evo3_cascade_id` | owning active-cascade ledger row |
| history actor | `random_faction_pending_history_sequence` | exact Event 017 history sequence awaiting result binding |
| history actor | `random_faction_pending_history_leader` | chosen leader if the marked baseline resolution preceded sequence binding |

Validate a stored country scope with both `country_exists = var:<name>` and `var:<name> = { exists = yes ... }`. `scope_exists` alone is insufficient because the variable scope can exist while its stored country is invalid. Clear the variable when validation fails.

### Temporary context

The following are temporary and unscoped: eligible-country pool, valid-leader pool, target/option weights, cascade desired count, and MTTH results. Initialize them in the caller block and reset them on every entry. Do not write `ROOT.temp_name` or `PREV.temp_name`. `random_faction_option_count` is a normal country variable because it must survive into the human or AI event; clear it on join, resistance, cancellation, and full cleanup.

### Persistent arrays

Keep only compact active ledgers:

- `global.random_faction_pressure_targets`
- `global.random_faction_aligned_minors`
- `global.random_faction_faction_leaders`
- aligned `global.random_faction_active_cascade_*_entries` arrays for cascade id, region id, owner scope, scheduled count, resolved count, joined count, and expiry day
- aligned Event 017 chosen-leader history arrays described below

All ledgers are sanitized at Event 017 entry, before decision target use, on narrow lifecycle hooks, and during Event 017 cleanup. They are not maintained by a periodic world scan.

## Weighted target dispatch

`random_faction_prepare_runtime_context` has two explicit call contracts:

- Automatic random-event mode: build the full valid target pool and make one weighted draw.
- Explicit direct-current-country mode: revalidate the current country and use it. This mode is used only by an intentional manual/test or already-selected follow-up call.

Automatic mode must never infer direct-current-country mode from ROOT. Remove the unconditional flag assignment from the normal Event 017 branch in `fire_event_by_temp_id_no_cluster`.

The weighted pool includes only countries passing `is_random_faction_eligible_country` or the enabled Evolution II wartime extension and having at least one currently joinable faction. `random_faction_prepare_candidate_weight` may retain the spec inputs—minor status, nearby faction presence, war adjacency, stability, war support, pressure, and cooldown—but every coefficient comes from `random_faction_selection_weight`. A candidate with a non-positive final weight is not admitted.

`random_faction_context_ready` becomes true only after the chosen country has produced at least one valid faction leader. Otherwise the automatic firing is rejected before history is written.

## Exact one-to-four unique faction algorithm

`random_faction_collect_faction_options` runs in the selected-country scope:

1. Set `random_faction_option_count` to zero and clear temporary `random_faction_valid_leader_pool`.
2. Run one event-owned `every_country` scan limited by `is_random_faction_allowed_faction_leader` and the selected-country versus leader join contract. Add each leader scope exactly once.
3. If the pool is non-empty, draw one scope with `random_scope_in_array`, save `random_faction_option_1_leader`, remove that scope from the temporary pool, and increment the count.
4. Repeat the same unrolled block for option 2, 3, and 4 only while the pool remains non-empty.
5. Clear the temporary pool. Preserve only the count and regular option event targets.

Removing each selected scope makes uniqueness structural. The postcondition is exactly `min(original_pool_size, constant:random_faction_requirement.option_cap)`. Do not fill missing slots with repeated leaders, a tag list, or a geographically unrelated faction.

`random_faction_option_N_valid` must check the current count, `has_event_target`, current leader eligibility, target-country eligibility, no direct war with the leader or any faction member, and the target still being outside a faction and subject relationship.

Localisation uses `[random_faction_option_N_leader.GetFactionName]` and `[random_faction_option_N_leader.GetName]`. No faction name is embedded in script or localisation selection logic.

## Identical player and AI resolution

The chain is:

```text
chaosx.nr17.1
  -> choose one weighted target
  -> collect one saved option set
  -> human: chaosx.nr17.10
     AI:    chaosx.nr17.20 -> random_faction_select_ai_option
  -> random_faction_resolve_selected_option
  -> random_faction_join_selected_faction
```

Remove option recollection from `.10` and `.20`. Human option effects only map option number to `random_faction_selected_leader`. The hidden AI resolver scores the same four saved leaders, chooses among only positive valid weights, saves the same target, and enters the same resolver.

Add `common/mtth/017_random_faction_mtth.txt` with at least:

- `random_faction_target_dispatch_weight`
- `random_faction_faction_option_weight`
- `random_faction_evo1_followup_days`
- `random_faction_evo2_incident_days`
- `random_faction_evo3_candidate_spacing_days`
- `random_faction_pressure_resistance_weight`
- `random_faction_leader_reaction_days`

Evaluate `random_faction_faction_option_weight` while scoped to each saved leader and copy the result into `random_faction_option_N_weight`. Its modifiers consume ideology match, land or maritime reach, common enemy, relations, faction strength, active-war help, neutrality resilience, same-region alignment, encirclement, and chaos. Then one `random_list` uses the four computed weights. This replaces the current slot-specific OR trigger and duplicated `ai_chance` blocks.

At click/resolution time, `random_faction_resolve_selected_option` revalidates the selected leader. If it became invalid, rebuild options for the same country and return to the same human or AI resolver. If the refreshed count is zero, clear pending state and end without membership, pressure, news, or a successful history result.

## Shared join and persistent memory

`random_faction_join_selected_faction` is the sole membership mutation used by baseline, AI, neighbor copy/counter-alignment, and Evolution III candidates. It runs in selected-country scope and accepts only `random_faction_selected_leader`.

On success it performs, in order:

1. Revalidate country and leader through `can_random_faction_join_faction`.
2. Execute `event_target:random_faction_selected_leader = { add_to_faction = ROOT }`.
3. Confirm ROOT is in that faction.
4. Save the leader scope into `random_faction_chosen_leader`; save it into the pending-history leader only when `random_faction_history_result_pending` marks the baseline firing.
5. Call `random_faction_cleanup_country_pressure` before applying the joined-country alignment state.
6. Apply alignment shock, cooldown, arrays, regional memory, leader reaction, evolution scheduling, achievements, news, and history result exactly once.

Failure before step 3 produces none of steps 4–6. This prevents pressure or log success when `add_to_faction` did not produce membership.

## Regional pressure and leader succession

Add `random_faction_set_current_region_id` using the seven tokens in vanilla `map/continent.txt`: `europe`, `north_america`, `south_america`, `australia`, `africa`, `asia`, and `middle_east`. Map them to centralized `random_faction_region_id.*` constants.

`random_faction_collect_regional_pressure_targets` uses two designed reach rules:

- land reach: eligible independent minor neighbors of the newly aligned country;
- maritime reach: only when land reach yields none, eligible same-region countries where both anchor and candidate have a controlled coastal state and the selected faction has a coastal member or otherwise satisfies the scripted corridor reach trigger.

The maritime rule is part of the region model. It does not select arbitrary countries merely to ensure an outcome.

For every pressured target, `random_faction_apply_pressure_to_current_region_target` stores source country, source leader, anchor, region, pressure value, resilience, and absolute expiry before adding ideas, missions, arrays, or UI state. All targetable decisions resolve their source through `random_faction_resolve_live_pressure_leader`.

That resolver follows one canonical succession chain:

1. Use the stored leader if it exists and remains the source country's faction leader.
2. If the source country still belongs to a faction, resolve its current `faction_leader`, overwrite the stored leader, and continue.
3. If the source has no valid faction or no valid leader, clear that pressure packet.

`on_assume_faction_leadership` provides the immediate path: ROOT is the new leader and FROM the old leader. Transfer Event 017 regional pull/target ownership, replace FROM with ROOT in `global.random_faction_faction_leaders`, and update only entries in `global.random_faction_pressure_targets` whose stored source leader is FROM. Do not scan every country.

## Evolution scheduling and strict caps

Only the highest enabled stage schedules a follow-up packet after a successful join. A stage packet incorporates the lower-stage pressure memory; it does not schedule all lower dispatcher events again.

### Evolution I

`random_faction_schedule_neighbor_followup` selects at most one unique valid regional target, stores its source memory, sets one pending flag, evaluates `mtth:random_faction_evo1_followup_days`, and schedules `.30` on that country. One baseline firing therefore produces zero or one delayed neighboring response.

### Evolution II

`random_faction_run_evo2_pressure` may admit a war-adjacent target only after direct-enemy, useful-front, and land/maritime reach checks. It schedules at most one visible pressured-neutrality incident per baseline join and at most one active border/corridor mission per affected country. Pressure ideas may exist on the bounded region pool, but they do not each open another automatic join chain.

### Evolution III

`random_faction_run_evo3_cascade` allocates `global.random_faction_next_cascade_id`, creates one active-cascade ledger row, and records its owner, region, source leader, expiry, and counters. It builds a temporary unique eligible pool from the one region only.

Draw `random_faction_evo3_desired_count` once between `random_faction_requirement.evo3_min_followups` and `.evo3_max_followups`. Clamp it to:

- the valid unique pool size;
- `random_faction_evolution_limit.evo3_absolute_cap`;
- the centralized maximum share of currently eligible minors in that region.

Remove each chosen country from the pool and assign it the cascade id. Schedule candidates sequentially with `mtth:random_faction_evo3_candidate_spacing_days`. Each candidate resolves exactly once through the same human/AI option and join helpers and increments that cascade row's resolved and joined counters. Resistance counts as resolved, not joined.

The cascade closes when resolved equals scheduled or its expiry is reached. A region cannot open another automatic cascade while its ledger row is active. Two different regions use different rows and counters. No global scalar join counter controls both.

## Expiry and lifecycle cleanup without periodic scans

`random_faction_cleanup_country_pressure` clears Event 017 pressure ideas, flags, source/anchor/leader/region/expiry variables, pending response state, active missions, target selectors, and membership in active pressure arrays. It does not clear unrelated alignment history.

On first pressure application, set `random_faction_pressure_expiry_worker_pending` and schedule a hidden country event, reserved as `chaosx.nr17.90`, for the current remaining duration. Extending pressure changes `random_faction_pressure_expiry_day` but does not schedule a second worker. At wake-up:

- if pressure is invalid or `global.num_days` has reached the stored expiry, run cleanup;
- if pressure was extended, compute the remaining days and reschedule the same worker once;
- if the country no longer exists, the narrow lifecycle hook removes its ledger entry.

The following on-actions are allowed only with a cheap Event 017 flag/array guard:

| On-action | Scope contract | Event 017 work |
| --- | --- | --- |
| `on_join_faction` | ROOT joins, FROM is leader; vanilla says this does not cover `add_to_faction` | clean externally joined pressured ROOT only |
| `on_offer_join_faction` | ROOT/THIS leader, FROM invited country | clean affected FROM after confirmed membership |
| `on_leave_faction` | ROOT leaves, FROM leader | clear/reconcile ROOT alignment memory and affected pressure ownership |
| `on_assume_faction_leadership` | ROOT new leader, FROM old | run succession transfer on compact Event 017 arrays |
| `on_capitulation` | ROOT capitulated, FROM winner | clean ROOT; reconcile it if it was a source or leader |
| `on_annex` | ROOT winner, FROM annexed | remove FROM from every Event 017 ledger and reconcile affected sources |
| `on_subject_annexed` | ROOT subject, FROM overlord | clean ROOT and its owned jobs |
| `on_subject_autonomy_level_change` | ROOT subject, FROM overlord | clean ROOT when it no longer meets independence rules |
| `on_puppet` / `on_release_as_puppet` | ROOT subject, FROM overlord | clean ROOT |
| `on_government_exiled` | ROOT government in exile, FROM host | clean ROOT |
| `on_government_change` | ROOT changed | revalidate ROOT only when it carries Event 017 state |

The direct shared join effect calls cleanup itself because vanilla explicitly notes that `add_to_faction` does not fire `on_join_faction`. World-end cleanup is called directly by the world-end path and iterates only Event 017 active ledgers.

## Event-log result architecture

The existing default actor branch correctly maps Event 017 to `random_faction_target_country`, but the chosen leader must be added without racing multiplayer history rows.

Extend history with parallel arrays:

- `global.events_log_history_secondary_actor_entries`
- `global.events_log_history_has_secondary_actor_entries`
- matching history-view, open-detail, and selected-detail arrays

`record_events_log_history_entry` inserts zero placeholders for every event. Before dispatch, the selected country receives `random_faction_history_result_pending`; immediately after the Event 017 history row is recorded, `random_faction_bind_history_sequence` stores the exact `global.events_log_history_sequence` only while that marker is present. It never stores array index zero. Follow-up pressure and Evolution III joins lack the marker and cannot write pending history state.

`random_faction_finalize_history_result` searches `global.events_log_history_sequence_entries` for that exact sequence and writes the chosen leader scope and `has_secondary_actor = 1` at the matching index. It is called by both sides of the possible timing order:

- post-log binding, if an AI result already stored `random_faction_pending_history_leader`;
- shared join success, if the history sequence is already bound for a human result.

Cancellation clears the baseline-result marker, pending sequence, and pending leader without writing a successful result. Sanitization, history sorting, history-details rebuild, and event-details rebuild must copy both new arrays at the same indices as the existing actor arrays.

Scripted localisation displays the primary actor as the selected minor and the secondary actor as the chosen faction leader, using its current `GetName` and `GetFactionName` loc objects. Add the three Event 017 evolution previews in `events_log_rebuild_open_event_details_view` with the existing Event 017 constants.

## Engine-validation gates and precedents

The following were verified against official documentation and vanilla structure:

- regular versus global event-target lifecycle and variable scope pointers;
- temporary arrays, `random_scope_in_array`, and removal effects;
- dynamic `add_to_faction` on a faction-leader scope;
- faction localisation through `GetFactionName`;
- faction/on-action scope contracts;
- script constants and `mtth:<entry>` value injection.

Relevant vanilla precedents include:

- `events/LAR_Spain.txt`, especially `lar_spain.33` and `.51`, for selecting and saving multiple unique random country/state targets;
- `events/WTT_PRC.txt` for `add_to_faction = event_target:<country>`;
- `events/GOE_Raj.txt` for `random_scope_in_array` over stored scope arrays;
- `common/on_actions/00_on_actions.txt` for the explicit warning that `on_join_faction` does not fire from `add_to_faction`;
- `map/continent.txt` for the complete live continent token set.

Before gameplay acceptance, run focused prototypes for these remaining engine questions:

1. Prove that removing a selected country scope from a temporary scope array inside `random_scope_in_array` produces four unique draws. Documentation supports both effects, but a matching vanilla combined example was not found.
2. Prove that an MTTH entry evaluated in saved leader scope can read the Event 017 regular target and that its result is accepted as a `random_list` weight. Do not replace it with duplicated slot AI blocks if this fails; stop for an architecture decision.
3. Prove that a variable-computed remaining duration is accepted by delayed `country_event` scheduling for the expiry worker. Do not introduce a periodic scan if it is rejected.
4. Prove that Event 017's post-history hook binds the sequence after the row is inserted for both visible human and hidden AI resolution ordering.

Task-specific acceptance scenarios:

- zero valid factions rejects the firing before history; one through three factions show exactly that many options; four and five-plus show exactly four unique options;
- automatic dispatch statistically follows candidate weights and does not always select the dispatcher country;
- player and AI receive the identical precomputed option set and both enter the same join helper;
- a leader invalidated before click triggers same-country revalidation; no valid leader cancels with no side effects;
- a faction leadership change transfers stored leader memory and keeps valid decisions attached to the new leader;
- an externally pressured country joining a faction is cleaned, while unrelated faction joins do no Event 017 work;
- island pressure remains within the explicit region/reach contract;
- pressure extension leaves one expiry worker and clears arrays at the final due day;
- concurrent Evolution III cascades in two regions keep distinct ids and caps, while a second cascade in the same region is refused until closure;
- one Evolution I firing schedules no more than one response and one Evolution III cascade never exceeds its draw, pool, absolute, or regional-share cap;
- the history row shows both the selected minor and the exact chosen leader after human and AI resolution;
- world-end cleanup empties Event 017 active ledgers without a world-country iteration.

## References consulted

Offline wiki snapshot: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Faction modding.

Official vanilla documentation: `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/dynamic_variables_documentation.md`, `documentation/loc_objects_documentation.md`, `common/script_constants/documentation.md`, `common/factions/_documentation.md`, and `common/on_actions/_documentation.md`.

No gameplay changes, fallbacks, or simplifications are authorized by this report.
