# Event 021 active evolution effects

This file documents `021_random_civil_war_active_evolution_effects.txt`: the opening-stage provenance helpers and the Evolution I review of civil wars that were already running when Evolution I activated.

## Opening provenance

`event021_capture_pending_opening_evolution_stage` accepts ANY scope and reads the existing global active evolution flags.
Its output is `global.random_civil_war_pending_opening_evolution_stage`, with baseline zero and the highest active stage from the existing centralized stage constants.
It changes no country history, generation, actor, weight, timing, or Chaos.
The opening identity helper calls it before mutation.

`event021_commit_opening_evolution_provenance` accepts COUNTRY scope and copies that serial transaction field into `random_civil_war_opening_evolution_stage` after successful host or primary commitment.
It first clears any earlier crisis's `random_civil_war_evolution_i_management_ready` and `random_civil_war_active_evolution_i_pending` receipts, so a new crisis role always starts in its opening phase.
Missing scratch does not infer a stage from current world flags or the number of actors.
The host commit, ordinary primary initializer, and proved Event 006 primary war call it.

`event021_inherit_crisis_opening_evolution_provenance` accepts COUNTRY scope with a normal country pointer in `random_civil_war_crisis_host_scope`.
It clears the same two stale receipts, validates the real host and its stage receipt, reads the host value through a temporary variable, then assigns it in the actor's own scope.
Missing identity or provenance leaves the field unchanged.
Ordinary and complete Event 006 secondary actors use this path, so an additional front inherits the original crisis stage rather than pretending that a baseline war began after an evolution.

The pending field is overwritten on each serial opening and cleared by startup and rollback.
The public opening wrappers call `event021_parent_release_completed_front_plan` after their mutation executor returns, and that helper clears the pending field only when the template is proven complete.

## Evolution I review of running wars

### Queueing

`event021_parent_attach_active_evolution_i_reviews` runs from `event021_parent_apply_evolution_i` only on the first recorded activation of an enabled Evolution I.
It traverses the bounded `global.random_civil_war_active_theaters` registry and queues every country that passes `event021_active_review_baseline_host`: the canonical government of a live crisis whose `random_civil_war_opening_evolution_stage` is the baseline stage.
A crisis without that stage receipt fails closed and is never queued.
Each queued government receives `random_civil_war_active_evolution_i_pending`, the activation date in `random_civil_war_active_evolution_i_epoch`, its crisis ID in `random_civil_war_active_evolution_i_crisis_id`, and an empty `random_civil_war_active_evolution_i_reviewed_front_ids` array.
`event021_parent_grant_evolution_i_management` gives the government and every live registered side of the same crisis `random_civil_war_evolution_i_management_ready`.
No MTTH sample, cost, mission, or GUI is added; the Evolution I due date is unchanged.

`event021_parent_process_active_evolution_i_reviews` runs at the end of the existing global-host pulse.
It visits at most `constant:event021_active_review.pulse_theater_scan` rows of the theater registry from the rotating `global.random_civil_war_active_evolution_i_cursor`, counting every inspected row, and sends hidden callback `chaosx.nr21.20` to each queued government whose retry date is absent or due.
There is no world iteration.

### Review

`event021_parent_review_active_evolution_i_theater` runs in the queued government's scope with ROOT on the same country.
It closes the review when the government is no longer the canonical live host of the queued crisis or when `event021_active_review_host_closing` holds: Evolution I inactive or switched off, settlement recorded, reconstruction under way, or every internal front resolved.
It first asks `event021_parent_request_idle_front_plan_release` to let the owner of a finished opening template release it through the owner's own release checks, then defers the whole review while `event021_active_review_globally_blocked` holds: no spare global front, another opening, launch, scenario, or secondary transaction in flight, a published template, or settlement talks in progress.

`event021_parent_review_active_evolution_i_sources` snapshots every active registered front ID of the crisis that is not yet in the reviewed array and reviews each through `event021_parent_review_active_evolution_i_source`.
`event021_parent_resolve_active_review_source` resolves an ID to the registry actor of that exact row, accepting only the government itself or an opposition actor whose crisis host is this government, with matching front and crisis IDs.
Each source ends in one result from `event021_active_review_result`:

| Result | Cause | Effect |
| --- | --- | --- |
| `ineligible` | Row gone, crisis mismatch, or a source generation that is missing, fractional, negative, above `constant:random_civil_war_capacity.maximum_generation`, or different from its registry row | Source marked reviewed |
| `deferred` | Successor grace, the source or its immediate opponent near defeat, or no spare front | Review stays queued and retries after `constant:event021_active_review.retry_days` |
| `no_side` | Same-tag contest, Event 006 carrier, capitulated side, lost capital, too few states or divisions, or no candidate that survives the checks below | Source marked reviewed |
| `opened` | At least one new side registered | Source and every new side marked reviewed |

A source at the generation cap may still open a side; the new side inherits the source generation and the crisis ID, so no descendant crisis is created and `random_civil_war_generation_allowed` is not consulted.
When no source is deferred the review finishes and `event021_parent_finish_active_evolution_i_review` clears the queue receipts; management access stays.

### Candidates

`event021_parent_collect_active_front_candidates` fills the same aligned candidate scratch as the opening collector, with `event021_parent_dynamic_active_mode` set to one for the shared region grower.
Its pool is the source's own held states that pass `event021_parent_active_source_state_candidate`: populated, with infrastructure, not the source capital, not another front's capital, and not reserved, marked, or held by a scenario.
Routes come from the source's own route evidence flags.
The detachable state budget is `maximum_detach_share` of that pool, never cutting the source below `minimum_remnant_states`.
The source keeps `remnant_division_share` of its live divisions, at least `minimum_remnant_divisions`, and the rest is the child budget.
The ordinary row capacity is the smallest of spare global fronts, the territory rows the budget allows at `minimum_region_states` each, and the force rows the child budget allows at `minimum_child_divisions` each.
It is further limited to the free dynamic civil-war tags; when the pool is exhausted and no other side opens, the source is deferred rather than closed.
`event021_parent_grow_dynamic_ordinary_front_regions` then grows connected regions from the best-scoring anchors, spending the state budget across the ordinary slots still open.
When the source is the government itself and the crisis is neither an Event 006 nor a same-tag crisis, `event021_parent_collect_dynamic_event6_front_candidates` adds complete Event 006 packages through the existing finder with ROOT as the government.

`event021_parent_build_active_front_rows` keeps a candidate only when the source capital's connected region, measured by `event021_parent_measure_active_source_remnant`, loses exactly the candidate's own states and stays at or above `minimum_remnant_states`.
The flood fill uses the temporary state flag `event021_active_remnant_reach` and clears it before returning.
Kept ordinary rows split the child budget by region weight with whole divisions; a row below `minimum_child_divisions` is dropped rather than borrowing from a sibling.
`event021_parent_append_active_front_row` writes each kept row to the government's own `random_civil_war_active_front_*` arrays with a fresh front ID, the source front ID and generation, the exact state span, its stockpile share (its divisions over the source's, clamped between `minimum_child_stockpile_share` and `event021_parent_tuning.maximum_actor_size`), and navy and air shares only when its span holds a naval base or an airfield.
`event021_parent_validate_active_front_receipt` publishes `random_civil_war_active_front_transaction_ready` only for aligned rows, unique positive IDs, positive contiguous exhaustive spans, unique states, anchors inside their own spans, every state still held by the source, and enough spare fronts.
It never sets `random_civil_war_front_plan_ready` and never touches the global opening template.

### Commit

`event021_parent_commit_active_front_rows` holds `random_civil_war_active_front_commit_in_progress`, the existing `random_civil_war_dynamic_front_activation_active` recursion guard, and the global target `random_civil_war_active_front_commit_owner` for one synchronous pass.
`event021_parent_save_active_commit_bridge` and `event021_parent_restore_active_commit_bridge` preserve the existing host target and pending generation, severity, crisis, archetype, and opposition front globals, including their absence.
`event021_parent_commit_active_front_row` resolves the source again by ID and generation, then:

- for an ordinary row, marks the source-held span with `event021_parent_mark_active_front_row_states`, publishes the existing secondary pending inputs, and calls `event021_parent_start_secondary_civil_war` on the source;
- for an Event 006 row, publishes the existing planned-package inputs and calls `event021_parent_try_event6_secondary_front` on the government.

The existing loader, receipt validator, state-span copy, opening-receipt copy, and row binding each have an active branch while the commit lock is held: `event021_parent_load_active_secondary_front`, `event021_parent_validate_active_secondary_transfer_receipt`, `event021_parent_copy_active_front_state_span`, the active branch of `event021_parent_copy_opening_state_receipts`, and `event021_bind_active_front_row`.
The new side therefore carries the crisis host pointer, its immediate opponent, the inherited generation, its route goal and profile, its exact states, its measured forces, and `random_civil_war_source_front_id`, and it is registered once in the front registry and the host roster.
A row is consumed only when its new side registers; otherwise only that row is marked rejected and the adapter's own rollback returns its states and troops to the source.
`event021_parent_refresh_active_source_receipt` then keeps only still-held states in the source's retained membership and refreshes its measured forces and registry region count without touching historical provenance.
`event021_parent_clear_active_front_row_markers` clears every transfer marker in the row's span.

### Cleanup

`event021_parent_clear_active_front_rows` releases the receipt rows after every source review.
`event021_parent_clear_active_evolution_i_state` runs from `event021_parent_cleanup_crisis` and removes the queue receipts and management access.
`event021_parent_clear_evolution_i_management` runs at the start of settlement and removes management access from every registered side of the crisis.
`event021_prepare_successor_roster_adoption` carries a queued review, its reviewed front IDs, and management access to a proven ordinary successor; the successor's grace defers the review.
An annexed or vanished government takes its receipts with it, which closes its review.

## Example

Evolution I activates while Ruritania fights one claimant.
Ruritania is queued, it and its claimant gain the Evolution I management phase, and the next pulse reviews the crisis.
The claimant holds eight eligible states and twelve divisions, so it can give up four states and must keep eight divisions for itself.
One connected region with a regional route survives the remnant check, so the claimant's southern provinces open a new regional side with four divisions, its own capital, and the crisis's generation.
Ruritania's own review finds no route, so its result is no side, and the review closes.

## Validation limits

The review, candidate, remnant, and commit paths are source-reviewed only.
Native civil-war rounding, stockpile and manpower transfer on rollback, and live campaign behavior remain `needs_live_game` evidence for the user.
No MCP lifecycle or probability certificate is claimed.
A narrow `hoi4.event_inspect` lint of `chaosx.nr21.20` (depth 2, helpers not expanded) returned `EVENT_INSPECTED_PARTIAL` with zero lint issues and zero blocking diagnostics at source revision `862e183c2c76633803bdee1163396a2ff44a2ede00700dcbe238e41fa3e090ab`; the server deferred helper projection, so the scripted helpers behind the callback are not covered by that result.
