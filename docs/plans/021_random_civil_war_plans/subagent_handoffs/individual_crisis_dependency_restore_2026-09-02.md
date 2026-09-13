# Individual-crisis dependency restore handoff

Status: read-only architecture handoff dated 2026-09-02.

This turn changed only this handoff file.

No gameplay files or constants files were edited, no balance target was selected, and no commit was created.

Parent and other workers' changes were left in place.

## Executive finding

The shared effect `adjust_individual_crisis_candidate_ticket_weight` is missing, not merely renamed.

There are six current generic callers and no declaration anywhere in the Chaos Redux repository or the inspected vanilla files.

The distinct effect `adjust_individual_crisis_existing_provider_candidate_ticket_weight` is also missing, with one current caller in the Random Terror wave pool.

Its similar name is not evidence of a replacement because its documented behavior excludes the candidate's current Random Terror package exactly once.

The shared trigger `individual_crisis_load_is_below_cap` is missing, with eleven current references and no declaration found.

No authoritative persistent load counter was found.

The targeting design explicitly derives load from provider lifecycle markers so that cleanup immediately changes eligibility without maintaining a second central counter.

The fixed-target companion `apply_individual_crisis_fixed_target_event_pressure` is documented but has no source declaration or caller found in this audit.

It is a separate restore item and must not be silently aliased to the candidate-ticket effect.

## Source basis

The primary design source was `docs/systems/event_system/individual_crisis_targeting.md`.

The shared numeric contract was read from `common/script_constants/individual_crisis_targeting_constants.txt`.

The exact current caller bodies were read in `common/scripted_effects/021_random_civil_war_parent_effects.txt`, `common/scripted_effects/024_video_game_in_sweden_effects.txt`, `common/scripted_effects/030_time_traveler_effects.txt`, `common/scripted_effects/031_random_terror_effects.txt`, and `common/scripted_effects/039_murder_mystery_integration_effects.txt`.

The fourteen provider lifecycle rows and their owner predicates were traced through the corresponding scripted trigger and effect files listed below.

The required `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-mtth` skill instructions were read before this audit.

The required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding were consulted.

The installed vanilla documentation was consulted, including `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, and the relevant effect and trigger entries for temporary variables, temporary arrays, loops, and scope selection.

The installed trigger documentation gives direct evidence for temporary-variable mutation in a trigger context, but the exact boundary must remain explicit.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:5108-5113` says that a hidden trigger can have side effects such as temporary variables.

Its example at `:5124-5135` contains `hidden_trigger = {`, `set_temp_variable = { unlock_compare = 0 }`, and `add_to_temp_variable = { unlock_compare = num_armies }` inside the trigger block.

The same installed file lists `add_to_temp_variable` under “Triggers for scope any” at `:601-604`, documents it as supported for any scope with examples at `:713-725`, and documents `set_temp_variable` as supported for any scope with examples at `:7482-7500`.

Those lines prove the documented hidden-trigger syntax and operator registration, but they do not explicitly state that every user-defined scripted trigger may mutate temporary variables.

Therefore the proposed load rebuild inside `individual_crisis_load_is_below_cap` remains an engine-contract validation item for the parent, not an assumption from memory.

The fixed-point schema is real, but every current candidate-ticket caller supplies a whole-number base after its own normalization.

The helper restore must therefore not invent fractional rounding, flooring, ceiling, or minimum behavior for callers that do not currently exist.

## Exact constants and caller-owned tuning

The following values are prescribed by the existing targeting constants file.

| Constant | Value | Use in this restore |
| --- | ---: | --- |
| `constant:individual_crisis_targeting.zero` | `0` | Empty load, zero base, and zero result. |
| `constant:individual_crisis_targeting.one` | `1` | One active-provider increment and the ordinary one-ticket base used by five callers. |
| `constant:individual_crisis_targeting.load_one_upper_bound` | `2` | Separates load one from load two without unsupported inclusive comparison syntax. |
| `constant:individual_crisis_targeting.active_cap` | `3` | Hard capacity cap. A load of three or more is not eligible and receives zero tickets. |
| `constant:individual_crisis_targeting.load_zero_tickets` | `4` | Candidate tickets at derived load zero. |
| `constant:individual_crisis_targeting.load_one_tickets` | `2` | Candidate tickets at derived load one. |
| `constant:individual_crisis_targeting.load_two_tickets` | `1` | Candidate tickets at derived load two. |
| `constant:individual_crisis_targeting.load_zero_factor` | `1.00` | Fixed-target companion factor only. Do not use for the candidate-ticket helper. |
| `constant:individual_crisis_targeting.load_one_factor` | `0.50` | Fixed-target companion factor only. Do not use for the candidate-ticket helper. |
| `constant:individual_crisis_targeting.load_two_factor` | `0.25` | Fixed-target companion factor only. Do not use for the candidate-ticket helper. |

The current Event021 caller additionally divides its owner score by `constant:event021_parent_tuning.target_pool_weight_scale`, rounds, and clamps it between one and `constant:event021_parent_tuning.target_pool_weight_cap` before invoking the missing helper.

The current values `target_pool_weight_scale = 100` and `target_pool_weight_cap = 10` are caller-owned tuning and are not selected or changed by this handoff.

The known quantization risk remains explicit: a reduced major factor such as `0.35` can produce a post-division value that rounds or clamps to the same base one as a normal candidate, so the helper then emits the same `4`, `2`, `1`, or `0` load-band ticket count.

That is a caller-side normalization issue for the later weighted baseline and compare, not a basis for silently changing the helper curve.

## Proposed source contract

### Generic effect

Proposed public identifier: `adjust_individual_crisis_candidate_ticket_weight`.

Execution context: the candidate country is current when the effect runs.

`THIS` identifies the current candidate scope where the caller uses it, but it is not a prefix for any temporary variable.

Required input: the caller sets the unprefixed temporary variable `individual_crisis_candidate_base_weight` immediately before invoking the effect.

Output: the effect sets the unprefixed temporary variable `individual_crisis_candidate_adjusted_weight` to an integer ticket count on every path.

Temporary variables are not scoped variables.

They have no country, ROOT, PREV, or THIS qualification.

They are unprefixed names resolved in the current evaluation context, so the implementation must not write `THIS.individual_crisis_candidate_base_weight`, `ROOT.individual_crisis_candidate_base_weight`, or `PREV.individual_crisis_candidate_base_weight`.

The effect owns no regular variables, country flags, ideas, event targets, arrays, or persistent counters.

The effect does not add or remove the candidate from any pool.

The existing caller owns the `while` loop that consumes the returned integer as repeated array entries.

### Source-ready arithmetic contract

The following is the narrow implementation shape the parent can apply after its required probability baseline.

```text
adjust_individual_crisis_candidate_ticket_weight = {
    set_temp_variable = {
        individual_crisis_candidate_adjusted_weight = constant:individual_crisis_targeting.zero
    }
    if = {
        limit = {
            check_variable = {
                var = individual_crisis_candidate_base_weight
                value = constant:individual_crisis_targeting.zero
                compare = greater_than
            }
            individual_crisis_load_is_below_cap = yes
        }
        if = {
            limit = {
                check_variable = {
                    var = individual_crisis_active_load
                    value = constant:individual_crisis_targeting.zero
                    compare = equals
                }
            }
            set_temp_variable = {
                individual_crisis_candidate_adjusted_weight = individual_crisis_candidate_base_weight
            }
            multiply_temp_variable = {
                individual_crisis_candidate_adjusted_weight = constant:individual_crisis_targeting.load_zero_tickets
            }
        }
        else_if = {
            limit = {
                check_variable = {
                    var = individual_crisis_active_load
                    value = constant:individual_crisis_targeting.load_one_upper_bound
                    compare = less_than
                }
            }
            set_temp_variable = {
                individual_crisis_candidate_adjusted_weight = individual_crisis_candidate_base_weight
            }
            multiply_temp_variable = {
                individual_crisis_candidate_adjusted_weight = constant:individual_crisis_targeting.load_one_tickets
            }
        }
        else = {
            set_temp_variable = {
                individual_crisis_candidate_adjusted_weight = individual_crisis_candidate_base_weight
            }
            multiply_temp_variable = {
                individual_crisis_candidate_adjusted_weight = constant:individual_crisis_targeting.load_two_tickets
            }
        }
    }
}
```

The code block is a contract sketch, not a gameplay edit made in this turn.

The parent should use the repository's exact Clausewitz formatting and effect syntax when applying it.

The `else` branch above is reached only after the cap trigger has accepted the candidate and the load is neither zero nor below the load-one upper bound, which means the valid remaining band is load two.

The cap trigger must still return false for load three or more, so that the output remains zero at and above the cap.

The curve is therefore exactly `base * 4` at load zero, `base * 2` at load one, `base * 1` at load two, and `0` at load three or more.

The helper must initialize the output before any conditional so a zero, missing, or capped candidate cannot inherit a temporary value from an earlier candidate evaluation.

### Shared cap trigger

Proposed public identifier: `individual_crisis_load_is_below_cap`.

Execution context: country scope when the trigger is evaluated.

Contract: rebuild `individual_crisis_active_load` from the fourteen provider predicates on every invocation, then return true only when the load is strictly less than `constant:individual_crisis_targeting.active_cap`.

The temporary load must be reset to `constant:individual_crisis_targeting.zero` before provider checks.

Each active provider contributes exactly one `constant:individual_crisis_targeting.one` increment regardless of how many states, fields, flags, or stages that provider owns.

The implementation must use the lower-level provider markers and predicates in the table below, not eligibility wrappers that themselves call this missing cap trigger.

The proposed trigger-side rebuild uses the documented `set_temp_variable` and `add_to_temp_variable` syntax shown above.

The installed documentation does not explicitly prove arbitrary scripted-trigger mutation beyond the documented `hidden_trigger` example, so the parent must validate this exact scripted-trigger context before claiming that the source contract is engine-safe.

If that validation cannot be established, leave the trigger-side mutation contract unresolved rather than replacing it with a persistent counter or an arbitrary blanket default.

If the parent chooses to factor the fourteen checks into provider triggers, each provider trigger must remain a pure candidate-country predicate and the cap trigger must remain the only load accumulator.

### Internal exclusion worker for the Random Terror caller

The existing Random Terror call is intentionally not a silent alias for the generic effect.

Proposed public identifier: `adjust_individual_crisis_existing_provider_candidate_ticket_weight`.

Scope and input/output are identical to the generic effect.

Its only semantic difference is that the current candidate's active Random Terror provider contributes zero for this load calculation because the candidate is already inside that provider package.

The narrow implementation can set a temporary exclusion marker in the current evaluation context, invoke a shared internal ticket-curve worker, and clear the marker immediately afterward.

Suggested temporary marker: `individual_crisis_exclude_random_terror`.

The Random Terror provider predicate must skip exactly one current Random Terror provider when this marker is active and must count every other active provider.

The generic public effect must clear or set that exclusion marker to zero before its own calculation so a previous specialized call cannot leak state across an `every_country` iteration.

The specialized effect must also clear it after the shared worker returns.

The marker is an implementation detail of the shared calculation and is not a new gameplay flag or persistent variable.

Do not subtract all Random Terror states, all Random Terror flags, or all providers with a broad `NOT` wrapper.

## Fourteen provider source contracts

The following table maps each documented provider to the authoritative reusable predicate or exact lifecycle marker that should feed the derived load.

The proposed `individual_crisis_provider_*_is_active` names are source-ready wrapper names, not declarations found in the current repository.

| # | Proposed provider wrapper | Candidate-country active test | Lifecycle evidence and restore risk |
| ---: | --- | --- | --- |
| 1 | `individual_crisis_provider_holy_realm_is_active` | Reuse `is_holy_realm_country = yes`, which checks `holy_realm_active`. | Set in `common/scripted_effects/003_holy_realm_effects.txt:1801`. An exact `clr_country_flag = holy_realm_active` search found no clear, so the owner lifecycle must prove or add cleanup before claiming that load drops after completion. This handoff does not invent that cleanup. |
| 2 | `individual_crisis_provider_soviet_collapse_is_active` | Reuse `is_soviet_collapse_active_origin_country = yes`. | `common/scripted_triggers/chaosx_liberation_release_triggers.txt:98-103` also validates existence, origin, and no active independence wave. The marker is set and cleared in `common/scripted_effects/005_soviet_collapse_effects.txt:5716` and `:5722`. |
| 3 | `individual_crisis_provider_fury_is_active` | Reuse `is_fury_actor = yes`, which checks `fury_actor`. | Set in `common/scripted_effects/007_fury_effects.txt:209` and cleared at `:1064`. Do not substitute `fury_actor_can_continue`, because that is a gameplay viability predicate rather than occupancy. |
| 4 | `individual_crisis_provider_secret_alliance_is_active` | Use `OR = { has_country_flag = secret_alliance_target_country has_country_flag = secret_alliance_active_member }`. | The target and member markers are set in `common/scripted_effects/011_secret_alliance_effects.txt:1010`, `:1045`, and `:1292`. Their owner clears occur at `:1341`, `:7752`, and the additional member cleanup sites at `:1680`, `:2379`, `:4906`, `:6064`, `:6072`, `:6270`, `:6297`, `:6339`, `:6415`, `:6889`, and `:7631`. `secret_alliance_founder` is derived from the active-member state and is not a replacement marker. |
| 5 | `individual_crisis_provider_natural_disaster_is_active` | Use `OR = { has_country_flag = natural_disaster_queue_active has_country_flag = natural_disaster_chain_mission_active natural_disaster_country_has_warning = yes natural_disaster_country_has_open_aftermath = yes }`. | `natural_disaster_country_has_warning` is defined at `common/scripted_triggers/013_natural_disasters_triggers.txt:678-686` and covers impact scheduled, warning scheduled, and warning active states. `natural_disaster_country_has_open_aftermath` is at `:671-676` and excludes unresolved recovery territory. Queue and chain markers are set at `common/scripted_effects/013_natural_disasters_effects.txt:1929` and `:6661`, and queue cleanup is at `:7563` with chain release at `:6954`. The aftermath state lifecycle is set at `:7816` and `:7838` and must be represented through the existing open-card trigger. Do not use the UI-only `natural_disaster_aftermath_category_visible` flag. |
| 6 | `individual_crisis_provider_utopia_manifesto_is_active` | Use `has_country_flag = utopia_manifesto_accepted`. | Set in `common/scripted_effects/015_utopia_manifesto_effects.txt:306` and cleared at `:364` and `:8037`. Do not use `utopia_manifesto_candidate_has_active_event_package`, because that broad trigger includes unrelated packages. |
| 7 | `individual_crisis_provider_brilliant_scientist_is_active` | Reuse `brilliant_scientist_is_current_host = yes`. | The predicate is at `common/scripted_triggers/016_brilliant_scientist_triggers.txt:91-93` and verifies the current-host marker plus `has_character = KRG_warren_kruger`. Current-host setup is at `common/scripted_effects/016_brilliant_scientist_effects.txt:464-465`; clears are at `:3030`, `common/scripted_effects/016_brilliant_scientist_country_effects.txt:983`, and `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:929`. Do not use the any-scope `brilliant_scientist_has_current_host` as the per-candidate test. |
| 8 | `individual_crisis_provider_resources_found_is_active` | Use `OR = { has_country_flag = resources_found_field_system_participant any_controlled_state = { resources_found_is_active_field = yes } }`. | The field predicate at `common/scripted_triggers/018_resources_found_triggers.txt:21-25` requires an active, non-closed, non-cave field sequence. The participant marker is set at `common/scripted_effects/018_resources_found_effects.txt:84` and cleared at `:143`, with cave cleanup at `common/scripted_effects/018_resources_found_cave_effects.txt:2368`. |
| 9 | `individual_crisis_provider_random_civil_war_is_active` | Use `has_country_flag = random_civil_war_active`. | The marker is set by `common/scripted_effects/021_random_civil_war_effects.txt:712` and `common/scripted_effects/021_random_civil_war_parent_effects.txt:2050`, `:2176`, `:3080`, and `:3198`. Clears are in `common/scripted_effects/021_random_civil_war_effects.txt:1623`, the parent effect at `:2871`, `:2897`, `:2976`, `:3585`, and `:3616`, and lifecycle cleanup at `common/scripted_effects/021_random_civil_war_lifecycle_effects.txt:886`. Do not substitute `random_civil_war_country_can_manage_crisis`, because it adds side and terminal gameplay gates. |
| 10 | `individual_crisis_provider_video_game_in_sweden_is_active` | Use `has_country_flag = video_game_in_sweden_program_active`. | The marker is set and cleared in `common/scripted_effects/024_video_game_in_sweden_effects.txt:174`, `:1648`, and `:1686`. Do not use `video_game_in_sweden_can_receive_program`, because that eligibility wrapper already calls the missing cap trigger and would recurse. |
| 11 | `individual_crisis_provider_riches_found_is_active` | Use `any_controlled_state = { riches_found_is_active_mine = yes }`. | `riches_found_is_active_mine` delegates to the active-mine state predicate at `common/scripted_triggers/029_riches_found_triggers.txt:158-163` and `:740`. Mine setup is at `common/scripted_effects/029_riches_found_effects.txt:250`; terminal cleanup clears active state at `:2134` and `:2234`, with collapse and cleanup at `common/scripted_effects/029_riches_found_incident_effects.txt:610` and `common/scripted_effects/029_riches_found_effects.txt:2171`. |
| 12 | `individual_crisis_provider_time_traveler_is_active` | Use `OR = { has_country_flag = time_traveler_prefire_pending has_idea = time_traveler }`. | The pending reservation is set, tested, and cleared in `events/030_time_traveler.txt:49`, `:68`, and `:77`. The timed `time_traveler` idea is added at `:79` and is an existing owner marker used by `events/016_brilliant_scientist.txt:372`, `common/scripted_effects/016_brilliant_scientist_context_effects.txt:684`, and `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:1471`. |
| 13 | `individual_crisis_provider_random_terror_is_active` | Reuse `random_terror_country_has_active_package = yes`. | The existing predicate combines `random_terror_affected_country` with active controlled state markers. Affected-country setup is at `common/scripted_effects/031_random_terror_effects.txt:622` and `:1274`, with clear at `:4222`; active state markers are initialized and cleared around `:296-327`. This wrapper is generic-load truth. The specialized Random Terror effect must exclude only this one current provider unit. |
| 14 | `individual_crisis_provider_murder_mystery_is_active` | Use `murder_mystery_runtime_is_active = yes` together with `has_country_flag = murder_mystery_original_host`. | Runtime activation and original-host registration are at `common/scripted_effects/039_murder_mystery_runtime_effects.txt:232-238`. The country marker clears at `:1941`, global runtime clears at `:1975`, and integration cleanup is at `common/scripted_effects/039_murder_mystery_integration_effects.txt:529-533`. A stale global runtime target without the original-host marker must not count the candidate. |

The provider wrappers must each contribute one unit only.

For providers that own several states or stages, `any_controlled_state` or an existing country helper is a boolean occupancy test, not a per-state increment.

For Secret Alliance, the founder, recruit, and sponsor flows share the same capacity gate, so the target/member marker OR must be used consistently.

For Natural Disasters, warning, impact sequencing, queue, chain mission, and aftermath remain one occupied slot throughout their lifecycle.

For Random Terror, follow-up phases continue the existing package without taking another slot, while a new candidate still sees the other active providers.

## Existing helpers and recursion boundaries

The following are authoritative reusable predicates already present in the repository and should be reused where their scope and meaning match the documented provider marker.

| Existing helper | Reuse decision |
| --- | --- |
| `is_holy_realm_country` | Reuse for the Holy Realm marker. |
| `is_soviet_collapse_active_origin_country` | Reuse for the Soviet Collapse origin package. |
| `is_fury_actor` | Reuse for Fury occupancy. |
| `natural_disaster_country_has_warning` and `natural_disaster_country_has_open_aftermath` | Reuse as the state-derived Natural Disaster lifecycle tests. |
| `brilliant_scientist_is_current_host` | Reuse as the candidate-scope Brilliant Scientist host test. |
| `resources_found_is_active_field` | Reuse inside a candidate-country controlled-state test. |
| `riches_found_is_active_mine` | Reuse inside a candidate-country controlled-state test. |
| `random_terror_country_has_active_package` | Reuse for generic Random Terror occupancy and as the exact unit omitted by the specialized effect. |
| `murder_mystery_runtime_is_active` | Reuse with `murder_mystery_original_host` for the candidate host. |

These existing eligibility wrappers must not be called from the load trigger or its provider wrappers because they recurse into the missing cap trigger or include broader gameplay conditions.

| Wrapper to avoid inside load calculation | Reason |
| --- | --- |
| `video_game_in_sweden_can_receive_program` | It calls `individual_crisis_load_is_below_cap`. Use the raw program-active marker. |
| `riches_found_is_eligible_discovery_country` | It calls the missing cap trigger. Use the active-mine state predicate. |
| `event021_parent_scenario_country_eligible` | It calls the missing cap trigger and is route eligibility, not occupancy. |
| `random_terror_country_is_eligible_wave_target` | It calls the missing cap trigger. Use `random_terror_country_has_active_package` directly. |
| `murder_mystery_prefire_host_is_valid` | It calls the missing cap trigger. Use runtime-active plus original-host markers. |
| `random_civil_war_country_can_manage_crisis` | It includes management-side gameplay restrictions beyond provider occupancy. |
| `utopia_manifesto_candidate_has_active_event_package` | It includes unrelated event packages. Use `utopia_manifesto_accepted`. |
| `fury_actor_can_continue` | It is continuation viability rather than active package occupancy. |

The neutral shared registry `common/scripted_effects/chaosx_dynamic_effects.txt` has no individual-crisis load or ticket helper.

The matching markdown registry `common/scripted_effects/chaosx_dynamic_effects.md` has no individual-crisis declaration to reuse.

The shared trigger registry contains classifiers but no individual-crisis load trigger.

The later owner patch should add the shared helper and its documentation to the existing neutral shared registry or to a dedicated shared individual-crisis file following the repository's registry convention.

It must not create a second central router or an undocumented alias.

## Exact current weighted callers

The following seven source references are the direct ticket-producing surfaces in the current workspace.

Line numbers are audit snapshots and may move when the parent restores the dependency.

| Surface | Current reference | Base input before missing effect | Output consumer |
| --- | --- | --- | --- |
| Event021 automatic target pool | `common/scripted_effects/021_random_civil_war_parent_effects.txt:4393` in `event021_parent_add_target_to_selection_pool` | Owner score after divide by `event021_parent_tuning.target_pool_weight_scale`, round, and clamp to the owner cap. | `individual_crisis_candidate_adjusted_weight` becomes `event021_parent_target_pool_remaining`; each positive unit adds `THIS` to `event021_parent_target_selection_pool`. |
| Event021 scenario target pool | `common/scripted_effects/021_random_civil_war_parent_effects.txt:4416` in `event021_parent_add_scenario_target_to_weighted_pool` | `constant:individual_crisis_targeting.one`. | Output becomes `event021_parent_scenario_pool_remaining`; each positive unit adds `THIS` to `event021_parent_scenario_target_pool`. |
| Event024 prefire host pool | `common/scripted_effects/024_video_game_in_sweden_effects.txt:14` in `video_game_in_sweden_add_current_country_to_prefire_pool` | `constant:individual_crisis_targeting.one`. | Output becomes `video_game_in_sweden_prefire_pool_remaining`; each positive unit adds `THIS` to `video_game_in_sweden_prefire_host_pool`. |
| Event030 prefire host pool | `common/scripted_effects/030_time_traveler_effects.txt:10` in `time_traveler_add_current_country_to_prefire_pool` | `constant:individual_crisis_targeting.one`. | Output becomes `time_traveler_prefire_pool_remaining`; each positive unit adds `THIS` to `time_traveler_prefire_host_pool`. |
| Event031 new Random Terror wave candidate | `common/scripted_effects/031_random_terror_effects.txt:970` in `random_terror_add_current_country_to_wave_target_pool` | `constant:random_terror_value.one`, equivalent to the targeting one base. | Output becomes `random_terror_wave_pool_remaining`; each positive unit adds `THIS` to `random_terror_wave_country_pool`. |
| Event031 existing Random Terror provider candidate | `common/scripted_effects/031_random_terror_effects.txt:967` in the same effect | `constant:random_terror_value.one`. | Uses the distinct existing-provider helper, then the same `random_terror_wave_pool_remaining` loop. The current provider is omitted once, not all Random Terror states. |
| Event039 prefire host pool | `common/scripted_effects/039_murder_mystery_integration_effects.txt:21` in `murder_mystery_add_current_country_to_prefire_pool` | `constant:murder_mystery_value.one`, equivalent to the targeting one base. | Output becomes `murder_mystery_prefire_pool_remaining`; each positive unit adds `THIS` to `murder_mystery_prefire_host_pool`. |

All current generic callers set `individual_crisis_candidate_base_weight` before the call and read `individual_crisis_candidate_adjusted_weight` afterward.

No current caller passes a fractional base to this helper.

Event021 is the only current caller with an owner-weighted base above one.

The other ordinary candidate surfaces begin at one and therefore produce exactly one load-band ticket multiplier before any later pool selection.

## Shared cap-trigger consumers

The missing `individual_crisis_load_is_below_cap` trigger has eleven current references.

| Current reference | Affected gate |
| --- | --- |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:345` | Event021 scenario-country eligibility. |
| `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:27` | Video Game in Sweden program host eligibility. |
| `common/scripted_triggers/029_riches_found_triggers.txt:737` | Riches Found discovery-country eligibility. |
| `common/scripted_triggers/031_random_terror_triggers.txt:108` | Random Terror wave-target eligibility. |
| `common/scripted_triggers/031_random_terror_triggers.txt:310` | Another Random Terror capacity-gated route. |
| `common/scripted_triggers/039_murder_mystery_integration_triggers.txt:29` | Murder Mystery prefire-host eligibility. |
| `events/005_soviet_collapse.txt:41` | Soviet Collapse capacity branch for the first relevant event path. |
| `events/005_soviet_collapse.txt:63` | Soviet Collapse capacity branch for the second relevant event path. |
| `events/005_soviet_collapse.txt:78` | Soviet Collapse capacity branch for the third relevant event path. |
| `events/030_time_traveler.txt:37` | Time Traveler prefire reservation failure path. |
| `events/030_time_traveler.txt:69` | Time Traveler handoff acceptance path. |

Restoring the trigger is therefore a shared eligibility repair, not only an Event021 fix.

Its provider calculation must be identical to the generic candidate helper's load calculation except for the explicit Random Terror current-provider exclusion used by the specialized effect.

## Zero, cap, and removal semantics

If `individual_crisis_candidate_base_weight` is zero or less, the adjusted output is zero and no candidate ticket is added.

If the derived active load is three or more, the adjusted output is zero and `individual_crisis_load_is_below_cap` is false.

At derived load zero, the output is base multiplied by four.

At derived load one, the output is base multiplied by two.

At derived load two, the output is base multiplied by one.

Missing flags, missing ideas, absent active fields, absent active mines, invalid runtime markers, and absent lifecycle predicates contribute zero.

The helper does not remove entries from an already-built temporary pool.

The helper is called during pool construction, so a zero output naturally causes the caller's existing positive-only `while` loop to add no entries.

If a candidate becomes invalid after pool construction, existing pool-owner selection and post-selection eligibility remain responsible for handling that stale scope.

Provider cleanup must clear the owner marker, idea, or active state that the provider predicate reads.

Because load is derived rather than centrally counted, the next trigger or effect invocation sees the reduced load immediately after that cleanup.

The helper must not add a new decrement effect, array removal pass, persistent load variable, or broad fallback marker.

Event021 increments `global.random_civil_war_scenario_eligible_count` before it invokes the ticket helper.

Consequently, a route-valid candidate that receives zero tickets at cap can still increment that separate eligible-count variable under the current caller ordering.

This handoff preserves that ordering and flags it for the parent to baseline or explicitly resolve because changing it would alter Event021 route semantics beyond dependency restoration.

The fixed-point schema creates one unresolved edge for future callers that supply fractional bases.

The restore should either keep the proven whole-ticket input contract or make an explicit rounding rule part of a later owner decision and probability baseline.

It must not silently floor a fraction to zero, round it to one, or apply a minimum that is not present in the existing caller contract.

## Probability baseline and compare matrix

The parent must baseline the complete weighted surfaces before applying the helper and run `hoi4.probability_compare` afterward with the same named scenarios.

This handoff selects no new numeric balance target.

The current MCP inspections were run before restoration and are not complete-pool evidence.

For Event021, Event024, Event031, and Event039, `hoi4.probability_inspect` returned status `PROBABILITY_SOURCE_INSPECTED` with `poolComplete = false` and zero exposed candidates because the missing effect prevents the source pool from being expanded.

For Event030, `hoi4.probability_inspect` returned the exact blocker `INTERNAL_ERROR: Unexpected internal error` with no artifact.

The later baseline must rerun Event030 after the helper is restored instead of treating that failure as a probability result.

### Event021 surfaces

Direct weighted surface: automatic target ticket pool in `event021_parent_add_target_to_selection_pool`.

Baseline the exact `TGT-01` through `TGT-10` scenarios from `docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md`.

`TGT-01` compares a stable minor against an unstable minor.

`TGT-02` compares an unstable minor against a stable major after Evolution I.

`TGT-03` compares a stable minor against an unstable major after Evolution I.

`TGT-04` compares a recent target against a fresh candidate.

`TGT-05` compares player and AI candidates.

`TGT-06` compares one complete actor against three actors after Evolution I.

`TGT-07` compares a nearby Event021 war against a distant one.

`TGT-08` verifies a nonhuman candidate receives zero.

`TGT-09` verifies a human Event006 candidate after the grace period.

`TGT-10` verifies an incompatible civil-war candidate receives zero.

Direct weighted surface: Event021 scenario target ticket pool in `event021_parent_add_scenario_target_to_weighted_pool`.

Baseline the exact `FRT-01` through `FRT-05` force-result target scenarios from the same matrix.

`FRT-01` covers a small coherent region.

`FRT-02` covers a medium case with two valid opposition regions.

`FRT-03` covers a major case with four actors and capacity pressure.

`FRT-04` covers a large map with one valid leader.

`FRT-05` covers two overlapping Event006 packages.

Capacity and scheduler gates that must be rerun with the restored cap trigger are `GLB-01` through `GLB-07`.

Cross-package capacity interactions that must be rerun are `CLU-01` through `CLU-05`.

Scenario-band coverage that must be rerun is `SCN-01` through `SCN-07`.

The matrix also names ARC, SEV, EVO, SPN, STR, SET, and REC groups, but those are downstream or adjacent Event021 weighted surfaces and should only be included in this dependency compare if the parent confirms that the restored candidate pool feeds them in the same scenario.

### Event024 surface

Direct weighted surface: Video Game in Sweden prefire host pool in `video_game_in_sweden_add_current_country_to_prefire_pool`.

Baseline the opening host-selection scenarios `P24-O1` through `P24-O4` from `docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_ai_probability_scenarios.md`.

Include `P24-F5` for an invalid or exhausted pool because it exercises the zero-output and pool-exhaustion path.

Do not claim that the helper alone establishes the later foreign-response, incident, escalation, crisis, or de-escalation balance groups.

### Event030 surface

Direct weighted surface: Time Traveler prefire host pool in `time_traveler_add_current_country_to_prefire_pool`.

Baseline every named host-selection projection `TT_AI_01` through `TT_AI_10` from `docs/specs/030_time_traveler_specs/specs/030_time_traveler_spec_part_10_scenario_integrations_ai_balance.md`.

Include the pending-reservation and timed-idea transitions in the same later scenario run because they change whether a candidate is already occupied.

Do not use the earlier MCP internal error as a balance conclusion.

### Event031 surfaces

Direct weighted surface: new Random Terror wave candidates using the generic helper.

Direct weighted surface: existing Random Terror package candidates using the specialized helper that excludes one current provider.

Baseline the exact `P01_stable_peace_state`, `P02_unstable_wartime_authoritarian`, `P03_occupied_resistance_context`, `P04_successful_response`, `P05_transnational_safe_haven`, `P06_territorial_spawn`, `P07_muslim_government_against_jihadist`, `P08_cannibal_border`, `P09_major_intervention`, and `P10_maximum_scenario` scenarios from `docs/specs/031_random_terror_specs/031_random_terror_spec_part_9_ai_balance_probability.md`.

The compare must include at least one candidate with an active Random Terror package and another candidate with no current package in the same world state so the one-provider exclusion can be observed.

Do not treat the specialized branch as a new balance target.

### Event039 surface

Direct weighted surface: Murder Mystery prefire host pool in `murder_mystery_add_current_country_to_prefire_pool`.

Baseline the exact named scenarios `Scenario A` through `Scenario J` from `docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_13_ai_probability.md`.

`Scenario A` is a stable major with strong agency.

`Scenario B` is a war-torn major with weak agency.

`Scenario C` is a small eligible player country.

`Scenario D` is a secondary with strong shared evidence.

`Scenario E` is a secondary near revolt.

`Scenario F` is an Assassin State immediate-threat case.

`Scenario G` is a strong decentralized movement.

`Scenario H` is a pragmatic industrial movement.

`Scenario I` is a ready World of Anarchy case.

`Scenario J` is an unlocked but collapsing World of Anarchy case.

The compare must preserve the existing runtime-active and original-host requirement and must not treat a stale global runtime target as an eligible country.

## MCP evidence

The required weighted-logic workflow began with `hoi4.probability_inspect` on each direct owner effect.

The Event021 artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92c523351c5cb33531569c7aeac4793fb08fc65188caa96b9f59f7ca341eef00/afdfc2ed8d19593247aadd6aa95fade5ba3c7db2a823d75826589d6266eefbfd/probability-inspect-f7019a0a6ebd.json`.

The Event024 artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e718ce6cf4c6f7c13f6cf22b3a13f9e4ab90945b6dd6cef85e2c6d74aaa31575/e47aedf2f2d8512bcd13f225b22cc96c55f84f9d033ae5ff34eadc1a39eaeeb4/probability-inspect-a322f1f7e177.json`.

The Event031 artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e7d99cd54596c2c48d3a0020a3700b2b961cf1c5708e6a231c8f45c7e3a0d2a/bdd756e8ecc3b1ff14c4bd91ef979f9ec350ba04cae83a7e904aa7f3f334f183/probability-inspect-905aa529d150.json`.

The Event039 artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ace8772cfc1905fc9dc1b201b10c2ee2b271e984e86f81e2e23a9519ebb505e/2b749a081adebc94a9f631349bc67c9296ad295a02a4db1499d0462814c9c210/probability-inspect-12f8859e3d40.json`.

The Event030 inspect was attempted on `common/scripted_effects/030_time_traveler_effects.txt` and returned `INTERNAL_ERROR: Unexpected internal error` without an artifact.

The `chaosx_ai_probability_auditor` read-only audit was dispatched with the same repository paths and was instructed to report complete-pool status, exact scenario coverage, and blockers without choosing balance.

That auditor did not return a final report after repeated bounded waits and was shut down, so this handoff makes no additional auditor claim beyond the direct MCP evidence above.

No probability compare was run in this turn because the source pools are incomplete and the user explicitly reserves balance application for the parent after baseline.

## Narrow restore sequence for the parent

1. Preserve the current owner tuning and complete a baseline for each direct weighted surface before restoring the dependency, recording that the pre-restore pools are incomplete where the MCP says `poolComplete = false`.

2. Add the fourteen provider-country tests using the exact markers and existing predicates in this handoff.

3. Restore `individual_crisis_load_is_below_cap` so it resets and rebuilds a temporary load and returns true only below cap three.

4. Restore the generic ticket effect with explicit output initialization and the exact four, two, one, zero curve.

5. Restore the separate Random Terror existing-provider effect with a temporary exclusion marker in the current evaluation context that omits one current Random Terror provider and then resets the exclusion.

6. Keep the Event021 scenario eligible-count increment ordering unchanged until the parent has a baseline and an explicit route-semantics decision.

7. Reinspect all seven direct ticket callers and all eleven cap-trigger consumers.

8. Run the same named scenarios through `chaosx_ai_probability_auditor` with `hoi4.probability_compare` after restoration.

9. Audit provider cleanup in the same run, with special attention to the Holy Realm marker that currently has no exact clear found.

10. Treat the fixed-target pressure helper as a separate follow-up unless a later owner task explicitly includes it.

The restore should remain a narrow shared dependency patch plus matching helper documentation.

It should not rewrite candidate eligibility, change pool arrays, tune target scores, or introduce broad new tooling.

## Risks and unresolved contracts

The Holy Realm active marker has a setter but no exact clear found in the repository search, so derived load can remain occupied after the provider should have ended.

The Event021 scenario eligible-count variable is incremented before ticket adjustment, so zero-ticket candidates may still count as route-eligible under current ordering.

The targeting schema is fixed-point while the proven helper callers are whole-ticket inputs, leaving fractional input rounding unresolved for future callers.

Event021's scale 100 and cap 10 remain caller choices, and the reduced major factor 0.35 can quantize to the same base one after divide, round, and minimum clamp.

The specialized Random Terror behavior must exclude one provider package, not every Random Terror marker or every active state.

Natural Disaster occupancy must remain one slot across queue, warning, impact sequencing, chain mission, and aftermath rather than counting stages separately.

Murder Mystery requires both live runtime state and the original-host marker, so a global runtime target alone is insufficient.

The current MCP inspection cannot prove final weighted distributions until the missing effect and trigger exist.

The Event030 MCP route has an internal error that must be retried after restoration.

No new balance, probability, or risk number was chosen in this handoff.

## Completion boundary

This handoff is complete as a source-ready restore plan, not as gameplay implementation.

The only file changed for this bounded task is `docs/plans/021_random_civil_war_plans/subagent_handoffs/individual_crisis_dependency_restore_2026-09-02.md`.

Gameplay and constants changes remain intentionally deferred to the parent after the required probability baseline.

There is no balance success claim.
