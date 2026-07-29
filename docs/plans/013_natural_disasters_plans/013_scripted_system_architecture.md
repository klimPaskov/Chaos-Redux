# Event 013 Natural Disasters Scripted System Architecture

## Status and authority

Implementation closure, 2026-07-12: this file is the preserved pre-implementation architecture handoff. The live public contract and implemented outputs are authoritative in `common/scripted_effects/chaosx_dynamic_effects.md`, while `docs/plans/013_natural_disasters_plans/013_event_completion_final_audit.md` records the final disposition. References below to an inert entry event, proposed enums, four outputs, or constants still to add describe the planning snapshot and are not current implementation instructions.

This architecture required a fresh Event 013 Natural Disasters implementation and did not authorize legacy recovery or reuse. Deleted Event 013 history and the former Earth Earthquake implementation were outside the reference set and were not copied or adapted.

This architecture follows:

- `docs/specs/013_natural_disasters_specs/README.md`
- `docs/specs/013_natural_disasters_specs/manifest.md`
- the current shared Chaos Redux event, event log, event cluster, Deaths, and dynamic-effect APIs
- the offline Paradox wiki pages required by `AGENTS.md`
- official Hearts of Iron IV script documentation
- current vanilla natural-disaster and delayed-event precedents

The design has four hard guarantees:

1. Every accepted top-level public call creates exactly one disaster sequence. Internal physical continuation may join exactly one live parent sequence, but that continuation is not a public caller contract.
2. Every top-level sequence is associated with exactly one history row. Event 013-owned sequences write exactly one Event 013 row. A verified bridge may attach to its one existing source-event row, but it never writes a second row.
3. An affected country receives its requested report and aftermath activation even when another event calls the API and returns before delayed work runs.
4. No Event 013 maintenance path uses `on_daily`, `on_weekly`, `on_monthly`, or another whole-world periodic country iteration.

## Architectural decision

Use a thin public wrapper, a global active-sequence ledger, country-owned delayed-job queues, state-owned aftermath cards, and event-driven cleanup.

```text
caller
  -> call_natural_disaster
      -> validate and normalize call
      -> allocate one sequence row
      -> resolve or queue impacts
      -> write one history row through the selected log mode
      -> schedule hidden country queue worker
          -> pop one persistent job row
          -> rebuild current target event targets
          -> dispatch family impact, report, news, follow-up, or cleanup
              -> Deaths API
              -> family damage API
              -> state aftermath card
              -> optional future job
          -> close sequence when every counter reaches zero
```

The queue worker always removes a job row before dispatching it. A handler may therefore append new jobs without moving the row currently being processed or invalidating its index.

Regular event targets are used only for the current call and current worker dispatch. Persistent state is stored in variables and arrays. Global event targets are prohibited because concurrent sequences would overwrite the same names and require fragile manual cleanup.

## Planned file ownership

| File | Required ownership |
| --- | --- |
| `common/script_constants/013_natural_disasters_constants.txt` | Public enum values, timing, severity, family lethality, damage, report delay, queue expiry, and aftermath tuning |
| `common/mtth/013_natural_disasters_mtth.txt` | Weighted target selection, warning probability, follow-up probability, and compact AI choice weights |
| `common/scripted_triggers/013_natural_disasters_triggers.txt` | Public call validation, family target eligibility, heat exclusion, card state, and decision availability |
| `common/scripted_effects/013_natural_disasters_effects.txt` | Call normalization, sequence ledger, target selection, queue storage, queue worker, logging mode, and lifecycle cleanup |
| `common/scripted_effects/013_natural_disasters_family_effects.txt` | Family dispatch, family-specific death and building profiles, spread, and follow-up selection |
| `common/scripted_effects/013_natural_disasters_aftermath_effects.txt` | Report scheduling, state cards, recovery transitions, reassessment, supersession, transfer, and closure |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | Thin documented public effect `call_natural_disaster = yes` |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Public API documentation, inputs, outputs, defaults, side effects, and examples |
| `events/013_natural_disasters.txt` | Canonical random entry, hidden queue worker, family reports, family news, and hidden dispatch events |
| `common/on_actions/013_natural_disasters_on_actions.txt` | Narrow state-control and country-lifecycle hooks only, if the exact vanilla on-action scopes are verified |
| `common/decisions/categories/013_natural_disasters_categories.txt` | Later aftermath category activation and visibility |
| `common/decisions/013_natural_disasters_decisions.txt` | Later warning, rescue, stabilization, reconstruction, and relief actions |
| `common/dynamic_modifiers/013_natural_disasters_dynamic_modifiers.txt` | Later state aftermath modifiers owned by Event 013 |
| `common/scripted_effects/chaosx_settings_effects.txt` | Event 013 preparation hook before normal random dispatch |
| `common/scripted_effects/chaosx_logic_effects.txt` | Event 013 event-log actor mapping and any narrow shared log input override |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Optional event-id and actor override consumed by a direct external history write |
| `common/script_constants/chaos_meter_constants.txt` | New Deaths reason enum value for natural disasters |
| `events/099_desert_storm.txt` or its live Event 099 equivalent | Later narrow compatibility bridge into Event 013 only |

An untracked draft of `common/script_constants/013_natural_disasters_constants.txt` and `common/scripted_triggers/013_natural_disasters_triggers.txt` was present during this architecture pass. This plan preserves its useful public names and enumerated family matrix, but the draft is not treated as accepted implementation. In particular, its `natural_disaster_impact_guard` flag needs to be reconciled with the date-based same-day guard below before gameplay implementation.

Every new script file needs the repository overview header. Reusable public logic added to `chaosx_dynamic_effects.txt` needs matching documentation in `chaosx_dynamic_effects.md` in the same change.

## Public call contract

### Public wrapper

The only cross-system entry point is:

```text
call_natural_disaster = yes
```

The wrapper lives in `common/scripted_effects/chaosx_dynamic_effects.txt`. It calls the internal `natural_disaster_begin_sequence = yes` effect. Event 013 family handlers, queue internals, and cleanup effects are private and must not be called by other systems.

The call executes in country scope. The current country is the host used for caller-facing policy and queue ownership until the target country is resolved. A call that cannot resolve a valid target is rejected without a history row and without any delayed job.

### Temporary scalar inputs

All scalar inputs are temporary variables and are therefore unscoped. Callers must set them in the same outer effect block before invoking the wrapper.

| Input | Enum or value | Default | Meaning |
| --- | --- | --- | --- |
| `natural_disaster_call_caller_type` | `natural_disaster_caller.*` | `random` | Random system, cluster, scenario, external event, deity, hostile actor, or debug |
| `natural_disaster_call_caller_event_id` | numeric event id | `0` | Source event id for audit and bridge attribution |
| `natural_disaster_call_family` | `natural_disaster_family.*` | `random` | Explicit family or weighted random family |
| `natural_disaster_call_family_group` | proposed `natural_disaster_family_group.*` | `any` | Optional geological, hydrological, meteorological, fire, cryosphere, extraterrestrial, or abnormal filter |
| `natural_disaster_call_target_mode` | `natural_disaster_target_mode.*` | `random_valid` | Selected state, selected country, selected region, coast, nearby enemy, dense state, or random valid |
| `natural_disaster_call_target_region` | strategic region id | `0` | Required only for `selected_region` |
| `natural_disaster_call_severity` | `natural_disaster_severity.*` | `local` | Local, severe, regional, catastrophic, or abnormal |
| `natural_disaster_call_sequence_mode` | `natural_disaster_sequence_mode.*` | `single` | Single, local season, regional system, global pulse, moving corridor, or barrage |
| `natural_disaster_call_sequence_count` | positive integer | mode default | Optional exact number of primary impacts within the mode's safe range |
| `natural_disaster_call_news_policy` | `natural_disaster_news_policy.*` | `meaningful` | News threshold and suppression behavior |
| `natural_disaster_call_report_policy` | `natural_disaster_report_policy.*` | `affected_country` | Recipient policy for delayed reports |
| `natural_disaster_call_aftermath_policy` | `natural_disaster_aftermath_policy.*` | `normal` | None, light, normal, full, or emergency aftermath card depth |
| `natural_disaster_call_chain_policy` | `natural_disaster_chain_policy.*` | `family` | Follow-up family and risk policy |
| `natural_disaster_call_death_override_mode` | proposed `natural_disaster_override_mode.*` | `default` | Default, multiply, replace, or suppress death calculation |
| `natural_disaster_call_death_scale` | fixed point | `1.0` | Multiplier or replacement input according to override mode |
| `natural_disaster_call_damage_override_mode` | proposed `natural_disaster_override_mode.*` | `default` | Default, multiply, replace, or suppress building damage calculation |
| `natural_disaster_call_damage_scale` | fixed point | `1.0` | Multiplier or replacement input according to override mode |
| `natural_disaster_call_log_mode` | `natural_disaster_log_mode.*` | `event_013_history` | Event system, direct Event 013 history, scenario history, or an internal no-write mode |
| `natural_disaster_call_parent_sequence_id` | sequence id | `0` | Historical proposal only. The live wrapper rejects this public shape; internal continuation uses a separately validated private override. |

The wrapper must normalize omitted inputs explicitly. It must not depend on a temporary variable accidentally surviving a prior scripted effect call.

`natural_disaster_log_mode.none` is valid only for a child call joining a live parent or for a verified bridge that is already attached to one source-event history row. A normal top-level external call with `none` is rejected. This prevents unlogged standalone disaster sequences.

### Regular event-target inputs

| Event target | Required mode | Meaning |
| --- | --- | --- |
| `natural_disaster_call_target_country` | `selected_country`, optional constraint for `selected_state` or `selected_region` | Country inside which a state is selected |
| `natural_disaster_call_target_state` | `selected_state` or `caller_provided` | Exact impact state |
| `natural_disaster_call_actor` | hostile actor, deity, selected attribution | Actor stored in the Event 013 history row |

These must use `save_event_target_as`, never `save_global_event_target_as`. Regular event targets remain in the originating effect chain and carry into events fired from it. The public API must copy every persistent fact into its sequence row or job row before it returns.

There is no silent recovery from a missing event target. For example, a `selected_state` call without `natural_disaster_call_target_state` is rejected. Random selection happens only when the caller explicitly chooses a random-capable target mode.

### Outputs

The wrapper leaves these temporary variables for the caller:

| Output | Meaning |
| --- | --- |
| `natural_disaster_call_result` | Result enum `accepted` or `rejected`; generic sequence joining is not part of the public contract |
| `natural_disaster_call_reject_reason` | Live enum identifying invalid family, severity, sequence, target, region, heat exclusion, abnormal access, policy, scale, caller proof, or scenario context |
| `natural_disaster_call_sequence_id` | Allocated sequence id, `0` on rejection |
| `natural_disaster_call_primary_job_count` | Number of accepted primary impact jobs |

The caller must initialize all four output temporary variables before invoking the scripted effect. The offline variable documentation warns that a temporary first created inside a scripted effect may not reliably exist outside it, while a temporary created before the call is carried into the effect and can be modified safely. Inputs are reset to their documented defaults before the wrapper returns. Outputs are not reset. Regular input event targets cannot be manually cleared, so no internal logic may read them after normalization.

### Result and rejection constants

Add these categories to `common/script_constants/013_natural_disasters_constants.txt`:

```text
natural_disaster_call_result = {
	schema = {
		any_key = yes
		data = int
	}

	rejected = 0
	accepted = 1
}

The accepted implementation deliberately does not expose a generic `joined` result or parent-sequence input. Internal physical follow-ups use a separately validated continuation override and never broaden the public API.

natural_disaster_call_reject_reason = {
	schema = {
		any_key = yes
		data = int
	}

	none = 0
	invalid_family = 1
	invalid_family_group = 2
	invalid_severity = 3
	invalid_sequence_mode = 4
	missing_target = 5
	invalid_target = 6
	no_eligible_target = 7
	invalid_region = 8
	heat_exclusion = 9
	abnormal_locked = 10
	invalid_parent = 11
}
```

Also add exact enum categories for `natural_disaster_family_group`, `natural_disaster_override_mode`, `natural_disaster_job_type`, and `natural_disaster_sequence_status`. Do not represent boolean state with numeric variables. Use flags for active or inactive state and enums only when more than two states exist.

## Sequence identity and global ledger

`global.natural_disaster_next_sequence_id` is incremented once per accepted top-level call. Sequence ids are never reused during a campaign.

The active ledger is a set of aligned global arrays. Every row index refers to one active sequence.

### Identity and attribution arrays

- `global.natural_disaster_sequence_id_entries`
- `global.natural_disaster_sequence_owner_entries`, scope array containing the first affected country
- `global.natural_disaster_sequence_actor_entries`, scope array containing the attributed actor when present
- `global.natural_disaster_sequence_has_actor_entries`
- `global.natural_disaster_sequence_caller_type_entries`
- `global.natural_disaster_sequence_caller_event_id_entries`
- `global.natural_disaster_sequence_log_mode_entries`
- `global.natural_disaster_sequence_status_entries`

### Policy and mode arrays

- `global.natural_disaster_sequence_family_entries`
- `global.natural_disaster_sequence_family_group_entries`
- `global.natural_disaster_sequence_target_mode_entries`
- `global.natural_disaster_sequence_target_region_entries`
- `global.natural_disaster_sequence_target_country_entries`, scope array when selection is constrained to a country
- `global.natural_disaster_sequence_has_target_country_entries`
- `global.natural_disaster_sequence_mode_entries`
- `global.natural_disaster_sequence_severity_entries`
- `global.natural_disaster_sequence_news_policy_entries`
- `global.natural_disaster_sequence_report_policy_entries`
- `global.natural_disaster_sequence_aftermath_policy_entries`
- `global.natural_disaster_sequence_chain_policy_entries`
- `global.natural_disaster_sequence_death_override_mode_entries`
- `global.natural_disaster_sequence_death_scale_entries`
- `global.natural_disaster_sequence_damage_override_mode_entries`
- `global.natural_disaster_sequence_damage_scale_entries`

### Progress and cleanup arrays

- `global.natural_disaster_sequence_created_day_entries`
- `global.natural_disaster_sequence_expiry_day_entries`
- `global.natural_disaster_sequence_last_impact_day_entries`
- `global.natural_disaster_sequence_total_impact_entries`
- `global.natural_disaster_sequence_remaining_impact_entries`
- `global.natural_disaster_sequence_completed_impact_entries`
- `global.natural_disaster_sequence_pending_impact_entries`
- `global.natural_disaster_sequence_pending_report_entries`
- `global.natural_disaster_sequence_pending_followup_entries`
- `global.natural_disaster_sequence_open_card_entries`
- `global.natural_disaster_sequence_news_count_entries`
- `global.natural_disaster_sequence_history_written_entries`

`natural_disaster_get_sequence_index = yes` receives temporary `natural_disaster_current_sequence_id` and sets temporary `natural_disaster_current_sequence_index`. It searches only `global.natural_disaster_sequence_id_entries` and returns `-1` when absent. Every mutation checks the index before reading a parallel array.

The ledger holds active sequences only. Completed rows are removed from every aligned array using the same index. Campaign history belongs in the existing event log plus compact aggregate counters, not in an ever-growing second disaster ledger.

## Country-owned delayed-job queues

Each affected country owns its own aligned arrays. Queue work never requires iterating all countries. A call schedules the worker directly on every queue owner that receives at least one job.

### Job arrays

- `natural_disaster_job_id_entries`
- `natural_disaster_job_type_entries`
- `natural_disaster_job_sequence_id_entries`
- `natural_disaster_job_due_day_entries`
- `natural_disaster_job_target_state_entries`, scope array
- `natural_disaster_job_origin_state_entries`, scope array with a numeric sentinel companion when no origin exists
- `natural_disaster_job_family_entries`
- `natural_disaster_job_severity_entries`
- `natural_disaster_job_news_policy_entries`
- `natural_disaster_job_report_policy_entries`
- `natural_disaster_job_aftermath_policy_entries`
- `natural_disaster_job_chain_policy_entries`
- `natural_disaster_job_death_override_mode_entries`
- `natural_disaster_job_death_scale_entries`
- `natural_disaster_job_damage_override_mode_entries`
- `natural_disaster_job_damage_scale_entries`
- `natural_disaster_job_attempt_entries`

Country flags:

- `natural_disaster_queue_active`

Country variables:

- `natural_disaster_next_job_id`

Job types must include `primary_impact`, `secondary_impact`, `affected_report`, `caller_report`, `news`, `family_followup`, `card_reassessment`, and `sequence_expiry`.

### Scope-array implementation gate

Official documentation confirms that `add_to_array` stores the current scope when `value` is omitted and that `for_each_scope_loop` changes to each stored scope. Before the full queue is implemented, make a focused prototype that proves a state scope stored in `natural_disaster_job_target_state_entries` can be recovered at the same dynamic index as its scalar metadata.

Preferred indexed form:

```text
var:natural_disaster_job_target_state_entries^natural_disaster_current_job_index = {
	save_event_target_as = natural_disaster_current_target_state
}
```

If the parser rejects indexed array scope access, stop and report the blocker. Do not replace it with a global event target, a random target, a fixed state list, or a world iteration. An accepted alternative needs explicit user approval because it changes the concurrency model.

### Worker event

Use `chaosx.nr13.2` as a hidden, triggered-only country event:

```text
country_event = {
	id = chaosx.nr13.2
	hidden = yes
	is_triggered_only = yes

	immediate = {
		natural_disaster_process_due_job = yes
	}
}
```

`natural_disaster_process_due_job` performs these steps:

1. Find the due job with the lowest due day. Ties use the lowest job id.
2. Copy every scalar field to temporary variables.
3. Rebuild `natural_disaster_current_target_state` and `natural_disaster_current_target_country` as regular event targets.
4. Remove the selected index from every job array.
5. Remove the job's sequence and due-day pair from the reservation ledger.
6. Dispatch the copied job by `natural_disaster_current_job_type`.
7. Clear queue flags and variables if no work remains.

Every enqueue schedules one `chaosx.nr13.2` wakeup on the queue owner for that job's absolute due day. The delayed event carries no mutable job data. On wakeup, it pops the earliest due row from the owner's persistent queue. If the corresponding job was canceled or moved, the delayed event finds no due row and exits without changing another job.

Hearts of Iron IV does not expose a general cancellation effect for an already scheduled country event. The one-wakeup-per-enqueue rule therefore treats old wakeups as harmless stale notifications after transfer or cancellation. A moved job receives a new wakeup on its new owner. Its old owner's wakeup becomes a no-op. This preserves target reliability without pretending that only one delayed event can exist per country.

The due check uses the supported long comparison:

```text
check_variable = {
	var = global.num_days
	value = natural_disaster_job_due_day_entries^i
	compare = greater_than_or_equals
}
```

The event delay is passed through a normal variable because duration fields do not universally accept `constant:` tokens:

```text
set_variable = {
	natural_disaster_worker_delay_days = natural_disaster_current_job_due_day
}
subtract_from_variable = { natural_disaster_worker_delay_days = global.num_days }
country_event = {
	id = chaosx.nr13.2
	days = natural_disaster_worker_delay_days
}
clear_variable = natural_disaster_worker_delay_days
```

The worker delay must be at least one day. A newly appended already-due job is moved to the following day, never processed recursively on the same date. Every enqueue increments a debug-only scheduled-wakeup counter and every worker event decrements it. The counter is diagnostic and does not control gameplay.

## Same-day prevention and sequence spacing

Every delayed subevent uses an absolute due day. The first impact is scheduled from `natural_disaster_sequence.first_impact_min_days` through `first_impact_max_days`. Later primary impacts add a mode-specific gap. Every gap is clamped to at least `natural_disaster_sequence.same_day_guard_days`.

Only the first primary impact is queued when a sequence opens. The sequence stores its total and remaining primary impact count. After an impact, the handler first reserves its affected-country report day, then any news and follow-up days, then the next primary impact day. This order preserves the required one-day or two-day report window and moves the next impact later if it would collide.

At sequence creation, `total_impact` is the normalized count, `remaining_impact` is that count minus one, and `pending_impact` is one after the first job is enqueued. Completing or canceling the queued impact decrements `pending_impact`. If `remaining_impact` is positive, scheduling the next primary decrements `remaining_impact` and increments `pending_impact`.

Maintain a separate global reservation ledger:

- `global.natural_disaster_reserved_sequence_id_entries`
- `global.natural_disaster_reserved_due_day_entries`

`natural_disaster_reserve_sequence_due_day = yes` receives a sequence id and candidate absolute day. It enforces a minimum of the next calendar day, searches the paired reservation arrays, and advances the candidate one day until the pair is unique. It then stores the pair and returns `natural_disaster_reserved_due_day`. Every queued job uses the returned day.

The worker removes the reservation pair when it pops the job. Cancellation and transfer remove the old pair before reserving the replacement. Sequence expiry removes every reservation owned by the expiring sequence. Jobs from different sequences may share a date, but two delayed jobs from the same sequence may not.

Store `natural_disaster_last_impact_day` on each impacted state. A state is eligible only when that value differs from `global.num_days`. This avoids timed-flag duration parsing and prevents two independent sequences from striking the same state on the same day.

The current draft trigger excludes `natural_disaster_impact_guard`. Replace that check with a dedicated scripted trigger using the date variable, or prove a constant-safe timed flag assignment and document it. Do not keep both mechanisms.

Reports are always scheduled one or two days after the relevant impact by `natural_disaster_sequence.report_min_days` and `report_max_days`. The report reserves its date before news, follow-ups, and the next impact. News and reports are separate job types and must not execute in the impact's same effect block.

## Target resolution

### General validity

`natural_disaster_is_valid_impact_state` remains the baseline and must require:

- passable state
- positive `state_population_k`
- existing owner
- no same-day impact recorded on that state
- family-specific eligibility

An open aftermath card does not make a state invalid. Unresolved aftermath is a vulnerability factor and repeated impacts must merge or supersede the existing card.

The draft `natural_disaster_closed_card` exclusion should not permanently immunize a state. If the flag means temporary recovery protection, rename it to a duration-specific concept and clear it through a scheduled job. If it means card presentation only, remove it from impact eligibility.

### Explicit state

`selected_state` requires `natural_disaster_call_target_state`. The target must pass the exact family trigger. If a target country is also supplied, the state must be owned by that country at normalization time. Failure rejects the call.

### Explicit country

`selected_country` requires `natural_disaster_call_target_country`. The system builds a temporary array of the country's valid owned and controlled states, applies family weights, and chooses one. No eligible state rejects the call.

### Explicit strategic region

`selected_region` requires a positive `natural_disaster_call_target_region`. Use `meta_trigger` or `meta_effect` to inject the numeric region into the static region field after a parser proof:

```text
meta_effect = {
	text = {
		random_state = {
			limit = {
				is_in_strategic_region = [REGION_ID]
				natural_disaster_is_valid_family_target = yes
			}
			save_event_target_as = natural_disaster_current_target_state
		}
	}
	REGION_ID = "[?natural_disaster_call_target_region|.0]"
}
```

Verify the exact strategic-region trigger against current vanilla documentation before implementation. If the actual field is `region =`, use that documented form instead. A supplied target country constrains region selection to its owned and controlled states. Without a supplied country, any valid state in the named region is eligible. An invalid or empty region rejects the call.

### Random and weighted modes

`random_valid`, `coast`, `nearby_enemy`, and `dense_state` are explicitly random-capable. Selection builds a bounded temporary candidate array from the relevant country or strategic neighborhood. It never performs a hidden global country loop from an on-action.

For the normal random Event 013 entry, the shared event selector already chooses a country host. State selection is limited to that host and family-compatible nearby states. Global and barrage sequence modes may select a bounded list once at call time under their explicit contract. They do not establish periodic global scans.

### Family target routing

Preserve the 25 family ids in the draft constants:

| IDs | Family group | Required target behavior |
| --- | --- | --- |
| 1 | earthquake | Populated passable state, tectonic weighting is future data, dense and built states receive higher weight |
| 2 | flood | River, lake, coast, lowland, or high infrastructure exposure when data is available |
| 3, 19, 20 | tropical cyclone, tsunami, storm surge | Coastal state required |
| 4, 5, 6, 7, 25 | extreme wind, tornado outbreak, thunderstorm, hailstorm, moving storm corridor | Regional or corridor-capable land states |
| 8, 9 | blizzard, cold wave | Cold climate weighting and winter weighting when exposed through supported state data |
| 10 | heat wave | Must pass the Event 051 exclusion guard |
| 11, 12 | drought, dust and sandstorm | Dry climate weighting, Event 099 may bridge only to family 12 |
| 13 | wildfire | Dry, forested, damaged, or unresolved states weighted higher |
| 14, 15 | dry and wet mass movement | Mountain, hill, rain, or damaged infrastructure weighting when supported |
| 16, 17, 18, 24 | volcanic eruption, ashfall, lahar, massive eruption | Family chain maintains origin state and applies bounded spread |
| 21, 22 | meteor impact, meteor shower | Any valid state with abnormal access rules for extreme paths |
| 23 | whole Earth rupture | Abnormal-only bounded global path, never a world-end path |

Family data that the engine does not expose reliably must remain a declared uncertainty. Do not infer unsupported biome or tectonic data from localisation names.

## Severity and sequence normalization

Preserve the draft severity ids from local through abnormal and the sequence modes from single through barrage.

`natural_disaster_normalize_sequence_count = yes` derives the hit count from mode and current Event 013 evolution when the caller omits it. An explicit count is clamped to the documented mode range. Clamping is an API rule, not a hidden fallback. The public docs and call tooltip must state the allowed range.

Baseline, Evolution I, Evolution II, and Evolution III ranges come from `natural_disaster_sequence.*` in the draft constants. Evolution II remains materially harder through higher hit count, shorter spacing, increased lethality, increased spread, and more demanding aftermath. Evolution III uses abnormal paths and extreme family behavior, but does not end the world.

Abnormal severity or an abnormal-only family must pass `natural_disaster_can_open_evolution_iii` and `natural_disaster_abnormal_family_is_allowed`. A failed explicit abnormal request is rejected. It does not downgrade itself to catastrophic.

## Family-specific damage API

The impact dispatch is:

```text
natural_disaster_apply_impact = {
	natural_disaster_get_family_profile = yes
	natural_disaster_calculate_deaths = yes
	natural_disaster_register_deaths = yes
	natural_disaster_calculate_damage_points = yes
	natural_disaster_apply_family_damage = yes
	natural_disaster_open_or_merge_aftermath_card = yes
	natural_disaster_schedule_impact_outputs = yes
}
```

`natural_disaster_apply_family_damage` routes to named family helpers such as:

- `natural_disaster_damage_earthquake`
- `natural_disaster_damage_flood`
- `natural_disaster_damage_tropical_cyclone`
- `natural_disaster_damage_wildfire`
- `natural_disaster_damage_volcanic_eruption`
- `natural_disaster_damage_tsunami`
- `natural_disaster_damage_meteor_impact`

Each helper owns a weighted building profile. Earthquakes may emphasize infrastructure, civilian industry, and military industry. Floods may emphasize infrastructure, rail, supply nodes, and local industry. Cyclones and storm surge may emphasize ports, dockyards, infrastructure, radar, and air bases. Wildfires may emphasize infrastructure, resources, and civilian industry. Meteor and abnormal families may use broader profiles with explicit caps.

Building type is static in `damage_building`. Use `meta_effect` to select the verified building token after the family profile chooses an enum. Dynamic damage amount remains a variable.

Do not use `damage_buildings_in_random_states` for Event 013 impacts. It discards the resolved state and family profile. Do not use a single generic damage roll for all families.

Death and damage overrides modify the resolved family result. They do not replace family identity. `suppress` is permitted only when explicitly selected by a caller contract. A missing scale in `multiply` or `replace` mode rejects the call rather than assuming a value.

## Deaths integration

Add `natural_disaster` as the next unused value in `chaos_meter_deaths_reason` in `common/script_constants/chaos_meter_constants.txt`. At the time of this plan, the intended value is `14`. Confirm the enum immediately before implementation because parallel work may allocate it.

Every state population loss routes through `chaos_meter_register_state_civilian_deaths_percent = yes`:

```text
set_temp_variable = {
	chaos_state_deaths_percent = natural_disaster_current_death_percent
}
set_temp_variable = {
	chaos_state_deaths_mult = natural_disaster_current_death_multiplier
}
set_temp_variable = {
	chaos_state_deaths_cap_factor = natural_disaster_current_death_cap_factor
}
set_temp_variable = {
	chaos_deaths_reason = constant:chaos_meter_deaths_reason.natural_disaster
}
chaos_meter_register_state_civilian_deaths_percent = yes
set_variable = {
	natural_disaster_last_deaths = chaos_deaths_change
}
```

The Deaths helper's default state cap factor is too restrictive for catastrophic and abnormal disaster paths. Event 013 must calculate a severity-specific cap factor and still respect the shared hard maximum. Family lethality, severity fraction, warning result, preparedness, war, stability, unresolved aftermath, evolution, neighbor falloff, and explicit override all feed the calculated percentage before registration.

Event 013 casualties must use the shared Deaths transaction. A standalone population-only helper would bypass required Deaths attribution and does not belong in the shared API.

## Aftermath card ownership

Each state owns at most one active aftermath card. A repeated impact on the same state merges into or supersedes the card. It does not create a second card row.

### State flags

- `natural_disaster_aftermath_active`
- `natural_disaster_warning_active`
- `natural_disaster_warning_action_taken`
- `natural_disaster_report_pending`
- `natural_disaster_heat_aftermath`

### State variables

- `natural_disaster_active_sequence_id`
- `natural_disaster_family`
- `natural_disaster_severity`
- `natural_disaster_card_state`
- `natural_disaster_phase`
- `natural_disaster_recovery_score`
- `natural_disaster_chain_risk`
- `natural_disaster_last_impact_day`
- `natural_disaster_last_deaths`
- `natural_disaster_total_deaths`
- `natural_disaster_damage_points`
- `natural_disaster_report_status`
- `natural_disaster_next_reassessment_day`
- `natural_disaster_card_expiry_day`

When a card changes sequence ownership, decrement the old sequence's `open_card` counter before incrementing the new sequence's counter. When a weaker repeat belongs to the same sequence, keep the stronger severity, accumulate bounded damage and deaths, refresh the reassessment date, and retain one card counter.

Card phases are warning, early rescue, middle stabilization, late reconstruction, and closed. Phase changes are driven by decision completion and queued `card_reassessment` jobs. There is no periodic country maintenance hook.

`natural_disaster_close_card = yes` removes active modifiers, clears active flags and current-card variables, decrements the owning sequence counter, and preserves only compact historical country or global counters needed for achievements and statistics.

## Reliable reports, news, and follow-ups

Every persistent job copies the relevant policies from its sequence row. No delayed handler reads a caller's temporary variable.

### Affected-country report

After a serious impact, `affected_country`, `global`, and `delayed_batch` policies enqueue a report on the affected country with a one-day or two-day delay. The report family is derived from persistent job data. The report event is not chosen from current world state alone.

Use these event id bands:

- `chaosx.nr13.101` through `chaosx.nr13.125` for family-specific affected-country reports
- `chaosx.nr13.201` through `chaosx.nr13.225` for family-specific news events

Store `report_event_base = 100` and `news_event_base = 200` in `natural_disaster_event`. Use a meta effect to build the static event id from the family integer after a focused parser proof.

`report_policy = caller` sends the report to the original caller country. The sequence owner scope array must therefore be complemented by a caller-country scope array if caller and first affected country can differ. Add `global.natural_disaster_sequence_caller_country_entries` and `global.natural_disaster_sequence_has_caller_country_entries` when this policy is implemented.

`report_policy = silent` creates no popup but does not suppress aftermath card activation. `aftermath_policy = none` suppresses the card independently.

`report_policy = global` fires one global news-style report event. It does not loop over countries and does not enqueue one country event for every tag.

### News

News policy evaluates after a primary impact:

- `always` queues news for every primary impact, still respecting the no-same-day worker rule
- `first_family` queues only the first family occurrence in a sequence
- `major_only` requires the severity threshold defined in constants
- `meaningful` uses severity, deaths, damage, and family cooldown
- `none` queues no news

News cooldown is tracked by family, not by report. It must not suppress the affected-country report.

### Follow-ups

Family follow-up jobs join the parent sequence through a separately validated internal continuation override. They increment and decrement the parent's pending follow-up counter and never write another Event 013 history row. A generic caller-supplied `natural_disaster_call_parent_sequence_id` is not part of the live API.

Family chain examples include aftershock, tsunami, famine, disease, wildfire spread, refugee pressure, supply collapse, lahar, and political shock. A follow-up may call another event only through an explicit bridge contract. If that receiving event has no live implementation, keep the follow-up inside Event 013 rather than invoking a placeholder.

## One Event 013 history row

### Normal random Event 013 firing

The normal event selector currently calls `fire_event_by_temp_id_no_cluster = yes`, then invokes the repeatable-event handler. Event 013 must prepare its target and sequence before the shared handler records the row.

Add a narrow branch inside `fire_event_by_temp_id_no_cluster`:

```text
if = {
	limit = {
		check_variable = {
			var = event_id
			value = constant:natural_disaster_event.id
			compare = equals
		}
	}
	natural_disaster_prepare_random_event_fire = yes
}
```

Preparation creates the sequence with `natural_disaster_log_mode.event_system`, resolves the history actor, and stores `natural_disaster_prefire_sequence_id` on the firing country. The canonical `chaosx.nr13.1` event consumes that prepared sequence and does not create another one. A direct console or scripted fire of `.1` without the marker opens a fresh sequence through the normal wrapper.

`events_log_set_default_actor_for_current_event` needs an Event 013 branch that reads `natural_disaster_history_actor` from the active regular event target or an explicit actor override prepared before logging.

### External API firing

An external wrapper call uses `natural_disaster_log_mode.event_013_history`. It records one row directly through `record_events_log_history_entry` with a temporary event-id override set to 13. It must not call `on_repeatable_event_fired`, because that handler also changes random-event pacing and repeatable event state.

Add optional shared inputs only if the existing logger cannot already accept them:

- `events_log_history_event_id_override`
- `events_log_history_actor_override`
- `events_log_history_has_actor_override`

The logger consumes and clears these temporaries in the same effect block.

### Log guard

`natural_disaster_sequence_history_written_entries` begins at zero. The only successful history writer changes it to one. Child impacts, reports, news, aftermath decisions, follow-ups, Event 099 bridge calls that join a sequence, and super-event presentation must not call a repeatable-event handler.

If Event 013 is fired as a cluster member, its sequence uses the existing event-system row owned by the cluster member path. The Event 013 system must not add a direct history row on top of that path.

### Actor propagation uncertainty

The offline wiki states that regular event targets carry into events fired from their effect chain. A focused test must confirm that the Event 013 actor target prepared before the root event remains available to the post-event shared logger in the current dispatch structure. If it does not, implement the explicit shared actor override above. Do not use a global event target as a substitute.

## Event 051 heat exclusion

Event 051 currently applies the country idea `heat_wave`. Event 013 family 10 must be ineligible while the candidate state's owner has that idea:

```text
OWNER = {
	NOT = { has_idea = heat_wave }
}
```

The draft trigger also checks `natural_disaster_heat_exclusion` and `natural_disaster_heat_aftermath`. Keep them only if Event 013 itself owns and clears them. Event 013 must not apply the Event 051 `heat_wave` idea, and Event 051 must not open Event 013 aftermath cards.

Because the current Event 051 idea is applied broadly by its own event, this guard can exclude Event 013 heat-wave targets broadly for the idea's active duration. That is the current live integration signal and must be validated in scenario testing. A narrower cross-event signal would change Event 051 and requires separate design approval.

## Event 046 isolation

Event 046 is an inactive placeholder. Event 013 must not call Event 046, use its namespace, expect a return value, or schedule a follow-up into it. Any Event 013 volcanic eruption, ashfall, or lahar behavior remains wholly owned by Event 013 until Event 046 receives an approved live contract.

No Event 046 file needs to change for the Event 013 scripted-system tranche.

## Event 099 narrow bridge

Event 099 may become a compatibility bridge into family 12, `dust_and_sandstorm`. It does not keep an independent damage implementation.

The bridge contract is:

- caller type `external_event`
- caller event id `99`
- family `dust_and_sandstorm`
- selected country when Event 099 has a clear root country, otherwise explicit `random_valid`
- severity `local`
- sequence mode `single`
- news policy `meaningful`
- report policy `affected_country`
- aftermath policy `normal`
- chain policy `family`
- log mode chosen to prevent duplicate Event 099 and Event 013 history rows

If Event 099 is fired through the normal random event system and already owns its Event 099 row, use `natural_disaster_log_mode.none` for its Event 013 child sequence. If design requires the history row to be Event 013 instead, Event 099 must stop being logged independently in the same change. This is a user-facing event-log choice and must be resolved before bridge implementation.

The existing `desert_storm` dynamic modifier is not automatically adopted. Event 013 should own a family-specific aftermath modifier with Event 013 naming. Reuse or migration of the existing modifier requires a deliberate audit of its live consumers.

## No world-iteration on-actions

Event 013 must not define or extend:

- `on_daily`
- `on_weekly`
- `on_monthly`
- other periodic on-actions that implicitly iterate every country

Permitted lifecycle hooks are narrow engine events with known scopes, such as a verified state-control change hook or capitulation hook. Each hook touches only the affected state, old owner, new controller or owner, and sequence rows directly referenced by the state card.

The preferred implementation needs no on-action for ordinary operation. Hidden queue events handle timing. If transfer support requires `on_state_control_changed`, verify ROOT and FROM scopes against current vanilla usage before adding the hook.

On state control change:

1. If the state has a pending or active card, rebuild its owner reference.
2. Move future state-targeted jobs to the new valid queue owner, preserving due day and sequence id.
3. Move or cancel the affected-country report according to whether it already fired.
4. Preserve the sequence owner used for the existing history row.
5. Schedule a worker only on a country that received a moved job.

On country removal or annexation, jobs targeting still-existing states move to the new owner. Caller-only jobs whose caller no longer exists are canceled and their sequence counters are decremented. No cleanup path scans unrelated countries.

## Lifecycle and cleanup invariants

### Call lifecycle

1. Normalize inputs.
2. Validate enum ranges and required event targets.
3. Resolve explicit or random target.
4. Check abnormal access and heat exclusion.
5. Allocate or join a sequence.
6. Store policy and ownership in persistent rows.
7. Queue the first primary impact and the sequence expiry job. Later impacts, reports, news, and follow-ups are queued by the current impact after reserving unique sequence dates.
8. Write or defer exactly one history row according to log mode.
9. Return outputs and reset inputs.

### Job lifecycle

1. Enqueue aligned row.
2. Increment the matching sequence pending counter.
3. Reserve a unique sequence day and schedule the local country worker.
4. Pop the row and remove its reservation before dispatch.
5. Execute or safely cancel the job.
6. Decrement exactly one matching pending counter.
7. Queue any explicit child job and increment its counter.
8. Attempt sequence cleanup.

The `sequence_expiry` safety job does not increment a content pending counter. Normal sequence closure cancels its queue row and reservation. Its delayed worker wakeup later exits as stale.

### Sequence closure

A sequence can close only when all of these are zero:

- remaining primary impact count
- pending impact count
- pending report count
- pending follow-up count
- open aftermath card count

The sequence also needs a written history row unless its log mode is `none`. A `sequence_expiry` job is a safety close, not a silent deletion. It cancels stale jobs by sequence id, closes or detaches expired cards according to aftermath rules, balances every counter, then removes the ledger row.

### Array integrity

Create `natural_disaster_validate_sequence_arrays = yes` and `natural_disaster_validate_job_arrays = yes` as debug-only effects. They compare every aligned array length to the identity array length and log the first mismatch. They do not repair arrays. Automatic repair would hide data loss and is not allowed.

No debug effect remains wired to normal gameplay after validation.

## MTTH usage

Use `common/mtth/013_natural_disasters_mtth.txt` for weighted computation, not for hidden time progression.

Proposed entries:

- `natural_disaster_target_weight`
- `natural_disaster_warning_probability`
- `natural_disaster_followup_probability`
- `natural_disaster_ai_warning_weight`
- `natural_disaster_ai_recovery_weight`

The queue's due-day calculation remains explicit and deterministic. An MTTH variable may produce a weight or probability from current state, but it does not replace the persistent job schedule.

Example:

```text
set_temp_variable = {
	natural_disaster_current_target_weight = mtth:natural_disaster_target_weight
}
```

For decision AI, use the repository MTTH pattern to keep `ai_will_do` small:

```text
ai_will_do = {
	base = 1
	modifier = {
		factor = mtth:natural_disaster_ai_recovery_weight
	}
}
```

If the target field does not accept an MTTH token, compute it into a temporary variable in a supported effect or trigger context. Do not add verbose duplicated AI ladders merely to avoid a helper.

## Public wrapper examples

Every caller begins with this output preamble in the same outer effect block:

```text
set_temp_variable = {
	natural_disaster_call_result = constant:natural_disaster_call_result.rejected
}
set_temp_variable = {
	natural_disaster_call_reject_reason = constant:natural_disaster_call_reject_reason.none
}
set_temp_variable = { natural_disaster_call_sequence_id = 0 }
set_temp_variable = { natural_disaster_call_primary_job_count = 0 }
```

The examples below show the target and policy portion after that preamble.

### Explicit state and family

```text
GER = {
	random_owned_controlled_state = {
		limit = {
			natural_disaster_is_valid_impact_state = yes
		}
		save_event_target_as = natural_disaster_call_target_state
	}
}

set_temp_variable = {
	natural_disaster_call_caller_type = constant:natural_disaster_caller.external_event
}
set_temp_variable = { natural_disaster_call_caller_event_id = 77 }
set_temp_variable = {
	natural_disaster_call_family = constant:natural_disaster_family.earthquake
}
set_temp_variable = {
	natural_disaster_call_target_mode = constant:natural_disaster_target_mode.selected_state
}
set_temp_variable = { natural_disaster_call_target_state_supplied = 1 }
set_temp_variable = {
	natural_disaster_call_severity = constant:natural_disaster_severity.severe
}
set_temp_variable = {
	natural_disaster_call_sequence_mode = constant:natural_disaster_sequence_mode.single
}
set_temp_variable = {
	natural_disaster_call_news_policy = constant:natural_disaster_news_policy.meaningful
}
set_temp_variable = {
	natural_disaster_call_report_policy = constant:natural_disaster_report_policy.affected_country
}
set_temp_variable = {
	natural_disaster_call_aftermath_policy = constant:natural_disaster_aftermath_policy.normal
}
set_temp_variable = {
	natural_disaster_call_chain_policy = constant:natural_disaster_chain_policy.family
}
call_natural_disaster = yes
```

This example intentionally saves the state target before the wrapper and sets every policy that matters to the caller. The current execution scope still needs to be a country when the wrapper runs.

### Selected country with random compatible state

```text
FRA = {
	save_event_target_as = natural_disaster_call_target_country
}
set_temp_variable = { natural_disaster_call_target_country_supplied = 1 }
set_temp_variable = {
	natural_disaster_call_caller_type = constant:natural_disaster_caller.scenario
}
set_temp_variable = {
	natural_disaster_call_family = constant:natural_disaster_family.flood
}
set_temp_variable = {
	natural_disaster_call_target_mode = constant:natural_disaster_target_mode.selected_country
}
set_temp_variable = {
	natural_disaster_call_severity = constant:natural_disaster_severity.regional
}
set_temp_variable = {
	natural_disaster_call_sequence_mode = constant:natural_disaster_sequence_mode.regional_system
}
call_natural_disaster = yes
```

### Strategic region

```text
set_temp_variable = {
	natural_disaster_call_caller_type = constant:natural_disaster_caller.deity
}
set_temp_variable = {
	natural_disaster_call_family = constant:natural_disaster_family.tropical_cyclone
}
set_temp_variable = {
	natural_disaster_call_target_mode = constant:natural_disaster_target_mode.selected_region
}
set_temp_variable = { natural_disaster_call_target_region = 27 }
set_temp_variable = {
	natural_disaster_call_severity = constant:natural_disaster_severity.catastrophic
}
set_temp_variable = {
	natural_disaster_call_sequence_mode = constant:natural_disaster_sequence_mode.moving_corridor
}
call_natural_disaster = yes
```

The caller must treat rejection as a valid output. It must not fire a substitute family when the region has no eligible coastal state.

### Event 099 bridge

```text
ROOT = {
	save_event_target_as = natural_disaster_call_target_country
}
set_temp_variable = { natural_disaster_call_target_country_supplied = 1 }
set_temp_variable = {
	natural_disaster_call_caller_type = constant:natural_disaster_caller.external_event
}
set_temp_variable = { natural_disaster_call_caller_event_id = 99 }
set_temp_variable = {
	natural_disaster_call_family = constant:natural_disaster_family.dust_and_sandstorm
}
set_temp_variable = {
	natural_disaster_call_target_mode = constant:natural_disaster_target_mode.selected_country
}
set_temp_variable = {
	natural_disaster_call_severity = constant:natural_disaster_severity.local
}
set_temp_variable = {
	natural_disaster_call_sequence_mode = constant:natural_disaster_sequence_mode.single
}
set_temp_variable = {
	natural_disaster_call_log_mode = constant:natural_disaster_log_mode.none
}
call_natural_disaster = yes
```

This is only the scripted bridge shape. It is not permission to edit Event 099 during the Event 013 core implementation tranche.

### Historical child-follow-up sketch

```text
set_temp_variable = {
	# Rejected public shape; live code uses a private continuation override.
	natural_disaster_call_sequence_id_override_supplied = 1
	natural_disaster_call_sequence_id_override = natural_disaster_current_sequence_id
}
set_temp_variable = {
	natural_disaster_call_family = constant:natural_disaster_family.tsunami
}
set_temp_variable = {
	natural_disaster_call_target_mode = constant:natural_disaster_target_mode.selected_state
}
set_temp_variable = {
	natural_disaster_call_log_mode = constant:natural_disaster_log_mode.none
}
call_natural_disaster = yes
```

The private continuation id must refer to a live sequence. A stale id rejects the continuation and decrements no parent counter. External callers must not set this override.

## Event namespace allocation

Reserve:

| Event id | Purpose |
| --- | --- |
| `chaosx.nr13.1` | Canonical visible random entry and direct-fire entry |
| `chaosx.nr13.2` | Hidden country queue worker |
| `chaosx.nr13.3` | Optional hidden report dispatcher only if meta event-id dispatch is not parser-safe |
| `chaosx.nr13.4` | Optional hidden news dispatcher only if meta event-id dispatch is not parser-safe |
| `chaosx.nr13.101` to `.125` | Family affected-country reports |
| `chaosx.nr13.201` to `.225` | Family news events |

Do not assign a separate event id to each impact. Impact execution belongs in scripted effects and hidden worker dispatch. This prevents history duplication and keeps event ids for player-facing content.

If meta-built event ids fail a parser proof, use the reserved static dispatchers with explicit family branches. That is a supported implementation choice, not a gameplay fallback, because recipient, delay, family, and policy remain unchanged.

## Vanilla and repository precedents inspected

Use these as structural references only:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/TOA_Generic_Events.txt`, Chillan earthquake and delayed news structure
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/GOE_Raj.txt`, cyclone and famine chains
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/IRQ.txt`, flood building damage
- `common/scripted_effects/chaosx_event_cluster_effects.txt`, country-owned delayed queue precedent
- `events/chaosx_event_clusters.txt`, hidden queue worker event
- `common/scripted_effects/chaosx_settings_effects.txt`, random event dispatch
- `common/scripted_effects/chaosx_logic_effects.txt`, repeatable event handler and actor selection
- `common/scripted_effects/chaosx_events_log_effects.txt`, persistent event history arrays
- `common/scripted_effects/chaos_meter_effects.txt`, state civilian Deaths registration
- `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md`, public dynamic-effect conventions

Do not copy the vanilla disaster rewards as the Event 013 balance model. They are syntax and delay precedents, while Event 013 uses its own family, severity, Deaths, damage, and aftermath APIs.

## Required implementation proofs

### API and target proofs

- An explicit valid state produces `accepted`, one sequence id, and one primary job.
- An explicit invalid state produces `rejected` with `invalid_target`, no arrays changed, and no history row.
- A missing selected-state event target produces `missing_target`.
- A valid selected country resolves a family-compatible state inside that country.
- A selected region never silently selects outside the region.
- A coastal family rejects a region or country with no valid coast.
- An abnormal explicit call rejects when Evolution III access is absent.
- Two calls in the same outer effect block do not inherit omitted inputs from one another.

### Queue and concurrency proofs

- Two sequences can queue jobs for the same country without overwriting metadata.
- Two jobs for the same state on the same date cannot both impact that date.
- A multi-hit sequence spaces every impact by at least the configured guard.
- No two delayed jobs owned by one sequence reserve the same calendar day.
- A serious impact reserves its report inside the one-day or two-day window before reserving the next impact.
- A job row is removed from every aligned array before its handler appends another job.
- Every enqueue or moved job creates one matching delayed worker wakeup on its current owner.
- A stale wakeup left by cancellation or transfer does not consume a future job before its due day.
- A worker fired after all jobs were moved or canceled exits cleanly.
- State scope recovery from a dynamically indexed scope array is parser-safe and scope-correct.

### History proofs

- Normal random Event 013 produces one Event 013 row.
- A three-hit season with three reports, two news events, and two follow-ups still produces one Event 013 row.
- An external event call produces one Event 013 row without changing normal random-event cooldown or total fired state.
- A cluster-member Event 013 path does not add a second row.
- An Event 099 child path follows the chosen one-row ownership rule.
- History actor and affected country remain correct after delayed processing.

### Report and aftermath proofs

- A serious external call sends the affected country its family report one or two days after impact.
- The state card exists before the report and remains usable after the caller's effect chain ends.
- `report_policy = silent` suppresses popup only.
- `aftermath_policy = none` suppresses card only.
- Repeated impact merges or supersedes one card and balances both sequence card counters.
- Successful reconstruction closes the card without waiting for a periodic on-action.
- Expiry closes stale cards and balances every pending counter.

### Damage and Deaths proofs

- Every population reduction appears under Deaths reason `natural_disaster`.
- Local, severe, regional, catastrophic, and abnormal severity produce ordered death and damage expectations.
- Evolution II is materially harder than baseline under the same family and target.
- Evolution III abnormal paths remain bounded and never invoke a world-end outcome.
- Family building profiles differ in the actual damaged building types.
- A suppress override causes no deaths or damage only when explicitly requested.
- A multiply override scales the family result and retains its caps.

### Cross-event proofs

- A country with Event 051 `heat_wave` idea cannot receive Event 013 heat wave.
- Other Event 013 families remain eligible during Event 051 heat.
- Event 013 never fires Event 046.
- Event 046 remains an inert placeholder.
- Event 099 bridge, if implemented, calls only family 12 and applies no independent damage.

### Lifecycle proofs

- State control change moves or reassigns only jobs and cards tied to that state.
- Annexation does not leave a scheduled worker dependent on a nonexistent country.
- Every closed sequence is removed from all active arrays.
- Sequence and job array length validators report no mismatch after cancellation, transfer, supersession, and expiry scenarios.
- Search confirms Event 013 introduced no periodic all-country on-action.

## Uncertainties and stop conditions

These points require a focused parser or runtime proof before broad implementation:

1. Dynamic indexed access to a scope array element as a state scope.
2. Exact current trigger syntax for a numeric strategic region inside a meta-built block.
3. Regular event-target visibility from Event 013 prefire preparation through the post-event shared logger.
4. Whether the logger already has a safe actor or event-id override path that avoids a new shared input.
5. Exact ROOT, FROM, and state scope behavior of the current vanilla state-control change on-action.
6. The next unused `chaos_meter_deaths_reason` value immediately before the Deaths enum edit.
7. Whether the existing Event 099 row or the Event 013 child row owns history when the compatibility bridge is activated.

If items 1, 2, 3, or 5 fail, stop and report the exact result. Do not introduce a global event target, fixed state fallback, random substitute, world scan, or dropped report. The user must approve any architecture change that weakens the call contract.

## Suggested implementation order

1. Finalize constants and public enum gaps.
2. Prototype scope-array storage and dynamic retrieval in an isolated debug effect.
3. Implement call normalization, rejection outputs, sequence allocation, and array validators.
4. Implement country queue storage, worker scheduling, pop-before-dispatch, and expiry.
5. Implement target selection and family eligibility, including Event 051 exclusion.
6. Implement one representative family end to end with Deaths, family damage, report, and aftermath card.
7. Prove one-row history for normal random and external calls.
8. Expand the remaining family handlers and family reports.
9. Implement multi-hit modes, follow-ups, and bounded abnormal paths.
10. Implement aftermath decisions, AI, transfer, cancellation, and cleanup.
11. Resolve the Event 099 history ownership choice and add the narrow bridge only after the Event 013 API is stable.
12. Run event completion, localisation, decision and mission, and country package audits required by the project workflow before any completion claim.

## Completion boundary for this architecture tranche

This document defines the scripted-system contract only. It does not implement gameplay, localisation, assets, decisions, reports, news events, spreadsheets, Event 099 wiring, or Event 013 presentation. There are no approved simplifications or fallbacks in this plan. The uncertainties above are explicit implementation gates, not permission to weaken the system.
